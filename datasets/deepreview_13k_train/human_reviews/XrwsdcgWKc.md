# Enhancing Variational Quantum Algorithms: Effective Quantum Ansatz Design Using GFlowNets

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
Quantum computing promises significant computational advantages over classical computing. However, current devices are constrained by a limited qubit count and noise. By combining classical optimization methods with parameterized quantum circuits, Variational Quantum Algorithms (VQAs) offer a potential solution for noisy intermediate-scale quantum systems (NISQ). This makes VQAs particularly promising strategies for achieving near-term quantum advantages; such approaches are now widely explored for nearly all quantum computing applications. However, designing effective parameterized circuits, also known as ansatz, remains challenging. In this work, we introduce the use of GFlowNets as an efficient method to automate the development of efficient ansatz for various quantum computing problems. Our approach leverages GFlowNets to efficiently explore the combinatorial space of parameterized quantum circuits. Our extensice experiments demonstrate that GFlowNets can discover ansatz with an order of magnitude fewer parameters, gate counts, and depths compared to current approaches for the molecular electronic ground state energy problem. We also apply our approach to the unweighted Max-Cut problem, where we observe similar improvements in circuit efficiency. These results highlight the potential of GFlowNets to significantly reduce the resource requirements of VQAs while maintaining or improving solution quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors proposed a novel quantum architecture search algorithm utilizing GFlowNets. The GFlowNet based algorithm is able to generate efficient ansatz tailored for tasks such as the ground state energy estimation and the unweighted max-cut problem. Numerical experiments show that the proposed algorithm is able to reduce the gate count while achieving good accuracy compared to previous literature.

### Strengths
1. The essence of GFlowNets actually fits the nature of quantum architecture search, which can be further explored as one of the AI for quantum algorithms.
2. Well-structured article with properly selected experimental tasks to demonstrate the efficiency of the proposed method.

### Weaknesses
1. The scalability of the QAS approaches is always a main concern in ensuring the practical utility of these methods. The authors could provide a more detailed discussion about this topic. Specifically, the manuscript lacks a rigorous analysis of how the GFlowNet's computational cost scales with increasing qubit number and circuit depth. It is essential to understand the limitations of the proposed method in terms of the size of quantum systems it can effectively handle, and how the training time and resources increase with problem complexity.

2. The results of both bond lengths in Figure 2 are very close to the ground state, which is hard to tell from the figure. It would be better if you could provide the energy error along with the energy value (as in [1]). The current presentation makes it difficult to assess the precision of the method in comparison to the true ground state energy, and a more detailed analysis of the energy differences is needed to demonstrate the method's practical utility.

3. As QAS is evolving very fast, QuantumDARTS is actually not the SOTA at this time. [2] provided a curriculum reinforcement learning method that surpasses QuantumDARTS on the ground state energy estimation problem. The authors could consider their results. The manuscript should include a more thorough comparison with the most recent state-of-the-art methods, including a discussion of the relative strengths and weaknesses of the proposed approach in comparison to these alternatives.

4. The proposed method is mainly examined by numerical results and lacks theoretical guarantees (with only theorem 4.1). While numerical experiments are important, a deeper theoretical analysis of the convergence properties of the GFlowNet-based search algorithm is needed. This should include a discussion of the conditions under which the algorithm is guaranteed to converge to an optimal or near-optimal solution, and an analysis of the algorithm's robustness to different initial conditions and hyperparameter settings.

### Questions
No Questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper deployed a generative model (GflowNet) to assist the design of variational quantum algorithm. The novelty is relatively weak as it applied a popular techniques of generative machine learning to a quantum application. Quantum architecture search problem has been widely studied by many literature, where the biggest challenge lie on the architecture search space and computational cost. However, the authors do not explore or discuss it deep enough. Meanwhile, the numerical results are relatively weak.

### Strengths
Leveraging generative models for quantum algorithms is an interesting topic

### Weaknesses
 The novelty is relatively weak as it applied a popular techniques of generative machine learning to a quantum application. Quantum architecture search problem has been widely studied by many literature, where the biggest challenge lie on the architecture search space and computational cost. However, the authors do not explore or discuss it deep enough. Meanwhile, the numerical results are relatively weak.

 The computational cost is not discussed.
The numerical experiments are weak and are not well reported. 
Please see the detailed comments in Questions.

### Questions
Here are a few major questions and comments regarding the methodology and numerical experiments:
1. How is the state space designed? How to deal with exponential complexity in the design state? How is the scalability of the approach? 
2. How to optimize the ansatz parameters and ansatz architecture simultaneously, especially from the computational cost perspective. Some computational cost should be reported. 
3. The sizes of the example cases are very small, e.g., 4 and 6 qubits Hamitonians for ground state energy problem. 
4. How many iterations/circuit trails does the framework take to converge? 
5. In Figure 3 and Tables 1 & 3, the standard deviation should be reported. 
6. In Figure 3, the authors only compare to one architecture search algorithm (QDARTS) whose idea was first proposed in arXiv 2010.08561 and a modified version (Wu et al 2023) is published in ICML 2023. The baseline is not strong enough given that there are many quantum architecture search literatures now. 
7. Although the proposed generative model finds better ansatz than the QDARTS, I image QDARTS would be more efficient.

### Soundness
2

### Presentation
2

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
In this paper, the quantum circuits are tokenized as input for a sequence model. GFlowNets, along with trajectory balance, are applied to find the optimal composition of a basis gate set to minimize the loss function of a certain task. Such an approach can find a better circuit architecture with fewer gates and shorter depth for variational tasks, including ground state energy and unweighted max cut.

### Strengths
1.	Introduce GFlowNets into quantum circuit architecture search as its close relationship with DAGs and state transform;
2.	Utilize a forward mask to filter out redundant gates;
3.	Achieve chemical precision and great transferability for ground state energy problems, and exhibit a major reduction in circuit depth, gate counts, and the number of parameters for max cut problems

### Weaknesses
1.	This paper applies the trajectory balance due to faster credit assignment and robustness to long trajectories. However, this paper lacks a convincing explanation of how these two features contribute to the generation of effective quantum circuit ansatz. Specifically, it is unclear how faster credit assignment translates to better circuit structures, and the notion of 'long trajectories' in the context of quantum circuit construction is not well-defined. Also, this paper should provide circuit generated with GFlowNets using other objective functions, such as the original flow matching loss mentioned in the paper, subtrajectory balance objective (Madan, K., Learning GFlowNets From Partial Episodes For Improved Convergence And Stability), and another objective function which deals with extra long trajectories (Pan, L., Better Training of GFlowNets with Local Credit and Incomplete Trajectories).
2.	This paper highlights that the ansatz generation method could result in fewer parameters, gate counts, and depths and deals with scalability problems. However, the experiment circuits are relatively small, and the maximum circuit scale is only 10 nodes in the max cut problem. The authors should consider adding larger problems as related research has demonstrated its circuit search with more than 100 qubits (Wang, H., QuantumNAS: Noise-Adaptive Search for Robust Quantum Circuits). The current scale does not sufficiently demonstrate the method's ability to handle complex quantum systems. The number of parameters, while reduced, is not shown to scale favorably with increasing problem size.
3.	This paper does not take into consideration hardware constraints, including hardware topology and noise, which are crucial to NISQ devices. These constraints may lead to an increase in circuit depth and gate counts. The absence of hardware considerations makes the practical applicability of the generated circuits questionable, as real-world quantum devices have significant limitations that must be addressed during circuit design.

### Questions
1.	When discussing transferability, Figure 2 only shows the comparison results between VQE-GFNs and HF, how is the transferability of other generated circuits, such as UCCSD, QuantumDARTS, QCAS, and DQAS as shown in Table 1?
2.	In Table 1, all methods except QCAS achieve a result within the chemical accuracy, and “Ours” does not get the smallest error. However, in Figure 3, the “Ours” method achieves a parameter count smaller than the maximum limit. Does that mean the training process should not stop here, or are certain masks too strict?
3.	In Figure 3, 7, 8, and 9, all circuits achieve a parameter count smaller than the parameter limit set by the training process. Will certain experiments return a circuit which has exactly the number of parameters as the limit? As the problem grows more complicated, can the model always return a circuit that is below the parameter number limit?

### Soundness
2

### Presentation
3

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
This paper proposes to use GFlowNets (GFNs) to design the ansatz of variational quantum algorithms (VQAs). The authors apply their quantum architecture search (QAS) framework to ground state energy estimation and the unweighted max-cut problems. The results indicate that for ground state energy estimation, GFNs achieve chemical accuracy while using fewer parameters, gates, and with smaller circuit depths than existing methods such as QuantumDARTS and the UCCSD ansatz. For unweighted max-cut, their approach solves 10-node instances with smaller circuit depths than QuantumDARTS.

### Strengths
- To my knowledge, the application of GFlowNets to variational quantum circuits is novel.
- The experimental results show a substantial advantage over existing methods, particularly for the ground state energy problem.
- The generalizability of GFNs is nice to have, although there are no quantitative results presented in comparison to other methods for quantum architecture search.

### Weaknesses
 - While the experiments show that QAS does better than other models, the problems are relatively small and it is somewhat unclear how well this approach scales for larger problems.
- The use of GFNs doesn't seem to take into account much (if any) problem structure, such as symmetries. Many VQAs leverage permutation symmetry to reduce the size of the search space and achieve better results.
- Overall, this paper could be considered incremental as it simply uses a different ML model for VQAs to obtain improved performance. Among all the other papers along this line, there isn't much in this paper that particularly stands out.
- Several minor grammatical issues and typos throughout the paper.

### Questions
- For unweighted max-cut, why was conditional value-at-risk (CVaR) used rather than more common metrics, such as the average and maximum size of the cut found? CVaR seems to be a rather unusual metric, and it would be useful to also provide the operational meaning of this metric.

### Soundness
3

### Presentation
2

### Contribution
3
