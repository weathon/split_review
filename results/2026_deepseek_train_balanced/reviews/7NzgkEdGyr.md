## Summary

This paper proposes BOFT (Orthogonal Butterfly), a parameter-efficient variant of Orthogonal Finetuning (OFT) that parameterizes the orthogonal matrix as a product of sparse orthogonal matrices using butterfly factorization. This reduces the parameter count from O(d²) to O(d log d) while still being able to generate dense matrices (unlike the block-diagonal structure in OFT). The method is validated on LLMs (GLUE, MMLU, GSM8K/MATH), vision transformers (VTAB-1K, SAM), and text-to-image diffusion models (controllable and subject-driven generation), demonstrating consistent performance with fewer trainable parameters than OFT.

## Strengths

- **Novel and technically sound parameterization**: BOFT uses butterfly factorization to parameterize dense orthogonal matrices with O(d log d) parameters, a significant reduction from O(d²). The construction is clean: recursive butterfly factors are made orthogonal via Cayley parameterization of 2×2 (or 2b×2b) blocks. This is a principled extension of OFT that subsumes it as a special case (m=1).

- **Consistent empirical validation across diverse domains with fewer parameters than OFT**: The paper validates BOFT on LLMs (GLUE, MMLU, GSM8K/MATH), vision transformers (VTAB-1K), SAM segmentation, and diffusion models. BOFT uses fewer parameters than OFT in all comparisons while achieving matching or slightly better performance. The SAM results are particularly striking: BOFT-SAM with 0.04M parameters matches HQ-SAM with 1.33M parameters (33× reduction). The controllable generation results (Table 5) show the clearest improvement, with BOFT achieving error 5.667 vs. OFT's 6.407 (≈11.5% relative improvement).

- **Free weight interpolation property**: A genuinely novel and interesting finding (Figure 8): after training, setting butterfly components to identity one by one (without retraining) produces smooth, semantically meaningful interpolation from controlled to uncontrolled generation. This provides evidence that the butterfly-structured hypothesis space preserves semantic structure, and is not shared by LoRA or block-diagonal OFT.

- **Expressivity analysis**: Theorem 1 formally proves BOFT is more expressive than OFT with the same block size, and the simulation in Figure 4 shows BOFT approximates random orthogonal matrices more parameter-efficiently than block-diagonal OFT.

## Weaknesses

### Fatal
None.

### Major

- **The central claim about butterfly-specific inductive bias is not tested**: The paper repeatedly attributes BOFT's improvements to the inductive bias of the butterfly structure (lines 20–21, 152, 222). However, the ablation in Figure 7 only varies the number of butterfly components m (making the matrix denser), which is equally consistent with the simpler explanation that a denser orthogonal matrix is more expressive. The paper does not compare against an alternative sparse factorization with the same parameter count but a different topology. Without such a control, the "butterfly inductive bias" claim is an untested hypothesis. This is a central rhetorical pillar of the paper that lacks direct evidence.

### Minor

- **Improvements over OFT on standard benchmarks are modest and the "considerable margin" framing (line 27) overstates the evidence**: On GLUE, BOFT averages 89.89 vs. OFT's 89.77 (+0.12). On MMLU 5-shot, 47.9 vs. 47.5 (+0.4). On GSM8K, 50.6 vs. 50.1 (+0.5). On MATH, 8.6 vs. 8.4 (+0.2). These margins are small enough that they could fall within run-to-run variance (the paper states significance at p<0.05 but does not specify the test, making this difficult to assess). The paper's core contribution is primarily one of *parameter efficiency* — achieving similar or marginally better performance with fewer parameters — which is legitimate and valuable, but should be framed as such rather than as "considerable" performance gains.

- **The information transmission framework (Section 3) is pedagogical rather than generative**: The framework is presented as a first contribution (line 24) and used to derive two desiderata (dense connectivity and minimum free edges) that the butterfly structure satisfies. However, it does not generate any novel candidate factorizations beyond what was already known, nor does it provide an algorithmic tool for searching over sparsity patterns. The framework provides an intuitive illustration but does not yield new design choices or results. The contribution is more modest than claimed.

- **Statistical significance claim is underspecified**: Line 161 states results "have passed significant tests with p < 0.05" without specifying the test used, the null hypothesis, or whether corrections for multiple comparisons were applied across the many tasks. This is too vague to evaluate.

- **The practical relevance of Theorem 1's full orthogonal group representability is unclear**: The theorem shows that O(d) butterfly matrices can represent the entire orthogonal group, but this would use more parameters than a single dense matrix. The practical regimes used in experiments (m=2, m=4) do not approach this regime. The paper acknowledges this (line 146), but the theorem's practical implications remain unclear.

### Trivial
None.

## Nice-to-Haves

- A wall-clock training time comparison between BOFT and OFT/other baselines would help readers assess the cost of improved parameter efficiency (the paper acknowledges higher runtime in Section 7 but never quantifies it).
- Additional comparison with an alternative sparse factorization (e.g., random permutation-based sparse orthogonal matrices) at the same parameter budget would directly test the butterfly inductive bias claim.
- More detail on the hyperparameter selection procedure (line 347 mentions "the best possible hyperparameters" without describing the selection process).

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Missing baselines (DoRA, PiSSA)**: Removed per rule that missing related works should not be mentioned without external verification of existence/contemporaneity.
- **"Minimum free edges derivation is muddled"**: Removed — the paper's explanation (lines 75–76) is sufficiently clear; the distinction between necessary edges (d edges for bijection) and free edges is explained.
- **"Block-diagonal cannot approximate classic transforms" relevance**: Removed — the paper uses this as motivation for butterfly structure, which has known connections to classic fast transforms. The relevance is adequately established.
- **Strength about "ablation isolates the effect of butterfly components"**: Downgraded — the ablation varies m but does not isolate butterfly topology vs. denser-matrix expressivity, as noted in the Major weakness above.
- **Strength about "principled information transmission framework" being constructive**: The framework is pedagogical, not generative; this overstates the strength.
- **Strength about "rigorous experimental methodology"**: Kept but the significance test underspecification weakens this somewhat.

## Novel Insights

The synthesis of the reviews reveals that the paper's most solid contribution is the parameter-efficiency improvement itself (O(d log d) vs. O(d²) for dense orthogonal matrices, or O(bd) for block-diagonal), not the inductive bias explanation. The free weight interpolation finding (Figure 8) is genuinely surprising and well-demonstrated; it suggests the butterfly factorization yields a structured hypothesis space on the orthogonal manifold where intermediate checkpoints (by setting components to identity) produce semantically meaningful results without retraining. This is a property unique to the factorized orthogonal parameterization and is worth highlighting as the paper's most distinctive empirical discovery. The paper's weakest link is the mismatch between its rhetorical claims ("considerable margin," "inductive bias of butterfly structure") and what the experiments actually support. The empirical evidence primarily says: "BOFT achieves comparable or slightly better performance with fewer parameters than OFT across many tasks" — which is a real contribution that does not need overclaiming.

## Suggestions

- Tone down the "considerable margin" language and instead emphasize the parameter-efficiency advantage combined with competitive performance.
- Add a controlled experiment comparing butterfly sparsity against an alternative sparse orthogonal factorization (same parameter count, different topology) to substantiate the butterfly-specific inductive bias claim, or explicitly remove the claim.
- Specify the statistical test used for the significance claims (line 161), including what correction for multiple comparisons was applied.

## Score and Decision

This paper has a sound technical core — butterfly factorization applied to orthogonal finetuning is novel, well-motivated, and validated across diverse domains. The free weight interpolation finding is genuinely interesting. However, the paper consistently overstates the magnitude of its improvements, and the central rhetorical claim about butterfly-specific inductive bias is not tested. The contribution is real but more modest than the paper presents it. The paper merits acceptance with significant revisions to calibrate claims to evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>