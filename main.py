def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    for i in range (5):
        num = int(input('Enter a number  '))
        numbers.append(num)
    minval = numbers[0]
    maxval = numbers[0]
    for j in numbers:
        if j < minval:
            minval = j
        if j > maxval:
            maxval = j

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
