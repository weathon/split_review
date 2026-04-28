# ACCO: Accumulate while you Communicate, Hiding Communications in Distributed LLM Training

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6, 5

## Abstract
Training Large Language Models (LLMs) relies heavily on distributed implementations, employing multiple GPUs to compute stochastic gradients on model replicas in parallel. However, synchronizing gradients in data parallel settings induces a communication overhead increasing with the number of distributed workers, which can impede the efficiency gains of parallelization. To address this challenge, optimization algorithms reducing inter-worker communication have emerged, such as local optimization methods used in Federated Learning. While effective in minimizing communication overhead, these methods incur significant memory costs, hindering scalability: in addition to extra momentum variables, if communications are only allowed between multiple local optimization steps, then the optimizer's states cannot be sharded among workers. In response, we propose \textbf{AC}cumulate while \textbf{CO}mmunicate (\acco), a memory-efficient optimization algorithm tailored for distributed training of LLMs. \acco~allows to shard optimizer states across workers, overlaps gradient computations and communications to conceal communication costs, and accommodates heterogeneous hardware. Our method relies on a novel technique to mitigate the one-step delay inherent in parallel execution of gradient computations and communications, eliminating the need for warmup steps and aligning with the training dynamics of standard distributed optimization while converging faster in terms of wall-clock time. We demonstrate the effectiveness of \acco~on several LLMs training and fine-tuning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The submission presents a method for training large models in a distributed setting where the computation and communication overlap. The method has been named "ACcumulate while COmmunicate or ACCO". The work extends the delayed parameter updates of sharded training to introduce an estimate of the model state after the step when the current ongoing gradient computation would have been applied. 

The introduced algorithm has been evaluated on pre-training of GPT-neo 36M on TinyStories dataset, GPT-neo 125M on OpenWebText dataset, and fine-tuning of GPT-neo 2.7B on Alpaca dataset.

The results claim that the presented method has better time to accuracy in some cases, such as for finetuning over 4 nodes.

### Strengths
The submission attempts to address a significant problem in contemporary machine learning, which is improving the scalability and efficiency of training algorithms for large language models. The presentation is fair and highlights the performance of the proposed method.

### Weaknesses
The submission lacks both novelty and insights. More specifically, 
* The delayed update with estimated gradients is a well-known technique and has already been even theoretically analyzed for its convergence in distributed machine learning; see "Elastic consistency: A practical consistency model for distributed stochastic gradient descent. Nadiradze et al. AAAI 2021, Section: Elastic Scheduling". In essence, introducing estimated gradients before the actual update while gradient updates are computed for the previous batch is well-known and implemented. Elastic scheduling of Nadiradze et al. also showed better time to accuracy for the model it trained.
* The theoretical discussion of the work is only at a very high sketch level. Again, Elastic consistency for the convergence of the presented algorithm could be a good approach here. 
* There is no insight into why the performance gain happens in some cases and not in multiple other cases. In this context, it is less than fair to advertise this work as "Comparedto ZeRO, our implementation and experiments on several LLMs pre-training and fine-tuning tasks demonstrates that ACCO reduces the learning time upto 87% and successfully allows both sharding optimizer states across workers and the use of heterogeneous hardware."

### Questions
1. Can you please comment on how ACCO differs from Elastic Scheduling? Sharding is a system-related aspect brought into elastic scheduling. However, this is only a very incremental work described in some detail in the submission. Sharding in its merit is not novel; standard SGD implementation to achieve a minibatch size that does not fit on GPU memory naturally requires sharding.
2. Can you please explain why ACCO does not outperform DDP in Figure 6 results?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper proposes a gradient accumulation technique to address the communication overhead in synchronous training while maintaining low memory consumption. The approach involves splitting each mini-batch into two parts: the first half is used to compute an approximate next step of the model parameters, while the full mini-batch is then used to calculate a precise gradient update. The authors validate the effectiveness of this method through large-scale experiments.

### Strengths
This paper addresses a highly relevant challenge in large-scale model training: addressing the communication overhead that arises in synchronous distributed training, especially in large-scale scenarios. This approach addresses this challenge while keeping memory consumption low. The experimental results presented in this work are compelling. The authors show notable reductions in training time on realistic large-scale scenarios while keeping performance levels comparable to a standard synchronous method.

### Weaknesses
 * The gradient accumulation technique in this approach may introduce numerical instability, particularly when the approximate gradient step is computed using a significantly smaller batch size than the full gradient. This discrepancy could lead to a mismatch in the gradient landscape explored by the approximate and full updates, potentially causing the optimization to diverge or converge to a suboptimal solution. The accumulation of these errors over long training sessions, especially when slower devices are involved, could further exacerbate these issues, leading to exploding gradients or oscillations in the loss function.

* The paper would benefit from a clearer presentation, particularly regarding the implementation details of the sharded optimizer. The current description lacks clarity on how the optimizer states, such as the momentum and variance vectors in adaptive methods like Adam, are partitioned and managed across different workers. A more detailed explanation of how the sharded optimizer handles these memory-intensive parameters and how the local update step is performed with only a portion of the optimizer state would greatly improve the paper’s accessibility and allow readers to fully understand the memory reduction benefits of the proposed approach and its advantage over local updates.

### Questions
Which optimizer parameters contribute to high memory consumption? How do sharded optimizers work to reduce this memory load? Specifically, which optimizer parameters are divided among the workers, and what information is required for a sharded local optimization step, such as the one used to compute the estimated model parameters in this approach?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed an algorithm named ACCO, which jointly optimizes the memory cost and communication in LLM training. ACCO reduces communication overhead by concealing it under gradient computing. Experiments have been done on some pre-training tasks and fine-tuning tasks, which prove the effectiveness of ACCO.

### Strengths
•	Algorithm Design: The paper provides a new algorithm to conceal communication overhead of distributed training under gradient computing to support communication-efficient parallel training strategy.

•	Empirical Validation: The method is verified on some pre-training and fine-tuning tasks, results show that in some condition the time cost of distributed LLM training has been reduced a lot.

### Weaknesses
•	Experiment Weakness: The experiment is not rigorous enough, and it does not show a clear advantage when compared with the baseline DDP. The chosen pre-training and fine-tuning tasks are also not broad and sufficient. Specifically, the paper lacks a detailed analysis of the performance across different model sizes and hardware configurations. The experiments should include a more diverse set of LLM architectures and datasets to demonstrate the generalizability of the proposed ACCO algorithm. Furthermore, the paper does not provide sufficient details on the hyperparameter tuning process for both ACCO and the baseline, making it difficult to assess whether the comparison is fair. A more thorough ablation study is needed to understand the impact of different components of the ACCO algorithm on its performance.

•	Motivation Weakness: While the paper aims to optimize the distributed training process of large language models (LLMs), it would benefit from providing deeper insights and observations that clarify why the ACCO algorithm is particularly advantageous for LLMs, how split the mini-batch would influence the convergence. The paper does not adequately explain the specific characteristics of LLM training that make ACCO a superior choice compared to existing methods. The rationale behind the design choices of ACCO, especially in the context of LLM training, needs to be more clearly articulated. The paper should include a theoretical analysis or empirical evidence to support the claim that ACCO is particularly well-suited for LLMs.

•	Contribution to Memory Optimization is Weak: Although the paper claims to address both memory and communication challenges, its primary contribution lies in proposing a pipeline that divides the computation of mini-batch gradients into two successive stages. This approach primarily focuses on mitigating communication overhead rather than optimizing memory usage. Memory cost is more than ZeRO-1 actually. The paper does not provide a detailed analysis of the memory footprint of ACCO compared to other memory optimization techniques, such as activation checkpointing or gradient accumulation. A more thorough investigation of the memory usage of ACCO, including a breakdown of memory consumption for different components of the algorithm, is needed.

### Questions
Looking at weakness part.

•	Add more experiments ?

•	Could you provide more insights and observations on why the ACCO algorithm is particularly beneficial for training large language models (LLMs)?

•	Are there specific cases or experimental results that support the unique advantages of the ACCO algorithm for LLMs?

•	Beyond mitigating communication overhead, does your approach offer direct contributions to memory optimization?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose The ACCumulate while COmmunicate (ACCO) algorithm, which is a memory-efficient distributed optimizer. It overlaps gradient computation and communication to reduce overhead and enables sharding optimizer states. Experiments show ACCO achieves communication and memory efficiency in large language model training and fine-tuning.

### Strengths
1. Figure 2 is a good illustration of the proposed method where the authors propose an interleaved update method. The idea appears very novel.
2. The proposed method can be adopted in ZeRO, without obvious memory overheads.
3. The proposed method achieve similar convergence curves as DDP but higher throughput.
4. Memory efficiency as summarized in Table 1. Though it's still not as efficient as ZeRO1.

### Weaknesses
1. From Table 2, the performance of ACCO deteriorates when increasing the number of workers from 8 to 32. There might be an scaling issue for the proposed method. Could you provide model performance v.s. number of workers like Figure 3? Specifically, it's unclear if the observed performance drop is due to the increased number of workers or other confounding factors such as different hardware or training time. A more controlled experiment is needed to isolate the impact of worker count on the performance of ACCO. For example, experiments should be conducted on the same hardware and for the same number of training steps to provide a fair comparison.
2. Lacking in theoretical analysis. It appears easy to have a convergence analysis given the update formulation. It will be better to see how $\tilde{\theta}$ affects the convergence. The analysis should consider the impact of the delayed gradient on the convergence rate and stability of the training process. It would be beneficial to provide a bound on the error introduced by using $\tilde{\theta}$ instead of $\theta$ for gradient computation. Furthermore, the theoretical analysis should consider the impact of the communication frequency on the convergence behavior.
3. It does not seem appropriate to claim "as a form of plain SGD with no delay", because part of the gradient is computed at $\tilde{\theta}$ instead of $\theta$. This is a crucial point, as the use of $\tilde{\theta}$ introduces a form of gradient staleness, which is not present in standard SGD. The authors should clarify this point and avoid misleading claims. The update rule is more akin to delayed SGD, and the analysis should reflect this.

### Questions
1. Do you update optimizer states in both Eq(1) and (2), or only Eq(2)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes ACCO, a memory-efficient optimization algorithm tailored for distributed training of LLMs. ACCO introduces 1-step delay to overlap the execution of gradient computations and communications, and then compensate this delay via weight prediction. The experiments show that in both pretraining and finetuning tasks, ACCO can accelerate training almost the same accuracy compared to the baseline.

### Strengths
1. This paper proposes ACCO, a memory-efficient optimization algorithm tailored for distributed training of LLMs. ACCO introduces 1-step delay to overlap the execution of gradient computations and communications, and then compensate this delay via weight prediction. The experiments show that in both pretraining and finetuning tasks, ACCO can accelerate training almost the same accuracy compared to the baseline.
2. The proposed algorithm is compatible with data-parallel sharding.
3. The paper also proposes a strategy to maximize GPU usage, even with heterogeneous hardware.

### Weaknesses
My major concern is that some part of the proposed algorithm has already been proposed in some previous papers, which are not discussed. Regardless of some systematic improvement (adapting to DP sharding and heterogeneous hardware), 1-step delay and delay compensation would weaken novelty and contribution, and probably make the contribution incremental compared to those previous work. For more details:

1. SGD with one-step delay (DPU explained at the beginning of Section 3) is actually PipeSGD [1]. However PipeSGD is not cited or discussed.

2. PipeSGD + delay compensation has been proposed in SAPipe [2]. However SAPipe is not cited or discussed. And in SAPipe paper, this compensation method is also called weight prediction (WP). Although there are some differences in details, the delay compensation proposed in ACCO can generally be viewed as a variant of SAPipe, additional to the 3 options already proposed in SAPipe. To the best of my knowledge, Option 1 of SAPipe is the one closest to ACCO, where SAPipe Option 1 uses latest local gradients without synchronization, and ACCO uses the latest but half-accumulated local gradients with synchronization applied.

### Questions
1. The weight prediction of ACCO uses half-accumulated gradients (1st stage of gradient accumulation). Is it because the 2nd stage of gradient accumulation is required to overlap with and hide the communication (synchronization, averaging across workers) overhead of these half-accumulated gradients? If so, what about using the locally accumulated gradient without averaging across workers (I think it is still compatible with data-parallel parameter sharding), which will allow the algorithm to use more than half or even the entire accumulated gradients? Basically, I think there could be a tunable trade-off between accumulation error (difference between half-accumulated gradients and fully-accumulated gradients) and synchronization error (difference between local gradients and globally synchronized gradients).

2. What about theoretical analysis of ACCO? I see there is a short discussion at the end of Section 3 but no rigorous analysis/proof is provided for convergence. I think the theoretical analysis from SAPipe paper could be easily modified to adapt to the convergence analysis of ACCO.

### Soundness
2

### Presentation
3

### Contribution
2
