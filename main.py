import sorting, timing, createlist
import matplotlib.pyplot as plt
import numpy as np

def plot_sorting_algorithms(max_length, step):
    list_types = {
        'Sorted': createlist.sorted,
        'Mostly Sorted': createlist.mostlysorted,
        'Reversed': createlist.reversed,
        'Shuffled': createlist.shuffled
    }
    
    sorting_algorithms = {
        'Bubble Sort': sorting.bubble,
        'Merge Sort': sorting.merge,
        'Insertion Sort': sorting.insertion,
        'Quick Sort': sorting.quick
    }
    
    for list_name, list_func in list_types.items():
        plt.figure()
        for alg_name, alg_func in sorting_algorithms.items():
            lengths = []
            times = []
            for length in range(0, max_length + 1, step):
                test_list = list_func(length)
                t, _ = alg_func(test_list)
                lengths.append(length)
                times.append(t)
            plt.plot(lengths, times, label=alg_name)

        plt.title(f'{list_name}')
        plt.xlabel('List Length')
        plt.ylabel('Time (s)')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'{list_name}_plot.png')
        
    plt.show()
    
plot_sorting_algorithms(1000, 10)