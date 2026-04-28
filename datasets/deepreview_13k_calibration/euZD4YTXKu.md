# ZO-Offloading: Fine-Tuning LLMs with 100 Billion Parameters on a Single GPU

- Decision: Reject
- Avg Score: 3.75
- Scores: 8, 3, 3, 1

## Abstract
Fine-tuning pre-trained LLMs typically requires a vast amount of GPU memory. Standard first-order optimizers like SGD face a significant challenge due to the large memory overhead from back-propagation as the size of LLMs increases, which necessitates caching activations during the forward pass and gradients during the backward pass. In contrast, zeroth-order (ZO) methods can estimate gradients with only two forward passes and without the need for activation caching. Additionally, CPU resources can be aggregated and offloaded to extend the memory and computational capacity of a single GPU.
To enable efficient fine-tuning of LLMs on a single GPU, we introduce ZO-Offloading, a framework that strategically utilizes both CPU and GPU resources for ZO. ZO-Offloading dynamically offloads model parameters to the CPU and retrieves them to the GPU as needed, ensuring continuous and efficient computation by reducing idle times and maximizing GPU utilization. Parameter updates are integrated with ZO's dual forward passes to minimize redundant data transfers, thereby improving the overall efficiency of the fine-tuning process. The ZO-Offloading framework also incorporates a novel low-bit precision technique for managing data transfers between the CPU and GPU in AMP mode, as well as asynchronous checkpointing for LLM fine-tuning.
With ZO-Offloading, for the first time, it becomes possible to fine-tune extremely large models, such as the OPT-175B with over $\textbf{175 billion}$ parameters, on a single GPU with just $\textbf{24GB}$ of memory—a feat unattainable with conventional methods. Moreover, our framework operates without any additional time cost compared to standard ZO methodologies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes ZO-Offloading, a framework that efficiently fine-tunes large language models (LLMs) on GPUs and CPUs by leveraging zeroth-order (ZO) optimization. ZO-Offloading alleviates the memory requirements of standard first-order optimizers by using two forward passes instead of backpropagation, eliminating the need for activation caching. It optimizes resource usage by minimizing GPU idle times by offloading model parameters between the GPU and the auxiliary memory of CPU. It also enables low-bit data transfers and synchronous checkpointing to optimize against memory space.

### Strengths
1. Devise a dynamic workload scheduler to arrange overlaps of computation and communication, including mechanism such as reusable one block space and asynchronous checkpointing that have industrial value.
2. Offloading partial GPU memory to auxiliary CPU memory fit in models of large capacities.

### Weaknesses
As Table 1 conveys memory usages and throughputs of ZO-Offloading and other baselines, authors may consider showing overlapped computation and communication time, the ratio of overlaps compared with other ZO baselines. Doing so gives a clear picture of the advantages of ZO-Offloading's dynamic overlap scheduling. Specifically, the table lacks a direct comparison of the time spent on computation, communication (both upload and download), and the degree of overlap achieved by ZO-Offloading. This makes it difficult to assess the effectiveness of the proposed dynamic scheduling against naive implementations. Furthermore, the analysis should include a breakdown of communication time into parameter transfer and gradient transfer, as these may have different overheads and overlap characteristics. The absence of this detailed timing data makes it challenging to fully appreciate the benefits of the dynamic scheduling mechanism.

### Questions
The authors are encouraged to elaborate preemptive parameter updates by 1). showing a diagram regarding this mechanism, especially how it "halves the usage of interconnection bandwidth" compared with traditional two data transfer streams.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a technique called ZO-Offloading which scales zeroth-order optimization methods of LLM finetuning by offloading model parameters to CPU. ZO-Offloading attempts to efficiently overlap the layer computation with transfers between CPU and GPU in order to minimize/avoid computation stall times. ZO-Offloading also integrates mixed-precision techniques and asynchronous model checkpointing to improve overall finetuning efficiency. The key result is the ability to finetune a 175B model using just 24GB of memory.

### Strengths
- The paper tackles an important AI democratization problem of reducing the hardware cost of using SOTA LLMs.
- Extending systems optimizations, such as offloading, to less-studied zeroth-order optimization techniques is empowering to the model scientists.

### Weaknesses
 - The main weakness is that this work appears to overlook critical prior work such as ZeRO-Infinity. This oversight harms the paper in at least two major ways: 
 1. There is no clear novelty in the parameter offloading approach since ZeRO-Infinity already demonstrated overlapping parameter offloading with forward (and backward) pass. 
 2. The claim that finetuning 175B model using 24GB is unprecedented given that ZeRO-Infinity enables finetuning 1T model with Adam using 32GB.

 [**Suggestion**]: To address the above concern, the authors should compare ZO-Offloading to ZeRO-Infinity, highlighting any key differences or improvements. Also, authors should revise their claims about novelty and unprecedented capabilities in light of ZeRO-Infinity's achievements.

- The asynchronous checkpointing appears to be missing from the evaluation section, making it difficult to appreciate the efficiency or effectiveness. 

 [**Suggestion**]: This concern can be addressed by updating the evaluation with results comparing asynchronous checkpointing and the baseline synchronous checkpointing. A useful evaluation metric to report would be training slowdown of checkpointing across different model sizes.

- Given that zeroth-order optimization requires only forward pass, I think comparison with the prior offloading inference work like FlexGen or ZeRO-Inference (another overlooked prior work) would be appropriate. Such comparisons could focus on forward pass efficiency.

 [**Suggestion**]: To address this concern, the authors should include a comparative analysis table or graph that shows forward pass efficiency metrics (e.g., throughput, latency) for ZO-Offloading versus FlexGen and ZeRO-Inference across different model sizes (and perhaps batch sizes). Since this is a finetuning scenario, throughput comparison is probably most useful.

### Questions
1. Does the dual forward computation of block i occur before that of i+1? If so, how is block i updated based on loss information? (Figure 2). 
2. What is the hardware environment of evaluation?

### Soundness
2

### Presentation
2

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
The main goal of this paper is to allow fine-tuning of very large LLMs even on a single-GPU.  Their technique utilizes the host (CPU) memory for shuttling data between GPU and CPU memory. It maximizes GPU utilization by dynamically offloading model parameters to the CPU. 
Parameter updates are integrated with ZO’s dual forward passes to minimize redundant data transfers. They have shown the integration of their technique with low-precision format. They claim to have no overheads compared to standard ZO methodologies.
They claim to be the first work that allows fine-tuning extremely large models, such as the OPT-175B with over 175 billion parameters, on a single GPU with just 24GB of memory.

### Strengths
They claim to be the first work that allows fine-tuning extremely large models, such as the OPT-175B with over 175 billion parameters, on a single GPU with just 24GB of memory. If so, this is a great feat and very useful to the community. 
They utilize ZO's architectural features for CPU offloading, so that is an intelligent integration.

They have shown the integration of their technique with low-precision format.
Good ablation studies: they show breakup of performance due to several individual ideas.

### Weaknesses
 * Some other works also claim to run OPT-175B on a single GPU, e.g., 

--FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU
--LUT-GEMM: QUANTIZED MATRIX MULTIPLICATION BASED ON LUTS FOR EFFICIENT INFERENCE IN LARGE-SCALE GENERATIVE LANGUAGE MODELS
--OPTQ: ACCURATE POST-TRAINING QUANTIZATION FOR GENERATIVE PRE-TRAINED TRANSFORMERS

Please comment on them. If required, you may need to modify the sentence in your manuscript "With ZO-Offloading, for the first time, it becomes possible to fine-tune extremely large models...."


* Can you comment how your technique compares against
https://huggingface.co/docs/accelerate/index

* BLOOM models are also open-source. Running only OPT models limits your showcase of the applicability of this model. Communication delays are not primary bottleneck for OPT, but may be so for other LLMs.
Also, MeZO paper has shown results with multiple datasets; this paper shows results with only one dataset.
This reviewer has carefully examined the supplementary material also.

* Table 3: no benefit from using FP8, compared to FP16? Even FP16/BF16 are useful only for OPT-6.7B. This means that uploading/offloading low-precision data does not help much, which means the CPU-GPU transfer (Communication) is not a bottleneck. Actually, the real benefit of your technique will be clear when this communication is a bottleneck. The lack of improvement with lower precision formats suggests that the memory bandwidth between CPU and GPU is not the limiting factor for performance, and the computational overhead within the GPU is likely the dominant bottleneck.

* Experimentation is somewhat weak and the proposed ideas are not very novel. Many works have already been done on shuttling data between CPU and GPU memories. The core idea of offloading parameters to CPU memory is not new, and the paper lacks a detailed comparison to other similar techniques. The novelty of the approach, therefore, is not very clear.


Minor:
* It may have been better to conduct ablation experiments on different CPU-GPU interconnect (PCIe) bandwidths/configurations, although the reviewer understands it is not easy. But some ablation could have been performed on GPU systems space. The lack of ablation studies across different interconnect speeds makes it difficult to assess the robustness of the approach under varying hardware conditions.

* Figures 2 and 3 and 4 use white color for text, which gets faded (with color background) when printed.

* Figure 1, instead of 0, X should have been shown. 0 is misleading.
Figure 1 caption could mention that these values are observed for a single GPU, because with multiple GPUs, you can definitely find these numbers.

Figure 1 shows GPU memory or CPU memory?

* "previously unattainable with conventional methods" is redundant.

* Incomplete phrase "Since CPU resources can be combined and offloaded to expand the memory and computational capacity of a single GPU"

* Can you theoretically say: What is the largest OPT model that your technique can run on a 24GB GPU, assuming that any OPT size model is available?

* Table 3 should have been shown all the way till OPT 175B.

* Is ZO same as ZO-SGD? You are using both the terms.
* Comparison could have been performed with other techniques, if possible.

### Questions
See the comments above in the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper present to conduce CPU offloading for zero-order optimizer methods in LLM fine-tuning/post-training. The problem to solve is practical and useful. The implementation incorporating with Nvidia's Automatic Mixed Precision (AMP) is necessary and essential. The experiment results show good speedup compared with previous zero-order method as MeZO.

### Strengths
Paper presentation is good and logic flow is clear. 

Problem to solve is a good direction.

Auto-cast and AMP support is a good thing to have for CPU offloading scenarios.

### Weaknesses
My first major concern is, this paper seems not technical sound and may have misunderstanding in cuda and amp techniques:

In Figure 1, it is unfair and unreasonable to compare memory consumption of using Adam vs using SGD, since Adam offers higher model training quality in general compared with simple SGD. That is the reason why Adam is dominantly adopted in LLM world. Comparing optimizer without aligning on model quality is unfair. Please provide more comparison results on different optimizers and its convergence results

Additionally, how did the authors collect the memory usage size numbers for different optimizers on a 24GB mem size GPU? If empirically measured, how to measure memory usage size (e.g.,68870MB roughly 68GB) over GPU memory capacity (24GB)?

Also the paper's implementation is not practical and not sound. from line 295 to 305 on page 6, the authors describe sync between computation and offload H2D D2H mem data transfer is implemented by the authors with some **lock** mechanism. This is impractical and cuda already provided multiple data transfer and compute sync techniques. For example, for memcpy specifically, it can be async or sync, by forcing it to be synchronized memcpy, there is no need at all to use any extra **lock** developed by the authors. For more generally multi-stream sync, cuda offers plenty of synchronization methods at stream/event/block/thread level. Usually, it is unnecessary to build new wheels without leveraging existing more efficient functionality. Please illustrate more on why a customized lock mechanism is needed here.

Further, by looking at supplementary materials, on page 16 line 812, the author reports using pytorch **3.11**. As far as I know, pytorch has not have any **3.x** version yet. I think authors may not familiar with the basic framework as well. Even assuming it is a typo, the only pytorch version cover number **11** is version **1.11.0**, which is quite old and experiment numbers based on this pytorch version seems a bit outdated and unconvincing. Please discuss more on which pytorch version is selected and why.

My second concern is about paper motivation, zero-order methods are not widely used for real large model training, as it is widely agreed these kind of gradient estimation methods could lead to model divergence. Please provide more citations or example applications on how zero-order methods is adopted in real world model training.

My third concern is paper novelty. Overall the paper's system design and implementation are very similar to zero-offload (https://arxiv.org/pdf/2101.06840) case (e.g. overlap data memcpy with computation as sec 5.1, dedicated memory block reuse and mem management as sec 5.2, AMP support as sec 5.4 which is by default supported in zero-offload code inside deepspeed).

Although sec 5.5 briefly discussed extension to async checkpointing seems novel, it mentioned async checkpoint without interfere training pipeline, this kind of idea already have much more solid design and implementation such as checkfreq, check-n-run

CheckFreq: Frequent, Fine-Grained DNN Checkpointing, FAST'21

Check-N-Run: a Checkpointing System for Training Deep Learning Recommendation Models, NSDI'22

Please provide a more detailed comparison of this zo-offload approach with zero-offload and other related works, highlighting specific novel aspects of this method.

My fourth concern is evaluation, it only reports simple throughput or token per sec results, without reports any model convergence/accuracy tests compared with more widely adopted first order methods. Could you include convergence comparison with first order methods?

some minor issues:
1. for figure 5a 5b mentioned in introduction, it would be great to cover them in main text Not appendix because these figures are essential for reader to understand main difference between first order and zero order methods.
2. Figure 3 and 4 seems 90% identical, maybe merge into 1 figure and highlight which part is new for AMP support. 
3. For a more uniformed paper structure and shape, it is better to only describe and illustrate a few major contributions rather than extending methods to multiple minor ones (e.g. extending to async checkpoint).

### Questions
1. regarding to paper novelty, what big/major LLM model is pre-train/post-train using zero-order optimization methods?

2. For system design and implementation, how it different from zero-offload?

3. how higher memory usage (e.g, 68870MB) profiling is conducted with 24GB memory GPU?

### Soundness
1

### Presentation
2

### Contribution
2
