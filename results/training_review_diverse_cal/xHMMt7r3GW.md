Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces LieRE (Lie group Relative position Encodings), a method that generalizes Rotary Position Embeddings (RoPE) to arbitrary n-dimensional inputs. Rather than RoPE's block-diagonal 2D rotations, LieRE learns a skew-symmetric matrix basis and uses the matrix exponential to produce dense rotation matrices for each position. On CIFAR-100, LieRE achieves a 10.0% relative accuracy improvement over the DeiT III baseline and a 2.2% improvement over RoPE-Mixed; on UCF101 (3D video), it achieves a 15.1% relative improvement over absolute position encodings. The paper also claims compute and data efficiency advantages.

## Strengths

1. **Principled generalization of RoPE to higher dimensions.** LieRE replaces RoPE's block-diagonal 2D rotations with dense rotations generated via a learned skew-symmetric basis and the matrix exponential (Algorithm 1, Section 3). This allows it to encode n-dimensional positions (2D, 3D) within the same mathematical framework, whereas RoPE is inherently 1D and RoPE-Mixed is limited to 2D block-diagonal structure. The connection to Lie groups is well-motivated and the formulation is clean.

2. **Significant and consistent accuracy improvements.** On CIFAR-100, LieRE achieves a 10.0% relative improvement over DeiT III, 7.3% over VisionLlama, and 2.2% over RoPE-Mixed (Table 1). On ImageNet, LieRE maintains competitive accuracy and shows a clear advantage over RoPE-Mixed at higher resolutions (Figure 2). On UCF101 (3D video), the 15.1% relative improvement over absolute encodings is substantial. These gains are demonstrated across multiple architectures (ViT-T, ViT-B, ViT-L) in Table 4.

3. **Thorough ablation of design choices.** The paper systematically examines the effect of basis block size (Figure 4a, showing smooth improvement from block size 2 to 64), parameter sharing across heads and layers (Table 2), and transformer backbone scaling (Table 4). This provides useful insights into how LieRE's capacity can be controlled.

4. **Multi-resolution generalization.** LieRE with simple sequential position scaling maintains strong accuracy across resolutions from 196×196 to 448×448 on ImageNet, outperforming RoPE-Mixed at most resolutions (Figure 2). This is a practical advantage for real-world deployment.

5. **Patch-shuffling analysis.** LieRE-based models exhibit the largest accuracy drop when patches are shuffled (Table 3), demonstrating that they more effectively leverage positional information than the baselines. This provides convergent evidence that LieRE's positional encoding is functionally meaningful.

## Weaknesses

### Fatal
None.

### Major

1. **Compute efficiency claim conflates steps/epochs with actual compute savings.** The paper claims "3.9-fold reduction in training time" (abstract) and "3.9X reduction in training compute" (§5.4), but the actual measurement is training *epochs* (or *steps*) to reach a target accuracy. The per-step computational overhead of LieRE is never accounted for: computing the matrix exponential for every position, head, and layer adds non-trivial FLOPs. The paper contains no analysis of wall-clock time, total FLOPs, or even a rough estimate of the matrix exponential's cost. Since each LieRE step is more expensive than a baseline step, the net compute savings could be substantially smaller than claimed, or could even vanish. This is not a minor oversight — it directly undermines one of the paper's headline contributions. The inconsistency in the reported numbers (abstract and §5.4 say "3.9," while the conclusion in §8 says "3.5") further erodes confidence in the efficiency claims.

### Minor

2. **Parameter-capacity confound not fully resolved.** LieRE adds ~580k parameters to a ViT-B backbone. The block-size ablation (Figure 4a) and parameter-sharing experiments (Table 2) partially address whether improvements come from the rotation structure or just extra parameters, but the paper lacks a controlled comparison where a baseline (e.g., RoPE-Mixed or DeiT III) receives a comparable number of additional parameters in a non-positional way (e.g., increased width/depth or a learnable linear transformation after the rotation). The existing evidence is suggestive but not conclusive.

3. **Data efficiency claim lacks statistical rigor.** The claim that LieRE outperforms the full-dataset DeiT III baseline using only 70% of the training data (Figure 3b) is supported by a single curve without error bars, confidence intervals, or any indication of variance across random subsamples or seeds. For a quantitative claim of this nature, this level of support is insufficient.

4. **3D experiments (UCF101) presented with minimal analysis.** The paper states it "did not optimize any hyperparameters for the LieRE model" on UCF101. It is unclear whether the baselines received tuning or not. The 15.1% relative improvement over absolute encodings is very large, yet the paper provides no analysis of why the absolute baseline is so weak, nor of how LieRE's spatiotemporal structure differs from RoPE-Mixed's in the 3D setting. This makes it difficult to assess reproducibility or interpret the improvement.

5. **Missing geometric intuition for why non-commutativity matters.** The Lie groups background (§2.1) derives the commutativity property of RoPE and notes that LieRE relaxes it, but never provides geometric intuition or a proof-of-concept for why non-commutative dense rotations should be beneficial for 2D/3D data. The paper simply asserts that it gives "more capacity," leaving the reader to guess why that capacity is useful for spatial reasoning.

6. **Inconsistent efficiency numbers.** The abstract and §5.4 report a "3.9×" reduction, while the conclusion (§8) reports "3.5 times less training computed." These are materially different numbers applied to the same finding, with no explanation for the discrepancy.

### Trivial

- **Naming inconsistency.** The paper uses "DeiT" and "DeiT III" interchangeably (both refer to Touvron et al. 2022). While clearly the same work, this is occasionally confusing.

## Nice-to-Haves

- Providing a compute-efficiency comparison that accounts for per-step cost (wall-clock time or total FLOPs including the matrix exponential). Even a rough estimate ("the matrix exponential adds ~X% overhead per step, so net savings are ~Y×") would dramatically increase credibility.
- Adding error bars / multiple-seed reporting to the data efficiency experiment.
- Running a controlled comparison where a baseline receives extra non-positional parameters to match LieRE's parameter count.
- Ablating whether learning the skew-symmetric basis matters vs. fixing it to a random or canonical basis.
- Including a chance-level baseline in the patch-shuffling experiment for context.

## Removed Points

- **"Section 4.1.1 structure is messy"** — Removed as a formatting/style nitpick likely exacerbated by PDF parsing. The content is clear enough.
- **"LieRE per-step cost comparison requires wall-clock time" framed as fatal** — Kept as the core concern (Major weakness #1), but re-framed from "the claim is meaningless" to "the claim conflates steps with compute and needs per-step cost analysis."
- **Strength: "Substantial training compute reduction"** — Removed because it conflicts with verified weakness #1 (the compute claim is not properly supported). Moved here per the rule that when a strength and weakness disagree, the weakness wins.
- **Critic's suggestion to compare against models that are closed-source / API-only for probing** — Not applicable; none of the critic's asks involve this.
- **"Missing related works"** — Not mentioned; not an issue.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the core idea is sound and the accuracy gains are genuine, but the efficiency claims require substantially more support than currently provided.

## Suggestions

1. **The single highest-impact revision** would be to add a proper compute-efficiency analysis: measure wall-clock time or total FLOPs (including matrix exponential computation) for LieRE vs. baselines at matched accuracy. Even a single number with an uncertainty estimate would separate the genuine convergence-speed advantage from the conflated "fewer steps = less compute" narrative.
2. Resolve the 3.9 vs. 3.5 inconsistency and commit to a single, well-defined metric (e.g., training epochs to accuracy X, or total FLOPs to accuracy X).
3. Add error bars or multiple-seed runs to the data efficiency experiment (Figure 3b) and report how many random subsamples were used.
4. Strengthen the parameter-capacity argument by adding a baseline with extra non-positional parameters matched to LieRE's count, or by explicitly arguing why the block-size ablation and sharing experiments already address the concern.

## Score and Decision

The paper introduces a clean, principled generalization of RoPE to higher dimensions and demonstrates genuine accuracy improvements on 2D and 3D classification tasks. The core contribution — LieRE as a positional encoding method — is novel, well-motivated, and empirically validated. However, the paper's two secondary claims (compute and data efficiency) are not supported with sufficient rigor: the compute claim conflates training steps with actual compute savings without accounting for per-step overhead, and the data efficiency claim lacks any statistical grounding. The inconsistency in the reported efficiency numbers (3.9 vs. 3.5) is a concrete error. These problems are concentrated in the efficiency claims and do not fatally undermine the primary contribution (accuracy improvements from a better positional encoding), but they significantly weaken the paper as a whole. The accuracy gains alone may be sufficient for publication, but the overclaiming and the gaps in support reduce the paper's impact and trustworthiness.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>