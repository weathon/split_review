# Learning the Optimal Stopping for Early Classification within Finite Horizons via Sequential Probability Ratio Test

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Time-sensitive machine learning benefits from Sequential Probability Ratio Test (SPRT), which provides an optimal stopping time for early classification of time series. However, in *finite horizon* scenarios, where input lengths are finite, determining the optimal stopping rule becomes computationally intensive due to the need for *backward induction*, limiting practical applicability. We thus introduce FIRMBOUND, an SPRT-based framework that efficiently estimates the solution to backward induction from training data, bridging the gap between optimal stopping theory and real-world deployment. It employs *density ratio estimation* and *convex function learning* to provide statistically consistent estimators for sufficient statistic and conditional expectation, both essential for solving backward induction; consequently, FIRMBOUND minimizes Bayes risk to reach optimality. Additionally, we present a faster alternative using Gaussian process regression, which significantly reduces training time while retaining low deployment overhead, albeit with potential compromise in statistical consistency. Experiments across independent and identically distributed (i.i.d.), non-i.i.d., binary, multiclass, synthetic, and real-world datasets show that FIRMBOUND achieves optimalities in the sense of Bayes risk and speed-accuracy tradeoff. Furthermore, it advances the tradeoff boundary toward optimality when possible and reduces decision-time variance, ensuring reliable decision-making. Code is included in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers sequential probability ratio test (SPRT) under finite horizon. Bayes optimality characterizes backward induction equation, given in Theorem 2.1 in the paper. The contribution of the paper is to provide a statistical method that implements this formulation. This task involves estimating the conditional expectation function as well as density ratio estimation. The former exploits concavity in the backward induction equation and gives an option of Gaussian process (GP) regression for speed-up. Theorem 3.2 indicates that the proposed method is statistically consistent. An extensive set of experiments provides numerical evidence that the propose method works better than vanilla SPRT with static threshold.

### Strengths
- SPRT under finite horizon seems very relevant in practice.
- The proposed method is well grounded in Bayes optimality.
- The numerical results are extensive.
- The figures look impressive, although information contained in each of them is very dense.

### Weaknesses
 - The paper is very lengthy if we include the appendices (60 pages in the current format). Purely based on the length, one might argue that it might be better to publish this paper in JMLR or a journal outlet.
- Theorem 3.2 informally states the consistency of the proposed method and Theorem J.1 in Appendix J gives a formal statement. However, assumptions are given in the forms of lemmas and thus they are not low-level or easy-to-understand conditions. In fact, the lemmas are theoretical results from Siahkamari et al. (2022, ICML) titled "Faster algorithms for learning convex functions". In view of that, it is not very innovative in terms of proving the consistency of the proposed method.

### Questions
- It would be helpful to clarify the main contribution of this paper. It seems to me that this paper is a convex combination of three existing results: (i) Bayes optimality via backward induction equation, (ii) convex function learning, and (iii) density ratio estimation. Would it be fair to say that the current paper is novel in the sense that it combines the three above but each of them is already developed by previous works?
- It is intriguing that Gaussian process (GP) regression gives a substantial speed-up. Would it be possible to establish consistency using GP?
- There is no theoretical result regarding the convergence rates or minimax lower bound. It might be good to indicate them as possible future research topics.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a framework to enhance early classification in time-sensitive applications by adapting the Sequential Probability Ratio Test (SPRT) for scenarios with finite horizons. The contribution is motivated by applications where decisions must be made within limited timeframes. The paper draws from ideas in Convex Function Learning (CFL), Density Ratio Estimation (DRE), and Gaussian Process (GP) Regression—and develops a framework for achieving optimal stopping in early classification tasks. Notably, CFL is used to estimate continuation risk efficiently, providing theoretically consistent estimations; GP regression is used as a faster, though slightly less statistically consistent, alternative; and integrates Density Ratio Estimation (DRE) algorithm for accurate log-likelihood ratio (LLR) estimates. The authors focus on Bayes-optimal solutions for early classification, which are supported by consistency results for CFL and DRE estimations.

### Strengths
CFL is chosen specifically for its ability to offer statistically consistent estimates of the continuation risk function, which is concave in nature. This consistency is achieved by leveraging convex regression to estimate the conditional expectations that are key to solving the backward induction. The authors support this choice by citing prior work. 

The DRE algorithm, specifically the SPRT-TANDEM variant, enhances LLR estimation accuracy by directly estimating the density ratios, avoiding the need to estimate individual probability densities. This approach reduces degrees of freedom, resulting in more stable and accurate LLR estimates across various data distributions (both i.i.d. and non-i.i.d.). The resulting approach handles both synthetic and real-world datasets more flexibly.

GP regression is presented as a faster but less consistent alternative, primarily for cases where computational speed outweighs the need for the strict statistical consistency.

### Weaknesses
1. The paper would benefit from more detailed empirical comparisons with traditional methods to demonstrate performance gains in practice.

2. Assessment/comparison of DRE’s advantage with respect to other estimation remains a question.

3. More discussion is needed on scenarios where GP regression’s speed justifies its consistency loss. Overall leaving tradeoff in consistency with GP regression is underexplored.

4. The overall approach becomes multi-component approach – adding implementation complexity and training across datasets. Specialized tuning (e.g., ADMM for CFL) may raise setup complexity.
Some potentially related work (in terms of ideas/concepts) include:

“Analyzing the discrepancy principle for kernelized spectral filter learning algorithms,” Alain Celisse and Martin Wahl, (2020) J. Mach. Learn. Res.

“WALD-Kernel: A method for learning sequential detectors,” Diyan Teng and Emre Ertin (2016) IEEE Statistical Signal Processing Workshop (SSP)

“Bayesian Optimization Meets Bayesian Optimal Stopping,” Zhongxiang Dai and Haibin Yu and K. H. Low and Patrick Jaillet (2019). Proposes unifying GP-UCB with Bayesian Optimal Stopping (BO-BOS). Focuses on hyperparameter tuning efficiency rather than early classification tasks.

### Questions
While the paper contributes to the question of how Convex Function Learning (CFL) be effectively integrated with Density Ratio Estimation (DRE and Gaussian Process Regression (GPR) for synergistic benefits in early classification tasks, what would be authors’ recommendation on evaluation of their combined advantage and limitations in practical settings?  This overall question relates to items 1-4 in the “weaknesses” section above. 

Under what conditions does the proposed multi-component framework maintain statistical consistency in small sample settings typically found in real-time applications? Although some statistical properties are explored, there is still uncertainty about how these methods perform and remain consistent under stringent data constraints.

Finally, what practical obstacles exist in deploying these methods at scale in time-sensitive applications?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces FIRMBOUND, a framework for early classification of time series tasks that builds on the Sequential Probability Ratio Test (SPRT) to address computational challenges in estimating the solution to backward induction from training data. FIRMBOUND uses density ratio estimation and convex function learning to provide consistent estimators for the sufficient statistic and conditional expectation, enabling to minimize Bayes risk for optimality. The paper then presents a faster alternative using Gaussian process regression, which reduces training time while retaining low deployment overhead, albeit with potential compromise in statistical consistency. Experiments demonstrate that FIRMBOUND achieves optimalities in the sense of Bayes risk and speed-accuracy tradeoff.

### Strengths
1. Convex function learning could give a consistent estimator of the backward induction functions. The Gaussian process regression gives a computationally more efficient approach for  CFL. 
2. The minimizer of the Log-Sum-Exp Loss gives a consistent estimation of the log density ratio. 
3. Combining the two approaches, FIRMBOUND with CFL is consistent and Bayes optimal for ECTS. 
4. The paper performed experiments across synthetic data and real world data, demonstrating that FIRMBOUND achieves optimalities in the sense of Bayes risk and speed-accuracy tradeoff. 

In general, this paper provides a method that solves an important task and works well in practice.

### Weaknesses
1. The procedure requires a two-step estimation: first estimate the sufficient statistics (log density ratio) with finite samples; then, based on the estimated sufficient statistics, estimate the backward induction function. The error made in the first step could make the second step much harder. Figure 5 seem to show that estimated LLRs indeed perform worse than true LLRs.


### Questions
NA

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies the problem of optimal stopping time for early classification of time-series. The problem is to identify the best time to stop and identify the correct class of a time-series as the time-progresses. It is known that the optimal method for this problem with a finite time-horizon is the backward induction equation that is computationally and sample complexity wise intractable. The paper makes two contribution (i) reducing the complexity of the backward induction method by observing that conditional expectation in backwards induction is a convex function learning under noise problem which has standard techniques. (ii) Further assuming the conditional expectation sequence follows a gaussian process thus reducing it to GP regression learning. They show their method achieves close to optimal speed accuracy trade-off for the problem against four baselines on synthetic and real world datasets.

### Strengths
1. The paper tackles an interesting and technically hard problem. 

2. The ideas and the algorithm seems sound and practically implementable.

3. The empirical experiments are thorough and has real world datasets.

4. The paper explains the ideas in a nice sequence even though some parts are hard to parse.

### Weaknesses
1. Some parts of the paper are too dense and hard to parse. For instance can the authors expand on the intuition behind the various terms of the backward induction equation in Theorem 2.1. Specifically, the paper would benefit from a more detailed explanation of how the conditional expectation in equation (5) relates to the overall risk minimization problem. The connection between the expected future minimum risk and the current decision to stop or continue is not entirely clear. A more intuitive explanation of how this expectation is calculated and used in the backward induction process would be beneficial.

2. Why does FIRMBOUND not improve upon vanilla SPRT in terms of performance gains on the real datasets? The paper mentions that the sufficient statistic trajectories are relatively monotonic, but this explanation is not entirely convincing. It would be helpful to see a more rigorous analysis of why this monotonicity limits the performance gains. For example, are there specific characteristics of the real-world datasets that lead to these monotonic trajectories, and how do these characteristics differ from the synthetic datasets where FIRMBOUND shows more significant improvements? A deeper investigation into the properties of the sufficient statistic trajectories and their impact on FIRMBOUND's performance is needed.

### Questions
Asked above.

### Soundness
3

### Presentation
2

### Contribution
3
