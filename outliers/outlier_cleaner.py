#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    ### your code goes here
    all_data = []
    n = 0
    all_len = len(predictions)

    while n < all_len:
        error = (predictions[n] - net_worths[n]) * (predictions[n] - net_worths[n])
        t = ages[n], net_worths[n], error
        all_data.append(t)
        n = n + 1

    new_len = int(all_len * 0.9)

    cleaned_data = (sorted(all_data, key = lambda data: data[2]))[:new_len]
 
    return cleaned_data

