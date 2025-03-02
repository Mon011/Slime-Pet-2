#include "MenuScene.hpp"

void MenuScene::Load()
{
    background = LoadTexture("background.png");
    banner = LoadTexture("banner.png");
}

void MenuScene::Render()
{
    DrawTexture(background, 0, 0, WHITE);
    DrawTexture(banner, 250, 0, WHITE);

    DrawRectangle(476, 346, 288, 78, BLACK);
    DrawRectangle(480, 350, 280, 70, GRAY);

    DrawText("START", 536, 364, 48, BLACK);

    DrawRectangle(476, 436, 288, 78, BLACK);
    DrawRectangle(480, 440, 280, 70, GRAY);

    DrawText("EXIT", 556, 454, 48, BLACK);

    DrawRectangle(476, 526, 288, 78, BLACK);
    DrawRectangle(480, 530, 280, 70, GRAY);

    DrawText("CREDITS", 510, 544, 48, BLACK);
}