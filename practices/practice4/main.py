from recommendations import critics, sim_distance, sim_pearson, top_matches
import matplotlib.pyplot as plt


def print_plots():
    x = []
    y = []
    for key, value in critics.items():
        for key1, value1 in value.items():
            if key1 in 'Каникулы в Простоквашино':
                x.append(value1)
            elif key1 in 'Ёжик в тумане':
                y.append(value1)

    if len(x) > len(y):
        x = x[:len(y)]
    else:
        y = y[:len(x)]

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel('оценки за Каникулы в Простоквашино')
    ax.set_ylabel('оценки за Ёжик в тумане')
    plt.show()


if __name__ == '__main__':
    # print_plots()
    # sim_distance(critics, 'Кот Матроскин', 'Пёс Шарик')
    # sim_pearson(critics, 'Кот Матроскин', 'Пёс Шарик')
    print()
    top_matches(critics, 'Кот Матроскин')
