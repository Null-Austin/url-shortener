from flask import Flask, redirect, request, url_for
import ast

app = Flask(__name__)

def readat():
    with open('dict.data', 'r') as f:
        return ast.literal_eval(f.read())

@app.route('/')
def home():
    return "HEY YOU'RE NOT SUPPOSED TO BE HERE\n\n *He gives the user an angry stare*"

@app.route('/<path:subpath>')
def catch_all(subpath):
    # Capture the full path including subpath
    previous_path = request.path[1:]  # Remove leading slash
    try:
        # Redirect to the stored URL, if available
        target_url = readat()[previous_path]
        return redirect(target_url)
    except KeyError as e:
        print(f"KeyError: {e} - No matching URL for path '{previous_path}'")
        return "Oopsies, I made a poopsies", 404

if __name__ == '__main__':
    app.run(debug=True)
