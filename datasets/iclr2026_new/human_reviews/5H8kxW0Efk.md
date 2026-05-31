## Human Reviewer 1

### Summary
This paper introduces a novel neural network-based method inspired by Ising machines for solving combinatorial optimization problems. The approach is trained using a zero-order optimization method proposed by Reifenstein et al. (2024). The authors benchmark their method against recent state-of-the-art (SOTA) techniques from both the unsupervised combinatorial optimization and Ising machine communities, demonstrating strong performance across a wide range of problems. Additionally, the paper includes ablation studies examining problem difficulty, parameter count, and problem size.

### Strengths
- **Novelty:** The proposed method appears to be original and distinct from existing approaches.
- **Performance:** The method achieves competitive results on well-established benchmarks.
- **Rigor:** The inclusion of ablation studies provides valuable insights into the method’s robustness and sensitivity to key variables.

### Weaknesses
- **Lack of Clarity on Optimization:** The paper employs a zero-order optimizer from Reifenstein et al. (2024), but the algorithm itself is not explained. A brief introduction or intuition about the optimizer would significantly improve accessibility for readers unfamiliar with the reference.
- **Reward Function Assumptions:** The reward functions in Appendix F relies on knowledge of the optimal energy value. This assumption raises concerns about fairness in comparisons with methods that do not use such information.

### Questions
1. **Gradient Derivation (Q1):**
   Could the authors provide an intuitive explanation of the principles underlying the gradient derivations in Appendix G? This would enhance the paper’s clarity and make it more self-contained.

2. **Reward Function Justification (Q2):**
   How is the use of the optimal energy value in the reward justified? Since other methods do not rely on this information, it is unclear whether the comparison is equitable. A discussion on this point—and an exploration of the method’s performance using only the raw energy as a reward—would be highly informative.

3. **Architectural Alternatives (Q3):**
   The MLP parametrization resembles recurrent architectures like LSTMs. Have the authors explored using LSTMs or similar architectures instead? If so, how does their performance compare to the proposed MLP-based approach?

4. **Clarification on Table 1 (Q4):**
   What does “top 30” refer to in Table 1? Could the authors please clarify?

5. **Diversity of the solutions (Q5):**
If I understand correctly in each trajectory the best solution is taken and for example in Table 1 then the average of these solutions is computed. Is there some diversity in the best solution between trajectories or do all trajectories propose give the same best solution?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper proposes a learning-based approach for combinatorial optimization via learning the parameters of an iterative dynamical system (Ising machines).  The major contributions of this work are in the combination of algorithmic unrolling, ising machines, and zeroth-order optimization in the context of CO problems.  Computationally, once trained, their approach achieves strong results on benchmark instances for max independent set, max clique, and max cut CO problems.

### Strengths
- **Novelty**:  This paper proposes a novel approach that combines algorithmic unrolling, ising machines, and zeroth-order optimization in the context of CO problems.  While this is a combination of existing frameworks, I believe this combination is sufficiently novel and quite refreshing from recent approaches that primarily utilize RL/transformer-style rollouts. 
-  **Results**: On the instances evaluated, this approach performs quite well, with the ability to compute high-quality solutions relatively quickly.

### Weaknesses
- **Adaptability**: From my understanding, this approach is relatively limited in terms of the classes of optimization problems that it can be used on, e.g., those that can be formulated as Equation (1).  Compared to other exact/heuristic/learning-based methods, this is a relatively strong limitation in terms of applicability.  
- **G-Set Results**: The authors compute time-to-solution (TTS) on the G-set benchmarks using reference cut values drawn from prior Ising-machine literature rather than from the globally best-known Max-Cut results reported in combinatorial-optimization studies. While this choice maintains consistency with neural Ising comparisons, it also means that the reported TTS values correspond to approximate rather than truly optimal targets. For this reason, it would be more informative to include information on the differences in solution quality and time compared to the best-known approaches.  
- **Scalability**: The experiments are limited to G-set instances up to $N=1000$, with no results reported for the larger, more challenging graphs. The authors state that the scalability is with respect to model size, rather than CO problem size, so I am not sure why they would limit their evaluation to small instances.  The absence of results on larger instances makes it difficult to assess how well the method scales relative to state-of-the-art Ising and Max-Cut solvers.  This is a further concern given the limited applicability to other classes of problems. Additionally, there is no reporting of training time, which makes the scalability of training unclear.

### Questions
**Questions**
- [1] propose an approach based on learning and Ising machines for CO.  Can the authors detail the differences in these works and include this in the paper?  
- How long do these methods take to train, especially compared to other methods, e.g., DiffUCO?  These should all be included in the appendix.  
- How does the performance of a model generalize out-of-distribution?
- Can the authors provide more information on the Gurobi results, i.e., optimality gaps and the time Gurobi takes to find equivalent quality solutions (when Gurobi finds better solutions)?  Furthermore, was Gurobi run with MIPFocus=1 (to prioritize primal solutions)?  If not, this should be done, given the heuristic focus of this work.  

**Remarks**:
- In the abstract and throughout the paper, the authors constantly state that they are "solving" instances.  This needs to be changed since their method is a heuristic, and solving should be reserved for exact methods.  
- Figure 7 "training training" should be "training". 

**References**:
- [1] Bo Lu, Yong-Pan Gao, Kai Wen, and Chuan Wang. Combinatorial optimization solving by coherent
ising machines based on spiking neural networks. Quantum, 7:1151, 2023.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper studies Ising machines as optimizers for combinatorial problems—specifically Max-Cut, Maximum Independent Set (MIS), and Max-Clique—and proposes a zeroth-order (gradient-free) optimization approach for tuning/steering the machine. The authors compare against prior Ising-based methods and aim to demonstrate improved solution quality and/or efficiency.

### Strengths
The Ising formulation is a natural modeling choice for quadratic objectives, and the paper targets three canonical NP-hard problems with broad interest.

Using zeroth-order optimization is well-motivated in settings with noisy or non-differentiable hardware, and the paper’s perspective could be useful to practitioners working with analog or black-box solvers.

The manuscript attempts to position the work within the growing literature on physical/Ising-style optimizers for CO, which is timely.

### Weaknesses
Evaluation metrics (TTS vs objective quality). The paper emphasizes “time to solution” (TTS), defined as the time required to reach a solution with 99% success probability. While TTS is common in annealing/Ising communities, it is less standard in the combinatorial optimization literature, which typically leads with objective quality (cut value, clique size, independent set size), approximation ratios or normalized optimality gaps, and then reports wall-clock time. I encourage the authors to complement TTS with conventional CO metrics. This would make results easier to compare with non-Ising baselines.

### Questions
None

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
3