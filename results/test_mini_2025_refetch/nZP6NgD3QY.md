Now I have a comprehensive set of anchors. Let me write the consolidated review.

**Round 1 bracket**: 5.5–7.0 (clearly above CABS/4.75 and TATR/5.75, below the theory paper at 7.5 and the test-time adaptation paper at 8.0)

**Round 2 narrowing**: Comparing to Fine-Tuning Attention Modules (6.25, Accept Poster) — AdaMerging has stronger novelty but a more significant evaluation concern. Compared to Mitigating Backdoor Effect (7.00, Accept Poster) — that paper had more thorough evaluation. AdaMerging sits between these, closer to the 6.0 side.

**Final score**: 6.0

---

## Summary

This paper proposes AdaMerging, a method that learns per-task or per-layer merging coefficients for multi-task model merging via entropy minimization on unlabeled test data. The core idea is that instead of using a single global merging coefficient λ (as in Task Arithmetic and Ties-Merging), the method adaptively learns distinct coefficients for each task vector or each layer of each task vector, using test-time entropy minimization as a surrogate objective. Results on eight image classification tasks with CLIP ViT-B/32 and ViT-L/14 backbones show substantial improvements over static baselines.

## Strengths

- **Well-motivated and novel approach**: The paper identifies a genuine limitation of existing task-vector merging methods — their sensitivity to a single global merging coefficient — and proposes a principled solution: learning per-task/per-layer coefficients via entropy minimization. The idea of using unsupervised entropy minimization as a proxy objective for model merging is novel and grounded in the test-time adaptation literature.

- **Empirical validation of the entropy-loss correlation**: Section 3.2.2 presents Figure 3, showing a Spearman correlation coefficient of 0.87 between entropy and prediction loss across all eight tasks, with clear monotonic behavior. This directly supports the core premise that minimizing entropy is a valid surrogate for minimizing multi-task prediction loss during coefficient optimization.

- **Large and consistent performance gains**: Layer-wise AdaMerging achieves 80.1% average accuracy on ViT-B/32 vs. 69.1% for Task Arithmetic and 72.4% for Ties-Merging (Table 1). On ViT-L/14 it achieves 90.8% vs. 84.5% and 86.0% respectively (Table 2). These gains are consistent across architectures.

- **Interpretable learned coefficients**: Figure 4 shows that shallow layers receive smaller coefficients than deep layers, which aligns with the well-known principle that shallow features are more task-general. This provides qualitative validation that the learned coefficients capture a meaningful structure.

- **Demonstrated generalization and robustness**: Table 3 shows that AdaMerging adapts effectively to unseen tasks (outperforming baselines by 4.4–9.1%), and Table 4 shows robustness to seven types of distribution shift, with an average improvement of 8.45% over Task Arithmetic.

## Weaknesses

### Fatal
None.

### Major

- **Unclear test-data separation in evaluation**: The paper uses unlabeled test data for optimizing merging coefficients (Section 3.2.2) but does not clearly state whether the same test samples used for adaptation are also used for computing the final accuracy numbers. If they are, this conflates test-time adaptation with the benefit of the coefficient structure. The claim that "even if only 0.1% or 1% of unlabeled tests are available" suggests awareness of this concern, but the main experiments lack a clearly described hold-out protocol. This makes the headline "11% improvement" over static baselines difficult to interpret — it combines the effect of test-data access with the effect of the adaptive coefficient structure. The paper should either (a) use a separate hold-out set from each task's test split for adaptation, (b) clearly state that all test samples are used for both adaptation and evaluation and note that this is a transductive setting, or (c) compare against baselines that also receive test-data access (see next point).

- **Missing control baseline**: There is no baseline where a single global λ is learned via the same entropy-minimization objective on unlabeled test data. This would isolate whether the performance gains come from the per-task/layer coefficient structure or simply from the ability to adapt to the test distribution. Notably, the paper's own data partially mitigates this concern: Task-wise AdaMerging (per-task coefficients, using test data) achieves 71.1% on ViT-B/32, which is *worse* than Ties-Merging's 72.4% without test data. This suggests that test-data access alone does not automatically produce large gains, and the per-layer structure is critical. However, this is not the same as a single-λ entropy-minimization baseline, and the absence of this control weakens the attribution of gains to the proposed coefficient structure.

- **No error bars or variance reported**: None of the tables report standard deviations, confidence intervals, or multiple seeds. Given that the method involves optimization on test data, overfitting is a real risk. Single-run results leave the stability of the reported gains unverified.

### Minor

- **Computational cost not quantified**: The paper states that the optimization is "cheap" but provides no concrete numbers (batch size, number of gradient steps, wall-clock time). Since the method requires backpropagation through the full merged model for each gradient step, this cost could be non-trivial for larger models. A quantitative assessment would help practitioners assess the practical overhead.

- **Entropy-loss correlation measured on a single fixed model**: The correlation analysis in Figure 3 is computed on predictions from one specific merged model (with a particular λ). It does not directly prove that the gradient of entropy with respect to λ points in a direction that reduces loss across the optimization landscape. The optimization could encounter spurious minima where low entropy does not correspond to low loss. The paper acknowledges this implicitly but does not analyze the optimization landscape.

- **Generalization framing**: The generalization experiment (Table 3) adapts coefficients on test data from unseen tasks. This is more accurately described as test-time adaptation to new tasks rather than "generalization" in the traditional sense (where the model is fixed and tested on new tasks without additional adaptation). The results are still valuable, but the framing could be more precise.

### Trivial
None.

## Nice-to-Haves
- Include a baseline where a single λ is learned via entropy minimization on test data (would strengthen the attribution of gains to the coefficient structure).
- Add a small ablation showing results when a held-out portion of the test set is used for adaptation and the remainder for evaluation, to directly address the data-leakage concern.
- Report standard deviations across 3–5 random seeds for the main results.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Figure 1 is misleading"** (Harsh Critic): The critic claimed the figure is misleading because the AdaMerging line was generated after test-data adaptation while baseline lines reflect fixed λ. The figure correctly shows AdaMerging as a constant (since it adaptively learns coefficients) while baselines vary with the global λ hyperparameter. This is standard visual communication and not misleading — the figure's purpose is to show sensitivity to λ, and AdaMerging's flat line correctly shows it is not sensitive to a global λ value.

- **"The correlation analysis does not guarantee that minimizing entropy drives λ in the right direction"** (Harsh Critic, overstated): The critic raised this as a "methodological gap" but the paper provides substantial evidence (Spearman ρ=0.87, clear monotonic relationship in Figure 3). The concern about spurious minima is valid but minor; it was already moved to Minor weaknesses above.

- **"Generalization experiment is unfair because test data from unseen tasks was used for adaptation"** (Harsh Critic): This is not an unfair comparison — it demonstrates a legitimate capability of the method (test-time adaptation to new tasks). The baselines are static and cannot do this. The criticism would only be valid if the paper claimed the generalization happened without adaptation, which it does not. The framing could be clearer (see Minor weaknesses), but the experiment itself is valid.

- **"Robustness comparison is unfair because Task Arithmetic could also benefit from adaptation"** (Harsh Critic): This is speculative. The experiment shows a real capability: AdaMerging optimized on clean test data transfers to corrupted data. If the critic wants to claim Task Arithmetic would benefit equally, they would need to demonstrate it. The comparison as-is tests "does adaptation on clean data help when tested on corrupted data?" which is a fair and informative question.

- **"11% improvement is not an improvement of the merging scheme per se"** (Harsh Critic): The paper's own data contradicts this: Task-wise AdaMerging (which also uses test data) is worse than Ties-Merging (71.1 vs 72.4), showing that test-data access alone does not explain the gains. The per-layer structure is clearly responsible for much of the improvement.

- **Strengths removed from Strength Finder**: Several strengths flagged by the Strength Finder were generic or conflicted with verified weaknesses. Specifically, "Large and consistent performance gains" was kept but with a caveat; the claim of "11% improvement" as stated by the Strength Finder was qualified to note the evaluation concern. Supporting strengths about robustness and interpretability were kept as they are concrete and evidence-backed.

## Novel Insights

The synthesis of the reviews reveals a key tension: the paper makes a genuine contribution (learning per-layer merging coefficients via entropy minimization is a new and well-motivated idea), but the evaluation protocol sits in an uncomfortable middle ground between standard model merging (where all methods use the same fixed test set for evaluation only) and test-time adaptation (where using test data for adaptation is the point of the method). The paper's own data — showing that the task-wise variant (which also accesses test data) underperforms Ties-Merging — is an important self-control that partially addresses the concern, but this point is not highlighted in the paper. A cleaner framing as a transductive model-merging method, with appropriate baselines (e.g., single-λ entropy minimization), would substantially strengthen the contribution.

## Suggestions
1. Add a baseline where a single global λ is learned via the same entropy-minimization objective on unlabeled test data. This is the most impactful single experiment to isolate the benefit of the per-task/layer coefficient structure.
2. Clearly specify in the experimental setup how test data is partitioned for adaptation vs. evaluation. If all test data is used for both, state this explicitly and frame the method as transductive model merging.
3. Report standard deviations for the main results across multiple random seeds or optimization runs.
4. Provide wall-clock time or FLOPs for the gradient-based coefficient optimization to substantiate the "cheap" claim.

## Score and Decision

**Round 1 bracket**: After bracketing calibration, the paper sits between weak anchors at ~2.3–3.4 (papers with obvious flaws or limited scope) and strong anchors at 7.5–9.0 (polished papers with thorough evaluation). The plausible range was 5.5–7.0.

**Round 2 narrowing**: Compared against:
- CABS (4.75, Reject) — AdaMerging has much larger gains and a more novel approach. Clearly better.
- Foldable SuperNets (5.50, Reject) — AdaMerging has a stronger contribution. Better.
- TATR (5.75, Reject) — AdaMerging has a more novel approach and larger gains. Better.
- Fine-Tuning Attention Modules Only (6.25, Accept Poster) — AdaMerging has stronger novelty but a more significant evaluation concern. Comparable, slightly lower due to the test-data issue.
- Mitigating Backdoor Effect (7.00, Accept Poster) — That paper had a more thorough evaluation with multiple runs. AdaMerging is weaker due to the evaluation concern.
- When is Task Vector Provably Effective (7.50, Accept Oral) — A theory paper with a different contribution type; not directly comparable.

The paper lands at **6.0**: a genuine contribution with strong results, but the evaluation protocol concern (unclear test-data separation) prevents a higher score. The test-data issue is not fatal because the paper's own data (Task-wise AdaMerging underperforming Ties-Merging) partially rebuts the strongest form of the criticism, but the missing hold-out protocol and absent single-λ entropy baseline are significant gaps that would need to be addressed.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>