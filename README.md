# MouseVelViz - Mouse Velocity Visualizer

# Demonstration

[YouTube Video](https://youtu.be/fcy1u2AIUw0)

# Usage

1. Download the executable [here]().
2. start your game
3. start MouseVelViz
4. In OBS/StreamlabsOBS add a new `window capture source`
5. Add a `Chroma Key` filter with the following settings:

![]()

6. Add a `Color Correction` filter to change the line color. Here's an example configuration to make the lines appear white

![]()

# Pricing

Free of charge. MouseVelViz is a passion project of mine with no commercial intent whatsoever.

# Additional Notes

- MouseVelViz can only be run in `Administrator` mode. This is because of the API it's using under the hood (native Windows System API for `Raw Device Input`).
- Minimizing MouseVelViz will pause the mouse input processing. This means you won't see anything.
- MouseVelViz should work in fullscreened games as well as windowed ones.
