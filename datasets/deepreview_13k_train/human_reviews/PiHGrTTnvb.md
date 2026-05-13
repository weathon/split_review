# Closed-loop Diffusion Control of Complex Physical Systems

- Decision: Accept
- Scores: 8, 10, 3

## Abstract
The control problems of complex physical systems have broad applications in science and engineering.  Previous studies have shown that generative control methods based on diffusion models offer significant advantages for solving these problems. However, existing generative control approaches face challenges in both performance and efficiency when extended to the closed-loop setting, which is essential for effective control. In this paper, we propose an efficient Closed-Loop Diffusion method for Physical systems Control (CL-DiffPhyCon). By employing an asynchronous denoising framework for different physical time steps, CL-DiffPhyCon generates control signals conditioned on real-time feedback from the system with significantly reduced computational cost during sampling. Additionally, the control process could be further accelerated by incorporating fast sampling techniques, such as DDIM. We evaluate CL-DiffPhyCon on two tasks: 1D Burgers' equation control and 2D incompressible fluid control. The results demonstrate that CL-DiffPhyCon achieves superior control performance with significant improvements in sampling efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript addresses a closed-loop diffusion control problem of complex physical systems. The proposed CL-DiffPhyCon (Wei et al., 2024) extends the work of DiffPhyCon (Wei et al., 2024).

### Strengths
One advantage is to improve the computation efficiency, which is achieved by an asynchronous denoising framework. This aspect is validated using numerical simulations. Overall, this manuscript is well-written and organized.

### Weaknesses
There are some technical limitations, including noise-free inputs, input constraints, and numerical validations by using full in-domain control and observation.

Detailed comments are summarized below:

1. How restrictive is the consideration of noise-free control? There are many noise issues arising from complex engineering systems and applications. Can the proposed method be extended to account for plant, control, and measurement noise?

2. Another important aspect associated with complex and practical physical systems is physical constraints. For example, physical control actions are implemented via actuators which often have upper and lower limits. That is one major reason model predictive control is useful. Can the proposed method handle physical constraints associated with control actions?

3.  From Figure 2 and the limitation mentioned in the appendix, the algorithm is trained offline. In that case, it is not clear how the control is designed and employed in a real environment, as controllers are typically designed and used in practice in an interactive manner. In Figure 2, the ending time instance is T, can it be changed to T+1, as a bigger loop, to make it useful in an online/interactive manner?

4. In both examples, the controls are defined as a spatiotemporal function in the PDE model, which is too ideal to be implemented in a realistic system. For PDE system control, typically, the control is implemented as a temporal function. The corresponding actuator is located in the boundary or a small part of the entire spatial domain. It would be interesting to see the results in these more realistic settings by using the proposed method.

5. In the Burgers’ equation example, there is no difference between the full observation and partial observation cases, because the latter case only observes and controls two parts of the entire domain. In the case considered in the manuscript, one can simply treat each observed sub-domain as a total entire domain and apply the algorithm on the PDE with new spatial coordinates/ranges/boundary conditions. Partial observation typically refers to the case using partial observation to control the entire domain. The control performance results of the unobserved state should be added to fully demonstrate the effectiveness of the proposed algorithm. Similarly. practical applications often have sensors installed in the boundary of PDE systems. It would be good to also add results by using boundary observation data.

6. The limitations of the proposed method should be moved to the conclusion section for better readability.

### Questions
Detailed comments are summarized below:

1. How restrictive is the consideration of noise-free control? There are many noise issues arising from complex engineering systems and applications. Can the proposed method be extended to account for plant, control, and measurement noise? 

2. Another important aspect associated with complex and practical physical systems is physical constraints. For example, physical control actions are implemented via actuators which often have upper and lower limits. That is one major reason model predictive control is useful. Can the proposed method handle physical constraints associated with control actions? 

3.  From Figure 2 and the limitation mentioned in the appendix, the algorithm is trained offline. In that case, it is not clear how the control is designed and employed in a real environment, as controllers are typically designed and used in practice in an interactive manner. In Figure 2, the ending time instance is T, can it be changed to T+1, as a bigger loop, to make it useful in an online/interactive manner? 

4. In both examples, the controls are defined as a spatiotemporal function in the PDE model, which is too ideal to be implemented in a realistic system. For PDE system control, typically, the control is implemented as a temporal function. The corresponding actuator is located in the boundary or a small part of the entire spatial domain. It would be interesting to see the results in these more realistic settings by using the proposed method. 

5. In the Burgers’ equation example, there is no difference between the full observation and partial observation cases, because the latter case only observes and controls two parts of the entire domain. In the case considered in the manuscript, one can simply treat each observed sub-domain as a total entire domain and apply the algorithm on the PDE with new spatial coordinates/ranges/boundary conditions. Partial observation typically refers to the case using partial observation to control the entire domain. The control performance results of the unobserved state should be added to fully demonstrate the effectiveness of the proposed algorithm. Similarly. practical applications often have sensors installed in the boundary of PDE systems. It would be good to also add results by using boundary observation data. 

6. The limitations of the proposed method should be moved to the conclusion section for better readability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper proposes a novel method for using diffusion policies for closed loop control that speeds up the generation of a control sequence of a length up to a chosen horizon by avoiding full denoising of the latter steps in the sequence, as they will likely not be executed by a receding horizon controller. The proposed method demonstrates superior performance in terms of achieving control objectives, due to closed loop control using a diffusion policy, with computation time much shorter than other diffusion policy baseline controllers.

### Strengths
The main strength of the proposed method is the idea to save computation by not fully denoising the latter steps of the control sequence, with the understanding that in receding horizon control, the controls for those latter stages will likely not be used, as new state observations will appear in the meantime and the control sequence will be replanned. This idea addresses one of the main shortcomings of controllers based on diffusion policies - the very long process of denoising during sampling, which is currently a major obstacle to the wider adoption of diffusion policies that have shown considerable advantages with respect to more traditional behavior cloning schemes.

### Weaknesses
I believe the proposed method is excellent and clearly applicable to very difficult control problems involving PDEs. However, most control problems are not of this kind. Why not show the performance on a simpler control problem with a handful of variables, hopefully not requiring high-end GPUs? This could potentially increase the applicability and appeal of the method significantly.

Some minor typos:

P. 3, L. 112: "It" -> "They"
P. 3, L. 140: "has" -> "have"
P. 7, L. 376: "well well" -> "perform well"?
P. 10, L. 539: "done" -> "drone"?
P. 19, L. 1009: "128 grids" -> "128 cells"

### Questions
I am not quite sure why the proposed method achieves a better control objective than DiffPhyCon-1 - isn't the latter replanning at each control step by means of full denoising, thus as closed-loop as the proposed method? Can the authors clarify this? 

The planning horizon for the two control tasks is fixed. Why exactly to these lengths? What happens if full denoising is done over shorter horizons, replanning at each time step, using DiffPhyCon-1?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the problem of designing feedback control algorithms using diffusion techniques. Differently from open-loop control strategies, which compute a pre-determined control sequence that is applied to a system over time, closed-loop methods use information about the state of the system to tune the control inputs to compensate for deviations of the system trajectories from the predicted one, due to unmodelled dynamics or noise. The paper focuses on the computational complexity of the methods, and it proposes a technique to render closed-loop diffusion-based control computationally efficient.

### Strengths
The overall objective of the paper is interesting and timely: to design closed-loop diffusion-based control algorithms. The issue of computational complexity is important, since diffusion-based methods may work well but require extensive computations, making them difficult to use in feedback settings.

### Weaknesses
The paper is poorly presented, to an extent that makes the contributions unclear and difficult to appreciate. This start with the definition of the problem (where what is known/unknown/available to the designer is unclear, where there is confusion between system and environment, where   the stated problem is inherently open-loop and the feedback structure is not evident), and continues into the description of the proposed method (the synchronous and asynchronous parts are vague and difficult to grasp). Additionally, and importantly, the paper doesn't seem to offer performance guarantees for the proposed method, which makes it difficult to advocate for the proposed method in any practical use.

As a side note, the problem described in equation (1) is inherently an open loop problem, since no structure is imposed on the input w. In fact, the set of open-loop sequences include the set of closed-loop sequences, but the converse may not be true. Since the system dynamics are deterministic, it is also unclear why using a closed-loop strategy would be necessary. Finally, the used notation (w for control inputs and u for the system state) is very unusual and, to the best of my knowledge, never been used in any controls paper.

### Questions
A careful rewriting of the manuscript seems necessary to clarify the problem setting and contribution, and to appreciate the differences between the propose method and the existing ones. A characterization of the performance of the proposed method is necessary, otherwise the  method takes the form of a heuristic that may not be desirable in controls applications.

As a side note, the problem described in equation (1) is inherently an open loop problem, since no structure is imposed on the input w. In fact, the set of open-loop sequences include the set of closed-loop sequences, but the converse may not be true. Since the system dynamics are deterministic, it is also unclear why using a closed-loop strategy would be necessary. Finally, the used notation (w for control inputs and u for the system state) is very unusual and, to the best of my knowledge, never been used in any controls paper.

### Soundness
2

### Presentation
1

### Contribution
2
