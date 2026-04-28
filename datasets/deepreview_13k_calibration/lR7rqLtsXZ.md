# Fira: Can We Achieve Full-rank Training of LLMs Under Low-rank Constraint?

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Low-rank training has emerged as a promising approach for reducing memory usage in training Large Language Models (LLMs). Previous methods either rely on decomposing weight matrices (e.g., LoRA), or seek to decompose gradient matrices (e.g., GaLore) to ensure reduced memory consumption. However, both of them constrain the training in a low-rank subspace, thus inevitably leading to sub-optimal performance. This raises a question: whether it is possible to consistently preserve the low-rank constraint for memory efficiency, while achieving full-rank training (i.e., training with full-rank gradients of full-rank weights) to avoid inferior outcomes? In this paper, we propose a new plug-and-play training framework for LLMs called Fira, as the first attempt to achieve this goal. First, we observe an interesting phenomenon during LLM training: the scaling impact of adaptive optimizers (e.g., Adam) on the gradient norm remains similar from low-rank to full-rank training. Based on this observation, we propose a norm-based scaling method, which utilizes the scaling impact of low-rank optimizers as substitutes for that of original full-rank optimizers to enable full-rank training. In this way, we can preserve the low-rank constraint in the optimizer while achieving full-rank training for better performance. Moreover, we find that there are sudden gradient rises during the optimization process, potentially causing loss spikes. To address this, we further put forward a norm-growth limiter to smooth the gradient via regulating the relative increase of gradient norms. Extensive experiments on the pre-training and fine-tuning of LLMs show that Fira outperforms both LoRA and GaLore, achieving performance that is comparable to or even better than full-rank training. For instance, our Fira can reduce the memory usage of optimizer states by 61.1\%, while achieving improved performance for pre-training on the LLaMA 1B architecture. Notably, for pre-training on the LLaMA 7B architecture, our method uses an $8\times$ smaller rank than GaLore, yet outperforms it by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a memory-efficient training framework called Fira for the pre-training and fine-tuning of large language models (LLMs). Fira aims to reconcile the memory efficiency of low-rank training with the performance benefits of full-rank updates. Building upon GaLore [1], Fira introduces two key components: Norm-Based Scaling and the Norm-Growth Limiter. In Norm-Based Scaling, Fira leverages the empirical observation that the scaling effect on gradient norms remains similar between low-rank and full-rank training. Thus, it uses scaling factors from low-rank optimizers to approximate gradient corrections in full-rank training. The Norm-Growth Limiter mitigates sudden spikes in training loss by limiting the relative increase in gradient norms between steps, effectively converting sudden spikes into gradual rises. The paper validates Fira in both pre-training by evaluating the perplexity on the C4 dataset and fine-tuning by evaluating performance on the CommonSenseQA tasks across various model sizes (60M, 130M, 350M, 1B).

[1] GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection

### Strengths
1. The observation of the similarity in scaling factors of adaptive optimizers between low-rank and full-rank training is insightful and forms a solid foundation for the proposed method.
2. In Norm-Based Scaling, Fira not only maintains memory efficiency but also enables full-rank updates, giving it an advantage over other methods.
3. The Norm-Growth Limiter is a simple yet effective approach to addressing sudden spikes in training loss.
4. The authors conduct extensive experiments, including ablation studies and scaling analyses, across multiple model sizes and tasks, strengthening the empirical validation of their approach.

### Weaknesses
1. Limited theoretical justification. While the empirical observations are compelling, the paper lacks a rigorous theoretical analysis explaining why norm-based scaling effectively approximates full-rank gradient corrections. Specifically, the paper does not provide any formal analysis of the approximation error introduced by using low-rank scaling factors for full-rank updates, nor does it explore the conditions under which this approximation is valid or may break down.
2. Inconsistent and incomplete baseline comparisons. The baseline comparisons are not comprehensive enough; more recent memory-efficient fine-tuning methods (such as LISA[2], FLoRA[3] that gradient based memory-efficient training method) should be included for a stronger evaluation. Additionally, the evaluation settings between pre-training and fine-tuning are inconsistent: in pre-training, the comparisons include full-rank, Fira, GaLore, LoRA, and ReLoRA, whereas in fine-tuning, full-rank and ReLoRA are omitted, and instead, prefix tuning, series, and parallel methods are included. This inconsistency leads to some confusion. Since the scope of comparison is memory-efficient training, the experiments should be as consistent as possible. For example, the absence of full-rank fine-tuning results makes it difficult to assess the true trade-off between memory efficiency and performance.
3. Lack of comparison with existing methods addressing loss spikes. Restricting the magnitude of gradients to address abrupt changes in gradients or loss is a commonly adopted approach. While gradient clipping employs absolute value thresholds, the Norm-Growth Limiter uses a relative threshold. Furthermore, sudden spikes are not unique to memory-efficient or parameter-efficient training; they are common issues even in full training. Several studies have proposed methods based on gradient and layer norms to address loss spikes [4,5,6]; however, the paper does not provide comparisons with these methods. The paper should clarify how the proposed limiter compares to existing techniques in terms of effectiveness and computational overhead.
4. Lack of detailed memory efficiency metrics. As a memory-efficient training method, the paper lacks actual memory usage comparisons. In the comparison with GaLore, the paper emphasizes training performance but overlooks memory efficiency and throughput, which is inconsistent with the experiments provided by GaLore. The paper should provide a detailed breakdown of memory usage, including the memory footprint of the model parameters, optimizer states, and intermediate activations, for both Fira and the baseline methods.

### Questions
1. Can you provide theoretical analysis explaining why the norm-based scaling effectively approximates full-rank gradient corrections? Is this phenomenon present in any LLM training, or is it conditional?
2. Can the baseline comparisons in pre-training and fine-tuning be kept consistent?
3. As a memory-efficient training method, could you provide comparisons regarding training memory usage? Including more experiments on overhead would be a plus.
4. For the Norm-Growth Limiter, could you provide comparative experiments with other methods that address loss spikes?

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
This work proposes a new memory-efficient training approach built on top of GaLore. It leverages low-rank gradients while appropriately combining the residual gradient components with gradient scaling. Experiments demonstrates FIRA achieves significant improvements comparied with previous baselines in both pre-training and fine-tuning scenarios.

### Strengths
- The improvements is significant as shown in Table 2.

- The observations of gradient scaling, that can effectively incorporate the gradient residual is interesting and novel.

- The method is clearly explained and easy to follow.

### Weaknesses
 - Intuitively, incorporating the residual gradient can lead to performance improvements, though it is typically not expected to surpass Adam. However, as shown in Table 2, Fira significantly outperforms Adam. Is there any insights why it is even better than adam.

- $\gamma = 1.01$ seems to effectively avoid the gradient spiking, whether the performance is senstive to the choice of $\gamma$.

### Questions
Please refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new method to achieve efficient training of LLMs by reducing the memory usage for optimizer states. Specifically, it designs a norm-based scaling method that approximates full-rank training by using the scaling impact of low-rank optimizers as substitutes for that of original full-rank optimizers. It also proposes a norm-growth limiter to address the issue of loss spikes.

### Strengths
The proposed method demonstrates strong empirical performance. While the training efficiency is close to the SOTA method, GaLora, the proposed method significantly outperforms GaLora even using 8X smaller ranking. Moreover, it can even outperform full-rank training.

### Weaknesses
1. The authors support the use of low-rank scaling factors to approximate full-rank scaling factors by demonstrating that the order of the average scaling factors of the weight matrix is highly similar. However, similarity in order is not equivalent to similarity in value. Therefore, the validity of this approximation method is questionable.

2. Since the proposed method aims to approximate full-rank training, we would assume that the performance of full-rank training is the upper bound. However, the proposed method even outperforms full-rank training. It is unclear why the proposed method outperforms.

3. If the scaling factor for the full rank gradient can be approximated by a low rank scaling factor, why not just apply the low rank scaling factor to the full rank gradient? This strategy has the same memory usage in the optimizer state as the proposed method. Could the authors conduct experiments to validate this strategy? This would be a good support for the effectiveness of the scaling factor approximation.

Minor:

4. The phenomenon of loss spiking does not seem to be specific to low-order training, therefore, the proposed norm growth limiter is not intended for low-rank training.

5. The proposed method is only applicable to adaptive optimizers. I know that Adam is very important for efficient training, so this is not a major concern.

### Questions
Please address the concerns in weakness. I am impressed with the performance of the proposed method. However, I am skeptical that the proposed method works in the way the author suggests, or if it works in any other way. I would be willing to increase my score if the authors address these concerns.

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
2

### Summary
This work considers training LLMs with full-rank gradients and weights within the low-rank constraints (i.e. imposing low-rank structures on gradient or weights). The main goal of this work is to improve Galore (a low-rank gradient projection optimizer [1]) by incorporating the orthogonal complement information of the Galore projected gradient, without maintaining its optimizer states (1st and 2nd order momentums).

Specifically, the authors observe that (Figure 3), when training LlaMA-60M on C4 dataset with Galore, the scaling factor (the ratio between the norm of the corrected gradient an original gradient) of each matrix exihibits similar rank orders across different choices of GaLore-rank $r$. This motivates the authors to extend GaLore to Fira, a full-rank weight & gradient optimizer under low-rank constraint that consists of two components: 1) a norm-based scaling method, which replace the full-rank scaling factor with the low-rank counterpart; 2) a norm-growth limiter to smooth the training gradient by restricting the gradient norm's increase. The authors showed that proposed Fira outperforms the full-rank baselines on both pretraining and finetuning datasets across various settings.

[1]. *Jiawei Zhao, Zhenyu Zhang, Beidi Chen, Zhangyang Wang, Anima Anandkumar, and Yuandong Tian. Galore: Memory-efficient llm training by gradient low-rank projection. ICML 2024.*

### Strengths
1. Compared to the Galore, this paper proposed to utilize the scaled gradient information (Algorithm 1, line 15) resides in the orthogonal complement of the Galore gradient, which achieves improved training performance. The utilization of the orthogonal complement gradient information is new.
2. The authors proposed a new 'gradient clipping' scheme, i.e. the norm-growth limiter in Eq. (12) to alleviate the spikes arouse in during the Fira training process.
3. The authors show evident outperformance of Fira compared to the standard Galore within a similar parameter amount (Table 1 and Table 2).

### Weaknesses
My mainly concerns lies in the motivation of using the norm-based scaling Eq. (10).  

The authors observed that, the average scaling factors (averaged every 20 steps) of the weight matrices exihibit similar orders across different Galore-rank-$r$ training settings (Figure 3 and Table 7). The authors also mentioned that 'the absolute magnitude of the scaling factors can be regarded as the learning rate to which Adam is not sensitive' (Page 5, lines 266-267).

However, from my perspective, several logical gaps still remain between this observation and the 'utilization of norm-based scaling in Eq. (10) at every training step': 

1. To approximate the effect of $(G_t-P_tR_t)$, according to the anaysis and discussions in Page 5 line 238-240, we want to scale it to approximate $\psi_t(G_t-P_tR_t)$ or $\psi_t(G_t-P_t\psi_t(R_t))$, that is, the full-rank gradient dynamic with optimizer states of the orthogonal complement or the full-gradient. But the similarity of the scaling factor orders of $\phi_t(R_t)$ with different Galore-ranks (Figure 3 and Table 7) does not sufficiently implies $\phi_t(R_t)\approx \phi_t(G_t-P_tR_t)$ or $\phi_t(R_t)\approx \phi_t(G_t-P_t\psi_t(R_t))$. 
2. The scaling factor orders shown in Figure 3 and Table 7 only consider the top-10 weights matrices. Thus, this evidence does not sufficiently imply this 'stable order phenomenon' holds for all optimizable weight matrices. 
3. Even if the order of scaling factors of all matrices are the same, this can not sufficiently imply the magnitude of the scaling factors can be absorbed into the learning rate (as mentioned in Page 5 line 267). This is because different matrices have different scaling factors, and the equivalent learning rates of all matrices are different. 

According to Table 4, it seems that the performance gain mainly comes from this norm-based scaling. Therefore, it is necessary to identify the motivation and mechanism of how this works and what is the essential effect of this scaling effect.

### Questions
See **Weakness**.

### Soundness
2

### Presentation
1

### Contribution
3
