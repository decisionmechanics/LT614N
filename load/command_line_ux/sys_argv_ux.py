import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file path>")
else:
    file_path = sys.argv[1]

    with open(file_path) as f:
        lines = f.readlines()
        print(f"{file_path} contains {len(lines)} line(s).")