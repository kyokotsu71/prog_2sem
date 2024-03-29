# Создание массива размером 16x16 и заполнение его нулями
grid = [[0 for _ in range(16)] for _ in range(16)]

grid[0][1] = 1
grid[1][0] = 1
# Заполнение первой строки и первого столбца значениями 1

# Вычисление количества путей для каждой ячейки массива
for i in range(1, 16):
    for j in range(1, 16):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

# Вывод количества путей из левого нижнего угла в правый верхний угол
print(grid[15][15])
