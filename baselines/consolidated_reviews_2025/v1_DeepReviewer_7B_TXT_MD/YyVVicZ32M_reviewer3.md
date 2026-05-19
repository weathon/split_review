### Summary

The paper proposes a new decoding algorithm called Permute-and-Flip (PF) decoding, which is a variation of the Gumbel-max trick. The authors show that PF decoding has better stability properties than softmax sampling, and is more greedy than greedy decoding. They also propose a watermarking scheme for PF decoding, which can detect watermarked text with low false positive rates. The authors empirically demonstrate that PF decoding outperforms traditional decoding methods in terms of perplexity, while maintaining the same stability.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper provides a theoretical analysis of the PF decoding algorithm, showing that it has better stability properties than softmax sampling, and is more greedy than greedy decoding.
- The authors propose a watermarking scheme for PF decoding, which can detect watermarked text with low false positive rates.
- The authors empirically demonstrate that PF decoding outperforms traditional decoding methods in terms of perplexity, while maintaining the same stability.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed PF decoding algorithm is very similar to the Gumbel sampling algorithm, and the theoretical analysis of the PF algorithm is very similar to that of the Gumbel sampling algorithm. The main difference is that the PF algorithm uses a different noise distribution (exponential distribution instead of Gumbel distribution). The authors should provide a more detailed discussion of the differences between the PF algorithm and the Gumbel sampling algorithm, and explain why the PF algorithm is better than the Gumbel sampling algorithm.
- The empirical results are not very convincing. The authors should provide more empirical results to demonstrate the effectiveness of the PF algorithm and the watermarking algorithm. For example, the authors could provide results on more datasets and tasks, and compare the performance of the PF algorithm with other decoding algorithms.
- The authors should provide a more detailed discussion of the limitations of the PF algorithm and the watermarking algorithm. For example, the authors could discuss the computational cost of the PF algorithm and the watermarking algorithm, and the robustness of the watermarking algorithm to different types of attacks.

### Suggestions

The paper would benefit from a more thorough comparison between the proposed Permute-and-Flip (PF) decoding algorithm and the Gumbel sampling method. While the authors highlight the use of an exponential distribution, a deeper analysis of the implications of this choice is needed. Specifically, the authors should explore how the tail behavior of the exponential distribution affects the decoding process compared to the Gumbel distribution. This could involve analyzing the variance of the samples and how they impact the stability of the decoding. Furthermore, a more detailed explanation of why the PF algorithm is expected to be more greedy than Gumbel sampling is required. This could be supported by a theoretical analysis of the algorithms' behavior under different conditions, such as varying temperature parameters or input sequence lengths. The authors should also consider providing a visual comparison of the sample distributions from both algorithms to illustrate the differences.

To strengthen the empirical evaluation, the authors should expand the range of datasets and tasks used to assess the performance of the PF algorithm. The current evaluation, while demonstrating the algorithm's effectiveness, is limited in scope. It would be beneficial to include datasets with varying characteristics, such as different vocabulary sizes, sequence lengths, and levels of complexity. Additionally, the authors should compare the PF algorithm with a broader range of decoding algorithms, including other sampling and greedy decoding methods. This would provide a more comprehensive understanding of the PF algorithm's strengths and weaknesses. The authors should also consider reporting additional metrics beyond perplexity, such as BLEU score or ROUGE score, to provide a more complete picture of the algorithm's performance. Furthermore, the authors should provide a more detailed analysis of the computational cost of the PF algorithm, including its time and space complexity, and compare it to other decoding methods. This is crucial for understanding the practical applicability of the algorithm.

Finally, the paper needs a more detailed discussion of the limitations of the proposed PF decoding algorithm and the watermarking scheme. The authors should address the potential computational cost of the PF algorithm, especially for large-scale applications. They should also discuss the robustness of the watermarking scheme to different types of attacks, such as paraphrasing, editing, and adversarial attacks. This could involve conducting experiments to evaluate the watermark's performance under various attack scenarios. The authors should also consider the potential for the watermarking scheme to introduce biases or artifacts into the generated text. A thorough discussion of these limitations is essential for a balanced and realistic assessment of the proposed methods.

### Questions

- Can the authors provide a more detailed discussion of the differences between the PF algorithm and the Gumbel sampling algorithm, and explain why the PF algorithm is better than the Gumbel sampling algorithm?
- Can the authors provide more empirical results to demonstrate the effectiveness of the PF algorithm and the watermarking algorithm?
- Can the authors provide a more detailed discussion of the limitations of the PF algorithm and the watermarking algorithm?

### Rating

5

### Confidence

3

**********
