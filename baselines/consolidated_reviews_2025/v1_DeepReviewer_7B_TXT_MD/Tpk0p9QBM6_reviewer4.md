### Summary

This paper proposes a unified framework for iterative minimum-entropy coupling (IMEC) algorithms, which is based on the idea of iteratively performing (approximate) MECs between a conditional distribution of one of the variables and the posterior over blocks of a partition associated with the other variable. The authors show that the IMEC algorithm of Sokota et al. (2022) and the factored IMEC algorithm of FIMEC (Sokota et al., 2023) can be seen as special cases of this framework. The authors also introduce a new algorithm, ARIMEC, which is based on the prefix tree partition set. They show that ARIMEC is a special case of the proposed framework and demonstrate its effectiveness in two settings: Markov coding games and steganography.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a comprehensive literature review and clearly state their contributions.
- The proposed algorithm, ARIMEC, is a novel contribution that extends the applicability of IMEC to arbitrary large-support distributions.
- The authors provide a detailed analysis of the computational complexity of ARIMEC and show that it is polynomial in the size of the support of the marginal distributions.
- The paper includes a thorough discussion of the related work and the limitations of their approach.

### Weaknesses

#### Some Related Works


#### comment

 - The main weakness of the paper is the lack of a rigorous theoretical analysis of the proposed algorithm. While the authors provide some theoretical results, they are not sufficient to establish the convergence and optimality of the algorithm. Specifically, the paper lacks a proof of convergence for the iterative algorithm, and it does not provide any guarantees on the quality of the solution. The authors mention that the algorithm is based on a formulation of MEC that unifies two existing approaches, but they do not provide a detailed comparison of the proposed algorithm with these approaches. It is unclear how the proposed algorithm improves upon the existing approaches, and what are the advantages and disadvantages of each approach.
- The experimental results are not very convincing. The authors only evaluate their algorithm in two settings: Markov coding games and steganography. It is unclear how the algorithm would perform in other settings, and what are the limitations of the algorithm in these settings. The paper also does not provide a detailed analysis of the experimental results. It is unclear how the results were obtained, and what are the implications of the results. The authors should provide a more comprehensive evaluation of their algorithm, including experiments on a wider range of datasets and settings, and provide a more detailed analysis of the experimental results.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the proposed ARIMEC algorithm. The authors should provide a proof of convergence for the iterative algorithm, demonstrating that the algorithm converges to a stationary point or a local minimum of the objective function. Furthermore, they should provide guarantees on the quality of the solution, such as bounds on the approximation error or the suboptimality gap. This analysis should include a discussion of the conditions under which the algorithm is guaranteed to converge and the factors that affect the convergence rate. The authors should also compare their algorithm with the two existing approaches that it unifies. This comparison should include a discussion of the computational complexity, the memory requirements, and the convergence properties of each algorithm. A more detailed theoretical analysis would significantly strengthen the paper and provide a more solid foundation for the proposed algorithm.

To address the concerns about the experimental results, the authors should conduct a more comprehensive evaluation of their algorithm. This should include experiments on a wider range of datasets and settings, beyond the two settings currently considered. For example, they could evaluate the algorithm on standard benchmark datasets for minimum-entropy coupling, as well as on other applications where minimum-entropy coupling is used, such as information theory, cryptography, and machine learning. The authors should also provide a more detailed analysis of the experimental results, including a discussion of the performance of the algorithm under different parameter settings and the sensitivity of the algorithm to the choice of hyperparameters. This analysis should also include a comparison of the performance of their algorithm with existing state-of-the-art algorithms for minimum-entropy coupling. A more comprehensive experimental evaluation would provide a more convincing demonstration of the effectiveness of the proposed algorithm.

Finally, the authors should provide a more detailed discussion of the limitations of their algorithm and the assumptions that are required for the algorithm to work correctly. This should include a discussion of the potential issues that can arise when applying the algorithm in practice, such as numerical instability or sensitivity to the choice of parameters. The authors should also discuss the potential future research directions that could address these limitations and improve the performance of the algorithm. A more thorough discussion of the limitations and future directions would provide a more balanced and nuanced perspective on the proposed algorithm and its potential impact.

### Questions

- How does the proposed algorithm compare to existing state-of-the-art algorithms for minimum-entropy coupling in terms of computational complexity and performance?
- What are the limitations of the proposed algorithm, and under what conditions is it guaranteed to converge to a good solution?
- How does the proposed algorithm perform in other settings beyond Markov coding games and steganography?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
