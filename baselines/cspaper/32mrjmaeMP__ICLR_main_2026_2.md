---
job_id: 6f9ac7bb-1b60-424b-b8f1-b89c650f3e1c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 32mrjmaeMP.pdf
paper: Dataless Weight Disentanglement in Task Arithmetic via Kronecker-Factored Approximate Curvature
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, sitting at the intersection of transfer learning, representation learning, model composition/task arithmetic, and optimization via curvature approximations.

## Minimum Quality
Pass ✅. The submission contains the necessary scientific components, including abstract, introduction, methodological development, experiments with quantitative results, and conclusion; while some claims are stronger than the evidence provided, the paper is complete, technically substantive, and above desk-reject quality.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies dataless regularization for task arithmetic. The main idea is to rewrite representation-drift regularization under model linearization as a quadratic form involving the Jacobian Gram matrix, interpret that matrix as a generalized Gauss-Newton object, and then approximate it with KFAC to obtain a practical regularizer, called TAK. The paper evaluates TAK on vision and language task arithmetic, including task addition and task negation, and also proposes a heuristic for merging per-task KFAC factors into a single regularizer with constant complexity in the number of tasks.

## Strengths
The paper addresses a meaningful limitation of prior representation-drift regularizers, namely the need to access data from other tasks during training. Framing the drift penalty as a curvature approximation problem is a sensible and technically grounded way to remove this dependency, and the resulting method is conceptually aligned with the structure of linearized fine-tuning.

I found the empirical comparison in the linearized regime reasonably convincing. In **Table 1 (Page 6)**, TAK consistently improves over plain linear fine-tuning and also over the diagonal GGN approximation across all three CLIP backbones. The gap versus the diagonal approximation is not tiny, especially on ViT-B/32 and ViT-B/16, which supports the paper’s claim that capturing intra-layer structure matters here. The fact that TAK is competitive with $\tau$Jp while being dataless is a real practical advantage.

The task negation results in **Table 2 (Page 7)** are also a meaningful strength. TAK achieves lower target-task accuracy while preserving control-task performance at a similar or better level than the baselines. This broadens the paper beyond “just another addition benchmark” and suggests the regularizer is affecting the geometry of edits in a way that is useful for more than one downstream operation.

The paper does a good job showing that the method is not merely improving peak performance after careful coefficient tuning, but also improving robustness to task-vector scaling. This comes through clearly in **Figure 4 (Page 8)**, where the green TAK curve is both higher and flatter over a broad $\alpha$ range than the non-linear post-hoc merging baselines in panel (a). Even if one debates whether this completely “eliminates” tuning, the figure does support the narrower claim that the method is less sensitive to $\alpha$ than several alternatives.

I also appreciated the explicit computational analysis. **Table 3 (Page 9)** is important because it directly tests the accumulated-regularizer heuristic against the naive $O(T)$ formulation; the empirical gap is small. Likewise, **Figure 6 (Page 9)** gives a reasonably concrete picture of the precomputation and training overheads, which is helpful because curvature-based methods often look attractive on paper and painful in practice.

The exposition around the connection between representation drift and curvature is mostly understandable. In particular, the chain from Eq. (3) to the GGN discussion in **Section 3.2, Pages 3-4** is one of the more useful parts of the paper, because it ties the proposed regularizer to a familiar second-order object rather than presenting it as an isolated heuristic.

## Weaknesses
1. **The core “dataless” claim is slightly overstated, because the method still depends on task-specific statistics computed from data, and this distinction matters scientifically.**  
   The paper repeatedly frames TAK as a dataless approach, but in practice the method requires precomputed per-task KFAC factors from the external tasks, see **Algorithm 1 (Page 3)** and the discussion in **Section 3.4 (Page 5)**. This is not the same as requiring no external task information. The raw data are not needed at regularization time, yes, but task-specific second-order summaries still must be estimated somewhere from those datasets. This matters because the practical modularity story depends on who computes, stores, and shares these factors, and whether that is allowed under the same privacy or segregation constraints used to motivate the problem. The paper partially acknowledges this only later in the appendix, but in the main paper the rhetoric is stronger than the method actually supports. A more precise characterization would be “no raw external data at fine-tuning time,” not simply “dataless.”

2. **The accumulation/merging step in Eq. (8) is a heuristic with weak justification in the main paper, yet it is central to the claimed constant-complexity result.**  
   The practical value proposition of TAK relies heavily on replacing $\sum_t \lambda_t (B_t^l \otimes A_t^l)$ by a single merged Kronecker product in **Eq. (8), Page 5**. However, the paper gives essentially no derivation in the main text, only the statement that it “empirically matches” the un-merged formulation. That is a thin foundation for the method’s most deployment-relevant claim. Worse, the expression itself is asymmetric: the $\lambda_t$ weights appear only on the $A_t^l$ side, not on the $B_t^l$ side. If this is intentional, the paper should justify why the task weighting acts differently on activations and output-gradient covariances. If it is shorthand, the notation is misleading. Since the merged approximation is the difference between an elegant but impractical method and the proposed practical one, this should not be hand-waved.

3. **There are mathematical and notational inconsistencies that make the derivation harder to trust than it should be.**  
   A few examples:
   - In **Section 3.1 (Page 3)**, the paper defines representation drift earlier as $\Delta_{t\to t,t'}(x):=\|z_{t,t'}(x)-z_t(x)\|_2$, but then the derivation writes $\Delta_{t\to t,t'}(x)=\|J_\theta f_{\mathrm{lin}}(\cdot)\tau_{t'}\|_2^2$, which changes the quantity from an $\ell_2$ norm to a squared norm without warning. This is not a cosmetic issue, because the following regularizer becomes a quadratic form only for the squared norm. The loss should be redefined explicitly, for example as $\Delta^2$ or with a separate notation.
   - In **Eq. (7), Page 5**, the left-hand side starts with $\mathcal{L}_{\mathcal{D}_t}(\tau_{t'})$ while the right-hand side uses $\mathcal{L}_{\mathcal{D}_{t'}}(\tau_{t'})$. That appears to be a typo, but it is sitting in the central training objective.
   - In **Algorithm 2 (Page 3)**, line 1 says “Linearize the net: $(f,\theta_0)\to f_{\mathrm{lin}}(\bullet,\tau_{t'}-\theta_0)$,” which is dimensionally and conceptually odd; the linearization should be around $\theta_0$, and the trainable variable is the displacement or task vector. As written, it looks like the second argument of $f_{\mathrm{lin}}$ is a parameter vector, then later the objective uses $\tau_{t'}+\theta_0$. This should be made consistent.
   These issues are fixable, but they accumulate in the exact part of the paper where rigor matters most.

4. **The non-linear experiments are useful, but the paper overstates what they establish.**  
   The method is derived for the linearized setting, and the paper is transparent about that to some extent. However, in **Section 4, Pages 6-7**, the extension to non-linear fine-tuning is justified largely by citing attention-only fine-tuning as approximately linear, then showing empirical gains when pairing TAK with that regime. This is suggestive, not a validation of the theory. In **Table 1**, the non-linear results are also less clean than the linear ones. For example, “Attn. Only FT + TAK” with $\alpha=1.0$ is much worse than tuned versions and still trails some tuned baselines, which weakens the headline narrative about robustness and plug-and-play usage. The right panel of **Figure 2 (Page 5)** also visually shows more instability than the linear regime. I do not object to including these experiments, but the paper should treat them as exploratory evidence rather than as a near-equal second pillar.

5. **The empirical evidence is solid in breadth, but weaker than it looks in statistical depth.**  
   Most main tables report single numbers without uncertainty estimates. The paper does include some seed analysis for $\lambda$ in the appendix, but the key comparisons in **Table 1**, **Table 2**, and **Table 3** do not show variances, confidence intervals, or statistical tests. This matters because several margins are small, for example TAK versus $\tau$Jp in the linearized task-addition results, or TAK versus naive multi-task regularization in **Table 3 (Page 9)**. If the central message is that KFAC is competitive with data-dependent methods while being more modular, then confidence in these close comparisons matters.

6. **The paper’s claims about “eliminating the need for held-out tuning” are stronger than what the results fully justify.**  
   The strongest support comes from **Table 1**, where TAK with $\alpha=1.0$ is indeed close to or equal to the best-$\alpha$ setting in the linearized regime. That is good. But the non-linear regime clearly does not support the same claim, and even in linearized settings this is shown only on a small number of benchmarks and backbones. More importantly, the method itself introduces a new regularization hyperparameter $\beta$ and task weights $\lambda_t$; in the implementation details, there are backbone-specific regularization magnitudes and an extra $0.1$ rescaling for the last CLIP layer. So the paper is really trading one type of post-hoc coefficient tuning for another type of training-time tuning. That may still be a good trade, but it is not the same as tuning disappearing.

7. **The task-localization / OOD narrative is interesting but oversold relative to the evidence in the main paper.**  
   In **Figure 5 (Page 8)**, the histograms do suggest a better separation between inliers and outliers under KFAC regularization than under naive linear FT. However, this is presented as evidence for task localization and then further extrapolated to a “natural use for out-of-distribution detection.” That jump is too large. The figure is a diagnostic on a very specific benchmark setup where outliers are other known tasks from the same training pool. It is not an OOD evaluation in the usual sense, and no quantitative OOD metric is reported in the main paper. This matters because otherwise readers may walk away believing the method has a validated OOD capability, when the paper actually shows only a task-conditioned score separation.

8. **The method comparison is not always apples-to-apples, especially when mixing training-time regularization with post-hoc merging methods.**  
   In **Figure 4 (Page 8)**, TAK is compared against TIES, TSV, and ISO. The paper correctly notes these are complementary because they operate post hoc, but the framing still leans toward “TAK makes simple TA competitive with state-of-the-art merging strategies.” That is partly true, but these methods solve somewhat different optimization problems and can in principle be combined with TAK, as also hinted in the appendix. The main-text comparison would be more compelling if it more sharply separated “improves the quality of task vectors during training” from “best final merge pipeline overall.”

9. **The literature positioning is good overall, but there are still gaps around adjacent approaches to enforcing disentanglement or distilling linearized behavior.**  
   The paper is well cited on KFAC and task arithmetic, and it covers the main immediate baselines. Still, the positioning around alternative ways to enforce weight disentanglement appears narrower than it should be. There is room to discuss more explicitly methods that regularize task-vector geometry or distill favorable linearized behavior into non-linear models, since these are very close in spirit to the paper’s stated goals. This does not invalidate the contribution, but it does make the novelty feel somewhat under-contextualized.

10. **Some implementation choices with nontrivial effect are only lightly justified in the main narrative.**  
    The appendix notes several details that could materially affect outcomes, including using full GGN for LayerNorm/class token, estimating KFAC on subsets of data, and down-weighting the final CLIP layer regularization. These may all be sensible, but they indicate that the practical recipe has more knobs and design decisions than the clean high-level story suggests. Since the method’s appeal is “simple, modular, practical,” these choices deserve clearer exposure in the main paper, not only in supplementary material.

## Questions
1. In **Eq. (8)**, why are the task weights $\lambda_t$ applied only to the $A_t^l$ factors and not to the $B_t^l$ factors? Is this intentional? If yes, please provide the derivation or at least the intuition, because the current expression looks asymmetric in a way that is hard to reconcile with $\sum_t \lambda_t (B_t^l \otimes A_t^l)$.

2. Please clarify the exact drift quantity being minimized in **Section 3.1**. The text first defines $\Delta_{t\to t,t'}(x)$ as an $\ell_2$ norm, but the derivation and Eq. (3) correspond to the squared norm. Is the actual objective
   $$
   \frac{1}{|\mathcal D_t|}\sum_{x\in\mathcal D_t}\|J_\theta f(x,\theta_0)\tau_{t'}\|_2^2
   $$
   rather than the average norm? If so, please rewrite the notation consistently.

3. Can the authors provide variance across seeds for the main comparisons in **Table 1-3**? This would increase confidence in several close margins, especially TAK vs. $\tau$Jp in the linearized regime and TAK vs. naive multi-task regularization in **Table 3**.

4. The paper emphasizes “dataless” regularization. Could the authors be more precise about the threat/privacy model? Which of the following are assumed shareable: per-task KFAC factors, merged factors, dataset sizes $|\mathcal D_t|$, and architecture-specific layerwise statistics? Clarifying this would help assess the real deployment advantage over data-based regularizers.

5. For the non-linear regime, what evidence suggests that attention-only fine-tuning is linear enough for the KFAC penalty derived from the linearized argument to remain appropriate? Even a simple diagnostic correlating the regularizer with observed representation drift in that regime would strengthen the claim.

6. Regarding **Figure 5**, can the authors report a quantitative separation metric, such as AUROC or a rank-based statistic, rather than only histograms? This would make the task-localization claim easier to evaluate and would prevent over-interpretation from visual inspection.

7. Since **Table 3** suggests the accumulated regularizer is close to the naive $O(T)$ formulation, can the authors report when it fails most clearly, for example as a function of task heterogeneity or backbone size? That would help understand the operating regime of the heuristic.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The paper discusses privacy and modularity motivations, but it does not introduce a dataset collection pipeline, human-subject protocol, or deployment setting that raises a specific ethics flag requiring dedicated review.

## Soundness Rating
3: good. The core technical idea is plausible and generally supported by experiments, but several mathematical definitions and practical approximations, especially around Eq. (7)-(8), need clarification, and some claims are stronger than the evidence provided.

## Presentation Rating
3: good. The paper is readable and generally well organized, with useful figures and tables, but there are enough notation inconsistencies, objective-definition ambiguities, and slightly overstated claims that I cannot rate presentation as excellent.

## Contribution Rating
3: good. The paper makes a useful contribution by connecting dataless task-arithmetic regularization to curvature approximations and demonstrating a practical KFAC-based method, though the practical method relies on a heuristic merge step and the novelty is more in adaptation and execution than in a fundamentally new principle.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a meaningful idea, solid empirical breadth, and practical relevance, especially in the linearized setting. At the same time, the main practical approximation is heuristic, the derivation has avoidable inconsistencies, and several claims are a bit more ambitious than the evidence. I lean positive because the contribution is useful and likely interesting to the ICLR community, but I do not think this is a clean accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant areas of task arithmetic, linearized fine-tuning, and curvature approximations, though I did not independently verify every implementation detail beyond what is stated in the paper.