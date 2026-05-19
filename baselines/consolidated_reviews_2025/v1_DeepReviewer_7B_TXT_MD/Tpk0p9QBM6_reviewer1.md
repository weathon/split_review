### Summary

This paper addresses the problem of minimum-entropy coupling (MEC), which seeks a joint distribution with minimum entropy among all the joint distributions that have specified marginal distributions. The authors focus on the case where the marginal distributions are large, and they introduce a new algorithm for approximating MEC. The algorithm is based on a formulation of MEC that unifies two existing approaches, and it is also robust to hyperparameter choices. The authors evaluate their algorithm in two settings: Markov coding games and steganography.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow, and the problem is well-motivated. The authors provide a comprehensive literature review and clearly state their contributions. The proposed algorithm is intuitive and well-motivated, and the experimental results are promising. The authors also provide a detailed discussion of the related work and the limitations of their approach.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a rigorous theoretical analysis of the proposed algorithm. While the authors provide some theoretical results, they are not sufficient to establish the convergence and optimality of the algorithm. Specifically, the paper lacks a proof of convergence for the iterative algorithm, and it does not provide any guarantees on the quality of the solution. The authors mention that the algorithm is based on a formulation of MEC that unifies two existing approaches, but they do not provide a detailed comparison of the proposed algorithm with these approaches. It is unclear how the proposed algorithm improves upon the existing approaches, and what are the advantages and disadvantages of each approach. The paper also does not provide a detailed analysis of the computational complexity of the proposed algorithm. It is unclear how the computational cost of the algorithm scales with the size of the input data, and how it compares to the computational cost of existing algorithms. The experimental results are also not sufficient to demonstrate the effectiveness of the proposed algorithm. The authors only evaluate their algorithm in two settings: Markov coding games and steganography. It is unclear how the algorithm would perform in other settings, and what are the limitations of the algorithm in these settings. The paper also does not provide a detailed analysis of the experimental results. It is unclear how the results were obtained, and what are the implications of the results. The paper also does not provide a detailed discussion of the limitations of the proposed algorithm. It is unclear what are the assumptions of the algorithm, and what are the potential problems that can arise when applying the algorithm in practice.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the proposed algorithm. The authors should provide a proof of convergence for the iterative algorithm, and they should also provide guarantees on the quality of the solution. This could involve showing that the algorithm converges to a local or global optimum, or providing bounds on the approximation error. The authors should also provide a detailed comparison of the proposed algorithm with the two existing approaches that it unifies. This comparison should include a discussion of the advantages and disadvantages of each approach, and it should also explain how the proposed algorithm improves upon the existing approaches. For example, the authors could analyze the computational complexity of each approach, and they could also analyze the convergence rate of each approach. The authors should also provide a detailed analysis of the computational complexity of the proposed algorithm. This analysis should include a discussion of how the computational cost of the algorithm scales with the size of the input data, and how it compares to the computational cost of existing algorithms. The authors should also provide a more detailed analysis of the experimental results. This analysis should include a discussion of how the results were obtained, and what are the implications of the results. The authors should also discuss the limitations of the proposed algorithm, and what are the assumptions of the algorithm. The authors should also consider evaluating their algorithm in more settings, to demonstrate its effectiveness in a wider range of applications. This could include evaluating the algorithm in other settings, such as entropic causal inference, random number generation, functional representations, and dimensionality reduction. The authors should also consider comparing their algorithm with other state-of-the-art algorithms for minimum-entropy coupling. This comparison should include a discussion of the advantages and disadvantages of each algorithm, and it should also explain why the proposed algorithm is a better choice for the problem that the authors are considering.

### Questions

1. Can you provide a more detailed comparison of your algorithm with the two existing approaches that it unifies? What are the advantages and disadvantages of each approach, and how does your algorithm improve upon them?
2. Can you provide a more detailed analysis of the computational complexity of your algorithm? How does the computational cost of your algorithm scale with the size of the input data, and how does it compare to the computational cost of existing algorithms?
3. Can you provide a more detailed discussion of the limitations of your algorithm? What are the assumptions of the algorithm, and what are the potential problems that can arise when applying the algorithm in practice?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
