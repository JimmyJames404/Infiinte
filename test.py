import time
import json

i=0
def main(environ,start_response):
    while True:
        headers = [('Content-type','text/html')]
        print("Where on "+ str(i))
        start_response('200',headers)
        i = i+1
        time.sleep(5)
        response = {
            "Result ==> ":"Nce"    
        }
        return [bytes(json.dumps(response),'utf-8')]


if __name__ == "__main__":
    main()
