### Summary

The paper considers the problem of computing a low-entropy coupling between two distributions over large sample spaces. The paper presents a new algorithm that builds on top of prior work on iterative MEC (IMEC) algorithms. The paper also presents experimental results that demonstrate the effectiveness of the proposed algorithm.

### Soundness

3

### Presentation

2

### Contribution

3

### Strengths

The paper presents a novel algorithm for computing low-entropy couplings between two distributions over large sample spaces. The algorithm builds on top of prior work on IMEC algorithms, but it makes a number of new contributions, including the use of a partition set that is compatible with autoregressive models, a search procedure for finding a maximum-entropy partition, and a merging technique for improving the robustness of the algorithm. The paper also presents experimental results that demonstrate the effectiveness of the proposed algorithm in two settings: Markov coding games and steganography.

### Weaknesses

#### Some Related Works


#### comment

The paper is technically sound, but it could be improved in terms of clarity and presentation. For example, the paper could provide more intuition and motivation for the proposed algorithm, and it could also provide more details on the experimental setup and results. Additionally, the paper could be more self-contained and provide more background information on the relevant concepts and techniques. The paper also lacks a clear explanation of the trade-offs between the proposed method and existing approaches, particularly in terms of computational complexity and performance guarantees. The experimental section could benefit from a more thorough analysis of the results, including a discussion of the limitations of the proposed method and potential areas for future research. Furthermore, the paper does not clearly articulate the specific challenges in applying existing low-entropy coupling techniques to large-support distributions, which would help to contextualize the contribution of the proposed algorithm.

### Suggestions

To improve the clarity and presentation of the paper, the authors should begin by providing a more detailed explanation of the problem of computing low-entropy couplings and its significance in various applications. This should include a discussion of the limitations of existing methods when dealing with large-support distributions, highlighting the specific challenges that the proposed algorithm aims to address. For instance, the authors could elaborate on why traditional iterative MEC algorithms struggle with large sample spaces, and how the proposed partition set and search procedure help to overcome these limitations. This would provide a stronger motivation for the proposed approach and make the paper more accessible to a broader audience. Additionally, the authors should provide a more detailed explanation of the merging technique, including a discussion of its theoretical properties and its impact on the performance of the algorithm. 

In the experimental section, the authors should provide more details on the experimental setup, including the specific datasets used, the parameter settings, and the evaluation metrics. The results should be presented in a more structured manner, with clear explanations of the observed trends and patterns. The authors should also include a more thorough analysis of the limitations of the proposed method, discussing potential failure cases and areas for future research. For example, it would be beneficial to explore the sensitivity of the algorithm to different parameter settings and to compare its performance with other state-of-the-art methods. Furthermore, the authors should provide a more detailed discussion of the computational complexity of the proposed algorithm, including a comparison with existing approaches. This would help to clarify the trade-offs between the proposed method and existing techniques, and to identify the specific scenarios in which the proposed algorithm is most effective. 

Finally, the authors should consider adding a section that summarizes the key contributions of the paper and discusses potential directions for future research. This section should highlight the novelty of the proposed algorithm and its potential impact on the field. It should also identify the limitations of the current work and suggest specific areas where further research is needed. For example, the authors could discuss the potential for extending the proposed algorithm to other types of distributions or to other applications. This would help to contextualize the contribution of the paper and to provide a roadmap for future research in this area.

### Questions

1. Can the authors provide more details on the experimental setup and results? For example, what are the specific datasets used in the experiments, and what are the evaluation metrics?
2. Can the authors provide more intuition and motivation for the proposed algorithm? For example, why is it important to use a partition set that is compatible with autoregressive models, and how does this help to improve the performance of the algorithm?
3. Can the authors provide more details on the merging technique? For example, how does it work, and what are its theoretical properties?

### Rating

6

### Confidence

3

**********
