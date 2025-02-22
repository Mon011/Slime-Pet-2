
class State {
public:
    GameState gameState;
    SceneType sceneType;

    State() {
        gameState = PLAYING;
        sceneType = MENU;
    }
};


enum GameState {
    PLAYING,
    PAUSED
};

enum SceneType {
    MENU,
    DUMMY
};
