Now I have a thorough understanding of the paper and its calibration anchors. Let me compile the final review.

---

## Summary

This paper proposes studying how language models learn context-free grammars (CFGs) through the lens of "subgrammars" — compositional substructures of CFGs. The authors define inner and outer subgrammars, prove that the autoregressive KL divergence decomposes recursively over subgrammar structure, and conduct small-scale experiments with transformers on synthetic PCFGs. Key empirical findings include: (1) the loss decomposition matches theory across training, (2) subgrammars appear to be learned in parallel (unlike child language acquisition), (3) subgrammar pretraining yields modest representational alignment benefits for small models, and (4) recursion depth rather than sequence length is the primary obstacle to generalization.

## Strengths

- **Clean conceptual framework (Sections 3–4):** The definitions of inner and outer subgrammars (Defs 3.3, 3.5) and the KL decomposition theorems (Thm 4.3, Cor 4.5, Thm 4.6) provide a principled lens for studying how autoregressive LM training interacts with grammar substructure. The decomposition to leaves of the subgrammar DAG (Cor A.1) is a useful organizing principle.

- **Empirical validation of the loss decomposition (Figure 1):** The paper demonstrates that the total KL loss matches the sum of per-subgrammar divergences plus overhead throughout training — even when subgrammar probabilities are unequal. This anchors the theoretical framework in observable training dynamics.

- **Depth vs. length disentanglement (Figure 3, Section 6):** The finding that model error stays flat when context is lengthened without increasing recursion depth, but grows sharply with recursion depth, is a clear and well-controlled result. It isolates recursion depth as the primary difficulty and connects naturally to Theorem 4.6.

- **Representational alignment evidence (Table 1):** CKA analysis across 30 seeds shows that subgrammar pretraining produces higher inter-model alignment in attention layers (+8–22%), suggesting that pretraining steers models into a shared representational regime aligned with grammar substructure. The effect is modest but measurable and consistently observed.

## Weaknesses

### Fatal

None.

### Major

- **"Parallel learning" claim exceeds the evidence (Section 4, Figures 1–2, abstract):** The abstract and Section 4 assert that "small transformers learn subgrammars in parallel," but the evidence is purely visual — all per-subgrammar loss curves decrease concurrently. This does not rule out interdependent progress on a shared representation, nor does it establish independence of subgrammar optimization. Corollary 4.7 offers a sufficient condition for parallel learning, but the paper explicitly states it does not verify whether the experimental setup satisfies this condition (line 225: "An immediate future direction would be to study whether the small transformers... satisfy the independence condition"). The claim needs either stronger evidence (e.g., intervention experiments freezing one subgrammar) or substantially softened framing.

### Minor

- **Abstract overstates the LLM recursion finding (abstract, Section 6):** The abstract claims models struggle with deeper recursion as "a limitation even of large language models." The actual LLM evidence is 5 prompted examples on GPT-5.1 Instant, which the paper itself labels "purely anecdotal and should not be interpreted as direct evidence" (footnote 3). The controlled small-transformer result (Figure 3) stands on its own; the LLM gesture adds rhetorical weight without evidential support.

- **Definition 3.3 may lack closure:** An inner subgrammar is defined via rules whose LHS non-terminal belongs to N', but there is no explicit requirement that RHS non-terminals also belong to N'. If a rule A → αBβ with A ∈ N' but B ∉ N' is included, the subgrammar cannot expand B and is not a well-formed standalone PCFG. The decomposition theorems likely assume closure; the definition should state it.

- **Narrow experimental scope limits generality (Sections 5–6):** Experiments use 2-layer and 4-layer transformers on a small set of hand-crafted PCFGs. The curriculum pretraining benefit on final loss disappears with 4-layer models. CKA effects are concentrated in attention layers with near-zero change in MLP layers (Table 1). The depth-vs-length result (Figure 3) uses a single grammar. These are reasonable choices for an exploratory study, but the paper occasionally draws broader conclusions than the setup supports.

- **Theoretical contributions are organizational rather than deep (Section 4):** The decomposition theorems correctly apply the chain rule and the factorization induced by the PCFG. While the framing as a recurrence over subgrammars is a useful conceptual contribution, the paper's language ("fundamental theorems," "the most important contribution") overstates the mathematical depth.

- **No variance reporting for main loss curves:** Figures 1 and 2 show loss curves without error bars or confidence intervals, making it difficult to assess the reliability of the per-subgrammar decomposition across seeds. CKA results use 30 seeds, but loss curves appear to be single runs.

### Trivial

- **Definition 4.2 notation is difficult to parse:** The "restricted KL divergence" definition contains garbled notation (e.g., "D_KL(P_G || Q | ¬s)") that makes the conditioning structure unclear. The surrounding prose explains the concept, but the formal definition needs cleanup.

## Nice-to-Haves

- A comparison of subgrammar pretraining against other curriculum baselines (e.g., training first on shorter sequences or lower-entropy subsets) would strengthen the claim that the benefit is specifically due to subgrammar structure rather than any form of gradual learning.
- Expanding the depth-vs-length analysis to additional grammar families would test whether the finding generalizes beyond Nested Parentheses.
- A systematic check of the "context-insensitivity" condition (Corollary 4.5) across subgrammars and training checkpoints would bridge the theory-experiment gap more rigorously.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim that theoretical results are "largely restatements of the chain rule and provide limited new insight":** While the mathematical steps are straightforward, the framing as a recurrence over subgrammars is a genuine organizational contribution. Demoted from "Critical Issue" to Minor.
- **Harsh Critic claim about missing baseline for curriculum pretraining:** The paper compares against training from scratch, which is the most relevant baseline. Other curriculum forms would be nice but are not essential. Moved to Nice-to-Haves.
- **Harsh Critic claim about "missing appendix" and "definitions deferred to appendix":** The parser strips appendix sections. The original submission presumably contains these. REMOVED per hard rules.
- **Harsh Critic criticism that Corollary 4.5's context-insensitivity condition "is not assessed":** The paper does address this: "varying the prefix did not result in qualitatively different results, suggesting these models are largely context-insensitive" (line 211). The check is informal but present. Demoted.
- **Strength Finder's claim about "rigorous loss decomposition theorem":** The decomposition is correct but not mathematically deep. Kept with softened framing.
- **Strength Finder's claim about "quite definitively" showing representational alignment:** The CKA effects are modest (+8–22% in attention, near-zero in MLP). The word "definitively" overstates. Kept with caveat.

## Novel Insights

The paper's most distinctive insight is the recursive decomposition of autoregressive KL loss over the subgrammar DAG of a PCFG (Theorem 4.3 → Corollary A.1). While the decomposition itself follows from the chain rule, the observation that it yields a clean recurrence over grammatical substructure — and that this recurrence is empirically visible throughout training — opens a principled way to study how compositional structure interacts with optimization. The depth-vs-length dissociation (Figure 3), where flattening the recursion hierarchy eliminates error while deepening it causes degradation, gives empirical teeth to the theoretical expectation from Theorem 4.6 and suggests that recursion depth is the "hard axis" for gradient-based learners on CFGs.

## Suggestions

- **Soften "parallel learning" to "co-occurring learning"** unless stronger evidence (e.g., intervention experiments) can be provided. The current phrasing promises more than the visual evidence delivers.
- **Add the closure condition to Definition 3.3** (RHS non-terminals must be in N') or explain why it is unnecessary for the intended use.
- **Report variance across seeds for the main loss decomposition curves** (Figures 1–2), not just for CKA.
- **Remove or drastically downweight the GPT-5.1 anecdote**, or reframe it as a speculative remark rather than a finding. The controlled small-model result in Figure 3 is sufficient to motivate the recursion-depth concern.

## Score and Decision

**Round 1 bracket:** The paper falls between 4.5 and 6.5 based on comparison with anchors on formal language learning, synthetic grammar experiments, and transformer training dynamics.

**Round 2 narrowing:** Compared against the closest anchors:
- "How transformers learn structured data: insights from hierarchical filtering" (5.00, Reject): Our paper is stronger — more diverse experiments, cleaner theoretical framework, better writing.
- "Sudden Drops in the Loss: Syntax Acquisition, Phase Transitions, and Simplicity Bias in MLMs" (5.50, Accept): Our paper is comparable in quality but uses synthetic-only data versus real language, and has less thorough experimental validation (no causal interventions).
- "Geometric Signatures of Compositionality Across a Language Model's Lifetime" (5.40, Reject): Similar quality tier, synthetic/controlled analysis of compositionality.
- "Training Neural Networks as Recognizers of Formal Languages" (6.25, Accept): Our paper is clearly weaker — narrower scope, less systematic evaluation.

The paper sits between the 5.00 and 5.50 anchors. It has a clean conceptual contribution, correct theory, and some genuine empirical insights (depth-vs-length), but the evidence for its strongest claims (parallel learning) is thin and the experimental scope is narrow. Score: **5.5**.

### Anchor comparison summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| F0Zd3knG9j — How transformers learn structured data | 5.00 | R2 | Our paper is stronger: more diverse experiments, clearer framework |
| MO5PiKHELW — Sudden Drops in the Loss | 5.50 | R2 | Comparable; ours is synthetic-only, lacks causal interventions |
| q5lJxCXjiY — Geometric Signatures of Compositionality | 5.40 | R2 | Similar quality tier; both study compositionality in controlled settings |
| fp77Ln5Hcc — Depth Extrapolation of Decoders | 4.50 | R1 | Our paper is stronger: better theory, clearer writing, more experiments |
| 0pLCDJVVRD — Percolation Model of Emergence | 7.00 | R1 | Our paper is clearly weaker: less thorough, synthetic-only, weaker evidence |
| aWLQTbfFgV — Training NNs as Recognizers of Formal Languages | 6.25 | R1 | Our paper is weaker: narrower scope, less systematic evaluation |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>