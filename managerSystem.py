from student import *


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()

        while True:
            self.show_menu()

            menu_num = int(input('请输入序号:'))

            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    @staticmethod
    def show_menu():
        print('-----------------')
        print('1.添加学生')
        print('2.删除学生')
        print('3.修改学生信息')
        print('4.查找学生')
        print('5.展示所有学生信息')
        print('6.保存学生信息')
        print('7.退出系统')

    def add_student(self):
        name = input('请输入姓名')
        gender = input('请输入性别')
        tel = input('请输入电话')

        student = Student(name, gender, tel)

        self.student_list.append(student)

        print(self.student_list)
        print(student)

    def del_student(self):
        del_name = input('请输入要删除的姓名：')

        # for a in self.student_list:
        #     if a.name==del_name:
        #         self.student_list.remove(a)
        #         break
        # else:
        #     print('查无此人')

        student = self.search(del_name)
        if student is not None:
            self.student_list.remove(student)
        else:
            print('查无此人')

        print(self.student_list)

    def modify_student(self):
        old_name = input('请输入要修改的学员姓名：')

        student = self.search(old_name)

        if student is not None:
            student.name = input('请输入学生姓名：')
            student.gender = input('请输入学生性别：')
            student.tel = input('请输入学生电话：')
            print(f'修改该学员信息成功，姓名：{student.name},性别：{student.gender}, 手机号：{student.tel}')
        else:
            print('查无此人')

    def search_student(self):
        search_name = input('请输入要查询学生的姓名：')

        student = self.search(search_name)

        if student is not None:
            print(f'姓名{student.name},性别{student.gender}, 手机号{student.tel}')
        else:
            print('查无此人!')

    def show_student(self):
        print('姓名\t性别\t手机号')
        for a in self.student_list:
            print(f'{a.name}\t{a.gender}\t{a.tel}')

    def save_student(self):
        f = open('student.data', 'w')
        new_list = [a.__dict__ for a in self.student_list]
        print(new_list)

        f.write(str(new_list))

        f.close()

    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student_data', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(a['name'], a['gender'], a['tel']) for a in new_list]
        finally:
            f.close()

    def search(self, name):
        for a in self.student_list:
            if a.name == name:
                return a
        else:
            return None

