## Summary
The paper diagnoses three failure modes of existing static-pretraining Supervised Causal Learning (SCL) — fragility to distribution shifts, failure of compositional generalization, and the synthetic-to-real gap — and proposes TTT-SCL, a test-time training framework that dynamically synthesizes a per-test-instance training set aligned to the test data. The concrete instantiation, TACTIC, performs stochastic graph refinement under a likelihood-based Alignment-of-Distribution (AD) score with an L0 sparsity penalty, regresses mechanisms with SIM, and trains a fresh SCL model on the resulting synthetic instances. On Sachs and SynTREn, TACTIC (Notears) reports substantial AUROC gains over AVICI (scm-v0) and traditional baselines.

## Strengths
- The §3 diagnostic study decomposes the SCL failure modes along graph/mechanism/noise axes and adds a component-mixed condition (Fig. 2, Table 1). This is concrete, well-controlled, and motivates the framework cleanly.
- The sparsity ablation (Table 3) is the right experiment for a likelihood+L0 score: removing the sparsity penalty consistently and substantially degrades AUROC (e.g., 83.0 → 69.7 on Chebyshev_G; 78.9 → 63.5 on Sachs), corroborating the design choice.
- The stage-wise analysis (Table 4) directly addresses the most natural objection — that TACTIC is just dressed-up score-based search — by reporting seed → highest-score → final SCL outputs. Whether or not the explanation is satisfying, presenting this decomposition is exactly the right scientific move.
- Real-world / pseudo-real results on Sachs (78.9) and SynTReN (80.1) are clearly above the strongest reported SCL and traditional baselines, which is the relevant regime if the paper's central claim about test-time alignment is true.

## Weaknesses

### Fatal
None.

### Major
- **The "learning improvement" stage is unexplained mechanistically (Table 4).** On Sachs, the highest-scoring searched graph has AUROC 66.6, yet the SCL model trained on a set of such graphs reaches 78.9. A supervised learner trained on labels of quality ~66.6 AUROC should not, in general, exceed that label quality without an articulated mechanism (ensembling, denoising, identifiability under the function class in SIM, etc.). The paper observes this jump but offers no theoretical or empirical account that distinguishes a genuine effect from test-adaptive overfitting / leakage through SIM-fitted mechanisms tuned on D_test. This matters because §4.4 explicitly frames this learning step as the "fundamental distinction" of TACTIC over score-based discovery.
- **AD is fit and evaluated on the same D_test.** Eq. (3) regresses f_i^k from D_test under parents in G_train^k, then scores log p(X_i | f_i^k) on the same D_test. The paper acknowledges (§4.1) that this collapses to dense graphs and patches it with an L0 penalty, but never describes how λ is chosen per dataset, nor whether the SIM regressor class is held fixed. With AD/λ/SIM all driven by D_test and only one real-world graph reported per dataset, the pipeline is structurally vulnerable to test-set adaptive tuning that ordinary SCL benchmarks won't catch.
- **Real-world results lack any uncertainty quantification.** Sachs and SynTReN are reported as single AUROC numbers, while synthetic settings carry std. The central "Issue 3" claim and the headline gap over AVICI on Sachs (62.3 → 78.9) hinge on two unreplicated points. Given Sachs has only 11 nodes (≤110 ordered pairs), AUROC can move several points from edge-probability noise alone; multi-seed variance over initial DAGs and λ values is essential to support the real-world claim.

### Minor
- **Sampler specification is inconsistent.** Fig. 3 gives the transition probability as min[1, score(G_{k+1})/score(G_k)], but score(G) = AD − λ·Sparsity in Eq. (5) is not constrained to be positive (log-likelihoods can easily be negative), so a score *ratio* is not a valid MH acceptance probability. This is likely a notation error rather than a bug, but the sampler as written is under-specified — readers cannot tell whether acceptance uses score differences, exp(score) ratios, or temperature.
- **Ablation is narrow.** Only the sparsity term is ablated. The paper does not vary λ, K=200, the SIM regressor class, the noise distribution (defaulted to N(0,1), a substantive choice not defended), or the seed-DAG algorithm beyond random vs. NOTEARS.
- **Headline framing slightly overstates the result.** The abstract / §1 says TACTIC "significantly outperforms" existing SCL, but on RFF_G AVICI (scm-v0) is clearly better (97.8 vs. 91.8). A more accurate framing is "competitive in-distribution, stronger under shift and on real-world data."
- **Compositional-generalization conclusion rests on one training-scale regime.** §3 labels compositional failure as "fundamental," but Fig. 2 trains AVICI under each setting from scratch without scaling experiments. The phenomenon is plausibly real, but the categorical framing exceeds the evidence provided.
- **AD's identifiability footing is left implicit.** §4 gestures at LiNGAM/ANM/PNL, but AD is a generic regressed-likelihood score whose validity depends on the SIM regressor class matching one of those function-class/noise-class assumptions. A clear statement of which assumption AD relies on, and whether SIM respects it, would strengthen the methodological claim.

### Trivial
None substantive.

## Nice-to-Haves
- A "search-only" baseline matched to TACTIC's compute budget (e.g., GES / NOTEARS+L0 with the same number of proposals) to isolate the contribution of the SCL training step beyond what Table 4's "highest-score graph" already shows.
- A sensitivity sweep over λ and over the SIM regressor (linear / GP / MLP) to rule out test-adaptive tuning.
- A visualization of the K=200 refined graphs' edit distance to G_test, AD, and sparsity, to show whether the search produces a coherent neighborhood vs. a noisy ensemble — this would help explain the 2→3 improvement.
- Wall-clock / compute comparison vs. AVICI, since TTT-SCL trains a fresh SCL model per test instance.

## Removed Points
These points are flagged to be removed; treat them with caution.
- "Missing comparison to score-based search methods like GES/NOTEARS+L0 under matched compute" framed as a fatal issue — partially addressed by Table 4's stage-wise analysis, which already reports the highest-scoring searched graph. The deeper request is reasonable as a nice-to-have, not as a structural flaw.
- "i.i.d baseline reaches 100 AUROC, suggesting trivial settings or leakage" — speculative; d=10 is small and AVICI is a strong in-distribution learner. Not strong enough evidence of label leakage to keep as a weakness.
- Any concern rooted in doubting AVICI (scm-v0), SynTReN, or other cited artifacts exists — they do.

## Novel Insights
None beyond the paper's own contributions. The cleanest conceptual contribution is reframing SCL training-set design as test-time data synthesis driven by a distributional-alignment score, which is genuinely interesting; the rest of the review identifies things to verify rather than independent insights.

## Suggestions
- Report multi-seed mean ± std on Sachs and SynTReN over ≥10 runs varying random init, λ, and SIM regressor.
- Specify the sampler precisely: write the acceptance rule in terms of score *differences* (e.g., min[1, exp((score(G_{k+1}) − score(G_k))/T)]) and give T or any annealing schedule.
- Add an explicit statement of which identifiability assumption AD presumes and verify that SIM's regressor class matches it.
- Add a λ-sensitivity figure and a SIM-regressor ablation; both are cheap relative to the central claim's importance.
- Soften abstract/intro to acknowledge the RFF_G in-distribution gap with AVICI.
- Provide an argument (theoretical sketch or controlled simulation) for why the SCL stage can exceed the label quality of the training graphs.

---

**Calibration anchors (full batch):**
- `ZXs3pkmrRG.md` (avg 5.50, Reject) — *Test-Time Learning of Causal Structure from Interventional Data (TICL)*: closest topical match — also a TTT-style SCL framework that self-augments training data from D_test; reviewers liked the idea but flagged framing, baseline fairness, and applicability. Very similar profile to the paper under review.
- `lQYi2zeDyh.md` (avg 5.00, Reject) — *Demystifying amortized causal discovery with transformers*: analyzes CSIvA, raises identifiability concerns about supervised causal learning trained on synthetic data; relevant because it formalizes the exact concern this paper's AD score implicitly inherits.
- `WhvTLognS0.md` (avg 5.00, Reject) — *Learning Task Relations for Test-Time Training*: general TTT paper; less topical but anchors the "test-time training is interesting but execution under-specified" band.
- `qT0IWGqo1j.md` (avg 4.25, Reject) — *Training on test proteins improves prediction*: TTT in a different domain; weakly similar.
- `iaP7yHRq1l.md` (avg 5.50, Accept) — *Robustness of differentiable causal discovery in misspecified scenarios*: empirical benchmark study; provides a "useful but limited" anchor on the borderline.
- `HBf6HFnpmH.md` (avg 5.50, Reject) — *Scalability of causal models*: benchmarks paper, borderline.
- `wmV4cIbgl6.md` (avg 7.33, Accept) — *CausalRivers benchmark*: high-anchor; this is a clearer/more polished contribution with a real-world benchmark, decisively above the paper under review.
- `pAoqRlTBtY.md` (avg 6.25, Accept) — *Causal Modelling Agents*: LLM+DSCM hybrid, well-presented; moderately above the paper under review.
- `zwMfg9PfPs.md` (avg 6.75, Accept) — *Out-of-Variable Generalisation*: theoretical contribution, cleanly executed; above the paper under review on rigor.
- `7f5hNhzVAe.md` (avg 4.00, Reject) — *Causal Invariant BNNs*: weaker execution; below the paper under review.
- `22ywev7zMt.md` (avg 5.67, Reject) — *OOD generalization of SSL*: borderline.
- `Wgb8tuu5BI.md` (avg 3.67, Reject), `S1U0CIuejF.md` (avg 4.00, Reject), `cbFqqtJGtA.md` (avg 4.25, Reject) — low-band causal-discovery anchors; the paper under review is clearly above these on motivation and experimental scope.
- `fSxiromxAq.md` (avg 3.00, Reject), `AvXrppAS2o.md` (avg 3.00, Reject), `zgM66fu0wv.md` (avg 2.50, Reject) — very weak causal-discovery papers; the paper under review is decisively above these.

The paper sits closest to TICL (5.50) and Demystifying (5.00): a creative reframing of SCL with concrete experimental support, but with under-explained mechanism (the 2→3 jump in Table 4), AD/D_test in-sample concerns, a sampler notation issue, and single-number real-world results. Slightly below the better-executed TICL because TACTIC's headline real-world claim leans on two unreplicated points and the central "learning improvement" stage is observed rather than explained.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>