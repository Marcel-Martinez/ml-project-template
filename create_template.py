import os

folders = ["data",
           "data/processed",
             "data/raw",
             "docs",
             "notebooks",
             "src",
             "src/models",
             "src/serve",
             "src/utils"]

for folder in folders:
    os.mkdir(folder)

files = [".dockerignore",
         "README.md",
         "config.yml"
         "Dockerfile",
         "requirements.txt",
         "setup.py",
         "docs/index.md",
         "src/models/__init__.py",
         "src/serve/__init__.py",
         "src/utils/__init__.py",
         "src/train.py",
         "src/eval.py",
         "src/main.py"
         ]

for file in files:
    with open(file, "a") as f:
        f.close()