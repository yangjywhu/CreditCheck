# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import re

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
        same_course_flatten = [i for j in same_course for i in j]
        all_short = {}
        for key, value in all_course.items():
            all_short[re.sub("[A-E]", '', key)] = value
    
        for my in self.course:
            if my.type in ignore:
                continue
            my.warning = "fail"

            if my.short_name in all_short.keys():
                target = all_short[my.short_name]
                my.convert_to(target, "not" if my == target else "diff")

            elif my.name[:2] == "体育":
                if my.name[-1] == ')':
                    target = all_short[my.name.split('(')[0]]
                    my.convert_to(target, "not")

            elif my.name[:2] == "二外":
                target = my.name.split('(')[0].replace("二外", "大学基础英语")
                target = all_short[target]
                my.convert_to(target, "diff")
            
            elif my.name in same_course_flatten:
                break_flag = False
                for name_group in same_course:
                    if my.name in name_group:
                        for target in name_group:
                            if target in all_course.keys():
                                my.convert_to(all_course[target], "diff")
                                break_flag = True
                                break
                    if break_flag:
                        break


    def check_must(self, must_now, pass_score):
        my_courses = set(i.name for i in self.course if i.is_pass(pass_score))
        must_courses = set(i.name for i in must_now.values())
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
