# On the Universality of Self-Supervised Representation Learning

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 6, 3, 6, 5

## Abstract
In this paper, we investigate the characteristics that define a good representation or model. We propose that such a representation or model should possess universality, characterized by: (i) discriminability: performing well on training samples; (ii) generalization: performing well on unseen datasets; and (iii) transferability: performing well on unseen tasks with distribution shifts. Despite its importance, current self-supervised learning (SSL) methods lack explicit modeling of universality, and theoretical analysis remains underexplored. To address these issues, we aim to explore and incorporate universality into SSL. Specifically, we first revisit SSL from a task perspective and find that each mini-batch can be viewed as a multi-class classification task. We then propose that a universal SSL model should achieve: (i) learning universality by minimizing loss across all training samples, and (ii) evaluation universality by learning causally invariant representations that generalize well to unseen datasets and tasks. To quantify this, we introduce a 
$\sigma$-measurement that assesses the gap between the performance of SSL model and optimal task-specific models. Furthermore, to model universality, we propose the GeSSL framework. It first learns task-specific models by minimizing SSL loss, then incorporates future updates to enhance discriminability, and finally integrates these models to learn from multiple mini-batch tasks. Theoretical and empirical evidence supports the effectiveness of GeSSL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduce a new self-supervised learning (SSL) framework to improve the universality by explicitly modeling discriminability, generalizability, and transferability. The method combines self-motivated target learning, multi-batch collaborative updates, and task-based bi-level optimization to better balance model performance across different tasks and domains. The approach is validated on multiple scenarios (unsupervised learning, semi-supervised learning, transfer learning, few-shot learning) showing consistent improvements over existing SSL methods.

### Strengths
1. Different from previous works that mainly focus on discriminability, the authors propose to use a self-motivated target and bi-level optimization to explicitly model universality properties, leading to more robust and transferable models.


2. The authors have conducted comprehensive experiments across multiple learning paradigms and datasets. Thorough ablation studies demonstrate the necessity of each component (self-motivated target, multi-batch updates, bi-level optimization). The theoretical analysis provides performance guarantees through the $\sigma$-measurement and proves convergence properties.

3. The proposed method can be applied to enhance various existing SSL methods. The extensive empirical results demonstrate consistent improvements when integrating GeSSL with different baseline approaches like SimCLR, MoCo, BYOL etc., showing the broad applicability of the proposed method.

### Weaknesses
1. It remains unclear to me why using KL divergence alone is sufficient for measuring distribution differences in the self-motivated target. The authors argue that KL divergence better reflects the uncertainty between distributions compared to other metrics like MSE or cross-entropy, but don't fully explain why this specific choice leads to optimal universality properties compared to alternatives like Wasserstein distance. Specifically, the argument that KL divergence captures uncertainty better is not sufficient; a more detailed explanation of how this uncertainty translates to improved universality is needed. Furthermore, while KL divergence is non-negative and zero only when distributions are identical, this property is shared by other metrics, so the unique advantage of KL divergence in this context is not fully justified.

2. My another concern is how the method balances computational efficiency with model performance. While the authors demonstrate performance improvements, the bi-level optimization introduces additional memory overhead and computational complexity. The optimal trade-off between efficiency and universality lacks thorough analysis, especially for resource-constrained scenarios. The use of approximate implicit differentiation is mentioned, but the practical impact on training time and memory footprint compared to standard SSL methods is not sufficiently detailed. A more rigorous analysis of the computational overhead, including wall-clock time and memory usage, across different batch sizes and model architectures is needed to fully assess the practicality of the proposed approach.

### Questions
1. Why choose KL divergence over alternatives like Wasserstein distance? Were there any empirical observations that led to this choice?

2. In Section 3.3, you mention K is typically set to 1 due to batch size and training complexity constraints. Could you elaborate on how sensitive the model performance is to different K values?

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
4

### Summary
The authors propose that a robust representation or model should exhibit universality, defined by three core attributes: (i) discriminability—performing well on training samples; (ii) generalization—achieving strong performance on unseen datasets; and (iii) transferability—adapting effectively to new tasks with distribution shifts. To explicitly capture universality within the self-supervised learning (SSL) process, the authors introduce a novel framework, GeSSL. GeSSL employs KL divergence to distill knowledge from future states into the current state, thus lowering training loss; it promotes generalizability by extracting causal features through multi-task learning (multiple mini-batches); and it incorporates a bi-level optimization mechanism to structure SSL learning in a meta-learning format, enhancing transferability.

### Strengths
The paper is easy to follow, though the abstract is somewhat overwhelming.

The authors conduct comprehensive experiments across a diverse range of applications and datasets, effectively demonstrating the proposed method's effectiveness.

### Weaknesses
1. Some important information, such as the classifier $\pi$, the parameter M and reference, is not well-described in the paper. Please see the questions section for more details. Clarifying these aspects would greatly enhance the reader's understanding of the paper.

&nbsp;

2. Section 2: Treating each mini-batch in the SSL training phase as a multi-class classification task is well-established in the SSL literature. For example, contrastive loss, widely used in frameworks like SimCLR and MoCo, functions as an instance discriminator [1,2,3]. The authors should acknowledge this in the text.


&nbsp;

3. I think as the authors state MEASUREMENT OF UNIVERSALITY is one of main contribution, F.4 should be appear as the result on the main text.


### Questions
**Q1:** Line 149-153: "According to Theorem 9 in Ahuja et al. (2020), if a model achieves good performance across multiple different tasks, it can be considered to have learned causal representations. Moreover, Schölkopf et al. (2021) and Ahuja et al. (2023) conclude that causality in representations is a sufficient condition for generalizability. Thus, a generalizable representation should be causally invariant across multiple tasks, enabling the model to achieve very low loss on these tasks using the same representation"

The authors refer to Theorem 9 in Ahuja et al. (2020), but I was unable to find it in that paper. Furthermore, as I understand it in the context of causal representation, multitasking for causal representation implies using a shared representation, z=f(x), to perform multiple tasks on the same representation. However, in GeSSL, multitasking is applied across different mini-batches (i.e., different samples x), which do not yield the same representation. This approach may still allow the model to rely on spurious features for good performance. Could the authors clarify this?

&nbsp;

**Q2:** The authors repeatedly mention employing the classifier $\pi$ to output class probabilities for the mini-batch, but I couldn't find any part of the paper describing how this is obtained. 

Additionally, if π is a classifier per mini-batch, it would need to be retrained at every iteration. On the other hand, if $\pi$ is a classifier for the entire dataset, does that imply prior knowledge of the task before training?

&nbsp;

**Q3:** (σ-measurement): When referring to π in the context of $\sigma$-measurement, does π denote tasks like LIN, SEMI, or AP for image-based examples? I’m unclear on how the model is evaluated using $\sigma$-measurement in the ablation study F.4: Universality of Existing SSL Methods. Could the authors clarify? 

Additionally, since the authors identify the measurement of universality as a primary contribution, F.4 should appear as a main result in the core text.

&nbsp;

**Q4:** GeSSL processes M mini-batches simultaneously during training:
-I couldn’t find any information on the size of M or any ablation study regarding M.

- Since SSL performance is highly dependent on batch size, it would be beneficial if the authors compared GeSSL with a baseline that uses M× the original batch size.

In Table 20, the model analysis includes parameter size, training time, and performance, showing that GeSSL achieves better results than the baseline with less training time (in hours). However, GeSSL’s optimization is more intensive, utilizing ($\lambda=10$) and a second-order gradient-based approach. Does this mean GeSSL requires fewer epochs to converge? If so, Table 9 shows some baselines achieving better performance in 400 epochs than GeSSL does in 1000 epochs.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper aims to formalize the notion of "goodness of a representation". The authors introduce the definition comprising three simple characteristics of a representation to be good: (i) discriminability, (ii) generalization and (iii) transferability. Furthermore, the authors develop the methodology that instantiates this definition. This methodology is compatible with existing SSL approaches. The authors evaluate the proposed approach on a variety of tasks and in conjunction with a few SSL methods.

### Strengths
* The proposed methodology is compatible with many existing SSL methods and leads to their improvements.

### Weaknesses
 * The presentation of the paper does not convincingly demonstrates the novelty behind the proposed definitions for the representations to be "good". Specifically, the stated principles are already the ultimate goal of the entire representation learning community, thus, it is not clear what specifically novel authors introduce in their narration.

* Given that the proposed methodology is applied to existing SSL methods, the results demonstrate only minor quantitative improvements upon the corresponding SSL method.

### Questions
* I suggest authors to restructure their tables and display the results of their method next to the corresponding used SSL method to simplify parsing the results.

* Given that authors propose new definitions and argue that the existing approaches do not meet these definitions, I would expect some experimental evidence towards to support this.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on a news representation quality evaluation of self-supervised learning (SSL) frameworks. In particular, the authors first introduce a definition for SSL universality, which combines three available factors, including discriminability, generalizability, and transferability, together with a σ-measurement to quantify it. They next propose GeSSL, a novel framework that models universality by unifying a self-motivated target for discriminability, a multi-batch collaborative update mechanism for generalizability, and a task-based bi-level learning paradigm for transferability. Experimental results on benchmark datasets demonstrate the superior performance of GeSSL compared to the original baselines.

### Strengths
The paper is well-written and easy to follow. Its idea of introducing a definition of measurable universality for SSL settings and a novel SSL framework (GeSSL) is novel and interesting. The experimental results on several benchmark datasets consistently show the benefit of using GeSSL compared to the mentioned self-supervised baselines.

### Weaknesses
My major concerns are about the actual novelty and the theoretical part of the paper. In particular:
- The definition of universality (Def. 3.1) is not mathematically well-defined since it contains several unclear terms, such as "competitive performance", "quickly", "few samples", and "comparable performance". I suggest the authors provide precise mathematical definitions or quantitative thresholds for these terms. For example, what specific metrics or benchmarks would constitute "competitive performance"? What time or iteration limit defines "quickly"? What fraction of the total dataset constitutes "few samples"? This would help make the definition more rigorous.
- The definition of a "$\sigma$-measurement" (Def. 3.2) is not well-defined since we do not know the term $f_{\Phi_l}^{*}$. Also, it is not unclear how the KL term in Eq. (1) is computed. Could the authors explicitly define $f_{\Phi_l}^{*}$ and provide more details on how the KL divergence is calculated in practice, including any approximations or estimation techniques used? Specifically, what is the target distribution that the model is trying to match when calculating the KL divergence, and how is this target distribution derived from the task-specific optimal model?
- The main theoretical contribution of the paper (Theorem 4.1) is not very meaningful. In particular, assuming that the proof is true (I did not have enough time to carefully verify it), the inequality $\tilde f_\theta - f_\theta \leq 0$ does not imply that $\tilde f_\theta$ is a good approximation of $f_\theta$.  I suggest the authors provide additional theoretical results or empirical evidence to demonstrate the practical significance of this inequality. For example, what does this inequality imply about the performance or convergence of the algorithm in practice? Also, it would be better to provide the upper bound of $\|\tilde f_\theta - f_\theta\|$.
- As mentioned in the paper (lines 193-294), GeSSL seems to be a computationally expensive and not scalable method since it requires the computation of the second-order derivatives (Hessian) w.r.t the (high-dimensional) parameters. Could the authors provide a more detailed analysis of the computational complexity of their method, perhaps including comparisons with existing approaches? Also, can the authors discuss potential approximations or optimizations that could make the method more scalable for high-dimensional problems? It would be beneficial to understand how the computational cost scales with the size of the model and the dataset.

### Questions
Please see my comments about the weaknesses of the paper.

### Soundness
3

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
This paper advances self-supervised learning (SSL) by defining "Universality," which includes discriminability, generalizability, and transferability. This paper introducs GeSSL, a framework that models universality by enhancing discriminability with Kullback-Leibler divergence, promoting generalizability through causal feature extraction across tasks, and implementing a bi-level optimization for transferability.

### Strengths
This paper introduces a comprehensive framework for incorporating universality into self-supervised learning (SSL) by defining it through discriminability, generalization, and transferability. The σ-measurement quantifies performance gaps, strengthening the theoretical foundation of SSL methods. The GeSSL framework effectively integrates task-specific learning and focuses on causally invariant representations, enhancing adaptability and performance across diverse tasks. Overall, the paper addresses critical gaps in SSL methodologies and presents a novel approach supported by theoretical and empirical evidence.

### Weaknesses
1.The self-supervised learning (SSL) paradigm requires algorithms to exhibit good alignment and uniformity. However, the concepts of discriminability and alignment mentioned in the paper seem to overlap. Similarly, generalizability and transferability appear to be closely related to uniformity, as improved uniformity is essential to prevent collapse and ensure good generalizability and transferability of the model.

2.In line 230, the paper mentions M mini-batches. If these M mini-batches are assumed to be independently and identically distributed (i.i.d.), it raises concerns about how diversity between different mini-batches is guaranteed. If the diversity is insufficient, the assumption that supports the model’s effectiveness may not hold.

3.Meta-learning typically requires longer run times, raising questions about the relationship between the running time of this algorithm and that of the original methods. For instance, it would be beneficial to compare the time taken to run one epoch of SimCLR with the time required when incorporating the proposed algorithm. This comparison could provide insights into the practical implications of adopting the new method.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2
