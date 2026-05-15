Now I have all the information needed to produce the consolidated review. Let me synthesize everything carefully.

## Summary

The paper proposes RDNet, a Reversible Decoupling Network for single image reflection removal (SIRR). It introduces two main innovations: (1) a multi-column reversible encoder (MCRE) that uses reversible connections between levels and columns to preserve information during feature decoupling, and (2) a transmission-rate-aware prompt generator (TAPG) that estimates per-channel transmission rate parameters and uses them to modulate features for better generalization to real-world reflection variations. The method achieves state-of-the-art PSNR/SSIM on five standard benchmark datasets under the with-Nature-data training setting, with consistent SOTA or near-SOTA results in the without-Nature setting.

## Strengths

- **Novel architecture that advances the SIRR paradigm.** The multi-column reversible encoder is a genuine architectural contribution — it goes beyond the standard dual-stream interaction designs (YTMT, DSRNet) by introducing reversible cross-level and cross-column connections. The ablation (Setting F) shows a 2.6 dB drop when reversible connections are replaced with U‑Net connections, confirming the importance of this design choice (even if the ablation is not perfectly isolated). The approach of applying reversible architectures to the decoupling (rather than generation) problem in reflection removal is well-motivated.

- **Consistent SOTA results across multiple benchmarks.** In the with-Nature-data setting, RDNet achieves the top PSNR on all five datasets (Real20: 25.58, Objects: 26.78, Postcard: 26.33, Wild: 27.70, Nature: 26.21). In the without-Nature setting, it achieves best PSNR on 4 of 5 datasets (Real20, Postcard, Wild, Average). The improvements are particularly notable on the challenging Real20 dataset (+1.35 dB over DSRNet in w/o Nat., +1.67 dB in w Nat.).

- **Well-designed prompt generator with clear ablation.** The TAPG is a sensible solution to the synthetic-to-real domain gap caused by varying transmission rates. The ablation cleanly decomposes the contribution: removing all transmission-rate awareness drops 1.13 dB (Setting A vs. Ours), and the naive input-correction baseline (Pre.) recovers only 0.47 dB of this gap, while the full prompt-based modulation recovers the full amount. This demonstrates that feature-level modulation is superior to input-level adjustment.

- **Strong qualitative results on in-the-wild cases.** The paper shows challenging real-world examples with dense reflections that defeat all competitors, where RDNet produces nearly complete reflection removal. This validates practical applicability beyond constrained benchmarks.

## Weaknesses

### Fatal
None.

### Major

1. **The reversibility claim is asserted without rigorous analysis, and the key ablation is confounded.** The paper states in Eqs. 3–4 that the cross-column connection is "information lossless" because one can reconstruct \(F_j^{i-1}\) from \(F_j^i\) via the reverse operation. While this claim is mathematically valid *locally* (the \(\gamma\) scaling is invertible and the \(\omega\) term can be recomputed from available features), several issues remain unaddressed: (a) The paper never analyzes whether the *full multi-column computation* is globally reversible — the reverse path for a single connection depends on values from neighboring levels/columns whose own reversibility is not established. (b) The functions \(\omega\), \(\theta\), and \(\delta\) are never specified beyond their names; without knowing whether \(\omega\) contains down/upsampling or other non-injective operations, the practical reversibility chain is unclear. (c) Critically, the ablation that claims to demonstrate the necessity of invertibility (Setting F: "replace the reversible connection with the U-Net connection") confounds multiple architectural differences — skip connectivity pattern, parameter sharing, memory footprint, and information flow topology — and does not isolate the invertible property. A cleaner control (e.g., replacing \(\gamma F_j^{i-1}\) with a plain residual connection \(F_j^{i-1}\) while keeping the \(\omega\) term) would be needed to attribute the 2.6 dB gap specifically to reversibility.

2. **The multi‑column encoder's advantage over simpler alternatives is marginal.** The ablation shows that replacing the multi-column design with a dual-stream variant (Setting D) causes only a 0.28 dB drop (26.65 → 26.37), despite "double computation." Given that the multi-column architecture is presented as a core contribution grounded in the part-whole hierarchy (GLOM) and information preservation, a 0.28 dB improvement — without reported variance — provides weak empirical justification for the added complexity. This undercuts the paper's central architectural narrative.

3. **The prompt generator's architecture from 6 scalars to a full feature map is underspecified.** The paper states that a "three-layer MLP" maps the six estimated parameters \((\alpha_{RGB}, \beta_{RGB})\) to a prompt \(P \in \mathbb{R}^{C \times H \times W}\) with \(C=64\). An MLP with 6 inputs cannot directly produce a 3D tensor of spatial dimensions \(H \times W\); there must be a spatial broadcasting mechanism, a learned basis expansion, or a conditional normalization scheme. This detail is critical for reproducibility and is not explained. Additionally, the training procedure for the transmission-rate estimator is described only briefly ("first stage, we train the estimator"), and the paper does not report how accurately it estimates \(\alpha,\beta\) on synthetic data where ground truth is known — making it difficult to assess whether the prompt generator's benefits come from accurate rate estimation or from learned feature modulation that could be achieved by other means.

### Minor

1. **The ablation table's training setting is not specified.** The "Ours" entry in the ablation table reports average PSNR 26.65 dB, which matches the with-Nature-data setting in Table 1 — but the ablation text never states which data split or hyperparameters are used. This makes the ablation results uninterpretable in isolation and prevents readers from comparing them directly to the main results.

2. **The number of columns \(N\) is never stated.** The notation \(i \in \{1, 2, \ldots, N\}\) is introduced but \(N\) is not specified anywhere in the paper, including the implementation details. This is a basic architectural parameter that should be reported.

3. **Several implementation details are missing.** The structure of \(\omega\) (described only as "the network operation"), the design of the Level Decoder and its "multiplication modulation," and the specific architecture of the hierarchy decoder are not described beyond high-level statements. While some of these could be inferred from the figure or code release, the paper would benefit from more precise specification.

### Trivial

- The radar chart (Fig. 1) caption does not specify which training setting (with/without Nature data) is used. Since Nature results are included, the chart presumably uses the with-Nature setting, but this should be explicit.

## Nice-to-Haves

- Reporting results with variance (e.g., 3 random seeds with mean and std) would help assess the significance of the small margins (0.04–0.17 dB on some benchmarks).
- An ablation that isolates reversibility more cleanly — e.g., replacing \(\gamma F_j^{i-1}\) with a standard residual connection \(F_j^{i-1}\) while keeping all other components identical — would substantially strengthen the paper's core claim.
- Visualizing learned features across columns to demonstrate progressive decoupling would add qualitative support for the information-preservation narrative.

## Removed Points

These points from the harsh critic were flagged for removal with justification:

- **Criticism that \(\omega\) containing non-invertible operations invalidates reversibility:** This reflects a misunderstanding of coupling-based reversible networks. In standard reversible blocks (Eq. 2), the coupling functions \(\mathcal{F}\) and \(\mathcal{G}\) can also be non-invertible — reversibility comes from the additive coupling structure, not from component invertibility. The paper's Eq. 3–4 follow the same principle. **Removed** (factually incorrect about coupling layer theory).

- **Claim that the paper contradicts itself on "new records on all 5 datasets":** The critic points to the w/o-Nat. setting where Ours loses on Objects (25.76 vs. 26.28). However, the radar chart (Fig. 1) includes Nature dataset results, which are only available in the with-Nature setting — where Ours does achieve best PSNR on all five datasets. The paper's claim is consistent in context, though the caption could be clearer. **Removed** (not a factual contradiction).

- **Claim that the 24.34 dB prompt-generator baseline "is not a meaningful baseline":** The paper uses this number as a sanity check to show the estimated parameters carry meaningful signal, not as a competing method. This is standard practice. **Removed** (misreading of the paper's intent).

- **Criticisms about 20 epochs, batch size 2, fixed learning rate:** These are standard hyperparameter choices, not unusual for this setting. Many SIRR methods use similar configurations. **Removed** (nitpick, not a genuine weakness).

- **Criticism about missing variance/statistical significance:** Single-run evaluation on fixed benchmarks is the norm in SIRR literature. Moved to Nice-to-Haves. **Removed from weaknesses** (not a standard requirement for this field).

- **Criticism that missing related works are not discussed:** The paper provides a thorough review of relevant SIRR methods and reversible networks for low-level vision. **Removed** (not verifiable and adequately covered).

- **Pure formatting/style nitpicks** about notation ambiguity, figure choices, etc. — These are either addressed in the paper or are parser artifacts. **Removed**.

## Novel Insights

None beyond the paper's own contributions. However, one subtle point emerges from the review process: the paper's reversible connection (Eq. 3) is structurally different from standard additive coupling layers (Eq. 2). In standard coupling, the split is along the channel dimension of a single tensor; here, reversibility operates across *columns* at the same level, using features from lower- and higher-level representations. This is a genuinely different application of the reversible principle — it preserves cross-level feature reuse rather than enabling memory-efficient backpropagation. The paper does not frame this distinction explicitly, and readers familiar with standard reversible networks (e.g., RevNet) may incorrectly assume the same memory-saving benefits apply.

## Suggestions

1. **Specify the missing architectural details:** Report the number of columns \(N\), describe the \(\omega\) network structure, and explain how the 3-layer MLP maps 6 scalars to a \(64 \times H \times W\) prompt tensor (e.g., broadcast, learned basis, or spatial feature map generation).
2. **Add a cleaner invertibility ablation:** Replace the \(\gamma F_j^{i-1}\) term with a simple residual connection \(F_j^{i-1}\) while keeping all other components identical. This would isolate the effect of reversibility from other architectural differences.
3. **State which training setting the ablation table uses** — the numbers match the with-Nature setting, and this should be explicit.
4. **Report the prompt generator's estimation accuracy** on synthetic data where ground-truth \(\alpha,\beta\) are known, to validate that it learns meaningful physical parameters rather than just learned feature modulation.
5. **Clarify the Fig. 1 radar chart caption** to specify the training setting.

## Score and Decision

This paper makes a genuine architectural contribution to SIRR and achieves consistent SOTA results. The weaknesses are real but not fatal: they concern presentation completeness and the strength of causal evidence for specific design choices, not the validity of the overall method. The paper would benefit from cleanup but is solid in its current form.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>