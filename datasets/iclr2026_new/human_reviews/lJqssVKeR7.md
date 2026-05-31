## Human Reviewer 1

### Summary
This paper proposes HiSo, a novel Hessian-informed zeroth-order optimization method for federated learning that achieves dimension-free communication while accelerating convergence. The key innovation lies in leveraging global diagonal Hessian approximations as preconditioners without transmitting second-order information, thus preserving the scalar-only communication paradigm. Theoretically, the authors establish a convergence rate independent of model dimension and Lipschitz constant under certain Hessian approximation assumptions, providing the first such result for ZO methods in FL with multiple local updates. Empirically, HiSo demonstrates 1-5× speedup in communication rounds and up to 90 million times communication savings compared to first-order baselines across diverse LLM fine-tuning tasks.

### Strengths
The primary strength is the elegant resolution of a fundamental tension between leveraging second-order information for acceleration and maintaining extreme communication efficiency. HiSo represents a conceptually novel approach with non-trivial theoretical analysis and compelling empirical results. The scalar-only communication property holds significant practical value for bandwidth-constrained federated LLM fine-tuning.

### Weaknesses
The main weakness concerns the foundational assumptions underlying its theoretical advantages. The critical "well-approximated Hessian" condition is challenging to verify empirically, particularly during early training stages. While outperforming ZO baselines, the accuracy gap with first-order methods remains, highlighting inherent limitations of the ZO approach.

### Questions
The theoretical advantages rely on the "well-approximated Hessian" condition. Do you have any empirical evidence (e.g., comparing with true Hessian on small models) suggesting your learning method effectively captures principal curvature directions?

In extreme FL scenarios with massive client populations (e.g., millions), could maintaining client participation history become a server-side memory bottleneck? How do you assess this scalability aspect?

The Hessian smoothing parameter ν appears to have minimal impact. Does this indicate HiSo is genuinely insensitive to this hyperparameter, or are there implicit guidelines for its selection?

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes HiSo, a novel federated learning (FL) algorithm designed for communication-efficient fine-tuning of Large Language Models (LLMs). HiSo innovatively combines zeroth-order (ZO) optimization for dimension-free communication with Hessian-informed preconditioning to accelerate convergence. The core idea is to use a global, diagonal Hessian approximation to guide the random search directions in ZO optimization, effectively creating a "natural gradient" style update. Crucially, this Hessian information is learned and applied without transmitting any second-order matrices, preserving the scalar-only communication property that makes ZO methods attractive for high-dimensional problems. Theoretically, the authors provide a convergence analysis suggesting that under a "low-effective-rank" assumption for the Hessian, HiSo can achieve a rate independent of the model dimension d and Lipschitz constant L. Empirically, HiSo demonstrates significant speedups (1-5x in communication rounds) and up to 90 million times lower communication cost compared to first-order baselines like FedAvg on LLM fine-tuning tasks.

### Strengths
1.  Novel and Well-Motivated Idea: The combination of Hessian-informed updates with scalar-only communication is highly innovative. It directly addresses the primary weakness of ZO methods (slow convergence) while preserving their key advantage (low communication cost). The motivation is clear and grounded in the practical challenge of federated LLM fine-tuning.
2.  Strong Empirical Evaluation: The experiments are comprehensive, spanning from simple CNN/MNIST setups to LLM fine-tuning on standard NLP benchmarks (SST-2, QQP, SQuAD). The comparisons against a wide range of baselines (FedAvg, FedAdam, FedZO, DeComFL) are convincing and demonstrate clear improvements in convergence speed and final accuracy for ZO methods.
3.  Significant Practical Impact: The reported communication savings (MBs vs TBs) are monumental. If applicable to even larger models, HiSo could have a substantial impact on the feasibility of federated fine-tuning in bandwidth-constrained environments.
4.  Theoretical Depth: The paper goes beyond mere algorithm design by providing a non-trivial theoretical analysis. The introduction of the "low whitening rank"  to explain the accelerated convergence is a valuable conceptual contribution that helps reconcile the practical efficiency of ZO methods with their pessimistic worst-case theoretical bounds.

### Weaknesses
1.  Limited Discussion on Computation Overhead: While communication is the primary bottleneck, the computational cost of ZO methods is inherently higher than first-order methods due to the need for multiple forward passes. The paper briefly mentions the preconditioning time is negligible but does not provide a full comparison of the total wall-clock time (computation + communication) against first-order methods. This is crucial for assessing real-world utility, as increased computation time might offset communication savings.
2.  Validation of Theoretical Assumptions: The core theoretical improvement hinges on the "well-approximated Hessian" condition (Eq. 17) and the low-effective-rank property. While the empirical results are strong evidence, the paper does not directly validate that the learned diagonal matrix H actually satisfies this condition for the LLMs used in the experiments. A more rigorous analysis or measurement of the whitening rank  during training would strengthen the theoretical claims.
3.  Comparison with Parameter-Efficient Fine-Tuning (PEFT): The discussion of FL+PEFT baselines (like FedLoRA) is brief and relegated to the appendix. Given that PEFT is a dominant approach for efficient LLM fine-tuning, a more thorough comparison in the main text is warranted. HiSo's claim of "full-parameter" tuning is a different paradigm, but a direct comparison on metrics like final accuracy, communication cost, and memory usage would better situate HiSo within the existing landscape.
4.  Hyperparameter Sensitivity: The ablation study on the Hessian smoothing parameter ν shows robustness, but the performance of adaptive methods like HiSo can be sensitive to other hyperparameters like the learning rate and the exponential moving average decay factor. A more detailed sensitivity analysis would be helpful for practitioners.

### Questions
1.  How does the total energy consumption (a function of both communication and computation) of HiSo compare to first-order methods and DeComFL, especially when considering the additional forward passes required for ZO estimation?
2.  Could the HiSo framework be naturally extended to incorporate PEFT techniques (e.g., applying Hessian-informed updates only to low-rank LoRA parameters)? Do you see this as a promising future direction?
3.  The theory suggests performance degrades to match DeComFL if the Hessian approximation is poor. Did you observe this in practice during the initial stages of training or on any specific tasks?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
In this paper, the authors propose HiSo, a Hessian informed, scalar only, federated zeroth order optimizer for large language model fine tuning.  The authors first generalize the scalar only paradigm into a reusable federated optimization framework, where the server and clients exchange only scalar update codes and can reconstruct each other's parameter trajectories without ever sending high dimensional tensors. Within that framework, they introduce HiSo, which maintains a global diagonal Hessian approximation on the server and uses it to precondition the zeroth order perturbation directions. Effectively, HiSo samples Hessian aware update directions, similar in spirit to natural gradient or approximate Newton steps, but still communicates only scalars.

### Strengths
1. Theoretical contribution:  The paper proves non convex convergence bounds where the rate depends on a whitening rank related to the effective Hessian spectrum instead of the raw model dimension, and extends DeComFL style theory to multiple local steps per round.

2. Strong and concrete motivation:  Existing scalar only ZO methods solve bandwidth but converge painfully slowly. HiSo squarely targets this convergence bottleneck without giving up the scalar only advantage.

3. The paper repeatedly reports actual bandwidth numbers in KB and TB, and highlights 10^7 to 10^8 fold savings compared to FedAdam and FedAvg.

### Weaknesses
1. Benchmark scale and diversity：The main LLM experiments involve six clients with two sampled per round, and tasks are classification and extractive QA. Although these are standard NLP benchmarks and good stress tests for convergence and accuracy, they are still small compared to industrial federated networks across hospitals, phones, or enterprises. The paper would be stronger if it included either larger federations or at least a stress test with many more clients and skew patterns.


2. Backbone model: The authors only conduct experiments on OPT series models, how about the Qwen series models? I am curious about the performance of proposed method on those models. 

3. Theory assumptions and coverage:
   The convergence guarantee depends on a low effective rank Hessian spectrum and on the quality of the diagonal Hessian approximation. While the paper provides evidence that the estimated diagonal Hessian has a long tail and argues that large language models empirically satisfy this, it does not show failure cases or quantify how often the whitening rank assumption holds in domains beyond language. This makes it harder to judge how robust the dimension independent claim really is.

### Questions
see weakness 1,2,3

### Soundness
4

### Presentation
3

### Contribution
4

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper studies federated learning via zeroth-order optimization. By proposing a method that preserves scalar-only communication and avoids transmitting second-order information, it significantly reduces computational costs. Theoretically, they demonstrates an accelerated convergence rate under a suitable Hessian structure.

### Strengths
The paper is well-written, with a well-motivated research goal and a clear description of the  algorithm.

### Weaknesses
I have the following concerns regarding the paper:

Theoretical Practicality and Depth: The theoretical analysis relies on a good approximation of the Hessian, yet the method employed in practice is only a diagonal approximation. This gap makes it difficult to appreciate the practical relevance of Theorem 1. Furthermore, a simple non-convex analysis seems insufficient, as it fails to capture the specific landscape properties of neural network loss functions.

Experimental Comprehensiveness: The experimental validation appears somewhat limited. It would be strengthened by including plots of the training loss against both iterations and wall-clock time on more experiments. Additionally, experiments on more datasets and with larger models would better demonstrate the scalability and robustness of the proposed method.

Novelty of Insight: The core idea seems limited. Since zeroth-order optimization inherently accesses only scalar information at each step, the advantage of communicating solely scalars appears straightforward. I did not find significant novel algorithmic insights in the current work.

### Questions
See the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 5

### Summary
The authors of this manuscript propose HiSo, a Hessian-informed federated zeroth-order (ZO) optimization method. It aims to accelerate the convergence of ZO-FL, which is attractive for LLM fine-tuning due to its scalar-only (dimension-free) communication, but typically suffers from slow convergence. The method computes a global diagonal Hessian approximation using an Adam-style update rule, which does not require transmitting any second-order information. The authors use this approximation to inform the ZO update direction. They provide a theoretical analysis showing convergence rates independent of model dimension and empirical results demonstrating a 1-5x speedup in communication rounds over the DeComFL baseline.

### Strengths
1- The improved convergence by HiSo is significant in comparison to other ZO-FL benchmarks, while keeping the communication costs significantly small. The 1-5x speedup over DeComFL is a practical and valuable improvement.

2- The paper provides a theoretical analysis to support the method, proving a convergence rate independent of model dimension `d` for non-convex functions.

3- The proposed method addresses a clear and important bottleneck in federated LLM fine-tuning, namely the high communication cost of traditional first-order methods and the slow convergence of previous ZO methods.

### Weaknesses
1- The experimental validation is limited to the OPT family of models (OPT-125M to OPT-2.7B). These models are somewhat dated and are known to be undertrained. The effectiveness of HiSo on newer, more capable models (e.g., smaller variants of LLaMA-3.2, Qwen-2.5, Gemma 3, or SmolLM) is not demonstrated. It is unclear if the same optimization behavior will hold on these new architectures.

2- The claim that HiSo is a "Hessian-informed" or "second-order" method is potentially misleading. The proposed update for the diagonal Hessian approximation in Equation (12) is a recursive exponential moving average of the squared updates. This formulation is functionally identical to the variance/second-moment tracking in first-order adaptive optimizers like RMSProp or Adam. This makes the contribution appear more as an application of an adaptive preconditioner to the ZO setting, rather than a true second-order method.

### Questions
1- How does the performance of HiSo change when applied to newer generations of models, such as the HuggingFace SmolLM or smaller variants of Qwen-2.5, LLaMA-3.2, and Gemma 3? Do the same convergence benefits hold?

2- The authors call the method "Hessian-informed." However, the update in Equation (12) is mathematically very similar to the variance/second-moment update in the Adam optimizer (a first-order method). Could the authors clarify why this should be considered a second-order method and not a first-order adaptive method? A direct comparison of the HiSo formulation with Adam would be insightful.

3- The paper focuses on fine-tuning. Can the proposed ZO-FL framework be used for the pretraining of LLMs? What are the primary challenges in applying this method to the pretraining regime? I understand pretraining is expensive and do not expect experiments, but insight into the challenges would be helpful.

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
5