### Summary

This paper introduces a decoding method that aims to align generated text with human text across multiple aspects. The method involves minimizing the reverse KL divergence between the model's distribution and the human text distribution, subject to constraints on expected metric scores. The authors provide theoretical guarantees and demonstrate the effectiveness of their method through experiments on various domains and model scales.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel approach to decoding that considers multiple aspects of text generation simultaneously, which is a departure from traditional methods that focus on individual aspects.
2. The authors provide theoretical guarantees for their method, which adds credibility to their approach.
3. The experimental results are comprehensive and demonstrate the superiority of the proposed method over strong baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not extensively discuss the limitations of the proposed method. It would be beneficial to explore scenarios where the method might not perform well or to compare its performance on a wider range of tasks and datasets. Specifically, the reliance on a development set for estimating the coefficients $\boldsymbol{\mu}$ raises concerns about the method's robustness to distributional shifts. If the distribution of the development set differs significantly from the test set or the distribution of human-written texts, the estimated coefficients might not be optimal, potentially leading to suboptimal performance. Furthermore, the paper does not explore the sensitivity of the method to the size and quality of the development set, which is a critical factor in the practical application of the method.
2. The paper could provide more details on the computational cost of the proposed method compared to baseline methods. While the authors mention that the method is efficient, a more detailed analysis of the time and memory requirements would be helpful for practitioners. The paper lacks a detailed breakdown of the computational overhead introduced by the Sampling-Importance-Resampling (SIR) technique, particularly in terms of the number of samples required for effective resampling and the impact of this on overall decoding time. A comparison of the computational cost with and without SIR would be valuable.
3. The paper could benefit from a more in-depth discussion of the choice of evaluation metrics and their correlation with human judgment. While the paper uses a set of automatic evaluation metrics, it would be helpful to discuss the limitations of these metrics and how well they capture the nuances of human text generation. The paper does not adequately address the potential biases or limitations of the chosen metrics, such as their sensitivity to specific linguistic features or their ability to capture higher-level semantic properties of text. A more thorough discussion of the validity and reliability of these metrics in the context of evaluating text generation would be beneficial.

### Suggestions

The paper should include a more thorough investigation into the limitations of the proposed DAEEMON method. Specifically, the authors should explore the method's performance under various distributional shifts between the development set used for estimating the coefficients and the test set. This could involve experiments where the development set is drawn from a different domain or has a different statistical distribution than the test set. Additionally, the sensitivity of the method to the size and quality of the development set should be analyzed. For example, the authors could investigate how the performance of DAEEMON changes as the size of the development set is reduced or when the development set contains noisy or low-quality samples. This analysis would provide a more complete understanding of the method's robustness and practical applicability. Furthermore, the authors should consider comparing the performance of DAEEMON on a wider range of tasks and datasets, including those that are more challenging or have different characteristics than the Wikipedia and News domains. This would help to identify the strengths and weaknesses of the method and its potential for generalization.

To address the concerns about computational cost, the authors should provide a detailed breakdown of the time and memory requirements of the DAEEMON method, including a comparison with baseline methods. This analysis should include the computational overhead introduced by the SIR technique, particularly in terms of the number of samples required for effective resampling and the impact of this on overall decoding time. The authors should also investigate the trade-off between the number of samples used in SIR and the quality of the generated text. For example, they could analyze how the performance of DAEEMON changes as the number of samples is varied and identify the optimal number of samples that balances computational cost and generation quality. A comparison of the computational cost with and without SIR would also be valuable to understand the impact of this technique on the overall efficiency of the method. This analysis should be presented with clear quantitative data, such as wall-clock time and memory usage, for different model sizes and sampling parameters.

Finally, the paper should include a more in-depth discussion of the choice of evaluation metrics and their correlation with human judgment. The authors should discuss the limitations of the chosen metrics and how well they capture the nuances of human text generation. This discussion should include an analysis of the potential biases or limitations of the metrics, such as their sensitivity to specific linguistic features or their ability to capture higher-level semantic properties of text. The authors should also consider using additional evaluation metrics that are more closely aligned with human judgment, such as metrics that measure the coherence, fluency, and informativeness of the generated text. Furthermore, the authors should provide a more detailed analysis of the correlation between the automatic evaluation metrics and human ratings, including a discussion of any discrepancies or inconsistencies. This analysis should help to validate the effectiveness of the chosen metrics and provide a more comprehensive evaluation of the proposed method.

### Questions

1. How does the performance of DAEEMON vary with different language model architectures and sizes? Are there any specific model characteristics that significantly impact the effectiveness of the method?
2. The paper mentions that the coefficients $\boldsymbol{\mu}$ are estimated on a small development set. How sensitive is the method to the size and quality of this development set? What are the practical considerations for selecting an appropriate development set?
3. The paper uses a set of automatic evaluation metrics to assess the quality of generated texts. How well do these metrics correlate with human judgment? Are there any limitations to using these metrics for evaluating text generation?
4. The paper introduces the Sampling-Importance-Resampling (SIR) technique for tractable sampling. How does the performance of DAEEMON vary with different numbers of samples used in SIR? What is the trade-off between computational cost and generation quality?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
