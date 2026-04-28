# L-MSA: Layer-wise Fine-tuning using the Method of Successive Approximations

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
With the emergence of large-scale models, the machine learning community has witnessed remarkable advancements. However, the substantial memory consumption associated with these models has emerged as a significant obstacle to large-scale training. To mitigate this challenge, an increasing emphasis has been placed on parameter-efficient fine-tuning methodologies, which adapt pre-trained models by fine-tuning only a subset of parameters.  We observe that in various scenarios, fine-tuning different layers could lead to varying performance outcomes, and selectively fine-tuning certain layers has the potential to yield favorable performance results. Drawing upon this insight, we propose L-MSA, a novel layer-wise fine-tuning approach that integrates two key components: a metric for layer selection and an algorithm for optimizing the fine-tuning of the selected layers. By leveraging the principles of the Method of Successive Approximations, our method enhances model performance by targeting specific layers based on their unique characteristics and fine-tuning them efficiently. We also provide a theoretical analysis within deep linear networks, establishing a strong foundation for our layer selection criterion. Empirical evaluations across various datasets demonstrate that L-MSA identifies layers that yield superior training outcomes and fine-tunes them efficiently, consistently outperforming existing layer-wise fine-tuning methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel approach for efficient fine-tuning of large-scale models. It addresses the challenge of substantial memory consumption associated with such models by introducing L-MSA, a method that fine-tunes only selected layers based on a new metric derived from the Method of Successive Approximations (MSA). This metric guides layer selection and optimizes their fine-tuning, resulting in better model performance with reduced computational costs.

The paper provides a theoretical analysis within deep linear networks and evaluates L-MSA across various datasets and tasks. It compares the proposed method with other layer-wise fine-tuning techniques, demonstrating its superior performance. The experimental results show that L-MSA consistently identifies the most impactful layers for fine-tuning and optimizes them effectively, outperforming baseline methods.

### Strengths
1. **Novel Layer Selection Metric:** The paper introduces a new metric for layer selection based on the Method of Successive Approximations (MSA), which is theoretically grounded and offers a fresh perspective on fine-tuning strategies.

2. **Theoretical Foundations:** The authors provide a comprehensive theoretical analysis within the context of deep linear networks, which strengthens the credibility of the proposed approach.

3. **Empirical Validation:** The paper demonstrates the effectiveness of L-MSA across multiple datasets and tasks, showing consistent improvement over several existing layer-wise fine-tuning methods.

4. **Parameter-Efficiency Focus:** By targeting specific layers for fine-tuning, the method aims to reduce computational costs, addressing a key challenge in training large-scale models.

5. **Clear Contributions to Layer-Wise Fine-Tuning:** The research highlights the potential of selectively fine-tuning layers to achieve better performance, contributing to the growing field of parameter-efficient fine-tuning methods.

### Weaknesses
1. **Lack of Comparison with State-of-the-Art Methods:** The paper does not compare L-MSA with prominent methods like **LoRA**[Hu et, al], which limits the evaluation of its relative effectiveness and practical impact. Specifically, the absence of comparisons against low-rank adaptation techniques, which are also parameter-efficient, makes it difficult to assess L-MSA's advantages in scenarios where parameter reduction is critical. The paper should include experiments that directly compare L-MSA with methods that achieve similar parameter efficiency to understand its performance trade-offs.

2. **Disjointed Presentation:** The flow of the paper is disrupted by referencing equations and concepts out of order, requiring readers to frequently navigate back and forth, which hampers comprehension and readability. For example, the introduction of the MSA metric should be more clearly motivated before diving into the mathematical details, and the connection between the theoretical analysis and the empirical results needs to be more explicitly stated.

3. **Inadequate Contextualization of Contributions:** The novelty of the proposed method is not sufficiently contextualized against a broader range of parameter-efficient fine-tuning techniques, making it harder to assess its uniqueness and value. The paper needs to clearly articulate how L-MSA differs from existing layer selection methods and other parameter-efficient fine-tuning techniques, highlighting the specific problem it addresses and the unique solution it offers.

4. **Generalization Concerns:** The paper acknowledges that the approximated updated loss may not always guarantee strong generalization to test data, which raises questions about the robustness of the approach in diverse real-world scenarios. The paper should provide a more in-depth analysis of the conditions under which the approximation is valid and explore strategies to mitigate potential generalization issues, such as regularization techniques or adaptive layer selection.

5. **Computational Demands:** Despite aiming for parameter efficiency, the method still involves substantial computational overhead due to both forward and backward propagation, which could limit its practicality for very large-scale models. The paper should provide a detailed analysis of the computational cost of L-MSA, including the time and memory requirements for both layer selection and fine-tuning, and compare these costs with other parameter-efficient methods.

6. **Limited Scope of Empirical Comparisons:** While the paper evaluates L-MSA across several tasks, the range of comparative baselines is not exhaustive, potentially missing out on broader insights. The paper should include a more comprehensive set of baselines, including a wider range of layer-wise fine-tuning methods and parameter-efficient techniques, to provide a more robust evaluation of L-MSA's performance.

### Questions
1. Why were methods like LoRA and other recent parameter-efficient fine-tuning techniques not included in the comparison? Would the results hold up against these widely-used benchmarks?

2. How does the method perform on more diverse and real-world tasks outside the provided datasets? Are there specific domains where L-MSA is particularly effective or less so?

3. Given the still significant computational demands, how does L-MSA compare in terms of efficiency gains relative to other lightweight fine-tuning techniques? Is the trade-off between computational cost and performance improvement justified?

4. The method currently selects one layer at a time for fine-tuning. Could this approach be extended to simultaneously fine-tune multiple layers, and if so, how would it impact performance and computational cost?

5. Have the authors considered dynamically reselecting layers during the training process? Would this adapt better to changing training dynamics and potentially improve generalization?

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
4

### Summary
This paper explores layer-wise fine-tuning strategies for adapting large pretrained models. The authors found that fine-tuning specific layers can lead to varied performance outcomes, and selectively fine-tuning certain layers may enhance results. Building on these insights, they propose a novel layer-wise fine-tuning approach that leverages Pontryagin’s Maximum Principle to guide layer selection for fine-tuning. The effectiveness of this method is demonstrated through transfer learning from ImageNet to CIFAR100.

### Strengths
1. The task of parameter-efficient fine-tuning is crucial for practical applications of pretrained models.

2. The authors performed an in-depth analysis on the effectiveness of fine-tuning at the layer level.

### Weaknesses
1. The paper's novelty is somewhat limited, as the idea that fine-tuning different layers can lead to varying performance outcomes has already been widely explored in previous research. It is not clear what is the main contribution of the paper. 

2. The proposed method, which relies on the Method of Successive Approximation, lacks clear motivation. It’s unclear why this approach would lead to improved layer selection or how it compares favorably to other existing methods. In other words, what are the benefits of the proposed approach?

3. For the theoretical analysis, it is not clear what is the main contribution. The authors should also connect the theoretical analysis to the proposed method and discuss why the proposed method can lead to better layer selection and fine-tuning. 

4. The explanation based on PMP is interesting, but the main technical contribution is not clear. It would be helpful if the authors could clarify where the primary novelty lies.

Overall, while the paper presents a reasonable idea, it suffers from poor writing, insufficient motivation and unclear contribution.

### Questions
1. Why the Method of Successive Approximations is good for layer selection and layer fine-tuning?
2. What is the goal of the proposed method? Which layer should be actually selected for fine-tuning?
3. Compared with the baseline fine-tuning methods, what is the main advantage of the proposed method?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method to do a more targeted fine-tuning process where instead of updating every single layer/parameter in the architecture, the layer that has the strongest effect in the total loss is selected and updated on each iteration of the fine-tuning process.

Towards this goal the paper proposes a metric to select the layer to be updated and an algorithm for the fine-tuning of the selected layers.

Experiments on several datasets (CIFAR-100, CIFAR-C, CIFAR-Flip, Living-17 and ImageNet-C) including several related methods (full fine-tuning, LIFT, LISA, surgical Fine-tuning and Auto-RGN) provide evidence on the performance of the proposed method.

### Strengths
- A theoretical analysis for the proposed method has been provided (Sec. 3 & Sec. A.1).
    
- The empirical evaluation of the proposed method includes a good variety of datasets and competing methods. This allows to assess the applicability of the proposed method in different contexts.
    
- The validation of the proposed method includes an ablation analysis this is effective towards obtaining insights on how the different components of the proposed method contribute to its performance and how it compares w.r.t. full fine-tuning.
    
- The paper adequately highlights the limitations of the proposed method (Sec. 5)

### Weaknesses
 - The originality of the paper is somewhat reduced. While the method put forward by the paper outperforms (in some cases) the considered baselines, as admitted by the paper (Sec. 4.1)  there are already methods in the literature that aim at a more targeted fine-tuning process.
    
- In its current form the paper does not feel self-contained, there are several aspects of the paper that are delegated to the appendix. For instance, the models considered in experiments of Sec. 4.2 are not explicitly indicated. In other cases, the protocols and motivations behind the conducted experiments are not clear. Here a proper balance must be achieved to ensure the paper provides sufficient details as to allow the reader to critically analyze the proposed method and its conducted validation.
    
- While pairing a method with its corresponding theoretical analysis is very desirable, the extend to which such analysis is currently provided (Sec. 3) is just too shallow as to be informative.  Perhaps it could be completely moved to the appendix in order to allocate space to further elaborate on other parts of the paper that are currently not detailed enough.
    
- Some statements seem to lack supporting evidence. For instance, in several parts of the paper (l.535) statements are made regarding to the reduced computational costs of the proposed method. The evaluation section is missing however a proper experiment addressing that aspect.
    
- The improvement put forward by the proposed method is not that outspoken. For instance, in Table 1 it is observed that the proposed method is better in only 2/4 considered settings.
    
- In Fig. 6, averaged results over different datasets are reported. This not only hinders the variations in performance across datasets, but also behavior observed for the different methods across the considered datasets.
    
- Weak positioning; Good part of the related work is centered around other not directly related aspects. For instance, Sec. 6.1 discusses large architectures, which has close no link w.r.t. the proposed method.  Similarly l.497-502 from Sec. 6.2 is related to prompt-based methods. Thus having a relatively weak link with the proposed method. This weak positioning w.r.t. related efforts becomes more evident when we consider that almost none of the related methods considered in the experimental section (Sec. 4) are covered in the related work section. In addition, I would suggest looking at the two references below which seem to be very related to the proposed method.
    
    - Youngmin Ro, Jin Young Choi, "AutoLR: Layer-wise Pruning and Auto-tuning of Learning Rates in Fine-tuning of Deep Networks", AAAI 2021
    - Basel Barakat; Qiang Huang, "Enhancing Transfer Learning Reliability via Block-Wise Fine-Tuning",  ICMLA 2023

### Questions
- [Suggestion] Some of the contributions listed in the paper need to be merged and toned down. The paper currently lists four contributions. not contributions. The first contribution is closely related with the fourth one. Hence my suggestion to merge them, Moreover, this fourth contribution is related to the empirical validation of the proposed method. In this regard, the proper validation of a proposed method is not a plus but a must for a decent piece of scientific work. Therefore, I would suggest toning down this claim.
    
- [Suggestion] In Fig. 6, I suggest reporting the loss curves on a per-dataset basis. It might also be informative to discuss any trend observed during the training iterations.
    
- [Question] In l.379, it is indicated that “…he results illustrate that our L-MSA metric consistently identifies layers associated with improved training loss, effectively pinpointing those that contribute to better training outcomes...“ May you indicate how do you observe this in that figure? From what I can interpret, the results from Fig. 4 are point estimates at a given training iteration. Therefore, it is hard for me to assess how this figure allows to observe a consistent behavior.
    
- [Question] In l.408, it is stated “…Notably, using L-MSA for layer-wise fine-tuning results in performance improvements of up to 20% compared to full fine-tuning” May you indicate the source of this observation?
    
- [Question] In Sec. 4.3 a “No Adaptation” baseline is included. In l.432 it is indicated that this baseline “…provides a reference point for model performance without fine-tuning”, May you motivate how good of a reference this baseline is for datasets like CIFAR-Flip and ImageNet-C considering the number of output classes is significantly different (CIFAR-Flip) and/or reduce (ImageNet-C).

### Soundness
3

### Presentation
2

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
The machine learning community has made remarkable progress with the advent of large-scale models, but these models become a significant obstacle by consuming large amounts of memory during training. In this paper, we propose a fine-tuning Method using the Method of Successive Approximations, L-MSA. Experiments on different data sets verify the effectiveness of L-MSA

### Strengths
- The paper is well-written and easy to follow.
- The experimental results seem to be promising, surpassing Full Fine-tuning on part of the dataset

### Weaknesses
 - This paper emphasizes the advantages on large-scale models, but the datasets used seem to focus on extremely small datasets such as CIFAR, which show the worst performance on experimental fine-tuning on Imagenet-C. The only LIFT that seems to outperform is a paper that has not yet been published through peer review. This makes me worry about its practical prospects.
- Not enough experiments, this paper is motivated by the fact that large-scale models consume memory, but there is no comparison of memory overhead in the paper.

### Questions
- Q1.The other works compared in this paper are all about NLP and LLM. Why did the authors only apply these works to image datasets and test them on image datasets instead of NLP datasets used in other papers?
- Q2.Does L-MSA introduce additional memory overhead compared to randomly selecting other papers? I have not been involved in PEFT, but in theory it seems to require the same memory spikes as Full Fine-turn, which runs counter to the motivation of the authors.The authors should provide a detailed analysis of the memory usage of L-MSA compared to full fine-tuning and other PEFT methods, including peak memory usage and average memory consumption?
- Q3.Does performing MSA on the loss of the network introduce more training time? Especially when the network size increases, it is necessary to calculate and compare the state and co-state variables layer by layer.
- Q4.In Figure 5, in the experiments of ImageNet to CIFAR-100, it can be clearly observed that Full-Finetuning and Auto-RGN continue to converge, while L-MSA seems to have completed convergence. Can you show the results for more epochs?

If the author resolves my questions, I will consider raising my rating.

### Soundness
2

### Presentation
3

### Contribution
2
