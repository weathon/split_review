# MAGE: Leveraging LLMs for Automated Mapper Generation in Parallel Programming

- Decision: Reject
- Scores: 6, 6, 3, 5

## Abstract
Efficiently mapping tasks to processors and data to memories is a cornerstone of parallel programming to achieve high performance. Traditionally, this critical task has been handled by expert-crafted mapper programs, tailored for specific machine architectures and problem domains. However, creating customized mappers for each unique application is labor-intensive and time-consuming. Large language models (LLMs) have recently demonstrated remarkable capabilities in understanding and generating code, as well as in self-improvement for optimizing specific performance metrics. Inspired by these advancements, we introduce the task of mapper generation (MAGE), which frames generating high-performance mappers as a discrete optimization problem aimed at maximizing compute throughput. To solve this optimization problem, we leverage reinforcement learning (RL) to guide LLMs in the mapper generation process. At the core of our approach lies a novel domain-specific language (DSL), which provides a high-level interface for LLMs to generate the mapper code without getting entangled with complicated, low-level system programming. Moreover, our DSL defines a structured and constrained search space for RL to explore, guiding LLMs to discover the optimal mapping policy. The evaluation shows that our LLM-generated mappers can surpass expert-written mappers in performance, achieving up to 34% speedup across 9 benchmarks. Notably, our approach improves the throughput of parallel matrix multiplication algorithms by up to 31%, reducing development time from several days to just a few minutes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new automated mapper generation framework (MAGE) that utilizes large language models (LLMs) and a domain-specific language (DSL) to generate efficient mappers. The research aims to address the high costs and time consumption associated with manually crafting traditional mappers. By introducing reinforcement learning (RL), the paper demonstrates that the generated mappers can significantly improve performance in multiple benchmark tests compared to expert-written mappers, achieving up to 34% acceleration and improve the throughput of parallel matrix multiplication algorithms by up to 31%, reducing development time from several days to just a few minutes.

### Strengths
1. The introduction of the DSL simplifies the complexity of mapper generation and improves the efficiency of the generation process.

2. The reinforcement learning feedback mechanism enhances the performance optimization capabilities of the mappers.

3. Experimental results show that the generated mappers outperform expert-written mappers in terms of performance, validating the effectiveness of the proposed method.

### Weaknesses
1. Limited Experimental Scope:

   In Section 5, the authors primarily focus on benchmarks such as "circuit simulation," "stencil computation," and "Pennant." The selection of these applications is relatively narrow and lacks testing across other types of parallel computing tasks. Failing to cover a broader range of application scenarios may limit the generalizability and reliability of the proposed method.

2. Insufficient Discussion on Mapping Strategy Selection

   Although the authors propose the generation of multiple mapping strategies, Section 4.2 lacks a thorough analysis of the specific impacts of different strategy choices. For example, when discussing decisions such as "task selection" or "memory allocation," there is no exploration of how these decisions may affect final performance in various scenarios.

3. Lack of Discussion on Failure Cases

   In Section 5, while the authors present successful cases, there is minimal discussion regarding instances where the generated mappers failed in certain tests. The authors do not provide an analysis of the reasons for these failures, which is a significant oversight. Understanding the failure modes could offer valuable insights into the limitations of the proposed method and help identify areas for improvement. This lack of analysis may lead to an incomplete understanding of the robustness and reliability of the mapper generation approach in practical applications.

### Questions
1. In Section 4, the authors introduce the DSL designed for mapper generation. The text states that "By providing a higher-level abstraction than C++ APIs, the DSL simplifies interfacing with LLMs," but it does not elaborate on how this abstraction specifically addresses the complexities of C++ APIs and low-level details. Additionally, there is no discussion about whether using this DSL results in the loss of low-level details inherent to C++, which could be crucial for performance optimization and effective resource management. With such a high level of abstraction, will using the DSL result in the loss of low-level C++ details?

2. In Figure 7(c), the Perf+Err line and the Full Feedback Mode line exhibit alternating performance increases over 10 iterations. Is there a need for more iterations to ensure that the Full Feedback Mode consistently outperforms the others?

3. In Figure 7, the error explanation is provided when errors occur due to inappropriate mapping decisions or syntax errors. Why do such explanations have a significant impact on the final throughput results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed a new DSL to describe/map parallel programming (e.g., to various processors and physical memories) and demonstrated the high-level interface/model makes it efficient for LLM based agents to optimize the codegen of this DSL that reaches expert crafted mappings.

### Strengths
* The introduction of a new DSL for LLM to codegen and optimize is intuitive and efficient. LLMs currently are not good at codegen system level compiled languages like C++ (due to lack of context and hallucination) but good at instruction-following structured (and syntax restricted) problems (e.g, math and function-level coding), A DSL significantly regularize the outputs of LLMs

* The use of agentic workflow to automate the iteration and tuning of performant codegen is efficient in catching up with human expert level performance in a much less time/effort

* The experiments and ablation studies make it qualitatively clear DSL is helpful making the codegen functional and the agentic discrete optimization makes it performant

### Weaknesses
 * The writing can be a bit more verbose, e.g.,:
  - IIUC, the parallel programming is at task/processors level instead of kernel (e.g., CUDA) level, if so it might be worth pointing out earlier in the context (e.g., when people see matrix multiply or GEMM optimization, it is easy to think of kernel instead of distributed GEMM at first impression)
  - The use of "RL" tends to lead people to think of gradient-descent based RL algo instead of agentic based RL flow, a couple explanations in the early context would be helpful to setup the overall pictures

* Ablation study of feedback. The baseline already has performance feedback provided to the agent, a more foundamental baseline IMO would be single or few shot prompting before adapting an agentic flow

### Questions
* Is it possible for LLM to discover new GEMM algorithms given target machines, input sizes etc instead of given the algorithms, find the index mapping of iteration/device space as shown in section 5.3?

* IIUC, the index mapping is basically "sharding" in distributed ML frameworks (e.g, Tensor Parallellisms), is it possible to generalize the ideas to automate sharding in a distributed system?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces MAGE, a reinforcement learning-based generator for task mappers, designed to allocate tasks to various devices in distributed environments. The key idea is to propose a domain-specific language (DSL) to represent the mapping strategy, using large language models (LLMs) to produce mapping code in this DSL. Experimental results show that this approach achieves a higher success rate for generating correct mappers and better performance across different benchmarks.

### Strengths
1. Proposed a concise DSL representing the task mapping strategies, enabling LLMs to generate valid programs.
2. Used LLM as a heuristic to propose new mapping strategies in a reinforcement learning pipeline.

### Weaknesses
1. The work does not introduce new techniques; incorporating an LLM into an existing reinforcement learning framework does not appear to be a novel contribution.
2. There is insufficient insight or evidence explaining why the proposed DSL is well-suited for task mapping representation or LLM generation. The necessity of specific statements and the grammar structure in Figure 3(a) are not clearly explained. The DSL's design choices, such as the specific keywords and the hierarchical structure, lack justification in terms of their impact on the LLM's ability to generate effective mappings. The paper does not explore alternative DSL designs or provide a comparative analysis to demonstrate the superiority of the chosen approach.
3. Evaluations are limited to simple benchmarks, lacking experiments on realistic applications like device placement for deep learning model training. The benchmarks, while involving multiple kernels, do not represent the complexity of real-world distributed applications. The paper lacks a discussion on how the proposed method would scale to larger, more complex applications with intricate communication patterns, such as those found in distributed deep learning.
4. The correctness of task mappings is not discussed. Some mappings may require inter-device communication to ensure final results' accuracy. The paper assumes that the underlying runtime will handle all communication, which may not be the case in all distributed environments. The lack of explicit correctness guarantees for the LLM-generated mappers is a significant concern, especially given the potential for subtle errors in distributed systems.

### Questions
1. Why is the proposed DSL well-suited for representing task mapping? What is the rationale for the statements in Section 3, and why is the grammar structured as shown in Figure 3(a)?
2. Why does the proposed DSL improve LLM generation? Are there fundamental limitations when using LLMs to generate C++ code? Given that LLMs are typically trained on widely-used languages like C++, might they perform better with more C++ examples in the prompt or constraints to prevent invalid variable names? Alternatively, using a template with fill-in-the-blank prompts in C++ could improve success rates. Thus, the experiments in Section 5.1 don’t entirely prove the DSL’s effectiveness or necessity.
3. Can the two errors shown in Table 1 for your DSL be avoided by improving the prompt?
4. "Mappers do not change the correctness of an application's output; they only affect its performance." This statement may be inaccurate—some mapping strategies require device communication to ensure correctness (e.g., tensor parallelism in Transformer training). How do you verify that the LLM-generated mapper is correct? Are there any formal guarantees? Are communication operations (e.g., all_reduce) handled afterward?
5. One advantage of DSLs is abstracting away low-level parallelization details to generalize across different backends. Is your DSL general enough to apply parallel strategies to other frameworks, like TaskFlow [A]? How much effort is required to support frameworks other than Legion? Would your DSL need adjustments?
6. "Experiments are conducted on a GPU cluster ..." How many GPU nodes were used?
7. Does the underlying hardware affect mapping strategies? For example, if A100 GPUs were used instead of P100s, would the RL pipeline need to be rerun?
8. Can your approach apply to distributed LLM training, and how do the generated task mapping strategies compare with Alpa [B]?
9. Some early RL-based task mappers [C] are not discussed. Could you explain why including LLMs produces better results? Could your method handle the experiments presented in [C]?

[A] Tsung-Wei Huang, Dian-Lun Lin, Chun-Xun Lin, Yibo Lin, "Taskflow: A Lightweight Parallel and Heterogeneous Task Graph Computing System", IEEE Transactions on Parallel and Distributed Systems (TPDS), 2021.

[B] Lianmin Zheng, Zhuohan Li, Hao Zhang, Yonghao Zhuang, Zhifeng Chen, Yanping Huang, Yida Wang, Yuanzhong Xu, Danyang Zhuo, Eric P. Xing, Joseph E. Gonzalez, Ion Stoica, "Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning", OSDI, 2022.

[C] Azalia Mirhoseini, Hieu Pham, Quoc Le, Mohammad Norouzi, Samy Bengio, Benoit Steiner, Yuefeng Zhou, Naveen Kumar, Rasmus Larsen, Jeff Dean, "Device Placement Optimization with Reinforcement Learning", ICML, 2017.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach to finding the right mapping strategy to map parallel tasks onto processors and memory. The idea is to describe the mapping strategy and tuning parameters like data layouts and memory placement in a domain-specific language (DSL) and then ask LLM to generate a mapping plan in the DSL. The proposed approach uses reinforcement learning to drive the LLM code generation process to provide feedback for the LLM (GPT-40) to improve the correctness of the generated code. The proposed approach was evaluated on a CPU-GPU system using selected HPC workloads. Experimental results show that the proposed approach can match or exceed the performance given by an expert-crafted mapper.

### Strengths
This paper provides an interesting study of the use of LLMs to generate high-level code for parallel mapping.

The paper is, in general, easy to follow. 

Some interesting results were presented.

### Weaknesses
The overall approach appears unnecessarily complex for the problem to be solved. For example, the proposed method requires using a DSL to describe the optimization space, which is likely to be dependent on the specific program being optimized. This, thus, increases engineering overhead and prevents adoption. Additionally, given that only a small set of parameters (processor type, data placement, and data layout) are found to be crucial, why not simply expose these as tunable parameters for classical parameter tuning algorithms? Well-established frameworks like OpenTuner and CompilerGym are designed for performance parameter tuning and could be used for the same purpose.

Similarly, while it may be interesting to test the LLM's capability to generate high-level DSL code, this does not seem to be the right problem for LLMs. The idea of using LLMs to generate a DSL that is then mapped to C/C++ code seems overly complicated and unnecessary.

The evaluation is weak and lacks important details. For example, only three applications were used, but how were these applications implemented? Are they CUDA applications? What CUDA driver and CPU were used in the evaluation? Additionally, why were well-established GPU benchmark suites like Parboil and Rodinia not considered?

### Questions
Does the decision procedure described in Figure 4a depend on the program to be optimized? In other words, how general is the decision procedure? 

Why not just expose the parameters to a tuning framework? Can you provide a direct comparison?

Why were only three benchmarks used in the evaluation, and how were they implemented? 

Please provide details of your evaluation platforms.

### Soundness
3

### Presentation
3

### Contribution
2
