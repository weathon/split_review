# Meta-Learning Adaptable Foundation Models

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
The power of \textit{foundation models} (FMs) lies in their capacity to learn highly expressive representations that can be adapted to a broad spectrum of tasks. However, these pretrained models require multiple stages of fine-tuning to become effective for downstream applications. Conventionally, the model is first retrained on the aggregate of a diverse set of tasks of interest and then adapted to specific low-resource downstream tasks by utilizing a parameter-efficient fine-tuning (PEFT) scheme. While this two-phase procedure seems reasonable, the independence of the retraining and fine-tuning phases causes a major issue, as there is no guarantee the retrained model will achieve good performance post-fine-tuning. To explicitly address this issue, we introduce a meta-learning framework infused with PEFT in this intermediate retraining stage to learn a model that can be easily adapted to unseen tasks. For our theoretical results, we focus on linear models using low-rank adaptations. In this setting, we demonstrate the suboptimality of standard retraining for finding an adaptable set of parameters. Further, we prove that our method recovers the optimally adaptable parameters. We then apply these theoretical insights to retraining the RoBERTa model to predict the continuation of conversations between different personas within the ConvAI2 dataset. Empirically, we observe significant performance benefits using our proposed meta-learning scheme during retraining relative to the conventional approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a meta-learning approach to learning task-specific models when starting with a pretrained foundation model.  In place of standard retraining (also commonly referred to as continued-pretraining or pre-finetuning) on diverse tasks, a separate set of adapter weights are learned per tasks along with a shared set of global weights.  The shared weights are analogous to weights learned by meta-learning methods like MAML and Reptile that can be quickly adapted downstream to tasks drawn from a task distribution.  The task-specific adapters are taken to be LoRA weights for the theoretical analysis in the linear model setting and the subsequent experiments on a conversational dataset.  In the linear setting, the paper shows that standard retraining and task-specific finetuning is suboptimal relative to the meta-learning approach.  Experiments on the ConvAI2 dataset which models tasks as text from different personas shows meta-learning to outperform standard retraining.

### Strengths
- Meta-learning a set of shared global weights for ease of downstream adaptation is a well motivated problem but the writing does not make this motivation clear and the execution is poor especially on the empirical front.
- The performance of meta-learning for better downstream task adaptation is strong on the considered ConvAI2 dataset.

### Weaknesses
- The paper note multiple other approaches for meta-learning for foundation models but does not compare to other baselines beyond the retraining + finetuning paradigm.
- There is a lot of work on improving finetuning performance by mixing task specific data with either pretraining data or data from related tasks as the second stage or to replace both stages.  I would expect some of this work to be a baseline in addition to the retraining + finetuning baseline considered.
- It is unclear how the meta-learning stage is conducted.  In particular, are tasks considered one at a time or all mixed together and how are the shared weights $W$ updated?
- The theoretical results in the linear setting are not very useful.  They show that when there are $\geq 3$ tasks, the optimal global parameters can be recovered but that does not tell me what the benefit of increasing additional tasks are.  Typical analysis in meta-learning will consider the task distribution and provide regret bounds that depend on characteristics of the task distribution (for example [1](https://arxiv.org/pdf/1906.02717)).
- Empirical results are limited to just the ConvAI2 dataset when given the limited contributions of other aspects of the paper, I would have expected more of a focus on empirical performance.  Results in Table 1 (b) for rank-8 and rank-16 finetuning are not well explained nor as far as I can tell justified by the theory.

### Questions
- Please provide pseudocode for how the meta-learning is conducted.  How does your training approach compare to something like Reptile?
- Why is the performance for rank-16 meta training followed by rank-16 finetuning worse than that for rank-16 meta training followed by rank-8 finetuning?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel meta-learning framework for fine-tuning a foundation model to be adaptable to unseen downstream tasks via LoRA fine-tuning. The paper shows for a linear model that standard retraining is suboptimal whereas the proposed method can recover the unique optimal model parameters up to orthogonal symmetry when retraining on three or more tasks. They evaluate the method on a synthetic linear task and a text classification task, finding that Meta-LoRA outperforms standard retraining.

### Strengths
- The motivation makes intuitive sense; the standard way we prime models for downstream tasks diverges from how we actually fine-tune them.

### Weaknesses
- My main concern is that the experimental evaluation is weak. The paper has one non-synthetic experiment: if I'm understanding correctly, the LLM experiment involves turning the ConvAI2 dataset into a classification task where the model aims to select among possible continuations. There are many standard text classification benchmarks with publicly shared results that would give a better sense of how much Meta-LoRA contributes to downstream performance. Furthermore, there are many substantially better language models than RoBRETa. I'd suggest looking into SmolLM-(135M, 360M) or Qwen-2.5-0.5B in the <1B parameter regime, and there are several other larger models than that which should comfortably fit in a single GPU.
- I found the writing in section 2 to be unnecessarily complicated. For example, section 2.1 describes two stages of fine-tuning with datasets, where the first is over all weights and the second is over LoRA parameters. I think the matrix notation was unnecessary, and the setup shouldn't take over one page to describe.
- You state in the introduction that your framework can be implemented with any PEFT algorithm. Which other PEFT methods do you think the proposed method will work well with?

### Questions
Please see weaknesses above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the dependency of retraining and fine-tuning in the foundation models. They introduce a meta-learning framework infused   
LoRA, namely Meta-LoRA, to fine-tuning for the downstream tasks. They prove that their algorithm can find the second order stationary point and show good performance in ConvAI2 dataset.

### Strengths
This paper theoretically shows the standard "Retraining and fine-tuning" method fails to recover the optimal parameters in a low-rank space. Then it proposes a meta-learning framework, namely Meta-LoRA, and prove theoretical guarantee for finding second order stationary point for multi-task fine-tuning.

### Weaknesses
Please address the following concerns,

1. This paper proposes a Meta-LoRA method, but uses symmetric low-rank adapters in their method. I am not sure it works in some language models since this restricts the input dimension and output dimension in a layer to be the same, i.e., $U$ and $V$ have the same dimension. For example, not all the layers in RoBERTa satisfy this assumption. The authors also mentioned that they allow asymmetric adapters at test time. If so, I am curious how to get the asymmetric adapters based on the obtained symmetric adapters. So I think this method is somehow limited for most language models in practice. Please address the following questions:

- Clarify how to handle layers with different input and output dimensions in practice.
- Explain in detail how to transit from symmetric adapters during training to asymmetric adapters at test time.
- Discuss any potential limitations or modifications needed for applying the method to common language model architectures.

If they solve these concerns, I'd be willing to increase my rating.

2. The proof of Theorem 3 seems to show $\hat A = A^*$ and $\hat U_t \hat U_t^T  =  U^*_t  (U^*_t)^T $ when $T=3$. How does it hold when $T>3$?

3. This paper construct a contradiction to prove Theorem 4, I think it is the most interesting part in this paper. But it is pretty limited as $T=2$, which means this theory seems unconvincing in practice. So I hope that they can discuss the implications of this limitation for real-world applications where T is typically larger than 2.

4. In experiments, I don't see the report about the number of trainable parameters in your algorithm and SR method. Do both algorithms use the same number of adapters for tasks. If both algorithm tune a specific adapter for a retraining task and use the same number of tuning parameters, I think it is a fair comparison. Please consider the following suggestions:

- Provide a table or detailed description of the number of trainable parameters for each method in the experimental setup.
- Clarify whether the same number of adapters and tuning parameters were used for both algorithms across all tasks.

### Questions
Please refer to Weakness.

### Soundness
3

### Presentation
3

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
This paper studies the problem of supervised fine-tuning or retraining of foundation models and proposes an adaptation-aware objective that is trained using the fact that the final downstream purpose of retraining is to be adapted using a PEFT method like LoRA. They show that the standard objective will not require the optimal parameter in linear model setting while their objective will (under assumptions about infinite samples per task). The validate their findings on experiments in both the linear model and Transformer settings.

### Strengths
1. The problem studied is highly relevant and brings in ideas from meta-learning towards the analysis of fine-tuning of FMs. It is interesting to study whether an adaptation-aware objective can bring provable benefits.
2. The authors make progress by showing that, under a specific model, a meta-learning-style objective does better at parameter recovery.
3. The authors validate their findings experimentally, and the theoretical/empirical optimization result at T=2 and T=3 is interesting.

### Weaknesses
1. The lower-bound for “standard retraining” is stated in terms of rank, which does not seem very convincing. For example, the rank could be high but the norm difference between \hat A_{SR} and A^* could be very small (e.g O(1/T)) in which case we would still be doing fine with standard retraining. For example, Theorem 1 and Corollary 1 do not imply that “The optimal test error even scales with T.”
2. I do not understand how the “infinite sample loss” (Equation 6) is derived. It is defined as the expectation of a finite sample loss L_t^N, but then the limit as N->\infty is not taken. Furthermore, even at infinite samples the underlying noise in the model should still be present after taking expectations and a limit, but it is absent. Somehow the loss can be zero, which is better than the Bayes’ risk.
3. It is somewhat dissatisfying that the proposed objective and analysis largely depends fully on doing some type of low-rank adaptation. At full rank the Meta-LoRA objective is not useful, but in-principle an effective objective will interpolate smoothly between being able to do low-rank and full-rank adaptation effectively. In practice it does not seem like LoRA is useful for purposes of model capacity control, only to reduce fine-tuning memory usage,.
4. The model demonstrates no benefit of being useful beyond 3 tasks, despite this presumably being useful in practice. It seems the main purpose of optimization here is parameter recovery rather than statistical learning.
5. Code is not provided for the experiments.

### Questions
1. The abstract describes the FM paradigm as a two-phase procedure but the intro describes it as a three-phase procedure (it seems the abstract does not consider retraining a separate step).
2. Remark 1 alludes to the “generation process of each U_t^*” but I could not find any description of how those matrices are generated. The same remark also states that “k(T+1)\ll d” but I could not find that assumption anywhere (and while perhaps fine for theory, in practice it is not always true).

### Soundness
2

### Presentation
3

### Contribution
2
