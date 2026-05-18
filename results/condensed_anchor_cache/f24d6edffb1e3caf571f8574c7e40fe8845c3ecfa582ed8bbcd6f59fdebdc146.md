- Decision: Reject
- Scores: 5, 5, 3, 5

## Merged Review

### Summary
This paper addresses the problem of calibrating model confidence in source-free domain adaptation (SFDA), where only unlabeled target-domain data is available. The authors propose Source-Free Confidence Calibration (SFCC), a method that first refines pseudo-labels via a clustering-based strategy (GEPL) and then applies temperature scaling using the refined pseudo-labels. Experiments on VisDA, DomainNet, and Office-Home are conducted with three SFDA methods (SHOT, AaD, DCPL). The authors claim that SFCC achieves results comparable to or better than existing calibration methods that use labeled source data.

### Strengths
- The calibration problem in SFDA is important for model robustness and generalization in real-world scenarios where source data is inaccessible due to privacy or storage concerns. (R1, R2, R3, R4)
- The paper is structured clearly with step-by-step explanations (R1). However, other reviewers found the presentation hard to follow (see Weaknesses).
- Extensive testing across multiple datasets (VisDA, DomainNet, Office-Home) and three SFDA baselines validates the method (R1). (Note: some argue not enough baselines – see Weaknesses.)
- It is good that code implementation is provided (R2).
- The proposed method is effective empirically (R4).

### Weaknesses
- **Limited technical novelty.** The two main components of SFCC – the GEPL algorithm (used in SHOT and other SFDA works) and temperature scaling – are existing techniques; no new calibration or pseudo-labeling method is introduced (R1, R2, R4). One reviewer specifically notes that “it seems the technical novelty of this paper is very limited due to the use of many existing techniques without proposing a new one” (R2). Another notes that “simply transferring pseudo-labels from semi-supervised learning to calibration lacks novelty” and that the method does not filter out incorrect pseudo-labels based on confidence (R4).
- **Unclear necessity of the setting.** One reviewer questions whether source-free calibration is needed at all, since calibration relies on only a single parameter T: “In real practice, we can try to label some data manually and achieve calibration. For example, for each class, we can simply label one or three samples, which I think will not bring much more cost.” The authors are asked to discuss the differences and applications between this setting and TransCal’s source-data-based calibration (R4).
- **Weak theoretical/empirical justification for core assumptions.** The central claim that noisy pseudo-labels can reliably estimate true bin-wise accuracy (Equation 6) is not convincingly supported (R1, R2, R3). Specifically:
    - The assumption that “two versions of A_{i,1} are equal by definition” (lines 191-208) is confusing and lacks rigor; it is unclear which definition justifies this (R2). The discussion from line 198 to line 215 is “only based on assumptions without any theoretical or generalized empirical guarantee” (R2).
    - Equation 6 assumes that the number of correctly self-predicted data points equals the number where self-prediction matches an incorrect pseudo-label in the same bin – this is not theoretically justified and Figure 4(b) only shows low average error but with several high-error outliers, casting doubt on the assumption (R1, R3).
    - Replacing true accuracy A_i with estimated accuracy \hat{A}_i from pseudo-labels is questionable; “the core issue here is the substitution … it’s highly unlikely that \hat{A}_i will accurately reflect A_i” (R3). The manipulation in Eq. 6 “should not be held” (R3).
    - The empirical observation in Figure 4(b) may be an artifact of the strong pre-trained network used; the authors need to demonstrate it holds for a broader range of models and datasets (R3).
- **Insufficient experimental coverage and ablation.**
    - Only three SFDA methods (SHOT, AaD, DCPL) are tested; it is not shown that these fully represent existing SFDA approaches (R2).
    - No ablation comparing GEPL with other pseudo-label improvement techniques (e.g., thresholding-based method) is provided (R2).
    - Other calibration error metrics besides ECE should be reported (e.g., SCE) because ECE can be misleading (R2, R4). Also, the accuracy of all SFDA models should be reported (R2).
    - The relation between Figure 3(b) and Figure 4(b) regarding Eq. 6 is unclear (R1). Figures 1 and 2 should clarify whether results are recorded at the end of adaptation, and how these indicators evolve during adaptation with associated accuracy levels (R1).
- **Presentation is hard to understand.** Several reviewers note poor readability: Section 3 needs better splitting (R4); lines 191-208 are confusing (R2); the distinction between “pseudo label” and “predicted label” in Equation 4 is unclear – both are derived from the model’s output at different stages but need precise definitions (R3); the figure illustrating the basic calibration setting is missing (R4).
- **Minor / specific concerns.**
    - How was the number of bins decided? Would variations in bin number affect calibration outcomes? (R1, R3: “Are the bins divided manually with a fixed number?”)
    - For temperature scaling, is the optimal temperature calculated on the entire dataset or per mini-batch? (R1)
    - Line 309: “we followed the evaluation protocol described in the TransCal Paper, which involves splitting each target domain into 80% for training and 20% for validation” – It appears TransCal split the *source* domain, not the target domain (R4). Clarification needed.