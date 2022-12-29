import unittest
import forward_index
import inverted_index

class IndexesTests(unittest.TestCase):
  def setUp(self):
    self.forwardIndex = forward_index.format()[0]
    self.invertedIndex = inverted_index.format()[0]

  def test_forward_index(self):
    self.assertEqual(self.forwardIndex.get('mock_1.txt'), ['software', 'helping', 'work'])
    self.assertEqual(self.forwardIndex.get('mock_2.txt'), ['over'])
    self.assertEqual(self.forwardIndex.get('mock_3.txt'), ['software', 'over'])
    self.assertEqual(self.forwardIndex.get('mock_4.txt'), ['collaboration', 'over', 'negotiation'])
    self.assertEqual(self.forwardIndex.get('mock_5.txt'), ['over'])

  def test_inverted_index(self):
    self.assertEqual(self.invertedIndex.get('over'), ['mock_2.txt', 'mock_3.txt', 'mock_4.txt', 'mock_5.txt'])
    self.assertEqual(self.invertedIndex.get('software'), ['mock_1.txt', 'mock_3.txt'])
    self.assertEqual(self.invertedIndex.get('processes'), ['mock_2.txt'])
    self.assertEqual(self.invertedIndex.get('collaboration'), ['mock_4.txt'])
    self.assertEqual(self.invertedIndex.get('and'), ['mock_1.txt', 'mock_2.txt'])

if __name__ == "__main__":
  unittest.main()