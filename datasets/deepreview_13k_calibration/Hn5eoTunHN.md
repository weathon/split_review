# RandLoRA: Full rank parameter-efficient fine-tuning of large models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Low-Rank Adaptation (LoRA) and its variants have shown impressive results in reducing the number of trainable parameters and memory requirements of large transformer networks while maintaining fine-tuning performance. 
However, the low-rank nature of the weight update inherently limits the representation power of the fine-tuned model, potentially compromising performance on complex tasks.
This raises a critical question: when a performance gap between LoRA and standard fine-tuning is observed, is it due to the reduced number of trainable parameters or the rank deficiency?
This paper aims to answer this question by introducing RandLoRA, a parameter-efficient method that performs full-rank updates using a learned linear combinations of low-rank, non-trainable random matrices. Our method limits the number of trainable parameters by restricting optimization to diagonal scaling matrices applied to the fixed random matrices. This allows us to effectively overcome low-rank limitations while maintaining low parameter count and memory usage during training.
Through extensive experimentation across vision, language, and vision-language benchmarks, we systematically evaluate the limitations of LoRA and existing random basis methods.
Our findings reveal that full-rank updates are beneficial across vision and language tasks separately, but especially so for vision-language tasks, where RandLoRA significantly reduces---and sometimes eliminates---the performance gap between standard fine-tuning and LoRA, demonstrating its efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces RandLoRA, a method designed for efficient parameter tuning of both visual and linguistic models. The researchers discuss the shortcomings of conventional low-rank adaptation techniques, known as LoRA, and highlight the significance of non-critical ranks in the adaptation process. As a result, compared with traditional LoRA, RandLoRA earns better performance with fewer trainable parameters. The convergence of RandLoRA is discussed in detail. Extensive experiments verify its effectiveness on vision and language tasks.

### Strengths
+ RandLoRA is proposed to approximate low-rank updates under a clear motivation about the importance of non-critical ranks.
+ Multiple scales of models are selected as baselines, and RandLoRA can lead to good improvement in most situations.
+ The paper is well-written and easy to follow.

### Weaknesses
 - The motivation here mainly focus on how to approximate and improve low-rank adaptation methods like LoRA. The conclusion is to use full-rank updates and thus the authors propose RandLoRA. However, RandLoRA also outperforms full fine-tuning in various tasks like image classification. How to explain this experimental result? Why we can earn improvement by approximating low-rank updates to full-rank updates over both LoRA and full fine-tuning?
- Some important baselines are missing. For example, in the field of tuning CLIP on image classification tasks, many state-of-the-art methods use prompt-based tuning methods, e.g. PromptSRC (ICCV'23)[a], DePT (CVPR'24)[b] instead of LoRA. Such kind of parameter-efficient fine-tuning methods should also be discussed and compared with, given that the most-related works VeRA and LoRA are not initially proposed for image classification tasks.

### Questions
Please see weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes RandLoRA for parameter-efficient fine-tuning for vision and language models. The authors start from analyzing the drawbacks of traditional low rank adaptation methods(LoRA) and argue that the importance of non-essential ranks during adaptation. RandLoRA shows better performance than existing methods on fine-tuning CLIP models on image classification and fine-tuning LLMs on 8 commonsense reasoning tasks.

### Strengths
- The presentation is clear and easy to understand
- The proposed RandLoRA's convergence has been theoretically proved
- Various experiments on different tasks and models are done

### Weaknesses
 - Limited technical novelty. What is the main difference between VeRA and RandLoRA? There is a fairly similar update formulation in VeRA, e.g. two frozen low-rank matrices and two trainable small matrices.
- Lack of some important experiments for further verification. Most competitors, e.g. VeRA and LoRA, in the paper are proposed for language models and language tasks. To confirm the superiority of RandLoRA, the authors should directly compare the performance between RandLoRA and former competitors on standard language tasks, e.g. GLUE and E2E used in VeRA. The current evaluation is insufficient to demonstrate the claimed general applicability of RandLoRA, especially given that the method's core idea seems closely related to existing low-rank adaptation techniques.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes RandLoRA, a new method to address the limitations of LoRA in complex tasks. RandLoRA overcomes the low-rank constraint of LoRA by learning a combination of random low-rank basis matrices to achieve full-rank updates, and trend-off a balance between parameter efficiency and model performance. However, the paper needs to be further strengthened in several aspects. Overall, the paper is novel, but there is room for improvement in experimental and theoretical.

### Strengths
1. RandLoRA proposes a full-rank optimization strategy based on random low-rank matrix combinations, which helped the limitations of LoRA in complex tasks, especially the problem that its low-rank matrix cannot fully capture the complexity distribution of the task.
2. In the case of limited parameters, RandLoRA shows higher performance than LoRA, especially in vision-language tasks, showing that the method has certain parameter efficiency.
3. The paper provides novel ideas for the fine-tuning of large models, while reducing computing resource consumption and memory usage, while improving the performance of the model on specific tasks.
4. This paper well analysis the rationale behind the effectiveness of the proposed method.

### Weaknesses
1. The paper's derivation of RandLoRA is based on SVD and random basis matrix combination, but the theoretical rigour is still insufficient. The derivation assumes that the basis matrix obeys a specific random distribution (such as Gaussian or uniform distribution), which is difficult to strictly guarantee in practice. Specifically, the method relies on pseudo-random number generators which, while practically useful, do not provide the same guarantees as true random distributions, potentially affecting the theoretical analysis. In addition, the combination of random basis matrices may cause stability problems in large-scale training. It is recommended to conduct experiments on models with larger parameter amounts to verify the robustness of the method.
2. Theorem 4.1 proposed in the paper gives the approximation error bound of RandLoRA, but does not explain in detail how to control the size of the error in practical applications, especially as the model size increases, whether the error will accumulate, which may affect its approximation effect. The theorem provides a bound, but lacks practical guidance on how to adjust hyperparameters or the method itself to minimize this error, particularly when scaling to larger models where the number of parameters to estimate grows quadratically.
3. The introduction of sparse matrices is intended to reduce computational complexity, but the impact of sparse matrices on the full-rank approximation effect has not been fully demonstrated. Although Table 3 shows the experimental effect of sparse matrices in RandLoRA, the paper does not explore the theoretical impact of sparse matrices in full-rank approximation in depth, and it is recommended to add analysis in this regard. Specifically, the paper needs to address the potential for co-linearity issues when using sparse matrices, which could lead to a loss of the desired full-rank approximation.
4. The comparative experiment of the paper selected LoRA, NoLA, VeRA and other parameter efficient fine-tuning methods, but did not include full parameter fine-tuning as a control. It may not be sufficient to select only LoRA as the main benchmark. It is recommended to supplement the full parameter fine-tuning results to fully evaluate the advantages and disadvantages of RandLoRA.
5. RandLoRA has relatively small improvements in visual tasks, but its effect in visual-language tasks is significantly enhanced. It may be related to the complexity of the task and the characteristics of multimodal data?
6. The impact of different configurations of RandLoRA (such as the sparsity of the random basis matrix and the distribution selection of the basis matrix) on the effect deserves further study. It is recommended to add ablation experiments on factors such as the basis matrix generation method and parameter scale to more comprehensively reveal the performance influencing factors of RandLoRA.
7. Although RandLoRA performs well on small-scale parameter models, its effectiveness in larger-scale models (such as LLaMA 70B and LlaVA 32B) has not been verified. It is recommended to conduct experiments on larger-scale models.

### Questions
see the weaknesses.

### Soundness
3

### Presentation
2

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
This paper introduces RandLoRA, a novel method for parameter-efficient fine-tuning (PEFT) of large pre-trained models. By leveraging learned linear combinations of low-rank, non-trainable random matrices, RandLoRA enables full-rank updates, which significantly enhance the adaptability and efficiency of fine-tuning processes. The method strategically limits the number of trainable parameters by optimizing diagonal scaling matrices, which are applied to the fixed random bases, thus maintaining a low parameter count and minimal memory usage during training.

### Strengths
(1): The manuscript is well-crafted with a clear and logical progression of ideas.
(2): Visual aids like figures and tables are effectively used to illustrate key points and compare performance metrics clearly.
(3): The extensive experiments across various tasks and architectures demonstrate the method's effectiveness and adaptability.

### Weaknesses
(1): Lines 86-89: The phenomenon of performance saturation as the rank of LoRA increases is well-known in the field (This has already been explained in the VeRA paper.). I suggest that this point be rephrased or discussed within the context of known literature to maintain the integrity of the paper. Specifically, the paper should acknowledge that while increasing the rank of LoRA can improve performance, it often leads to diminishing returns and increased computational cost, which has been observed in prior work. The current phrasing implies this is a novel observation, which is misleading.
(2): While the method is promising in terms of parameter efficiency and memory usage, its practicality is challenged by the substantially increased training times on the Llama3B model. A more thorough investigation into the computational trade-offs and possible optimizations to reduce training times would benefit the study and its broader applicability. The paper should include a detailed analysis of the computational overhead introduced by RandLoRA, including a breakdown of the time spent on different operations (e.g., matrix multiplications, scaling operations). Furthermore, the paper should explore potential optimizations, such as using sparse matrix operations or alternative hardware implementations, to mitigate the increased training time.


### Questions
(1): Lines 77-80: The paper claims that RandLoRA consistently outperforms LoRA across the same parameter counts. However, based on Figure 1(a) and 1(b), it appears that RandLoRA surpasses LoRA only when LoRA begins to overfit as the parameter count increases. I recommend the authors to qualify their statements to reflect that RandLoRA's superiority emerges prominently under conditions of LoRA’s overfitting.
(2): In the related work section of this paper, the authors have omitted some significant recent advancements in LoRA modifications. For example: SVFT, HydraLoRA, PISSA, LoRA-XS, FLoRA, etc. The inclusion of these advancements is essential for enriching the research background and understanding the current research progress in this field. While DoRA is mentioned in the related work, it is not compared with RandLoRA in the experimental section. I recommend that the authors consider such comparisons in future work. This would not only enhance the persuasiveness of the paper but also better showcase the advantages and distinct characteristics of RandLoRA among the plethora of methods.

### Soundness
3

### Presentation
2

### Contribution
2
