## Summary
This paper introduces Fed-MADS, a Federated Active Learning (FAL) framework tailored for Explainable Federated Learning (XFL). Utilizing the Information Bottleneck (IB) principle, the authors derive a data selection strategy that identifies informative samples by maximizing the divergence between local client models and the global server model in both a semantically-rich latent space and the final label prediction space.

## Strengths
- **Theoretical Integration with XFL:** The paper provides a formal derivation using the Information Bottleneck principle to justify its selection criteria, specifically adapting the variational distributions to be implemented by the global model. This aligns conceptually with the architecture of XFL models (like LR-XFL) that rely on semantically-rich latent representations.
- **Improved Explainability Metrics:** The method shows improvements in specific interpretability metrics. Table 1 indicates that Fed-MADS achieves higher Rule Accuracy and Rule Fidelity compared to several baselines across the four evaluated datasets.
- **Labeling Efficiency:** The learning curves in Figure 2 suggest that Fed-MADS can reach high accuracy levels with a limited number of queries (up to 250) in the specific tested environment compared to the reported performance of other FAL methods.

## Weaknesses

### Major
- **Anomalous Baseline Performance:** In Figure 2, the "Random" sampling baseline consistently outperforms established FAL methods such as LoGo (CVPR 2023) and KSAS (ICCV 2023) across nearly all datasets. In typical Active Learning literature, Random sampling serves as a lower-bound floor; if sophisticated SOTA methods underperform Random, it usually suggests an implementation issue, lack of proper hyperparameter tuning for those baselines, or a fundamental incompatibility with the base `LR-XFL` architecture. This significantly undermines the claim of "significantly outperforming SOTA" because the method is effectively only competing against a Random baseline in an environment where other methods are non-functional.
- **Conceptual Gap in Heuristic Justification:** The transition from the IB objective (minimizing $I(X,Z)$ for compression) to the selection logic in Eq. (13) relies on the heuristic that samples maximizing the objective are "more informative." While common in loss-based AL, the paper lacks a rigorous discussion or empirical ablation to prove why this specific minimax divergence in the bottleneck space is more informative rather than just selecting outliers or noise.
- **Restrictive Evaluation (IID Assumption):** Federated Learning's primary challenge is data heterogeneity (Non-IID). Section 3.1 explicitly assumes I.I.D. data. This significantly limits the practical relevance of the findings, as AL is often most valuable for navigating distribution shifts and heterogeneity across clients which are absent from this study.

### Minor
- **Semantics of Explanations:** Despite the "Explainable" branding, the selection metric ($s_1 + \beta s_2$) treats the latent representation as a standard feature vector for a KL-divergence calculation. The method does not leverage the *semantics* or the logical rules themselves in the selection process. Therefore, the connection to explainability is methodological (working with an XFL architecture) rather than intrinsic to the selection logic.
- **Training Convergence Uncertainty:** The query budget is very small (5 samples per round for 10 clients). With MNIST augmented to 120,000 samples, querying 250 samples (0.2% of total) results in very high accuracy (90%+ in Fig 2a), suggesting the model might already be near convergence from the initial labeled set. This makes the relative gains from the AL strategy less impactful.
- **Computational Overhead:** Evaluating every unlabeled sample using two models (global and local) doubles the forward pass cost for selection. While the authors claim $O(|U_i|)$ efficiency, a discussion on the wall-clock time overhead compared to simpler metrics (like entropy) is missing.

## Nice-to-Haves
- Comparison of selection time vs. accuracy gain.
- Evaluation on Non-IID data splits to demonstrate robustness in typical FL scenarios.

## Removed Points
- **Criticism of citing unreleased models/references:** (Rule: If the paper cites it, it exists). 
- **Formatting/Style nitpicks:** (Rule: Ignore parser artifacts).
- **Missing Appendix/Proofs:** (Rule: Parser strips these; they are assumed to exist).

## Novel Insights
The integration of a global model to serve as the variational distribution within an IB-driven active learning framework is an interesting way to bridge information theory and federated dynamics. It provides a formal, albeit heuristic, justification for "local-global disagreement" as a selection signal, specifically targeting the latent representation bottlenecks used in explainable AI models.

## Suggestions
- **Calibrate Baselines:** Re-evaluate and tune the baselines (LoGo, KSAS) to ensure they are being applied correctly to the LR-XFL architecture, or clarify the reasons for their failure to beat Random sampling.
- **Non-IID Experiments:** Add experiments with Dirichlet-based label skew to demonstrate the method's effectiveness in heterogeneous federated environments, which is the standard benchmark for FL.
- **Ablation of s1 vs s2:** Provide a clearer breakdown of how the latent divergence ($s_1$) specifically improves rule fidelity compared to just using prediction divergence ($s_2$).

## Score and Decision

**Bracketed Range (Round 1):** Between 3.0 and 5.0. Comparisons with `GbXn0Dgf7f` (3.4) and `VRCh74Liu9` (4.25) suggest the paper is significantly weakened by the baseline performance issue and the IID assumption in a Federated context.

**Narrowing and Final Score:** 
- `GbXn0Dgf7f` (Avg 3.4): Evaluates if DAL works "in the wild." Reject. This paper shares the theme of AL underperforming or behaving unexpectedly compared to Random. Our paper is similar in that the baselines are failing against Random, but our paper presents a new method (`Fed-MADS`).
- `VRCh74Liu9` (Avg 4.25): Federated Generalization rejection. Our paper's lack of Non-IID evaluation makes it weaker than typical "Accept" level FL papers.
- `NK09Bcvuxl` (Avg 3.67): Low-budget Active Learning. This paper also shows degradation of AL algorithms at low budgets. Our paper operates at very low budgets (0.2% data) but reports very high performance, which raises questions about the strength of the evaluation setup.

The paper's reliance on IID data in an FL context and the extremely poor performance of reported SOTA baselines (beating Random) suggest major flaws in the experimental rigor. While the IB-based derivation is interesting, it does not currently outweigh the evaluation gaps.

| Anchor Paper | Avg Score | Round | Comparison |
|--------------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/GbXn0Dgf7f.md` | 3.40 | 1 | Our paper has similar issues with baseline/random comparison. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/NK09Bcvuxl.md` | 3.67 | 2 | Related to low-budget AL issues; our paper's result looks suspicious. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/VRCh74Liu9.md` | 4.25 | 1 | Stronger evaluation on non-IID than our paper, yet rejected. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ZG2AiVMj1I.md` | 5.00 | 2 | More robust theoretical framework for task trade-offs than our paper. |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>