def line(func):
    def show(*args):
        print("=" * 30)
        func(*args)
        print("=" * 30)
    return show


class Report:
    count = 0

    def __init__(self, title):
        self.title = title
        Report.count += 1

    @classmethod
    def total_reports(cls):
        print("Total reports:", cls.count)

    @line
    def display(self):
        print("Report Title:", self.title)

    def __str__(self):
        return "Report: " + self.title


r1 = Report("Student Report")
r2 = Report("Library Report")

r1.display()
r2.display()

print(r1)

Report.total_reports()