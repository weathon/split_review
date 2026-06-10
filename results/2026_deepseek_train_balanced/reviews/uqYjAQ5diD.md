## Summary

FMapping proposes a factorized NeRF framework for real-time dense RGB-only mapping, operating in two stages: an initialization stage with noisy poses (using a self-supervised SDF–NeRF consistency loss), followed by an on-the-fly mapping stage that leverages a pre-trained depth covariance function (GP-based, borrowed from Dexheimer & Davison, 2023) to provide per-pixel depth priors and uncertainty-guided adaptive sampling. The core technical contribution is coupling a factorized (TensoRF-style) representation with covariance-guided sampling to focus samples on high-uncertainty surface regions, aiming for RGB-only mapping quality comparable to RGB-D methods.

## Strengths

- **Well-motivated pipeline design with clear architectural reasoning.** The two-stage framing (noisy initialization → stabilized on-the-fly mapping) addresses a genuinely difficult real-world problem. The paper includes a concrete comparison (Figure 4) showing that the factorized (BTD) representation outperforms tri-plane representation under noisy-pose initialization, providing empirical justification for a key design choice rather than asserting it.

- **Covariance-guided adaptive sampling is principled and clearly described.** The mechanism (Eq. 11–12) that uses per-pixel uncertainty $\sigma_n^2$ from the GP-based depth covariance function to enlarge truncation intervals for high-uncertainty rays is cleanly formalized. This goes beyond simply plugging in a depth prior and actually uses the uncertainty to guide where samples are allocated.

- **Real-time capability demonstrated with standard PyTorch.** The paper reports ~5 Hz depth inference without custom CUDA kernels (Table 2), and compares parameter count and model growth rate (scaling as O(L^(2/3))) against iMAP and NICE-SLAM. This efficiency claim is grounded in a concrete comparison.

- **Honest failure documentation.** The omission of Room1 results is explicitly noted in a Table 1 footnote ("the initialization stage does not generate satisfactory prior"), which adds credibility compared to papers that silently drop failure cases.

## Weaknesses

### Major

- **Evaluation is critically thin for the claims being made.** The paper claims "state-of-the-art RGB mapping" and "comparable to RGB-D dense mapping," yet experiments are conducted on **only one dataset** — Replica, which is synthetic. The depth covariance function was pre-trained on real data (ScanNet), making it especially important to validate on real sensor data. No real-world evaluation (ScanNet, TUM RGB-D, 7-Scenes) is provided. For a method aimed at "robot sensing and navigation," this is a significant gap.

- **No comparison against DIM-SLAM (Li et al., 2023), the most directly relevant baseline.** The related work section describes DIM-SLAM as "the first dense RGB SLAM system entirely based on the neural implicit mapping" and explicitly critiques its approach. Yet DIM-SLAM is completely absent from Table 1 and all experimental comparisons. The only RGB baselines are Orbeez-SLAM and a variant of NICE-SLAM without depth. This makes the claimed "state-of-the-art" status unverifiable.

- **No ablation studies.** The paper introduces multiple interacting components: (a) the factorized representation vs. a standard NeRF, (b) covariance-guided sampling vs. uniform or coarse-to-fine sampling, (c) the self-supervised SDF loss vs. photometric-only training, (d) the covariance depth loss vs. no depth prior. **None** of these components is ablated. Without ablations, it is impossible to attribute the reported performance to the claimed innovations rather than to engineering coincidences.

- **Room1 failure is noted but unanalyzed.** One test scene (out of what appears to be 5–6) fails completely, yet the paper provides no analysis of why the initialization fails on this scene, how frequently such failures occur, or under what conditions the method is robust vs. brittle. This undermines the reliability claims for a mapping system.

### Minor

- **The self-supervised SDF loss (Eq. 7) is a self-consistency constraint whose behavior is not validated.** The loss enforces consistency between SDF-derived depth and volume-rendered depth, but both quantities are outputs of the same learned representation. The paper does not analyze whether this loss actually improves geometry over photometric supervision alone (which would require the missing ablation), or whether it could converge to degenerate solutions where both branches agree on an incorrect surface. While not necessarily fatal — the photometric and warping losses provide external signal — the paper's silence on this point is a gap.

- **The noisy-pose noise model is never specified numerically.** The paper introduces a covariance matrix $Q$ for pose noise (Section 2) and a "noisy start" framing, but the actual experiments do not report what noise level was used, how it was injected, or whether results are sensitive to this parameter. This makes the initialization experiments difficult to reproduce or assess.

- **Reliance on a pre-trained covariance function without analysis of its reliability.** The depth covariance function (from Dexheimer & Davison, 2023) is the primary geometric prior, but the paper does not characterize when its depth predictions are accurate vs. inaccurate (beyond the Room1 failure), report the quality of $\tilde{D}_{l_*}$ against ground truth, or compare against simpler alternatives (e.g., monocular depth networks or warping-only approaches).

### Trivial

None.

## Nice-to-Haves

- Providing per-scene numbers (Table 1 is an image in the extracted version; machine-readable tables would aid verification).
- Reporting inference time per-frame breakdown (covariance estimation vs. NeRF rendering vs. sampling).
- Clarifying how the SDF and density fields are reconciled architecturally — the paper mentions both but does not explain whether density is derived from SDF or they are separate branches.

## Removed Points

These points were flagged but removed with justification:
- **"Numerical results are not readable in text"** — The tables-as-images issue is a parser artifact from PDF extraction; the original submission would have proper formatted tables. Removed per hard rule on formatting artifacts.
- **"Room1 results are silently omitted"** — The omission is documented in a footnote (line 211), not silent. The *analysis* of the failure is missing, which is addressed above.
- **"Self-supervised depth training has a fatal circularity problem"** — The SDF loss is a self-consistency constraint, but it is regularized by photometric and warping losses. The critic's speculation about "trivial solutions" is not grounded in any evidence from the paper. Demoted from a structural concern to a Minor weakness about lack of validation.
- **"Covariance function's role is overclaimed"** — The paper appropriately cites Dexheimer & Davison (2023) and does not claim to have invented the covariance function. The valid sub-points (no analysis of reliability, no comparison against alternatives) are folded into the Minor weaknesses above.
- **Strength: "Self-supervised depth from SDF–NeRF consistency without external depth"** — This conflicts with the verified weakness that the loss is not validated. Per rule, weakness wins; dropped.
- **Strength: "Honest failure-case documentation"** — Kept as a strength; the room1 footnote is genuinely honest. The lack of *analysis* is a separate weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between an interesting architectural idea and insufficient empirical validation, but do not expose any deeper insight about the problem or methodology that the paper itself does not discuss.

## Suggestions

1. **Add ablation studies on Replica** isolating at minimum: (a) the factorized representation vs. a standard MLP NeRF baseline, (b) covariance-guided sampling vs. standard hierarchical sampling, (c) the SDF loss vs. photometric-only training. Without these, the contribution cannot be assessed.

2. **Include DIM-SLAM as a baseline** in Table 1. Since the paper criticizes DIM-SLAM in the related work, it must compare against it numerically on the same benchmark.

3. **Evaluate on at least one real-world dataset** (ScanNet being the most natural choice since the covariance function was pre-trained on it). This is essential to support the practical relevance claims.

4. **Characterize the Room1 failure** — analyze what causes initialization to fail and report success rate statistics across scenes/random seeds.

5. **Specify the pose-noise parameters** used in the initialization experiments numerically, and consider a sensitivity analysis.

## Score and Decision

The paper addresses a real problem and has a coherent architecture with reasonable individual components. However, the experimental evaluation is not sufficient to support claims of "state-of-the-art RGB mapping" or "comparable to RGB-D dense mapping." The evaluation is limited to one synthetic dataset, omits the most directly relevant baseline (DIM-SLAM) from comparisons, contains no ablation studies, and does not analyze a documented failure case. These are major evidentiary gaps at the ICLR standard. The method may have merit, but the paper in its current form does not meet the bar.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>