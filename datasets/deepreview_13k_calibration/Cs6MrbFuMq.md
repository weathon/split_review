# HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Disaggregating the prefill and decoding phases represents an effective new paradigm for generative inference of large language models (LLM). This approach offers some significant system advantages, such as eliminating prefill-decoding interference and optimizing resource allocation. However, it is still an challenging open problem about how to deploy the disaggregated inference paradigm across a group of heterogeneous GPUs, which can be an economic alternative of the deployment over the homogeneous high performance GPUs.
Towards this end, we introduce HexGen-2, a distributed system for high throughput and cost-efficient LLM serving on heterogeneous GPUs following the disaggragated paradigm. Built on top of HexGen, the core component of HexGen-2 is a sophisticated scheduling algorithm that formalizes the allocation of disaggregated LLM inference computations and communications over heterogeneous GPUs and network connections as a constraint optimization problem. We leverage the graph partitioning and max-flow algorithm to co-optimize resource allocation, parallel strategies for distinct inference phases, and the efficiency of inter-phase key-value (KV) cache communications. We conduct extensive experiments to evaluate HexGen-2, i.e., on OPT (30B) and Llama-2 (70B) models in various real-world settings, the results reveal that HexGen-2 delivers up to a 2.0$\times$ and on average a 1.3$\times$ improvement in serving throughput, reduces the average inference latency by 1.5$\times$ compared with state-of-the-art systems given the same price budget, and achieves comparable inference performance with a 30% lower price budget.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the disaggregated LLM servings into the heterogeneous environment. The deployment is formulated as an optimization problem, a graph max flow problem. Results show improvement compared to the homogeneous methods.

### Strengths
- The idea of scheduling among heterogeneous GPUs is intuitive. And the design provides insights. Using graph partitioning and modeling the query processing as max-flow problem is valid.

- The paper is well-written and generally easy to follow.

### Weaknesses
 - Perhaps the paper can provide some analysis about the optimization problem.
  - Is there an upper bound of the performance (from the perspective of graph partitioning and max flow problem, respectively) your approach can reach? How is the performance your method achieves compared to this upper bound?

- The main contribution seems to be formulating the optimization problem while some parts of the solutions are not that new.

- Some details can be clarified in the paper.
  - Which GPU is used in Figure 1?
  - What is the outcome (objective) of the graph partitioning? How to determine which group is prefill group and which one is decoding group? Are the results optimal?
 
- Miscellaneous
  - carefully use \cite and \citep for citation.
  - Capitalize the first letter after the colon.

### Questions
See above.

### Soundness
3

### Presentation
3

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
The paper introduces HexGen2, a distributed LLM inference framework targeting heterogeneous GPU clusters. The framework disaggregates prefilling and decoding tasks onto different GPUs, ensuring that the two phases do not interfere with each other and that they can be parallelized in different ways when doing so is beneficial.

### Strengths
- LLM inference on heterogeneous GPUs is a critical and timely issue. Separating the prefill and decode stages when serving LLMs in diverse clusters represents a novel approach.
- Evaluation is thorough
- Very clear presentation

### Weaknesses
 - The evaluation does not include an ablation study that compares HexGen2's runtime with those of DistServe and HexGen. Understanding HexGen2's performance in terms of throughput and latency compared to DistServe and HexGen in a homogeneous setting would be valuable.
- In the introduction, the authors assert that disaggregated inference is the most efficient framework for serving large language models (LLMs) without providing proof or citations. Is this assertion already widely accepted by the community, or is there still an ongoing debate regarding the advantages of disaggregation versus chunked prefills? It would be beneficial for the authors to clarify this—at least in the related work section—and to explain their reasoning for choosing the disaggregation approach over chunked prefills.

### Questions
- Is HexGen2 built on an existing runtime, or was it developed from scratch? Specifically, how does HexGen2's runtime compare to those of DistServe and HexGen? Understanding this would be helpful for better assessing the end-to-end performance comparison with the other two frameworks.
- In the evaluation settings, could you explain your motivation for selecting a 70% lower budget as the target for the evaluation scenario? How did you arrive at this percentage?
- Do you have any insights or, preferably, evaluation data regarding which additional heterogeneous clusters HexGen2 would perform well with, besides those already evaluated? Does HexGen2 support any type of cluster, or are there specific restrictions regarding GPU types, interconnects, or CUDA architectures?

### Soundness
3

### Presentation
4

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
This paper presents HexGen-2, a framework designed for serving language models on heterogeneous clusters with disaggregating prefill and decode computation on different devices. HexGen-2 first used a multi-round partition to divide all devices into multiple groups, and then introduced a maxflow algorithm to decide how to dispatch and route the workload on each device partition.
The authors did experiments on 5 different heterogeneous clusters, as well as 4 different workload pattern. Results show that even under a lower price budget, HexGen-2 matches the performance of the state-of-the-art disaggregated serving platform, DistServe, if not surpassing.

### Strengths
- The paper is the first to combine disaggregated serving together with heterogeneous devices, which is an important direction. This enhances the paper's novelty.
- The approach of using Max-Flow to solve the scheduling problem is interesting and efficient.

### Weaknesses
 - The detail of the paper's method is not well motivated, neither well explained (to clarify physical node with abstract graph `nodes` in the algorithm, I use `this font` for abstract graph nodes):
  - In Graph Partition, the motivation of partitioning with two steps is not well explained. Specifically, it is confusing that why the first round minimizes the edge cost, while the second round maximizes the cost. Besides, why the `node` weight should be balanced (i.e., the computation capacity of each partition should be roughly the same)?
  - In Graph Partition, step 2, the concept of "partition" and "replica" causes confusion. Does each partitioning output group correspond to a replica? Is there multiple replicas for prefill, or only one replica for prefill, and one fore decide?
    - It seems to me that there are multiple prefill replicas (according to Max-Flow "for prefill model replicas, ..."). However, in this case, maximizing the total edge cost is not reasonable because the edges between prefill replicas are meaningless.
    - Does the algorithm consider the balance between node weights of (all) prefill replica(s) and that of (all) decode replica(s)? I think this is important because it avoids one part having too few devices to compute.
  - In Graph Partition, there is an input argument for the targeted group size $K$. How is this argument defined and set?
  - In Max-Flow, the author estimated the communication cost by dividing the total communication volume to the bandwidth. However, there exists a case that the bandwidth of some `node`s are shared, because these GPUs belong to the same physical node. On the other side, when both the send and receive side are on different physical nodes, the communication can be parallelized. Using the collective performance is not accurate.
  - In Max-Flow, the author mentioned that each "model replica" finds the optimal parallelism strategy themselves. Is this model replica inherited from Graph Partition? If so, what is the motivation of the projection?
  - In Max-Flow, what is the search space of the parallelism strategy? For example, when a model replica has two type of GPUs (e.g. one A100 and 4 V100), what is the parallelism strategy?
- The evaluation is not convincing to me. The baseline is too weak (see Question section for more details);

### Questions
Some questions that could help make the paper more clear is already mentioned in the Weakness section. In addition to that, there are some other concerns:
- According to Figure 4, the network topology is globally heterogeneous but locally homogeneous: to any destination device $u$, the bandwidth $(u_1,v),(u_2,v)$ from the same type of GPU $u_1$, $u_2$ is always the same. In this case, the Graph Partition algorithm seems an overkill to me: what if we consider to directly merge devices by the GPU types they belongs to, and then bipartition GPU types according to the inter-type bandwidth? Showing some nontrivial examples generated by HexGen-2 could also explain the importance of the graph partition algorithm.
- The context of serving with heterogeneous cluster lacks detailed introduction. As an important benchmark baseline, as well as the system that this work is built on top of, HexGen itself is not well introduced and explained. For example, the author mentioned the "genetic algorithm" in ablation study of scheduling algorithm but never explained it. Adding more detail to section 2 and 5 about the background of heterogeneous serving and the two specified baseline could help improve the paper's self-completeness.
- The benchmark baseline is too weak. On Llama-70B, vLLM, which does not even support disaggregation, reported a throughput of 25 req/s ($\approx$400 tok/s) on **4 H100-80GB** GPUs with the "prefill-heavy" workload (https://blog.vllm.ai/2024/09/05/perf-update.html). Given that their prefill token's average length is only around 400 tokens, I compare it with the "LPLD" benchmark: In this way, HexGen-2 uses 2x more budgets, but only with a maximum throughput around 550 (1.4x higher). Adding more experiments with state-of-the-art LLM serving platform for the homogeneous setup could better show the predominance of HexGen-2 against using homogeneous clusters with the same budget.

### Soundness
2

### Presentation
2

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
Traditional LLM serving frameworks co-locate the execution of prefill and decode stages, leading to prefill-decode interference.
Disaggregated inference is a more efficient LLM serving approach that reduces such interference and allows more flexible scheduling of the two stages.
This paper proposes HexGen-2, a disaggregated LLM inference framework that coordinates distributed LLM inference over a heterogeneous set of GPUs and network connections.
The core of HexGen-2 is a two-level scheduling algorithm that leverages graph partitioning and max-flow algorithm to determine the resource allocation and parallelization plan for the prefill and decode stage.
Evaluations have shown that HexGen-2 could achieve better serving throughput and lower average latency compared to SOTA works.

### Strengths
1. The problem of scheduling heterogeneous resources over disaggregated LLM inference makes sense.
2. The framework shows good improvement over prior works on serving throughput and latency.

### Weaknesses
1. Lack of intuition and lack of clear and detailed explanation for the core scheduling algorithm.
2. Did not compare the scheduling decision with the optimal solution in small cases.
3. Lack of justification on scalability of the framework.

### Questions
Thank you for submitting to ICLR 2025! I think this paper tries to tackle the important problem of scheduling heterogeneous GPU and network resources for disaggregated LLM serving.
Despite the good evaluation results, I have a few comments for the paper and it would be great if the authors could address them.

The current explanation for the core scheduling algorithm is confusing and unclear.
There is no clear intuition on why the algorithm should be designed at these two levels.
There is also no clear guidance on what the objective is during each phase of the algorithm.
For example, in the first step of the first phase: graph partition, is balancing the node weights (memory capacity) the overall objective at this step?
The node weight in the global graph seems to be determined by GPU memory but not GPU compute, why is that the case?
Why is the coarsen step necessary in Step 2?
My understanding is that a prefill or decode replica could have multiple super nodes, is that right?

In addition, in the second phase, why is it required that each compute node needs to be connected to two other nodes in the same graph?
How are latency-optimal configuration and throughput-optimal configuration for prefill and decode replicas respectively related to the max-flow algorithm used?
In iterative refinement, what is the physical meaning of swapping edges?
I think the scheduling algorithm should also have easy-to-follow examples on the side to clearly give intuitions to readers.
The current Figure 3 is hard to understand even after reading the entire Section 3.

I am also wondering how the current algorithm compares to the optimal allocation and parallelization plan.
Despite the NP-hardness of the problem, the optimal plan should be solvable by just brutal forcing all possible plans in small cases such as 4 H100 and 4 A100 GPUs.
In Section 5.3, it says "Our scheduling algorithm identifies optimal assignments for all scenarios within 90 to 120 seconds". 
How is optimality defined here?
Is the algorithm always guaranteed to find the optimal solution given enough search time?

Also, how much overhead would the algorithm incur if running on a cluster with, for example, hundreds of GPUs?
It may be hard to rent such a large number of GPUs for experiments, but evaluating algorithm overhead should be possible.

In the evaluation, it says HexGen-2 is compared against DistServe under the homogeneous setting with 8 H100 GPUs.
Why is DistServe appearing in all heterogeneous settings in both Figure 6 and Figure 7?

### Soundness
3

### Presentation
2

### Contribution
3
