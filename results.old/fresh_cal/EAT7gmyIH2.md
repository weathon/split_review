## Summary

This paper proposes DAME (Distillation Approach for Model-agnostic Explainability), a post-hoc explainability method that replaces the linear local approximator used by methods like LIME with a pair of learned neural networks: a mask generator G and a mildly non-linear student network R. The core idea—separating mask generation from local approximation and using a non-linear student to better capture black-box behavior locally—is well-motivated and conceptually clean. The paper evaluates DAME on image classification (Pascal VOC, ImageNet) and audio tasks (ESC-10, COVID-19 cough diagnosis), comparing against LIME, RISE, GradCAM, and others.

## Strengths

- **Statistically significant human preference for DAME (Section 5.1.1, Figure 4a):** In a subjective evaluation with 35 human subjects rating explanations on a 1–10 scale, DAME achieved the highest average MOS. A pairwise t-test between DAME and RISE yields p ≪ 0.05. This direct human judgment provides strong evidence that DAME's explanations are perceived as more useful, and it is a genuinely rigorous piece of evaluation that goes beyond automated metrics.

- **Counterfactual fidelity evaluation shows DAME identifies more salient regions (Section 5.1.2, Figure 4b):** The paper includes a feature-removal-based faithfulness test: masking regions identified as salient by each XAI method and measuring the drop in target-class probability. DAME produces the largest drop among the compared methods (LIME, RISE, DAME). This evaluation directly tests faithfulness to the black box rather than alignment with human annotation, and is methodologically cleaner than the IoU metric.

- **Novel and well-motivated architecture design:** The separation of the explainability task into two learnable components—a mask generator for identifying salient features and a student network for local approximation—is a genuine departure from LIME's linear approximation and RISE's random-masking approach. Operating directly on the input image space (rather than on binary segment masks) is a principled design choice that enables finer-grained explanations.

## Weaknesses

### Fatal
None. The core approach is viable and the subjective evaluation provides credible evidence. The weaknesses below are significant but addressable.

### Major

1. **No ablation studies isolate the paper's central claim.** The paper's core thesis is that a *mildly non-linear* student outperforms a linear approximator. Yet no experiment varies the student's non-linearity, replaces it with a linear model (which would directly test the claim), removes the mask generator, or ablates the distillation loss. Without this, improvements cannot be attributed to the non-linear student specifically — they could come from the learnable mask generator, the joint training procedure, the L1 penalty, or better hyperparameter tuning. This is the single most significant gap in the empirical evaluation.

2. **The primary quantitative metric (IoU with human segmentation masks) conflates faithfulness with human alignment.** The paper uses Intersection-over-Union between binarized saliency maps and human-annotated object segmentation masks as its main quantitative metric (Table 1). This assumes a faithful explanation must match object boundaries, but classifiers frequently rely on background cues, textures, or partial object features that differ from human segmentation. The paper compounds this by evaluating only on correctly classified high-confidence samples, which may be precisely those where the black box aligns with human perception. The IoU results therefore partially measure alignment with human annotation rather than faithfulness to the black box's decision process. The counterfactual evaluation (Figure 4b) is a better proxy but is run on only 3 methods.

### Minor

3. **The synthetic experiment motivating the core claim (Section 3) provides no results.** Section 3 describes an experiment on a synthetic dataset intended to show that "explanation error increases drastically" with black-box non-linearity for linear approximators. This is a critical piece of motivation, but the section contains no quantitative results, figures, or tables — only a verbal description of the experimental design. The reader is asked to accept the claim on faith.

4. **Counterfactual evaluation compares only 3 methods (DAME, LIME, RISE).** The fidelity-based evaluation in Figure 4b is the paper's strongest faithfulness test, but it excludes gradient-based methods (GradCAM, GradCAM++, Integrated Gradients) that are already compared in the IoU tables and that sometimes outperform DAME on certain metrics. Including them would strengthen the comparison.

5. **Inconsistent performance across architectures is not analyzed.** On ResNet-101, gradient-based methods (GradCAM, GradCAM++) achieve higher IoU than DAME; DAME leads only on ViT. The paper acknowledges this (line 185: "For the Resnet-101 model, the gradient CAM based approaches give the best IoU values") but offers no discussion of *why* DAME's relative performance varies with the black-box architecture. This limits the reader's understanding of when the method is and is not advantageous.

6. **Computational cost is under-documented and the stated figure appears questionable.** The paper states "25% more computational time per sample over the prior work of RISE" (line 240). DAME trains two small neural networks per input sample (requiring backpropagation over multiple epochs), while RISE only performs forward passes. No wall-clock time, number of training epochs, number of gradient updates, or batch size is reported. Without these details, the 25% figure cannot be assessed, and the practical feasibility of per-sample training for large-scale deployment remains unclear.

7. **Missing reproducibility details.** The following are not specified: learning rate, optimizer, number of training epochs (only variable `n_e` is mentioned without a value), kernel sizes and number of filters in G and R, L1 penalty weight, threshold for binarizing saliency maps, and the number of perturbations *p*. The paper states hyperparameters were "frozen after tuning on a held-out set" but gives no values. This makes reproduction and fair comparison difficult.

### Trivial
- Fine-tuning details for the black-box classifiers (learning rate, epochs, data splits) for the Pascal-VOC adaptation of ResNet-101 and ViT are not provided.

## Nice-to-Haves
- Including error bars or confidence intervals for the counterfactual evaluation plot (Figure 4b) would help assess significance.
- A failure analysis explaining why DAME misses parts of objects in certain cases (e.g., Indian-elephant, cock in Figure 3) would be useful for understanding the method's limitations.
- The L1 penalty mentioned in the text is not explicitly written in any equation in the main paper — adding it explicitly rather than relying on a reference would improve clarity.

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Missing loss function (eq. 8):** The critic noted that Algorithm 1 references "eqn. 8" which is not shown. This content was likely in the appendix stripped by the parser; per policy, weaknesses about missing appendix content are removed.
- **"Distillation" used loosely:** The critic notes that "distillation" typically refers to matching across the full data distribution. The paper uses it for per-sample local fitting — this is a minor semantic issue that does not affect the paper's technical contribution.
- **Generic "reproducibility" framing:** The critic frames missing hyperparameters as a "structural" reproducibility issue. While missing details are a real concern (captured above as Minor #7), the framing as a fatal structural flaw is overstated given that the core method is described.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective or synthesis that the paper itself does not already contain.

## Suggestions

1. **Add ablation studies that directly test the core claim:** (a) Replace the non-linear student R with a linear model while keeping G and the loss identical; (b) ablate the mask generator G by learning the saliency map directly without separation; (c) vary the degree of non-linearity in R to show a monotonic improvement. This is the single most impactful addition.

2. **Complete the synthetic experiment (Section 3) with actual results:** Provide a plot of explanation error (XE) vs. black-box non-linearity for both LIME and a non-linear student to directly validate the motivating premise.

3. **Expand the counterfactual evaluation** to include gradient-based methods (GradCAM, GradCAM++) and report results with confidence intervals or error bars. Run on a larger sample set (e.g., 500+ images).

4. **Report computational cost transparently:** State number of training epochs, gradient updates per sample, and wall-clock time for DAME vs. LIME vs. RISE on comparable hardware.

5. **Publish all hyperparameters** in a table: learning rate, optimizer, number of epochs *n_e*, number of perturbations *p*, L1 weight, CNN architecture details (kernel sizes, filters, strides), and the saliency binarization threshold.

## Score and Decision

**Originality:** Good. The separation of mask generation and local approximation with a non-linear student is a novel contribution to model-agnostic explainability.

**Importance of research question:** High. Improving post-hoc explainability for black-box models is an active and important area.

**Claims well supported:** Moderately. The subjective evaluation is strong, but the core methodological claim (non-linear student outperforms linear) lacks direct ablation evidence, and the main quantitative metric (IoU) has known limitations.

**Soundness of experiments:** Moderate. The subjective and counterfactual evaluations are well-designed; the IoU experiments are standard but flawed; the missing Section 3 results and absent ablation studies weaken the empirical foundation.

**Clarity of writing:** Adequate but could be improved. The architecture is described, but key details (loss function, hyperparameters) are missing or referenced to stripped sections.

**Value to the research community:** Moderate. If validated with proper ablations, DAME would be a useful addition to the model-agnostic explainability toolkit. In its current form, the evidence is promising but incomplete.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>