# $\gamma-$MoD: Exploring Mixture-of-Depth Adaptation for Multimodal Large Language Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Despite the significant progress in multimodal large language models (MLLMs), their high computational cost remains a barrier to real-world deployment. Inspired by the mixture of depths (MoDs) in natural language processing, we aim to address this limitation from the perspective of ``activated tokens''. Our key insight is that if most tokens are redundant for the layer computation, then can be skipped directly via the MoD layer. However, directly converting the dense layers of MLLMs to MoD layers leads to substantial performance degradation. To address this issue,  we propose an innovative MoD adaptation strategy for existing MLLMs called $\gamma$-MoD.  In $\gamma$-MoD,   a novel metric is proposed to guide the deployment of MoDs in the MLLM, namely \textit{rank of attention maps} (ARank). Through ARank, we can effectively identify which layer is redundant and should be replaced with the MoD layer.  Based on ARank,  we further propose two novel designs to maximize the computational sparsity of MLLM while maintaining its performance, namely \textit{shared vision-language router} and \textit{masked routing learning}.   With these designs, more than 90\% dense layers of the MLLM can be effectively converted to the MoD ones. To validate our method, we apply it to three popular MLLMs, and conduct extensive experiments on 9 benchmark datasets.  Experimental results not only validate the significant efficiency benefit of $\gamma$-MoD to existing MLLMs but also confirm its generalization ability on various MLLMs.  For example, with a minor performance drop, \emph{i.e.,} -1.5\%, $\gamma$-MoD can reduce the training and inference time of LLaVA-HR by 31.0\% and 53.2\%, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel Mixture-of-Depth (MoD) adaptation method, $\gamma$-MoD, designed to improve computational efficiency for multimodal large language models (MLLMs). By introducing ARank, a metric to identify redundant layers, $\gamma$-MoD selectively replaces dense layers with MoD layers to reduce computational costs while maintaining performance. The model is validated across several benchmarks, showing promising efficiency gains.

### Strengths
1. $\gamma$-MoD significantly reduces training and inference time by efficiently identifying and replacing redundant layers.
2. The use of ARank as a layer redundancy metric is novel and provides a structured approach to layer selection in MLLMs.
3. The shared vision-language router and masked routing learning modules are thoughtfully designed for multimodal alignment, enhancing the model's performance in cross-modal tasks.

### Weaknesses
1. ARank’s accuracy heavily depends on the diversity and representativeness of the input samples, which may lead to inaccurate redundancy assessment, especially in varied multimodal tasks. The reliance on a small batch of samples for ARank calculation could result in a biased assessment of layer importance, particularly when the dataset exhibits significant intra-class variance or contains outliers. This could lead to suboptimal layer selection for MoD replacement, as the metric might not capture the full range of feature representations required for robust performance across different modalities.
2. ARank’s reliance on low-rank attention maps to identify redundancy may overlook the contextual importance of low-rank layers, which could contain compressed but critical information. The method assumes that low-rank attention maps directly correlate with redundancy, which may not always hold true. Low-rank layers might still encode crucial contextual relationships or fine-grained details that are essential for the model's overall understanding, and discarding them based solely on their rank could lead to a loss of important information.

### Questions
How does $\gamma$-MoD ensure that ARank’s redundancy metric accurately reflects the importance of layers across diverse multimodal tasks, especially given the unique challenges posed by visual information?

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
5

### Summary
This article introduces the Mixture-of-Depth (MoD) scheme into multimodal large language model (MLLM) architectures. By analyzing the rank of attention maps (ARank) of existing MLLMs, the authors identify a model-agnostic and data-agnostic pattern, revealing significant redundancy in certain layers of MLLMs. Building on this insight, the paper proposes the $\gamma$-MoD method, which (1) incorporates a shared vision-language router into existing MLLMs, transforming them into the MoD structure, and (2) employs masked routing learning to adapt MLLM architectures to the MoD scheme by refining the instruction tuning process used during MLLM training. Extensive experiments on multiple multimodal benchmarks and MLLM models demonstrate that $\gamma$-MoD effectively reduces both training and inference time, while largely preserving performance on benchmark tasks.

### Strengths
1. Originality: I appreciate the authors' effort in implementing the MoD scheme in MLLMs in a plug-and-play manner. In my view, the significance of this work lies in maintaining the pre-training stage unchanged, which contrasts with most approaches in the field of sparse LLMs/MLLMs (e.g., MoE structures) that focus on pre-training models from scratch. While there are some aspects that warrant further consideration (see weaknesses & questions), this approach could inspire future research into converting existing models into sparse structures in an off-the-shelf manner.
2. Clarity: This article is mostly well-written. The motivation is clearly articulated and the solutions towards solving the existing problems are logically sound.
3. Experiments: This article conducts extensive experiments across multiple MLLM structures and benchmark datasets to demonstrate the generalizability of $\gamma$-MoD. Their results strongly suggest that $\gamma$-MoD successfully reduces training and inference cost on MLLM models. Abundant analysis experiments also demonstrated that $\gamma$-MoD leads MLLMs to focus on informative tokens and skip the redundant ones.

### Weaknesses
1. Method designs: In the introduction (Line 87), this article suggests that $\gamma$-MoD is a *plug-and-play* method that can be integrated to current MLLMs. Existing MLLMs follow a 2-stage pre-training and instruction tuning training pipeline, and $\gamma$-MoD modifies the instruction tuning pipeline to convert LLaVA models in $\gamma$-MoD-LLaVA structure. In my opinion, this design is arguably *plug-and-play*, since open-source MLLM weights are mostly instruction tuned, so that $\gamma$-MoD cannot be directly applied on published MLLM checkpoints. To evaluate the validity of $\gamma$-MoD, the authors also pre-trains MLLMs on the LCS-558K dataset first. This hinders the applicability of $\gamma$-MoD, as training the $\gamma$-MoD model also requires conducting the complete pre-training pipeline.
2. Further generalizability of $\gamma$-MoD: The experiments in this article primarily focus on LLaVA structures, likely due to the availability of open-source pre-training and instruction tuning datasets, which are necessary for $\gamma$-MoD as it modifies the instruction tuning process. However, as a general method for introducing the MoD scheme to MLLM models, additional experiments on other MLLMs are needed to further demonstrate the generalizability of $\gamma$-MoD.
3. Some ambiguities in the methodology: Key information are missing from the article & Some statements are quite confusing. See Questions for more details.
4. Significance when compared to existing works: In the experiments section, this article finds that most image tokens can be skipped in MLLM inference. This discovery corresponds with [1], in which image tokens are simply pruned from off-the-shelf MLLMs without further training. experiment results in [1] indicates that this simple procedure reduces the FLOPs in MLLMs by over 50% without introducing performance drops, similar to that reported in $\gamma$-MoD. If so, pre-train MLLMs from scratch and modify the instruction tuning methods would be too costly for accelerating an MLLM.

### Questions
Things that WILL affect my overall rating towards this article:

1. Regarding Weakness 1, since the authors consider the disadvantage of MoD to be demanding training from scratch (Line 49-50), the authors should demonstrate how to apply $\gamma$-MoD to existing published MLLM checkpoints, rather than pre-training one from scratch like in the experiment section.
2. Regarding Weakness 2, I would like to see more experiments on other MLLM models beside the LLaVA series. Considering the time of rebuttal and your reported time of training in Table 4, I would like to see this point resolved.
3. Regarding Weakness 3:
   - What is the applied value of the pre-defined sparse target in Equation 4? What is the relationship between the sparse target $\alpha$ and the "routing ratio" and the "skip ratio" in the experiment section?
   - Normally, the sparse target factor $\alpha$ in Equation 4 satisfies $\alpha\in[0, 1]$ , but $\alpha$ is actually the sum of multiple indicator functions with values $\\{0,1\\}$. The left side (value of the sum of indicator function) should be normalized.
   - In Equation 8, the authors put one-hot vectors $\hat{R}$ and $1-\hat{R}$ inside $\log$. This obviously doesn't seem right. Moreover, it is hard to understand what does the routing objective (Equation 8) do in $\gamma$-MoD training. The authors should provide a more detailed explanations of that learning objective.
4. Regarding Weakness 4: Since both works lead to inference acceleration of MLLMs, the authors should provide a detailed comparison with [1] and demonstrate the exclusive advantage of $\gamma$-MoD.

Things that WILL NOT affect my overall rating towards this article:

1. Figure 2 indicates that transformer layers with $\text{Rank}<110$ would be considered as redundant layers. The authors could provide a more detailed analysis on the rank distributions of tested models, instead of giving a figure without quantitative statistics like Figure 3.

[1] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models (ECCV 2024)

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes γ-MoD, a novel mixture-of-depth (MoD) adaptation strategy for existing multimodal large language models (MLLMs). The goal is to maximize computational sparsity while maintaining competitive performance. γ-MoD achieves this by identifying redundant layers using the rank of attention maps (ARank) metric and replacing them with MoD layers. The Key contributions of this paper include: **1.** γ-MoD Framework: A novel MoD framework for sparse computation of existing MLLMs, seamlessly converting most dense layers to sparse MoD layers. **2.** ARank Metric: An metric to measure layer redundancy, guiding the selection of layers for MoD adaptation. **3.** Shared Vision-Language Router and Masked Routing Learning: Designs to maximize the benefits of MoDs in MLLMs, achieving up to 51.6% computational sparsity with minimal performance sacrifice.

### Strengths
1. While MoD has been explored in LLMs, this is the first work to adapt them to MLLMs, which face unique challenges due to the combination of visual and textual modalities.
2. This paper proposes a metric, rank of attention maps (ARank), to identify redundant layers in MLLMs, addressing the lack of guidance in existing MoD approaches.
3. The paper introduces two designs to maximize the benefits of MoD for MLLMs, The Masked Routing Learning prevents critical tokens, such as question subjects, from being skipped during training, preserving the model’s ability to generate accurate answers.
4. This paper provides comprehensive theoretical analysis, empirical validations. And it is well-structured and clearly explains the motivations, methodology, and experimental results.

### Weaknesses
1. The metric ARank seems to be a repurposed version of HRank [1] specifically for attention maps. This connection should be discussed in detail.
2. The ablation study of the routing mechanisms is not enough. This paper only explores a binary routing mechanism (skip or not skip). Exploring more sophisticated routing strategies, such as weighted routing or adaptive routing thresholds and so on, could make the article more comprehensive.
3. While the paper compares γ-MoD with dense and MoE-based MLLMs, it lacks a comparison with other sparsity techniques like pruning or quantization.
4. The author should consider rearranging Table 5 or highlighting the optimal results, as the current version is somewhat challenging to compare the results of different methods

### Questions
1. In this paper, the binary mask Mq assigned the question tokens to 0. Therefore, during the training process, the value of Mq should be fixed. But for different tasks or datasets, the location of the question tokens may be different. How did the author determine and design Mq on different tasks or datasets?
2. I would like to know how the "All layer" in Table 1 is specifically implemented.
3. How sensitive is ARank to the choice of hyperparameters, such as the batch used for estimation?
4. What are the criteria for determining the threshold for converting dense layers to MoD layers based on ARank values? Is there a more principled way to set this threshold?

### Soundness
3

### Presentation
3

### Contribution
3
