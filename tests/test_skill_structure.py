"""Structural checks only; teaching quality needs the scenarios in scenarios.md."""

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "teach-from-scratch"
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
FENCE = re.compile(r"^```.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)


def read_text(path):
    return path.read_text(encoding="utf-8")


def markdown_links(path):
    text = FENCE.sub("", read_text(path))
    for match in LINK.finditer(text):
        yield match.group(1).strip()


class SkillStructureTests(unittest.TestCase):
    def test_frontmatter_uses_portable_nonempty_fields(self):
        text = read_text(SKILL / "SKILL.md")
        match = re.fullmatch(r"---\n(.*?)\n---\n(.*)", text, re.DOTALL)
        self.assertIsNotNone(match, "Expected UTF-8 without BOM and YAML frontmatter")
        fields = {}
        for line in match.group(1).splitlines():
            key, separator, value = line.partition(":")
            self.assertTrue(separator, "This skill uses single-line YAML scalars")
            self.assertNotIn(key, fields, "Duplicate frontmatter key")
            self.assertTrue(value.strip(), "Empty frontmatter value")
            fields[key] = value.strip()
        self.assertEqual(set(fields), {"name", "description"})
        self.assertEqual(fields["name"], SKILL.name)
        self.assertRegex(fields["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(fields["name"]), 64)
        self.assertLessEqual(len(fields["description"]), 1024)
        self.assertNotRegex(fields["description"], r"[<>]")

    def test_core_stays_small_enough_to_load(self):
        text = read_text(SKILL / "SKILL.md")
        self.assertLess(len(text.splitlines()), 200)
        self.assertLess(len(text), 6000)

    def test_every_reference_is_discoverable_from_core(self):
        referenced = {
            (SKILL / unquote(urlsplit(link).path)).resolve()
            for link in markdown_links(SKILL / "SKILL.md")
            if not urlsplit(link).scheme
        }
        files = set((SKILL / "references").glob("*.md"))
        self.assertTrue(files, "Expected optional reference material")
        self.assertTrue({path.resolve() for path in files} <= referenced)

    def test_all_local_markdown_links_resolve_inside_repository(self):
        paths = [ROOT / "README.md", *SKILL.rglob("*.md"), *Path(__file__).parent.glob("*.md")]
        for path in paths:
            for link in markdown_links(path):
                with self.subTest(file=str(path.relative_to(ROOT)), link=link):
                    parsed = urlsplit(link)
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    target = (path.parent / unquote(parsed.path)).resolve()
                    self.assertTrue(target.is_relative_to(ROOT.resolve()))
                    self.assertTrue(target.exists(), f"Missing local link: {link}")

    def test_runtime_skill_has_no_external_skill_links(self):
        for path in SKILL.rglob("*.md"):
            for link in markdown_links(path):
                with self.subTest(file=str(path.relative_to(SKILL)), link=link):
                    self.assertFalse(urlsplit(link).scheme)
                    self.assertFalse(urlsplit(link).netloc)

    def test_runtime_package_contains_only_instructions(self):
        allowed = {SKILL / "SKILL.md", *(SKILL / "references").glob("*.md")}
        files = {path for path in SKILL.rglob("*") if path.is_file()}
        self.assertEqual(files, allowed, "Keep maintainer docs and tests outside the skill")

    def test_markdown_is_utf8_without_bom_and_has_balanced_fences(self):
        paths = [ROOT / "README.md", *SKILL.rglob("*.md"), *Path(__file__).parent.glob("*.md")]
        for path in paths:
            with self.subTest(file=str(path.relative_to(ROOT))):
                data = path.read_bytes()
                self.assertFalse(data.startswith(b"\xef\xbb\xbf"))
                text = data.decode("utf-8")
                self.assertEqual(len(re.findall(r"^```", text, re.MULTILINE)) % 2, 0)
                self.assertTrue(text.endswith("\n"))

    def test_existing_gear_names_remain_documented(self):
        text = read_text(SKILL / "references" / "GEARS.md")
        for gear in ("simplified-paper", "full-paper", "skeleton", "full"):
            with self.subTest(gear=gear):
                self.assertIn(f"`{gear}`", text)


if __name__ == "__main__":
    unittest.main()
