# A Watermark for Low-entropy and Unbiased Generation in Large Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Recent advancements in large language models (LLMs) have highlighted the risk of misusing them, raising the need for accurate detection of LLM-generated content. In response, a viable solution is to inject imperceptible identifiers into LLMs, known as watermarks. Previous work demonstrates that unbiased watermarks ensure unforgeability and preserve text quality by maintaining the expectation of the LLM output probability distribution. However, previous unbiased watermarking methods suffer from one or more of the following issues: (1) requiring access to white-box LLMs during detection, (2) incurring long detection time, (3) being not robust against simple watermarking attacks, (4) failing to provide statistical guarantees for the type II error of watermark detection, and (5) being not statistically unbiased for low-entropy scenarios, which hinder their deployment in practice. This study proposes the Sampling One Then Accepting (STA-1) method, a watermark that can address all of these issues. Moreover, we discuss the tradeoff between watermark strength and text quality for unbiased watermarks. We show that in low-entropy scenarios, unbiased watermarks face a tradeoff between watermark strength and the risk of unsatisfactory outputs. Experimental results on both low-entropy and high-entropy datasets demonstrate that STA-1 achieves text quality and watermark strength comparable to existing unbiased watermarks, with a low risk of unsatisfactory outputs. Implementation codes for this study are available online

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a pattern-based watermarking framework specifically designed for order-agnostic LMs. The experiments on ProteinMPNN and CMLM demonstrate PATTERN-MARK’s efficiency, generation quality, and robustness.

### Strengths
1.	Clarity: The article is written clearly and logically.

2.	Originality: This is the first work to explore watermarking for order-agnostic LMs.

3.	Significance: The proposed watermark is designed for order-agnostic LMs, which are popular architectures in diverse real-world applications. Therefore, to a certain extent, this work is of practical significance.

### Weaknesses
1.	What are the advantages of this method compared to the traditional modification-based watermark (generate content first and then embed watermark)?
2.	How can this method be extended to multi-bit watermarking, which is more applicable in real-world scenarios?

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a watermarking method, Sampling One Then Accepting (STA), an unbiased watermark designed to effectively balance watermark strength and text quality, especially in low-entropy scenarios. The paper also introduces an extension, STA-M, which further enhances watermark strength while maintaining acceptable text quality. Additionally, STA does not require white-box access to models, making it more accessible for practical applications. It is also robust against watermarking attacks.

### Strengths
1. The paper theoretically analyze the problem of  balancing between text quality and detection performance in existing unbiased watermarks under low-entropy scenarios.
2. It provides theoretical proofs of STA's unbiasedness and guarantees regarding Type II error, etc.

### Weaknesses
1. Unclear Contribution Hierarchy: The paper lacks clarity in distinguishing its main contributions, leading to a somewhat confusing narrative. And the experiment results cannot clearly support the theoretical analysis.
 - The key contributions should emphasize that (1) unbiased watermarks claim to outperform traditional red-green watermarks in preserving text quality, but the authors find no significant advantage in low-entropy scenarios, and (2) the proposed watermark aims to alleviate this issue.
- However, results from Tables 1 and 2 do not support the first claim. In fact, there is no clear distinction in the ability of red-green and unbiased watermarks to preserve text quality across high and low entropy scenarios.
- The performance of STA compared to other unbiased watermarks is not significantly superior.
2. Confusing Presentation of Results: The experimental results are presented in a confusing manner, particularly with multiple best and second-best results highlighted, which complicates interpretation.
3. Insufficient Testing of Text Quality: The evaluation of text quality is inadequate, especially in low-entropy scenarios, as it relies solely on code generation tasks, limiting the scope of the findings.

### Questions
See the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel unbiased watermarking method for large language models, named Sampling One Then Accepting (STA-1), which offers statistical guarantees regarding type II errors in watermark detection. The authors also address the tradeoff between watermark strength and text quality, presenting STA-M as an extension of STA-1 that enhances watermark strength with low text quality shifts. They demonstrate the empirical performance and robustness of the method through experiments conducted on the C4 and HumanEval datasets.

### Strengths
1. This paper proposes a novel watermarking method called Sampling One Then Accepting (STA-1) that is unbiased and robust, requiring no access to white-box large language models during detection.

2. This paper also introduces STA-M, an extension of STA-1 that enhances watermark strength with low text quality shifts

### Weaknesses
1. There is no significant difference in text quality between the proposed STA-1 and other unbiased watermarking methods on both the HumanEval and C4 datasets. This is expected, as they are all distortion-free, resulting in text quality that is similar to the no-watermark baseline.

2. AUC is not an ideal metric for these experiments. It would be more informative to provide direct results such as true positive rates at very low false positive rates, such as 0.1%, 0.01%, and 0.001%. In real-world applications, the cost of false positives is significantly high, making it essential to focus on results with very low false positive rates.

3. Results on the C4 dataset indicate that the detection performance of STA-1 on high-entropy datasets shows no improvement compared to current unbiased baselines. Additionally, the proposed STA-M is outperformed by KGW in terms of both text quality and watermark strength.

4. The AUC scores for the HumanEval dataset are too low, leading me to suspect that the true positive rates may also be very small. This suggests that all of these methods may not be useful for low-entropy datasets.

In summary, I believe this paper proposes a novel method that yields results comparable to current baselines but shows little to no improvement in performance.

### Questions
Could you provide the results for smaller values of $\alpha$ (e.g., 0.1 and 0.2) for Dipmark in Table 3? Since Dipmark also involves a trade-off between watermark strength and text quality, a lower $\alpha$ may resemble the original unwatermarked distribution and could potentially perform better than STA-1. Additionally, Dipmark retains the unbiased property, whereas STA-M does not.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a modification to the watermark of Kirchenbauer et al. [1] in which logit perturbations are replaced with rejection sampling at the token level. The authors explore two variants of this scheme: STA-1, in which at most one red-list token is rejected at each generation step, and STA-M, in which up to M red-list tokens are rejected at each step if an entropy threshold on the token distribution is satisfied. The authors show that for the generation of low-entropy text, the proposed method allows for higher quality while maintaining similar robustness to existing watermarks.
[1] https://arxiv.org/abs/2301.10226 (https://arxiv.org/abs/2301.10226)

### Strengths
1) Exploring the low-entropy generation setting is interesting
2) Using the entropy of the token distribution to govern watermark embedding is a good idea, although existing methods (e.g. the fixed-magnitude logit perturbation proposed by Kirchenbauer et al.) already do this implicitly
3) Evaluating watermarked text quality through the risk of unsatisfying outputs is an interesting idea and a natural fit for reasoning / question-answering tasks

### Weaknesses
1. The writing is problematic. For example, in Hu et al (see its appendix), the unbiased watermarking method also has the model-agnostic detection method which does not require the white box language model. If you consider this into your manuscript, the first problem identified in the abstract would be void.
2. Is it really necessary to discuss the very low entropy scenario? The example you showcased is not common in real life. From my understanding, it would be most likely that the model is prompted to repeat the prompt, so the entropy is very low. Can we expect the watermark are added in this scenario, what is the rational behind it?

### Questions
Same as the weakness. The authors proposed valuable insights about designing unbiased watermark with type II error guarantee, however, the motivation they showed is not satisfying and can be re-organized. I would be happy to raise my score if the authors can think of a better way to present their work.

### Soundness
3

### Presentation
3

### Contribution
3
