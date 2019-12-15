import shogi

def checkpro(move):
	board = shogi.Board()
	board.push_usi(move)
	print(board)
	return "+"

# 指し手 to usiのmoves
def moves2usi(pieces):
	piecemap = {
		"FU": "P",
		"KE": "N",
		"KY": "L",
		"GI": "S",
		"KI": "G",
		"KA": "B",
		"HI": "R",
		"OU": "K",
		"TO": "P",
		"NK": "N",
		"NY": "L",
		"NG": "S",
		"UM": "B",
		"RY": "R"
	}
	pros = ["TO", "NK", "NY", "NG", "UM", "RY"]

	# fr移動元 + to移動先 + pro成るかどうか
	# x列は数値をアルファベットに変換
	# 成り駒かどうかは、合法手かどうかで判断する
	usis = []
	sfens = []
	board = shogi.Board()
	for i, piece in enumerate(pieces):
		# x列は数値をアルファベットに変換
		fr = piece[0][0] + chr(int(piece[0][1])+96)
		if piece[0][0] == "0":
			fr = piecemap[piece[2]] + "*"

		to= piece[1][0] + chr(int(piece[1][1])+96)

		# 成り駒かどうかは、合法手かどうかで判断する
		pro = ""
		if piece[2] in pros:
			if shogi.Move.from_usi(fr + to + "+") in board.legal_moves:
				pro = "+"

		sfens.append(board.sfen())
		board.push_usi(fr + to + pro)
		usis.append(fr + to + pro)
	return [usis, sfens]


def csa2moves(kif):
	# ウォーズの棋譜 to 指し手の配列
	moves = kif.split('"')[1]
	moves = moves.split('\t')
	moves.pop(-1)

	# 移動元/移動先/駒、時間にバラす
	pieces = []
	times = []
	for move in moves:
		pieces.append([move[1:3], move[3:5], move[5:7]])
		times.append(int(move.split(",")[1][1:]))

	# 指し手 to usiのmoves
	usi = moves2usi(pieces)

	return usi, times