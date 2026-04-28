# Optimal Transport for Time Series Imputation

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 5

## Abstract
Missing data imputation through distribution alignment has demonstrated advantages for non-temporal datasets but exhibits suboptimal performance in time-series applications. The primary obstacle is crafting a discrepancy measure that simultaneously (1) $\textit{captures temporal pattern}$—accounting for patterns such as periodicities and temporal dependencies inherent in time-series—and (2) $\textit{accommodates non-stationarity}$, ensuring robustness amidst multiple coexisting temporal patterns. In response to these challenges, we introduce the Proximal Spectrum Wasserstein (PSW) discrepancy based on the stochastic optimal transport framework, which incorporates a pairwise spectral distance to encapsulate temporal patterns, coupled with selective matching regularization to accommodate non-stationarity. Building upon PSW, we develop the PSW for Imputation (PSW-I) framework, which iteratively refines imputation results by minimizing the PSW discrepancy. Extensive experiments demonstrate that PSW-I effectively addresses these challenges and significantly outperforms prevailing time-series imputation methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Providing methods for time series imputations while respecting the temporal dependence.

### Strengths
- Very good empirical investigation.

- Clear presentation.

### Weaknesses
NA

### Questions
- What if the time series components are observed at different temporal frequencies (say days vs. hours, or hours vs. mins)?

### Soundness
3

### Presentation
4

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
The paper proposes a time series imputation method based on optimal transport. The key idea is the combination of a frequency-based Wassertein discrepancy  and selective matching regularization. Theoretical justification is also provided. The experimental results show the imputation accuracy outperforms many sota methods.

### Strengths
1. An interesting and well-motivated design of the spectral-enhanced Wasserstein distance (WD)
2. A theoretical justified design of proximal spectral WD to account for non-stationarity.
3. seemingly excellent performance in real-world benchmark datasets.

### Weaknesses
1. The biggest issue from my end is the lack of standard deviation. From Table 1, the error of the proposed method seems really good, but i am not informed if these results are averaged over multiple train/test runs or just one run. To avoid cherry picking, the authors are encouraged to highlight how these numbers were obtained, what the training/test splits were, and what hyperparameter selection/cross-validation process was involved, etc.  Similar expectations apply to table 3 and 4.

2. Lack of convergence discussion/analysis. From Fig. 3 and Section 3.4, the imputation procedure seems to repeatedly sample patches from the time series, compute PSW, and use the gradient of the PSW to update the imputation. There seems a lack of convergence guarantees or discussions about this procedure. Can authors provide at least some discussion on this?

3. Data noise issue. Real time series data often includes noises. That means, just computing the distance after DFT in lin154 might be affected by data noises. Have the authors consider any methods or trade-offs, such as low-pass filters, in your SWD definition, to improve the robustness and/or counteract the noise effect?

### Questions
see above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes an optimal transport (OT) based time-series imputation method. The authors claim that naive application of OT does not work for time-series data. The proposed method consider applying OT in the frequency domain of the original data, called pairwise spectrum distance (PSD). Further, to deal with multiple modes, proximal spectral Wasserstein (PSW) distance is also proposed, in which mass constraint is removed to make transportation more flexible.

### Strengths
- Using OT to impute time-series data is an interesting approach.

- Empirical evaluation shows high performance.

### Weaknesses
 - Some technical justification is vague. Clearer descriptions would be desired.

- Introduction is a bit too abstract about the proposed method. It describes what problem is solved in the paper, but does not describe the basic technical idea how it is achieved.

- In 'Contributions', the authors mention that PSW-I eliminates the need for masking, but PSW-I seems to use masking (eg as shown in Fig3). What does this description mean?

- What does Lemma 3.2 indicate? How do you know 'deviates more from the typical elements of \beta'? Further, how do you know the PSW discrepancy avoid the problem indicated by this lemma? In Theorem C.2, the perturbation in PSW discrepancy is shown. Is it possible to compare this with Lemma 3.2? Even if it is possible, what does it mean? Is it clear how large (or small) perturbation caused by outliers ultimately affect the final imputation?

- Although D_KL is used in (2), T 1_m and T^T 1_n is not a probability distribution (because the normalization (sum equals 1) constraint is removed). How are they normalized?

- What is the definition of the 'DFT matrix' in the gradient? How does the gradient of (2) become \Delta_alpha_i P and \Delta_beta_j P? The second term in (2) disappear? The optimality condition wrt T is considered in this gradient calculation?  

- After (1), D is squared distance, while in definition 3.1 D is distance without square. Which is correct?

Minor issues:

- In the end of p3: Fig. 4 should be Fig 1? In Fig 1(a), the left is W^(F)?

- The first word of Sec3.2: 'time-series' -> 'Time-series'

### Questions
- In 'Contributions', the authors mention that PSW-I eliminates the need for masking, but PSW-I seems to use masking (eg as shown in Fig3). What does this description mean?

- What does Lemma 3.2 indicate? How do you know 'deviates more from the typical elements of \beta'? Further, how do you know the PSW discrepancy avoid the problem indicated by this lemma? In Theorem C.2, the perturbation in PSW discrepancy is shown. Is it possible to compare this with Lemma 3.2? Even if it is possible, what does it mean? Is it clear how large (or small) perturbation caused by outliers ultimately affect the final imputation?

- Although D_KL is used in (2), T 1_m and T^T 1_n is not a probability distribution (because the normalization (sum equals 1) constraint is removed). How are they normalized?

- What is the definition of the 'DFT matrix' in the gradient? How does the gradient of (2) become \Delta_alpha_i P and \Delta_beta_j P? The second term in (2) disappear? The optimality condition wrt T is considered in this gradient calculation?  

- After (1), D is squared distance, while in definition 3.1 D is distance without square. Which is correct?

Minor issues:

- In the end of p3: Fig. 4 should be Fig 1? In Fig 1(a), the left is W^(F)?

- The first word of Sec3.2: 'time-series' -> 'Time-series'

### Soundness
2

### Presentation
2

### Contribution
2
