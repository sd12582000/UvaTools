"""
Store Uva Problem data{
Problem ID
Problem Number
Problem Title
}
dictionary
"""

class UvaProblems:
    """
    Uva Problem Data Bridge
    """
    def __init__(self, fileName='uvaDic.json'):
        data = None
        try:
            import pkgutil
            from json import loads
            data = pkgutil.get_data(__package__, fileName)
            print(type(data.decode('utf-8')))
            self.dic = loads(data.decode('utf-8'))
        except FileNotFoundError:
            self.dic = self.get_problem_name_dic_from_uhunt()
            self.save_dic(fileName)

    def save_dic(self, file_name='uvaDic.json'):
        """
        save problems dictionary to json file

        Args:
            self: self
            file_name: json file name

        Returns:
            None
        """

        from os.path import abspath, join, dirname
        from json import dump

        file_path = join(abspath(dirname(__file__)), file_name)
        print(file_path)
        with open(file_path, 'w') as json_file:
            dump(self.dic, json_file)

    @staticmethod
    def get_problem_name_dic_from_uhunt():
        """
        get problem dictionary from uhunt

        Returns:
            problem dictionary
        """

        import requests

        result = {}
        req = requests.get(url='http://uhunt.felix-halim.net/api/p').json()

        for problem in req:
            result[problem[1]] = {
                'pid':problem[0],
                'pNumber':problem[1],
                'pTitle':problem[2]
            }
        return result
