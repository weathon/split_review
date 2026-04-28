# WAPITI: A Watermark for Finetuned Open-Source LLMs

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
Watermarking of large language models (LLMs) generation embeds an imperceptible statistical pattern within texts, making it algorithmically detectable. 
Watermarking is a promising method for addressing potential harm and biases from LLMs, as it enables traceability, accountability, and detection of manipulated content, helping to mitigate unintended consequences. 
However, for open-source models, watermarking faces two major challenges: 
(1) incompatibility with fine-tuned models
(2) vulnerability to fine-tuning attacks.
In this work, we propose WAPITI, a new method that transfers watermarking from base models to fine-tuned models through parameter integration.
To the best of our knowledge, we are the first to embed watermarks into fine-tuned model parameters and preserve their fine-tuned capabilities. 
Furthermore, our approach offers an effective defense against fine-tuning attacks. 
We test our method on various model architectures and watermarking strategies. 
Results demonstrate that our method can successfully inject watermarks and is highly compatible with fine-tuned models. 
Additionally, we offer an in-depth analysis of how the strength of 
parameter editing influences the watermark strength and overall capabilities of the resulting models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces WAPITI, a watermarking method for fine-tuned open-source LLMs. It embeds watermarks directly into model parameters, ensuring robustness against fine-tuning without additional training. Experiments show that WAPITI maintains watermark detectability with minimal performance impact, supporting traceability in open-source AI models.

### Strengths
This paper presents WAPITI, a watermarking method for fine-tuned, open-source LLMs that embeds watermarks directly in model parameters, aiming for robustness against fine-tuning. The approach is somewhat novel, addressing a recognized challenge in model traceability with a parameter-based watermarking solution that does not require additional training.

### Weaknesses
1.	While the end watermarking algorithm is very simple, it relies on multiple approximations and heuristic observations of the experimental results. Such as the orthogonality between the parameter differences. This may undermine the theoretical rigor and precision of the proposed method. The reliance on approximations, particularly in assuming orthogonality of parameter differences, needs more rigorous justification. The method's performance could be highly sensitive to deviations from this assumption, especially in complex, high-dimensional parameter spaces of large language models. Furthermore, the heuristic nature of parameter selection for watermarking raises concerns about the method's robustness across different model architectures and training regimes. A more principled approach to parameter selection, potentially guided by sensitivity analysis or information theoretic measures, would be beneficial.
2.	The experimental validation appears somewhat limited, with relatively few comparisons to other state-of-the-art watermarking methods. This raises questions about the generalizability and robustness of WAPITI. Therefore, the overall contribution may be incremental, and broader validation would strengthen its significance. The comparison to only AAR and KGW is insufficient to establish the superiority or even the competitiveness of WAPITI. A more comprehensive evaluation should include a wider range of watermarking techniques, especially those designed for parameter-based watermarking. Furthermore, the evaluation should consider different types of attacks, such as model pruning, quantization, and adversarial fine-tuning, to assess the robustness of the watermark under various scenarios. The current evaluation lacks a thorough analysis of the trade-off between watermark detectability and model performance across different tasks and datasets.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present a watermarking technique for open-weight LLMs that involves interpolating between the parameters of non-watermarked and watermarked models. Preserving the capabilities of open-source models is a challenge when embedding a watermark. The authors show a controllable way of injecting the watermark with limited loss in the model's capabilities. Their method entails training a distilled, watermarked base model and adjusting the parameters of a fine-tuned model along the path between the non-watermarked and watermarked base models. The authors assess their method's detectability and generation quality using two well-known watermarking techniques.

### Strengths
- The method is relatively simple but provides a method of embedding a watermark with a controllable loss in text generation capabilities

- The approach is motivated and presented clearly. 

- The experiments in the paper appear sound.

### Weaknesses
 - The paper's main contribution is fairly limited. Equations 4-13 can be added to the appendix as they are relatively straightforward. The idea of interpolating between parameters to control the strength of a modification has been applied before (e.g., in LoRA [B]).

- The paper is missing a threat model. Assume the user has access to the base model. Then they can invoke Algorithm 1, obtain $\Delta \theta_{Base}$ and undo the watermark. This is a significant oversight, as it renders the watermark easily removable if the base model is accessible, which is a reasonable assumption for open-source models.

- The authors claim that distillation impacts the model's math capability for Llama-2-7B while their approach has a controllable trade-off. What parameters did the authors use for distillation, and do distillation parameters exist that have a lower impact on the model's (math) capabilities? The authors need to provide a detailed analysis of the distillation process, including the specific datasets, hyperparameters, and training procedures used, and explore whether alternative distillation strategies could mitigate the observed performance degradation in mathematical reasoning.

- The authors' claim that they are the first to distil watermarks is confusing. As the authors themselves correctly state in the introduction, Gu et al. [A] can distil a watermark from one "base" model into another "fine-tuned" model. The authors state that they are the first to additionally achieve the preservation of the model's "fine-tuned capabilities," but this property is not well defined and can be challenged. The notion of preserving "fine-tuned capabilities" needs to be rigorously defined, ideally with a quantitative metric, and the authors need to demonstrate that their method demonstrably preserves these capabilities better than existing methods.

- I do not understand how the method is considered train-free if it has to invoke the watermark distillation algorithm as a subroutine (see Algorithm 1). The authors need to clarify the "train-free" claim, as the distillation process itself involves training. It would be more accurate to describe the method as requiring a single distillation step for the base model, which can then be applied to multiple fine-tuned models.

- The authors do not evaluate the robustness of their approach. The absence of robustness analysis is a critical weakness. The authors should evaluate the watermark's resilience to common attacks, such as text editing, paraphrasing, and changes in decoding parameters (e.g., temperature scaling).

- The authors do not ablate over the effect of the hyperparameter $\lambda$ on the watermark detectability and accuracy on MMLU or GSM8k, which I believe could strengthen the paper. A thorough ablation study of $\lambda$ is necessary to understand its impact on both watermark detectability and model performance. This should include a range of $\lambda$ values and their effects on metrics like p-values for detection, MMLU accuracy, and GSM8k accuracy.

### Questions
Please see above.

### Soundness
4

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the challenge of watermarking the weights of fine-tuned large language models (LLMs). Traditional watermarking techniques often degrade the performance of fine-tuned models, prompting the need for a new approach. The authors propose a novel method that involves embedding the watermark into a base model and subsequently applying the weight delta between the base and the watermarked base model to the fine-tuned model. This technique preserves the quality of the fine-tuned model while ensuring the watermark remains detectable.

### Strengths
Watermarking open source LLMs is an important topic. The fact that finetuned LLMs are hard to watermark is an interesting observation. 
The propose method makes it possible to watermark fine-tuned models just by one operation of the weights

### Weaknesses
The experiments presented in the paper are insufficient and lack detailed explanation and evidence.

- In Figure 2, the authors highlight a key weakness of watermarking fine-tuned models by demonstrating that training on watermarked mathematical data reduces performance. However, mathematics is notoriously difficult to watermark due to its low entropy, making this a cherry-picked example where failure is expected. The authors could have employed watermarks specifically designed for low-entropy text, as suggested in [1].
- The approach of fine-tuning a non-watermarked model on watermarked mathematical data as a baseline seems counterintuitive. The authors should demonstrate that a pre-trained watermarked model, when fine-tuned on mathematical data, does not exhibit watermark detectability. This would provide a more convincing baseline. The authors only cite Gu et al. as evidence that fine-tuning a watermarked base model removes the watermark.  But [2] show that it is pretty resilient. 
- Section 3.2 in my opinon excessive to intuitively justify Equation 13.
- Table 2 is lacking critical information. The p-values of 0.5 appear to be expected rather than computed, but it is crucial to show that the tests yield random p-values under the null hypothesis (H0) to confirm that the scores are accurately computed. The authors do not specify which scoring method they use: for Kirchenbauer, is it binomial or z-score based? Additionally, how many tokens are scored? Do the authors perform appropriate deduplication to get reliable p values?
- The reason it is easier to distill with kgw-k1 than aar-k2 is not due to the method itself but rather the window size, as discussed in [2].

### Questions
see weaknesses.

- 1.3M samples necessary for distillation? what does sample mean? for what method, which window size etc?

### Soundness
2

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
The paper addresses the watermarking issues associated with open-source large language models by proposing a novel parameter integration method that facilitates the migration of watermarks from the base model to the fine-tuned model. This approach effectively avoids the performance degradation and high computational costs typically associated with watermark distillation. Building upon the watermark distillation method outlined in Gu2024, the paper resolves the incompatibility issues with fine-tuning and the inability to withstand fine-tuning attacks. Initially, watermark distillation is applied to the base model to calculate the weight difference Δθ. Subsequently, the base model is fine-tuned to obtain a fine-tuned model, and the weighted sum of the fine-tuned model's weights and Δθ results in the new fine-tuned distilled model.

### Strengths
1. The core idea of WAPITI is to leverage the impact of watermarks on the model's output distribution. The paper demonstrates that watermarks induce similar alterations in the output distribution of both the base and fine-tuned models. By adding the watermark parameter vector from the base model to the fine-tuned model parameters, the output distribution of the fine-tuned model is similarly modified, enabling the transfer of the watermark.
2. This paper introduces, for the first time, a parameter integration-based watermarking method that facilitates the migration of watermarks from the base model to the fine-tuned model, thereby avoiding the performance degradation and high computational costs associated with watermark distillation.
3. The proposed method effectively maintains the fine-tuning capabilities while ensuring the presence of the watermark, thereby providing robust defense against fine-tuning attacks and enhancing the security of the watermark.
4. The paper is well-structured, with a generally clear logical flow and clearly articulated viewpoints, effectively conveying the main content.

### Weaknesses
1. The issue of watermark distillation's inability to withstand fine-tuning, mentioned in the contributions of Chapter 1, has already been raised in Gu2024 and cannot be considered a primary contribution of this paper. While the authors frame their contribution as addressing the impact of fine-tuning on watermarked fine-tuned models, the core problem of watermark fragility under fine-tuning was already identified. The distinction between fine-tuning as an attack versus a post-watermarking process needs more explicit differentiation.
2. This paper serves as an improvement on the watermark distillation scheme proposed by Gu2024, which somewhat diminishes its novelty; further research is needed to solidify its impact. The parameter integration approach, while novel, still relies on the foundation of watermark distillation, which limits its originality.
3. In line 78, the paper emphasizes that WAPITI effectively resists fine-tuning attacks, yet this contribution is not mentioned in the summary, and the subsequent content lacks a comprehensive discussion on fine-tuning attacks. The lack of a clear definition of what constitutes a 'fine-tuning attack' and how it differs from standard fine-tuning procedures makes it difficult to assess the robustness of the proposed method.
4. Table 1 is missing a checkmark for the Decoding-based Watermarks row, and the description for "It undermines capabilities" is unclear; using parentheses in the table for clarification is also inappropriate. Additionally, the paragraph referencing this table mentions higher computational costs, which should prompt the addition of corresponding comparisons in the table, such as differences in vulnerability, robustness, and efficiency. The table lacks quantitative measures for the claimed advantages and disadvantages.
5. In Appendix E.2, the paper attempts to prove that even when models undergo fine-tuning attacks, the watermark detection rate and model usability decline synchronously to support the conclusion that WAPITI can resist fine-tuning attacks. However, the fine-tuning experiments in Gu2024 indicate that fine-tuning may remove the watermark without specifying whether model usability also declines synchronously. If usability in Gu2024’s experiments similarly declines, then WAPITI does not demonstrate a clear advantage over Gu2024 in resisting fine-tuning attacks, necessitating additional comparative experiments to substantiate this work. The synchronous decline argument needs stronger empirical evidence.
6. Figure 2 lacks clear annotations and fails to adequately explain the content depicted; it is recommended to split this into two figures or use line charts for a more intuitive presentation of data trends. The lack of clear labels and axes makes it hard to interpret the results.
7. In line 415, it is stated that WAPITI is effective and efficient. However, the term "efficient" requires supporting execution time data; to substantiate this conclusion, time cost experiments for the WAPITI scheme under various models and watermark methods should be added. Claims of efficiency need to be backed by quantitative comparisons.
8. In section 4.3, line 365 mentions that Appendix F will analyze the selection of the hyperparameter λ, yet only partial analysis regarding λ is found in Appendix E.1, and it does not provide a detailed explanation of the selection method for the λ hyperparameter. The hyperparameter selection process lacks sufficient detail and justification.
9. The appendix contains graphical and typographical errors, such as the identical experimental figure in section F.3 and E.1, the same images for Figures 2 and E.2 Figure 7, an incorrect reference to Figure 14 as Figure 6 in Appendix E.1, missing descriptions for the captions of Figures 9-14 in Appendix F, and incorrect writing of "coefffcient.S" in Appendix E.1. These errors detract from the credibility of the work.

### Questions
1. The paper does not provide a sufficient and detailed description of fine-tuning attacks related to Gu2024, which undermines the persuasiveness of its conclusions. For instance, while it mentions adding the KGW watermark to Llama-Math and Llama-QA, it neglects the Llama-chat and Pythia-chat models used in the main text, and it omits the AAR watermarking method. Additionally, it is unclear which dataset was used for fine-tuning Llama-Math and Llama-QA after watermarking, leading to a decline in fine-tuning capabilities.
2. If the paper aims to assert the incompatibility of the Gu2024 watermark distillation model with fine-tuning, it should validate this claim across diverse datasets. The relative entropy space of mathematical datasets is lower, and the performance of GSM8K may not sufficiently support this argument.
3. Generally, distilling larger models is often more effective due to their greater number of parameters and enhanced learning capacity, allowing them to capture richer features and complex patterns. Why does the paper choose to distill smaller models? What are the results of applying this approach to larger models?
4. If the parameters of the fine-tuned base model differ significantly from the original model across certain dimensions, could this result in the watermark being ineffective or lead to the loss of watermark information?

### Soundness
2

### Presentation
3

### Contribution
3
