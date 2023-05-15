def countdown(i):
    # base case
    if i <= 0:  # добавляем стопор/ограничение в рекурсию
        return 0
    # recursive case
    else:
        print(i)
        return countdown(i - 1)


if __name__ == '__main__':
    print(countdown(5))
