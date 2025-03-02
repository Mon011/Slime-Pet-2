#include "raylib.h"
#include "resource_dir.h" // utility header for SearchAndSetResourceDir

#include "../src/systems/System.hpp"
#include "../src/systems/SceneSystem.hpp"
#include <vector>

void GameLoop();

int main()
{
	SetConfigFlags(FLAG_VSYNC_HINT | FLAG_WINDOW_HIGHDPI);
	InitWindow(1280, 720, "Slime Pet 2");
	SearchAndSetResourceDir("resources");

	while (!WindowShouldClose())
	{
		GameLoop();
	}

	CloseWindow();
	return 0;
}

void GameLoop()
{
	std::vector<std::unique_ptr<System>> systems;
	systems.push_back(std::make_unique<SceneSystem>());

	BeginDrawing();
	ClearBackground(WHITE);

	for (auto &system : std::move(systems))
	{
		system->Load();
	}

	for (auto &system : std::move(systems))
	{
		system->Update();
	}

	EndDrawing();
}