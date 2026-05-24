Now I have sufficient calibration data. Let me synthesize the final review.

**Calibration Summary:**

| Anchor | Avg Score | Round | Comparison to VISTA |
|--------|-----------|-------|---------------------|
| DUfwD5yiN4 (Distributed BN Structure Learning) | 5.25 | R1 | Most topically similar. Similar decomposition approach but narrower experiments. VISTA is comparable — broader empirical but similar theoretical gaps. |
| 2pEqXce0um (Root Cause Analysis) | 4.50 | R1 | VISTA is clearly stronger — more original, broader scope, better empirical evaluation. |
| Lxst78Rrwj (Invariance-based Causal Discovery) | 5.00 | R2 | Comparable quality. Has a fundamental theoretical gap (downsampling proxy lacks guarantees). VISTA's issues are less fundamental but similar severity overall. |
| fGhr39bqZa (Homologous Surrogates) | 6.00 | R1 | Cleaner theoretical contribution. VISTA is below this — lacks comparable theoretical depth. |
| xByvdb3DCm (Selection + Interventions) | 8.00 | R1 | VISTA is significantly below this — this is a top-tier theoretical contribution. |

**Round 1 bracket**: 4.5–6.5. VISTA is better than 4.5 anchors (RCA paper), weaker than 6.0+ anchors (homologous surrogates, selection+intervention).

**Round 2 narrowing**: The most comparable anchor is DUfwD5yiN4 at 5.25 (similar distributed structure learning approach) and Lxst78Rrwj at 5.00 (similar empirical breadth with a theoretical gap). VISTA has broader empirical evaluation than both but comparable theoretical issues. **Final score: 5.0.**

---

## Summary

VISTA is a modular, model-agnostic framework for large-scale causal discovery that decomposes global DAG learning into Markov blanket (MB) neighborhoods, applies any off-the-shelf base learner to each local subgraph, and reconciles the results via a lightweight weighted voting mechanism followed by GreedyFAS-based acyclicity enforcement. The framework is designed to be plug-and-play with respect to both MB identification and base learners, requires no solver or retraining during aggregation, and supports parallel execution across subgraphs. The paper provides finite-sample error bounds (Theorem 3.4) and an asymptotic consistency result (Theorem 3.5) for the weighted voting scheme, and evaluates VISTA across five diverse base learners, two graph families, and node counts up to 300, demonstrating consistent improvements in FDR, SHD, and runtime.

## Strengths

- **Solid coverage guarantee (Proposition 3.1):** The proof that the union of all MB-induced subgraphs contains every true edge of the original DAG is correct and provides an essential foundation for the divide-and-conquer strategy. No true causal edge can be lost in the decomposition.

- **Broad, convincing empirical evaluation:** The paper tests VISTA across five diverse base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE) spanning linear, nonlinear, differentiable, and combinatorial methods, on both Erdős–Rényi and scale-free graphs with up to 300 nodes. VISTA-WV consistently reduces FDR (often by 50–80% relative to standalone baselines) while maintaining reasonable TPR, and does so with a single fixed hyperparameter setting (λ=0.5, t=0.7) across all experiments — no per-dataset tuning. The runtime improvements are substantial (e.g., NOTEARS on n=300 drops from ~12,500s to ~2,100s).

- **Lightweight, retraining-free aggregation:** The weighted voting uses only edge counts and a one-time O(|V|²) scoring step. The hyperparameter λ can be swept without recomputing local graphs, making the precision–recall trade-off analysis practically effortless. This is a genuine practical advantage over solver-based merging approaches like DCILP.

- **Model-agnostic design:** VISTA imposes no assumptions on base learner internals, identifiability conditions, or data distribution, and the empirical results confirm that improvements transfer across very different base learners (from NOTEARS to SCORE to GraN-DAG). This plug-and-play property is well demonstrated.

- **Empirical λ sensitivity curves align with theory:** The precision–recall curves for varying λ (Figure 4) show the smooth, monotonic trade-off predicted by Theorem 3.4, with plateaus at extreme λ values — confirming that the theoretical analysis, despite its simplifying assumptions, captures the qualitative behavior.

## Weaknesses

### Fatal
None. The core idea is sound, the empirical results largely support the claims, and no single verifiable error invalidates the paper.

### Major

- **Pipeline ordering contradiction between text and figure:** The main text (Acyclicity Guarantee paragraph, line 118) states that "cycles are first removed using GreedyFAS, after which edges with weights below a global threshold t are filtered out." The Figure 3 caption (line 122) states the opposite: "The merged graph is filtered (if s < t, remove X→Y) and then GreedyFAS is applied to remove cycles." The pseudocode in Figure 2 is ambiguous (WV incorporates t, then post_prune is applied separately). This makes it impossible for a reader to determine the actual algorithm pipeline from the text alone. The paper does provide a rationale for one ordering (GreedyFAS-first), which suggests the figure caption is the error, but the contradiction must be resolved for the method to be well-defined.

- **Asymptotic consistency theorem premise is not satisfied by VISTA:** Theorem 3.5 requires the number of local subgraphs per candidate edge to satisfy m = C log n. In VISTA, a true edge (X→Y) appears only in the subgraphs centered at X and Y (and possibly a few others whose MBs contain both endpoints), making m bounded by a small constant determined by graph density — it does not grow with n. The paper presents this result as a key theoretical contribution supporting VISTA ("Theorem 3.5 establishes that weighted voting is asymptotically consistent... Notably, the required number of independent subgraphs per edge grows only logarithmically with the graph size"), but the premise is not guaranteed by the VISTA framework. This significantly weakens the theoretical contribution as presented.

### Minor

- **MB identification method not specified:** The paper emphasizes that VISTA is agnostic to the MB estimator, but never states which specific MB algorithm was used in the experiments. This is a gap for reproducibility. The paper mentions implementing "the MB solver used in that work" in reference to DCILP (line 178), but the algorithm name is not given in the main text.

- **Independence assumption in theoretical analysis:** Theorem 3.2 and all subsequent results model votes from different subgraphs as independent Bernoulli trials. The paper acknowledges this as "an idealized assumption" and that the bound should be interpreted as "a qualitative guide." While the λ sensitivity curves (Figure 4) do align qualitatively with the theory, the theoretical claims carry less weight than if dependence were modeled — a limitation the paper is transparent about but that readers should note.

- **No sensitivity analysis for MB estimation errors:** The entire decomposition relies on accurate MB identification, yet there is no ablation or sensitivity study showing how MB errors propagate to the final graph. Figure 1 shows MB F1 is high and stable, but this is a single MB estimator; robustness under varying MB quality is not demonstrated.

- **Runtime measurement details unclear:** Table 3 reports "total computing time" but does not specify whether these are wall-clock times under parallel execution or the sum of sub-problem times, nor the parallelization setup (number of workers, etc.). This matters for the scalability claim.

### Trivial

- The DCILP comparison is deferred to Appendix F.2. While referenced in the main text, placing even a summary result in the main experimental section would strengthen the positioning relative to the most directly comparable prior work.

## Nice-to-Haves

- A study of how errors in Markov blanket identification affect downstream graph recovery would strengthen the empirical argument considerably, even if only via synthetic MB perturbation.
- Clarifying the runtime measurement methodology (wall-clock vs. sum of times, parallelization setup) would make the scalability claim more concrete.
- Including a larger real-world or semi-synthetic benchmark beyond the small (n=11) Sachs network would better support the large-scale discovery claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim that the pipeline contradiction is "fatal" and makes the method "undefined":** The contradiction is real and must be fixed, but the paper provides a clear rationale for one ordering (GreedyFAS before threshold), and the algorithm is implementable — the error is in the figure caption, not a conceptual void. Demoted from fatal to major.

- **Harsh Critic claim that "the asymptotic consistency guarantee does not follow" and "makes the theoretical contribution unsound":** The theorem is mathematically correct as a conditional statement (if m = C log n, then consistency). The issue is that VISTA doesn't guarantee the premise, making the result less relevant to the framework than claimed. The finite-sample bounds (Theorem 3.4) remain valid and useful. Demoted from fatal to major.

- **Strength Finder claim that "Theoretical error control and asymptotic consistency... provide rigorous conditions":** The asymptotic consistency is weakened by the premise gap (see Major weakness above). The finite-sample bounds do provide theoretical grounding but under independence assumptions. The strength is real but qualified.

- **Harsh Critic claim that "No comparison to DCILP in main experimental section":** The paper explicitly references the comparison in Appendix F.2. Since the appendix is stripped by the parser, this content exists but is not visible to us. Not a real omission.

- **Harsh Critic claim about hyperparameter selection lacking justification:** The paper uses λ=0.5, t=0.7 across all experiments and states this explicitly. The λ sweep curves (Figure 4) show the chosen values lie in a reasonable operating region. The fixed-operating-point design is a deliberate choice to avoid cherry-picking and is clearly communicated.

- **Harsh Critic criticism about "Gran-DAG not being turned into a strong one":** This is an observation about base learner quality, not a weakness of VISTA. VISTA improves Gran-DAG meaningfully (FDR drops from 0.92 to 0.43 on ER5), which is the relevant metric.

- **Strength Finder's generic strengths:** "The weighted voting uses only edge counts" and "Stable performance with fixed hyperparameters" are accurate but are supporting features rather than core strengths. They've been integrated into the main strengths where appropriate.

## Novel Insights

The paper's observation that MB identification accuracy remains stable as graph size increases while base learner accuracy degrades sharply (Figure 1) is a genuinely useful empirical insight that motivates the divide-and-conquer approach beyond mere computational convenience — it suggests that decomposition may provide robustness even when individual learners fail at scale. The inverse relationship between this stability gap and VISTA's improvement margin warrants further investigation.

## Suggestions

- Resolve the pipeline ordering contradiction: either correct the Figure 3 caption to match the text (GreedyFAS before threshold) or update the text. Cite the specific line in the rebuttal.
- Qualify Theorem 3.5 explicitly: state that m = C log n is a sufficient condition and acknowledge that in VISTA, m is graph-structure-dependent and typically constant rather than growing with n. Consider reframing the asymptotic analysis around sample size per subgraph rather than graph size.
- State the MB algorithm used in experiments (e.g., IAMB, PCMB, or the method from DCILP) to enable reproduction.
- Clarify whether Table 3 times are wall-clock or sum-of-subproblem times, and note the parallelization setup.

## Score and Decision

The paper presents a practical, well-engineered framework with broad empirical validation. The core idea — decomposing causal discovery into MB neighborhoods and reconciling via calibrated weighted voting — is sound and demonstrably effective. However, the theoretical contribution is weakened by a contradiction in the algorithm specification (text vs. figure) and by presenting an asymptotic consistency result whose premise is not satisfied by the framework. These issues are significant enough to weigh against acceptance but are addressable. Compared to calibration anchors, VISTA is most similar to DUfwD5yiN4 (distributed BN structure learning, 5.25) — comparable theoretical gaps but stronger empirical breadth — and sits above Lxst78Rrwj (invariance-based causal discovery, 5.00).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>