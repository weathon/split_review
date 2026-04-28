# offline_rl_ope: A Python package for off-policy evaluation of offline RL models with real world data

- Decision: Reject
- Avg Score: 2.33
- Scores: 3, 3, 1

## Abstract
offline_rl_ope is a fully unit tested and runtime type checked Python package for performing off-policy evaluation of offline RL models. offline_rl_ope has been designed for OPE workflows using real world data by: naturally handling uneven trajectory lengths; including novel convergence metrics which do not rely on OPE estimator ground truths; and providing a compute and data efficient API which can be integrated with many offline RL frameworks. This paper motivates and describes the core API design and functionality to enable ease of use and extension. The implementations of OPE methods have been benchmarked against existing implementations to ensure consistency and reproducibility. The offline_rl_ope source code can be found on GitHub at: REDACTED.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a python package for off-policy evaluation methods. It has integrated common methods such as IS, WIS, PD, WPD, etc. The package supports multiple metrics and portable APIs for most of the classic methods. The paper also compares with a similar work **Scope-RL**, and shows the advantages of this work. Some details of the implementation of the existing work are discussed in the paper, which provides readers with necessary background information on the relevant techniques.

### Strengths
- The paper proposes a useful Python package for the off-policy evaluation methods in the RL domain, which can be helpful for an easy-to-use toolbox if one wants to implement an evaluation method quickly. 
- The paper discussed some technique details of existing work, making readers out of the domain clearer on how the authors provide unified implementations. 
- The author also provides a flowchart on how the package is designed and how each module is connected with each other.

### Weaknesses
 - The paper is obviously written in a rush, with multiple unclear expressions and roughly created tables. For example, the caption text is not aligned between lines in Figure 1, the missing caption in Figure 2. Lack of explanations for equations  - see details in the questions section.
- Based on the content of the paper, it is not clear the significant contributions made by this work, while the unified framework for multiple off-policy evaluators is appreciated, it seems like the calibration of performance of the implemented methods is not mentioned, but it is crucial for a standard comparisons and potential users to care about. 

> E.g1., authors can consider the use of Mean Absolute Error (MAE) to calculate the error between the OPE estimates and the ground truth for each method, while lower MAE indicates that the method is better calibrated.

> E.g2., another suggestion is the calibration curve: authors can consider generating the calibration visualization plots by showing the estimated returns (OPE results) against actual returns. In this test, a well-calibrated model should ideally fall on the diagonal line. This can provide better insights into how trustworthy this work's implementation is.
- The presentation in the paper is too simple and not informative. 
E.g., it is unclear how many times the experiments have been done for the result report, from the table 6-7-8, are the values reported in the table average values or the experiment results from one execution? A more convincing way of conveying the results is by: mean ± std for a method's stable performance. Similarly for the content in the Figure 2.

### Questions
1. The format for the caption in Figure 1 seems not aligned, it is suggested to adjust for better presentation.
2. Figure 2 is not completed. The caption content is not described at all.  
3. In line 794, what does `??` refers to? 
4. In the section 4, line 380, there are some grammar issues in the writing for this paragraph, e.g., `been unit tested however....`, there lacks a comma before the 'however', and the content is actually no contrast in the content of this sentence.  
5. Since this is a benchmark paper, it is important to know whether the author has calibrated the performance of the implemented IS methods and DR estimators? Are the performance of these methods aligned with the original research papers? 
6. The equations are not fully numbered, for example, the equation about the `self-normalized weights` is not labeled, besides, it lacks explanations for this equation, and notation $\epsilon$. 
7. In table 5, what does the difference mean? I.e., the difference between oracle IS vs implemented version in offline-rl-ope? or between Scope-RL vs offline-rl-ope (it seems like the two columns are duplicated, there is no further discussion regarding the table)?

### Soundness
2

### Presentation
1

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
This paper describes a novel software library called offline_rl_ope to make real-world off-policy evaluation of RL policies easier. In particular, the python package (and paper) focus on Importance Sampling-based OPE methods (in contrast to fitted Q evaluation), as IS-based methods are missing a canonical implementation. The paper describes the problem of OPE, motivates the API design and functionality, and discusses common metrics for OPE.  Finally, the authors perform benchmarks against other existing software to ensure correctness. 

Overall, I think the paper is interesting and potentially useful to the community. I have some questions about novelty, and what are the claimed contributions. Some of the results are difficult to evaluate. Perhaps the authors can help shed light on key questions that will better inform my decision. 

I recommend rejecting the paper in its current form, as I do not believe it holds up to ICLR standard.

### Strengths
The paper proposes a software library with a good API. The abstractions utilized by the API are organized around important calculations in the OPE problem setup. The high-level code interface makes it easy for non-experts to evaluate their policies with simple python code.

The proposed library fills gaps in existing work (ie., Scope RL). In particular, facilitating evaluation of policies with uneven trajectories is a particularly useful feature.

The experimental cross-validation of the offline_rl_ope implementation and existing implementations is very strong and suggests the quality of the algorithms.

### Weaknesses
The overall contribution (while useful) seems small as other libraries do exist. Scope RL has a number of useful features, while d3rlpy has implemented FQE. I am not saying the proposed work has zero novelty; only that there is meaningful prior art in the space.

The claimed contributions are not entirely clear. I understand that the software package is new and how it compares to previous work. However, some of the contributions regarding metrics are not clear. For example, the VWP and WeightStd metrics are presented and experimentally validated. This would suggest that they are novel to the paper. Additionally, the authors state, “the metric ”VWP” (valid weight proportion) is proposed.” This leads me to believe that they are proposed here, but this verbiage is somewhat ambiguous as this also follows a discussion of ESS, which is not new. The major difficulty is that this contribution is stated neither in the abstract nor in the introduction, which casts doubt on the conclusion that they are novel to this paper.

The experimental validation of continuous action space in Section 4.2 is difficult to understand. The authors state, “offline rl ope and Scope-RL differed significantly in their approach and as such, could not be compared against one another.” Consequently, the authors only compare the relative ranking of the OPE outputs and compute the spearman correlation coefficient. While ranking is useful, I cannot assess the absolute quality of the OPE outputs under this condition, which casts doubt on the quality. Additionally, the authors state “estimators implemented in offline rl ope were able to accurately rank the performance of policies against the ground truth performance.” Some of the ranking statistics in Table 6 are fairly low (i.e., 0.3-0.5); I’m not sure the preceding statement is entirely true given this result. The lack of a direct comparison with Scope-RL on continuous action spaces, due to the differing approaches, makes it difficult to assess the practical value of the proposed method. The reliance on ranking metrics, while common in OPE, does not provide a clear picture of the estimator's accuracy in absolute terms.

The paper does not seem entirely complete. There are some typos and presentation issues. One of the most glaring problems is the empty caption in Figure 2. This error makes it seem like the paper was hastily written. Other typos:
- Line 427 “integrogate” should be interrogate
- Line 462: “effected” → “affected”

### Questions
What metrics are novel to this paper? Can the authors please state this clearly?
Why can they only compare the ranking of continuous actions? How do these implementations differ? Why do the spearman ranking correlation coefficients seem low in some instances?


Other suggestions:

The experiments in Section 5 reminded me of recent work on probabilistic policy ranking, which could potentially be incorporated into future releases:

Da, Longchao, et al. "Probabilistic Offline Policy Ranking with Approximate Bayesian Computation." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 38. No. 18. 2024.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors introduce a Python package for offline policy evaluation (OPE)
and discuss a number of improvements it offers such as handling uneven trajectory length, including novel metrics, providing effective API.
They also report experimental results for reproducibility check and some performance statistics.

### Strengths
It provides an extensive explanation of a new software package for OPE.

### Weaknesses
The paper is incomplete, poorly organized and inconclusive.
It is not ready for publication.

It is incomplete because no research question/problem is clearly raised or addressed. Also, the caption of Figure 2 is incomplete.

There is no conclusion to be made since there is no research question/problem in the first place. Also, the experimental results are not enough to draw any clear conclusion as to whether `offline_rl_ope` is useful.

The authors just put some new features and experimental results of the package in the paper without explicitly indicating any intention or explanation.

Overall, it is more of a technical paper describing a software package, not a research paper.

### Questions
NA

### Soundness
1

### Presentation
1

### Contribution
1
