# Visual Instruction Tuning with 500x Fewer Parameters through Modality Linear Representation-Steering

- Decision: Reject
- Scores: 8, 6, 5, 6

## Abstract
Multimodal Large Language Models (MLLMs) have significantly advanced visual tasks by integrating visual representations into large language models (LLMs). The textual modality, inherited from LLMs, equips MLLMs with abilities like instruction following and in-context learning. In contrast, the visual modality enhances performance in downstream tasks by leveraging rich semantic content, spatial information, and grounding capabilities. These intrinsic modalities work synergistically across various visual tasks.
Our research initially reveals a persistent imbalance between these modalities, with text often dominating output generation during visual instruction tuning. This imbalance occurs when using both full fine-tuning and parameter-efficient fine-tuning (PEFT) methods. We then found that re-balancing these modalities can significantly reduce the number of trainable parameters required, inspiring a direction for further optimizing visual instruction tuning. Hence, in this paper, we introduce Modality Linear Representation-Steering (MoReS) to achieve the goal. MoReS effectively re-balances the intrinsic modalities throughout the model, where the key idea is to steer visual representations through linear transformations in the visual subspace across each model layer. 
To validate our solution, we composed LLaVA Steering, a suite of models integrated with the proposed MoReS method. Evaluation results show that the composed LLaVA Steering models require, on average, 500 times fewer trainable parameters than LoRA needs while still achieving comparable performance across three visual benchmarks and eight visual question-answering tasks.
Last, we present the LLaVA Steering Factory, an in-house developed platform that enables researchers to quickly customize various MLLMs with component-based architecture for seamlessly integrating state-of-the-art models, and evaluate their intrinsic modality imbalance. This open-source project enriches the research community to gain a deeper understanding of MLLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces Modality Linear Representation-Steering (MoReS), a new parameter-efficient fine-tuning method for Multimodal Large Language Models (MLLMs) that addresses the imbalance between text and visual modalities during visual instruction tuning. The authors note that existing methods like LoRA underutilize visual information, resulting in text-dominant outputs. MoReS remedies this by steering visual representations through linear transformations in a lower-dimensional subspace at each layer, re-balancing modality influence without altering core LLM parameters. Experiments with LLaVA Steering models show that MoReS matches LoRA's performance on various visual benchmarks and VQA tasks while using up to 500 times fewer trainable parameters. Additionally, the paper introduces the LLaVA Steering Factory, a flexible framework for developing and evaluating MLLMs, which aids in research on modality imbalance and simplifies the integration of different model components.

### Strengths
1. The paper is well-written and easy to understand. The motivation for addressing modality imbalance is clearly stated, and the MoReS method is illustrated with diagrams and mathematical formulations. The experimental setup and results are also clearly presented. 

2. The experimental evaluation covers multiple visual benchmarks and VQA tasks, comparing LLaVA Steering with established baselines and demonstrating its effectiveness.

3. LLaVA Steering models demonstrate a substantial reduction in trainable parameters (up to 500x less than LoRA) while maintaining comparable performance, making visual instruction tuning more accessible.

4. I like the idea of designing "steering" mechanism to balance the multi-modal clues. The use of linear transformations within a subspace to steer visual representations is a clever and seems an efficient way to achieve modality balance without significantly increasing the number of trainable parameters.

### Weaknesses
1. The motivation presented is unconvincing. In my view, relying more on visual information may not yield correct answers for certain Visual Question Answering (VQA) tasks, as many of these tasks require the MLLM to possess relevant world knowledge in addition to visual cues. It would be helpful to provide specific examples that illustrate how the "steering" module functions across different tasks that require either visual or textual information. In the current version, while experimental results are provided, they are insufficient on their own; understanding the underlying reasons— the "why"—is equally important for a persuasive argument. 

2. Insufficient ablation studies. While the comparison with LoRA provides a good baseline, the paper would benefit from more ablation studies to analyze the contribution of different components of MoReS. For example, exploring the impact of removing the linear transformations in certain layers or varying the downsampling rate could provide valuable insights.

3. Although I like the general idea of "steering" in terms of different modalities, the downsampling function $\phi$ within MoReS lacks a detailed explanation of its implementation and the rationale behind the chosen dimensionality. This makes it difficult to fully understand the mechanism and reproduce the results. Further clarification on the impact of subspace dimensionality on performance would strengthen the paper. Furthermore, as with the reparameterization trick underlying LoRA, this work should also include a theoretical analysis of the proposed method.

### Questions
see "weaknesses"

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
4

### Summary
The paper introduces Modality Linear Representation-Steering (MoReS), a parameter-efficient fine-tuning method for multimodal LLMs that aims to address modality imbalance between visual and textual representations. The key idea is to steer visual representations through linear transformations similar to LoRA but in a reduced subspace across model layers. They also introduce LLaVA Steering Factory, a framework for developing and evaluating MLLMs.

### Strengths
Novel perspective on modality balancing in MLLMs through representation steering. 

Comprehensive empirical evaluation across multiple benchmarks and ablations. 

Open-source framework (LLaVA Steering Factory) that could benefit the research community

### Weaknesses
Unclear correlation between attention scores and performance. Full models performing better despite lower attention scores. The paper lacks causal analysis demonstrating that higher visual attention scores lead to better performance

The comparison to LoRA's parameter count may be misleading since LoRA can be configured with very small ranks. And with adapter methods, most compute for training MMLM still happen in the heavy frozen backbone.

Missing discussion on computational overhead: Unlike LoRA, MoReS transformations appear to require additional runtime compute. Lora can be merged into the backbone matrices but the isolated MoReS seem not.

### Questions
Have you explored whether the increased visual attention scores directly contribute to improved performance? 

Is there a way to merge/optimize the MoReS transformations into the base model to reduce runtime overhead?

### Soundness
3

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
4

### Summary
I found this paper to be an innovative contribution to the field of multimodal AI. The researchers tackle a fascinating challenge: the imbalance between text and visual processing in multimodal language models. 

They've developed a clever approach called MoReS that dramatically reduces the number of parameters needed for visual instruction tuning - we're talking about using 500 times fewer parameters while maintaining comparable performance.

### Strengths
In this paper, the researchers have spotted something that others seemed to have missed - there's an inherent imbalance in how these models handle text versus visual information. Meanwhile, the development of the LLaVA Steering Factory provides a valuable contribution to the research community, offering a standardized framework for implementing and evaluating various MLLM architectures and training strategies.

### Weaknesses
Overall, I feel that the contributions of this paper are insufficient. The discovery of the modality imbalance is not original, and the proposed method does not demonstrate particularly outstanding performance compared to existing approaches.

At last, I think the LLaVA Steering Factory is not an academic innovation, it's more like an engineering contributions.

### Questions
How does the performance of MoReS change when dealing with images that contain both rich textual and visual information? Is there a potential trade-off between visual and textual understanding when rebalancing the modalities?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an approach to visual instruction tuning for MLLMs by introducing Modality Linear Representation-Steering (MoReS). The MoReS method addresses the issue of intrinsic modality imbalance where textual data tends to dominate visual data during tuning by steering visual representations through linear transformations within the model’s layers. This technique reduces the number of trainable parameters required by up to 500 times compared to traditional methods while maintaining competitive performance across visual benchmarks and question-answering tasks. The authors also developed the LLaVA Steering Factory, an open-source framework that enables researchers to customize and experiment with MLLMs more effectively.

### Strengths
1. The MoReS provides a solution to balancing visual and textual modalities, reducing computational requirements without sacrificing performance.
2. The MoReS significantly lowers trainable parameters compared to established techniques, like LoRA and full fine-tuning, making it a resource-efficient alternative.
3. This method is tested across multiple model sizes and visual benchmarks, with consistent performance, demonstrating its robustness.
4. The development of the LLaVA Steering Factory offers a tool for the research community.

### Weaknesses
1. MoReS aims to improve the visual attention score distribution. However, is a higher visual attention score necessarily better? I hope the authors can conduct an exploratory experiment on this aspect to provide more insight for the readers.
2. Although the model is effective on visual benchmarks, its performance on entirely text-only tasks has not been tested, leaving questions about its generalizability.
3. Table 2 and Table 3 describe the results of different benchmarks. However, there is an anomaly: the performance of the 3B parameter model is significantly higher than that of the 7B and 13B parameter models.
4. FastV[1] finds that attention computation over visual tokens is extremely inefficient in the deep layers of popular LVLMs, suggesting a need for a sparser approach compared to textual data handling. Therefore, this implies that in the deep layers, the role of visual attention is not very significant, raising the question of whether increasing its attention score in these layers is necessary.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
