Now I have a complete understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes AutoLoRa, a robust fine-tuning (RFT) framework that disentangles adversarial and natural objective optimization by routing natural objectives through a low-rank (LoRa) branch and adversarial objectives through the feature extractor (FE). The paper first identifies that prior RFT methods (vanilla RFT, TWINS) suffer from divergent gradient directions when optimizing both objectives through the FE (Figure 1a). AutoLoRa resolves this by introducing a parameter-efficient LoRa branch (<5% of FE parameters) that processes natural data, while the FE only processes adversarial data, with a KL distillation term connecting them. Additionally, the paper proposes heuristic schedulers for the learning rate (inspired by AutoAttack's step-size scheduler) and loss scalars λ₁, λ₂ (based on standard accuracy). Experiments across 6 downstream tasks with ResNet-18/50 and ViT/DeiT backbones show consistent improvements in PGD-10 and AutoAttack accuracy over vanilla RFT and TWINS, with statistical significance testing.

## Strengths

1. **Empirical identification of gradient divergence in prior RFT methods.** Figure 1a quantitatively shows that the cosine similarity between gradients of natural and adversarial objectives w.r.t. the FE is very low (~−0.4 to −0.5) for both vanilla RFT and TWINS on DTD-57. This is a clean diagnosis that goes beyond prior work (including TWINS) which did not analyze this specific optimization conflict. The paper validates this across multiple datasets in Appendix B.1.

2. **Architectural disentanglement via a low-rank branch is clean and effective.** The LoRa branch routing natural data and the FE routing adversarial data directly eliminates the gradient conflict (Figure 1c, Eq. 5). The resulting robustness gains are consistent across all 6 datasets in Tables 1 and 2 (e.g., +2.03% AA on CIFAR-100 with ResNet-18 vs. TWINS; +3.03% AA on DOG-120 with ResNet-50 vs. TWINS). The p-values from t-tests (Table 7, Appendix) support statistical significance.

3. **Parameter efficiency and zero inference overhead.** The LoRa branch uses <5% of FE parameters (Table 4, rank 8) and is dropped at inference time, matching the PEFT paradigm (Hu et al., 2021) without extra test-time cost. This makes the method practical for deployment.

4. **Consistent gains across diverse backbones.** Tables 1–3 show improvements with ResNet-18, ResNet-50, ViT-S/16, ViT-B/16, DeiT-tiny, and DeiT-small, on both low-res (CIFAR-10/100) and high-res (DTD-57, DOG-120, CUB-200, Caltech-256) tasks. Table 4 ablates the rank parameter, and Table 8 ablates different pre-training adversarial budgets.

5. **Automated scheduler reduces hyperparameter burden.** While TWINS required per-task grid search (noted in Section 3.2), AutoLoRa uses fixed defaults (α=1.0, λ₂^max=6.0, initial LR=0.01) that work across tasks. Table 9 shows that applying the LR scheduler to TWINS matches its tuned performance, validating the scheduler's design.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The loss scalar λ₂^max is fixed without ablation.** λ₂^max = 6.0 is set by default but never ablated. Since λ₂ controls the KL distillation scale, which directly affects the trade-off between natural and adversarial learning, the sensitivity of this choice is unclear. The paper ablates α (Table 10) but not λ₂^max. This is a gap, albeit minor since the default appears to work across all 6 datasets.

2. **The LR scheduler is validated on TWINS, not on AutoLoRa itself.** Table 9 shows that applying the automated LR scheduler to TWINS yields comparable performance to tuned TWINS. However, there is no ablation that removes the scheduler from AutoLoRa to quantify its contribution separately from the disentanglement. The paper attributes the benefit to the full AutoLoRa package, but the disentanglement (LoRa branch) and the scheduler are confounded in the main results.

3. **No training cost / wall-clock time comparison.** AutoLoRa introduces extra overhead: (a) the LoRa branch adds forward/backward computation, (b) a PGD-10 attack on the validation set every epoch for LR scheduling. The paper does not report training time or FLOPs vs. baselines, making it difficult to assess the computational price of the robustness gains. This is standard to report for systems papers in this field.

4. **Some gains are marginal on particular datasets.** On Caltech-256 with ResNet-50, the PGD-10 improvement is +0.03% (47.79→47.82) and AA improvement is +0.36% (42.27→42.63) vs. TWINS. While the p-values in Table 7 indicate statistical significance, the practical significance of such small improvements is questionable for practitioners. The paper could benefit from discussing when improvements are meaningful vs. negligible.

5. **The claim of "without tuning hyperparameters" is slightly overstated.** The automated scheduler has its own hyperparameters (α, λ₂^max, initial LR, halving ratio, checkpoint frequency, 75% threshold). While defaults work across the tested tasks, the paper does not study sensitivity to these choices. In particular, the 75% threshold in Condition 1 and the checkpoint spacing are not analyzed.

6. **The LoRa branch's soft-label quality is not analyzed.** The KL distillation term distills from the LoRa branch into the FE. The paper does not analyze how the quality of these soft labels evolves during training or whether the LoRa branch's predictions are indeed better or simply different. This could be addressed with a simple analysis of the LoRa branch's standalone accuracy over training.

### Trivial

- The notation θ₁ ∈ ℝ^{d×v} in Section 3.1 is used as an abstract parameterization of the FE (i.e., the collection of all FE weights across layers, flattened for notational convenience). This is standard practice in ML theory papers. The paper could clarify that this is a notational abstraction — the actual implementation follows standard LoRA (Hu et al., 2021) by inserting low-rank adapters at specific layers of the FE (the code is available on GitHub). The harsh critic's characterization of this as a "fatal flaw" is incorrect.

## Nice-to-Haves

- An ablation of the automated LR scheduler applied to AutoLoRa itself (not just to TWINS) would directly quantify the scheduler's contribution.
- Reporting wall-clock training time and/or FLOPs per epoch for AutoLoRa vs. baseline methods.
- An analysis of LoRa branch standalone accuracy over training epochs to understand whether soft-label quality degrades/improves.
- An ablation study on λ₂^max values (e.g., 2, 4, 6, 8, 10) to show sensitivity.
- Discussion of when the method yields small vs. large gains (e.g., correlation with dataset size, class count, or intrinsic dimensionality).

## Removed Points

**From Harsh Critic:**
- **"Mathematical formulation is incompatible with actual neural network architectures" (classified as fatal).** The paper uses θ₁ ∈ ℝ^{d×v} as a notational abstraction for the FE parameters — the FE is a composite function f_θ: ℝ^d → ℝ^v whose total parameter tensor is abstracted as having dimensions d×v. This is standard practice in ML papers (see line 71: "For notational simplicity"). The LoRa branch BA ∈ ℝ^{d×v} mirrors this abstraction. The actual implementation follows standard LoRA applied layer-wise, and code is available. This does not "invalidate the core contribution" nor is it "incompatible" — it is a conventional mathematical simplification. → REMOVED (misunderstanding of notation; not a real flaw).

- **"The FE is adversarially pre-trained (so the approach may not transfer)"** — The paper's scope is RFT (Robust Fine-Tuning), which by definition starts from adversarially pre-trained models. Criticizing this as a limitation is scope creep. → REMOVED.

- **"Missing related works"** — Not verifiable without external sources. → REMOVED per protocol.

- **"Missing appendix" / "cannot see appendix"** — Parser artifact; appendix exists in original submission. → REMOVED per protocol.

**From Strength Finder:**
- All strengths were concrete and evidence-backed. No strengths removed.

## Novel Insights

The harsh critic's framing of the notation issue as "fatal" is the most striking pattern in these reviews. The critic interprets θ₁ ∈ ℝ^{d×v} literally as claiming the FE is a single linear layer, rather than as a standard high-level abstraction of a function's parameter space (a convention used throughout the RFT literature, including the cited TWINS paper). This reflects a genre mismatch between the reviewer's assumed granularity and the paper's chosen level of abstraction. Beyond the paper's own contributions, the calibration exercise surfaced an interesting observation: papers that identify a *specific, measurable pathology* in prior work (here, gradient cosine similarity) tend to be rated higher than those proposing methods based on general intuitions, regardless of whether the proposed fix is mathematically deep. The gradient similarity plots (Figure 1a) are the paper's strongest rhetorical device — they provide a concrete diagnosis that makes the solution (disentanglement) feel necessary rather than ad-hoc.

## Suggestions

1. Clarify in Section 3.1 that θ₁ ∈ ℝ^{d×v} is an abstraction of the FE's total parameter space (including across layers), and specify in Section 4.1 that LoRA adapters are inserted at the final FE layer(s) following standard practice (Hu et al., 2021). Even a short sentence would preempt the confusion.

2. Add an ablation of λ₂^max to strengthen the claim that the automated scheduler requires no tuning.

3. Report training time (wall-clock or relative) comparing AutoLoRa to the baselines, including the PGD-10 validation overhead.

4. Add an ablation of AutoLoRa without the automated LR scheduler (use a fixed LR schedule instead) to isolate the disentanglement contribution from the scheduler contribution.

## Score and Decision

**Calibration protocol results:**

**Round 1 — Bracketing:**
| Anchor | Avg Score | Band | Comparison |
|--------|-----------|------|-----------|
| EIfcSw6MW0 (certified robustness) | 3.00 | <3.5 | Much weaker — lacks clear empirical diagnosis |
| sr0My6yDNu (continual learning robustness) | 3.25 | <3.5 | Much weaker — limited evaluation |
| dIK7GpOwNY (effective dimensionality) | 3.00 | <3.5 | Much weaker — inconclusive results |
| ZxcMfJzFaZ (CLAT) | 5.20 | (3.5, 7.5) | Weaker — less datasets, weaker motivation, rejected |
| aKkDY1Wca0 (multi-index models) | 6.86 | (3.5, 7.5) | Stronger theory, but less practical breadth |
| 1op5YGZu8X (NTK robust overfitting) | 6.40 | (3.5, 7.5) | Stronger theory, narrower scope |
| PGNdDfsI6C (LoRA vs full FT) | 4.75 | (3.5, 7.5) | Weaker — analysis without practical method |
| 6Mxhg9PtDE (safety alignment) | 9.50 | >7.5 | Much stronger — broader impact, deeper analysis |
| TwJrTz9cRS (HiRA) | 8.00 | >7.5 | Stronger — cleaner presentation, more thorough ablations |

**Round 1 bracket:** [3.5, 7.5]

**Round 2 — Narrowing:**
| Anchor | Avg Score | Band | Comparison |
|--------|-----------|------|-----------|
| VQ7Q6qdp0P (fine-tuning cripples) | 4.75 | (4.5, 6.5) | Weaker — analysis without strong method solution |
| kUH1yPMAn7 (safety layers in LLMs) | 6.00 | (4.5, 6.5) | Similar quality — clear finding, practical method |
| 1BuWv9poWz (transferable attacks on ViTs) | 5.33 | (4.5, 6.5) | Weaker — narrower scope, specialized |
| pE6gWrASQm (AT without perturbing all) | 6.50 | (5.0, 7.5) | Slightly stronger — more thorough analysis, accepted |
| OALIb8oNfl (structural integrity PEFT) | 5.75 | (5.0, 7.5) | Similar — good experimental scope, accepted |

**Final calibration:** The paper sits between CLAT (5.20, rejected) and AT without perturbing all examples (6.50, accepted). It is stronger than CLAT (more datasets, clearer motivation, statistically validated) but slightly weaker than the AT paper (which had deeper analysis of its phenomenon). The paper's core contributions are solid, the experiments are broad, and the weaknesses are addressable. No fatal flaws exist. The notation concern raised by the harsh critic is a misunderstanding of standard mathematical abstraction.

**Score:** 6.0 — strong accept at a workshop; poster at a main conference.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>