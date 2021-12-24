from event_handler.web_functions import create_file

functions = {
    'web': {
        'create_file': create_file
    }
}
def event_handler(Topic,key,value):
    functions[Topic].get(key)(value)


