# End-to-End Conformal Prediction for Trajectory Optimization

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 6, 8

## Abstract
Conformal Prediction (CP) is a powerful tool to construct uncertainty sets with coverage guarantees, which has fueled its extensive adoption in generating prediction regions for decision-making tasks, e.g., Trajectory Optimization (TO) in uncertain environments. However, existing methods predominantly employ a sequential scheme, where decisions rely unidirectionally on the prediction regions, and consequently the information from the decision-making end fails to be transmitted back to instruct the CP end. In this paper, we propose a novel End-to-End CP (E2E-CP) framework for shrinking-horizon TO with a joint risk constraint over the entire mission time. Specifically, a CP-based posterior risk calculation method is developed by fully leveraging the realized trajectories to adjust the posterior allowable risk, which is then allocated to future times to update prediction regions. In this way, the information in the realized trajectories is continuously fed back to the CP end, enabling attractive end-to-end adjustments of the prediction regions and a provable online improvement in trajectory performance. Furthermore, we theoretically prove that such end-to-end adjustments consistently maintain the coverage guarantees of the prediction regions, thereby ensuring provable safety. Additionally, we develop a decision-focused iterative risk allocation algorithm with theoretical convergence analysis for allocating the posterior allowable risk which closely aligns with E2E-CP. The effectiveness and superiority of the proposed method are demonstrated through benchmark experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors proposed an E2E-CP framework for shrinking-horizon TO in uncertain environments and the collision risk over the total mission time is always constrained. The proposed method leverages the information of past decisions to adjust prediction regions in an end-to-end fashion. The experiment results demonstrate the effectiveness of the proposed model for trajectory prediction task.

### Strengths
1.The paper provides detailed theoretical proof for the proposed method.
2. This paper compares the model performance of sequential CP, average risk allocation setting, and iterative risk allocation setting.

### Weaknesses
1.The prediction regions are expected to cover the ground truth trajectory and narrow. Otherwise, overlarge prediction regions would also achieve a high collision avoidance rate. The authors should provide more details about how narrow the prediction regions are.

2. The authors should demonstrate the model performance by implementing more state-of-the-art models but not only the models proposed about 20 years ago.



### Questions
Please see the above limitations and address the questions. In addition to the limitations, another question is:

Based on Eqs. 9, 13, and 17, both the upper bound of the posterior violation probability and the allocable risk at specific time step are fixed for the average risk allocation setting, as the upper bound of the posterior violation probability is calculated based on the calibration data D_{cal}^{2}. This violates the real-world situation where the real-world data and calibration data follow different distribution. However, experiment result in Table 1 shows that this average risk allocation method still achieves 89.1% collision avoidance rate. Are there any data distribution shifts in the testing data? If not, what’s the performance of the proposed method under distribution shift?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel trajectory optimization algorithm grounded in conformal prediction, which dynamically adjusts posterior risk based on observed trajectories. Benchmark experiments highlight the algorithm’s effectiveness, showcasing its superior performance compared to existing methods.

### Strengths
1. The algorithm proposed in the paper is novel, supported by rigorous theorems and proofs that strengthen its theoretical foundation.
2. The presentation is clear and well-structured.

### Weaknesses
1. I have concerns regarding the assumptions made in this paper, particularly the strong independence assumptions on obstacle trajectories, which form the basis of the proposed algorithm. In Section 3.1, the authors assume the independence between D and system (1) (lines 134-135) and further assume that the real joint obstacle trajectory Y and the N available joint obstacle trajectories Y^(i) are independent and identically distributed (i.i.d.) (lines 143-145). However, in real-world applications such as autonomous driving, obstacle trajectories—specifically those of other vehicles on the road—are highly interdependent, as each vehicle’s decisions are influenced by the behaviors of surrounding vehicles. The interdependence between obstacle trajectories is a key factor contributing to the complexity of real-world problems. Assuming independence significantly simplifies the problem but may limit the algorithm's applicability in practical, interdependent scenarios. It would be beneficial for the authors to provide a justification for these independence assumptions and to identify any real-world applications where obstacle trajectories can be reasonably assumed to be independent.

2. Another concern is the limited performance improvement observed with the proposed algorithm. In Table 1, the collision avoidance rate shows only a marginal increase, raising questions about the practical impact of the algorithm. Furthermore, in Table 3 (Appendix C.2), the collision avoidance rate actually decreases when using the proposed algorithm, suggesting potential issues with its robustness. Additionally, the benchmark experiments include only two robotic systems, which may not provide sufficient diversity to fully evaluate the algorithm's effectiveness across different scenarios.

3. Additionally, this paper’s focus on trajectory optimization is largely unrelated to machine learning or deep learning. Given the emphasis on trajectory optimization techniques rather than learning-based methods, it would be more appropriately submitted to robotics-focused publication venues rather than conferences dedicated to deep learning.

4. Minor typo: On line 190, "level beta" should be corrected to "level alpha."

### Questions
1. As noted in the weaknesses section, it would be valuable for the authors to provide a rationale for these independence assumptions and to highlight any real-world applications in which obstacle trajectories can reasonably be assumed to be independent.
2. The paper would benefit from additional benchmark examples beyond the two robotic systems currently evaluated. Expanding the benchmarks would provide a more comprehensive assessment of the algorithm's effectiveness across diverse scenarios.
3. It would be helpful if the authors could clarify why a paper focused on trajectory optimization, rather than on learning-based approaches, is suitable for a deep learning conference.

### Soundness
3

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
5

### Summary
In this paper, the authors proposed a conformal prediction based posterior risk calculation method to obtain the posterior probability of collision conditional on realized trajectories. This method leverages the realized trajectories to adjust the posterior allowable risk in an online setting. The experiment results demonstrate the efficacy of the proposed method.

### Strengths
1) The paper is well organized and easy to follow.
2) This paper utilizes the conformal prediction-based method to achieve the end-to-end adjustments of the prediction region, improving the limitation of conformal prediction.

### Weaknesses
1) The prediction regions should be narrow and cover the ground truth data. However, large prediction regions would also achieve a high collision avoidance rate but not meaningful in real-world situations. The authors should provide more details about the prediction region. 
2) Proving the effectiveness of the proposed method is very important. However, the authors merely apply the proposed method on two trajectory prediction models which were proposed in 2001 and 2006, respectively. The authors should provide experiment results on more state-of-the-art models.

### Questions
1) Performance of the proposed method on more state-of-the-art methods.
2) Performance of the proposed method under data distribution shift.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the problem of online trajectory optimization in an uncertain environment. The proposed algorithm includes a chance-constrained optimization problem that applies conformal prediction (CP) in two ways. First, it uses forward-looking CP to predict a priori confidence intervals for future obstacle positions, which are used for planning. Second, it uses backward-looking CP to compute the posterior confidence intervals of past obstacle positions to estimate how much of the risk budget was actually "used up" compared to the planned amount of risk. The risk budget freed up by this backward-looking assessment is applied to future timesteps, allowing less conservative behavior. The experiments are simple, presenting well-chosen ablations rather than a comprehensive suite of baseline methods, but I found them to be compelling.

### Strengths
I really enjoyed reading this paper. The core of the paper is a really interesting idea (understand how much risk you have previously incurred, so as to better decide how much risk to take on in future), and the authors rigorously build a rigorous framework around this idea to design an intuitive trajectory optimization framework.

The paper is clearly written throughout, and although I did not check all proofs, the ones I did check were fairly clear. It is possible that there is some nuance of conformal prediction that I am missing, but overall the approach seems sound.

### Weaknesses
The paper is missing some key implementation details (notably: how was the optimization problem solved/what solver was used?). The paper is also missing a discussion of limitations. If there is not space in the main paper, these could be included in the appendix, but I would like to see limitations at least mentioned in the main text.

### Questions
1. In section 3.2, is the prediction also conditioned on the history of obstacle positions $Y_{0:t}$ or only on the most recent observation $Y_t$? Your notation implies the latter, but I'd imagine that the former would yield more accurate predictions.
2. Line 90: "level $\beta$ quantile" -- do you mean "level $1-\alpha$ quantile"? If not, what is $\beta$?
3. The empirical results suggest that the proposed method (E2E-CP with IRA) is still conservative. What do you think are the reasons for this, and how would you go about reducing this conservatism?

### Soundness
4

### Presentation
4

### Contribution
4
