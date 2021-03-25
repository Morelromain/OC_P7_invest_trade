

def fun (n: int) -> int:
    if (n == 0):
        return
    
    print(n % 2)
    fun(n // 2)

fun(33)