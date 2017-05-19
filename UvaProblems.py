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
        self.id2num_dic = {}

        try:
            from .lib import GeneralMethod
            self.dic = GeneralMethod.load_json_data(__package__, fileName)
        except (FileNotFoundError, AttributeError):
            from .lib import uhunt_api
            self.dic = uhunt_api.get_problem_name_dic_from_uhunt()
            self.save_dic(fileName)
        finally:
            self.create_id2num_dic()

    def create_id2num_dic(self):
        """
        Creat ProblemId mapping ProblemNumber dictionary
        """
        self.id2num_dic = {}

        for key, problem in self.dic.items():
            self.id2num_dic[problem["pid"]] = key


    def save_dic(self, file_name='uvaDic.json'):
        """
        save problems dictionary to json file

        Args:
            self: self
            file_name: json file name

        Returns:
            None
        """
        from .lib import GeneralMethod
        from os.path import abspath, join, dirname
        file_path = join(abspath(dirname(__file__)), file_name)
        GeneralMethod.save_json_data(self.dic, file_path)

    def problem_id_to_num(self, problem_id):
        """
        problem Number to problem title

        Args:
            self: self
            problem_id: problem Id

        Returns:
            String:problem Number if exist
                else return "-1"
        """
        if problem_id in self.id2num_dic:
            return self.id2num_dic[problem_id]
        else:
            return "-1"

    def get_title(self, problem_num):
        """
        problem Number to problem title

        Args:
            self: self
            problem_num: problem Number

        Returns:
            String:problem title if exist
                else return ""
        """

        if problem_num in self.dic:
            return self.dic[problem_num]["pTitle"]
        else:
            return ""
