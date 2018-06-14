json_body2 = [{
  "measurement": 'weather',
  "tags":{
    "location_one": 'atx',
    "location_two": 'sfo'
    },
  "time": 1234567,
   "fields": {
    "temp_one": 105,
    "temp_two": 85
    }
}]

def data_call():
    data = json_body2
    print(data)
    return (data)

data_call()
