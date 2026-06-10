I've now thoroughly verified all claims against the paper. Let me write the final review.

## Summary

The paper introduces NIMBA, a proximity-preserving reordering strategy for converting point cloud patches into a 1D sequence before feeding to Mamba-based SSMs. The key idea is to order patch centers so consecutive elements are close in 3D Euclidean space, reducing the need for positional embeddings and sequence replication. Theoretical analysis contrasts the permutation invariance of softmax attention with Mamba's order-dependence, and experiments cover classification (ModelNet40, ScanObjectNN) and segmentation (ShapeNetPart).

## Strengths

- **Informative PE ablation (Table 5) directly supports the core claim.** NIMBA's accuracy drops only 1.68% when positional embeddings are removed (89.80% → 88.12%), compared to 4.11% for PointMamba, 5.96% for PoinTramba, and 6.53% for Point-MAE. This is quantitative, comparative evidence that the proximity ordering carries spatial information effectively.

- **Concrete training time reduction.** Table 3 reports ~14% faster training on ModelNet and ~17% on ScanObjectNN relative to PointMamba at equal parameter count, traced to the single-sequence length (N vs. 3N). This is a real efficiency gain directly attributable to the method design.

- **Competitive accuracy across benchmarks with systematic improvements over PointMamba.** NIMBA (12.3M params) achieves 89.29% vs. 87.20% (PointMamba) and 86.83% (Point-MAE, 22.1M) on ScanObjectNN OBJ-ONLY, with consistent margins on all three ScanObjectNN variants and ShapeNetPart.

- **Theoretical formalization of ordering challenge.** Propositions 1–2 formally establish that softmax attention is permutation-invariant while Mamba's S6 is not. This grounds the motivation more rigorously than the purely empirical treatment in prior Mamba-for-point-clouds work.

- **Well-motivated robustness advantage under rotation.** Since proximity ordering is based on pairwise distances (preserved under rotation), NIMBA's ordering is naturally stable under rotation — a clean property explained in the paper (Figure 4).

## Weaknesses

### Major

- **Missing comparisons against relevant Mamba-based baselines.** The paper discusses Point Cloud Mamba (PCM), OctreeMamba, PoinTramba, and PointABM in related work and Table 0, but the main accuracy tables compare only against PointMamba among Mamba-based models. OctreeMamba (which also uses sequence length N with octree z-ordering) and PCM (which uses axis-wise ordering with bidirectional scanning) are directly relevant ordering-based methods discussed in the paper itself. Without these comparisons, the central "state-of-the-art" claim in the abstract is insufficiently supported — Table 0 sets up the expectation of a thorough comparison that the experiments do not fulfill.

- **The proximity reordering algorithm is underspecified for reproduction.** Section 3.4 (lines 201–206) describes the algorithm in three sentences of natural language. Specific missing details: (1) what search order is used when looking for a replacement center (forward? backward? from the current index?)? (2) what happens to the center that was displaced — is it reinserted later, discarded, or does the algorithm restart? (3) is the algorithm deterministic? (4) what is its computational complexity as a function of n_c? Without these details the method cannot be independently reproduced from the paper.

- **The "no positional embeddings" rhetoric oversells the finding.** The abstract states the method "does not require positional embeddings" and the contribution list claims "safe removal." However, NIMBA's accuracy drops from 89.80% to 88.12% without PE — a 1.68% gap that, while much smaller than alternatives' gaps, is still meaningful and runs against the framing of "safe removal." The claim should be framed as "NIMBA substantially reduces dependence on positional embeddings," which is well-supported. As written, the language invites readers to expect that PE makes no difference, which the data does not show.

### Minor

- **FPS preprocessing and proximity ordering have an unexamined tension.** Farthest Point Sampling selects centers that are maximally far apart. NIMBA's ordering then tries to enforce that consecutive centers are within distance r=0.8 of each other. The paper does not discuss whether this constraint is satisfiable for FPS-selected centers, nor does it report statistics on what fraction of consecutive pairs satisfy the distance constraint after reordering. If the constraint is rarely satisfied, the ordering may be close to the initial y-sort.

- **On ModelNet40, NIMBA does not surpass transformer-based models.** The abstract claims "surpassing Transformer-based models in both accuracy and efficiency," but Point-MAE (transformer, 22.1M params) achieves 92.30% vs. NIMBA's 92.10%. The claim holds on ScanObjectNN and ShapeNetPart but is too sweeping in the abstract.

- **PoinTramba achieves 92.42% with PE on OBJ-BG, outperforming NIMBA's 89.80% by 2.6%.** The paper acknowledges this, but the practical significance of NIMBA's contribution to the broader point-cloud-Mamba landscape is weakened if a hybrid model with standard PE achieves substantially higher accuracy. The paper could better scope this by clarifying that the contribution targets pure-Mamba architectures.

- **Robustness results (Figure 4) are presented only qualitatively.** Reporting the actual numerical accuracy for each noise condition would let readers assess the magnitude of the advantage quantitatively.

### Trivial

- **Equation (2) notation error (line 125):** $Z_i = C_i Z_i + D_i X_i$ has $Z_i$ on both sides. The standard SSM output equation should use a different variable (e.g., $Y_i$).
- **Table 5 caption is a copy-paste error:** It reads "Performance comparison on the ShapeNetPart segmentation task" but reports the PE ablation on ScanObjectNN OBJ-BG classification.

## Nice-to-Haves

- Reporting inference throughput or FLOPs alongside training time would strengthen the efficiency claim.
- A brief diagnostic on why the Hydra (bidirectional Mamba2) substitution degrades performance would clarify whether it is an optimization issue or a fundamental mismatch.
- A sensitivity analysis for the threshold parameter r (beyond the theoretical discussion of extremes r=0 and r≥2√3) would be valuable.

## Removed Points

- **Hyperparameter search details**: The paper states the grid search is reported (line 228), likely in the appendix which is stripped by the parser. Removed per hard rules.
- **r=0 explanation confusion**: The paper's explanation that "no centers will be considered close enough" with r=0 is actually clear and correct. Removed.
- **Formatting/typo concerns** (including "Conlusion" heading): Removed per hard rules; these may be parser artifacts.
- **Mamba3D and PointABM baseline demands**: These methods address different aspects (local feature enhancement, hybrid architecture) less central to the ordering claim. Removed to focus on the relevant baselines (OctreeMamba, PCM).
- **Reproducibility nitpicks about undisclosed implementation details**: The paper provides reasonable-level implementation information for a conference paper. Removed.

## Novel Insights

The most interesting observation that goes beyond the paper's own framing is the tension between FPS center selection (which greedily maximizes inter-center distances) and the proximity-preserving reordering (which depends on close centers). This suggests that center sampling and ordering should be co-designed rather than treated independently. The robustness result — that NIMBA's ordering is naturally stable under rotation because pairwise distances are rotation-invariant — is an elegant property that could be further exploited, e.g., for out-of-distribution generalization.

## Suggestions

1. Add comparisons against OctreeMamba and Point Cloud Mamba (PCM) in the main accuracy tables.
2. Provide pseudocode for the proximity reordering algorithm and report statistics (fraction of pairs satisfying the distance constraint, number of swaps, sensitivity analysis for r).
3. Replace "safe removal of positional embeddings" with "substantially reduced dependence on positional embeddings" to align rhetoric with evidence.
4. Add numerical accuracy values for each noise condition in the robustness experiment.
5. Fix the equation notation error in Eq. (2) and the Table 5 caption.

## Score and Decision

The paper addresses a legitimate problem — applying sequential SSMs to non-sequential point cloud data — and proposes a sensible direction. The PE ablation and training-time improvements are genuine contributions. However, the evaluation is incomplete in a way that matters for the paper's core claims: several Mamba-based methods the paper itself discusses are absent from the experimental comparison, the core reordering algorithm is described too vaguely for reproduction, and the "no PE" claim is rhetorically inflated. These issues are fixable but the paper in its current form does not meet the ICLR acceptance bar.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>