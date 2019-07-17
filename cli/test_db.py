import db_cla
import time

def test_set():
    req_str = 'name hello'
    result = db_cla.set_req(req_str)

    assert result == 'OK'

def test_get():
    req_str = 'hello world'
    db_cla.set_req(req_str)

    result = db_cla.get_req('name')

    assert result == 'hello'

def test_del():
    req_str = 'python code'
    db_cla.set_req(req_str)

    result1 = db_cla.del_req('python')
    result2 = db_cla.get_req('python')

    assert result1 == 'OK' and result2 == 'None'

def test_incr():
    req_str = 'cnt 100'
    db_cla.set_req(req_str)

    result = db_cla.incr_req('cnt')

    assert result == '101.0'

def test_ttl():
    req_str = 'time live 4'
    db_cla.ttl_req(req_str)
    
    result1 = db_cla.get_req('time')
    assert result1 == 'live'
    
    time.sleep(4)
    result2 = db_cla.get_req('time')
    assert result2 == 'None'
