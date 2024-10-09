class API:
    @classmethod  #(dekorator) diky teto metode muzu pouzit primo tridu v radku 9
    def get_data(cls):  #cls = class pokud pouziju dekorator
        return open('aa').readlines()  # 'aa' textak s daty



def get_only_numbers():
    numbers = []
    for line in API.get_data():
        digits = [x.strip() for x in line.split(',') if x.strip().isdigit()]
        # TODO zjistit jestli je digits jen pojmenovani?
        numbers.extend(digits)

    return '|'.join(numbers)

if __name__ == "__main__":
    print(get_only_numbers())  # do print vkladam nazev definovane funkce
