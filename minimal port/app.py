from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Save Contact Form Data
@app.route("/save_message", methods=["POST"])
def save_message():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Save message to a text file
        with open("messages.txt", "a") as file:
            file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

        # Show success message
        return render_template("contact.html", success=True)

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
