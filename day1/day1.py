import csv

def find_total_distance(file_path):
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=' ')
        lines = list(reader)
        first, x, y, second = list(zip(*lines))
        first = list(first)
        first.sort()
        second = list(second)
        second.sort()
        diffs = [abs(int(first[i]) - int(second[i])) for i in range(len(first))]
        print(sum(diffs))

def find_similarity_score(file_path):
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=' ')
        lines = list(reader)
        first, x, y, second = list(zip(*lines))
        first = list(first)
        second = list(second)
        similarities = [second.count(n) * int(n) for n in first]
        print(sum(similarities))

def main():
    find_total_distance('day1/input.txt')
    find_similarity_score('day1/input.txt')

if __name__ == "__main__":
    main()