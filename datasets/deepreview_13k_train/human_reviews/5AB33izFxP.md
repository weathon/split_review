# Simultaneous Online System Identification and Control using Composite Adaptive Lyapunov-Based Deep Neural Networks

- Decision: Reject
- Scores: 8, 5, 6, 8

## Abstract
Although deep neural network (DNN)-based controllers are popularly used to control uncertain nonlinear dynamic systems, most results use DNNs that are pretrained offline and the corresponding controller is implemented post-training. Recent advancements in adaptive control have developed controllers with Lyapunov-based update laws (i.e., control and update laws derived from a Lyapunov-based stability analysis) for updating the DNN weights online to ensure the system states track a desired trajectory. However, the update laws are based on the tracking error, and offer guarantees on only the tracking error convergence, without providing any guarantees on system identification. This paper provides the first result on simultaneous online system identification and trajectory tracking control of nonlinear systems using adaptive updates for all layers of the DNN. A combined Lyapunov-based stability analysis is provided, which guarantees that the tracking error, state-derivative estimation error, and DNN weight estimation errors are uniformly ultimately bounded. Under the persistence of excitation (PE) condition, the tracking and weight estimation errors are shown to exponentially converge to a neighborhood of the origin, where the rate of convergence and the size of this neighborhood depends on the gains and a factor quantifying PE, thus achieving system identification and enhanced trajectory tracking performance. As an outcome of the system identification, the DNN model can be propagated forward to predict and compensate for the uncertainty in dynamics under intermittent loss of state feedback. Comparative simulation results are provided on a two-link manipulator system and an unmanned underwater vehicle system with intermittent loss of state feedback, where the developed method yields significant performance improvement compared to baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper is introducing an adaptive DNN-based controller. Standard adaptive DNN-based controllers are based on Lyapunov-based analysis and allow updates on the last layers of the NNs only. They only use the tracking error as a metric to indicate when adaptation is needed, and only provide guarantees on the tracking error convergence. This paper introduces a dual (composite) method, for continuous system identification combined with trajectory tracking, and guarantees that the tracking error, state-derivative estimation error, and DNN weight estimation errors are uniformly ultimately bounded. The last two reflect identifying the dynamics of the system.
The system identification is performed via a dynamic state-derivative estimator and under the assumption of persitence of excitatiton. The controller is evaluated in simulation on a two-link manipulator system and an unmanned underwater vehicle system with intermittent loss of state feedback, and shows improvement compared to baseline methods.

### Strengths
The paper is on a very timely topic, DNN-based control. With the emergence of AI-based approaches, a principled treatment of a learning-based controller is an impactful contribution. Introducing a controller which allows for updates in all layers, in contrast to the state of the art where only thelast layers can be updated, and where system dynamics is not considered explicitely, is a big contribution. 
Given the complexity of the paper, it is very clearly presented. The simulation examples are relevant and not just datasets, but dynamical systems.

### Weaknesses
1. In the simulations, there is only comparison to DNN-based controllers. 
It would highly interesting to see how is the peroformance, compared to more standard controllers used in robotics (for example, MPC-based, or RL-based controllers). I am willing to raise my rating if this is added.



### Questions
1. Shouldn’t there be an assumption for the activation functions to be convex? How do you deal with the nonconvex dependence of the underlying loss function on weights of hidden layers? Is it playing a role?

2. How can input and state constraints be integrated in the proposed approach?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses a methodology for simultaneously performing online system identification for the plant system and adaptation in the feedback control logic. Under some technical assumptions, stability conditions are presented, more specifically, the asymptotic stability of the equilibrium point of the entire feedback control system is ensured.

### Strengths
The simultaneous approach to online system identification and adaptation in the control logic, addressed in this paper, is well-motivated and justified with attractive numerical experiments.  In addition, as claimed by the authors, the convergence analysis for the identification error and control error is novel.

### Weaknesses
Assumptions 1 and 2 are mathematically severe.  While this paper claims its contribution lies in simultaneous system identification and control, Assumption 1 implies that performing system identification can achieve arbitrary control performance (arbitrary system dynamics is realized by u= g^+(r - f(x,\dot{x}))). In this sense, the problem addressed in this paper is not essentially simultaneous.  Specifically, the assumption that the control input can be designed to perfectly cancel the nonlinear dynamics, $f(x, \dot{x})$, and achieve arbitrary dynamics via $u = g^+(r - f(x, \dot{x}))$ severely limits the practical relevance of the proposed method. This assumption essentially bypasses the core challenge of simultaneous identification and control by assuming perfect control authority, which is rarely the case in real-world systems. This assumption reduces the problem to a trivial case where the system dynamics can be arbitrarily shaped, thus eliminating the need for adaptive control to compensate for model uncertainties. Furthermore, there are too many technical assumptions on the modeling accuracy, meaning the existence of \bar{\varepsilon}, \bar{\theta}, etc.

### Questions
Could you relax Assumptions 1 and 2?  In particular, as commented in Weakness, Assumption 1 is mathematically (and practically) severe.  The authors comment that the developed methods can be extended to underactuated systems. However the details of the extension are scarcely explained, and no theoretical analysis is provided.  The reviewer believes that the extension to underactuated cases and its convergence analysis should be the main contribution of this paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provides the first result on simultaneous online system identification and trajectory tracking control of nonlinear systems using adaptive updates for all layers of the DNN. The Lyapunov-based stability analysis is provided, which guarantees that the tracking error, state-derivative estimation error, and DNN weight estimation errors are uniformly ultimately bounded.

### Strengths
This is first application of the Jacobian of the DNN to develop simultaneous online system identification and control. The theoretical content of the paper is good. The literature research is sufficient.

### Weaknesses
The practical application of this method requires high computing resources and is not suitable for personal computers. The presence of measurement noise does not seem to be considered in the two simulation tests, which is unreasonable. Control inputs of two simulations should also be presented. Moreover, the nonlinear dynamics of the selected simulation system is weak.

### Questions
1)	The existence of measurement noise should be considered, which is common in practical engineering; Please provide the control inputs of two simulation tests;
2)	I wonder if this method is effective for highly dynamic systems like quadcopters?
3)	Provide more experimental details, such as control inputs, weights update, and the selected control parameters.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a kind of Lpapunov-based adaptive framework, that can update all layers of DNN. The proposed method can handle nonlinear-in-parameters uncertainties. Moreover, a dynamic state-derivative estimator is utilized to obtain the state-derivative information. Overall, some novel theoretical results are developed in this paper with rigid proofs. The presentation is also clear. However, some drawbacks exist and many improvements can be further considered. There are some inappropriate statements and comparisons. The simulation tests are not enough to show its efficiency. Please refer to below for more details.

### Strengths
1. The main contribution is that a Lpapunov-based adaptive framework is proposed to update **all layers** of DNN.
2. Rigid convergence analysis.
3. Two applied examples, despite only numerical simulations.

### Weaknesses
1. The Abstract is too long, preventing the reader from capturing key points quickly. It is recommended to only highlight the main contributions in the Abstract and technique details can be removed.

2. It is claimed that the tracking, state-derivative, and weight estimation errors can be guaranteed to converge to bounded sets. **The factors that determine the upper bounds** of convergence sets should be provided in the Abstract.

3. The previous work (OConnell, 2022) is compared in the Intro. It is claimed the limitation of the composite adaptive approach used by OConnell, 2022, is the inner-layer weight cannot be online updated. However, the considered case of OConnell, 2022 is different from the one of this paper. OConnell mainly focuses on a composited disturbance, which comes from external disturbance and internal state-related uncertainties. The last layer of DNN is updated online to handle external disturbances, while the inner layers correspond to internal state-related uncertainties, which would not change in application. However, the internal state-related uncertainty is mainly considered in this paper, i.e., $f({x, \dot{x}})$. **The direct comparison with (OConnell, 2022) is inappropriate**.

4. One important problem is only simulation examples are demonstrated in this paper, and no noises exist in the measured states, despite the theorems that seem to be relatively complete. A small upper bound of the convergence set depends on a large gain. However, the gain may enlarge the noises in a real system. Thus, **the effect of the real application is questionable**.

5. In the simulation of two link manipulators, it is recommended to cover the ESO comparison and the composite adaptive method developed in (Slotine and Li, 1989). The gain selection strategy for all comparison methods should be provided to ensure fairness.

### Questions
1. If the proposed framework could be combined with offline learning?  It seems the proposed update strategy only relies on current measurements and has no historical data-mining procedure. It is a kind of traditional adaptive control, instead of modern data-based learning. Maybe a control journal is more applicable to this paper.

2. If the considered uncertainty $f({x, \dot{x}})$ can be extended to the composited disturbance, like $f({x, \dot{x}, d})$, where $d$ denotes the external disturbance. It will be valuable in real applications.

### Soundness
2

### Presentation
2

### Contribution
3
