import json

def count_words_in_notebook(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        word_count = 0
        for cell in data['cells']:
            if cell['cell_type'] == 'markdown':
                content = cell['source']
                for line in content:
                    # Split by whitespace and filter out markdown syntax elements
                    words = line.split()
                    clean_words = [word for word in words if not word.startswith('#')]
                    word_count += len(clean_words)
        
        print(f"Total word count (excluding markdown syntax): {word_count}")
    except FileNotFoundError:
        print("The file path specified does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace '/PATH_TO_YOUR_NOTEBOOK.ipynb' with the path to your Jupyter Notebook
notebook_path = '/PATH_TO_YOUR_NOTEBOOK.ipynb'
count_words_in_notebook(notebook_path)
