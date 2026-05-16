Now I have all the information needed. Let me construct the final consolidated review.

## Summary

SuperMark proposes a training-free image watermarking framework that repurposes a pretrained diffusion-based super-resolution (SR) model for both watermark embedding and extraction. Watermarks are injected into Gaussian noise via existing methods (Gaussian Shading or Tree-Ring), embedded through the SR denoising process, and recovered via DDIM inversion. The method achieves 99.46% bit accuracy under normal distortions and 89.29% under adaptive attacks on MS-COCO, outperforming nine baselines on robustness while maintaining reasonable fidelity (PSNR 32.49, SSIM 0.93), all without any model training.

## Strengths

- **Genuinely training-free framework.** SuperMark reuses a frozen pretrained diffusion SR model for both embedding and extraction, bypassing the expensive encoder–decoder training required by all deep-learning baselines. The paper explicitly states that "both the SR model M and the VAE operate with frozen parameters, meaning no additional training is required" (Sec. 3.2), and the full pipeline in Figure 2 runs without fine-tuning. This is a clean architectural contribution that directly contrasts with the traditional encoder–noise–decoder paradigm.

- **Strong robustness against both normal distortions and adaptive attacks.** In Table 1, SuperMark achieves the highest average bit accuracy of 99.46% under normal distortions and 89.29% under adaptive attacks—substantially exceeding all nine baselines. Many baselines collapse to near-chance under adaptive attacks (e.g., DwtDctSvd at 51.22%, MBRS at 57.28%), while SuperMark maintains high accuracy. This is the paper's strongest empirical contribution.

- **Good transferability across diverse settings.** SuperMark maintains consistent extraction accuracy across four additional datasets (DiffusionDB, WikiArt, CLIC, MetFACE; Table 2), two different SR models (SD-Upscaler vs. LDM-SR; Table 3), a different watermark injection method (Tree-Ring; Table 4), and different resolutions. This demonstrates practical flexibility beyond a one-off configuration.

- **Elegant conceptual insight linking watermarking and diffusion processes.** The paper identifies and exploits the symmetry between watermark embedding/extraction and the denoising/noising processes in diffusion models. Leveraging DDIM inversion's inherent robustness to perturbations provides a principled theoretical foundation for why robustness emerges without adversarial training.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled watermark payload across baselines.** The paper embeds 32 bits for SuperMark (Sec. 4.1) but does not report the payload sizes of any baseline method. In digital watermarking, payload directly affects both robustness and fidelity—smaller payloads make the task easier. Without controlling for payload (either by equalizing it or by presenting accuracy-vs-payload curves), the robustness advantage claimed in Table 1 may partially reflect asymmetric task difficulty. This is a structural gap in the evaluation that needs to be addressed before the comparative claims can be fully trusted.

### Minor

- **Fidelity claim is slightly overstated.** The abstract and introduction state that SuperMark offers "fidelity comparable to existing methods." Table 1 shows SuperMark at PSNR 32.49/SSIM 0.93, while top baselines reach 36–37 PSNR and 0.97 SSIM. The fidelity is reasonable and within the range of methods tested, but "comparable" glosses over a meaningful gap to the best-performing methods. The paper would be more credible if it explicitly acknowledged this trade-off and framed the contribution as "competitive fidelity in exchange for significantly superior robustness."

- **ZoDiac comparison (Table 4) relies on numbers from the original paper without controlled conditions.** The paper transparently states "The corresponding results of ZoDiac are those presented in their paper," but this means experimental conditions (distortion parameters, dataset sampling, resolution pipeline) may differ. While citing published results is common practice, the claim that SuperMark "maintains better fidelity and exhibits significantly stronger robustness against rotation" relative to ZoDiac would be much stronger if ZoDiac were run under identical conditions. This is a standard limitation of cross-paper comparisons, not a fatal flaw.

- **Distortion parameters are not specified.** The paper lists normal distortions (JPEG compression, random cropping, Gaussian blur, Gaussian noise, brightness adjustments) but does not give exact parameters (e.g., JPEG quality factor, cropping percentage, blur kernel size, noise variance). This hinders reproducibility and makes it difficult for readers to assess whether the distortion severity is comparable to that used by baselines.

- **No statistical significance reported.** With 500 images, standard deviations or confidence intervals on bit accuracy should be provided, especially for the adaptive attack results where performance varies more.

- **The claimed "critical insight" that the encoder–noise–decoder architecture creates a trade-off between robustness and fidelity is not novel.** This trade-off is well-understood in the watermarking literature. The paper's real insight is the specific idea of leveraging SR diffusion models for training-free watermarking, which should be emphasized instead.

### Trivial
None.

## Nice-to-Haves

- A systematic trade-off analysis varying the strength factor $f_s$ (currently fixed at 0.4) and plotting PSNR/SSIM vs. bit accuracy would let readers evaluate the Pareto frontier directly and strengthen confidence in the chosen operating point.
- Adding perceptual metrics (LPIPS, or qualitative examples) would strengthen the fidelity argument, especially since the method uses a generative SR model whose outputs may look different from originals at the same PSNR.
- Reporting baseline payload sizes and/or running a controlled payload-equalized experiment would fully resolve the major weakness above.

## Removed Points

These points are flagged to be removed per policy; treat them with caution:

- **Missing Section 4.4 (ablation study).** The reviewer criticized the absence of Section 4.4 referenced in the paper. This section was almost certainly present in the original submission and stripped by the PDF parsing/extraction pipeline. Per policy, parser-stripped content is not a valid weakness.
- **"Fidelity is not comparable — the gap is substantial and the paper does not discuss it."** The paper explicitly discusses the robustness–fidelity trade-off in Sec. 3.3 (introducing the strength factor $f_s$ and the downscaling trade-off) and references Sec. 4.4 for detailed analysis. While the fidelity claim is mildly overstated (noted in Minor above), the characterization of a paper that "does not even discuss this discrepancy" is inaccurate.
- **"The critical insight is not new; it is well understood."** While the trade-off itself is known, the specific insight about leveraging the denoising/noising symmetry in diffusion models for training-free watermarking is genuinely novel. The reviewer conflates a general observation with the paper's specific instantiation.
- **Claims about missing perceptual metrics being necessary.** PSNR and SSIM are standard fidelity metrics in the watermarking literature. While LPIPS would be a welcome addition, its absence is not a weakness.
- **Strength from Strength Finder about "competitive fidelity" and "unifying robustness and fidelity without the trade-off."** This conflicts with the verified weakness that fidelity is below top baselines, so it is moved here per policy (weakness wins over strength when they disagree).

## Novel Insights

The reviews surface a tension that the paper itself does not fully engage with: the claimed "comparable fidelity" sits uncomfortably next to a 4–5 dB PSNR gap versus the best baselines. This is not fatal—the fidelity numbers are still within an acceptable range—but the paper would benefit from explicitly characterizing this as a deliberate trade-off (better robustness, acceptably lower-but-not-degraded fidelity) rather than claiming parity. The payload control issue is the one genuinely structural concern that, unaddressed, weakens the comparative claims. Neither reviewer identified any fatal flaw; the core idea is sound and the robustness results are impressive.

## Suggestions

1. **Report and control for payload.** Add a supplementary table showing baseline payload sizes. Better yet, evaluate all methods at a common payload (e.g., 32 bits) to verify the robustness advantage holds under equal conditions.
2. **Acknowledge the fidelity trade-off explicitly.** Replace "comparable" with language like "competitive fidelity given the substantial robustness gains" and consider a trade-off plot of PSNR vs. accuracy across different $f_s$ values.
3. **Run ZoDiac under identical conditions or soften the comparison claims.** If running ZoDiac is infeasible, explicitly note the cross-paper limitation.
4. **Specify all distortion parameters** in the experimental setting for reproducibility.
5. **Add confidence intervals or standard deviations** to the main results table.

## Score and Decision

This paper presents a genuinely novel, training-free watermarking framework with strong robustness results across a thorough set of baselines and distortions. The core idea is elegant and clearly explained. The main concerns—uncontrolled payload, slightly overstated fidelity claims, and cross-paper ZoDiac comparison—are real but fixable and do not undermine the central contribution. The method's 89.29% adaptive-attack accuracy is particularly notable given that most baselines collapse under such conditions. With the evaluation gaps addressed, this would be a solid contribution to the watermarking community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>