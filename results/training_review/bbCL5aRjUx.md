Now I have all the information needed to verify the claims. Let me construct the final consolidated review.

---

## Summary

This paper introduces MONet, a polynomial network architecture that replaces all activation functions with multilinear operations (elementwise products of linear projections). The core building block is the PolyMLP layer, which stacks bilinear transformations with shortcut connections. MONet is the first polynomial network to achieve competitive ImageNet accuracy (81.3% top-1, 32.9M params) without any activation functions, and it demonstrates strong robustness on ImageNet-C (mCE 49.7). The work is motivated by compatibility with fully homomorphic encryption (FHE), which allows only additions and multiplications.

## Strengths

- **First no-activation architecture competitive on ImageNet**: MONet-S achieves 81.3% top-1 accuracy with 32.9M parameters and zero activation functions, improving over prior polynomial networks (Π-Nets: 65.2%, Regularized Π-Nets: 70.2%) by more than 10 points. This is shown in Table 2. The ablation in Table 5 confirms that replacing the PolyMLP layer with a standard MLP collapses accuracy from 82.94% to 67.61% on ImageNet100, isolating the core contribution.

- **State-of-the-art robustness on ImageNet-C**: MONet achieves the lowest mean Corruption Error (mCE=49.7) among all compared methods, outperforming DeiT (54.6), Swin (62.0), CycleMLP (53.7), and prior polynomial networks (73.8). It wins in all Weather and Digital corruption subcategories (Table 4). This is a concrete, practically relevant advantage.

- **Clean, principled architecture with clear motivation**: The design replaces activation functions with a mathematically well-defined multilinear operator, is simple to implement, and has a genuine use case in FHE-constrained settings. The paper correctly identifies this niche and the ablation study convincingly attributes the performance to the multiplicative interactions, not to architectural scaffolding.

## Weaknesses

### Fatal
None.

### Major

- **Neural ODE experiment lacks methodological detail on symbolic extraction**: The paper claims MONet can "recover the equations behind the dynamic system and explicitly restore the symbolic representation" (Section 3.3), showing coefficients recovered to within 0.00001 of ground truth (e.g., 1.12001 vs. 1.12). However, **no mechanism is described** for how the symbolic equation is extracted from the trained model. MONet is a deep architecture with many parameters and multiple PolyMLP blocks — how a composition of bilinear layers with shortcuts maps back to a sparse, 2-equation quadratic ODE is unexplained. There is no discussion of sparsity-inducing regularization, single-block constraints, post-hoc symbolic regression, or weight analysis. Without this, the experiment cannot be reproduced or assessed, and the claimed interpretability advantage over black-box neural ODE solvers is unsubstantiated. (Section 3.3, Equations 4–5)

- **Missing key modern baselines from the main ImageNet table**: Table 2 omits several standard modern architectures that would provide a clearer picture of where MONet stands. Most notably, **Swin-T (81.3% top-1, 29M params)** is absent from the main table even though the authors include Swin results in the robustness experiments (Table 4). ConvNeXt-T and EfficientNet are also missing. The paper claims performance "on par with modern architectures," but without these baselines in the main comparison, the claim is insufficiently supported. The conclusion statement "outperforms modern transformers models across a range of challenging benchmarks" (line 433) is an overclaim — MONet-S (81.3%) ties with CycleMLP-T (81.3%) and is within 0.1% of DeiT-S/16 (81.2%); it does not clearly *outperform* them.

- **The 4^N degree-of-interaction claim is unsubstantiated**: The paper states (line 120) that each block captures up to 4th-degree interactions and that N blocks capture up to 4^N interactions, with N > 10 in practice. No derivation or proof is provided. The Proposition in Section 3.1 merely restates that the layer captures multiplicative interactions. The depth ablation (Table 7) shows diminishing returns beyond depth 12, but this does not validate exponential growth in interaction degree. The authors acknowledge this gap ("left as future work" in a footnote), but the claim is nevertheless presented as a property of the architecture without support. Either provide a theoretical characterization or qualify the claim more carefully.

### Minor

- **Pyramid patch embedding framing is misleading**: The paper claims pyramid patch embedding "enhances overall performance" (line 121) and "improves performance" (Section 4.5). However, Table 6 shows that **single-level patch size 7 achieves higher top-1 accuracy (83.08%) than the best pyramid scheme (14,7 → 82.94%**), albeit at much higher FLOPs (28.14 vs. 7.28). The pyramid scheme improves over *patch size 14* (79.54%) and dramatically reduces FLOPs relative to patch 7. The contribution should be framed as an *efficiency* improvement — not a performance improvement. The text referring to a single-level baseline of "81.78%" does not match any entry in the table and needs clarification.

- **The comparison with prior polynomial networks conflates multiple architectural changes**: The paper frames the 10%+ improvement over Π-Nets as evidence of the proposed module's superiority. However, prior polynomial nets use convolutional backbones, few layers, and different input representations, while MONet adopts a token-based design with pyramid embedding, spatial shift, deep stacking (32–45 blocks), and large hidden dimensions. While the ablation (Table 5) does isolate the PolyMLP layer's contribution on ImageNet100, the ImageNet-scale comparison mixes many design choices. The framing should acknowledge that the improvement reflects a full architectural redesign, not just the operator change.

- **Low-rank bilinear factorization not cited**: The decomposition Λ = BD in Equation (1) is a standard low-rank factorization for bilinear models (similar to factorized bilinear models, FiLM-style conditioning, etc.). The paper does not cite relevant prior work on low-rank bilinear methods, which would help position the technical contribution.

### Trivial
None.

## Nice-to-Haves

- Include Swin-T, ConvNeXt-T, and other common modern architectures in the main ImageNet comparison table to substantiate the "on par" claim.
- Report FHE inference cost (number of multiplications, concrete latency estimates) to back the FHE motivation with quantitative evidence.
- For robustness experiments (Table 4), include parameter counts for all compared models to enable fair comparison by model size.
- Visualize the learned bilinear interactions (e.g., heatmap of A, B matrices or Gram matrix) to illustrate what multiplicative patterns are captured.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Row coloring confusing"* (Critic #3): This is a formatting/presentation nitpick about LaTeX rowcolor naming. The PDF rendering is likely correct as intended. *Reason: formatting nitpick per Hard Rules.*
- *"The paper does not acknowledge that the token-based design is borrowed directly from MLP-Mixer"*: The paper explicitly states (Related Work, lines 73) that it is "inspired by the modern setup of considering the input as a sequence of tokens" and that this departs from prior polynomial nets. The borrowing is acknowledged. *Reason: strawman — the paper already addresses this.*
- *"Missing FHE inference cost characterization"*: This is a nice-to-have extension, not a weakness of the presented experiments. *Reason: scope creep — the paper's core claim is architectural, not about FHE deployment analysis.*
- *Strength Finder's claim about "pyramid patch embedding improves accuracy"*: The single-level patch 7 (83.08%) outperforms pyramid (82.94%). *Reason: conflicts with verified weakness (accuracy is slightly lower), so the strength must be dropped per rules.*
- *Strength Finder's claim about "Exact symbolic recovery of ODE dynamics" as unqualified strength*: The methodological gap (no extraction mechanism described) undermines the strength. *Reason: conflicts with verified weakness.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful tension: MONet's core innovation (eliminating activation functions via multilinear operations) is validated by clean ablations, but several evidential gaps (ODE extraction, 4^N derivation, incomplete baselines) prevent the paper from fully establishing its claimed advantages. The robustness results, however, stand out as a genuinely surprising and underexplored benefit of the multilinear design.

## Suggestions

1. **Clarify the ODE extraction methodology** — or drop the experiment. Explain whether sparsity constraints, single-block models, or post-hoc symbolic regression were used. Without this, the interpretability claim is not reproducible.
2. **Add Swin-T and at least one ConvNeXt variant to Table 2** — these are standard baselines and their absence weakens the "on par with modern architectures" claim.
3. **Tone down the conclusion** — "outperforms modern transformers" is not supported by the numbers (ties with CycleMLP-T, within 0.1% of DeiT-S/16). Replace with "competitive with."
4. **Re-frame the pyramid patch embedding** as an efficiency-performance trade-off, not a strict accuracy improvement.
5. **Provide a derivation or experimental bound** for the 4^N interaction degree claim, or remove it. A simple test on synthetic polynomials of known degree would suffice.

## Score and Decision

This paper makes a genuine contribution — a no-activation architecture achieving ImageNet-level performance — and the robustness results are compelling. However, the paper is weakened by overclaiming (especially in the conclusion and the ODE experiment), incomplete baselines, and unsubstantiated theoretical claims. These issues are addressable in revision but prevent the paper from establishing its full contribution in its current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>