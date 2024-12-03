def find_safe_reports(file_path):
    
    def check_report(report):
        if report[-1] < report[0]:
            report.reverse()
        x0 = report[0]
        x1 = report[1]
        for i in range(len(report)):
            if i == 0:
                continue
            else:
                x0 = report[i-1]
                x1 = report[i]
            if 3 >= x1 - x0 >= 1:
                continue
            else:
                return False
        return True

    with open(file_path) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split() for line in lines]
        lines = [[int(n) for n in line] for line in lines]
    checked_reports = [check_report(report) for report in lines]
    print(sum(checked_reports))

def find_safe_reports_with_dampener(file_path):
    
    def check_report(report):
        if report[-1] < report[0]:
            report.reverse()
        x0 = report[0]
        x1 = report[1]
        for i in range(len(report)):
            if i == 0:
                continue
            else:
                x0 = report[i-1]
                x1 = report[i]
            if 3 >= x1 - x0 >= 1:
                continue
            else:
                return False
        return True

    with open(file_path) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split() for line in lines]
        lines = [[int(n) for n in line] for line in lines]
        check_reports = []
        for report in lines:
            check = check_report(report)
            if not check:
                for i in range(len(report)):
                    dampened_report = report.copy()
                    del dampened_report[i]
                    check = check_report(dampened_report)
                    if check:
                        break
            check_reports.append(check)

    print(sum(check_reports))

def main():
    find_safe_reports('day2/input.txt')
    find_safe_reports_with_dampener('day2/input.txt')

if __name__ == "__main__":
    main()
