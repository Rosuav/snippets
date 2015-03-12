import snippets
import unittest

class TestSnippets(unittest.TestCase):
	def test_set_and_retrieve(self):
		name, value = "test_snippet", "This is the text"
		snippets.put(name, value)
		self.assertEqual(snippets.get(name), value)

	def test_retrieve_bogus(self):
		self.assertIs(snippets.get("bogus"), None)

if __name__=='__main__':
	unittest.main()
