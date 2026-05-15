Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper develops a theoretical framework for understanding how semantic associations emerge during the early stages of training attention-based transformers on natural language data. By analyzing the leading terms of the gradient updates, the authors derive closed-form expressions for the output, value, query-key, and positional encoding matrices as compositions of three corpus-derived basis functions: a bigram mapping, an interchangeability mapping, and a context mapping. These basis functions compactly capture token co-occurrence statistics, functional (distributional) similarity, and longer-range prefix-suffix relationships. Experiments on a 3-layer attention-only model trained on TinyStories show learned weights achieving cosine similarities ≥0.99 with the theoretical predictions early in training, and remaining above 0.7 after 100 epochs. Extension to Pythia-1.4B on OpenWebText shows suggestive though less rigorous alignment between theoretical leading-term features and token-embedding covariances across layers.

## Strengths

- **Novel theoretical contribution with realistic setup**: The paper provides the first closed-form characterization of transformer weight matrices (output, value, QK, positional) trained on natural language text under standard next-token prediction loss. The analysis retains causal masking, learned relative positional encodings, and residual streams — components that prior theoretical work often simplified away. The leading-term approximation (Theorem 4.1) yields explicit Frobenius-norm bounds showing weights stay close to corpus-statistic expressions for O(1/η) steps, a non-trivial technical result.

- **Elegant decomposition into three interpretable basis functions**: The leading terms are expressed as compositions of a bigram mapping (B̄, capturing next-token dependencies), an interchangeability mapping (Σ_B̄, capturing distributional similarity of preceding-token contexts), and a context mapping (Φ̄, capturing longer-range prefix-suffix co-occurrence). The paper illustrates these with concrete examples in Figure 5 (e.g., "red"→"truck" for bigram, "fish"↔"pond" for context), and Figure 2 provides a clear visual walkthrough of how these mappings compose across weight matrices.

- **Strong controlled validation on 3-layer model**: On a 3-layer attention-only transformer trained on TinyStories, cosine similarities between theoretical leading terms and learned weights range from 0.998–0.999 at early checkpoints (Table 1) and remain above 0.7 after 100 epochs despite loss dropping from 8.00 to 5.35 (Figure 4). This provides direct empirical support for the theory's characterization of the weight directions.

- **Compositional interpretation of weight cooperation**: Section 4.2.3 derives how the leading-term computation decomposes into a residual-stream component (XW_O providing average bigram predictions) and a self-attention block that selectively attends to tokens most predictive under the learned value/output projections. This offers a coherent mechanistic picture of how the components collaborate.

## Weaknesses

### Fatal

None.

### Major

- **Pythia-1.4B analysis lacks null baselines, weakening the extension-to-practice claim**: The comparison between theoretical leading-term features and Pythia embeddings/attention weights (Figure 6) reports cosine similarities without any baseline — e.g., similarities obtained with randomly initialized or row/column-shuffled versions of the leading-term matrices. Without such baselines, it is unclear whether the reported similarities (which range from roughly 0.2 to 0.8 depending on layer and step) exceed chance or are specific to the corpus-statistic structure. The embedding mapping (right panel of Figure 6) already shows non-trivial similarity at step 0, which raises concerns about whether the covariance-based comparison methodology introduces spurious alignment. The paper's primary empirical contribution is the controlled 3-layer experiment (Section 5.1), so this does not invalidate the core claims, but it substantially weakens the argument that the theory "extends to practical LLMs" — a claim the paper prominently makes.

- **Theory-experiment step-budget gap is acknowledged but not analyzed**: Theorem 4.1 guarantees weight proximity to the leading terms for s ≤ η⁻¹ min(5/(8√T), 1/(12L)). For the experimental setting (T=200, L=3, η=0.005), this yields only ~5.6 gradient steps. The experiments show alignment persisting for 100 epochs (hundreds or thousands of steps). The paper acknowledges this in one sentence ("remain informative well beyond [the early stage]"), but does not discuss *why* the alignment persists — e.g., whether the gradient direction itself remains aligned with the leading term, whether higher-order corrections are small, or whether the leading-term direction is a stable attractor. The current narrative risks conflating what the theorem proves with what the experiments show. A brief discussion or a gradient-alignment tracking experiment would substantially clarify the relationship between theory and empirical observation.

### Minor

- **Weight magnitude not reported in 3-layer experiment**: High cosine similarity could, in principle, reflect weights that have barely moved from initialization while the leading-term direction happens to align with the initial random direction. The observed loss decrease (8.00 → 5.35) makes this unlikely, but reporting Frobenius-norm distance from initialization at each checkpoint would definitively rule out this concern and strengthen the empirical argument.

- **Semantic interpretation is descriptive rather than behaviorally validated**: Section 4.2 interprets the theoretical matrices as capturing semantic associations (e.g., bigram, interchangeability, context relations), and Figure 5 provides qualitative examples. However, no analysis of actual attention patterns, next-token prediction behavior, or probing tasks demonstrates that the model's runtime computation relies on these associations in a context-sensitive way. This is within scope for a theory paper, but a single behavioral demonstration (e.g., showing that the model's predictions reflect the predicted bigram or context associations on held-out sequences) would transform the interpretation from plausible to convincing.

- **MLP ablation claim is speculative**: The observation that removing the MLP in Pythia-1.4B leaves embedding correlations largely unchanged beyond layer 1 is interesting, but the conclusion that "the MLP at early stages functions similarly to the leading-term value mapping" is stated without any causal test or mechanistic analysis of the MLP's actual transformation. This should be presented as a hypothesis rather than a finding.

### Trivial

- Some imprecision in the prose when describing Figure 6: the "very strong agreement at the early stage" claim is qualified in the following sentence for the attention mapping, but the overall phrasing could be more precise about which panels and layers show strong vs. weak agreement.

## Nice-to-Haves

- Reporting per-head cosine similarity for the 3-layer model (analogous to Figure 7 for Pythia) to show whether different heads specialize differently even in the controlled setting.
- A causal intervention on the Pythia model (e.g., patching attention weights toward or away from the leading-term direction) to test whether the alignment is behaviorally meaningful.
- Tracking gradient alignment with the leading-term direction over training in the 3-layer model, to provide a mechanistic explanation for why weight-direction alignment persists beyond the proven step budget.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Theorem statements are presented only informally, with the crucial bound on s omitted from the main text"* — **Factually incorrect.** Theorem 4.1 explicitly includes the bound: "if s ≤ η⁻¹ min(5/(8√T), 1/(12L))." The bound is right there in the main text.

- *"The interpretation... reduces to a description of the leading-term matrices, not a mechanistic analysis"* and *"The paper does not examine actual attention weights..."* — **Scope creep.** The paper's contribution is characterizing what structures emerge in the weights during training. It does not claim to provide a full causal/behavioral mechanistic interpretation. Section 4.2.3 does provide a compositional analysis of how the components cooperate under the leading-term approximation.

- *"The left panel shows low similarity at early steps and an increase later, not 'very strong agreement... at the early stage'"* — **Cherry-picking.** The paper states "at the early stage of training, there is very strong agreement... excluding only the first layer" and separately notes that "the attention weights... excluding only the first layer" show strong agreement. The description is accurate when read in full.

- *"The introduction's statement that the analysis is 'grounded in a more realistic setting' should be tempered"* — **The claim is explicitly relative to prior work** (synthetic data, no positional encoding, non-standard training). The paper acknowledges its own simplifications. This is a framing preference, not a weakness.

- *"The framing overstates the gap reduction relative to prior work"* — **Relative claim, not absolute.** The paper cites specific prior work that used more restrictive assumptions and positions itself as a step forward, which is accurate.

## Novel Insights

None beyond the paper's own contributions. The decomposition of transformer weights into bigram, interchangeability, and context basis functions is the paper's core novel insight, and the reviews do not surface additional conceptual framings beyond what the paper already offers.

## Suggestions

- Add null baselines (random matrices, shuffled leading terms) to Figure 6 to establish that the observed Pythia cosine similarities exceed chance. This is the single most impactful improvement the authors could make.
- Report weight-norm trajectories for the 3-layer experiment to rule out the near-initialization trivial-alignment concern.
- Add a paragraph discussing plausible mechanisms for why weight-direction alignment persists beyond the theorem's step budget (e.g., track gradient alignment with the leading term over training, or argue qualitatively about the structure of higher-order corrections).
- Recast the MLP ablation finding as a hypothesis rather than a conclusion.

## Score and Decision

**Anchor comparison:**

- **CfFj68C9Cn (6.5, Accept Poster)**: Similar type — early-phase gradient dynamics of transformers on a retrieval task, explicit formulas, tight empirical validation. Our paper is more ambitious in scope (multi-layer, natural language, richer basis functions) but has less rigorous empirical validation (Pythia lacks baselines). Slightly weaker overall.
- **utSqpxQHXq (6.0, Accept Poster)**: Signal propagation theory with novel REM mapping. Our paper's theoretical contribution is comparably novel and well-executed; both papers have some disconnect between asymptotic theory and finite experiments. Comparable quality.
- **EAfMzT8ZLy (4.5, Withdrawn/Reject)**: Induction head dynamics on synthetic data. Our paper is clearly stronger — uses natural language data, validates on a real LLM, has a more complete theory.
- **J2peqXPQbB (5.0, Accept Poster)**: Mechanistic interpretability of algebraic reasoning. Comparable scope; our paper's theoretical contribution is more fundamental.
- **iQG6CObQ7E (4.0, Reject)**: Scaling theory in NTK/lazy regime. Our paper explicitly avoids the lazy regime and validates on language models — clearly stronger.
- **466gVY2sBQ (2.67, Reject)**: Token dynamics in Mamba, limited and incremental. Our paper is much stronger.
- **EbSkBZQF9g (0.5, Reject)**: Single-layer, single NP-complete problem, weak evidence. Not comparable — our paper is far stronger.

The paper makes a genuine theoretical contribution — the first closed-form characterization of transformer weights trained on natural language — with an elegant decomposition into three interpretable basis functions. The 3-layer controlled experiment provides strong validation. The Pythia extension is suggestive but needs null baselines to be convincing. The step-budget gap between theory and experiment is acknowledged but underexplored. Overall, this is a solid theoretical paper with room for strengthened empirical support, placing it squarely in the Accept (Poster) range.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>