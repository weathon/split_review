Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces the Subgraph Multilinear Extension (SubMT) as a theoretical framework for analyzing interpretable GNNs (XGNNs). It proves that existing attention-based XGNNs using weighted message passing fail to approximate SubMT (Proposition 3.3), which the paper argues leads to unfaithful interpretations and poor OOD generalization. To address this, the authors propose GMT (Graph Multilinear neT) with two variants: GMT-lin (linearized classifier with reduced message-passing rounds) and GMT-sam (MCMC sampling to estimate SubMT). GMT-sam is proven to ε-approximate SubMT with high probability (Theorem 5.1), and extensive experiments across 9 benchmarks with 3 backbone architectures show consistent improvements over state-of-the-art XGNNs like GSAT, often by 10–15% in interpretability and prediction accuracy.

## Strengths

1. **Novel theoretical framework identifying a fundamental limitation of attention-based XGNNs.** The paper formalizes interpretable subgraph learning as SubMT (Def. 3.1) and proves that existing XGNNs using weighted message passing fail to approximate SubMT (Proposition 3.3). This provides the first rigorous explanation for why prior methods may yield unfaithful interpretations, going well beyond empirical observations.

2. **Provably more powerful architecture (GMT-sam) with strong empirical gains.** GMT-sam is proven to ε-approximate SubMT with high probability (Theorem 5.1, using Hoeffding-based PAC bound). Under this guarantee, the method achieves consistent improvements of up to 15% in interpretability AUC and 13–16% in accuracy on challenging distribution-shift datasets (Spurious-Motif) over GSAT. These gains hold across three backbone architectures (GIN, PNA, EGNN) and two data modalities (regular graphs and geometric graphs).

3. **Principled faithfulness metric (counterfactual fidelity).** The paper introduces counterfactual fidelity (Def. 4.1) as a joint measure of interpretability and generalizability, and connects it theoretically to SubMT approximation (Proposition 4.2: ε-SubMT approximation implies \((\delta, 1-\frac{2\epsilon}{\delta})\)-counterfactual fidelity). Empirical validation (Fig. 2(b,c)) shows GSAT's counterfactual fidelity is 2–3× lower than simulated SubMT, confirming the theoretical diagnosis.

4. **Comprehensive and diverse experimental evaluation.** GMT is tested on 9 graph classification benchmarks spanning regular graphs (BA-2Motifs, Mutag, Spurious-Motif, MNIST-75sp, Graph-SST2, OGBG-MolHIV) and geometric graphs (Actstrack, Tau3mu, Synmol, Plbind), compared against both post-hoc methods and multiple XGNN baselines (GSAT, LRI, DIR, IB-subgraph). The breadth of evaluation convincingly demonstrates generality.

5. **Ablation studies confirming design choices.** Fig. 3(a) directly shows that GMT-lin and GMT-sam achieve higher counterfactual fidelity than GSAT. Fig. 3(b,c) show robust performance across a range of sampling rounds and regularization weights, with interpretability improving as sampling rounds increase, directly supporting the theoretical rationale.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **The theoretical guarantee for GMT-lin requires a linearized classifier, and the abstract's "provably more powerful" framing does not immediately differentiate between variants.** The paper proves (Sec. 5.1, Eq. 12–14) that GMT-lin fits SubMT under the assumption that the classifier is linear (∃T such that T·f_c(G_c) = P(Y|G_c)). The paper does acknowledge this limitation explicitly in Sec. 5.2 ("Although GMT-lin works for linearized GNNs, the non-linear GNNs are more widely used in practice"). However, the abstract and introduction state that *GMT* is "provably more powerful" without distinguishing that this guarantee applies unconditionally to GMT-sam (Theorem 5.1, which holds for any GNN) but only conditionally to GMT-lin. A reader who skims the paper may overestimate the scope of the rigorous guarantee for GMT-lin. The paper would benefit from stating upfront that the unconditional provable result applies to GMT-sam, while GMT-lin's guarantee requires linearity.

2. **The theoretical analysis of existing XGNNs (Proposition 3.3) is proven for linear GNNs; the extension to nonlinear architectures is heuristic.** Proposition 3.3 states that "Eq. 8 with linear GNNs (Eq. 9) and k>1 can not approximate SubMT." The paper then uses the Jensen gap (convexity of f_c(E[A]) ≤ E[f_c(A)] when k=2, |V|=1) to illustrate the issue, and argues heuristically that nonlinear GNNs face analogous problems. While the general claim is plausible and the linear-case proof is rigorous, the theoretical foundation for the exact architectures used in experiments (GIN, PNA, EGNN, which are nonlinear) remains heuristic rather than formally proven. This is not a fatal issue — the paper's main provable contribution (Theorem 5.1 for GMT-sam) does not depend on this extension — but it means the diagnosis of prior methods is not as tight for the architectures actually evaluated.

3. **The counterfactual fidelity metric, while theoretically connected to SubMT, would benefit from more direct validation.** The metric is theoretically grounded (Proposition 4.2 links it to SubMT approximation), and Fig. 3(a) shows it correlates with interpretability improvements. However, the current validation relies on comparing GMT and GSAT's own metric values without an independent ground-truth check (e.g., showing that the metric correlates with motif-accuracy across models with known faithfulness levels). This does not invalidate the metric, but the paper's argument for the metric's validity would be stronger with such an experiment.

4. **The exact number of sampling rounds t used in the main experimental tables (Tables 1–4) is not explicitly stated.** Fig. 3(b) provides an ablation showing robust performance across a range of t values, and the paper notes saturation with moderate sampling, but specifying the exact t used in each main-table experiment is important for reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Controlled comparison of GMT-lin and GMT-sam with identical backbones.** The paper's main experiment uses GMT-lin with a linearized classifier and GMT-sam with nonlinear classifiers. A controlled comparison (both variants on linearized GNNs, or both on nonlinear GNNs) would more cleanly isolate the source of improvements.
- **Reporting of wall-clock time or relative computational overhead.** GMT-sam requires t forward passes, which the paper acknowledges as a challenge. A quantitative comparison of training/inference time versus GSAT would help practitioners assess the trade-off.
- **Direct validation of counterfactual fidelity against ground-truth motif accuracy.** An experiment showing that counterfactual fidelity scores correlate with known motif recovery accuracy across a diverse set of models would independently validate the metric.

## Removed Points

- **"Circularity risk" in counterfactual fidelity (Harsh Critic, Point 2).** The critic claimed the metric is defined in terms of "the very attention distribution that GMT aims to improve" and thus has a circularity risk. This is not correct. Definition 4.1 measures prediction sensitivity to meaningful subgraph perturbations (with δ ensuring only non-trivial changes count). The practical estimation uses perturbations of the attention scores, but that is standard for input-sensitivity faithfulness measures and does not create circularity — the metric does not assume the attention distribution is correct. Removed as factually incorrect.
- **Claim that the paper overclaims generality of the theory beyond what is proven (Harsh Critic, Point 3, part about "the claim is that the failure generalizes to all attention-based XGNNs").** Proposition 3.3 is explicitly scoped to linear GNNs. The paper's broader claim about existing approaches is supported by the Jensen gap argument, which illustrates the fundamental issue and is standard theoretical practice. The critic overstates the gap between what is proven and what is claimed. Removed as a misreading of the paper's clear scoping.
- **"Missing appendix" style concerns.** Any references to missing proofs, appendices, or supplementary material are parser artifacts; these sections exist in the original submission. Removed per hard rules.

## Novel Insights

The reviews collectively surface a subtle but important tension that the paper itself does not fully discuss: the connection between the *distribution-free* nature of GMT-sam's guarantee (Theorem 5.1 holds for any attention distribution) and the *distribution-dependent* nature of its empirical success. Theorem 5.1 uses a PAC bound that is agnostic to the quality of the attention scores — it only requires i.i.d. sampling from whatever distribution the extractor produces. This means GMT-sam's theoretical advantage over GSAT is purely about *estimation* (replacing a biased plug-in estimate with an unbiased Monte Carlo estimate), not about *extraction* (finding the right subgraph). The empirical results suggest that better SubMT estimation also leads to better subgraph extraction via gradient feedback, but the theory does not yet model this feedback loop. This observation suggests a potentially fruitful direction: analyzing how improved SubMT estimation during training affects the convergence of the subgraph extractor g, beyond the current analysis which focuses on the behavior of the classifier f_c at a fixed extractor.

## Suggestions

1. In the abstract and introduction, clarify the scope of the provable guarantee: "GMT-sam is provably more powerful (Theorem 5.1, for any GNN classifier), while GMT-lin provides an alternative with a provable guarantee under a linearity assumption."
2. Add a reproducibility statement specifying the exact number of sampling rounds t used in each experimental setting.
3. Include a table or paragraph quantifying the computational overhead of GMT-sam (e.g., relative training time vs. GSAT) so readers can assess the trade-off.
4. For the counterfactual fidelity metric, add a simple experiment correlating the metric with known motif accuracy (e.g., on BA-2Motifs where ground-truth motifs are known) across models with different faithfulness levels.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>