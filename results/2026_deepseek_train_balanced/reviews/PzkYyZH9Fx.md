Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

NARCISSUS proposes an unsupervised anomaly detection method built on the insight that neural networks trained on mixed normal-and-anomalous data converge on normal data first. It uses Very Early Stopping (VES) to halt training once the model has fit normal data but not yet fit anomalies, and Robust VES (RVES), an ensemble strategy, to mitigate stochastic bias from validation-set selection. The method is model-agnostic — any semi-supervised AD model can be used underneath. Evaluated on time series (6 datasets, 7 base methods), images (MVTec2D, MNIST), and graphs (UCI Message, Digg), the paper claims NARCISSUS achieves accuracy comparable to semi-supervised methods without requiring any labeled data.

## Strengths

1. **Compelling central empirical result (Tables 1–2).** Across 7 semi-supervised base methods and 6 time-series datasets, NARCISSUS-trained models achieve F1 scores within 0.02–0.04 of the same models trained on clean normal data, and sometimes surpass them (e.g., SMAP). Table 1 further shows NARCISSUS significantly outperforming all purely unsupervised baselines. This directly supports the paper's core claim.

2. **Ablation convincingly isolates the contribution of VES (Figure 3, Section 5.4).** Removing VES (pure bootstrapping) yields F1 scores ranging from 0.43 to 0.97 on TranAD/MBA — demonstrating that naive random-subset selection is unreliable. Removing RVES also degrades performance. This gives confidence that both components are necessary.

3. **The core insight is well-motivated and grounded.** The paper provides a formal conditional statement (Theorem 4.2) linking sparsity, gradient boundedness, and convergence direction, and illustrates the phenomenon empirically (Figure 1). While the theorem is not a deep proof (see weakness #1 below), it provides useful formal scaffolding connecting data characteristics to convergence behavior.

4. **Candid limitations section (Section 6).** The paper explicitly states the conditions under which NARCISSUS may underperform (non-sparse anomalies, very small datasets) and acknowledges the limited image/graph evaluation. This transparency is valuable.

5. **Demonstrated across three data modalities with three different base methods.** Even though the non-time-series experiments are limited (see weakness #3), the paper shows the approach generalizes beyond a single data type.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or statistical reliability reported for any main result.** Tables 1 and 2 report only point estimates (precision, AUC, F1). NARCISSUS involves randomness through validation-set selection (RVES) and random initialization, so results must exhibit variance. The only variance shown is for the *bootstrapping baseline* (Figure 3), which the paper then uses to argue bootstrapping is unstable — but without comparable variance measures for NARCISSUS, the reader cannot assess whether the claimed F1 advantages are meaningful or within noise. At a top venue, this is a significant evidential gap.

2. **Missing comparison against self-supervised pseudo-label methods.** The paper states (line 185) that self-supervised methods (Li et al., 2021; Zhang et al., 2023) are "not considered because they would need a method like NARCISSUS as a module." This justification is circular — it presumes the conclusion that NARCISSUS is superior. These methods represent the most directly competing paradigm for unsupervised AD aiming to approach semi-supervised performance. The paper's claim that self-supervised workflows are "unnecessary" is not supported by the evidence presented. A direct comparison on at least a subset of benchmarks is needed.

### Minor

3. **Theorem 4.2's novelty is overstated.** The theorem is a correctly stated conditional: *if* N_n·δ_n >> N_a·δ_a, *then* SGD converges toward fitting normal data. The paper motivates the condition via data sparsity and well-boundedness (Section 4.2), but never formally bounds δ_a relative to δ_n — the line "assuming δ_a is not excessively larger than δ_n" (line 113) is asserted, not proven or systematically validated. The theorem formalizes the intuition but does not independently prove it; the paper presents it as stronger theoretical grounding than it actually delivers.

4. **No sensitivity analysis for η (anomaly proportion bound).** The η parameter is described as "the upper bound of the portion of anomalous data" (line 147). In a truly unsupervised setting this is unknown; the paper's suggestion to "choose a large η" (line 158) is a reasonable heuristic, but the paper does not report what η values were used for each dataset or show how results vary with η. Without this, the reader cannot assess how dependent the method is on this parameter choice.

5. **Limited non-time-series evaluation relative to the generalizability claim.** The image experiments use MNIST (an easy AD benchmark) and PatchCore with fixed pretrained features (not end-to-end training). The graph experiments are described as "comparable" without specific numbers in the extracted text. The paper acknowledges this limitation (line 250), but the scope of the evidence for generalizability is thin.

6. **Computational cost of RVES not discussed.** RVES retrains the model multiple times with different validation splits. For transformer-based time-series models, this could be substantial. No analysis of total training time relative to baselines is provided.

7. **Optimization problem (Eq. 3) is introduced but never formally connected to VES.** The paper states VES "constraint[s] ... Eq. 3 is met" (line 149) but does not derive VES from Eq. 3 or prove the connection. The optimization formalization motivates the approach but is not operationalized — it could be removed without affecting the paper's core contribution.

### Trivial

- Line 149: notation inconsistency — "V'∩V*" uses the same symbol V' for what appear to be two different sets, making that sentence difficult to parse.

## Nice-to-Haves

- Report means and standard deviations over ≥5 random seeds for all main tables.
- Add sensitivity analysis for η (e.g., η ∈ {1%, 5%, 10%, 20%}) on a subset of datasets and base methods.
- Compare against at least one self-supervised pseudo-label method on a representative benchmark.
- Track the ratio of normal-to-anomalous gradient norms during training on one model/dataset to provide direct empirical evidence for the condition in Theorem 4.2.

## Removed Points

These points were flagged by the harsh critic but are removed after verification:

- *"Theorem 4.2 does not prove the paper's central claim — it assumes it"* → The theorem is a correctly formed conditional statement. That condition is motivated by data characteristics (sparsity + well-boundedness). The theorem contributes formalization even if it does not independently prove the insight. The harshest version of this criticism is inaccurate; the milder version (overclaimed novelty) is retained as Minor weakness #1.

- *"VES algorithm description is difficult to follow / notation inconsistent"* → The full pseudocode is in the appendix (stripped by parser). Notation roughness in the main text is partially a parser artifact. Removed per formatting/parser rules.

- *Strength: "Model-agnostic applicability across data modalities"* → Weakened/removed because the paper itself admits limited non-time-series experiments. The genuine but qualified evidence is already reflected in strength #5.

## Novel Insights

The harsh critic's observation that Theorem 4.2 is a conditional statement that assumes rather than proves gradient dominance is the most penetrating synthesized insight. It correctly identifies a gap between the paper's presentation (which implies the theorem independently establishes the convergence property) and what the theorem actually does (formalize the sufficient condition). The critic also correctly identifies that the missing variance reporting and η sensitivity analysis are the paper's weakest evidential links. These are genuine, addressable gaps — none are fatal, but in aggregate they make the paper's evidence less complete than its claims suggest.

## Suggestions

1. Report all main results as means and standard deviations over ≥5 random seeds.
2. Add a sensitivity analysis for η across at least 3–5 datasets.
3. Include a direct comparison to at least one self-supervised pseudo-label method.
4. Provide empirical gradient-ratio tracking on one model/dataset to validate the Theorem 4.2 condition directly.
5. When claiming generalizability beyond time series, either strengthen the experiments or proportionally qualify the claims.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>