# Knowledge Accumulating Contrastive Prompt for Continual Learning

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Continual learning has been challenged by the issue of catastrophic forgetting (CF). Prompt-based methods have recently emerged as a promising approach to alleviate this problem, capturing the previous knowledge by the group of prompts. However, selecting an appropriate prompt during the inference stage can be challenging, and may limit the overall performance by the misaligned prompts. 
In this paper, we propose a novel approach to prompt-based continual learning, which accumulates the knowledge in a single prompt, which has not been explored previously. Specifically, inspired by contrastive learning, we treat the input with the current and previous prompt as two different augmented views (i.e., positive pair). We then pull the features of the positive pairs in the embedding space to accumulate knowledge. Our experimental results demonstrate the state-of-the-art performance in continual learning even with a single prompt, highlighting the potential of this approach towards a `holistic' prompt for the model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The core idea of this paper is that the upper-bound prompt is the prompt optimized by the merged dataset for all tasks. To approximate the upper-bound prompt, drawing inspiration from contrastive learning, the authors treat the input along with the current and previous prompts as two different augmented views (i.e., positive pairs). Then, the authors pull the features of these positive pairs in the embedding space together to accumulate knowledge. Experimental results demonstrate the performance increase of their method in continual learning.

### Strengths
1. The writing is clear.
2. This work applies the contrastive loss in the self-supervised learning to the class-incremental learning.

### Weaknesses
1. If using the same prompt for different sessions, the prompt is essentially a set of parameters that are constantly being updated. From this pespective, the loss proposed in this paper is very similar to the regularization loss in LwF. To be more specific, the loss used in this paper requires that the current prompt and previous prompts be similar, essentially demanding that the output of the new model and the old model be similar. However, the authors do not compare their methods to any classic regularization techniques, such as knowledge distillation or other methods that directly constrain the output space.

2. The comparison in this paper is insufficient, as it does not compare their method to the CODA-Prompt [1]. Different from most existing prompt-based incremental learning methods, the authors use the same prompt for different sessions. To support the technique selection contrary to most existing methods, more comparison is essential. Furthermore, the comparison to HiDe-Prompt [2], a very recent and relevant work, is also missing, which is critical for establishing the novelty and effectiveness of the proposed approach.

3. The authors do not provide the performance of using the upper-bound prompt. It is insufficient to only prove that the prompt has been close to the upper-bound prompt. Whether is the performance of using the upper-bound prompt higher than the performance of state-of-the-art prompt-based incremental learning methods using task-specific prompts (including CODA-Prompt and HiDe-Prompt [1,2])? The absence of this comparison makes it difficult to assess the practical benefit of the proposed method.

4. This method restricts the model ability to learn new tasks, so I suspect that it may not work when there is a large gap between the pre-trained data and new-task data. It is essential to use other pre-trained models or conduct experiments on other datasets, e.g., using the model pretrained on ImageNet-1K with MoCo v3 [2,3]. For more datasets, the authors can refer to [4]. The lack of experiments across various datasets and pre-trained models limits the generalizability of the findings.

### Questions
1. Can the authors provide more evidences (e.g., analyses or experimental results) for supporting the use of the same prompt for different sessions rather than the use of task-specific prompts for different sessions?

2. The loss in this paper is essentially a regularization loss to prevent forgetting. Compared to the regularization loss in LwF, which one is better? Why is the regularization loss in this paper better? This is a very important problem.

3. Can the authors provide the comparison to CODA-Prompt? It will be better if the authors can provide the comparison between their method and HiDe-Prompt.

4. When using the upper-bound prompt, how does the model perform? 

5. How is the model performance when using different pre-trained models or different datasets?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a novel prompt-based approach to continually learn new tasks using just a single prompt. It accumulates both the previous and current task’s knowledge  in a single prompt  using contrastive learning without negative pairs, thereby removing the need for a pool of prompts and a corresponding task-id prediction mechanism  to select the prompt during inference (as in previous works).

### Strengths
1. The application of contrastive learning without negative pairs on prompt based continual learning seems novel.

2. The proposed approach helps in reduction of parameters and inference time without loss in performance.

3. Writing is clear and easy to understand.

### Weaknesses
[1]. The contrastive learning is novel but in compared to the recent work [1,5] paper does not shows the SOTA results. The recent prompting based baselines shows much better result but are missing in the paper. 

[2]. The approach in [1]  seems to outperform the proposed approach. One justification can be the the approach requires two passes through the ViT during inference: one pass with the old prompt and another with the new prompt (referred to as ensemble in the paper). However, without the ensemble also, the approach seems to perform better as can be inferred from table 3 of their paper. Similarly, look the other work [4,5].

[3]. The prompting based model is mostly expansion based approach (where prompt is the expansion parameter) where these approach leverages over the strong pretrained model. In the absence of the pretrained model how the approach behaves? There are few expansion based recent work [2,3] that does not leverages the pretraiend model can author show the result compared to these approach.

[4] In the ablation (Table-4) the author has shown the model performance and prompt parameters growth which is good. The different parameter growth vs model performance is missing. How the model will behave if the prompt parameter are increased? If the next tasks are complex we require model prompt parameter to adapt the novel task.

[5] The paper mentions that the prompt selection  mechanism in l2p and dual-prompt can introduce mis-alignment of prompts. I am a bit curious as to how much mis-alignment does each of the approaches have?

### Questions
Please refer to the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new prompt-based method to address the catastrophic forgetting issue in continual learning. Instead of learning a group of prompts to capture the previous knowledge, the key idea of the proposed method is to learn the knowledge in a single prompt. The proposed method uses contrastive learning to pull the features of two different augmented views  in the embedding space. Experimental results demonstrate SOTA performance in continual learning.

### Strengths
1. This paper is overall well-structured and easy-to-follow.

2. The proposed single prompt learning based approach is effective in performance, memory saving and time-efficient.

3. The authors have done comprehensive analyses on different continual learning benchmarks, module ablation study, etc.

### Weaknesses
1. My major concern on this paper is that the performance improvement of the proposed method over the most relevant SOTA method (i.e., DualPrompt) is mirror on all benchmarks. This make it questionable why learning a single prompt is an optimal solution than learning a pool of prompts.

2. Compared to these prompt learning-based baseline methods (e.g., L2P, DualPrompt), what is the advantage of the proposed method on learning a single prompt in continual learning is not very well justified.

3. The formulation of $L_{ctr}$ and $L_{prev}$ are very similar except that different W are used. It is unclear to me which part plays a more important role in the method. It will be great more discussions and experiments on how $\lambda_{ctr}$ and $\lambda_{prev}$ affect the model performance on different benchmark are provided to help better understand these two losses.

### Questions
See "Weaknesses".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper analyzed a critical issue of prompt-based approaches in continual learning, i.e., the errors in selecting an appropriate prompts from the prompt pool. To alleviate this issue, the authors proposed to accumulate knowledge in a single prompt through a contrastive learning strategy and transfer of top eigenvectors. Experimental results demonstrate that their method can achieve comparable performance as some representative baselines with smaller parameter cost.

### Strengths
1. This paper is well-written and easy to follow. The motivation is clear and well supported by empirical analysis.

2. The proposed method is reasonable. It’s good to seen that the capacity of a single prompt can be comparable to a prompt pool, especially in continual learning.

### Weaknesses
1. Despite the clear motivation, the proposed method only marginally outperforms the relatively earlier baseline in this direction, i.e., DualPrompt (ECCV22). There have been many more recent work based on constructing a prompt pool, e.g., CODA-Prompt (CVPR’23) and HiDe-Prompt (NeurIPS’23). I'm concerned about whether there is enough room for further development of the core insight of this paper, i.e., learning all tasks in a single prompt. Although I appreciate that the proposed method uses less parameters than L2P and DualPrompt, the improvement seems to be less significant because the prompts are light-weight. Specifically, the performance gains over DualPrompt appear to be quite small, and it's unclear if the single prompt approach can truly scale to more complex continual learning scenarios given the limitations observed with current benchmarks.

2. In addition to the results of parameter cost and inference cost, I would encourage the authors to further compare their training cost, as the use of contrastive learning usually requires more computation in training phase. The computational overhead of contrastive learning, particularly concerning the number of forward and backward passes required, needs to be quantified. It would be beneficial to compare the training time per epoch and the overall training time with other methods to fully assess the practical implications of the proposed approach.

3. I find a recent work [1] also discussed some similar issues, such as the misaligned prompts and the use of contrastive learning. While not required, I encourage the authors to make comparisons (at least conceptually) with this work.

### Questions
Please refer to the Weakness.

Besides, I would suggest the authors to consider other fine-tuning techniques, such as adapter and LoRa. They usually have better capacity than prompts to fit downstream distributions, and might make the proposed method much stronger.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
