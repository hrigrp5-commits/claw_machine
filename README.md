# How Precision Affects User Trust in Teleoperation of a Robot Arm Using Keyboard

A Human-Robot Interaction (HRI) user study from Constructor University, Bremen.

**Authors:** Mariam Machaidze, Amanuel Basaznew Legesse, Anuraag Deshpande, Dan Akai

![Experiment setup](figures/setup.jpg)

## Overview

This study examines how the accuracy and predictability of a robot's movements affect human trust. Participants teleoperated a Franka Emika Panda arm with the keyboard in a "claw machine" style pick-and-place task, moving eight blocks on a 12×18 grid (3 cm cells) to a discard pile.

**Hypothesis (H1):** Accurate and predictable robot movements result in higher perceived trust than inaccurate ones.

## Study Design

Between-group experiment with 21 participants:

| Group | Condition | n |
|-------|-----------|---|
| A | Noisy movements: some commands are randomly turned into diagonal moves | 11 |
| B | Normal movements: the robot executes commands exactly | 10 |

- **Controls:** `W` `A` `S` `D` to move (3 cm steps), `C` to pick up, `Q` to quit
- **Pick sequence:** descend, grip, ascend, move to discard pile, release, return home
- **Software:** ROS, MoveIt!, RViz, ROS bags for logging
- **Measures:** pre-study questionnaire; post-study questionnaire (NASA-TLX, Trust in Automation, Human-Artefact Trust Model; 7-point Likert); task completion time, keystrokes, movement direction and joint states

## Key Findings

- Both groups started with similar attitudes toward automation (no significant pre-study differences).
- Group A (noisy) rated the system significantly lower (p < 0.05) on:
  - correct interpretation of input
  - trust
  - reliability
  - performing its role well
  - satisfaction with their own performance
- Group A rated the system as significantly more **unpredictable**.
- Group A took longer on average to complete the task (247 s vs. 203 s).
- Unpredictable robot behavior lowered trust and led participants to blame themselves for the system's errors.

## Limitations

- Some questionnaire items were unclear to non-robotics participants.
- The noise algorithm may have been too pattern-like to be seen as a real fault.
- Sudden arm movements and proximity to participants were not measured.
- MoveIt!/FCL planning latency (occasional freezes) is a possible confound.

## Repository Contents

```
.
├── HRI_Group_5_Report.pdf   # Full paper
├── figures/                 # Images used in this README
└── README.md
```

## Keywords

Teleoperation, Human-Robot Interaction, Robot Arm, Franka Panda, Trust, Predictability

## Citation

```
Machaidze, M., Legesse, A. B., Deshpande, A., & Akai, D.
How Precision Affects User Trust in Teleoperation of Robot Arm using Keyboard.
Constructor University, Bremen, Germany.
```
