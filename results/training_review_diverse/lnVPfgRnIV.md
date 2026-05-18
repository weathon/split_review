Now I have a complete picture. Let me write the final consolidated review.

---

## Summary

This paper proposes a "compression-sparsity" principle for incremental segmentation, arguing that instead of freezing old knowledge, the model should dynamically compress the feature subspace of old classes and enforce sparse separation (large inter-class distances) among Gaussian mixture peaks to improve plasticity without sacrificing stability. The method applies a learnable affine transformation to features with diameter and distance constraints, then fuses transformed and original features via a weighted combination. On VOC, the method reports substantial improvements over prior state-of-the-art (e.g., +11.7% MIoU on the 10-1 setting), with consistent gains across five incremental configurations and on ADE20K.

## Strengths

- **Large and consistent empirical gains across multiple challenging settings.** The method outperforms prior state-of-the-art by substantial margins on VOC across five different incremental configurations (11.7%, 9.8%, 6.2%, 11.8%, 7.1% in incremental-stage MIoU) and shows consistent improvement on ADE20K (100-5, 11 steps). These gains are much larger than typical incremental segmentation improvements, making a strong case for the value of the approach.

- **Ablation confirms both compression and sparsity are independently necessary.** Table 3 shows that removing either component degrades performance, with the most severe drop when sparsity is removed in the 19-1 setting. This directly ties the empirical success to the proposed design principles rather than to confounding factors.

- **Analysis of design choices (fusion method, α/β balance).** The paper systematically compares attention-based vs. weighted feature fusion (Table 4) and examines the impact of the α/β trade-off (Table 5), providing engineering guidance for practitioners.

- **Generalization to a larger, more challenging dataset.** Results on ADE20K (100-5, 11 steps) show consistent improvements over prior methods in both base and incremental stages, demonstrating scalability beyond the simpler VOC benchmark.

## Weaknesses

### Major

- **Constraint enforcement mechanism is underspecified, making the method non-reproducible from the main text.** Equations 9–10 define hard inequality constraints on the transformed features \(F_t^r\) (diameter must shrink below intra-class peak distances; inter-class peak distances must exceed the maximum intra-class diameter). The paper states that \(\gamma\) and \(\tau\) are "learnable parameters that satisfy the constraint conditions," but it never explains *how* these constraints are enforced during optimization. The loss function in Equation 14 contains no term that directly implements these inequalities — no penalty term, no projection operator, no reparameterization trick is described. Without this mechanism, a reader cannot determine whether the method actually enforces the constraints or merely uses them as a loose intuition. This is a critical gap for a method paper, and it is not addressed by the supplementary materials reference (which may help with other details but does not rescue the missing optimization description in the main text).

- **The theoretical derivation (Section 3.2, Equations 1–7) does not convincingly establish the compression-sparsity principle.** The paper claims this as a key contribution ("Mathematical analysis demonstrates the benefit of compression-sparsity"), but the logical chain is broken at several points. Equation 6 shows a proportional relationship between the Hessian/Fisher information and the variance of Gaussian mixture components, but the jump from "there is a proportional relationship between optimal parameter search and variance" to "we should perform preliminary feature contraction" is an intuition, not a deduction. Equation 7 states that pixel-level class features should be well-separated — a generic desideratum for any classifier, not a unique justification for the specific sparsity mechanism. The math provides motivation but does not *derive* the design choices in Section 4. The paper would benefit from characterizing this as a heuristic or empirical motivation rather than claiming it as a formal derivation.

### Minor

- **Hyperparameter reporting across Table 1 and Section 5.3 is confusing.** Section 5.2 reports the 10-1 result as 11.7% with \(\alpha=0.2/\beta=0.8\) and also reports 9.8% with \(\alpha=0.8/\beta=0.2\) for the same setting. Section 5.3 then states "\(\alpha\) and \(\beta\) are set to 0.8 and 0.2 in this paper for qualitative and quantitative analysis." This creates ambiguity about which hyperparameter setting produced which numbers in Table 1. The paper does explain the rationale (tuned best vs. consistent setting for cross-dataset robustness), but the presentation could be much clearer — e.g., by explicitly noting in the table caption which \(\alpha/\beta\) value was used per column and separating the "tuned best" from "consistent-setting" results.

- **Key implementation details are vague.** The paper mentions "convex points in feature space," "peak points \(P_1, P_2\) in the Gaussian mixture distribution," and "three-dimensional Gaussian mixture distribution" but does not explain how these are computed from neural network features — e.g., whether the Gaussian mixture parameters \(\mu_k, \sigma_k\) are estimated from class-conditional feature statistics, learned via a separate network, or derived from normalizing flows. The paper references supplementary materials, but the main text should at least sketch the procedure.

- **The knowledge distillation loss (Equation 14) is introduced without justification relative to simpler alternatives.** The contrastive formulation using normalized dot products and the BCE term is presented as a single combined loss, but the paper does not compare against standard KD baselines (e.g., pixel-wise KL divergence) or ablate the choice of contrastive formulation. Given that the ablation (Table 3) focuses on compression and sparsity rather than the loss function, it is unclear how much of the gain comes from the loss design versus the compression-sparsity mechanism.

### Trivial

- The text contains several grammatical issues and awkward phrasings (e.g., "the plasticity of in the incremental stage") that slightly hinder readability but do not affect scientific content.

- Some figure references in the text are not clearly connected to their discussion (e.g., Figure 4 is mentioned but the surrounding text on line 205 discusses classes 16–20 without a clear figure callout).

## Nice-to-Haves

- Adding per-class IoU breakdowns for incremental stages would help substantiate that plasticity gains are not concentrated in a single easy class.
- A comparison against a baseline that also adjusts old knowledge (e.g., by running a few gradient steps on old exemplars or updating prototypes) would help isolate the effect of the compression-sparsity mechanism from simply "doing something different" with old knowledge.

## Removed Points

- **"Ablation gains are modest" (Harsh Critic):** The reviewer claimed ablation gains are "modest" (e.g., 18.5/26.3 → 24.0/27.1 in 19-1). A 5.5% MIoU improvement from a single component is substantial in incremental segmentation. This criticism is factually too harsh and is removed. The paper's Table 3 also shows larger gains in other groups.
- **"KD loss not compared against standard KD baselines" portion of the Harsh Critic's "Other Observations":** Kept in Minor but the reviewer overstated its severity — the paper compares against prior methods that use various forms of distillation; the issue is that the specific contrastive formulation is not ablated, not that no KD baseline exists.
- **"Memory sampling strategy not specified":** The paper explicitly states "we adopt the same memory sampling strategy (Cha et al., 2021)" — this IS specified. Removed.
- **"Does not compare against dynamic distribution methods":** The reviewer asks for comparisons against methods from a different sub-field (domain incremental learning), which is scope creep for a class-incremental segmentation paper. Moved here.
- **"Qualitative evaluation lacks quantitative evidence" (as a standalone weakness):** t-SNE visualizations are a standard qualitative tool; per-class IoU tables are already present in the paper's Figures 4–5 (referred to in text). The weakness as framed conflates qualitative with quantitative. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no cross-paper insight that the authors have not already identified.

## Suggestions

1. **Clarify constraint enforcement.** Explicitly state whether the constraints in Equations 9–10 are (a) enforced via a differentiable penalty added to the loss, (b) satisfied architecturally (e.g., through the parameterization of \(\gamma,\tau\)), or (c) approximately satisfied through the optimization dynamics. If the constraints are not strictly enforced, say so and describe how the network approximately learns to satisfy them. Add the constraint term (if one exists) to the loss function or describe the projection step.

2. **Tighten the theoretical claims.** Either (a) present the math as an intuition/heuristic rather than a derivation, or (b) provide a proof-of-concept on a synthetic problem that validates the claimed link between compression-sparsity and improved incremental likelihood. Remove claims of "demonstrating" or "proving" the principle from the math alone.

3. **Disambiguate the hyperparameter reporting.** In Table 1, explicitly mark which \(\alpha/\beta\) value was used for each column, and separate the "tuned best" results (11.7%) from the "consistent-setting" results (9.8%) if both are reported. Alternatively, report only the consistent-setting results in the main table and move the tuned results to an appendix.

4. **Specify the Gaussian mixture computation.** Briefly describe how \(\mu_k,\sigma_k\) are obtained from network features (e.g., per-class empirical mean/variance from the feature maps, or learned via a small head network) and how "convex points" and "peak points" are detected.

## Score and Decision

This paper addresses a genuine limitation of existing incremental segmentation methods (frozen old knowledge limits plasticity) and demonstrates impressive empirical gains. The core idea — compressing and sparsifying feature distributions dynamically — is novel and well-motivated at a conceptual level. However, the method section has a critical gap: the constraint enforcement mechanism for Equations 9–10 is not described, making the approach non-reproducible from the main text. The theoretical derivation is also overclaimed relative to its actual rigor. These issues are addressable but substantial — the paper needs a clear description of how \(\gamma, \tau\) are optimized to satisfy the constraints before its claims can be reliably evaluated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>