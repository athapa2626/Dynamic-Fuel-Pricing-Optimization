def summarize_results(actual_profits, optimized_profits):

    total_actual = sum(actual_profits)
    total_optimized = sum(optimized_profits)
    improvement = total_optimized - total_actual

    return total_actual, total_optimized, improvement