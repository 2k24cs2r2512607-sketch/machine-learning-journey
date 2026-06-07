import argparse

# Step 1: Create a parser
parser = argparse.ArgumentParser(description="A greeting script")

# Step 2: Define what arguments you accept
parser.add_argument(["name", "fdf"], help="Your name")

# Step 3: Parse what the user typed
args = parser.parse_args()

# Step 4: Use the values
print(f"Hello, {args.name,args.fdf}!")
