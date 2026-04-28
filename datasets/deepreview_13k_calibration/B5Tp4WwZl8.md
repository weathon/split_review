# Error Feedback Shines when Features are Rare

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 8, 3, 8

## Abstract
We provide the first proof that gradient descent (\algname{GD}) with greedy sparsification ($\topk{K}$)  and error feedback (\algname{EF}) can obtain better communication complexity than vanilla \algname{GD} when solving the distributed  optimization problem $\min_{x\in \R^d} \{f(x)=\frac{1}{n}\sum_{i=1}^n f_i(x)\}$, where $n$ = \# of clients, $d$ = \# of features, and $f_1,\dots,f_n$ are smooth nonconvex functions.  
Despite intensive research since 2014  when \algname{EF} was first proposed by Seide et al., this problem remained open until now. %Surprisingly, this superior performance holds in and is facilitated by a heterogeneous data regime. 
Perhaps surprisingly, we show that \algname{EF} shines in the regime when features are rare, i.e., when each feature is present in the data owned by a small number of clients only. To illustrate our main result, we show that  in order to find a random vector $\hat{x}$ such that $\norm{\nabla f(\hat{x})}^2 \leq \varepsilon$ in expectation, \algname{GD} with the $\topk{1}$ sparsifier and \algname{EF} requires  
$\cO\left( \left(L +   \xr\sqrt{ \frac{\xc}{n} \min \left\{ \frac{\xc}{n}  \max_i L_i^2, \frac{1}{n}\sum_{i=1}^n L_i^2 \right\}}  \right) \frac{1}{\varepsilon} \right) $ bits to be communicated by each worker to the server only, where $L$ is the smoothness constant of $f$, 
$L_i$ is the smoothness constant of $f_i$, $\xc$ is the maximal number of clients owning any feature ($1\leq \xc\leq n$), and $\xr$ is the maximal number of features owned by any client ($1\leq \xr \leq d$). Clearly, the communication complexity improves as $\xc$  decreases (i.e., as features become more rare), and can be much better than the $\cO(\xr L \frac{1}{\varepsilon})$ communication complexity of \algname{GD} in the same regime.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors try to make sense on the gap in our understanding of the theoretical and practical aspects of gradient descent algorithms in the distributed setting. The try to reason why the algorithm based on heuristics like the greedy sparsification and error feedback performs better in practice than the distributed gradient descent, but theoretically the opposite is observed. They identify scenarios when "features are rare" and prove that in these scenarios one can prove that the performance of the heuristic algorithms are better than the distributed gradient descent.

### Strengths
This is one of the few papers trying to understand, or rather prove theoretically, why is a heuristic algorithm performing better than another algorithm in practice though theory suggests otherwise.

### Weaknesses
The paper proves that under certain assumptions the EP21 algorithm performs better than the DGD algorithm. The assumptions are quite strong and hence it is not clear if this is best scenario to explain the performance of EP21 algorithm.

### Questions
Can you say how often one expects to find real life data satisfying the assumptions under which the improved theoretical study is done?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies error feedback in distributed optimization. It provides a first theoretical analysis of how greedy sparsification and error feedback can improve the communication complexity of distributed gradient descent. Specifically, when $\sqrt{\frac{c}{n}}L_+ \leq L$, the communication complexity improves. Numerical experiments are conducted to validate the theoretical results.

### Strengths
1. This paper is well written and most ideas are presented in a straightforward and easy-to-read manner.
2. It provides meaningful observations to motivate the research.
3. Theoretical results are solid and only rely on simple and standard assumptions.

### Weaknesses
1. I have some concerns about the novelty and contribution of the paper since it mostly builds on the previous work EF21. I hope the authors can clarify this and explain how this work advances error feedback algorithms or distributed optimization in the future.
2. As the authors said in the paper, the experiments are rather toy and the practical applicability is limited because most real-world datasets are not sparse enough. It would be helpful and convincing to conduct some experiments on real-world datasets.

### Questions
in the above

### Soundness
4 excellent

### Presentation
4 excellent

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
The paper studies the theoretical advantage of the error feedback mechanism for compressed distributed gradient descent (DGD). The authors first defined two quantities that measure the sparseness and rareness of the data features. Then the non-convex convergence rate shows that when the data has sparse and rare features, EF21 has better communication complexity than DGD. Some simple experiments are conducted to justify the theory.

### Strengths
Strength:
+ The writing is clear and easy to follow.
+ The introduction to related works and existing results is comprehensive and helpful to understand the context.
+ Introducing feature “rareness” to the analysis of optimization methods is a good attempt.

### Weaknesses
Weakness: There are several limitations of this work.

1.	In my opinion, the motivation for this work is not very strong.

a.	The authors claim that the goal is to explain why EF21 empirically performs much better than DGD in terms of communication complexity but theoretically does not. However, their analysis relies on some strong assumptions about the data which are uncommon in practice. Indeed, does the fact that EF21 performs well in practice on many types of data (without strong assumptions) indicate that the feature rareness and sparsity assumed in this paper are NOT the true reasons? While there are many engaging words like “breakthrough” or “milestone”, I don’t really feel surprised because a better rate shall be expected when we limit the function class and propose strict data assumptions. But I doubt whether this is the correct direction given the points above.

b.	It seems that Lemma 2 – 5 are general results not specific to EF. Can we apply the same analysis and argument to DGD? In other words, can rare and sparse features also improve the rates of DGD?

2.	It seems that the arguments are limited to simple linear models. This is because the feature sparsity would lead to model sparsity (which is a key component in the analysis, for example Lemma 5) only for linear models. For non-linear models (for example the DNNs), the arguments will not hold.

3.	Empirically, the experiments also only used convex regression models but not more complicated neural networks. There is a discrepancy between the experiments with the non-convex theoretical analysis. So, the experiments are kind of limited.

4.	As a theoretical paper, the setups and technicality are not comprehensive and strong enough. The paper only studied deterministic setting without stochastic gradients. SGD-type methods are more practical. What’s the situation in the stochastic setting? Does the same problem exist? From the technical perspective, the main modification in the proof compared with prior works is improving Young’s inequality and the smoothness constant $L$ using rareness/sparsity. This is not very challenging and novel in my evaluation.

### Questions
See as above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the paper, the authors showed that greedy sparsification (TopK compressor), together with error feedback, can beat distributed gradient descent in terms of theoretical communication complexity, by characterizing its fast convergence rate in a certain regime (that depends on the sparsity parameters c and r). 
See Example 1 and Theorem 2.
Numerical experiments are provided Section 6 to validate the proposed theoretical analysis.

### Strengths
The paper addresses the important problem of communication complexity in distributed ML.
The 
The paper is in good shape.

### Weaknesses
I do not see particular weakness for the paper but a few comments, see below.

### Questions
I do not have specific questions but the following general comments for the authors:

1. when referring to the appendix, please specify which section/part of the appendix.
2. I personally suggests the authors to further elaborate on the limitations of the analysis and future work, and move them to the main text (instead of leaving them in the appendix).

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
