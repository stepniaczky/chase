from src.models import Wolf, Sheep
from src.common import MAX_NUMBER_OF_ROUNDS, SIZE_OF_FLOCK
from src.common import config, to_csv, to_json


def simulation(size_of_flock: int, max_number_of_rounds: int) -> None:
    wolf = Wolf()
    sheep_flock = [Sheep(i + 1) for i in range(size_of_flock)]

    for round in range(1, max_number_of_rounds+1):
        for sheep in sheep_flock:
            sheep.move()

        wolf.find_nearest_sheep(sheep_flock=sheep_flock)
        wolf.move()

        # INFO
        print(f'Round: {round}')
        print(f'Wolf position: ({wolf.pos.x}, {wolf.pos.y})')

        alive_sheep_count = len(
            [sheep for sheep in sheep_flock if sheep.is_alive])
        print(f'Number of alive sheeps: {alive_sheep_count}')

        last_wolf_interaction = 'Chased sheep ID:' if wolf.nearest_sheep.is_alive else 'Eaten sheep ID:'
        print(last_wolf_interaction, wolf.nearest_sheep.id)

        to_json(round_no=round, wolf_pos=(wolf.pos.x, wolf.pos.y), sheep_pos=[
                (sheep.pos.x, sheep.pos.y) if sheep.is_alive else None for sheep in sheep_flock])
        to_csv(round_noumber=round, number_of_alive_sheep=alive_sheep_count)

        if not any(sheep.is_alive for sheep in sheep_flock):
            print(round)
            break


if __name__ == '__main__':
    config(json_file_path='pos.json', csv_file_path='alive.csv')
    simulation(size_of_flock=SIZE_OF_FLOCK,
               max_number_of_rounds=MAX_NUMBER_OF_ROUNDS)
