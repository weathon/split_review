Now I have a thorough understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper presents **LEG** (Language-conditioned Equivariant Grasp), a method for language-conditioned robotic grasping that maps language instructions to SO(2)-steerable kernels and cross-correlates them with visual features, thereby incorporating SE(2) symmetries into the grasping policy. The paper also introduces the Language-Grasp Benchmark with 10 tasks (plus 3 variations) and demonstrates strong sample efficiency in both simulation (outperforming baselines on 12-13 tasks) and real-robot experiments (82.5% part-specific grasp success with 5 human demos).

## Strengths

- **Novel incorporation of symmetries into language-conditioned grasping via steerable kernels**: The paper is the first to map language embeddings to SO(2)-steerable kernels for manipulation, enabling the cross-correlation between a rotated kernel and visual features to capture rotational symmetries in a way that prior methods (CLIPort, VIMA, PerActor) do not. This is a genuine architectural innovation.

- **Consistent and often large empirical gains across many tasks**: LEG outperforms all baselines on 12 of 13 tasks with 10 demos and on all 13 tasks with 1 demo (Tables 1, 2). The gains are not cherry-picked — the comparison covers both V-1 and V-2 task families, including novel combinations unseen during training. The FCN vs. ViT backbone comparison (Section 4.4) provides a useful empirical insight about the importance of translational equivariance in pixel-based manipulation.

- **Real-robot validation transfers the sample-efficiency benefit**: LEG-UNet trained on only 5 human demos (100 grasps) achieves 82.5% part-specific grasp accuracy on a UR5 with a Robotiq-85 gripper, using a different observation space (208×288 depth from Azure Kinect) than simulation. This goes beyond a purely simulated result and demonstrates generalization to real hardware.

- **New dedicated benchmark**: The Language-Grasp Benchmark fills a gap — no prior benchmark was designed specifically for language-conditioned grasping with fine-grained part and caption constraints. The inclusion of a scripted oracle and reward function enables reproducible evaluation.

## Weaknesses

### Major

- **Equivariance claim is overstated relative to the actual architecture**: The paper claims to "realize the equivariant policy" (line 10) and presents LEG as leveraging SE(2) symmetries. However, the overall function *f*(*o*, ℓ) = *κ*(ℓ) * *ϕ*(*o*, ℓ) uses a vision-language encoder *ϕ* (UNet or CLIPort encoder) that is **not** rotation-equivariant. Proposition 1 says the method "approximately satisfies" the symmetry, and the support offered is a throwaway line about the *ϕ*=identity case (line 122). The paper provides **no** analysis of how much equivariance is approximately preserved — no quantifiable equivariance error, no empirical test, no characterization of when the approximation breaks down. This is not fatal: the steerable kernel *does* capture object-level rotational symmetry in the cross-correlation *if the feature maps were equivariant*, and the method works well empirically regardless. But the gap between the strong theoretical framing and the actual approximate realization is significant and needs to be addressed. **The authors should either (a) run an empirical equivariance test (rotate input, measure angular deviation of argmax action) to quantify the approximation, (b) replace *ϕ* with a rotation-equivariant encoder, or (c) substantially soften the theoretical claims and present the steerable kernel as a heuristic that works well in practice.**

- **Proposition 1 is stated without argument**: The paper asserts "Proposition 1 if *κ*(ℓ) is a steerable kernel, it approximately satisfies the symmetry," but provides no proof, proof sketch, error bound, or any technical justification beyond an intuitive remark about the identity-mapping case. This gives the reader no way to assess the quality of the approximation or the conditions under which it holds. Either the proposition should be turned into a proper statement (with a proof or at least a formal error analysis), or it should be removed and replaced with an empirical analysis of equivariance error.

### Minor

- **Benchmark counting is confusing**: The abstract and introduction say the benchmark includes "10 different language-conditioned grasping tasks," but the task enumeration (Section 4.1.1) lists 13 numbered entries. The paper clarifies at line 146 that this is "10 fundamental tasks with 3 variations," but the discrepancy persists throughout and forces the reader to reverse-engineer which are the fundamentals and which are the variations. This is a presentational issue, not a substantive one, but it undermines clarity.

- **"1 demo" framing inflates perceived sample efficiency against prior work**: Each "demo" in pick-random-v1 contains 47 grasps; in pick-random-v2, ~22 grasps (lines 161, 175). While the paper clearly defines this, the abstract and comparisons to prior work (e.g., saying VIMA needs 10k demos) indirectly exaggerate LEG's sample efficiency because a reader naturally interprets "1 demo" as one trajectory/successful grasp rather than ~22–47 grasp samples. The comparison across methods in the paper is fair (all methods train on the same data), but claims of sample efficiency against external numbers from the literature should restate the per-demo grasp count.

- **No ablation isolating the steerable component**: The paper does not include a comparison against a variant where the steerable kernel is replaced with a language-conditioned but non-steerable kernel, or a steerable but static (not language-conditioned) kernel. Without this, it is unclear whether the gains come from the steerable property specifically, from the two-branch design, or from other architectural choices.

- **No limitations section**: The paper concludes with a sentence about future directions (line 210) but never explicitly discusses the approximate equivariance, the restriction to top-down orthographic views, or the fact that only pick-and-place tasks were tested. A brief limitations paragraph would improve the paper's scholarly completeness.

### Trivial

- The steerable kernel construction is described in a somewhat scattered way (lift → Fourier → inverse Fourier → even-frequency truncation across multiple paragraphs and footnotes). A more self-contained exposition would help readers unfamiliar with steerable CNNs.
- The paper reports test performance as the best across checkpoints tested every 10k steps (line 175). Reporting the mean/variance across seeds or at a fixed checkpoint would be more standard, though this is not a major issue given the large performance gaps.

## Nice-to-Haves

- An empirical equivariance error metric (angular deviation of argmax action under rotated input) would directly address the major weakness above.
- An ablation of the bilateral symmetry encoding (even-frequency truncation) would confirm whether this design choice helps.
- Releasing the benchmark environment and code would increase the paper's impact.
- Comparing against an E(2)-equivariant UNet as a vision encoder is a natural extension but goes beyond the paper's scope; it would be a separate contribution.

## Removed Points

These points were raised by reviewers but are either factually wrong, parser artifacts, or violate the review guidelines:

- **"Real-world results table is missing"**: The results table is an embedded image in the original PDF (line 203). The parser cannot extract image content, but the table exists in the submission. This is a parser artifact, not an author error.
- **"Simulated tables lack numerical content"**: Same parser artifact for Tables 1 and 2 (embedded images at lines 155, 159).
- **"Missing comparison to equivariant encoders as a weakness"**: Asking the authors to replace *ϕ* with an E(2)-equivariant UNet and re-run all experiments is requesting a different paper. The paper's contribution is language-conditioned steerable kernels, not building the best possible equivariant encoder. This belongs in Nice-to-Haves.
- **"Code/benchmark not open-sourced"**: Criticisms about the release status of code or benchmarks that the paper does not promise to release are not valid weaknesses per review guidelines.
- **"Missing appendix/proofs"**: These sections were removed by the parser; they exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, the finding that FCN backbones consistently outperform ViT backbones in this grasping setting (Section 4.4, "by a large margin") is a practically useful result. It reinforces that translational equivariance matters even when the main focus is on rotational equivariance, and that flattening image structure (as ViTs do) harms manipulation performance. This observation is independent of the steerable kernel contribution and is a clear takeaway for practitioners building pixel-based manipulation policies.

## Suggestions

1. **Add an empirical equivariance test**: Measure the angular deviation between the predicted action under the original input and under a rotated input (with the same language instruction). Plot the equivariance error distribution. This single experiment would quantify the "approximately" qualifier and could salvage the theoretical framing.
2. **Add an ablation replacing the steerable kernel** with a language-conditioned but non-steerable kernel to isolate the steerable component's contribution.
3. **Clarify the benchmark task count** by explicitly stating "10 fundamental tasks (6 V-1 + 3 color-shape V-2 + 1 pick-by-part) plus 3 additional composite variations (pick-random-v1, pick-random-v2, pick-novel-v2), for 13 total settings."
4. **Add a limitations section** discussing the approximate equivariance, the top-down view assumption, and the restriction to pick-and-place.
5. When making sample-efficiency claims against prior work, parenthetically note the per-demo grasp count (e.g., "with 1 demo (47 grasps)").

## Score and Decision

The paper presents a genuinely novel architectural idea (language-conditioned steerable kernels) backed by strong and consistent empirical results across 13 simulated tasks and a real robot. The main weakness is a misalignment between the paper's theoretical framing (claiming equivariance) and what the architecture actually delivers (approximate equivariance without quantification). This gap is significant but not fatal — the empirical results stand on their own, and the steerable kernel approach is a legitimate contribution regardless of whether the equivariance is exact. With an empirical equivariance analysis and softened theoretical claims, the paper would be a solid contribution to the manipulation community.

**Score**: 6.0 — a solid paper with a genuine contribution. It requires revision of the theoretical framing and additional analysis, but the core contribution is real and the empirical evidence is strong.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>