from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    appointments = []

    if request.method == "POST":

        patient_name = request.form.get("patient_name")
        doctor = request.form.get("doctor")
        date = request.form.get("date")
        time = request.form.get("time")

        appointments.append({
            "patient_name": patient_name,
            "doctor": doctor,
            "date": date,
            "time": time
        })

        return render_template(
            "index.html",
            appointments=appointments
        )

    return render_template(
        "index.html",
        appointments=appointments
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )