- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper introduces NARCISSUS, an unsupervised anomaly detection method that exploits the observation that models converge faster on normal data than on anomalous data when trained on mixed data. It uses a tailored early stopping scheme (VES) with an ensemble extension (RVES) to detect anomalies without labels. The core claim is that NARCISSUS achieves accuracy comparable to state-of-the-art semi-supervised methods while operating in a fully unsupervised setting.

## Strengths

- **Theoretical grounding for the core insight (Theorem 4.2, §4.3)**: The theorem formalizes a sufficient condition (N_n·δ_n ≫ N_a·δ_a) under which SGD updates are dominated by normal data, providing a mathematical rationale for why a model trained on mixed data initially fits normal instances. This directly supports the paper's central claim.

- **Empirical demonstration of matching semi-supervised accuracy (Table 2, §5.2)**: Across five time-series datasets (SMD, MBA, SMAP, SWaT, Synthetic), NARCISSUS applied to four different base models (GDN, TranAD, NPSR, MTAD-GAT) achieves F1 scores within 0.02–0.04 of the corresponding semi-supervised methods trained on clean normal data. On SMAP, it surpasses the semi-supervised baseline (0.91 vs. 0.89 F1). This is direct evidence for the paper's main claim.

- **Ablation isolating the contribution of VES (Figure 3, §5.4)**: Bootstrapping without VES (randomly selecting training subsets and training to convergence) yields wildly unstable F1 scores on the MBA dataset (0.43–0.97). This contrast cleanly demonstrates that the proposed early-stopping scheme is responsible for the method's stability, not merely the use of a semi-supervised base model.

- **Model-agnostic design and cross-modal demonstrations (§5.2–5.3)**: NARCISSUS is a wrapper that can be applied to any semi-supervised AD model as its base. The paper demonstrates this on 7 different base models for time series, and provides feasibility demonstrations on image (PatchCore on MVTec2D, AnoGAN on MNIST) and graph (AddGraph on UCI Message/Digg) anomaly detection. While the image/graph experiments are thin (the paper acknowledges this), they do show the method is not narrowly tied to time series.

- **Explicit handling of model uncertainty via RVES (Alg. 2, §4.4)**: The ensemble method (RVES) addresses the practical challenge of epistemic uncertainty from validation-set selection by repeatedly running VES with different random splits and ensembling the results. The paper also honestly discusses limitations (data boundedness, sparsity requirement, large-dataset need in §6), which strengthens the evaluation's credibility.

## Weaknesses

### Fatal

None.

### Major

- **Main results lack statistical variance information (Tables 1–2, §5.2)**: The paper reports only point estimates of F1, AUC, and precision without standard deviations or confidence intervals. Given that VES and RVES involve stochastic elements (random validation subsets, multiple retraining loops), variance is expected to be non-negligible. The paper does show one box plot for bootstrapping variance (Figure 3), but the main results — which support the central claim that NARCISSUS matches semi-supervised performance — provide no information about whether reported margins (e.g., differences of 0.01–0.02 in F1) are significant or within noise. Without this, a reader cannot assess the reliability of the core experimental claim. This is the single most impactful gap in the evaluation.

### Minor

- **VES hyperparameters are underspecified and lack sensitivity analysis (§4.4)**: The VES algorithm's η (fraction used to filter high-loss validation subsets) is discussed qualitatively ("empirically we can choose a large η") but no specific values used in experiments are reported, nor is a sensitivity analysis provided. Since η is meant to reflect an upper bound on the anomaly ratio — which is unknown in practice — guidance on how to set it and how robust performance is to misspecification would be necessary for practitioners to trust the method. Similarly, the number of validation subsets and the early-stopping patience are not disclosed in the main text.

- **Theory provides intuition but does not directly validate the VES algorithm (§4.3–4.4)**: Theorem 4.2 gives a sufficient condition under which SGD is dominated by normal data, and Corollary 4.3 states that "the first converged data are more likely normal." However, the specific VES mechanism (mean+max filtering across random validation subsets, intersection-based convergence detection) is not formally derived from this theory. The connection is intuitive and plausible, and many papers have theory-motivated heuristics, but the paper presents the mathematics as rigorous justification without explicitly linking the theory to the algorithm's design choices. Clarifying this gap would improve the paper.

- **Image and graph experiments are feasibility demonstrations rather than thorough evaluations (§5.3)**: The paper evaluates PatchCore on MVTec2D (where PatchCore uses a frozen pretrained feature extractor, making training dynamics potentially trivial), AnoGAN on MNIST (a simple toy dataset), and AddGraph on two graph datasets. The paper acknowledges this limitation ("Less image and graph cases are studied"). The results support the claim of cross-modal applicability but do not constitute a rigorous evaluation.

### Trivial

- None that are not parser artifacts.

## Nice-to-Haves

- **Computational overhead comparison**: The paper claims "comparable computational overhead" but provides no runtime comparison. RVES requires multiple training runs, so a quantitative overhead analysis would be useful for practitioners.
- **Systematic analysis of failure cases**: The paper identifies one failure case (MTAD-GAT on NAB, small dataset) but does not systematically analyze how dataset size or anomaly ratio affects performance. A sensitivity study across these dimensions would help define the method's applicability region.
- **Comparison against additional recent unsupervised/one-class methods**: While the paper compares against DAGMM, MSCRED, and Merlin, including methods like DROCC or GOAD (which also attempt strong unsupervised AD) would further contextualize results.

## Removed Points

These points from the input reviews were evaluated and removed with justification:

- **"Missing self-supervised baselines (Deep SAD, DROCC, GOAD)"** — REMOVED. Deep SAD is semi-supervised (requires labeled anomalies or labeled normal data). DROCC assumes clean training data. These operate in different supervision settings than NARCISSUS (which trains on mixed data with no labels). The paper's existing unsupervised baselines (DAGMM, MSCRED, Merlin) are appropriate.
- **"Hollow comparison in Table 1"** — REMOVED. The critic claimed comparing NARCISSUS against different unsupervised architectures is a "hollow" comparison. This is incorrect — the paper's claim is that NARCISSUS (wrapping a semi-supervised model) outperforms pure unsupervised methods, which is exactly what Table 1 shows. The within-architecture controlled comparison is provided in the ablation study (Figure 3, Table 6).
- **"EL2N claim not substantiated"** — REMOVED. The paper explicitly defers this discussion to the appendix (§A.2, Theorem A.2), which was stripped by the parser. The main paper clearly states where this substantiation can be found.
- **"Straw-man argument about self-supervised methods"** — REMOVED. The paper's reasoning (line 185) is logically sound: self-supervised pseudo-label methods require an initial unsupervised detector, and NARCISSUS could serve as that module.
- **General speculation about confounders or proxy metrics** — REMOVED as these were unanchored in specific paper content.
- **Pure formatting/style nitpicks** — REMOVED per instructions.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface a tension that the paper does not fully resolve: the gap between the clean theoretical framing (Theorem 4.2, which is about SGD convergence under bounded gradients) and the engineered heuristics of VES (random subsets, mean+max filtering, intersection-based detection). An insightful observation is that the paper could strengthen itself significantly simply by adding variance bars to its main tables and reporting η values — these are relatively low-effort changes that would address the most serious weakness without altering the method.

## Suggestions

1. **Add standard deviations to Tables 1–2** from multiple random trials (different validation splits). This is the single highest-leverage improvement — it would directly address the most significant weakness and let readers assess whether reported differences are meaningful.
2. **Report specific η values used in experiments** and, ideally, include a sensitivity analysis showing how performance varies with η on a few representative datasets (e.g., varying η from 1% to 30%).
3. **Clarify the connection between theory and algorithm** by stating explicitly which parts of VES are theoretically motivated and which are heuristics validated empirically.
4. **Add a short computational overhead table** showing training time for NARCISSUS vs. semi-supervised baselines.
