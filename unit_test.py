import unittest
import Csa2moves


class TestCsa2moves(unittest.TestCase):

	# ウォーズの棋譜を変換するテスト
	# 前後の不要な文字が消える
	def test_csa2moves1(self):
		# arrange
		pattern = '        receiveMove("+7968GI,L600	-3142GI,L599	SENTE_WIN_TORYO");'
		expected_value = ['7i6h', '3a4b']
		# act
		result = Csa2moves.csa2moves(pattern)
		# assert
		self.assertEqual(''.join(result), ''.join(expected_value))

	# ウォーズの棋譜を変換するテスト
	# 成りの場合は+がつく
	def test_csa2moves2(self):
		# arrange
		pattern = '        receiveMove("+7776FU,L600	-3334FU,L599	+8822UM,L598	GOTE_WIN_TORYO");'
		expected_value = ['7g7f', '3c3d','8h2b+']
		# act
		result = Csa2moves.csa2moves(pattern)
		# assert
		self.assertEqual(''.join(result), ''.join(expected_value))

	# ウォーズの棋譜を変換するテスト
	# 成駒を移動しても+はつかない
	def test_csa2moves3(self):
		# arrange
		pattern = '        receiveMove("+7776FU,L600	-3334FU,L599	+8822UM,L598	-3435FU,L596	+2211UM,L590	GOTE_WIN_TORYO");'
		expected_value = ['7g7f', '3c3d','8h2b+', '3d3e', '2b1a']
		# act
		result = Csa2moves.csa2moves(pattern)
		# assert
		self.assertEqual(''.join(result), ''.join(expected_value))