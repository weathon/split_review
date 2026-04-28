# Federated Residual Low-Rank Adaption of Large Language Models

- Decision: Accept
- Avg Score: 6.60
- Scores: 5, 6, 6, 8, 8

## Abstract
Low-Rank Adaptation (LoRA) presents an effective solution for federated fine-tuning of Large Language Models (LLMs), as it substantially reduces communication overhead. However, a straightforward combination of FedAvg and LoRA results in suboptimal performance, especially under data heterogeneity. We noted this stems from both intrinsic (i.e., constrained parameter space) and extrinsic (i.e., client drift) limitations, which hinder it effectively learn global knowledge. In this work, we proposed a novel Federated Residual Low-Rank Adaption method, namely FRLoRA, to tackle above two limitations. It directly sums the weight of the global model parameters with a residual low-rank matrix product (\ie, weight change) during the global update step, and synchronizes this update for all local models. By this, FRLoRA performs global updates in a higher-rank parameter space, enabling a better representation of complex knowledge structure. Furthermore, FRLoRA  reinitializes the local low-rank matrices with the principal singular values and vectors of the pre-trained weights in each round, to calibrate their inconsistent convergence, thereby mitigating client drift. Our extensive experiments demonstrate that FRLoRA consistently outperforms various state-of-the-art FL methods across nine different benchmarks in natural language understanding and generation under different FL scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces FRLoRA, a novel Federated Learning (FL) method that addresses limitations in global knowledge learning by combining residual low-rank adaptation with periodic recalibration of local models. FRLoRA expands the effective parameter space during global updates and mitigates client drift by reinitializing local model components with principal components from the pre-trained model.  Extensive experiments across various natural language processing tasks demonstrate FRLoRA's superior performance compared to existing FL methods.

### Strengths
The paper is clearly presented. The proposed method is sound. Experiment results are comprehensive and validate the quality improvement of the proposed method.

### Weaknesses
This paper presents a novel Federated Learning method, FRLoRA, which aims to improve global knowledge learning. However, the paper's practical value is limited due to two main weaknesses:

Lack of a compelling use case: The authors fail to clearly motivate the need for their proposed method within a real-world application scenario. While the technical contributions may be sound, the lack of a clear practical context diminishes the paper's impact and relevance.

High communication cost: Despite claims of efficiency, the method introduces significant communication overhead, hindering its practicality in real-world deployments, where many LoRA customers care about.

### Questions
Can the authors should further explore and demonstrate the method's effectiveness in a specific application domain and address the communication cost limitations to enhance its practical value.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method known as FRLoRA (Federated Residual Low-Rank Adaption) to address the problem of Parameter-Efficient Fine-Tuning (PEFT) for Large Language Models (LLMs) in Federated Learning (FL) scenarios. FRLoRA updates global model parameters by introducing a residual low-rank matrix product and reinitializes local low-rank matrices in each training round to mitigate client drift. The paper compares FRLoRA with existing FL baseline methods across multiple datasets in natural language understanding and generation tasks, demonstrating its consistent superiority and validating the effectiveness of the proposed FRLoRA.

### Strengths
1. FRLoRA effectively addresses the significant impact of data heterogeneity on PEFT in FL scenarios by accumulating the product of residual low-rank matrices, enabling the global model to learn more comprehensive knowledge.
2. By reinitializing local low-rank matrices at each training round, FRLoRA alleviates client drift issues, enhancing the convergence and performance of the model.
3. Extensive experiments validate the performance improvements of FRLoRA over existing methods across various natural language processing tasks.

### Weaknesses
1. The updates derived from averaging the uploaded matrices A and B at the server differ from the averaged updates across clients, and this discrepancy is likely to amplify in heterogeneous data scenarios. [Improving LoRA in Privacy-preserving Federated Learning]
2. Although the paper proposes extending the parameter space through residual updates, it does not clearly specify whether the rank of the model parameters is strictly improved after each residual update, lacking further explanation on how this mechanism operates, particularly regarding its impact on model rank and representational capacity.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents Federated Residual Low-Rank Adaptation (FRLoRA), a federated learning method that improves LoRA for LLMs. FRLoRA overcomes challenges like constrained parameter spaces and client drift by updating in a higher-rank parameter space and reinitializing local low-rank matrices based on the principal singular values of pre-trained weights. Experiments show that FRLoRA consistently outperforms existing federated learning methods across benchmarks in NLU and NLG tasks.

### Strengths
1. The paper introduces a unique adaptation of LoRA for federated learning with residual low-rank updates and reinitialization in the principal singular space.

2. Extensive experiments on multiple benchmarks confirm FRLoRA’s robust improvements across NLU and NLG tasks in various federated settings.

### Weaknesses
1. The reinitialization of local low-rank matrices and the use of SVD may introduce significant computational overhead, particularly for large-scale models. An in-depth analysis of this aspect or potential optimizations would provide added value to the paper.

2. Although the method shows performance improvements overall, in Table 3, the proposed approach does not appear to dominate across all evaluations. A similar pattern is observed in Table 4, indicating that while the method is strong, it may not consistently outperform existing baselines in certain subcases.

3. While the paper briefly touches on SVD stability, it lacks a detailed analysis of potential impacts and does not explore alternative methods for scenarios where SVD might lead to convergence issues. Additional insights on this aspect could reinforce the robustness and general applicability of the approach.

### Questions
Q1: Could the authors provide further analysis on the computational impact of using SVD for reinitialization in terms of time and memory requirements?

Q2: Could the authors provide further analysis on the behaviour on Table 3 and 4?

Q2:How does FRLoRA handle scenarios where singular value decomposition may be unstable? Are there alternative initialization strategies?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper explores the challenges of using LoRA in Federated Learning (FL) for fine-tuning large language models (LLMs) on non-IID data. The authors identify that LoRA in FL struggles to learn global knowledge due to two key issues: extrinsic client drift and an intrinsic constrained update space. The authors propose FRLoRA (Federated Residual Low-Rank Adaptation) to overcome these challenges. FRLoRA initializes the LoRA matrices  $A$  and  $B$  using the Singular Value Decomposition (SVD) of the initial weights  $W_0$, while freezing the residual initial weight. During training, the locally updated LoRA matrices are aggregated and combined with the residual weight, creating the initial model for the next training round. This method addresses both client drift and limited update space, of which theoretical justification is presented. The experiments on nine language model benchmarks show that FRLoRA consistently outperforms various baseline methods.

### Strengths
**Addressing Non-IID Challenges in FL with LoRA:** FRLoRA tackles an important challenge in federated fine-tuning of LLMs by addressing both client drift and constrained parameter space through aggregated $\Delta W$ updates via SVD.

**Theoretical Justification:** The authors provide a simple theoretical justification of FRLoRA using a rank analysis of the parameter space, although the rank analysis can be far from the practice.

**Comprehensive Evaluation:** The study provides extensive experiments across nine benchmarks, covering Natural Language Understanding and Generation, validating FRLoRA’s efficacy in terms of performance and communication cost.

### Weaknesses
 **Insufficient Evidence on the Problem Formulation:** The authors characterize the client drift using Figure 1 (c-d) but it is not convincing. To be specific, the norm of $\Delta W$ and the standard deviation can be simply reduced by the other factors, e.g., learning rate. Perhaps, it would be better to (i) focus on a single round rather than the sequence of rounds and (ii) observe the distribution of cosine similarity rather than the standard deviation. It is also helpful to analyze the other FL methods. The analysis should also consider the impact of varying local update steps on the observed drift. Furthermore, the presented analysis does not sufficiently isolate the effect of non-IID data from other confounding factors, such as differences in client-specific learning rates or batch sizes, which could also contribute to the observed drift. A more rigorous approach would involve controlling for these variables to ensure that the observed drift is indeed due to data heterogeneity.

In addition, the authors claim that the constrained parameter space is one of the major problems in the naive method (FedAVG + LoRA). The simple rank analysis supports this claim. However, it is not thoroughly studied in empirical analysis. Hypothetically, the constrained parameter space problem can be simply addressed by employing large rank $r$. The paper lacks a systematic study on how the rank $r$ impacts the performance of FedAvg + LoRA, and whether increasing $r$ can achieve comparable results to FRLoRA. This analysis should include a comparison of the communication costs associated with different rank values, as well as the computational overhead of SVD initialization in FRLoRA, to provide a comprehensive understanding of the trade-offs involved.


**Limitations in Non-IID Testing Scenarios:** Experiments use a Dirichlet (0.5) Non-IID setting with five clients for binary classification, while NLG tests are performed on IID data. Broader Non-IID experiments would better showcase FRLoRA's robustness instead of just increasing the number of benchmarks. The current non-IID setting is relatively mild, and the paper would benefit from experiments with more extreme data heterogeneity, such as scenarios where clients have very few overlapping classes or where the data distributions are significantly different. This could be achieved by varying the Dirichlet parameter or using more complex data partitioning strategies. Furthermore, the paper should include a more detailed analysis of the performance of FRLoRA under different levels of data heterogeneity, to better understand its limitations and applicability in real-world scenarios.


**Limited Comparision to Existing Works:** The baselines used for comparison, such as FedYogi, FedAdam, and FedProx, do not integrate LoRA, making comparisons with these methods less relevant. Only FFA-LoRA offers a directly comparable baseline. Apparently, there is another LoRA method for FL, FlexLoRA (https://arxiv.org/abs/2402.11505, Feb 2024), in which a similar idea of using SVD per round is proposed. In addition, the idea of using the residual is analog to the one in Chain of LoRA (https://arxiv.org/abs/2401.04151, Jan 2024), which needs to be discussed. The paper should also include a discussion of the computational complexity of FRLoRA compared to other methods, particularly the overhead of performing SVD in each round, and how this impacts the overall training time. A more thorough comparison with existing methods, including a discussion of their limitations and advantages, would provide a more comprehensive understanding of the contributions of FRLoRA.

### Questions
## Questions 
**Does FRLoRA Fully Address the Intrinsic Challenge?**: While FRLoRA expands the parameter space globally, it does not necessarily address the constrained optimization space at the local level. Can the expanded global space fully mitigate intrinsic issues without modifying local optimization constraints?

**Catastrophic Forgetting at Low Ranks**: Direct updates to $W_0$ in a low-rank context may risk catastrophic forgetting. Can FRLoRA’s SVD initialization mitigate this risk, or could additional ablation studies on learning rates clarify this?

**Comparison to Chain of LoRA’s Residual Framework**: Both FRLoRA and Chain of LoRA use residual structures for fine-tuning. How does FRLoRA’s SVD-based initialization impact its effectiveness relative to the iterative approach of Chain of LoRA? Further analysis of residual efficacy could enhance the comparative evaluation.

**More Diverse Data Heterogeneity**: Is there an empirical study for NLG with severe heterogeneity?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the author proposes a novel framework named federated residual low-rank adaption to effectively fine-tune the pretrained large language model in a privacy-preserving manner. The proposed method addresses both the intrinsic problem caused by constrained parameter space and the extrinsic problem caused by the drift among clients. Extensive experiments on several datasets have shown the effectiveness of the proposed method.

### Strengths
1. The idea of enlarging the parameter space when finetuning large laugunge model in federated learning is promising.
2. The paper is well organized and the related works are thoroughly summarized.
3. The discussion of the weakness of exsiting related works and the novelty of the proposed method are clear.
4. The author conducts comprehensive experiments to demonstrate the effectiveness of the proposed method, which is convincing.

### Weaknesses
 1. In Eqs. (6) and (7), the author initializes the local low-rank matrices by the low-rank matrices reconstructed from the top singular values, while remaining the residual part as the global model . In my opinion, this makes the low-rank matrices retain the most information in the pretrained model, while the information remained in the global model can be significanly reduces.  However, in FL, the global model should contain more generalized information from the pre-trained model, which is contrast to the above parameter decoupling operation. So I am curious that whether this operation can reduce the generalization capacity or convergence speed of FL?

2. The motivation of the proposed low-rank matrice initilization lacks further discussion. Can the author provide more detailed discussion about this by such as landscape visualization?

3. Why the global model are initialized by the residual matrice? It seems that directly using the pre-trained model parameters as the global model can provide a more generalized initialization during the FL training. Can the author provide a more detailed discussion about this?

4. In Eqs. (13) and (14),  the author claims that by using residual accumulation, the model fine-tuned space can be expanded. However, Eq. (14) seems to only give a upper bound of the summed matrices rather than increasing its lowe bounder of the summed matrices. So it can not guarantee that the rank of the summed matrices can be increased by such a residual accumulation operation. Can the author provide a more in-depth discussion about this?

5. Actually, the standard PEFT by LoRa in FL can also be formulated as Eq. (13), with $\delta W^t$ as the global update of the LoRa parts at each global round. So what is the real differences between the standard method and the proposed FRLoRA?

### Questions
The items listed in the weaknesses. If the author can address or partially address these problems, I will be pleasure to improve my score.

### Soundness
2

### Presentation
3

### Contribution
2
