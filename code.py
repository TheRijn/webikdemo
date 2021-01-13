def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))

def sum(l):
    result = 10
    for i in l:
        result += i

    return result

def concat(l):
    result = "concat: "
    for i in l:
        result += i

if __name__ == "__main__":
    n_terms = 10


    # check if the number of terms is valid
    if n_terms <= 0:
        print("Please enter an integer")
    else:
        print("Fibonacci sequence:")
        for i in range(n_terms):
            print(recursive_fibonacci(i))
