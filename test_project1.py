import project1

def test_find_word():
	assert project1.find_word('hi', ['hit', 'dog', 'him', 'hillbilly'] ) == ['hit', 'him', 'hillbilly']
	assert project1.find_word('josp', ['kfl', 'sejfod', 'isjfo']) == []
	assert project1.find_word('j', ['jack']) == ['jack']
	assert project1.find_word('', ['jack']) == ['jack']
	assert project1.find_word(' ', ['jack']) == []
	assert project1.find_word('joe', ['']) == []
	assert project1.find_word('joe', [' ']) == []