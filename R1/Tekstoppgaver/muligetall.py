def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None

def main():
    file_path = "results.txt"

    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        expression = line.strip()
        result = calculate_expression(expression)
        if result is not None:
            results.append(result)

    print(f"Number of valid results: {len(results)}")

if __name__ == "__main__":
    main()
