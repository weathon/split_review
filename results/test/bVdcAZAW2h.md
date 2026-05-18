I now have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper provides a principled framework for replacing Layer Normalization (LN) with RMSNorm without changing a network's output (inference) or training dynamics. The key insight is that if the linear module preceding an LN satisfies a column-centering constraint (each column of the weight matrix sums to zero), the output is guaranteed zero-mean, making LN's centering operation redundant. For inference, the paper proposes **Column Centered Weight Transformation (CCWT)** — a one-time, lossless transformation of pre-trained weights that enables LN to be replaced by RMSNorm, yielding identical outputs with reduced computation. For training, **Column Based Weight Centering (CBWC)** is a reparameterization that maintains the column-centering property during optimization, so that "CBWC+RMSNorm" has theoretically equivalent training dynamics to LN while being computationally cheaper. The paper validates the approach across multiple architectures (GPT-2, BERT, BLOOM, ViT, etc.) and tasks (translation, text classification, image classification).

## Strengths

1. **Clean, rigorous formalization of a practical idea.** The paper introduces clear definitions (redundant centering, column-centered constraint, foldable LN, regulable modules) that ground the intuition in precise mathematics. Proposition 1 (zero-mean property) and Proposition 2 (CCWT equivalence) are cleanly stated and proved. This goes beyond the ad-hoc LN→RMSNorm replacements in prior work.

2. **CCWT enables lossless inference acceleration for pre-trained models.** The transformation is a simple one-time operation (Definition 4) that does not change the model's outputs. The paper demonstrates a 10.31% reduction in total inference time for GPT-2 (0.0152s → 0.0136s) and 10%–20% acceleration in CUDA time across GPT-2, BERT, and BLOOM, while preserving exact output equivalence (Proposition 2).

3. **CBWC + RMSNorm closely matches LN training dynamics.** Proposition 3 proves that for foldable LNs (those whose centering is redundant due to column-centered preceding modules), CBWC+RMSNorm has identical optimization to LN. Empirical results on translation (Figure 2), text classification (Table 1, Figure 3), and image classification (Table 2) show CBWC+RMSNorm outperforms plain RMSNorm and closely tracks LN performance. The "continue learning" experiment (Section 5.4) confirms weight matrices converge to near-identical values (difference < 1e-5).

4. **Generality beyond linear layers.** The paper extends the column-centering idea to recurrent layers, convolution layers, and self-attention (via the posterior V-matrix), providing explicit transformations in Appendix A.3. This demonstrates broad applicability across architectures.

5. **Detect-and-fold algorithm validated on real models.** Algorithm 1 provides a systematic method for identifying foldable LNs, tested on GPT-2, BERT, ViT, Phi, T5, and BLOOM, finding all LNs foldable.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Contradictory or unclear handling of pre-norm architectures.** The paper states (line 211): *"Due to the residual structure and the none-zero-mean output of embedding layer, we cannot find any foldable LN in pre-norm transformer by this method."* It then immediately states (line 213) that ViT — a pre-norm architecture — has all LNs foldable. The resolution (adding an extra centering after the embedding) is mentioned in the same paragraph, but the paper never explicitly confirms that this extra step was applied when declaring ViT's LNs foldable. A reader is left uncertain whether the claim relies on the raw algorithm or on a modified pipeline. This is a clarity problem, not a methodological flaw (the SWIN image classification experiment in Section 5.3 does explicitly add this centering and shows it works), but it undermines confidence in the advertised claim of "immediate applicability" to all pre-trained models.

2. **Inference speedup lacks measurement methodology.** The paper reports a 10.31% inference speedup for GPT-2 (0.0152s → 0.0136s) and "10% to 20%" CUDA time acceleration for GPT-2, BERT, and BLOOM, but does not report batch size, sequence length, hardware configuration, or measurement methodology. Without these details, the results cannot be independently reproduced or compared. Given that memory-bandwidth-bound operations dominate LLM inference, reporting these settings is essential to evaluate the practical significance.

3. **Proposition 3 claims identical optimization without upfront caveat about dropout.** Proposition 3 states that the optimization processes of a foldable LN and CBWC+RMSNorm are *identical*. The paper correctly acknowledges later (Section 5.3) that dropout layers disrupt the zero-mean property, breaking this equivalence for many practical architectures. While the empirical validation is honest (and shows CBWC+RMSNorm still performs competitively), the strong claim in Proposition 3 is presented without this caveat. The mismatch between the theoretical claim and the practical setting (where dropout is standard) should be flagged upfront rather than deferred to the experiments section.

### Trivial

- The paper could be clearer about how "corresponding modules" are identified for a given LN in residual architectures, particularly for pre-norm transformers where the linear layer is not immediately adjacent to the LN.
- The CCWT/CBWC transformation matrix \((I - \frac{1}{m}\mathbf{1}\mathbf{1}^\top)\) is always a projection onto the orthogonal complement of \(\mathbf{1}\); noting this linear-algebraic interpretation would improve conceptual clarity.

## Nice-to-Haves

- A wall-clock time comparison for training (forward/backward pass time per batch for LN vs RMSNorm vs CBWC+RMSNorm) would strengthen the efficiency claim.
- Reporting downstream task performance (not just weight similarity) for the "continue learning" experiment (Section 5.4) would make the claim of identical optimization more concrete.
- An ablation removing dropout entirely to verify that the theoretical equivalence holds exactly in that setting (isolating the dropout-induced gap) would cleanly partition the empirical picture.

## Removed Points

- **"No experiment on a model larger than GPT-2 (1.5B?)":** Factually incorrect — the paper tests BLOOM (176B parameters). Removed.
- **Parser artifacts about Algorithm 1 text:** The extracted text shows "Section 19: end if" and "Section 20: end for," but these are parser artifacts, not author errors. Removed per instruction.
- **Criticism that the definition of foldable LN does not explicitly require applicability to pre-trained weights:** The definition is about function equivalence, which inherently covers pre-trained weights. The concern reflects a misreading. Removed.
- **Nitpick about ambiguous algorithm description due to parser issues:** Largely a PARSER artifact; the surrounding prose is sufficient for the reader to understand the method.

## Novel Insights

The reviews surface one genuinely useful point beyond the paper's own contribution: the paper's handling of pre-norm architectures with an extra centering step is conceptually analogous to how Batch Normalization folds into adjacent linear layers at inference time (Jacob et al., 2018). The paper does not draw this parallel, but it is instructive: just as BN folding is well-understood and widely deployed, the LN→RMSNorm folding proposed here follows the same logic of absorbing a normalization's statistics into the preceding linear layer's parameters. Framing CCWT explicitly as the LN analogue of BN folding would strengthen the paper's appeal to practitioners familiar with that technique.

## Suggestions

1. **Clarify the pre-norm vs. post-norm handling explicitly.** Add a one-paragraph taxonomy: (a) post-norm: all LNs foldable via raw CCWT; (b) pre-norm: requires one extra centering after the embedding layer; (c) with that centering, all LNs foldable. State clearly whether ViT/etc. were evaluated with or without this extra step.

2. **Add experimental methodology details for speed measurements.** Report batch size, sequence length, GPU type, CUDA version, and number of warmup/measurement iterations for all timing experiments.

3. **Restructure the Proposition 3 / dropout discussion.** Move the dropout caveat into or immediately after Proposition 3 so readers see the limitation alongside the theoretical claim.

## Score and Decision

The paper's core contribution — a clean, theoretically grounded method to replace LN with RMSNorm at inference (losslessly) and during training (with equivalent dynamics) — is sound and practically useful. The weaknesses are primarily about presentation clarity and missing experimental details, not about the validity of the claims. With straightforward clarifications on the pre-norm handling and additions to the experimental methodology, the paper would be a solid contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>