'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Check for the negative values
    if n < 0:
        # means we didn't get to one of the ways
        return 0
    #only one way to eat one cookie
    if n <= 1:
        return 1
    #two ways: 1+1 or 2
    if n == 2:
        return 2
    #ways if he ate 1 at a time + 2 cookies at a time + 3 cookies at a time   
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
