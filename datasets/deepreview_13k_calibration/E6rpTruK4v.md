# CodeUnlearn: Amortized Zero-Shot Machine Unlearning in Language Models Using Discrete Concept

- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 1, 5, 5, 5

## Abstract
Large Language Models (LLMs) offer extensive knowledge across various domains, but they may inadvertently memorize sensitive, unauthorized, or malicious data, such as personal information in the medical and financial sectors. Machine unlearning methods aim to remove specific information from models after training to address this. However, current approaches require additional model training or struggle to effectively erase particular data points and their associated context due to LLMs' complex, dense, and continuous nature. In this study, we propose a novel amortized unlearning approach using codebook features and Sparse Autoencoders (SAEs). By leveraging a bottleneck to decompose the activation space and regulate information flow, our method efficiently unlearns targeted information while preserving the model's performance on unrelated data. To the best of our knowledge, this is the first work that successfully enables unlearning specific topics with contextual relevance in an LLM, marking a significant step towards real-world applications of machine unlearning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper propose a method for training a language model that is able to "unlearn" specified topics. The method involves using a sparse auto-encoder, aka codebook, to disentangle the representation learned in attention layers. The unlearning is achieved by removing the learned codes linking mostly to the targeted topics.

### Strengths
1. The studied problem is interesting and meaningful

2. The paper focuses on generative machine translation tasks, not just discriminative classification

### Weaknesses
This paper has significant issues with the technical soundness and presentation / writing clarity. Details are as follows:

Regarding the method:

1. The paper did not mention what kind of LLM is compatible. Only in line 370, it mentions "a large language model", without concretely specifying it. Suppose the method is for normal multi-transformer layer LLMs, then which transformer layer(s) is the single bottleneck inserted into? It is unclear if this method is intended for encoder-only, decoder-only, or encoder-decoder architectures, and the implications for each are not discussed. The lack of specificity makes it difficult to assess the general applicability of the approach.

2. How to prevent the learned codes from collapse? There is no supervision signal to guide the learning of disentangled codes. Since interpretability is emphasized in the paper, how to ensure that the learned codes are for topics but not for other task-related semantics? The paper does not address the potential for the codebook to learn task-specific information unrelated to the intended topics, which could undermine the unlearning process. This is a critical issue for the method's validity.

3. For retrieving the codes for unlearning, it seems there is a need to create a controlled dataset. How is this dataset generated? If we can directly generate such dataset, why we need the proposed method for unlearning? Is the dataset only for training or for inference also? The paper does not explain the process for creating this controlled dataset, nor does it justify why this dataset is needed given the stated goal of zero-shot unlearning. The dependence on a controlled dataset raises questions about the method's practicality.

4. Since the proposed method requires a. joint training, and b. an extra controlled dataset for retrieval, how can the method be termed as "Zero-shot" as reflected in the title? There should be further detailed explanation on it in the paper. The claim of zero-shot unlearning is misleading given the method's reliance on a training phase and a controlled dataset. This discrepancy needs to be addressed.

Regarding experiments

5. The experiment section needs significant improvement. There is no concrete experiment settings. What LLMs, tasks, datasets is the method tested on? What is the statistics of the dataset? What does each experiment tell us? Currently all the analyses are mixed together without subsections. The lack of detailed experimental settings makes it impossible to reproduce the results or assess the method's effectiveness. The analysis is also disorganized, making it difficult to follow the key findings.

6. Key experiments are missing. The paper needs systematic experiments on ablation, parameter sensitivity study, case studies, and most importantly, analyses on the learned codebook. The absence of these crucial experiments limits the paper's ability to demonstrate the robustness and interpretability of the proposed method. A thorough exploration of these aspects is essential.

Regarding clarity

7. The writing of the paper is not clear, many key details are not clarified, such as those mentioned point 1.

8. In the one single case study, it's unable to be understood for readers who does not know the targeted language. Explanation is needed in the caption.

9. The results should be put closer to the corresponding analyses.

### Questions
Please see above. Significant revision is recommended for this paper before re-submission.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper introduces a zero-shot machine unlearning method to remove sensitive or unwanted data from a model without retraining. By using discrete representations and sparse autoencoders, it structures the latent space to enable targeted information removal while preserving model performance on unrelated data. Tis paper claims to be the first effective method for unlearning contextually specific topics in LLMs, aiming to make unlearning more scalable and practical.

### Strengths
The paper introduces a zero-shot unlearning approach that leverages vector quantization and discrete representations, enabling targeted information removal without retraining and enhancing scalability and efficiency.

### Weaknesses
The paper introduces a zero-shot unlearning approach that leverages vector quantization and discrete representations, enabling targeted information removal without retraining and enhancing scalability and efficiency.

The paper makes claims about unlearning in large language models (LLMs) but only evaluates its approach on sparse autoencoders rather than actual LLMs, raising questions about its applicability to LLMs as it stated. Additionally, it asserts novelty as "the first work that successfully enables unlearning specific topics with contextual relevance," yet overlooks significant existing research in machine unlearning. This overstatement of novelty, along with the lack of relevant evaluations, weakens the paper's contributions and claims.

### Questions
N/A

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a zero-shot unlearning method for language models using the concept of a codebook. The idea appears novel and is expected to be effective in unlearning. However, there are some questionable aspects in the model design. Additionally, the evaluation lacks comparisons with existing methods, raising concerns about the practicality of the proposed approach.

### Strengths
The idea of integrating the concept of a codebook into machine unlearning seems novel and sound.

### Weaknesses
1. The proposed method requires a special architecture and is not applicable to existing large language models (LLMs).
2. The methodology is unclearly structured and described (see Questions 1–7).
3. There is a lack of comparison with existing unlearning methods (see Questions 8-9).
4. There is insufficient analysis proving the benefit of the codebook concept (see Questions 10-11).

**Method**

1. **Relationship Between Sections 3.1 and 3.3**: What is the relationship between Section 3.1 (Equations 1–3) and Section 3.3 (Equations 4–7)? It appears that the only difference is the inclusion of two additional linear layers for encoding and decoding. It is unclear how the process in Section 3.1 is utilized in the overall pipeline beyond Section 3.3. What is the purpose of Section 3.1?

2. **Differentiability of Code Selection**: In the code selection process, the use of *argtopk* would cut off the gradient. How did you make this process differentiable to enable model training?

3. **Sensitivity to $S$ and $S'$**: The performance seems sensitive to the choice of $S$ and $S'$, while $S$ is set to 8 according to Appendix A. Is this number sufficient to represent the complex context of a long input consisting of at least 512 tokens? Additionally, as shown in the evaluation results, the trade-off between performance and unlearning success is highly variable. How can a user choose an appropriate $S$ and $S'$ in practice?

4. **Security Through ReLU**: In the "Security through ReLU" section (Section 3.3), why do you believe there would be information leakage in the encoding/decoding process that consists of a single linear layer? Can you provide a scenario where data integrity is compromised during the unlearning process without ReLU? How does ReLU mitigate this issue?

5. **L1 Penalty and Sparsity**: Why do you think the L1 penalty term promotes sparsity? Given that the code selection process uses cosine similarity, there might be a possibility that the scale of each code vector decreases, but this does not necessarily lead to sparsity.

6. **Requirement of $D_T$ and $D_\tilde{T}$**: Does a user always need to prepare both $D_T$ and $D_\tilde{T}$ for unlearning?

7. **Motivation for Using Equation 14**: What is the motivation for using Equation 14 as a description of enrichment? Are there other metrics that could avoid low-frequency scenarios without requiring an additional chi-squared test?


**Evaluation**

8. **Unlearning Performance Metrics**: Is "Normalized Improvement Drop" a commonly used metric for measuring unlearning performance? Are there standard metrics or benchmarks for assessing unlearning performance used in the papers of related works section?

9. **Comparison with Existing Methods**: Please provide a comparison with other existing unlearning methods. The methods mentioned in the related works section would be ideal candidates for this comparison.

10. **Quality of the Learned Codebook**: Have you verified the quality of the learned codebook?

11. **Relationship Between $D_T$ Quality/Size and Performance**: Have you investigated how the quality and size of $D_T$ affect unlearning performance? There may be additional interesting analyses to explore in this area.


**Minor Questions & Suggestions:**

12. **Placement of Code Selection Process**: Locating the code selection process after the residual connection is an important design consideration to prevent information leakage, but this is not mentioned in the main text (only in the caption of Figure 1). Could you elaborate on this in the paper?

13. **Complexity of Encoding/Decoding Layers**: Do you think a single linear layer with ReLU is sufficient for sparse encoding and decoding? Have you experimented with increasing the number of layers?

14. **Placement of Section 3.2**: It might be more appropriate to include Section 3.2 in the Related Work section. In the Method section, focusing on why the paper selects a single codebook and uses $S>1$ might be sufficient.

15. **Understandability of the Example**: The provided example is difficult to understand without knowledge of French. Consider using an example that is accessible to a broader audience.

### Questions
**Method**

1. **Relationship Between Sections 3.1 and 3.3**: What is the relationship between Section 3.1 (Equations 1–3) and Section 3.3 (Equations 4–7)? It appears that the only difference is the inclusion of two additional linear layers for encoding and decoding. It is unclear how the process in Section 3.1 is utilized in the overall pipeline beyond Section 3.3. What is the purpose of Section 3.1?

2. **Differentiability of Code Selection**: In the code selection process, the use of *argtopk* would cut off the gradient. How did you make this process differentiable to enable model training?

3. **Sensitivity to $S$ and $S'$**: The performance seems sensitive to the choice of $S$ and $S'$, while $S$ is set to 8 according to Appendix A. Is this number sufficient to represent the complex context of a long input consisting of at least 512 tokens? Additionally, as shown in the evaluation results, the trade-off between performance and unlearning success is highly variable. How can a user choose an appropriate $S$ and $S'$ in practice?

4. **Security Through ReLU**: In the "Security through ReLU" section (Section 3.3), why do you believe there would be information leakage in the encoding/decoding process that consists of a single linear layer? Can you provide a scenario where data integrity is compromised during the unlearning process without ReLU? How does ReLU mitigate this issue?

5. **L1 Penalty and Sparsity**: Why do you think the L1 penalty term promotes sparsity? Given that the code selection process uses cosine similarity, there might be a possibility that the scale of each code vector decreases, but this does not necessarily lead to sparsity.

6. **Requirement of $D_T$ and $D_\tilde{T}$**: Does a user always need to prepare both $D_T$ and $D_\tilde{T}$ for unlearning?

7. **Motivation for Using Equation 14**: What is the motivation for using Equation 14 as a description of enrichment? Are there other metrics that could avoid low-frequency scenarios without requiring an additional chi-squared test?

\
**Evaluation**

8. **Unlearning Performance Metrics**: Is "Normalized Improvement Drop" a commonly used metric for measuring unlearning performance? Are there standard metrics or benchmarks for assessing unlearning performance used in the papers of related works section?

9. **Comparison with Existing Methods**: Please provide a comparison with other existing unlearning methods. The methods mentioned in the related works section would be ideal candidates for this comparison.

10. **Quality of the Learned Codebook**: Have you verified the quality of the learned codebook?

11. **Relationship Between $D_T$ Quality/Size and Performance**: Have you investigated how the quality and size of $D_T$ affect unlearning performance? There may be additional interesting analyses to explore in this area.

\
**Minor Questions & Suggestions:**

12. **Placement of Code Selection Process**: Locating the code selection process after the residual connection is an important design consideration to prevent information leakage, but this is not mentioned in the main text (only in the caption of Figure 1). Could you elaborate on this in the paper?

13. **Complexity of Encoding/Decoding Layers**: Do you think a single linear layer with ReLU is sufficient for sparse encoding and decoding? Have you experimented with increasing the number of layers?

14. **Placement of Section 3.2**: It might be more appropriate to include Section 3.2 in the Related Work section. In the Method section, focusing on why the paper selects a single codebook and uses $S>1$ might be sufficient.

15. **Understandability of the Example**: The provided example is difficult to understand without knowledge of French. Consider using an example that is accessible to a broader audience.

### Soundness
3

### Presentation
2

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
This paper aims to address a critical issue in the deployment of Large Language Models (LLMs): the inadvertent memorization of sensitive or unauthorized data, a highly relevant topic, especially given the increasing use of LLMs in domains where data privacy is paramount. To this end, the authors introduce a novel amortized unlearning approach using codebook features and Sparse Autoencoders (SAEs). Finally, some experiments are conducted to verify the effectiveness of the proposed method.

### Strengths
The method is designed to unlearn targeted information efficiently without additional model training. This is an advantage over existing approaches that often necessitate retraining, which can be computationally expensive and time-consuming.

The proposed method is simple yet effective, and the experimental results are decent.

### Weaknesses
From a methodology point of view, the proposed approach is to remember what should be unlearned rather than to unlearn something. Namely, if we take the whole model as a system, no sensitive knowledge is removed, while the authors claim in the abstract section that machine learning methods aim to remove specific information.

It is unclear why Sparse Autoencoder is employed here and why it works.

### Questions
Leveraging sensitive knowledge to avoid utilizing sensitive information can be a bit confusing. What if the employed information is forbidden to use?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel approach called "CodeUnlearn" for zero-shot machine unlearning in LLMs. The primary contribution is leveraging codebook features combined with sparse autoencoders (SAEs) to achieve efficient, targeted removal of specific information from models without the need for retraining. This method addresses the challenges of handling complex language tasks, preserving model performance while selectively unlearning sensitive or unwanted data.

### Strengths
1. The paper introduces a new method using discrete representations (codebook features), which is a step forward in the machine unlearning space, particularly for LLMs.

2. The amortized zero-shot unlearning technique scales well with large models, unlike traditional retraining-based methods that are computationally expensive and inefficient.

3. The paper presents experimental results with various metrics (e.g., BLEU, METEOR, BERTScore) to assess the unlearning procedure's effectiveness across different topics.

### Weaknesses
1. The writing quality is poor, with typos, errors, and incomplete sentences.

2. The paper lacks thorough and empirical comparisons with other machine unlearning methods, including zero-shot unlearning techniques.

3. The evaluation focuses heavily on metrics like BLEU and BERTScore, which may not capture all dimensions of model quality, such as fluency or overall task accuracy after unlearning.

4. There are no ablation studies to evaluate the importance of different components in the unlearning pipeline, making it hard to assess which part of the method contributes most to its success.

5. The paper lacks specific details on how the codebook and sparse autoencoder (SAE) are implemented, making it difficult to reproduce the experiments.

6. The discussion lacks sufficient consideration of the risks of unintentionally removing valuable information during the unlearning process. The procedure may negatively impact semantically related concepts (e.g., unlearning "love" also affecting performance on "like").

### Questions
1. Can more baselines, including zero-shot unlearning methods, be added to highlight the method's comparative effectiveness?

2. Could additional metrics, like human evaluations or task accuracy, be used to better capture fluency and performance post-unlearning?

3. Can the authors provide ablation studies to clarify the impact of individual components?

4. Could the authors help better understand the risks of unintentionally removing valuable information during the unlearning process?

### Soundness
3

### Presentation
2

### Contribution
2
