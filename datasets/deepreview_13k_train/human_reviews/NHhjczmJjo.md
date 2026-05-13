# On the Learn-to-Optimize Capabilities of Transformers in In-Context Sparse Recovery

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
An intriguing property of the Transformer is its ability to perform in-context learning (ICL), where the Transformer can solve different inference tasks without parameter updating based on the contextual information provided by the corresponding input-output demonstration pairs. It has been theoretically proved that ICL is enabled by the capability of Transformers to perform gradient-descent algorithms~\citep{vonoswald2023transformers, bai2023transformers}. This work takes a step further and shows that Transformers can perform learning-to-optimize (L2O) algorithms. Specifically, for the ICL sparse recovery (formulated as LASSO) tasks, we show that a $K$-layer Transformer can perform an L2O algorithm with a provable {\it convergence rate linear in $K$}. This provides a new perspective explaining the superior ICL capability of Transformers, even with only a few layers, which cannot be achieved by the standard gradient-descent algorithms. 
Moreover, unlike the conventional L2O algorithms that require the measurement matrix involved in training to match that in testing, the trained Transformer is able to solve sparse recovery problems generated with different measurement matrices.  Besides, Transformers as an L2O algorithm can leverage structural information embedded in the training tasks to accelerate its convergence during ICL, and generalize across different lengths of demonstration pairs, where conventional L2O algorithms typically struggle or fail. Such theoretical findings are supported by our experimental results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a theoretical study of transformers to address the hypothesis regarding in-context learning for sparse recovery problems, as discussed in lines 62-65. Transformers are an integral part of modern deep learning architectures, and their contributions cannot be overstated. In particular, this work focuses on making theoretical claims that transformers can perform LISTA-type algorithms. The authors support this with a rigorous theoretical claim in Theorem 5.1, which demonstrates with high probability that transformers can recover the optimal sparse vector. Lastly, the authors empirically validate their claim in Figure 1.

### Strengths
**Strengths:**

1. **Strong Theoretical Contributions:**  
   The paper presents a compelling theoretical claim addressing a crucial aspect of machine learning with significant potential for diverse applications. Moreover, the proof techniques introduced are versatile and can be extended to other domains beyond sparse vector recovery, such as compressed sensing and various inverse problems.

2. **Clarity and Rigor of Proofs:**  
   The proofs are well-written and easy to follow, both in the main text and in the appendix.

3. **Robust Empirical Validation:**  
   The empirical experiments are thorough and effectively corroborate the theoretical findings

### Weaknesses
The hypothesis outlined in lines 62-65 appears somewhat disconnected from the application to sparse recovery. The connection between in-context learning (ICL) and sparse recovery is not clearly established, making it challenging to understand why this particular relationship is being explored.

### Questions
1). Could the authors clarify their rationale for choosing to study this problem in the context of sparse vector recovery and explain how it relates to the hypothesis presented in this work?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors leverage the ability of Transformers to perform in-context learning (ICL) for solving the sparse recovery problem. It is shown that the Transformers can implement first-order optimization algorithms (such as ISTA) and their learned variants (e.g., LISTA) for sparse approximation. Moreover, it is shown theoretically that a K-layer transformer has a linear convergence rate in K (with high probability). The ability of transformers to solve the sparse recovery problem corresponding to a different sensing matrix than what it was trained on is also demonstrated.

### Strengths
1. The theoretical insights on the versatility of the transformer architecture are interesting and useful for a broader class of problems. For example, the fact that LISTA-type algorithms can be implemented using a transformer opens up the possibility of using transformers for building more powerful learned reconstruction operators for more general inverse problems. 

2. The convergence rate results (for sparse estimation and prediction) place the proposed approach on a concrete theoretical footing. 

3. Generalizability to a different sensing matrix during the inference time is a very powerful property of a learned approach, which (in my knowledge) is not generally possessed by standard learned reconstruction operators trained on a specific measurement matrix.

### Weaknesses
1. The notion of ICL in the context of sparse recovery is not very well explained. I would suggest rewriting Sec. 4.1 with a better explanation of the setup (i.e., exactly what the model is trained on and what exactly is given as input to the model during inference). Specifically, it is unclear how the training data is generated, what the input to the transformer consists of (e.g., is it the measurement vector concatenated with the sensing matrix, or something else?), and how the model is expected to generalize to new sensing matrices at inference time. A more detailed explanation of the data generation process and the input format is needed to fully understand the ICL setup.

2. The convergence result (Theorem 5.1) merely ascertains the existence of a set of parameters such that the recovery is accurate with high probability, and does not state anything about the convergence of a pre-trained transformer on a new problem instance. It is not clear how this theoretical result translates to the practical performance of a pre-trained transformer when applied to a new, unseen sparse recovery problem. The theorem provides a bound on the performance of an *ideal* transformer, but it does not address the convergence behavior of a transformer trained using a practical algorithm on a finite dataset. The gap between the theoretical result and the practical implementation needs to be addressed.

3. The phrase L2O is not appropriate in the context of this paper (or any approach for constructing a learned network to solve an inverse problem for that matter). These methods essentially try to approximate the conditional mean of the parameter of interest given the measured data and do not find an approximation to a variational reconstruction problem such as LASSO (not without any constraints on the learnable units in the architecture, at least).

4. How does a K-layer pre-trained transformer perform if more layers are added during the inference time (by extending the learned layers using some reasonable strategy)? If this leads to divergence, it would not be appropriate to claim that this approach learns to approximate the LASSO solution. This just gives us a more powerful and expressive architecture that does a better job of approximating the conditional mean estimator of the underlying sparse vector from its linear measurement. The behavior of the model with increased layers during inference needs to be investigated to support the claim of learning an optimization algorithm.

5. Could you explain whether Figure 1 considers the same sensing matrix during training and inference? Maybe I missed it, but I was not able to figure it out from Section 6. The experimental setup in Figure 1 needs to be clarified, specifically whether the sensing matrix is fixed or varying during the inference phase for the proposed method and the baselines.

6. How is the support constraint incorporated into your framework? In particular, why does the performance of the proposed method improve with these constraints, while the other baseline methods perform roughly the same? The mechanism by which the support constraint is incorporated and its impact on performance needs to be better explained. It is unclear why the proposed method benefits from this constraint while other methods do not.

7. While first-order optimization methods for LASSO can only achieve a sublinear rate (and not anything faster, provably), the result in Theorem 5.1 appears paradoxical. I would suggest highlighting the key differences in the setting and assumptions made in the optimization literature and this work to make this bit clear. I understand that the rate in Theorem 5.1 holds with high probability, but is it possible to construct a sparse signal for which a pre-trained transformer fails to achieve a linear rate? The theoretical result needs to be contextualized within the existing optimization literature, and the limitations of the result need to be discussed.

8. Assumption 1 seems somewhat non-standard to what is generally assumed about the sensing matrix in the compressed sensing literature. For instance, a Gaussian sensing matric would not satisfy this assumption. The implications of this assumption and its limitations need to be discussed, especially in the context of more common sensing matrix models.

### Questions
- In my opinion, the phrase L2O is not appropriate in the context of this paper (or any approach for constructing a learned network to solve an inverse problem for that matter). These methods essentially try to approximate the conditional mean of the parameter of interest given the measured data and do not find an approximation to a variational reconstruction problem such as LASSO (not without any constraints on the learnable units in the architecture, at least). 

- How does a K-layer pre-trained transformer perform if more layers are added during the inference time (by extending the learned layers using some reasonable strategy)? If this leads to divergence, it would not be appropriate to claim that this approach learns to approximate the LASSO solution. This just gives us a more powerful and expressive architecture that does a better job of approximating the conditional mean estimator of the underlying sparse vector from its linear measurement. 

- Could you explain whether Figure 1 considers the same sensing matrix during training and inference? Maybe I missed it, but I was not able to figure it out from Section 6. 

- How is the support constraint incorporated into your framework? In particular, why does the performance of the proposed method improve with these constraints, while the other baseline methods perform roughly the same?

- While first-order optimization methods for LASSO can only achieve a sublinear rate (and not anything faster, provably), the result in Theorem 5.1 appears paradoxical. I would suggest highlighting the key differences in the setting and assumptions made in the optimization literature and this work to make this bit clear. I understand that the rate in Theorem 5.1 holds with high probability, but is it possible to construct a sparse signal for which a pre-trained transformer fails to achieve a linear rate? 

- Assumption 1 seems somewhat non-standard to what is generally assumed about the sensing matrix in the compressed sensing literature. For instance, a Gaussian sensing matric would not satisfy this assumption.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper threw an interesting hypothesis: the trained transformers essentially play the role of the L2O algorithm when solving the inverse problem. Enriched theory analysis and derivation are proposed, which are almost correct. This hypothesis is validated underlying a sparse recovery problem with respect to ISTA-based alternating algorithms. The fundamental idea can be summarized as proving the convergence and accuracy follow a similar criterion in ISTA-variant algorithms. Simulations on the trained transformer and ISTA-based algorithms for solving sparse recovery tasks are presented, and the blind inverse problem is particularly picked out to show the stronger performance of the transformer, and thus leads to the L2O capability.

### Strengths
The manuscript is articulated with clarity and is accessible for comprehension. 
The proposed hypothesis presents a valuable avenue for in-depth analysis. 
Preliminary concepts are provided with comprehensive equations and definitions. 
Elaborate proofs are accessible in the appendix. 
The quality of English is commendable and articulated naturally.

### Weaknesses
I made a rejection at this stage as the following shortbacks, I am willing to change my score after the rebuttal phase with respect to the author's responses.
1. The entire work is divided. The primary concept, prove that transformer has the L2O approximation capability in forward process, is isolated to the main task, sparse recovery problem. In this version ,this paper tends to mash-up the L2O approximation on transformer and sparse recovery problem. Essentially, each of them deserves to publish an independent paper. 
2. Followed by 1, this causes the following issues: i) no analysis and illustrations on the necessity of L2O for sparse recovery tasks; ii) the bridge between the fundamental proofs and evaluation tasks is fragile; iii) the increments of this paper compared to . Von Oswald et al. (2023a) and  Bai et al. (2024) are invisible, though the authors claim the difference is the L2O consideration.
3. The writing of this paper is also a mixture. The logical flow of the introduction is saltatory. The fundamental motivation is not clear enough to convince me that the L2O algorithmic principle is the explanation of the success of the transformer because of there are L2O-based algorithms that achieve similar performance. 
4. The whole section 3 is overwhelming. I don't think it deserves so much context to present details network layer symbols and definition. Besides, Definition 3.1-3.3 is kind of a definition abuse. I highly suggest a concise and shorter version of this section.
5. The key parts, Sections 4.3, 5.1, and 5.2, show a trivial way of proving the author's hypothesis. Performing LISTA-type algorithms do not provide a direct derivation of the L2O of the transformer forward process, at least to me. 
6. Last but the most fatal issue lies in simulation. The authors tend to show the superior performance of a trained transformer compared to those alternating minimization-based ISTA-type algorithms, concluding the L2O capability of transformer in the blind inverse problem of sparse recovery where matrix X is not given. This is unfair and not reasonable. The trained transformer obviously surpasses those model-based algorithms which are designed for matrix X is given. The transformer solves the blind inverse problem due to the data-driven prior from the training process, instead of L2O capability that focuses on improving the optimization strategy during the iterations. A fair comparison should be set among algorithms with learning ability and capable of solving blind inverse problems, such as
[1] Zero-shot image restoration using denoising diffusion null-space model
[2] Metalearning-based alternating minimization algorithm for nonconvex optimization
[3] Invertible Diffusion Models for Compressed Sensing
[4] OmniSSR: Zero-shot Omnidirectional Image Super-Resolution using Stable Diffusion Model
[5] Blind Super-Resolution Via Meta-Learning and Markov Chain Monte Carlo Simulation

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors of this paper study sparse recovery using transformers in an in-context scenario. They provided theoretical results and conducted experiments regarding the ability of transformers to execute an L2O algorithm.

### Strengths
The paper is well-written, with clearly presented theoretical findings and compelling experimental results. The insights are both intriguing and hold valuable potential for contributing to the scientific community.

### Weaknesses
I have two concerns which should be better explained in the paper:
- The embedding form in Equation 4.2 appears somewhat ad hoc; do you have any references supporting this choice? I understand that this choice is closely tied to the design of the four attention heads in Appendix C1, so I wonder: are alternative forms feasible, and if so, how might they impact the theoretical results? Specifically, it's unclear why the embedding uses a concatenation of the input vector, a placeholder, and an indicator, rather than a more standard approach like a learned embedding matrix. The current form seems overly specific to the LISTA-VM algorithm and may not generalize well to other L2O algorithms. It would be beneficial to explore the theoretical implications of using different embedding strategies, such as those that incorporate positional information or use a more generic learned representation.

- In the experimental section, the authors test with GPT-2 using 8 heads, which differs from the 4-head configuration in the theoretical analysis. What motivates this discrepancy? Additionally, I encourage the authors to discuss how varying the number of heads might affect the theoretical findings. The use of GPT-2, a model with a different architecture and a larger number of heads, introduces a significant gap between the theoretical framework and the experimental setup. It is not clear whether the observed performance of GPT-2 can be directly attributed to the theoretical properties established for the 4-head model. Furthermore, the paper lacks a discussion on how the number of attention heads impacts the convergence rate and the overall effectiveness of the in-context learning algorithm. A more thorough analysis of this aspect is needed to bridge the gap between theory and practice.

### Questions
See in the comments in Weakness.

### Soundness
3

### Presentation
4

### Contribution
4
