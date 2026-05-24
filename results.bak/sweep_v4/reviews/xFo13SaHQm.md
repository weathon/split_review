Now I have sufficient context from the calibration anchors. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper identifies and formalizes "copy-paste artifacts" in identity-consistent image generation (where models overly replicate the reference image rather than generating natural variations). It contributes (1) MultiID-2M, a large-scale paired multi-person dataset with multiple references per identity, (2) MultiID-Bench, a benchmark with a novel copy-paste metric M_CP, and (3) WithAnyone, a FLUX-based model using paired training, GT-aligned ID loss, and an ID contrastive loss with extended negatives to reduce copy-paste while maintaining high identity fidelity.

## Strengths

- **Breaks the established trade-off between identity fidelity and copy-paste.** In Table 1, WithAnyone achieves Sim(GT)=0.460 (comparable to the best face customization baseline InstantID at 0.464) while attaining CP=0.144 — far lower than all face customization baselines (InstantID 0.337, PuLID 0.315). Figure 5 shows that WithAnyone is the only model that deviates from the regression curve into the high-Sim(GT), low-CP region. This is the paper's central empirical contribution and is well-supported.

- **The paired-training strategy (Phase 3) is convincingly shown to reduce copy-paste.** Table 3 shows that removing Phase 3 raises CP from 0.161 to 0.239 while leaving Sim(GT) essentially unchanged (0.405 vs 0.406), directly demonstrating that paired training — not reconstruction — is the key driver of copy-paste reduction.

- **MultiID-2M is a significant resource for the community.** The dataset of 500k labeled multi-ID images with ~400 reference images per identity across ~3k identities, plus 1.5M unpaired images, fills a real gap. The ablation (FFHQ-only row in Table 3: Sim(GT)=0.224, CP=0.027) confirms that the dataset is necessary for the reported performance.

- **The M_CP copy-paste metric (Eq. 2) is a useful formalization.** It quantifies the relative bias of the generated embedding toward the reference vs. the ground truth, and cleanly reveals the trade-off across 12 models in Figure 5. This provides a standardized tool for future work that goes beyond reporting only Sim(Ref), which rewards copying.

- **The GT-aligned ID loss is a practical engineering contribution.** Using ground-truth landmarks to align generated images for ID loss computation avoids unstable landmark extraction at high noise levels, enabling ID supervision across all noise levels with negligible overhead. Figure 7 and the ablation (w/o GT-Align: Sim(GT) drops from 0.405 to 0.385, CP increases from 0.161 to 0.175) support its effectiveness.

## Weaknesses

### Fatal
None.

### Major

- **The extended negatives ablation raises an unaddressed question about the contrastive loss design.** In Table 3, removing extended negatives (w/o Ext. Neg.) yields CP=0.074 — substantially *lower* (better) than the full setting's CP=0.161 — while Sim(GT) drops from 0.405 to 0.368. This means the extended negatives improve identity similarity at the cost of increasing copy-paste artifacts. The paper states that "the effectiveness of ID contrastive loss is greatly reduced" without specifying which dimension (Sim or CP), and offers no explanation for why the component designed to reduce artifacts has this side effect. This does *not* invalidate the overall contribution (the full model still beats all baselines on the combined trade-off), but it undermines the clean narrative that all components uniformly reduce copy-paste. The authors should either explain why this CP increase is acceptable relative to the Sim(GT) gain, or reframe the claim about the contrastive loss's role.

- **The evaluation does not fully test "controllable generation" under novel prompts.** MultiID-Bench evaluates on a reconstruction-style task: given a reference and a prompt *derived from a ground-truth image*, measure similarity to that ground truth. While this tests prompt-following ability, it never isolates the model's response to a prompt describing a pose, expression, or attribute *not present in any target image* (e.g., fix a reference, prompt for "wearing sunglasses" or "extreme head turn," and measure attribute accuracy via CLIP or a face attribute classifier). The qualitative examples (Fig. 6) do show improved prompt adherence over baselines (e.g., making subjects smile when reference is neutral), which partially supports the controllability claim, but a dedicated quantitative experiment would significantly strengthen the paper.

### Minor

- **User study is small and lacks inter-rater reliability reporting.** Ten participants ranking 230 groups is acceptable for this community, but the absence of any agreement metric (e.g., Fleiss' kappa) reduces confidence. The study is cited as supporting evidence rather than primary evidence, so this does not threaten the paper's main conclusions, but the reporting should be more rigorous.

- **Reliance on celebrity images limits insight into generalizability.** MultiID-2M uses publicly known figures, and all evaluations use these identities. Whether the approach generalizes to unseen non-celebrity individuals with different demographic distributions is unknown. The paper should acknowledge this as a limitation more explicitly.

### Trivial

- Table 3 has minor formatting issues in the parsed text (e.g., merged column values), but these are parser artifacts, not author errors. The underlying table is standard.

## Nice-to-Haves

- A dedicated controllability experiment (fixed reference + novel prompt, measuring attribute accuracy via CLIP similarity or attribute classifiers) would directly support the "controllable generation" claim in the title and abstract.
- Testing on non-celebrity faces (e.g., from a consented dataset like LFW or a private collection) would strengthen claims of real-world applicability.
- Inter-rater reliability metrics for the user study would improve its evidentiary weight.

## Removed Points

- **"Ablation contradiction is fatal to the core claim"** (Harsh Critic Issue 1, framed as "structural flaw"). The criticism claims the ablation directly contradicts the paper's central claim. However, the paper's central claim is that the *full method* (all components combined) breaks the trade-off compared to all baselines — which is supported by Table 1 and Figure 5. The contrastive loss is explicitly designed to strengthen identity preservation, not specifically to reduce CP. The increase in CP from w/o Ext. Neg. (0.074) to full (0.161) is accompanied by a meaningful Sim(GT) gain (0.368 → 0.405), and the full method still achieves the best trade-off among all face customization methods. This is a design trade-off within the method, not a contradiction. The criticism has been downgraded to a Major weakness about clarity/interpretation.

- **"Evaluation is entirely a reconstruction task"** (Harsh Critic Issue 2, framed as evidential gap). The evaluation uses different images as reference and target (paired training), so it is not "reconstruction" in the traditional sense of generating the exact same image. The prompts describe specific poses/expressions different from the reference, and the qualitative results show the model follows these prompts better than baselines. The gap is real (no experiment with entirely novel prompts) but is a missing piece of evidence, not evidence that the claim is false. Downgraded to Major weakness.

- **"User study is unconvincing"** (Harsh Critic Issue 3). This criticism is valid but the study is supplementary evidence, not primary. Ten participants ranking 230 groups is common in this field. Downgraded to Minor.

- **Missing related works** (implied in Harsh Critic's notes). Removed per instructions.

- **Formatting/style nitpicks, appendix references, reproducibility concerns about hyperparameters.** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a fundamentally new perspective on the problem that the paper itself does not already articulate.

## Suggestions

1. **Explain the CP increase from extended negatives.** Add a paragraph or a small analysis discussing why w/o Ext. Neg. achieves lower CP at the cost of lower Sim(GT), and why the net trade-off in the full model is favorable compared to all baselines. This will resolve the apparent contradiction and strengthen the paper's technical narrative.

2. **Add a controllability experiment with novel prompts.** Select a set of reference identities and prompt for expressions/attributes not present in any target image (e.g., "smiling," "looking left," "wearing sunglasses"). Measure attribute accuracy (e.g., via a face attribute classifier or CLIP score) while reporting identity similarity. This directly supports the "controllable generation" claim in the paper's title.

3. **Acknowledge the celebrity-data limitation explicitly and add one analysis on non-celebrity faces** if possible, or frame it as a clear limitation for future work.

4. **Report inter-rater agreement for the user study**, even a simple percentage of agreement or Fleiss' kappa.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| ID-Booth (face generation diffusion) | 3.00 (Reject) | Much weaker: limited novelty, insignificant improvements over baselines. WithAnyone has clear quantitative advantages and more substantial contributions. |
| TLDR (data reconstruction) | 2.50 (Reject) | Much weaker: no metrics, no SOTA comparison, toy datasets only. WithAnyone is far more rigorous. |
| Towards Enhanced Controllability (diffusion control) | 3.75 (Reject) | Weaker: limited experiments, no clear advantage. WithAnyone has stronger empirical support. |
| Refine-by-Align (artifact refinement) | 5.75 (Accept) | Comparable: well-motivated task, decent experiments, but limited novelty. WithAnyone has stronger contributions (dataset + benchmark + model). |
| Vec2Face (face generation) | 6.00 (Accept) | Comparable: strong results but concerns about unfair comparisons and data dependency. WithAnyone is similarly solid with different trade-offs in weaknesses. |
| CTRL (diffusion control with RL) | 6.50 (Accept) | Slightly stronger: rigorous theory, but limited experiments. WithAnyone has more comprehensive evaluation but weaker theory. |

The paper makes three concrete, well-supported contributions (dataset, benchmark, model) and demonstrates the headline claim convincingly in Figure 5 and Table 1. The weaknesses are about clarity of interpretation (ablation explanation) and scope of evaluation (controllability testing), neither of which invalidates the core contribution. However, these gaps are significant enough that the paper would benefit from addressing them before publication. Positioned relative to the anchors, the paper sits solidly in the mid-range of accept-quality work.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>