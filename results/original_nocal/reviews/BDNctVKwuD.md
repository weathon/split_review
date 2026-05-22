Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper identifies a theoretical limitation of HiResCAM: its explanations are not uniquely determined because adding the same matrix M to all class maps leaves softmax probabilities unchanged. The authors propose ContrastiveCAMs (pairwise differences of HiResCAMs) that are invariant to this shift and provide class-versus-class granularity. Using ContrastiveCAMs to analyze model behavior reveals substantial non-core region contributions. They then introduce Core-Focused Cross-Entropy (CFCE), which penalizes non-core region contributions during training by incorporating the core mask into the loss via ContrastiveCAMs. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show substantial improvements in alignment metrics (IoU, core-region ablation accuracy, RFS) at some cost to clean accuracy, with downstream segmentation benefits.

## Strengths

- **ContrastiveCAMs are a clean, principled extension with proven invariance.** The M-invariance (Theorem 3.5) is straightforward from the definition, but it directly addresses the identified non-uniqueness. The qualitative examples in Figure 2 show that ContrastiveCAMs reveal regions hidden by standard HiResCAMs, demonstrating practical value beyond the theoretical fix.

- **Large quantitative alignment gains on Hard-ImageNet are supported by multiple independent metrics.** Table 2 shows CFCE raises ContrastiveCAM IoU from 30.27% to 89.22% and CFCE+KL to 93.39%. Crucially, these gains are corroborated by independent metrics: accuracy under gray-mask ablation drops from 76.53% (CE) to 41.78% (CFCE), RFS goes from negative (−0.23) to positive (0.224), and GradCAM IoU also improves. The alignment improvement is not merely an artifact of the training loss.

- **Practical applicability with approximate masks.** Table 3 demonstrates competitive IoU using SAM-generated masks (83.95% binary validation IoU) or bounding boxes (79.13%), showing the method does not require pixel-perfect ground truth and has practical deployment potential.

- **Downstream transfer benefits are demonstrated.** The PASCAL VOC segmentation results (bar chart in Section 5.3) show that CFCE+KL pre-trained backbones improve mean IoU across most classes in both fine-tuned and end-to-end settings, suggesting more aligned features transfer to dense prediction tasks.

- **The connection between interpretability and training is a worthwhile direction.** Using post-hoc explanation maps not just for analysis but as a training signal to enforce feature alignment is conceptually novel and opens a productive research avenue.

## Weaknesses

### Fatal
None.

### Major
- **The primary alignment metric (ContrastiveCAM IoU) has partial circularity with the training objective.** The CFCE loss is defined using ContrastiveCAMs and a core mask H, and then ContrastiveCAM IoU is reported as a success metric. A high overlap between ContrastiveCAMs and the mask is partly a direct effect of the loss optimization. This concern is mitigated by other independent metrics in Table 2 (GradCAM IoU, Gray Mask / Gray BBOX / Tile accuracy, RFS) which also improve and are not directly optimized. However, the paper's framing would be stronger with a clearer separation between the metric closest to the training signal and truly independent evaluations.

- **Clean accuracy trade-off is not sufficiently analyzed.** CFCE drops from 94.25% (CE) to 90.53% on Hard-ImageNet and from 94.41% to 92.96% (multiclass) and 90.08% (CFCE+KL) on Oxford Pets. This ∼3–4 point penalty is acknowledged but not discussed in depth. For practitioners considering the method, the circumstances under which this trade-off is acceptable versus problematic need clearer characterization.

### Minor
- **The HiResCAM non-uniqueness motivation is mathematically correct but somewhat overstated.** Theorem 3.2 follows directly from softmax shift-invariance (Proposition 3.1). The paper frames this as HiResCAMs being "arbitrarily corrupted," but for any single trained model the HiResCAM computation is deterministic and well-defined. The non-uniqueness describes the mapping from predictions to explanations, not an instability in the explanation for a fixed model. This does not invalidate the contribution — ContrastiveCAMs remove a genuine redundancy — but the rhetoric inflates the severity of the problem. The paper already softens this slightly with "can, in principle, completely corrupt" (Section 1), but the framing in the abstract and introduction implies a more concrete failure than is demonstrated.

- **No computational cost analysis is provided.** The method requires computing CAM_{(c_t,c)}^{Cntrst} for every pair of classes, which in principle scales with the number of classes. For a linear classifier (the paper's setting), HiResCAMs have a closed form that is efficiently computable with a single matrix multiply, but the paper does not discuss or measure this. The absence of any runtime or gradient computation analysis makes it difficult to assess scalability to datasets with many classes (e.g., full ImageNet with 1000 classes).

- **The absolute value in the CFCE loss (Eq. 15) lacks theoretical justification.** Definition 4.5 introduces |CAM_{(c_t,c)}^{Cntrst}| for the non-core penalty term without explanation of why absolute value is used rather than, e.g., squaring or relu. The gradient of the absolute value is non-smooth at zero, and no analysis of optimization stability is provided. Theorem 4.6 claims consistency with the CCRM objective, but the proof is in the missing appendix (which cannot be verified from the provided text).

- **Method scope is limited to linear classifiers and convolutional architectures.** The paper explicitly assumes h is a single linear layer (Eq. 1), which excludes modern architectures with MLP heads (ConvNeXt, ViT). While this is a stated scope, the paper would benefit from at least a discussion of how the approach might extend to non-linear classifiers (e.g., using gradient-based CAM approximations) rather than leaving this entirely unaddressed.

### Trivial
- **Minor notation inconsistency between c_i and c_t.** In Proposition 4.2 (Eq. 12, 13) and Definition 4.4 (Eq. 14), the notation uses c_i where c_t (target class index) would be consistent with Definitions 3.3, 3.4, and 4.5. The intended meaning is clear but the inconsistency is a minor clarity issue.

## Nice-to-Haves
- An ablation study isolating the contribution of the absolute-value penalty term vs. the CFCE core term vs. the KL regularization would help understand which component drives the alignment improvement.
- Testing on a subset of ImageNet with more classes (e.g., ImageNet-100) would provide evidence of scalability.
- Analysis of failure cases where approximate masks are inaccurate and CFCE degrades performance would give a more balanced picture.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **"Theorem 4.6 proof is in the missing appendix"** — Removed per hard rule: the parser strips appendix sections from all papers; proofs exist in the original submission.
- **"CE w/ Arch baseline has unspecified architectural modifications in missing Appendix C"** — Removed per hard rule: the parser strips appendix sections; details exist in the original submission.
- **"RFS metric values are implausible (0.224 suggests improved accuracy when foreground is corrupted)"** — Removed: this misunderstands the RFS metric, which measures relative foreground sensitivity. A positive RFS means the model is *more sensitive* to foreground corruption (good for alignment), not that accuracy improves. The baselines have negative RFS, confirming they are not foreground-sensitive.
- **"The non-uniqueness is a non-issue since HiResCAMs are deterministically computed"** — Partially removed/softened. The non-uniqueness is a real property of the mapping from predictions to explanations, even if deterministic for a fixed model. The paper's motivation is valid in principle, but the severity is overstated — this is captured in the Minor weakness above.
- **"GradCAM comparison is not apples-to-apples because baselines don't use CAM supervision"** — Removed: the fact that CFCE uses CAM-based supervision while baselines don't is exactly why the comparison is meaningful (it tests whether adding this supervision improves alignment on an independent explanation method). The GradCAM IoU improvement (16.25→18.88, and 51.52 with KL) provides independent validation.
- **Strength about "consistency theorem" removed from strengths** — kept, it's a claimed theorem. But I should note the proof is claimed to be in the appendix.

Actually, let me reconsider the strength about Theorem 4.6. The theorem statement is in the paper, it's a valid claimed strength even if the proof is in the appendix. I'll keep it.

Let me also reconsider "GradCAM comparison is not apples-to-apples" — the harsh critic says baselines don't use CAM supervision so comparing their GradCAM IoU to the CFCE model's GradCAM IoU confounds the explanation method with the training signal. But the whole point is to test whether CFCE training changes GradCAM alignment. The baselines are the control (no CAM supervision) and CFCE is the treatment. The GradCAM IoU is measured using the same GradCAM method for both. This is a valid comparison. So I'll remove this criticism.

## Novel Insights

The reviews surface one genuinely novel insight beyond the paper's own framing: **the reversal of direction between interpretability and training.** Most prior work uses interpretability as a post-hoc diagnostic; this paper instead uses interpretability maps as a *procedural constraint* during training. The harsh critic's skepticism about the circularity of this approach highlights an important meta-methodological point that the paper's community would benefit from — namely, that when the explanation method used for evaluation is the same as the one embedded in the loss, the evaluation confound must be addressed head-on with a clearly separated, independent measurement framework. The paper partially does this (GradCAM IoU, ablation metrics, RFS, downstream segmentation) but could be more explicit about which metrics are independent and which are not.

## Suggestions
1. Add a clear "Independence of Evaluation" paragraph explicitly separating metrics that are circular with the training objective (ContrastiveCAM IoU) from those that are independent (GradCAM IoU, RFS, ablation accuracy) and state what each proves.
2. Include a brief computational cost analysis: wall-clock time per training step and total training time vs. cross-entropy, especially as a function of number of classes.
3. Provide theoretical justification for the absolute value in Eq. 15 (or replace with a smooth alternative like squared penalty).
4. Add a discussion section on the clean accuracy trade-off: under what conditions is the 3–4 point drop acceptable, and can the hyperparameter λ₁ in the KL term be tuned to control this trade-off?
5. Add a simple ablation comparing CFCE to a baseline that directly regularizes CAMs to match masks (e.g., ||H ⊙ (1 − CAM)||) to isolate the benefit of the ContrastiveCAM machinery.

## Score and Decision

The paper makes a solid contribution: it identifies a genuine redundancy in HiResCAMs, proposes ContrastiveCAMs that remove it cleanly, and demonstrates that using these maps during training improves feature alignment across multiple datasets and metrics. The main concerns — some overstatement of the theoretical motivation, partial circularity in the primary evaluation metric (though mitigated by independent metrics), missing computational analysis, and a clean accuracy trade-off — are real but not fatal. No weakness undermines the core claims when the full set of evidence is considered.

I assess this as a solid paper that would benefit from revision but is a legitimate, novel contribution. The contributions are concrete, the experiments are broad, and the core idea is interesting.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>