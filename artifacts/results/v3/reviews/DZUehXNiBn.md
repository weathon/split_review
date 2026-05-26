Now I have sufficient calibration. Let me compile the final review.

## Summary

The paper introduces VISTA, a modular framework for causal structure learning that decomposes the global problem into Markov Blanket subgraphs, aggregates them via a weighted voting mechanism with exponential confidence calibration, and enforces acyclicity via a Feedback Arc Set (FAS) heuristic. The framework is designed to be model-agnostic, parallelizable, and lightweight. The authors provide finite-sample error bounds and asymptotic consistency guarantees, and evaluate across 5 base learners on synthetic and real (Sachs) data, reporting improvements in F1 and runtime.

## Strengths

1. **Consistent F1 improvements via weighted voting across diverse base learners**: Tables 1 and 2 show that VISTA-WV improves F1 over standalone baselines for 5 different learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE) on both ER and scale-free graphs. For example, GOLEM F1 on ER5 improves from 0.35→0.60, DAG-GNN from 0.33→0.59. These gains are achieved with fixed hyperparameters (λ=0.5, t=0.7), avoiding cherry-picking.

2. **Substantial computational speedup via parallelizable design**: Table 3 reports 2–10× runtime reductions (e.g., NOTEARS at n=300 from 12,515s to 2,136s; GraN-DAG at n=300 from 25,205s to 2,336s). The gains stem from the lightweight O(|V|²) edge-level aggregation and full parallelism of the divide stage.

3. **Coverage guarantee for decomposition (Proposition 3.1)**: The proof that every true edge appears in at least one MB subgraph ensures no information loss in the decomposition step—a formal property absent in heuristic partitioning approaches.

4. **Interpretable hyperparameter control without retraining**: Figure 4 demonstrates smooth precision-recall trade-offs under varying λ, and since λ only affects the final aggregation step, sweeping it is retraining-free. Theorem 3.4 provides a principled feasible range for λ.

## Weaknesses

### Major

1. **Pipeline contradiction between text and Figure 3 (undermines reproducibility).** Section 3.1 explicitly states: *"In VISTA, cycles are first removed using GreedyFAS, after which edges with weights below a global threshold t are filtered out"* and provides a detailed rationale for this ordering. However, Figure 3's description says: *"The merged graph is filtered (if s < t, remove X→Y) and then GreedyFAS is applied to remove cycles"* — the reverse order. The pseudocode ("post_prune(G_merged)") is ambiguous. The text's rationale directly argues against the pipeline depicted in the paper's own central figure. A reader cannot determine which pipeline the paper actually proposes, implements, or evaluates. This is a basic soundness issue that must be resolved.

2. **Missing Markov Blanket solver robustness analysis (undermines the claimed model-agnostic generality).** The paper advertises that VISTA is "fully plug-and-play with respect to MB identification" and "places no restrictions on the choice of Markov Blanket identification algorithm." Yet the experimental evaluation uses a single MB estimator throughout, with no variation or ablation. Proposition 3.1 (coverage guarantee) assumes correct MBs, so the practical robustness of the method entirely depends on this upstream component. Since Figure 1 shows the MB solver achieves F1~0.9 across all graph sizes, it is unclear how VISTA would behave under a weaker MB solver. A framework paper claiming generality must demonstrate sensitivity to its modular choices.

### Minor

1. **Theoretical guarantees rest on an acknowledged violated assumption.** Theorems 3.2 and 3.5 assume independent votes across subgraphs, which the paper immediately acknowledges is violated because "subgraphs learned from the same dataset can induce correlations among votes." The bound is then described as "a qualitative guide." While the paper is transparent about this caveat, the abstract and introduction prominently advertise "finite-sample error bounds" and "asymptotic consistency" without this qualification, which overstates what is actually established.

2. **Framing of Naive Voting (NV) results is incomplete.** The paper states "The NV variant already lifts recall by pooling evidence" as a positive intermediate result. While NV does increase TPR (e.g., NOTEARS TPR 0.74→0.97), Tables 1 and 2 show this comes at a catastrophic cost in many cases: NOTEARS F1 drops from 0.76→0.23 on ER5, SHD surges from 209→3172. The narrative would be more balanced if it explicitly acknowledged that NV destroys precision and is unusable as a standalone aggregation strategy, rather than framing it primarily as a success that WV "builds on."

3. **Real-data (Sachs) results are more modest than the narrative suggests.** Table 4 shows that SHD improvements are minimal for several methods (GOLEM 16→16, SCORE 18→15, DAG-GNN 15→14), TPR drops for GraN-DAG (0.53→0.29) and SCORE (0.18→0.12). While FDR consistently decreases, the claim that VISTA "consistently reduces false discoveries and improves structural accuracy" overstates the combined evidence when structural accuracy (SHD) barely changes or TPR drops.

### Trivial

None.

## Nice-to-Haves

- An ablation comparing VISTA against simpler ensemble heuristics (e.g., majority voting of subgraphs, intersection, simple score averaging with thresholding) would help isolate the effect of the specific weighted voting mechanism.
- The exponential weighting term $1-e^{-\lambda m}$ is justified by analogy to Bayesian smoothing priors, but the paper does not test whether other monotonic functions of $m$ would perform similarly.
- A small experiment correlating per-edge performance with the number of subgraphs $m$ could help gauge how informative the theory is for the practical setting.

## Removed Points

*The following points from the harsh critic were considered but removed for the reasons stated:*

1. *"The paper should include comparison against simpler strategies such as running the base learner on the full data with bootstrapped edge confidence scoring"* — This is a reasonable suggestion but constitutes a Nice-to-Have rather than a core weakness, as the paper already includes the baseline comparison (standalone base learner) and state-of-the-art comparison (DCILP in Appendix F.2).

2. *"Theorem 3.4's λ interval depends on m, which varies per edge; a single global λ cannot satisfy the condition uniformly"* — The paper acknowledges this implicitly by adopting the relatively large admissible λ within the interval (end of Section 3.2, line 156). The empirical λ sweep (Figure 4) further demonstrates that a fixed λ works acceptably. This is a valid theoretical point but a Minor concern at most.

3. *"The justification for the exponential weighting term is hand-wavy"* — While the justification is indeed brief, this is a design choice whose impact is empirically evaluated via the λ sensitivity study. Most papers do not exhaustively justify every design decision when the empirical behavior is characterized.

4. *"The connection between the theorems and the practical choice of λ in experiments is unclear"* — The paper does state that λ=0.5 lies within the feasible range prescribed by Theorem 3.4, and the sensitivity study demonstrates the practical effect. This connection, while not fully formalized, is adequate for an empirical paper.

## Novel Insights

The harsh critic's observation that the pipeline contradiction (FAS vs threshold ordering) is not a minor typo but fundamentally undermines verifiability is a genuine insight. Also useful is the observation that the NV failure mode should be treated as evidence of fragility rather than as a positive intermediate step — this reframes how the paper's empirical story should be told.

## Suggestions

1. **Resolve the pipeline contradiction.** Pick a single, unambiguous order for FAS and filtering, and ensure the text, Figure 3, pseudocode, and implementation all agree. Given the text's explicit rationale for FAS→filtering, this is likely the intended pipeline and the figure should be corrected.

2. **Add MB solver robustness experiments.** Show VISTA's performance with the current MB estimator, an intentionally degraded MB estimator, and ideally an oracle MB. This is the single most impactful missing analysis for supporting the claimed model-agnostic generality.

3. **Reframe the Naive Voting discussion.** Acknowledge explicitly that NV destroys precision and is not usable on its own, then treat VISTA-WV as the actual proposal. This would make the empirical narrative more honest and clearer.

4. **Adjust the theoretical claims in the abstract/introduction** to reflect that the error bounds are derived under idealized independence assumptions and serve as qualitative guides rather than strict guarantees for the practical setting.

## Score and Decision

### Calibration details

**Anchors consulted (all rounds):**

**Round 1 — Topic bands:**
| Anchor path | Avg score | Query bucket | Comparison |
|---|---|---|---|
| JzFLBOFMZ2 | 3.20 | round1-topic-low | LLM-based CSL; rejected due to weak evaluation. Our paper has stronger empirical work. |
| AvXrppAS2o | 3.00 | round1-topic-low | Medical CSL; rejected due to strong assumptions and limited scope. Our paper addresses a different (arguably broader) problem. |
| DUfwD5yiN4 | 5.25 | round1-topic-mid | Exact distributed structure-learning; rejected despite novel theory. Limited experiments (PC only). Our paper has more thorough experiments but its own issues (pipeline contradiction). |
| Lxst78Rrwj | 5.00 | round1-topic-mid | Invariance-based causal discovery; rejected due to fundamental concern about the invariance test. Comparable evaluation breadth. |
| iaP7yHRq1l | 5.50 | round1-weakness | Robustness benchmark; accepted. Comprehensive but had standardization issues. Our paper has a novel method rather than a benchmark. |

**Round 2 — Narrowing:**
| Anchor path | Avg score | Query bucket | Comparison |
|---|---|---|---|
| 2pEqXce0um | 4.50 | round2 | Root cause analysis; rejected. Strong assumption (single root cause). Our paper is methodologically more solid. |
| WqovbCMrOp | 5.80 | round2 | Temporal aggregation in causal discovery; rejected. Different topic. |
| 9UGAUQjibp | 5.80 | round2 | Quantized local independence for RL; rejected. Different topic. |

**Round-1 bracket:** 3.5–5.5. The low-band anchors (~3) were rejected for much weaker empirical evaluation or fundamental methodological flaws that our paper does not share. The mid-band anchors (5.0–5.25) share with our paper the pattern of a novel method with real but addressable weaknesses. **What the low-band anchors failed at:** LLM-based methods with no rigorous evaluation, or papers with very limited experiments and unclear methodology. Our paper does not share those failures — it has rigorous experiments and a clearly described method (setting aside the pipeline contradiction).

**Final score determination:** The paper is stronger than the ~3-range low-band anchors but has two Major weaknesses (pipeline contradiction, missing MB ablation) that place it below papers like DUfwD5yiN4 (5.25) which, despite fewer baselines, had no internal contradiction. The paper is comparable to Lxst78Rrwj (5.00, rejected) — both have novel frameworks with issues that require substantial revision. The combination of two Major weaknesses that respectively undermine reproducibility and a core generality claim justify a score at the lower end of the comparable range.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**