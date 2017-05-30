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
            self.dic = GeneralMethod.load_json_data(fileName)
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
        file_path = file_name
        #file_path = join(abspath(dirname(__file__)), file_name)
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

    def creat_problem_dir(self, root_path, problem_num):
        """
        Creat Dir in my style
        root/volume{:0>3}/ProblemTitle
        """
        import os
        problem_int = int(problem_num)
        dir_path = os.path.join(root_path, 'volume{:0>3}'.format(problem_int//100))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        problem_title = self.get_title(problem_num)
        error_char = ['<', '>', ':', '\"', '/', '\\', '|', '?', '*']
        for ecr in error_char:
            problem_title = problem_title.replace(ecr, ' ')
        problem_title = '{}-{}'.format(problem_num, problem_title)
        problem_path = os.path.join(dir_path, problem_title)
        if not os.path.exists(problem_path):
            os.makedirs(problem_path)
