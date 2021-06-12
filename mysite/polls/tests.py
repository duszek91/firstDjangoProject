from datetime import timedelta

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.utils import timezone
from .models import Question

class TestQuestionModel(TestCase):

    def test_was_published_recently_with_future_question(self):
        t = timezone.now() + timedelta(days=30)
        future_question = Question(pub_date=t)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        t = timezone.now() - timedelta(days=1, seconds=1)
        old_question = Question(pub_date=t)

        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        t = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=t)
        self.assertIs(recent_question.was_published_recently(), True)


class TestQuestionIndexViews(TestCase):
    def test_page_exists(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_questions_on_index(self):
        response = self.client.get(reverse('polls:index'))
        # self.client.force_login()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'brak pytań')