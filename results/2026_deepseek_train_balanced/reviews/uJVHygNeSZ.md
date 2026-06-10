## Summary

This paper proposes Geometric Transform Attention (GTA), which replaces conventional positional encodings in transformers with a group-theoretic mechanism that applies relative transformations directly to QKV features. By representing each token's geometric attributes (camera extrinsics, image positions) as group elements and using their representations to align query and key-value tokens into a shared coordinate space, GTA provides a principled alternative to APE/RPE that respects the 3D Euclidean structure of multi-view data. Evaluated on sparse wide-baseline novel view synthesis tasks, GTA consistently improves PSNR over SRT, RePAST, and Du2023CVPR baselines across four datasets without adding learned parameters.

## Strengths

- **Mathematically principled formulation grounded in group theory.** The derivation from Eq. (5) to Eq. (7) showing the computationally efficient O(n) form (transforming each QKV vector once rather than computing n² pairwise transforms) is clean and rigorous. This provides a theoretical foundation that distinguishes GTA from ad-hoc PE schemes.

- **Consistent and substantial gains across four NVS datasets.** GTA improves PSNR over its respective baseline on every dataset: CLEVR-TR (+6.12 over SRT, +2.36 over RePAST), MSN-Hard (+1.45 over SRT, +1.25 over RePAST), RealEstate10k (+1.20 over Du2023CVPR), and ACID (+0.75 over Du2023CVPR). The gains are meaningful and hold across both synthetic and real-world datasets.

- **Learning efficiency demonstrated with a concrete metric.** The validation PSNR curves (Fig. 4) show GTA reaches RePAST's performance using only 1/6 of the training steps on MSN-Hard, directly supporting the "improves learning efficiency" claim from the abstract.

- **Attention analysis provides mechanistic evidence.** The PR-AUC comparison (0.492 for GTA vs 0.204 for RePAST in the second attention layer) shows that GTA learns object-level correspondences early in the encoder, not just pixel-level matching. This is the strongest evidence that GTA does something qualitatively different from prior PE schemes.

- **Value transformation ablation yields a novel insight.** Removing the transformation on V drops PSNR by ~2.5 dB on CLEVR-TR (Table 5 left), demonstrating a concrete limitation of RoPE (which omits the V transform) and providing clear design justification for GTA's approach of transforming Q, K, and V jointly.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core contribution is well-supported; the issues below are presentation and completeness gaps that are addressable in revision.

### Minor

- **The anomalously large CLEVR-TR gain is not discussed.** GTA achieves 39.63 PSNR on CLEVR-TR versus SRT's 33.51 (+6.12 dB) and RePAST's 37.27 (+2.36 dB). This gap is an order of magnitude larger (in relative terms) than gains on other datasets. The paper provides no discussion of why GTA benefits so dramatically on this particular dataset (simple objects, only 2 context views), leaving open questions about whether this reflects a genuine geometric understanding advantage or a dataset-specific interaction. The PR-AUC analysis is conducted on MSN-Hard, not CLEVR-TR, so the mechanistic explanation does not directly address this.

- **The DiT/ImageNet experiment lacks all methodological detail.** Table 5 (right) reports Inception Score and FID for DiT-B/2 on ImageNet 256×256, comparing vanilla DiT, DiT+2D-RoPE, and DiT+GTA. The paper provides zero description of how GTA was adapted to this 2D image generation task: no token structure, no ρ representation design, no training hyperparameters. One sentence ("Additionally, Table 5 right shows the performance on the ImageNet generative modeling task with diffusion models") is all that accompanies the numbers. As presented, this result cannot be evaluated or reproduced. The authors should either provide full experimental details or remove this entry — the paper's NVS results are sufficient to support its claims.

- **Multiplicity parameters (s, t, u, v) are never reported.** These parameters in Table 1 determine how many copies of each sub-representation are included and therefore the effective dimensionality of ρ_g and, indirectly, the model's capacity. The paper never states what values were used for any experiment. The claim that GTA introduces "no additional learned parameters" is correct, but the representation's *design* parameters are still choices that affect performance and must be reported for reproducibility.

- **No empirical computational cost comparison.** The paper claims "only minor computational overhead" supported only by an asymptotic argument (O(n) vs O(n²) matrix-vector multiplies). No wall-clock time, FLOP count, memory usage, or throughput is reported for any experiment. Since GTA applies a block-diagonal matrix multiplication to every QKV vector at every attention layer, and the overhead depends on the representation's dimensionality (determined by s, t, u, v), the absence of any measured overhead is a gap for a method whose selling point includes computational efficiency.

### Trivial

None.

## Nice-to-Haves

- Reporting error bars or confidence intervals for main results would strengthen the paper, though single-run reporting is standard for these large-scale benchmarks.
- The hypothesis that SO(3) "may encode object-centric features more efficiently" (line 470) could be tested more directly by visualizing whether attention maps under SO(3) are more object-centric than under SE(3).
- The APE/RPE rows in Table 1 use the same base architecture as GTA — this is stated at line 354 but could usefully be mentioned in the table caption itself.

## Removed Points

These points appeared in the inputs but were removed under the filtering rules:

- **"RPE baseline is custom"** — The paper transparently discloses this limitation ("we could not find an RPE-based method that is directly applicable… we use an RPE-version of our attention"). This is the authors being honest about baseline availability, not a weakness.
- **"No cross-dataset comparison of same architecture"** — The paper explains that different base architectures are appropriate for different dataset groups (SRT-derived for synthetic 360°, Du2023CVPR for real-world). This is an acknowledged design choice, not an oversight.
- **Section-by-section observations** (e.g., "the connection to transforming autoencoder and capsule neural networks is suggestive but not fleshed out") — These are comments, not identified weaknesses.
- **"No error bars or variance reporting"** — Moved to Nice-to-Have because single-run evaluation is the norm for these benchmarks.
- **Strength Finder's "Mathematically principled formulation"** — Retained above as a strength; no conflict with verified weaknesses.
- **Strength Finder's "Generalization beyond NVS to image generation"** — The DiT result is mentioned in strengths above but qualified by the documented lack of context. The existence of improved numbers is a strength; the lack of detail is a separate weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's self-reported contributions and gaps; no reviewer identified a finding that the paper itself did not articulate.

## Suggestions

1. Add a paragraph or controlled experiment explaining the CLEVR-TR gain — e.g., decompose the gain by component (camera extrinsics encoding, image position encoding, value transformation) on CLEVR-TR vs MSN-Hard to calibrate expectations.
2. Either provide full experimental details for the DiT experiment (token structure, ρ design, hyperparameters, training setup) or remove it from the paper.
3. Report the multiplicity values s, t, u, v for every experiment and add a table relating these to the effective dimension of ρ_g.
4. Include wall-clock time, throughput, or FLOP comparison against APE/RPE baselines for at least one dataset.

## Score and Decision

This is a solid paper with a novel, well-motivated, and principled contribution. The experimental evidence is largely consistent and the attention analysis provides compelling mechanistic support. The presentation gaps (DiT details, multiplicity values, runtime, CLEVR-TR discussion) are real but addressable in revision and do not undermine the core claim. The paper merits acceptance at a top venue.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>