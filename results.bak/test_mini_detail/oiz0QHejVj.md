## Summary

This paper proposes CLIP-Map, a mapping-based CLIP compression framework that replaces the conventional select-based pruning paradigm with learnable Kronecker-factorized mapping matrices. Instead of dropping "unimportant" weights, CLIP-Map learns transformations \(F^{in}, F^{out}\) that map large weight matrices to smaller ones via matrix multiplication, combined with a linear depth-compression operator. A Diagonal Inheritance Initialization scheme (initializing mapping matrices as identity-like diagonals) stabilizes what would otherwise be a variance-exploding optimization problem. The two-stage pipeline (mapping → retraining with distillation) is evaluated on zero-shot retrieval (MSCOCO, Flickr30K) and classification (ImageNet-1K + 20 datasets), showing strong results particularly at extreme compression ratios (1% and 10% of original parameters).

## Strengths

1. **Genuinely novel compression paradigm for CLIP.** The paper introduces *mapping-based compression* as an alternative to the dominant select-based pruning paradigm for vision-language models. Rather than dropping weights, CLIP-Map learns to project original weights into a smaller space via Kronecker-factorized matrices (Eqs. 3-4), which reduces mapping parameter complexity from \(O(D_1^2 D_2^2)\) to \(O(D_1 D_2)\). This is a conceptually clean departure from prior work and is clearly distinguished from model-growth mapping methods (LiGO, LeTs) in Section 2.2.

2. **Clear gains at extreme compression ratios (1% and 10%).** Table 1 shows that at 1.0% compression, CLIP-Map (0.84M params) achieves 15.8 TR@1 on MSCOCO versus 12.5 for progressive TinyCLIP and 10.5 for non-progressive TinyCLIP — a gap of 3-5 recall points. At 10.0% compression (8+3M params), CLIP-Map reaches 38.4 TR@1 vs. 36.2 (progressive TinyCLIP) and outperforms on all Flickr30K and text-to-image metrics. These are the paper's strongest and most reliable results.

3. **Diagonal Inheritance Initialization is convincingly shown to be essential.** Section 3.2.3 provides a clean mathematical derivation (Eqs. 5-8) of why independent Kronecker factors cause multiplicative variance explosion. Table 5 demonstrates that Diagonal Init achieves 28.9% ImageNet-1K top-1 accuracy versus 4.9% (Xavier) and 4.4% (Kaiming) — a roughly 6× improvement — confirming the initialization is the key enabler of the mapping-retraining pipeline. This is well-executed and well-motivated.

4. **Fewer seen samples than TinyCLIP at comparable accuracy.** Table 3 shows CLIP-Map_small reaches 42.7% ImageNet-1K zero-shot with only 0.45B seen samples, while TinyCLIP-8M/16 needs 0.75B to reach 41.1%. Similarly, CLIP-Map_base reaches 63.7% with 0.30B vs. TinyCLIP-39M/16's 63.5% with 0.75B. This supports the efficiency claim, though see weaknesses about transparency of these counts.

## Weaknesses

### Fatal
None.

### Major

1. **Efficiency claim is not fully verifiable from reported data.** The paper repeatedly states that CLIP-Map requires "fewer training epochs" and "fewer seen samples," and Table 3 provides seen-sample counts for the retraining stage. However, the paper never clarifies whether these counts include the mapping stage (which forward-passes the full teacher model through the dataset for several epochs). Since the mapping stage processes all data through the large frozen teacher, excluding it understates total compute. The gap between CLIP-Map (0.45B) and TinyCLIP (0.75B) in Table 3 would narrow if 5 epochs of YFCC15M mapping (~0.15B additional samples) were included. The authors should report a full breakdown: mapping stage epochs × data size + retraining stage epochs × data size for each reported model, so the efficiency comparison can be properly evaluated.

### Minor

2. **Gains at 50% compression are marginal, but the abstract overclaims slightly.** At 50% compression (Table 1), CLIP-Map and TinyCLIP are essentially tied on MSCOCO (55.1 vs. 54.9 TR@1, 78.8 vs. 79.4 TR@5), and CLIP-Map is notably worse on Flickr30K TR@1 (81.9 vs. 84.6). The abstract says CLIP-Map "outperforms select-based frameworks across various compression ratios," which is not true for the 50% setting on Flickr30K. The paper's body accurately describes this as "competitive performance," but the abstract should be qualified to reflect that the method's primary advantage is at aggressive compression ratios. This does not undermine the paper's core contribution — extreme compression is the harder setting — but the framing should be precise.

3. **"Inevitable information loss" framing is overstated.** Section 1 claims pruning "inevitably leads to information loss" (p. 1), which is technically true of any compression method (including mapping), and the paper's own empirical contribution shows that mapping + retraining outperforms pruning + retraining — a fair quantitative finding that does not need an absolute-sounding rhetorical frame. Softening this would not weaken the paper.

### Trivial
None.

## Nice-to-Haves

- **FLOPs or wall-clock comparison of mapping vs. retraining stages.** Table 4 already provides a controlled comparison with fixed total epoch budgets (0+25 vs. 5+20, etc., all summing to 25 epochs), which is sufficient to show the mapping stage's accuracy benefit. However, reporting the additional FLOPs or wall-clock time incurred by the frozen-teacher forward pass during mapping would strengthen the efficiency analysis and make the "fewer seen samples" claim fully transparent.
- **A Kronecker vs. alternative low-rank decomposition comparison.** The paper could ablate Kronecker factorization against, e.g., a single low-rank SVD-based mapping to further justify the design choice, though the Kronecker formulation is well-motivated by the need for separate input/output dimension transformations.

## Removed Points

- *"No ablation comparing total training cost (FLOPs/wall-clock) between mapping-retraining and equivalent-length pure-retraining baseline"* — **Removed because Table 4 already provides this controlled comparison.** Every row in Table 4 sums to 25 total epochs (0+25, 1+24, 3+22, 5+20, 7+18). The Manual Drop (0 epoch) row is exactly the select-based pruning + retraining baseline. The paper does compare mapping+retraining vs. manual-prune+retraining under a fixed epoch budget.
- *"Missing ablation comparing Kronecker factorization to full-mapping matrix"* — **Removed as impractical.** The full mapping matrix has \(O(D_1^2 D_2^2)\) parameters; for ViT-B/16 this is \(\sim O(10^{12})\), making training infeasible. Kronecker factorization is a design necessity, not an arbitrary choice, so an ablation against the infeasible alternative is not meaningful.
- *"Cross-modal joint mapping not explored"* — **Removed as scope creep.** The paper applies mapping independently to each encoder, which is a natural starting point. Exploring cross-modal interactions is a separate research direction.
- *"Table 1 has an oddly repeated row"* — **Removed as a parser formatting artifact.** The original submission's table formatting was garbled during PDF extraction.
- *"Missing appendix / reproducibility details"* — **Removed per review guidelines.** The appendix was stripped during PDF parsing; it exists in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a supplementary table (or extend Table 1/3) that breaks down total training compute as: (mapping epochs, mapping seen samples) + (retraining epochs, retraining seen samples) for every reported model variant, alongside the same breakdown for baselines. This single fix would resolve the main transparency concern.
2. Qualify the abstract's "outperforms across various compression ratios" to explicitly note the regime of strongest advantage (high compression) and the competitive-but-not-superior results at moderate compression.
3. In Section 1, replace "inevitably leads to information loss" with a more measured statement, e.g., "select-based pruning can result in substantial information loss, especially under high compression ratios."

## Score and Decision

Calibration anchors used across all rounds:

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| j1FLTvgyAh.md | 2.50 | R1 | Weak few-shot CLIP paper, rejected. CLIP-Map is far stronger. |
| hgayrNSbri.md | 3.40 | R1 | Retrieval-augmented captioning, rejected. CLIP-Map has clearer contribution. |
| FwkYeLovHk.md | 3.33 | R1 | CLIP weak-to-strong generalization, withdrawn. Not comparable in rigor. |
| 8GMUa79ZKc.md | 5.00 | R1 | AMAP pruning, withdrawn. Incremental contribution. CLIP-Map has greater novelty. |
| 0eRJRbVG95.md | 4.40 | R1 | MLLM pruning, withdrawn. CLIP-Map has stronger empirical evidence. |
| MKpiaqh7R0.md | 5.00 | R1 | Input compensation pruning, rejected. Novelty concerns. CLIP-Map is more novel. |
| tnBaiidobu.md | 5.75 | R1/R2 | CLIP generalization analysis, accepted poster. Useful analysis but no method. CLIP-Map has practical compression contribution. Comparable overall quality. |
| 5Ca9sSzuDp.md | 8.00 | R1 | CLIP representation decomposition, oral. Far more impactful. CLIP-Map is not at this level. |
| 9ccZzuix2D.md | 5.33 | R2 | Data pruning + KD, rejected. CLIP-Map is stronger empirically and methodologically. |
| 3BhZCfJ73Y.md | 6.25 | R2 | APTP prompt-based pruning, accepted poster. Mixed reviews. CLIP-Map is comparably solid but less architecturally novel. |
| GTcEe5fayC.md | 6.00 | R2 | Token pruning for SSL ViTs, accepted poster. Comparable quality. |
| MVmT6uQ3cQ.md | 6.00 | R2 | OPTIN pruning framework, accepted poster. Comparable quality. |
| sb7qHFYwBc.md | 6.50 | R2 | C-CLIP continual learning, accepted poster. Stronger benchmark contribution. CLIP-Map has comparable methodology contribution. |

The paper is clearly stronger than anchors at 5.0 (rejected/withdrawn pruning papers with incremental contributions) and comparable to anchors at 5.75-6.25 (accepted posters with solid but not exceptional contributions). It is weaker than the 8.0 oral-level papers. The core novelty — mapping-based CLIP compression with Kronecker factorization and a principled initialization — is genuine and well-supported at extreme compression ratios. The main weakness is incomplete transparency around the efficiency claim, which is addressable in revision. The paper's contribution warrants acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>