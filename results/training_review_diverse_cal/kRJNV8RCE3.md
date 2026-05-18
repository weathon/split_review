Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes hiding secret images in diffusion models by modifying the learned score function at a single chosen time step (t_s), using a distillation-based secrecy loss to preserve generation quality and a hybrid parameter-efficient fine-tuning (PEFT) approach combining sensitivity-based parameter selection with LoRA variants (rsLoRA, LoRA+, LoCon). The method enables one-step extraction, supports multiple secret images with distinct keys, and achieves hiding times of ~0.3 GPU hours on 32×32 images. Experiments on DDPM, EDM, and consistency models across CIFAR-10 and LSUN bedroom demonstrate strong fidelity and secrecy.

## Strengths

- **One-step hiding/extraction dramatically improves efficiency.** By concealing the secret image at a single chosen time step instead of requiring multi-step guided denoising, the method achieves hiding times of ~0.3 GPU hours (Tables 2, 3), compared to 5.0 hours for the next-best competitor (WDP). This is a clear operational advantage over prior diffusion-model hiding methods.

- **Hybrid PEFT demonstrably improves secrecy over full fine-tuning.** Table 6 shows that replacing the PEFT component with full fine-tuning degrades secrecy (FID rises from 7.17 to 8.28; sample-level PSNR of secrecy drops from 31.81 to 28.32), while full fine-tuning does not improve fidelity. This proves that the PEFT design is necessary for the method's secrecy claim.

- **Generalizability beyond DDPM is explicitly validated.** Table 7 shows the same pipeline works on EDM and consistency models, not just the primary DDPM implementation. This demonstrates the method is not tied to a specific diffusion architecture or training scheme.

- **Ablation identifies optimal secret time step.** Figure 5 systematically varies t_s and shows the best fidelity-secrecy trade-off occurs in the range [700, 900], providing actionable guidance and supporting the robustness of the design.

- **Extension to multiple secret images is demonstrated.** Tables 4 and 5 show that even with up to 10 secret images, extraction fidelity remains acceptable (e.g., PSNR ~32 dB for 32×32), a functional advance over prior diffusion-based methods focused on single-image hiding.

## Weaknesses

### Fatal
None.

### Major

1. **The PEFT design is insufficiently ablated relative to its billed contribution.** The proposed hybrid PEFT — sensitivity-based layer selection + LoRA variants — is presented as a key methodological contribution, yet the only ablation (Table 6) compares it against full fine-tuning. There is no comparison against: (a) standard LoRA applied to all layers without sensitivity selection, (b) selective fine-tuning of sensitive parameters without LoRA, or (c) random layer selection with LoRA. Without these controls, it is impossible to tell whether the sensitivity-guided selection, the choice of LoRA variants, or simply using fewer parameters is responsible for the observed secrecy and efficiency gains. Additionally, the hyperparameters γ (parameter sparsity), δ (layer sparsity), the LoRA rank, and M (sensitivity accumulation iterations) are defined in the method section (lines 172, 182) but never reported in the experimental setup, making the design choices opaque and the method harder to reproduce.

2. **The multi-image claim about preventing cross-extraction is asserted but never tested.** The paper claims (line 151) that "without additional secret keys, the i-th recipient is unable to extract other secret images," yet no cross-extraction experiment is reported. The claim that the method provides recipient-specific access control requires direct evidence — e.g., showing that extracting image A with key B yields low PSNR — before it can be accepted as a validated property of the method. This is a gap in the evaluation that weakens the flexibility claim.

### Minor

3. **Comparison tables include methods operating on fundamentally different cover media.** Tables 1–3 include image steganography methods (Baluja, Zhu, Weng, Jing, Yang) that embed into cover images, not into neural networks. The paper acknowledges this is "not directly comparable" (line 227) for secrecy, yet these methods still appear in the tables, and the text draws unqualified comparative conclusions (e.g., "Our method achieves the highest fidelity… the best secrecy"). Since the task difficulty, constraints, and secrecy definition differ substantially, the claimed "superiority" is partly an artifact of an apples-to-oranges comparison. The paper's own absolute performance numbers still stand, but the comparative framing inflates the apparent state-of-the-art.

4. **Sample-level secrecy metrics assume paired access to the original model.** The sample-level metrics (PSNR/SSIM/LPIPS/DISTS between original and stego model outputs given the same initial noise) require the inspector to have paired outputs from both models. The stated inspection scenario (Section 3.2) only gives the inspector the stego model. The paper does report FID, which is the appropriate unpaired metric, but the narrative around "best secrecy" is partly built on these paired-sample numbers, which are weaker evidence for the stated threat model than they appear. A brief justification or reframing would clarify this.

5. **The sensitivity computation overhead is not separated from total reported time.** The method requires M iterations of forward/backward passes for sensitivity accumulation before fine-tuning. Since one of the method's claimed advantages is efficiency, the cost of this pre-computation step should be explicitly accounted for rather than folded into the total 0.3 GPU hours.

6. **Key training details for the secrecy loss are omitted.** The secrecy loss involves an expectation over t and x_t (line 132), but the paper does not specify how many clean images are sampled per iteration, whether the same batch is used for both the fidelity and secrecy losses, or the value of the trade-off parameter λ. These affect reproducibility and the reported efficiency.

### Trivial

- The framing of pixel-space vs. latent-space diffusion models (Section 2, line 29) could be more neutral — the paper describes prior work's focus on latent diffusion as a limitation rather than a complementary design choice.

## Nice-to-Haves

- A discussion of how much FID divergence from the original model is detectably suspicious, referencing known variability of FID estimates, would ground the secrecy claim more concretely.
- An analysis showing that the one-step reconstruction at t_s genuinely behaves as a denoising step (rather than degenerating into a learned noise-to-image mapping unrelated to diffusion) would strengthen the mechanistic understanding of the method. This could be as simple as visualizing the reconstruction from the original (unmodified) model's output at the same noise.

## Removed Points

- **Criticism about λ not being reported "in the main paper, not solely in an appendix"** — The parser strips appendix sections from all papers; content that may exist in the original appendix cannot be verified and should not be penalized. However, the fact that λ's value is absent from the main text is a valid reproducibility concern, so this was absorbed into Minor weakness #6.
- **Criticism about the latent diffusion framing** — This is a presentational preference, not a substantive weakness. Moved to Trivial.
- **Generic strengths from the Strength Finder** (e.g., "this paper addressed an important problem") were already filtered; the retained strengths are all concretely supported by specific results in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that meaningfully extends or reframes the paper's findings.

## Suggestions

1. **Ablate the PEFT design systematically.** Add comparisons against: (a) standard LoRA on all layers, (b) selective fine-tuning of sensitive parameters without LoRA, (c) random layer selection + LoRA. Report γ, δ, LoRA rank, and M in the main text or a dedicated table.

2. **Add cross-extraction experiments for multi-image results.** For the C=5 or C=10 setting, report a matrix showing PSNR when extracting each secret image using each recipient's key. This directly tests the claim that recipients cannot extract each other's images.

3. **Clean up baseline presentation.** Either remove the image steganography methods from the main comparison tables (keeping them only in a separate supplementary table), or clearly separate them with a visual divider and explicitly qualify any comparative statements.

4. **Report λ's value and its sensitivity.** Since fidelity and secrecy are fundamentally traded off, the chosen λ value should be stated, and ideally a brief sensitivity analysis should be included.

5. **Separate the sensitivity computation cost from the hiding time.** Report the GPU hours for both the M-iteration sensitivity accumulation and the subsequent fine-tuning.

## Score and Decision

The paper introduces a creative and technically sound core idea — hiding at a single time step with distillation-based regularization — that meaningfully advances diffusion-model steganography. The absolute performance numbers (extraction fidelity ~34–35 dB PSNR, FID close to the original model, hiding time <0.5 GPU hours) are competitive and promising. However, the evaluation has two substantiated gaps: the PEFT design (a claimed contribution) lacks adequate ablation against simpler alternatives, and the multi-image claim about cross-extraction resistance is asserted without evidence. These are real but addressable issues. The paper should be accepted because the core contribution is novel and the absolute results are strong, but the authors should address both gaps in a revision or rebuttal.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>