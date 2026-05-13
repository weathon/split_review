# Memory-Efficient Block Coordinate Descent for Hessian-Informed Zeroth-Order Optimizer

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Fine-tuning large language models (LLMs) for specific downstream tasks has traditionally relied on memory-intensive optimizers using classical backpropagation, which demands substantial memory to store model states for gradient computation, motivating the development of memory-efficient zeroth-order optimizers that operate in a forward-only manner.
However, the slower convergence of the zeroth-order optimizer remains a challenge, which recent research addresses by incorporating Hessian information to accelerate training, although storing even the diagonal Hessian requires memory equivalent to that of the model weights, leading to significant memory usage.
To mitigate this problem, we propose a novel approach that integrates the block coordinate descent (BCD) method with a Hessian-informed zeroth-order optimizer, allowing us to treat model layers as separate blocks and update only a subset of layers per training iteration, thereby reducing memory requirements and accelerating convergence.
Specifically, at each iteration, an active block of layers is selected according to the chosen BCD rule, such as ascending order, and their weights are updated while the other layers remain fixed, with diagonal Hessian information stored and updated exclusively for the active layers.
For fine-tuning foundation models of medium size (OPT-1.3B and LLaMA-2-7B), our method achieves up to 39\% memory reduction compared to existing Hessian-informed zeroth-order methods, while preserving baseline accuracy and memory usage to zeroth-order methods across various tasks, offering a memory-efficient alternative method for LLMs fine-tuning, especially on memory-constrained devices.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This study proposes a memory-efficient fine-tuning approach for large language models by integrating block coordinate descent (BCD) with a Hessian-informed zeroth-order optimizer.

### Strengths
Their method is more memory efficient than the previous methods HiZOO and has a comparable memory footprint as MeZO

### Weaknesses
The authors’ claim that their method is a practical, convergence-enhanced alternative to MeZO is not substantiated by evidence. I will summarize in three perspectives. 
1. In terms of memory usage, MeZO is more memory-efficient than the proposed method, as demonstrated in Tables 1, 2, and 4.
2. In terms of performance, the improvement of their method is minimal, with an average score of 70.2 compared to 70.0 for MeZO
3. In terms of convergence rate, Figure 3 indicates that the convergence rate of their method is similar to that of MeZO, showing no clear advantage.

### Questions
See the above weaknesses for questions.

### Soundness
3

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
4

### Summary
In this paper, the authors propose an optimisation algorithm for LLM fine-tuning which combines the block coordinate descent method with a Hessian-informed zero-order optimiser. This combination takes advantage of the hessian matrix information in HiZOO and memory efficiency in MeZO.  Mainly in OPT-1.3B, the authors demonstrate the benefits of proposed approach.

### Strengths
1. The paper is well-written and well structured, thus very easy to follow, even for the readers from other domains.

2. The proposed approach is well motivated, and could absorb the benefits from both HiZOO and BCD.

### Weaknesses
1. From my understanding, the proposed approach is a combination of both techniques of HiZOO and BCD with limited novelty. Are there any further insights from such a combination?

2. The evaluation of optimisation seems limited. Most of experiments focus on OPT-1.5B with limited dataset, please provide more evidence that B-PDF performs better than both HiZOO and MeZO in terms of the tradeoff, especially on LLaMA-2-7B, or larger-sized models. For instance, the runtime, memory and accuracy , or the convergence of various optimization algorithms. From Table 2, it seems that the authors only compare the optimisation algorithms under the toy setup considering the runtime for SGD is only 4 minutes. 

3. In equation 7, the authors showcase multiple types of BCD algorithms. But how different algorithms affect the memory / runtime / accuracy are not explained. 

4. Please correct me if I am wrong. LoRA rank can also affects the memory / runtime. Can we reduce the lora rank to reduce the memory to the same level that zeroth-order optimiser could achieve?

5. What is the performance of MeZO with BCD?

### Questions
Please see the above.

I have a minor question that: can we achieve the similar level of memory by reduce batch size in first-order approach? From Table 2, it sacrifices  much more runtime for memory, which makes me concern of the application of zeroth-order algorithm in real-world applications.  In a much larger model or larger finetuning dataset, can we afford such a runtime sacrifice (more than 50 times compared to LoRA)?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims to reduce the memory cost of Hessian-informed zeroth-order (ZO) optimization. The main idea of the paper involves incorporating block coordinate descent (BCD) with the Hessian-informed ZO optimizer (HiZOO), which selects a subset of layers to be tuned at each fine-tuning step. Experiments show that the proposed method achieves a significant memory reduction compared to an existing Hessian-informed ZO method in fine-tuning LLMs, while retaining comparable performance.

### Strengths
S1: Background and problem is well motivated, providing an extension to HiZOO, proposing several BCD methods that can be used to reduce the expensive memory consumption introduced by the hessian-informed ZO problem.

### Weaknesses
W1: Some challenges in clarity of methodology. For instance, the concept of blocks is not made clear, in some parts of the paper, there is an impression that each block corresponds a layer, but other sections imply that a block can correspond to a subset of layers. The BCD partitioning granularity used for experiments is not explicitly mentioned, causing some confusion and discrepancy.

W2: Authors emphasize more practical analysis in section 4.2 but experiments section is lacking. Only two models, OPT-1.3B and LLaMA2-7B were evaluated, making it difficult to compare how well the approach scales to different and larger models. In particular, HiZOO, the main baseline compared against evaluated on many larger models ranging from 13B to 66B. Some experiments on the effects of different block sizes would have been nice to help understand if there exists any tradeoffs between performance and memory consumption.

### Questions
Q1: It seems like there are various hyperparameters associated with BCD block selection like update interval and block granularity. How do you determine these?

Q2: How would the approach perform on larger models like LLaMA2-70B? Would performance still remain competitive compared against HiZOO?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to run 0-order optimization by diagonal Hessian precondition (HiZOO) in a block-wise fashion. This reduces memory requirement since it only needs to store model parameters and Hessian information for each block.

### Strengths
Results are better than for HiZOO using much less memory.

### Weaknesses
Results are compared to weakly engineered baselines, and activation storage needs are overexaggerated. The main missing ingredients here are gradient-checkpointing, which is easily enabled in most models by doing `model.gradient_checkpointing_enable()` and the possibility of doing weight update during backward computation (like LOMO and GaLORE do).

For example, one can easily fine-tune Llama-2-7B on a 24GB GPU, even on 4096 token sequences with gradient checkpointing, LOMO-like updates, and flash-attention2. The paper claims this will get an OOM error on the SST2 dataset (which has small sequences) on a 48GB GPU! 

The proposed algorithm's (B-PDF) main two contenders are HiZOO and BCD (block coordinate descent) using a first-order optimizer.
B-PDF seems better than HiZOO, but I believe the authors are using a suboptimal version of BCD with no gradient checkpointing, thus getting OOM errors. When BCD does not get OOM errors, it is clearly better (Table 3). 

And if one can run BCD with a first-order method, why bother with B-PDF?

The problem of exaggerating activation storage needs gets even more apparent when one thinks about scaling.
If we take a model with D blocks and embedding size N, the number of parameters is $O(DN^2)$. With batch size B and sequence length L, the activation storage needs are O(BLDN) (assuming flash attention here, which removed the $O(L^2)$ factor). The bigger the network, the smaller the activation storage compared to the parameter storage.

### Questions
How would B-PDF compare to properly engineered BCD or GaLORE?

### Soundness
2

### Presentation
3

### Contribution
1
