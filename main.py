import functions_framework
from transformers import pipeline

@functions_framework.http
def hello_http(request):

    model_name = "pysentimiento/roberta-es-sentiment"
    pipe = pipeline('sentiment-analysis', model=model_name)
    
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    result = pipe(name)

    return result
    
    """return 'Hello {}!'.format(name)"""
