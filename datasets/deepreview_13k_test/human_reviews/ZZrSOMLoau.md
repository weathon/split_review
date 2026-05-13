# Unraveling Cross-Modality Knowledge Conflicts in Large Vision-Language Models

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Large Vision-Language Models (LVLMs) have demonstrated impressive capabilities for capturing and reasoning over multimodal inputs.
However, these models are prone to parametric knowledge conflicts, which arise from inconsistencies of represented knowledge between their vision and language components.
In this paper, we formally define the problem of \textbf{cross-modality parametric knowledge conflict} and present a systematic approach to detect, interpret, and mitigate them.
We introduce a pipeline that identifies conflicts between visual and textual answers, showing a persistently high conflict rate across modalities in recent LVLMs regardless of the model size.
We further investigate how these conflicts interfere with the inference process and propose a contrastive metric to discern the conflicting samples from the others.
Building on these insights, we develop a novel dynamic contrastive decoding method that removes undesirable logits inferred from the less confident modality components based on answer confidence. 
For models that do not provide logits, we also introduce two prompt-based strategies to mitigate the conflicts.
Our methods achieve promising improvements in accuracy on both the ViQuAE and InfoSeek datasets.
Specifically, using LLaVA-34B, our proposed dynamic contrastive decoding improves an average accuracy of 2.24\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces the concept of knowledge conflict in vision-language models (VLMs) and designs a pipeline to detect such conflicts, tested across various VLMs. Additionally, it proposes a decoding method to mitigate the impact of these conflicts through denoising during the decoding process, thereby enhancing the performance of VLMs on visual question-answering (VQA) tasks.

### Strengths
1. The study addresses a generally prevalent and practically valuable problem and proposes a new perspective on the causes of hallucinations in vision-language models.

2. The presentation is clear and comprehensible, with intuitive and illustrative figures effectively conveying the proposed ideas.

3. The experiments are thorough and comprehensive, covering a variety of model sizes and architectures.

4. The proposed method demonstrates strong performance, resulting in significant improvements over baseline models.

### Weaknesses
1. The definition of the problem is somewhat unclear, with certain edge cases omitted, which could pose potential issues (see Question 3).

2. Some result analyses are inconsistent with the quantitative data presented in the tables (see Questions 4 and 5).

3. The motivation behind the proposed method is not sufficiently explained, particularly regarding the rationale for its design (see Questions 6 and 7).

### Questions
1. Why was an LLM (e.g., LLaMA) used instead of a VLM to generate incorrect distractor choices during dataset construction? The prompts in the appendix indicate that the LLM generates incorrect yet relevant choices. However, as LLaMA is a single-modality model without image input capabilities, it implies the model does not have access to the complete original question when synthesizing relevant choices.

2. What is the rationale behind down-sampling the InfoSeek dataset to match the size of the ViQuAE dataset? Comparisons should focus on models, not datasets.

3. Does the flip rate account for cases where both the visual and text answers are incorrect (but not equal)? For subsets entirely consisting of such cases, N_p=N×0=0 and N_f=N×1=N resulting in CR=1. This scenario is more likely attributable to a lack of knowledge or weak reasoning abilities in the LLM rather than knowledge conflicts.

4. In Table 2, why is the R.Acc lower than the Acc for the Qwen2-VL-7b model on the InfoSeek dataset? Could the authors provide a possible explanation for this observation?

5. In Section 4.3, the authors claim that the knowledge conflict rate (CR) is consistent across datasets, regardless of model scale. However, Table 2 shows that for the InfoSeek dataset, as the LLaVA model size increases, the CR decreases, with the reduction becoming more pronounced with larger models. This observation appears to contradict the authors' claim.

6. What is the meaning of the proposed contrastive metric? Section 5.2 states that the contrastive metric is designed to differentiate between consistent and conflicting answers. However, Equation 6, which calculates the metric, uses the logits of both the text and visual answers. If the logits for both approaches are already available, why not directly decode the final answers and determine conflicts by checking their equivalence?

7. In Section 5.1, the authors mention that confidence is unreliable for indicating the more reliable modality. Yet, in Section 6.1, confidence is used as a parameter to scale the logits, followed by a subtraction operation (Equation 7). Could the authors elaborate on why confidence is assumed to be reliable in this context and the significance of this subtraction?

8. The explanation of why larger models benefit more from the prompting strategy is unconvincing. The assumption that incorrect predictions stem from cross-modality knowledge conflicts contrasts with the demonstration that such conflicts exist across various model scales. If these conflicts consistently occur across modalities, what enables larger models to implicitly discern which modality's knowledge is more reliable?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the phenomenon of cross-modality parametric knowledge conflict in vision language models. Specifically, when a VLM provides different answers with and and without the vision modality (with effective textual substitute for visual input), those instances are considered as cross-modality knowledge conflicts. To study this scenario, the authors construct a multiple-choice question answering dataset from two datasets: ViQUAE and InfoSeek where the questions are based on named entities presented in the accompanying image. They first extract answers based on both image and text input (visual accuracy), and then extract answers from the VLM with textual input only (textual accuracy). Their exploration shows that there can be large gaps between the textual accuracy and visual accuracy of contemporary VLMs. The accuracy on the subset of data where the VLM succeeds at recognizing the named entity is used for further evaluations. The QA accuracy gap on this subset can be attributed to knowledge conflicts and performance gaps, according to the authors. Performance gaps refer to the inability of the model to connect the visual encodings to the underlying parametric knowledge in LLMs in order to answer the question correctly. The conflict rate is calculated as the difference between flip rate (cross-modality inconsistency) and performance gap (calculated as diff. Of textual and visual acc. On the subset). Further exploration shows that confidence measured using logits is not a good indicator of instances with parametric knowledge conflict. However, a contrastive interpretation of the logits serves as a good indicator of instances where the modalities lead to knowledge conflict. Further, this paper proposes a dynamic contrastive decoding method and prompting method to mitigate cross-modality knowledge conflicts and shows significant improvements in QA accuracy for VLMs.

### Strengths
**Well-written paper**: This paper is well-written with a clear motivation for exploration on this topic, well-structured sections and flow of contents. Experimental results are conveyed clearly and hypothesis are discussed extensively in the main text.


**Important Topic**: Topics related to parametric knowledge are always an important research topics, with those pertaining to VLMs becoming even more important as VLMs become mainstream in day-to-day use.

### Weaknesses
**Soundness of the cross-modality parametric knowledge conflict explanation**: 

The authors outline an explanation of the cross-modality knowledge conflict in Sec. 4.2. Following the provided explanations, these are the four categories of samples present in the evaluation set of recognized accuracy (also represented in Fig. 2):

1. Correct Text, Correct Visual
2. Correct Text, Incorrect Visual
3. Incorrect Text, Correct Visual
4. Incorrect Text, Incorrect Visual

According to the provided definitions in 4.1,

Flip Rate = size(2) + size(3)

$\Delta$Acc. = size(1) + size(2) - size(1) - size(3) = size(2) - size(3)

So, conflict rate = Flip Rate - $\Delta$Acc. = size(3) * 2

Please correct me if my understanding seems wrong. This seems like an inadequate measure for the cross-modality conflict since it only captures the size of category 3. Specifically, I think that the samples that are being attributed to performance gap (primarily category 2) should also be counted towards conflict since at least a part of this category implies that the visual-language knowledge is at odds with the language-only knowledge.

**Dynamic Decoding Method**: While this method does achieve significant improvements, this method lacks practical use because it requires that the user knows the named entity being shown via image to the VLM. If the user already has this information, then it would make more sense to simply pose this question to a capable LLM.

**Limited Generalizability of Results**: The results presented in this paper are specific to MCQ questions only. The MCQ format does make it easy to study this phenomena, however, it may not generalize to open-domain natural language answers which are the dominant format of interaction with current LLMs and VLMs.

### Questions
- The main motivation of this paper is to study conflicts between the LLM knowledge and VLM knowledge about the same topic. However, I am not completely convinced by the term 'conflict' for this scenario because the visual modality merely adds new knowledge to the LLM. Any conflict that arises from this addition can be solely because the training process could not bridge the gap between visual modality and language modality correctly, which has been termed as performance gap in this paper. What other reasons could there possibly be for this conflict, which is being captured in the Conflict rate? I would appreciate more discussion on this point in the rebuttal. Apologies if I have missed the point of this paper.

- How exactly is $\Delta$ accuracy calculate? Is it calculated based on the accuracies on the complete evaluation set? If yes, it might change my interpretation of the Conflict Rate outlined under Weaknesses.

- Suggestion to also report $\Delta$ accuracy in the table for easier interpretation of the results.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the issue of parametric knowledge conflicts within LVLMs. It defines this cross-modality conflict problem and develop a systematic pipeline to detect, interpret, and mitigate such conflicts, revealing a consistently high conflict rate across modelse. They introduce a contrastive metric to differentiate conflicting samples and propose a dynamic contrastive decoding method that selectively removes low-confidence logits, which improves model accuracy.

### Strengths
- The paper introduces and formally defines a critical, underexplored issue in LVLMs, cross-modality parametric knowledge conflict, and its implications for model inference.
- A well-structured pipeline for conflict detection, interpretation, and mitigation provides a comprehensive framework for handling multimodal inconsistencies.

### Weaknesses
This work is compelling, as multimodal knowledge plays a vital role in advancing LVLMs. However, a fundamental challenge remains: for LVLMs, the core focus is still the generation task. The approach in this article appears limited to classification and token generation, focusing mainly on calibrating output probability. Addressing this challenge more directly is crucial for the current stage of LVLM development.

In particular, you may need to consider Image Caption or CoT Reasoning tasks, like Coco, ScienceQA, M3CoT.

### Questions
- Adding discussion of knowledge conflicts on how to multimodally generate tasks will be much helphul for the community.

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
4

### Summary
This paper addresses the issue of cross-modality parametric knowledge conflicts in Large Vision-Language Models (LVLMs). The authors identify that inconsistencies between the visual encoder and the language model components can lead to contradictory outputs when processing the same entity presented in different modalities. They propose a pipeline for detecting these conflicts, introduce a contrastive metric to interpret their impact on inference, and suggest mitigation strategies like dynamic contrastive decoding.

### Strengths
The paper raises and formally defines the phenomenon of cross-modality parametric knowledge conflicts in LVLMs.

The authors not only detect and quantify the conflicts but also delve into their interpretation and propose practical mitigation strategies.

The introduction of a dynamic contrastive decoding method shows promise in effectively reducing knowledge conflicts during inference without the need for additional training, which is resource-efficient.

The paper provides experimental results demonstrating the persistence of knowledge conflicts across various model scales and architectures, highlighting the significance of the problem.

### Weaknesses
The study evaluates the proposed methods on only two knowledge-intensive datasets. This narrow scope raises concerns about the generalizability of the findings across different domains and types of data. The paper should consider adding other evaluations like MMBench, Vibe Eval, and Mistral evals to justify that the method can generalize well.

The introduction and explanation of the contrastive metric could be more detailed. Additional clarification on how it effectively distinguishes conflicting samples would strengthen the paper.

While the paper proposes using a decoding method to solve the problem, more analysis should be given to study whether the problem comes from model training or inference. While a decoding based is lightweight, I wonder whether improving LVLM training can solve the problem too.

### Questions
See the weaknesses above.

(1) Can the authors provide more evaluations beyond knowledge intensive tasks?

(2) More justification about why choosing this decoding method?

(3) Is the problem solvable with improving LVLM training?

### Soundness
3

### Presentation
3

### Contribution
2
