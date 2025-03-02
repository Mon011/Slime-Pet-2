#include "SceneSystem.hpp"

void SceneSystem::Load()
{
    scenes.push_back(std::make_unique<MenuScene>());

    for (auto &scene : scenes)
    {
        scene->Load();
    }
}

void SceneSystem::Update()
{
    for (auto &scene : scenes)
    {
        scene->Render();
    }
}