## Summary
This paper presents closed-form gradient leading-term approximations for all weight matrices in an L-layer attention-only transformer trained on natural language text. Theorem 4.1 shows that output (W_O), value (V^(l)), query-key (W^(l)), and positional encoding (P^(l)) matrices can each be expressed as compositions of three corpus-derived basis functions: a bigram mapping (B̄), an interchangeability mapping (Σ_B̄), and a context mapping (Φ̄). Experiments on TinyStories achieve cosine similarities exceeding 0.998 between theoretical predictions and learned weights, with follow-up analysis on Pythia-1.4B providing indirect covariance-level evidence of generalization.

---

## Rebuttal Assessment

**Weakness: Architecture diverges from practical transformers**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly identifies that Section 3.2 is explicitly contrastive to prior *theoretical* work, not to production LLMs. This is verified: Section 3.2 says "Prior works have analyzed the training dynamics of attention-based models under simplifying assumptions... In line with Nichani et al. (2024), we study an attention-based architecture that retains these components." Wang et al. (2025) is also genuinely cited in the paper (Definition 3.1 paragraph: "recent work shows that self-attention-only models can match the performance of architectures with MLP layers"). The MLP ablation in Figure 6 middle panel is real. However, Contribution 1 in the paper still reads "the first explicit characterization of weights in attention-based transformers trained on real-world text corpora" without a qualifier — the promised "clarifying parenthetical" is a future revision, not in the paper. The framing issue partially exists.
- **Score impact:** Weakness downgraded (from major to minor framing issue, with real paper evidence supporting the contrastive framing)

**Weakness: Pythia-1.4B validation cannot verify the specific compositional structure**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly acknowledges the limitation and correctly identifies that Section 5.2 already uses appropriately hedged language ("This suggests that our analysis on attention-based models generalizes... and acts as a starting point"). Verified: Section 5.2 conclusion reads: "This suggests that our analysis on attention-based models generalizes with the addition of multi-head attention or MLP and acts as a starting point for a finer-grained analysis of full training dynamics." However, Contribution 3 in the Introduction still uses the word "validate" without qualification. The author promises revision but the paper still overclaims at the contribution-level statement. The weakness is not removed from the paper as-submitted.
- **Score impact:** Weakness unchanged (acknowledged by author, but Contribution 3 still overclaims; revision is a promise, not current text)

**Weakness: Persistence beyond validity window is empirically observed but theoretically unexplained**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as an address — Author honestly acknowledges the gap and lists plausible mechanisms as open questions. This is scientifically honest, but the weakness is genuine and unaddressed. The Pythia observation about gradual drift is noted but does not constitute a theoretical account.
- **Score impact:** Weakness unchanged

**Weakness: Error bounds not discussed in terms of relative magnitude**
- **Author's response:** Acknowledge
- **Assessment:** Partially convincing — Author correctly states that for W^(l) and P^(l) the error is O(s^5η^5 T) while the leading term is O((s choose 4)η^4) ≈ O(s^4η^4/24). The relative error is thus O(sηT/1), which at the bound limit sη ≤ 1/(12L) gives relative error ≈ T/(12L). For T=200, L=3 this is ~5.6, meaning the bound may not be practically informative for W^(l) and P^(l). The author acknowledges this and promises a remark addition, but the current paper lacks this discussion.
- **Score impact:** Weakness unchanged (acknowledged but not addressed in the submitted paper; the concern about bound informativeness for W^(l) and P^(l) may be non-trivial)

**Weakness: "Interchangeability" label slightly overreaches**
- **Author's response:** Partially address
- **Assessment:** Convincing — The paper already contains the disclaimer at line 138: "this captures structural patterns such as nouns being preceded by articles or adjectives and objects being preceded by common descriptors." The reviewer's concern is valid but the paper already partially hedges it. The author's point that it reflects distributional similarity in the Harris sense is grounded.
- **Score impact:** Weakness downgraded to trivial

---

## Strengths
- **Near-perfect empirical validation on the target architecture:** Table 1 shows minimum cosine similarity >0.998 across all weight types; Figure 4 confirms persistence above 0.9 after 30 epochs and above 0.7 after 100 epochs. This strongly validates the theorem for the attention-only model class.
- **Hierarchical emergence ordering:** Theorem 4.1 predicts W_O acquires its leading structure at O(sη), V^(l) at O(s²η²), and W^(l)/P^(l) at O(s⁴η⁴) — quantitatively accounting for differential rates of component specialization during training.
- **Interpretable and linguistically grounded decomposition:** The three-way decomposition (bigram, interchangeability, context) aligns with distributional semantics (syntagmatic, paradigmatic, contextual). Figure 5 confirms concrete lexical examples from the TinyStories corpus.
- **Honest transparency about architectural scope:** Section 3.2 is explicit about the theoretical setting; Section 5.2 is appropriately hedged about what the Pythia comparison establishes.

---

## Weaknesses

### Fatal
None.

### Major
- **Contribution 3 still overclaims.** As-submitted, the paper's Contribution 3 reads: "We finally validate our theoretical interpretation on both self-attention models and practical LLM, demonstrating the generality and relevance of our theorems." The covariance-based Pythia comparison cannot verify the three-way compositional decomposition at the weight level. The hedged language exists in Section 5.2 but not in Contribution 3 itself. The revision promise does not fix the paper as reviewed.

### Minor
- **Architecture gap in Contribution 1 language.** Contribution 1 — "the first explicit characterization of weights in attention-based transformers trained on real-world text corpora" — is not yet qualified to the attention-only, vocabulary-space model class. The revision promise is noted but not in the submitted paper.
- **Persistence of leading-term features far beyond the validity window is empirically observed but theoretically unexplained.** Theorem 4.1's formal guarantee covers s ≤ η^{-1}·min(5/(8√T), 1/(12L)); the paper offers no account of why cosine similarity remains above 0.7 after 100 epochs.
- **Error bounds for W^(l) and P^(l) may not be informative.** The relative magnitude of leading term to error for W^(l) and P^(l) involves a factor of T in the denominator of the ratio; for T=200, L=3, the bound may not be quantitatively informative within the stated regime. The author acknowledges this but provides no analysis.

### Trivial
- The "interchangeability" label has partial syntactic-semantic ambiguity, but the paper itself acknowledges this at line 138.
- Section 4.2.3 references Appendix A for Q̄ construction; more in-text detail would aid readability.

---

## Nice-to-Haves
- A controlled bridge experiment (train full transformer with learned embeddings, project to vocabulary space) would directly test whether the compositional structure survives the bottleneck embedding rather than relying on covariance proxies.
- Even a partial analysis of persistence mechanisms (gradient orthogonality to leading-term direction in later steps, loss landscape geometry) would substantially deepen the theoretical contribution.
- An explicit relative-magnitude table comparing leading-term scale to error-bound scale for each weight class would clarify the practical informativeness of the bounds.

---

## Novel Insights
The paper's most genuinely original contribution is the hierarchical emergence ordering derived analytically: the output matrix acquires bigram structure first (one gradient step equivalent), value matrices acquire their context-bigram composition quadratically, and the query-key and positional encoding matrices acquire their interchangeability-context structure quartically. This is not a post-hoc empirical observation but a quantitative prediction from the gradient leading-term expansion. Combined with the corpus-statistical basis decomposition, it provides a mechanistic account of *why* transformers initially behave as bigram language models before developing more structured attention routing — grounded in the differing orders of magnitude of gradient contributions rather than in architectural choices or training curricula.

---

## Suggestions
1. Revise Contribution 3 in the submitted text to replace "validate" with language consistent with what the covariance-level evidence can establish ("provide empirical evidence consistent with").
2. Add a qualifier to Contribution 1 to reflect that the characterization is for the attention-only, vocabulary-space architecture of Definition 3.1.
3. Add a limitations section or theorem remark with relative-magnitude analysis of leading-term vs. error-term, especially for W^(l) and P^(l) where the T factor may make bounds non-informative.
4. Add at least a hypothesis-level discussion of why the leading-term features persist beyond the formal validity window.

---

## Score and Decision

The rebuttal is substantively honest: the authors do not spin weaknesses, correctly identify where the paper itself is already hedged, and acknowledge the genuine gaps. Several of the reviewer's concerns are partially addressed by evidence already in the paper (the contrastive framing in Section 3.2, the hedged language in Section 5.2, the MLP ablation, the acknowledgment of syntactic-semantic scope in Σ_B̄). However, the two major weaknesses are not eliminated by the rebuttal: Contribution 3 still overclaims "validate" in the submitted text, and the persistence-beyond-validity-window gap remains theoretically unaddressed. The revision promises, while credible, do not count under the review guidelines.

The architecture weakness is partially downgraded since the paper's own framing is defensibly contrastive to the theoretical literature; the interchangeability label is downgraded to trivial since the paper already hedges it. These adjustments are modest, and the core assessment of the paper — a theoretically solid but practically bounded contribution whose claims around Pythia slightly exceed the evidence — is unchanged.

The score remains at **6.5**, consistent with the original calibration: above comparable mechanistic theory papers on synthetic data, below papers where the architecture-gap bridge to practice is tighter.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>