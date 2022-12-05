import csv


class Sonnet:
    def __init__(self, number, text):
        self.number = number
        self.text = text.replace("[p]", "")

    def __str__(self):
        out = [
            self.text,
            "\t\t-- William Shakespeare, Sonnet {}".format(self.number),
        ]
        return "\n".join(out)


def generate_sonnets():
    sonnets = []
    with open('sonnets.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sonnets.append(Sonnet(row[0], row[1]))
    with open("./sonnets", "w") as f:
        f.writelines(["%% Shakespeare Sonnets\n"])
        for sonnet in sonnets:
            f.writelines(["%", "\n", str(sonnet), "\n"])


def main():
    generate_sonnets()


if __name__ == '__main__':
    main()
