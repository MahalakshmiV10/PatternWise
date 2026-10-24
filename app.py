"""PatternWise Flask app. Run: python app.py  ->  http://127.0.0.1:5000"""
import contextlib
import importlib
import inspect
import io
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, request
from patterns.catalog import PATTERNS, get_pattern
from quiz.quiz import QUESTIONS

BASE = Path(__file__).parent


def run_demo(info):
    """Really run the pattern's demo() and capture what it prints."""
    module = importlib.import_module(info.module)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        module.demo()
    return buffer.getvalue()


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html", patterns=PATTERNS, total_q=len(QUESTIONS))

    @app.route("/pattern/<int:number>")
    def pattern(number):
        info = get_pattern(number)
        if info is None:
            abort(404)
        module = importlib.import_module(info.module)
        code = inspect.getsource(module)
        mmd = (BASE / "diagrams" / (info.module.split(".")[-1] + ".mmd")).read_text(encoding="utf-8")
        return render_template("pattern.html", p=info, code=code, output=run_demo(info),
                               diagram=mmd, prev=get_pattern(number - 1), next=get_pattern(number + 1))

    @app.route("/quiz")
    def quiz():
        return render_template("quiz.html")

    @app.route("/progress")
    def progress():
        return render_template("progress.html", patterns=PATTERNS)

    @app.get("/api/quiz")
    def quiz_questions():
        # Answers are NOT sent here; they are checked by /api/quiz/check.
        return jsonify([{"number": q.number, "text": q.text, "options": list(q.options), "code": q.code}
                        for q in QUESTIONS])

    @app.post("/api/quiz/check")
    def quiz_check():
        data = request.get_json(silent=True) or {}
        number, choice = data.get("number"), data.get("choice")
        question = next((q for q in QUESTIONS if q.number == number), None)
        if question is None or not isinstance(choice, int) or not 0 <= choice < len(question.options):
            return jsonify(error="Invalid question or choice"), 400
        return jsonify(correct=choice == question.answer_index, answer=question.answer_index,
                       explanation=question.explanation)

    @app.errorhandler(404)
    def not_found(_):
        return render_template("404.html"), 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=False)
