### Summary

This paper proposes a new decoding method called Permute-and-Flip (PF) decoder. It enjoys stability properties similar to the standard sampling decoder, but is provably up to 2x better in its quality-stability tradeoff than sampling and never worse than any other decoder. The authors also design a cryptographic watermarking scheme analogous to Aaronson (2023)'s Gumbel watermark, but naturally tailored for PF decoder. The watermarking scheme does not change the distribution to sample, while allowing arbitrarily low false positive rate and high recall whenever the generated text has high entropy. The authors provide the code in the supplementary materials.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed PF decoder is novel and theoretically grounded.
3. The proposed PF watermark is novel and theoretically grounded.
4. The authors provide the code in the supplementary materials.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead of the PF decoder compared to standard softmax sampling. While the authors claim improved quality-stability tradeoff, the practical implications of this in terms of decoding speed and memory usage are not thoroughly explored. It's unclear how the permutation and flipping operations scale with vocabulary size and sequence length, which are critical for real-world applications.
2. The experimental evaluation of the PF watermark could be more comprehensive. The paper primarily focuses on the theoretical aspects of the watermark, but lacks a thorough empirical evaluation of its robustness against various attacks, such as paraphrasing, translation, or adversarial modifications. The detection accuracy under different noise levels and the impact of text length on watermark detection are not sufficiently addressed.

### Suggestions

The authors should provide a more detailed analysis of the computational complexity of the PF decoder. Specifically, they should analyze the time and space complexity of the permutation and flipping operations in relation to the vocabulary size and sequence length. It would be beneficial to include a comparison of the decoding speed of the PF decoder with standard softmax sampling on various hardware platforms. Furthermore, the authors should investigate the memory footprint of the PF decoder, especially when dealing with large vocabulary sizes. This analysis should include both theoretical bounds and empirical measurements to provide a comprehensive understanding of the practical implications of using the PF decoder.

To strengthen the evaluation of the PF watermark, the authors should conduct a more extensive set of experiments. This should include evaluating the robustness of the watermark against various attacks, such as paraphrasing, translation, and adversarial modifications. The authors should also investigate the impact of different noise levels on the detection accuracy of the watermark. Furthermore, the authors should analyze the relationship between text length and watermark detection performance. It would be beneficial to provide a detailed analysis of the false positive and false negative rates of the watermark under different conditions. This would provide a more comprehensive understanding of the practical limitations and strengths of the proposed watermarking scheme.

Finally, the authors should consider exploring the potential trade-offs between watermark robustness and text quality. It is important to understand how the strength of the watermark affects the quality of the generated text. The authors should investigate whether increasing the watermark strength leads to a degradation in text quality. This analysis should include both quantitative metrics, such as perplexity and BLEU score, and qualitative assessments of the generated text. This would provide a more complete picture of the practical implications of using the PF watermark.

### Questions

1. How does the computational overhead of the PF decoder compare to standard softmax sampling in practice? Are there any specific hardware or software optimizations that can be applied to improve its efficiency?
2. How does the PF watermark perform in terms of robustness against various attacks, such as paraphrasing, translation, and adversarial modifications? What are the limitations of the proposed watermarking scheme in terms of detection accuracy and false positive rate?

### Rating

8

### Confidence

3

**********
