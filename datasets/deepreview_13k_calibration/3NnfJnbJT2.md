# GIO: Gradient Information Optimization for Training Dataset Selection

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
It is often advantageous to train models on a subset of the available train examples, because the examples are of variable quality or because one would like to train with fewer examples, without sacrificing performance. We present \ourmethod\ (\ourmethodabbrev), a scalable, task-agnostic approach to this data selection problem that requires only a small set of (unlabeled) examples representing a target distribution. \ourmethodabbrev\ begins from a natural, information-theoretic objective that is intractable in practice. Our contribution is in showing that it can be made highly scalable through a simple relaxation of the objective and a highly efficient implementation. In experiments with machine translation, spelling correction, and image recognition, we show that \ourmethodabbrev\ delivers outstanding results with very small train sets. These findings are robust to different representation models and hyperparameters for \ourmethodabbrev\ itself. \ourmethodabbrev\ is task- and domain-agnostic and can be applied out-of-the-box to new datasets and domains. We open source a pip-installable implementation of the algorithm as "pip install grad-info-opt".\footnote{\parbox [t] {\linewidth}{pip install grad-info-opt,  see \appref{app:algorithm} for details

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new approach for data selection called Gradient Information Optimization, based on a natural information-theoretic objective of minimizing the KL divergence between the sampled and target distribution. The paper then evaluates the approach thoroughly in a number of different settings.

### Strengths
- Data selection is an increasingly important problem, and the paper presents a new sound approach
- Overall, very polished and well-written; communicates their contributions clearly. Also, placed well within the context of related work
- Mostly thorough evaluation of proposed approach, including self-consistency checks, ablations, and different domains (language and vision)

### Weaknesses
 - It's not clear to me if the lack of hyperparameter/stopping criterion (which is argued as a strength) is real and if actually a strength. 
For example, in the self consistency section: there is still an implicit hyperparameter for GIO  when the authors denote "d(pX(x),pG(x))≫0". How do you define what is too big of a distance? So it seems as if it's a bit misleading to present the lack of the dataset size parameter as a strength, if the hyperparameter just shows up in a different form. Also, intuitively, I think it feels that there should naturally be a hyperparameter, as the optimal dataset really depends on the different constraints you have (whether that be size or something else).

- Lack of comparison to a similar recent approach: How does the approach here compare (both conceptually and empirically) to that of Xie et al. [1]? They also use a notion of KL distance over a feature space. Not sure if it's quite right to list their approach under one of the "heuristic" methos.

[1] Xie, Santurkar, Ma, Liang. Data selection for Language models via Importance Sampling.

### Questions
Other clarifications:
- In 4.2, "GIO works with different embedding models": are the selected examples themselves similar when using different embeddings?
More broadly, why should GIO be invariant to this choice though? For example, it's plausible that certain embeddings focus on certain features more than others, distorting the distribution.
- Did you try using simpler feature spaces, such as the n-grams one considered in Xie et al.?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes GIO, a new method for selecting subset of the training data in order to reduce data/compute cost while retaining performance similar to the original dataset. It is a task and domain agnostic scheme that requires a small set of unlabeled examples representing target distribution. It minimizes the KL divergence between the target distribution and subset in an iterative manner along with some approximations that make the procedure tractable. Empirical experiments show that this approach is competitive to the existing baselines such as submodular optimization and data pruning.

### Strengths
- task agnostic and domain agnostic approach to dataset pruning 
- does not require labels to apply GIO

### Weaknesses
 - Algorithm 1 is incomplete on its own. It does not define the inputs X, D, G. How does one find v_opt? Which equation are you referring to? Ideally, one should be able to infer the algorithm by reading this procedure.
- No benchmarking for the compute cost of the proposed method against baselines (submodular optimization, BM25, etc.). It is hard to judge how computationally expensive this approach is compared to various baselines?
- Its unclear if the proposed method could scale to large datasets (for instance on Image recognition task, only FashionMNIST is used)
- It could be challenging to select target state X and initial state D



### Questions
-  In table 4, why is D_KL lower for the random method than the proposed scheme, also random D_KL is much closer to Full dataset?	
-  Table 4 does not include other baselines for subset selection in the classification setting?
-  How do you define high quality in Table 3?
-  Have you compared the training cost of the proposed method against other baselines?
- How does the method perform when scaled to larger datasets? FashionMNIST seems too small a dataset (even random subset is not that bad in performance)?
-  Have you done any ablations to see the impact of target state X and the initial state D? How does one go about initializing these for a new task/domain?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a scheme to perform training data subset selection, connected to ideas in information theory by minimizing the (approximate KNN) KL divergence between the selected subset and the original dataset. However, this is intractable in practice, and the authors approximate this by finding the optimal data point (not necessarily contained within the training data) to add and then projecting this onto the nearest point contained within the training set. This only scales with the number of gradient steps (and not the size of the original dataset), which is much more computationally efficient. They run this gradient trick over K-means clusters rather than individual data points to make the problem more tractable.

The authors evaluate the proposed approach through multiple different qualitative and quantitative metrics: (1) self-consistency - coming from the same distribution, (2) negative-consistency - essentially ignoring outliers in the data distribution, (3) the selected subset should maintain similar values of KL divergence given a quantization of the data (i.e. K-means).

### Strengths
* The authors propose various methods/approximations to select a subset of training data with greater computational efficiency, and these approximations are tied to an underlying naive approach based on information theory. In addition, the method is simple and easy to understand.

* The paper is well-motivated and solves an important issue; improving the efficiency of pretraining (through shrinking the dataset size) makes the training of large models more available to researchers at lower costs.

* This approach sees good empirical results on multiple machine translation tasks and an image classification task, and the authors' intuitions are also demonstrated in synthetic experiments.

* The authors also provide ablations to demonstrate the proposed method is not very sensitive to different underlying embeddings or the hyperparameters of the K-means quantization.

### Weaknesses
 * I’m a bit confused as to the stopping criteria in Section 4.3. This seems to come out of nowhere and be rather ad-hoc. Why do you introduce the second stage of reselecting instances from G until the KL divergence begins to decrease? Why couldn't you simply run the first stage here? It's unclear what the motivation is for this two-stage process, and how it relates to the overall goal of minimizing KL divergence between the selected subset and the original dataset. The authors should provide a more rigorous justification for this particular stopping criterion, or at least explore the effects of using only the first stage.

* Not a big issue, but I also think the presentation in Section 4.3 is a bit confusing. The first sentence of the section seems to claim that GIO selects a subset of high-quality data with respect to a target set that is a combination of both high and low-quality data (which is confusing as something that minimizes the KL divergence should select both). However, this isn’t the experiment being run; the target set $X$ here is only a dataset of high-quality data. The description of the experiment does not match the stated goal of the method, and the authors should clarify the experimental setup and how it aligns with the theoretical motivation.

### Questions
1. Why were the other baselines not included in the FashionMNIST experiments?
2. See the weaknesses section regarding the stopping criteria in Section 4.3.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method called gradient information optimization (GIO) to select a subset of a large training dataset that preserves model performance. GIO is formulated as a problem of minimizing the KL divergence between the subset and the target distribution. As an algorithm for this minimization problem, the authors propose an algorithm using the gradient of the KL-divergence based on the greedy method.The authors experimentally demonstrate that the proposed method outperforms existing methods on the tasks of NLP and image recognition.

### Strengths
It seems reasonable to select the subset so as to minimize the KL divergence.The authors propose a feasible algorithm for this minimization problem.Experimental results suggest that their proposed method works better than existing methods for machine translation and spell-correct tasks.

### Weaknesses
1. There is a gap between the two equations, i.e., the solution obtained by the greedy method in equation (2) and the optimal solution in equation (1) are different. However, the authors did not discuss the gap between the two solutions. Specifically, the greedy approach in equation (2) is a local search method, while equation (1) represents a global optimization problem. The authors should provide a more thorough analysis of how well the greedy solution approximates the global optimum, considering that the objective function (KL divergence) is non-convex, which makes it difficult to guarantee the quality of the local optimum found by the greedy algorithm.
2. The subset selection given the target distribution is not sufficiently motivated and GIO seems not to be suitable for the natural setting of subset slection, $D=\emptyset$, $G=X$. For this setting, $V=X$ (selecting all data) is the obvious optimal solution to equation (1) as the authors state in Section 3.4. The paper lacks a clear explanation of why a target distribution is needed in practical scenarios, and how it should be chosen. The authors should provide a more concrete discussion of the real-world use cases where a target distribution is available and how the proposed method can be applied to these cases. The current discussion is too abstract and lacks practical motivation.
3. It is not clear whether $\mathbf v_{opt}$ obtained by the gradient method and the optimal solution of equation (3) match. From appendix A.2., the authors assume that the two solutions match if the data density is sufficient. However, from Algorithm 1, the data are selected only from k-means centroids(G_c). Their assumption does not seem to hold, especially in high-dimensional spaces.There is not enough discussion about this. The authors need to justify how the gradient-based optimization on the relaxed space relates to the discrete selection problem, especially when the data is selected only from k-means centroids. The assumption that the relaxed solution is close to the discrete solution needs more rigorous justification, especially in high-dimensional spaces where the data density is often sparse.

### Questions
1. Could you discuss the gap between the solutions of equations (1) and (2), on the theoretical side or on the experimental side? For example, on the theoretical side, if submodularity holds for the objective function, the approximation rate is bounded. On the experimental side, could you evaluate the rate of approximation between the solutions obtained by equation (1) and equation (2), and algorithm 1?
2. Could you discuss what real-world situations where target distributions can be obtained? Could you also discuss what kind of data should be set as target distributions? For example, in the experiment, to improve the performance of the WMT14 test set, the authors set the WMT08-13 dev set as the target instead of the WMT14 training set. As a result, they report that the performance of the WMT14 test set actually improves. Could you discuss this result, for example?

Comments
1. $\Omega$ is not defined.
2. In Algorithm 1, $D_c \gets D_c + \\{\mathbf v_b\\}$ should be $D_c \gets D_c \cup \\{\mathbf v_b\\}$.
3. The definition of relaxed $\mathbf v$ and $\mathbf v_{opt}$ is ambiguous. $\mathbf v \in \Omega$?


## Post-rebuttal
My main concerns were (1) about the gap between Eq.1 and Eq.2 and (2) about the usefulness of the proposed method in real-world tasks.

There is a gap between the optimization problem (i.e., minimization of KL-divergence; "information-theoretic approach") and the greedy algorithm in this paper.
The relationship between them was not clearly discussed.
In their response, the authors clarified that the objective function lacks certain properties, such as submodularity. 
Unfortunately, they couldn't demonstrate the (empirical) approximation ratio achieved by the greedy algorithm. 
However, it is acknowledged that the greedy algorithm is one of the natural approaches to discrete optimization.

In their experiments, the proposed method performs well compared to baseline methods, including the one using submodular optimization.
Furthermore, the authors' response highlighted that the proposed method outperformed existing methods in an experiment more closely resembling realistic scenarios.
Furthermore, this paper proposes an effective algorithm, which has actually been applied to more than 10M data, while the minimization of KL-divergence by naive greedy algorithm is intractable.
The response to C7wm states that the proposed method is computable in ~40min for a dataset containing 35M data.

Based on the above points, I agree that this paper holds significant value for the community, prompting me to revise my score from 5 to 8.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
