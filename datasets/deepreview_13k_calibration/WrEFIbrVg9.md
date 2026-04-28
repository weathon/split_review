# Non-asymptotic Analysis of Stochastic Gradient Descent under Local Differential Privacy Guarantee

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
In private machine learning algorithms, Differentially Private Stochastic Gradient Descent (DP-SGD) plays an important role. Despite this, there have been few studies that have explored the theoretical analysis that can be derived from DP-SGD, particularly in a more challenging scenario where individual users retain the autonomy to specify their differential privacy budgets. In this work, we conduct a comprehensive non-asymptotic analysis of the convergence of the DP-SGD algorithm as well as its variants. This will allow individual users to assign different privacy guarantees when releasing models trained by DP-SGD. Most importantly, we provide readers with practical guidelines regarding the effect of various hyperparameters, such as step size, parameter dimensions, and privacy budgets, on convergence rates. The problem we consider includes the most commonly used loss functions in standard machine learning algorithms. For strongly convex loss functions, we establish an upper bound on the expected distance between the estimators and the global optimum. In the case of non-strongly convex functions, we analyze the upper bound difference between the loss incurred by the estimators and the optimal loss. Our proposed estimators are validated in the theoretical and practical realms by rigorous mathematical derivation and numerous numerical tests.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper claims to perform a comprehensive non-asymptotic analysis of the convergence guarantee of the DP-SGD algorithm. Rightfully so, if this is done correctly, it provides guidelines to the practitioner how to best choose various hyperparameters if we aim to achieve certain convergence rates. Considering that hyperparameter tuning is one of the important problem, such a study is definitely worth pursuing.

### Strengths
The strength of the paper is to perform the tedious calculation to show the non-asymptotic analysis on the convergence rate.

### Weaknesses
While the major motivation of the paper is to provide a guideline to practitioners as to how they should choose hyperparameters, I really (like really) do not see how one can figure out these hyperparameters from the expression they have in the theorem statement. I find it extremely hard to parse their theorem statements. One benefit of asymptotic analysis is that it makes expression a bit easier to parse. If the authors do insist on writing the exact non-asymptotic bounds, then I would suggest they work a bit more on making the expression simpler. Having experience with practitioners, I can guarantee that no one would take their theorem and try to work out hyperparameters from it, at least not analytically. Nesterov-Nemerivoski's results are not influenced because they give an asymptotic bound, but because they give simple to state bounds, and in reality, they are not that far from what you get in practice for certain loss functions.

I also find the assumption on assumption on Hessian a bit too much.

The paper has several typos. One glaring one is citing the same set of authors on page 2 (second paragraph). Another one that comes to my mind is the missing cross reference on the first page of the supplementary material. The one that really annoyed me is the references in the Remarks. It does not take a lot of effort to write Theorem 3 instead of (3). However, it shows the lack of diligence the authors put in writing their paper.

### Questions
None. Please read the weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides the convergence result of sgd for lipschitz functions under the local differential privacy, both for the strongly convex setting and the non-convex setting.

### Strengths
The paper provides detailed proofs of their theoretical results, with several numerical simulations.

### Weaknesses
1. I think authors may not provide a good explaination on their motivation on using GDP instead of classical LDP notation, see also Question 1.

2. Both the results and proof techniques in this paper are similar to those in [1] in the non-private setting. It appears that the introduction of additional Gaussian noise does not pose significant challenges to the analysis. However, the authors do not explicitly compare their paper to [1] or other non-private research in both the proof and result sections. The lack of discussion on how the privacy mechanism impacts the convergence rate compared to the non-private setting is a significant oversight. Specifically, it is unclear how the added noise affects the constants in the convergence bounds, and whether the privacy parameter has a direct impact on the convergence speed. This makes it difficult to assess the practical trade-offs between privacy and accuracy.


### Questions
I have several questions on the paper's motivation and theoretical results:

1. Why did the authors choose to employ GDP notation rather than LDP in the paper? As far as my understanding goes, GDP's primary advantage is its tighter composition guarantee. However, within the context of this paper, where each user's data passes through the algorithm only once, the notion of composition does not apply. Consequently, I am struggling to understand the underlying motivation and advantages of adopting GDP notation.

2. Concerning the theoretical results when $\alpha = 1$: In the convergence rate section of Remark 1, the authors assert that "For a scenario where $\alpha = 1$, convergence of the LDP-SGD estimator $\theta_n$ is not assured." Nevertheless, based on my knowledge, at least in the strongly convex setting, the convergence analysis of LDP-SGD with a step size $\theta_i = O(1/i)$ seems to be readily attainable by adapting the proof provided in [1]. Have I possibly overlooked any technical complexities?

[1] Alexander Rakhlin, Ohad Shamir, Karthik Sridharan, "Making Gradient Descent Optimal for Strongly Convex Stochastic Optimization," 2011.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on the non-asymptotic analysis of the convergence of the DP-SGD (Differentially Private Stochastic Gradient Descent) algorithm and its variants. The authors analyze the convergence of the DP-SGD algorithm and provide practical guidelines on the effect of various hyperparameters such as step size, parameter dimensions, and privacy budgets on convergence rates. The paper provides theoretical bounds on the expected distance between the estimators and the global optimum for strongly convex loss functions. For non-strongly convex functions, the paper analyzes the difference between the loss incurred by the estimators and the optimal loss.

### Strengths
Strength:
1.	The paper provides a comprehensive understanding of the convergence behavior of DP-SGD and to help practitioners choose appropriate hyperparameters for their specific use cases.

2.	The paper contains fine analysis for both strongly convex case and non-strongly convex case.

### Weaknesses
Weakness:
1.	The paper does not provide any lower bounds so it is hard to evaluate the tightness of results. 

2.	This paper lacks comprehensive comparisons to prior works. There are many works on stochastic gradient descent on local differential privacy guarantee. For example, Algorithm 4 in Wang, Teng, et al. "Local differential privacy for data collection and analysis." Neurocomputing 426 (2021): 114-133 and Algorithm 1 in Liu, Ruixuan, et al. "Fedsel: Federated sgd under local differential privacy with top-k dimension selection." Database Systems for Advanced Applications: 25th International Conference, DASFAA 2020, Jeju, South Korea, September 24–27, 2020, Proceedings, Part I 25. Springer International Publishing, 2020.  From my point of view, this is not the first work on LDP-SGD, and therefore a comprehensive comparison is expected in this paper. I suggest the author adding a table including previous results and this work. Also, the upper bounds in the paper are unnecessarily long, for simplicity and better rendering I suggest keeping the leading asymptotic term.

3.	The technical contribution is relatively weak as I could not find sufficient novelty in the proofing techniques.

4.	The presentation of this work could be enhanced. Specifically, it appears there may be an issue with the visibility of equations 3 and 4, which I presume are the upper bounds in Theorems 3 and 4. This could potentially be a result of a compiling error.

### Questions
1.	There is an obvious typo in the proof. On page 1 of supplementary material, “For the second term of (1), by Condition ??, we have…”, here Condition ?? should be Condition 2.
2.	Why the authors particularly favor Polyak-Ruppert averaging estimator in the theoretical analysis? It would also be interesting to see the results of many other variants of SGD that give better performance.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the benefit of weight averaging (specifically, Polyak-Ruppert averaging) in private optimization. Specifically, it considers the strongly/general convex + smooth setting along with *Hessian smoothness* albeit only w.r.t. the optimum (i.e., Condition 3). Under these assumptions, it is shown that the (non-asymptotic) convergence bound of the Polyak-Ruppert averaging scheme is better than that of the last iterate with suitable step-size choices. Some small-scale experiments are shown to corroborate the theoretical findings.

### Strengths
Solid theoretical analysis showing the improvement offered by the averaged iterate over the last iterate in private optimization. I'm not up to speed on all of the recent papers in private optimization, but as far as I know, there are no results like the ones in this paper showing the benefits of weight averaging in private optimization. The paper just makes the cut for me because of this.

### Weaknesses
 **1.** *The presentation of the theoretical results needs to be improved and simplified*. For e.g., Theorem 4 is very hard to parse and overloaded with too many symbols. I'd recommend deferring the full versions to the Appendix and presenting abridged versions in the main paper having only the important terms. Also, I'd have liked to see a remark or something *explicitly* comparing the dependence of the convergence bounds of the averaged iterate and last iterate w.r.t. $n$ *together* (and therefore, explaining why the averaged iterate does better) rather than leaving it to the reader. The current presentation makes it difficult to quickly grasp the core message of the theorem and how the averaging procedure leads to a tighter bound. It is crucial to highlight the specific terms that contribute to the improved convergence rate due to averaging, such as the reduced variance component, and to clearly contrast this with the last iterate's bound. Without this explicit comparison, the reader has to perform a non-trivial amount of work to understand the benefit of the proposed approach. 

**2.** Looking at Theorem 4, there is a term of $||	heta_0 - 	heta^{\ast}||^4$ whereas in Theorem 3, there is just $||	heta_0 - 	heta^{\ast}||^2$. If our initialization is very far from the optimum, this may make the averaged iterate have worse convergence than the last iterate. This point should be discussed in the paper. The impact of this quartic term on the convergence behavior of the averaged iterate needs to be explored in more detail. Specifically, the paper should discuss scenarios where the initial parameter is far from the optimum and how this affects the practical performance of the algorithm. A more thorough analysis of the conditions under which the averaged iterate will outperform the last iterate is needed, especially considering the potential for a significant penalty due to the $||	heta_0 - 	heta^{\ast}||^4$ term.

**3.** I understand that this is a theoretical paper and so I don't want to complain too much about the scale of the experiments, but for this proposal to be more convincing and practically useful, the authors should consider performing some larger experiments -- beyond linear/logistic regression and definitely with larger $d$. The experiments should also include different privacy budgets to see how the performance changes in different privacy regimes. The current experiments, while demonstrating the theoretical findings, are not sufficient to show the practical relevance of the proposed method in real-world scenarios. 

**4.** It'd be nice to also provide some intuitive explanation of why averaging helps instead of just math.

### Questions
**1.** Is Condition 3 being used in Theorem 3? I don't see any $C_1$ term in Theorem 3.

**2.** Why are there $E\big(||\theta_0 - \theta^{\ast}||^2\big)$ and $E\big(||\theta_0 - \theta^{\ast}||^4\big)$ terms in the results? These are deterministic, right? Or are you taking expectation w.r.t. something else here?

**3.** What are the constants $C_{3,0}$ and $C_{4,0}$ in Theorem 4? Overall this theorem needs to be simplified and cleaned up as I mentioned in Weaknesses.

**4.** Can the results be extended to regular $(\varepsilon,\delta)$-DP? Or is there a reason the authors are considering GDP?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
