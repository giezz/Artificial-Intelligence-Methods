import re


def task1(string):
    return re.match(r"^(#([A-Fa-f0-9]){3}(([A-Fa-f0-9]){3})?)$", string).group(0)


def task2(string):
    if re.match(r"^(https?://)?([0-9A-Za-z]+\.)([A-Za-z]+)([/?&]|$)", string):
        return re.findall(r"([0-9A-Za-z]+\.)([A-Za-z]+)", string)


def task3(string):
    return re.match(r"^([A-Za-z]+\.)(png|gif|jpeg|jpg)$", string).group(0)


if __name__ == '__main__':
    print(task1("#FFF"))
    print(task2("https://vk.com/doc86821578_645914657?hash=esMK5BIpiy5vvI5JTbZatnY78SRzBH8YZJ9aJYAWu7o&dl=4beQ2l10lHrGvPO1PYu00ZnVch8EqawuNYT974XbnFP"))
    print(task3("f1le.png"))


