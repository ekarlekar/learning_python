import project2

def test_rev_array():
	assert project2.create_rev_array('soupdouppladouup') == 'puuodalppuodpuos'
	assert project2.create_rev_array('racecar') == 'racecar'
	assert project2.create_rev_array('') == ('')

def test_smoosh_array():
	assert project2.create_smoosh_array('soupdouppladouup') == 'spouuupoddoaulppppluaoddopuuuops'
	assert project2.create_smoosh_array('racecar') == 'rraacceeccaarr'
	assert project2.create_smoosh_array('') == ''

def test_decoded_array():
	assert project2.create_decoded_array('spouuupoddoaulppppluaoddopuuuops') == 'soupdouppladouup'
	assert project2.create_decoded_array('rraacceeccaarr') == 'racecar'
	assert project2.create_decoded_array('') == ''

def test_all_together(): 
	s = "".join(['how', 'to', 'train', 'your', 'dragon'])
	assert project2.create_decoded_array(project2.create_smoosh_array(s)) == s

