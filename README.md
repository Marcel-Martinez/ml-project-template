# 🚀 ML Project Structure Generator

This is a light template generator for **Machine Learning** projects. 


## 📂 Folder Structure


```text
.
├── data/                   # store the data
│   ├── processed/          # store clean and processed data
│   └── raw/                # inmutable data
├── docs/                   # Documentation
│   └── index.md            # markdown for documentation indexing
├── notebooks/              # Jupyter Notebooks
├── src/                    # source code
│   ├── models/             # models achitecture
│   │   └── __init__.py
│   ├── serve/              # scripts to serve (ex. APIs)
│   │   └── __init__.py
│   ├── utils/              # utils
│   │   └── __init__.py
│   ├── eval.py             # scripts for evaluations
│   ├── main.py             # scripts for orchestation
│   └── train.py            # scripts for training
├── .dockerignore           
├── Dockerfile              
├── README.md               
├── config.yml              # global config
├── requirements.txt        # dependencies
└── setup.py                
```

## ⚙️ How to use it

1. Copy the script in the directory where you like to start your project.
2. Open the terminal.
3. Execute the following command:

```bash
python generate_structure.py
```
