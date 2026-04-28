# Adam-mini: Use Fewer Learning Rates To Gain More

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
\vspace{-0.2cm}
We propose Adam-mini, an optimizer that achieves on par or better performance than AdamW with $50\%$ less memory footprint. Adam-mini reduces memory by cutting down the learning rate resources in Adam (i.e., $1/\sqrt{v}$). By investigating the Hessian structure of neural nets, we find Adam’s $v$ might not function at its full potential as effectively as we expected. We find that $\geq 99.9\%$ of these learning rates in $v$ could be \emph{harmlessly} removed if we (1) carefully partition the parameters into blocks following our new principle on Hessian structure; (2) assign a single but good learning rate to each parameter block. We then provide one simple way to find good learning rates and propose Adam-mini. Empirically, we verify that Adam-mini performs on par or better than AdamW on various language models sized from 39M to 13B for pre-training, supervised fine-tuning, and RLHF. The reduced memory footprint of Adam-mini also alleviates communication overheads among GPUs, thereby increasing throughput. For instance, Adam-mini achieves $49.6\%$ higher throughput than AdamW when pre-training Llama 2-7B on $2\times$ A800-80GB GPUs, which saves $33\%$ wall-clock time for pre-training.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Adam-mini presents a memory-saving approach to optimization, targetting large transformer models by cutting down the number of learning rates needed for each parameter. It does this by using Hessian-based partitioning to group parameters, so it assigns just one learning rate per block instead of for every single parameter, which cuts down memory use a lot. This setup holds up well in performance next to more traditional optimizers like AdamW, especially in terms of throughput and training speed, as it lowers GPU communication needs. Adam-mini shows it can work well on various deep learning tasks, optimizing models efficiently while saving both computing resources and training time.

### Strengths
1. Adam-mini cuts memory use by almost half (up to 50%) vs AdamW, by smartly dividing params based on Hessian structures and using block-level learning rates; this gives major memory savings without losing much performance on big language models.  

2. By reducing comunication overheads between GPUs, Adam-mini boosts throughput by about 49.6% during Llama 2-7B training and lowers training time by 33%, which is really helpful in setups with limited resources.  

3. Adam-mini provides a more efficient computational approach by skipping per-param learning rates while still matching AdamW's performance, closing the gap between memory efficiency and optimizer effectiveness across different neural net types, like LLMs and other deep learning architectures.

### Weaknesses
- This study mostly benchmarks on transformer models, leaving its effectivness on other architectures like CNNs and RNNs a bit underlooked; more benchmarking could either show it’s limitations or confirm its ability to adapt across other models types.

- The influence of the Hessian-based learning rate grouping on different gradient structures wasn’t deeply investigated, and comparing it with fully adaptive methods would make it’s efficiency clearer.

- Optimizer stability over long training durations hasn’t really been tested, so longer training runs would give more confidence in its reliability, especially for deep networks or tasks that need extended training.

- Adam-mini’s sensitivity to hyperparameters hasn’t been very explored, which might make tuning it more difficult, and more understanding here could show if it raises computational cost.

- Even though they briefly mention it, there’s no strong comparison with newer optimizers like Sophia and Lion; a head-to-head test would help show Adam-mini's specific advantages or where it could improve.

- Performance of the optimizer on tasks like fine-tuning and transfer learning is not talked about, and testing it on practical applications could confirm its strengths beyond just primary training.

- The grouping of parameters lacks deep mathematical support in the study, and adding a stronger theoretical basis would back up the partitioning method chosen and possibly lead to more improvements.

### Questions
1. How does Adam-mini make sure that its reduced learning rate partitions, relying on Hessian structures, can deliver a comparable optimization efficiency as full adaptive optimizers like Adam or AdamW, specially in dealing with sparse gradients and complex non-convex landscapes?

2. In which ways does Adam-mini maintain stability and avoid training instabilities, given its loss of per-parameter adaptation? Are there any specific mechanisms to prevent oscillations or divergence, particulary in deeper and more complex neural networks?

3. To what degree is the claimed memory savings consistent across varied model sizes and architectures, and does Adam-mini reliably reach faster convergence and throughput compared to the traditional adaptive optimizers?

4. How does Adam-mini approach hyperparameter sensitivity without the presence of per-parameter learning rates, and does this require additional hyperparameter tuning or raise computational costs?

5. What generalization ability does Adam-mini show when used on non-transformer models, such as CNNs or GNNs, and could its block-wise learning rate method limit performance in architectures where Hessian matrices are less structured?

6. How effectively does Adam-mini perform when compared to other recent memory-saving optimizers like Sophia or Lion, and is there potential for combining Adam-mini’s technique with finer adaptive methods to reach higher efficiency?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Adam-Mini, a new Adam variant for reducing the training memory cost. It changes Adam's parameter-wise learning rate scaling to block-wise learning rate scaling to reduce the cost of the second-order optimizer state. Extensive experiments show that Adam-mini can achieve on-par or better performance than AdamW with less memory footprint.

### Strengths
1. This paper studies an important problem and provides an interesting and novel solution. 
2. The paper is well-written with clear motivation and good presentation flow.
3. Extensive experiments are conducted to justify Adam-mini's effectiveness.

### Weaknesses
1. Integrating Adam-mini into existing training frameworks seems non-trivial. For example, according to Algo 2, we need to specify the partitions manually for large models. Is there any solution to automatically get a good partition given general Pytorch models? 
2. It will be good to add discussions/insights about how to adapt hyper-parameters when switching from AdamW to Adam-mini.
3. In addition to training curves, it will be better to have comparisons after model convergence. Additionally, it will be interesting to see results on diffusion transformers for diffusion model experiments. Some public diffusion transformer training codebases:
- https://github.com/facebookresearch/DiT
- https://github.com/mit-han-lab/efficientvit/blob/master/applications/dc_ae/README.md

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Adam-mini, a variant of Adam with significantly reduced memory requirements. The approach leverages the near-block-diagonal structure observed in the Hessian of neural networks, and assigns a single learning rate to groups of parameters within a block, thereby reducing memory usage substantially.

The Authors observe limitations in PyTorch’s default partition, particularly for Transformers. To address this the Authors examine the Hessian structure of a small Transformer and identify three distinct classes of Hessian sub-blocks within Transformers and propose a tailored partitioning strategy based on this. Additionally, the authors introduce a simple method to determine a suitable learning rate for each block by assigning the average of Adam’s $\upsilon$ to that block. 

The claims are supported by various experiments including pre-training experiments on GPT-2 and Llama series where Adam-mini is compared against AdamW and other SOTA memory-efficient Adam variants, which demonstrate the effectiveness of Adam-mini in reducing memory overhead while maintaining performance.

### Strengths
The paper is well-written, and the proposed idea is novel. The approach, though simple, achieves a substantial reduction in memory usage, higher throughput, and shorter wall-clock time without compromising performance. Given the increasing adoption of LLMs and their high demands on memory resources, this method has the potential to be impactful in memory-constrained LLM applications.

### Weaknesses
The method proposed in the paper does not seem to address large-scale non-Transformer models. Although Section C.2 includes experiments on various non-LLM tasks, it would be helpful to discuss whether Adam-mini offers advantages for large-scale non-LLM applications or if AdamW is preferred in these cases.

Moreover, given the success of the method on GPT-2 and Llama series and its potential impact, demonstrating the effectiveness of Adam-mini on more diverse models, such as BERT-like and vision transformers would be highly beneficial.

Minor referencing errors and typos:

- Line 294: instability on 1B models (see Figure 7 (d)) → instability on 1B models (see Figure 8)
- Line 349-350: As shown in Figure 7 (d). This strategy → As shown in Figure 8, this strategy
- Lines 1053-1054: The results are shown in Figure 15 → The results are shown in Figure 16
- Lines 418-419: Figure 9 (b) shows the loss curves → Figure 9 shows the loss curves
- Line 483: As shown in Figure 12 → As shown in Figure 12 (a)
- Table1 does not seem to be referenced except in the caption of Figure 14 in the appendix
- There appears to be no reference to Figure 19 in Section D.2
- What is “Adam-mini-2e-4-1B-v” in Figure 12 (a)?
- Line 374: BP in “where e is certain BP error” is defined 2 lines later.
- Lines 449-450: This might because → This might be because

### Questions
Minor referencing errors and typos:

- Line 294: instability on 1B models (see Figure 7 (d)) → instability on 1B models (see Figure 8)
- Line 349-350: As shown in Figure 7 (d). This strategy → As shown in Figure 8, this strategy 
- Lines 1053-1054: The results are shown in Figure 15 → The results are shown in Figure 16
- Lines 418-419: Figure 9 (b) shows the loss curves → Figure 9 shows the loss curves
- Line 483: As shown in Figure 12 → As shown in Figure 12 (a)
- Table1 does not seem to be referenced except in the caption of Figure 14 in the appendix 
- There appears to be no reference to Figure 19 in Section D.2
- What is “Adam-mini-2e-4-1B-v” in Figure 12 (a)?
- Line 374: BP in “where e is certain BP error” is defined 2 lines later. 
- Lines 449-450: This might because → This might be because

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel memory-efficient optimizer Adam-mini to reduce the memory cost by cutting down the learning rate resources in Adam. I tries to partition the parameters into different blocks and assign a single learning rate to each parameter block to reduce the memory cost from `v` in adam. The experimental results illustrate that the proposed method can achieve 49.6% higher throughput than AdamW for LLaMA2-7b pre-training.

### Strengths
1. This paper focus on an interesting and important problem. memory-efficient optimization is very important for llm training. 

2. The paper provides the results from diverse domains to verify the efficiency and performance of Adam-mini. 

3. This paper provides the results on LLM pre-training, SFT and RLHF to verify the performance of proposed method Adam-mini.

### Weaknesses
1. The paper is not very easy to follow for me. For example, the paper first aims to partition the model parameters into blocks by Hessian structure. However, in the algorithm part, the paper first tried the PyTorch default partition to construct the blocks for middle-scaled non-transformer tasks and then said the default partition can not work well for transformers. Therefore, they analyzed the exact Hessian at
initialization of transformer training and define the method of partitioning for different layers (such as attention layers, MLP layers). That make me feel a little confused about your proposed method. 

2. The motivation is also not very clear to me. I can understand that different blocks need different learning rates. But why a single learning rate can work well for the parameters of the whole block is not very clear to me. I noticed that the authors provided a toy example (random quadratic minimization problem) to show that, but I am not clear whether the conclusion can be general (for neural network training). Because the conclusion is very important and the proposed algorithm is also based on this conclusion, I think the authors could provide more analysis. 

3. The most visualization in this paper (Figure 2, 3, 4, 7) can just say different blocks show different patterns, but we cannot obtain the conclusion that the whole parameters of each block should use the same learning rate. 

4. The introduction about using the mean of (v * v) to calculate the learning rate is also not very clear. That is also the main contribution of your proposed method. Since you use the mean of (v * v) to change second-order momentum. 

5. I can understand that the paper proposes many valuable experimental findings, but the proposed method make me feel a little tricky. In the proposed method, the authors design too many components and make me consider the generality and scalability of the method. 

6. The paper should also provide some comparisons with strong baselines, such as Lion. These memory-efficient optimizers is very easy to use and general for different models (resnet and transformers). Therefore, you do not need to consider different algorithm design for different model architecture. They can also save the memory cost and obtain higher flops. Based on that, actually, I don't think adam-mini has too many advantages compared with them.

Although the paper provides the results of Lion, I am not sure whether the authors fully tune the hyper-parameters, because Lion usually need a very different LR. In addition, [1] provides thorough comparisons between different optimizers (memory-efficient optimizers) and the results illustrate that the memory-efficient optimizers can obtain comparable results with Adam.  Therefore, I guess these memory-efficient optimizers can finally achieve a very similar performance.

### Questions
1. Figure 6, training loss is not a great metric to compare the performance of different methods, a lower training loss may mean overfitting. It could be better id the authors can provide results on downstream tasks.

### Soundness
2

### Presentation
3

### Contribution
2
