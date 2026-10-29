#!/usr/bin/env python3
"""Runtime integrity and ZIP packaging smoke tests for the nine standalone Skills."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAMES = (
    "ecom-content", "ecom-content-strategy", "ecom-content-ideas",
    "ecom-reel", "ecom-carousel", "ecom-story", "ecom-caption",
    "ecom-brand-voice", "ecom-content-review",
)


def validate(checkout):
    return subprocess.run(
        ["python3", str(checkout / "scripts" / "validate_skills.py")],
        cwd=checkout, capture_output=True, text=True, check=False,
    )


class SkillIntegrityTests(unittest.TestCase):
    def test_all_nine_zip_archives_have_expected_root(self):
        for name in NAMES:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as tmp:
                zip_path = Path(tmp) / f"{name}.zip"
                with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
                    for path in (ROOT / name).rglob("*"):
                        if path.is_file():
                            archive.write(path, path.relative_to(ROOT))
                with zipfile.ZipFile(zip_path) as archive:
                    members = archive.namelist()
                    self.assertIn(f"{name}/SKILL.md", members)
                    self.assertTrue(all(member.startswith(f"{name}/") for member in members))
                    self.assertFalse(any(member.startswith(f"{name}/{name}/") for member in members))
                    extraction = Path(tmp) / "extracted"
                    archive.extractall(extraction)
                self.assertTrue((extraction / name / "SKILL.md").is_file())

    def temp_checkout(self, directory):
        target = Path(directory)
        (target / "scripts").mkdir()
        shutil.copy(ROOT / "scripts" / "validate_skills.py",
                    target / "scripts" / "validate_skills.py")
        for name in NAMES:
            shutil.copytree(ROOT / name, target / name)
        return target

    def test_validator_accepts_complete_checkout(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = validate(self.temp_checkout(tmp))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("VALIDATION OK", result.stdout)

    def test_validator_rejects_missing_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.temp_checkout(tmp)
            (root / "ecom-brand-voice" / "references" / "calibration.md").unlink()
            result = validate(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing reference", result.stdout.lower())

    def test_validator_rejects_incorrect_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.temp_checkout(tmp)
            path = root / "ecom-content-review" / "SKILL.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "name: ecom-content-review", "name: ecom-caption", 1
                ), encoding="utf-8"
            )
            result = validate(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("name does not match", result.stdout)

    def test_validator_rejects_missing_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.temp_checkout(tmp)
            shutil.rmtree(root / "ecom-reel")
            result = validate(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Expected", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
