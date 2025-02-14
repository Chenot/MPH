# TOWER OF HANOI

The Tower of Hanoi is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can slide onto any rod.
The puzzle begins with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a conical shape.

The objective of the puzzle is to move the entire stack to one of the other rods, obeying the following rules:
- Only one disk may be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
- No disk may be placed on top of a disk that is smaller than it.

This task consists of a training (3 disks) and then 22 trials (4 disks) following the Revised Tower of Hanoi (Welsh et al., 2001).

The "scenario_TowerOfHanoi.csv" file contains:
- Initial positions of the disks (disk1_init,disk2_init,disk3_init,disk4_init)
- Target position (disk1_target,disk2_target,disk3_target,disk4_target)
- Minimal number of moves (n_moves).
- Trials (trial)


# REFERENCES

Welsh, M. C., & Huizinga, M. (2001). The development and preliminary validation of the Tower of Hanoi-Revised. Assessment, 8(2), 167-176.
