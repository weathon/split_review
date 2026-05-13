# PerPO: Perceptual Preference Optimization via Discriminative Rewarding

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
This paper presents Perceptual Preference Optimization (PerPO), a perception alignment method aimed at addressing the visual discrimination challenges in generative pre-trained multimodal large language models (MLLMs). PerPO employs discriminative rewarding and listwise preference optimization to align MLLMs with human visual perception processes. By utilizing the reward as a quantitative margin for ranking, our method effectively bridges generative preference optimization and discriminative empirical risk minimization. PerPO significantly enhances MLLMs’ visual discrimination capabilities while maintaining their generative strengths, mitigates image-unconditional reward hacking, and ensures consistent performance across visual tasks. This work marks a crucial step towards more perceptually aligned and versatile MLLMs. We also anticipate that PerPO will inspire the community to reconsider MLLM alignment strategies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes PerPO, a listwise reward optimization algorithm to address the poor visual discrimination performance of MLLMs and the reward hacking issues in DPO. Specifically, the authors propose to (1) directly use the task-specific score in the output space as the discriminative reward; (2) using a list of negative discrimination rewards can reduce reward hacking. While the authors show a variety of empirical results, this paper lacks a more informative explanation on why such a method can address the critical issue it mentioned.

### Strengths
+ This paper discusses an important topic by investigating the reward optimization issue in MLLMs, and they believe this fundamental issue derives from a misspecified reward definition and reward hacking in DPO. They propose corresponding measures to address issue.
+ This paper contains many empirical results.

### Weaknesses
 + While this paper provides many empirical results (e.g. the authors constantly referring to fig.1), the authors only explain their method with intuition, while a more in-depth or theoretical analysis is expected for a paper like this. Only empirical results are not convincing enough.
+ Since this paper simply uses the scalar task-specific discriminative score as the reward, why don't the authors compare their method to PPO while using the reward they defined? It seems equation (8) also seeks to optimize a list of accumulated scalar rewards like PPO did. Could the authors provide more thorough theoretical analysis on the difference of PerPO and PPO, especially in terms of optimization objective and smoothness?
+ It is not very clear why the authors use a list of "negative" rewards? Why woul negative only rewards be sufficient and good enough to optimize using their objective?

### Questions
See above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes Perceptual Preference Optimization (PerPO) for aligning multimodal large language models (MLLMs) in discriminative vision-language tasks such as object grounding and OCR. By introducing the discriminative reward (measured by the discrepancy between the prediction and the ground truth) into the pairwise weighting in Listwise Preference Optimization (LiPO), PerPO enables sample-efficient alignment of generative MLLMs in discriminative tasks. Empirical results validates that PerPO achieves better performance than DPO and SFT in visual discriminative tasks such as object grounding and dense OCR.

### Strengths
1. The writing is clear and smooth, providing great explanation of the background and the proposed method.

2. Compared with DPO and SFT, PerPO enables more sample-efficient alignment for visual discriminative tasks.

3. PerPO also improves general image understanding and mitigates image-unconditional reward hacking.

### Weaknesses
 1. The evaluation of general vision-language comprehension is based on LLaVA-Bench-in-the-Wild (LLaVA$^W$), a very tiny benchmark with less than 100 samples. The scores may not sufficiently reflect the MLLM image understanding ability. Larger, widely adopted benchmarks such as VQAv2 and MM-Bench are preferred.

2. In Section 5.1, it is claimed that "discriminative reward also aligns well with human," but the results are evaluated by GPT-4o, not human users.

3. From Figure 2(b), the performance on RefCOCO+ seems to saturate after data size > 5k, and more such data can hurt general vision-language capabilities (shown by lowered LLaVA$^W$ scores). Therefore, including more finetuning data does not seem to support PerPO in this scenario. Do SFT and DPO show similar trends? Is PerPO only better than SFT and DPO when the finetuning data scale is small?

4. The tested MLLM and visual perception tasks are somewhat limited (only LLaVA-1.5 and LLaVA-NeXT on object grounding and dense OCR). Thus, the generalizability of PerPO may be unclear. It would be better to include results on more MLLMs (e.g., Cambrian-1, LLaVA-OneVision, Qwen2-VL) and visual tasks (e.g., LISA or GLaMM on segmentation).

### Questions
Please check the weakness section above.

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
3

### Summary
The paper presents an approach termed Perceptual Preference Optimization (PerPO) aimed at addressing visual discrimination challenges in generative pre-trained multimodal large language models (MLLMs). The goal of PerPO is to enhance the models' visual discrimination capabilities while maintaining their generative strengths. The approach utilizes discriminative rewarding and listwise preference optimization to align MLLMs with human visual perception processes. The experiments demonstrate that PerPO significantly improves model performance across various visual tasks and contributes to more perceptually aligned and versatile MLLMs.

### Strengths
The paper has several strengths. Firstly, it addresses an important challenge in the field of MLLMs, i.e., visual discrimination. Secondly, it presents a novel approach (PerPO) that bridges the gap between generative and discriminative functionalities of MLLMs, and does so effectively according to comprehensive empirical evaluations presented in the paper. Moreover, the PerPO framework reduces the reliance on human annotations for model training, which is a substantial contribution towards scalable and efficient training of MLLMs. Furthermore, the premise of the paper, the methodology, and the evaluations are clearly articulated and well organized, which enhances its readability and digestibility.

### Weaknesses
One significant weakness is that the effectiveness of PerPO highly depends on specific datasets, potentially limiting its generalization. The paper also acknowledges a limitation where complex tasks may still require human annotations, which might not always be feasible. Moreover, there might be a lack of comprehensive experiments demonstrating the performance of PerPO across a spectrum of different domains, which would validate its claim of general applicability further. Specifically, the reliance on datasets with well-defined answers for visual discrimination tasks raises concerns about the model's ability to handle more ambiguous or open-ended visual inputs. The current evaluation may not fully capture the nuances of real-world visual understanding, where tasks often involve subjective interpretations and contextual reasoning beyond simple object recognition or text extraction. Furthermore, the paper does not adequately address the potential for bias in the datasets used for training and evaluation, which could lead to skewed performance results and limit the practical applicability of the proposed method.

### Questions
1. Could you provide a more detailed explanation of the specific enhancements in MLLM's visual discrimination capabilities by PerPO?
2. How does the model perform when presented with complex visual tasks that require intricate discrimination capabilities?
3. How is the limitation associated with dependency on specific datasets planned to be addressed in future work?
4. Are there plans to integrate PerPO with other existing models or approaches to further improve the overall performance of MLLMs in diverse domains?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Perceptual Preference Optimization (PerPO), a method designed to enhance the visual discrimination abilities of multimodal large language models (MLLMs). By using discriminative rewards and listwise preference optimization, PerPO aligns MLLMs with human perception, addressing issues like image-unconditional reward hacking. It improves MLLM performance in visual tasks, such as object grounding and OCR, while maintaining generative capabilities and demonstrating generalizability across models and tasks.

### Strengths
1. This paper addresses a unique and intriguing research question by exploring the discriminative abilities of multimodal large language models (MLLMs), a direction not commonly emphasized in current studies.
2. Experiments demonstrate PerPO's superiority over baseline techniques like Direct Preference Optimization (DPO) across multiple benchmarks and visual tasks, highlighting its broad applicability and effectiveness.

### Weaknesses
1. The paper argues that the primary limitation in the visual discrimination capabilities of MLLMs is due to a lack of explicit perceptual alignment, but it does not provide sufficient evidence to support this claim. There is no experimental evidence that this issue arises from the alignment stage rather than other factors such as instruction tuning or an insufficient pre-training dataset. I recommend that the authors present more compelling evidence to confirm the assertion that the main challenge in the "limitations in MLLMs' visual discrimination" is mainly related to "perceptual alignment."
2. The current method may encounter limitations when applied to complex visual tasks that require significant contextual understanding. While these challenges are briefly mentioned, they are not fully investigated in the study.

### Questions
1. In Table 1, the performance of the LLaVA-Next model with PerPO shows a noticeable decrease. Could the authors explain the reasons behind this performance drop?
2. Could the authors provide results on the effect of scaling up the model on the discriminative reward?

### Soundness
3

### Presentation
2

### Contribution
2
