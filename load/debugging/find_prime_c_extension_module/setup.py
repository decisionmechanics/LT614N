from distutils.core import setup, Extension

def main():
    setup(name="findprime",
          version="1.0.0",
          description="Python interface for the find_nth_prime C library function",
          author="Andrew Tait",
          author_email="Andrew.Tait@decisionmechanics.com",
          ext_modules=[Extension("findprime", ["library.c"])])

if __name__ == "__main__":
    main()