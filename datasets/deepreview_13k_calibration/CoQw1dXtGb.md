# SPDIM: Source-Free Unsupervised Conditional and Label Shift Adaptation in EEG

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 5, 6, 6

## Abstract
The non-stationary nature of electroencephalography (EEG) introduces distribution shifts across domains (e.g., days and subjects), posing a significant challenge to EEG-based neurotechnology generalization.
Without labeled calibration data for target domains, the problem is a source-free unsupervised domain adaptation (SFUDA) problem.
For scenarios with constant label distribution, Riemannian geometry-aware statistical alignment frameworks on the symmetric positive definite (SPD) manifold are considered state-of-the-art.
However, many practical scenarios, including EEG-based sleep staging, exhibit label shifts.
Here, we propose a geometric deep learning framework for SFUDA problems under specific distribution shifts, including label shifts.
We introduce a novel, realistic generative model and show that prior Riemannian statistical alignment methods on the SPD manifold can compensate for specific marginal and conditional distribution shifts but hurt generalization under label shifts.
As a remedy, we propose a parameter-efficient manifold optimization strategy termed SPDIM.
SPDIM uses the information maximization principle to learn a single SPD-manifold-constrained parameter per target domain.
In simulations, we demonstrate that SPDIM can compensate for the shifts under our generative model.
Moreover, using public EEG-based brain-computer interface and sleep staging datasets, we show that SPDIM outperforms prior approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This study focuses on the realistic issue of label shifts in EEG across subjects and/or sessions (relative class proportions in target domains when source domains are class-balanced). Using theoretical analysis, it extends the SotA statistical alignment framework for handling distribution shifts in EEG to also include label shifts. The proposed SPDIM includes a domain-specific bias parameter estimated from unlabeled target data that reduces over-corrections done by the current SotA framework. Results on synthetic data and real-world EEGs demonstrate the value of SPDIM over baselines.

### Strengths
- Rigorous and clear presentation of technical details and full analytic workflow.
- This work is a great example of theory-guided methods design for EEG.
- Impactful choice of research problem - performance of EEG models under label shifts will remain a ubiquitous concern, both clinically and in the BCI space.

### Weaknesses
 - (line 166) Q: Is the assumption of number of latent brain sources = number of observed scalp channels = P necessary or realistic? This assumption, while common in some data-driven models like ICA, may not hold in all EEG scenarios. Specifically, the number of underlying neural sources contributing to the observed scalp signals is often considered to be less than the number of sensors. This over-completeness can lead to issues with identifiability and interpretability of the latent space. The method should clarify how it addresses this potential mismatch and whether the performance is sensitive to this assumption. 
- No discussion of study limitations and/or future directions. The absence of a discussion on limitations makes it difficult to assess the robustness of the proposed method. For example, the method's reliance on the estimation of a domain-specific bias parameter could be sensitive to noise and outliers in the unlabeled target data, potentially leading to incorrect shifts. Furthermore, the paper should discuss the computational complexity of the proposed method, especially in comparison to existing alignment techniques, and whether it scales well to large datasets.

### Questions
- Q: Does this framework treat one subject or one EEG recording as one source/target domain containing both/multiple class labels?
- Q: How does this framework for "latent space alignment" compare/relate to non-reimannian approaches for SFUDA for EEGs/multivariate timeseries? See [1] for a recent example. The "test-time adaptation" (Section 3.2) studies listed in [2] might also be relevant.
- Q: What factors other than dataset size and label shifts could account for the high variability/stdev in Table 1? In most cases, handling label shift (either with RCT or SPDIM) decreases variability compared to "w/o", but its still seems high.
- Minor comments: 1) pixel resolution of Figure 1 can be improved, 2) typo in citations at line 218 and 236., 3) line 443 remove "standard-deviation in brackets"
- The anonymous code link is broken?

[1] He, Huan, et al. "Domain adaptation for time series under feature and label shifts." International Conference on Machine Learning. PMLR, 2023.

[2] Garg, Saurabh, et al. "Rlsbench: Domain adaptation under relaxed label shift." International Conference on Machine Learning. PMLR, 2023.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The study addresses a source-free unsupervised domain adaptation problem and proposes SPDIM, a framework based on the SPD manifold. 
SPDIM compensates for label shifts using proposed generative models, which prior Riemannian statistical alignment methods do not effectively handle. 
Additionally, SPDIM applies the information maximization principle to learn domain-specific parameters. 
Simulation experiments demonstrate its superiority under various levels of label shift, and empirical analysis on real EEG datasets shows that it outperforms previous approaches.

### Strengths
- The motivation is clear and easy to follow. SPDIM aims to address adaptation under label shifts, a common challenge in real-world EEG datasets. 
  Theoretical analysis further explains the causes of deviations under label shifts.

- Simulation experiments qualitatively validate the benefits of SPDIM in the presence of label shifts. 
   Cross-subject and cross-session experiments on motor and sleep-staging EEG datasets illustrate its superiority over existing alignment methods based on the SPD manifold.

### Weaknesses
 - Some notations in equations seem confusing. For example, the index $j$ under $\sum$ may need to be $i$ in Eq. (2). The invertible mapping $upper$ is defined on $S$, but $upper^{-1}$ appears in Eq.(10). 
Additionally, $j_i$ and $j$ use the same letter but with different meanings, which could lead to ambiguity. The notation $Q$ in Eq.(15) seems to appear without prior introduction. 

- Some aspects of the method require further clarification. As mentioned in Line 249, the right-hand side of Eq. (15) is claimed to contain only domain-invariant terms. However, from my perspective, $C_i$ depends on the domain-specific 
matrix $A_{j}$, as suggested by Eq. (13). According to Proposition 1, $ \bar{C} _ {j(i)} $ converges to $I_P$. These indicate that $Q$ is linked to $A_{j}$, which may not be domain-invariant. Additionally, the relationship between the information maximization approach introduced in Section 3.3 and SPDIM (bias) / SPDIM (geodesic) is unclear. 

- To better demonstrate SPDIM’s effectiveness, it would be beneficial to compare it with additional statistical alignment methods beyond those based on the SPD manifold. This would provide a more comprehensive evaluation against existing approaches.

### Questions
- Is the domain-specific formard model $A_{j}$ learned from features of a specific domain, or is it predefined? 
- How are domain specific parameters $\Phi_{j(i)}$ and the geodesic step-size parameters $\varphi_{j(i)}$ learned according to the proposed information maximization principle described in Section 3.3?
- Is there any relationship between the adaptation performance and predefined hyperparameters, such as the rank of $A$ and the number of domains within $\mathcal{D}_{s}$?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The "SPDIM" paper introduces a novel geometric deep learning framework aimed at enhancing source-free unsupervised domain adaptation (SFUDA) for EEG data under both conditional and label shifts. By leveraging the symmetric positive definite (SPD) manifold and employing a parameter-efficient manifold optimization strategy, the proposed method, SPDIM, addresses significant generalization challenges in EEG data processing, especially where traditional Riemannian geometry methods fall short due to label shifts. SPDIM shows promising improvements across multiple EEG-based applications, including brain-computer interface tasks and sleep staging, demonstrating its efficacy over prior alignment frameworks

### Strengths
1.	The introduction of an SPD-manifold-constrained bias parameter is an advancement for tackling SFUDA in EEG.
2.	The framework has been applied effectively across different tasks, showcasing broad applicability.
3.	SPDIM outperforms conventional methods, showing its resilience under varying label distributions.

### Weaknesses
1.	The motivation behind addressing label shifts and domain gaps with SPDIM is somewhat implicit, without clearly laying out why these challenges necessitate the proposed framework. Specifically, the paper does not adequately explain why existing methods are insufficient to handle label shifts in EEG data, and how the proposed SPD manifold approach offers a more principled solution. The connection between the geometric properties of the SPD manifold and the specific challenges posed by label shifts is not clearly established.
2.	The paper contains an extensive number of equations and mathematical formulations in the main text, which can make the methodology difficult to follow. The density of equations, particularly in sections 3 and 4, overwhelms the reader, making it challenging to grasp the core concepts and the practical implications of the proposed method. The lack of intuitive explanations alongside the mathematical derivations further exacerbates this issue.
3.	Although the paper compares SPDIM with several baselines, a broader set of comparisons, especially with newer unsupervised or semi-supervised EEG methods, could provide further insights into SPDIM’s performance and robustness. The current comparisons do not fully explore the landscape of recent advancements in unsupervised domain adaptation for EEG, potentially overlooking relevant benchmarks that could highlight the strengths and weaknesses of SPDIM more clearly.
4.	While SPDIM improves accuracy under domain shifts, the model’s interpretability remains limited. The paper does not discuss how the learned parameters on the SPD manifold can be interpreted in the context of EEG signals, which is crucial for understanding the underlying neural mechanisms. The lack of interpretability limits the practical utility of the model in clinical settings where understanding the model's decision-making process is essential.

### Questions
Plz go and check weaknesses

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces SPDIM, a framework for source-free unsupervised domain adaptation (SFUDA) in EEG-based applications, which are challenged by distribution shifts across sessions or subjects. SPDIM leverages the geometry of symmetric positive definite (SPD) matrices to handle conditional and label shifts, aligning EEG data across domains without requiring labeled target data. The approach introduces a domain-specific SPD-manifold bias to counteract label shifts, and optimizes alignment using an information maximization principle, which prevents mode collapse by ensuring class diversity and prediction confidence. Experimental results on EEG datasets for motor imagery and sleep staging show that SPDIM outperforms baseline SFUDA methods, demonstrating robust generalization across domains even under significant label distribution changes.

### Strengths
- The paper is well written.
- The modelisation is original and insightful. I really enjoyed reading the modelisation part of the paper.
- The developed methods are tested on 3 setups: synthetic data, Motor-Imagery and Sleep-Staging.

### Weaknesses
 - At the time of reviewing the paper, the code is not available: “The repository is not found.” is returned by anonymous.4open.science
- A modelisation per domain of EEG data was proposed in [1] which could be worth citing in your introduction. Indeed, the authors mention there exists a linear mapping per domain to get domain-invariant tangent vectors (and without assumption on the mixing matrix (9)).
- The experiment on motor imagery is limited since you artificialy unbalance the labels. Finding real world data which are naturally unbalanced would add value to the paper.
- The mean accuracy of the 2 proposed methods are within the standard deviation of the recenter for the motor imagery application.
- On the sleep-staging setup, you do not compare with adaptation methods expect recenter. You should compare at least to STMA or TMA (Spatio-Temporal Monge Alignment) which is presented in [2].
- The presentation of the results is not homogeneous between the two applications. In particular, it is strange to me to call an “ablation study” a comparison with other methods.

### Questions
- You mention there are conditional shifts in EEG data (p_j(x|y) changes between domains). Can you relate this with your modelization?
- What is D in the Remark 1?
- Does the Propostion 2 still hold when M_j does not tend to the infinite?
- You train your model on the target domain (in an unsupervised manner). Did you train/test split the target domain?
- How easy to train are the methods you use? e.g. USleep is rarely used as a baseline in other sleep staging papers. Providing infos the lr scheduler, batch size, … would be valuable.
- I am surprised that the spatial covariance is enough to classify sleep stages. Usually, the temporal information is used but not the spatial one. Can you comment on this?

A few typos:
- D and P are both used for the data dimension
- There are “?” in lines 218 and 236.
- Q and U are both used for domain-invariant par of the mixing matrix.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Due to the difficulty of the SPD method in handling label shift issues, this paper proposes a geometric deep learning framework, SPDIM, for SFUDA problems under specific distribution shifts, including label shifts. SPDIM employs the information maximization principle to learn a single SPD-manifold-constrained parameter per target domain. Using public EEG-based brain-computer interface and sleep staging datasets, we demonstrate that SPDIM outperforms prior approaches.

### Strengths
This paper investigates the label shift problem in SFUDA, with a very strong motivation and significant practical relevance.

The method proposed in this paper has a certain theoretical foundation, and the derivation of some propositions may provide inspiration for solving the label shift problem.

### Weaknesses
Although this paper focuses on EEG SFUDA problems, the proposed method does not appear to be specifically designed for EEG but seems to be a more general approach applicable to any label shift scenario. From the perspective of EEG research, the method lacks specificity for EEG data, while from the perspective of SFUDA research, the paper only validates the method on EEG data, lacking more reliable experimental verification.

The experiments are not solid. The paper does not clearly present the experimental setup, such as the hyperparameters of the models, the partitioning method of the source and target domains, etc. Additionally, the EEG decoding methods compared in the experiments are not sufficiently strong. The paper does not compare some classic EEG decoding models, such as EEGNet and EEG Conformer, nor does it compare some sleep staging models, such as DeepSleepNet. The domain adaptation methods only compare Information Maximization (IM), and such insufficient comparisons are not enough to prove the superiority of the proposed method.

The writing of this paper still has some room for improvement. For example: Figure 1 has low resolution, and the four sub-figures in Figure 2 lack sub-titles.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2
