# # prime.py
# def prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#

def prime(n):
    for k in (2, n):
        if n % k == 0:
            break
    if k == n:
        return 1
    else:
        return 0