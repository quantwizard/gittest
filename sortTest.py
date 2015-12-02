from operator import itemgetter


def main():
    oriList = [
        {"name": "John", "age": 22, "score": "A"},
        {"name": "Jack", "age": 21, "score": "A"},
        {"name": "Bob", "age": 20, "score": "B"},
        {"name": "Jenny", "age": 22, "score": "C"}
    ]

    sortByAgeList = sorted(oriList, key=lambda x: x["age"])
    print sortByAgeList
    sortByAgeAndNameList = sorted(oriList, key=itemgetter("age", "name"))
    print sortByAgeAndNameList

if __name__ == '__main__':
    main()
