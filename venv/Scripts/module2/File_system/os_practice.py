import os
import os.path
import shutil

path = os.getcwd()
print(path)
print(os.listdir())
print(os.listdir("Tasks"))
print(os.path.abspath("files.py"))
print(os.path.exists("files.py"))
print(os.path.exists("input.txt"))
print(os.path.exists("Tasks"))

print(os.path.isfile("files.py"))
print(os.path.isfile("Task"))

print(os.path.isdir("files.py"))
print(os.path.isdir("Tasks"))
print()

shutil.copytree("Tasks", "Tasks\Tasks")
for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)