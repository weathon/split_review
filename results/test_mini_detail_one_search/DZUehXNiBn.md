Now let me write the final consolidated review.

## Summary

VISTA is a modular divide-and-conquer framework for causal structure learning. It decomposes the global DAG learning problem into node-centered Markov Blanket subgraphs, applies any off-the-shelf base learner to each subgraph independently, then aggregates the local edge predictions via a weighted voting scheme (with exponential decay based on vote count) and enforces acyclicity through a Feedback Arc Set heuristic. The paper provides finite-sample error bounds and an asymptotic consistency theorem, and evaluates across six base learners on synthetic and one real dataset.

## Strengths

- **Model-agnostic modular design with broad empirical coverage.** VISTA is applied to six different base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, CAM) spanning both differentiable and combinatorial paradigms. Tables 1 and 2 show that the framework improves (or at least maintains) F1 for the majority of base learners across linear and nonlinear settings. This breadth is a genuine advantage over prior modular approaches that are tied to specific algorithm families.

- **Clean coverage guarantee (Proposition 3.1).** The proof that every true edge appears in the union of Markov Blanket subgraphs is simple and correct, establishing that the decomposition does not lose ground-truth edges. This provides a sound foundation for the downstream aggregation.

- **Substantial and consistent runtime reductions.** Table 3 shows that VISTA reduces wall-clock time substantially (e.g., NOTEARS from 1474 s to 340 s at n=100; DAG-GNN from 2193 s to 371 s; SCORE from >10 s to 225 s at n=300, where the baseline failed). The speedup directly follows from the divide-and-conquer design and is the paper's clearest practical contribution.

- **Fixed hyperparameters without per-dataset tuning.** The paper uses λ=0.5, t=0.7 across all experiments without dataset-specific selection. The sensitivity analysis (Figure 4) shows the precision-recall trade-off varies smoothly, supporting this as a reasonable default.

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical guarantees are undermined by the independence assumption, which the paper itself acknowledges cannot hold.** Theorems 3.2, 3.4, and 3.5 model votes from local subgraphs as independent Binomial trials. As the paper explicitly states (lines 142–143): "subgraphs learned from the same dataset can induce correlations among votes, so the bound should be interpreted as a qualitative guide." This is not a minor caveat — Markov Blanket subgraphs overlap substantially (each edge appears in subgraphs centered on both endpoints and possibly spouses), making the votes *structurally* dependent. The paper's theoretical contribution is therefore presented as formal guarantees but is conceded to be only a qualitative guide. This gap between presentation and actual provable content is significant.

2. **The asymptotic consistency condition (Theorem 3.5) cannot be satisfied by the framework.** Theorem 3.5 requires *m = C log n* independent subgraphs per candidate edge for consistency. However, in the VISTA framework, each edge appears only in the subgraphs of its endpoints and their spouses — at most *O(d²)* subgraphs for maximum degree *d*. For sparse graphs (where divide-and-conquer is most needed), *d* is constant, so *m* does not grow with *n*, and the *m = C log n* condition cannot be met. The asymptotic guarantee is thus stated under a premise that the method's own design does not satisfy.

3. **The Markov Blanket estimator used in experiments is not specified.** The paper calls `MB_solver(v)` (Figure 2) and states it is "agnostic to the choice of MB identification methods" (line 63), but never reveals which MB estimator was actually used to produce results in Tables 1–4 and Figure 1. Figure 1 claims MB identification maintains ~0.9 F1 across all graph sizes — without specifying the estimator, this claim is not reproducible. Since errors in MB estimation would cascade into the local subgraphs and final aggregation, this is a significant reproducibility gap that limits trust in the reported results for realistic (non-synthetic) settings.

### Minor

4. **Accuracy improvements are modest for several baselines and may not be statistically significant.** For NOTEARS on ER5 (Table 1), F1 rises from 0.76 ± 0.24 to 0.79 ± 0.02 — the standard deviations overlap heavily. For GraN-DAG, F1 goes from 0.06 to 0.17 (both near zero). On the Sachs dataset (Table 4), VISTA reduces TPR for most methods (GOLEM: 0.26→0.18; SCORE: 0.18→0.12; GraN-DAG: 0.53→0.29) while improving FDR and SHD marginally (1–3 units). The paper does not report statistical significance tests. The claim of "notable improvements" is overstated for some configurations.

5. **Real-data evaluation is limited to a single small dataset (Sachs, 11 nodes).** While Sachs is a common benchmark, the paper's main selling point is scalability to large graphs. Evaluating on at least one moderately sized real-world dataset (e.g., with 50–200 nodes) would substantially strengthen the claim that the divide-and-conquer advantage transfers to practical applications.

6. **Comparison to alternative modular frameworks is deferred to the appendix.** The paper mentions DCILP (Dong et al., 2024) as a related modular approach and states a comparison appears in Appendix F.2. Given that the paper's contribution is situated in the modular/divide-and-conquer paradigm, placing this comparison in the main paper would better situate the contribution. (The appendix is stripped from the review copy, so the comparison cannot be assessed.)

### Trivial

7. **Theorem 3.4's feasible λ interval depends on *m*, but *m* varies across edges.** The paper fixes λ=0.5 globally. Since different edges appear in different numbers of subgraphs, a single λ cannot simultaneously satisfy inequality (5) for all edges. This is a minor technical point since λ=0.5 appears to work empirically, but it means the "guarantee" of Theorem 3.4 is per-edge rather than global.

## Nice-to-Haves

- Evaluate with an imperfect (off-the-shelf) MB estimator (e.g., IAMB, Hiton-PC) and report sensitivity to MB quality. This would directly address the main practical concern about the method.
- Report the empirical distribution of *m* (votes per edge) to assess whether the asymptotic condition in Theorem 3.5 is approximately approached.
- Add a simple majority-voting ablation (without the exponential weight) to isolate the benefit of the *1 − e^(−λm)* term.
- Include statistical significance tests (e.g., paired bootstrap) for the key comparisons in Tables 1 and 4.

## Removed Points

- *"The theorems are standard concentration inequalities with low novelty"* — This is a subjective assessment of novelty, not a factual weakness. Many papers in causal discovery use standard concentration tools. Removed.
- *"Missing related work"* — Per policy, I cannot verify the existence of missing citations. Removed.
- *"No comparison to SADA/Cai et al. baselines"* — SADA is cited (lines referenced as "Cai et al., 2013; 2018") and described as limited to LiNGAM. The reviewer's demand for this comparison is scope creep — the paper's framework is model-agnostic; SADA is not. Removed.
- *"Formatting/style nitpicks"* — Removed per policy (parser artifacts).
- *"Reproducibility concerns about hyperparameters/implementation details"* — The paper provides code and a fixed hyperparameter setting; undisclosed trivial details are not a valid weakness. Removed.
- Strength Finder's claimed strength about "Careful ordering of cycle resolution and filtering" — This is a minor implementation detail, not a core strength. Removed.
- Strength Finder's claim about "Principled hyper-parameter selection with theoretical range" — While Theorem 3.4 provides a range, the fixed λ=0.5 cannot satisfy it for all edges simultaneously (noted in Weakness 7). The strength is overstated. Demoted.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely converge on the same set of issues (independence assumption, unspecified MB solver, modest empirical gains) and the same strengths (model-agnostic design, runtime reduction). The most noteworthy observation from merging the reviews is that the theoretical framework and the empirical validation are somewhat misaligned: the theory promises asymptotic guarantees under idealized independence, but the main empirical case for VISTA rests on its practical speed and model-agnostic flexibility, not on the formal guarantees.

## Suggestions

1. **Clarify what the theory actually provides.** Either add a dependence-aware analysis (e.g., using dependent Bernoulli concentration) or downgrade the theoretical claims to "heuristic guidance" throughout, removing the language of guarantees and asymptotic consistency.
2. **Specify the MB estimator used in all experiments** in the main text, and add a sensitivity analysis showing how MB accuracy affects downstream VISTA performance.
3. **Add at least one medium-scale real dataset** (e.g., gene regulatory network with 50–200 nodes) to substantiate the scalability claim on real data.
4. **Include a simple majority-voting baseline** (without the exponential weight) to isolate the benefit of the *1 − e^(−λm)* weighting term.
5. **Report the empirical distribution of vote counts *m* per edge** across the synthetic benchmarks, to show whether edges typically appear in enough subgraphs for the theoretical conditions to be even approximately relevant.

## Score and Decision

**Anchor comparison:**
| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| High (8.00) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xByvdb3DCm.md` | 8.00 | "When Selection meets Intervention" — accepted, strong novel theoretical framework, well-motivated, rigorous experiments. VISTA is substantially weaker on theory and evaluation depth. |
| High (8.00) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nx4PMtJ1ER.md` | 8.00 | "Signature Kernel CI Tests" — accepted, novel methodology with solid theory. VISTA is weaker. |
| Medium-High (7.00) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oCdIo9757e.md` | 7.00 | "Analytic DAG Constraints" — accepted, strong theoretical analysis with extensive experiments. VISTA's theory is shallower and the experimental validation less rigorous. |
| Medium (6.33) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mGmx41FTTy.md` | 6.33 | "Two Time-Slices Help Topological Ordering" — rejected but decent evaluation with clear theoretical framing. VISTA has broader base-learner coverage but weaker theoretical grounding. |
| Medium (5.25) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DUfwD5yiN4.md` | 5.25 | "Exact Distributed Structure-Learning" — rejected, similar topic with comparable issue (limited experiments relative to claims). VISTA has more extensive base-learner evaluation but similar theory-reality gap. |
| Medium (5.00) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Lxst78Rrwj.md` | 5.00 | "Causal Graph Learning via Distributional Invariance" — rejected, comparable quality level with some methodological gaps. |
| Low (3.20) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JzFLBOFMZ2.md` | 3.20 | "Causal Structure Learning Supervised by LLM" — rejected, weak theory, unclear contributions. VISTA is clearly stronger. |
| Low (3.00) | `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AvXrppAS2o.md` | 3.00 | "Outcome prediction using causal structure learning" — rejected, marginal improvements, weak baselines. VISTA is clearly stronger. |

Relative to the anchors, VISTA is stronger than the low-scoring papers (3.0–3.2) but weaker than the accepted papers (7.0–8.0) in both theoretical depth and experimental rigor. It is comparable to 5.0–6.3 papers but has unresolved gaps: the theory's core independence assumption is acknowledged as violated, the asymptotic condition is not satisfiable, and the MB solver is unspecified.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>