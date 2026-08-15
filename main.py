from flask import Flask, request, render_template_string
app = Flask(__name__)

register = {
    "1": "david",
    "2": "isreal",
    "3": "daniel",
    "4": "timothy",
    "5": "favour",
    "6": "grace",
    "7": "clevon",
    "8": "mercy",
    "9": "daniela",
    "10": "dangote",
}

html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Student Register</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #4f46e5, #06b6d4);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #1f2937;
        }

        .card {
            background: #ffffff;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
            width: min(90%, 480px);
        }

        h1 {
            margin-top: 0;
            text-align: center;
            color: #4f46e5;
        }

        .hint {
            text-align: center;
            color: #64748b;
            margin-bottom: 16px;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        label {
            font-weight: bold;
        }

        input {
            padding: 12px;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 16px;
        }

        button {
            padding: 12px;
            border: none;
            border-radius: 8px;
            background: #4f46e5;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #4338ca;
        }

        .result {
            margin-top: 16px;
            padding: 12px;
            border-radius: 8px;
            background: #ecfdf5;
            color: #065f46;
        }

        .error {
            margin-top: 16px;
            padding: 12px;
            border-radius: 8px;
            background: #fef2f2;
            color: #b91c1c;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Student Register</h1>
        <p class="hint">Enter a registration number to get the student name.</p>

        <form method="post">
            <label for="reg_no">Registration Number</label>
            <input type="text" name="reg_no" id="reg_no" placeholder="Example: 1" required>
            <button type="submit">Get Student Name</button>
        </form>

        {% if result %}
            <div class="result">
                <strong>Student name:</strong> {{ result }}
            </div>
        {% endif %}

        {% if error %}
            <div class="error">
                <strong>{{ error }}</strong>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        reg_no = request.form.get("reg_no", "").strip()

        if not reg_no:
            error = "Please enter a registration number."
        elif reg_no in register:
            result = register[reg_no]
        else:
            error = "Student name does not exist!"

    return render_template_string(html, result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000)
    
