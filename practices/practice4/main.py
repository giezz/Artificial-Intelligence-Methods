from recommendations import critics, sim_distance, sim_pearson, top_matches
import matplotlib.pyplot as plt


def print_plots(film1, film2):
    x = []
    y = []
    for key, value in critics.items():
        if (film1 and film2) in value:
            x.append(value[film1])
            y.append(value[film2])
        else:
            continue

    print(x)
    print(y)

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel(f'оценки за {film1}')
    ax.set_ylabel(f'оценки за {film2}')
    plt.show()


if __name__ == '__main__':
    print_plots('Каникулы в Простоквашино', 'Ёжик в тумане')
    print(sim_distance(critics, 'Кот Матроскин', 'Пёс Шарик'))
    print(sim_pearson(critics, 'Кот Матроскин', 'Пёс Шарик'))
    top_matches(critics, 'Кот Матроскин')
