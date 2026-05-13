# REMEDY: Recipe Merging Dynamics in Large Vision-Language Models

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Model merging has emerged as a powerful technique for combining task-specific vision models into a unified and multi-functional model. Previous methods represented by task arithmetic, have demonstrated effectiveness and scalability in this domain. When large vision-language models (LVLMs) arise with model size scaling up, this design becomes challenging to fuse different instruction-tuned LVLMs for generalization enhancement. The large scale and multi-modal nature of LVLMs present unique obstacles, including constructing reusable and modular components to accommodate the multi-component architecture of LVLMs and the requirement for dynamic fusion based on multi-modal input tokens. To address these challenges, we propose the \textbf{RE}cipe \textbf{ME}rging \textbf{DY}namics (REMEDY) method, a scalable and flexible paradigm for model merging in LVLMs. We first define reusable modules termed \textit{recipes} including the projector and shallow LLM layers, enhancing visual-language understanding. Then, we introduce a modality-aware allocator dynamically generates weights in a one-shot manner based on input relevance to existing recipes, enabling efficient cross-modal knowledge integration. REMEDY thus offers an adaptive solution for LVLMs to tackle both seen (i.e., multi-task learning) and unseen (i.e., zero-shot generalization) tasks. Experimental results demonstrate that our method consistently improves performance on both seen and unseen tasks, underscoring the effectiveness of REMEDY in diverse multi-modal scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces REMEDY (Recipe Merging Dynamics), a model merging framework tailored for large vision-language models (LVLMs). REMEDY leverages modular "recipes" and a dynamic, modality-aware allocator for effective cross-modal knowledge integration, enhancing multi-task learning and zero-shot generalization across diverse vision-language tasks.

### Strengths
1. The paper presents a unique "recipe" construction framework, creating modular, reusable components that facilitate task-specific adaptation and multi-task learning within large vision-language models.

2.  Extensive experiments on multiple datasets demonstrate REMEDY’s efficacy, highlighting superior performance over baseline methods on multi-task and zero-shot generalization. 

3. The study provides a thorough analysis of task similarity and allocation strategies, offering insights into how specific recipes contribute to various tasks.

### Weaknesses
1.  The process of constructing recipes heavily relies on experimental insights, such as which layers and modules to fine-tune. This empirical approach may limit REMEDY's scalability and adaptability to new tasks or models without extensive trial-and-error adjustments.

2.  Although REMEDY introduces modularity, the recipe construction phase lacks dynamic or automated selection mechanisms to identify optimal modules or layers. 

3. The paper does not extensively discuss the computational demands of the proposed approach, especially in the context of training and inference with the modality-aware allocator.

### Questions
As shown in weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes REMEDY, a new technique for merging large vision-language models (LVLMs). It addresses the challenges of scale and multi-modal input by creating reusable fine-tuned modules called "recipes" and dynamically combining them using a "modality-aware allocator." This allocator analyses the input image and text to generate weights for each recipe, enabling adaptive fusion and improved performance on both seen and unseen vision-language tasks.

### Strengths
1. The analysis of finetuning strategies is interesting. The paper shows that fine-tuning the projector and shallow layers of the LLM leads to better improvements.
2. The motivation that uses the most relevant experts to better answer user questions is reasonable.

### Weaknesses
1. There is a typo in line 054: the vision encoder should be 0.3B.
2. There are some redundant definitions in this paper and the "recipes" are actually MoE-based LoRA layers. The use of global and module-wise routing is not novel.
3. The experiments include only 4 seen tasks and evaluation benchmarks. And I suspect that the proposed method can generalize well. It is expected that REMEDY surpasses the zero-shot setting on seen tasks since it is trained on these datasets. My main concern is the improvement on unseen tasks, which appears weak overall.
4. TextCaps and TextVQA use the same images, so TextCaps is not an unseen task if TextVQA is already seen.
5. The baseline is somewhat weak. There are stronger open-source baselines available, such as LLaVA-NeXT and LLaVA-OneVision.

### Questions
Please see the weaknesses.

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
This paper introduces REMEDY, a model merging technique for LVLMs that addresses the challenges of combining knowledge across multi-modal tasks. REMEDY explores components of LVLMs and propose recipes for learn specific tasks. It further propose a dynamic allocator that learns weights for different recipes. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The method propose a new approach for model merging for LVLMs, which is effective for enhancing the multi-task learning capabilities of LVLMs.
2. The paper is well-writing and the experiments are comprehensive.

### Weaknesses
1. The work trains the model in few-shot way, e.g., on seen tasks and expected to generalize to unseen tasks. But current MLLMs are expected to have strong zero-shot capabilities. And from the comparison results of Table 2, REMEDY seems not have explicit performance improvement compared to the zero-shot way or simple average way. Considering the complexity it adds on the training and inference stage, it may limit the practical use case of it.
2. Does the model needs to compute the weights for different recipes and then update the model weights for each inference time. If so, how about the extra inference time introduced and the comparison with the baseline?

### Questions
How about the performance of REMEDY compared to LLaVA fine-tuned on the seen tasks?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a straightforward approach to addressing the multi-task learning challenge in Large Vision-Language Models (LVLMs) using model merging techniques. Given the large parameter scale of LVLMs, the authors first select layers to merge, referred to as 'recipes,' based on preliminary experiments. These layers include the projection layer and the shallow layers of the LVLM. An attention-based module is then trained to dynamically assign merging weights to the 'recipes' based on the input multi-modal token, allowing for adaptive weighting to handle the complexity of VL tasks. The proposed method demonstrates improvements on both learned tasks and zero-shot generalization across multiple datasets.

### Strengths
- **Clarity**: The paper is well-structured and easy to follow.
- **Motivation**: As the size of the visual language model continues to grow, it becomes costly to maintain a separate model for each specific task. It makes sense to combine task-specific models into a unified model through model merging that can simultaneously solve different downstream tasks.
- **Novelty**: This paper designs a merging strategy that takes into account the characteristics of multimodal tasks and the difference in fine-tuning paradigms between LVLM and traditional models. Meanwhile, this paper also analyzes the influence of each component in LVLM on fine-tuning performance, which is suggestive for the follow-up works.
- **Results**: The experimental results across multiple datasets effectively highlight the potential and robustness of the method.

### Weaknesses
- **Detail in Weight Generation**: The paper does not explain how the proposed attention-based module is trained to generate the merging weights. Neither the main text nor the supplementary materials provide insights into the optimization objective used. While the authors may consider this aspect elementary, I believe a detailed explanation is necessary.
- **Analysis of Computational Overhead**: The work in this paper is carefully designed when selecting an extended module, which may reduce the cost of calculating overhead and model parameters. However, the experiment lacks analysis of the training and inference overheads.
- **Details Error**: The introduction states that the new challenges facing the LVLM merger will be analyzed from three aspects, but only two aspects are introduced below.

### Questions
I have some additional concerns:

- **Evaluation Metric**: What does the Hscore metric indicate? Is the average accuracy calculated as a direct average of the accuracies on the different datasets or is it weighted by the number of samples in the dataset?

- **Score Visualization Analysis**: In Figure 4, the weight distribution across different layers shows considerable variation, with some layers dominated by distinct 'recipes.' This phenomenon is intriguing, and I would appreciate further explanation from the authors. For VizWiz, an unseen dataset with the same VQA task, why does the "Recipe" of TextVQA have a smaller layer-wise score?

Finally, the proposed Modality-aware Allocator is designed for multimodal tasks, which is one of the advantages over previous research on visual models. Therefore, I am curious whether using only visual or textual input as clues for allocation will result in a performance degradation?

### Soundness
4

### Presentation
3

### Contribution
3
