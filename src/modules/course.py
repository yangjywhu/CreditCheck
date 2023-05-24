# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import re

@dataclass
class Course:
    name: str = field(default = None)
    type: str = field(default = None)
    credit: str = field(default = None)
    score: str = field(default = None)
    semester: str = field(default = None)
    warning: str = field(default = None)


    def __post_init__(self):
        level = re.compile("[A-E]").findall(self.name)
        self.level = None if not level else level[0]
        self.raw_name = self.name
        self.short_name = re.sub("[A-E]", '', self.name)
        self.credit = float(self.credit)
        self.score = int(self.score)
        gp = self.score / 10 - 5
        self.gp = gp if gp >= 1 else 0


    def __str__(self):
        return "%s %s %.1f %d %s" % (self.name, self.type, self.credit, self.score, self.warning)

    def __eq__(self, other):
        cond1 = self.name == other.name
        cond2 = self.credit == other.credit 
        cond3 = self.type == other.type
        return cond1 and cond2 and cond3


    def convert_to(self, other, warning = "not"):
        self.name = other.name
        self.credit = other.credit
        self.type = other.type
        self.warning = warning


    def to_list(self):
        return [self.name, self.type, self.credit, self.score, self.semester]

  
    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "credit": self.credit,
            "score": self.score,
            "semester": self.semester
        }


    def can_replace(self, other):
        if self.short_name != other.short_name:
            return False
        if self.credit < other.credit:
            return False
        return True


    def name_changed(self):
        return self.name != self.raw_name or self.warning


    def in_list(self, course_list):
        return self.name in course_list


    def is_pass(self, pass_score):
        return self.score >= pass_score



def list_to_course(raw_list):
    """
    If course name is started with English letter, it may contain "第*学期"
    """
    course_list = []
    for raw in raw_list:
        new = list(raw)
        if raw[0][1].isdigit():
            new[0] = raw[0][4:]
        course = Course(*new)
        course_list.append(course)

    return course_list

# def dict_to_course(raw_dict):
#     return [Course(**i) for i in raw_dict]