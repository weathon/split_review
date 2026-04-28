# RAC-LoRA: A Theoretical Optimization Framework for Low-Rank Adaptation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Fine-tuning has become a popular approach to adapting large foundational models to specific tasks. As the size of models and datasets grows, parameter-efficient fine-tuning techniques are increasingly important. One of the most widely used methods is Low-Rank Adaptation (LoRA), with adaptation update expressed as the product of two low-rank matrices. While LoRA was shown to possess strong performance in fine-tuning, it often underperforms when compared to full-parameter fine-tuning (FPFT). Although many variants of LoRA have been extensively studied empirically, their theoretical optimization analysis is heavily under-explored. The starting point of our work is a demonstration that LoRA and its two extensions, Asymmetric LoRA and Chain of LoRA, indeed encounter convergence issues. To address these issues, we propose a general optimization framework that rigorously analyzes the convergence rates of LoRA-based methods. Our approach inherits the empirical benefits of LoRA-style heuristics, but introduces several small but important algorithmic modifications which turn it into a provably convergent method. Our framework serves as a bridge between FPFT and low-rank adaptation. We provide provable guarantees of convergence to the same solution as FPFT, along with the rate of convergence. Additionally, we present a convergence analysis for smooth, non-convex loss functions, covering gradient descent, stochastic gradient descent, and federated learning settings. Our theoretical findings are supported by experimental results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper deals with the convergence issue in LoRA, by proposing a method that randomly initializes one matrice (A) and fixes it, while fully training the other one (B), in every step. The authors provide both empirical and theoretical motivations for this convergence issue of LoRA, and provide theoretical convergence guarantees for the proposed method. The proposed optimization method is evaluated on both convex problems, like simulated linear regression and classification problems, and also non-convex finetuning of language models.

### Strengths
1. This paper’s motivation is well-justified and tries to solve an important problem in the LoRA domain.
2. The solution is relatively simple and easy to implement.

### Weaknesses
1. There is still a gap between the theoretical analysis and the real LoRA setting, and the current analysis only works on smooth problems.

2. There is no evaluation in terms of training efficiency (beyond the number of parameters). Given now A or B needs to be fully trained, I assume training will be more time-cosuming. It would be nice to show the training curve and the convergence pattern in the NLP task as well. It would be nice to discuss what is the potential "cost" of utilizing this method, comparing to the original LoRA.

3. Proof of the analysis may depend on previous work, but it is not clear in the main paper, if we do not try to tease it out from the appendix. It would be nice to state clearly how things are proved so that it is easier to evaluate any theoretical contribution.

4.  The presentation in the technical sections is not very consistent and sound. See questions.

### Questions
1. In line 368, you mentioned the “smallest eigenvalues’’ in 5.1 but I believe there is no mention of that in 5.1. There is also a typo in line 352.

2. When discussing the related work in LoRA, the authors mentiond that “LoRA is highly sensitive to the choice of the hyper-parameters. A good theory should be able to explain or remove this issue.” So, for the proposed method, I was wondering whether the theory provides a recommended stepsize? How does it work in practice?

### Soundness
2

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
2

### Summary
This paper proposes a new Low-Rank Adaptation algorithm RAC-LORA and theoretically proves its convergence, which is lacking in other Low-Rank Adaptation algorithms. Experiments validate the effectiveness of the proposed algorithm.

### Strengths
1. The authors provide rigorous proofs for the convergence and convergence rate of RAC-LORA under the smoothness and PL conditions.
2. The authors demonstrate the superiority of their method for convex problems and problems under the condition of restricting the capacity of the low-rank adaptations.

### Weaknesses
For NLP tasks, the algorithm proposed by the authors shows no significant advantage in performance compared to existing methods. The authors did not discuss other potential advantages of the algorithm in depth, aside from the convergence guarantee of their algorithm. Please see the below comments about other weaknesses.

Significant issues
1. Could the authors clarify how the final output of RAC-LORA is selected in practice? Is it the low-rank matrix chosen uniformly at random according to the theory, or from the last iteration? What is the difference in performance between these two approaches in practice?
2. The process of RAC-LORA seems like unfolding the gradient-based optimization algorithm for solving Problem (1) in Line 104, where each part of the chain can be understood as a single step of gradient descent. Could the authors further explain the relationship between each step of RAC-LORA and each step of gradient descent used in LoRA, as well as the role of using a new randomized matrix at each step?
3. RAC-LORA requires calculating the pseudoinverse each step. Could the authors comment on its time efficiency compared to other algorithms?

Minor issues
1. Could the authors provide the performance of other algorithms on convex problems as discussed in Section 6.1? Is their performance similar to that in Figure 1?
2. In Line 342, it seems that letting $U=W^t, V=B_S^t \hat{A}^t$ does not lead to the inequality in Line 343.
3. Could the authors explain the meaning of "iteration" in Figure 4?

### Questions
Significant issues
1. Could the authors clarify how the final output of RAC-LORA is selected in practice? Is it the low-rank matrix chosen uniformly at random according to the theory, or from the last iteration? What is the difference in performance between these two approaches in practice?
2. The process of RAC-LORA seems like unfolding the gradient-based optimization algorithm for solving Problem (1) in Line 104, where each part of the chain can be understood as a single step of gradient descent. Could the authors further explain the relationship between each step of RAC-LORA and each step of gradient descent used in LoRA, as well as the role of using a new randomized matrix at each step?
3. RAC-LORA requires calculating the pseudoinverse each step. Could the authors comment on its time efficiency compared to other algorithms?

Minor issues
1. Could the authors provide the performance of other algorithms on convex problems as discussed in Section 6.1? Is their performance similar to that in Figure 1?
2. In Line 342, it seems that letting $U=W^t, V=B_S^t \hat{A}^t$ does not lead to the inequality in Line 343.
3. Could the authors explain the meaning of "iteration" in Figure 4?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel parameter efficient fine-tuning dubbed RAC-LoRA, for fine-tuning the large models. Specifically, the authors theoretically analyze the smooth issue in the vanilla LoRA type of algorithms and give motivating example about how existing LoRA algorithm can fail easily in simple case. Additionally, the authors establish the convergence rates for the non-convex objectives with gradient descent, stochastic gradient descent and federated learning setting. To validate RAC-LoRA, the authors leverage simple to complex models with a few datasets. The results show that RAC-LoRA performs competitively with other low-rank adaptation methods.

### Strengths
1. The investigated topic is very interesting and critical. Particularly, fine-tuning large models is the most popular method to enable models performing downstream tasks.
2. This work is motivated well through examples and theoretical analysis, on top of the existing methods. 
3. The literature survey looks extensive and thorough to include different LoRA variants.
4. The paper presents sufficient theoretical analysis to cover different objectives and algorithms for LoRA.
5. The proposed algorithm is validated through the empirical evidence.

### Weaknesses
1. The issue of Assumption 3.1. Though in this work, the authors point out the smoothness issue related to Assumption 3.1. However, they still use it, with Assumption 5.1. My first question is that, why the authors didn't directly address this issue to probably derive a new smoothness constant when the parameters have LoRA update. Specifically, the standard Lipschitz smoothness constant may not hold when the parameters are updated with the low-rank matrices. The authors should provide a detailed analysis on how the low-rank update affects the smoothness constant, instead of relying on the original smoothness assumption.

2. The issue of Assumption 5.1. This assumption seems a bit problematic in this work. Since the smallest eigenvalue of a projection matrix is 0, as pointed out in the paper. Then, the authors mentioned that "the smallest eigenvalue of the expected value of the projection matrix can be strictly greater than zero". However, the expectation of a projection matrix is still a projection matrix, which would have the smallest eigenvalue being 0. Though in the Remark, the authors have verified this, I am still a bit confused about this. The authors need to clarify how the expectation of a projection matrix can have a non-zero smallest eigenvalue, given that each individual projection matrix has a zero smallest eigenvalue. A more rigorous explanation with concrete examples would be beneficial.

3. Also, in Theorem E.2, the authors have defined the expected smoothness. Why do you need Assumption 3.1 again in the theorem statement? Typically, people would relax smoothness to expected smoothness, which is a weaker condition. Also, the notations in Assumption E.1. are not consistent. The authors should clarify the relationship between the standard smoothness assumption and the expected smoothness assumption, and why both are needed in the theorem statement. Additionally, the inconsistent notations in Assumption E.1 need to be addressed for clarity.

4. The proof techniques are fairly standard, but with the help from Assumption 5.1. However, to me, such an assumption didn't really help resolve the issue of Loss of Lipschitz smoothness presented in the paper. The authors should provide more insights on how Assumption 5.1 directly addresses the loss of Lipschitz smoothness, instead of just relying on the assumption. A more detailed explanation on the connection between the assumption and the smoothness issue is needed.

5. The experimental results on the image classification tasks to me are not promising. The authors should test their proposed algorithm on more complex datasets and larger models, such as CIFAR 100 with ResNet, instead of just MLP with MNIST. Also, it seems like freezing A matrix can yield the better results? From Table 2, the authors mentioned that "We find that RAC-LoRA performs competitively with other low-rank adaptation methods, but does not outperform Asymmetric LoRA despite having greater capacity". By looking at the results from Table, RAC-LoRA achieves 77.0 and Asymmetric LoRA gets 76.8. I wonder if the lower value, the better? Did I misunderstand here? It is good to see results on simple models and datasets, but to make the paper more technically solid and sound, more complex tasks are required. The authors should clarify whether higher or lower values are better for the reported metric, and provide more extensive experiments on complex datasets and models to validate the effectiveness of the proposed method.

6. Regarding the FL setting with RAC-LoRA, there are no results to validate the proposed algorithm and the corresponding analysis. The authors should present empirical evidence for the RAC-LoRA in the FL setting and show comparison with baselines. The lack of experimental results in the FL setting is a significant weakness. The authors should include experiments to validate the performance of RAC-LoRA in federated learning scenarios and compare it with existing baselines.

### Questions
Please see questions in the above comments.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces RAC-LoRA, a new framework that addresses the convergence issues of Low-Rank Adaptation (LoRA) methods. It provides theoretical guarantees that RAC-LoRA can converge to the same solution as full-parameter fine-tuning (FPFT) but with reduced computational costs. The framework supports various optimization settings, including gradient descent and federated learning. Experimental results confirm the effectiveness of RAC-LoRA, showing competitive performance with other low-rank adaptation methods.

### Strengths
1. The paper introduces RAC-LoRA, a novel framework that rigorously addresses the convergence issues of existing Low-Rank Adaptation (LoRA) methods. It provides strong theoretical guarantees, including proofs of convergence rates for various optimization settings, which fills a critical gap in the literature.
2. RAC-LoRA is versatile and applicable to a wide range of machine learning tasks. The framework is tested on both traditional convex problems like logistic and linear regression and more complex tasks involving multilayer perceptrons (MLPs) on MNIST and RoBERTa on the GLUE benchmark.
3. The paper is exceptionally clear in its exposition, with important concepts and technical details explained thoroughly, making it accessible and valuable for both researchers and practitioners.

### Weaknesses
1. The paper primarily focuses on theoretical analysis and provides empirical validation to support its claims. However, the empirical comparisons with other state-of-the-art low-rank adaptation methods could be more extensive. Additional benchmarks and real-world datasets might further strengthen the practical relevance of the proposed framework.

2. Fixing one of the two low-rank matrices A and B in LoRA and training only the other can establish theoretical convergence guarantees, but it also partially diminishes the learning capability of LoRA.

3. Some typos: line 167: choose, line 342 $U=W^{t+1}$, $V=W^t$

### Questions
1. Fixing one of the two low-rank matrices A and B in LoRA and training only the other might impair the learning capability of LoRA. Could the authors provide more experimental results, such as using LoRA for SFT (Supervised Fine-Tuning) on GPT models? Would RAC-LoRA perform better in such tasks?

### Soundness
2

### Presentation
3

### Contribution
2
