# Elastic and Balanced End-to-end Training of Dynamic LLMs with DynMo

- Decision: Reject
- Scores: 5, 8, 5, 3

## Abstract
To reduce the computational and memory costs of Large Language Models (LLMs), schemes that introduce dynamic training are increasingly emerging. Examples of dynamic models are: a) Mixture of Experts (MoEs) at which token routing affects the compute balance, b) gradual pruning of the parameters of a model, c) dynamically freezing layers, d) dynamic sparse attention schemes, e) early exit of tokens as they pass through the model layers, and f) Mixture of Depths (MoDs) schemes where tokens bypass blocks. One side effect that limits the practical value of dynamic models is the introduction of workload imbalance among workers, which in turn negatively affects the efficiency in distributed training. We propose a dynamic load balancing solution DynMo), with a proof that it satisfies maximum reduction in imbalance, to adaptively maintain equal compute workloads among different workers in pipeline parallelism. In addition, DynMo dynamically packs work into fewer workers, while sustaining training throughput, to release the idle workers back to the job manager. DynMo supports both single nodes with multi-GPUs and systems with multi-GPU multi-nodes. In comparison to static distributed training solutions (Megatron-LM and DeepSpeed), DynMo accelerates the end-to-end training of dynamic GPT models by up to 1.23x (MoEs), 3.18x (parameter pruning), 2.23x (layer freezing), 4.02x (sparse attention), 4.52x (early exit), and 1.17x (MoDs). DynMo is available at https://anonymous.4open.science/r/DynMo-4D04/.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
To address workload imbalance in LLM training, this paper proposed a method to redistribute the workload. It composes well with dynamoc training technics including MoE/MoD, parameter pruning, layer freezing, and early exit. As workload shrinks, DynMo can pack work into fewer works and release idle workers for better GPU utilization. 

In terms of redistribution overhead, the author shows that it's <10% of the training QPS, including profiling, making decision, and actual data transfer

### Strengths
a) open sourced: the proposed method is open sourced and is built on top of megatron. The instructions are clear and easy to follow
b) covers critical details: it explained how to overcome the fact that each gpu can only have 1 NCCL communicator. These are practical challenges we need to resolve to truly reuse the idle worker

### Weaknesses
a) it remains unclear how resouce are isolated for safty purpose. For example, if NCCL communicator are shared, how could we make sure main job are safe as 3rd party job can do intentionally use it for other purpose.
b) the imbalance detection overhead is proportional to profiling frequency and is highly empirical. The claim of single digit overhead is up to a specific job setting

### Questions
When repacking jobs into fewer workers, what are things we are serializing? Are they model states and optimizer states? Do all the workers stop at the same time and start repacking? How do we deal with NCCL timeout if some rank are faster?

When consolidating profiler results, how to measure the imbalance among different workers? If the imbalance is caused by a straggler rank, how do we deal with it?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel dynamic load balancing solution (DynMo) designed to address the computational and memory challenges associated with Large Language Models (LLMs). The authors identify that dynamic training schemes, such as Mixture of Experts (MoEs), parameter pruning, layer freezing, dynamic sparse attention, early exit strategies, and Mixture of Depths (MoDs), can lead to workload imbalance among workers in distributed training environments, negatively impacting efficiency.

The primary contributions of this paper are as follows:
1. A dynamic load balancing framework that adaptively maintains equal compute workloads among different workers in pipeline parallelism, ensuring balanced pipeline stages during training.
2. This paper provides a proof that DynMo satisfies the maximum reduction in imbalance, effectively mitigating the negative effects of dynamic models on pipeline utilization.
3. DynMo dynamically packs work into fewer workers while sustaining training throughput, allowing for the release of idle workers back to the job manager, which can lead to cost savings and improved resource utilization.

### Strengths
1. The authors have identified and formulated the problem of workload imbalance in dynamic LLMs, which is a relatively unexplored area. The formulation of this problem and the proposed solution are original contributions to the field.
2. This paper provides mathematical proofs that DynMo satisfies maximum reduction in imbalance, which adds a strong theoretical foundation to the work.
3. The framework's compatibility with various dynamic compute and model reduction schemes suggests that it could be widely adopted across different domains and models, increasing its significance.

### Weaknesses
As the author said in section 3.6, this paper only focuses on the end-to-end training problem of dynamic LLMs, and the proposed DynMo framework and method are only applicable to dynamic LLMs. In addition, the method proposed in this paper cannot automatically detect imbalance and must be manually configured by the user before training begins.

### Questions
I think the contribution of this paper is valuable and universal, so I suggest that the author can explain how their idea can be applied in an automated framework in the future, or even integrate it into existing mainstream frameworks.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
DYNMO is a load-balancing system for dynamic models where the loads of the workers change during training. DYNMO provides better load balance than state-of-the-art static load balancing approaches, which results in better efficiency and faster end-to-end training time. DYNMO implements two load balancing algorithms built on top of DeepSpeed’s load balancing utility functions. The first is centralized parameter-based partitioning and the second algorithm is an iterative decentralized diffusion-based algorithm. Empirical results for LLMs with 6 example cases of dynamic models show that DYNMO significantly improves the training throughput over the counterparts.

### Strengths
Thank you for submitting this paper to ICLR! 

1. Comprehensive evaluation. The study presents an extensive evaluation conducted on a large-scale GPU cluster with hudreds of H100 GPUs. This rigorous assessment demonstrates the scalability and effectiveness of the proposed approach.

2. Provide source code repository. This resource not only facilitates the replication of the presented results but also empowers others to leverage the system for improved training times through dynamic techniques.

3. Interesting topic. This paper addresses a issue involving the integration of pipeline parallelism with dynamic pruning and freezing.

### Weaknesses
1. Limited Technical Innovation: The technical contribution of the paper is somewhat restricted, as it relies on the application of established techniques in a novel context rather than introducing entirely new methodologies. 

2. Unclear algorithm descriptions: The second algorithm is an iterative decentralized diffusion-based algorithm. For the "diffusion", it is not clear how the diffusion is performed. The paper should provide a more intuitive example / explanation of the algorithm.

3. Omission of a Dynamic Baseline Configure: I think Megatron and Deepspeed are also support some naive dynamic baseline configure (manually). The paper should compare with them as a stronger baseline.

### Questions
As a training framework, it is a bit wired to support elastic (I mean reduce GPU amount). Most work discusses fault-tolerance for LLM-pretraining (e.g., Gemini [SOSP '23], ReCycle [SOSP '24]). In other words, it is important to demonstrate the wide requirement of dynamic training (e.g., layer freezing).

1. I highly recommend changing the story to cluster-level scheduler instead of a training framework. It makes sense to automatically reduce some resources when some layer is freeze. Other jobs can better utilize the resource.

2. The experiment is solid, but if I focus on MoE training case, I want to see some comparison with MoE-tailored system like Tutel https://github.com/microsoft/tutel

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper discusses how to reduce the load imbalance during dynamic model training. Dynamic training is emerging to reduce the computational and memory costs of LLMs. However, it leads to workload imbalance among workers, which negatively affects training efficiency. This paper proposes DynMo that adaptively maintains equal compute workloads among workers in pipeline parallelism as well as packs work into fewer workers. The evaluation with six different example cases of dynamic models demonstrates the effectiveness of DynMo.

### Strengths
+ This paper discovers load imbalance in six example cases of dynamic training and measures their bubble ratios with pipeline parallelism.
+ The extensive evaluation shows DynMo can greatly reduce the bubble ratios and improve the end-to-end training efficiency without harming model accuracy.
+ The paper uses a production-level cluster for the evaluations

### Weaknesses
 - The paper writing needs to be improved. 1/ Load imbalance is a major motivation for this paper, but there is no formal definition in the paper; 2/ This paper identifies six example cases for load imbalance, but it is unclear why these dynamic model training leads to load imbalance and worsens communication bubbles. More fundamental analysis is needed to understand the problem. Specifically, the paper lacks a clear explanation of the underlying mechanisms that cause the observed load imbalances in dynamic models. For instance, it is not clear how specific dynamic behaviors like conditional computation or adaptive layer skipping translate into uneven computational loads across workers in a pipeline parallel setup. The paper should delve deeper into the root causes, perhaps by analyzing the variance in execution time of different model components or by providing a theoretical model that explains the observed imbalances.
- The two algorithms introduced in Section 3.3 are not convincing to achieve the claimed goal for optimal load balancing. The paper presents the algorithms without sufficient justification for why they should converge to an optimal solution. The description lacks a clear explanation of how the algorithms handle the complexities of dynamic model execution, such as varying computational costs of different model parts. Furthermore, the detailed description of this critical algorithm is not included in the main body, but in the appendix. At least some intuitions for why it can achieve load balancing should be discussed in Section 3. The lack of a clear explanation in the main body makes it difficult to assess the validity and practicality of the proposed approach.
- From a system perspective, re-packing dynamic models to fewer workers requires to reshard the model checkpoint, recompute the graph, and restart the training process, which will incur costly overhead up to several minutes for LLMs. However, this paper claims the overhead of DynMo is negligible, without discussing how it minimizes these incurred system overheads. The paper needs to provide a detailed analysis of the overhead associated with re-packing, including the time required for checkpoint resharding, graph recomputation, and training restart. It should also discuss how the frequency of re-packing is determined and how it balances the benefits of reduced worker count against the overhead of the re-packing process. A more thorough discussion of the implementation details and the system-level challenges is necessary for a complete evaluation of the proposed method. I think an implementation section is needed for fidelity.

### Questions
N/A

### Soundness
2

### Presentation
1

### Contribution
2
