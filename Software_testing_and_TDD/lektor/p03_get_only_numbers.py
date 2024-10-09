class API:
    @classmethod
    def get_data_from_file(cls):
        return open('aa').readlines()


def get_only_numbers():
    numbers = []
    for line in API.get_data_from_file():
        digits = [x.strip() for x in line.split(',') if x.strip().isdigit()]
        numbers.extend(digits)

    return '|'.join(numbers)


if __name__ == "__main__":
    print(get_only_numbers())
