import os
with open("dir_path.txt", "w") as f:
    for current_dir, dirs, files in os.walk("sample"):
        for item in files:
            if item.endswith(".py"):
                f.write(current_dir + "\n")
                break
