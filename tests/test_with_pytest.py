def test_always_passes():
    from mainapp import some_func
    value = some_func()
    print('passed custom')
    assert value==0
