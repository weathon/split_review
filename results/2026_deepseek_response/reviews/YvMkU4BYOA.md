Now I have sufficient calibration material. Let me compose the final consolidated review.

## Summary

XBIC augments BIC's complexity penalty with edge-specific Shapley values from XGBoost classifiers to improve edge orientation in discrete Bayesian network structure learning. On 10 benchmark networks (6–76 nodes) across 7 sample-size regimes (700 runs), XBIC with w=2 achieves a 5.6% relative F₁ improvement over BIC-HC, alongside additional claimed improvements over PC (+20.9%) and GES (+9.6%). The method is clearly presented and gracefully reverts to standard BIC when directional evidence is weak.

## Strengths

1. **Novel, principled integration of feature attributions into score-based structure learning.** The idea of using local Shapley values from predictive classifiers to edge-specifically modulate the BIC penalty is, to my knowledge, genuinely new. Unlike prior work that assumes a known causal graph to constrain explanations (Frye et al. 2020, Heskes et al. 2020), XBIC uses explanations when the graph is unknown to improve structure learning itself. This is a creative and timely bridge between XAI and causal discovery.

2. **Consistent empirical improvement over the primary baseline (BIC-HC).** Table 2 shows that XBIC (w=2) achieves positive F₁ deltas over BIC-HC in 47 out of 54 reported cells across ten networks and seven sample-size regimes. Negative values appear only in a few small-network or small-sample cases (e.g., Win95pts at 8M²: −0.09 vs BIC). Table 4 aggregates this into a +5.6% relative (0.04 absolute) F₁ improvement across all 700 runs. The comparison to BIC-HC is clean and supports the core claim.

3. **Graceful degradation when directional signal is weak.** XBIC is designed so that when w=0 or SHAP(G)=0 it reduces to standard BIC, and the confidence threshold τ filters low-certainty predictions before computing attributions. The paper explicitly documents cases where XBIC does not improve over BIC (small samples), which strengthens credibility (Section 4.3, Table 2).

4. **Transparent computational cost reporting.** Table 5 provides concrete wall-clock comparisons (e.g., Alarm: BIC 9.30s, PC 12.22s, XBIC 523.52s). The Limitations section honestly discusses runtime, small-sample issues, and scalability constraints. This allows practitioners to assess the cost-benefit trade-off rather than having overhead hidden.

## Weaknesses

### Major

**1. PC and GES comparisons are undermined by random orientation of baseline PDAGs.**  
The paper states: "For baselines that return a PDAG, we complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics" (Section 4.1). PC and GES output CPDAGs that respect Markov equivalence — they are designed to leave edges undirected when data cannot resolve the direction. Randomly orienting those edges injects arbitrary noise into precision and recall for the baselines, creating a fundamentally unfair comparison. The claimed +20.9% over PC and +9.6% over GES largely reflect how much better a purpose-built DAG-orientation scheme (XBIC) performs versus random orientation of baseline outputs. This undermines two of the three headline claims in the abstract. The BIC-HC comparison (the paper's primary baseline, since XBIC is a modification of BIC) is unaffected, but the inflated PC/GES claims reduce trust in the experimental design.

**2. The core assumption that Shapley-value asymmetry indicates causal direction is unvalidated.**  
The method assumes that if |\bar{φ}_{j→i}| > |\bar{φ}_{i→j}|, this asymmetry provides evidence favoring edge Xⱼ→Xᵢ over Xᵢ→Xⱼ. The paper offers only an intuitive statement (Section 3.2: "Intuitively, if |\bar{φ}_{1→2}| ≫ |\bar{φ}_{2→1}|, the edge X₁→X₂ has stronger directional support") but provides no theoretical or empirical validation. In a purely predictive setting, a strong predictor of a variable could be its descendant, a confounded sibling, or a collider — not necessarily its cause. Without a controlled experiment showing that this asymmetry actually tracks true causal direction (e.g., on a known graph comparing asymmetry to ground-truth orientation), the mechanism remains a plausible but untested heuristic. This matters because without knowing *why* XBIC works, one cannot predict when it will fail.

### Minor

**3. Hyperparameter w is only explored over {1,2,3}, and its interaction with data regimes is under-analyzed.**  
The sweep is coarse (three values), and the paper averages gains across all 700 runs to report the headline 5.6% figure. Figure 2 shows that the precision-recall trade-off shifts with sample size and network — for some settings larger w helps recall at noticeable precision cost. The paper aggregates across these heterogeneous regimes rather than characterizing *when* XBIC helps and why. The blanket "5.6% improvement" masks cases where XBIC provides no benefit (small samples) or harms performance (e.g., Win95pts at large samples). A more nuanced characterization of the method's operating regime would strengthen the paper.

**4. The "drop-in upgrade" framing overstates practicality.**  
The abstract and conclusion claim XBIC "remains a drop-in upgrade within the familiar BIC framework" and is a "drop-in modification of a familiar score." In practice, XBIC requires: (i) training M XGBoost classifiers with 5-fold CV hyperparameter search, (ii) computing exact TreeSHAP on confidently predicted instances for each target, and (iii) running a hill-climbing search with the modified score. Table 5 shows XBIC is 100–1000× slower than BIC-HC (e.g., Alarm: 9.30s → 523.52s). While the score equation itself is a simple modification of BIC, the front-loaded attribution pipeline is a substantial addition. The paper acknowledges the runtime in Limitations, but the "drop-in upgrade" language in the abstract and conclusion is misleading.

**5. Absolute F₁ improvements are small (0.02–0.06 absolute).**  
Even accepting all comparisons at face value, Table 4 shows absolute F₁ improvements of 0.02–0.06 over baselines. At 100–1000× the runtime of BIC-HC, these modest absolute gains raise questions about practical significance, particularly given that the method has not been validated on real-world (non-benchmark) discrete data.

### Trivial

- The confidence threshold τ value is not stated in the paper. The text mentions varying it between 0.7 and 0.95 changes F₁ by <1%, but the actual value used in experiments is not reported.
- The exponential form in Eq. (2) (dim(G) / exp(w·SHAP(G))) is presented without justification for why exponential rather than linear or additive modulation was chosen.

## Nice-to-Haves

- A comparison on the CPDAG/PDAG level (e.g., structural Hamming distance on the CPDAG, or oriented-edge metrics restricted to edges that the baseline actually orients) would fix the PC/GES comparison issue and could strengthen the paper substantially.
- A controlled experiment validating the Shapley asymmetry → direction assumption on a known graph.
- Per-network, per-sample-size breakdowns with error bars rather than blanket averages, to characterize the regime where XBIC is useful.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Missing code link (reviewer flagged missing URL):** The parser strips URLs from all papers; the original submission includes a code link.
- **Missing MMHC baseline:** The paper explicitly scopes out MMHC as "target[ing] large sparse graphs and is not the focus here" — a reasonable scope decision.
- **Missing comparison to continuous-variable methods like CAM:** Requiring additional baselines from a different paradigm (continuous SEMs) is scope creep for a paper focused on discrete BNs.
- **Insufficient τ sensitivity analysis:** The paper states varying τ between 0.7–0.95 changes F₁ by <1% on average; a figure would be nice but the summary is sufficient.
- **No theoretical analysis of exponential form:** The consistency argument (penalty remains O(log N)) is provided; a formal theory analysis is deferred to future work, which is acceptable for an empirical paper.
- **Statistical rigor on GES comparison:** 175 samples from a biased subset is acknowledged honestly by the authors; the paired t-test is standard for this setting.
- **Missing appendix/proofs:** The parser strips appendices; they exist in the original submission.
- **Formatting/style nitpicks:** These are parser artifacts, not author errors.

## Novel Insights

The most interesting tension this paper surfaces is between the predictive power of a classifier and the causal structure it is trained on. The paper bets that strong predictive asymmetries (|φ_{j→i}| ≫ |φ_{i→j}|) reflect causal direction, but this is not obviously true — a descendant can be the best predictor of its ancestor. This points to a deeper question: under what conditions does the conditional distribution P(Xᵢ | X_{ⱼ}) encode directional information beyond the graph's Markov properties? The XBIC framework makes this implicit assumption explicit and testable, which is valuable even if the paper does not resolve it. The combination of a well-known score (BIC) with local explanations (Shapley) is a clean template that others could build upon with different base learners or attribution methods.

## Suggestions

1. **Fix the PC/GES comparison.** Compare on the CPDAG level (SHD on CPDAG, or oriented-edge metrics restricted to edges the baseline actually orients). Alternatively, drop these comparisons entirely and present XBIC solely against BIC-HC, which is a fair and already-strong benchmark.

2. **Validate the Shapley directionality assumption.** Add a controlled experiment: on a known graph, compute the Shapley asymmetry for each variable pair and compare it to the true causal direction. Report agreement rates and characterize failure modes (deterministic relationships, near-deterministic relationships, small samples).

3. **Characterize the operating regime.** Replace blanket averages with per-network and per-sample-size breakdowns (possibly in a table or figure with confidence intervals). Explicitly state where XBIC helps vs. hurts rather than reporting a single aggregate number.

4. **Tone down the "drop-in" language.** Acknowledging the front-loaded overhead honestly in the abstract (e.g., "at additional computational cost for attribution computation") would better align the claims with the evidence.

## Score and Decision

**Calibration anchor summary:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| JzFLBOFMZ2 | 3.20 | R1-low | Weaker — flawed LLM-based causal discovery, unclear methodology |
| fSxiromxAq | 3.00 | R1-low | Weaker — sparse-data causal model with limited rigor |
| AvXrppAS2o | 3.00 | R1-low | Weaker — narrow prediction-focused causal learning |
| TRHyAnInUC | 3.25 | R1-low | Weaker — diffusion-based CD with stability issues |
| eeJz7eDWKO | 6.00 | R1-mid | Stronger — solid methodology, clean evaluation, accepted |
| DUfwD5yiN4 | 5.25 | R1-mid | Similar in quality but different flaws (presentation) |
| eqQFBnjjPP | 4.00 | R1-mid | Weaker — exact DBN learning, limited experiments |
| 3n6DYH3cIP | 5.60 | R1-mid | Stronger — clean iterative SL with theory and experiments |
| xByvdb3DCm | 8.00 | R1-high | Much stronger — top-tier causal discovery analysis |
| EO8xpnW7aX | 8.00 | R1-high | Much stronger — unrelated topic but stellar execution |
| ljZFM2mhbR | 5.00 | R2 | Similar — DAG-SHAP: interesting Shapley+causal idea with evaluation concerns |
| i5JfdnCob7 | 4.40 | R2 | Weaker — incremental kernel selection for causal discovery |
| iaP7yHRq1l | 5.50 | R2 | Similar quality — CD robustness benchmark, mixed acceptance |

**Round 1 bracket:** 4.0 – 5.5 (below the stronger mid-band anchors at 5.6–6.0, above the weak anchors at 3.0–3.25)

**Round 2 narrowing:** The paper sits between the 4.4 kernel selection paper (weaker experiments, less novelty) and the 5.5–5.6 papers (cleaner evaluations). It is comparable to the DAG-SHAP paper at 5.0 (interesting Shapley+causal bridge, evaluation concerns), slightly below the 5.25 distributed SL paper (which had stronger theory but worse presentation). The paper's novel idea and thorough BIC-HC evaluation are strengths, but the unfair PC/GES comparison and unvalidated core assumption keep it below the acceptance threshold.

**Final score and decision:**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>