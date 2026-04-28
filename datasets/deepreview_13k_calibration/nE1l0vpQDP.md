# The Implicit Bias of Stochastic AdaGrad-Norm on Separable Data

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
This work explores stochastic adaptive gradient descent, i.e., stochastic AdaGrad-Norm, when applied to linearly separable datasets. For the stochastic AdaGrad-Norm method equipped with a wide range of sampling noise, we demonstrate its almost surely convergence result to the $\mathcal{L}^{2}$ max-margin solution. This means that stochastic AdaGrad-Norm has an implicit bias that yields good generalization, even without regularization terms. We show that the convergence rate of the classification direction is $o({1}/{\ln^{(1-\epsilon)/{2}}n})$. Our approach takes a novel stance by explicitly characterizing the $\mathcal{L}^{2}$ max-margin direction. By doing so, we overcome the challenge that arises from the dependency between the stepsize and the gradient and also address the limitations in the previous AdaGrad-Norm analyses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the stochastic AdaGrad-Norm method, with a broad range of sampling noise, applied to linearly separable classification problems. Specifically, it proves that the method exhibits an implicit bias, converging almost surely to the L2 max-margin solution without explicit regularization.

### Strengths
Examining the implicit bias of optimization methods is an important research direction for understanding the statistical efficiency of machine learning models. This work uncovers the implicit bias of AdaGrad-Norm along with its convergence rate.

### Weaknesses
The most significant issue is that I cannot trust the correctness of these results. I detected a number of technical errors and unclarity in the proof of Lemma B.4, which is the very first theoretical analysis that the authors provide, and is the basis of the proof of other theoretical results. I will list the details in the Questions section.

There are two possibilities. The first is that the authors' analysis is actually incorrect, and the second is that the authors' theory is correct but is very poorly presented with numerous typos, calculation misses, and unclear explanations. Even if the optimistic second possibility is the case, I vote for rejection of the paper because its current quality of presentation is poor and far away from the level that is adequate for publication. At the most technical level, the proofs are very sloppy and difficult to read through, and includes too many major/minor errors causing doubts on the soundness of the theoretical statements. Additionally, there are plenty of sentence-level grammar issues and parts whose meaning are unclear. At a higher level, the organization of the main paper features a large volume of technical information that contains notations that were never defined within the main text and hence is not comprehensible unless one goes through the appendix. In pg. 5, the paper declares through the paragraph title that it will illustrate the "Intuition of the theorem", but at least to me, only little proportion of the subsequent materials was informative.

Besides the above issues, there is a weakness that the paper considers a specific setup and it is questionable whether their theory and techniques (if are correct) can be generalized to broader problem classes.

### Questions
Can you explain the theoretical advantage of AdaGrad-Norm compared to GD? Currently, it is unclear as both methods exhibit the same implicit bias.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the implicit bias of the stochastic AdaGrad-Norm algorithm in the binary classification setup with logistic regression loss for linearly separable data. The authors provide the almost sure convergence result to the $\mathcal{L}^2$ max-margin solution, together with a quantitative convergence rate. This demonstrates the implicit regularization effect of stochastic Adagrad-Norm towards the max-margin solution.

### Strengths
Implicit regularization is a topic of interest in optimization theory, and the paper studies the popular Adagrad algorithm. It provides a setup where in-depth technical analysis can be performed.

### Weaknesses
The most significant issue is that I cannot trust the correctness of these results. I detected a number of technical errors and unclarity in the proof of Lemma B.4, which is the very first theoretical analysis that the authors provide, and is the basis of the proof of other theoretical results. I will list the details in the Questions section.

There are two possibilities. The first is that the authors' analysis is actually incorrect, and the second is that the authors' theory is correct but is very poorly presented with numerous typos, calculation misses, and unclear explanations. Even if the optimistic second possibility is the case, I vote for rejection of the paper because its current quality of presentation is poor and far away from the level that is adequate for publication. At the most technical level, the proofs are very sloppy and difficult to read through, and includes too many major/minor errors causing doubts on the soundness of the theoretical statements. Additionally, there are plenty of sentence-level grammar issues and parts whose meaning are unclear. At a higher level, the organization of the main paper features a large volume of technical information that contains notations that were never defined within the main text and hence is not comprehensible unless one goes through the appendix. In pg. 5, the paper declares through the paragraph title that it will illustrate the "Intuition of the theorem", but at least to me, only little proportion of the subsequent materials was informative.

Besides the above issues, there is a weakness that the paper considers a specific setup and it is questionable whether their theory and techniques (if are correct) can be generalized to broader problem classes.

### Questions
List of (serious) technical issues regarding the proof of Lemma B.4
- In derivation of equation (10), the authors seem to combine the previous equations. I think the $\alpha_0^3$ factor is missing from the second line, and more importantly, it seems like the term $\frac{\alpha_0}{2\hat{K}^2} \mathbf{1}_{\mathcal{B}_n} \frac{||\nabla g(\theta_n)||^2 ||\nabla g(\theta_n, \xi_n)||^2}{\sqrt{S_n}}$ has suddenly disappeared.
- In the lines 732-734, it seems that the authors have upper-bounded the term $-\mathbb{E} [ (1_{B_n} - 1_{B_n} 1_{B_{n+1}}) g(\theta_{n+1}) ]$ by $\min ( \delta_0, \delta_1 ) \cdot \mathbb{E}[ (1_{B_n} - 1_{B_n} 1_{B_{n+1}}) ]$, but how can this be true? The event $B_n$ does not imply that $g(\theta_{n+1}) \le \delta_2 = \min ( \delta_0, \delta_1 )$. Also, the second term has been bounded as $-\mathbb{E} [ (1_{B_n} 1_{B_{n+1}} - 1_{B_{n+1}}) g(\theta_{n+1}) ] \le \min ( \delta_0, \delta_1 ) \cdot \mathbb{E} (1_{B_n} 1_{B_{n+1}} - 1_{B_{n+1}})$, but I believe that the sign of the right hand side should be flipped, as it is currently nonpositive.
- I do not understand how lines 740-745 implies (12). There is a logical jump here, and I even do not consider the lines 740-745 reliable due to the aforementioned issues.
- In lines 758-762, I think the authors upper-bounded the inner product term $-1_{B_n}^{(-)} \frac{\alpha_0 \nabla g(\theta_n)^T \nabla g(\theta_n, \xi_n)}{\sqrt{S_n}}$ by  $-1_{B_n}^{(-)} \frac{\alpha_0}{2} ( \frac{1}{M+1} \frac{||\nabla g(\theta_n, \xi_n)||^2}{\sqrt{S_n}} + (M+1) \sqrt{||\nabla g(\theta_n)||^2}{\sqrt{S_n}})$ using Young's inequality, but the direction of the inequality is incorrect. First I guessed they might have mistakenly put the minus sign on the right hand side, but then I do not understand how the next inequality (line 767) is derived.

Below, I pinpoint the some writing issues including unclear sentences, grammar/vocabulary issues, missing/incorrect notations and typos, and other problems compromising the paper's flow and readability. Note that this is not even a comprehensive list, and the paper would require a lot of polishing with respect to the below list and more.
- In line 27, "optimums" should become "optima".
- In line 39, "varient" should become "variant".
- In line 55-56, "The $L^2$ max-margin solution $\theta^* / ||\theta^*||$ as the vectors ..." is grammatically incorrect. Something like "is defined" should be inserted in the middle. Also, some discussion on the uniqueness of (2) might be needed here.
- In lines 77-78, the phrase "are based on the situation that mini-batch stochastic gradient holds" is unclear, both in terms of the grammar and meaning. Please be precise with technical terminologies at least. I think "mini-batch stochastic gradient" isn't something that can "hold" in any sense.
- In lines 84-86, the sentence "For example, ..., bypassed by considering the dynamic system in different segments." is entirely unclear to me. I think there is no point of including this discussion if the authors can't clearly convey the high-level intuition behind what the challenges are to the readers who are not already familiar with the detailed proof techniques they have.
- In line 96, the authors mention some prior work on AdaGrad-Diagonal (which they haven't defined at this point) that are seemingly contradictory to the paper's main results, and this was confusing during the first pass. Please further clarify how AdaGrad-Norm and AdaGrad-Diagonal are different, and why this isn't a contradiction.
- In line 138, the concept of filtration appears suddenly. Does it belong to this location? 
- In lines 153-154, what did the authors precisely mean by "Since the choice of logistic regression does not affect the validity of our analysis"?
- In line 186, "there is" seems to be inserted mistakenly.
- In line 204-206, the notation $k_2$ appears suddenly without clarifying what it is. Although the authors mention Lemma B.8, I think they should explicitly mention that $k_2$ is a constant that is used for bounding the gradient of $g$ in terms of the function value.
- In line 211, what does it mean that policy learning "a classification problem in the policy space"?
- In lines 214-215 the authors say "since the rewards ... in the reinforcement learning setting are bounded, it can be shown that the stochastic gradients are almost surely bounded", which seems to be an overly strong statement. Are they claiming that this true within arbitrary RL setups? If not, precisely which cases are they referring to?
- In lines 228, 234, "inequity" were used in place of "inequality".
- In line 256, how is the law of large numbers (LLN) related to approximating $-\nabla g(\theta_n, \xi_n)$ by $-\nabla g(\theta_n)$ as $n\to \infty$? Aren't the gradient noises independent at every iteration and LLN has nothing to do with them?
- In the equation spanning lines 261-267, the undefined notation like $f_{x_i}$ is used, and it is not clearly specified what $A_n$ and $B_n$ precisely are. In fact, I believe that having this equation does not align with the purpose of illustrating the intuition of the proof because there is no clear explanation of what this expansion means, and as a reader, I have not gained any idea of what the terms $A_n, B_n$ are and where they come from.
- In line 271, "That concludes $A_n$ is the dominate term" seems grammatically incorrect.
- In line 282, what does it precisely mean by "which tends to $||\cdots||$ as $||\theta|| \to + \infty$"? I think the authors could explain more on how $f(\theta_n) \to 0$ a.s. implies their desired implicit bias.
- In line 305, "where the definition of ... can refer Equation (38) in ..." seems grammatically incorrect.
- Isn't equation (6) completely redundant with lines 261-267?
- I felt very demotivated to carefully read through Steps 1~5 of Section 4, where the authors make use of numerous notations including $T_n, f_{x_i}, C_n, D_n, \mathcal{L}$ and $s'$ whose meaning cannot be fully understood at the moment of reading through the main text, which lacks a sufficiently motivating explanation. I speculate that this can happen to many readers. I recommend the authors to rewrite this section with more careful consideration of which essential ideas and intuition they trying to convey, and how this can be done without bombarding the readers with unfamiliar mathematical terms.
- In Lemma B.3, $\epsilon$ has been used without being specified what it is.
- In line 635 (the first line of the equation), $\nabla f(\theta_n))^T$ has an extra $)$.
- In lines 674-675, I think it is authors' responsibility to show through calculations that $||\nabla^2 g(\theta)|| = \Theta(||\nabla g(\theta)||)$. Furthermore, the meaning of $\Theta$ notation is not only that $||\nabla^2 g(\theta)|| \le \tilde{d}_0 ||\nabla g(\theta)||$, but the reverse inequality should hold true with some constant other than $\tilde{d}_0$. 
- In lines 675-676, "That means existing ..." seems grammatically incorrect. 
- In line 695, I think they have a typo: $\hat{\delta}_1$ in place of $\tilde{\delta}_1$.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies the convergence of stochastic AdaGrad-Norm in the presence of linearly separable datasets. In particular, the authors want to explore if this method can converge to the max-margin solution, and hence demonstrate its implicit bias property to achieve good generalization without using regularization. A convergence rate result is also provided. Some techniques like divide-and-conquer based on the distance to the stationary point are proposed, which seem to be different from previous convergence analysis for AdaGrad-Norm type of algorithms. A small simulation is provided to validate the theory.

### Strengths
1.	Studying the convergence and implicit bias of stochastic adaptive algorithms has not been studied yet. This work provides the first attempt to close the gap.
2. Technically, the analysis seems not trival compared to previous convergence analysis of AdaGrad-Norm.

### Weaknesses
1.	The paper is not written well. There are a couple of places to be revised. First, the definition of almost surely (a.s.) is not defined. From 163-166, it is said ‘e’ is the margin vector of the data set $(x_i,y_i)$. How is it defined? From 210-215, it is a little bit hard to understand why the policy gradients under Markiv sampling becomes to the assumption made in this paper. Please elaborate. Some concrete examples might be helpful here. From line 225-239, the explanations are not clear. For example, what is the relationship between equation (4) and the goal to prove the difference between the gradient norms at $\theta_{n+1}$ and $\theta_{n}$ to be small. In line 269, why $x_{i_n}$ is the closest one to $\theta_n$? In line 305, ‘refer’ should be ‘refer to’.
2.	In step 5 of the proof sketch, could you please elaborate how to derive this recursion. 
3.	I understand that the main contribution of this work is to prove the implicit bias of stochastic AdaGrad-Norm in terms of the max-margin direction. However, the authors should mention more about why it is important to study the implicit bias. It would be more interesting to me if the authors can show some extra properties of this adaptive methods over non-adaptive methods when converging to the max-margin direction. 
4.	The proof may need double check. In (5), the first term (denoted by -A, for example) at the right side has a negative sign, i.e., Left < -A + something. Then, in line 302-303, it shows that A < E(Hn), which does not give the inequality Left < -E(Hn) because of the negative sign. I suggest a more careful check needs to be done for the entire proof. Given the current form, I am not convinced by the current version.
5.	More experiments, e.g., in real datasets, should be provided.

Overall, this work has big room to improve, in terms of writing, clarification, proof, and experiments. I am lean on the negative side.

### Questions
Please refer to the questions in the weakness part.

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
2

### Summary
This paper analyses the Adagrad-Norm algorithm on linearly separable data. The goal is study its implicit bias; i.e., the $L^2$ margin of its iterates. In particular, Adagrad-Norm is run on the cross-entropy loss. Under a boundedness assumption on the stochastic gradient norms (Assumption 3.1), the authors show that Adagrad-Norm converges to the max-margin solution almost surely (Theorem 4.2) and additionally characterize the rate of convergence (Theorem 4.3). They also show that under mini-batch stochastic gradients, the assumption holds and, thus, so do the results (Corollaries 4.1 and 4.2). The paper also conducts a small experiment to show that gradient descent and Adagrad-Norm both converge to the max-margin, while the algorithm Adagrad-Diagonal does not.

### Strengths
- The paper is clear and organized.

- Understanding the implicit bias of algorithms is important and the paper contributes in this direction by not only showing the convergence to the max-margin but also the rate of convergence.

- Rather than restricting to mini-batch stochastic gradients, the analysis holds more generally as long as Assumption 3.1 is satisfied.

### Weaknesses
- On page 8, when comparing the convergence to GD, I think it would be beneficial to explicitly mention what its rate is.

- The small dataset used for empirical validation seems limited in scope. It would be interesting to see how robust the results are for larger and more complex data.

- The paper would benefit from more concrete examples where Assumption 3.1 holds, as it is the main ingredient in the theoretical results.

### Questions
- Is there a reason why only 8 data points were used? Are results similar when there is more data? How about for higher-dimensional data?

- Given that the theoretical results hinge on linear separability, how applicable are these findings to real-world problems where data may not be perfectly separable?

### Soundness
3

### Presentation
3

### Contribution
3
