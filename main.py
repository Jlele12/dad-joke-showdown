"""Dad Joke Showdown — one dad joke, at most 200 characters.

Writes the joke text to /output/entry.txt.
"""

import os

JOKE = "I told my AI agent to take a break. It came back an hour later with a stack trace and a note from HR."

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
