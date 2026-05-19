### Summary

This paper proposes a new decoding algorithm called Permute-and-Flip (PF) decoding. The PF algorithm is claimed to have stability properties similar to softmax sampling while being more greedy and having lower perplexity. The authors also propose a watermarking algorithm that can be applied to PF decoding. The authors provide theoretical analysis of the PF algorithm and compare it with softmax sampling and greedy decoding. The authors also provide empirical results on open-ended text generation and question-answering tasks to demonstrate the effectiveness of the PF algorithm and the watermarking algorithm.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical analysis of the PF algorithm is thorough and provides a solid foundation for the proposed method.
3. The empirical results demonstrate the effectiveness of the PF algorithm and the watermarking algorithm.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed PF algorithm is very similar to the Gumbel sampling algorithm, and the theoretical analysis of the PF algorithm is very similar to that of the Gumbel sampling algorithm. The main difference is that the PF algorithm uses a different noise distribution (exponential distribution instead of Gumbel distribution). The authors should provide a more detailed discussion of the differences between the PF algorithm and the Gumbel sampling algorithm, and explain why the PF algorithm is better than the Gumbel sampling algorithm.
2. The empirical results are not very convincing. The authors should provide more empirical results to demonstrate the effectiveness of the PF algorithm and the watermarking algorithm. For example, the authors could provide results on more datasets and tasks, and compare the performance of the PF algorithm with other decoding algorithms.
3. The authors should provide a more detailed discussion of the limitations of the PF algorithm and the watermarking algorithm. For example, the authors could discuss the computational cost of the PF algorithm and the watermarking algorithm, and the robustness of the watermarking algorithm to different types of attacks.

### Suggestions

The paper would benefit from a more rigorous comparison between the Permute-and-Flip (PF) algorithm and Gumbel sampling. While the authors mention the use of different noise distributions, the practical implications and theoretical advantages of this choice are not sufficiently explored. A deeper analysis should be provided, perhaps by examining the tail behavior of the two distributions and how they affect the decoding process. Specifically, the authors should investigate whether the exponential distribution used in PF leads to a more uniform sampling of the output space compared to the Gumbel distribution, and if this uniformity translates to improved performance in practice. Furthermore, a more detailed analysis of the stability properties of both algorithms, beyond the theoretical bounds, would be valuable. This could involve empirical studies of how the algorithms behave under various conditions, such as different temperature settings or input sequences. The authors should also consider providing a more intuitive explanation of why the PF algorithm is expected to perform better than Gumbel sampling, perhaps by relating it to the underlying principles of each method.

To strengthen the empirical evaluation, the authors should expand their experiments to include a wider range of datasets and tasks. The current evaluation is limited in scope, making it difficult to assess the generalizability of the PF algorithm. For example, the authors could evaluate the algorithm on datasets with different characteristics, such as those with longer sequences or more complex dependencies. Additionally, the comparison with other decoding algorithms should be more comprehensive, including both sampling-based and greedy decoding methods. The authors should also consider reporting additional metrics beyond perplexity, such as BLEU score or ROUGE score, to provide a more complete picture of the algorithm's performance. It would also be beneficial to include ablation studies to understand the impact of different components of the PF algorithm, such as the permutation step and the flipping step. This would help to identify the key factors that contribute to the algorithm's effectiveness.

Finally, the paper should include a more thorough discussion of the limitations of the proposed methods. The authors should address the computational cost of the PF algorithm, particularly in comparison to simpler decoding methods. While the authors mention that the algorithm is efficient, a more detailed analysis of the time and space complexity would be helpful. Furthermore, the robustness of the watermarking algorithm to different types of attacks should be investigated more thoroughly. The authors should consider evaluating the algorithm against a wider range of attacks, including those that are specifically designed to remove or alter watermarks. The discussion of limitations should also include potential failure modes of the algorithms, such as cases where the algorithm produces suboptimal outputs or fails to detect watermarks. Addressing these limitations would provide a more balanced and realistic assessment of the proposed methods.

### Questions

1. The authors should provide a more detailed discussion of the differences between the PF algorithm and the Gumbel sampling algorithm, and explain why the PF algorithm is better than the Gumbel sampling algorithm.
2. The authors should provide more empirical results to demonstrate the effectiveness of the PF algorithm and the watermarking algorithm.
3. The authors should provide a more detailed discussion of the limitations of the PF algorithm and the watermarking algorithm.

### Rating

5

### Confidence

3

**********
