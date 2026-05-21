---
job_id: 4ad17268-0bb4-4d2b-a046-20ba58847565
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 41JeFWdVFa.pdf
paper: LDP: A Lightweight Denoising Plugin Enhancing Generalization in Single-Image Super-Resolution
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies a learned degradation/denoising plug-in for image super-resolution, touching generative modeling, representation learning for vision, and diffusion-based restoration.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, experiments with quantitative and qualitative results, and a conclusion/limitations section. While I found substantial concerns about novelty, clarity, and experimental support, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, instructions aimed at automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes LDP, a lightweight denoising autoencoder plug-in for single-image super-resolution that learns to map an HR image, conditioned on an LR high-frequency residual, back to a predicted LR image. The module is used in two ways: as an auxiliary cycle-consistency style loss during fine-tuning of existing SR models, and as an inference-time guidance term for posterior sampling in diffusion-based SR. Experiments are reported on synthetic multi-degradation benchmarks and several real-world datasets, with comparisons across multiple SR backbones and diffusion models.

## Strengths
The paper has a reasonably clear high-level goal, namely improving SR robustness to unseen degradations without redesigning each base SR architecture. That objective is important and practically relevant.

The plug-in aspect is appealing. The same LDP module is used in two modes, training-time regularization and inference-time posterior guidance, and the paper demonstrates this on diverse backbones including GAN-, Transformer-, Mamba-, and diffusion-based SR models. Even if I have reservations about how fully this generality is validated, the attempt to provide a model-agnostic mechanism is a meaningful design choice.

The architecture is lightweight in parameter count. Section 4.1 states that LDP has only 642k parameters, and the framework in **Figure 2** is simple enough that one can understand the intended data flow: the LR high-frequency residual \(y_{hf}\) is fed into the degradation prediction module, HR is corrupted patchwise, and the denoiser then predicts features that are downsampled to LR. In particular, **Figure 2(a)-(d)** helps make the modular decomposition concrete, and **Figure 2(b)** is useful in clarifying that the conditioning signal is implemented via a learned degradation prompt modulated by a weight map from \(y_{hf}\). This figure does real explanatory work for the paper.

There is a fairly broad empirical sweep. **Table 3** shows results across four families of SR models and five degradation types, and the trend is mostly positive. The gains for StableSR are especially noticeable on the synthetic benchmarks, for example on Hybrid and JPEG. Even if some gains are small for stronger deterministic models like MambaIR and SwinIR, the consistent direction of improvement on PSNR/SSIM is a favorable sign that the plug-in is not completely brittle.

The qualitative examples in **Figure 4** and **Figure 5** do suggest that LDP can suppress some visually unpleasant artifacts. In **Figure 4**, the FeMaSR outputs with LDP look less aggressively over-textured than the original FeMaSR outputs, and in **Figure 5** there are visible reductions in ringing and repetitive texture artifacts for some methods. These figures support the narrower claim that the method can act as an artifact suppressor.

The paper includes several ablations, especially around the loss composition and conditioning design. **Table 6** and **Table 7** at least show that the reported gains are not solely from one arbitrary hyperparameter setting, and **Table 8-10** further explore patch size, wavelet band selection, and the residual scale factor \(s'\). I would not call the ablations complete, but there is effort here.

The limitations section is short but at least acknowledges that the method is not a generative degradation model in the strongest sense and that it cannot support unpaired degradation modeling.

## Weaknesses
I have multiple substantial concerns, and several of them go to the core scientific claim rather than presentation polish.

1. **The central theoretical motivation is asserted much more strongly than it is established.**  
   On **Page 3-4**, the paper claims to leverage a “property of diffusion models” that after adding noise, HR features and LR features become aligned, making denoising noisy HR features equivalent to denoising noisy LR features. This is doing enormous conceptual heavy lifting for the method, but in the paper it is only cited to prior work and never formalized for the current setting. There is no statement of what “aligned” means, under what degradation family this equivalence is expected to hold, whether it is approximate or exact, or why it should remain valid when the corruption is **patch-dependent** as introduced in **Equation (7)**. The method is then built around this equivalence, yet the paper never derives a condition like
   \[
   p(x_t \mid x, t) \approx p(\tilde y_t \mid y, t)
   \]
   or any feature-level relation that would justify replacing LR-side denoising by HR-side denoising. As written, this is more intuition than technical grounding. That matters because the main methodological contribution rests on a bridge that is never convincingly built.

2. **The degradation model is not actually well specified mathematically, despite several equations.**  
   The notation around the conditioning pathway and the denoiser is muddled enough that it is hard to tell what is computed per pixel, per patch, or globally. In **Equation (6)**, \(P_D \in \mathbb{R}^{N_p \times C}\) while \(C' \in \mathbb{R}^{H \times W \times C}\). The paper says a resized weight map is multiplied element-wise with the degradation prompt, but this only makes sense if one first explains how the prompt dimension \(N_p\) is lifted to spatial dimensions. Is \(P_D\) reshaped to a spatial tensor, tiled, or projected? The current equation
   \[
   C' = P_D \otimes \mathrm{Resize}(w, H, W)
   \]
   is dimensionally unclear.

   Similarly, in **Equations (8)-(11)**, the conditioning variable \(z\) is mentioned in the text but never appears explicitly in the equations, which instead use \(C' + t_{emb}\). Yet \(t_i\) is assigned per patch in **Equation (7)**, while \(C'\) appears spatially dense over the image. It is unclear whether AdaLN parameters \((\alpha,\beta,\gamma)\) are produced per patch, per spatial site, or per channel only. This ambiguity is not cosmetic, it makes the implementation and even the intended inductive bias hard to reconstruct.

   There is also slippage between “HR images”, “HR features”, and “noisy HR features”. In **Equation (2)**, \(x_t = NAM(x,t)\), where \(x\) is an image. In the text around **Equation (11)**, the denoiser operates on features \(F_i\), with \(F_0=x_t\). So is \(x_t\) an image tensor or an encoded feature tensor? The paper uses both interpretations interchangeably.

3. **The training objectives are underspecified and in places conceptually shaky.**  
   In **Equation (13)**, the loss is computed on \(M \otimes y'\) and \(M \otimes y\), where \(M\) is formed by summing high-frequency DWT subbands of the *predicted* LR image \(y'\). This choice has nontrivial implications because the weighting mask then depends on the model output, and gradients flow not only through the image term but also through the mask. That can be fine, but the paper does not discuss it at all. If the intent is a fixed weighting map, then \(M\) should arguably be detached or derived from \(y\); if the intent is adaptive emphasis, then the optimization consequences should be explained. Right now it reads like an implementation choice that could materially change the training dynamics without any justification.

   The same issue appears in fine-tuning with **Equation (16)** through \(M'=\tau M\). Again, \(M\) depends on the predicted LR image. This means the “symmetric loss” is not merely comparing predicted and observed LR, it is also reweighting that comparison according to model predictions. That is a very different objective than a standard cycle consistency loss, and the paper never analyzes it.

   In **Equation (14)**, the frequency loss is defined over Fourier coefficients using a distance \(D\) in **Equation (15)**. The text says this supervises amplitude and phase, but the formula is simply the Euclidean distance in real-imaginary coordinates. That is not the same as explicitly supervising amplitude and phase. The wording should be corrected or the derivation rewritten in polar form.

4. **The experimental positioning of the degradation model is weak, and some tables undercut the paper’s own narrative.**  
   The LR prediction evaluation in **Section 4.2** is not as convincing as the text suggests. In **Table 1**, LDP beats DualSR clearly and often improves LPIPS a lot, but DRN still has much higher PSNR on Down and JPEG. The authors explain this away by saying DRN behaves like bicubic downsampling, but then **Table 2** is supposed to support that claim by measuring similarity between generated LR and downsampled SR. Here the interpretation becomes awkward: LDP indeed has lower similarity to downsampled SR than DRN, but its LPIPS values are *worse* than DRN by a large margin on all degradations in **Table 2**. That means LDP’s generated LR is farther from simple downsampling, yes, but the paper equates this with “better degradation modeling” without showing why this deviation is desirable beyond the chosen narrative. A model can be different from bicubic without being more faithful.

   Put differently, the pair of **Table 1** and **Table 2** demonstrates non-collapse only indirectly, and the evidence is not airtight. The argument would be much stronger if the paper evaluated degradation-parameter recovery, or at least whether the learned LR predictions preserve the degradation family indicated by the input. Right now the tables mostly show that LDP is not trivial, not that it is correct.

5. **The baseline selection is too narrow for the degradation-modeling claim, and the literature positioning is incomplete.**  
   For the core degradation-model comparison in **Table 1-2**, only DRN and DualSR are used. These are not enough to establish the proposed method as the right answer to robust degradation-aware SR in 2026. The paper itself cites several other relevant approaches in the introduction and related work, especially methods using consistency, test-time adaptation, or diffusion-based guidance, but does not compare against them in the central experiments. This matters because the claimed contribution is not just “another SR regularizer”, it is specifically a degradation-modeling plug-in.

   More broadly, the paper’s “plug-in denoiser / plug-and-play restoration” framing feels under-positioned relative to established restoration literature. The work would benefit from discussing how it differs from broader plug-and-play denoiser priors and diffusion-based restoration guidance methods, because the current related-work section is very SR-specific and somewhat siloed.

6. **The claimed generality is overstated relative to the actual evidence.**  
   The paper repeatedly says LDP can be seamlessly integrated into arbitrary SR models, but the actual evidence is much less universal. The fine-tuning setup in **Section 4.3** uses only four models, and the diffusion posterior sampling in **Section 4.4** applies only to latent diffusion pipelines where the predicted clean image \(\hat x_0\) is decoded and then guided. Even within those settings, the appendices reveal special handling, for example StableSR requires an extra noise-subtraction trick during posterior sampling. That does not invalidate the method, but it weakens the “arbitrary” and “seamless” language.

   **Figure 1(a)** is also slightly guilty here. It presents a clean, generic diagram where LDP can be attached to any SR model at training or inference, but the experimental section shows that the inference-time mode is really only demonstrated for diffusion-based samplers, not arbitrary SR models. The figure visually suggests a broader plug-in universality than the evidence supports.

7. **The real-world evaluation is difficult to interpret because the no-reference metrics move in inconsistent directions, and the paper selectively rationalizes this.**  
   In **Table 4**, many entries improve, but many also worsen. For FeMaSR on DPED and RealSRSet, several no-reference metrics deteriorate. The paper argues this is because flashy artifacts may be rewarded by some metrics. That may be true, but it is also a convenient post hoc explanation. Without user studies, task-specific downstream evaluation, or at least a more careful analysis of which metrics correlate with human preference in this setting, the real-world evidence remains mixed. The conclusion “consistently improves across almost all datasets and metrics” on **Page 8-9** is too rosy.

   The qualitative examples in **Figure 5** do show artifact reduction, but they also support a more nuanced conclusion: LDP often smooths or regularizes outputs. Whether that is always preferable is not resolved by the paper. On some methods, the trade-off looks like artifact suppression versus texture richness, which the appendix itself acknowledges.

8. **The posterior sampling contribution is modest and somewhat confounded.**  
   The diffusion-guidance results in **Table 5** are lukewarm. Many gains are tiny, several metrics worsen, and the method appears meaningfully helpful mainly for StableSR. The text says “the baselines show improvements across nearly all metrics on most datasets”, but this overstates what the table shows. For LDM in particular, the changes are mixed to negative. For ResShift and UPSR, many numbers are nearly unchanged. If anything, **Table 5** suggests that LDP-as-guidance is fragile and architecture-dependent.

   The qualitative results in **Figure 6** do suggest reduced artifacts, but because the StableSR posterior sampling setup also includes the extra noise-subtraction procedure discussed later in the appendix, it is hard to isolate what belongs to LDP itself versus the auxiliary artifact-removal trick. Since the main-paper claim is about LDP’s inference-time usefulness, the main paper should present this interaction much more transparently.

9. **There are several presentation and correctness issues in the tables and references that reduce trust.**  
   Some table headers and metric names are inconsistent or erroneous. In **Table 4** and **Table 5**, NIQE is written as “NQE”; MANIQA / CLIPIQA / QAlign appear as “MANXQA”, “CLIPQA”, and “QAlqut” in **Table 5**. **Table 6** has malformed loss names, such as repeated and corrupted symbols. The references section also contains obvious citation corruption, for example the entry for Chung et al. [2023] appears broken and mixed with the classic SRCNN citation. These may look minor, but when a paper makes many technical claims, this level of sloppiness undermines confidence that all experiments and formulas were checked carefully.

10. **The empirical gains, while often positive, are not large enough to outweigh the novelty and rigor concerns.**  
    In **Table 3**, the strongest deterministic models, especially MambaIR and SwinIR, often improve only marginally, sometimes by \(0.2\) to \(0.8\) dB and with tiny SSIM/LPIPS changes. For a method that introduces an additional learned module, extra losses, and a fairly specific degradation-conditioning design, I expected a more decisive empirical case, stronger baselines, or deeper analysis. The main headline seems to be that LDP is usually helpful, not that it substantially changes the state of the art or clarifies a previously unresolved mechanism.

## Questions
1. The key motivation in **Section 3.1** is that adding sufficient noise aligns HR and LR features, making denoising noisy HR features equivalent to denoising noisy LR features. Can the authors state this claim more formally, including what notion of alignment is intended and why it should still hold under the patch-wise corruption in **Equation (7)**? A concise derivation or even an explicit approximation statement would significantly increase my confidence.

2. Please clarify the tensor shapes and broadcasting rules in **Equations (5)-(11)**. In particular, how is \(P_D \in \mathbb{R}^{N_p \times C}\) converted into a spatial map compatible with \(\mathrm{Resize}(w,H,W)\)? Also, are \(\alpha,\beta,\gamma\) generated per patch, per location, or per channel? This needs to be unambiguous in the main paper.

3. In **Equation (13)** and **Equation (16)**, is the weighting map \(M\) detached from gradients or fully differentiable through \(y'\)? If fully differentiable, did the authors compare against using a target-derived or detached mask? This matters because otherwise the optimization objective is more adaptive than the text suggests.

4. The text says **Equation (14)-(15)** supervise amplitude and phase in the frequency domain, but the formula is written in real and imaginary components. Can the authors either justify this equivalence explicitly or revise the wording?

5. For the LR prediction study in **Table 1-2**, can the authors provide a stronger non-collapse analysis? For example, how does LDP behave when the same HR is paired with multiple degradations, and can it recover degradation-specific properties beyond merely being different from bicubic downsampling?

6. Since the paper emphasizes plug-in generality, could the authors clarify exactly which parts are universal and which require method-specific engineering? For instance, the posterior-sampling setup for StableSR appears to rely on an additional artifact-removal trick. How much of the reported gain comes from LDP alone?

7. The real-world results in **Table 4** are mixed across no-reference metrics. Is there any human preference study, or at least a more careful calibration of which metrics align with the intended visual improvements? A rebuttal with this analysis would help.

8. Could the authors report training and inference overhead in the main paper, not only the appendix? This is especially important because “lightweight” is a central claim, and the posterior-sampling runtime in the appendix appears nontrivial.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond the standard caution that image enhancement methods can be misused. The paper uses public image datasets and does not raise an ethics issue that requires special review based on the main text.

## Soundness Rating
2: fair. The overall methodology is plausible and supported by some experiments, but the central motivation is under-justified, several equations/objectives are underspecified, and parts of the empirical argument are weaker than claimed.

## Presentation Rating
2: fair. The high-level story is understandable and several figures are helpful, but the paper has too many notation ambiguities, table/reference errors, and overstatements for me to call the presentation good.

## Contribution Rating
2: fair. The plug-in idea is useful and practically motivated, but the conceptual novelty feels moderate, the differentiation from prior degradation-modeling and plug-and-play restoration work is not sharp enough, and the empirical evidence does not fully elevate it to a stronger contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and probably useful in practice, but in its current form I do not think the technical grounding, clarity, and experimental validation are strong enough for a clear ICLR accept.

## Reviewer Confidence
4: confident. I am familiar with SR, degradation modeling, and diffusion-based restoration, and I checked the main equations/tables carefully, though some implementation details are too ambiguous in the paper to verify completely.