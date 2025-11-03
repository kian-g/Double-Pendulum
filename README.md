# Double-Pendulum
Play around with these variables:
- `radius1`
- `radius2`
- `angle1`
- `angle2`
- `mass1`
- `mass2`
---
Equations for angle acceleration from [myPhysicsLab.com](https://www.myphysicslab.com/pendulum/double-pendulum-en.html).
- Angle 1 acceleration: $$\theta_1'' = \frac{-g (2m_1 + m_2)\sin\theta_1 - m_2 g \sin(\theta_1 - 2\theta_2) - 2\sin(\theta_1 - \theta_2)m_2((\theta_2'^2 L_2 + \theta_1'^2 L_1 \cos(\theta_1 - \theta_2)))}{L_1(2m_1 + m_2 - m_2 \cos(2\theta_1 - 2\theta_2))}$$
- Angle 2 acceleration: $$\theta_2'' = \frac{2\sin(\theta_1 - \theta_2)\left(\theta_1'^2 L_1 (m_1 + m_2) + g(m_1 + m_2)\cos\theta_1 + \theta_2'^2 L_2 m_2 \cos(\theta_1 - \theta_2)\right)}{L_2(2m_1 + m_2 - m_2 \cos(2\theta_1 - 2\theta_2))}$$

Where $g$=gravity, $m_1$=mass of ball one, $m_2$=mass of ball two, $\theta_1$=angle of connector one, $\theta_2$=angle of connector two, $L_1$=length of connector one, $L_2$=length of connector two.

Implemented as follows: 
```py
 angle1_acceleration = (
    -g * (2 * mass1 + mass2) * sin(angle1)
    - mass2 * g * sin(angle1 - 2 * angle2)
    - 2
    * sin(angle1 - angle2)
    * mass2
    * (
        angle2_velocity**2 * radius2
        + angle1_velocity**2 * radius1 * cos(angle1 - angle2)
    )
) / (radius1 * (2 * mass1 + mass2 - mass2 * cos(2 * angle1 - 2 * angle2)))

angle2_acceleration = (
    (2 * sin(angle1 - angle2))
    * (
        angle1_velocity**2 * radius1 * (mass1 + mass2)
        + g * (mass1 + mass2) * cos(angle1)
        + angle2_velocity**2 * radius2 * mass2 * cos(angle1 - angle2)
    )
) / (radius2 * (2 * mass1 + mass2 - mass2 * cos(2 * angle1 - 2 * angle2)))
```
