# The Quest for Winning Tickets in Low-Rank Adapters

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 3, 6, 6, 5

## Abstract
Low-Rank Adaptation (LoRA), a prominent parameter-efficient fine-tuning (PEFT) method, offers an effective strategy for adapting large pre-trained models to specific tasks with minimal computational overhead. LoRA achieves this by introducing low-rank parameter matrices to the frozen pre-trained models. However, despite their efficiency, LoRA and its variants modify all elements of a parameter block, which is unnecessary as LoRA primarily aims to adjust a small set of subspaces that capture task-specific knowledge. Drawing inspiration from the Lottery Ticket Hypothesis (LTH), which posits that dense neural networks contain sparse subnetworks capable of performing similarly to fully-parameterized models, we investigate whether similar sparse subnetworks exist for low-rank adapters. We demonstrate that such subnetworks, often referred to as "winning tickets" in the context of LTH, indeed exist for low-rank adapters. We introduce a method to identify this sparse subset of weights for each layer by relating the top subspaces of the pretrained parameter block to the elements of the corresponding weight matrix. This subset is then fine-tuned using LoRA. We show that this sparse subset is not necessarily unique; as long as sparsity is kept within a certain bound defined by the task, random subnetworks with similar sparsity can act as winning tickets. Building on this discovery, we propose a novel approach called Partial-LoRA, which adds sparse low-rank parameters to pre-trained models. Through extensive experiments on 8 vision and 4 language tasks, we demonstrate that Partial-LoRA can reduce trainable parameters by up to 87% while maintaining or even improving model performance in some cases. Our work thus reduces memory needs and theoretically grounds sparse LoRAs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends the concept of winning tickets to low-rank adapters, demonstrating through theoretical and experimental evidence that masking a significant proportion of LoRA adapters can be done without compromising performance. The authors introduce Partial-LoRA, which strategically selects sparse low-rank parameters, achieving substantial reductions in trainable parameters (up to 87%) while maintaining or even enhancing model performance in certain cases.

### Strengths
1. This paper is well-written and interesting. It introduces the concept of winning tickets to low-rank adapters in a novel way and is backed by theoretical grounding.
2. From an empirical perspective, the method of masking a proportion of parameters offers more flexibility compared to existing approaches and shows strong performance across multiple experiments on vision and language models.

### Weaknesses
1. The datasets chosen by the authors are relatively simple, and the model used is comparatively small. In such tasks, which inherently may require fewer parameters[1] to learn effectively, the performance gap between full fine-tuning and PEFT methods, including LoRA, tends to be minimal. In more challenging tasks where LoRA underperforms compared to full fine-tuning possibly due to capacity limitations[2], it is unclear whether Partial-LoRA would maintain its advantage. Specifically, the datasets used do not represent the complexity of real-world fine-tuning scenarios, such as those involving extensive knowledge injection, complex reasoning, or code generation. These tasks often require substantial parameter adjustments and may expose limitations in the proposed method. The current evaluation does not sufficiently demonstrate the method's robustness in these more demanding contexts.
2. A discussion on the impact of the few-shot dataset for the sparsity ratio is necessary. While larger datasets could provide more accurate estimates, they would also require significantly more time to compute. Furthermore, the method's sensitivity to the size and diversity of the few-shot dataset used for determining the sparsity ratio is not explored. It is unclear how the quality of the selected subnetworks is affected by the representativeness of the few-shot samples. A more thorough analysis of this aspect is needed to ensure the reliability of the proposed approach.

### Questions
1. Figure 2 shows that Partial-LoRA, with its sparsity ratio derived from the 90% performance threshold, is comparable to or outperforms LoRA. Would it be possible to set this threshold lower to achieve a higher sparsity ratio? What is the maximum sparsity ratio at which performance remains stable?
2. To reduce memory usage, two strategies could be considered: (a) lowering the rank of LoRA or (b) increasing the sparsity of LoRA. Does the author suggest that using a higher rank with a more sparse LoRA could improve performance, as implied by Section 5.5 and Figure 6?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the existence of sparse LoRA adapters in the context of the Lottery Ticket Hypothesis (LTH). The authors give some theoretical proof that sparse subnetworks exist for low-rank adapters. They also propose a method, Partial-LoRA, to add sparse low-rank parameters to pre-trained models. The experiments show that Partial-LoRA can reduce trainable parameters by up to 87% while maintaining or even improving model performance in some cases.

### Strengths
The authors address an interesting problem and draw inspiration from previous works. The paper is well-organized and structured.

### Weaknesses
The theoretical proof in this paper, specifically **Theorem 4.1**, is based on previous works, such as **Theorem 2.5** in (Gadhikar et al., 2023), which proves the existence of a sparse mask satisfying the error bound. However, the authors make an ambiguous statement in Theorem 4.1, not clarifying whether they are discussing the existence (there exists a mask U that satisfies the condition) or universality (for all mask U, the condition is satisfied). This needs to be clarified. 
Following above question, if Theorem 4.1 is discussing the existence of a sparse mask, how to ensure the mask satisfying Theorem 4.1 can be decomposed into a low-rank format as in Equation (6)? The paper does not provide a proof that the mask $U$ from Theorem 4.1, which is shown to exist, can be represented by the decomposed form $(u_{row}B)(u_{col}A)$ used in the proposed method. This is a critical gap in the theoretical justification. Otherwise, if Theorem 4.1 is discussing the universality of the sparse mask, the proof provided by the authors is not sufficient because the reference (Gadhikar et al., 2023) only proves the existence of a sparse mask.
The experiments in this paper are not so convincing in 2024, such as the DeBERTa-v3-base (86M) model and GLUE benchmark. The authors should consider using more recent models and benchmarks to evaluate the performance of Partial-LoRA. The choice of DeBERTa-v3-base and GLUE benchmark limits the impact of the paper, as these are not representative of current state-of-the-art models and tasks. The paper lacks experiments on large language models, which are the primary focus of current research in parameter-efficient fine-tuning.
The most significant impact of Partial-LoRA is reducing the number of trainable parameters. However, the authors do not provide any analysis and evidence on why we should care about this metric. Considering that the LoRA adapters do not account for a significant portion of the model size and computation, the authors should provide more insights into the importance of pruning them. The paper does not adequately address the practical benefits of reducing the number of trainable parameters in LoRA, especially given that LoRA parameters are a small fraction of the overall model size. The authors should provide a more compelling argument for why this reduction is important.

### Questions
1. The theoretical proof in this paper, specifically **Theorem 4.1**, is based on previous works, such as **Theorem 2.5** in (Gadhikar et al., 2023), which proves the existence of a sparse mask satisfying the error bound. However, the authors make an ambiguous statement in Theorem 4.1, not clarifying whether they are discussing the existence (there exists a mask U that satisfies the condition) or universality (for all mask U, the condition is satisfied). This needs to be clarified. 
2. Following above question, if Theorem 4.1 is discussing the existence of a sparse mask, how to ensure the mask satisfying Theorem 4.1 can be decomposed into a low-rank format as in Equation (6)? Otherwise, if Theorem 4.1 is discussing the universality of the sparse mask, the proof provided by the authors is not sufficient because the reference (Gadhikar et al., 2023) only proves the existence of a sparse mask.
3. The experiments in this paper are not so convincing in 2024, such as the DeBERTa-v3-base (86M) model and GLUE benchmark. The authors should consider using more recent models and benchmarks to evaluate the performance of Partial-LoRA.
4. The most significant impact of Partial-LoRA is reducing the number of trainable parameters. However, the authors do not provide any analysis and evidence on why we should care about this metric. Considering that the LoRA adapters do not account for a significant portion of the model size and computation, the authors should provide more insights into the importance of pruning them.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores the concept of "winning tickets" within the Low-Rank Adaptation, inspired by the Lottery Ticket Hypothesis. The authors present a new method (denoted Partial-LoRA) that relies on random masking to identify sparse low-rank networks that can maintain or improve performance in fine-tuning pre-trained models on specific tasks while trying to reduce the number of trainable parameters. The authors present experiments on various vision and language tasks demonstrating significant parameter reductions while maintaining or improving accuracy.

### Strengths
1. The paper proposes a novel, interesting method that extends the lottery ticket hypothesis to low-rank adaptation.
2. The authors provide a good theoretical foundation to justify the LTH concept within LoRA.
3. The experiments cover a wide range of vision and language tasks, providing solid results in terms of maintaining accuracy while reducing the total number of parameters.

### Weaknesses
1. I think there is a main weakness in the presentation of the results: while the plots are nice, there should be a table showing the number of parameters and accuracy. Additionally, it should compare against methods of close parameter count if feasible (e.g., current results show how the method can maintain the accuracy while using few param counts, there should be a comparison the other way around, too, showing how methods with similar parameter count cannot achieve the same result to justify the original methods weren’t over -parameterized to being with).
2. Lack of experiments on larger models (e.g., llama), which are usually the main beneficiaries of PEFT.
3. The approach's reliance on random masking, rather than more targeted sparsification, could potentially limit its performance on more complex tasks or architectures.
4. The method relies on random masking for the LoRA matrices, which is itself low-rank (compressed), i.e., the mask itself is practically compressed; the method could benefit from comparing masking full-rank weights vs low-rank adapter.
5. A separate training phase on a subset dataset is needed to identify sparsity ratios.
6. Minor nit, the theorems can be a bit more rigorous (e.g., define all symbols T, U..etc, instead of relying on the context or the common use).

### Questions
1. As I mentioned in the weakness, is there a comparison with methods with similar parameter counts showing that your method can achieve x improvement using y params, while other methods can’t achieve the same improvement using also ~y params?
2. Why do masked LoRAs sometimes significantly outperform full LoRAs (e.g., Flowers dataset)? Is this purely preventing overfitting, or is there a more fundamental advantage?
3. The approach randomly prunes weights without considering inter-layer dependencies. Could more intelligent layer-wise tuning (e.g., adjusting pruning intensity per layer based on importance) improve results? 
4. Did you experiment with larger models (e.g. LLM) that usually benefit from PEFT more? Or is there a reason for sticking to smaller models?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to reduce the parameters of LoRAs by only training a subset of rows/columns of the low-rank matrices. The feasibility of this approach is backed by a theoretical argument that extends the existence of sparse subnetworks in arbitrary models to models that include low-rank adapters. Experiments on six image classification tasks and four sentence classification tasks show that performance similar or better than the original LoRA formulation can be obtained with the proposed method. Additionally, this paper proposes a method to select the sparsity ratio and which rows/columns to prune based on relevant prior work in the pruning domain. The main finding here is that choosing specific rows/columns of the low-rank matrices is unnecessary, and selecting these randomly is enough as long as the optimal sparsity ratio is respected.

### Strengths
1. This paper presents an interesting and valuable observation that LoRA adapters can be sparsified to reduce fine-tuning parameters further. If this holds in all cases, it is of great interest and usefulness to the community.
2. The proposed method is supported by a theoretical insight.
3. The paper includes extensive ablations to confirm that randomly selecting rows/columns to tune is a simple and strong method to sparsify LoRAs. While this does not rule out that some method exists to strategically select these rows/columns, it should be encouraged to also report such negative insights.
4. The presentation of the paper is excellent, it is clear and well-written

### Weaknesses
While the proposed idea is interesting, the experimental evaluation should be improved:
1. Experiments and Algorithm 1 only consider classification tasks. However, other tasks, such as LLM instruction tuning, are also very relevant applications. This paper would greatly benefit from including at least one generation task in the evaluation and showing the applicability of the proposed method there as well. The current formulation of Algorithm 1, which relies on a threshold based on a target accuracy, is not directly applicable to generative tasks where accuracy is not a viable metric. The paper should address how the method can be adapted to tasks where the evaluation is based on metrics such as BLEU, ROUGE, or CIDEr.
2. Experiments are only conducted on a subset of the VTAB and GLUE benchmarks. However, no details are given on why these particular tasks were chosen and why the whole benchmarks are not evaluated. This raises concerns about the generalizability of the results. The selection of tasks should be justified, and a more comprehensive evaluation across the full benchmarks would strengthen the findings. The current selection may lead to cherry-picking of tasks where the proposed method performs well, while potentially underperforming on other tasks within the same benchmarks.
3. It is unclear why results are only reported on the development split of GLUE tasks, although test set results can be obtained from the web API. Furthermore, it is unclear if the GLUE development split was also used to select the top 5 hyperparameter configurations or if a different subset of the data was used. The paper should clarify the data split used for hyperparameter selection and justify the choice of not using the test set for evaluation, as this limits the comparability with other works.

### Questions
Overall, I think this paper misses the aspect that LoRA is not only used in classification settings. Thus, I recommend to add a variant of Algorithm 1 and experiments for natural language generation tasks such as instruction tuning. Furthermore, the evaluation should be more aligned with the original evaluation of baselines, for example in DoRA [1] or VeRA [2] by including full benchmarks and similar tasks. This would allow for a better assessment of the respective strengths and weaknesses of the proposed method.

Otherwise, the paper should make it more clear that the proposed method is for classification scenarios only and revise the storyline accordingly.

[1] Liu et al.: DoRA: Weight-Decomposed Low-Rank Adaptation. In ICML (2024) -- https://arxiv.org/pdf/2402.09353

[2] Kopiczko et al.: VeRA: Vector-Based Random Matrix Adaptation. In ICLR (2024) -- https://arxiv.org/pdf/2310.11454

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores applying the Lottery Ticket Hypothesis (LTH) to Low-Rank Adaptation (LoRA) and proposes that LoRA’s low-rank adapters contain sparse, essential subnetworks, or 'winning tickets. The authors introduce Partial-LoRA, which identifies sparse subnetworks in LoRA matrices to reduce trainable parameters while retaining model performance. Through a series of experiments on vision and language tasks, they demonstrate that Partial-LoRA can achieve notable parameter reductions with minimal loss in accuracy. The paper presents a practical approach for enhancing parameter efficiency in model fine-tuning.

### Strengths
1. By leveraging Partial-LoRA, the work demonstrates that it’s possible to reduce trainable parameters by up to 87% while maintaining accuracy. This reduction supports resource-efficient fine-tuning, which is highly beneficial for deploying large models on devices with limited computational capacity.

2. The authors conduct comprehensive experiments across vision and language tasks, providing quantitative results that support the claimed parameter reduction benefits. This thorough testing on multiple datasets strengthens the paper’s claims regarding Partial-LoRA's performance consistency.

3. The work provides theoretical basis for applying LTH to LoRA, detailing how randomly masked adapters can achieve performance close to fully parameterized adapters. This theory analysis contribution enhances the credibility and relevance.

### Weaknesses
(1) **Absence of Adaptive Masking Mechanism.** Unlike recent techniques that employ adaptive sparsity adjustments per layer [1], this paper applies a fixed, random masking ratio for identifying "winning tickets." While the method calculates a sparsity ratio per layer, the application of random masks based on this ratio does not allow for the selection of specific, important parameters within each layer. This lack of adaptivity at the parameter level may lead to suboptimal performance, especially in tasks where parameter importance varies significantly within a layer, not just between layers.

(2) **Inadequate Theoretical Justification.** Although the authors discuss some theoretical underpinnings, there’s no formal analysis or proof of generalization guarantees for Partial-LoRA. Recent works typically provide theoretical bounds or assumptions [2], which help predict how sparse adapters might perform across different tasks or model architectures. The theoretical discussion would benefit from a more rigorous treatment, including specific theorems and proofs related to the convergence and generalization properties of the proposed method.

(3) **Lack of Robustness and Noise Testing.** The paper does not address Partial-LoRA's robustness under noisy or adversarial conditions, which is often included in parameter-efficient adaptation research. Testing under noise or adversarial setups would demonstrate the approach's practical resilience. It is crucial to evaluate how the identified sparse subnetworks behave when the input data is perturbed, as this can reveal the stability and reliability of the method.

(4) **Limited Reproducibility Information.** The paper lacks essential implementation details, such as hyperparameter settings, initialization strategies, and optimization schedules, which hinders reproducibility. Additionally, a provided open-sourced code repository will be beneficial to enhance the reproducibility. The description of the sparsity ratio derivation process is also vague, making it difficult to replicate the results.

(5) **No Exploration of Cross-Domain Transferability.** While Partial-LoRA performs well in selected domains, there’s no assessment of how it handles cross-domain adaptation (e.g., high-resource to low-resource tasks), a feature increasingly addressed in recent LoRA adaptations. This gap limits the understanding of the method’s robustness in varied application scenarios. Specifically, it is unclear whether the identified sparse subnetworks are transferable to new tasks or domains, or if they are highly specific to the training data.

### Questions
**1. Rationale for Random Masking Selection.** Could you clarify the choice of random masking as opposed to an adaptive sparsity mechanism, which recent studies have shown to be beneficial for task-specific and layer-specific adaptation? How does this fixed, non-adaptive approach account for variations in parameter importance across layers or tasks, and was any analysis conducted to validate the effectiveness of random masks for achieving optimal performance?


**2. Sparsity Ratio Derivation and Consistency.** The paper mentions deriving sparsity ratios based on a subset of labeled data. Could you provide details on how this subset was chosen and whether its selection impacts the stability of the resulting sparsity patterns? Additionally, is there consistency in performance if the sparsity ratios are derived from different subsets, or does it introduce variability in results?


**3. Layer-Wise Performance Variability.** Did you observe any significant performance differences across layers when applying a uniform sparsity ratio? Recent studies suggest that certain layers contribute more critically than others in large models. How did you assess the impact of sparsity on each layer, and were any experiments conducted to explore layer-specific adaptations or sparsity adjustments?


**4. Missing comparison with existing Lottery Ticket-based LoRA methods.** The authors should include existing Lottery Ticket Hypothesis-based LoRA approaches [a] [b] [c] in the related works section and provide a comparative discussion in the experimental results section. Specifically, it would be beneficial to discuss how the proposed Partial-LoRA differs from and compares to these established techniques, highlighting unique contributions and performance differences.


**5. Impact on Model Transferability Across Domains.** While Partial-LoRA performs well within specific task domains, there is limited evidence on its cross-domain performance, such as transfer from high-resource to low-resource settings. Were any experiments conducted to assess its effectiveness in such transfer scenarios? This would help clarify whether Partial-LoRA’s masking strategy generalizes well across diverse data distributions.

**6. Absence of Robustness Validation.** Given the potential application of Partial-LoRA in real-world tasks, was any consideration given to its robustness under adversarial attacks or noisy data? How does the model handle sparsity under these conditions? Many recent methods include robustness testing to validate performance stability, and it would be helpful to understand how Partial-LoRA performs in this regard.


**7. Implementation Details on Hyperparameters.** There is minimal detail on hyperparameter selection, initialization settings, and optimization schedules. Also, it is suggested the authors provide implementation codes of your proposed Partial-LoRA.

**References.**

[a] Panda, Ashwinee, et al. "Lottery ticket adaptation: Mitigating destructive interference in LLMs." arXiv preprint arXiv:2406.16797 (2024).

[b] Xu, Jing, and Jingzhao Zhang. "Random Masking Finds Winning Tickets for Parameter Efficient Fine-tuning." arXiv preprint arXiv:2405.02596 (2024).

[c]  Yuan, Fei, et al. "KS-Lottery: Finding Certified Lottery Tickets for Multilingual Language Models." arXiv preprint arXiv:2402.02801 (2024).

### Soundness
3

### Presentation
2

### Contribution
2
