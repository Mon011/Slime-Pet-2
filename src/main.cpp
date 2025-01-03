#include "raylib.h"
#define SCREEN_WIDTH 650
#define SCREEN_HEIGHT 450

int main() {
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Slime Pet 2");

    Texture2D background = LoadTexture("..\\resources\\background.png");
    Texture2D slime = LoadTexture("..\\resources\\slime.png");

    SetTargetFPS(60);

    while(!WindowShouldClose()) {

        BeginDrawing();
        
        ClearBackground(WHITE);

        DrawTextureEx(background, (Vector2){ 0,0 }, 0.0f, 1.25f, WHITE);
        DrawTextureEx(slime, (Vector2){ 225,260 }, 0.0f, 0.30f, WHITE);

        EndDrawing();
    }

    UnloadTexture(background);

    CloseWindow();

    return 0;
}