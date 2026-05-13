# On Temperature Scaling and Conformal Prediction of Deep Classifiers

- Decision: Reject
- Scores: 8, 3, 6

## Abstract
In many classification applications, the prediction of a deep neural network (DNN) based classifier needs to be accompanied by some confidence indication. Two popular approaches for that aim are: 1) {\em Calibration}: modifies the classifier's softmax values such that the maximal value better estimates the correctness probability; and 2) {\em Conformal Prediction} (CP): produces a prediction set of candidate labels that contains the true label with a user-specified probability, guaranteeing marginal coverage, rather than, e.g., per class coverage.  In practice, both types of indications are desirable, yet, so far the interplay between them has not been investigated. We start this paper with an extensive empirical study of the effect of the popular {\em Temperature Scaling} (TS) calibration on prominent CP methods and reveal that while it improves the class-conditional coverage of adaptive CP methods, surprisingly, it negatively affects their prediction set sizes. Subsequently, we explore the effect of TS beyond its calibration application and offer simple guidelines for practitioners to trade prediction set size and conditional coverage of adaptive CP methods while effectively combining them with calibration. Finally, we present a theoretical analysis of the effect of TS on the prediction set sizes, revealing several mathematical properties of the procedure, according to which we provide reasoning for this unintuitive phenomenon.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper provides a very detailed theoretical and empirical study of the effect of temperature scaling on prediction set sizes and conditional coverage in conformal prediction. It finds that temperature scaling can (sometimes drastically) increase set sizes for common classification tasks. It explains this phenomenon theoretically and provides guidelines to practitioners about how to set the parameter moving forward.

### Strengths
The paper is strong and I recommend acceptance.

I was impressed and surprised by the insights in this paper. Temperature scaling has a huge effect, the experiments bear this out, and the theory provides some explanation as to why, and might be useful to others in the field. (Specifically, the theory about how set size is affected by temperature is fairly general-purpose.)

* The empirical experiments are painstakingly detailed and very scientific.
* The theory is useful and correct.

### Weaknesses
 * The theorems are somewhat weak, and of limited practical value in terms of being applied directly. They seem to be useful mostly for the purpose of post-hoc explanation of why this phenomenon happens.


### Questions
I have not much to ask or say. The paper was clear!
A typo/English language check would improve it before the next round.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors investigate the interplay between conformal prediction and calibration. Firstly, the paper empirically shows that while temperature scaling improves the class-conditional coverage of adaptive CP methods. Then, the authors establish a mathematical theory that explains this phenomenon. Finally, the paper offers a guideline to effectively combine adaptive CP with calibration.

### Strengths
1. The work is well-writing. Basically, the paper is written in a good manner and I believe readers can easily touch the core idea.  

2. This paper provides a theoretical analysis to show how temperature values influence the properties of prediction sets. With the theoretical results, researchers can understand why temperature scaling can affect the conformal prediction.

3. The authors provide empirical validation of their theoretical framework.

### Weaknesses
1. The paper presents an inconsistency in its mathematical derivations. In Eq. (3), the analysis is mainly based on the relationship between $\sum_{i=1}^M\pi_i-\sum_{i=1}^M\pi_{T,i}\quad\text{and}\quad{q}-q_T$ (omit \hat for \pi and q due to the tex support),
which represents the difference of accumulated probability and threshold value before and after applying a temperature. Later, in Eq. (5), the problem above is translated to investigate the relationship between 
$$\sum_{i=1}^M\exp(z_i)-\sum_{i=1}^M\exp(z_i/T)\quad\text{and}\quad\sum_{i=1}^M\exp(z_i^q)-\sum_{i=1}^M\exp(z_i^q/T).$$However, based on the definition on $z^q$, we know that if $M$ is not the true label of $z^q$, then $\sum_{i=1}^M\exp(z_i^q/T)\neq\hat{q}_T$. Therefore, it's unclear how the problem in Eq. (3) can be equivalent to the analysis in Eq. (5). The analysis needs to explicitly address the difference between using the true label's rank and the predicted label's rank when calculating the cumulative probabilities, as this difference is not negligible and impacts the validity of the subsequent analysis.

2. The assumptions in Theorem 4.4 appear to be unreasonable. Theorem 4.4 in the paper states that if $\Delta z>b(T)$, then rising $z_1$ leads to an increase in the set size. However, the assumption that '$\Delta z$ is preserved as $z_1$ increases' (line 458) is not natural for me because counterexamples exist where $\Delta z$ increases as $z_1$ increases. Furthermore, even if we accept the condition that $\Delta z$ remains constant, the paper's claim that '$z^q$ has a larger dominant entry than typical $z$' lacks proper justification. The paper needs to provide a more rigorous argument for why the quantile sample $z^q$ would consistently have a larger $\Delta z$ than a typical sample, considering that the quantile is based on the score and not directly on the logit differences.

3. The theoretical bounds and empirical results show inconsistency. The paper reports an empirical critical temperature of $T^{*}=1.524$. However, this value falls between the theoretical temperature ranges $(0,0.813)$ and $(1.25,4.81)$, suggesting a gap between theory and practice. This inconsistency challenges the paper's claim that 'the bounds in Theorem 4.4 do not require unreasonable values of $\Delta z$ and T' (line 463). Moreover, it indicates that using the median of $\Delta z$ to estimate $T_{critical}$ may not be a reliable approach. The paper should clarify how the critical temperature is derived from the theoretical bounds and why the empirical value does not align with the predicted ranges. The use of the median $\Delta z$ also needs further justification, as it may not be representative of the samples that determine the critical temperature.
    
4. The proposed approach of using $T_{critical}$ to enhance conditional coverage (as proposed in Section 5) has limitations. As discussed in Weaknesses[3], the theorem may fail to provide accurate estimation of $T_{critical}$. Even though an accurate estimation can be achieved, simply applying $T_{critical}$ falls short of achieving group-wise coverage that Mondrian conformal prediction provides. Furthermore, the paper does not present empirical evidence demonstrating how their proposed guideline enhances conformal prediction performance. Overall, these limitations restrict the practical applicability of the theoretical results. The paper needs to provide a more detailed comparison with Mondrian CP, particularly in scenarios where group-wise coverage is a priority, and should include empirical results that demonstrate the effectiveness of the proposed guideline in practical settings.


**Minor Comments:**
1. The paper's analysis is limited to Temperature Scaling, while leaving out other important calibration methods such as histogram binning.
2. The mathematical proofs lack clarity. For example, in proof of Theorem 4.1, the first equation (line 750-755) is stated without proper mathematical justification.
3. typo in Section 5: "guidelinse" should be "guidelines".

### Questions
1. While Theorem 4.4 provides valuable theoretical insights, it is hard to understand how to use the theoretical results for estimating $T_{critical}$. I would greatly appreciate it if the authors could provide an explicit expression for computing $\hat{T}_{critical}$.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper delves into the impact of Temperature Scaling (TS) on conformal prediction methods. 
Traditionally, researchers have applied TS before conducting conformal prediction on the resulting classifiers. 
The paper argues that while it enhances group coverage, it negatively affects set size. 
I find this paper offers valuable experiments and intriguing insights into the interplay between conformal prediction and temperature scaling, and I recommend an acceptance. My hesitation to give a higher score stems from (a) the paper's inherently limited scope to classification tasks, as regression tasks do not typically encounter this issue; (b) it is somehow intuitive that TS might not be the best choice for the set size, which is not particularly surprising.

### Strengths
1. The paper focuses on an interesting question: the influence of temperature scaling on conformal prediction outcomes, concerning group coverage and band length.
2. Empirical evidence is provided to suggest that TS can detrimentally harm the set size of conformal prediction measures such as APS and RAPS, while simultaneously improving group coverage.
3. The authors demonstrate that TS facilitates a trade-off between set size and group coverage.
4. Theoretical insights into the empirical findings are offered, along with practical guidelines for practitioners.

### Weaknesses
have few major concerns with this paper. As previously mentioned, my decision not to assign a higher score is based on:
1. The limited scope of the paper to classification tasks, as regression tasks do not typically present this issue.
2. The somewhat expected nature of the finding that TS might impact set size negatively. Specifically, since Temperature Scaling (TS) is a post-hoc calibration method and not an end-to-end training approach, it is not surprising that it might not be optimal for conformal prediction (CP) set size. Intuitively, if a neural network consistently predicts the correct label with high confidence (e.g., 95% accuracy), the ideal confidence band for a 5% error rate would be a set of size 1. In this scenario, an infinite temperature parameter (or very small temperature) would be optimal, whereas TS would likely not achieve this. This suggests that TS might not be the best choice for minimizing set size in CP.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3
