# Dropout Enhanced Bilevel Training

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Bilevel optimization problems appear in many widely used machine learning tasks. Bilevel optimization models are sensitive to small changes, and bilevel training tasks typically involve limited datasets. Therefore, overfitting is a common challenge in bilevel training tasks. This paper considers the use of dropout to address this problem. We propose a bilevel optimization model that depends on the distribution of dropout masks. We investigate how the dropout rate affects the hypergradient of this model. We propose a dropout bilevel method to solve the dropout bilevel optimization model. Subsequently, we analyze the resulting dropout bilevel method from an optimization perspective. Analyzing the optimization properties of methods with dropout is essential because it provides convergence guarantees for methods using dropout. However, there has been limited investigation in this research direction. We provide the complexity of the resulting dropout bilevel method in terms of reaching an $\epsilon$ stationary point of the proposed stochastic bilevel model. Empirically, we demonstrate that overfitting occurs in data cleaning problems, and the method proposed in this work mitigates this issue.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a dropout method to address the issue of overfitting in bilevel training tasks. The authors provide theoretical convergence guarantees from an optimization perspective and demonstrate its effectiveness through experiments, using data cleaning as an illustrative example.

### Strengths
The paper is generally well-written and easy to follow. It investigates a relatively unexplored area and aims to analyze the dropout bilevel method for addressing this problem. Another advantage is the detailed theoretical analysis provided in the paper.

### Weaknesses
- Based on the results figures, it appears that early stopping can effectively resolve the issue of overfitting, even though the accuracy without dropout is higher.
- The theoretical analysis in the current context is not particularly challenging. In contrast, in many stochastic bilevel optimization studies, such as [2], a more comprehensive framework is presented, along with convergence rate guarantees for stochastic bilevel optimization. You can try to answer the extra challenge in these theoretical literatures [2].
- The experimentation conducted on data cleaning is insufficient, and it would be better to observe more results on other bilevel optimization tasks.
- Each figures should be accompanied by a brief caption.

### Questions
- In addition to the theoretical analysis, literature [1] also investigates the impact of dropout rate on bilevel optimization. However, what are the other distinguishing factors between these studies?
- What is the relationship between the objective function after incorporating dropout and the original objective function? 

[1] Delta-STN: Efficient Bilevel Optimization for Neural Networks using Structured Response Jacobians. Juhan Bae, Roger Grosse. NeurIPS 2020.

[2] Bilevel Optimization: Convergence Analysis and Enhanced Design. Kaiyi Ji, Junjie Yang, Yingbin Liang. ICML 2021.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper brings dropout to bilevel optimization to avoid overfitting issues. The author forms a statistical bilevel optimization problem that includes the distribution of the dropout masks and propose a dropout method to solve it. To analyze the convergence of the proposed method, they delicately quantify the bias induced by the dropout. The empirical performance of the proposed method is tested on the data hyper cleaning task and shows that dropout efficiently improve the test accuracy and is more stable.

### Strengths
1. This paper incorporates the dropout technique in the bilevel optimization to avoid overfitting. The idea is new to the bilevel optimization community and has been tested effective. 
2. The analysis of dropout by modeling the dropout mask as a stochastic distribution is thorough and novel. 

Overall, I felt this is a solid and novel paper for bilevel optimization.

### Weaknesses
1. The motivation of considering the dropout in bilevel optimization could be explained more. For example, why avoiding overfitting is important in bilevel optimization, that is, does bilevel structure exacerbate the overfitting issues? 
2. The convergence analysis is built up on the stationarity measure $\frac{1}{T-1} \sum_{k=1}^{T-1} \mathbb{E}\left\|\nabla F_{M^{k}}\left(\lambda^{k}\right)\right\|^{2}$, which is the dropout bilevel objective. To fortify the analysis, it is conceivable to draw connections between this measure and the one based on the original bilevel objective $\frac{1}{T-1} \sum_{k=1}^{T-1} \mathbb{E}\left\|\nabla F\left(\lambda^{k}, w(\lambda^{k})\right)\right\|^{2}$. This could elucidate the relaxation error introduced by dropout and establish a guarantee for the original objective's convergence, thereby validating efficiency of the dropout approach more rigorously.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper uses dropout methods for bilevel training tasks. Bilevel optimization problems consist of two intertwined optimization problems and can be particularly sensitive to small changes, especially when data is limited. The study introduces a bilevel optimization model that considers the distribution of dropout masks and examines how varying dropout rates impact the hypergradient of this model. The authors adapt an existing bilevel method to incorporate dropout and provide theoretical convergence guarantees for this new approach. Empirical tests on data cleaning problems show that this method can mitigate overfitting.

### Strengths
Incorporating dropout in bilevel training tasks is a novel approach, offering a new method to combat overfitting in such tasks. The authors study the convergence properties of the introduced method. The study offers empirical proof, especially in the context of data cleaning problems, demonstrating the efficacy of the proposed method in reducing overfitting. The paper paves the way for adapting other state-of-the-art bilevel methods to account for dropout, making it a foundational study for further research in this direction.

### Weaknesses
The use of datasets like MNIST, which is relatively small and simplistic, might not fully showcase the potential or limitations of the proposed method in real-world, complex scenarios. Furthermore, the empirical evaluation primarily focuses on data cleaning problems. While this is a relevant application, the paper would benefit from demonstrating the method's effectiveness across a broader range of bilevel optimization tasks. The current empirical analysis lacks a comprehensive exploration of the sensitivity of the method to different hyperparameter choices, particularly the dropout rate. A more detailed analysis of how the dropout rate affects the convergence speed and the final performance would be valuable. Additionally, the theoretical convergence guarantees, while a strength, could be further strengthened by analyzing the convergence rate under various conditions, especially in relation to the chosen dropout strategy.

### Questions
Beyond data cleaning, how might this method be applied to other machine learning tasks, especially those that inherently involve bilevel optimization?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper points out that overfitting is a common challenge in bilevel training task. To address this issue, the author proposes the dropout mask for the bilevel optimization problem. Specifically, the author proves the convergence of dropout bilevel methods theoretically and empirically shows that proposed method mitigates the overfitting issue.

### Strengths
Overfitting issue has not been fully investigated in the bilevel area and this paper proposes the new method to address it.

### Weaknesses
1. It looks like this paper studies data cleaning problem rather than the bilevel problem. Both the introduction and experiments are based on data cleaning context. The authors are suggested to discuss and conduct experiments on other bilevel optimization settings to demonstrate applicability of proposed algorithm.

2. Overfitting issue can be easily addressed by early stopping. The authors are encouraged to make an experimental comparison between proposed dropout and early stopping to demonstrate the necessity of adopting dropout.

3. In Theorem 2, the authors demonstrate that dropout rate "influences" the upper bound. However, it only influences the constant term and does not influence the convergence rate. Furthermore, the theoretical results only demonstrates the dropout rates "influence" the convergence but does not demonstrates it "improves" the convergence rate, even for the constant term. I expect to see inspiration about dropout rate selection from this theorem. The same issue also occurs for the Lemma 1 which is about variance term.

### Questions
Can you discuss the technical difficulties of applying dropout analysis into bilevel optimization problem? That will be helpful to understand the theoretical contribution.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
