import tempfile
import unittest
from pathlib import Path

from patterns.behavioural.observer import NewsPublisher, Subscriber
from patterns.creational.singleton import AppConfig
from patterns.structural.decorator import Espresso, MilkDecorator, SugarDecorator
from quiz import quiz


def scripted(answers):
    iterator = iter(answers)

    def fake_input(prompt: str = "") -> str:
        try:
            return next(iterator)
        except StopIteration:
            raise EOFError from None

    return fake_input


class TestQuizData(unittest.TestCase):
    def test_fifteen_well_formed_questions(self) -> None:
        self.assertEqual(len(quiz.QUESTIONS), 15)
        for number, question in enumerate(quiz.QUESTIONS, start=1):
            self.assertEqual(question.number, number)
            self.assertEqual(len(question.options), 4)
            self.assertEqual(len(set(question.options)), 4, f"duplicate options in Q{number}")
            self.assertTrue(0 <= question.answer_index < 4)
            self.assertTrue(question.explanation)

    def test_all_question_types_are_covered(self) -> None:
        kinds = {question.kind for question in quiz.QUESTIONS}
        for expected in ("Scenario", "Code understanding", "Pattern selection", "When NOT to use"):
            self.assertIn(expected, kinds)

    def test_code_questions_match_real_program_behaviour(self) -> None:
        def answer(number: int) -> str:
            question = quiz.QUESTIONS[number - 1]
            return question.options[question.answer_index]

        AppConfig.reset_instance()
        self.assertEqual(answer(9), str(AppConfig() is AppConfig()))
        AppConfig.reset_instance()

        drink = SugarDecorator(MilkDecorator(Espresso()))
        self.assertEqual(answer(10), str(drink.cost()))

        publisher, a, b = NewsPublisher(), Subscriber("a"), Subscriber("b")
        publisher.attach(a)
        publisher.attach(b)
        publisher.detach(b)
        self.assertEqual(answer(11), str(publisher.publish("Hi")))

    def test_markdown_files_match_the_questions(self) -> None:
        folder = Path(quiz.__file__).resolve().parent
        self.assertEqual((folder / "quiz.md").read_text(encoding="utf-8"), quiz.build_quiz_markdown())
        self.assertEqual(
            (folder / "answer_key.md").read_text(encoding="utf-8"), quiz.build_answer_key_markdown()
        )

    def test_export_writes_both_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            quiz.export_markdown(Path(temp))
            self.assertTrue((Path(temp) / "quiz.md").exists())
            self.assertTrue((Path(temp) / "answer_key.md").exists())


class TestParseAnswer(unittest.TestCase):
    def test_valid_inputs(self) -> None:
        self.assertEqual(quiz.parse_answer("a", 4), 0)
        self.assertEqual(quiz.parse_answer(" D ", 4), 3)
        self.assertEqual(quiz.parse_answer("2", 4), 1)

    def test_invalid_inputs(self) -> None:
        for text in ("", "E", "5", "0", "AB", "hello", "-1", "!"):
            self.assertIsNone(quiz.parse_answer(text, 4), text)


class TestRunQuiz(unittest.TestCase):
    def run_with(self, answers):
        lines: list[str] = []
        result = quiz.run_quiz(scripted(answers), lines.append)
        return result, "\n".join(lines)

    def test_perfect_score(self) -> None:
        answers = [quiz.LETTERS[q.answer_index] for q in quiz.QUESTIONS]
        (score, answered), text = self.run_with(answers)
        self.assertEqual((score, answered), (15, 15))
        self.assertIn("Final score: 15/15", text)

    def test_all_wrong_answers(self) -> None:
        answers = [quiz.LETTERS[(q.answer_index + 1) % 4] for q in quiz.QUESTIONS]
        (score, answered), _ = self.run_with(answers)
        self.assertEqual((score, answered), (0, 15))

    def test_invalid_input_is_retried_not_counted(self) -> None:
        first_correct = quiz.LETTERS[quiz.QUESTIONS[0].answer_index]
        (score, answered), text = self.run_with(["zzz", "9", "", first_correct, "q"])
        self.assertEqual((score, answered), (1, 1))
        self.assertEqual(text.count("Invalid answer"), 3)

    def test_quit_early(self) -> None:
        (score, answered), text = self.run_with(["q"])
        self.assertEqual((score, answered), (0, 0))
        self.assertIn("Quiz stopped", text)

    def test_closed_input_does_not_crash(self) -> None:
        (score, answered), _ = self.run_with([])
        self.assertEqual((score, answered), (0, 0))


if __name__ == "__main__":
    unittest.main()
