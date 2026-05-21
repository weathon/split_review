---
job_id: 061f3f24-df4a-43d5-b7ec-de597b2db978
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cSpjHOf04S.pdf
paper: Gen2Seg: Generative Models Enable Generalizable Instance Segmentation
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on generative models, representation learning, transfer/generalization, and vision.

## Minimum Quality
Pass ✅. The submission contains all core components expected of a research paper, including abstract, introduction, related work, method, experiments, quantitative and qualitative results, and conclusion; the empirical study is substantial enough to clear the bar for full review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-directed text, or other apparent attempts to manipulate automated reviewing in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes **gen2seg**, a simple way to repurpose pretrained generative models, specifically Stable Diffusion and MAE with decoder, for category-agnostic instance segmentation. The key idea is to cast instance segmentation as image-to-image translation into a color-coded instance map and train with an instance-coloring loss that encourages low intra-instance variance and separation between instances, using supervision from a narrow synthetic training set consisting mainly of indoor furnishings and cars.

The paper evaluates zero-shot generalization to unseen object categories and styles across several datasets, and reports that finetuned generative models transfer much better than discriminative baselines trained on the same limited data, in some settings approaching or even surpassing SAM, especially on fine structures and ambiguous boundaries.

## Strengths
1. **The paper asks a meaningful and fairly sharp question.**  
   The central question is not just whether diffusion or MAE features can be used for segmentation, but whether generative pretraining induces grouping priors that transfer to *unseen object types and styles* even when finetuning supervision is deliberately narrow. That framing is interesting, and it is more scientifically focused than a generic “we improve benchmark X” paper.

2. **The method is conceptually simple and easy to understand.**  
   Casting instance segmentation as prediction of an RGB instance-color image, then training with the three-part instance coloring loss in **Equations (3) to (6)**, is a neat formulation. In particular, the objective avoids committing to a fixed color assignment while still encouraging within-instance consistency and between-instance separation. This is a clever way to exploit image-generative decoders without adding a task-specific mask head.

3. **The paper provides a fairly broad empirical study across models, domains, and training regimes.**  
   The experiments span Stable Diffusion, MAE-B, MAE-H, DINO-B, SimpleClick, and SAM, and test on COCO variants, DRAM, EgoHOS, iShape, PIDRay, and BSDS500. This breadth matters because the paper’s claims are about transfer and generalization, not just in-domain segmentation quality.

4. **The comparative evidence against non-generative baselines is compelling in the main story.**  
   **Table 1 (Page 7)** is one of the stronger pieces of evidence in the paper. The gap between generative backbones and the two finetuned alternatives on the same limited training data is large, especially versus SimpleClick and DINO-B. For example, on iShape, gen2seg (SD) reaches 51.4 mIoU versus 16.8 for SAM and 27.4 for DINO-B, which is exactly the kind of result that supports the paper’s claim that generative pretraining helps with detailed grouping rather than merely objectness activation.

5. **The training-data ablations are valuable and directly tied to the paper’s thesis.**  
   **Table 2 (Page 8)** is important because it probes whether the reported generalization is just an artifact of the chosen synthetic data. The fact that performance remains nontrivial even with only 10 or 5 classes, or with ClevrTex, strengthens the argument that the effect is not purely due to semantic coverage in the finetuning set.

6. **The qualitative evidence is informative rather than decorative.**  
   **Figure 2 (Page 3)** is effective because it shows specific failure modes of the baselines, such as missed thin structures and ambiguous boundaries, that align with the paper’s quantitative claims. Likewise, **Figure 6 (Page 9)** supports the edge-quality argument by showing that even when trained on polygonal COCO masks, the SD model can output smoother and perceptually cleaner boundaries than the annotations themselves. This figure is especially relevant because it strengthens the paper’s claim that the behavior comes from the pretrained generative prior, not merely from fitting clean synthetic masks.

7. **The paper includes useful ablations instead of only headline results.**  
   The loss ablation in **Table 3 (Page 18)** is helpful. It shows that $\mathcal{L}_{\mathrm{var}}$ is essential, while $\mathcal{L}_{\mathrm{sep}}$, $\mathcal{L}_{\mathrm{mean}}$, smooth $\ell_1$, and normalization each contribute to the final result. This improves confidence that the proposed objective is not an arbitrary pile of terms.

8. **The paper surfaces an intriguing emergent-compositionality angle.**  
   The examples in **Figure 3 (Page 4)** and the Pascal-Part analysis in **Table 7 (Page 20)** suggest that the learned color space may encode more than just whole-object grouping. I would not overclaim this, but it is a genuinely interesting observation that makes the work more than a straightforward transfer paper.

## Weaknesses
1. **The strongest claim, that generative pretraining yields an “inherent grouping mechanism,” is still somewhat stronger than what the evidence strictly establishes.**  
   The experiments clearly show that the proposed recipe works better than the chosen baselines under narrow supervision. However, the causal interpretation is less pinned down than the writing suggests. For example, several factors are entangled: decoder-based dense generation, preservation of spatial detail, architecture differences, pretraining objective, training resolution, and the specific prompting/readout procedure. The paper often attributes the gains directly to “generative priors,” but the presented evidence does not fully isolate pretraining objective from these other factors. This matters because the main scientific contribution is an explanatory claim, not just a performance report.

2. **The baseline design is not always as strong or as controlled as it should be for such a bold conclusion.**  
   The DINO comparison in Section 4.2 is especially vulnerable here. The paper defines **DINO-B** as DINO features attached to a frozen Stable Diffusion VAE decoder through “a simple up-conv” and then finetuned end-to-end. That is a fairly specific and somewhat homemade baseline, and it is not obvious that poor performance should be interpreted as evidence against discriminative pretraining in general. Similarly, SimpleClick is a promptable interactive segmenter with a learned decoder and training recipe designed for a different operating point, so using its failure on this narrow-data setting as evidence that “existing segmentation architectures cannot generalize” is too sweeping. A more controlled comparison would keep the output parameterization and decoder as matched as possible across generative and non-generative pretraining.

3. **Some aspects of the mathematical formulation are under-justified, even if the method works empirically.**  
   The losses in **Equations (3) to (6)** are understandable, but several design choices feel heuristic and are not analyzed enough:
   - In **Equation (4)**, the factor $\frac{1}{\sqrt{|S_i|}|T_i|}$ is said to “emphasize smaller objects,” but the exact normalization effect is not explained. Since the inner term already averages over $T_i$, the dependence on $|S_i|$ deserves more justification.
   - In **Equation (5)**, the mean-level separation averages pairwise penalties over all instance pairs, but the paper does not discuss what happens when many instances are present, or whether this term becomes dominated by numerous easy pairs.
   - The paper states in **Appendix C** that it “compute[s] all losses in the range of $[0,255]$ to weight all terms equally” and sets $\lambda_{\text{sep}}=\lambda_{\text{mean}}=300$, but the main paper never explains the scaling logic. Since the loss geometry depends strongly on these magnitudes, the main text should clarify this rather than leaving it implicit.

4. **The promptable segmentation readout in Section 3.2 is not fully specified or well motivated mathematically.**  
   In **Equation (7)**, similarity is defined as
   $$
   S_p(x,y)=\min\left(1,\frac{1}{\|F(x,y)-q_p\|_2}\right),
   $$
   followed by normalization, bilateral filtering, max-merging across prompts, and thresholding. This pipeline has several arbitrary choices: the Gaussian width, the clipping at 1, the bilateral filtering window, and especially the fixed threshold of $\frac{3}{255}$ later stated in **Appendix C**. The paper positions this as a simple probe of whether the features carry object shape, which is fair, but because all headline promptable segmentation numbers depend on this conversion, the lack of threshold sensitivity analysis in the main paper weakens the evaluation. In practical terms, one wants to know whether the method is robust or whether these mIoU values are fragile to post-processing.

5. **The evaluation setup leaves some ambiguity about fairness of comparison to SAM.**  
   SAM is used off-the-shelf, which is reasonable as a reference point, but the comparison is a little asymmetrical. The proposed method is trained specifically for the object-grouping task and evaluated with access to a custom prompt-processing pipeline designed around its learned color space, while SAM is evaluated using its default interface. This does not invalidate the result, but some claims in the introduction and experiments read as if the comparison were apples-to-apples. It would help to separate “approaches SAM under this evaluation protocol” from stronger claims that it is generally comparable as a promptable segmentation system.

6. **The paper repeatedly interprets qualitative observations as evidence for deeper structural properties without enough restraint.**  
   For example, **Figure 3** is visually interesting, but the interpretation that the model learned “hierarchical scene representations” is a stretch based on the presented evidence. Likewise, the discussion around Table 7 suggests emergent compositionality, but the quantitative evidence is mixed. On several classes the gains over the “No Compositionality” baseline are modest or absent, and SAM remains much stronger overall. This is one of those places where the paper is at its most exciting, but also a bit too eager.

7. **The small-object limitation is significant, and the main result tables show it clearly.**  
   The paper acknowledges this on **Page 10**, but it is not a minor caveat. In **Table 1**, the method performs very poorly on $\mathrm{COCO}^{M/S}_{\mathrm{exc}}$, especially relative to SAM. If the overarching claim is broad category-agnostic segmentation from narrow supervision, the inability to recover medium and small objects is a serious boundary on applicability. This should be emphasized more plainly in the title-level narrative, because the gains are concentrated on larger objects and fine boundaries, not uniform instance segmentation performance across scales.

8. **Some important implementation decisions are pushed out of the main paper even though they affect the scientific interpretation.**  
   Two examples stand out. First, the authors state in **Appendix C** that when images have many instances they compute the loss on at most 1250 instances, which could materially affect training on crowded scenes. Second, for the 5-class and 10-class settings the loss is disabled inside bounding boxes of disallowed objects, which changes the supervision structure in a nontrivial way. These choices are not necessarily wrong, but they are central enough that the main paper should discuss them more explicitly.

9. **The related-work positioning around prior generative approaches to instance or segmentation-style prediction could be sharper.**  
   The paper cites some diffusion-for-segmentation work, but the related-work discussion is still a bit selective given the breadth of claims. In particular, because the paper’s contribution is as much about *repurposing generative backbones for segmentation* as about the specific loss, a more thorough distinction from prior diffusion-based segmentation formulations would make the novelty claim cleaner. Right now the reader has to infer that the key novelty is the narrow-supervision generalization framing plus the color-image decoding recipe.

10. **Presentation is generally good, but there are several places where the writing overstates what has been demonstrated.**  
   The tone is engaging, but phrases like “inherent grouping mechanism” and “human-like perception” overshoot the empirical support. The paper would be stronger if it were slightly less promotional and more precise about what is shown: strong transfer from generative pretraining under a narrow supervision regime, with notable advantages on boundaries and fine structures.

## Questions
1. **Can the authors better isolate the source of the gains?**  
   The rebuttal would be much stronger if you could disentangle at least some of: generative pretraining objective, decoder architecture, dense image reconstruction pathway, and the specific color-space readout. For example, can you provide a more tightly matched discriminative baseline using the same decoder and output parameterization, or argue more carefully why the current baselines are sufficient?

2. **How sensitive are the promptable segmentation numbers to the post-processing hyperparameters in Section 3.2?**  
   In particular, how sensitive are results to the threshold, Gaussian bandwidth, and bilateral filter window? A compact sensitivity table on one or two datasets would increase confidence that Table 1 is not heavily tuned to a fixed operating point.

3. **Can you clarify the scaling and optimization behavior of the loss terms in Equations (3) to (6)?**  
   I would like to understand why $\lambda_{\text{sep}}=\lambda_{\text{mean}}=300$ is appropriate, why the losses are computed in $[0,255]$ space, and whether alternative normalizations materially change the outcome. Even a short explanation of relative term magnitudes during training would help.

4. **For Equation (4), can you give a more principled justification for the $\frac{1}{\sqrt{|S_i|}|T_i|}$ weighting?**  
   If the intention is to emphasize smaller objects, why this exact dependence rather than, say, $\frac{1}{|S_i||T_i|}$ or class-balanced sampling? A short derivation or empirical comparison would strengthen the method section.

5. **How should readers interpret the comparison to SAM?**  
   Are you claiming parity as a general promptable segmentation system, or parity only under this center-point-based evaluation on selected datasets? Tightening this framing would avoid overinterpretation.

6. **Can you clarify whether the threshold and other prompting hyperparameters were selected on a validation set, and if so which one?**  
   This matters for assessing possible evaluation bias. If they were fixed once and reused everywhere, say that explicitly in the main paper.

7. **Can you provide more evidence for the compositionality claim, or soften it?**  
   Figure 3 and Table 7 are intriguing, but at present they read more like preliminary evidence than a firm result. Either a stronger controlled evaluation or more cautious wording would improve the paper.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work uses existing datasets and focuses on category-agnostic segmentation. The paper does mention potential applications in robotics, medical imaging, and autonomous systems, but these are aspirational rather than deployment claims.

## Soundness Rating
3: good. The empirical study is substantial and the main claims are mostly supported, though several conclusions are phrased more strongly than the evidence strictly warrants, and some methodological choices in the objective and prompting pipeline need better justification.

## Presentation Rating
3: good. The paper is readable, well organized, and helped by effective figures and tables, but parts of the writing are overly assertive, and some important implementation and mathematical details should be surfaced more clearly in the main text.

## Contribution Rating
4: excellent. The contribution is meaningful for the ICLR community because it reframes instance segmentation as a test of transferable generative representations, introduces a simple and effective adaptation recipe, and presents surprisingly strong cross-category generalization under narrow supervision.

## Overall Rating
8: Accept, good paper (poster). The paper is not airtight in its causal interpretation, and a few comparisons and mathematical choices need more care, but the core empirical finding is strong, interesting, and likely to stimulate useful follow-up work on generative representations for perceptual grouping.

## Reviewer Confidence
4: confident. I am familiar with the relevant literature on representation learning, generative models, and segmentation, and I checked the main method and experimental claims carefully, though I did not independently verify implementation details beyond what is in the paper.