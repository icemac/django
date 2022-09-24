from django.conf import ASSERT_FORM_SET_ERROR_RENAMED_MSG
from django.test import SimpleTestCase
from django.utils.deprecation import RemovedInDjango50Warning
from tests.test_utils.tests import TestFormset


class SimpleTestCaseDeprecationTests(SimpleTestCase):
    def test_rename_assert_form_set_error(self):
        msg = ASSERT_FORM_SET_ERROR_RENAMED_MSG
        with self.assertRaisesMessage(RemovedInDjango50Warning, msg):
            self.assertFormsetError(TestFormset.invalid(), 0, "field", "invalid value")
