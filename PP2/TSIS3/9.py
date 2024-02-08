def calculate_running_average(sequence):
    running_sum = 0
    averages = []
    for i, num in enumerate(sequence, start=1):
        running_sum += num
        average = running_sum / i
        averages.append(average)
    return averages


input_sequence = input()
numbers = [int(num) for num in input_sequence.split()]


running_averages = calculate_running_average(numbers)
print(running_averages)