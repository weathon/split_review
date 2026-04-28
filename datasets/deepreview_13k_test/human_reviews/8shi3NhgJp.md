# IBCL: Zero-shot Model Generation under Stability-Plasticity Trade-offs

- Decision: Reject
- Scores: 3, 8, 3, 6

## Abstract
Algorithms that balance the stability-plasticity trade-off are well-studied in the continual learning literature. However, only a few of them focus on obtaining models for specified trade-off preferences. When solving the problem of continual learning under specific trade-offs (CLuST), state-of-the-art techniques leverage rehearsal-based learning, which requires retraining when a model corresponding to a new trade-off preference is requested. This is inefficient since there exist infinitely many different trade-offs, and a large number of models may be requested. As a response, we propose Imprecise Bayesian Continual Learning (IBCL), an algorithm that tackles CLuST efficiently. IBCL replaces retraining with constant-time convex combination. Given a new task, IBCL (1) updates the knowledge base in the form of a convex hull of model parameter distributions and (2) generates one Pareto-optimal model per given trade-off via convex combination without any additional training. That is, obtaining models corresponding to specified trade-offs via IBCL is zero-shot. Experiments whose baselines are current CLuST algorithms show that IBCL improves by at most 45\% on average per task accuracy and by 43\% on peak per task accuracy, while maintaining a near-zero to positive backward transfer. Moreover, its training overhead, measured by number of batch updates, remains constant at every task, regardless of the number of preferences requested.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper, introduces Imprecise Bayesian Continual Learning (IBCL) to address the Continual Learning under Specific Trade-offs (CLuST) problem. Traditional methods that balance stability and plasticity often rely on rehearsal-based learning, requiring retraining for each new trade-off, which is inefficient. IBCL offers a more efficient approach by constructing a convex hull of model parameter distributions and enabling zero-shot model generation for specific trade-offs without retraining. IBCL achieves this by updating a knowledge base in the form of a convex set of distributions and using convex combinations to generate Pareto-optimal models according to user-specified preferences. Experiments indicate that IBCL improves per-task accuracy and backward transfer compared to existing CLuST methods, with constant-time overhead and sub-linear memory growth.

### Strengths
1. The algorithm offers many favorable features, including the efficiency in model generation and sub-linear memory growth
2. It is innovative to investigate the problem through a Bayesian lens.

### Weaknesses
I do not think this paper is well written enough for me to follow easily. First, some definitions are not formal. For example Definition 1, 2 should be written more formally. See questions 1 and 2 below. Second, some important concepts should be presented in detail with formulae. For example, in line 218, continual Bayesian learning appears without a formal introduction. Third, the words and phrases should be picked more carefully. For example, in line 8 of Algorithm 1, one should state: store xxx and use xxx when xxx instead of saying remember xxx and use xxx later on.

### Questions
1. What is the definition of $q^j$? Is it a real vector?
2. In definition 2, what is $\int$ is a minimum?
3. Are $\mathcal{X}, \mathcal{Y}$ subsets of the Euclidean space?
4. Variational inference can be computationally intensive? Will this algorithm become computationally infeasible in real-world settings?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper models the problem of continual learning under specific trade-offs (CLuST) as a convex combination of previous tasks to the preference vector. The authors propose an algorithm named Imprecise Bayesian Continual Learning (IBCL) that transforms the convex combination of data distributions into the convex combination of model parameters under the framework of Bayesian learning. This algorithm is training-free for any newly arrived preference vectors compared to previous rehearsal-baed methods. The algorithm also performs well in numerical experiments.

### Strengths
1. The paper is written in a well-organized and self-contained way. The key concepts are clearly defined and sufficiently explained.
2. The idea of avoiding re-training models when receiving new preference vectors is smart. Transforming the convex combination of distributions into the convex combinations of posterior distributions of model parameters is natural, especially when the tasks are similar.
3. The numerical experiments verify the excellence of the algorithm. The code is also well-written.

### Weaknesses
1. The contribution is restricted to the domain-incremental continual learning scenario.
2. The algorithm's effectiveness relies on a core assumption that there is a continuous mapping from the data distribution to the distribution of the ground-truth model parameters and that mapping is (approximately) linear. The authors should specify this reliance and perhaps give more discussions on the validity of the assumption (for example, the dependence on the model/prior choices and the dependence on the underlying data distributions).
3. The theory part does not have an in-depth algorithm analysis. Theorem 1 is about the modeling rather than the algorithm. Theorem 2 is unnecessary: a) the theorem relies on the assumption that the Pareto-optimal parameter follows the estimated posterior distribution, which directly assumes the correctness of the estimation; b) the theorem does not provide any useful information since the coverage guarantee is already defined in the high-density region (HDR). I suggest deleting Theorem 2 to avoid confusion. Some more in-depth discussions are preferred.

### Questions
1. What are the benefits of IBCL compared to linearly weight interpolation? For example, for a preference vector, the linear combination of model weights $\sum_{j=1}^m q_j \hat{\theta}_j$ itself induces a model (here the $\hat{\theta}_j$ can be any estimated model weights, for example, via empirical risk minimization). Some theoretical analysis and numerical experiments would be preferred.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the stability-plasticity trade-off for continual learning, with a focus on obtaining models for specified trade-off preferences. Differently from the typical rehearsal-based CL, which requires to retrain for every task and every preference, the authors propose a new paradigm named Imprecise Bayesian Continual Learning (UBCL) that replaces the retraining with weighted average of the extreme elements in the knowledge base, whose weights are provided by a preference vector. Since there is no additional training on the models, the entire procedure to achieve the provided trade-off is zero-shot. The main computation step is to compute the highest density region (HDR) under a distribution induced by weighted parameter posteriors of previous tasks. Empirically, the authors demonstrate that the proposed method outperforms existing algorithms in terms of accuracy significantly, with small overhead.

### Strengths
1.	The idea of using Bayesian techniques, FGCS and the convex combination of posteriors of previous tasks to achieve zero-shot training seems interesting in the context of continual learning. 
2.	In the problems of continual learning under specific trade-offs (CluST), the proposed method significantly improves existing rehearsal-based and prompt-based algorithms.

### Weaknesses
1.	This paper is not well written. First, the motivation is not very clear. The paper considers CL under given preferences (i.e, weights). Although the paper gives some examples in recommendation systems, it does not talk much about how to get such weights. In addition, what is the setting of infinitely number of perferences? Some motivating examples are highly needed. 
2.	In terms of the presentation, there are also multiple places to be clarified. First, in line 208, there is a probability $\hat q_{\bar w}$ that is not defined at the first place. I find its definition later in equation (1). I suggest using a different notation or explain clearly here. In algorithm 1, some details or explanations may be needed, since some readers may be not familiar with this procedure. In theorem 2, how to find the pareto-optimal parameters $\theta^*_{\bar w}$? Is there any guarantee that the output of the proposed algorithm is parato-optimal? More clarifications should be provided.
3.	The design contains multiple heuristics and multiple hyparameters to be deciede. For example, in algorithm 1, lines 4-8 remove similar elements, based on a threshold d. How to select d in practice? Is the performance sensitive to it? Why such elimination is useful? In algorithm 2, why choosing $\beta^1_k=….=\beta^m_k$? Is it just because of simple implementation? How about other choices? Finally, the number $m$ of distributions for each task is selected to be 3 in the experiments. How about other choices? Is there any trade-off between the accuracy and efficiency?   
4.	The assumption made in this paper may be strong. In Assumption 1, it assumes all tasks have the same data distributions. It can happen that tasks share some level of similarity in data distribution, but they may involve different distribution components. In addition, in assumption 1, how to define $r$? This is because r can be either very large or very small. The final performance may be highly dependent on r. However, is there no such analysis. 
5.	Experiments are not entire convincing. Algorithms are compared in term of accuracy but how about their performance in forgetting? In addition, perhaps I missed something, but are there any ablation studies on the selection of d, m, \alpha and other hyperparameters?

### Questions
Please refer to all the questions I mentioned in the weakness section. Overall, this paper gives an interesting idea but the proposed approach is not well explained and the results are not entire convincing. However, I am willing to raise my scores if my questions are well addressed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Imprecise Bayesian Continual Learning (IBCL), a zero-shot, Pareto-optimal model with sublinear buffer growth, designed to address the Continual Learning under Specific Trade-offs (CLuST) problem. It also provides a mathematical formulation of the CLuST problem and presents experiments to evaluate IBCL's effectiveness.

### Strengths
The paper is well-written and easy to follow. The mathematical formulation of the problem is clear, and the figures effectively illustrate the proposed algorithm. Additionally, the paper provides analytical insights into the proposed algorithm, and the experimental results demonstrate its effectiveness.

### Weaknesses
[1]I'm not sure about the applicability of the problem setup and the proposed model. It seems that the target distribution for learning (line 188) is only optimal under entropy loss for predictions. For more details, please refer to the questions section.

[2]A minor issue is the lack of ablation studies on the choices of prior distributions $q_0^j$'s and the parameter $\beta$'s. In the experiments, prior choices (lines 968-975) are fixed, and the $\beta$ values are uniformly chosen to recover the preference vector (Algorithm 2). Ablation studies on these choices would provide helpful insights.

### Questions
I’m curious about the “optimality” of the distribution to learn $p_{\bar{w}}$. Given a preference vector, the mixed probability $p_{\bar{w}}=\sum w_i p_i$ seems optimal under entropy loss; specifically, if $(X,Y)\sim p_{\bar{w}}$  then the probability $p_{\bar{w}}$ (conditional on $X$) minimizes the entropy loss when predicting $Y$ given $X$. However, if we consider an L2 loss, the optimal prediction becomes $\mathbb{E}[Y|X]$, a point estimate rather than a distribution. My questions are:

(1) Is the convex combination of true distributions $p_{\bar{w}}=\sum w_i p_i$ only optimal under entropy loss?

(2) If so, could the current method be extended to accommodate other loss functions, such as L2  or absolute loss?

Also, in the broader impact section, the potential of the proposed approach for large language models is mentioned. However, the experiments are conducted with a small neural network with only a single hidden layer. How does IBCL perform in terms of efficiency and effectiveness, particularly in training time per new task, when applied to larger models?

### Soundness
3

### Presentation
4

### Contribution
3
