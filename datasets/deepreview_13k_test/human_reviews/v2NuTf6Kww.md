# Network-based Active Inference for Adaptive and Cost-efficient Real-World Applications: PV Panel Inspection

- Decision: Reject
- Scores: 3, 1, 3, 3, 5, 5

## Abstract
This paper introduces Network-based Active Inference (NetAIF), a novel framework that integrates random attractor dynamics and the Free Energy Principle (FEP) to improve trajectory generation and control in robotics. NetAIF optimizes the intrinsic dynamics of neural networks, enabling robots to quickly adapt to dynamic and complex real-world environments with minimal computational resources and without the need for extensive pre-training. Unlike traditional learning methods that rely on large datasets and prolonged training periods, NetAIF offers a more efficient alternative. 

In real-world scenarios, such as Photovoltaic (PV) panel inspections, NetAIF demonstrates its ability to execute dynamic tasks with both high efficiency and robustness. The system excels in unpredictable environments while maintaining a low computational footprint. These capabilities make NetAIF a promising solution for industrial applications, offering cost-effective, adaptive robotic systems that can reduce operational expenses and enhance performance, particularly in sectors like energy, where adaptability and precision are crucial.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes NetAIF, a network-based adaptive inference framework, based on random attractor dynamics and Free Energy Principles (FEP), to improve adaptive control problems in robotic systems, and PV panel inspection. The experimental results show that NetAIF performs well on a PV panel inspection and a robotic tasks.

### Strengths
- The NetAIF framework, especially the application of random pullback attractor to it is interesting

### Weaknesses
- The introduction contains several statements and justifications without clear evidence or relevant citation.
- The number of references used in this study is low (only 21), several of which are not peer-reviewed.
- There is a rich body of literature that supports using (deep)RL for similar applications. The application of these approaches is not studied in detail. 
- I expected the authors to use SOTA (deep)RL and AIF approaches as baselines for comparison with NetAIF. Therefore, the experiment section is limited
- The paper lacks adequate background and theory about different components of the method such as AIF, FEP, RDS, and random attractor dynamics.
- The equation numbers are missing
- Section 2 lacks effective connections between its subsections, which results in disjointed and potentially misleading descriptions. This section should be thoroughly revised to improve readability and flow. Additionally, the relationship between the equations and Algorithm 1 is unclear.

### Questions
- In section 1.3, what is the definition of "surprise"?
- It is stated in Section 1.3 that DRL requires "fixed environments", which I believe is not true. Could you please clarify this?
- The equation in page "v" is vague

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper proposes Network-based Active Inference (NetAIF), a framework for trajectory generation and control in robotics. NetAIF integrates random attractor dynamics and the Free Energy Principle (FEP) to create a system that can adapt in real-time with low computational requirements. The authors focus on a practical application in PV panel inspections, demonstrating the system's efficiency, adaptability, and robustness. Evaluation is performed in a simulated Mujoco environment, and on a very simple task on a real robot.

### Strengths
- If verified thoroughly, the reduced computational requirements and real-time capabilities are promising.
- The method is designed for practical applications, which is nice.

### Weaknesses
- The implementation details are not very clear; from what I understand, the method does not seem particularly novel.

- Experimental Validation: The evaluation is limited to simulations and controlled lab conditions, which makes the results not very convincing. In particular, no baseline is provided.

- Figures 1 and 2 are not particularly informative, nor are their captions (e.g., for figure 1, "parameters that determine the network
structure such as number of layers, strides were determined through hyper parameter search").
- Table 4 seems overkill to report the results; the values would be more appropriate just mentioned in the text (as they are) and in the caption of figure 11.

- Minor: is the template correct? This is the only one among the ICLR papers I reviewed that used roman numerals for the page numbers.
- Minor: reporting network sizes in bytes is not very useful, and it's the first time I see it in a paper. Reporting the number of parameters is better.

- Possibly major: The authors cite a paper from the same group in concurrent submission to ICLR ( https://openreview.net/pdf?id=Hm7RYDspQP );  the two papers seem to have major overlap (including using many of the same figures and whole sections / parts of the text). It feels like the authors have tried to write two papers on the same method, splitting evaluations and applications.

### Questions
Can the authors please elaborate on the differences between this paper and the connected one?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents "Network-based Active Inference" (NetAIF), a novel framework for trajectory generation and control in robotics. The main novelty is replacing traditional activation functions with a discrete weight-assigning mechanism, especially for a system focused on achieving and maintaining stability within a NESS framework. The authors mainly focus on a photovoltaic panel inspection task, where a robot arm needs to reach a pre-determined distance from a panel, perpendicular to the panel's surface. The experiments evaluate error and planning time of the system both in simulation and on a real robot arm.

### Strengths
- The authors propose a novel robot control algorithm, and evaluate both in simulation and on a real robot arm.

### Weaknesses
- The paper focuses on the particular task of PV panel inspection in title and abstract. However, the actual task considered is controlling a robotic arm to a particular end-effector pose and orientation. I would think there are many other approaches to do PV panel inspection, and wouldn't necessarily require a robot arm (e.g. using a drone for instance). Also the actual "visual inspection" is not addressed. 

- The introduction discusses deep RL systems, but the paper does no comparison against any of those, but refers to another paper in the conclusion.

- The methodology section lacks detail, making it challenging to reproduce the work. Comparative analysis with traditional control methods in particular for visual servoing, which are well-established for inspection tasks, is also absent.

- The paper lacks a formal proof of system stability. To verify stability, the authors might consider using Lyapunov’s stability criteria. Identifying a well-defined Lyapunov function could reveal whether trajectories converge to an attractor, A(ω), suggesting stability.

### Questions
- What do you mean with "Unlike DRL, which requires fixed environments,". DRL methods can generalize quite well to unstructured unseen environments, see for instance https://arxiv.org/abs/2109.11978, https://arxiv.org/pdf/2010.11251

- The paper does not address how the model would adapt to obstacles in the environment. How does the current approach account for or avoid collisions?

- The statement “the random attractor dynamically explores within the constraints set by the control law” raises some questions:
  - How are these constraints practically defined?
  - What control law ensure that exploration remains controlled and the robot behaves predictably during this process?

- The pseudo algorithm suggests that prediction errors are minimized by randomly sampling new weights, with updates only occurring if the input surpasses a certain threshold. A few points to clarify:
  - How is this threshold determined?
  - Why is this threshold-based sampling considered an optimal method for weight updates?
  - What does it mean to reset a weight? Is it reset to a default value? If so, which value?

 - “The joint pose was directly fed into the system, and the attractor calculated waypoints for a smooth and efficient trajectory to the specified pose,”:
   - What specifically is the simple control law—is it a linear law?
   - How are waypoints computed? Is it a linear interpolation between current and target joint angles?
   - Why is there not a single goal-based attractor, and does the choice affect stability?

- The text states that “noise affecting the system at time t is related to past noise.” Does this formulation assume a colored noise model?

- Based on Table I, the robotic arm with 6 DOF has a position accuracy of 14 mm from a fixed base. While this may suffice for inspecting large panels, it is insufficient for precision tasks, like assembly, which require sub-millimeter accuracy.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper introduces NetAIF, a method that integrates random attractor dynamics and the Free Energy Principle (FEP) to improve trajectory generation and control in robotics. The paper shows the performance of NetAIF in applications of PV Inspection.

### Strengths
This paper proposes an alternative to reinforcement learning by adopting the Active Inference framework from cognitive neuroscience, in which perception, action, and learning are obtained through the minimization of variational free energy.

### Weaknesses
Overall, the paper is not well-written and hard to follow. It gives a superficial idea without going through technical details. I do not understand the mathematics behind NetAIF from this paper. More explicit mathematical equations/formulas should be written: what are the explicit formulas of (variational) Free Energy and surprise? What is the structure of networks? Are they multilayer perceptions? What are the parameters and how are they being updated? how are the explicit feedback loops sent to the previous layers?

The algorithm 1 is not clearly explained and hard to reproduce. Please elaborate more what do each variable represents and how are they obtained/calculated.

The algorithm 1 used “desired state” which means it required the ground truth of optimal trajectory. Would this not be equivalent to having a reward or a set of demonstrations of experts in Deep reinforcement learning?

Experiments lack benchmarks and comparisons with DRL methods. It is not clear whether the results are good. Are PRM and Hybrid RRT-PRM tested in this experiment?

It is also not clear how your work is different from “Deep active inference as variational policy gradients (Millidge, 2020)” and “Deep active inference (”K. Ueltzhoffer, 2018”)

### Questions
see questions in weaknesses

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Network-based Active Inference (NetAIF) as a  novel framework that leverages the Free Energy Principle (FEP) and random attractor dynamics for efficient and adaptive robotics. 
The authors demonstrate their ideas through the use case of a photovoltaic (PV) panel inspection. The authors claim that "NetAIF optimizes the intrinsic dynamics of neural networks and  enables robots to quickly adapt to dynamic and complex real-world environments with minimal computational re- sources and without the need for extensive pre-training. Unlike traditional learning methods that rely on large datasets and prolonged training periods, NetAIF offers a more efficient alternative."
The authors also provide supplementary material which is a slide show of the paper but the experiments with  the 6DOF robotic arm show performance against a few experiments in a lab setting. 

While the work uses a novel approach the paper lacks mathematical rigor and the paper relies very heavily on a few papers forcing the reader to read several papers before extracting value form this work. While citations are needed and not everything needs to be reintroduced the paper should have enough content to stand on its own.   This makes it challenging to evaluate and reproduce the proposed NetAIF framework. Without any formal mathematical treatment, the claims remain at a high level, reducing the work’s overall scientific and practical value. Integrating a comprehensive mathematical model would significantly enhance the credibility and applicability of the approach.  For example, the use of stochastic processes and attractors should be backed by a comprehensive set of equations that demonstrate how these elements interact dynamically within the network. Without this, it is unclear how the system transitions between states, adapts to sensory inputs, and minimizes free energy in a precise manner, additionally , intentionally introducing instability has risks and managing instability should be critical for convergence, the authors mention controlled instabilities and cite a paper but do not provide any formal treatment or plots showing what this looks like.

### Strengths
Novelty:The use of FEP with random attractor dynamics, for real-time control, is innovative. This combination offers an efficient alternative to Deep Reinforcement Learning (DRL) by minimizing computational requirements and avoids extensive pre-training​.
Real-world Applicability: The application of NetAIF in PV panel inspections is practical and addresses significant challenges in the clean energy sector. The use of a physical 6-DoF robotic arm for experiments shows a commitment to real-world validation​
Efficiency: The framework’s low computational footprint and rapid adaptability in dynamic environments are highlighted as key benefits, making it suitable for industries needing quick, cost-effective automation solutions​.

### Weaknesses
Clarity: The explanation of the technical mechanisms, such as the use of random attractors and the free energy landscape, can be complex and may not be accessible to readers unfamiliar with advanced robotics or neural dynamics. Visual aids, while present, could have been better integrated to explain these concepts more intuitively​
Reproducibility: The paper lacks detailed implementation specifics, such as parameter settings and hyperparameters used during the experiments, which limits the reproducibility of results. Clearer code snippets or references to an open-source implementation would enhance its utility for other researchers​.
Strong Assumptions: The paper assumes that the Free Energy Principle (FEP) is applicable to all dynamic robotic systems without extensive empirical validation outside the PV panel inspection case. Additionally, the scalability of the model to other industries or tasks is presumed but not explicitly tested​.
Citations: Citations  lack depth and specificity, especially in sections where novel methods are introduced.
Authors often  rely on generic references rather than recent, more relevant studies directly supporting the claims made in the paper.
Some citations are self-referential, reducing the overall credibility.  The paper would benefit from a more thorough literature review, inclusion of detailed empirical comparisons from other studies, and references to supplementary or reproducible materials that validate the methods described.
Mathematical rigor: While the work uses a novel approach the paper lacks mathematical rigor. This makes it challenging to evaluate and reproduce the proposed NetAIF framework. Without any formal mathematical treatment, the claims remain at a high level, reducing the work’s overall scientific and practical value.

### Questions
Grammar and sentence structure : the paper could use a read through and improve upon sentence structure and layout, also several typos, omissions could be rectified
ex. Active Inference (AIF) = Active Inference Framework 
In my opinion, given the complexity of the proposed solution the paper could benefit from a more rigorous mathematical treatment.While the work uses a novel approach the paper lacks mathematical rigor and this paper relies very heavily on published work forcing the reader to read several papers before extracting value from this work. While citations are needed and not everything needs to be reintroduced, the paper should have enough content to stand on its own.   
Mathematical Model Integration: can the authors incorporate mathematical models demonstrating how NetAIF functions in practice ? This could involve equations showing how the network computes trajectories, adjusts weights, or minimizes prediction errors dynamically.
Formal Optimization Framework: Strongly suggest that authors introduce a formal optimization framework to enhance enhance the credibility of claims regarding efficiency and adaptability. For instance, showing how free energy is minimized using a variational approach or Bayesian inference would connect the theoretical claims with a concrete mathematical foundation.
Sensitivity Analysis and Stability Proofs: This is another weakness of the  paper. Suggest authors to include a mathematical analysis of system stability and sensitivity to changes in parameters or inputs. This would validate the robustness of NetAIF and its applicability to real-world scenarios beyond the initial PV panel inspection.
Stability analysis: it would be very beneficial to see a formal treatment on the intentional use of controlled instability and/or some plots in that regard.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
By integrating active inference and neural network learning schemes, this paper presents a novel control framework, aiming to adapt to an unknown dynamical environment, without pre-training and extensive computations. The focused topic is important considering the shortcomings of traditional deep reinforcement learning. Several numerical simulations and experiments are conducted to demonstrate the proposed control strategy. Although some initial valuable results have been provided in this paper, there are still many important improvements that need to be considered, including clear presentations, solid theorem, and extensive comparisons.

### Strengths
The scheme of interrogating active inference and neural network.
The experimental demonstrations.

### Weaknesses
1. **Experimental comparisons** are lacking in this paper. The authors claim the proposed method has robust and lightweight advantages, in comparison with DRL, while there are no compared results quantitatively. Maybe some of the results are mentioned in the companion paper, but this paper needs to be self-contended. Moreover, the proposed strategy can avoid the traditional planning module and some feedback scheme is integrated into the proposed strategy. It is curious to see how the proposed method compares with the traditional approach (planning + feedback control or MPC).

2. Improve the presentation quality. The used symbols in this paper are unfamiliar and lack illustrations. The symbols employed in Fig 3 need to be illustrated, otherwise, the purpose of intuitional expression will be lost. 

3. The key idea of the Net AIF is to introduce the controlled instabilities by random attractors, while the whole system is within the safety region. More rigid convergence or stability analyses are needed.

4. Experimental details need to be added. For example, the accurately measured states, noised states, and unknown states in Section 3.1 should be clearly provided.

5. An ablation study is needed. It seems that the proposed framework consists of several parts. The functionality of each part needs to be quantified. For example, the efficiency of the replaced discrete weight-assigning mechanism is unknown. 

6. The limitations should be analyzed finally. It is highly recommended to provide the source code.

### Questions
1. In Algorithm 1, what is the difference between Hidden_signals_prev and Hidden signals in lines 12-13?

2. Is there some drawbacks (prices) to induce the random attractors?

3. The function of feedback is still a bit confusing. If its implicit structure can be described in Fig 1?

### Soundness
2

### Presentation
2

### Contribution
2
