def needleman_wunsch(seq1, seq2, match, mismatch, gap):

	matrix = []

	l1 = len(seq1)
	l2 = len(seq2)

	first_row = [-i for i in range(0, l1+1)]
	first_column = [-i for i in range(0, l2+1)]

	matrix.append(first_row)

	current_row = [first_column[1]]

	for i in range(0, len(seq2)):
		for j in range(0, len(seq1)):

			status = 0

			if seq1[j] == seq2[i]:
				status = match
			else:
				status = mismatch

			current_score = max(matrix[-1][len(current_row)-1] + status, matrix[-1][len(current_row)] + gap, current_row[-1] + gap)
			current_row.append(current_score)

		matrix.append(current_row)
		try:
			current_row = [first_column[i+2]]
		except:
			pass


	seq1a = []
	seq2a = []

	c1 = -1
	c2 = -1

	row = -1
	column = -1

	for i in range(0, len(matrix)):
		up = -10000000000000
		left = -10000000000000
		up_left = -10000000000000

		try:
			left = matrix[row][column-1]
		except:
			pass

		try:
			up_left = matrix[row-1][column-1]
		except:
			pass

		try:
			up = matrix[row-1][column]
		except:
			pass

		maximum = max(left, up_left, up)

		if maximum == up_left:

			seq1a.append(seq1[column])
			seq2a.append(seq2[row])

			try:
				row = row - 1
				column = column - 1
			except:
				pass

		elif maximum == left:

			seq1a.append(seq1[column])
			seq2a.append("-")

			try:
				column = column -1
			except:
				pass

		elif maximum == up:
			seq1a.append("-")
			seq2a.append(seq2[row])

			try:
				row = row -1
			except:
				pass

	seq1a.reverse()
	seq2a.reverse()

	seq1a = ''.join(seq1a)
	seq2a = ''.join(seq2a)
	aligned_sequences = (seq1a, seq2a)

	return(aligned_sequences)