from flask import Flask, render_template, request, redirect, url_for
from encrypt import encrypt_text, decrypt_text, encrypted_texts

# Setup Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cypher_text = ""
    plain_text = ""
    
    # Handle encryption form submission
    if request.method == "POST":
        if "plain_text" in request.form:  # Check if it's an encryption request
            plain_text = request.form["plain_text"]
            cypher_text = encrypt_text(plain_text)
            encrypted_texts.append({"plain_text": plain_text, "encrypted_text": cypher_text})

        elif "cypher_text" in request.form:  # Handle decryption request
            cypher_text = request.form["cypher_text"]
            plain_text = decrypt_text(cypher_text)
    
    return render_template("index.html", cypher_text=cypher_text, plain_text=plain_text, encrypted_texts=encrypted_texts)

@app.route("/list")
def list_encrypted():
    return render_template("list.html", encrypted_texts=encrypted_texts)

if __name__ == "__main__":
    app.run(debug=True)
