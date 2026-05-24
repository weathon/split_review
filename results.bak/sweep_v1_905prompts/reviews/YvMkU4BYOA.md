I now have a comprehensive understanding of the paper and the calibration landscape. Let me produce the final review.

## Summary

XBIC enhances BIC for score-based causal discovery on discrete data by softening the complexity penalty using aggregated Shapley values from per-node XGBoost classifiers. Edges whose candidate parent has a strong Shapley attribution get a reduced penalty, guiding hill-climbing toward better orientations within Markov equivalence classes. Evaluated on 10 benchmark networks (6–76 nodes) across 7 sample-size regimes (700 runs), XBIC with w=2 achieves a +5.6% relative F₁ improvement over hill-climbing BIC, alongside +20.9% over PC and +9.6% over GES.

## Strengths

- **Novel integration of local feature attributions into a score-based causal discovery objective.** Using edge-specific Shapley evidence to modulate BIC's complexity penalty is a genuinely new idea in the discrete causal discovery setting. The pipeline — train per-node classifiers, compute TreeSHAP, aggregate directional signals, and inject them as soft weights during hill-climbing — is clearly described and well-motivated. The paper correctly positions this as distinct from prior work that assumes a known causal graph to constrain explanations (Frye et al., 2020; Heskes et al., 2020) or that uses Shapley for other purposes (Breuer et al., 2024; Renero et al., 2025).

- **Consistent and non-trivial improvement over the most directly relevant baseline (BIC-HC).** The +5.6% relative F₁ gain over hill-climbing BIC (Table 4) is clean because both XBIC and BIC-HC output DAGs directly — no evaluation artifact affects this comparison. The improvement is observed across diverse networks and sample sizes, with statistical significance confirmed by adjusted Friedman and Wilcoxon tests (p < 0.05). The precision–recall breakdown (Figure 2) further shows that XBIC trades precision for recall in a controlled way as w increases.

- **Extensive evaluation scope.** Ten benchmark networks (6–76 nodes, medical/insurance/weather/software domains), seven sample-size regimes, 700 runs, and three baselines (BIC-HC, PC, GES) represents a thorough empirical effort. The ablation over w ∈ {1,2,3} and the sensitivity analysis for the confidence threshold τ (varying 0.7–0.95 changes F₁ by < 1%) demonstrate robustness. The GES comparison is handled honestly: runs that exceeded the 7-day limit are excluded, and XBIC is compared on the subset where GES completed, yet still shows lower SHD.

## Weaknesses

### Fatal
None.

### Major

- **PC and GES are evaluated after randomly orienting their undirected edges, which inflates the reported improvement over these baselines.** The paper states: "For baselines that return a PDAG, we complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics." PC outputs a CPDAG whose undirected edges are deliberately unresolved by the algorithm; randomly orienting them injects ≈50% error on those edges, artificially lowering precision and F₁. The same issue applies to GES. This does **not** affect the central comparison against BIC-HC (the most relevant baseline for a score-based method), but the headline figures of +20.9% over PC and +9.6% over GES are likely substantially inflated. A proper evaluation would compare at the CPDAG level (e.g., SHD on the Markov equivalence class, or reporting directed/undirected edge metrics separately). (See Section 4.1, bottom of p. 5.)

- **The core premise — that asymmetric Shapley values from associational classifiers reliably indicate causal direction — is stated without theoretical or controlled empirical support.** The paper builds on the intuition that |φ̄₁→₂| ≫ |φ̄₂→₁| implies X₁→X₂ is the correct direction (Section 3.2). However, these Shapley values come from purely associational classifiers (predicting Xᵢ from all other variables), and in many common generative mechanisms (e.g., linear-Gaussian chains), predictive asymmetries may be small, symmetric, or confounded. The paper does not provide a controlled experiment (e.g., on synthetic two-variable systems with known ground truth) that isolates whether this Shapley asymmetry aligns with causal direction across a range of discrete mechanisms. The method may still work empirically on the tested benchmarks, but the mechanism by which it works is not interrogated, making it harder to predict when it will fail or generalize.

- **The theoretical grounding is superficial and may not justify the claimed "consistency."** The "consistency remark" (Section 3.3) states that since the penalty scales as c(G)·(log N)/2·dim(G) with c(G) ∈ (0, 1], it "preserves BIC's order of penalization" and "preserves large-sample consistency." The issue is that c(G) = 1/exp(w·SHAP(G)) depends on the graph G, and SHAP(G) grows with the number of edges — potentially making the effective penalty per edge vanish for dense candidate graphs. This is not a rigorous consistency guarantee; it is an order-of-magnitude observation. The method is best understood as a heuristic with empirical motivation, not a principled extension of BIC with proven statistical properties.

### Minor

- **The exact confidence threshold τ used in the main experiments is not reported.** The paper states τ is varied between 0.7 and 0.95 with < 1% F₁ impact, but never specifies which value was actually used for the results in Tables 2, 4, and 5. This hinders exact reproducibility. (Section 4.1, p. 5.)

- **The "drop-in upgrade" framing overstates the practicality.** While the XBIC score function can be substituted for BIC in a hill-climbing loop, the method requires training M XGBoost classifiers with 5-fold CV and Optuna hyperparameter search, computing TreeSHAP on all confidently predicted instances, and then running the search. Table 5 shows XBIC is 10–200× slower than BIC (e.g., 2139 s vs 75 s on Win95pts). This is a significant practical limitation that the "drop-in" language obscures. The paper does acknowledge this in the Limitations section, but the abstract and introduction use "drop-in upgrade" without qualification.

- **Hyperparameter w cannot be selected without ground truth or a principled criterion.** The paper sweeps w ∈ {1,2,3} and reports the best (w=2) as the main result. In practice, the true graph is unknown, so w cannot be tuned on a validation set. The paper shows w=2 works best on average, but a practitioner deploying XBIC on a new dataset has no principled way to choose w without knowing the trade-off characteristics. A robustness analysis (w=1 and w=3 both show positive results but with varying precision-recall balance) somewhat mitigates this, but does not resolve it.

### Trivial

- None that are not addressed above.

## Nice-to-Haves

- A controlled synthetic experiment (e.g., two-variable systems with linear, nonlinear, and noisy discrete mechanisms) that directly measures whether Shapley asymmetry aligns with causal direction would substantially strengthen the paper's core premise.
- Reporting CPDAG-level SHD for PC and GES alongside the directed-edge metrics would address the evaluation concern without requiring extensive reruns.
- An ablation that replaces SHAP(G) with the number of edges (or total absolute coefficient magnitude) would help isolate whether the Shapley content itself drives the gains versus simply a softened penalty.

## Removed Points

The following points from the inputs were removed with justification:

- **Harsh critic's claim that "XBIC is not a drop-in upgrade because it requires training classifiers"** — this is a semantic dispute. "Drop-in" refers to the score function being substitutable in the search; the paper does acknowledge the computational overhead. Kept as a **minor** weakness (re: "drop-in upgrade" framing) rather than a separate item.

- **Criticism about "no theoretical or synthetic validation" of the Shapley directional signal** — kept as a major weakness **but rephrased**: the paper does provide empirical validation on 10 benchmark networks with known ground truth, so the claim of "no validation" is an overstatement. The weakness is that the mechanism is not diagnosed via controlled experiments, not that validation is absent entirely.

- **Criticism about "many entries are zero or small, and some are negative" in Table 2** — removed. This is expected behavior on small networks and limited data where the confidence filter fires rarely and XBIC defaults to BIC. The paper explicitly discusses this (Section 4.3, p. 6).

- **Criticism about missing comparison to MMHC** — removed. The paper says MMHC "targets large sparse graphs and is not the focus here." This is a reasonable scope choice given that several test networks are dense and small-to-medium sized.

- **"Code release" reproducibility concern** — removed per hard rules: the paper cites a URL and the rules state to treat cited artifacts as real.

- **Strength Finder's strength about "drop-in compatibility"** — downgraded to a caveated point; the framing is somewhat misleading for practitioners.

- **Strength Finder's claim that comparison is "fair"** — removed the "fair" characterization from the supporting strength; the comparison has a fairness issue with PC/GES.

- **Strength Finder's strength about "robust confidence-based filtering" showing <1% F₁ change** — kept, but noted that the exact τ value used is unreported.

## Novel Insights

None beyond the paper's own contributions. The core empirical finding — that aggregating Shapley directional signals from per-node classifiers and injecting them as a soft penalty into BIC can improve orientation within equivalence classes on discrete benchmarks — is the paper's central contribution. The reviews do not generate a genuinely novel insight beyond what the authors already establish.

## Suggestions

1. **Fix the PC/GES evaluation.** Re-run with CPDAG-level metrics (e.g., report SHD on the equivalence class, or report directed-edge metrics only on edges that the baseline orients with high confidence, leaving undirected ones as "no decision"). This would remove the most serious concern about the paper's headline numbers.
2. **Add a controlled diagnostic experiment.** Generate data from simple 2–4 variable discrete DAGs with known, varied mechanisms and measure whether the Shapley asymmetry score |φ̄ᵢ→ⱼ| − |φ̄ⱼ→ᵢ| consistently points in the correct causal direction. This would validate the method's core premise and help users understand its failure modes.
3. **Report the exact τ value used** and consider releasing the code's configuration files alongside the paper.
4. **Temper the "drop-in upgrade" claim** or pair it with a concrete runtime expectation (e.g., "XBIC adds a front-loaded computation ≈1–30 minutes for networks up to 76 nodes, after which the search itself runs at similar speed to BIC").
5. **Provide guidance on selecting w** — e.g., show that w=1 is a safer default when data is limited, or propose a data-driven criterion (based on effective sample size or SHAP(G) distribution) for choosing w without ground truth.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for score-based causal discovery papers in three bands:
- Low band (<3.5): anchors at 3.00–3.25 (papers with fatal flaws or minimal contributions)
- Mid band (3.5–7.5): anchors at 4.00–5.60 (mixed quality, ExDBN: 4.0, Optimal Kernel: 4.4, CI Test: 5.6, Determinism-Aware DGES: 6.25, Extendable Structure Learning: 5.6)
- High band (>7.5): anchors at 8.00 (clearly strong papers)

**Initial bracket:** Between 4.5 and 6.5.

**Round 2 (Narrowing):** Searched inside (4.5, 6.5) with topically relevant queries:
- Extendable Structure Learning (5.60): Accepted, solid incremental contribution with strong empirical results but heuristic with limited theory. Comparable to XBIC in contribution type and empirical scope, though XBIC has a more novel core idea.
- Meta-Learning Bayesian Causal Discovery (6.00): Accepted, well-executed but incremental architecture contribution. Stronger theoretical framing than XBIC.
- Determinism-Aware DGES (6.25): Rejected despite strong reviews; issues with novelty and limited completeness. Comparable in having a genuine idea with notable limitations.
- ψDAG (4.75): Rejected, standard continuous optimization approach with limited novelty.
- Causal Graph Learning via Distributional Invariance (5.00): Rejected, interesting idea but limited scope.

**Final score:** **5.0**. The paper has a genuinely novel core idea (Shapley-enhanced BIC) that is well-motivated and a thorough empirical evaluation against the most relevant baseline (BIC-HC). However, the evaluation issue with PC/GES random orientation inflates the headline improvement figures for those baselines, the theoretical grounding is thin, and the method's core premise (Shapley asymmetry → causal direction) is asserted without controlled validation. The paper is clearly stronger than the 3.0–4.0 papers (which have fatal or near-fatal flaws) but less polished than the 5.5–6.0 papers, which either have stronger theoretical framing or cleaner evaluation. The idea is worth pursuing, but in its current form the evidence overclaims relative to what the evaluation design supports.

**Final Decision:** **Reject** — the evaluation issue with PC/GES and the lack of validation for the core directional signal are significant enough that the paper does not meet the acceptance bar in its current form. With proper CPDAG-level evaluation and a controlled diagnostic experiment for the Shapley signal, a resubmission would be competitive.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>