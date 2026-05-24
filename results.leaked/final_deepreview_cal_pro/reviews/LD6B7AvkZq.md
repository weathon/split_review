Now I have sufficient calibration. Let me synthesize my final review.

**Round 1 bracket:** The paper sits between the weak anchors (~3.0-3.25) and the strong anchors (7.6-8.0). Compared to the middle anchors, it's better than hNkXTqDrfb (3.75) but weaker than 0pLCDJVVRD (7.00), placing it roughly in the 4.5–6.5 range.

**Round 2 narrowing:** Compared to F0Zd3knG9j (5.00, rejected — similar PCFG/transformer study with limited novelty) our paper has a more novel theoretical framework but comparable execution quality. Compared to MO5PiKHELW (5.50, accepted — clearer narrative, stronger causal experiments), our paper is weaker. Compared to aWLQTbfFgV (6.25, accepted — systematic, well-executed benchmark), our paper is noticeably weaker. The paper lands near **5.0**.

---

## Summary

This paper introduces a framework for analyzing how language models learn context-free grammars by decomposing KL loss over "subgrammar" structure (inner and outer subgrammars). The core theoretical contribution is a suite of theorems showing that the KL divergence between a PCFG distribution and a language model can be recursively decomposed into subgrammar-specific terms. The paper validates this decomposition empirically on small transformers, observes that transformers learn subgrammars in parallel (rather than sequentially), explores curriculum learning via subgrammar pretraining with CKA analysis, and demonstrates that depth of recursion, not sequence length, is the primary difficulty for transformers.

## Strengths

- **Novel subgrammar framework.** Definitions 3.3 and 3.5 formalize inner and outer subgrammars for PCFGs, providing a new lens for studying how grammar substructure relates to language model training. Theorem 4.1 (unique decomposition into inner subgrammars) gives the framework structural grounding.

- **KL decomposition validated empirically.** Theorem 4.3 and Corollary 4.4 are directly validated in Figure 1, which shows that overall KL loss tightly tracks the sum of subgrammar losses throughout training on small transformers. This confirms the decomposition is not merely formal but observable in practice.

- **Parallel learning observation.** Figure 2 and Section 4.2 demonstrate that all subgrammar losses decrease simultaneously — not sequentially — challenging the intuitive expectation of a curriculum-like progression and opening a concrete direction for studying when parallel vs. sequential acquisition occurs.

- **Depth generalization result.** Section 6 and Figure 3 cleanly separate the effects of sequence length and recursion depth, showing that transformer error grows markedly with depth (0.173 at depth 200) while remaining low for long but shallow sequences (0.017). This pinpoints depth as the core representational challenge.

- **CKA analysis of pretraining effects.** Table 1 and the surrounding analysis (Section 5.2) provide quantitative evidence that subgrammar pretraining reshapes internal representations — pretrained models show higher CKA alignment across attention layers (+8–22% for 2-layer transformers) and better separate subgrammar from non-subgrammar sequences.

## Weaknesses

### Fatal

None.

### Major

- **The paper lacks a coherent through-line and spreads across too many directions.** The subgrammar decomposition theorems (Section 4) are the paper's strongest contribution, but the later sections on curriculum pretraining (Section 5), CKA alignment, and depth generalization (Section 6) do not build on those theoretical results in a principled way. The reader encounters a collection of loosely related explorations — decomposition, parallel learning, curriculum pretraining, representational alignment, depth generalization — rather than a unified investigation. The mismatch between the paper's theoretical ambitions and the exploratory nature of the experiments weakens the contribution as a whole.

- **The parallel learning claim is assessed only qualitatively and is not rigorously tested.** The central empirical claim that transformers learn subgrammars "in parallel" (Section 4.2, Figure 2) rests entirely on visual inspection of loss curves. No quantitative criterion is offered — e.g., time to reach a fixed fraction of final loss for each subgrammar, or a statistical test for simultaneity. Corollary 4.7 (stated informally) assumes gradient updates that never hurt other subgrammars, which is so strong that it functions as a thought experiment rather than a testable prediction. The paper acknowledges this as an open direction, but the claim is presented more confidently than the evidence warrants.

### Minor

- **The theoretical contribution is more modest than the framing implies.** Theorems 4.3–4.6 are decomposition identities that hold for any model at any point in training. They express KL divergence as a sum over subgrammar terms — a useful structural relationship, not a dynamic prediction about learning. The paper frames these as "fundamental theorems" that "reveal how loss behaves with respect to subgrammar structure," which is accurate but oversells their depth. They are accounting identities that enable analysis; they do not by themselves explain or predict acquisition dynamics. The paper would benefit from more modest framing of the theory's scope.

- **Limited empirical scope.** All experiments use a few tiny, hand-crafted CFGs (definitions relegated to the stripped appendix). While the controlled setting is appropriate for validating the decomposition, it limits the generality of the observations about parallel learning, curriculum pretraining benefits, and depth generalization. The paper does not explore whether these phenomena hold across a broader range of grammar structures or model scales.

- **The notation in Definition 4.2 is ambiguous.** $D_{\text{KL}}(P_G \parallel Q \mid \neg s)$ is used without formal definition, and the intended meaning of the nested sums is unclear. This makes the key definition hard to parse and the claimed recurrence difficult to verify from the main text alone.

### Trivial

- **Definition 3.5 (outer subgrammar) is truncated.** The clause "and for each of its non-terminals" appears incomplete, leaving a minor definitional gap that should be fixed.

## Nice-to-Haves

- Developing a quantitative measure of parallel vs. sequential learning (e.g., time-to-threshold per subgrammar) would give the framework predictive bite and strengthen what is currently a qualitative observation.
- Tightening the connection between the theoretical decomposition and the curriculum-learning / depth-generalization experiments would produce a more unified paper. For instance, using the decomposition to predict *when* pretraining on a particular subgrammar should help, or *which* subgrammars cause depth-generalization failures.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The GPT-5.1 results are anecdotal and do not meet the standard of controlled experimentation."** The paper itself states: "These arithmetic tests are purely anecdotal and should not be interpreted as direct evidence about training difficulty on recursive PCFGs" (Section 6). The authors already acknowledge the limitation; the criticism is redundant.
- **"The core theoretical results amount to simple algebraic identities that do not by themselves yield insight into learning dynamics."** This is partially addressed above in Minor weaknesses with the necessary nuance — the identities are useful structural tools but are oversold. The harsh critic's version overstates by dismissing the theorems entirely, when in fact they enable the paper's key empirical observations (Figure 1, parallel learning).

## Novel Insights

The key insight emerging from this work is that the subgrammar structure of a PCFG provides a natural coordinate system for decomposing and monitoring language model training loss. While the decomposition itself is an algebraic identity, its value lies in what it enables: observing that transformers reduce loss on all subgrammars simultaneously rather than mastering simpler ones first, and that curriculum pretraining on subgrammars can measurably reshape internal representations. The framework offers a principled way to connect the static structure of formal grammars to the dynamics of neural network training — a connection that prior work on CFG learning (e.g., Allen-Zhu & Li, 2023; Cagnetta & Wyart, 2024) did not exploit.

## Suggestions

- Focus the paper on the subgrammar decomposition framework and its most immediate consequences (validation, parallel learning). The curriculum-learning and depth-generalization sections could be condensed or moved to an appendix to create a tighter narrative.
- Provide a quantitative metric for parallel vs. sequential learning, even if simple — this would transform the qualitative observation into a testable claim.
- Clarify Definition 4.2 with explicit, formal notation for the conditioned KL divergence and its computation.
- Complete Definition 3.5.
- Consider whether Corollary 4.7, in its current informal form, adds enough value to justify inclusion; either formalize it or present it as a conjecture.

## Score and Decision

**Round 1 bracket:** 4.5–6.5, based on comparison with hNkXTqDrfb (3.75, below) and 0pLCDJVVRD (7.00, above).  
**Round 2 narrowing:** The paper is comparable to F0Zd3knG9j (5.00, rejected) — both study transformers on tree-structured formal languages with some theoretical framing and limited empirical validation — but our paper has a more novel theoretical framework (subgrammar decomposition). It is somewhat weaker than MO5PiKHELW (5.50, accepted), which has a sharper narrative and stronger causal experiments. It is clearly weaker than aWLQTbfFgV (6.25, accepted), a well-executed systematic benchmark.

**Anchor papers consulted:**
- uOnElfFuey (3.00, round 1) — weaker; about regular languages, unrelated framing
- OW5Gf4cse1 (3.00, round 1) — weaker; limited task-complexity study
- hNkXTqDrfb (3.75, round 1) — weaker; similar theory/experiment disconnect but less novel framework
- MO5PiKHELW (5.50, rounds 1 & 2) — slightly stronger; clearer narrative, causal experiments
- 0pLCDJVVRD (7.00, round 1) — stronger; more polished theory + experiments on formal languages
- aWLQTbfFgV (6.25, round 2) — stronger; systematic benchmark, clearer contribution
- F0Zd3knG9j (5.00, round 2) — similar; comparable PCFG/transformer study, less novel framework
- pK4Z6NZ2DB (5.20, round 2) — similar; novel method with presentation/validation issues

The paper introduces a genuinely novel framework (subgrammar decomposition for CFG-based LM training) and validates it empirically, but it spreads across too many directions without a strong through-line, and several central claims (parallel learning, benefits of curriculum pretraining) are supported only qualitatively or preliminarily. The theoretical results, while useful, are decomposition identities rather than dynamic predictions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>