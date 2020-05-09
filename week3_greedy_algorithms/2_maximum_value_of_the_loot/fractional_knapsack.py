# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    value_per_unit_of_weight = [values[i] / float(weights[i]) for i in range(0, len(weights))]
    while capacity > 0 and len(value_per_unit_of_weight) > 0:
        best_value_index = value_per_unit_of_weight.index(max(value_per_unit_of_weight))
        if (weights[best_value_index] > capacity):
            value += value_per_unit_of_weight[best_value_index] * capacity
            break
        
        value += values[best_value_index]
        capacity -= weights[best_value_index]
        del value_per_unit_of_weight[best_value_index]
        del weights[best_value_index]
        del values[best_value_index]
        
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
