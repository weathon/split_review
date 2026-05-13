# Robustifying and Boosting Training-Free Neural Architecture Search

- Decision: Accept
- Scores: 8, 3, 5

## Abstract
\emph{Neural architecture search} (NAS) has become a key component of AutoML and a standard tool to automate the design of deep neural networks. Recently, training-free NAS as an emerging paradigm has successfully reduced the search costs of standard training-based NAS by estimating the true architecture performance with only training-free metrics. Nevertheless, the estimation ability of these metrics typically varies across different tasks, making it challenging to achieve robust and consistently good search performance on diverse tasks with only a single training-free metric. Meanwhile, the estimation gap between training-free metrics and the true architecture performances limits training-free NAS to achieve superior performance. To address these challenges, we propose the \emph{\underline{ro}bustifying} \textit{and} \textit{\underline{bo}osting} \textit{\underline{t}raining-free} \textit{NAS} (\alg{}) algorithm which \textit{(a)} employs the optimized combination of existing training-free metrics explored from Bayesian optimization to develop a robust and consistently better-performing metric on diverse tasks, and \textit{(b)} applies greedy search, i.e., the exploitation, on the newly developed metric to bridge the aforementioned gap and consequently to boost the search performance of standard training-free NAS further. Remarkably, the expected performance of our \alg{} can be theoretically guaranteed, which improves over the existing training-free NAS under mild conditions with additional interesting insights. Our extensive experiments on various NAS benchmark tasks yield substantial empirical evidence to support our theoretical results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces RoBoT, an algorithm for robustifying and boosting training-free neural architecture search (NAS). Motivated by the inconsistent performance estimation of existing training-free NAS metrics, this work proposes to explore a linear combination of multiple metrics that is more robust than each single metric, and exploit the robustified metric combination with more search budgets. The overall framework includes two stages. The first exploration stage employs Bayesian optimization (BO) to find the best linear combination weights for the robust metric. Then, in the second exploitation stage, the remaining search budgets are used to investigate the top-scoring architectures given by the robust metric. The proposed algorithm, RoBoT, is supported by both theoretical and empirical results.

### Strengths
- This work is built on existing training-free NAS methods, and extends them to a robustified ensemble. Therefore, the proposed framework is promising for future extension when better training-free NAS methods are discovered.

- Theoretical analysis is provided to understand the proposed algorithm, RoBoT.

- Extensive and solid experiment results on various datasets and settings are provided to demonstrate the efficacy of RoBoT.

### Weaknesses
 - Missing details regarding robust metric: It seems that some important details about the BO-searched robust estimation metric are missing. What are the base training-free metrics considered in the search? What are the optimized linear combination weights for them? Do they significantly differ on different datasets/tasks? It is unclear how the choice of base metrics impacts the final performance and whether the linear combination weights are stable across different tasks or if they require re-optimization for each new task. The lack of this analysis makes it difficult to assess the generalizability of the proposed approach.

- Recent NAS methods: It is suggested to include some more recent NAS methods into the comparison, e.g., Shapley-NAS [1], $\beta$-DARTS [2]. The current comparison is limited to older methods, and it is important to benchmark against state-of-the-art techniques to fully understand the contribution of the proposed method. The absence of these comparisons makes it difficult to assess the true advancement offered by this work.

Disclaimer: Although I know BO and NAS literature, I’m not familiar with the theoretical background in this work. Therefore, I cannot provide helpful feedback on the theoretical part. I would like to read how other reviewers think about the theoretical results.

### Questions
- In Table 3, why are the results on TransNAS-Bench-101 presented as the validation ranking? It seems to be inconsistent with the accuracy/error in the other two datasets (Tables 2 and 4). Also, the search costs are not listed in Table 3.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to tackle the research gap, the difference between training-free metrics with the final performance. This paper however, propose a weighted linear combination of traditional training free metrics as a estimator, where the weights are obtained automatically via Baysian optimization. Interestingly, this work use partial monitoring theory to prove their method has theoretical performance guarantee. Experiments are conducted on NASBench201.

### Strengths
Propose theory seems interesting

### Weaknesses
This paper aims to tackle the research gap, the difference between training-free metrics with the final performance. This paper however, propose a weighted linear combination of traditional training free metrics as a estimator, where the weights are obtained automatically via Baysian optimization. Interestingly, this work use partial monitoring theory to prove their method has theoretical performance guarantee. Experiments are conducted on NASBench201.

This paper does not read like an academic paper, where the introduction did not cover the full story. Their related work is quite short to cover the existing literature. I suggest the authors try to read more papers in this field instead of submitting their paper in a rush. Results on NASBench201 shows an incremental improvement without realistic benchmarking their method's performance. The method's reliance on Bayesian optimization, while automated, introduces a hyperparameter tuning step that is not thoroughly explored. The paper lacks a discussion on the sensitivity of the method to the choice of Bayesian optimization parameters, such as the acquisition function or the kernel used in the Gaussian process. Furthermore, the theoretical guarantees, while interesting, are not clearly linked to the practical performance gains observed in the experiments. The paper does not provide sufficient analysis on how the partial monitoring framework translates to the specific problem of training-free NAS, and whether the assumptions of the theory hold in this context.

### Questions
I found the author regularily let the reader "see later section" in their introduction, including Section 3 and section 4. I think this is a not a professional way to write the introduction. We should at least grasp the main idea when reading the intro but instead reading the entire paper.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes to find a linear combination of training-free metrics to boost the performance on NAS tasks. Specifically, the authors first train a GP to capture the relationship between weights of training-free metrics and the objective evaluation metric f and obtain a robust estimation metric $M^*$. Then the authors collect the queries during the training procedure of BO as $Q_T$. Finally, the authors utilize the learned $M^*$ as a performance estimator and adopt the greedy search to obtain the best architecture.

### Strengths
1.	The motivation, that using a linear combination of existing training-free metrics to obtain a robust estimation metric $M^*$, makes sense.

2.	Experiments on NAS benchmarks show the effectiveness of the proposed method.

### Weaknesses
1. The authors propose to train a BO to capture the relationship between the weight vector and the objective evaluation metric f. However, the queried architecture should be trained from scratch to obtain the objective evaluation during the BO stage, which seems to require large amounts of search costs since a standard BO procedure usually requires tens of queries. It is unclear how the authors mitigate the computational overhead associated with training each architecture from scratch for every BO query, especially since the paper mentions a standard BO procedure requires tens of queries.

BTW: What does $R_f(A)$ denote in Eq. 1? Does it represent the objective evaluation of an architecture? Since Alg.1 directly uses $f$ to denote the objective evaluation metric, I suggest the authors utilize the same notation.

2. I wonder about the effectiveness of the searched robust estimation metric $M^*$. According to Fig. 2, it seems that the optimal architecture has been found in less than 10 queries during the BO procedure. It shows that there is no need to conduct the greedy search through $M^*$, and BO is enough to get the optimal architecture. The paper does not provide a clear justification for why the greedy search is necessary after the BO phase appears to have already converged to a near-optimal solution. The marginal benefit of the greedy search given the BO results is not well-established.

3. Table 4 shows that RoBoT only requires 0.6 GPU-day to search, does it only count the search cost of the greedy search procedure? I wonder what is the cost of the BO stage, which I am afraid is much larger. The computational cost breakdown between the BO stage and the greedy search stage is not detailed enough, making it difficult to assess the true efficiency of the proposed method. The reported 0.6 GPU-day could be misleading if the BO stage is significantly more expensive.

### Questions
Please see the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
