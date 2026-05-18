Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes CADS (Condition-Annealed Diffusion Sampler), a training-free inference-time method that improves the diversity of conditional diffusion models. The core idea is to add scheduled, monotonically decreasing Gaussian noise to the conditioning signal during sampling — breaking dependence on the condition early for broader exploration, then restoring it later for quality. The method is evaluated across four conditional generation tasks (class-conditional ImageNet, pose-to-image, identity-conditioned face, text-to-image), demonstrates consistent improvements in FID, Recall, and diversity metrics, and reports new SOTA FIDs of 1.70 on ImageNet 256×256 and 2.31 on ImageNet 512×512 using a fixed pretrained DiT-XL/2 model.

## Strengths

- **Novel, simple, and training-free method**: CADS adds only an additive noise operation to the conditioning signal during inference (Eq. 1) and requires no retraining or model modification. It works with any pretrained diffusion model and any sampler (DDIM, PNDM, DPM-Solver, Heun — demonstrated in Table~Samplers).

- **Consistent diversity improvements across multiple tasks and metrics**: CADS yields better FID, Recall, MSS, and Vendi Score compared to standard DDPM sampling at the same high guidance scale across class-conditional ImageNet (DiT-XL/2), pose-to-image (DeepFashion, SHHQ), identity-conditioned face (ID3PM), and text-to-image (Stable Diffusion) generation (Table~Main). Precision is largely preserved, confirming the method maintains quality while improving diversity.

- **New SOTA FID on ImageNet at two resolutions using a fixed pretrained model**: CADS applied to DiT-XL/2 achieves FID 1.70 on ImageNet 256×256 and 2.31 on ImageNet 512×512 (Table~Sota), surpassing the previous best from MDT (1.79) which required retraining. This is a strong result because it demonstrates that a simple sampling-side modification can outperform architecture/training innovations.

- **Extensive ablation study**: The paper systematically evaluates the noise scale \(s\), cut-off threshold \(\tau_1\), and rescaling mixing factor \(\psi\), providing practical guidance for tuning CADS. The ablations use both FID and diversity metrics to map the trade-off landscape.

- **Theoretical intuition provided**: Section 3.2 connects condition annealing to score smoothing via a Bayesian perspective, explaining why noisy conditions early cause the model to follow the unconditional score (promoting exploration), while clean conditions late restore conditional alignment.

- **Outperforms the natural Dynamic CFG baseline**: CADS is compared against Dynamic CFG (directly modulating the guidance weight during inference) and substantially outperforms it (FID 9.47 vs 18.42, Recall 0.62 vs 0.39 at the same setting), demonstrating that additive stochasticity provides benefits beyond simply underweighting the condition.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported across multiple tasks and settings.

### Minor

- **Lack of uncertainty quantification on headline FID numbers**: The SOTA results (FID 1.70 for ImageNet 256×256, 2.31 for 512×512) are reported as single values without error bars, confidence intervals, or multiple-seed experiments. Generative model evaluation is known to be noisy — FID can vary by 0.1–0.2 across runs. The claimed improvement over MDT (1.79 → 1.70) is within this noise margin. The paper does use the same random seeds for fair pairwise comparisons (line 94), which controls variance in relative comparisons, but absolute numbers remain unqualified. Given that the SOTA claim is one of the paper's headline contributions, reporting variance would significantly strengthen confidence. The paper's consistent improvements across many tasks partially mitigates this concern but does not fully resolve it.

- **SOTA claim lacks full transparency in the main text about baseline configurations**: The paper states that CADS achieves FID 1.70 by "employing higher guidance values" (line 107) but does not specify in the main text (a) the exact guidance scale used, (b) the FID of standard DDPM at that same guidance scale, or (c) the sampling steps. While the SOTA table (Table~Sota) presumably contains these details, the main narrative would benefit from stating, e.g., "DDPM with DiT-XL/2 at guidance scale X yields FID Y, while CADS at the same scale yields FID 1.70." This is a presentational choice that the authors can address in a revision, but the current presentation places a burden on the reader to trust the numbers line up as claimed.

### Trivial

- **The diversity metrics MSS and Vendi Score use SSCD features designed for copy detection, not distribution coverage.** The paper's primary diversity metric is Recall, with MSS and Vendi Score as supplementary. The improvements are consistent across all three, so this does not affect the conclusions, but a brief justification that SSCD features capture perceptual diversity in the intended sense would be welcome.

- **The Dynamic CFG comparison at one operating point** (FID 20.83 for DDPM) shows CADS at a large improvement, but this is at a setting where DDPM already has poor FID. The comparison would be more informative across a range of guidance scales, as in Figure~plots.

## Nice-to-Haves

- A direct ablation comparing CADS (annealed noise) against constant (non-annealed) noise of the same average level would sharpen the claim that the *annealing schedule* — not just noise injection — is responsible for the improvement. The τ₁ ablation partially covers this (varying how long noise is applied), but a constant-noise control at, say, γ(t)=0.5 for all t would be a cleaner test.

- Reporting FID as mean±std over 3 seeds for the core ImageNet SOTA result would address the main reproducibility concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The DDPM baseline is deliberately operated at a suboptimal guidance scale to highlight CADS's benefit"** — Removed because this is the paper's intended experimental design, not a flaw. The paper's core argument is that CADS *enables* the use of higher guidance scales without the diversity penalty that normally limits them. Comparing DDPM and CADS at the same high guidance is the correct comparison; the paper does not claim CADS improves over DDPM at the optimal guidance of 1.5. The whole contribution is about unlocking higher guidance values.

2. **"Dynamic CFG comparison should test whether constant low-level noise without annealing would match CADS"** — Moved to Nice-to-Haves. The paper's ablations on τ₁ and s already explore the spectrum from "too much noise" to "too little noise." A constant-noise control would be informative but not necessary to support the paper's claims. The reviewer's point is a suggestion for further analysis, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a transparent concern about statistical grounding of the SOTA claim but do not reveal any unarticulated weakness in the method itself.

## Suggestions

1. Report FID results (at minimum for the SOTA comparison on ImageNet 256×256) as mean±std over 3 different random seeds, or explain why this is not done and note the known noise level.
2. In the main text, state the exact guidance scale and the DDPM baseline FID at that scale alongside the CADS SOTA FID (1.70), so the reader can directly see the improvement without cross-referencing the table.
3. Add a brief justification for using SSCD features for diversity measurement, or note the assumption.
4. (Optional) Include a constant-noise control ablation to directly demonstrate the benefit of the annealing schedule over non-annealed noise injection.

## Score and Decision

This is a solid methods paper. The core idea is simple, well-motivated, and clearly demonstrated across multiple tasks and metrics. The weaknesses are presentational and statistical (lack of error bars on the SOTA claim) rather than structural. The method itself is sound and the evidence of improved diversity is convincing even setting aside the SOTA claim. The paper should be accepted with the expectation that the authors address the error bar issue and improve transparency of the SOTA comparison in the main text.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>