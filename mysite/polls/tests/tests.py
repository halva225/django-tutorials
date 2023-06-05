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
        q1 = Question.objects.all()

        # test assert
        self.assertQuerysetEqual(q1, [])


    def test_no_data_with_filtering_returns_no_questions(self):
        """
        A questions dataset with zero records and filtering returnes no data.
        """

        # test init
        # NOTE: an empty db schema will be created

        # test execution
        q1 = Question.objects.filter(question_text__startswith="What")

        # test assert
        self.assertQuerysetEqual(q1, [])

    def test_returns_correct_number_of_questions(self):
        """
        A test which returns a correct number of questions.
        """

        # test init
        # NOTE: an empty db schema will be created
        before = Question(question_text = "test", pub_date = timezone.now())
        before.save()

        # test execution
        after = Question.objects.count()

        # test assert
        self.assertEqual(1, after)


    def test_returns_questions(self):
        """
        A questions dataset which returnes records.
        """

        # test init
        # NOTE: an empty db schema will be created
        before = Question(question_text = "test", pub_date = timezone.now())
        before.save()

        # test execution
        after = Question.objects.all()

        # test assert
        self.assertQuerysetEqual(after, [before])