Now let me run the calibration searches to score the paper.Now I have sufficient information to write the final meta-review.

---

## Summary

VISTA (Voting-based Integration of Subgraph Topologies for Acyclicity) is a model-agnostic modular framework for causal structure learning that decomposes global DAG learning into Markov Blanket subgraph problems, aggregates local results via a weighted exponential voting mechanism, and enforces acyclicity via a Feedback Arc Set post-processing step. The framework is evaluated against six base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, and CAM-like setups) on ER and scale-free synthetic graphs, as well as the Sachs real-world benchmark, demonstrating consistent FDR reduction and runtime improvement over standalone base learners.

---

## Strengths

- **Model-agnostic empirical consistency across diverse base learners.** Tables 1 and 2 show that VISTA-WV reliably reduces FDR by 50–80% relative to standalone baselines while keeping TPR ≥ 0.68 across linear (NOTEARS, GOLEM, DAG-GNN) and nonlinear (GraN-DAG, SCORE) learners on both ER and scale-free graph families. The consistency of gain across estimators directly supports the plug-and-play claim.

- **Significant runtime improvements from the divide-and-conquer design.** Table 3 quantitatively documents large runtime reductions: e.g., NOTEARS runtime drops from 12,515 s to 2,137 s at n=300, and DAG-GNN from 17,714 s to 1,960 s. These are not artifact-specific; they are a structural consequence of the local subgraph decomposition and demonstrated across all tested learners.

- **Principled sensitivity analysis of the weighting parameter λ.** Figure 4 shows smooth monotonic precision–recall trade-offs as λ varies, consistent with the prediction of Theorem 3.4 that larger λ relaxes the penalty on low-support edges. This confirms interpretability of the parameter and practical tunability.

- **Finite-sample error bound and asymptotic consistency result.** Theorem 3.2 provides an explicit sample-complexity bound for edge-level correct orientation; Theorem 3.5 establishes O(log n) subgraph coverage sufficient for asymptotic consistency. The theoretical framework, while idealized (see weaknesses), provides a concrete justification for the voting mechanism beyond pure heuristics.

---

## Weaknesses

### Fatal
None.

### Major

- **The central theoretical guarantees apply to an idealized algorithm that explicitly differs from VISTA as implemented.** Theorems 3.2 and 3.5 both assume that votes from different local subgraphs are *independent*. The paper itself acknowledges (Section 3.1, end of paragraph on Theorem 3.2): *"Theorem 3.2 is stated under an idealized assumption that the votes from different local subgraphs are independent. In practice, subgraphs learned from the same dataset can induce correlations among votes, so the bound should be interpreted as a qualitative guide."* Because VISTA's subgraphs are derived from overlapping Markov Blanket neighborhoods of the same dataset, this independence assumption is structurally violated: any edge covered by multiple overlapping MBs receives correlated votes. The paper acknowledges this but offers no partial mitigation — no bounding of the correlation under sparsity assumptions, no comparison of the idealized vs. actual coverage structure. This means Theorem 3.5's consistency guarantee strictly speaking proves consistency for an oracle ensemble of independent learners, not for VISTA. This is a real theoretical gap, not a formality.

- **All experimental comparisons are internal (VISTA+X vs. X alone) — no absolute benchmark against purpose-built scalable competitors.** The paper's primary motivation is scalability in large-scale causal discovery, where base learners (NOTEARS, DAG-GNN) degrade. Yet every row in Tables 1–4 pairs a base learner against its VISTA-wrapped version. There is no comparison against purpose-built methods designed for that regime (e.g., PC-stable, GES, FGES). Without this, readers cannot assess whether VISTA+NOTEARS at n=300 is competitive in absolute terms with a dedicated constraint-based method. The claim of being useful for "large-scale" discovery is thus unverified beyond relative improvement over already-degraded baselines.

- **CAM is listed as a baseline in Section 4.1 but is absent from all result tables.** The experimental section (line 174) explicitly states: *"we benchmark VISTA against…CAM Bühlmann & Peters (2016)…for the linear setting."* Yet CAM appears in none of Tables 1–4. No explanation is offered. This unexplained omission of a named baseline is a significant reproducibility and transparency concern.

### Minor

- **The real-data evaluation on the Sachs network (11 nodes, 17 edges) is too small to validate scalability claims.** Table 4 results are reported as single runs (no standard deviations), making them unreliable for small networks where stochasticity matters. The improvements shown (e.g., GOLEM: SHD 16→16; SCORE: SHD 18→15) are mostly marginal at this scale. The dramatic GraN-DAG result (FDR: 0.82→0.00, SHD: 16→12) comes from a single unreplicated run and is therefore uninterpretable in isolation.

- **The practical hyperparameter choice λ=0.5 may lie outside the theoretical feasible interval of Theorem 3.4 for experimentally-realistic subgraph counts.** Theorem 3.4 prescribes the range $-\frac{1}{m}\ln(1-t) < \lambda \leq -\frac{1}{m}\ln\varepsilon$. With typical values (t=0.7, ε=0.05) and modest m (e.g., m≈10 for edges covered by few MBs in sparse graphs), the upper bound is approximately −(1/10)ln(0.05) ≈ 0.30, placing λ=0.5 outside the range. The paper asserts on line 205 that "this choice lies within (5)" without demonstrating this for the experiment-specific parameter values. The inconsistency should be resolved, either by showing m is consistently larger than assumed or by adjusting the example values.

- **VISTA-NV's dramatic inflation of SHD (208→3,171 for NOTEARS, Table 1) is framed as a feature ("NV lifts recall") rather than a problem.** While it is technically correct that NV raises TPR to 0.97, a practitioner would not use an output with SHD=3,171 as an intermediate step. The paper should be clearer that NV is presented only to motivate WV, not as a usable configuration.

### Trivial
None requiring attention beyond the above.

---

## Nice-to-Haves

- A comparison of VISTA+base against at least one dedicated scalable competitor (e.g., PC-stable or FGES) at n≥300 would substantially strengthen the absolute performance argument. Even a single such comparison would close the main evidential gap.

- A larger real-data benchmark (e.g., a gene regulatory network with 50–200 nodes commonly used in the literature) would lend the real-data section credibility commensurate with the synthetic claims.

- A partial theoretical treatment of vote correlation — even bounding the pairwise covariance under a max-degree sparsity assumption — would transform the current theoretical contribution from a qualitative guide into a genuine guarantee about VISTA's actual behavior.

- Proposition 3.1 is logically correct but is essentially a restatement of the Markov Blanket definition (that X→Y implies Y∈MB(X) and X∈MB(Y)). Presenting it as a foundational proposition overstates its analytical content; it could be integrated into the text as a coverage remark rather than elevated to a proposition.

- The runtime table (Table 3) does not separate MB identification time from local learning time. This breakdown matters because MB identification using IAMB or HITON-MB is itself nontrivial; including it would clarify whether the efficiency claim holds end-to-end.

---

## Removed Points

*These points were reviewed and removed. Treat with caution — they may reflect genuine concerns not warranting inclusion or reviewer misreadings.*

- **"VISTA-WV at λ=0.5 is cherry-picked."** Removed because the paper explicitly states (line 205) that λ=0.5 is fixed across all main table experiments and precision–recall curves are reported for transparency. No post-hoc selection is performed.

- **"Comparison with DCILP relegated to appendix."** Removed per hard rule against criticizing appendix-deferred content. The parser strips appendices; the full paper does include this comparison.

- **Proposition 3.1 is "a tautology contributing nothing."** Partially removed. Retained as a Trivial/Nice-to-Have note that it is better framed as a coverage remark than an elevated proposition, but the harsh characterization of "tautology" is demoted since it does serve to formally ground the framework.

- **"Latent confounding in subgraphs invalidates the coverage argument."** Removed as a fatal claim. Proposition 3.1 is about edge coverage, not orientation correctness under confounding. The paper does acknowledge the confounding issue in Section 5 as a limitation ("latent confounding introduced by restricting the learner to subsets may produce high-confidence redundant edges"). The paper's framing is honest and the concern is pre-addressed.

- **"GraN-DAG gains on Sachs are evidence of selective reporting."** Removed — there is no evidence of selective reporting; all base learners are reported in Table 4.

- **"Unfair comparison: VISTA wraps mediocre learners."** Removed per hard rule. Any asymmetry favors the baselines (standalone is already optimized; VISTA adds overhead and decomposition), making reported gains, if genuine, a stronger result.

- **Generic strengths from Strength Finder about "addressing an important problem."** Removed as insufficiently specific.

---

## Novel Insights

The paper's most actionable methodological contribution — which neither reviewer fully foregrounds — is that the weighted exponential confidence modulator $(1 - e^{-\lambda m})$ provides a retraining-free precision–recall operating curve: once votes are cached, sweeping λ recomputes the full curve in O(n²) time without re-running any base learner. This makes VISTA particularly attractive as a post-processing layer for expensive learners (SCORE takes over 10,000 s at n=100), where the aggregation cost is negligible compared to the learning cost. The theoretical independence gap limits the formal guarantees, but this practical reuse property is a genuine and underemphasized advantage.

---

## Suggestions

1. **Add one absolute comparison** (e.g., VISTA+NOTEARS vs. PC-stable at n=100 and n=300) to address the most significant evidential gap. This is the single highest-leverage addition.

2. **Explain the absence of CAM from all tables** or restore it. If CAM results were omitted because they were unfavorable, that should be stated.

3. **Scope the theoretical contribution honestly.** Either add a partial independence-relaxation result (e.g., bounding error for ρ-correlated votes), or explicitly state in the theory section that Theorems 3.2 and 3.5 are idealized guarantees that motivate VISTA rather than certify it. The current text partially does this but could be stronger.

4. **Report multi-run statistics on the Sachs benchmark** (at minimum 5 runs with mean ± std) to make the real-data section interpretable.

---

## Score and Decision

**Round 1 Bracket:** Based on the retrieved anchors and initial reading, the paper sits in the 4.5–6.5 range. It is clearly above the weak-anchor band (2.5–3.4) that featured incomplete, shallow, or LLM-augmentation-of-existing-methods papers. It is clearly below the strong-anchor band (≥8.0) of papers with clean theory and complete evaluation.

**Round 2 Narrowing:** The most relevant anchors at 4.5–6.5 are:
- *UAkVjK00Wv* (Auto-Ensemble BN Structure Learning, avg 4.75): D&D + ensemble aggregation, criticized for insufficient novelty and limited comparison. VISTA is more principled (explicit theory, wider base-learner coverage) and arguably more novel in aggregation design. VISTA is **better** than this anchor.
- *DUfwD5yiN4* (Exact Distributed BN Learning, avg 5.25): Exact D&D with theoretical guarantees, criticized for limited comparison (only vs PC) and scalability claims unverified. Almost identical structural profile to VISTA — both lack absolute competitor comparison and both have acknowledged theoretical idealizations. VISTA is **comparable**, with slight edge in empirical breadth.
- *mGmx41FTTy* (Two Time-Slices for DAG Ordering, avg 6.33): Clean theoretical story, good empirical support. Stronger theoretical grounding than VISTA; VISTA falls **below** this anchor.
- *iaP7yHRq1l* (Robustness of Differentiable Causal Discovery, avg 5.50, accepted): Extensive benchmark, accepted despite being more survey-like. VISTA has more algorithmic contribution but larger evaluation gaps.

**Positioning:** VISTA sits between DUfwD5yiN4 (5.25) and mGmx41FTTy (6.33). The missing absolute competitor comparison and unexplained CAM omission pull it closer to DUfwD5yiN4. The broader empirical coverage (6 learners, 4 graph sizes, runtime, sensitivity analysis) and the novel weighted-voting formulation pull it above UAkVjK00Wv. Score: **5.0**.

**All retrieved anchors summary:**

| Paper | Avg Score | Round | Comparison to VISTA |
|---|---|---|---|
| AvXrppAS2o (Causal + outcome prediction) | 3.00 | R1 | Much weaker — shallow contribution |
| JzFLBOFMZ2 (LLM-supervised CSL) | 3.20 | R1 | Weaker — LLM-augmented heuristic |
| Idygh9MX0N (Multi-agent causal discovery) | 3.40 | R1 | Weaker — mostly empirical, no theory |
| zgM66fu0wv (IRIS real-time causal) | 2.50 | R1 | Much weaker |
| DUfwD5yiN4 (Exact distributed BN learning) | 5.25 | R1+R2 | Closest comparable — similar gaps |
| Lxst78Rrwj (Distributional invariance causal) | 5.00 | R1+R2 | Comparable — single-method approach |
| 9UGAUQjibp (Quantized local independence, RL) | 5.80 | R1 | Slightly stronger — cleaner problem scope |
| mGmx41FTTy (Two time-slices DAG) | 6.33 | R1+R2 | Stronger — cleaner theory, cleaner story |
| UAkVjK00Wv (Auto-Ensemble BN learning) | 4.75 | R2 | Slightly weaker — less principled aggregation |
| iaP7yHRq1l (Robustness of differentiable CD) | 5.50 | R2 | Comparable, accepted |
| ZXs3pkmrRG (Test-time causal learning) | 5.50 | R2 | Comparable |
| xByvdb3DCm (Selection + intervention causal) | 8.00 | R1 | Much stronger |
| k38Th3x4d9 (Granger causal anomaly) | 8.00 | R1 | Much stronger |

**Final score: 5.0 — Reject.** The paper makes a genuine practical contribution (consistent, model-agnostic, retraining-free aggregation with runtime benefits), but the theoretical gap (unresolved independence assumption), the missing absolute competitor evaluation, and the unexplained CAM omission together prevent acceptance in the current form. The contributions are real but insufficiently validated.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>