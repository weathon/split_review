# I-Lora: Iterative Merging of Routing-Tuned Low-Rank Adapters for Multi-task Learning

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
The advancement of vision-language models has significantly boosted the performance of embodied and game AI, endowing them with more robust general visual understanding capabilities and logical abilities for action planning. However, the substantial computational cost of model training and the performance degradation during fine-tuning limit the models' ability to learn emerging new tasks continually. Creating a versatile and dynamically updatable vision-language model is an essential area of research. To this end, we propose a Low-Rank Adapter-based fine-tuning approach called I-LoRA, which enables iterative and independent learning of new tasks while preserving the logical capabilities of the previously trained model. Specifically, we first design the routing-tuning method to minimize the impact of original capabilities from the new task by minimizing activation values of LoRA matrices as low as possible in the general task. Secondly, we propose a novel approach to iteratively merge new adapters, allowing for continuous integration of adapters trained on new tasks without being influenced by task order, thereby reducing interference between them. Finally, we conducted extensive experiments on public datasets with significant behavioral and logical differences between tasks. The results demonstrate that our approach achieves excellent single-task performance, strong multi-task compatibility, and flexible scalability without increasing the number of model parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an iterative LoRA merging method for multi-task learning. The authors employ Singular Value Decomposition (SVD) to reduce the number of redundant parameters and keep the components with the most significant influence to ensure task performance. The authors conduct experiments on Atari game and show that the proposed method outperforms state-of-the-art RL methods.

### Strengths
- The idea of iterative mering LoRA adapters is interesting.
- The proposed method achieves competitive results.

### Weaknesses
 - The task formulation is not clear. According to the description in L67 'this paper focuses on enabling the model to learn new tasks while maintaining performance on other tasks.', the task is more likely to be continual learning/lifelong learning, rather than multi-task learning. However, in L158 the problem definition seems to be more like multi-task learning. The former focuses on learning a series of tasks and keeping the old task performance, i.e. alleviating catastrophic forgetting. Usually the old tasks are not accessible when learning new tasks. In contrast, the latter focuses on learning multiple tasks simultaneously. The authors should further clarify the problem definition in Section 3.1. 
- The assumption of the proposed constraint is not convincing. The authors propose to constrain the LoRA's activation to zero when dealing with general or other tasks. What if the new task is beneficial for the general ability of the VLM? For instance, there are several studies investigating the forward transfer [1] in lifelong learning, and the task conflict in multi-task learning [3]. Therefore, the assumption behind is somewhat not convincing.
- The experimental setting is not convincing enough. Is there any specific reason to choose Atari Game? It seems that there is no public or widely-used Atari benchmark for VLM-based agent. Why not choose Minecraft, meta-world to verify the effectiveness of the proposed method? At least, there are lifelong learning agent baseline for Minecraft (VOYAGER) and multi-task RL baselines for meta-world [4,5].
- The experiment part is limited to VLA task, i.e. Atari Game. Does the proposed I-LoRA also apply to other general LLM/VLM Multi-task/Continual learning? It seems that the I-LoRA is not specifically designed for Game. 
- Minor points:
    - More details of the general dataset should be provided.
    - The authors could adopt a more intuitive metric for Table 1, such as average ranking, or normalized average score.
    - The performance drop could be provided for clearer comparison in Table 3.
    - Baselines are mostly RL methods. The authors should compare with more baselines and variations, including vanilla VLM, PEFT-based methods, LoRA-merging methods and their variants.

### Questions
- How is the ratio of kept singular value determined?
- What is the input of the VLM? The authors mentioned text input, how about the visual input? 
- How are the game rules described? 
- How is the COT conducted? 
- How to make action to interact with the Atari environment from the VLM's output?

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
This paper presents I-LoRA, a fine-tuning approach for vision-language models designed to overcome performance degradation associated with adapting models to new tasks. The authors highlight limitations in current vision-language models, which, despite improving visual and logical task capabilities, face challenges in continual learning due to high computational costs and reduced performance during fine-tuning.

I-LoRA addresses these issues by introducing:

1. A **Routing-Tuning** method that minimizes interference with the model's original capabilities when learning new tasks, keeping the activation of Low-Rank Adapter (LoRA) matrices low.
2. A **Merging Mechanism** for adapters, which supports continuous learning by allowing new tasks to be added without performance loss from task order interference.

Experiments on diverse datasets reportedly validate I-LoRA’s advantages, achieving strong single-task performance, effective multi-task compatibility, and scalability without parameter increases.

### Strengths
Empirical results show a considerable improvement in different games when compared to the selected baselines in Tables 1 and 3.

### Weaknesses
 **Method**

- Routing: I am unsure about the novelty of maintaining the information learned from the vanilla VLM using a *data-driven* approach. It uses data similar to that used to train the based model. It requires training the LoRA with the target and the previous datasets to teach when intervening with the weights of the base model, which doesn't look ideal and is not generalizable since, for many VLM, we don't necessarily have access to the datasets that have been trained.

---
 
**Experiment**

- No ablation of the losses that are proposed? What are the $\epsilon_1$, $\epsilon_2$, and $\epsilon_3$, and what values do they take?


---

**Literature review**

A couple of papers on model merging are missing from the literature review, especially in L57-59 and L64-L66.

- [1] Yang, E., Wang, Z., Shen, L., Liu, S., Guo, G., Wang, X., & Tao, D. Adamerging: Adaptive model merging for multi-task learning, ICLR 2024

- [2] Zhang, F. Z., Albert, P., Rodriguez-Opazo, C., Hengel, A. V. D., & Abbasnejad, E.. Knowledge composition using task vectors with learned anisotropic scaling. NeurIPS 2024

- [3] Yang, E., Shen, L., Guo, G., Wang, X., Cao, X., Zhang, J., & Tao, D. (2024). Model merging in llms, mllms, and beyond: Methods, theories, applications and opportunities. arXiv preprint arXiv:2408.07666.

- [4] Ilharco, G., Ribeiro, M. T., Wortsman, M., Gururangan, S., Schmidt, L., Hajishirzi, H., & Farhadi, A. Editing models with task arithmetic. ICLR 2023

Also, concerning Adapters
.
- [5] Zhang, Q., Chen, M., Bukharin, A., He, P., Cheng, Y., Chen, W., & Zhao, T. Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning. ICLR 2023

---

**Presentation**
- Figures and Tables have very poor captions.
- Typo: Llava L161, L347 and L430
- Table 1: you could add some colours to rows and distinguish when the method is better than human or SOTA.

### Questions
1. Equation 4. Is this making the activations approach zero? Do you have any visualization of it? Visualising the activations for a target and base datasets test set would be ideal.
2. L431. Why do you decide to use 30,000 samples from the general data? How do you sample the dataset?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the challenge of multi-task learning in vision-language models, specifically tailored for mastering multiple Atari games and general VQA tasks. It begins by gathering Atari data for training the vision-language model. Next, it introduces a method named Routing Tuning, which develops distinct LoRA adapters for various tasks. Finally, it presents an iterative maximum merging technique to consolidate these different LoRA adapters into a single one.

### Strengths
- Multi-task learning in vision-language models is a significant and intriguing area of study.

- The method is straightforward and easy to understand.

- Experiments demonstrate that multi-task learning using the proposed approach achieves performance comparable to single-task models, while maintaining a reasonable level of general vision-language understanding.

### Weaknesses
 - In the experiments, is there an explanation for why the performance of some tasks improves after "routing tuning," while others decline compared to "single task fine-tuning" (see Table 2)? Specifically, the variance in performance changes across different Atari games after routing tuning is quite significant, and it's unclear what factors contribute to this. For example, why does 'Breakout' improve substantially, while 'Pong' sees a noticeable drop? This inconsistency needs further investigation and explanation.

- Similarly, in Table 3, the performance on most general tasks worsens after Routing Tuning, which seems to contradict the claim in Line 466 that "both single-task fine-tuning and Routing Tuning improve the model’s performance on general datasets." Am I misunderstanding this? The claim is not supported by the data presented, and the observed performance degradation on general tasks after routing tuning raises concerns about the method's generalizability and the potential for negative transfer.

- The concept of "Maximize Merge" seems a bit unusual. I’m not saying it’s unfeasible, but what if we simply trained all game tasks together with general data in one model over more iterations? This important multi-task learning baseline is missing in Table 2. The absence of a direct comparison to a standard multi-task learning approach, where all tasks are trained jointly, makes it difficult to assess the true effectiveness and efficiency of the proposed merging technique. It's crucial to understand if the proposed method offers any advantage over a simpler, more established baseline.

### Questions
- Motivation: Why do we want to merge different LoRA adapters? Can we simply retain the task-specific adapter for this use case?


- I've noticed several typos, including those in lines 259, 261, and 433. The captions for images and tables could be more informative and helpful.

I am open to rating adjustment if my concerns discussed above are addressed.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method for fine-tuning VLMs in a continual learning setting, progressively adding new tasks via LoRA adapters. To preserve the original model's performance while fine-tuning for each new task, two additional losses are introduced: (i) a KL-divergence loss that aligns the logits of the fine-tuned model with those of the original model and (ii) a norm loss to push general task activations toward zero. When fine-tuning multiple tasks, the method uses SVD to iteratively merge the pairwise task-specific adapters into a single unified model.

### Strengths
The paper is clearly written, well-structured, and provides a strong motivation for the proposed method. Each stage of the process is well-explained, with experiments on pre-trained Atari tasks that demonstrate the approach’s effectiveness.

### Weaknesses
1. Comparison to Baselines in Experiments

While the proposed method is compelling, the choice of baselines and experimental setup could be improved for clarity. The Atari dataset is derived from a pre-trained APPO algorithm, more like treated as the expert dataset for distillation. Thus, the approach aligns more with multi-task distillation than traditional RL. Comparing the method directly to RL approaches like DreamerV3 and DART, which train from scratch, may not be fully appropriate. Instead, it would be more informative to present the original performance scores from the APPO algorithm and compare them to the distilled VLM's scores after each fine-tuning step. This would clarify how well the method preserves performance relative to the initial expert model. Furthermore, the paper should clarify whether the VLM is initialized with random weights or pre-trained weights before distillation, as this significantly impacts the baseline performance.

2. Baseline Methods and Table 4 Clarifications

The explanation of the baselines in Table 4, especially the SVD method and the DARE method variants, is somewhat unclear. Providing a detailed description of these baselines and how they integrate into the benchmark would improve clarity, especially for readers who may be unfamiliar with each method. A brief explanation of each baseline’s structure, strengths, and limitations would also better highlight the unique challenges and contributions of the proposed approach. Specifically, the paper should clarify if the SVD method is applied to the LoRA weights directly or to the full weight matrices, and how DARE is adapted to the continual learning setting.

3. Task Weight Balancing in Loss Function

The paper lacks discussion about task weighting (Equation 2) and how it impacts model performance. Specifically, how is the balance between general task data and fine-tuning data managed, and how sensitive is the method to this balance? A series of ablation studies exploring the effect of task weightings and data distribution would enhance understanding and demonstrate the robustness of the approach. It is unclear how the loss weights for the KL-divergence and norm loss are chosen, and whether these are tuned for each task or kept constant. The paper should also discuss the impact of different weighting strategies on the final performance.

4. Direct Multi-Task Fine-Tuning Performance

It would be insightful to assess LoRA’s performance when applied directly to multi-task fine-tuning, as a reference point. This could help define an upper-bound performance level without SVD approximations, allowing readers to see the potential trade-offs introduced by the proposed merging approach and better appreciate the value of SVD in merging adapters without significant performance loss. This direct multi-task fine-tuning should also be compared to the proposed method in terms of computational cost and memory requirements, to provide a more comprehensive analysis.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
