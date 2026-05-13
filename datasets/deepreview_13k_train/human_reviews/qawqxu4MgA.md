# Transfer Learning for Control Systems via Neural Simulation Relations

- Decision: Reject
- Scores: 5, 5, 1, 5

## Abstract
Transfer learning is an umbrella term for machine learning approaches that leverage knowledge gained from solving one problem (the source domain) to improve speed, efficiency, and data requirements in solving a different but related problem (the target domain). 
The performance of the transferred model in the target domain is typically measured via some notion of loss function in the target domain. 
This paper focuses on effectively transferring control logic from a source control system to a target control system while providing approximately similar behavioral guarantees in both domains. 
However, in the absence of a complete characterization of behavioral specifications, this problem cannot be captured in terms of loss functions. 
To overcome this challenge, we use (approximate) simulation relations to characterize observational equivalence between the behaviors of two systems.

Simulation relations ensure that the outputs of both systems, equipped with their corresponding controllers, remain close to each other over time, and their closeness can be quantified {\it a priori}. 
By parameterizing simulation relations with neural networks, we introduce the notion of \emph{neural simulation relations}, which provides a data-driven approach to transfer any synthesized controller, regardless of the specification of interest, along with its proof of correctness. 
Compared with prior approaches, our method eliminates the need for a closed-loop mathematical model and specific requirements for both the source and target systems. 
We also introduce validity conditions that, when satisfied, guarantee the closeness of the outputs of two systems equipped with their corresponding controllers, thus eliminating the need for post-facto verification. 
We demonstrate the effectiveness of our approach through case studies involving a vehicle and a double inverted pendulum.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a way of performing transfer learning by quantifying the closeness of the simulated data among two systems and controllers, along with formal guarantees. The method is evaluated in simple vehicle dynamics and double inverted pendulum.

### Strengths
The paper presents the proposed algorithm with rigorous definitions and propositions. The proposed algorithm nicely transforms to reasonable loss functions to train the neural networks $V$ and $\mathcal{K}$. In addition, the author rigorously proved that the resultant neural simulation relation is an $\epsilon$-approximate simulation.

### Weaknesses
1. The experiments, though demonstrated $||y - \hat{y}||<\epsilon$ for the observed trajectories and plotted the trajectories, lacks comparison to relevant baselines. Given that the proposed transfer learning algorithm relies on the discretization of the state space, several transfer learning algorithms mentioned in the original paper's reference, even requiring access to the dynamical model, could be compared with by approximating or learning the system dynamics in local regions. Specifically, methods that leverage local linear approximations or Gaussian Process-based techniques for system identification could provide a strong baseline for comparison, especially given the reliance on state-space discretization inherent in the proposed approach. The absence of such comparisons makes it difficult to assess the practical advantages of the proposed method over existing techniques.
2. The robustness of the trained models with regard to hyper parameters is unclear. An addition of ablation studies on the sensitivity for the hyper parameters could be added. The paper does not explore the impact of varying the neural network architecture (e.g., number of layers, number of neurons per layer), learning rate, batch size, and other optimization parameters on the final performance. Without this, it is difficult to ascertain the reliability and generalizability of the results. Furthermore, the paper does not discuss the sensitivity of the method to the choice of discretization of the state space, which is a crucial hyperparameter that directly affects the performance of the proposed algorithm.

Nit picks: (1) The figure is not properly referenced at line 427. (2) Grammar error in the sentence of the lines 164-165: "To automate the transfer of control strategies [in] different domains". (3) Line 418-409, "We train the neural networks [with] the following parameters. I suggest the authors to thoroughly read the paper to reduce avoidable errors and increase the clarity of the menuscript.

### Questions
I wonder whether the authors have observed failure cases during their experiments. If so, is there a way to measure whether the failure case is due to the difficulty of learning, or due to inherent problems of the given source and target system?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an approach to establish a type of equivalence between two discrete-time, continuous-state dynamical control systems. Formally, an approximate simulation relation is established between the two systems, which relates states from which trajectories remain within a given distance from each other in the output space, assuming that an appropriate sequence of inputs is applied.

The construction of the simulation relation is achieved indirectly, via two functions: a function V that maps a pair of states of the systems to the interval [0,1], and a function K that maps a pair of states of the systems and an input for the first system to a corresponding input of the second system. While V is used to encode related states, K is used to encode related inputs.

The intended application is to relate states in a complex dynamical system to a surrogate model. If successful, a control policy designed for the simpler surrogate model can then be mapped, using K, to a policy for the complex system. 

The basic idea is promising, but there are a number of major issues that remain to be addressed (see weaknesses). In sum, the paper in its current form is not ready for publication.

(review revised after clarification from authors, including an error on my part)
 

Minor remarks:
- the definition of a control policy is missing (required for Def. 3)
- Prob. 4 is not clearly formulated (*whether* … exists)
- loss on page 5 not clear (how is the forall quantifier implemented)
- line 427: Figure ??

### Strengths
The paper proposes to use neural networks to tackle a difficult problem using methods from machine learning.

### Weaknesses
 - V seems to take the role of a simulation function. It is formulated such that it is amenable to learning using a loss function, but it is not immediately clear why this should work better than a direct approximation of a simulation function.
- The use of the cross entropy loss should be better motivated; it's not immediately clear to me why that would be the best choice.
- The experiments are not convincing. The first one is extremely simple, yet seems to require a surprising amount of computational resources. 
- The second experiment constitutes a simplified model of a double pendulum, and it is not immediately clear to me how difficult the problem is. A comparison with a baseline from the literature may help to clarify this issue.
Some of the formal details of the paper are unclear (see minor remarks), and the experiments should be accompanied by more detailed descriptions (training curves, etc.).

### Questions
Why did you use cross-entropy loss? Why map V to [0,1] rather than [0,\infty), like a simulation function?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a data-driven approach that guarantees the behavior transfer from a source control system to a target control system. It also proposes using neural networks to find a simulation relation and its corresponding interface function between these systems, which are called neural simulation relations. The effectiveness of our approach is demonstrated through simple numerical examples of a vehicle and a double-inverted pendulum.

### Strengths
The proposed framework can be understood as addressing the domain gap (between the source and target systems) by transfer learning.

### Weaknesses
1. As stated in paragraphs 1 and 2 of the Introduction, the safety of a real physical system is a critical motivation behind the proposed work. The design aims to render the target system (e.g., a real system) and source system (e.g., a simulator) have similar behavior, such that the control policy of a source system can be deployed to real systems. A critical limitation is that the controllers of source systems must be verifiable safe; otherwise, you cannot guarantee their safety in target systems. Taking the simulator as one example, a typical challenge is the sim-to-real gap, which hinders the safety guarantee of its controller in the real systems. The proposed approach will also face domain. How can you prove your framework can tolerate such gaps to guarantee safety?
2. Figure 1 describes the framework at a high level. Is it online or offline? However, for each case, I think it will be very hard to apply to real safety-critical systems (such as autonomous vehicles and power grids). If the framework is online, what is the inference time of the interface function? Time is also critical for many safety-critical systems; a second can make a difference. If offline, it can be very hard to apply to the systems (e.g., cars) whose operating environments are dynamic. Safety or system behavior will not be guaranteed in a real-time environment, whose dynamics is not captured by the simulator or offline data-driven training.
3. The reviewer cannot agree with some critical statements in the paper, such as, ``The classic control-theoretic approaches require a mathematical model of the system and use search (Prajna & Jadbabaie, 2004) and symbolic exploration (Tabuada, 2009) to analyze and provide guarantees on the resulting system. These symbolic approaches typically face the curse-of-dimensionality where the systems with high dimensions become exceedingly cumber some and time-consuming to design.” I would suggest the authors have a systematic literature review of classic control (e.g., MPC, linear control, PID) and ML control to figure out why the mathematical model is needed, what unique benefits the mathematical models can offer, and why we need an ML-based or data-driven control.
4. In Definition 3, the formal mathematical formula or definition of ε-close is missing.
5. This paper’s technical contribution is very small. Significant parts of the paper are Definitions, Assumptions, Propositions, etc., cited from others.
6. Definition 8 is very hard to follow and understand. Many more explanations should be included.
7. The motives and explanations for Assumption 9 are missing. Because of this, I cannot conclude the correctness of the theoretical result (Theorem 10) and practice of Assumption 9.
8. The experimental systems are simple and low-dimensional numerical examples. They have a very large mismatch with the real systems. In my opinion, the experimental results are not convincing.
9. The paper lacks comparisons with other transfer learning approaches while considering addressing domain gaps.
10. The paper is not well-written and has many typos (see Figure ?? on page 8).
11. According to Figure 2 (a), I think the paper overstates the proposed framework due to very strong assumptions. I do not believe a control policy for one car can be safely deployed to a very different car (having different weights, different actuator structure, etc.), using the proposed approach.

### Questions
1. Why do the conditions in Defination have 0.5? What is the meaning of 0.5?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on leveraging neural networks to learn simulation relations between two control systems, which enables the transfer of control policies without system models. The proposed approach guarantees that the behaviors of the two systems remain close by learning a relation and an interface function between them. The approach is tested through case studies involving a vehicle model and a double pendulum.

### Strengths
1. Using neural networks to learn the similarity between two dynamical systems is interesting. 
2. Formal guarantees on simulation are provided.

### Weaknesses
1. This work focuses on synthesizing simulation relations, which is a classical problem in formal methods. As this work is positioned as transfer learning, please clarify how it enables transfer learning.
2. While the overall approach is intuitive and theoretically sound, I believe many in-depth analyses are missing.
    - 2.1. As $\epsilon$ should be a small positive number, it usually leads to a very fine-grained partition of the state space in Equation 9 and is supposed to be exponential with the state dimension. It is also reflected by only toy examples considered in the experiment. 
    - 2.2. The completeness is not discussed.
3. The experiment only considers toy examples (the vehicle model is 2 dimensional and the double pendulum is 4 dimensional). In addition, the authors do not compare the approach with the state of the arts in simulation/bisimulation learning, e.g., [1] either empirically or theoretically.

Minors:
1. In Definition 3, what does it formally mean by "their corresponding outputs remain $\epsilon$-close for all time"?
2. The figure reference is broken in the first line of Section 5.2.

### Questions
1. Please clarify how this work enables transfer learning.
2. Please provide a complexity analysis of the discretization approach, especially as it scales with state dimension.
3. Address how the proposed approach might scale to higher-dimensional systems. For instance, the authors can build experiments over any MuJoCo benchmarks to demonstrate the scalability.
4. Please provide a direct comparison with [1] both empirically and theoretically ([1] considers bisimulation relation, the authors can only discuss the simulation part). This work also partitions the state space into finite sets but uses a binary decision tree to learn the simulation relation.

### Soundness
3

### Presentation
2

### Contribution
2
