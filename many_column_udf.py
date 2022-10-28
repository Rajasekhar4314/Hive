for line in sys.stdin:
        line = line.strip("\n\r")
        country, quantity = line.split("\t")
        quantity = int(quantity)
        quantity = quantity* 100
        result = "\t".join([country, str(quantity)])
        print(result)
