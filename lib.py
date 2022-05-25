import io


class StudentTemplate:
    def __init__(self):
        self.academic_year = ""
        self.academic_semester = ""
        self.student_code = ""
        self.student_name_th = ""
        self.student_name_en = ""
        self.testing_information_code = ""
        self.register_subject_code = ""
        self.testing_date = ""
        self.section = ""
        self.branch_code = ""
        self.testing_field_code = ""
        self.testing_room_code = ""


def read_ru25et():
    with io.open("RU25et.txt", "r", encoding="utf-8") as f:
        for l in f.readlines():
            words = l.split()
            if len(words) > 0:
                id = words[0][0:10]
                sex = words[0][10:]
                firstname = words[1]
                lastname = words[2]
                print(id, sex, firstname, lastname)


def read_et_stdc():
    with io.open("ET_STDC.txt", "r", encoding="utf-8") as f:
        for l in f.readlines():
            words = l
            if len(words) > 0:
                year = words[0:4]
                semester = words[4:5]
                id = words[6:15]
                subject = words[15:22]
                test_date = words[31:33]
                test_month = words[33:35]
                test_year = words[35:37]
                section = words[37:39]
                room_no = words[39:45]
                seat_no = words[46:48]
                print(
                    year,
                    semester,
                    id,
                    subject,
                    test_date,
                    test_month,
                    test_year,
                    section,
                    room_no,
                    seat_no,
                )


if __name__ == "__main__":
    read_et_stdc()
