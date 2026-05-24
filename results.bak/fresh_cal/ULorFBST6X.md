Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces the Fair Submodular Cover (FSC) problem, combining submodular cover with proportional group fairness constraints. The authors develop a conversion framework that turns bicriteria approximation algorithms for Fair Submodular Maximization (FSM) into bicriteria algorithms for FSC, and design new discrete and continuous FSM algorithms to plug into this framework. The key theoretical result is a continuous algorithm that achieves a bicriteria ratio matching the best-known guarantee for submodular cover without fairness.

## Strengths

1. **First formulation of Fair Submodular Cover (FSC).** The paper is the first to formally define and study the FSC problem, combining submodular cover with proportional fairness constraints (Section 1, Eq. 1). This addresses a clear gap in the literature, where prior fair submodular work only considered maximization.

2. **Conversion framework from FSM to FSC (Algorithm 1, Theorem 1).** The paper develops a principled conversion that turns any bicriteria FSM algorithm into a bicriteria FSC algorithm via iterative guessing of |OPT|, extending prior non-fair conversion results (Iyer & Bilmes 2013) to the fairness setting. This is the paper's core algorithmic idea and enables reuse of FSM algorithms for the cover problem.

3. **Continuous algorithm matching best-known guarantee without fairness (Theorem 3).** The continuous algorithm (contialg) claims a (1−7ε, ln(1/ε)+1)-bicriteria ratio for FSM, which—via the conversion—yields an FSC guarantee matching the best-known submodular cover result without fairness constraints. This suggests that fairness need not degrade the asymptotic approximation rate.

## Weaknesses

### Fatal
None.

### Major

1. **Fairness guarantee gap in the conversion algorithm.** The paper's bicriteria definition for FSC (line 39) requires exact fairness: p_c|X| ≤ |X∩U_c| ≤ q_c|X|. However, the rounding procedure in Algorithm 1 (convert-fair) only guarantees |S∩U_c| ∈ [β⌊p_cκ⌋, β⌈q_cκ⌉] for a final solution of size |S| = βκ. Since β⌊p_cκ⌋ can be up to β less than p_c·βκ, and β⌈q_cκ⌉ can be up to β more than q_c·βκ, the fairness constraints can be violated by an additive factor of up to β elements. For the discrete algorithms (β = 1/ε), this additive slack is large. The paper does not address this gap or adjust the definition to allow additive slack. This does not invalidate the conversion framework conceptually, but the guarantees of Theorem 1 as stated are not fully supported. A fix would require either (a) relaxing the bicriteria definition to allow additive O(β) fairness error, or (b) redesigning the rounding step.

2. **Experiments severely limited and partially misrepresented.** (a) The abstract and introduction (line 48) claim experiments on "fair image summarization," but no such experiments appear in Section 5—only maximum coverage on the Twitch dataset is presented. (b) Only one dataset (Twitch, 5000 nodes) and one submodular function (max coverage) are tested. (c) No fairness parameters (p_c, q_c) are reported, making it impossible to assess whether the constraints are meaningful or whether the algorithms actually satisfy them. (d) The only baseline is the standard greedy (which ignores fairness); a natural fair baseline (e.g., greedy constrained to maintain fairness during selection) is missing. These gaps significantly weaken the empirical claims.

### Minor

3. **No pseudocode for the discrete FSM algorithms.** The continuous algorithm (contialg) has full pseudocode (Algorithms 2, 3), but greedy-fairness-bi and threshold-fairness-bi are only described textually. Given the theoretical complexity of the β-extension and exchange Lemma 2, pseudocode would aid reproducibility.

4. **Fairness parameters p_c, q_c not specified in experiments.** Without these values, the reader cannot verify whether the algorithms' output satisfies the formal fairness definition from Section 1, or assess the difficulty of the fairness constraints used.

5. **No error bars or statistical variation in experimental results.** The figures (Figure 2, cost, f-value, fairness difference) show single runs without error bars, confidence intervals, or replication. While single-run evaluation is common in submodular optimization benchmarks, at minimum the sensitivity of the fairness difference metric to randomness in the algorithms should be quantified.

6. **Continuous algorithm not evaluated experimentally.** The continuous algorithm (contialg) has the best theoretical guarantee, but only the discrete algorithms are tested. An experimental comparison would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- A more natural fair baseline (e.g., greedy with feasibility checks against the fairness matroid) would help demonstrate that the bicriteria approach is needed.
- Sensitivity analysis with respect to ε (theoretically, cost grows as 1/ε and f approaches 1−O(ε)) would validate the theoretical predictions.
- The complex expression in Theorem 2 (for the continuous conversion) could be simplified or bounded by a cleaner quantity to aid intuition.

## Removed Points

- **"FSM bicriteria guarantees unsubstantiated"** — The theorems are stated as restatable environments, meaning their proofs are in the appendix. The parser strips appendices. The paper does provide the key Lemma 2 (exchange property for β-extension) to support these results. Remove per rule about missing appendix content.
- **"Assumption justification unclear"** — The paper (lines 156–157) explains this assumption: it requires enough elements per group to run the FSM subroutine. This is reasonable and scoped.
- **"Missing related works"** — Cannot verify existence of missing citations without external knowledge; remove per instructions.
- **"Typos, formatting"** — Parser artifacts, not author errors.
- **"Pure formatting/style nitpicks"** — Removed per instructions.

## Novel Insights

The most interesting observation from the reviews is the structural tension in the conversion framework: ensuring exact proportional fairness in the cover solution while using the β-extension (which relaxes constraints by a factor of β) requires more careful rounding than the paper provides. This gap—that the FSM subroutine's β-extended feasibility guarantees do not translate to exact proportional fairness in the final FSC solution—is a subtle but real issue that future work on fair submodular cover should address. The core idea of leveraging the dual relationship between FSM and FSC via β-extensions is otherwise sound and could be repaired with a fairness-aware rounding scheme or a bicriteria definition that explicitly accommodates additive slack.

## Suggestions

1. Fix the fairness guarantee gap. The simplest path is to add a small additive term to the bicriteria definition (e.g., allow p_c|X| − δ ≤ |X∩U_c| ≤ q_c|X| + δ with δ ≤ β) and adjust theorems accordingly.
2. Remove the claim about image summarization experiments, or add them before publication.
3. Report the specific p_c, q_c values used in the experiments and show a table of per-group solution counts vs. allowed bounds.
4. Add pseudocode for greedy-fairness-bi and threshold-fairness-bi.
5. Add at least one more submodular function (e.g., facility location on a small dataset) to broaden the evaluation.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>