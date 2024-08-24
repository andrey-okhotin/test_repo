import argparse

def main()
    print("here")
    with open("../app/output.txt", "w") as f:
        f.write("here")
    parser = argparse.ArgumentParser()
    parser.add_argument('-gpu', '--gpu', default='', type=str)
    parser.add_argument('-port', '--port', default='8900', type=str)
    args = parser.parse_args()
    args.gpu = tuple(map(int, args.gpu.split('_')))
    print(f"\n\n {args.gpu} \n\n", flush=True)
    pass

if __name__ == '__main__':    
    main()
