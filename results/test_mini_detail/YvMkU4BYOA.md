Now I have a good understanding of the paper and the calibration landscape. Let me synthesize the final review.

## Round-1 Bracket

Based on the calibration search:
- **Weak anchors** (avg < 3.5): avg 2.5–3.4 — papers with major flaws, missing experiments, or unclear contributions.
- **Middle anchors** (3.5–7.5): avg 4.0, 5.5, 5.6, 6.0, 6.0, 6.5, 7.33 — papers with solid ideas but various limitations.
- **Strong anchors** (7.5+): avg 8.0 — papers with clear impact, strong theory, and comprehensive validation.

**Initial bracket: 4.0–6.5.** The XBIC paper is clearly stronger than the weak-band rejects (it has real experiments, a coherent pipeline, and consistent results) but its modest absolute gains, missing ablation, and unsubstantiated core premise keep it below the 7+ tier.

After reading the round-2 anchors in detail, here is my assessment of where the paper sits:

- **DrBO (6.5)** — stronger empirical results and more established method family; XBIC is slightly below this.
- **Meta-Learning Bayesian CD (6.0)** — comparable thoroughness but better theoretical framing; XBIC is similar.
- **COSMO (5.6)** — both have clever ideas but significant limitations; XBIC is comparable.
- **Robustness of Differentiable CD (5.5)** — extensive experiments but debatable conclusions; XBIC is similar.
- **MPRT (6.0, rejected)** — good method but rejected due to limited applicability and scope mismatch; XBIC is comparable quality.

The paper lands around **5.5**. It is a borderline paper — the idea is novel and the evaluation is thorough, but the core premise lacks justification, the missing ablation prevents attributing gains to Shapley specifically, and the absolute improvements are modest relative to the computational cost.

Now let me write the final review.

Let me verify a few specific claims from the harsh critic against the paper text before writing:

1. "The penalty term dim(G) / exp(w·SHAP(G)) is not a standard multiplicative adjustment to BIC; it is a division." - Let me check the paper. Equation (2): XBIC_w = log P(D|G) - (log N/2) * dim(G) / exp(w * SHAP(G)). Yes, this is a division. This is just a statement of mathematical fact, not a criticism per se. The critic is pointing out it's unusual. I'll let this through as noted.

2. "consistency remark... SHAP(G) depends on the data through the classifier and thresholding; its value may change with N in ways that alter the asymptotic penalty order." - This is a valid concern about the hand-wavy consistency argument. Let me verify the paper's argument: Section 3.3 says "For fixed w and bounded SHAP(G), this scales as c(G) * (log N)/2 * dim(G) with c(G) ∈ (0, 1]." The critic notes that SHAP(G) itself may change with N. This is accurate criticism. RETAIN as minor.

3. "uses absolute Shapley values... discards the sign" - Paper uses |φ̄| in Equation (3). This is by design. I'll drop this - the justification for using absolute values is that they measure the strength of the attribution regardless of positive/negative influence on the prediction. This makes sense for determining whether an edge matters.

Now let me write the full review.## Summary

The paper proposes XBIC, a score-based causal discovery method for discrete data that augments the standard BIC objective with edge-specific Shapley values. For each variable, a classifier is trained to predict it from all others; TreeSHAP attributions are computed and aggregated to produce a directional signal for each candidate edge. This signal is used to soft-weight BIC's complexity penalty (edges with strong attribution support are penalized less), while defaulting to standard BIC when evidence is weak. The method is evaluated on 10 benchmark discrete Bayesian networks across 7 sample-size regimes (700 runs total) and shows consistent F₁ improvements over BIC hill-climbing (+5.6% relative), PC (+20.9%), and GES (+9.6%).

## Strengths

- **Novel integration of local feature attributions into a discrete score-based causal discovery pipeline.** The idea of using Shapley values from per-node predictors to modulate BIC's complexity penalty is, to my knowledge, new. The method cleanly reverts to standard BIC when no directional signal is detected (Eq. 2, Section 3), making it a drop-in replacement in existing BIC-based search procedures.

- **Extensive and well-organized empirical evaluation.** The paper tests across 10 benchmark networks (6–76 nodes), 7 sample-size regimes from sparse to very dense (0.125M² to 8M²), with 10 repetitions each (700 runs). This breadth exceeds what is typical for discrete causal discovery evaluations and allows the authors to characterize where the method helps (moderate-to-large samples, larger networks) and where it does not (very small samples, some small networks).

- **Consistent directional F₁ improvements in aggregate.** Table 4 shows XBIC (w=2) achieves +5.6% relative F₁ over BIC-HC, +20.9% over PC, and +9.6% over GES, with statistical significance via adjusted Friedman and Wilcoxon tests. The gains are most pronounced on larger networks (Alarm, Insurance, Hailfinder) where Markov-equivalence orientation is hardest for BIC.

- **Clear presentation of the precision–recall trade-off.** Figure 2 and the w sweep (w ∈ {1,2,3}) show how the softened penalty increases recall (admits more edges) at some precision cost, and the paper honestly reports that on several (network, sample-size) cells XBIC shows zero or negative deltas (Table 2).

## Weaknesses

### Major

- **The core premise — that the asymmetry in absolute Shapley values from a black-box predictor indicates causal direction — is asserted but never justified or ablated.** The mechanism is introduced in Section 3.2 as an intuitive statement ("Intuitively, if |φ̄₁→₂| ≫ |φ̄₂→₁|, the edge X₁→X₂ has stronger directional support"), but no theoretical argument, synthetic toy example, or diagnostic experiment demonstrates that this asymmetry actually correlates with ground-truth direction for the kinds of models studied. In a Bayesian network, Xⱼ predicting Xᵢ well does not imply causation; for the reversed direction Xᵢ → Xⱼ, Xⱼ is a function of Xᵢ plus noise, so Xⱼ may predict Xᵢ just as well. Because the entire method's directional signal rests on this claim, the lack of analysis is a significant gap.

- **Missing central ablation: would any measure of association work as well?** The penalty modulation exp(w·SHAP(G)) could be implemented with any edge-wise importance measure — e.g., absolute mutual information, correlation, or the classifier's built-in feature importance. Without an ablation that replaces Shapley values with a simpler (cheaper) importance measure, we cannot attribute the observed improvements to anything specific about Shapley values. The gains may reflect a generic "edges that are statistically associated are penalized less" effect, which correlation or mutual information would also capture. This weakens the evidence for the claimed contribution.

- **Practical utility is unclear given the cost–benefit ratio.** The absolute F₁ improvement over BIC is 0.04 (relative +5.6%), while runtime increases by 10–100× (e.g., 75s → 2139s on Win95pts, Table 5). On several networks and sample sizes, the improvement is 0.00 or slightly negative (Table 2). The paper mentions parallelization potential but provides no demonstration or quantification of how much it helps. Given the modest absolute gains, it is hard to argue XBIC is a practical replacement for BIC-HC in its current form.

### Minor

- **The consistency argument (Section 3.3) is hand-wavy.** The paper argues that because exp(w·SHAP(G)) is a constant factor for fixed G, the penalty still grows as O(log N). However, SHAP(G) depends on data through the trained classifiers and the confidence threshold τ, and its value may change with N in ways that alter the effective penalty order. No formal asymptotic analysis is provided.

- **The GES comparison is weakened by selective filtering.** GES runs exceeding the 7-day limit were excluded (Section 4.5), so the comparison is on the easiest (smaller, sparser) subsets. The paper acknowledges this honestly, but it means the headline "+9.6% vs. GES" applies to a favorable subset.

- **No analysis of how often XBIC actually resolves Markov-equivalence ambiguities.** The paper reports aggregate F₁ and SHD, but never breaks down how many undirected edges in the initial skeleton get correctly oriented by XBIC vs. BIC. This makes it hard to tell if the improvement is coming from orientation specifically or from other effects of the penalty modulation (e.g., including/excluding different edges).

### Trivial

- The confidence threshold τ sensitivity is mentioned as affecting F₁ by <1%, but τ also determines which instances contribute to Shapley aggregates — this aspect of sensitivity could be reported more explicitly.

## Nice-to-Haves

- A synthetic experiment or toy example demonstrating that the Shapley asymmetry actually tracks causal direction (even in a simple 3-variable collider vs. chain setup) would significantly strengthen the paper.
- A runtime-vs-parallelization analysis showing how many cores are needed to bring XBIC's wall-clock time down to competitive levels.
- Precision and recall curves (not just F₁) for all networks in the main text, not just three in Figure 2.

## Removed Points

The following points from the reviewers are removed with justification:

- *"Paper conflates 'contributes to prediction' with 'is a parent'"* — This is a softened version of the core-preme issue, already covered under Major weakness 1. Duplicate.
- *"The penalty is a division not a multiplicative adjustment"* — This is a statement of mathematical form, not a weakness. The paper explicitly defines the score in Equation (2).
- *"Absolute Shapley values discard sign information"* — Using absolute values is a deliberate design choice to measure attribution magnitude regardless of influence direction. This is reasonable.
- *"Missing comparison to simple weighting scheme"* — Already covered under Major weakness 2 (missing ablation).
- *"No discussion of overfitting risk from penalty reduction"* — The paper provides a consistency argument and notes the method reverts to BIC when SHAP(G)=0. Further discussion would be nice-to-have but not a core flaw.
- *Strength Finder: "Scalability analysis with parallelization potential"* — This is a promise, not demonstrated evidence. Kept as a minor supporting point but deemphasized.
- *Strength Finder: "Confidence-threshold filtering improves efficiency"* — Valid point, retained.

## Novel Insights

The reviewers' comments do not surface genuinely novel observations beyond what the paper itself provides. The main tension is between the paper's claimed mechanism (Shapley values provide directional signal) and the missing evidence for that mechanism. This is a gap the paper identifies as future work (Section "Limitations and future work"), not an insight.

## Suggestions

1. **Add the central ablation immediately.** Replace Shapley values in the XBIC penalty with (a) mutual information and (b) the XGBoost model's built-in feature importance (gain). If XBIC-Shapley outperforms these, the contribution is supported. If not, the paper should honestly characterize what is gained by the Shapley machinery.
2. **Provide a diagnostic experiment for the directional claim.** Use a small synthetic network (e.g., 3 nodes with a known collider and chain) to show that |φ̄ᵢ→ⱼ| − |φ̄ⱼ→ᵢ| correlates with the true direction. Even a few examples would help.
3. **Report improvements in terms of orientation accuracy for Markov-equivalence edges specifically.** Create a table showing, for each network, how many undirected edges get correctly oriented by XBIC vs. BIC. This would directly demonstrate the claimed benefit.
4. **Quantify the parallelization gains.** Show wall-clock time for XBIC with 1, 2, 4, 8 CPUs to give practitioners a concrete sense of the trade-off.

## Score and Decision

**Round-1 bracket:** 4.0–6.5 (below strong anchors at 7.5+, above weak anchors below 3.5).

**Round-2 narrowing:** Compared against DrBO (6.5, poster), Meta-Learning Bayesian CD (6.0, poster), COSMO (5.6, poster), Robustness of Differentiable CD (5.5, poster), and MPRT (6.0, reject):

- **DrBO (6.5):** Stronger empirical results with more dramatic structural improvements; XBIC's gains are more modest. **Paper is slightly weaker.**
- **Meta-Learning Bayesian CD (6.0):** Comparable thoroughness, but better theoretical motivation for the approach. **Paper is similar but with larger methodological gap.**
- **COSMO (5.6):** Both have clever ideas with significant limitations; COSMO's computational gains are more clearly demonstrated. **Paper is comparable.**
- **Robustness of Differentiable CD (5.5):** Extensive benchmark with some controversial elements; XBIC has a stronger novel contribution. **Paper is comparable.**
- **MPRT (6.0, reject):** Solid method but limited scope; XBIC has broader evaluation. **Paper is comparable.**

The paper has a genuinely novel idea and thorough evaluation, but the missing theoretical justification for the core directional claim and the missing ablation study prevent the contribution from being clearly distinguished from simpler alternatives. The absolute improvements are modest, and the computational cost is substantial.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>