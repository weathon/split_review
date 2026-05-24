Now I have enough information. Let me write the final consolidated review.

---

## Summary

This paper demonstrates that CLIP models trained on smaller datasets (CC3M, CC12M) are undertrained, and shows that a simple heuristic—resetting the learning rate scheduler and training for a few additional epochs—yields large accuracy gains (e.g., 31% → 41.7% ImageNet zero-shot for a ResNet-50 on CC12M). The gains saturate after only 3 extra epochs, match or exceed results from more complex CLIP-improvement methods, and largely disappear on large-scale data (LAION-400M), bounding the phenomenon's scope.

## Strengths

1. **A striking and directly actionable empirical finding.** Figure 1 shows a 10 percentage-point zero-shot ImageNet gain on a ResNet-50 trained on CC12M from a single LR reset with 10 extra epochs. This is a practically useful result for any practitioner training CLIP models at modest scale.

2. **Consistency across architectures and multiple benchmarks.** Table 2 reports gains on seven ImageNet variants (e.g., +41.3% on ImageNet-R for ResNet-50) and for three CLIP architectures (RN50, ViT-B-32, ViT-B-16), supporting the generality of the phenomenon.

3. **The benefit saturates quickly.** Figure 3 shows accuracy plateaus after only 3 extra epochs across all three architectures, demonstrating that the improvement comes from the reset itself, not from prolonged additional training.

4. **Early reset further isolates the LR schedule as the key factor.** Figure 4 shows that resetting after just 10 epochs (training 10+10=20 total) already beats the fully trained 75-epoch model (37% vs. 31%). This strongly supports the claim that the single-cycle cosine schedule is a bottleneck.

5. **The scope is honestly bounded.** Table 6 shows minimal gains on LAION-400M (e.g., ImageNet: 62.94 → 63.29), confirming that the undertraining claim is specific to smaller datasets and is not over-generalized.

## Weaknesses

### Major

1. **Baseline inconsistency between the paper's own training and cited literature.** The paper's own training (Figure 1, Section 3.1) produces a ResNet-50 on CC12M at **31%** ImageNet zero-shot accuracy. Yet Table 7 cites the "CLIP (baseline)" from Radford et al. (2021) at **36.5%** — a 5.5-point gap. Table 2's caption then claims an "improvement of 11.3% compared to the performance reported by the literature," but 41.7 − 36.5 = 5.2, not 11.3. The +11.3% clearly references the authors' own ~31% baseline. This inconsistency between the authors' reproduction and the literature baseline, and the confusing caption, undermines the reader's ability to interpret how the reported gains relate to prior work. The authors should explain why their baseline (31%) differs from the original CLIP paper's (36.5%) and clarify which baseline is used in each comparison.

### Minor

2. **Missing direct control: reset vs. extended single-cycle training.** The paper claims the improvement comes from the LR restart rather than from additional training iterations. However, there is no experiment that directly compares (a) train for 75 epochs + reset for 10, against (b) train for 85 epochs with a single continuous cosine schedule. Figure 5 (from-scratch multi-cycle vs. single-cycle) is a related but different experiment. The evidence in the paper (Figure 3's saturation, Figure 4's early-reset results) is suggestive but not definitive on this attribution. Adding this control would cleanly resolve the question.

3. **No variance estimates.** All main results are reported from single runs. While large-scale CLIP training is expensive, the gains are large enough that even 2–3 seeds would substantially increase credibility. This is especially relevant for Figure 4's surprising finding that resetting after 10 epochs beats the full 75-epoch model.

4. **Uncontrolled comparison with prior work.** Table 7 aggregates results from several papers (ProtoCLIP, CyCLIP, CLOOB, DeCLIP, CLIP Improved) without specifying backbone architectures, training epochs, batch sizes, or data splits used by those methods. The caption says "ResNet-50 CLIP model," but whether all methods used identical training recipes is unclear. This limits the strength of the claim that the simple LR-reset strategy is "competitive with existing approaches."

### Trivial

5. **Minor presentation issues.** The caption of Table 2 conflates the authors' own baseline with the literature baseline when describing the improvement magnitude.

## Nice-to-Haves

- The direct control experiment (85-epoch single cycle vs. 75+10 reset) would cleanly separate the effect of more training from the effect of the LR restart.
- Reporting results with 2–3 random seeds would increase confidence, especially for the most striking results (Figure 1, Figure 4).

## Removed Points

- **Criticism that the paper does not report whether other methods used the same data/preprocessing (Section 3.6):** This is already evident from the way Table 7 is constructed (citing literature results); the paper does not claim a tightly controlled comparison. Removed as overly demanding for a literature survey table.
- **Criticism that the LAION-400M results are "equivocal" (Section 3.5):** The paper's conclusion ("less likely to be undertrained") is appropriate given the minimal and mixed improvements. The critic's characterization is not a genuine weakness—the negative result is informative.
- **Criticism questioning reproducibility due to missing hyperparameters:** These details are standard for the community and would likely appear in the appendix (which was stripped by the parser).
- **Strength claiming the paper matches or exceeds prior complex methods:** Partially moderated; the comparison is uncontrolled so this strength is discounted accordingly (but not fully removed since the results are still suggestive).

## Novel Insights

The most interesting observation from the review process is how the harsh critic's three main concerns (baseline inconsistency, missing control, uncontrolled comparison) each independently reduce confidence in different parts of the argument, yet all three orbit the same underlying issue: the paper would benefit from more rigorous experimental design and clearer communication of what is being compared. The strength finder correctly identified the paper's core empirical contribution, but the calibration against venues like ICLR poster-level work (e.g., the CLIP OOD analysis at 5.75, AlignCLIP at 6.29) shows that the paper's weaker areas are precisely where those accepted papers tended to be stronger—particularly in controlled comparisons and variance reporting.

## Suggestions

1. **Clarify the baseline.** State explicitly that the paper's own reproduction yields 31% on CC12M, explain any gap from the literature 36.5%, and clearly label which baseline is used in Table 2 vs. Table 7.
2. **Add the total-epochs control.** Compare (75+10 with reset) directly against 85 epochs of a single cosine cycle to solidify the attribution to the restart.
3. **Report at least 2-3 seeds** for the principal experiments (Figures 1, 3, 4) to establish that the gains are not due to lucky initialization.

## Score and Decision

**Calibration:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Understanding Transferable Representation Learning and Zero-shot Transfer in CLIP | S5yOuNfSA0 | 6.50 | R1 | Stronger theoretical contribution but similar empirical scope |
| Does CLIP's generalization performance mainly stem from high train-test similarity? | tnBaiidobu | 5.75 | R1, R2 | Similar empirical/analytical nature; fair comparison on rigor |
| FastCLIP: A Suite of Optimization Techniques to Accelerate CLIP Training | FbQLFsBbTe | 3.67 | R1 | Weaker; limited novelty, unclear presentation |
| Mitigate the Gap: Improving Cross-Modal Alignment in CLIP | aPTGvFqile | 6.29 | R2 | More comprehensive evaluation (incl. retrieval); similar strong empirical results |
| X-Sample Contrastive Loss | c1Ng0f8ivn | 6.00 | R2 | Similar simplicity of idea; some comparison fairness concerns |
| Follow-Up Differential Descriptions | g6rZtxaXRm | 6.00 | R2 | Stronger controlled experiments |
| Semi-Supervised CLIP Adaptation | 97D725GJtQ | 5.80 | R2 | Comparable evaluation rigor |

**Round 1 bracket:** between 3.5 and 7.5, narrowed to [5, 6.5].

**Round 2 narrowing:** The paper sits below the 6.29 AlignCLIP paper (which had more comprehensive evaluation including retrieval and fine-tuning) and the 6.0 X-Sample paper (more controlled experiments). It is comparable to the 5.75 CLIP OOD paper (similar empirical/analytical nature, similar evaluation scope). The baseline inconsistency and missing control prevent a higher score, but the core finding is too striking to place much lower.

**Final score:** 5.5. The paper has a real, practically useful finding that is clearly demonstrated in self-contained experiments. However, the unnecessary baseline inconsistency and the missing direct control for total training epochs prevent it from reaching the 6+ range.

**Decision:** Accept

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>