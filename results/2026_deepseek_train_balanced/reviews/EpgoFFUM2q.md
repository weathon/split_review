## Summary

This paper studies test-time adaptation (TTA) for graph neural networks under distribution shifts, specifically targeting **structure shifts** (changes in homophily and degree) which existing TTA methods fail to handle. The authors provide theoretical analysis showing that attribute shifts primarily bias the classifier (Δ_g > 0) while structure shifts degrade node representations (Δ_f > 0). Based on this insight, they propose AdaRC, which adapts hop-aggregation parameters (γ) via a prediction-informed clustering (PIC) loss. The method is plug-and-play compatible with existing TTA methods and achieves strong empirical gains on both synthetic and real-world graphs.

## Strengths

- **Formal decomposition of the accuracy gap into representation degradation (Δ_f) and classifier bias (Δ_g):** Propositions 3.3 and 3.4 prove that under attribute shifts Δ_f = 0 and Δ_g = Θ(‖Δμ‖₂²), while under structure shifts Δ_f = Θ(Δh + Δd) and Δ_g = 0. This clean theoretical result provides a principled explanation for why existing classifier-adapting TTA methods fail under structure shifts and directly motivates the paper's approach.

- **Provably optimal γ adaptation with closed-form solution:** Proposition 3.5 derives the optimal hop-aggregation parameter γ_T = d_T(2h_T − 1) and shows that adapting γ improves accuracy by Θ((Δh)² + (Δd)²). This gives the method a theoretically grounded target rather than a heuristic.

- **Scale-invariant PIC loss with convergence guarantee:** The PIC loss (σ²_intra / (σ²_intra + σ²_inter)) is explicitly designed to avoid the trivial-solution problem of entropy minimization (scaling up logits). Theorem 4.1 provides a convergence guarantee at rate O(1/T), which is absent from most competing graph TTA methods.

- **Strong and consistent empirical gains:** AdaRC improves over the source model by up to 31.95% and boosts existing TTA methods by up to 40.61% across diverse settings — multiple structure shift types (homophily, degree), multiple TTA backbones (T3A, Tent, AdaNPC), multiple GNN architectures (GPRGNN, JKNet, APPNP, GCNII), and both synthetic (CSBM) and real-world datasets (Syn-Cora, Syn-Products, Twitch-E, OGB-Arxiv).

- **Computational efficiency:** AdaRC adds only 11.9% overhead per adaptation epoch (vs. 486% for GTrans and 247% for SOGA), and the PIC loss complexity is O(NCD), linear in the number of nodes.

- **Ablation confirms the design choice:** Adapting only γ works better than adapting the MLP parameters θ or both — the latter causes model forgetting (accuracy drop after initial gains). This ablation directly validates the paper's design thesis.

## Weaknesses

### Fatal

None.

### Major

- **Improvement metric is reported ambiguously as "up to X%":** The paper repeatedly states improvements such as "up to 31.95%" and "up to 40.61%" (lines 28, 227–230) without clarifying whether these are absolute percentage points or relative improvements. This is a significant communication gap because the two interpretations imply very different effect sizes. Since the improvement claims are the paper's headline quantitative results, this ambiguity prevents the reader from assessing the actual magnitude of the gains. The authors should state explicitly (ideally reporting both metrics).

- **PIC loss depends on BaseTTA predictions in a circular manner not systematically tested for failure regimes:** The PIC loss computes class centroids from BaseTTA's soft predictions (line 188). The paper frames this as positive "mutual reinforcement" — better predictions → better clustering → better representations → better predictions. However, the method is designed precisely for settings where BaseTTA performs poorly (severe structure shifts degrade representations). When BaseTTA initializes with poor pseudo-labels, centroids will be incorrect and PIC could cluster around wrong centers. The paper does not investigate where this loop breaks (e.g., by corrupting BaseTTA predictions and measuring whether AdaRC can still recover). This is a robustness concern that the current evaluation does not address.

### Minor

- **Gap between theoretical setting and experimental implementation:** The theory analyzes a single-layer GCN with a single scalar γ on CSBM graphs with uniform degree d and homophily h, deriving γ_T = d(2h−1). The experiments use GPRGNN with K+1 gamma parameters (γ₀,...,γ_K) learned via gradient descent on real graphs with heterogeneous degree and local homophily. The paper states (line 135) that "a wide range of GNN models possess similar parameters," which is true in spirit but does not formally bridge the gap between the closed-form optimum for a single parameter and gradient-based optimization of a multi-parameter gamma vector. The theory provides intuition rather than guarantees for the actual implementation.

- **Proposition 3 considers only a restricted form of attribute shift:** The analysis (line 117) models attribute shifts as a global translation of all class means by the same vector Δμ, which keeps inter-class separation unchanged. If different classes shift by different amounts or in different directions, the conclusion that Δ_f = 0 may not hold. This is a limitation of the theoretical analysis that is not acknowledged.

- **Proposition 4 only covers decreasing structure shifts:** The analysis (line 125) assumes d_T < d_S and h_T < h_S. The reverse direction (target graph has higher homophily or degree than source) is not addressed, and the paper does not discuss whether the method would still be beneficial in that regime.

### Trivial

None.

## Nice-to-Haves

- A diagnostic experiment where BaseTTA predictions are deliberately corrupted (e.g., by adding label noise at varying levels) to test whether AdaRC's mutual reinforcement loop is robust to poor initial pseudo-labels.
- A synthetic experiment validating that gradient descent on the PIC loss recovers the theoretical γ_T = d(2h−1) across different (d,h) configurations, which would strengthen the bridge between theory and practice.
- Discussion of conditions where AdaRC's advantage diminishes (e.g., extremely low homophily, very large degree disparities, simultaneous severe attribute and structure shifts).

## Removed Points

These points were raised by one or more reviewers but removed per the filtering rules:

- **SOGA tested on heterophilic graphs / unfair comparison:** The paper acknowledges SOGA is only applicable to homophilic graphs (line 35). Testing baselines across all settings is standard evaluation practice. REMOVED (asymmetry favors the author's method, so criticism is removed per filtering rules).

- **GraphPatcher tested on homophily-shift-dominated scenarios:** Same logic. REMOVED.

- **Missing comparison against GAPGC and GT3:** The paper states these methods are designed for graph classification (line 35), while this paper addresses node classification. REMOVED.

- **No confidence intervals or statistical tests:** Reporting mean and std over 5 seeds is standard for this setting. REMOVED.

- **Convergence guarantee only to flat region:** The paper is transparent about the nature of the guarantee. The concern about L not being concretely bounded is partially addressed by Lemma \ref{lem:linear} (in the appendix, stripped by parser). REMOVED.

- **PIC loss not compared against contrastive losses:** Contrastive losses are not standard TTA surrogate losses. The paper compares against entropy and pseudo-label, which are the standard baselines. REMOVED.

## Novel Insights

The most incisive observation from the reviews is the circular dependency in the PIC loss design: it uses exactly the predictions that are most unreliable in the regime the method targets. The paper's framing of "mutual reinforcement" cuts both ways — it could equally describe a failure cascade (bad predictions → wrong centroids → worse clustering → worse predictions). A diagnostic experiment probing this asymmetry would substantially strengthen the paper's robustness claims. The second key insight is that the theory-practice gap (single scalar γ on uniform CSBM vs. multi-parameter γ vector on heterogeneous real graphs) is wider than the paper acknowledges — the elegant closed-form solution provides intuition, but the actual gradient-based optimization on real graphs with the PIC loss could behave quite differently from what the theory predicts.

## Suggestions

1. Clarify whether the reported percentages (e.g., 31.95%, 40.61%) are absolute percentage points or relative improvements — ideally report both.
2. Add a diagnostic experiment corrupting BaseTTA predictions to test whether AdaRC's mutual reinforcement loop is robust to poor initial pseudo-labels, with accuracy measured as a function of noise level.
3. Acknowledge the limitations of the theoretical model explicitly: the restricted form of attribute shift (global translation), the decreasing-only direction of structure shifts, and the single-parameter-to-multi-parameter gap.
4. Consider adding a synthetic experiment showing that gradient descent on the PIC loss recovers the theoretical γ_T = d(2h−1) across different (d,h) configurations.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>