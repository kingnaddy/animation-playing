import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Plotly Animation Demo", layout="wide")

st.title("4 Basic Plotly Animations in Streamlit")

animation_choice = st.selectbox(
    "Choose an animation",
    [
        "Rotating 3D Helix",
        "Moving Sine Wave",
        "Bouncing Ball",
        "Waving Flag",
    ],
)

num_frames = 60


def rotating_3d_helix():
    t = np.linspace(0, 8 * np.pi, 200)
    x = np.cos(t)
    y = np.sin(t)
    z = np.linspace(-2, 2, 200)

    frames = []
    for i in range(num_frames):
        angle = 2 * np.pi * i / num_frames
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=x_rot,
                        y=y_rot,
                        z=z,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Rotating 3D Helix",
        scene=dict(
            xaxis=dict(range=[-1.5, 1.5]),
            yaxis=dict(range=[-1.5, 1.5]),
            zaxis=dict(range=[-2.5, 2.5]),
            aspectmode="cube",
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def moving_sine_wave():
    x = np.linspace(0, 4 * np.pi, 300)

    frames = []
    for i in range(num_frames):
        phase = 2 * np.pi * i / num_frames
        y = np.sin(x + phase)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=x,
                        y=y,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=np.sin(x),
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Moving Sine Wave",
        xaxis=dict(range=[0, 4 * np.pi]),
        yaxis=dict(range=[-1.5, 1.5]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def bouncing_ball():
    x_positions = np.linspace(0, 10, num_frames)
    y_positions = np.abs(np.sin(np.linspace(0, 3 * np.pi, num_frames))) * 5

    frames = []
    for i in range(num_frames):
        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=[x_positions[i]],
                        y=[y_positions[i]],
                        mode="markers",
                        marker=dict(size=20),
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=[x_positions[0]],
                y=[y_positions[0]],
                mode="markers",
                marker=dict(size=20),
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Bouncing Ball",
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 6]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 60, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def waving_flag():
    x = np.linspace(0, 4, 60)
    y = np.linspace(0, 2, 35)
    X, Y = np.meshgrid(x, y)

    surface_colors = np.zeros_like(X)
    surface_colors[(Y >= 2 / 3) & (Y < 4 / 3)] = 0.5
    surface_colors[Y >= 4 / 3] = 1.0

    colorscale = [
        [0.0, "red"],
        [0.33, "red"],
        [0.33, "white"],
        [0.66, "white"],
        [0.66, "blue"],
        [1.0, "blue"],
    ]

    frames = []
    for i in range(num_frames):
        phase = 2 * np.pi * i / num_frames

        amplitude = 0.22 * (X / X.max())
        Z = amplitude * np.sin(2 * np.pi * (X / 1.8 - i / num_frames))
        Z += 0.04 * (X / X.max()) * np.sin(4 * np.pi * (X / 1.8 - i / num_frames))

        frames.append(
            go.Frame(
                data=[
                    go.Surface(
                        x=X,
                        y=Y,
                        z=Z,
                        surfacecolor=surface_colors,
                        colorscale=colorscale,
                        cmin=0,
                        cmax=1,
                        showscale=False,
                    ),
                    go.Scatter3d(
                        x=[0, 0],
                        y=[0, 2],
                        z=[0, 0],
                        mode="lines",
                        line=dict(color="gray", width=8),
                    ),
                ],
                name=str(i),
            )
        )

    initial_amplitude = 0.22 * (X / X.max())
    initial_Z = initial_amplitude * np.sin(2 * np.pi * (X / 1.8))
    initial_Z += 0.04 * (X / X.max()) * np.sin(4 * np.pi * (X / 1.8))

    fig = go.Figure(
        data=[
            go.Surface(
                x=X,
                y=Y,
                z=initial_Z,
                surfacecolor=surface_colors,
                colorscale=colorscale,
                cmin=0,
                cmax=1,
                showscale=False,
            ),
            go.Scatter3d(
                x=[0, 0],
                y=[0, 2],
                z=[0, 0],
                mode="lines",
                line=dict(color="gray", width=8),
            ),
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Waving Flag",
        scene=dict(
            xaxis=dict(visible=False, range=[-0.2, 4.2]),
            yaxis=dict(visible=False, range=[-0.2, 2.2]),
            zaxis=dict(visible=False, range=[-0.5, 0.5]),
            aspectratio=dict(x=2.8, y=1.4, z=0.8),
            camera=dict(eye=dict(x=1.6, y=-1.8, z=0.8)),
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 60, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


if animation_choice == "Rotating 3D Helix":
    fig = rotating_3d_helix()
elif animation_choice == "Moving Sine Wave":
    fig = moving_sine_wave()
elif animation_choice == "Bouncing Ball":
    fig = bouncing_ball()
else:
    fig = waving_flag()

st.plotly_chart(fig, use_container_width=True)