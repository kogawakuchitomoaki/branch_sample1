from search_address import search_address


def main():
    zipcode = input('郵便番号<ハイフン無し7桁>は？')

    address = search_address(zipcode)

    print(address)


if __name__ == '__main__':
    main()