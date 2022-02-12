class school_requirements:
    def __init__(self, class_size, gender_split, main_language, ability):
        self.class_size = class_size
        self.gender_splits = gender_split
        self.main_language = main_language
        self.ability = ability

    def skl_class_stats(self):
        print(
            "Your class has these values: "
            + "\n"
            + self.class_size
            + "\n"
            + self.gender_splits
            + "\n"
            + self.main_language
            + "\n"
            + self.ability
        )


class_size_query = input("What is the size of your class? ")
class_size_query += " pupils"
gender_split_query = input("What is the gender split of the class? ")
main_language_query = input("What is the main language of the class? ")
main_language_query += " is the main language"
ability_query = input("What is the ability level of the class? ")
ability_query += " ability in the class"

class1a = school_requirements(
    class_size_query, gender_split_query, main_language_query, ability_query
)

class1a.skl_class_stats()
# class2b =
