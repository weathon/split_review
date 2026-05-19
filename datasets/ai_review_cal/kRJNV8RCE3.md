- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5
Now I have thoroughly read the paper and verified the claims. Let me construct the final consolidated review.

---

## Summary

This paper proposes hiding images in diffusion models by modifying the learned score function at a single "secret" denoising time step. A hybrid parameter-efficient fine-tuning (PEFT) approach—combining gradient-based parameter sensitivity selection with LoRA variants (rsLoRA, LoRA+, LoCon)—is introduced to limit the number of modified parameters, improving both secrecy and hiding efficiency. Experiments on DDPM (CIFAR-10, LSUN bedroom), EDM, and consistency models show high extraction fidelity, minimal degradation of the original model's generation quality (FID nearly unchanged), dramatic reductions in GPU hours relative to baselines, and the ability to hide multiple images for different recipients.

## Strengths

- **Novel and well-motivated idea**: Hiding at a single denoising time step via score function editing is a conceptually clean departure from prior work that relies on modifying the entire guided reverse process. The one-step extraction formula (Eq. 6) follows naturally from the DDPM derivation and enables fast extraction.

- **Strong empirical results on NNS tasks**: Among neural-network-steganography (NNS) baselines (Chou, Chen, Peng, WDP), the method consistently yields the best extraction fidelity (PSNR 36.32 on 32×32, 32.34 on 256×256) while keeping the stego model's FID nearly indistinguishable from the pre-trained model (3.72 vs. 3.70 on CIFAR-10). Tables 2 and 3 show these advantages clearly for the NNS subset.

- **Dramatic efficiency gains**: The method requires 0.05 GPU hours for CIFAR-10 and 0.25 for LSUN bedroom vs. the nearest NNS competitor (WDP at 0.65/1.26 hours). This is a concrete, practically meaningful improvement.

- **Generalizability across diffusion model families**: Table 7 demonstrates the method works on EDM and consistency models, not only the DDPM backbone used for the main experiments. This provides evidence that the approach is not an artifact of a specific architecture.

- **Multi-image hiding with per-recipient extraction**: Tables 4 and 5 show that up to 10 secret images can be hidden simultaneously while maintaining acceptable fidelity and secrecy, with recipient-specific keys controlling extraction.

## Weaknesses

### Fatal

None.

### Major

1. **Conflated comparisons in secrecy and fidelity tables undermine the evaluation's clarity.** Tables 2 and 3 include image steganography methods (Baluja, Zhu, Weng, Jing, Yang) alongside NNS methods under a shared "Secrecy" column. The paper itself acknowledges (line 227) that "the secrecy evaluation of image steganography methods is based on the fidelity of the stego image, which is not directly comparable to the secrecy of NNS methods." For image steganography, the secrecy metrics (FID, PSNR, etc.) measure distortion of the *cover image*; for NNS methods, they measure distortion of the *model's generated outputs* — these are fundamentally different quantities. Including them in a single table without clear visual separation or a dedicated disclaimer near the table implies comparability that the paper admits does not exist. The same issue applies to Table 1 (fidelity comparison), where image steganography methods and NNS methods operate under entirely different cover-media constraints. This weakens the paper's strongest comparative claims even though the method likely still leads among NNS methods alone.

2. **Key experimental hyperparameters are not reported, hindering reproducibility.** Specifically: the trade-off parameter λ (Eq. 9) is introduced but never given a value; the number of sensitivity accumulation iterations M (Eq. 11) is not reported; the number of training iterations/epochs, learning rate, batch size, and optimizer are absent from the paper. The paper states "The architecture and hyperparameters of DDPM follow the specification of Ho et al. (2020)," but the fine-tuning procedure for hiding is separate from pre-training, and its hyperparameters are essential for reproducibility. The value of γ (sparsity of sensitive parameters) and δ (sparsity of sensitive layers) are also not reported. Without these, the results cannot be independently verified.

3. **Insufficient ablation of the proposed PEFT design.** The only PEFT comparison is against full fine-tuning (Table 6). There is no ablation comparing the proposed hybrid approach against: (a) standard LoRA applied to all linear layers (without sensitivity-based selection), (b) LoRA applied to a random subset of layers, (c) simpler fine-tuning of only the top-τ parameters by gradient masking, or (d) other PEFT techniques (Adapter, etc.). Without these, it is impossible to determine whether the complexity of sensitivity computation + layer selection + LoRA variants provides any benefit over simpler alternatives. The core claim that this specific PEFT design is necessary remains unvalidated.

4. **Efficiency claims lack controls.** The GPU hours reported in Tables 2 and 3 are raw wall-clock times. The paper does not report the number of training iterations used by each baseline or by the proposed method. If the method simply uses far fewer gradient steps, the speed advantage could be due to an unfair training budget rather than intrinsic efficiency of the PEFT approach. A controlled comparison (e.g., fidelity vs. iteration count or wall time) is needed. Additionally, the cost of the sensitivity pre-computation step (M forward/backward passes through the full model) is not included or discussed in the GPU-hour accounting.

### Minor

5. **Missing justification for default secret time step.** The default is t_s=500, but Figure 5 shows that t_s between 700 and 900 yields better fidelity-secrecy trade-offs. The paper does not explain why 500 was chosen over these better-performing values, nor whether the optimal t_s depends on the dataset.

6. **No security analysis for the multi-image scenario.** The paper claims (line 151) that without the correct secret key, a recipient "is unable to extract other secret images." This cross-receiver isolation claim is not experimentally verified — there is no experiment showing that using the wrong key yields an unrecognizable image. Without this verification, the "multiple images for different receivers" feature is not fully supported.

7. **Number of FID evaluation samples not reported.** The paper states FID is the "population-level metric" but does not state how many generated samples were used for FID computation. The reliability of FID depends heavily on sample count, especially for smaller datasets.

8. **Point estimates without variance.** All metrics in Tables 1–7 are reported as single numbers without standard deviations or confidence intervals. For FID and sample-level metrics, this makes it impossible to assess whether differences between methods are statistically significant. (This is a common issue in the field but should still be noted.)

9. **Lower fidelity on higher-resolution/more-diverse data.** The PSNR drops from ~35.5 (CIFAR-10, 32×32) to ~26.6 (ImageNet 64×64 via EDM). While this is acknowledged implicitly, the paper does not discuss why the method works less well for harder distributions or what the expected limits are.

### Trivial

10. The notation for the gradient mask uses the same symbol *M* that was used earlier for the number of sensitivity accumulation iterations, which could cause confusion (lines 166 vs. 177).

## Nice-to-Haves

- A comparison against standard LoRA (without rsLoRA/LoRA+ variants) to isolate the benefit of each component.
- An ablation on λ showing how different trade-off values affect fidelity vs. secrecy.
- A discussion of whether an adversary could detect the stego model by probing its outputs at the secret time step with multiple noise inputs (as the secrecy loss only constrains average behavior across all time steps, not the specific t_s behavior).
- Extension of the analysis to the range of 20+ hidden images to better understand scaling limits.

## Removed Points

The following points from the reviewers are removed with justification:

- **"Secret image dataset is an arbitrary collection"** (Critic §4): The paper aggregates from COCO, DIV2K, LSUN church, and Places — all standard, well-known datasets. This is a reasonable benchmark composition, not arbitrary.
- **"Backbone models used are outdated" and practical significance limited to pixel-space** (Critic, Missing Parts): The paper explicitly scopes itself to pixel-space diffusion models (line 29), and the critic's own "Strengthening" section acknowledges the gap being addressed. Criticizing a paper for not doing what it explicitly scoped out is inappropriate. The method is demonstrated on DDPM, EDM, and consistency models, which covers the main pixel-space families.
- **"How does fidelity degrade with 100 or 1000 images?"** (Critic, Abstract/Introduction): The paper demonstrates scalability up to 10 images, which is already more than what prior work in this specific domain typically shows. Asking for 100–1000 images without motivating why such capacity is needed for the NNS use case is scope creep.
- **"No discussion of the risk of overfitting the secret sample"** (Critic, Missing Parts): The secrecy loss (Eq. 8) is explicitly designed to address this by regularizing the score function toward the pre-trained model's outputs on average over all time steps. The critic acknowledges this is a "plausible approach" but asks for adversarial analysis that goes beyond the paper's stated evaluation scope. This is a valid future direction, not a current weakness.
- **"Future work suggestion is vague"** (Critic, Conclusion): This is a generic complaint applicable to most paper conclusions. It does not affect the paper's contribution.
- **Strength Finder strength about "challenging natural secret images"** is kept but noted as a relatively minor point.
- **All formatting/grammar nitpicks** removed per parser-error rule.

## Novel Insights

The harsh critic correctly identified that the core weakness is not in the method itself but in how the evaluation is presented — the decision to include image steganography methods in the same tables as NNS methods, while acknowledging they are not comparable, creates a self-inflicted credibility problem. On the other hand, the strength finder correctly identified that when restricting to a like-for-like comparison against NNS diffusion-model methods only, the paper's results are genuinely strong across fidelity, secrecy, and efficiency simultaneously — a combination that prior work does not achieve. The meta-review synthesis confirms that the main gap is in evaluation framing and missing experimental details rather than any flaw in the technical approach.

## Suggestions

1. **Restructure the main evaluation tables.** Present image steganography methods and NNS methods in clearly separated blocks or separate tables. Alternatively, keep only NNS methods in the main paper and relegate the cross-domain comparison to the appendix with a clear explanation of why it is included (e.g., for completeness of the literature survey). The claim "best secrecy" should be explicitly qualified as "among NNS methods for diffusion models."

2. **Report all missing hyperparameters** (λ, M, γ, δ, number of training iterations, learning rate, batch size, optimizer, LoRA rank) either in the main text or in an appendix.

3. **Add controlled PEFT ablations**: compare against LoRA on all layers (no sensitivity selection), LoRA on random layers, and gradient-masking-only fine-tuning to justify each component of the hybrid design.

4. **Control for iteration count in efficiency comparison**: report fidelity vs. GPU hours or fidelity vs. training iterations for the proposed method and at least one baseline, to demonstrate that the speed advantage is not simply due to fewer training steps.

5. **Verify the multi-receiver isolation claim** with a quantitative experiment showing that using an incorrect secret key produces low PSNR/SSIM against the intended secret image.

6. **Report variance** (standard deviations over multiple runs or multiple secret images) for all metrics, particularly FID and sample-level PSNR/SSIM.
