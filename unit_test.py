import unittest
import Csa2moves


class TestCsa2moves(unittest.TestCase):

	def test_moves2piecestimes(self):
		# arrange
		pattern = ['"t":600,"n":0,"m":"+7968GI"}']
		expected_value = ['7i6h', '3a4b']
		# act
		result = Csa2moves.moves2piecestimes(pattern)
		# assert
		self.assertEqual(''.join(result[0][0]), ''.join(expected_value))


	# ウォーズの棋譜を移動元/移動先/駒、時間にバラす
	def test_kif2moves1(self):
		# arrange
		pattern = '<div data-react-class="games/Show" data-react-props="{&quot;gameHash&quot;:{&quot;name&quot;:&quot;safeoff-ghouls2000-20200116_161028&quot;,&quot;gtype&quot;:&quot;&quot;,&quot;opponent_type&quot;:0,&quot;sente&quot;:&quot;safeoff&quot;,&quot;gote&quot;:&quot;ghouls2000&quot;,&quot;sente_dan&quot;:-1,&quot;gote_dan&quot;:-1,&quot;sente_avatar&quot;:&quot;_&quot;,&quot;gote_avatar&quot;:&quot;_&quot;,&quot;result&quot;:&quot;SENTE_WIN_TORYO&quot;,&quot;handicap&quot;:0,&quot;init_sfen_position&quot;:&quot;lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1&quot;,&quot;moves&quot;:[{&quot;t&quot;:600,&quot;n&quot;:0,&quot;m&quot;:&quot;+7968GI&quot;},{&quot;t&quot;:599,&quot;n&quot;:1,&quot;m&quot;:&quot;-8252HI&quot;},{&quot;t&quot;:599,&quot;n&quot;:2,&quot;m&quot;:&quot;+5756FU&quot;},{&quot;t&quot;:598,&quot;n&quot;:3,&quot;m&quot;:&quot;-5354FU&quot;},{&quot;t&quot;:598,&quot;n&quot;:4,&quot;m&quot;:&quot;+6857GI&quot;},{&quot;t&quot;:597,&quot;n&quot;:5,&quot;m&quot;:&quot;-7162GI&quot;},{&quot;t&quot;:596,&quot;n&quot;:6,&quot;m&quot;:&quot;+8879KA&quot;},{&quot;t&quot;:596,&quot;n&quot;:7,&quot;m&quot;:&quot;-6253GI&quot;},{&quot;t&quot;:595,&quot;n&quot;:8,&quot;m&quot;:&quot;+5968OU&quot;},{&quot;t&quot;:594,&quot;n&quot;:9,&quot;m&quot;:&quot;-5364GI&quot;},{&quot;t&quot;:594,&quot;n&quot;:10,&quot;m&quot;:&quot;+6878OU&quot;},{&quot;t&quot;:593,&quot;n&quot;:11,&quot;m&quot;:&quot;-1314FU&quot;},{&quot;t&quot;:592,&quot;n&quot;:12,&quot;m&quot;:&quot;+3948GI&quot;},{&quot;t&quot;:591,&quot;n&quot;:13,&quot;m&quot;:&quot;-5455FU&quot;},{&quot;t&quot;:592,&quot;n&quot;:14,&quot;m&quot;:&quot;+5655FU&quot;},{&quot;t&quot;:590,&quot;n&quot;:15,&quot;m&quot;:&quot;-6455GI&quot;},{&quot;t&quot;:588,&quot;n&quot;:16,&quot;m&quot;:&quot;+3736FU&quot;},{&quot;t&quot;:588,&quot;n&quot;:17,&quot;m&quot;:&quot;-6172KI&quot;},{&quot;t&quot;:587,&quot;n&quot;:18,&quot;m&quot;:&quot;+4837GI&quot;},{&quot;t&quot;:586,&quot;n&quot;:19,&quot;m&quot;:&quot;-2213KA&quot;},{&quot;t&quot;:581,&quot;n&quot;:20,&quot;m&quot;:&quot;+4958KI&quot;},{&quot;t&quot;:584,&quot;n&quot;:21,&quot;m&quot;:&quot;-0056FU&quot;},{&quot;t&quot;:576,&quot;n&quot;:22,&quot;m&quot;:&quot;+5746GI&quot;},{&quot;t&quot;:583,&quot;n&quot;:23,&quot;m&quot;:&quot;-5546GI&quot;},{&quot;t&quot;:572,&quot;n&quot;:24,&quot;m&quot;:&quot;+3746GI&quot;},{&quot;t&quot;:581,&quot;n&quot;:25,&quot;m&quot;:&quot;-1346KA&quot;},{&quot;t&quot;:571,&quot;n&quot;:26,&quot;m&quot;:&quot;+4746FU&quot;},{&quot;t&quot;:535,&quot;n&quot;:27,&quot;m&quot;:&quot;-4132KI&quot;},{&quot;t&quot;:563,&quot;n&quot;:28,&quot;m&quot;:&quot;+4645FU&quot;},{&quot;t&quot;:522,&quot;n&quot;:29,&quot;m&quot;:&quot;-3142GI&quot;},{&quot;t&quot;:537,&quot;n&quot;:30,&quot;m&quot;:&quot;+2726FU&quot;},{&quot;t&quot;:500,&quot;n&quot;:31,&quot;m&quot;:&quot;-0034GI&quot;},{&quot;t&quot;:504,&quot;n&quot;:32,&quot;m&quot;:&quot;+2625FU&quot;},{&quot;t&quot;:495,&quot;n&quot;:33,&quot;m&quot;:&quot;-3445GI&quot;},{&quot;t&quot;:503,&quot;n&quot;:34,&quot;m&quot;:&quot;+2524FU&quot;},{&quot;t&quot;:494,&quot;n&quot;:35,&quot;m&quot;:&quot;-2324FU&quot;},{&quot;t&quot;:499,&quot;n&quot;:36,&quot;m&quot;:&quot;+0025FU&quot;},{&quot;t&quot;:488,&quot;n&quot;:37,&quot;m&quot;:&quot;-4534GI&quot;},{&quot;t&quot;:498,&quot;n&quot;:38,&quot;m&quot;:&quot;+2524FU&quot;},{&quot;t&quot;:485,&quot;n&quot;:39,&quot;m&quot;:&quot;-0022FU&quot;},{&quot;t&quot;:489,&quot;n&quot;:40,&quot;m&quot;:&quot;+3635FU&quot;},{&quot;t&quot;:483,&quot;n&quot;:41,&quot;m&quot;:&quot;-3445GI&quot;},{&quot;t&quot;:485,&quot;n&quot;:42,&quot;m&quot;:&quot;+0023GI&quot;},{&quot;t&quot;:471,&quot;n&quot;:43,&quot;m&quot;:&quot;-2223FU&quot;},{&quot;t&quot;:484,&quot;n&quot;:44,&quot;m&quot;:&quot;+2423TO&quot;},{&quot;t&quot;:469,&quot;n&quot;:45,&quot;m&quot;:&quot;-0027FU&quot;},{&quot;t&quot;:481,&quot;n&quot;:46,&quot;m&quot;:&quot;+2827HI&quot;},{&quot;t&quot;:467,&quot;n&quot;:47,&quot;m&quot;:&quot;-4536GI&quot;},{&quot;t&quot;:467,&quot;n&quot;:48,&quot;m&quot;:&quot;+2724HI&quot;},{&quot;t&quot;:457,&quot;n&quot;:49,&quot;m&quot;:&quot;-0015GI&quot;},{&quot;t&quot;:453,&quot;n&quot;:50,&quot;m&quot;:&quot;+2428HI&quot;},{&quot;t&quot;:454,&quot;n&quot;:51,&quot;m&quot;:&quot;-0027GI&quot;},{&quot;t&quot;:449,&quot;n&quot;:52,&quot;m&quot;:&quot;+2848HI&quot;},{&quot;t&quot;:451,&quot;n&quot;:53,&quot;m&quot;:&quot;-3223KI&quot;},{&quot;t&quot;:427,&quot;n&quot;:54,&quot;m&quot;:&quot;+0028FU&quot;},{&quot;t&quot;:434,&quot;n&quot;:55,&quot;m&quot;:&quot;-1526GI&quot;},{&quot;t&quot;:422,&quot;n&quot;:56,&quot;m&quot;:&quot;+2827FU&quot;},{&quot;t&quot;:431,&quot;n&quot;:57,&quot;m&quot;:&quot;-2637NG&quot;},{&quot;t&quot;:420,&quot;n&quot;:58,&quot;m&quot;:&quot;+2937KE&quot;},{&quot;t&quot;:430,&quot;n&quot;:59,&quot;m&quot;:&quot;-3637NG&quot;},{&quot;t&quot;:403,&quot;n&quot;:60,&quot;m&quot;:&quot;+4846HI&quot;},{&quot;t&quot;:426,&quot;n&quot;:61,&quot;m&quot;:&quot;-0065KE&quot;},{&quot;t&quot;:379,&quot;n&quot;:62,&quot;m&quot;:&quot;+0053FU&quot;},{&quot;t&quot;:424,&quot;n&quot;:63,&quot;m&quot;:&quot;-5253HI&quot;},{&quot;t&quot;:377,&quot;n&quot;:64,&quot;m&quot;:&quot;+0054FU&quot;},{&quot;t&quot;:423,&quot;n&quot;:65,&quot;m&quot;:&quot;-5354HI&quot;},{&quot;t&quot;:375,&quot;n&quot;:66,&quot;m&quot;:&quot;+0045KA&quot;},{&quot;t&quot;:419,&quot;n&quot;:67,&quot;m&quot;:&quot;-5455HI&quot;},{&quot;t&quot;:368,&quot;n&quot;:68,&quot;m&quot;:&quot;+4523UM&quot;},{&quot;t&quot;:411,&quot;n&quot;:69,&quot;m&quot;:&quot;-5657TO&quot;},{&quot;t&quot;:332,&quot;n&quot;:70,&quot;m&quot;:&quot;+5859KI&quot;},{&quot;t&quot;:404,&quot;n&quot;:71,&quot;m&quot;:&quot;-5747TO&quot;},{&quot;t&quot;:307,&quot;n&quot;:72,&quot;m&quot;:&quot;+0041KI&quot;},{&quot;t&quot;:401,&quot;n&quot;:73,&quot;m&quot;:&quot;-5162OU&quot;},{&quot;t&quot;:297,&quot;n&quot;:74,&quot;m&quot;:&quot;+4656HI&quot;},{&quot;t&quot;:396,&quot;n&quot;:75,&quot;m&quot;:&quot;-5556HI&quot;},{&quot;t&quot;:296,&quot;n&quot;:76,&quot;m&quot;:&quot;+2356UM&quot;},{&quot;t&quot;:393,&quot;n&quot;:77,&quot;m&quot;:&quot;-6557NK&quot;},{&quot;t&quot;:269,&quot;n&quot;:78,&quot;m&quot;:&quot;+7957KA&quot;},{&quot;t&quot;:390,&quot;n&quot;:79,&quot;m&quot;:&quot;-0028HI&quot;},{&quot;t&quot;:261,&quot;n&quot;:80,&quot;m&quot;:&quot;+5768KA&quot;},{&quot;t&quot;:373,&quot;n&quot;:81,&quot;m&quot;:&quot;-0057FU&quot;},{&quot;t&quot;:205,&quot;n&quot;:82,&quot;m&quot;:&quot;+4142KI&quot;},{&quot;t&quot;:361,&quot;n&quot;:83,&quot;m&quot;:&quot;-5758TO&quot;},{&quot;t&quot;:203,&quot;n&quot;:84,&quot;m&quot;:&quot;+0051HI&quot;},{&quot;t&quot;:341,&quot;n&quot;:85,&quot;m&quot;:&quot;-5868TO&quot;},{&quot;t&quot;:201,&quot;n&quot;:86,&quot;m&quot;:&quot;+5968KI&quot;},{&quot;t&quot;:322,&quot;n&quot;:87,&quot;m&quot;:&quot;-2868RY&quot;},{&quot;t&quot;:200,&quot;n&quot;:88,&quot;m&quot;:&quot;+6968KI&quot;},{&quot;t&quot;:317,&quot;n&quot;:89,&quot;m&quot;:&quot;-0061KI&quot;},{&quot;t&quot;:186,&quot;n&quot;:90,&quot;m&quot;:&quot;+5161RY&quot;}]},&quot;userConfig&quot;:{&quot;imgPieceType&quot;:&quot;ja_single&quot;,&quot;soundEnable&quot;:1,&quot;voiceEnable&quot;:1,&quot;voiceType&quot;:0},&quot;isNeedRealtime&quot;:false,&quot;settings&quot;:{&quot;cdn.web&quot;:&quot;//shogiwars-cdn.heroz.jp&quot;,&quot;cdn.image&quot;:&quot;//image-pona.heroz.jp&quot;,&quot;cdn.sound&quot;:&quot;//sound-pona.heroz.jp&quot;,&quot;goldengate.host&quot;:&quot;wss://shogiwars-webapp.heroz.jp&quot;,&quot;javascript.log_level&quot;:&quot;error&quot;},&quot;version&quot;:&quot;&quot;}"></div>'
		expected_value = ['7i6h', '3a4b']
		# act
		result = Csa2moves.kif2moves(pattern)
		# assert
		self.assertEqual(''.join(result[0][0]), ''.join(expected_value))

	# ウォーズの棋譜を変換するテスト
	# 前後の不要な文字が消える
	def test_csa2moves1(self):
		# arrange
		pattern = '        receiveMove("+7968GI,L600	-3142GI,L599	SENTE_WIN_TORYO");'
		expected_value = ['7i6h', '3a4b']
		# act
		result = Csa2moves.csa2moves(pattern)
		# assert
		self.assertEqual(''.join(result[0][0]), ''.join(expected_value))

	# ウォーズの棋譜を変換するテスト
	# 成りの場合は+がつく
	def test_csa2moves2(self):
		# arrange
		pattern = '        receiveMove("+7776FU,L600	-3334FU,L599	+8822UM,L598	GOTE_WIN_TORYO");'
		expected_value = ['7g7f', '3c3d','8h2b+']
		# act
		result = Csa2moves.csa2moves(pattern)
		# assert
		self.assertEqual(''.join(result[0][0]), ''.join(expected_value))

	# ウォーズの棋譜を変換するテスト
	# 成駒を移動しても+はつかない
	def test_csa2moves3(self):
		# arrange
		pattern = '        receiveMove("+7776FU,L600	-3334FU,L599	+8822UM,L598	-3435FU,L596	+2211UM,L590	GOTE_WIN_TORYO");'
		expected_value = ['7g7f', '3c3d','8h2b+', '3d3e', '2b1a']
		# act
		result = Csa2moves.csa2moves(pattern)
		# assert
		self.assertEqual(''.join(result[0][0]), ''.join(expected_value))