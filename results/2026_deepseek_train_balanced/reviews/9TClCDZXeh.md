Now let me produce the final review.

## Summary

This paper introduces WGATR, a fully-learnable neural surrogate for wireless signal propagation that applies an E(3)-equivariant Geometric Algebra Transformer (GATr) with a custom tokenizer to encode 3D scene geometry, antenna positions, and orientations into projective geometric algebra tokens. The paper additionally contributes two new simulated wireless datasets (Wi3Rooms and WiProcTHOR) and evaluates across forward prediction, inverse receiver localization, and diffusion-based probabilistic inference on both simulated and real-world data.

## Strengths

- **Near-perfect robustness to symmetry transformations from built-in E(3)-equivariance**: Table 1 shows that under scene rotation, WGATR's MAE stays at 0.74 dB on Wi3Rooms while the vanilla Transformer catastrophically degrades to 78.68 dB. Under translation, WGATR remains at 0.74 dB vs. 64.05 dB for the Transformer. This is direct, quantitative evidence that the equivariant architecture delivers on its core design goal — the contrast is unambiguous and cannot be explained away by implementation noise.

- **Real-world validation demonstrates practical viability**: On the DICHASUS dataset, WGATR achieves >35% lower error than hybrid techniques and >70% lower error than a calibrated wireless ray tracer (Section 5.4, Fig. 4). Real-world validation of neural wireless surrogates is rare, and the fact that a fully-learned approach closes the sim-to-real gap against hybrid methods that incorporate physical priors is a practically significant result.

- **First fully-learned surrogate operating on full 3D geometry rather than 2D/2.5D representations**: The paper (line 104) correctly identifies that prior work uses lossy 2D representations. The GA tokenizer maps mesh faces to planes, antenna positions to points, and orientations to vectors in PGA space — a principled design that enables the 3D+orientation reasoning that 2D approaches cannot capture. The ablation (line 227) confirms that this tokenization scheme provides benefits over a simple sequence of 3D positions.

- **Sample efficiency demonstrated with multiple evidence sources**: WGATR achieves an MAE of 0.64 dB using only 10% of the training data, surpassing PLViT (1.28 dB) and a vanilla Transformer (0.69 dB) trained on the full dataset (Fig. 2). The data efficiency curves across both datasets are consistent and show WGATR dominating at every data regime.

- **Differentiability enables inverse problems that competing baselines cannot solve**: WGATR's full differentiability w.r.t. simulation parameters (line 42) enables receiver localization via gradient descent achieving accuracy up to 60 cm (Fig. 3). The paper honestly notes that neither SEGNN nor PLViT are differentiable with respect to object positions in their official implementations (footnote, line 290), giving WGATR a functional capability that competing architectures lack.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Table 1 (main results) reports only point estimates without variance information.** No standard errors, confidence intervals, or multi-seed results are provided for the principal quantitative evidence. While the gaps between WGATR and non-equivariant baselines are so large (e.g., 0.74 vs. 78.68 dB under rotation) that they are clearly robust, the identical MAE values across multiple conditions for WGATR (e.g., 0.41 for nearly every condition on WiProcTHOR) would be more interpretable with variance estimates to distinguish genuine invariance from a floor effect or rounding coincidence. The localization figure (Fig. 3) does include error bands, showing the authors have the machinery to report uncertainty — its absence from the main results table is a gap.

- **Real-world validation is on a single simple hallway that does not test the paper's core geometric reasoning claim.** The DICHASUS evaluation (Section 5.4) is conducted in a hallway with two receiver arrays and an occluded corridor — minimal geometric complexity. The paper honestly acknowledges this (line 367: "we attribute this to simplicity of the dataset, where symmetry transformations of 3D space are neither observed nor required"), but the consequence is that the headline real-world claims (>35% and >70% error reduction) are demonstrated in an environment that does not distinguish WGATR's distinguishing feature (equivariance) from a well-tokenized Transformer. The paper's central thesis — that geometric inductive biases are the key enabler — remains tested only on simulated data.

- **Tokenizer ablation claims are stated qualitatively without supporting numbers in Table 1.** The paper mentions "a transformer without it, which represents the scene as a simple sequence of 3D positions" (line 208) and states "we find clear benefits of our wireless tokenizer" (line 227), but the corresponding numerical comparison does not appear in the main results table. Quantifying this ablation would strengthen the tokenizer's claimed contribution.

- **Inference speed is advertised as an advantage but never quantified.** The paper mentions test-time speed (line 230, line 376) as a benefit but provides no wall-clock timing comparison against any baseline or against the ray tracer. If speed measurements exist, they should be reported; if not, the speed claim should be tempered.

- **PLViT comparison details are underspecified.** PLViT's MAE of 4.52 dB on Wi3Rooms (roughly 4–7× worse than other methods) is so large that a reader cannot assess whether this reflects a fundamental limitation of 2D representations or an artifact of how PLViT was adapted to a non-grid evaluation protocol. A brief sentence describing how PLViT was adapted (2D resolution, input representation, handling of sparse Tx/Rx coordinates) would clarify whether the comparison is fair or inadvertently staged.

### Trivial

None.

## Nice-to-Haves

- A more complex real-world evaluation (multi-room, varied materials, non-line-of-sight configurations) would directly test the geometric equivariance claims. The authors correctly note that collecting such data is expensive, so this is aspirational rather than a required fix.
- Parameter counts for WGATR vs. baselines would help contextualize scaling and efficiency comparisons.
- A brief explanation of how negative ELBO values arise in the diffusion geometry reconstruction results (Table 2) would help readers unfamiliar with continuous-data likelihood parameterizations.

## Removed Points

These points were flagged by reviewers but removed during consolidation. They are documented here for completeness but should be treated with caution:

- **"Paper does not demonstrate WGATR is better than other equivariant approaches"** (Harsh Critic, Issue 3): This is factually incorrect. Table 1 shows WGATR (0.63) beating SEGNN (0.92) on Wi3Rooms Rx interpolation, and WGATR (0.74) beating SEGNN (1.02) on unseen floor plans and under symmetry transformations. The paper does demonstrate superiority over the one other equivariant method it could fit in memory.
- **Tokenizer details deferred to appendix**: Per the review guidelines, appendix content stripped by the PDF parser should not be flagged as a weakness.
- **Model sizes and training hyperparameters absent**: Per the review guidelines, undisclosed implementation details that are standard appendix content are reproducibility nitpicks, not review weaknesses.
- **"Abstract claim about 10% data not verifiable from tables alone"**: The claim is directly supported by Fig. 2, which is a standard way to present data efficiency curves. This is not a weakness.
- **"Datasets are not yet a contribution the community can build on"**: Release status of datasets is orthogonal to the paper's scientific contribution and is speculative at this stage.

## Novel Insights

None beyond the paper's own contributions. The core insight — that E(3)-equivariant Geometric Algebra Transformers, when equipped with a properly designed tokenizer for wireless primitives, provide substantial robustness and sample efficiency gains over non-equivariant alternatives — is the paper's contribution and is well-supported by the evidence.

## Suggestions

1. Add standard errors, confidence bands, or multi-seed results to Table 1. The localization figure already includes error bars (Fig. 3, caption mentions standard error), so the infrastructure exists.
2. Quantify the tokenizer ablation numerically — either report the "transformer without the tokenizer" results in Table 1 or in a dedicated ablation table.
3. Provide wall-clock inference speed comparisons (WGATR vs. baselines vs. ray tracer) or remove the unquantified speed claims.
4. Add a sentence specifying how PLViT was adapted to the evaluation protocol (input resolution, representation of sparse coordinates, any architectural modifications).
5. Clarify in the main text that the real-world results, while practically impressive, are in a geometrically simple setting that does not exercise the equivariance properties — the paper already hints at this in line 367 but the abstract and introduction do not qualify the real-world claims accordingly.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>