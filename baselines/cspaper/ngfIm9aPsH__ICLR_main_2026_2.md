---
job_id: 026fd410-9f02-41b5-903b-0b3fd29c5bb7
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ngfIm9aPsH.pdf
paper: Object Fidelity Diffusion for Remote Sensing Image Generation
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies controllable diffusion models, conditional generation, and downstream learning utility for object detection, all of which are standard ML and generative modeling topics.

## Minimum Quality
Pass ✅. The paper includes the expected scientific components, namely abstract, introduction, related work, method, experiments, quantitative and qualitative results, discussion, and conclusion; despite several technical and presentation issues, it clears the bar for non-desk-reject review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence of hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes OF-Diff, a remote sensing layout-to-image diffusion framework that aims to improve object shape fidelity and controllability without requiring real-image references at inference time. The method combines an Enhanced Shape Generation Module (ESGM) for extracting or sampling object masks, a dual-branch diffusion architecture with online distillation between a mix-feature teacher branch and a shape-feature student branch, and a DDPO fine-tuning stage for improving diversity and downstream detection utility. Experiments on DIOR and DOTA, with additional results on HRSC2016 in the appendix, evaluate generation fidelity, layout consistency, shape fidelity, and downstream object detection performance.

## Strengths
1. The paper addresses a meaningful problem. For remote sensing generation used for data augmentation, bounding-box-level controllability and shape fidelity matter more than generic photorealism, and the paper is well motivated in arguing that coarse text or semantic guidance is often insufficient for instance-level control.

2. The central design is reasonably intuitive and practically motivated. The decomposition in **Figure 3** is helpful here: the distinction between the shape-conditioned branch, the mix-feature branch, and the online-distillation consistency path makes the training/inference asymmetry easy to understand. In particular, the paper clearly communicates the intended benefit that stronger image-conditioned supervision is used only during training, while sampling requires only labels and shape priors.

3. The qualitative comparisons are fairly compelling. **Figure 4** shows several cases where OF-Diff seems to preserve object count, placement, and morphology better than the compared methods, especially for small vehicles, ships, and airplanes. The failure modes highlighted earlier in **Figure 1** also give a concrete visual framing of what the method is trying to fix, namely leakage outside the layout, deformed objects, and collapse in dense scenes.

4. The empirical evaluation is broader than many application papers in this space. The authors do not rely only on FID-like scores; they also report layout consistency, edge-based shape metrics, and downstream detection. This is a good choice because a pure image-generation evaluation would miss whether the generated data is actually useful for object detection.

5. **Table 1** is a real strength of the paper. OF-Diff is not just better on one cherry-picked metric; it is competitive or best across most reported metrics on both DIOR and DOTA. The gains over AeroGen and CC-Diff are especially meaningful on YOLOScore and FID/CMMD, which supports the claim that the method improves both fidelity and controllability rather than trading one entirely for the other.

6. **Table 2** strengthens the main claim beyond standard generative metrics. Since the paper’s stated contribution is object fidelity, it is appropriate to measure shape similarity explicitly, and OF-Diff improves IoU/Dice/SSIM while reducing CD/HD on both datasets. That is a better match to the paper’s thesis than relying only on FID.

7. The ablation in **Table 4** is useful and largely aligned with the method components. ESGM seems to provide the biggest jump in fidelity and YOLOScore, while \(L_c\) and DDPO provide incremental gains. This gives at least some evidence that the paper is not just a bag of tricks with no attribution.

## Weaknesses
1. The methodological novelty is somewhat narrower than the framing suggests. The paper combines several known ingredients, ControlNet-style conditioning, a teacher-student or self-/online-distillation flavor, shape-mask guidance, and DDPO fine-tuning, into a remote-sensing pipeline. That combination may still be useful, but the paper often writes as if the contribution is conceptually broader than what is actually demonstrated. For example, on **Page 2**, the contrast to prior methods is framed very strongly, yet the method still depends on real images during training for ESGM mask extraction, ControlNet features, and teacher supervision. So the practical claim is really “no real-image reference at inference”, not “reduced reliance on real images” in any broader sense. That distinction matters because the paper repeatedly sells reduced dependence on real data as a central benefit.

2. The mathematical specification of the core online-distillation mechanism is underspecified and partly inconsistent. In **Equation (3)** on **Page 4**, the mix feature is defined as
\[
c_m = \frac{n}{N} c_i + \operatorname{sg}[c_s].
\]
This raises several questions that are not answered in the main paper. Are \(c_i\) and \(c_s\) normalized to compatible scales before addition? If not, the relative contribution of image and shape features depends not only on \(n/N\) but also on arbitrary feature magnitudes. Also, using \(\operatorname{sg}[c_s]\) while leaving \(c_i\) trainable means the teacher input distribution changes over training; the text calls this a “stable anchor point,” but that is not obviously true. A more careful justification or normalization scheme is needed because this equation is central to the method. As written, it looks like a heuristic schedule rather than a principled objective.

3. The notation and parameterization around the dual-decoder architecture are confusing enough to affect technical clarity. In **Equations (4)-(6)**, the paper introduces \(\epsilon_\theta^s\), \(\epsilon_\theta^m\), and then a teacher term \(\epsilon_{\theta'}^{m}\) in **Equation (6)**, but it is not clear whether \(\theta\) and \(\theta'\) are shared, partially shared, EMA-related, or simply notational placeholders for different branches. The text later mentions “parameter sharing” in the conclusion, but the actual scope of sharing is not explicitly defined in the method section. Since the paper’s main idea is an online-distillation framework, ambiguity about which parameters are optimized and which are frozen is not a cosmetic issue; it directly affects reproducibility and interpretation of the claimed teacher-student mechanism.

4. The DDPO section is the weakest technical part of the paper. On **Page 5**, **Equation (8)** presents a gradient estimator,
\[
\hat{g}=\mathbb{E}\left[\sum_{t=0}^{T}\frac{p_{\theta}(\mathbf{x}_{t-1}\mid c,t,\mathbf{x}_{t})}{p_{\theta^{\prime}}(\mathbf{x}_{t-1}\mid c,t,\mathbf{x}_{t})}\cdot r(\mathbf{x}_{0},c)\cdot\nabla_{\theta}\log p_{\theta}(\mathbf{x}_{t-1}\mid c,t,\mathbf{x}_{t})\right],
\]
but the derivation is deferred out of the main paper, and the formulation of the reward in **Equation (9)** is particularly problematic:
\[
r(\mathbf{x}_{0},c)=\left(KNN(\mathbf{x}_{0},\mathbf{x}_{0})-\omega KL(\mathbf{x}_{0},\mathbf{x}_{0}^{\prime})\right).
\]
This is too vague to be scientifically satisfying in the main paper. \(KNN(\mathbf{x}_0,\mathbf{x}_0)\) is not a meaningful definition unless one specifies the feature space, batch/reference set, and exact aggregation; similarly, \(KL(\mathbf{x}_0,\mathbf{x}_0')\) between images is not well defined unless one specifies a probabilistic representation. The appendix partially clarifies that features come from a pretrained encoder, but the main paper’s formula is still misleading as written. Since DDPO is one of the claimed contributions, the reward should be defined precisely in the main text, for example as \(KNN(f(x_0), \{f(x_j)\}_{j\neq 0})\) in feature space, with a clearly specified empirical distribution used for KL.

5. There is a mismatch between the method description and implementation details around feature extraction models. On **Page 5**, the main paper says “Following standard practice, we compute the KNN in the low-dimensional embedding space of CLIP’s image encoder.” However, in the appendix (**Page 14**), the DDPO feature extractor is described as “a ResNet101 pre-trained on ImageNet-1K.” These are not interchangeable details. This inconsistency matters because the reward function used for RL fine-tuning can strongly affect results; if the authors use CLIP in the main text and ResNet101 in the appendix, it becomes unclear what was actually used in experiments.

6. The experimental evidence is good but still incomplete relative to the paper’s claims about practicality and superiority. The main comparisons are only on DIOR and DOTA in the main paper, with HRSC2016 moved to the appendix. That is a bit thin for broad claims about remote sensing generation, especially because the task is specialized and the paper emphasizes general applicability to dense scenes, small objects, and polymorphic objects. A stronger main-paper case would include either more datasets or more stress tests varying density, scale, and layout shift systematically.

7. The unknown-layout experiment in **Table 3** is useful, but it is not convincing enough to support robust generalization claims. The table uses DIOR validation layouts unseen during training, but this is still within the same dataset distribution and object vocabulary. That is a much weaker test than cross-dataset or cross-region generalization. The gains are also somewhat mixed; for example, OF-Diff is best on most metrics, but **CC-Diff is actually higher on YOLOScore** (51.74 vs 49.59), which complicates the narrative that OF-Diff dominates under layout shift. The paper should discuss this explicitly rather than summarizing the result as simply “performs well.”

8. The evaluation protocol for shape fidelity is not fully convincing. On **Page 8**, the method crops each instance using a horizontal box converted from the rotated box, pads by 20%, resizes to \(64\times64\), extracts Canny edges, and computes IoU/Dice/CD/HD/SSIM. This pipeline introduces several arbitrary choices, namely H-box conversion, padding ratio, resize resolution, and edge threshold behavior. Those choices can materially change scores, especially for very small or elongated objects. Since **Table 2** is a central result supporting the “object fidelity” claim, it would be important to either report sensitivity to these preprocessing choices or use a more direct mask/contour-based metric when possible.

9. Some of the claimed practical advantage is undercut by the actual system complexity. **Figure 3** makes clear that the training pipeline includes ESGM with RemoteCLIP and RemoteSAM, ControlNet conditioning, a dual-decoder diffusion setup, online distillation, and optional DDPO post-training. That is a fairly heavy stack. The paper argues that it improves applicability by avoiding image references at inference, which is fair, but the broader messaging about practicality is too rosy. **Table 7** in the appendix also shows OF-Diff is not especially lightweight in memory or inference time. This is not a fatal flaw, but the paper should be more honest that it trades simpler inference for a more complicated training pipeline.

10. The presentation has several rough edges that weaken confidence in the details. There are multiple awkward or incorrect phrases, inconsistent notation, and reference formatting issues. A few examples: the paper refers to Stable Diffusion using a “pre-trained VQ-VAE” on **Page 3**, which is not the standard wording for SD 1.5; the references section contains visible formatting errors and malformed entries; and some claims in the main text point to appendix figures/tables in a way that suggests the core story is partly outsourced there. None of this invalidates the empirical findings, but it does make the paper feel less polished than it should be for a method-heavy submission.

11. The discussion of captions and aesthetics is interesting, but it is awkwardly integrated into the main narrative. On **Pages 8-9**, the paper states that captions improve aesthetics but hurt fidelity to the real data distribution and downstream performance. This is plausible, and **Figure 9** in the appendix supports it qualitatively via t-SNE. However, the caption-conditioned setting is not part of the method as presented in the main contribution, and this discussion ends up taking space that could have been used to clarify the core algorithm or evaluation. It feels like an auxiliary side story rather than a tightly connected part of the paper.

12. The baseline set is good but not obviously exhaustive for the specific claimed angle of shape/edge-guided layout generation. The paper compares against AeroGen, CC-Diff, LayoutDiffusion, and GLIGEN, which are reasonable, but the positioning against other recent region- or edge-guided diffusion/data augmentation methods is limited. This matters because the claimed differentiator of OF-Diff is precisely stronger structural guidance for object fidelity. The paper would benefit from a clearer argument for why the chosen baselines are the most relevant ones for that claim.

## Questions
1. Please clarify the exact parameter-sharing scheme in the dual-decoder/online-distillation setup. In **Equations (4)-(6)**, what parameters are shared between the shape branch and mix branch, and what does \(\theta'\) denote in **Equation (6)**? Is the teacher branch an EMA copy, a separately optimized branch, or simply the same branch with stop-gradient applied to its output?

2. For **Equation (3)**, are \(c_i\) and \(c_s\) normalized before addition? If not, how do you prevent the feature with larger norm from dominating the mixed condition? A rebuttal with exact implementation details here would substantially improve my confidence in the method.

3. Please define the DDPO reward in mathematically correct form in the main paper. What is the exact feature extractor actually used in experiments, CLIP as stated on **Page 5**, or ResNet101 as stated in Appendix A.2 on **Page 14**? Also, how is KL divergence computed from deterministic image features?

4. For the shape-fidelity metrics in **Table 2**, how sensitive are the results to the preprocessing pipeline, especially the 20% padding, the \(64\times64\) resize, and the specific Canny settings? Even a small sensitivity analysis would help establish that the gains are not an artifact of the evaluation recipe.

5. The unknown-layout result in **Table 3** is encouraging, but still in-distribution. Do you have evidence, preferably quantitative, on cross-dataset transfer, for example train on one dataset and evaluate generation utility or consistency on another? If not, I would encourage the authors to soften the generalization claims.

6. Since **Figure 3** reveals a fairly complex training stack, it would be useful to know what the minimum effective variant is. For example, can the authors comment on whether ESGM + \(L_c\) already captures most of the gains, and whether DDPO is worth the additional complexity given the rather small improvements in **Table 4**?

7. In **Table 1**, OF-Diff slightly trails CC-Diff on DIOR CAS (82.55 vs 82.61), and in **Table 3**, CC-Diff exceeds OF-Diff on YOLOScore under unknown layouts. Can the authors explain these failure cases or metric trade-offs more directly, rather than mostly emphasizing aggregate wins?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper concerns generation of realistic remote sensing imagery for downstream object detection. Even if the datasets are public and there are no human subjects, this line of work has plausible dual-use implications, including surveillance, military reconnaissance support, spoofing of geospatial data pipelines, or generation of deceptive imagery for benchmarking and system manipulation. The ethics statement on **Page 10** acknowledges possible misuse, but the discussion remains brief and generic. I do not see an ethics violation in the conduct of the research itself, but I do think the application space warrants ethics flagging due to possible safety and security misuse.

## Soundness Rating
3: good. The paper has a sensible method and solid empirical evidence, but the technical exposition around the online-distillation and DDPO objectives is not precise enough for a higher soundness score.

## Presentation Rating
2: fair. The high-level story is understandable and the figures help, especially **Figures 1, 3, and 4**, but several notation issues, mathematical ambiguities, and writing/reference inconsistencies materially hurt clarity.

## Contribution Rating
3: good. The paper makes a useful contribution to controllable remote sensing image generation, especially through its emphasis on object-shape fidelity and downstream detection utility, though the novelty is more in the system combination and empirical execution than in a fundamentally new modeling principle.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper solves a relevant problem and presents consistently strong empirical results, especially in **Tables 1, 2, and 4**, with qualitative evidence in **Figure 4** that aligns with the claims. However, the main-paper technical specification is noticeably sloppier than it should be, especially for the distillation and DDPO parts, and the generalization/practicality claims are somewhat overstated relative to the evidence.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main method, equations, figures, and tables carefully, though a few implementation ambiguities remain unresolved from the paper alone.