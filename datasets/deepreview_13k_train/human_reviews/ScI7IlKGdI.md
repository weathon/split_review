# Spurious Forgetting in Continual Learning of Language Models

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
Recent advancements in large language models (LLMs) reveal a perplexing phenomenon in continual learning: despite extensive training, models experience significant performance declines, raising questions about task alignment and underlying knowledge retention. This study first explores the concept of "spurious forgetting", proposing that such performance drops often reflect a decline in task alignment rather than true knowledge loss. Through controlled experiments with a synthesized dataset, we investigate the dynamics of model performance during the initial training phases of new tasks, discovering that early optimization steps can disrupt previously established task alignments. Our theoretical analysis connects these shifts to orthogonal updates in model weights, providing a robust framework for understanding this behavior. Ultimately, we introduce a Freezing strategy that fix the bottom layers of the model, leading to substantial improvements in four continual learning scenarios. Our findings underscore the critical distinction between task alignment and knowledge retention, paving the way for more effective strategies in continual learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the phenomenon of "spurious forgetting" in continual learning for language models. It challenges the assumption that performance degradation across sequential tasks implies actual knowledge loss, suggesting that many performance drops arise from suboptimal task alignment. The authors propose a new method, "Freeze," which involves freezing the lower layers of a model to reduce this issue.

### Strengths
1. The paper brings a novel perspective by distinguishing between knowledge forgetting and spurious forgetting, addressing a misconception in continual learning research. This distinction enhances our understanding of model behavior across sequential tasks, highlighting the significance of this work.

2. The work is generally well-articulated and of good quality, with well-structured arguments and detailed explanations, making the complex ideas accessible to a broad audience.

3. The "Freeze" approach is simple yet effective, offering a practical solution for reducing spurious forgetting. Its ease of implementation is particularly noteworthy.

### Weaknesses
1. Freezing layers for fine-tuning has long been a common practice and is not a novel approach. For instance, freezing lower layers was explored in the VGG paper [1].  
 
2. The empirical results in this work do not provide strong evidence to support the assumptions related to orthogonality. Specifically, the angles between weight updates, as shown in Figure 4(b), are mostly below 45 degrees, which does not strongly support the claim of near-orthogonality. This undermines the theoretical justification for the proposed method.

3. The proposed method is only compared to the SEQ method in real-world scenarios, which is a pretty weak baseline.

### Questions
1. Why are Task 1 knowledge and Task 0 alignment used as the bases for plotting the loss landscapes?

2. The theoretical framework relies primarily on a linear model. Could this assumption of linearity be too strong to realistically capture the complexities of the problem? What are the limitations of using a linear model?

3. Why isn’t exact match accuracy used as the evaluation metric for all tasks?

4. From a model weight perspective, why is the angle computed based on the column spaces rather than directly from the weight updates?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper analyzes the phenomenon of catastrophic forgetting in the continual learning of language models. The authors argue that this forgetting stems from a decline in task alignment rather than a loss of knowledge. They support their claim through: (1) constructing a biography dataset to demonstrate their findings from the perspectives of performance, loss landscape, model weights, and features; (2) conducting a theoretical analysis of orthogonal updates in model weights. Then they revisit existing methods and propose a straightforward and effective freezing strategy to mitigate forgetting, which outperforms other methods.

### Strengths
1. The paper presents a novel and compelling claim regarding the phenomenon of forgetting in continual learning.
2. It adopts multiple perspectives to effectively substantiate this claim.
3. The paper provides a clear theoretical analysis based on the observation of orthogonal updates in model weights.
4. The proposed method, grounded in the theoretical analysis and observation, outperforms existing baseline methods.

### Weaknesses
The support for the assumption that the weight perturbation matrix lies in the left null space of the weight matrix in Assumption 4.4 appears to be simply based on the observations from Figure 4. However, in Figure 4, orthogonal updates occur only after the first 150 steps in the model's bottom layers. Based on performance observations, the accuracy of Task 0 has already significantly declined during these initial 150 steps. This does not support the conclusion that ``"observed performance declines are largely a result of orthogonal updates in model weights."``

I would appreciate it if the authors could address the concern or clarify if I have misunderstood any part of the paper.

### Questions
See above.

### Soundness
3

### Presentation
4

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
This paper studies the issue of forgetting during the training process of large language models (LLMs) and proposes a novel perspective on LLM forgetting. The authors categorize forgetting into two types: "decrease in task alignment capability" and "loss of knowledge." The decrease in task alignment capability is referred to as "pseudo-forgetting." When pseudo-forgetting occurs, the model’s capability can be restored with minimal data replay.
The authors also explore the pseudo-forgetting process at the model parameter level and find that, when aligning to different tasks, the orthogonal gradient directions of different tasks result in a loss of alignment with the original task when aligning with a new one. Furthermore, the authors study parameter changes across different model layers and find that the lower layers (embedding and first layer) play an essential role in task alignment. Freezing these layers can effectively alleviate the issue of pseudo-forgetting.

### Strengths
Proposes a novel perspective on catastrophic forgetting in LLM training, suggesting that LLMs do not lose knowledge but rather lose the ability to align with tasks.
Provides some theoretical support for the parameter-freezing training method through experiments.
Conducts thorough theoretical analysis. Experimental results across different methods are adequately explained, and a formalized definition of "pseudo-forgetting" is given.
The proposed method of freezing lower-layer parameters shows good performance.

### Weaknesses
1 Lack of Originality and Insufficient Literature Review:
The use of parameter freezing to mitigate forgetting in models is not a novel approach, and similar techniques have been explored previously. However, the authors do not provide an adequate discussion of prior research related to parameter freezing. This omission is significant, as a comparison with existing methods or a clear differentiation of this approach from prior studies would enhance the work's originality and position it within the context of established research.
2 Limited Evidence for Generalizability:
The experiments in the paper focus primarily on a synthetic biographical dataset, which raises questions about the broader applicability of the proposed parameter-freezing method. To demonstrate its effectiveness across diverse settings, it would be beneficial for the authors to test the method on additional, more varied datasets, including real-world datasets, and on a broader range of model architectures. Without this evidence, the method's generalizability remains uncertain.
3 Unclear Representation and Interpretation in Figures:
The figures, particularly Figure 3, are challenging to interpret, making it difficult to follow the intended findings. For instance, the paper later claims that data replay aligns the model with task 1 initially and then realigns with task 0, but this interpretation is not evident in Figure 3. The gradient descent path seems to diverge further from task 0, which contradicts the paper’s claims about realignment. Clearer visualizations or explanations of how the figures illustrate these alignment shifts are necessary for readers to understand the proposed method’s impact fully.

### Questions
1 Distinguishing Knowledge and Alignment in LLMs:
In the Introduction, the authors propose that an LLM’s task performance consists of both underlying knowledge and alignment capability. However, it’s unclear how these two aspects can be empirically distinguished. While task performance can be observed directly, what methods can effectively gauge the model’s internal knowledge versus its alignment with specific tasks? In Chapter 3, the authors describe two parameter update directions as reflecting "task 1 knowledge" and "task 0 alignment." Could the authors provide more clarity or empirical evidence to substantiate this differentiation? For instance, could ablation studies or other targeted analyses help isolate the effects of knowledge retention versus alignment?
2 Practical Value of "Pseudo-Forgetting" as a Concept:
The authors introduce "pseudo-forgetting" to describe cases where the model’s performance declines not due to actual knowledge loss, but rather due to a misalignment with the task at hand. Given that continual learning models must retain task alignment to be effective, what is the practical utility of distinguishing between true forgetting and pseudo-forgetting? Does this concept offer actionable insights for the design of more resilient continual learning strategies? If so, could the authors expand on the implications of pseudo-forgetting and how it might guide future methods for reducing task misalignment?
3 Initial Training Phase and Task Alignment Loss:
In Chapter 3, the authors extensively discuss how LLMs lose alignment with the original task in the first 150 steps of training on a new task, then progressively align with the new one. Could the authors clarify whether a warm-up phase was applied during this fine-tuning process? Alternatively, might the observed alignment shift at this stage be influenced by initial optimizer state instability, leading to greater parameter fluctuations rather than true alignment loss? Additionally, given that 150 steps might be insufficient to fully assess alignment shifts, could the authors investigate the effects of a longer initial phase or analyze optimizer state changes to clarify the nature of this alignment shift?

### Soundness
2

### Presentation
3

### Contribution
2
