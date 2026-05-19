- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have all the information I need. Let me produce the final consolidated review.

## Summary
This paper formally characterizes the gap between the Tree-Form (TF) queries that prior query-embedding methods can handle and the broader family of Existential First-Order (EFO) queries. It identifies specific syntactic properties (existential leaves, multi-graph edges, cycles, negation without constants) that prior methods cannot represent syntactically, provides a complexity analysis showing TF queries are tractable while general EFO is NP-complete, releases a new 10-query-type dataset covering these gaps, and proposes FIT—a neuro-symbolic method that composes neural link predictors with fuzzy logic to answer arbitrary EFO queries. Experiments show FIT substantially outperforms prior methods on the new dataset and achieves competitive or better results on existing benchmarks.

## Strengths

1. **Rigorous formal characterization of the TF–EFO gap.** Theorem 1 precisely identifies which EFO queries are TF-representable: acyclic, simple query graphs without Property 1 (negation without constants) and Property 2 (existential leaves). The two properties cleanly expose the structural restrictions of existing datasets and methods. This is a crisp, valuable formalization that the community lacked.

2. **New dataset covering genuinely unaddressed query structures.** The ten query types (Figure 3) systematically include existential leaves (2il, 3il), multi-graph edges (2m, 2nm, 3mp, 3pm, im, 3cm), cycles (3c, 3cm), and negation without constants (pni). Prior benchmarks (BetaE, etc.) explicitly lack these, so this is a useful contribution for future research.

3. **FIT method handles arbitrary EFO query graphs in principle.** The fuzzy-logic inference procedure (variable elimination on query graphs) is general: it accepts any link predictor providing triple truth values and can handle cycles via candidate enumeration. The theoretical guarantees (Perfectness Theorem 2, Faithfulness Theorem 3) are correctly stated under stated assumptions and are verified empirically (Table 3 shows 100% MRR on all positive deductible answers).

4. **Empirical superiority on the new dataset is clear and expected.** Table 1 shows FIT outperforming all six baselines on every query type across three KGs, often by large margins (e.g., 64.8% avg. MRR vs. next-best 53.4% on FB15k). This is the expected outcome given that baselines can only syntactically *approximate* the new query types, and it convincingly demonstrates the paper's core claim.

5. **Complexity analysis provides a useful lower bound.** Proposition 2 (adapted from Dechter, 1987) shows TF-query answering is O(n k²), confirming tractability, while noting general EFO is NP-complete. This contextualizes the difficulty gap.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaim about universal quantifiers in prior datasets (Example 1 / Proposition 1 framing).** Proposition 1 is formally correct as a statement about the TF *definition* (negating an existential subformula produces a universal quantifier). However, Example 1 claims that BetaE's "pni" query "should have this kind of formulation in DNF" containing ∀x. The actual BetaE pni query is ∃x. r₁(a,x) ∧ r₂(x,y) ∧ ¬r₃(b,y) — a legitimate EFO formula with negation only on an atomic formula, not on an existential subformula. Prior work applies negation/complement only to the results of atomic projections, not to subformulas containing quantifiers. Therefore the claim that "both the methodology and dataset in previous research deviate from its original goal to answer EFO query" is not supported for the actual queries studied. The paper should drop the universal-quantifier framing and instead focus on the structural gaps (acyclic, simple, existential leaves, negation position), which are sufficient to motivate the new contributions. This overclaim undermines the paper's credibility in its critical Section 3.

2. **Fairness of comparison on the BetaE dataset (Table 2) is not fully controlled.** FIT fine-tunes the neural link predictor on complex queries via its differentiable loss (Section 5.4: "backward propagation helps to fine-tune the neural link predictors"). CQD (the primary baseline on BetaE queries) does *not* fine-tune on complex queries — it uses the pretrained link predictor directly. LMPNN does add learnable parameters, but the paper does not confirm whether training procedures (epochs, negative sampling, batch size) are comparable. While the new-dataset results (Table 1) are the main evidence and are unaffected by this concern, the BetaE-dataset comparisons are weakened by this asymmetry. The paper should either match training protocols or clearly acknowledge the limitation.

### Minor

3. **Dataset answer-set generation methodology is underspecified.** The paper states it re-samples answers for pni "according to our definition" (Section 6) and follows the standard protocol of splitting answers into deductible/predicted using the observed vs. full KG (Section 7.1). However, it does not describe how answer sets are algorithmically computed for queries with negation. For an OWA KG, the true answer set for a negated triple pattern (¬r₃(b,y)) is not directly available. The paper should state the procedure used (e.g., closed-world approximation over the full KG, as is standard).

4. **Faithfulness evaluation on negation queries is not fully explained.** Table 3 reports MRR of 65–90 for negation-containing queries (2in, 3in, inp, pin, pni). The Faithfulness Theorem (Theorem 3) covers only negation-free queries. The paper does not explain how "deductible answers" are defined for queries involving negation, nor how the model achieves these scores when observed triples only provide positive examples. A brief methodological clarification is needed.

5. **Softmax scaling construction (Q factor) is empirically unmotivated.** The paper constructs probabilistic matrices via softmax + scaling factor Q, then clamps to [0,1]. This design choice is not ablated: it is unclear whether the Q factor biases predictions toward entities with fewer observed facts, or whether simpler alternatives (sigmoid, constant-scaled softmax) would perform similarly. An ablation would strengthen the methodological section.

6. **Computational cost and scalability are not discussed.** The inference procedure involves matrix operations over the full entity set and, for cyclic queries, enumerating candidates (step 4 in the toy example). For KGs with millions of entities, this is impractical. The paper should acknowledge this limitation and discuss potential approximations (beam search, sparse operations).

### Trivial
- Line 248 refers to "Godel t-norm" where "Gödel t-conorm" (max) is the intended choice for the existential quantifier. The terminology is slightly off but the meaning is clear.
- The loss function in Section 5.4 treats unobserved triples as negatives under OWA — the critic notes this is standard in KGC, but a brief acknowledgement would improve clarity.

## Nice-to-Haves
- Include a baseline that can also handle arbitrary EFO queries (e.g., exhaustive DNF evaluation via a link predictor) to further isolate the benefit of FIT's inference architecture.
- Report inference time per query type, at least qualitatively, to inform practitioners about scalability trade-offs.
- Add an ablation comparing FIT with and without fine-tuning on complex queries on the BetaE dataset to separate the benefit of fine-tuning from the benefit of the inference architecture.
- Compare FIT using different link predictors (e.g., ComplEx vs. RotatE) to show robustness.

## Removed Points
- **"Loss function treats missing as negative under OWA"** — The critic acknowledges this is a standard issue in KGC. It is not a specific weakness of this paper; removed as generic.
- **"The method is essentially a general wrapper"** — This is a value judgment, not a specific weakness. Removed as subjective framing.
- **The section-by-section presentation notes** that do not identify specific problems but rather offer restructuring advice (e.g., "the paper should reframe this section") — These are editorial suggestions, not verifiable weaknesses, and are partially addressed in the Major weakness above.

## Novel Insights
None beyond the paper's own contributions. The two-reviewer synthesis does not surface an insight about the paper that the paper itself does not articulate.

## Suggestions
1. **Remove or thoroughly correct Example 1 and the universal-quantifier framing.** Drop the claim that BetaE's pni query contains a universal quantifier. Instead, reframe Section 3 around the graph-structural restrictions (acyclic, simple, no existential leaves, negation only with constant anchors) — these are correct, sufficient to motivate the new dataset, and do not depend on a contested reading of prior work.

2. **Clarify the training protocol for the BetaE-dataset comparison.** State explicitly whether FIT is fine-tuned on complex queries while CQD is used without fine-tuning, and if so, discuss the implications for interpreting the relative gains.

3. **Describe how answer sets are computed for the new dataset**, especially for negation-containing queries (closed-world over the training/full KG, or another procedure). This is essential for reproducibility.

4. **Explain how faithfulness MRR values for negation queries (Table 3) are computed**, including the definition of "deductible answers" under negation.

5. **Add an ablation on the softmax + Q-factor construction** to justify the design choice against simpler alternatives.
