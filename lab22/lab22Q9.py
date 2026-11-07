# (9) Write a decorator log_function_call that prints Running DNA analysis.... before
# and Analysis complete! after any function. Apply it to the above function that returns
# the GC % of a DNA sequence.

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper

@log_function_call
def gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

sequence = "ATGCGCAT"
gc_percentage = gc_content(sequence)

print("GC Content:", round(gc_percentage, 2), "%")