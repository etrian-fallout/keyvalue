from db_cla import set_req, get_req, del_req, incr_req, ttl_req
from functools import reduce

while True:
    qs = input('== ')
    qqs = qs.split()

    fn_map = {
        'set': set_req, 
        'get': get_req, 
        'del': del_req,
        'incr': incr_req,
        'ttl': ttl_req
    }
    
    req_fn = fn_map[qqs[0]]

    print(req_fn(reduce(lambda x, y: f'{x} {y}', qqs[1:])))

