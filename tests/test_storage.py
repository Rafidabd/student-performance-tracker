"""Storage regression tests; no real student records are modified."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from modules import storage


class StudentStorageTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        override = patch.object(storage, "DATA_FILE", Path(temp.name) / "data" / "students.json")
        override.start()
        self.addCleanup(override.stop)

    def test_empty_store_created_on_first_load(self):
        self.assertEqual(storage.load_data(), {})
        self.assertTrue(storage.DATA_FILE.exists())

    def test_round_trip_student_record(self):
        sample = {"S001": {"name": "Example Student", "section": "11A", "marks": {"math": 90}}}
        storage.save_data(sample)
        self.assertEqual(storage.load_data(), sample)


if __name__ == "__main__":
    unittest.main()
