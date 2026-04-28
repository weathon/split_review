# MergePrint: Robust Fingerprinting against Merging Large Language Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
As the cost of training large language models (LLMs) rises, protecting their intellectual property has become increasingly critical.
Model merging, which integrates multiple expert models into a single model capable of performing multiple tasks, presents a growing risk of unauthorized and malicious usage.
While fingerprinting techniques have been studied for asserting model ownership, existing methods have primarily focused on fine-tuning, leaving model merging underexplored.
To address this gap, we propose a novel fingerprinting method \textsc{MergePrint} that embeds robust fingerprints designed to preserve ownership claims even after model merging.
By optimizing against a \textit{pseudo-merged model}, which simulates post-merged model weights, \textsc{MergePrint} generates fingerprints that remain detectable after merging.
Additionally, we optimize the fingerprint inputs to minimize performance degradation, enabling verification through specific outputs from targeted inputs. 
This approach provides a practical fingerprinting strategy for asserting ownership in cases of misappropriation through model merging.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents MERGEPRINT, a fingerprinting method for large language models (LLMs) aimed at protecting against unauthorized use via model merging. Unlike traditional approaches that focus on fine-tuning, MERGEPRINT embeds resilient fingerprints specifically designed to persist through merging. By using a pseudo-merged model to simulate post-merge conditions, MERGEPRINT generates optimized input-output fingerprint pairs that remain detectable post-merging. The two-step optimization process for inputs and parameters minimizes performance loss and ensures reliable fingerprint retention across merging ratios. Experiments confirm MERGEPRINT’s effectiveness and robustness, with high fingerprint retention and minimal impact on model performance.

### Strengths
- This paper focuses on a fingerprinting method for large models specifically designed to withstand model merging, providing a new perspective for research in this area.
- Through relatively detailed experiments, the robustness, effectiveness, and harmlessness of the proposed method are demonstrated within specific experimental settings.
- The paper is well-structured and logically coherent, with detailed descriptions of the methodology and experimental setup, providing strong support for reader comprehension.

### Weaknesses
 - The method is overly simplistic, simulating resistance to model merging merely through weighted coefficient addition, lacking both innovation and theoretical proof of effectiveness.
- The setting is limited, as the approach can only be applied to merging scenarios involving models derived from the same source. Additionally, the experiments are restricted to three merging techniques: Task-Arithmetic, TIES-merging, and DARE, limiting the generalizability of the results.
- There are too few baseline methods used for comparison.
- The robustness experiments are relatively simple, embedding only one watermark in a single model during multi-model merging. It would be valuable to understand how the method performs with multiple models and multiple fingerprints.
- There is a lack of experiments addressing basic adversarial attacks, such as an overwriting attack by adversaries.
- The explanation for the choice of regularization coefficient $lambda$ and the two merging coefficients is limited to the methodology section, with no experimental analysis on these parameters in the results section.

### Questions
- Could you provide theoretical justification for using weighted coefficient addition to ensure fingerprint robustness in model merging?
- Have you considered testing MERGEPRINT in more complex or cross-origin model merging scenarios beyond Task-Arithmetic, TIES-merging, and DARE?
- Are there plans to include more baseline methods for a comprehensive evaluation?
- How does MERGEPRINT perform with multiple fingerprints embedded in multiple models in multi-model merging scenarios?
- Have you tested MERGEPRINT's resilience against basic adversarial attacks, such as overwriting?
- Could you provide experimental analysis on the impact of regularization coefficient $lambda$ and merging coefficients?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper "MERGEPRINT: Robust Fingerprinting Against Merging Large Language Models" addresses the critical issue of protecting the intellectual property of large language models (LLMs) in the context of model merging. Model merging, which combines multiple expert models into a single model capable of performing multiple tasks, poses a significant risk of unauthorized and malicious usage. The authors propose a novel fingerprinting method, MERGEPRINT, which embeds robust fingerprints designed to preserve ownership claims even after model merging. The method optimizes against a pseudo-merged model to generate fingerprints that remain detectable post-merging. Additionally, the paper optimizes fingerprint inputs to minimize performance degradation, enabling verification through specific outputs from targeted inputs.

### Strengths
1. **Novelty and Relevance**: The paper introduces a new approach to fingerprinting that specifically targets the challenge of model merging, which is a growing concern in the field of large language models.
2. **Robustness**: The proposed method is designed to be robust against model merging, ensuring that the fingerprints remain detectable even after the models are combined.
3. **Practicality**: The method minimizes performance degradation, making it a practical solution for real-world applications where maintaining model performance is crucial.
4. **Verification**: The paper provides a clear verification procedure using the Verification Success Rate (VSR) metric, which measures the effectiveness of the fingerprinting method.
5. **Experimental Validation**: The authors conduct extensive experiments to validate the effectiveness of MERGEPRINT, demonstrating its robustness, harmlessness, effectiveness, reliability, efficiency, and confidentiality.

### Weaknesses
1. **Confidentiality Concerns**: The paper acknowledges that highly memorized fingerprints with extremely low loss may still be vulnerable to adversarial attacks, such as membership inference. This is a significant limitation, as it undermines the security of the fingerprinting method. The vulnerability to membership inference attacks is particularly concerning because it could allow an adversary to determine whether a specific model contains a given fingerprint, potentially enabling the removal or circumvention of the fingerprint. The paper does not sufficiently address how the fingerprint input-output pairs are generated and whether these pairs could be reverse-engineered or guessed by an attacker with knowledge of the model architecture and training data.

2. **Lack of Formal Validation**: The process of verifying ownership claims through fingerprinting lacks formal validation. The authors do not utilize formal methods or cryptographic techniques, which could strengthen the credibility of the ownership claims. The absence of formal validation makes it difficult to establish a strong, legally defensible claim of ownership. The reliance on statistical significance alone may not be sufficient to convince a court or other legal body of ownership, especially if the fingerprinting method is not widely accepted or understood.

3. **Efficiency Trade-offs**: While the paper claims that the fingerprinting procedure is efficient, the trade-off between efficiency and robustness is not thoroughly explored. For instance, the use of a low learning rate (1e-6) and the early stopping approach might lead to suboptimal results in some scenarios. The paper does not provide a detailed analysis of how these parameters affect the robustness of the fingerprint. It is unclear whether the low learning rate is optimal for all models and merging scenarios, or if it might lead to underfitting or a failure to embed a sufficiently robust fingerprint. Similarly, the early stopping approach, while potentially preventing fingerprint transfer, may also prematurely terminate the fingerprinting process, resulting in a weaker fingerprint.

4. **Generalizability**: The paper does not provide extensive evaluations across a diverse range of models and merging scenarios. The effectiveness of MERGEPRINT in more complex and varied environments remains uncertain. The paper's evaluation is limited to a specific set of models and merging techniques. It is unclear whether the method would perform equally well on models with different architectures, training data, or merging strategies. The lack of diverse evaluations makes it difficult to assess the general applicability of MERGEPRINT.

5. **Ethical Considerations**: The paper mentions the potential for malicious exploitation of the embedded secret information, but it does not delve deeply into the ethical implications and safeguards needed to prevent such misuse. The paper does not explore the potential for malicious actors to use the fingerprinting method to embed harmful or biased information into models. The lack of discussion on ethical implications and safeguards raises concerns about the responsible use of the proposed method.

### Questions
1. **Scalability**: How well does MERGEPRINT scale to larger models and more complex merging scenarios? Are there any computational or resource limitations that need to be addressed?
2. **Adversarial Robustness**: Can the method be extended to defend against more sophisticated adversarial attacks beyond membership inference? What additional measures can be taken to enhance the robustness of the fingerprints?
3. **Formal Methods**: Is it feasible to integrate formal methods or cryptographic techniques into the fingerprinting process to provide stronger guarantees of ownership and security?
4. **Real-World Applications**: How can MERGEPRINT be integrated into existing model deployment pipelines without disrupting the workflow or introducing significant overhead?
5. **User Privacy**: What are the potential privacy implications of embedding secret information into models, and how can user data be protected from potential leaks?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new model fingerprinting method to protect model ownership against model merging attacks. The proposed MergePrint method works by optimizing the fingerprint input and embedding process against a pseudo-merged model to ensure the fingerprint embedded in a model survives the model merging operation. Empirical results show MergePrint is effective and can correctly verify the embedded fingerprint in the merged model and outperforms the prior work.

### Strengths
This paper has the following strengths: 
+ The authors propose a robust model fingerprinting method that provides proof of model ownership against the model merging scenarios. 
+ The authors develop a two-step optimization approach to ensure that MergePrint meets the harmfulness and reliability criteria.
+ Empirical results on LLaMA models show that MergePrint can verify the fingerprint for up to the merge of seven models and against a variety of merging ratios.

### Weaknesses
This paper has the following weaknesses:
- The related works in Section 1.1 are not sufficiently discussed. For example, the authors only talk about prior works on black-box model fingerprinting in Section 1.1. There are also a lot of works that embed fingerprints in the model weights (i.e., white-box setting). Furthermore, the problem of model ownership proof against model merging is more similar to model watermarking/fingerprinting in the federated learning setting (which has model aggregation that is similar to model merging). The authors should discuss the similarities and differences between the prior works in the FL setting and the one in this paper.
- The evaluation seems to be incomprehensive. For example, Section 5.2 mentions that the fingerprint y='transformers' in the model. It's not clear whether the performance of MergePrint is impacted by y. Also, the optimized fingerprint input x is not given.

### Questions
Please consider addressing the weak points mentioned above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a model fingerprinting method named MergePrint to provide robust ownership verification against the model merge. Specifically, MergePrint utilized the pseudo-merged model that mimics the merged model to generate the model fingerprint. MergePrint also proposed a two-step optimization including input optimization and parameter optimization to optimize both the input sample and the model.

### Strengths
1. The embedded fingerprint is robust against model merge.
2. This paper is easy to read.

### Weaknesses
1. Missing important related works. The method of this paper is a backdoor-based model ownership verification method that intends to embed a specific behavior into the model. However, there have been some works investigating backdoor attacks against model merge (e.g., [1]). There are also many works focusing on watermarking LLMs in ways other than weight watermarking [2,3,4]. It may be better for the authors to include a discussion on these related works.
2. Missing optimization details. This paper proposes a two-step optimization. However, it is not clear whether the two steps are performed alternatively in each epoch or whether the second step will be performed after the first one is completed. Additionally, this paper lacks a detailed description of the experimental settings, including the hyperparameters and the hardware.
3. Missing hyperparameter study. This paper introduces two important hyperparameters, $\alpha_x$ and $\alpha_w$. These two hyperparameters may have a great impact on the effectiveness of this paper. The authors should present a hyperparameter study to investigate the impact of these hyperparameters.
4. Insufficient ablation study. This paper presents the ablation study of the input optimization step. The authors should also conduct an ablation study on the parameter optimization step. Also, it may be better to investigate the effect of the pseudo-merged model (i.e., perform the two-step optimization only on the fine-tuned model).
5. The robustness of the fingerprint is not guaranteed. Although MergePrint is robust against model merge and the authors claim that fine-tuning is out of the scope, it does not mean that fine-tuning is not important in the real-world scenario. I highly recommend the authors conduct a study of the robustness of MergePrint against a wide range of attacks, such as fine-tuning, pruning, and distillation. If MergePrint can not resist these attacks, it should be noted as a limitation of this paper.
6. Insufficient analysis of efficiency. The authors should report the time or the time complexity of MergePrint to help the readers better understand its efficiency.
7. Typos and grammatical mistakes. There are some typos and grammatical mistakes in this paper (e.g., lines 223-224). It may be better for the authors to proofread the paper and correct potential mistakes.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
