import time

class DataStore:
    def __init__(self):
        # key: (value, expire_time)
        self.data_map = dict()

    def incr(self, key):
        value, expire_time = self.data_map[key]

        try:
            float_value = float(value)
            float_value += 1
            self.data_map[key] = (float_value, expire_time)

            return float_value
        except Error:
            return None
    
    def is_key(self, key):
        if key in self.data_map.keys():
            return True
        else:
            return False

    def set(self, key, value):
        self.data_map[key] = (value, -1)
    
    def set_ttl(self, key, value, ttl_time):
        if  not ttl_time:
            ttl_time = 0
        
        self.data_map[key] = (value, time.time() + ttl_time)

    def get(self, key):
        if self.is_key(key):
            value, expire_time = self.data_map[key]

            if expire_time != -1 and time.time() > expire_time:
                self.delete(key)
                return None
            else:
                return value
        else:
            return None

    def delete(self, key):
        del self.data_map[key]
    
