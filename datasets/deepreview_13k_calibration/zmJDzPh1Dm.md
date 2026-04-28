# Nemesis: Normalizing the Soft-prompt Vectors of Vision-Language Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
With the prevalence of large-scale pretrained vision-language models (VLMs), such as CLIP, soft-prompt tuning has become a popular method for adapting these models to various downstream tasks. However, few works delve into the inherent properties of learnable soft-prompt vectors, specifically the impact of their norms to the performance of VLMs. This motivates us to pose an unexplored research question: ``Do we need to normalize the soft prompts in VLMs?'' To fill this research gap, we first uncover a phenomenon, called the \textbf{Low-Norm Effect} by performing extensive corruption experiments, suggesting that reducing the norms of certain learned prompts occasionally enhances the performance of VLMs, while increasing them often degrades it. To harness this effect, we propose a novel method named \textbf{N}ormalizing th\textbf{e} soft-pro\textbf{m}pt v\textbf{e}ctors of vi\textbf{si}on-language model\textbf{s} (\textbf{Nemesis}) to normalize soft-prompt vectors in VLMs. To the best of our knowledge, our work is the first to systematically investigate the role of norms of soft-prompt vector in VLMs, offering valuable insights for future research in soft-prompt tuning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discussed the influence of soft-prompt to VLM, introduced REPLACE and RESCALE corruption affecting VLM, and proposed two normalization loss improving the performance of soft-prompt. The authors conducted a lot of experiments to confirm the effectiveness of method.

### Strengths
1、The paper is the first study to discuss the influence of soft-prompt toward VLM.
2、The paper conducted REPLACE and RESCALE to discuss the normalization of soft-prompt, and proposed Nemesis including two normalization losses to improve the effectiveness of soft-prompt.
3、The paper has conducted a lot of experiments to prove the effectiveness of the method.

### Weaknesses
1、The writing of some parts of the paper are not clear enough. It is recommended that the authors check. For example, there is a discrepancy between formula 4 and the symbol definition in the previous paragraph.
2、The two types of losses proposed in the paper lack a correlation with practical significance, suggesting authors discuss why the two forms of normalization affect soft prompt. Specifically, it's unclear how the proposed losses relate to the underlying mechanisms of soft prompt optimization, and how they affect the learned representations.
3、The paper lacks discussion on the applicable scenarios of two normalization losses. It is not clear under what conditions one loss should be preferred over the other, and what specific characteristics of the task or dataset would make each loss more suitable.

### Questions
1、The paper proposes two normalization methods, while only testing the effects of PEN and PAN on the experimental results respectively. Why cannot both types of losses be used simultaneously? If there is a contradiction between the two losses, it is recommended that the authors discuss the differences. If the two losses are similar, can the two losses be unified? If the two losses gain from different perspective, should relevant experiments be provided?
2、Can author discuss application circumstance of two normalization methods? In practical applications, what kind of normalization loss should we choose for what situation? Suggest the authors to discuss.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper, at its core, explores the significant yet uncharted territory around the impact of norms of soft-prompt vectors on the performance of vision-language models (VLMs), like CLIP. The authors have brought to light a unique phenomenon termed the "Low-Norm Effect", highlighting how reducing norms of specific learned prompts can sometimes boost the performance of VLMs. The effect seems to be more prevalent in certain datasets like Imagenet, OxfordPets, and Food101 as compared to others. Interestingly, the Low-Norm Effect appears to have a stronger presence when there's limited training data, hinting at potential issues with soft-prompt methods under data constraints.

To harness this Low-Norm Effect, the paper proposes a method named "Nemesis". This approach introduces two techniques – Position Equality Normalization (PEN) loss and the more refined Position Awareness Normalization (PAN) loss. While the PEN loss aims to normalize the norms of all prompt vectors, the PAN loss is more discerning, identifying positions that might induce the Low-Norm Effect before selectively normalizing them. The authors suggest that this method can notably enhance VLM performance without incurring significant computational costs.

### Strengths
1. The paper pioneers a systematic investigation into the role of soft-prompt vector norms in VLMs, addressing a previously unexplored research question.

2. The proposed Nemesis method, with its innovative PEN and PAN losses, offers a potential solution to the Low-Norm Effect, showing promise for improving VLM performance.

3. Extensive corruption experiments shed light on the Low-Norm Effect's impact, providing valuable insights for future soft-prompt tuning endeavors.

### Weaknesses
1. $\beta$ can be either 0 or 1, corresponding to two variants of the proposed Nemesis method. However, there is no ablation study on the selection of $\beta$, nor is there an exploration of the potential impact of setting $\beta$ with decimal values to assign weights to the two methods.

2. The paper introduces a pre-inference step before each training batch to identify positions inducing the Low-Norm Effect. Such a step could introduce computational overhead, especially with larger datasets or when rapid training iterations are required. The study hasn’t provided a detailed analysis of the computational cost or time implications this might have in different scenarios.

3. The Position Equality Normalization (PEN) loss applies equal weight to the norms of soft prompts at all positions. While the paper does acknowledge that normalizing prompt vectors at positions unaffected by the Low-Norm Effect may not yield performance improvement, the inherent assumption of the universality of the Low-Norm Effect across positions may not hold true for all datasets or real-world scenarios. The approach could benefit from a more dynamic, adaptive mechanism.

4. The paper utilizes the RESCALE operation with a specific rescaling factor, τ, described as a positive real number less than 1. However, there’s no mention of how the value of τ is determined, if it's consistent across datasets, or its sensitivity. The choice of τ could have implications on the effectiveness of the Nemesis method, and without clear insight into its selection, there’s potential variability in results.

### Questions
Given the significance of the parameter $\beta$ in differentiating between the two variants of the Nemesis method, why was an ablation study not conducted to evaluate its impact? Additionally, have you considered exploring decimal values for $\beta$ to potentially strike a balance between the effects of the PEN and PAN losses?

How does the proposed Nemesis method compare with other soft-prompt tuning methods in terms of computational efficiency and scalability, especially in larger datasets or more complex tasks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper answers the question "do we need to normalize the soft prompts in VLMs?" by (1) uncovering a phenomenon called the low-norm effect and (2) proposing a new method named normalizing the soft-prompt vectors of vision-language models (Nemesis) to normalize soft-prompt vectors in VLMs. The contributions include, (1) new soft-prompt vector normalization method for VLMs (normalizing soft prompts during soft-prompt tuning), (2) better results when evaluated by domain generalization settings for VLMs.

### Strengths
(1) new soft-prompt vector normalization method for VLMs, which can be incorporated into any soft-prompt based methods;
(2) better results when evaluated by domain generalization settings for VLMs.

### Weaknesses
1. prefer to learn more details of how you decide the length of soft prompt vectors, e.g., why 4 and 16, will there be more ranges to be investigated basing on the specificl tasks for VLMs?
2. prefer to learn more investigations of combining Nemesis with existing PEFT algorithms to see if the results can be further improved or not so that other researchers can better leverage your method to their existing frameworks.

### Questions
1. could there be a combination of between soft-prompt tuning and hard-prompt tuning? (hard = explicitly use some predefined words/phrases as part of the prompts);
2. any idea of further combining existing PEFT (prompt tuning, prefix tuning, LoRA...) with your Nemesis method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
