- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8
Now I have all the evidence needed. Let me compose the consolidated review.

## Summary

This paper introduces Multilinear Operator Networks (MONet), a polynomial-based architecture for image recognition that uses **no activation functions** — only matrix multiplications and elementwise products. The core μ-layer captures multiplicative interactions between token elements via two branches with a Hadamard product. MONet achieves a ~10% absolute improvement over prior polynomial networks on ImageNet (77.0% vs 70.2%), matches MLP-based models like CycleMLP-T at comparable sizes (81.3%), and achieves state-of-the-art robustness on ImageNet-C (mCE 49.7). The paper also demonstrates exact symbolic recovery of the Lotka-Volterra ODE dynamics as a unique capability.

## Strengths

- **Large improvement over prior polynomial networks on ImageNet**: Table 1 shows Multi-stage MONet-T achieves 77.0% top-1 accuracy, a ~7–12% absolute improvement over the best prior polynomial nets without activations (Reg-Π-Nets at 70.2%, Π-Nets at 65.2%). This directly substantiates the claimed closing of the performance gap.

- **First polynomial network without activations to match modern MLP-based models**: Multi-stage MONet-S (81.3%) equals CycleMLP-T (81.3%) and exceeds ResMLP-24 (79.4%) and S2MLP-Deep (80.7%), despite those models using GELU activations. This provides concrete evidence that purely multilinear operations can compete with activation-based designs at practical model sizes.

- **State-of-the-art robustness on ImageNet-C without activations**: Table 3 reports the best mean Corruption Error (mCE = 49.7) among all compared models, outperforming HireMLP (51.9), CycleMLP (53.7), and all MLP/Transformer/CNN baselines. MONet leads in all four corruption categories.

- **Ablation study cleanly isolates the μ-layer's contribution**: Table 4 shows that replacing the μ-layer with an MLP layer drops accuracy from 82.94% to 55.11% (Linear Block) or 67.61% (Mix Block), confirming the core layer is essential rather than the token-based architecture itself driving performance.

- **Exact symbolic recovery of ODE dynamics**: Section 4.3 shows MONet recovers the Lotka-Volterra coefficients (1.56, 1.12001, 3.10, 1.21001 vs true 1.56, 1.12, 3.10, 1.21) — a unique interpretability capability not demonstrated by prior polynomial networks.

- **Pyramid patch embedding improves efficiency**: Table 5 shows multi-level embedding achieves 82.94% accuracy at 7.28 GFLOPs, compared to 83.08% at 28.14 GFLOPs for single-level patch size 7 — a practical efficiency gain without sacrificing accuracy.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistency between "solely multilinear" claim and use of layer normalization without addressing the FHE tension**: The abstract and introduction assert the model "relies *solely* on multilinear operations" (lines 5, 21), yet the architecture uses layer normalization (lines 93, 114). Layer normalization involves computing per-sample mean and variance, division, and square roots — operations that are *not* multilinear (addition and multiplication only) and are not directly supported by the FHE constraint used to motivate the work. The paper never acknowledges this tension, nor does it discuss whether layer normalization can be removed, approximated, or replaced under FHE. This is the **single most important issue the authors must address**. The core empirical contribution (strong results without activation functions) stands independently, but the framing around "solely multilinear" and FHE motivation is inaccurate as written. The limitation section (lines 436–438) discusses only theoretical characterization and does not mention this issue.

### Minor

- **Unsubstantiated claim about polynomial degree growth**: The paper asserts "Each block captures up to 4th degree interactions, which results in the final architecture capturing up to 4^N interactions" (line 120) without any proof, derivation, or formal argument. Proposition 1 is a trivial observation from Equation (1) — it merely states that the μ-layer captures multiplicative interactions. The 4^N claim is an unsupported assertion. A footnote punts the theoretical justification to future work. While this does not invalidate the empirical results, it overstates what the paper demonstrates.

- **Missing parameter counts in the robustness table (Table 3)**: The ImageNet-C results (lines 299–322) lack parameter counts for the compared models, making it harder to assess whether MONet's robustness advantage stems from architecture or capacity differences. Adding parameter columns would strengthen the comparison.

- **The comparison to prior polynomial networks is partially confounded by the shift from convolutional to token-based design**: The paper acknowledges (line 73) that prior polynomial nets use convolutions while MONet uses token-based MLP, but does not control for this in the comparison — the ~10% gain over Π-Nets on ImageNet conflates architectural paradigm shift with the μ-layer innovation. The ablation study (Table 4) does show the μ-layer is crucial relative to MLP layers, but a simple token-based degree-2 polynomial baseline (e.g., a single-branch expansion with elementwise squaring) would more directly isolate the contribution of the specific two-branch multiplicative structure.

- **The conclusion overstates results relative to transformers**: Line 433 claims "performance levels outperforms modern transformers models," while Table 1 shows MONet-S (81.3%) is essentially tied with DeiT-S (81.2%) — this is "on par with" rather than "outperforms across the board." The paper's own abstract correctly says "performs on par with modern architectures." The conclusion should be consistent with that more accurate framing.

### Trivial

- The Lotka-Volterra ODE experiment (Section 4.3) is presented without error bars or comparison to standard neural ODE methods. As a proof-of-concept of a unique capability this is acceptable, but adding statistical precision measures would improve rigor.

## Nice-to-Haves

- Include an ablation without layer normalization (or with a polynomial-compatible replacement like affine normalization) on ImageNet100 to clarify the FHE compatibility landscape.
- Add a simple token-based polynomial baseline (e.g., a single-branch expansion (AX)² in token space) to strengthen attribution of gains to the μ-layer's specific two-branch design.
- Include parameter counts in the robustness table (Table 3).

## Removed Points

These points from the input reviews are excluded for the following reasons:

1. "No results for larger MONet models (50M+ params)" — Scope creep. The paper demonstrates Tiny (10.3M) and Small (32.9M) models competitive with models of similar size; requesting larger-scale results is beyond reasonable expectation for a single paper.
2. "Missing comparison to ConvNeXt-T / Swin-T in ImageNet table" — The paper already compares against a wide range of CNN, Transformer, MLP, and polynomial baselines. No single paper can compare against every architecture. The existing coverage is adequate.
3. "No comparison to other neural ODE methods" — The ODE experiment is presented as a proof-of-concept of a unique capability (exact symbolic recovery), not as a benchmark competition. Evaluating against other ODE methods would be a separate contribution.
4. "Pyramid patch embedding description is too brief to reproduce" — While additional detail would be helpful, this is a presentation improvement rather than a weakness of the method itself.
5. "The FHE motivation statement is a bit strong" — This is a nuance-level concern without substantive impact on the evaluation.
6. "Missing intuition about why two branches are needed" — A nice-to-have clarity improvement, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths and weaknesses; the main novel observation from the synthesis is that the layer normalization tension is the most consequential issue and was not adequately elevated by either input review alone.

## Suggestions

1. **Address the layer normalization / FHE tension directly**: (a) Clarify whether the "solely multilinear" claim refers only to the core block (excluding pre-processing like normalization), or adjust the claim. (b) Discuss whether layer normalization can be removed, replaced with a polynomial-compatible alternative (e.g., learned affine transform), or approximated under FHE. (c) Add an ablation without layer normalization on ImageNet100 to quantify any accuracy impact. This is the most important revision needed.

2. **Substantiate or temper the 4^N degree claim**: Either provide a derivation showing how the composition of blocks yields exponential degree growth, or replace the claim with a more modest empirical observation (e.g., "deeper blocks capture higher-degree interactions, as evidenced by the depth ablation in Table 6").

3. **Add a simple token-based polynomial baseline**: Include a variant where the μ-layer is replaced by a single-branch polynomial expansion (e.g., (AX)² or AX + (AX)²) to isolate the benefit of the two-branch multiplicative design from the token-based architecture.

4. **Add parameter counts to the robustness table (Table 3)** so readers can assess whether MONet's robustness advantage is due to architecture or capacity.

5. **Fix the conclusion wording**: Replace "outperforms modern transformers models" with "performs on par with modern architectures" to match the paper's own evidence.
