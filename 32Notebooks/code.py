import json

def do(j):
	cells = j['cells']
	for cell in cells:
		if cell['cell_type'] == 'markdown':
			cell['metadata'] = {
								"trusted": True,
								"editable": False,
								"deletable": False
								}
		elif cell['cell_type'] == 'code':
			l = len(cell['source'])
			if l>0:
				source = cell['source']
				line1 = source[0]
				if '# Put your answer' in line1:
					cell['metadata'] = {
										 'trusted':True,
										 'editable':True,
										 'deletable':False
										 }
				else:
					cell['metadata'] = {
										 'trusted':True,
										 'editable':False,
										 'deletable':False
										 }

	j['cells'] = cells
	return j




filepaths = ['W1/week1_introduction.ipynb',
			'W2/week2_simulation.ipynb',
			'W3/week3_binomial.ipynb',
			'W4/week4_summary_statistics.ipynb']
			

				
filepaths = ['W5/week5_variance_of_averages.ipynb']
for filepath in filepaths:
	s = filepath.split('/')
	dty,nm = s[0],s[1]
	new_file = dty+'/locked_'+nm
	j = json.load(open(filepath,'r'))
	j = do(j)
	json.dump(j,open(new_file, 'w'),indent= 2)
