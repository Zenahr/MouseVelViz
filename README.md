# MouseVelViz - Mouse Velocity Visualizer

# Planned

- Add Source Code (needs cleanup first)

# Demonstration

[YouTube Video](https://youtu.be/fcy1u2AIUw0)

# Usage

1. Download the executable [here](https://github.com/Zenahr/MouseVelViz/releases/download/v1.0.0/MouseVelViz.exe).
2. start your game
3. start MouseVelViz
4. In OBS/StreamlabsOBS add a new `window capture source`
5. Add a `Chroma Key` filter with the following settings:

![image](https://user-images.githubusercontent.com/47085752/120556125-5fb7fb80-c3fc-11eb-8992-82aa42cb28ee.png)

6. Add a `Color Correction` filter to change the line color. Here's an example configuration to make the lines appear white

![image](https://user-images.githubusercontent.com/47085752/120556189-72323500-c3fc-11eb-86e4-5f84299bac28.png)

# Pricing

Free of charge. MouseVelViz is a passion project of mine with no commercial intent whatsoever.

# Additional Notes

- MouseVelViz can only be run in `Administrator` mode. This is because of the API it's using under the hood (native Windows System API for `Raw Device Input`).
- Minimizing MouseVelViz will pause the mouse input processing. This means you won't see anything.
- MouseVelViz should work in fullscreened games as well as windowed ones.
