# General Stability Analysis for Zeroth-Order Optimization Algorithms

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Zeroth-order optimization algorithms are widely used for black-box optimization problems, such as those in machine learning and prompt engineering, where the gradients are approximated using function evaluations. Recently, a generalization result was provided for zeroth-order stochastic gradient descent (SGD) algorithms through stability analysis. However, this result was limited to the vanilla 2-point zeroth-order estimate of Gaussian distribution used in SGD algorithms. To address these limitations, we propose a general proof framework for stability analysis that applies to convex, strongly convex, and non-convex conditions, and yields results for popular zeroth-order optimization algorithms, including SGD, GD, and SVRG, as well as various zeroth-order estimates, such as 1-point and 2-point with different distributions and coordinate estimates. Our general analysis shows that coordinate estimation can lead to tighter generalization bounds for SGD, GD, and SVRG versions of zeroth-order optimization algorithms, due to the smaller expansion brought by coordinate estimates to stability analysis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this submission, the authors proposed a general frame-work to prove the generalization error for the zero-order optimization methods. They proved the generalization error bounds for different zero-order optimization algorithms such as SG, GD and SVRG under different convexity conditions. They also conduct numerical experiments.

### Strengths
This submission is very clear with simple structures and languages. The main idea is natural and understandable. The mathematical and theoretical analysis is strict and the empirical results are consistent with the theoretical analysis.

### Weaknesses
There is no significant weakness for this submission.

Only one question is that for the ZO-SGD, ZO-GD and ZO-SVRG with one-point and two-point gradient estimation, the authors only presented the results for the none-convex setting. Is there any theoretical results for the general convex and strongly convex settings? Like the results for the coordinate-wise gradient estimation. If the authors could add these theoretical results, it could make the theoretical contributions much more complete.

### Questions
Please check the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on zeroth-order optimization algorithms. While previous stability analysis results were limited to the basic 2-point zeroth-order estimate with a Gaussian distribution in stochastic gradient descent (SGD) algorithms, this paper introduces a general proof framework for stability analysis. This framework is applicable to convex, strongly convex, and non-convex conditions and provides results for various zeroth-order optimization algorithms, including SGD, gradient descent (GD), and stochastic variance-reduced gradient (SVRG) methods. It also covers different zeroth-order estimates, such as 1-point and 2-point estimates with various distributions and coordinate estimates. The general analysis reveals that coordinate estimation can lead to improved generalization bounds for SGD, GD, and SVRG versions of zeroth-order optimization algorithms by reducing the expansion in stability analysis.

### Strengths
- The paper exhibits a well-organized structure, including a clear motivation, an extensive literature review, and a rigorous theoretical analysis. However, I have not verified the validity of all statements in the Appendix.
- One intriguing and original contribution of the paper is its theoretical assertion that coordinate estimation can enhance the generalization bounds for zeroth-order optimization algorithms like SGD, GD, and SVRG.

### Weaknesses
 - Theoretical contributions, especially those stemming from the primary theoretical lemmas (Lemma 3 and 4), are incremental compared to prior works such as (Hardt et al., 2016) and (Nikolakakis et al., 2022).
- The paper could benefit from more extensive numerical experiments and a more detailed implementation section. Specifically, it should include a comparison of the performance of various zeroth-order estimators, providing empirical support for the favorable theoretical results associated with coordinate estimation.

### Questions
Majors:

1. What is the zeroth-order estimator used in the experiments?
2. How do different zeroth-order estimators affect the optimization performance?

Minors:
- Please indicate beta and C in Table 1.
- Figure 2(b):  Generalization error: GD - >  Generalization error: SGD?
- More implementation details are needed.
- Utilize parenthetical citations to enhance readability.

### Soundness
3 good

### Presentation
3 good

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
In this paper, a new simple framework for analyzing the generalization error of zeroth order optimization for Lipschitz and smooth objective functions is proposed and several novel generalization bounds are provided. The framework proposed consists of a method for analyzing the stability of a given optimization algorithm, based on the notions of boundedness and expansivity of the corresponding update rule. The update rules considered all correspond to zeroth order analogues of first order optimization algorithms, where a first order oracle is approximately simulated using queries to the values of the objective function (i.e., a zeroth order oracle). The simulated oracles considered are based on either 1-point, 2-point or coordinate-wise approximation, and the latter achieves the tightest generalization bounds for each of the algorithms considered, matching, in each case, the best known bounds achievable by the corresponding first order algorithms in each of the cases where the objective is strongly convex, convex or non-convex. The algorithms considered are Gradient Descent, Stochastic Gradient Descent as well as Stochastic Variance Reduced Gradient method. The theoretical guarantees of the paper are accompanied by experimental results on real world data.

### Strengths
The results provided in this paper, which are obtained by leveraging a simple yet powerful framework and the idea to approximate the gradient of a smooth and Lipschitz function coordinate-wise, are strong and, to the best of my knowledge, novel. The presentation of the results is clear and detailed.

### Weaknesses
One potential weakness of the paper is that the results assume that the objective function is smooth, which, in many important optimization problems (e.g., learning ReLU networks) is not true.

### Questions
Could your results be extended to the case where the objective function is not smooth? Are there any generalization bounds for this setting, even for first order algorithms?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the generalization bound of zero-order methods and presents a general analysis framework. Results on 2-point, 1-point, and coordinate-wise gradient estimators are established, which improves the existing work in this direction. Based on these results, the authors show that coordinate estimation leads to tighter generalization bounds for many zeroth-order methods. Experiments are also provided to verify the theoretical conclusions.

### Strengths
1. The paper is well-presented and well-organized. The motivation, technique, and results are clearly stated.

2. The framework established is a nice theoretical contribution. Consequently, the generalization bounds of many zero-order methods are developed. Moreover, the differences between these generalization bounds are captured and analyzed, making the whole theory complete and convincing.

3. The technique used in the paper is solid and interesting.

### Weaknesses
It would be better if the author emphasized the new technique and idea used in this paper compared with the existing work by Nikolakakis et al. (2022).

### Questions
In Figure 1 (b), why did the generalization bound of ZO-SVRG decrease at the beginning?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
