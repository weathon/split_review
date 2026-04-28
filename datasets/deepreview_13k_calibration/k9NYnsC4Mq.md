# Learning without Forgetting for Vision-Language Models

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Class-Incremental Learning (CIL) or continual learning is a desired capability in the real world, which requires a learning system to adapt to new tasks without forgetting former ones. While traditional CIL methods focus on {\em visual} information to grasp core features, recent advances in Vision-Language Models (VLM) have shown promising capabilities in learning generalizable representations with the aid of {\em textual} information. However, when continually trained with new classes, VLMs often suffer from catastrophic forgetting of former knowledge. Applying VLMs to CIL poses two major challenges: \textbf{1)} how to adapt the model without forgetting; and \textbf{2)} how to make full use of the multi-modal information. To this end, we propose PROjectiOn Fusion (\textbf{\textsc{Proof}}) that enables VLMs to learn without forgetting. To handle the first challenge, we propose training task-specific projections based on the frozen image/text encoders. When facing new tasks, new projections are expanded and former projections are fixed, alleviating the forgetting of old concepts. For the second challenge, we propose the fusion module to better utilize the cross-modality information. By jointly adjusting visual and textual features, the model can capture semantic information with a stronger representation ability.  Extensive experiments on nine benchmark datasets validate \mame\ achieves state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a class-incremental learning (CIL) method based on vision-language models. Specifically, this paper mainly focuses on two key challenges to CIL, named how to adapt the model without forgetting and how to make full use of the multi-modal information. To deal with the first challenge, a task-specific projections are proposed based on the frozen image/text encoders. To deal with the second challenge, a fusion module is proposed for better exploit the cross-modality information. Experiments have shown the state-of-the-art performance of the proposed method.

### Strengths
- In general, the proposed method is well motivated and clearly presented.
- The paper turns a VLM into a continual learner that is both retentive and comprehensive.
- Good performance is achieved.

### Weaknesses
 - The effectiveness of alleviating forgetting is uncertain. The process involves incrementally learning image projection heads and text projection heads, which are then combined for various tasks. When new tasks are learned, the projections of previous tasks are fixed and not updated. However, during inference, the projections of all tasks are merged, which might not be ideal for test data from older tasks due to potential side effects caused by the projections from the new tasks. Specifically, the fixed projections of older tasks, when combined with new task projections during inference, could lead to feature drift, where the representation of older classes is distorted by the influence of the new task's projection. This could manifest as decreased accuracy on older tasks, even if the model performs well on the new task.
- The extent to which contextual information is effective has not been extensively studied. The projection fusion method proposes to contextualize and merge embeddings and contextual information using self-attention. However, in the experiments, only the results of Projection & Fusion are compared with Projection & Fusion & Context Prompt, without explicitly evaluating the effectiveness of the concatenated context information in Q, K, V as [P_i(z), Context] in self-attention, or the effectiveness of the context prompt. In other words, the final context information is defined as Context = [P, W, C], but the specific contributions of W and C to the final results need further analysis. It's unclear whether the performance gain is due to the prototypes (P and W), the context prompt (C), or the interaction between them. For example, the self-attention mechanism might be primarily leveraging the prototypes, with the context prompt providing only a marginal benefit, or vice-versa. A more granular analysis is needed to isolate the impact of each component.
- The evaluation metric used may not provide a comprehensive measure of the extent of forgetting. The reported accuracy might not fully capture the nuances of catastrophic forgetting, especially if the model's performance on older tasks degrades significantly while maintaining high average accuracy due to good performance on newer tasks. A more detailed analysis of per-task accuracy would be beneficial.

### Questions
- To what extent the proposed method could alleviate forgetting?
- How does each component of the contextual information contribute to the final results?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Prior works only focus on the visual branch of CLIP for incremental learning. This paper argues both modalities are important.
- PROOF freezes the image and text encoders of the pre-trained VLM (e.g. CLIP). These contain the generalizable representations learned during pre-training.
- For each new incremental task, it adds new projection layers (P_i, P_t) on top of the frozen encoders. These projections are task-specific.
- When a new task arrives, only the parameters of the projections for the new task are trained. The old projections remain frozen.
- Cross-modal attention fusion is used to adjust the query embedding using context like prototypes and prompts. This allows utilizing both visual and textual information to obtain comprehensive embeddings.
- At inference time, the projections are aggregated to obtain a unified classification. But the old projections remain unchanged.

### Strengths
Technically a novel idea to incorporate both the visual and the text encoders. 
Improves upon SOTA.

### Weaknesses
 - Inference Mismatch - Projections are combined at inference time which may not fully match the training conditions for a specific task projection. Specifically, during training, each task's projection is optimized independently, focusing on the current task's data and a small set of exemplars. However, at inference, these task-specific projections are aggregated, potentially leading to a mismatch where the combined representation does not accurately reflect the individual task-specific feature spaces. This aggregation could result in suboptimal performance, particularly when the feature spaces of different tasks are not well-aligned.

- Representation Drift - The post-attention module representations learned by the frozen projections may drift or shift slightly during new task training due to weight updates elsewhere. While the projection layers are frozen, the cross-modal attention module is still being trained. This training could indirectly influence the representations learned by the frozen projections, causing them to drift from their original task-specific feature space. These small drifts, even if seemingly minor, can accumulate over multiple tasks, leading to a degradation in performance for earlier tasks. The issue is that the attention module is not completely isolated from the frozen projections, and its training can subtly alter the feature space they operate in.

- Section 3 is really long and has a lot of redundant information, it should be made much shorter. That space should be given to increase the length of section 4 to give a better understanding of the fusion module.

### Questions
- Any comments on the issues pointed out in the weaknesses will be appreciated.

- Also please make it more clear how you are using attention.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes one of the first mechanism to do continual learning with Vision-Language Models (VLM) such as CLIP. Through a system of projectors and a revised definition of context, the authors tested their model, PROOF, on a variety of datasets for continual learning obtaining state-of-the-art performances.

### Strengths
- The authors tested for the first time a VLM model for continual learning. 
- The authors tested their PROOF on a variety of datasets testing the effectiveness of the model.
- The authors proved the effectiveness of the model with very interesting and detailed ablation studies.

### Weaknesses
 - The paper lacks motivation and innovation: The authors suggest using CLIP for class-incremental continual learning, but it would be more interesting to see its performance on tasks like incremental captioning or retrieval. Unlike L2P, where a large pretrained model was used, CIL could have been just one application.
- Furthermore, the PROOF mechanism, while innovative, lacks depth. Projection networks are common in continual learning, and the new context definition isn't explored. The projection networks, while a valid approach, are not substantially different from existing methods. The paper does not explore the specific properties of these projection layers or their impact on the learned representations.
- The main paper lacks standard deviation in results and doesn't consider multiple runs with different class orders. 
- There's no analysis of time and memory usage, except for a basic mention of memory requirements in supplementary materials. 
- The paper's narration could also be improved

### Questions
- It looks like the supplementary materials are more informative and present more interesting results w.r.t. the main paper. Why did the authors exclude them from the main paper?
- The definition of W is not reported in the paper. How W is defined in the context?
- Can the authors provide an analysis of the accuracies of the model varying the number of exemplars?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
