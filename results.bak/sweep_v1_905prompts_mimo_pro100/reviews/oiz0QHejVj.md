## Summary

This paper proposes CLIP-Map, a mapping-based framework for compressing CLIP models that replaces select-based pruning with learnable Kronecker-factored transformation matrices for width compression and linear layer combinations for depth compression, followed by knowledge distillation retraining. The core idea—adapting mapping-based techniques from model growth to model compression—is novel, and the retrieval results demonstrate strong gains at extreme compression ratios (e.g., 15.8 vs. 12.5 TR@1 on MSCOCO at 1% compression).

## Strengths

- **Novel mapping-based paradigm for compression**: The paper's central contribution—reversing the direction of mapping-based model growth (LiGO, LeTs) to model compression—is a genuinely creative idea. The mathematical framework (Eqs. 1–4) cleanly derives how full mapping with Kronecker factorization reduces parameter complexity from O(D₁²D₂²) to O(D₁D₂), making the approach tractable.

- **Diagonal Inheritance Initialization is well-motivated and strongly validated**: The variance analysis (Eqs. 6–8) provides clear theoretical motivation for the initialization scheme, and Table 5 provides dramatic empirical evidence: Diag Init achieves 28.9% IN-1K accuracy vs. 4.9% for Xavier and 0.1% for Random at 10% compression. This is a clean, convincing ablation.

- **Strong retrieval results at extreme compression**: Table 1 shows CLIP-Map_base consistently outperforms TinyCLIP at 1.0% and 10.0% compression ratios across all retrieval metrics on MSCOCO and Flickr30K. For instance, at 1% compression, TR@1 on MSCOCO improves from 10.5/12.5 (TinyCLIP non-progressive/progressive) to 15.8, and on Flickr30K TR@5 from 21.3/24.5 to 30.3.

- **Efficient training**: Table 3 shows CLIP-Map_base achieves 63.7% zero-shot IN-val with 0.30B seen samples versus TinyCLIP-39M/16 achieving 63.5% with 0.75B seen samples—a ~2.5× reduction in training data with comparable performance.

- **Thorough ablation on mapping stage duration**: Table 4 systematically varies mapping epochs (0–7) and provides practical guidance that 5 epochs is optimal, with clear monotonic trends up to that point.

## Weaknesses

### Fatal
None.

### Major

- **Severe and unexplained regressions on several zero-shot classification benchmarks**: Table 2 reveals that at the most aggressive compression (ViT-8M/16, non-progressive), CLIP-Map dramatically improves on some datasets (ImageNet: 72.4 vs. 63.8, CIFAR100: 41.9 vs. 31.2) but suffers large regressions on others: RESISC45 drops from 16.5 to 8.4, KITTI from 10.8 to 3.9, DTD from 44.6 to 38.6. These are not marginal differences—on RESISC45 and KITTI, CLIP-Map approaches random performance while TinyCLIP retains meaningful accuracy. The paper never acknowledges or discusses this pattern. This directly undermines the paper's first claim that the method "better preserves the full information from the pretrained model." Without analysis of *why* certain domains are catastrophically degraded, it is unclear whether the method genuinely preserves more information or merely reshapes which information is preserved. The authors should acknowledge these regressions and investigate the cause (e.g., domain-specific feature alignment differences).

- **Missing Kronecker factorization ablation**: The paper introduces Kronecker factorization as a core technical contribution but never quantifies its accuracy cost compared to the unconstrained full mapping. While a full O(D₁²D₂²) mapping may be computationally prohibitive, even a single experiment at a moderate compression ratio (e.g., 10%) comparing a partial/full mapping to the Kronecker-factorized version would be valuable. Currently, it is impossible to determine whether the Kronecker decomposition is near-optimal or introduces significant accuracy loss.

- **Narrow baseline comparison**: The primary—and in most tables the only—baseline is TinyCLIP. The paper frames its contribution as demonstrating that mapping-based compression outperforms select-based compression as a paradigm, but only tests one instance of each paradigm. Table 3 includes MoPE-CLIP and MobileCLIP, but with substantially different model sizes (86+42M vs. 39+19M) or training data, making these more illustrative than decisive. Comparisons with other pruning approaches (e.g., UPoP, structured pruning, or direct magnitude pruning) would significantly strengthen the claim of paradigm superiority.

### Minor

- **"Fewer training epochs" claim is partially misleading**: The abstract and contributions claim "fewer training epochs" as a key advantage, but this advantage only holds against the progressive-compression variant of TinyCLIP (3×25ep = 75 epochs or 2×25ep = 50 epochs). Against the non-progressive single-stage TinyCLIP, CLIP-Map uses 5 mapping + 20 retraining = 25 epochs—comparable. The paper should clearly qualify this claim.

- **ResNet experiment is incomplete**: The paper states that "when ResNet serves as the vision encoder, we limit the process to the Mapping stage 5-epochs training, and don't perform the subsequent Retraining stage." This limits the claim of generalizing to "any CLIP-like architecture." The paper should either complete the ResNet evaluation or explicitly qualify the scope of the architecture-agnostic claim.

- **Depth compression receives almost no analysis**: The L_depth component (linear combination of layers for depth compression) is introduced in Eq. 2 but never independently analyzed. How many layers does the compressed model have? Which original layers contribute most? How does the mapping learn to combine layers? This is a non-trivial part of the method treated as a black box.

- **No distillation-only baseline**: It is unclear how much the mapping initialization contributes versus the distillation stage. A comparison where a small CLIP model is trained from scratch using only knowledge distillation (without mapping initialization) would isolate the contribution of the mapping stage.

### Trivial
None (formatting and presentation issues are parser artifacts, not paper issues).

## Nice-to-Haves

- Report total mapping parameter count alongside compressed model size to assess overhead.
- Include wall-clock training time or FLOPs for the mapping stage, which requires backpropagation through the frozen pretrained model.
- Visualize learned mapping structure (which dimensions are merged, which discarded) to provide insight into how mapping-based compression differs from pruning.
- Ablate the λ weighting coefficient in Eq. 13 in the main text (the paper defers this to the appendix).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Table 2 formatting/labeling concerns**: The harsh critic noted column alignment inconsistencies and a potential labeling error ("CLIP-Map_base" for 8M models). These are parser formatting artifacts, not paper issues.
- **Table 3 MobileCLIP dataset quality concern**: The critic noted that MobileCLIP uses higher-quality DataCompDR-12M. The paper already acknowledges this explicitly.
- **Missing appendix content**: The critic noted that diagonal initialization loss curves are in the appendix. The parser strips appendices; this content exists in the original submission.
- **Overstated novelty claim**: The critic noted that "learning linear transformations of pretrained weights has precedents in adapter and low-rank literature." While true, the specific application to compression (not adaptation or growth) is novel, and the paper does position its work relative to LiGO and LeTs.
- **λ weighting coefficient**: The critic noted this is deferred to appendix. This exists in the original submission.

## Novel Insights

The paper's genuinely novel contribution is the reverse-direction application of mapping-based techniques: rather than using learnable mappings to grow a small model into a larger one (LiGO, LeTs), CLIP-Map uses them to shrink a large model into a smaller one. The key technical insight is that Kronecker factorization naturally decomposes the mapping into independent input-dimension and output-dimension transformations, enabling parameter-efficient compression while the diagonal initialization scheme ensures stable optimization by approximating an identity transformation initially. The asymmetric behavior across datasets (strong on ImageNet-like domains, weak on others like RESISC45 and KITTI) is an intriguing empirical finding that, if analyzed, could yield insight into what structural information different compression paradigms preserve.

## Suggestions

1. **Acknowledge and analyze the regression pattern**: The inconsistent results across Table 2 are the most significant gap. A brief analysis (e.g., clustering the 21 datasets by domain, computing feature-space similarity between teacher and student representations per dataset, or examining which attention heads are most distorted) would transform this from a weakness into an interesting finding about the limits of mapping-based compression.

2. **Add the Kronecker ablation**: Even a single comparison at 10% compression between Kronecker-factorized and a moderately larger (but tractable) mapping would significantly strengthen the paper's technical contribution.

3. **Expand baseline comparisons**: Including at least one additional pruning method (UPoP or magnitude pruning) with knowledge distillation would support the claim that the mapping paradigm is superior to the pruning paradigm, not just that CLIP-Map is better than TinyCLIP.

4. **Complete the ResNet evaluation or scope the claim**: Either run the retraining stage for ResNet or change the claim from "any CLIP-like architecture" to "Transformer-based CLIP architectures."

## Calibration Anchors Retrieved

| Anchor ID | Avg Human Score | Round | How it compares |
|---|---|---|---|
| FwkYeLovHk | 3.33 | 1 | Weak paper on weak-to-strong generalization; CLIP-Map is clearly stronger |
| HfJxXbXlYJ | 3.00 | 1 | LLM2CLIP rejected; CLIP-Map has clearer contribution |
| XCugWIuHR8 | 3.00 | 1 | Convex distillation rejected; CLIP-Map is stronger |
| hgayrNSbri | 3.40 | 1 | Lightweight captioning rejected; CLIP-Map is stronger |
| I5S1a1NKxo | 5.00 | 1 | SIDCLIP: narrower scope, fewer results; CLIP-Map is better |
| 774F8gF0UO | 4.67 | 1 | MLLM compression survey; CLIP-Map has more focused contribution |
| LC6ZtQV6u2 | 6.50 | 1 | Proteus: distillation at ImageNet-level costs; CLIP-Map is comparable but with inconsistent classification results |
| 2y8XnaIiB8 | 5.50 | 1 | VL dataset distillation; different domain but CLIP-Map is comparable or stronger |
| 1aF2D2CPHi | 8.00 | 1 | DFKD for CLIP: stronger paper with broader evaluation; CLIP-Map is below this |
| sBJIVQvJqN | 5.50 | 2 | WFPP data pruning; CLIP-Map is stronger |
| 0eRJRbVG95 | 4.40 | 2 | MLLM inference pruning; CLIP-Map is stronger |
| VFhJtV29jZ | 4.75 | 2 | SlimLLaVA pruning; CLIP-Map is stronger |
| 8GMUa79ZKc | 5.00 | 2 | AMAP attention pruning; CLIP-Map is stronger |
| imT03YXlG2 | 6.50 | 2 | Sparse autoencoders for CLIP adapt.; different focus but comparable quality |
| S5yOuNfSA0 | 6.50 | 2 | Understanding CLIP transfer; theoretical; different but CLIP-Map is comparable |
| MSlF3GvUXI | 6.67 | 2 | SAIL structured init; similar idea of mapping/transformation; CLIP-Map has stronger empirical results but more inconsistent |
| 1RrOtCmuKr | 6.33 | 2 | JLCM codebook compression; accepted with good reviews; CLIP-Map is comparable |

**Round-1 bracket**: 5.5–7.0
**Round-2 narrowing**: After comparing to JLCM (6.33, accepted), SAIL (6.67, rejected), and the 6.50 anchors, CLIP-Map sits around 6.0: it has a genuine novel idea and strong retrieval results, but the unexplained classification regressions, missing key ablation, and narrow baselines hold it back from the 6.5+ range where papers have fewer gaps in their evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>