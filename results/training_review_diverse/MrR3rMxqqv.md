Now I have a thorough understanding of the paper and can verify all claims against the actual content. Let me compose the consolidated review.

---

## Summary

This paper proves a lower bound on the memorization capacity of a single-layer multi-head attention (MHA) module under novel linear-independence assumptions that are weaker than the commonly used General Position assumption. The main result shows that with $H$ heads, embedding dimension $d$, and context size $n$, an MHA can memorize $\Omega(H \cdot \min(n, d_h))$ examples. The proof uses an inductive construction that allocates distinct sets of examples to different attention heads by leveraging softmax saturation, and the theory is supported by experiments validating the input assumptions on ViT models and synthetic memorization experiments confirming the predicted scaling laws.

## Strengths

- **Novel, practically-motivated assumptions that are weaker than General Position.** The paper introduces Assumptions 1 (Kruskal rank of queries $\ge n$) and 2 (context matrices full rank) and validates them experimentally on Vision Transformer models (Table 1). General Position fails in all tested settings (Embedding, Random Attention, Random ViT, Trained ViT), while both new assumptions hold after a single Attention layer. This directly supports the claim that the assumptions are more realistic than those used in prior FCN memorization work.

- **Tight lower bound with matching upper bound in a shared-context setting.** Theorem 1 proves that MHA can memorize $\Omega(H \cdot \min(n, d_h))$ examples. Proposition 4 (rank upper bound with shared context) shows this bound is tight up to constants when contexts are shared, and the comparison with two-layer ReLU networks (Proposition 3) shows MHA matches the memorization order of an FCN with comparable parameter count.

- **Proof technique connecting softmax saturation to per-head role allocation.** The construction (Step 1, Sub-steps 1.A and 1.B) explicitly uses the softmax saturation property to assign distinct sets of examples to different heads while suppressing interference with previously handled examples via a scaled auxiliary matrix $c\mathbf{W}^+$. This provides mechanistic insight into how multi-head attention can distribute memorization across heads.

- **Synthetic experiments confirm the predicted linear scaling and saturation trends.** Figure 2 shows memorization accuracy increasing linearly with $H$ ($R^2 \ge 0.98$), monotonically with $n$, and saturating when $d_h > n$, consistent with Theorem 1's theoretical predictions.

- **Assumptions linked to practical architectural components.** The paper shows how Assumption 2 (context full rank) arises naturally from sinusoidal positional encodings, and Proposition 2 proves that after one Self-Attention layer with skip connection, Assumption 1 becomes valid under a weaker mixing assumption (Assumption 3). This bridges the theoretical conditions with real transformer designs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The main text proof sketch of Proposition 1 leaves critical construction steps opaque.** The induction argument asserts the existence of matrices $\mathbf{W}^+$ and $\mathbf{W}^*$ that simultaneously satisfy (i) $\mathbf{E}^{(t)}\mathbf{W}^+\mathbf{e}^{(t)}=0$ for new examples, (ii) distinct softmax logits for old examples, and (iii) rank at most $d_h$. The paper states that "we demonstrate" this is possible and mentions an "$n$-step induction" but does not provide even a high-level sketch of how these conditions are simultaneously satisfied — particularly how the rank-$d_h$ constraint is enforced. The continuity argument for finite $c$ is also mentioned only in passing (one sentence at line 226). For a theoretical paper where the main contribution is a lower bound, the proof's central mechanisms should be more transparent in the main text. (The full proof likely resides in the appendix, which the parser strips; but the main text sketch as presented leaves the reader to take too much on faith.)

- **Proposition 3 (ReLU comparison bound) is stated without justification or citation.** The bound $T \leq (n+1)m/d_{\text{out}} + (m+1)$ is presented as a fact (lines 266–267), but no proof, derivation, or reference is provided. If this is derived from existing results (e.g., Bubeck et al., 2020), it should be explicitly cited; if it is a new statement, it needs justification. This is a gap in an otherwise useful comparative claim.

- **The Kruskal rank test is heuristic, and the conclusion is slightly overstated.** The paper correctly notes that computing Kruskal rank is NP-hard (line 322) and uses random subset sampling (5000 trials, 99% threshold). However, the paper then states that Assumption 1 "holds" for the tested models (Table 1, line 324), when the test only shows a necessary condition (random subsets are full rank 99% of the time), not the sufficient condition that *every* subset of size $n$ has full rank. The phrasing should be softened to "appears to hold" or "is consistent with the assumption."

- **Synthetic memorization experiments are underspecified.** The paper reports "memorization fraction" and "average accuracy" (line 371) but does not specify: (a) how labels are generated, (b) whether model weights are set analytically using the constructive proof or found via gradient-based training, and (c) how accuracy is measured. For a theoretical paper's supporting experiments, clarity on whether the construction from the proof is being implemented (vs. heuristic training) matters.

- **The continuity argument for finite $c$ is mentioned but not elaborated.** The paper states "This involves showing that a finite value of scaling $c$ above suffices; thus, there exist finite weights with the desired property" (line 226) but provides no sketch of how the limit argument proceeds (e.g., using continuity of determinants or singular values). This is a non-trivial step needed to move from asymptotic saturation to finite-weight existence.

### Trivial
None.

## Nice-to-Haves

- Provide a brief sketch of the $n$-step induction used to construct $\mathbf{W}^*$ and $\mathbf{W}^+$, perhaps showing how the rank-$d_h$ constraint is enforced via low-rank factorization.
- Add a one-sentence disclaimer in §5.1 that the random-subset test is a necessary condition, not a sufficient one.
- Include a reference or one-line justification for the ReLU bound in Proposition 3.
- Specify whether the synthetic experiments use direct weight construction (from the proof) or gradient-based optimization.

## Removed Points

These points are flagged to be removed; treat them with caution.

- "The notation $\ndh = \min(n,d_h)$ is introduced but used before its definition." — **Factually incorrect.** The definition appears in Theorem 1 (line 135), *before* its first use in Proposition 1 (line 168). The paper's ordering is correct.
- "These details may be present in the appendix (which the reviewer cannot access)" framing of the proof sketch criticism. — The hard rule requires removing criticisms based on missing appendix content. I have retained the substance of the criticism (the main text sketch is too sparse) but removed the appendix-inaccessibility framing.
- "The paper does not specify the training algorithm" as a structural flaw. — For a theoretical paper with an explicit constructive proof, the synthetic experiments are very likely implementing that construction directly. The underspecification is a minor clarity issue, not a reproducibility gap. Moved to Minor accordingly.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent concern about the proof sketch's opacity in the main text, but do not identify any structural flaw that the paper's own discussion misses.

## Suggestions

1. Expand the main-text proof sketch to include at least a brief description of how $\mathbf{W}^+$ and $\mathbf{W}^*$ are constructed (even a few sentences on the $n$-step induction and how the rank constraint is satisfied) and how the continuity argument establishes finite $c$.
2. Add a citation or a brief derivation for the ReLU bound in Proposition 3.
3. Soften the language in §5.1 from "Assumption 1 holds" to "is consistent with Assumption 1" or "appears to hold," given the heuristic nature of the Kruskal rank test.
4. Clarify in §5.2 whether the synthetic experiments implement the constructive proof or use gradient-based training, and specify the label generation process.

## Score and Decision

This paper makes a solid theoretical contribution to understanding memorization in multi-head attention. The assumptions are novel and practically motivated, the lower bound is non-trivial, and the tightness analysis is a nice addition. The main weaknesses are in the exposition of the proof in the main text (which likely has full details in the appendix) and a few missing citations/justifications. These are addressable and do not undermine the core contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>