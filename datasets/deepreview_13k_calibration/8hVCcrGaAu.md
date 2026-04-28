# EDiSon: Efficient Design-and-Control Optimization with Reinforcement Learning and Adaptive Design Reuse

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Seeking good designs is a central goal of many important domains, such as robotics, integrated circuits (IC), medicine, and materials science. These design problems are expensive, time-consuming, and traditionally performed by human experts. Moreover, the barriers to domain knowledge make it challenging to propose a universal solution that generalizes to different design problems. In this paper, we propose a new method called Efficient Design and Stable Control (EDiSon) for automatic design and control in different design problems. The key ideas of our method are (1) interactive sequential modeling of the design and control process and (2) adaptive exploration and design replay. To decompose the difficulty of learning design and control as a whole, we leverage sequential modeling for both the design process and control process, with a design policy to generate step-by-step design proposals and a control policy to optimize the objective by operating the design. With deep reinforcement learning (RL), the policies learn to find good designs by maximizing a reward signal that evaluates the quality of designs. Furthermore, we propose an adaptive exploration and replay strategy based on a design memory that maintains high-quality designs generated so far. By regulating between constructing a design from scratch or replaying a design from memory to refine it, EDiSon balances the trade-off between exploration and exploitation in the design space and stabilizes the learning of the control policy. In the experiments, we evaluate our method in robotic morphology design and Tetris-based design tasks. Our results show that our method effectively learns to explore high-quality designs and outperforms previous results in terms of design score and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes the use of a design buffer (consisting of previously found good designs) to balance exploration and exploitation in the Transform2Act pipeline. More concretely, it proposes two strategies to utilize this buffer -- the first picks a good design from the buffer with probability $1-p$ and designs from scratch with probability $p$, while the second strategy uses UCB-esque score to decide when to design from scratch. Through experiments on robotic morphology and Tetris-based design tasks, the paper demonstrates the method's efficacy against Transform2Act.

### Strengths
- The paper conveys the main ideas clearly.
- The experimental results demonstrate the benefit of utilizing a design buffer.

### Weaknesses
 - My main concern with this paper is the very incremental nature of the contribution.

### Questions
Could the authors elaborate on some key challenges faced when integrating a design buffer into the Transform2Act pipeline, and how their method addresses them? All in all, I am trying to understand if this is straightforward.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the complexities of design optimization tasks, which are often resource-intensive and require specialized expertise. The authors introduce Efficient Design and Stable Control (EDiSON), a reinforcement learning-based approach with minimal human intervention. EDiSON has three key components: 1) a Design Policy that explores the design space step-by-step to efficiently find an optimal design, 2) a Control Policy that optimizes each design for specific tasks, and 3) a Bandit Meta-Controller that balances exploration and exploitation by dynamically choosing between reusing good designs or generating new ones. Experimental results showed that EDiSON outperformed the baseline, Transform2Act, in various design optimization tasks.

### Strengths
* The paper is well-structured, and the contributions are clear.
* Using the _adaptive exploration-exploitation balancing_ technique, EDiSON improves sample efficiency, making the approach more practical for real-world applications.
* The ablation study is comprehensive
* EDiSON shows a clear improvement over the baseline (Transform2Act) across various design tasks

### Weaknesses
 * The novelty of the proposed algorithm feels somewhat limited, as it mainly combines existing methods. The performance improvements therefore seem expected rather than groundbreaking.
* Lack of theoretical analysis on non-ergodic MDP. (But it’s ok, as such papers do not necessarily require theoretical foundations.)
* The single baseline used in the experiment (Transform2Act) makes it challenging to fairly evaluate the efficacy of the proposed method. Could the authors include comparisons with additional recent methods?

### Questions
**[Q1]** The control MDP structure described in the paper does not clearly appear to be ergodic. Could the authors elaborate on how EDiSON ensures stability and optimality in non-ergodic environments, either theoretically or experimentally?

**[Q2]** Even though the Bandit-based meta-controller adjusts its exploration dynamically, could there be scenarios where such adaptability might converge prematurely to suboptimal designs? How could one mitigate such risks?

**[Q3]** F(d) (score) can significantly change with each evaluation. Could the authors discuss the potential impact of score variability on the robustness of the design selection process?

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
4

### Summary
The paper presents Edison, a new method for automatic design and control. The method is based on the interactive adaptations of the design and controller, with features such as a design buffer to leverage the history of high quality designs encountered during learning.  The method is evaluated on robot morphology and tetris-based design tasks, and is shown to exhibit promising results.

### Strengths
The paper tackles an important and relatively under-explored problem of co-designing good  design-controller solutions. The paper is well written, and is fairly simple and easy to understand.

### Weaknesses
Some of the design decisions could benefit from better motivation, and should be justified better. Apart from this, the method is compared only with one other baseline. More thorough empirical investigations would be beneficial.

I doubt that setting p=1 is equivalent to transform2act. That approach is fundamentally different, with separate for loops for skeleton, attributes and actions.

As mentioned, a lack of diversity of designs in the design buffer could compromise performance.

### Questions
1.	The results currently only use transform2act as the baseline. However, other relevant methods [1,2] exist, which could be included as baselines or at least discussed in detail.
2.	To expand on the above point, when it comes to co-design, evolutionary methods [3] are a natural choice. Is there a specific reason why the authors have not considered such methods?
3.	In terms of the meta-controller, what motivated the use of an MAB solution? Could other approaches like Bayesian Optimisation have been considered?
4.	Is p in eq 4 fixed? In general, is it not better to anneal it? Since there is mention of using fixed values of p, perhaps it is also worth reporting empirically the effect of different fixed values.
5.	I doubt that setting p=1 is equivalent to transform2act. That approach is fundamentally different, with separate for loops for skeleton, attributes and actions. 
6.	In line 279, what do the authors mean by “artificially given good examples”?
7.	As mentioned, a lack of diversity of designs in the design buffer could compromise performance

[1] Luck, Kevin Sebastian, Heni Ben Amor, and Roberto Calandra. "Data-efficient co-adaptation of morphology and behaviour with deep reinforcement learning." Conference on Robot Learning. PMLR, 2020.

[2] Schaff, Charles, et al. "Jointly learning to construct and control agents using deep reinforcement learning." 2019 international conference on robotics and automation (ICRA). IEEE, 2019.

[3] Wang, Tingwu, et al. "Neural Graph Evolution: Towards Efficient Automatic Robot Design." International Conference on Learning Representations.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors study the design-and-control co-design problem. They propose a deep reinforcement learning algorithm to solve this problem. The main innovation is the reuse of previous designs to balance exploration and exploitation in the design space. Experiments on robotic morphology design tasks and a Tetris-based task show improvement over a baseline method.

### Strengths
1. The combination of a design buffer and a multi-armed bandit exploration-exploitation tradeoff policy is novel. It also makes intuitive sense why reusing prior good designs can help the optimization progress faster.

2. The paper is mostly well-written and easy to follow.

### Weaknesses
1. The experiment section has only a single baseline and the current submission misses several relevant papers [1, 2, 3]. These works all introduce methods for co-design of structure and control policy so their inclusion would strengthen the empirical significance of the submission.

2. While the proposed method is novel, the novelty is limited. The idea is closely related to the experience replay idea which is widely used in deep reinforcement learning algorithms.

[1] Wang, Yuxing, et al. "PreCo: Enhancing Generalization in Co-Design of Modular Soft Robots via Brain-Body Pre-Training." Conference on Robot Learning. PMLR, 2023.

[2] Dong, Heng, et al. "Symmetry-aware robot design with structured subgroups." International Conference on Machine Learning. PMLR, 2023.

[3] Hu, Jiaheng, Julian Whitman, and Howie Choset. "GLSO: grammar-guided latent space optimization for sample-efficient robot design automation." Conference on Robot Learning. PMLR, 2023.

### Questions
1. In the paragraph titled “Control As A Multi-Step MDP” (around line 216), is it correct to say that the observation space (both that of the environment and that of the design state) can change based on a specific design? If so, how do the authors ensure that a single control policy is compatible with different observation spaces?

2. Equation 3 seems incorrect. I think the correct formulation is a nested optimization problem
$$d^*=\arg\max_{d} J(\pi_d, d), s.t. \pi_d = \arg\max_{\pi}J(\pi, d)$$

3. In the EDiSon algorithm, the control policy learns from more trajectories as the iteration increases. It is likely that the initial trajectories were poor thus recording lower values for those designs, even if a design is good. This feels like a substantial issue, can the authors comment on this?

### Soundness
2

### Presentation
3

### Contribution
2
