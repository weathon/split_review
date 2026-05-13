# CO2: Efficient Distributed Training with Full Communication-Computation Overlap

- Decision: Accept
- Scores: 8, 6, 8, 6, 6, 8

## Abstract
The fundamental success of large language models hinges upon the efficacious implementation of large-scale distributed training techniques. Nevertheless, building a vast, high-performance cluster featuring high-speed communication interconnectivity is prohibitively costly, and accessible only to prominent entities. In this work, we aim to lower this barrier and democratize large-scale training with limited bandwidth clusters. We propose a new approach called \textbf{\textit{CO2}} that introduces local-updating and asynchronous communication to the distributed data-parallel training, thereby facilitating the full overlap of \textbf{\textit{CO}}munication with \textbf{\textit{CO}}mputation. CO2 is able to attain a high scalability even on extensive multi-node clusters constrained by very limited communication bandwidth. We further propose the staleness gap penalty and outer momentum clipping techniques together with CO2 to bolster its convergence and training stability. Besides, CO2 exhibits seamless integration with well-established ZeRO-series optimizers which mitigate memory consumption of model states with large model training. We also provide a mathematical proof of convergence, accompanied by the establishment of a stringent upper bound. Furthermore, we validate our findings through an extensive set of practical experiments encompassing a wide range of tasks in the fields of computer vision and natural language processing. These experiments serve to demonstrate the capabilities of CO2 in terms of convergence, generalization, and scalability when deployed across configurations comprising up to 128 A100 GPUs. The outcomes emphasize the outstanding capacity of CO2 to hugely improve scalability, no matter on clusters with 800Gbps RDMA or 80Gbps TCP/IP inter-node connections.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a novel distributed training method: CO2, which can overlap communication and computation in distributed training. This technique is particularly useful when there are a large number of GPU nodes and the inter-connection between nodes are very slow. Compared to previous works, this paper introduces (1) penalty on stale momentum (2) momentum clipping. Empirical ablations show these two techniques are crucial to improve the training convergence performance. The authors also conducted extensive empirical studies, including experiments on image classification, large language model training, to demonstrate the effectiveness of the proposed method.

### Strengths
- The paper has extensive empirical studies across different learning tasks as well as different network environments.
- The authors also provided a convergence analysis for the proposed method.

### Weaknesses
 - The idea of overlapping communication and computation is not new, as mentioned in the paper. The key contribution of this paper would be introducing the staleness penalty and momentum clipping mechanisms. They also present solid experimental resutls.
- The comparison with previous works are not enough. For example, totally overlapping communication and computation has already been achieved. like Wang et al, 2020. Overlap-Local SGD. The authors should include more discussions on the differences. or even include this method as a baseline.
- It is not very clear the convergence analysis was performed on which algorithm. Does the analysis consider staleness penalty and momentum clipping? Also, the convergence analysis looks like following previous works. It'd be better to cite few at the very beginning of the analyses.

### Questions
See the above section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a new distributed training algorithm called CO2, which aims to improve the communication efficiency of data-parallel training by overlapping local training iterations with parameter averaging from the previous global step. The proposed method is tested across multiple machine learning tasks and achieves better scalability than the baseline approaches while maintaining comparable convergence properties.

---
Post-rebuttal update: after reading authors' responses and other reviews, I decided to keep my weakly positive score unchanged and increase the confidence of my review. I think that the contributions of the study are solid and I am in favor of accepting the submission, but I am not fully sure that the work will have significant impact on the field in light of prior closely related publications.

### Strengths
* Overall, the proposed method is conceptually simple yet shows promising results.
* The paper has a broad range of experiments, covering 5 setups with models that are widely used in practice.
* Authors conduct a detailed ablation study for the components of CO2, as well as measure its scalability in different environments.

### Weaknesses
 * While I am not an expert in distributed optimization, to my understanding, similar methods allowing full overlap of communication and computation have been proposed previously. See, for example, [1] from the related work section: on page 17, they state that "as long as the number of local updates τ is large enough, the communication can be fully overlapped with the local computation." This appears to be quite close to the primary contribution of this work, therefore I believe that the submission needs to describe the key distinctions from prior work in more detail.
* I think that the experimental setup description could benefit from more details. For example, while the authors mention that their hyperparameters were tuned "to find the optimal balance between efficiency and performance", we do not see neither the exact values of $\tau$ for each experiment nor the exact description of the tuning procedure. Also, authors mention that they leverage ZeRO for TransNormer experiments, but do not state the exact stage of ZeRO used, which is crucial for understanding memory usage and communication patterns.
* Lastly, the majority of model sizes used in this work have quite small parameter counts (fewer than 1B), and therefore it is a bit surprising to see communication as the bottleneck for training even on 80Gbps networks. I think that it would be beneficial to provide more detailed breakdowns of computation and communication times (for example, the time to process 1 microbatch and 1 batch of data, as well as the time to exchange parameters) in each setting to demonstrate the necessity of large $\tau$. Furthermore, the paper lacks a clear analysis of how the overlap ratio changes with varying network bandwidths, which is essential for understanding the method's applicability in different environments.

### Questions
* What were the values of $\tau$ for each experiment?
* Which stage of ZeRO have you used for the TransNormer experiment?
* In Table 2, it is somewhat surprising to see that CO2 (an asynchronous method) obtains consistently lower perplexity than a non-asynchronous adaptive method (AdamW). Do you have any explanations of that phenomenon?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces CO2, a framework for improved communication/computation overlap for distributed deep learning, especially in the case of limited network bandwidth. CO2 leverages local SGD, performing a fixed (tunable) number of local iterations while allreduces perform synchronization in the background, allowing communication to almost always be hidden. To ensure good convergence, CO2 computes a staleness gap metric and uses this to scale updates, as well as a clipping mechanism to limit the variance of updates. A convergence bound is proven and experiments on a variety of network architectures and datasets show convergence matches that of standard SGD and other communication-avoiding algorithms; in the low-bandwidth regime, CO2 additionally offers significantly improved performance and scalability.

### Strengths
1. This paper is addressing an important situation: communication-bound training workloads. This can occur due to both large models and slower interconnects. I appreciate that the paper specifically and clearly calls out lower-bandwidth networks as an area it is focused on. While the idea is relatively straightforward, it includes some details to get it to work well in practice.
2. The paper adequately specifies its proposed algorithm and includes some theoretical justification to support its claims.
3. There are extensive experiments on a variety of models, including relatively large ones, demonstrating roughly equivalent convergence curves, indicating that the method does not compromise learning.
4. Scalability studies are also conducted, showing slightly improved performance on high-bandwidth networks and significantly improved performance on low-bandwidth networks relative to a standard allreduce implementation.

### Weaknesses
 1. I think the claims of "perfect 100% scalability" are a bit oversold. This relies on appropriately selecting $\tau$, the number of local steps between global communications; it seems clear that if you can arbitrarily set the amount of computation done to hide communication, you can easily hide it. (Though I wish to be clear that the paper is clear that you can't make $\tau$ arbitrarily high and still achieve good convergence.) This also neglects other aspects of training which may limit scalability (e.g., I/O for data ingestion).
2. The paper does not provide guidance on selecting an appropriate $\tau$, and in its experiments searches over a small set of potential values. This seems like a challenging parameter to tune in practice, as it could significantly increase hyperparameter tuning costs.
3. It is not clear to me how the paper improves upon existing communication-efficient works which try to tune the communication frequency to achieve both good learning and runtime performance. In particular, works like Wang & Joshi, "Adaptive Communication Strategies to Achieve the Best Error-Runtime Trade-off in Local-Update SGD", or Haddadpour et al., "Local SGD with Periodic Averaging: Tighter Analysis and Adaptive Synchronization", seem like relevant points of comparison.
4. The paper lacks implementation details. Specifically, it does not specify how the asynchronous allreduce is implemented (e.g., is it using a NCCL allreduce on a separate CUDA stream?). It is also not clear whether the asynchronous allreduce is operating on a separate weight/gradient buffer from the one being used for computation; or what the memory overheads of the method are.
5. While I appreciate that the experiments were run multiple times (Section 4.1), the results do not include any measure of variance. This makes it hard to understand whether CO2 amplifies the variance between runs and how much methods actually differ.
6. Scalability is only evaluated on one model. I would be interested to see how models other than the TransNormer-LLM scale; in my experience, smaller models tend to benefit less from communication optimizations as they are already often able to hide most communication.
7. The scaling study in Section 4.3 does not include any comparisons with other communication-efficient methods. Given that SlowMo demonstrates very similar convergence curves, it seems prudent to see whether CO2 offers better scalabiltiy.
8. From a performance perspective, the paper is missing a detailed analysis substantiating its claims. In particular, the communication/computation overlap achieved is never actually measured.
9. A more minor point: The paper refers to gradient bucketing as a way to overlap communication and computation (e.g., in Section 1). I think this is not quite correct; rather, gradient bucketing is a latency/bandwidth tradeoff (performing fewer allreduces on larger buffers). While this can be more efficient, and consequently improve communication/computation overlap, it does not itself enable overlap.

### Questions
1. I think the paper would be stronger if the claims of "perfect 100% scalability" were toned down and better contextualized. (See above for some details.)
2. How should $\tau$ be selected? Is hyperparameter tuning the only way to do so?
3. How does the paper improve upon prior works which tune the communication frequency (see above for some references)? Could these approaches be used to tune $\tau$ automatically?
4. Please add implementation details and a discussion of memory overheads. I think memory may be especially relevant for larger models such as LLMs.
5. Please add the observed variance to the accuracy results. It would also be good to include error bars in the scaling performance results.
6. How do other models considered in the paper (e.g., ResNets or ViTs) scale?
7. How do other communication-efficient (e.g., SlowMo) methods scale on the fast and slow network?
8. How much communication/computation overlap is actually achieved by CO2, particularly at scale?
9. A more minor point: The paper refers to gradient bucketing as a way to overlap communication and computation (e.g., in Section 1). I think this is not quite correct; rather, gradient bucketing is a latency/bandwidth tradeoff (performing fewer allreduces on larger buffers). While this can be more efficient, and consequently improve communication/computation overlap, it does not itself enable overlap.

-----

In light of the authors' response and promised updates, I have raised my score. They have addressed a number of points above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To address the communication problem in large-scale distributed training of deep neural networks, the paper proposes a combination of local-SGD and asynchronous communication to derive a new distributed training algorithm named CO2. In CO2, two novel approaches are developed to ensure that CO2 aligns the convergence performance with conventional distributed data-parallel algorithms. Experiments are conducted on a 64-GPU testbed, showing that CO2 outperforms existing methods significantly. The studied problem is timely and important. The paper is also well-written.

### Strengths
- Propose a new distributed training algorithm, CO2, using local updates and asynchronous communication to alleviate the communication problem in conventional synchronous data-parallel distributed training. 
- New tricks to address the convergence problem in stale gradients.
- Comphesive experiments to show the effectiveness of CO2.

### Weaknesses
 - Some stale parallel algorithms (e.g., SSP [ref1]), whose key ideas are quite similar to CO2, were not included in the discussion and comparison. The survey paper [ref2] may help find SSP-like methods for comparison.
- It seems that 100% scaling efficiency is over-claimed. The scaling efficiency highly depends on $\tau$. Higher $\tau$ has better scaling efficiency but has worse convergence performance. Thus, achieving 100% scaling efficiency with a $\tau>1$ while sacrificing the convergence performance cannot conclude the algorithm has true 100% scaling efficiency. The paper lacks a clear definition of what constitutes '100% scaling efficiency' in the context of their algorithm, making it difficult to evaluate this claim rigorously. Furthermore, the trade-off between $\tau$ and convergence is not sufficiently explored, and the paper does not provide a method for determining the optimal $\tau$ for different scenarios. The experiments should include a more detailed analysis of how the choice of $\tau$ impacts both scaling and convergence, and should also compare against other methods with similar trade-offs.

### Questions
- How about comparing with SSP-like algorithms in terms of theoretical convergence bound and empirical scaling efficiency? 
- How $\tau$ is set in Table 1?
- How about the end-to-end training performance (i.e., time to accuracy)?
- How to choose $\tau$ in a new distributed GPU cluster?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach called CO2 to improve throughput of distributed model training by overlapping computation and communication. Building on prior work that perform multiple training iterations with local updates before each global model synchronization, CO2 enables further throughput improvement by making the global synchronization asynchronous and overlapped with the next round of local updates. CO2 proposes two techniques for addressing the convergence issues of the asynchrony: (i) staleness penalty gap, and (ii) outer momentum clipping. The paper presents theoretical analyses of the convergence guarantees of these two techniques. The evaluation results show that CO2 can achieve convergence results comparable to baselines that are fully synchronous (e.g, Adam) and better than those using local updates (e.g, LocalSGD). The experimental results also show the throughput and scalability of CO2 are better than Adam.

### Strengths
The paper is tackling an important problem since communication is a major bottleneck for scaling model sizes and training hardware, and so approaches for reducing communication overheads are very relevant to the community. 

The idea of overlapping communication with computation is reasonable given the cost-effectiveness. I also liked the fact that the paper attempts to quantify and fix the resulting staleness update problem. 

The evaluation considers a diverse and important set of workloads and hardware environments, which helps to understand the generality of CO2.

### Weaknesses
I observe some critical problems in the draft that raise the question of whether CO2 can simultaneously achieve good convergence and high throughput. 

1. The convergence and throughput trade-off of inner loop step count ($\tau$) is not clearly reported in evaluation. In particular, the convergence results in Tables 1 & 2 should include the corresponding $\tau$ and throughput. I was unable to determine whether the good convergence results are achieved with $\tau$ that also provides throughput benefits. 

2. The paper is silent on the memory overheads of CO2 relative to baselines, even though Algorithm 2 suggests that multiple copies of the model is required to support asynchronous communication. It is unclear from the description how many model copies are required, and a detailed analysis of the memory footprint is missing. Specifically, Algorithm 2 appears to require at least four model copies: one for the current model, one for the outer model, and two additional copies for the asynchronous communication buffers. This needs to be explicitly addressed.

3. Equation 3 assumes learning rate decay in the inner loop which is not true for learning rate schedules, such as cyclic, which involve learning rate increases. The analysis of the staleness penalty gap relies on this assumption, and the paper does not discuss the implications of using learning rate schedules that do not monotonically decrease.

4. It is unclear to me whether CO2 can achieve expected throughput benefits in scenarios with parallelism techniques (e.g., tensor slicing, sequence parallelism, and zero stage 3) that introduce communication to forward/backward passes. It seems these (synchronous) communication operations would interfere with the overlapped communication and hurt overall throughput. Evaluating such scenarios could help to better understand the generality of CO2.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes CO2, a new approach that enables efficient distributed training of large language models on clusters with limited bandwidth. CO2 introduces local-updating and asynchronous communication to the distributed data-parallel training, allowing for full overlap of communication with computation. The approach achieves 100% scalability even on clusters with limited communication bandwidth. The paper also introduces staleness gap penalty and outer momentum clipping techniques to improve convergence and training stability. The proposed approach is validated through extensive experiments on computer vision and natural language processing tasks as well.

### Strengths
+ The paper is well-written and comprehensible.
+ The code is available in this work.
+ The utilization of local updating and asynchronous communication makes a full overlap of computation and communication. 
+ The paper provides enough theoretical explainability and empirical validation. 
+ The experimental results are sound and promising.

### Weaknesses
I do not have much to comment on the weakness, as this work goes beyond my acceptance threshold.

### Questions
How many runs for each task? I understand that training a Language Learning Model from scratch can be quite costly. However, conducting the experiment only once may not yield persuasive results.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
