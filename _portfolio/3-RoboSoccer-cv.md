
---
title: "RoboSoccer Fieldline Detection"
excerpt: "Developed a computer vision software using Python, OpenCV, and ROS for soccer field line detection. Utilizes a point cloud approach for improved accuracy, with 2D points transformed to 3D points in the robot's frame of reference, allowing for definition of field lines with known thickness.<br/><img src='/images/field_lines.png' height='300' width='500' >"
collection: portfolio
---

In \cite{b1}, the authors defined the line to be from point A to point B and used trivial OpenCV line detection to return the two endpoints of the line for detection. However, this approach fails to recognize the width of the field lines when the robot is close. Having this additional information on the thickness of the field lines is beneficial and can provide much more accuracy when it comes to localization. Instead of defining the field lines as point-to-point lines, lines can be represented as a point cloud that is transformed from the camera's perspective. See Figure \ref{fig:rviz}.

Our approach for detecting field lines involves first applying a cover horizon to isolate the field area. Then a thresholding operation will select only the field and ignore all areas that are not on the field. Morphological operations filter out noise around and inside the lines. Then a bitwise operation inverts the image to isolate the lines.

Projection of the point cloud from 2D to 3D space uses the pinhole camera model. See equation 1.
\begin{gather}
 \begin{bmatrix} x \\ y \\ z\end{bmatrix}
 =
 \frac{f}{Z}
  \begin{bmatrix}
  X \\ Y \\ Z
   \end{bmatrix}
\end{gather}


\begin{figure}[htbp]
\centerline{\includegraphics[width=0.5\textwidth]{scattered_points.png}}
\caption{Each point from the field line is transformed to a point cloud situated on the ground plane, image taken using the rviz robot visualizer}
\label{fig:rviz}
\end{figure}

Every 2D point that is detected by the computer vision gets sent into the localization module, which using the transformation of the camera, returns a list of 3D points $\{x_i, y_i\}$. These points represent coordinates from the robot's frame of reference. The field is defined by a series of lines. The field lines are defined as $\{x_1, y_1\}, \{x_2, y_2\}$ with known line thickness $d = 0.025$. Vertical lines have a constraint where $x_1 = x_2$ or $y_1 = y_2$. 

#### Field lines detected
<p align="center">
<img src="/images/field_lines.png" width="600"/>
</p>
