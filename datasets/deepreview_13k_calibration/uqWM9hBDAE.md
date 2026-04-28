# How Much is Unseen Depends Chiefly on Information About the Seen

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
It might seem counter-intuitive at first: We find that, \emph{in expectation}, the proportion of data points in an unknown population---that belong to classes that do \emph{not} appear in the training data---is almost entirely determined by the number $f_k$ of classes that \emph{do} appear in the training data the same number of times.
  While in theory we show that the difference of the induced estimator decays exponentially in the size of the sample, in practice the high variance prevents us from using it directly for an estimator of the sample coverage. However, our precise characterization of the dependency between $f_k$'s induces a large search space of different \emph{representations} of the expected value, which can be deterministically instantiated as estimators. Hence, we turn to optimization and develop a genetic algorithm that, given only the sample, searches for an estimator with minimal mean-squared error (MSE).
  In our experiments, our genetic algorithm discovers estimators that have a substantially smaller MSE than the state-of-the-art Good-Turing estimator. This holds for over 96\% of runs when there are at least as many samples as classes. Our estimators' MSE is roughly 80\% of the Good-Turing estimator's.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper makes a contribution to the estimation of the missing mass probability by providing a distribution free estimator that minimizes the mean-squared error after formalizing it as a constrained optimization problem. The authors provide a genetic algorithm that numerically solves the program. They use synthetic and real data experiments on various distributions to compare the resulting estimator to the classically used Good and Turing estimator.

### Strengths
- The paper clearly states the problem formulation (fitness function and search space) and proposes a numerical algorithm to solve it.
- The resulting estimator shows a strong performance in terms of MSE and is relatively cheap to compute.
- The presentation and the figures are very clear and well-explained.

### Weaknesses
 - The empirical application is $\textbf{insufficient}$, only one real world dataset was used and the experiments were done only on 50 datapoints. 
- No $\textbf{theoretical guarantees}$ were given for the minimal MSE estimator of the missing mass probability. 
- Comparing the proposed genetic Aagorithm to some other optimization approaches  as well as studying the properties of the resulting estimators would be helpful.

### Questions
- Are there any theoretical guarantees in terms of MSE when running the optimization on a smaller sample size to compute the estimator for a larger size using the provided formula ?

- How does the proposed minimum MSE estimator perform compared to a distribution-aware estimator for different distributions?

- How does the effectiveness of the proposed estimator look like for strictly positive values of $k$?

- Given a fixed dataset, what is the variance of the resulting estimator's MSE output by the GA (given randomness in mutations)?

### Soundness
3

### Presentation
3

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
This paper addresses the challenge of estimating the expected value of  $M_k$ , which represents the probability that the (n + 1)th observation is an element observed exactly $k$  times in the training data. By precisely characterizing the dependencies among frequency counts, the authors provide a detailed decomposition of $ \mathbb{E} [M_k] $. They introduce a class of estimators that can be constructed using algorithm-based optimization. These proposed estimators outperform the well-known Good-Turing estimator in terms of accuracy.

### Strengths
This paper is significant, since estimating the missing mass is a classic and fundamental problem in statistics with broad practical applications. Making advances over the widely used Good-Turing estimator is important, and such progress has the potential to bring substantial empirical improvements. This paper is also novel in its approach: their analysis do not rely on Poisson approximation, which allows for deeper and more flexible analysis. Additionally, the paper presents a thorough evaluation of the proposed algorithms, including theoretical insights and synthetic experiments that demonstrate the minimal-bias estimator’s substantially lower bias compared to the Good-Turing estimator across various distributions.

### Weaknesses
No obvious weakness is found.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the problem of estimating the probability of having test points that do not appear in the training data. A class of estimators is provided, and the method for finding an optimal estimator is discussed.

### Strengths
The paper is well-written: the setting discussed in this work, as well as the proposed methodology, is clearly stated, and relevant questions are answered.

### Weaknesses
I don't feel that the motivation for and usefulness of the problem are sufficiently explained.

I'm not sure if it is appropriate to call the proposed method a 'distribution-free' method. According to the footnote, the context in this work is that the method 'does not impose assumptions on the parameters $p$ or $n$,' but this seems more like a standard setting for a parametric (multinomial) model, and is quite different from the usual meaning of 'distribution-free' (such as in conformal prediction context).

### Questions
1. As stated in the 'weakness', could the authors provide more explanations for why this is an important problem? When is it helpful to know in advance the probability of a test point being equal to one of the training/calibration data points?

2. Specifically, what do the proposed method (or existing methods) advise practitioners to do with their datasets? For example, if one is given the training and calibration data along with test feature inputs, and the goal is to predict the test outcome, there can be various procedures with different approaches---how does the problem/method in this work affect the overall procedure? If we know that the test point is unlikely to be equal to (or drawn from the same distribution as) one of the observed points, what can we do with that information?

3. I'm not sure if it is appropriate to call the proposed method a 'distribution-free' method. According to the footnote, the context in this work is that the method 'does not impose assumptions on the parameters $p$ or $n$,' but this seems more like a standard setting for a parametric (multinomial) model, and is quite different from the usual meaning of 'distribution-free' (such as in conformal prediction context).

### Soundness
4

### Presentation
4

### Contribution
2
