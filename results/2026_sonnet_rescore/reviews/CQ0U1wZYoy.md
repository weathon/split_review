## Summary

PRISM is a prompted conditional diffusion framework for compound and controllable image restoration in scientific domains. It combines (1) a weighted contrastive disentanglement objective that enforces compositional structure in CLIP embeddings across degradation mixtures, and (2) compound-aware supervision over synthetic triplets drawn from 2M scientific images. This enables simultaneous removal of overlapping distortions and selective, expert-guided correction via natural language prompts. The paper also introduces a Mixed Degradations Benchmark (MDB) and a downstream scientific utility evaluation spanning remote sensing, ecology, microscopy, and urban monitoring domains.

---

## Strengths

- **Compositional scaling under increasing distortion count (Figure 3):** PRISM (Compound-Aware) achieves a ΔPSNR of 8.14 from 1→4 distortions versus 11.12 for AutoDIR, 11.33 for MPerceiver, and 10.56 for PRISM (Primitive-Aware). This directly demonstrates that training on composites — not just architecture — conveys robust generalization under increasing mixture complexity.

- **State-of-the-art zero-shot performance on unseen domains (Table 2):** PRISM achieves PSNR 22.18 on UIEB, 18.26 on POLED, and 22.36 on ThapaSet, outperforming all baselines including diffusion-based AutoDIR and MPerceiver on unseen real-world degradation composites, supporting the claim that compositional latent structure interpolates across novel mixtures.

- **Compelling downstream utility findings (Table 4, Figure 6):** Super-resolution improves segmentation mIoU but degrades fluorescence MSE, while denoising has the inverse effect — a concrete, domain-grounded result that no single restoration policy suits all scientific analyses. This is the paper's most internally compelling and original finding.

- **Selective restoration significantly improves downstream accuracy in three of four domains (Table 3):** Microscopy mIoU improves from 0.475 (full automated) to 0.580 (selective, p=0.018), camera traps from 0.976 to 0.984 (p=0.032), and urban scenes from 0.615 to 0.650 (p=0.041). These are statistically significant gains that substantiate the practical value of controllability.

- **Weighted Jaccard contrastive loss explicitly encodes mixture overlap (Section 3.2, Figure 4):** The formulation of $w_{jk} = \exp(1 - |d^{(j)} \cap d^{(k)}| / |d^{(j)} \cup d^{(k)}|)$ is principled and purpose-built for compositional degradation structure, and Figure 4 shows the compound-aware CLIP encoder narrows the sequential-vs-composite PSNR gap (~21.5→22.2).

- **Introduction of downstream scientific-utility benchmark and Rooftop Cityscapes dataset (Section 3.4):** Evaluation via landcover classification, species recognition, segmentation mIoU, and fluorescence MSE — using off-the-shelf pretrained models — provides a practically grounded and task-relevant complement to pixel-level PSNR/SSIM metrics.

---

## Weaknesses

### Fatal
None.

### Major

- **Training-distribution asymmetry in Table 1.** Section 3.2 explicitly states "all baselines are trained on the fixed set of primitive distortions" while PRISM trains on compound mixtures. The headline comparison in Table 1 therefore conflates two factors: PRISM's architectural design (contrastive disentanglement, SCPM) and its data advantage (compound training). The paper partially disambiguates this via Figure 3, where PRISM-Primitive-Aware (Δ10.56) still outperforms AutoDIR (Δ11.12) and MPerceiver (Δ11.33) on scaling behavior. However, the absolute PSNR gap in Table 1 (22.08 vs. 20.84 vs. 20.42) is never decomposed into how much comes from compound training data alone versus the architectural innovations. The compound-aware training is itself a contribution, but the primary evaluation conflates data and architecture gains, making it impossible to credit specific design choices for the magnitude of improvement.

- **Controllability argument in Table 3 conflates two experimental variables.** "Full Restoration" uses PRISM's automated MLP to predict distortions, while "Selective Restoration" uses expert manual prompting. These differ simultaneously on (a) *which* distortions are targeted and (b) *how accurately* distortions are identified. If the MLP makes classification errors (misses a distortion or predicts an absent one), selective restoration wins partly because expert prompts are more accurate, not because selectivity per se is beneficial. The paper does not include a "manual full restoration" condition — where an expert specifies all present distortions without withholding any — which would isolate the benefit of targeted correction from oracle identification. The remote sensing case (Table 3, p=0.11 non-significant, full automated slightly better) further reveals the domain-contingency of the thesis and is consistent with an MLP identification error rather than a principled selectivity finding. The Section 4.2.1 claim that "controllability is not a convenience but a necessity" is therefore not cleanly supported as stated.

### Minor

- **Factual error in Section 4.1 claim about FID.** The paper states "PRISM achieves the best results across both fidelity (PSNR/SSIM) and perceptual metrics (FID/LPIPS)." Table 1 shows MPerceiver achieves FID 48.18 versus PRISM's 48.97; MPerceiver holds the best FID. This specific claim is false and should be corrected to accurately represent PRISM's second-place FID.

- **Scale mismatch in Table 1 comparisons.** PRISM is built on Stable Diffusion v1.5, a large pretrained generative model. The all-in-one baselines (AirNet, Restormer, NAFNet, PromptIR) are encoder-decoder architectures with no large generative pretraining. Comparing these in a single table without noting scale differences gives a misleadingly wide apparent gap. The more informative comparisons are against diffusion baselines (MPerceiver, AutoDIR, DiffPlugin), where PRISM's lead is smaller and more architecturally meaningful.

- **Latent disentanglement visualization is appendix-only.** Appendix Figure 13 contains the embedding space analysis that justifies the contrastive design. The main paper refers to it but contains no direct quantitative or visual summary of latent geometry. A concise version in the main text would make the mechanism more transparent.

### Trivial

- **Table 2 POLED LPIPS bolding error.** AutoDIR's LPIPS of 0.431 is bolded as best, while PRISM's 0.419 is underlined as second-best. Since LPIPS is lower-is-better, PRISM's 0.419 is the superior result and should be bolded. This is a table formatting error that does not affect the scientific content.

---

## Nice-to-Haves

- Adding a "manual full restoration" condition to Table 3 (expert specifies all present distortions, model removes all) would cleanly isolate the benefit of withholding certain corrections from the benefit of expert-accurate distortion identification — a straightforward experiment that would significantly strengthen the controllability argument.
- Reporting the MLP's distortion identification accuracy would clarify how much of the Table 3 gap is driven by identification errors vs. principled selective correction.
- Including even a scalar disentanglement metric (e.g., linear probe separability of distortion categories before vs. after fine-tuning) in the main text would make the compositional structure claim more concrete without requiring Appendix Figure 13.
- Extending controllability to spatial localization (e.g., "remove haze in the sky only") is acknowledged as future work in Section 4.2.1 and would be a natural and impactful extension.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Missing DA-CLIP comparison (harsh critic):** Removed per hard rule against flagging missing related works/baselines. The existence and relevance of specific prior comparisons cannot be verified without external sources.

- **GPT-4 prompt alignment noise concern (harsh critic):** Removed as speculative. The paper explicitly describes using partial prompts and negative prompts to expose the model to semantically inconsistent conditions during training (Section 3.1), which directly addresses the concern about prompt-augmentation misalignment. The critic's concern is already handled.

- **SCPM ablation-cleanliness concern (harsh critic):** Partially removed. PRISM's SCPM is explicitly adopted from Jiang et al. (2024) (AutoDIR), meaning both models likely use it; therefore the comparison is not contaminated by SCPM as a confounder. This cannot be verified but per the paper's acknowledgment it is a shared module, not PRISM's exclusive advantage.

- **Zero-shot evaluation protocol favoriting PRISM's encoder (harsh critic):** Removed as minor/speculative. The paper uses the compound-aware encoder to generate category labels, then applies identical manual prompts to all models. Using the same prompts for all models is a reasonable and practical protocol; the concern that PRISM's encoder produces better categories for its own latent space cannot be confirmed from the paper.

- **Abstract "one distortion at a time" characterization (harsh critic):** Removed as a scope creep nitpick. The abstract is a reasonable simplification; Section 2.2 carefully acknowledges composite methods. This is not a factual misrepresentation.

- **Variance reporting in Table 1/Table 2 (harsh critic):** Moved to removed. Single-run evaluation without confidence intervals is the norm for large-scale image restoration benchmarks. The paper does report mean ± std in Table 3 where it matters most (downstream scientific utility). Demanding the same for Table 1 is above community norms.

- **Strength — "PRISM outperforms all baselines on FID" (strength finder, implicit):** Removed. Table 1 shows MPerceiver achieves better FID (48.18 vs. 48.97). This specific claim in the strength is incorrect.

---

## Novel Insights

The paper's most genuinely novel contribution is the empirical demonstration, in Table 4, that different scientific analyses of the *same* image require *opposing* restoration strategies: super-resolution maximizes segmentation accuracy but degrades fluorescence measurement precision, while denoising has the reverse effect. This "no single policy" finding is not a theoretical claim but a measured, domain-grounded result that challenges the standard assumption that cleaner images are uniformly better for downstream science. Combined with Figure 6's illustration that automated denoising erases biologically relevant structures in microscopy, this constitutes a credible and practically important argument for domain-expert-guided restoration that goes meaningfully beyond prior work on perceptual quality.

---

## Suggestions

1. **Add a "manual full restoration" row to Table 3** (expert labels all distortions, model removes all) to isolate selectivity as the causal factor in downstream improvements, decoupling it from MLP identification accuracy.
2. **Correct the FID claim in Section 4.1** to accurately reflect that MPerceiver holds the best FID on MDB.
3. **Fix the POLED LPIPS bolding in Table 2** — PRISM's 0.419 should be bolded as best, not AutoDIR's 0.431.
4. **Add PRISM-Primitive-Aware as an explicit row in Table 1** alongside baselines to enable readers to directly attribute the performance gap between PRISM and the best diffusion baseline to data vs. architecture.
5. **Add a concise latent space metric or visualization to the main paper** (e.g., Figure 13 excerpt or a linear probe accuracy table) to make the compositional disentanglement claim self-contained without relying on the appendix.

---

## Evaluation Axes

- **Originality:** High. The compositional Jaccard-weighted contrastive loss, the scientific downstream utility benchmark, and the task-dependency finding (Table 4) are novel contributions specific to this paper.
- **Importance of research question:** High. Controllable restoration for scientific imaging is a genuine gap in the field with real consequences for downstream analysis validity.
- **Claims well-supported:** Moderate. Zero-shot generalization and downstream utility findings are well-supported. The primary Table 1 comparison conflates data and architectural advantages, and the controllability argument (Table 3) has an uncontrolled confound. These are addressable but meaningful gaps.
- **Soundness of experiments:** Moderate-high. The experimental design across four domains is thorough; the statistical testing in Table 3 is appropriate. The confound in Table 3 and the training asymmetry in Table 1 reduce confidence in two of the paper's three headline claims.
- **Clarity of writing:** High. The paper is clearly structured, the method is well-described, and the motivation is effectively communicated.
- **Value to research community:** High. The benchmark, dataset (Rooftop Cityscapes), and the task-dependency finding provide concrete artifacts and insights directly applicable to practitioners in scientific imaging.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>