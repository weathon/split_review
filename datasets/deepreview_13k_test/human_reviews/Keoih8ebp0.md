# BAP: BRANCH-AWARE PARALLEL EXECUTION FOR FASTER DNN INFERENCE ON MOBILE CPUS

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
The growing demand for real-time applications on edge devices underscores the need for faster inference of complex deep neural network (DNN) models. Although mobile devices increasingly incorporate specialized processors like GPUs and TPUs, modern DNN models such as Whisper and Vision Transformers often involve dynamic control flows and tensor operations that are incompatible and unsupported on current frameworks with these mobile accelerators. CPU presents the most viable option to improve inference latency on mobile devices due to their widespread availability, substantial memory caches, and ability to support all types of tensor operations. However, existing CPU optimization techniques focus on sequential execution, overlooking potential parallelization within Automatic Speech Recognition (ASR) and transformer-based models, leading to inefficiencies. This work introduces a novel runtime model analysis pipeline that extracts layer and branch structures from DNN model graphs to identify parallelizable branches. We propose BAP, a branch-aware memory allocation strategy that isolates memory arenas for parallel branches, reducing contention and optimizing memory reuse within each branch. Additionally, we leverage CPU multithreading to execute these branches concurrently, optimizing thread management and memory access to minimize overhead. Evaluated on ASR models and transformer-based models, our approach reduces inference latency by up to 38.5%, decreases memory allocation requirements by up to 15.6x and saves up to 20.2% energy cost compared to the TFLite naive memory allocation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents BAP, a method to enhance neural network inference on mobile CPUs for models with multi-branch structures. BAP implements a branch-aware memory allocation strategy that isolates memory arenas for parallel branches, thereby improving cache locality and reducing memory overhead. Evaluated on ASR and transformer-based models, BAP achieves up to 38.5% reduction in inference latency, decreases memory allocation requirements by as much as 15.6×, and cuts energy consumption by up to 20.2% compared to the TFLite default memory allocator.

### Strengths
+ This work identifies the potential of parallel execution to improve the performance of models with multi-branch structures. 
+ The authors address critical challenges, such as dynamic allocation and operator reordering, which arise with parallel execution. 
+ Multiple evaluation metrics—latency, memory usage, and power consumption—are used to comprehensively demonstrate BAP's benefits.

### Weaknesses
- Adding figures to illustrate the multi-branch and dynamic properties of existing neural networks would improve clarity.
- Providing an overview of CPU and GPU computing capabilities would help emphasize the need for CPU-specific optimizations, or clarify why other processors are less suited for the targeted issues.
- The comparison is limited to TFLite; incorporating recent benchmarks such as operator reordering [1] would provide a stronger baseline.
[1] Liberis, Edgar, and Nicholas D. Lane. "Neural networks on microcontrollers: saving memory at inference via operator reordering." arXiv preprint arXiv:1910.05110 (2019).

### Questions
The work would benefit from additional data and explanations to clarify its contributions and significance. Key questions and concerns include: 
1. How does BAP improve cache locality, as mentioned in the abstract? 
2. What percentage of operators, or computational workload, can be parallelized effectively by this approach?
3. What is the quantified benefit of parallel versus sequential execution across different models? 
4. How does BAP address workload imbalance among branches? This explanation could be refined.
5. Many mobile CPUs now use asymmetric core designs—has this hardware feature been considered in the proposed solution?

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
3

### Summary
* The paper examines the challenges of executing models that require dynamic control flows on specialized processors and presents optimizations for executing these models on CPUs for edge devices.
* The paper proposes a branch-aware memory allocation policy (BAP), which improves memory utilization and facilitates efficient parallelization of the model, reducing the latency of DNN models.
* The paper presents results demonstrating the effectiveness of the BAP algorithm.

### Strengths
* The paper addresses a significant challenge for edge devices and employs a practical approach for implementing the solution, using TFLite as the foundational code. This choice enhances the potential for widespread adoption of the solution.

### Weaknesses
* Although the paper addresses an important problem and includes testing across multiple devices, some sections require rewriting to clearly highlight the contributions and provide sufficient supporting evidence. The major contributions of the paper, as presented in lines 85-91 (with inlined feedback), are:

> * We introduce BAP, a CPU-specific optimization system designed for ASR and transformer-based models with dynamic control flows and tensor operations.  
>> It is not clear if this point includes the other two points. Does this refer to multithreading optimization? It is not clear, and I recommend rephrasing this to present the contribution more explicitly.

> * We develop a novel branch-aware memory allocation strategy that minimizes memory conflicts and optimizes cache usage by isolating memory arenas for parallel branches.  
>> * The term "memory conflict" is unclear and is not discussed in detail within the paper. Additionally, there is no result presenting evidence related to cache optimization.

> * BAP significantly reduces latency, memory usage, and energy consumption without requiring model refactoring, making it practical for real-time inference on mobile edge devices.  
>> * This point overlaps significantly with the above points. Please rephrase the contributions to more clearly differentiate the primary contributions.

* The paper can benefit by improving formal sections of the paper. E.g.
  * Line 176-179: "A branch b, or subgraph S, is a set of sequentially connected nodes { v1,v2,...,vk} within a layer.  A subgraph may have multiple inputs or outputs, but within the subgraph, the nodes are strictly connected in a sequential manner. This ensures that each subgraph can be executed independently of others within the same layer, provided there are no inter-branch dependencies." 
  > * Is the term branch synonymous with subgraph? If so, using a consistent term could enhance readability.
  > * Last part "provided there are no inter-branch dependencies." looks redundant by the definition, in case of misunderstanding, please describe the cases it covers. 
  * In algorithm 1, line 15-24, please add a condition when a node is marked as visited. 

* For the results section, it will be helpful to provide more details about baseline. There are many implementations of vendor-specific Tflite  delegates e.g. [1] [2] and other frameworks for CPU execution. Kindly add a strong justification of using TFlite default implementation as the baseline. Further,
> Line 354-358: "While we compared allocation memory efficiency against both plans, we focused on comparing other aspects like latency and energy consumption against the first, as it represents TFLite’s optimal performance.  Also, we did not include methods like CoDL or NN-Stretch, as they mainly focus on DNNs without dynamic control flows and rely on heterogeneous processor co-execution. In this case, the TFLite runtime remains the SOTA for CPU-only execution."
>> It is not clear TFLite runtime as been described as SOTA for "allocation memory efficiency" or latency. Please provide an appropriate reference for the same.

* There is a lack of clarity on the TFlite's capability that is considered as baseline based on following lines.
Lines 375-377: Although TFLite also utilizes multi-core processing, its multithreading support for floating-point models remains limited. Specifically, TFLite’s parallelization is constrained to certain operations, leaving much of the computation serialized and diminishing its ability to fully capitalize on multi-core architectures"
> Does the TFLite implementation used in the experiment support multithreading? This is crucial for understanding whether the observed latency improvement should be attributed to "parallel vs sequential execution" or to enhanced parallelization due to the BAP algorithm.

[1] https://github.com/ARM-software/armnn

[2] https://www.qualcomm.com/developer/blog/2020/11/tensorflow-lite-inference-edge

### Questions
Please review my comments in "weakness" section. The same may be due to lack of understanding.

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
The authors propose BAP that aims at improving runtime performance of DNN models on CPU devices. They achieve this by categorizing nodes in the DNN graph into sequential nodes, which can be grouped into a set for parallelism, and branch nodes, which defines the "set boundaries". The sets are then top-sorted to resolve dependencies. The authors also considered memory allocation and thread management during parallel execution to resolve potential memory conflicts and minimize multi-threading overhead. They evaluated their proposed algorithms with several open-source ASR and image recognition models on several hardware. For the metrics they are concerned (latency, memory usage, power), the proposed algorithm outperforms their chosen baselines in several aspects.

### Strengths
The paper is well-written and easy to follow. References to figures and tables are adequate. The idea is moderately novel: increase parallelism in model inference for CPU execution.  The empirical results, though lacking in some aspects, are supportive of their hypothesis. However, I am less confidence about its relevance to the industry as devices with GPUs become more prevalent. As models gets larger, it's hard to imagine running them without GPUs. Smaller models, according to the paper, show less gain with or without parallelism on CPUs.

### Weaknesses
The evaluation using only 10 small images and 5 short audio samples repeated five run is a bit inadequate. I'd encourage the authors to also include long audio samples too. Based on the argument of the paper, longer audios should even exemplify the advantage of the algorithm. 
The authors can also improve the analysis in Section 4.3.3. by developing  relationships between the percentage of sequential nodes and the various performance metrics. Is it expected that higher percentage of sequential nodes lead to better performance? This could also lead to model design that is targeted for CPU devices. 
Also please share the code base if possible.

### Questions
While running large models on CPU is an option, I wonder whether it is a viable option, hence its relevance. Many high-end devices come with GPU-like units nowadays, what's the scenario when we need to fall back to CPU? Maybe smaller models that do not wish to compete with large models, like a wake up detector? In that case, are there any other model inference acceleration targeting CPU that should be compared with? 
Also how does the algorithm compare with GPU/TPU execution? Can it be a reliable fallback when GPUs get too busy?
Another aspect I'm interested in is how many other processes there were running on the CPUs when the measurements are taken. Does existing CPU usage affect the usage in any way?

### Soundness
4

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
3

### Summary
Deep neural networks are widely deployed on edge devices like mobile phones to serve the users on many different tasks, thus it is important to reduce its latency and engergy consumption. Existing works focus on sequential execution of the layers on mobile devices. The authors of this paper propose to parallelize independent branches of a model to acceleate the execution. Experiments show that the proposed method could achieve up to 38.5% speedup.

### Strengths
1. Enable the parallel execution of independent branches of deep nerual networks on mobile devices.
2. Experiments show that the proposed framework could achieve up to 38.5% speedup compard with the widely used inference library tflite on mobile platforms.

### Weaknesses
1. Scientific novelty is limited, this contribution of this work is more on the engineering side.
2. More ablation study is needed.

See below for more details.

### Questions
1. Scientific novelty is limited, this work is more like a good engineering work.
There are a bunch of works [1, 2, 3, 4] that have studied the parallel execution of the independent branches of deep nerual networks on CPUs or GPUs. The schedule (how to group the branches for execution) proposed by this paper is a kind of greedy schedule that also has been widely studied. Thus, the contribution of this work lies more on the enginnering side from my perspective. Could you provide more comparison with the schedule used in this paper vs. the schedules used in prior works?

- [1] Scheduling Computation Graphs of Deep Learning Models on Manycore CPUs
- [2] Rammer: Enabling Holistic Deep Learning Compiler Optimizations with rTasks
- [3] IOS: Inter-Operator Scheduler for CNN Acceleration
- [4] Nimble: Lightweight and Parallel GPU Task Scheduling for Deep Learning

2. More ablation study is needed.
Since each single operator (like matrix multiplication and convolution) can also be parallelized among the mobile CPU cores. More abation study is recommended to show that the intra-operator parallelism is not enough to fully utilize the mobile CPU cores. From the Table 3, we can see that BAP can achieve 2~3x speedup when there are many branches in the model. Could you provide more profiling results to show that why the sequential execution can not saturate the mobile CPUs? Potential reasons are: 1) the workloads are too small for the powerful mobile CPUs, 2) the kernel implementation in sequential execution is not efficient to use multiple cores, 3) the sequential execution is bottlenecked by some resources (like DRAM bandwidth, computation units, etc) and parallelizing branches would alliviate this problem.

### Soundness
2

### Presentation
2

### Contribution
2
