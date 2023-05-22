from dataclasses import dataclass, field

@dataclass
class Student:
    classid: str = field(default = None)
    id: str = field(default = None)
    name: str = field(default = None)
    major: str = field(default = None)
    course: list = field(default = None)


    def __post_init__(self):
        pass


    def __str__(self):
        return '-'.join(self.to_list())


    def to_list(self):
        return [self.classid, self.id, self.name, self.major]


    def check_convert(self, all_course, same_course, ignore):
        for my in self.course:
            if my.type in ignore:
                continue
            my.warning = "fail"
            for target in all_course:
                if my.short_name == target.short_name:
                    if my.name != target.name or my.credit != target.credit:
                        my.warning = "diff"
                    else:
                        my.warning = "not"
                    my.name = target.name
                    my.credit = target.credit
                else:
                    for name_group in same_course:
                        if my.name in name_group and target.name in name_group:
                            my.name = target.name
                            my.warning = "diff"
                            my.credit = target.credit


    def check_must(self, must_now, pass_score):
        my_courses = set(i.name for i in self.course if i.is_pass(pass_score))
        must_courses = set(i.name for i in must_now)
        incomplete = must_courses.difference(my_courses)
        return incomplete


    def get_course(
            self,
            types = "all",
            warnings = "not",
            intersect = True,
            sep = " / "
        ):

        courses = []
        for course in self.course:
            cond1 = True if types == "all" else course.type in types
            cond2 = True if warnings == "not" else course.warning in warnings
            if cond1 and cond2 if intersect else cond1 or cond2:
                courses.append(course.name + "(%s)" % course.credit)

        if sep:
            return sep.join(courses)
        else:
            return courses


    def gpa(self, target_types):
        total_credit = 0
        total_score = 0
        for course in self.course:
            if course.type in target_types:
                total_credit += course.credit
                total_score += course.credit * max(course.score, 50)

        avg_score = total_score / total_credit if total_credit else 50
        gpa = avg_score / 10 - 5
        return {"credit": round(total_credit, 1), "gpa": round(gpa, 4)}


    def converted_course(self):
        return [i.name for i in self.course if i.name_changed()]


    # def remind_change(self):
    #     remind_course = []
    #     for course in self.course:
    #         if course.warning and course.type == "less":
    #             remind_course.append(course.name)

    #     return remind_course
