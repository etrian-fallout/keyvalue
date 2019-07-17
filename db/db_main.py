from flask import Flask, request
from data_store import DataStore
import json

ds = DataStore()
app = Flask(__name__)

@app.route('/fn/set_fn', methods=['POST'])
def set_fn():
    data = json.loads(request.data.decode('utf-8'))
    key, value = data['key'], data['value']

    ds.set(key, value)
    
    return 'OK'

@app.route('/fn/del_fn', methods=['POST'])
def del_fn():
    data = json.loads(request.data.decode('utf-8'))
    key= data['key']

    ds.delete(key)

    return 'OK'

@app.route('/fn/get_fn', methods=['POST'])
def get_fn():
    data = json.loads(request.data.decode('utf-8'))
    key= data['key']

    value = ds.get(key)

    return str(value)

@app.route('/fn/incr_fn', methods=['POST'])
def incr_fn():
    data = json.loads(request.data.decode('utf-8'))
    key= data['key']
    
    value = ds.incr(key)

    return str(value)

@app.route('/fn/ttl_fn', methods=['POST'])
def ttl_fn():
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    key, value, ttl = data['key'], data['value'], data['ttl']
    
    ds.set_ttl(key, value, ttl)
    
    return 'OK'

def main(host='0.0.0.0', port=5000):
    app.run(host=host, port=port)

if __name__=='__main__':
    main()
