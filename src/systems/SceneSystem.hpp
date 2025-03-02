#pragma once

#include "System.hpp"
#include "../src/scenes/Scene.hpp"
#include "../src/scenes/MenuScene.hpp"

#include "raylib.h"

#include <vector>

class SceneSystem : public System
{
private:
    std::vector<std::unique_ptr<Scene>> scenes;

public:
    void Load() override;

    void Update() override;
};
