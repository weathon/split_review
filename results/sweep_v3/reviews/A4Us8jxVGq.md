Now I have sufficient calibration. Let me write the consolidated review.

## Summary

This paper analyzes the early training dynamics of attention-based transformers through a leading-term gradient expansion. The central contribution is deriving closed-form expressions for the output, value, query-key, and positional encoding weight matrices as compositions of three interpretable basis functions derived from corpus statistics: bigram mappings, interchangeability mappings (capturing functional similarity across tokens), and context mappings (capturing longer-range prefix-suffix co-occurrence). The theory is validated directly on a 3-layer attention-only transformer (TinyStories, cosine similarity >0.99) and indirectly via covariance analysis on Pythia-1.4B.

## Strengths

1. **Closed-form weight characterizations with error bounds (Theorem 4.1, Equations 5–8).** The paper provides explicit expressions for W_O, V^(l), W^(l), and P^(l) in terms of language corpus statistics, with Frobenius-norm error bounds that quantify how long the approximation holds. This is a substantial advance over prior work that gave only qualitative or synthetic analyses of learned features.

2. **Strong direct validation on matching architecture (Section 5.1, Table 1).** The 3-layer attention-only transformer experiment on TinyStories achieves cosine similarity >0.99 between predicted and learned weights for all parameter matrices. This direct verification—where the experimental architecture exactly matches the theoretical assumptions—provides clean evidence that the leading-term analysis captures the weight structure.

3. **Interpretable decomposition into three linguistically grounded basis functions (Section 4.2, Figure 2).** The paper shows how the learned weights decompose into bigram, interchangeability, and context mappings, with concrete examples (Figure 5) illustrating that these features capture both grammatical and semantic structure. This provides a unifying compositional account that goes beyond prior identification of individual mechanisms (e.g., induction heads).

4. **More realistic theoretical assumptions than prior work (Section 3.2–3.3).** The analysis retains causal masking, relative positional encodings, residual streams, and a standard next-token prediction objective on natural language data. This is a meaningful improvement over prior theoretical work that often uses synthetic structured languages, removes positional encodings, or employs non-standard training procedures.

5. **Per-head analysis of attention dynamics in Pythia (Figure 7).** The analysis showing that intermediate layers (e.g., layer 13) exhibit faster head specialization than early or late layers provides a fine-grained, testable prediction that goes beyond aggregate similarity.

## Weaknesses

### Fatal
None.

### Major

1. **Architecture gap between theory and headline validation on Pythia.** The theory (Definition 3.1, Theorem 4.1) is derived for a single shared query-key matrix W^(l) with tied Q-K weights, no MLP layers, and a single output matrix. The Pythia-1.4B validation (Section 5.2) uses separate query/key projections, 32 attention heads, MLPs, and layer normalization—deviations the paper acknowledges ("Unlike our theoretical setting, Pythia includes additional components such as MLP and multi-head attention, making it impossible to directly read off average token correlations from the weights"). The bridge between theory and practice relies on comparing covariance matrices of token embeddings rather than the weights themselves. While the paper's claim that the theory "generalizes with the addition of multi-head attention or MLP" may be true, the covariance analysis is an indirect test, and the paper does not establish which architectural components are responsible for the empirical alignment. This gap between the theoretical scope and the strength of the claims made about real-world LLMs is the paper's most significant limitation.

2. **Large timescale discrepancy between the theoretical bound and experimental training duration.** Theorem 4.1 provides bounds valid for s ≤ η^{-1}·min(5/(8√T), 1/(12L)). With the stated parameters (η=0.005, T=200, L=3), this gives approximately s ≤ 5 gradient steps. The TinyStories experiments train for 100 epochs (many thousands of steps with batch size 2048), and the features persist. The paper notes that the theory remains "informative well beyond" the bound but does not reconcile this gap theoretically. The empirical observation that leading-term features persist far beyond the proven bound is interesting and potentially important, but as presented it is an unexplained empirical finding rather than something the theory guarantees. The paper would benefit from either extending the bound or providing a specific argument (e.g., higher-order terms approximately aligning with the leading term).

### Minor

3. **Data mismatch in the Pythia validation (Section 5.2).** The theoretical matrices are computed from 100K samples of OpenWebText, but Pythia was trained on The Pile. Corpus statistics such as bigram frequencies and context co-occurrences are dataset-specific. While both are large English corpora and the shared structure likely explains the similarity observed, the lack of a controlled comparison weakens the evidence. The paper should acknowledge this caveat more explicitly or, where feasible, recompute using Pythia's actual training data.

4. **Full-batch GD assumption vs. mini-batch SGD used in experiments.** The theory (Section 3.3) assumes full-batch gradient descent, but TinyStories experiments (Section 5.1) use mini-batches with batch size 2048. The effect of stochasticity on the gradient leading-term approximation is not discussed.

5. **No comparison to a null distribution for cosine similarity.** The paper reports cosine similarities between learned and theoretical weights (e.g., 0.9 cos sim ≈ 25° angular difference) but does not compare against baselines such as similarity to random matrices or trivial bigram-only models. This makes it hard to calibrate what "strong agreement" means quantitatively.

6. **The "mechanistic interpretation" is largely static rather than dynamical.** While the paper claims to explain *how* semantic associations emerge during training (Section 1), the analysis characterizes the weights at an early stage in terms of pre-computed corpus statistics. This shows *what* the weights resemble early on, but the dynamical process—how these features interact across layers and steps, and how they shape model behavior—is not analyzed beyond the initial gradient expansion.

7. **The Q̄ construction description (Section 4.2.2) is too high-level to be independently verified.** The three-step narrative ("input-output matching scoring," "masking and centering," "next-to-query shift") lacks explicit mathematical expressions in the main text, making it difficult to assess without the appendix.

### Trivial
- Figure 6 x-axis: The logarithmic scale starts at 10^0 = 1, but it is unclear whether this corresponds to initialization or after the first gradient step.
- The paper's title asks "How do transformers learn to associate tokens" but does not address the role of training data quantity, model depth, or optimization hyperparameters in the development of semantic associations.

## Nice-to-Haves

- A comparison between the predicted and learned weights via scatter plots of individual entries (not just cosine similarity) would show whether the structure matches quantitatively beyond directional alignment.
- An ablation showing how much of the Pythia covariance structure is explained by bigram statistics alone, without the interchangeability and context mappings, would demonstrate the necessity of the full compositional theory.
- An explicit discussion of why the leading-term features persist beyond the proven bound (e.g., higher-order updates approximately aligning with the leading term, or weight norm remaining small).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about constants in bounds (bounds from appendix not evaluable):** The critic objects to constants like 3, 12, 13 appearing without derivations in the main text. These are standard informal theorem statements; full proofs are in Appendix D as the paper states. This is standard practice.
- **"Missing related works" / "no comparison to simpler baselines":** The related works section covers relevant prior work. The comparison-to-simpler-baselines request is a suggestion, not a weakness. Removed per soft rules.
- **"No analysis of layer norm":** The paper explicitly scopes its theory to the architecture in Definition 3.1, which does not include layer norm. Criticizing its absence is scope creep.
- **"Interchangeability mapping is derived from bigram statistics, so not independent":** The paper never claims these basis functions are orthogonal or independent. This is a correct description of their relationship, not a flaw.
- **Claim about "first explicit characterization" being unqualified:** This is a standard priority claim common in conference papers; the qualifying context (for this particular approach and setting) is implicit in the surrounding text.
- **"Section 4.2.2 description too vague":** Kept as Minor (reworded), not removed entirely.
- **Strength 4 ("Realistic theoretical assumptions") conflicting with weakness about simplifications:** Retained because these are relative comparisons to prior work (which used even more drastic simplifications). The paper indeed keeps more components than most prior theory.
- **Several generic criticisms from the harsh critic** about "evaluation lacks rigor" or "evidence is weak for the claims" that lack specific anchors in the paper.

## Novel Insights

The primary novel insight emerging from the review—beyond the paper's own contributions—is the observation that the leading-term features persist empirically far beyond the formal bound (thousands of steps vs. ~5 steps). This is an intriguing phenomenon that the paper notes but does not explain. It suggests either that the bound is highly conservative (due to worst-case constants) or that the higher-order gradient terms align constructively with the leading term rather than eroding it. Future theoretical work could investigate this alignment. Additionally, the per-head analysis (Figure 7) showing that intermediate layers specialize faster is a concrete, testable prediction about how different layers participate in learning semantic associations, which the paper identifies but whose implications could be explored further.

## Suggestions

1. **Acknowledge and discuss the step-bound discrepancy explicitly.** The paper should say: "The bound in Theorem 4.1 formally guarantees the approximation for ~5 steps; empirically it persists far longer. We conjecture this is because higher-order terms approximately align with the leading term, and leave a refined analysis to future work." This would turn a weakness into a forward-looking contribution.

2. **Strengthen the Pythia validation by testing a counterfactual.** The most convincing way to show that the three basis functions are necessary would be to ablate one of them (e.g., replace the interchangeability mapping with a random matrix) and show that the covariance similarity drops significantly.

3. **Provide null-distribution baselines for cosine similarity.** Report the 95th percentile of cosine similarity between the learned weights and random matrices, or between the learned weights and a bigram-only baseline, to calibrate what "strong agreement" means.

4. **For the Pythia validation, either use The Pile data or explicitly estimate the effect of dataset mismatch** by comparing bigram/context statistics between OpenWebText and a sample of The Pile.

5. **Make the construction of Q̄ more explicit in the main text.** A short mathematical expression (even if informal) for the three-step composition would improve verifiability without requiring readers to consult the appendix.

## Score and Decision

**Calibration anchors** (all papers from the deepreview_13k_calibration corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `hwSmPOAmhk.md` (Factual Recall via Assoc. Memories) | 7.33 | Similar pattern: simplified theory + synthetic validation. This paper has stronger real-world validation on Pythia but comparable theory-practice gaps. Slightly weaker overall. |
| `97rOQDPmk2.md` (Two-layer Transformers with SignGD) | 7.33 | Comprehensive training dynamics analysis for a simplified setting. This paper has stronger interpretability contribution but similar architecture gaps. |
| `SUc1UOWndp.md` (Attention Head Specialization via rLLC) | 7.00 | Strong empirical developmental interpretability work. This paper is more theory-heavy with comparable empirical grounding. |
| `GeUK3zGreN.md` (Taming Transformer without LR Warmup) | 6.50 | Solid theory + limited empirical validation on small models. This paper has better empirical validation and more interpretable results. |
| `aN4Jf6Cx69.md` (Mechanistic basis of ICL) | 4.50 | Limited in scope. This paper has broader theoretical ambitions and stronger validation. |
| `hNkXTqDrfb.md` (Syntax-then-Semantics Learning) | 3.75 | Rejected; similar training-dynamics theory with stronger assumptions and weaker empirical validation. This paper is significantly stronger on both theory (cleaner derivation) and experiments (direct weight matching + Pythia analysis). |
| `4dtwyV7XyW.md` (Principled Transformers for Knowledge Tracing) | 3.00 | Applicational, low theoretical contribution. This paper has much stronger theoretical novelty. |

**Overall assessment:** This paper makes a novel and principled theoretical contribution by deriving closed-form expressions for transformer weights in terms of interpretable corpus statistics. The direct validation on the matching architecture (TinyStories, cos sim >0.99) is strong. The main weaknesses are the architecture gap between theory and the Pythia validation, and the step-bound discrepancy, both of which are significant but not fatal—they limit the scope of the claims rather than invalidating them. The paper compares favorably to accepted papers in the calibration corpus (6.50–7.00 range) on novelty and quality of evidence, while its weaknesses are comparable to those of other accepted theory papers.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>