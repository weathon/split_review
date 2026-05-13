# Mitigating Catastrophic Forgetting in Large Language Models with Forgetting-aware Pruning

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
Recent advancements in Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks. These models are typically pretrained on extensive corpora and subsequently fine-tuned on task-specific datasets. However, during the fine-tuning process, LLMs often suffer from Catastrophic Forgetting (CF), wherein previously acquired general knowledge is lost. Traditional approaches to mitigating CF often rely on data replay, which may not be viable when the original training data is inaccessible. Additionally, methods that alter the training process or the model architecture can increase complexity and detract from the accuracy of downstream tasks, thus limiting their generalizability. In this paper, we propose Forgetting-Aware Pruning Metric (FAPM), a novel pruning-based approach to balance CF and downstream task performance. Our investigation reveals that the degree to which task vectors (i.e., the subtraction of pre-trained weights from the weights fine-tuned on downstream tasks) overlap with pre-trained model parameters is a critical factor for CF. Motivated by this insight, FAPM employs the ratio of the task vector to pre-trained model parameters as a metric to quantify CF, integrating this measure into the pruning criteria. Importantly, FAPM does not necessitate modifications to the training process or model architecture, nor does it require any auxiliary data. We conducted extensive experiments across six datasets encompassing natural language inference, question answering, reading comprehension, and cloze tests. The results demonstrate that FAPM limits CF to just 1% while maintaining 99% accuracy on downstream tasks, rendering FAPM highly competitive relative to the state-of-the-art methods that involve modifications to the training process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tries to tackle the problem of whether catastrophic forgetting (CF) due to finetuning be avoided without changing training process, without any additional data, and without altering model structure. To this end the authors come up with Forgetting-Aware Pruning Metric (FAPM) wherein the task vectors are not only pruned based on magnitude but also uses the ratio of task vector to pretrained parameters to avoid CF. The authors provide extensive experiments across various tasks and latest LLMs like Qwen and Llama3 models.

### Strengths
1. The simplicity of the technique introduced by the authors is really great. Also I loved reading section 3.1 wherein they provide analysis and a clear thinking process of how they arrived at the method.

2. There are extensive experiments in the paper across various tasks and two models. The models chose are the latest ones which makes this paper a bit more relevant. Section 5 in general is pretty enjoyable to read.

3. Although the method is not pareto optimal but the numbers are consistently high on all the tasks across both Llama3 and Qwen2.

### Weaknesses
 1. A small nitpick. It would be really great if the captions of the images and tables could be a bit longer and more informative.

 2. Nowadays most people prefer to use LoRA not because it reduces CF, but instead its pretty cheap. In my experience even LoRA suffers from CF if the finetuning domain is pretty niche. So I was wondering how informative are task vectors from LoRA merged models and how will this method perform if we use LoRA to finetune.

### Questions
1. Nowadays most people prefer to use LoRA not because it reduces CF, but instead its pretty cheap. In my experience even LoRA suffers from CF if the finetuning domain is pretty niche. So I was wondering how informative are task vectors from LoRA merged models and how will this method perform if we use LoRA to finetune.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors introduce Forgetting-Aware Pruning Metric (FAPM), a new pruning-based method aimed at striking a balance between reducing forgetting and maintaining downstream task performance. They find that the overlap between task vectors – which represent the difference between pre-trained weights and those fine-tuned on new tasks – and pre-trained model parameters is a major factor in forgetting. FAPM uses this overlap ratio as a metric for assessing forgetting and incorporates it into pruning decisions. A key advantage is that FAPM doesn't require changes to the training process or the model architecture, nor does it need any additional data. The authors conducted experiments across six datasets covering various tasks, and the results show that FAPM keeps forgetting to just 1% while achieving 99% accuracy on downstream tasks, making it very competitive against other state-of-the-art methods.

### Strengths
1. FAPM effectively limits forgetting to a mere 1%, which is a significant improvement.
2. The method maintains an impressive 99% accuracy in downstream tasks, showing that it preserves performance.
3. Unlike some existing methods, FAPM doesn’t complicate the model architecture or training process, making it easier to implement.
4. This approach doesn’t rely on replaying original training data or using additional datasets, making it more practical in various scenarios.

### Weaknesses
1. The reliance on the overlap between task vectors and pre-trained weights might not generalize across all types of tasks or models. Specifically, the metric's effectiveness could be highly dependent on the nature of the task vectors, which may vary significantly in different domains. For instance, tasks with highly non-linear decision boundaries might produce task vectors that do not align well with the pre-trained weights, leading to suboptimal pruning decisions.
2. While pruning is effective, it may not address all aspects of learning or forgetting, so there could be other methods worth exploring along with FAPM. For example, methods that focus on modifying the learning rate or using regularization techniques could complement FAPM by addressing different facets of the forgetting problem. The paper does not explore how FAPM interacts with these other methods, limiting its potential scope.
3. While the experiments are comprehensive, testing on even more diverse datasets could strengthen the generalizability of the findings. The current datasets, while varied, might not fully capture the range of challenges presented by real-world applications. For instance, datasets with significant noise or those requiring complex reasoning might reveal limitations in the FAPM approach.
4. The paper doesn’t discuss how FAPM performs in highly specialized or unusual task scenarios, which might reveal limitations. For example, tasks that require very specific knowledge or those that involve adversarial examples could expose vulnerabilities in the pruning strategy. It is unclear how FAPM would handle such scenarios, and this lack of analysis is a weakness.

### Questions
1. This appears to be a unique model merging method; however, why is there no comparison made with other methods of a similar nature?
2. While you have elucidated how to control FAPM to achieve a better balance between accuracy and forgetting levels, is there a more effective approach to directly estimate an optimal balance point rather than adjusting parameters through multiple rounds of performance feedback?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors identified pruning as a way to mitigate catastrophic forgetting. Specifically, the authors propose to prune weight updates due to fine-tuning, using a combination of pruning metrics including absolute magnitude of change in weights and relative magnitude of change in weights relative to the magnitude of pre-trained weights.

### Strengths
- Using pruning to mitigate catastrophic forgetting during fine-tuning is novel.
- This paper contains some original insights about the generality/specificity trade-off when fine-tuning LLMs.

### Weaknesses
 - This paper proposes a complicated pruning metrics that only shows marginal improvement over prior art.
- The quality of write-up is generally poor. For example, section 3.1 is entirely unnecessary and can be in the appendix without affecting the flow of the paper.
-  No ablation study. Why not use the relative portion of the pruning metric alone? It’s a complicated scoring metric, please ablate it.

### Questions
- See weakness.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on addressing the issue of catastrophic forgetting (CF) in large language models (LLMs) during fine-tuning, i.e., striking a balance between speciality and generality.
It proposes Forgetting-Aware Pruning Metric (FAPM): A novel method that integrates the ratio of task vector magnitude to pre-trained model parameters into the pruning criteria, allowing for the mitigation of CF without modifying the model architecture or training process.
FAPM successfully mitigates forgetting while retaining 99% of downstream task accuracy across various natural language tasks.
The experiments show that FAPM performs competitively against state-of-the-art methods.

### Strengths
1.This paper introduces two key concepts through preliminary experiments—“absolute change magnitude” and “relative change magnitude”—which are designed to balance the trade-off between task specialization and generality.

2.Building on these concepts, the paper proposes the Forgetting-Aware Pruning Metric (FAPM), aimed at deriving an optimal task vector to obtain the final model weights.

3.Extensive experiments demonstrate the effectiveness of FAPM, showing significant improvements over baseline methods.

### Weaknesses
1.This paper overlooks an important baseline—Wise-FT [1], a standard model parameter merging method.

2.The experimental setup for the preliminary experiments, particularly those in Sections 2 and 3, is not clearly detailed, e.g., the experimental model, raising concerns about whether similar observations would hold for other models.

3.While instruction-following is a critical aspect of generality, this paper focuses solely on world knowledge and generic reasoning, omitting this aspect.

4.The rationale and motivation for striking a balance between speciality and generality is not clearly articulated in the paper.

5.The limitation mentioned in lines 81-83, stating that "methods that alter the training process or model architecture not only make the training process more difficult to control but also degrade the accuracy of downstream tasks," lacks references to prior work supporting this claim.

6.The figures in this paper appear not to be in vector graphic format, which may affect the clarity and quality of the visualizations.

7.The quotation marks in line 212 are not properly formatted according to standard usage.

### Questions
1.The limitation mentioned in lines 81-83, stating that "methods that alter the training process or model architecture not only make the training process more difficult to control but also degrade the accuracy of downstream tasks," lacks references to prior work supporting this claim.

2.The figures in this paper appear not to be in vector graphic format, which may affect the clarity and quality of the visualizations.

3.The quotation marks in line 212 are not properly formatted according to standard usage.

### Soundness
4

### Presentation
3

### Contribution
3
