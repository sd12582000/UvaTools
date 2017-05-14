class UvaProblems:
    def __init__(self,fileName='uvaDic.json'):
        data=None
        try:
            import pkgutil
            from json import loads
            data = pkgutil.get_data(__package__, fileName)
            print(type(data.decode('utf-8')))
            self.dic=loads(data.decode('utf-8'))
        except FileNotFoundError:
            self.dic=self.getProblemNameDic()
            self.saveDic(fileName)

    def saveDic(self,fileName='uvaDic.json'):
        from os.path import abspath, join, dirname
        from json import dump

        filePath=join(abspath(dirname(__file__)),fileName)
        print(filePath)
        with open(filePath, 'w') as f:
            dump(self.dic, f)

    def getProblemNameDic(self):
        import requests
        
        result={}
        r=requests.get(
                url='http://uhunt.felix-halim.net/api/p'
            ).json()

        for problem in r:
            result[problem[1]]={
                'pid':problem[0],
                'pNumber':problem[1],
                'pTitle':problem[2]
            }
        return result