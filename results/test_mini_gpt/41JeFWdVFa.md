## Summary
The paper proposes LDP, a lightweight conditional denoising-autoencoder degradation module for single-image super-resolution. LDP predicts an LR image from an HR/SR image conditioned on the LR high-frequency residual, and is used either as an auxiliary cycle-consistency loss during fine-tuning or as a diffusion posterior-sampling guidance term at inference. The paper reports broad empirical improvements on synthetic SR benchmarks and some real-world no-reference metrics, but the central causal and generalization claims are not fully isolated by the experimental design.

## Strengths
- **Broad training-time evaluation across heterogeneous SR backbones.** Table 3 evaluates FeMaSR, StableSR, SwinIR, and MambaIR across five synthetic degradation types. The reported gains are especially substantial for StableSR, e.g. Hybrid PSNR improves from 19.27 to 21.43 and JPEG PSNR from 20.17 to 21.91. This supports that the proposed fine-tuning recipe can improve multiple classes of SR models.
- **The proposed module is genuinely lightweight relative to typical SR/diffusion systems.** Section 4.1 reports 642k LDP parameters, 60K training iterations, and training on a single RTX A6000 in about 16 hours. This concretely supports the “lightweight plug-in” aspect of the contribution.
- **The paper directly evaluates LR-prediction behavior.** Section 4.2 and Table 1 compare LDP with DRN and DualSR for predicting LR images from SR outputs under multiple degradation types; LDP performs best on several complex settings, including Hybrid PSNR/SSIM/LPIPS. Although this comparison has an important caveat noted below, it is a useful attempt to evaluate the degradation model itself rather than only downstream SR quality.
- **The paper includes some targeted ablations.** Tables 6 and 7 study loss-term combinations and the high-frequency weighting factor τ for SwinIR on the Hybrid synthetic setting. These ablations show that the full loss recipe performs best among the variants tested, even though they do not resolve the main attribution concern.

## Weaknesses

### Fatal
None.

### Major
- **The main fine-tuning results do not isolate LDP from ordinary fine-tuning and added losses.** Section 3.3 states that fine-tuning augments the original SR loss with a Fourier-domain frequency loss in Eq. 14–15 and the LDP-based symmetric loss in Eq. 16. Section 4.1 further states that existing SR models are fine-tuned on DF2K using BSRGAN degradation patterns. Tables 3 and 4 compare original pretrained models against “+LDP” fine-tuned models, but the decisive baseline is missing: the same models fine-tuned on the same DF2K/BSRGAN data with the same schedule and non-LDP losses, but without the LDP cycle constraint. As written, the gains in Tables 3–4 may come from additional degradation-specific fine-tuning, the frequency loss, or their combination with LDP. This is the most important evidential gap because it directly affects the central claim that LDP itself improves generalization.
- **The LR high-frequency conditioning creates a real shortcut/leakage concern that is not tested.** Eq. 4 defines \(y_{hf}=y-y\downarrow_{s^2}\uparrow_{s^2}\), i.e. the condition is derived from the target LR image. Section 3.1 acknowledges that using the LR image itself could cause shortcuts, but does not demonstrate that this high-frequency residual avoids the same issue. Since \(y_{hf}\) is spatially aligned with the target LR input and can contain edges, noise, compression artifacts, and texture residuals, LDP may partially reconstruct the target LR from the condition rather than learning a degradation operator from HR/SR to LR. This affects both the interpretation of Tables 1–2 and the strength of the cycle-consistency constraint in Eq. 16.
- **The “unseen/unknown degradation” claim is overstated relative to the evaluation.** Section 4.1 says LDP is trained on LSDIR with BSRGAN degradations, the SR models are fine-tuned using BSRGAN degradation patterns, and synthetic testing uses bsrGAN.plus / BSRGAN / Real-ESRGAN-style degradations. These are meaningful stress tests, but they remain within a related synthetic degradation family. Table 4 provides real-world evaluation, but the metrics are no-reference and mixed in several cases. The evidence supports improvement under related synthetic degradations and some real-world benchmarks, but not the broad headline claim in the abstract and conclusion that LDP “substantially improves” generalization to unseen/unknown complex degradations.
- **The inference-time posterior-sampling claim is much weaker than the training-time claim.** Eq. 17 proposes using LDP for diffusion posterior sampling, but Table 5 shows inconsistent and often tiny changes. LDM worsens on many RealSR metrics; ResShift changes are near zero in many entries; UPSR has small mixed changes; StableSR is the clearest positive case. This does not support the broad claim in the abstract/contributions that LDP generally “mitigates artifacts at inference independently of training.” The paper should narrow this claim to model-dependent inference-time benefits, with strongest evidence for StableSR.

### Minor
- **The real-world results are described more uniformly than the table supports.** Section 4.3 says LDP improves performance “across almost all datasets and metrics,” but Table 4 contains clear degradations for FeMaSR on DPED and RealSRSet for several no-reference metrics, and small degradations for SwinIR/MambaIR on NIQE in some datasets. The qualitative claim should be more carefully aligned with the mixed metric behavior.
- **The LR-prediction comparison is structurally unequal.** In Section 4.2, LDP is conditioned on \(y_{hf}\), while DRN is described as having only HR/SR input and no conditional signal. Table 1 therefore partly measures the advantage of target-derived conditioning, not only the quality of a learned degradation operator. This does not invalidate the experiment, but it weakens the interpretation.
- **Some reported improvements are numerically very small.** In Table 3, MambaIR gains on Down are +0.05 PSNR and +0.0010 SSIM, and several LPIPS/SSIM differences for strong baselines are similarly small. This is not a fatal issue, but the paper should avoid implying that all gains are equally meaningful.

### Trivial
None.

## Nice-to-Haves
- Add repeated-run statistics or confidence intervals for the smallest Table 3 improvements, especially for strong baselines such as MambaIR.
- Provide aggregate summaries for Table 4 and Table 5, e.g. average rank or win/loss counts per model and dataset, to make the mixed no-reference results easier to interpret.
- Include stronger held-out-degradation protocols: train/fine-tune while excluding one degradation family, then test on that family; or evaluate on a synthetic degradation generator not used in LDP training or SR fine-tuning.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **“The paper is invalid because the diffusion-alignment motivation is not proven.”** The paper’s motivation in Section 3.1 is somewhat under-justified, but the method is primarily empirical and cites prior diffusion-model observations. Lack of a formal proof is not a fatal flaw for this kind of empirical SR paper.
- **“The denoiser does not literally estimate an identifiable blur kernel.”** Section 3.2 says the CNN denoiser “estimates the blur kernel,” which may be interpretive rather than literal, but this is mainly a wording/interpretability issue and not a core methodological flaw.
- **“The prediction-dependent DWT mask \(M\) may create non-obvious optimization behavior.”** Eq. 13 derives \(M\) from predicted LR high-frequency subbands, but the criticism is speculative without concrete evidence of failure. It can be explored by the authors but should not count as a substantive weakness.
- **“The paper lacks missing appendix details/proofs.”** Appendix material is stripped from the extracted text, so missing appendix details should not be penalized.
- **Strength Finder claim: “Table 2 proves LDP is not merely learning trivial downsampling.”** Table 2 is a useful diagnostic, but low similarity to bicubic-downsampled SR does not by itself rule out copying target-like residuals from \(y_{hf}\). This strength is therefore overclaimed.
- **Strength Finder claim: “Real-world benchmarks validate generalization beyond synthetic degradations.”** Table 4 is a strength insofar as real-world benchmarks are included, but the results are mixed and use no-reference metrics. This should be treated as partial evidence, not validation of the full generalization claim.
- **Any criticism about missing related work or reference availability.** These are not included because external availability and missing-reference claims cannot be reliably verified here and are disallowed by the review instructions.

## Novel Insights
The key tension in this paper is that LDP’s conditioning is both the source of its apparent strength and the source of its main evidential vulnerability. Conditioning on LR high-frequency residuals plausibly helps distinguish different degradations for the same HR image, which is precisely the problem the paper targets; however, because that condition is derived from the target LR image, it also risks turning LR prediction into a target-conditioned reconstruction task rather than a clean degradation-modeling task. The paper would be much stronger if it embraced this ambiguity and directly quantified how much information comes from the HR/SR input versus the LR-derived condition.

## Suggestions
- Add the critical fine-tuning controls: original pretrained model; fine-tuned on the same DF2K/BSRGAN data without LDP; fine-tuned with frequency loss only; fine-tuned with a simple learned downsampler/cycle loss; and fine-tuned with full LDP.
- Test the \(y_{hf}\) shortcut hypothesis directly: zero \(y_{hf}\), shuffle it across images, shuffle it across degradations for the same HR image, and evaluate a \(y_{hf}\)-only LDP variant without HR/SR input.
- Narrow claims around “unseen degradation” unless stronger held-out-degradation results are added.
- Reframe posterior sampling as an optional guidance mechanism with model-dependent effectiveness, rather than a broadly established inference-time correction method.
- In Table 4 and Table 5, report aggregate win/loss counts and explicitly discuss cases where LDP hurts metrics.

## Overall Evaluation
In terms of **originality**, the paper has a moderately original and potentially useful idea: a lightweight conditional LR-prediction module used as a cycle-consistency regularizer or diffusion guidance term. In terms of **importance**, improving SR generalization to real-world degradations is a valuable research direction. The **claims are only partially supported**: the empirical breadth is good, but the main causal claim is confounded by fine-tuning and additional losses, and the target-derived conditioning is not adequately controlled. The **experimental soundness** is therefore mixed: many models and datasets are tested, but the most important baselines and leakage ablations are absent. The **writing is generally clear**, though several claims are stronger than the evidence. The work has potential value to the SR community, but it currently needs stronger isolation of the proposed mechanism before acceptance.

## Score and Decision

### Calibration and Anchors

**Round 1 retrieved anchors**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OKOjkFrhSs.md`, avg score 3.00, Round 1 weak anchor — A rejected SR plug-in paper with limited novelty and concerns about real-world robustness; the present paper is stronger because it evaluates more modern/diverse SR backbones and includes real-world benchmarks.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dAavOuxZvo.md`, avg score 3.00, Round 1 weak anchor — A diffusion inverse/inpainting paper with major effectiveness concerns; the present paper has more concrete SR evidence and is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/W4djmqKZC6.md`, avg score 3.00, Round 1 weak anchor — A diffusion-method paper judged weak due to methodological and empirical concerns; the present paper is better supported empirically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vK8C37eHXM.md`, avg score 3.20, Round 1 weak anchor — A diffusion/autoencoder paper with unclear contribution and evidence; the present paper is stronger and more directly evaluated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QO3yH7X8JJ.md`, avg score 5.25, Round 1 middle anchor — A diffusion SR paper with an interesting idea but overclaiming and experimental gaps; the present paper is comparable, with stronger breadth but similarly important attribution gaps.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JmGEZXkCH3.md`, avg score 3.67, Round 1 middle anchor — An SR augmentation paper with limited support and novelty; the present paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BtT6o5tfHu.md`, avg score 6.67, Round 1 middle/strong anchor — A plug-and-play diffusion SR sampling paper with stronger theoretical/experimental support despite concerns; the present paper is weaker because its main gains are not causally isolated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vTdwuKUc5Z.md`, avg score 4.25, Round 1 middle anchor — An SR prompt paper with limited novelty/evidence; the present paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6EUtjXAvmj.md`, avg score 8.00, Round 1 strong anchor — A posterior-sampling paper with strong theory and broad validation; the present paper is substantially weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OlzB6LnXcS.md`, avg score 8.00, Round 1 strong anchor — A strong diffusion-method paper with consistent results; the present paper is much weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6O3Q6AFUTu.md`, avg score 8.00, Round 1 strong anchor — A strong diffusion image-method paper with clearer novelty/evidence; the present paper is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I5lcjmFmlc.md`, avg score 8.00, Round 1 strong anchor — A strong diffusion robustness paper; not very topically close, but clearly above the present paper in support.

**Round-1 bracket:** Based on these anchors, the paper is clearly above the weak 3–4 SR/diffusion papers but below the 6.5–8 papers with stronger causal isolation, theory, or controlled evaluation. The plausible bracket after Round 1 was **5.0 to 6.0**.

**Round 2 retrieved anchors**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/46mbA3vu25.md`, avg score 5.75, Round 2 — A controlled empirical ISR comparison with useful insights but mixed conclusions and some setup concerns; the present paper has a more direct method contribution but weaker causal controls, so it is slightly weaker overall.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QO3yH7X8JJ.md`, avg score 5.25, Round 2 — Similar level: interesting diffusion/SR idea with overclaiming and missing decisive evaluations. The present paper is comparable but its missing no-LDP fine-tuning baseline is a central weakness.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2ogxyVlHmi.md`, avg score 4.75, Round 2 — A real-world SR diffusion paper with novelty/fairness concerns; the present paper is somewhat stronger due to breadth and a clearer plug-in formulation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FWpO8u2lim.md`, avg score 5.25, Round 2 — A diffusion Real-ISR paper with reasonable results but unresolved design/ablation questions; the present paper is very comparable, with similarly important missing ablations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/my0RqY48xz.md`, avg score 6.50, Round 2 — An SR generalization paper with clearer theoretical framing and analyses; the present paper is weaker because its main empirical effect is confounded.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BtT6o5tfHu.md`, avg score 6.67, Round 2 — A stronger plug-and-play diffusion SR method with better-supported claims; the present paper is below this anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5cYTAcZAgt.md`, avg score 5.67, Round 2 — A diffusion SR method with moderate novelty and empirical support; the present paper is comparable but held back by a more direct attribution gap.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1YO4EE3SPB.md`, avg score 5.50, Round 2 — A diffusion inverse-problem paper with interesting formulation but incomplete empirical support; the present paper is comparable in overall support level.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Z9Odi09Rv9.md`, avg score 4.75, Round 2 — A diffusion inverse-solver paper with major consistency concerns; the present paper is stronger.

**Final calibration:** Round 2 places this paper around the 5.0–5.5 range. It is stronger than the 4.75 anchors because it has a coherent method and broad SR evaluation, but weaker than the 5.75–6.5 anchors because the decisive no-LDP fine-tuning baseline and conditioning-leakage ablations are absent. I therefore assign **5.0**: a promising but insufficiently validated paper, below the acceptance threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>