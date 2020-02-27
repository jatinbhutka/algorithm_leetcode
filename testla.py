def test_find_plan():
    # finish the function
    # assert something == something else
    
    plans = ['AGG01', '01 Agg', 'abc', 'Agxg', 'ag g', '', ' ', 'AggG', 'AAgG', 'agg ']
    
    assert find_plan('AGg', plans) == ['AGG01', '01 Agg', 'AggG', 'AAgG', 'agg '], "Test 1 fail"
    assert find_plan(' Agg', plans) == ['01 Agg'], "Test 2 fail"
    assert find_plan('AGg ', plans) == ['agg '], "Test 3 fail"
    assert  find_plan('A Gg', plans) ==  [], "Test 4 fail"
    assert  find_plan('', plans) == ['AGG01', '01 Agg', 'abc', 'Agxg', 'ag g', '', ' ', 'AggG', 'AAgG', 'agg '], "Test 5 fail"
    assert  find_plan(' ', plans) == ['01 Agg', 'ag g', ' ', 'agg '], "Test 6 fail"

    print("All test cases passed")
