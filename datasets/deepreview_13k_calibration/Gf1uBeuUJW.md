# Unhackable Temporal Reward for Scalable Video MLLMs

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
In the pursuit of superior video-processing MLLMs, we have encountered a perplexing paradox: the “anti-scaling law”, where more data and larger models lead to worse performance. This study unmasks the culprit: “temporal hacking”, a phenomenon where models shortcut by fixating on select frames, missing the full video narrative. In this work, we systematically establish a comprehensive theory of temporal hacking, defining it from a reinforcement learning perspective, introducing the Temporal Perplexity (TPL) score to assess this misalignment, and proposing the Unhackable Temporal Rewarding (UTR) framework to mitigate the temporal hacking. Both theoretically and empirically, TPL proves to be a reliable indicator of temporal modeling quality, correlating strongly with frame activation patterns. Extensive experiments reveal that UTR not only counters temporal hacking but significantly elevates video comprehension capabilities. This work not only advances video-AI systems but also illuminates the critical importance of aligning proxy rewards with true objectives in MLLM development.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses a critical problem in MLLMs for video processing: "temporal hacking," where models simplify the task by focusing on select frames, missing broader context. The authors propose a framework called UTR that mitigates temporal hacking by emphasizing consistent frame activation across the entire video, leading to more accurate video comprehension. This framework incorporates TPL to quantify misalignment in temporal modeling and guides the model through two key principles: high frame information density and inter-frame information dynamics.

### Strengths
1.  The paper introduces temporal hacking as a new perspective on reward hacking in RL and effectively adapts this concept to video MLLMs.
2. TPL score is a notable contribution, providing a quantitative way to assess temporal misalignment, a challenge often overlooked in video modeling.
3. The approach shows promise for scalability with additional data, making it versatile for future applications and datasets.
4. The results are good comparing to various larger models.

### Weaknesses
1. UTR relies on high-density, high-dynamic frame descriptions. Several datasets is lack of this, I am wondering how are the other methods performance could be improved after simply data modeling.
2. The ablation study is confusing, does table 3 "-Data Modeling" means no data modeling and no task modeling or just no data modeling? 
The comparison data scale is different which is unfair to compare.
3. For ablation result, the Video-UTO is not the best without Data Modeling on MMVet and also UTR-Data size of 180K results are sometimes worse than 0K is also confusing.

### Questions
1. How is equation 6 used in loss function?
2. For equation 6, why using T:T instead of T-t:T for the second term?
3. Is that possible to get the TPL of your baselines comparing with Video-UTO?

### Soundness
2

### Presentation
2

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
This paper thoroughly analyzes the phenomenon of temporal hacking, where video MLLM learns to spuriously correlate its answer to query prompts to a subset of selected frames without considering the whole video context. The author introduces temporal perplexity (TPL) to assess this misalignment, showing a good correlation with model performance. Moreover, the author proposes the Unhackable Temporal Rewarding (UTR) frameworks and empirically demonstrates their effectiveness by comparing their methods with several open-sourced MLLM.

### Strengths
1. The proposed $\mathcal{T}\_{tpl}$ is interesting and correlates well with the model performance.

2. This paper systematically analyzes reward hacking from the RL perspective and proposes two guiding principles for designing unhackable rewards.

3. The proposed method Video-UTR outperforms several baseline methods on both video and image understanding tasks.

### Weaknesses
- **Over-complicated Presentation**: I feel the presentation of the paper is unnecessarily complicated and does not explain the details sufficiently. The paper spends too much space introducing the concept of **temporal hacking**, which can be efficiently summarized as *existing training data and objectives make the learned MLLM find shortcuts when answering the query prompt by spuriously correlating the answers with only a subset of video frames, ignoring the whole video frame context.* In contrast, the author is supposed to provide more details of their proposed methods in Section 3.2 instead of putting them in the Appendix.

- **Lack of detailed description of the proposed TPL $\mathcal{T}_{tpl}$**: Equation 6 defines $\mathcal{T}_{tpl}$, which requires query the function $\mathcal{R}_{ppl}$. However, the paper does not provide details about $\mathcal{R}_{ppl}$ other than citing the original paper developed the $\mathcal{R}_{ppl}$. For example, does calculating the $\mathcal{R}_{ppl}$ require access to a specific MLLM?

- **Empirical results**: comparison between the proposed Video-UTR and LLaVA-OneVision is insufficient. The paper only reports LLaVA-OneVision’s results on 3 out of 7 benchmarks, where it outperforms Video-UTR on 2 out of those 3. Besides, the authors should underline PLLaVA's accuracy for ANet-QA rather than underlining their Video-UTR. Additionally, the authors should include results for MLLMs that are also finetuned from QWen2-7B in Table 2. Without these results, it is difficult to assess the source of the performance improvements.

- **Regarding the RL perspective**: Reward hacking is not exclusive to reinforcement learning, as RL is just one approach to maximizing a reward function. In the field of aligning pretrained visual generation models, several methods optimize toward a reward model by directly backpropagating gradients from a differentiable reward model. These approaches are also susceptible to reward hacking, as discussed in [1, 2]. Reward hacking generally occurs when the learning objective fails to fully capture the intended model behavior. I recommend revising this statement and including a citation for [1,2] to provide a broader context.

Minor:

- **Lack of detailed figure captions**: The authors should thoroughly explain each figure within the main text rather than leaving readers to infer their meanings.

- **Missing citations**: Various benchmarks have recently been proposed to evaluate MLLM's video understanding capabilities, e.g., [3, 4]. The authors should consider evaluating their methods on these benchmarks and cite them in the related works sections.

Overall, the presentation of the paper can be significantly improved.

### Questions
1. There is an inconsistency between Table 1 and the text in Line 376 regarding the data scale used for Video-UTR. Table 1 lists the data scale as 1.1M, whereas Line 376 claims the performance is achieved with approximately 700K video data points. Which number is correct?

### Soundness
3

### Presentation
2

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
The paper addresses a paradox observed in training video-processing Multimodal Large Language Models (MLLMs), termed the "anti-scaling law," where increasing data and model size leads to decreased performance. The authors identify "temporal hacking" as the culprit—a phenomenon where models focus on select frames instead of capturing the full video narrative, effectively shortcutting temporal understanding. I believe this behaviour is analogous to posterior collapse in VAEs, where models find ways to ignore part of the input while still optimizing the objective, suggesting a fundamental challenge in enforcing comprehensive information utilization in deep learning models. The authors present a theoretical framework from a reinforcement learning perspective to explain temporal hacking and introduce the Temporal Perplexity (TPL) score as a metric to assess misalignment in temporal modelling. To mitigate temporal hacking, they propose the Unhackable Temporal Rewarding (UTR) framework, which enhances video comprehension by aligning proxy rewards with true objectives through spatiotemporal attribute extraction and bidirectional querying. This solution addresses the root cause: the misalignment between training objectives and desired behaviour in video understanding. Empirical results show that TPL correlates strongly with temporal modelling quality and that UTR significantly improves video MLLMs' performance across multiple benchmarks, while also demonstrating scalability with increased data and frame lengths.

### Strengths
- **Originality**: The paper introduces the novel concept of temporal hacking in video MLLMs and frames it within a reinforcement learning context, offering a fresh perspective on the anti-scaling issue.
- **Theoretical foundation**: The reinforcement learning perspective provides clear insights into the problem and guides the development of the solution.
- **Practical metric**: The introduction of the Temporal Perplexity (TPL) score provides a quantifiable measure of temporal misalignment, which correlates with model performance and can guide future research.
- **Proposed solution**: The Unhackable Temporal Rewarding (UTR) framework is a constructive approach to mitigate temporal hacking, showing significant improvements in video comprehension tasks.
- **Comprehensive evaluation**: The paper presents extensive experiments across multiple benchmarks and includes detailed ablation studies, demonstrating the effectiveness of the proposed methods.
- **Practical impact**: The proposed solution is implementable and shows strong empirical results, indicating its potential applicability in real-world video MLLMs.

### Weaknesses
 - **Clarity and organization**: My main issue is that the paper's presentation suffers from unclear explanations and a lack of cohesion in some sections. Technical terms are sometimes introduced without sufficient context, making it hard to follow, at least to me. I even found Figure 1, which aims to provide a clear illustration of the phenomenon, relatively unclear. Specifically, the description of the 'temporal hacking' phenomenon lacks a clear, step-by-step explanation of how the model exploits temporal shortcuts. The connection between the reinforcement learning framework and the observed behavior is not immediately obvious, and the paper would benefit from a more detailed walkthrough of this relationship. The introduction of the Temporal Perplexity (TPL) score also lacks sufficient motivation, leaving the reader wondering why this specific metric was chosen and how it directly relates to the 'temporal hacking' problem.
- **Limited discussion of computational overhead**: While the supplementary material provides some training details, the paper lacks a thorough analysis of the computational cost introduced by the UTR framework, particularly regarding the extraction of spatiotemporal attributes using expert models. This makes it difficult to assess the practicality and scalability of the approach compared to existing methods. The paper should include a detailed breakdown of the time and resources required for each stage of the UTR pipeline, including attribute extraction, trajectory construction, and the final training of the video MLLM. A comparison of these costs with those of standard video MLLM training would be beneficial.
- **Dependency on expert models**: The method relies heavily on the accuracy of expert models for attribute extraction, which may limit its applicability if these models are not sufficiently accurate or if they introduce significant computational overhead. The paper does not explore the sensitivity of the UTR framework to the quality of these expert models. It would be important to analyze how the performance of UTR degrades when using less accurate or computationally cheaper expert models. Furthermore, the potential for biases in the expert models to propagate into the final MLLM should be discussed.
- **Theoretical depth**: The reinforcement learning framework and the concept of temporal hacking could be more rigorously developed. Definitions and theoretical justifications need strengthening. The paper would benefit from a more formal definition of 'temporal hacking' and a more rigorous derivation of the reinforcement learning framework. The connection between the proposed reward function and the desired behavior should be made more explicit. The paper should also discuss the limitations of the reinforcement learning analogy and potential alternative theoretical frameworks.
- **Related work**: There is a lack of thorough comparison with existing methods addressing similar issues, which limits understanding of the paper's novelty and significance in the broader context. The paper should discuss how UTR compares to other techniques for improving temporal modeling in video MLLMs, such as attention mechanisms or temporal convolutions. A more comprehensive review of existing literature would help to contextualize the contribution of this work.
- **Limited exploration of failure cases**: The paper could benefit from more analysis of scenarios where UTR might not perform well, such as with highly redundant or static video content. The paper should discuss potential failure modes of UTR and provide examples of video content where the method might struggle. This would help to better understand the limitations of the approach and guide future research.
- **Reproducibility**: Details on experimental settings, such as hyperparameters, data preprocessing, and model configurations, are insufficient, hindering the ability to replicate results. The paper should include a detailed description of all experimental settings, including the specific hyperparameters used for training, the data preprocessing steps, and the architecture of the MLLM. The authors should also consider releasing their code and data to facilitate reproducibility.

### Questions
1. Could the authors provide more detailed explanations of the TPL score calculation and its computational overhead? How does it scale with longer video sequences?
2. How does the computational complexity of UTR compare to existing video MLLM approaches? Is the additional overhead from attribute extraction justified by the performance gains?
3. Have the authors explored how the quality and computational cost of expert models affect the final performance? Is there a minimum accuracy threshold needed for these models, and how does their use impact the overall training time?
4. Are there any limitations or potential drawbacks to the UTR approach in scenarios with highly redundant or static video content?
5. Could the authors provide more details about how TPL correlates with human judgment of video understanding quality?
6. Can the framework be applied to other domains involving sequential data, such as speech or time-series analysis?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Unhackable Temporal Rewarding (UTR), a framework to improve multimodal large language models (MLLMs) by addressing a phenomenon called "temporal hacking". This phenomenon occurs when MLLMs, which process video frames sequentially to understand narratives, exploit shortcuts by focusing on only a few frames (sometimes just the first and the last), thereby missing the entire context. This issue has led to an anti-scaling paradox where increasing model size or data volume degrades performance. The authors propose UTR to counteract this problem by enforcing comprehensive temporal processing, ensuring the model engages with the full video content.

### Strengths
The paper is well-written, with the key contributions listed clearly in the introduction. The authors also identified relevant literature in this line of research and highlighted their contributions in the paper. The authors introduce very fundamental principles that should be used to design a video captioning metric, which are high frame information density and high inter-frame information dynamics. They construct a metric by extracting the location, appearance, and action information of subjects in a frame using pre-trained models. They construct datasets based on 3 open-source video datasets, from which they extract subject attributions from each frame in the video.

### Weaknesses
1. Since the proposed metric relies on subject attributions extracted from pre-trained models, the errors from those models might propagate into the extracted metadata and subsequent make the metric unreliable. Can the authors comment on whether this is a viable concern?
2. Have the authors measured the reliability of extracted metrics in the presence of multiple subjects in one frame?

### Questions
Please see weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3
