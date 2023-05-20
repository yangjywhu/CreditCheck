from dataclasses import dataclass, field

@dataclass
class Student:
    classid: str = field(default = None)
    id: str = field(default = None)
    name: str = field(default = None)
    major: str = field(default = None)
    warn: bool = field(default = False)
    course: list = field(default = None)

    def __post_init__(self):
        pass

    def __str__(self):
        return '-'.join(self.to_list())

    def to_list(self):
        return [self.classid, self.id, self.name, self.major]

    def check_convert(self, all_course, ignore):
        for my_course in self.course:
            if my_course.type in ignore:
                continue
            raw_type = my_course.type
            my_course.type = "fail"
            for course in all_course:
                if my_course.can_replace(course):
                    my_course.name = course.name
                    my_course.type = raw_type
                    break

    def check_must(self, must_now, pass_score):
        my_courses = set(i.name for i in self.course if i.is_pass(pass_score))
        must_courses = set(i.name for i in must_now)
        incomplete = must_courses.difference(my_courses)
        return incomplete


    def type_names(self, types):
        return (i.name for i in self.course if i.type in types)

    def gpa(self, target_types):
        total_credi = 0
        total_gp = 0
        for course in self.course:
            if course.type in target_types:
                total_credi += course.credi
                total_gp += course.credi_gp
        
        gpa = total_gp / total_credi if total_credi else 0
        return {"credi": round(total_credi, 1), "gpa": round(gpa, 3)}
    
    def converted_course(self):
        return [i.name for i in self.course if i.name_changed()]