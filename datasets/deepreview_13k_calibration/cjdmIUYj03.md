# On the Generalization of Temporal Graph Learning with Theoretical Insights

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 3, 8

## Abstract
Temporal graph learning (TGL) is a widely-used technique in various real-world applications, but its theoretical foundations remain largely under-explored. In this paper, we fill in this gap by studying the generalization ability of different TGL algorithms (e.g., GNN-based, RNN-based, and memory-based methods) under the finite-wide over-parameterized regime. We establish the connection between the generalization error of TGL algorithms and \circled{1} "\textit{the number of layers/steps}" in the GNN-/RNN-based TGL methods and \circled{2} "\textit{the feature-label alignment (FLA) score}", where FLA can be used as a proxy for the expressive power and explains the performance of memory-based methods. Guided by our theoretical analysis, we propose \textit{\textbf{S}implified-\textbf{T}emp\textbf{o}ral-Graph-\textbf{Ne}twork} (SToNe), which simultaneously enjoys a small generalization error, the better overall performance, and a lower model complexity. Extensive experiments on real-world datasets demonstrate the effectiveness of SToNe. This paper provides critical insights into TGL from a theoretical perspective and paves the way for designing practical TGL algorithms in future studies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The submission addresses the increasingly researched direction of learning temporal graph structures, which is significantly more challenging compared to static graph learning. While multiple methods have been proposed, there is not yet a good understanding of when or why certain methods outperform others, in particular in terms of how well they predict temporal interactions between nodes in the future. This lack of understanding is something this manuscript aims to address by establishing an upper bound for the expected error in predictions in various proposed temporal graph learning frameworks. In particular this upper bound depends (in an increasing way) on the number of layers in the GNN and RNN based methods, the Lipschitz constant of the activation function in the memory based method, and the feature-label alignment score (FLA) in all considered methods.
This is taken as guiding principle to propose a new method with few layers and small FLA, the latter of which is achieved by a selection of some of the most recent interactions as input data. The proposed new method is shown to behave well (i.e. comparatively or better) in terms of generalizability as well as FLA and running time compared to methods from previous literature.

### Strengths
I believe the considered problem of temporal graph learning is relevant and fitting for ICLR. Also the more specific goal of explaining and justifying certain design choices of frameworks to learn temporal graphs is well-motivated. The empirical results suggest that the features identified as important for low generalization error, namely a small number of layers and small FLA, indeed are worth constraining when designing algorithms for temporal graph learning.

### Weaknesses
I do not see the formal and strong theoretic claim that the submission frames its theoretic contribution as strong. Specifically, since the given result only established an upper bound, I believe strictly speaking it can merely indicate desirable aspects of methods for temporal graph learning, and not really explain the difference in performance. This is because we have no lower bound relating the generalization error to e.g. the number of layers. This means a small number of layers gives us a good bound on the expected error with high probability, but a larger number of layers does not necessarily lead to  a large expected error.

Minor comments:
- abstract: *a* better overall performance
- page 1, last line: *has* demonstrated that simple
- if my major concern is correct, if would be better to say in the caption of Fig 1: Relationship between the *bound on the* generalization error
- page 4: I think it would be good to introduce the notation used in the definition of loss^{0-1}_i
- Algorithm 1: condition*ed*
- Assumption 1: *have* \ell_2-norm
- Thm. 1: R is fixed twice in the theorem statement
- page 8: could be *thought* of
- page 8: "compatible" is probably the wrong word here. I would suggest competitive or comparable

### Questions
Can you discuss my concerns about the framing of the theoretical contributions?

Can you give a formal argument of why memory blocks increase the FLA? Is this always true? (In particular my question relates to the second bullet on the top of page 7.)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considered the generalization bound for three methods of the temporal graph learning. It is the first attempt to reveal the relevance of the feature-label alignment in the performance of algorithms in this task theoretically. It also designed a more efficient algorithm for this task based on their theoretical results.

### Strengths
In general, it is quite interesting to study the interaction of FLA and the model performance. This paper introduced this idea to the temporal graph learning task and designed a novel model based on their theoretical findings. I believe both the originality and quality of the idea is great. The main body of this paper is also well organized.

### Weaknesses
The main weakness from my perspective is the vagueness of the proof for the main theorems. 

1. I think the discussion of the existing generalized bounds for GNN and so on should be elaborated on more in the literature review part and the comparison with the novel bound derived in this paper should be provided. Specifically, how does the proposed feature-label alignment (FLA) bound compare to data-independent bounds like Rademacher complexity or PAC-Bayesian bounds, which are commonly used for analyzing GNNs? What are the key differences in assumptions and implications?

2. The definition of FLA depends on the gradient of $f$ with respect to $	heta$. However, the ReLU networks are non-smooth, which may make FLA undefinable. The gradient of ReLU is not defined at 0. How is this handled in the computation of FLA, both theoretically and practically?

3. In the statement of Theorem 1, when $	heta_0$ is randomly initialized, $R$ should be a random variable. It is vague to compare two random variables in the result in theorem 1. How should the comparison between two random variables, specifically the FLA constant $R$ under different initializations, be interpreted in Theorem 1?

4. Based on your findings, SToNe outperforms other methods due to its smaller FLA and thus smaller generalization bound. I am curious about the comparison of FLA of the different methods in those real datasets. The current experiments to illustrate the effect of FLA are all on SToNe itself. It would be valuable to see empirical FLA comparisons across different methods on real datasets to further validate the theoretical claims.

The following are some questions in the proofs.

5. The proof of lemma 5 relies on the upper bound of $\|\partial loss_i(\theta)/\partial W^{(l)}\| $ for $\theta$ from the iteration of SGD. This upper bound is obtained in lemma 4, which is built on lemma 8 from Zhu et al. (2022) [1]. However, in that paper, they assumed that $W$ is a guassian random matrix, which is different in this paper (note that in this case, $W$ is obtained from SGD). Hence, i don't think that lemma can be applied here and there are some flaws in upper bounding $\|\partial loss_i(\theta)/\partial W^{(l)}\|$.

6. In the proof of Theorem 2, the part of constructing $f'\in \mathcal{F}(\theta_0,R)$ such that $\psi$ can be upper bounded by $1/\sqrt{N}$ is confusing (e.g., why $\langle \nabla_\theta f_i(\theta_0),\theta \rangle =y_i(B+B')$). I can't get the point how $R$ can make a difference in the result.

### Questions
1. I think the discussion of the existing generalized bounds for GNN and so on should be elaborated on more in the literature review part and the comparison with the novel bound derived in this paper should be provided. 
2. The definition of FLA depends on the gradient of $f$ with respect to $\theta$. However, the ReLU networks are non-smooth, which may make FLA undefinable. 
3. In the statement of Theorem 1, when $\theta_0$ is randomly initialized, $R$ should be a random variable. It is vague to compare two random variables in the result in theorem 1.
4. Based on your findings, SToNe outperforms other methods due to its smaller FLA and thus smaller generalization bound. I am curious about the comparison of FLA of the different methods in those real datasets. The current experiments to illustrate the effect of FLA are all on SToNe itself.

The following are some questions in the proofs.

5. The proof of lemma 5 relies on the upper bound of $\|\partial loss_i(\theta)/\partial W^{(l)}\|$ for $\theta$ from the iteration of SGD. This upper bound is obtained in lemma 4, which is built on lemma 8 from Zhu et al. (2022). However, in that paper, they assumed that $W$ is a guassian random matrix, which is different in this paper (note that in this case, $W$ is obtained from SGD). Hence, i don't think that lemma can be applied here and there are some flaws in upper bounding $\|\partial loss_i(\theta)/\partial W^{(l)}\|$.
6. In the proof of Theorem 2, the part of constructing $f'\in \mathcal{F}(\theta_0,R)$ such that $\psi$ can be upper bounded by $1/\sqrt{N}$ is confusing (e.g., why $\langle \nabla_\theta f_i(\theta_0),\theta \rangle =y_i(B+B')$). I can't get the point how $R$ can make a difference in the result.

I would appreciate it if you can clear my concerns.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the connection between the generalization error of temporal graph learning (TGL) algorithms and the feature-label alignment (FLA) score. The authors find that FLA can be used to estimate the expressive power and explain the performance of different methods. Based on their theoretical analysis, a new TGL method Simplified-Temporal-Graph-Network (SToNe) is proposed. The proposed method seems to have a small generalization error, better overall performance and lower model complexity.

### Strengths
The theoretical analysis and proof in this article are very detailed. The appended section also provides ample details. The discovered connection between FLA and the generalization error of temporal graph learning is quite intriguing. In addition, through the experiments, the proposed method demonstrated  good performance, e.g., small generalization error, better overall performance and lower model complexity.

### Weaknesses
*The motivation to define a new indicator for the generalization error is unclear: In the paper, the authors indicate that the generalization error bound decreases with respect to the number of training data, but increases with respect to the number of layers/steps in the neural-network-based methods and the feature-label alignment (FLA). Thus, FLA can be used as a proxy for the expressive power measurement. Although there is a connection between FLA and generalization error, using FLA can be unnecessary unless unique advantages of FLA exist, e.g., it is easier to measure. The paper does not clearly articulate why existing generalization bounds are insufficient and how FLA offers a distinct advantage beyond simply being another measure correlated with generalization error. It is not clear if FLA provides any additional insights into the generalization behavior that are not already captured by existing bounds, or if it is simply a more convenient way to calculate a similar quantity.

*The uniqueness of the temporal graph learning algorithms, compared to static graph learning algorithms, is not reflected: Based on the definition 1, FLA can be used for all gradient-based algorithms. It is not specific to temporal graph learning methods. The analysis does not sufficiently highlight the unique challenges and characteristics of temporal graph learning that necessitate a specific analysis using FLA. The paper should discuss how the temporal aspect of the data influences the feature-label alignment and why this is different from static graph learning scenarios. The current analysis seems equally applicable to static graphs, which weakens the claim of its relevance to TGL specifically.

*The proposed method is essentially a GNN method augmented with input data selection, hence have limited novelty as a new algorithm: Based on Section 4.1, the proposed method comprises three parts: input data preparation, encoding features via GNN and link prediction via MLP, which is similar to existing methods except for the feature engineering component. The input data selection mechanism, while potentially useful, does not represent a significant algorithmic innovation. The paper should more clearly differentiate the proposed method from existing GNN-based approaches, highlighting the unique aspects of the input selection process and its impact on performance.

*The performance resulting from the proposed method in the experiment is not  impressive empirically: some existing methods, e.g., TGN and GraphMixer, have a similar performance. Their average precision on the first five datasets are very close. Although the proposed method has better performance on the last dataset UCI, it is unclear whether this last dataset has some special data distribution or setting. The empirical results do not convincingly demonstrate the superiority of the proposed method over existing state-of-the-art techniques. The performance gains on the UCI dataset need to be further investigated, and the paper should provide more details on the dataset characteristics that might explain the observed performance differences.

### Questions
1. What’s the advantage of using FLA? In experiments, the authors still use the generalization gap, i.e., the absolute difference between the training and validation average precision scores, to compare different algorithms.
2. The FLA score of different algorithms should be shown as part of experimental results.
3. Why do most existing methods perform well on all datasets except for UCI dataset? Does UCI dataset contain a special distribution or other specific settings?
4. Can FLA be used for the generalization error of static graph learning algorithms? If so, what’s the uniqueness of the temporal graph learning algorithms in the aspect of generalization error?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors study the generalization ability of different Temporal Graph Learning (TGL) algorithms including GNN-based, RNN-based, and memory-based methods, under the finite-wide over-parameterized regime. To this end, they provide a unified framework for these algorithms and bound their generalization error measured by means of the {0,1}-loss. Their bound, explicited in Theorem 1, emphasizes mainly the dependencies of the generalization error to the number of layers/steps and the feature-label alignment (FLA) score. These motivate the use of shallow and non-recursive networks operating on properly shaped input data instead of depending on memory components. De facto, authors introduce a novel model coined SToNe that fits to these principles. Then they show that SToNE achieves highly competitive performances on link prediction tasks in transductive and inductive settings, with considerably less parameters and better running times.

### Strengths
-	The main theoretical result is clear and depends on reasonable assumptions. Plus it covers a lot of models proposed in the TGL literature. I did not find mistakes in the proofs.
-	The subsequent analysis and choices w.r.t architectures, hyperparameters and FLA are compelling.
-	SToNe shows clearly strong empirical performances reported both in the main paper and supplementary material. The latter also contains various ablation and sensitivity analysis of interest.

### Weaknesses
There are some typing erros in the main paper, and many ones in the supplementary material which is quite needed so please correct them. 

- 1. The presentations of the methods in Section 3, could be clearly improved. Some parts are rather unclear without checking at the corresponding literature: i) no context is provided on Algorithm 1 to position it in the corresponding optimization literature; ii) the time-encoding vector is never clearly defined. ; iii) the concept of temporal events for RNN is not clear.
- 2. Theorem 1: The dynamics w.r.t m* are not discussed, hence do not allow to access whether the chosen $m >= m^*$ in the experiments is relevant.
- 3. Some aspects regarding FLA are not clear: i) Rankings in Figure 3 do not seem to be consistent across methods, authors should explain this further. ; ii) The invertibility of $JJ^\top$ is not clearly discussed. Authors refer to (Nguyen, 2021) for this matter where results in this paper seems to depend on the assumption that at least one layer has to more parameters than there are samples in the dataset. It is not clear that used architectures satisfy this assumption.
- 4. A clear illustration of SToNe would be useful.

### Questions
I invite the authors to discuss the weaknesses I have mentioned above and to provide additional results/analyses for refutation. Follows some questions/remarks to clarify some points:

-	Q1. Could you further discuss the need for the LayerNormalization in SToNe ? e.g instead of no normalization or BatchNormalization ? 
-	Remark: I suggest you complete the list of additional experiments reported in the Supp mentioned in the "More experimental results" paragraph.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
