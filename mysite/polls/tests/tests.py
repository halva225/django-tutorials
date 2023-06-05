import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelPersistingTests(TestCase):

    def test_no_questions(self):
        """
        A questions dataset with zero records is returned.
        """

        # test init
        # NOTE: an empty db schema will be created

        # test execution
        q1 = Question.objects.filter(question_text__startswith="What")

        # test assert
        self.assertQuerysetEqual(q1, [])