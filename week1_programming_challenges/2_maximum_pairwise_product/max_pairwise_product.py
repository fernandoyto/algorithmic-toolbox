# python3

def max_pairwise_product(numbers):
    if len(numbers) == 2:
        return numbers[0] * numbers[1]

    max_index1 = 0
    for i in range(0, len(numbers)):
        if numbers[i] > numbers[max_index1]:
            max_index1 = i
    
    max_index2 = 0
    for j in range(0, len(numbers)):
        if numbers[j] > numbers[max_index2] and j != max_index1:
            max_index2 = j

    return numbers[max_index1] * numbers[max_index2] 

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))