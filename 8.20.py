def e_mu_x(x, sai_so, n=0, ket_qua=1):
        return e_mu_x(x, sai_so, n, ket_qua)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

x = float(input("Nhập giá trị của x: "))
sai_so = 1e-4
ket_qua = e_mu_x(x, sai_so)
print(f"e^{x} gần đúng với sai số {sai_so} là: {ket_qua}")
