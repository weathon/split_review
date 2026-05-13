# Capturing and Mitigating Gradient Aggregation Errors for Fault-Tolerant Distributed Training

- Decision: Reject
- Scores: 3, 1, 6, 3

## Abstract
Capturing and recovering from hardware failures is important in fault-tolerant distributed training to guarantee system efficiency. However, some hardware-related silent data corruption errors during gradient aggregation like bit corruptions or communication noise, are difficult to capture and address, leading to slow or failed convergence. 
To understand and mitigate these errors, we first mathematically formulate and generalize them as gradient inconsistency. Then, we theoretically analyze how it leads to model divergence accumulated during training and the failed convergence. 
Based on the analytical study, we design PAFT, a fault-tolerant distributed training system with dynamic and asynchronous parameter synchronization. PAFT includes two parts: (1) PAFT-Sync, which mitigates model divergence by periodically synchronizing parameters, and (2) PAFT-Dyn, which minimizes synchronization overhead through dynamic training overlap and synchronization frequency scheduling based on profiled error degrees. Together, they ensure efficient model convergence at scale.  The fault-tolerant synchronization in PAFT is optimized to support commonly used optimizers, e.g., Stochastic Gradient Descent (SGD), SGD momentum, and Adam. 
We implement PAFT on PyTorch Distributed and train ResNet, GPT-2, and LLaMA-2 on 4$\sim$ 32 GPUs. Experimental results show that PAFT efficiently defends against gradient aggregation error degrees while maintaining training performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper is focused on the reliability problem of distributed training. Specifically, it aims to mitigate the statistical divergence during the training caused by the unreliable gradient aggregation, i.e. silent data corruption problem. The method proposed by this paper is to periodically synchronize the model weights of workers. To reduce the extra overhead of model sync up, authors come up with a dynamic way to decide the sync-up frequence and overlap the communication with back propagation.

### Strengths
1. The research problem is quite important regarding the large-scale distributed training. How to deal with the potential unreliability of the data communication is crucial to model training.
2. The idea of dynamically adjusting the sync-up frequency is interesting since the* silent data corruption may happen by a random rate.

### Weaknesses
1. My biggest concern is that, if we assume the silent data corruption could randomly happen during the gradient aggregation, then it could also happen during the model synchronization. Therefore, how can we synchronize the model weights without any error?
2. The novelty of this paper is also quite limited. From many previous studies, we already know that in data parallel distributed training, if local models apply different local gradients for some steps, and then average the model weights globally, the global model can still converge [1]. So the theoretical contribution of this paper is limited. Besides, overlapping the communication with the back propagation is also a widely used technique in both research papers and real-world systems like pytorch.

### Questions
Please refer to the weakness

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The submission claims to introduce a technique for capturing and mitigating the errors in gradient accumulation in distributed SGD due to silent data corruption (SDC).

To this end, the submission presents the "PAFT" algorithm. The main feature of this algorithm is that it periodically synchronizes the models in a way quite similar to the standard local SGD algorithms. In a variant of this algorithm, which is fully synchronous periodic model averaging, in addition to the gradient communication after every gradient update step, the claim is that the algorithm suffers from high communication cost, whose mitigation requires the presentation of a variant where the averaging frequency is determined based on the model divergence measure. 

The algorithms are evaluated on ResNet-18 with CIFAR-10, ResNet-50 with CIFAR-100 for 120 epochs, and GPT-2 with Open WebText for 3000 iterations. Additionally, pre-trained LLaMA2 and GPT-2 are trained for an epoch on the Alpaca dataset using the Low-Rank Adaptation scheme. In all these experiments, SDC is simulated as white noise. 

The submission also includes convergence discussion of the presented algorithms.

### Strengths
The motivation of the approach is straightforward and relevant.

### Weaknesses
 The idea of this work is poorly conceived. In particular, 
* It is unclear why the discussion did not cite any of the local SGD papers. For example, a comparison with "Don't Use Large Mini-Batches, Use Local SGD, Lin et al. 2018" will be a relevant approach, where for multiple first epochs, distributed SGD is applied, and after that, periodic averaging is performed. 
* The periodic model averaging on top of gradient communication after every computation is an overkill. Can't the generated/simulated SDC vector be sent in the next round added to the gradient, much similar to the error feedback method? See "Elastic Consistency: A Practical Consistency Model for Distributed Stochastic Gradient Descent, Nadiradje et al. 2022". Once it is modeled with error feedback, it then automatically fits the Elastic Consistency framework for analysis.
* The simulated SDCs do not seem to be "capturing" it. Can the authors elaborate on some real-life cases of SDC that may be modeled as the standard N(0,1) distribution?
* The convergence results in the main body of the paper do not even include the convexity nature of the objective, which is mentioned only in the appendix. Thus, the results statements still need to be completed. It distracts a reader even when reading the derivations. 
* Today's Distributed SGD methods invariably include communication compression -- quantization, sparsification, etc. A full gradient communication approach is dated. See "Elastic Consistency: A Practical Consistency Model for Distributed Stochastic Gradient Descent, Nadiradje et al. 2022".
* Training ResNet18/50 models for 120 epochs on CIFAR 10/100 data is not standard. A more standard benchmark is training these models for 300 epochs. Is there any specific reason for using 120 epochs only? It looks more like training to subpar accuracy, an area where different training methods behave starkly differently but, after 200 or so epochs, are close to the known best results. Similarly, for other models.

### Questions
* How about trying out model averaging after every local gradient update? Very likely, the motivated mitigation will be achieved. If not, can the authors clarify why so? After all, the above-suggested scheme involves much less communication than the proposed one.
* Can you please address other comments included above in the "Weakness" assessment?

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper discusses an interesting research question: how silent data corruption in gradient aggregation impacts on distributed training and how to capture and mitigate them. The paper theoretically analyzes how silent data corruption causes accumulated model divergence and failed convergence. It then designs a fault-tolerant distributed training system that can be proved to illuminate model divergence and ensure convergence, as well as reduce incurred communication overhead.

### Strengths
+ This paper discusses how silent data corruption (SGC) influences training convergence for the first time
+ This paper theoretically analyzes how gradient inconsistency caused by SGC leads to failed convergence and empirically show that a small noise can already harm training convergence and accuracy
+ This paper proposes a simple yet effective synchronization scheme to eliminate model divergence. It also reduces the incurred communication overhead by overlapping synchronization with training.
+ This paper demonstrates its effectiveness with four models, different noise degrees, and different training scales.

### Weaknesses
 - Lack of real-world trace. It is true that SGC has negative impacts on training convergence, but how bad it could be depends on the frequency of SGC during training. Is it possible to provide any real-world traces to connect the noise degree with SGC frequency? Specifically, the paper should include data on the distribution of silent data corruption errors observed in real-world distributed training environments. This would allow for a more accurate assessment of the practical relevance of the proposed method. Without this, it's difficult to gauge the typical noise levels and whether the tested noise degrees are representative of actual scenarios.
- Test accuracy is still impacted in case of high noise degrees. As listed in Table 2, the test accuracy is dramatically lower than the DSGD baseline when the noise degree is 0.01 or 0.1. It appears that PAFT cannot avoid accuracy dropping under all scenarios and doesn’t completely address the problem. The paper needs to further explore the limitations of PAFT under high noise conditions and provide a more detailed analysis of why the accuracy drops despite the synchronization scheme. A more thorough investigation into the root causes of this accuracy degradation is needed, potentially exploring the interaction between noise and the optimization landscape.
- Only CIFAR-10 is used for the evaluations of ResNet. Could you also include ImageNet in the evaluation to check whether these conclusions still hold for a large image dataset? The evaluation should be extended to include a more diverse set of datasets, especially larger and more complex ones like ImageNet. This is crucial to demonstrate the generalizability of the proposed approach and to ensure that the conclusions are not limited to smaller datasets like CIFAR-10. The performance on larger datasets with more complex data distributions would provide a more robust evaluation of the method's effectiveness.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers hardware failures that can happen during gradient aggregation. These failures can cause different clients to obtain different noisy versions of aggregated gradients and, thus, different model weights. Such noise can accumulate over rounds and cause performance degradation and even divergence of the training process.

To account for such aggregation errors, the paper proposes PAFT, an algorithm that performs occasional model weight synchronization. PAFT has two versions: one where the model weight updates occur periodically and, another where the noise is estimated, and synchronization is invoked based on the estimated noise.

The paper also provides convergence rate analysis with noisy gradients and evaluates whether PAFT successfully mitigated the problem over different scenarios.

### Strengths
-	The paper is well-written and structured

-	The paper performs convergence analysis that takes the modeled aggregation errors into account

-	The experimental study considers different setups and scenarios

### Weaknesses
 - The failure model is vague, and it is unclear what exactly fails in real systems that cause aggregation errors. This is at the heart of the paper and should be made precise. For example, both in TCP and InfiniBand (with and without RDMA), there are data corruption checks (e.g., CRC checksums) that invalidate packets that experienced data corruption (e.g., link-level and e2e). It is not clear how a gradient corruption could occur without triggering these checks, especially given that these protocols are designed for reliable data delivery. The paper should specify the exact hardware or software components that are susceptible to these errors and explain why standard error detection mechanisms are insufficient.

- Weight synchronization is not a new idea, and critical related work is missing (e.g., see [1][2][3])


- The theoretical results are fairly standard and do not seem to provide new insight or techniques (e.g., see results in [1][2][3])

### Questions
1. How can a gradient corruption happen without the packet being discarded by the transport protocol, which must ensure reliable data delivery by design? Also, why is the noise assumed to be unbiased? An HW error can nullify a bit, for example.

2. As previous works have already suggested, if one is concerned with the modeled error, why not use weight synchronization instead of gradient synchronization to eliminate the problem altogether and without introducing overhead?

### Soundness
3

### Presentation
3

### Contribution
1
