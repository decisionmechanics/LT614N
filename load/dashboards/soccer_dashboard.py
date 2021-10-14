import numpy as np
import pandas as pd
import streamlit as st


def read_data():
    df = pd.read_csv("epl_2020_2021.csv", parse_dates=[["Date", "Time"]])

    df.rename({"Date_Time": "Kickoff"}, axis=1, inplace=True)

    df["Kickoff"] = df["Kickoff"].dt.tz_localize("Europe/London")

    return df


def calculate_points(df):
    df["HomeTeamPoints"] = np.where(df["FTHG"] > df["FTAG"], 3, 0)
    df["AwayTeamPoints"] = np.where(df["FTHG"] < df["FTAG"], 3, 0)

    home_points_df = df[["Kickoff", "HomeTeam", "HomeTeamPoints"]].rename(
        {"HomeTeam": "Team", "HomeTeamPoints": "Points"}, axis=1
    )
    away_points_df = df[["Kickoff", "AwayTeam", "AwayTeamPoints"]].rename(
        {"AwayTeam": "Team", "AwayTeamPoints": "Points"}, axis=1
    )
    points_df = pd.concat([home_points_df, away_points_df])

    points_df = points_df.set_index("Kickoff").sort_index()

    return points_df


@st.cache()
def read_points():
    df = read_data()

    return calculate_points(df)


def calculate_cumulative_points(points_df, team):
    cumulative_points_df = points_df[points_df["Team"] == team].copy()

    return cumulative_points_df.loc[
        cumulative_points_df["Team"] == team, ["Points"]
    ].cumsum()


points_df = read_points()
teams = sorted(points_df["Team"].unique())

st.title("Team progression dashboard")

selected_team = st.selectbox("Choose your team:", teams)

cumulative_points_df = calculate_cumulative_points(points_df, selected_team)
final_points = cumulative_points_df.iloc[-1, 0]

st.markdown(f"{selected_team} finished the season on **{final_points}** point(s)")

st.subheader(f"{selected_team}'s progression throughout the season")

st.line_chart(cumulative_points_df)
