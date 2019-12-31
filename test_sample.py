import basics 

def test_basics(): 
	assert basics.to_test(2) == 4
	assert basics.to_test(12) == 36 
	assert basics.to_test(13) == 7

def test_method_two(): 
	assert basics.building_on_to_test(12) == 4 
	assert basics.building_on_to_test(2) == 3 
