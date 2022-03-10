import GUI
import TD

def main(M=0, R=0, graph=0):
    if (M==0 & R==0):
        GUI.main()
    print(M, type(M), R, type(R))
    X = TD.create_TAD(M)
    TD.use_TAD(X,M,R)
    TD.evaluate_TAD(X,M, graph)
    TD.generate_prime_number(70766)
    TD.hash_justin_maxence(8, "test")


if __name__ == "__main__":
    main()




