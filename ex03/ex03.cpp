#include <string>
#include <vector>
using std::string;
using std::vector;

std::pair<int, int> find_snake_head(const vector<string>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 'h') {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

vector<vector<int>> trace_snake_path(const vector<string>& grid, int headRow, int headCol) {
    vector<vector<int>> path = {{headCol, headRow}};
    int rows = grid.size();
    int cols = grid[0].size();
    int row = headRow, col = headCol;
    while (true) {
        if (row > 0 && grid[row - 1][col] == 'v') {
            row--;
        } else if (row < rows - 1 && grid[row + 1][col] == '^') {
            row++;
        } else if (col > 0 && grid[row][col - 1] == '>') {
            col--;
        } else if (col < cols - 1 && grid[row][col + 1] == '<') {
            col++;
        } else {
            break;
        }
        path.push_back({col, row});
    }
    return path;
}

vector<vector<int>> find_snake_on_grid(const vector<string>& grid) {
    auto [headRow, headCol] = find_snake_head(grid);
    if (headRow == -1 || headCol == -1)
        return {};
    return trace_snake_path(grid, headRow, headCol);
}