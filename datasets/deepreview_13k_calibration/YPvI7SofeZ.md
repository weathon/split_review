# Scaleable Quantum Control via Physics Constrained Reinforcement Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5

## Abstract
Quantum optimal control is concerned with the realisation of desired dynamics in quantum systems, serving as a linchpin for advancing quantum technologies and fundamental research. 
Analytic approaches and standard optimisation algorithms do not yield satisfactory solutions for large quantum systems, and especially not for real world quantum systems which are open and noisy. 
We devise a physics-informed Reinforcement Learning (RL) algorithm that restricts the space of possible solutions.
We incorporate priors about the desired time scales of the quantum state dynamics -- as well as realistic control signal limitations -- as constraints to the RL algorithm. 
These physics-informed constraints additionally improve computational scalability by facilitating parallel optimisation. 
We evaluate our method on three broadly relevant quantum systems (multi-level $\Lambda$ system, Rydberg atom and superconducting transmon) and incorporate real-world complications, arising from dissipation and control signal perturbations. 
We achieve both higher fidelities -- which exceed 0.999 across all systems --  and better robustness to time-dependent perturbations and experimental imperfections than previous methods. 
Lastly, we demonstrate that incorporating multi-step feedback can yield solutions robust even to strong perturbations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Contributes in the field of optimal quantum state control, where the implementation of optimal external signals to quantum systems is difficult for real and noisy systems. The key idea is the use of physical information about the quantum state dynamics as priors to help the RL agent as constrains. The algorithm then learns a control policy that maximizes the fidelity of the quantum control task by reducing/removing control signals which result in overly fast quantum state dynamics, which helps with maintaining a better controllable system state. The approach is tested on three well known problems in the control literature and shown empirically to achieve higher fidelities than a set of baseline algorithms and robustness w.r.t. to state perturbations.

### Strengths
Three well motivated application examples. Short but good baseline study in table 1, with good statistical averages of 32 random seeds. Very clearly written, well referenced, brief but concise descriptions which were mostly understandable even from an outside perspective. Results appear sound and significant from what I understand. I think this is a generally solid paper with a sound contribution.

### Weaknesses
- A lot of use of quite specific jargon, which makes it harder to follow and otherwise very clearly written paper.

- The section on multi-step RL is very short and by only referencing results in the appendix, not self-contained material of this paper. The introduction (L 84) claims an “investigation to address larger levels of system noise” which is only pointed to / contained in the appendix.

- RL ‘framework’ is a very broad claim, a physical reward shaping with (as I understand) out-of-bound-step constraints may be effective as application to quantum state control, but is - in the context of RL and QRL - not very novel.

---
Minor Notes:

- Fig 1. Axis labels should be bigger. Split positioning of legend is a bit confusing.

- The terms state populations, rise time etc. could be better explained.

- L163 Typo Two dots after etc.

- L 202 Typo quantu[m] system, see [Section] 3.2.1)

- L 350 Typo That the learned pulses [are] physically

- L 350 Typo e.g.[,]

- Inconsistent use of references (eq / equations), (Fig. / Figure), (App. / Appendix)

- Inconsistent use of cf. inline and (cf. in brackets)

### Questions
- Is there a reason that the multi-step return does not include a discount factor as is usually the case?
- L. 260 What is a baseline ‘blackman envelope’?
- What differentiates the physically feasible control signals in Tab. 1?
- RL in general is known to be quite sensitive against reward shaping attempts (resulting in reward hacking instead), and some of the reward terms in Eq 6 seem just added for good measure. Was an ablation study done on these terms and components (ReLU, blackman envelope, the smoothness estimator etc.)?
- Although PPO is a solid choice in many RL applications, since the action-space is very simple, small and discrete, DQN or even simpler policy gradient methods may already be sufficient. Have you perhaps tested any ablation / combination of other RL approaches and could elaborate on their comparative performance?

---
All questions have been insightfully addressed by the authors in the rebuttal. As a result the confidence score has been updated from 3 -> 4.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper frames quantum control as a bandit problem and applies reinforcement learning to address it. It introduces a physical constraint as a reward term to penalize the required number of quantum simulation steps. The paper verifies the effectiveness of the approach on three problems, additionally showcasing the potential advantage of multi-step RL.

### Strengths
- The paper is well-written and easy-to-follow.  
- It is sound to take advantage of RL's search capability to solve optimization problems. 
- The implementation of GPU-accelerated parallel simulation is promising and useful. 
- The experiment is comprehensive and informative.

### Weaknesses
 - The contribution should be clarified and clear. It seems that the physical constraint is part of reward shaping, making the primary contribution of the paper the development of GPU-based simulation and the design of reward functions.
- The paper lacks theoretical results, though this is understandable given its focus on an RL application; therefore, this is only a minor weakness.

### Questions
- What is the MDP formulation in the multi-step RL case?
- Could the authors elaborate further on the comparison between multi-step RL and bandit approaches, and explain why multi-step RL provides a performance advantage?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a scalable quantum control framework utilizing physics-informed reinforcement learning (RL) to address the challenge of optimizing control signals for complex quantum systems. The authors devise an RL algorithm that incorporates physical constraints to restrict the solution space, focusing on desired time scales of quantum state dynamics and realistic control signal limitations.  The method is evaluated on three quantum systems—multi-level Λ systems, Rydberg atoms, and superconducting transmons—demonstrating higher fidelities and robustness to perturbations compared to previous methods.

### Strengths
- This manuscript introduces a novel framework that combines physics-informed constraints with reinforcement learning for quantum control. The use of physics-based constraints not only enhances solution quality but also ensures that the control signals are physically realistic and experimentally feasible.
- The paper provides a thorough evaluation of the method across different quantum systems and under various conditions, which strengthens the credibility of the results.

### Weaknesses
The main concern is that I do not consider ICLR the appropriate venue for this paper, as it does not provide the necessary background information for readers unfamiliar with quantum control. It would be more suitable for the paper to be published in a physics journal rather than an AI conference. Even though as a paper for physics journal, it still lacks the self-contained nature and clarity necessary for a comprehensive understanding by the readers. For instance, the experiments presented in this paper appear to be related  to a pre-existing methodology known as 'STIRAP'. However, the manuscript fails to provide adequate explanation or details regarding this method, which could leave readers without a clear understanding of its role and significance in the study. 

Furthermore, I am not convinced that the results presented in this paper sufficiently substantiate the authors' claims. Specifically, the authors claim "the applied constrained not only improves computational efficiency but also promotes the selection of more physically realistic control signals." However, the manuscript does not offer adequate numerical or theoretical evidence to validate this assertion. The paper lacks a rigorous analysis demonstrating how the physics-informed constraints directly translate to improved computational efficiency or more realistic control signals. For instance, the paper does not provide a clear definition of 'physical realism' in the context of control signals, nor does it offer a quantitative measure to assess this. The claim that the constraints lead to more realistic signals is not backed by a comparison with unconstrained RL methods or a theoretical justification of how the constraints enforce physical plausibility. The paper also does not sufficiently analyze the impact of the chosen constraints on the exploration-exploitation trade-off in the RL algorithm, which is crucial for understanding the method's performance.

### Questions
Please see "Weaknesses" above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides an approach to RL for open quantum control, evaluated on 3 quantum systems with a focus on hardware realistic control. They demonstrate SotA fidelity using this approach.

### Strengths
- The promise of open source code is good and beneficial to reproducibility
- More realistic quantum control is an important research direction
- The superconducting results are especially compelling

### Weaknesses
 - Minor mistakes, e.g. “quantu system”
- Figure 1 is the main selling point, but could be improved. There is an extra large space under the figure caption, I assume from latex formatting. The labels should be consistent, it’s called “infidelity” in the caption, but “fidelity” in the plot (obviously these are trivially related quantities, but just keeping the labeling consistent is worthwhile). I’m not sold on the one axis being log and the other y axis being non-log, it doesn’t make things super clear. Especially given that the log plot is basically just line going to small value (and it doesn’t bounce around a lot at these small values to make showing them super important). Also, Figure 1 would benefit from putting the legends in the same text block. All in all, I think there is a lot of room to make this a more compelling “Figure 1”
- The RL aspect of this paper is sometimes unclear. Reading from the beginning seems to indicate that bandit based algorithms would be the focus (but there isn’t much mention of bandit literature or the algorithms at play there). However, in 5.0.1, PPO is mentioned which doesn’t seem to come up again until 5.4. Clarifying this for the reader would be beneficial. Perhaps even explicitly writing out an algorithm block (could be in the appendix).
- Footnotes 2, 3 seem to be broken in Table 1
- Table 1 provides means, but no uncertainty/range on these estimates
- Figure 9 seems lower resolution/DPI than the other figures
- Two difficulties are mentioned in sec 4.1, which largely reduce down to 1) quantum simulation is hard and 2) RL is hard. While 2) is addressed through parallelism, 1) seems like a more important hurdle to this work and doesn’t seem to be addressed.
- Execution of the new superconducting pulses on real devices would be very interesting (but I recognize this may not be a realistic request)
- Ablation studies are lacking on the RL side (PPO vs other algorithms, parameters of PPO, etc.)

### Questions
- If the assumption is made of a white box simulator (here being an ODE), couldn’t one just directly optimize under constraints by differentiating through the solver? What’s the advantage of RL in cases of quantum control where we have perfect access to a differentiable simulator?

- To be clear, the RL agent (be it bandit or PPO) sees the entire quantum density matrix (“which is given as the density matrix”)?

### Soundness
2

### Presentation
2

### Contribution
2
