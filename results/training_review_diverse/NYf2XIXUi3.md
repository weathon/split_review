Now I have all the information I need. Let me compose my final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the consolidated review.

**Re: Claim about "no qualitative analysis" (Harsh Critic point 5):** The paper DOES have qualitative analysis on lines 222-223 and 239-240 (Figure 6 and text). So the claim that there is "no qualitative analysis" is inaccurate. However, the lack of a user study or any formal interpretability evaluation is a valid concern. I'll downgrade this.

**Re: Rule about "missing appendix":** The reviewer mentions derivations being "sketched" - this is about presentation quality, not about missing content. Keep as minor issue.

**Re: Claim about "does not release code":** The paper doesn't cite a code repository, and the rule says to remove criticisms about availability of cited entities. This is about noticing absence. I'll move this to a Nice-to-Have, as the method paper would benefit from code release but it's not a weakness of scientific content per se.

**Re: "no discussion of the sign of influence scores":** The paper uses sign implicitly in Section 5.2 (proper vs. opposite order) but never explicitly discusses what a negative influence means. This is a valid minor point.

Let me finalize the score. Given: 
- Novel theoretical contribution (influence functions for meta-learning) ✓
- Clear derivations ✓
- Significant experimental gaps (1 meta-learner instead of 2, no baselines, approximation not validated, limited scope)
- Overclaiming in abstract/conclusion

I'd say score 5.0 - borderline. The core idea is solid but the evidence is substantially weaker than claimed.

Wait, let me think about this more carefully. The paper claims to demonstrate with "MAML and Prototypical Network" but only uses MAML. This is a clear overclaim. The paper claims TLXML "effectively serves as a similarity measure" but has no baselines to compare against. The paper proposes a Gauss-Newton approximation but doesn't validate it.

These are significant gaps. In many conferences, this would be a weak reject (score ~4-5). But the theoretical contribution is genuinely novel and well-derived. The experiments, while limited, do show some validation.

I'll go with 5.0 - borderline, with the note that the paper could be strengthened significantly.## Summary

This paper proposes TLXML (Task-Level eXplanation of Meta-Learning), a method that extends influence functions to meta-learning to quantify how each training task influences meta-parameters, adapted weights, and inference outcomes of a meta-trained model. The authors derive task-level influence formulas (Eq. 4-7), propose a Gauss-Newton approximation to reduce Hessian computational costs from O(p q²) to O(p q), and handle non-invertible Hessians via pseudo-inverse projection. Experiments on MiniImagenet with MAML validate the approach in task-distinction and task-distribution-distinction settings.

## Strengths

- **Novel formal extension of influence functions to meta-learning's bi-level structure.** The paper derives task-level influence functions (Eq. 4–7) that respect the outer/inner loop separation, going beyond point-wise or meta-feature explanations. This is a principled adaptation of influence functions (Koh & Liang, 2017) to the meta-learning setting, which has been unexplored (Section 4.1).

- **Computational feasibility via Gauss-Newton approximation.** The paper identifies that exact Hessian computation costs O(p q²) and proposes a Gauss-Newton matrix approximation that reduces this to O(p q), making the method potentially scalable to larger models (Section 4.2).

- **Handling non-invertible Hessian with pseudo-inverse projection.** The paper addresses the practical reality that Hessians in overparameterized networks have flat directions by using the pseudo-inverse H⁺ to project influence onto the non-flat subspace. The need for this is empirically demonstrated by the observation that 92 of 1285 Hessian eigenvalues are negative (Section 5.1).

- **Empirical validation of task-distribution distinction with statistical significance.** In Section 5.2, TLXML distinguishes regular MiniImagenet tasks from noise tasks with p-values < 0.01 under task augmentation and weight decay. The alignment of influence scores with generalization behavior (proper order under augmentation, opposite order under overfitting) provides a meaningful signal that the method captures distribution-level information (Table 2).

- **Task-group extension for improved abstraction.** The paper generalizes influence to groups of tasks (Eq. 9), enabling explanations at coarser granularity (e.g., groups from task augmentation). This is a practical enhancement for user-facing explanations (Section 4.1).

- **Qualitative interpretability demonstration.** Figure 6 shows semantically meaningful alignment between highly-influential training tasks and the test task, with accompanying text analysis (Section 6, lines 239-240).

## Weaknesses

### Major

- **Abstract and conclusion overclaim the experimental scope: only MAML is tested, not Prototypical Network.** The abstract states the method is demonstrated "with MAML and Prototypical Network," and the discussion (line 222) claims "experiments with a small network and two meta-learners." However, the experimental setup (line 193) clearly states "We use MAML as a meta-learning algorithm." Prototypical Network is described in the preliminaries but never appears in any experiment. This is a direct mismatch between the paper's advertised scope and its evidence, and a reader cannot assess whether the approach generalizes to other meta-learners.

- **No baseline comparisons.** The experiments test whether TLXML influence scores correlate with expected properties but compare against no competing explanation method (random ranking, cosine similarity of gradients, or any alternative). Without baselines, the paper cannot support the claim that TLXML provides *useful* or *better* explanations — only that its scores are not random. Section 5.1 and 5.2 both lack even trivial competitors.

- **Gauss-Newton approximation is not empirically validated.** The approximation (Eq. 11) is used in all CNN experiments (Section 5.2), but the paper provides no comparison of approximated vs. exact influence scores (even on the small two-layer network where the exact Hessian is tractable). There are no runtime measurements, no rank-correlation comparison, and the key conditions (existence of P̄(X|ω*), closeness of ω̂ to ω*) are stated but never checked. The experimental results in Section 5.2 therefore rest on an unvalidated numerical method.

### Minor

- **The task-distinction experiment (Section 5.1) is a limited sanity check.** It uses a two-layer fully-connected network with Bag-of-Visual-Words features (1285 parameters) — far from modern meta-learning practice. Test tasks are identical to training tasks (an easy self-similarity check). More concerningly, Figure 3b shows that the self-rank is not always 1; the paper attributes this to non-convexity and negative Hessian eigenvalues (92 out of 1285) but does not investigate whether this instability correlates with test loss or model confidence.

- **The interpretability/evaluate claim is asserted but not rigorously tested.** The paper emphasizes that TLXML provides "concise, task-based explanations that align with users' abstraction levels" and are "more intuitive than local explanations," but there is no user study and no formal comparison against local explanation methods on interpretability criteria. The qualitative analysis in Figure 6 is present but shallow.

- **No discussion of the sign of influence scores.** Section 5.2 implicitly uses the sign of influence (proper order vs. opposite order), but the paper never defines what a negative influence on performance means or how to interpret it.

- **No runtime or memory measurements.** The paper claims O(p q) cost after optimization but never reports actual compute times or memory usage, leaving the computational contribution entirely theoretical.

### Trivial

- The conditions for the Gauss-Newton approximation (line 162: "if there exists a distribution P̄(X|ω*) that is well approximated by the training taskset, and ω̂ is close to ω*") are stated without ever being checked or discussed again.

- Section 5.2 interprets "proper order" vs. "opposite order" as overfitting vs. generalization, but does not independently verify model behavior (e.g., by reporting train/test accuracy or task-level losses) to confirm this interpretation.

## Nice-to-Haves

- **Prototypical Network experiment**: Adding even a small-scale experiment with Prototypical Network would satisfy the advertised claim and give confidence in generalizability.
- **Code release**: Publishing the implementation would aid reproducibility.
- **Sensitivity analysis**: A brief analysis of sensitivity to hyperparameters (MAML learning rate α, meta-batch size, number of training tasks) would indicate robustness.
- **Ablation: exact vs. approximated influence**: A small-network comparison of exact and approximated influence scores (rank correlation, not just trend) would directly validate the central computational claim.

## Removed Points

These points are flagged to be removed from the main review; treat them with caution.

- **"No qualitative analysis"** (Harsh Critic point 5, part): The paper does contain qualitative analysis in Section 6 (Figure 6 and accompanying text, lines 222-223, 239-240). The claim that there is "no qualitative analysis" is factually wrong. The legitimate concern about lacking a user study is preserved in Minor weaknesses above.
- **"The paper does not release code"**: The paper does not cite a code repository, so this criticism is about absence rather than doubting a cited entity. Moved to Nice-to-Haves as a practical suggestion.
- **"The conditions for the Gauss-Newton approximation are hand-wavy"**: This is preserved above as a Trivial point (the conditions are stated but not checked), but stripped of the "hand-wavy" characterization which is a style judgment.
- **Section-by-section minor presentation criticisms** about "sketched derivations" and "disjointed logic" that do not affect the core contribution are either absorbed into existing weakness tiers or removed as non-substantive.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the paper's main contributions (novel influence functions for meta-learning, Gauss-Newton approximation, pseudo-inverse handling) and its main gaps (overclaimed experimental scope, missing baselines, unvalidated approximation) but do not provide genuinely novel observations beyond what is already evident from the paper and its weaknesses.

## Suggestions

1. **Align claims with evidence**: Remove or qualify the claimed demonstration with Prototypical Network in the abstract/conclusion, or add a corresponding experiment.
2. **Add trivial baselines**: Compare TLXML influence scores against cosine similarity of task gradients and random ranking in both experiments. This is low-cost and would substantially strengthen the claim that TLXML provides useful information.
3. **Validate the Gauss-Newton approximation**: On the small two-layer network (Section 5.1 setup), compute both exact and approximated influence scores and report rank correlation (Spearman/Kendall). Also report wall-clock time for the exact vs. approximate computation.
4. **Investigate the self-rank failures**: Analyze why the self-rank is not always 1 for certain tasks in Section 5.1 — does it correlate with task difficulty, loss value, or degree of non-convexity?
5. **Define and discuss the sign of influence scores**: Add a paragraph explaining what positive vs. negative influence on test loss means for interpretability.

## Score and Decision

The paper presents a genuinely novel theoretical contribution — extending influence functions to task-level explanations in meta-learning — with clean derivations and a practical computational optimization. However, the experimental validation is significantly weaker than what the paper claims: the abstract promises demonstration with two meta-learners (only MAML is tested), no baselines are included against any alternative method, the central approximation (Gauss-Newton) is used without empirical validation, and the interpretability motivation is asserted but not tested. These are not fatal flaws — the theoretical work stands on its own — but they materially weaken the evidence for the paper's claims. The paper would benefit from a major experimental strengthening before it meets the bar for publication.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>