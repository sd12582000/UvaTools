"""
Uva User Statistics Object
"""

class UvaUser:
    """
    Uva User Statistics
    """

    def __init__(self, user_name):
        from . import UvaProblems
        from .lib import uhunt_api
        from .lib import GeneralMethod
        from os.path import join

        self.problem_set = UvaProblems()
        self.uid = uhunt_api.get_user_id(user_name)
        self.try_set = set()
        self.ac_set = set()

        file_name = "{}.json".format(self.uid)
        file_path = join("Users", file_name)

        try:
            self.submit = GeneralMethod.load_json_data(file_path)
            #print("load file")
        except (FileNotFoundError, AttributeError):
            self.submit = uhunt_api.get_user_submit(self.uid)
            self.save_user_sumbit()
            #print("get from uhunt")
        finally:
            self.init_user_statistics()

    def reload_user_sumbit(self):
        """
        Update user sumbit log from uhunt_api
        """
        from .lib import uhunt_api
        self.submit = uhunt_api.get_user_submit(self.uid)
        self.save_user_sumbit()
        self.init_user_statistics()

    def init_user_statistics(self):
        """
        init User Sumbit Statistics by user_submit
        Data Struct:

        Submission ID
        Problem ID
        Verdict ID
        Runtime
        Submission Time (unix timestamp)
        Language ID (1=ANSI C, 2=Java, 3=C++, 4=Pascal, 5=C++11)
        Submission Rank

        Verdict ID can be one of the following values:

        10 : Submission error
        15 : Can't be judged
        20 : In queue
        30 : Compile error
        35 : Restricted function
        40 : Runtime error
        45 : Output limit
        50 : Time limit
        60 : Memory limit
        70 : Wrong answer
        80 : PresentationE
        90 : Accepted

        Args:
            self: self

        Returns:
            None
        """
        for sub in self.submit:
            pro_num = self.problem_set.problem_id_to_num(sub[1])
            self.try_set.add(pro_num)
            if sub[2] == 90:
                self.ac_set.add(pro_num)

    def save_user_sumbit(self):
        """
        save user sumbit data to json file

        Args:
            self: self

        Returns:
            None
        """
        from .lib import GeneralMethod
        import os
        if not os.path.exists("Users"):
            os.mkdir("Users")
        file_path = os.path.join("Users", "{}.json".format(self.uid))
        GeneralMethod.save_json_data(self.submit, file_path)

    def is_acept(self, problem_num):
        """
        Is problem solved

        Args:
            self: self
            problem_num: Uva Problem Num

        Returns:
            boolen
            Is Problem solve?
        """

        return problem_num in self.ac_set
