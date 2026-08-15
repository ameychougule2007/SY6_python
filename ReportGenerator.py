def bold_text(func):
    def wrapper(title, content):
        result = func(title, content)
        return "**" + result + "**"
    return wrapper


class Report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = self.get_template(template_name)
        return template(self.title, self.content)

    def __str__(self):
        return self.title + "\n" + self.content


def simple_template(title, content):
    return title + "\n" + content


@bold_text
def fancy_template(title, content):
    return title + "\n" + content


Report.add_template("simple", simple_template)
Report.add_template("fancy", fancy_template)

title = input("Enter report title: ")
content = input("Enter report content: ")

report = Report(title, content)

print("\nChoose report format:")
print("1. Simple")
print("2. Fancy")

choice = input("Enter your choice: ")

if choice == "1":
    print("\nReport:")
    print(report("simple"))

elif choice == "2":
    print("\nReport:")
    print(report("fancy"))

else:
    print("Invalid choice")
