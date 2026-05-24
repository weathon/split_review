Now I have all the information I need. Let me write the final consolidated review.

## Verifications performed:

1. **Abstract vs. Table numbers**: Abstract claims "+8.5% over fully-finetune, +7% over VPT, +3.2% over LoRA." Table 1 overall means: SAN 79.26 vs. Full 71.76 = **+7.50%** (not 8.5%); SAN vs. VPT-Deep 74.62 = **+4.64%** (not 7%); SAN vs. LoRA 76.12 = **+3.14%** (≈3.2, fine). **Verified discrepancy.**

2. **Recalibration (Eq. 12–13)**: Present in methods (lines 174–191) with learnable A^l, b^l. **Nowhere** in experiments, ablation, or conclusion. Parameter counts are identical to SSF (0.34%). **Verified as unevaluated.**

3. **Fine-grained claim**: Eq. 5 shows scaling is γ^l ⊙ γ^{l-1} ⊙ w^l — outer product of two vectors, so O(d) degrees of freedom, not O(d²). The paper acknowledges this is "rank size equal to one" (line 37). **Claim is technically true but the framing is strong.**

4. **Regularization claim**: Eq. 6–8 derive a quadratic effect under a "simplified two-layer linear network scenario without any activation and normalization" (line 125). The paper calls this "implicit regularization." The derivation is caveated. **Not a flaw as presented.**

5. **No variance reported**: Verified — single numbers in Table 1. **True but common in PEFT benchmarks.**

---

## Summary

The paper proposes SAN, a parameter-efficient fine-tuning method that learns per-channel scaling factors for features and explicitly propagates them to the weights of the next layer, drawing inspiration from heterosynaptic plasticity. Experiments across 26 datasets with ViT, Swin, and ConvNeXt backbones show strong performance.

## Strengths

- **Large and consistent performance gains across 26 datasets**: Table 1 shows SAN achieves the highest mean accuracy (79.26%) on VTAB-1k using only 0.34% parameters, outperforming full fine-tuning (71.76%), LoRA (76.12%, 0.89% params), and SSF (77.68%, 0.34% params) — the top competitor with the same parameter budget. Gains are consistent across FGVC, VTAB-1k, and general classification.

- **Novel explicit propagation mechanism with formal justification**: Section 3.2.4 (Eq. 9–13) provides a clear mathematical derivation showing that any linear feature transformation implicitly affects the next layer's weights, and SAN makes this propagation explicit. This is a genuine conceptual contribution that distinguishes the method from prior feature-tuning approaches (SSF, LoRA) that only consider current-layer effects.

- **Ablation study validates both components**: Figure 4 demonstrates that using only feature scaling ("modeling") or only propagation gives lower accuracy than combining them, providing direct evidence that the cross-layer propagation is responsible for SAN's improvement.

- **Consistent across three diverse backbone architectures**: Figure 2 shows SAN achieves the highest accuracy on ViT-B, Swin-B, and ConvNeXt-B, demonstrating generality beyond transformer-based models. LoRA degrades on ConvNeXt, while SAN maintains its lead.

- **Extreme parameter efficiency**: SAN uses only 0.34% of model parameters (same as SSF) while outperforming methods with higher parameter budgets (e.g., LoRA at 0.89%, VPT-Deep at 0.81%).

## Weaknesses

### Major

- **Abstract numbers are inconsistent with the main results table.** The abstract claims "+8.5% over fully-finetune, +7% over Visual Prompt Tuning, and +3.2% over LoRA." From Table 1 overall means: SAN 79.26 vs. Full fine-tune 71.76 → **+7.50%** (not 8.5%); SAN vs. VPT-Deep 74.62 → **+4.64%** (not 7%); SAN vs. LoRA 76.12 → **+3.14%** (≈3.2, acceptable rounding). The first two figures are materially wrong — the gap for VPT is overstated by nearly 50%. This must be corrected. The paper also states "using only 0.20% of the parameters" (line 283) which conflicts with the table's 0.34% overall mean.

- **The adaptive recalibration (Eq. 12–13) is described in the method but never evaluated.** Section 3.2 introduces learnable matrices A^l and b^l as a mechanism to handle nonlinearities during propagation. However: (1) the parameter counts reported in Table 1 are identical for SAN and SSF (0.34%), impossible if per-layer A^l (d×d) and b^l (d) were used; (2) the ablation study (Fig. 4) evaluates only "modeling" and "propagation" with no mention of recalibration; (3) the conclusion does not discuss it. This means the paper presents a more complex method than what was actually implemented and evaluated. This needs to be resolved: either confirm recalibration was used (with corrected parameter counts and ablations) or remove it from the method description.

### Minor

- **No statistical variance reported.** The main results (Table 1) and backbone comparison show single numbers per method per dataset. Given the small margins on several entries (e.g., ImageNet-1k: SAN 83.69 vs. Full 83.58, +0.11%; CIFAR-100: SAN 94.11 vs. SSF 93.99, +0.12%), it is not possible to assess whether these improvements are meaningful. While single-run reporting is common in this benchmark setting, the paper's claims of superiority would be strengthened by multiple seeds with standard deviations.

- **"Fine-grained adjustment per parameter" framing is slightly strong.** The paper claims SAN achieves "a unique adjustment value for every individual parameter" (line 113). Technically true — each weight entry w_{i,j} is scaled by γ^l_i · γ^{l-1}_j, which can differ per entry. However, the scaling matrix is the outer product of two length-d vectors, giving O(d) effective degrees of freedom, not O(d²). The paper does acknowledge this is "a degraded LoRA with rank size equal to one" (line 37), but the method-section framing could mislead readers into thinking the expressivity is greater than it is.

- **The implicit regularization analysis (Eq. 6–8) is derived under an idealized linear two-layer network without activations or normalization.** The paper acknowledges this simplification (line 125), but the regularization is presented as a property of the method without experimental evidence (e.g., showing that γ values stay closer to 1 than SSF's). The quadratic damping effect would break under nonlinearities, so the practical significance of this analysis is unclear.

- **Some cases where SAN underperforms baselines are not discussed.** For example, on Clevr/distance: LoRA 66.90 > SAN 61.40; on SmallNORB/azi: LoRA 32.20 > SAN 30.30; on CIFAR100: VPT-Shallow 77.70 > SAN 74.30. A discussion of these failure cases would improve the paper's scientific rigor.

### Trivial

- None.

## Nice-to-Haves

- Comparison with rank-1 LoRA would isolate the benefit of SAN's specific scaling structure versus a LoRA variant with the same rank.
- Reporting training time / convergence behavior vs. SSF and LoRA would be useful for practitioners evaluating the method.
- Clarifying whether VTAB-1k follows the standard 1k-shot protocol with validation splits would aid reproducibility.

## Removed Points

These points were flagged by reviewers but are removed as invalid, misread, or non-substantive:

- **"Neuroscience analogy is untested / generates no falsifiable hypothesis"** — The analogy is used as motivation, not as a technical claim. Evaluating papers on their stated technical contributions, not their metaphors. Removed as scope creep.
- **"Missing hyperparameter details / baseline configurations"** — The paper states it "follows the protocol established by SSF" (line 220), which is standard practice in this benchmark line. Removed as non-substantive.
- **"Backbone comparison only on three datasets"** — Three backbones across a benchmark is a standard breadth of evaluation. The chart uses mean accuracy. Removed as unrealistic expectation.
- **"Regularization is not added to the loss / post-hoc rationalization"** — The paper explicitly frames this as an *implicit* regularization effect emerging from propagation structure (Eq. 6–8), under a stated simplified linear scenario. This is a valid theoretical analysis, not a misrepresentation.
- **"PEFT methods didn't overlook propagation / LoRA does affect next layer"** — The paper's framing is about *explicit vs. implicit* propagation, which it acknowledges. Removed as a misreading of the paper's argument.
- **Strength Finder: generic strengths** — Strengths like "addressed an important problem" were removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced two concrete problems (abstract-table mismatch, untested recalibration) but did not generate a new scientific insight about the method itself.

## Suggestions

1. **Correct the abstract** to match the numbers in Table 1 (e.g., +7.5% over full fine-tune, +4.6% over VPT-Deep). Also correct the "0.20% parameters" claim on line 283.
2. **Resolve the recalibration issue**: either confirm it was used (with evidence and corrected parameter counts) or remove Eq. 12–13 and the associated text from the method section, clearly stating it as a potential future extension.
3. **Add variance** (mean ± std over 3–5 seeds) for key results, or at minimum for the overall means, to establish statistical significance.
4. **Discuss failure cases** (Clevr/distance, SmallNORB/azi, CIFAR100 Natural subset) where SAN underperforms baselines, to improve scientific rigor.
5. **Tone down or clarify** the "fine-grained per-parameter" claim to avoid implying O(d²) expressivity.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>