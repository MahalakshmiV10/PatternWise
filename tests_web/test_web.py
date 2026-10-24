import unittest
from app import create_app
from patterns.catalog import PATTERNS
from quiz.quiz import QUESTIONS


class WebTests(unittest.TestCase):
    def setUp(self):
        self.c = create_app().test_client()

    def test_pages(self):
        for url in ("/", "/quiz", "/progress", "/static/style.css", "/static/app.js", "/static/quiz.js"):
            self.assertEqual(self.c.get(url).status_code, 200, url)

    def test_every_pattern_page(self):
        for p in PATTERNS:
            r = self.c.get(f"/pattern/{p.number}")
            self.assertEqual(r.status_code, 200)
            self.assertIn(p.name.encode(), r.data)

    def test_404(self):
        self.assertEqual(self.c.get("/pattern/99").status_code, 404)
        self.assertEqual(self.c.get("/nope").status_code, 404)

    def test_quiz_api_hides_answers(self):
        data = self.c.get("/api/quiz").get_json()
        self.assertEqual(len(data), len(QUESTIONS))
        self.assertNotIn("answer", data[0])

    def test_scoring(self):
        for q in QUESTIONS:
            self.assertEqual(len(q.options), 4)
            ok = self.c.post("/api/quiz/check", json={"number": q.number, "choice": q.answer_index}).get_json()
            self.assertTrue(ok["correct"])
            bad = self.c.post("/api/quiz/check", json={"number": q.number, "choice": (q.answer_index + 1) % 4}).get_json()
            self.assertFalse(bad["correct"])

    def test_invalid_quiz_input(self):
        self.assertEqual(self.c.post("/api/quiz/check", json={"number": 1, "choice": 9}).status_code, 400)
        self.assertEqual(self.c.post("/api/quiz/check", data="x").status_code, 400)


if __name__ == "__main__":
    unittest.main()
