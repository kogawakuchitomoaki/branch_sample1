from serch_address import search_address


def main():
    zipcode = '0287111'

    address = search_address(zipcode)
    print(address)


if __name__ == '__main__':
    main()