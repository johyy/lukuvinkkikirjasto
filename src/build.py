from initialise_database import initialise_database

def build():
    initialise_database()

# This allows us to call the build function using command line
if __name__ == '__main__':
    build()
