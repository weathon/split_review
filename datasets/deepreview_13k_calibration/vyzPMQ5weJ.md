# TURNIP: A “Nondeterministic” GPU Runtime with CPU RAM Offload

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 6, 5, 5

## Abstract
An obvious way to alleviate memory difficulties in GPU-based AI computing is via \emph{CPU offload}, where data are moved between GPU and CPU RAM. While CPU offload is useful, it can greatly slow down a computation due to the relatively slow transfer rate between CPU RAM and GPU RAM.  To address this, overlapping memory transfer and compute is a necessity, but this asynchronicity introduces nondeterminacy, and hence it is impossible to know beforehand what is the best order of operations. We describe \Sys{}, which is a system for running AI computations using CPU offload, designed to handle this nondeterminacy.  The key innovation in \Sys{} is the compilation of the AI computation into a dependency graph that gives the \Sys{} runtime freedom to run operations such as GPU kernel calls in many different orders; at runtime, \Sys{} chooses the best order on-the-fly, in response to real-time events.  We find that \Sys{} outperforms standard, PyTorch-based systems supporting constrained GPU RAM by a significant margin, and also avoids out-of-memory errors in a severely memory constrained environment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents TURNIP, a GPU Runtime that incorporates CPU-RAM offload into the execution graph of AI models under memory constraints. Specifically, the authors create a MemGraph and GPU memory mapping by simulating task graphs. Comparing with PyTorch-based systems, they show faster runtimes of LLMs primarily for short sequence lengths.

### Strengths
- The paper is well-written and the examples are helpful
- The problem addressed in this work is interesting and relevant
- Using LLaMA and LoRA in the experiments makes this work applicable

### Weaknesses
 - The idea of "nondeterministic" is not new. The described scheduler is simply a work-conserving dynamic scheduler. It lacks novelty in its scheduling approach, which is a well-established concept in parallel computing.
- The simulation of the task graph to create the MemGraph is omitting any possible knowledge of execution times. Therefore, the resulting memgraph is only dependent on the topological sort and thus likely suboptimal. The lack of execution time awareness during MemGraph construction means that the resulting graph may not reflect the actual runtime bottlenecks, leading to inefficient memory management.
- The authors only present memory allocation sizes of 1 unit each and claim that "In the 'real life' case where tensors are variably-sized, the algorithm does not change appreciably". Intuitively, the problem should get significantly harder with variable size allocations. The authors should elaborate on this. The claim that variable-sized tensors do not significantly impact the algorithm's performance is not sufficiently justified and requires further analysis and experimental evidence.
- Section 7 could benefit from a more formal analysis. The claims made in this section lack rigorous mathematical backing and would benefit from formal proofs or theorems.
- In Section 8: "Note that these are PyTorch-based systems, whereas TURNIP is not." Does that mean the authors are running their system in C++ while the others are running in Python? Does this explain the initial performance benefit for low sequence lengths? They should run a test of a model that has no memory problems. In that test all algorithms should be the same. The performance comparison is potentially biased due to the implementation language differences, and a fair comparison requires running all systems under identical conditions, specifically when memory is not a constraint.
- Section 8, Nondeterministic vs deterministic: In the deterministic case precedence constraints are added based on a topological order which has many solutions. Therefore, it is unsurprisingly weaker. The authors should compare to any other scheduling algorithm, such as priority-based algorithms (e.g. priority-based list scheduling). The comparison to a deterministic scheduler is not sufficient, and the authors should benchmark against other dynamic scheduling algorithms, such as priority-based list scheduling, to demonstrate the true effectiveness of their approach.

Minor issues:
- l147 takes is -> takes as
- Pacement of figures in Sec 4 is not ideal. Try placing them where they are discussed.
- Fig. 7: Why is there a memory dependency from 4 to 3. It should at least be dashed.
- Figure 8 -> Algorithm 1, Figure 9 -> Algorithm 2
- Figure 8: Assignment and comparison of v_allocHzn.loc in the first "if" clause is difficult to understand

### Questions
1) What is the effect of C++ vs Python?
2) Please elaborate on the effects of variable size allocations on the Memgraph generation
3) How does it compare to other existing work-conserving, priority-based algorithms?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a runtime system for executing AI applications via GPU-to-CPU offloading. The system dynamically determines whether to allocate AI computations to GPU or CPU memory. It begins by transforming a task graph into a memgraph and implementing the memgraph engine through simulations. This approach enables efficient execution of AI computations through best order of actions (offloading or reloading).

### Strengths
Provided detailed explanations of how to generate memgraph
 
Implemented a working system

### Weaknesses
The paper lacks detailed discussions on how Turnip differs from existing systems mentioned in the related work section.

It is unclear how the simulation for memgraph is generated.

The simulation-based memgraph implementation raises questions on how the system guarantees optimal action sequencing during runtime.

Has the system been opensourced?

There are language issues here and there:
Page 3: Turnip takes [as] input ...
Three GPUs, each [having] five ...
With seven tensors [in] total ...

### Questions
How is the simulation obtained to generate the memgraph?

How does the system ensure that operations are executed in the best order at runtime?

Has the system been open-sourced?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents TURNIP, a GPU runtime that supports offloading data to CPU RAM to remove GPU memory restrictions in AI computations. TURNIP addresses the challenges of nondeterministic execution introduced by the slow data transfer rate between CPU RAM and GPU RAM, which harms computational efficiency. TURNIP’s main contribution is its use of a dependency graph (MEMGRAPH) that allows for overlapping execution of GPU kernel operations and memory transfers. The system dynamically chooses the best order of execution based on real-time events, thus minimizing idle times caused by memory transfer delays. TURNIP outperforms existing systems like PyTorch-based ones in constrained GPU environments, contributing to efficient memory management in AI workloads.

### Strengths
1. Originality: TURNIP accepts an abstracted version of a generic GPU computation. Other systems are more specifically targeted to certain categories of models, optimization algorithms, or specific tasks such as training or inference. None of the previous work considers the effect of the non-determinism of offload and reload operations on system performance, nor does it focus on the system runtime.
2. Quality: The quality of the design is demonstrated by experiments under various hardware conditions (A100 and P100), using LLAMA 7B & 65B.
3. Clarity: The details of the idea are clearly demonstrated with graphs and explanations in section 4-7.
4. Significance: TURNIP provides a generic solution to democratize AI computing, especially LLMs, which extends the functionality of older GPUs and enables large-scale AI model operations in constrained environments, making it valuable to both the AI and systems communities.

### Weaknesses
2 limitations that the author stated in the conclusion section of the paper, which potentially harms the significance of contribution (1) and soundness (2):
1. The biggest limitation of TURNIP is that the input computation (in the form of a TASKGRAPH) must be static and known completely beforehand so that the MEMGRAPH can be constructed. This is not of consequence during model training, but can be an issue during any recursive, generative AI computation. This includes LLM inference, where the next token must repeatedly be generated and the KV -cache increases in size. There are some naive solutions to this (such as pre-compiling a MEMGRAPH for a specific number of token generations in the case of an LLM) but more work will be necessary to create a satisfactory solution to recursive
computation.
2. Another limitation is that while the experiments showed that TURNIP has certain performance advantages, it is impossible to be sure where those advantages come from. Our ablation shows that a fixed execution order slows TURNIP, suggesting that non-determinism is important. But unlike ZeRO and FlexGen, TURNIP was implemented from the ground up and does not rely on
Python or PyTorch—that fact alone could account for some of the performance differences.

Others:
1. The experiments conducted in this paper use the LLAMA 1st generation model, while the newest one up to date is already LLAMA 3.2. The paper will benefit from using the SOTA LLMs to demonstrate the effectiveness of TURNIP. The architectural differences between Llama 1 and later versions, such as the introduction of Grouped Query Attention (GQA) in Llama 2, significantly impact computational complexity and memory access patterns. GQA reduces the number of query heads, altering the dynamics of the attention mechanism and potentially leading to different runtime performance characteristics. Therefore, using Llama 1 may not accurately reflect the performance of TURNIP on current state-of-the-art models.
2. As nowadays, the sequence length has grown rapidly (e.g., LLAMA 3.1 models have already supported 128K context window), the paper only did experiments on max 16K, so experiments on longer sequence length will be appreciated to demonstrate the effectiveness of TURNIP. Furthermore, the experiments in Figure 10 do not explore the limits of the system, as no OOM (Out of Memory) errors are demonstrated for the 7B LLaMA model with batch sizes of 8 and 16. Longer sequence lengths should be tested until OOM occurs to fully evaluate the capabilities of TURNIP.
3. more diverse hardware, such as V100 and H100, can be used in the experiments if possible. Nowadays, people rarely use P100, while some still stick with V100. Meanwhile, H100 represents cutting-edge technology.
4. We already have the 405B model in LLAMA 3.1, so seeing how it performs with TURNIP can make the results more convincing.
5. In Figure 10: Time for LLaMA first token (prefill) inference, A100 server, TURNIP seems to show some scalability issues (e.g., 7B inference batch size 8, TURNIP starts to demonstrate the worst run time when the sequence length is 16K, compared to FlexGen and ZeRO Inference). Although the author mentioned that FlexGen uses very low precision arithmetic to save RAM and speed computing, this doesn't explain the issue here. The paper does not discuss that the softmax attention operation in TURNIP, when decomposed across multiple GPUs, can consume a large portion of GPU memory, potentially leading to performance bottlenecks when the sequence length increases. This is particularly evident in the 7B LLaMA model with a batch size of 8 and a 16K sequence length, where TURNIP's performance degrades significantly compared to ZeRO and FlexGen.

### Questions
The reviewer is happy to raise the rating if some/all the experiment issues stated are addressed.

1. Do you already have any plan to address your paper's known limitations? Since you build a customized framework that doesn't involve Python or PyTorch, For the second one, I believe a separate experiment, when no CPU offloading is involved, comparing your framework with Pytorch on top of the existing experiment parameters can somewhat contribute to the understanding of the performance differences.
2. Do you have any comments on the experiments that I think are missing? (In the weakness section, Others, 1-4)
3. Do you have any explanation for the 5th point in the weakness section under the others sub-section?
4. Just out of curiosity, would it be possible to apply TURNIP to generic graphics or data processing? I feel like it's highly possible.
5. Last question that doesn't contribute to the paper's rating: Will you open-source the code once the paper gets accepted in the future?

### Soundness
2

### Presentation
4

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
This paper presents Turnip, a software framework to support CPU memory offloading for training and inferencing deep neural networks. The key idea is to introduce a MemGraph, generated at the compilation phase, which is then used to maximize computation and memory transfer overlaps. Turnip was evaluated on 7B and 65B LLaMA models and compared against ZeRO-Inference. The experimental results demonstrate that Turnip reduces first-token latency during inference and accelerates LoRA-based model fine-tuning.

### Strengths
An interesting approach for incorporating dependency analysis during the compilation phase to optimize offloading and reloading operations. The evaluation was conducted using a state-of-the-art LLM.

### Weaknesses
A straightforward approach where the positions of tensors reloaded to GPUs are predefined at specific slots through a compilation process based on the data flow graph. This is fine for simple model architectures with a static execution flow but can struggle to deal with dynamic networks like MoEs where tensors/variables are activated based on the current input data?

The evaluation can be improved. For example, I would like to see a scalability evaluation by testing Turnip on various model sizes, as well as models with f16 during inference.

This may speed up simple model architecture, but is difficult to work with or achieve better performance on complex/dynamic model structures. Second, the experiment design could introduce more workloads such as 13B, 175B, 400B models and more scenarios such as half precision full parameter training and even more solutions such as ZeRO offload, seen Questions.

### Questions
What is the definition of the MemGraph referenced in Figure 5? Does it represent solely a data dependency graph with memory dependencies, or does it include additional information like control flow dependency?

In Figure 6, if the tensor locations on GPU devices are predetermined at the compilation stage, will different tensor sizes lead to GPU memory fragmentation? 

How does TURNIP compare to TensorRT or other GPU-only solutions for inference? This information will help us understand its overhead. 

ZeRO-Offload and ZeRO-Infinity adopt different strategies for allocating tensors between GPU devices and CPU memory. To provide a more comprehensive comparison, could you include GPU-only and ZeRO-Offload solutions in Figure 13?

Lastly, why was ZeRO-Infinity not configured with an NVMe as secondary storage, as shown in Figure 13? Doing so could potentially extend the input sequence length or support larger model sizes.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents TURNIP, a GPU runtime system optimized for AI computations under constrained GPU memory by utilizing CPU RAM offloading. TURNIP addresses the challenge of nondeterministic execution by introducing a dependency graph -- MEMGRAPH, which allows for flexible operation sequencing. The approach dynamically decides the best operation order at runtime, minimizing GPU stalls caused by memory transfers.

### Strengths
++ The paper targets important problem of addressing GPU utilization

### Weaknesses
-- The proposed approach may perform poorly when handling complex, dependency-heavy workloads, particularly those with long critical paths. The non-deterministic scheduling might lead to inefficient resource utilization if tasks on the critical path are frequently delayed due to the execution of other, less critical operations. This could result in significant performance degradation compared to a more carefully orchestrated schedule.

-- It is not clear what unique challenge in nondeterministic graph-based scheduling for AI computing. While the paper highlights the non-deterministic nature of GPU-CPU memory transfers, it does not sufficiently articulate why existing scheduling techniques, commonly used in compiler research, are inadequate for AI workloads. The paper needs to better differentiate the specific characteristics of AI workloads that necessitate a novel approach beyond what is already established in the field.

### Questions
While this paper applies a nondeterministic MEMGRAPH approach to AI computing, similar techniques have been extensively explored in compiler research for general-purpose workloads. What are the unique challenges of applying such memory management strategies to AI-specific workloads?

The non-deterministic, event-driven scheduling works best for tasks with loose dependencies. However, heavily dependent tasks are common in AI workloads (e.g., transformer models with layer-by-layer computations). When dependencies are heavy, it may leave GPUs idle because tasks are queued. How does the proposed approach work under such a case? 

The paper does not seem to optimize GPU assignments or balance workloads effectively across GPUs, especially when some GPUs are busy while others are idle. This could lead to bottlenecks and inefficient use of resources in multi-GPU settings.

What is the time complexity of the MEMGRAPH construction process, particularly for very large TASKGRAPHS? How much overhead in this process?

### Soundness
3

### Presentation
2

### Contribution
2
