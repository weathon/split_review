### Summary

This paper studies the problem of computing minimum entropy couplings of two distributions, which has applications in steganography, causal inference, and other areas. The authors propose a new algorithm called ARIMEC, which unifies previous approaches to iterative MECs under a single partition-based framework. They also introduce a merging technique to improve the robustness of the algorithm. The authors demonstrate the effectiveness of their approach through experiments in Markov coding games and steganography.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel algorithm, ARIMEC, which unifies previous approaches to iterative MECs under a single partition-based framework. This is a significant contribution to the field of minimum entropy coupling.
2. The authors introduce a merging technique to improve the robustness of the algorithm, which is a valuable addition to the method.
3. The paper is well-written and organized, with clear explanations of the concepts and algorithms. The use of figures and examples helps to illustrate the ideas.
4. The authors provide a thorough experimental evaluation of their approach, demonstrating its effectiveness in two different settings. The results show that ARIMEC outperforms existing methods in terms of communication rate and robustness to suboptimal partition sets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the proposed algorithm. It would be helpful to have some guarantees on the performance of ARIMEC, such as bounds on the approximation ratio or convergence time. Specifically, while the paper mentions that ARIMEC unifies previous approaches, it lacks a formal analysis of how the approximation quality of ARIMEC relates to the approximation quality of the individual iterative MEC algorithms it encompasses. A more rigorous analysis of the approximation guarantees, even if only in specific cases or under certain assumptions, would significantly strengthen the theoretical contribution.
2. The paper focuses on discrete distributions, but it is unclear whether the proposed approach can be extended to continuous distributions. The current formulation relies heavily on the concept of partitions of discrete sample spaces, and it is not immediately obvious how this framework could be adapted to continuous spaces where partitions are not well-defined in the same way. A discussion of the challenges and potential solutions for continuous distributions would be valuable.

### Suggestions

The paper would benefit from a more detailed discussion of the relationship between the proposed ARIMEC algorithm and existing iterative MEC methods. While the paper claims to unify these approaches, it would be helpful to see a formal analysis that demonstrates how the approximation quality of ARIMEC is related to the approximation quality of the individual iterative MEC algorithms it encompasses. For example, if a specific iterative MEC algorithm has a known approximation ratio, can the authors provide a bound on the approximation ratio of ARIMEC when using that specific algorithm as a subroutine? This would provide a more concrete understanding of the theoretical properties of ARIMEC and its relationship to existing methods. Furthermore, it would be beneficial to explore the conditions under which ARIMEC achieves optimal or near-optimal performance, and to identify any scenarios where it might perform poorly. This could involve analyzing the properties of the partition sets used by ARIMEC and their impact on the final coupling.

To address the limitation of focusing solely on discrete distributions, the authors should consider discussing potential extensions to continuous distributions. While a full solution for continuous distributions may be beyond the scope of this paper, a discussion of the challenges and potential approaches would be valuable. For example, the authors could explore the possibility of using quantization techniques to approximate continuous distributions with discrete ones, and then apply ARIMEC to these approximations. Alternatively, they could investigate whether the partition-based framework can be adapted to continuous spaces using concepts from measure theory or functional analysis. This discussion should also address the computational complexity of any proposed extensions and the trade-offs between accuracy and efficiency. Even a preliminary exploration of these ideas would significantly broaden the impact of the paper.

Finally, the experimental section could be strengthened by including a more detailed analysis of the computational cost of ARIMEC. While the paper demonstrates the effectiveness of the algorithm in terms of communication rate and robustness, it would be helpful to see a more thorough analysis of the time and memory requirements of the algorithm, especially as the size of the distributions increases. This analysis should also compare the computational cost of ARIMEC to that of existing methods, providing a more complete picture of the practical trade-offs involved in using the proposed algorithm. Furthermore, it would be beneficial to explore the sensitivity of ARIMEC to the choice of partition sets and to provide guidelines for selecting appropriate partition sets for different types of distributions.

### Questions

1. Can the authors provide a theoretical analysis of the proposed algorithm, such as bounds on the approximation ratio or convergence time?
2. Can the proposed approach be extended to continuous distributions?
3. How does the proposed algorithm compare to other methods for computing minimum entropy couplings, such as the greedy algorithm of Kocaoglu et al. (2017)?

### Rating

6

### Confidence

2

**********
