#pragma once

#include "raylib.h"
#include "Scene.hpp"

class MenuScene : public Scene
{
private:
    Texture2D background;
    Texture2D banner;

public:
    void Load() override;

    void Render() override;
};