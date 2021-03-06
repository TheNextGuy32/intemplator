import json

def GetTemplateFilePath(templateName):
    return os.path.join(os.path.dirname(__file__),'templates/' + templateName)

def ReadJson (path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
        return data