#include <raylib.h>

int main() {
    const int screenWidth = 800;
    const int screenHeight = 600;

    InitWindow(screenWidth, screenHeight, "Game View");

    Camera3D camera = { 0 };
    camera.position = (Vector3){ 0.0f, 10.0f, 10.0f };
    camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };
    camera.fovy = 45.0f;
    camera.projection = CAMERA_PERSPECTIVE;

    SetCameraMode(camera, CAMERA_FREE);

    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        UpdateCamera(&camera);

        BeginDrawing();
            ClearBackground(RAYWHITE);
            BeginMode3D(camera);

                DrawCube((Vector3){ 0.0f, 0.0f, 0.0f }, 2.0f, 2.0f, 2.0f, RED);
                DrawGrid(10, 1.0f);

            EndMode3D();
        EndDrawing();
    }

    CloseWindow();

    return 0;
}
