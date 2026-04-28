# MoH: Multi-Head Attention as Mixture-of-Head Attention

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
In this work, we upgrade the multi-head attention mechanism, the core of the Transformer model, to improve efficiency while maintaining or surpassing the previous accuracy level. We show that multi-head attention can be expressed in the summation form. Drawing on the insight that not all attention heads hold equal significance, we propose Mixture-of-Head attention (MoH), a new architecture that treats attention heads as experts in the Mixture-of-Experts (MoE) mechanism. MoH has two significant advantages: First, MoH enables each token to select the appropriate attention heads, enhancing inference efficiency without compromising accuracy or increasing the number of parameters. Second, MoH replaces the standard summation in multi-head attention with a weighted summation, introducing flexibility to the attention mechanism and unlocking extra performance potential. Extensive experiments on ViT, DiT, and LLMs demonstrate that MoH outperforms multi-head attention by using only 50\%$\sim$90\% of the attention heads. Moreover, we demonstrate that pre-trained multi-head attention models, such as LLaMA3-8B, can be further continue-tuned into our MoH models. Notably, MoH-LLaMA3-8B achieves an average accuracy of 64.0\% across 14 benchmarks, outperforming LLaMA3-8B by 2.4\% by utilizing only 75\% of the attention heads. We believe the proposed MoH is a promising alternative to multi-head attention and provides a strong foundation for developing advanced and efficient attention-based models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In the field of deep learning, multi-head attention mechanism has always been a core component of Transformer models, achieving great success in natural language processing and computer vision tasks. However, research has shown that not all attention heads are equally important, and many attention heads can be pruned without affecting model accuracy. Based on this insight, this paper proposes a new architecture called Mixture of Head Attention (MoH) aimed at improving the efficiency of attention mechanisms while maintaining or surpassing previous accuracy levels.

### Strengths
MoH can achieve competitive performance while using fewer attention heads.By introducing shared heads and a two-stage routing mechanism, MoH enhances the standard Mixture-of-Experts (MoE) method, enabling the model to capture shared knowledge more effectively across different contexts.

MoH can be fine-tuned from pre-trained multi-head attention models, such as LLaMA3-8B, significantly enhancing the applicability of the model.

The method has been validated across various popular model frameworks, including Vision Transformers (ViT), Diffusion Models (DiT), and Large Language Models (LLMs), demonstrating superior performance in both image classification and language tasks.

### Weaknesses
It is suggested to provide more evidence about the diversity within the selected heads. Visualizations and statistics of the distribution may provide more insights.

What is the effect of MoH on multi-task joint learning. More discussions or experiments are welcomed.

What is the `density' in Figure.3. Is it a weight used to select whether to activate?

The discussion section indicate that MoA only suitable for encoder-decoder architecture.  It requires more evidence and explanation.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce an approach that mitigates redundancy among attention heads through the use of the MoE, which adaptively selects attention heads according to input tokens. This method enhances inference efficiency by employing only those heads that are crucial for feature extraction during the inference process. The MoH demonstrates enhanced performance, even when utilizing a limited number of heads, as evidenced by comprehensive validation experiments.


I appreciate the authors' response. The response provided to my comment appears to be satisfactory, so I keep my score.

### Strengths
- The author conducts comprehensive verification experiments to assess the performance of MoH, demonstrating results that are equal to or surpass previous methods. 
- MoH can significantly reduce the head's resources, which can tackle the most important problem of heavy MHSA operations.

### Weaknesses
 - The author performed ablation studies utilizing different ratios to determine the optimal configuration of shared heads or activated heads; however, this approach is heuristic. The ablation study concerning the ratio of shared heads presented in Table 7 indicates that identifying the optimal head ratio shows significant challenges.
- Given that the primary focus of this paper is to enhance inference efficiency through the reduction of multi-head ratios, it is essential to conduct an experiment that compares this approach with prior methods aimed at decreasing multi-head ratios. Specifically, a comparison against methods that employ techniques like head pruning or knowledge distillation to reduce the computational overhead of multi-head attention would provide a more comprehensive evaluation.
- The author asserts that the shared head acquires common knowledge in Line [180-183], yet this paper is limited to providing evidence that the shared head genuinely learns common knowledge. The analysis should include more rigorous methods to validate this claim, such as examining the feature representations of shared heads across different tasks or datasets to confirm their generalizability.

### Questions
The author claims that the inference efficiency is improved by MoH. However, there is limited ground for this claim in the experiment. Is there any more evidence to support this claim? If further experiments are difficult, even a theoretical interpretation should be presented.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Mixture-of-Head Attention (MoH) to the multi-head attention mechanism in Transformer models, incorporating a routing mechanism that activates the most relevant attention heads for each token. Extensive experiments across diverse model architectures demonstrate that MoH achieves comparable or better performance with fewer attention heads than traditional multi-head attention.

### Strengths
1. The idea of applying the mixture-of-experts paradigm to attention heads is novel.
2. MoH shows clear effectiveness for reducing computational overhead by activating fewer attention heads without sacrificing accuracy.
3. The paper presents a wide range of experiments across different model types, demonstrating the effectiveness of MoH. The ability to fine-tune pre-trained multi-head attention models like LLaMA adds practical value to the method.

### Weaknesses
1. The contribution is incremental. Replacing the summation of heads with a weighted sum and using expert selection are not entirely new ideas in machine learning, and their application here may not be sufficiently ground-breaking to warrant significant attention without a stronger theoretical basis.
2. The ablation studies are limited in scope and fail to deeply explore the design choices behind MoH. For example, there is little discussion on the impact of different numbers of activated heads beyond the experiments shown. The use of shared heads is also not well-motivated, and the reported improvements may be marginally due to tuning specific hyperparameters.
3. The paper could benefit from evaluations on more diverse and challenging tasks, such as object detection and instance segmentation, in line with prior research on ViT designs.
4. MoH introduces additional complexity with its routing mechanism. The added complexity is not fully justified by the performance gains, especially given that the gains appear marginal in some cases (e.g., DiT models).

### Questions
See Weaknesses.

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
This paper observes that each attention head in multi-head attention operates in parallel. By formulating the multi-head attention in summation form, it builds a dynamic mixture-of-head attention without increasing the number of parameters. Meanwhile, it introduces shared heads and a two-stage routing mechanism to enhance the standard MoH method. Extensive experiments across popular model frameworks, including ViT, DiT, LLMs and continue-tuning LLMs demonstrate strong performance and applicability.

### Strengths
1. Without altering the number of parameters, this work treats standard multi-head attention as Mixture-of-Head attention, which enhances the flexibility of the attention mechanism and shows improved performance.
2. To consolidate common knowledge, it introduces shared heads along with a corresponding routing mechanism. The ablation study results have validated the effectiveness of these designs.
3. Popular tasks including ViT for image classification, DiT for image generation, and LLM for language generation, demonstrate superior performance. Furthermore, the proposed MoH attention can continue-tune pre-trained standard multi-head LLaMA3-8B, significantly enhancing its applicability.

### Weaknesses
1. This work claims enhanced inference efficiency multiple times. However, there is a lack of experimental evidence to support this claim. Upon reviewing the implementation provided in the Supplementary Material, it appears that you simply mask the useless heads after obtaining the whole multi-head results, which may not genuinely improve inference efficiency. Additionally, the process of dynamically routing each token to the appropriate heads could potentially increase inference costs. The current implementation does not demonstrate actual speedup, and the overhead of routing could negate any potential gains from reduced computation.
2. The cited works that show multi-head attention contains redundant attention heads primarily focus on natural language processing, it would be better incorporate additional studies from the field of computer vision to provide a more comprehensive perspective.
3. In Equation 5 on line 190, the dimension of $W_r x_t $ is $h-h_s$, so for indices where $h_s+1<i \leq h$, $i$ in $(W_r x_t)_i$ should be 
${i-h_s}$.
4. In Table 5 on line 383, does the baseline LLaMA3-8B refer to the model after continue-tuning with standard multi-head attention, consistent with the configuration of MoH models, or does it represent the starting point for continue-tuning? If the baseline is the starting point, it would be better to add a baseline that reflects the results after continue-tuning with multi-head attention, as continue-tuning is likely to improve performace.

### Questions
Please see weakness section

### Soundness
3

### Presentation
4

### Contribution
3
