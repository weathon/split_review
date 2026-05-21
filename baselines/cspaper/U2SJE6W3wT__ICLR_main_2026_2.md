---
job_id: 184c79bc-9f46-471a-b1b5-baf55a3f92d0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: U2SJE6W3wT.pdf
paper: Improved Adversarial Diffusion Compression for Real-World Video Super-Resolution
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, focusing on generative models, diffusion model compression, adversarial distillation, and representation learning for video restoration.

## Minimum Quality
Pass ✅ The paper includes the expected components, namely abstract, introduction, related work, method, experiments, quantitative/qualitative results, and conclusion, and it provides a technically coherent empirical study with nontrivial methodological contributions and substantial evaluation.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies efficient real-world video super-resolution by compressing a heavy one-step diffusion teacher, DOVE, into a smaller student called AdcVSR. The proposed method combines a pruned 2D Stable Diffusion-based backbone with lightweight 1D temporal convolutions, and introduces a dual-head, dual-domain adversarial distillation scheme intended to separately supervise spatial detail richness and temporal consistency. Experiments on synthetic and real-world Real-VSR benchmarks show strong efficiency gains relative to the teacher and competitive quality across fidelity, perceptual, and temporal metrics.

## Strengths
1. The paper targets a relevant problem. Compressing modern diffusion-based Real-VSR systems is practically important, and the paper makes a credible case that existing one-step methods are still too heavy for realistic deployment. The teacher-student framing is well motivated, and the efficiency numbers in **Table 1** are meaningful rather than cosmetic.

2. The central architectural idea is sensible and empirically supported. Replacing expensive 3D spatio-temporal attention with a "2D + 1D" student is not just an implementation tweak, because the student is asked to mimic a much larger 3D DiT teacher under aggressive compression. The ablation in **Table 2** is particularly helpful here: the plain 2D variant degrades sharply in temporal consistency, while the proposed 2D+1D design recovers most of the quality and improves \(E_{\mathrm{warp}}^*\) from 4.43 to 1.67 with only a tiny parameter increase from 0.52B to 0.55B. That is one of the more convincing pieces of evidence in the paper.

3. The adversarial design is more thoughtful than a generic "add GAN loss" recipe. The dual-head discrimination for detail vs consistency, applied in both pixel and feature domains, is well aligned with the paper's stated goal of resolving conflicting objectives. **Figure 2(b)** is actually useful here, not decorative, because it makes clear how the five data types induce asymmetric supervision for the two heads. The ablation in **Table 3** also supports that the design is not arbitrary: single-head dual-domain improves frame quality but hurts temporal consistency, while dual-head single-domain improves consistency but loses perceptual quality.

4. The experimental section is fairly comprehensive in the main paper. **Table 1** covers both synthetic and real-world settings, includes strong Real-VSR and Real-ISR baselines, and reports both quality and efficiency. The efficiency comparison is especially relevant because the claimed contribution is compression. Relative to DOVE, the paper shows a large reduction from 10.55B to 0.57B parameters and from 4.42s to 0.55s latency, while keeping quality in a competitive range.

5. The qualitative evidence is reasonably aligned with the quantitative story. In **Figure 3**, the temporal profiles are a useful choice because they directly visualize flickering, which is central to the paper's claims. The proposed method looks noticeably smoother than frame-wise image SR baselines such as AdcSR and HYPIR, while maintaining sharper details than several heavy video methods.

6. The paper is generally clearly written. The high-level motivation, method overview, and empirical narrative are easy to follow. **Figure 1** communicates the conceptual difference between prior ADC and the proposed extension to video quite effectively.

## Weaknesses
1. The novelty is meaningful but still somewhat incremental relative to prior ADC-style compression. At a high level, the paper extends image ADC to video by adding lightweight temporal modules and a more structured discriminator. That is a reasonable contribution, but the manuscript occasionally oversells it as if it were a broader methodological leap. The core recipe remains: prune a diffusion backbone, distill from a stronger teacher, and restore quality with adversarial learning. The paper would benefit from being more precise about what is genuinely new beyond AdcSR, especially since the architecture still reuses the same pruned SD2.1 backbone and much of the training philosophy from prior ADC work. This matters because for ICLR-level contribution, adaptation alone is not enough unless the paper clearly demonstrates why the video setting fundamentally changes the design problem.

2. A central methodological claim, that "details" and "consistency" are disentangled by the dual-head discriminator, is only partially validated. The ablations in **Table 3** are helpful, but they remain outcome-based. They show the final system works better, not that the two heads actually learn disentangled signals rather than acting as a stronger multi-task discriminator. There is no direct analysis of head behavior, gradient conflict, or head specialization. For example, the paper could have examined whether the detail head is insensitive to temporal shuffling while the consistency head reacts strongly, or whether gradients from the two heads have measurably different directional effects. Without such evidence, the strong language around "explicit disentangling" feels ahead of the validation.

3. The mathematical presentation around the losses is not fully clean. In **Equations (2) and (3)**, the generator loss uses \(\mathrm{Softplus}(-\mathcal{D}_{\text{pixel}}(\mathbf{x}_{\text{student}}))\) and \(\mathrm{Softplus}(-\mathcal{D}_{\text{feature}}(\mathbf{f}_{\text{student}}))\), but each discriminator has two heads according to the text. It is therefore unclear whether \(\mathcal{D}_{\text{pixel}}(\cdot)\) denotes a scalar obtained by summing the two head outputs, concatenating them, averaging them, or applying the adversarial term to both heads separately. This is not a cosmetic notation issue, because the exact generator objective determines how the student trades off detail and temporal realism. Similarly, in **Equation (4)** the loss is written over a generic \(\mathcal{D}\), but **Equation (5)** mixes pixel-domain and feature-domain tuples into a single set \(\mathcal{S}\), even though the two discriminators operate on different spaces. The intended implementation is inferable, but the formalism is sloppy. At minimum, the paper should define something like
\[
\mathcal{L}_{\mathrm{adv}}^{G} = \lambda_d \,\mathrm{Softplus}(-[\mathcal{D}_{\text{pixel}}(\mathbf{x}_{\text{student}})]_d) + \lambda_c \,\mathrm{Softplus}(-[\mathcal{D}_{\text{pixel}}(\mathbf{x}_{\text{student}})]_c)
\]
and analogously for the feature discriminator, if that is what is meant. Right now, the equations under-specify the core training objective.

4. The discriminator labeling scheme is clever, but some choices are under-justified and potentially brittle. In **Page 6**, real videos are left unlabeled for detail, while repeated images are labeled real for both heads, and random image collections are labeled real for detail but fake for consistency. These assignments encode a fairly strong assumption: that image detail richness transfers cleanly to video detail realism, while video data are not sufficiently detail-rich to supervise the detail head. That may be true for the chosen datasets, but the paper does not probe how sensitive the method is to this design. The appendix gives some ablations, but in the main paper this crucial supervision design is largely taken on faith. This matters because the paper's main conceptual contribution is exactly this structured adversarial supervision.

5. The empirical evidence, while broad, does not fully settle the trade-off against the teacher and stronger video baselines. **Table 1** supports the efficiency claim, but it also shows that AdcVSR is not uniformly close to DOVE or the strongest baselines on perceptual and reference metrics. For example on UDM10, AdcVSR trails DOVE on PSNR, SSIM, LPIPS, DISTS, CLIPIQA, and MUSIQ, even if it wins on \(E_{\mathrm{warp}}^*\) and DOVER. On VideoLQ, it is also not best on the perceptual metrics. That is fine in itself, but then the framing should be "very strong efficiency-quality trade-off" rather than implying near retention of teacher quality across the board. The current wording occasionally blurs this distinction.

6. The qualitative evaluation is somewhat selective. **Figure 3** supports the temporal consistency argument, but it only shows two examples, and both favor the proposed narrative quite cleanly. The paper would be more convincing with at least one failure case in the main paper, especially because the appendix itself later acknowledges limitations on foliage, water, and transparent regions. This matters because compressed generative restoration models often fail in exactly those texture-heavy scenarios where perceived sharpness can mask hallucination.

7. The ablation on temporal modeling is helpful but still incomplete for a paper making an architectural claim. **Table 2** and **Figure 5** show that adding 1D temporal convolutions is beneficial, but the design space is only lightly explored in the main paper. The method inserts 1D residual blocks "after each 2D spatial RB and Transformer block" in **Figure 2(a)**, yet there is no main-paper study of placement sensitivity, number of temporal blocks, or whether all insertion sites are needed. Since the core message is that lightweight temporal modeling is enough, a more careful breakdown of where that temporal modeling matters would substantially strengthen the claim.

8. Some experimental choices raise fairness and interpretation questions. The method is initialized from AdcSR pretrained by compressing PiSA-SR, as stated in **Section 4.1**, then distilled from DOVE. That means the student benefits from a fairly rich initialization history, not just from the proposed training scheme. It is not obvious from the main paper how much of the final performance comes from the proposed dual-head distillation versus inheriting a strong compressed image-SR prior. A stronger control would compare against a student trained from the same backbone without that specific AdcSR initialization, or with a simpler video adaptation baseline.

## Questions
1. Please clarify the exact generator adversarial objective corresponding to **Equations (2) and (3)**. Since each discriminator has two heads, does the student optimize against both heads separately, and if so with what weights? Writing the explicit formula would remove a core ambiguity.

2. For **Equation (4)** and the discriminator training description on **Page 6**, are the pixel-domain and feature-domain discriminator losses optimized independently with separate sample sets, or is \(\mathcal{S}\) just shorthand reused for both domains? The current notation suggests a single mixed-space set, which cannot literally be the implementation.

3. Can the authors provide more direct evidence that the dual heads are learning different functions, rather than simply acting as a larger discriminator? Even a simple analysis of head outputs on shuffled videos, repeated-image pseudo-videos, and real videos would increase confidence in the "disentangling" claim.

4. How sensitive is the result to the choice of head channel split, beyond the appendix setting? The appendix suggests \(75\%/25\%\) detail/consistency works best, which is interesting, but it also suggests the design is somewhat tuned. A short discussion of robustness would help.

5. How much does the AdcSR initialization contribute? A control experiment with the same 2D+1D student trained from a less specialized initialization, or from the pruned SD2.1 backbone directly, would help isolate the gain from the proposed compression-and-distillation method.

6. Since **Table 1** shows the student often wins temporal consistency but not always perceptual or fidelity metrics against DOVE and some baselines, can the authors sharpen the main claim to emphasize efficiency-quality trade-off rather than suggesting broad parity? That would make the contribution read as more precise and more credible.

7. A brief failure-case analysis in the main paper would be valuable. Under what motions or degradations does AdcVSR visibly lag behind DOVE?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard considerations for generative video restoration. The paper does not raise immediate ethics issues that require special review based on the information provided.

## Soundness Rating
3: good. The method is technically plausible and supported by substantial experiments, but the loss formulation and some central claims, especially around disentanglement, need clearer specification and stronger validation.

## Presentation Rating
3: good. The paper is generally clear and well organized, with useful figures and tables, though the mathematical notation around the discriminator and adversarial objectives is less precise than it should be.

## Contribution Rating
3: good. This is a useful and practically relevant contribution on efficient Real-VSR, though the conceptual advance over prior ADC-style compression feels more moderate than the paper's framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem, presents a solid efficiency-quality trade-off, and backs its claims with broad experiments and informative ablations. My hesitation comes from the somewhat incremental novelty relative to prior ADC, the underspecified adversarial objective in the equations, and the fact that the key "disentangling" claim is more implied by outcomes than directly demonstrated.

## Reviewer Confidence
4: confident. I am familiar with diffusion-based restoration, video super-resolution, and adversarial distillation, and I checked the main technical details carefully, though some implementation specifics remain ambiguous because of the paper's notation.