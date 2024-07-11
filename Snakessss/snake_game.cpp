#include <conio.h>
#include <iostream>
#include <windows.h>

using namespace std;

const int width = 80;
const int height = 20;

int x_cor, y_cor; // snake head coordinate
int food_x, food_y; // food coordinate
int score; // variable to store the score
int tail_x[100], tail_y[100]; // array to store the tail
int length; // to store the length of the tail
enum snakesDirection { STOP = 0, LEFT, RIGHT, UP, DOWN };
snakesDirection sDir; // direction of the snake
bool gameover;

// Game initialization
void gameinit() {
    gameover = false;
    sDir = STOP;
    x_cor = width / 2;
    y_cor = height / 2;
    score = 0;
    food_x = rand() % width;
    food_y = rand() % height;
    length = 0;
}

// Render the game board
void gamerender(string playername) {
    system("cls"); // Clear the console

    // Top wall
    for (int i = 0; i < width + 2; i++) {
        cout << "-";
    }
    cout << endl;

    // Side walls and game board
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width + 2; j++) {
            if (j == 0 || j == width + 1) {
                cout << "|"; // Side walls
            } else if (i == y_cor && j == x_cor + 1) {
                cout << "0"; // Snake's head
            } else if (i == food_y && j == food_x + 1) {
                cout << "#"; // Food
            } else {
                bool prTail = false;
                for (int k = 0; k < length; k++) {
                    if (tail_x[k] == j - 1 && tail_y[k] == i) {
                        cout << "o"; // Snake's tail
                        prTail = true;
                        break;
                    }
                }
                if (!prTail) {
                    cout << " "; // Empty space
                }
            }
        }
        cout << endl;
    }

    // Bottom wall
    for (int i = 0; i < width + 2; i++) {
        cout << "-";
    }
    cout << endl;

    // Display player's score
    cout << playername << "'s Score: " << score << endl;
}

// Update the game state
void UpdateGame() {
    // Store previous position of the first segment of the snake's tail
    int prevx = tail_x[0];
    int prevy = tail_y[0];
    int prev2x, prev2y;

    tail_x[0] = x_cor;
    tail_y[0] = y_cor;

    for (int i = 1; i < length; i++) {
        prev2x = tail_x[i];
        prev2y = tail_y[i];
        tail_x[i] = prevx;
        tail_y[i] = prevy;
        prevx = prev2x;
        prevy = prev2y;
    }

    switch (sDir) {
        case LEFT:
            x_cor--;
            break;
        case RIGHT:
            x_cor++;
            break;
        case UP:
            y_cor--;
            break;
        case DOWN:
            y_cor++;
            break;
        default:
            break;
    }

    // Check for collisions with walls
    if (x_cor >= width || x_cor < 0 || y_cor >= height || y_cor < 0) {
        gameover = true;
    }

    // Check for collisions with the snake's tail
    for (int i = 0; i < length; i++) {
        if (x_cor == tail_x[i] && y_cor == tail_y[i]) {
            gameover = true;
        }
    }

    // Check if the snake has eaten the food
    if (x_cor == food_x && y_cor == food_y) {
        score += 10;
        food_x = rand() % width;
        food_y = rand() % height;
        length++;
    }
}

// Handle user input
void UserInput() {
    if (_kbhit()) {
        switch (_getch()) {
            case 'a':
                if (sDir != RIGHT) sDir = LEFT;
                break;
            case 'd':
                if (sDir != LEFT) sDir = RIGHT;
                break;
            case 'w':
                if (sDir != DOWN) sDir = UP;
                break;
            case 's':
                if (sDir != UP) sDir = DOWN;
                break;
            case 'x':
                gameover = true;
                break;
        }
    }
}

// Set the game difficulty
int SetDifficulty() {
    int dfc, choice;
    cout << "\nSET DIFFICULTY\n1: Easy\n2: Medium\n3: Hard\n";
    cout << "NOTE: if not chosen or pressed any other key, the difficulty will be automatically set to medium\n";
    cout << "Choose difficulty level: ";
    cin >> choice;
    switch (choice) {
        case 1:
            dfc = 150; // Easier (slower)
            break;
        case 2:
            dfc = 100; // Medium (default)
            break;
        case 3:
            dfc = 50; // Harder (faster)
            break;
        default:
            dfc = 100;
            break;
    }
    return dfc;
}

// Main function
int main() {
    string playername;
    cout << "Enter your name: ";
    cin >> playername;

    int dfc = SetDifficulty();

    gameinit();
    while (!gameover) {
        gamerender(playername);
        UserInput();
        UpdateGame();
        Sleep(dfc);
    }

    cout << "Game Over! Final Score: " << score << endl;
    return 0;
}
