from datetime import datetime

now = datetime.now()
et_stdc_filename = "ET_STDC%s.txt" % (now.strftime("%Y-%m-%d %H-%M-%S"),)
thai_names = []
eng_names = []
year = "2565"
semester = "1"
id = "99%08d"
subject = ["RAM1007", "RAM1008"]
test_date = "30"
test_month = "05"
test_year = "65"
section_no = ["1", "2", "3"]
room_no = ["SKB801", "SKB802", "SKB803", "SKB804", "SKB805"]
seat_no = ["A%02d", "B%02d", "C%02d"]
row_id = ["A", "B", "C"]
room_index = 0
section_index = 0
seat_index = 0
seat_count = 0
subject_index = 0
max_seat = 99
max_per_day = max_seat * len(seat_no) * len(section_no) * len(room_no)
dup = 5
total = 9000
total_count = 0
actual = total
days = ["300565", "310565", "010665", "020665", "030665"]
day_index = 0
students = 0
seats_data = {}
for i in range(0, len(section_no)):
    seats_data[section_no[i]] = {}
    for j in range(0, len(room_no)):
        seats_data[section_no[i]][room_no[j]] = {}
        for k in range(0, len(row_id)):
            seats_data[section_no[i]][room_no[j]][row_id[k]] = 0


def get_seat(section, room, row):
    try:
        count = seats_data[section][room][row]
        count = count + 1
        seats_data[section][room][row] = count
        return row + "%02d" % count
    except KeyError as e:
        print("Key not found", e)
        exit(0)


with open(et_stdc_filename, "a") as f:
    for id_count in range(0, dup):
        id_count = id_count + 1
        students = students + 1
        total_count = total_count + 1
        seat_count = seat_count + 1
        subject_index = subject_index + 1
        if seat_count % (max_seat + 1) == 0:
            seat_index = seat_index + 1
            if seat_index % len(section_no) == 0:
                section_index = section_index + 1
                section_index = section_index % len(section_no)
                if section_index % len(room_no) == 0:
                    room_index = room_index + 1
                    if room_index == len(room_no):
                        room_index = 0
            seat_index = seat_index % len(seat_no)
            seat_count = 1
        thai_name = (
            "T"
            + ("99%08d" % id_count)
            + " "
            + (seat_no[seat_index % len(seat_no)] % (seat_count,))
            + "-"
            + subject[0]
        )
        eng_name = (
            "E"
            + ("99%08d" % id_count)
            + " "
            + (seat_no[seat_index % len(seat_no)] % (seat_count,))
            + "-"
            + subject[0]
        )
        thai_names.append(thai_name)
        eng_names.append(eng_name)
        f.write(
            year
            + semester
            + (id % (id_count,))
            + subject[0]
            + (
                "   %02d %02d "
                % (
                    99,
                    99,
                )
            )
            + days[day_index]
            + section_no[section_index]
            + " "
            + room_no[room_index]
            + (
                get_seat(
                    section_no[section_index], room_no[room_index], row_id[seat_index]
                )
                + " e-  000 000 000 0000\n"
            )
        )

students = 0
seat_index = 0
seat_count = 0
subject_index = 0
room_index = 0
with open(et_stdc_filename, "a") as f:
    for id_count in range(0, actual):
        id_count = id_count + 1
        students = students + 1
        total_count = total_count + 1
        seat_count = seat_count + 1
        subject_index = subject_index + 1
        if seat_count % (max_seat + 1) == 0:
            seat_index = seat_index + 1
            if seat_index % len(section_no) == 0:
                section_index = section_index + 1
                section_index = section_index % len(section_no)
                if section_index % len(room_no) == 0:
                    room_index = room_index + 1
                    if room_index == len(room_no):
                        room_index = 0
            seat_index = seat_index % len(seat_no)
            seat_count = 1

        if id_count <= dup:
            thai_names[id_count - 1] = (
                thai_names[id_count - 1]
                + ","
                + (seat_no[seat_index % len(seat_no)] % (seat_count,))
                + "-"
                + subject[1]
            )
            eng_names[id_count - 1] = (
                eng_names[id_count - 1]
                + ","
                + (seat_no[seat_index % len(seat_no)] % (seat_count,))
                + "-"
                + subject[1]
            )

            f.write(
                year
                + semester
                + (id % (id_count,))
                + subject[1]
                + (
                    "   %02d %02d "
                    % (
                        99,
                        99,
                    )
                )
                + days[day_index]
                + section_no[1]
                + " "
                + room_no[room_index]
                + get_seat(section_no[1], room_no[room_index], row_id[seat_index])
                + " e-  000 000 000 0000\n"
            )
        else:

            thai_name = (
                "T"
                + ("99%08d" % id_count)
                + " "
                + (seat_no[seat_index % len(seat_no)] % (seat_count,))
                + "-"
                + subject[subject_index % len(subject)]
            )
            eng_name = (
                "E"
                + ("99%08d" % id_count)
                + " "
                + (seat_no[seat_index % len(seat_no)] % (seat_count,))
                + "-"
                + subject[subject_index % len(subject)]
            )
            thai_names.append(thai_name)
            eng_names.append(eng_name)
            f.write(
                year
                + semester
                + (id % (id_count,))
                + subject[subject_index % len(subject)]
                + (
                    "   %02d %02d "
                    % (
                        99,
                        99,
                    )
                )
                + days[day_index]
                + section_no[section_index]
                + " "
                + room_no[room_index]
                + get_seat(
                    section_no[section_index], room_no[room_index], row_id[seat_index]
                )
                + " e-  000 000 000 0000\n"
            )

        if students >= max_per_day:
            day_index = day_index + 1
            day_index = day_index % len(days)
            students = 0

ru25et_filename = "RU25ET%s.txt" % (now.strftime("%Y-%m-%d %H-%M-%S"),)
sex = [1, 2, 3]
with open(ru25et_filename, "w") as f:
    for i in range(0, len(thai_names)):
        i = i + 1
        f.write(
            "99%08d%02d %s                          %s                       %s\n"
            % (
                (i),
                sex[(i - 1) % 3],
                thai_names[i - 1],
                eng_names[i - 1],
                "0601A1010525380100000003840",
            )
        )
