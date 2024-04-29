# preprocess.py
import os
import config.settings as cfg

def should_exclude(file_path):
    exclude_patterns = ['node_modules', '.sln', '.csproj']
    return any(x in file_path for x in exclude_patterns)

def preprocess_files():
    for subdir, dirs, files in os.walk(cfg.CURRENT_REPO_PATH):
        for file in files:
            file_path = os.path.join(subdir, file)
            if not should_exclude(file_path):
                yield file_path

def main():
    for file_path in preprocess_files():
        print(f"Processing {file_path}")

if __name__ == "__main__":
    main()
