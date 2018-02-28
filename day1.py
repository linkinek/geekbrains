with open('salary.csv', 'r', encoding='utf-8') as file:
    file_content = file.readlines()

print('Средняя зарплата')

for line in file_content:
    line_proceeded = line.replace('\n', '').split(',')
    worker_name = line_proceeded.pop(0)
    avg = sum(map(float, line_proceeded)) / len(line_proceeded)
    print(f'{worker_name} | {avg:.2f} руб')
