Now I have all the information needed. Let me write the consolidated final review.

## Summary

This paper proposes Duet, a certified robustness training method that uses a pre-trained vanilla model as a guide to preserve clean accuracy. The core idea is to decompose weight matrices via SVD into rotation matrices (U, V^T) and singular values (Σ), then enforce similarity between the vanilla model's rotation matrices and the certification model's during training. This targets the practical problem that certified robustness training degrades clean accuracy.

## Strengths

- **Novel knowledge-transfer mechanism**: The paper identifies that certified robustness training over-regularizes rotation structure in weight matrices, and uses SVD decomposition of the vanilla model's weights to preserve rotation information during certified training. This is a principled departure from prior work that focuses only on singular-value constraints. The loss function $Loss_{sim}$ is explicitly defined (Section 4.4), and the motivation connecting SVD components to clean accuracy vs. certified robustness is articulated.

- **Promising quantitative results are reported**: The paper states a 3.76% improvement in clean accuracy over a global-Lipschitz baseline with only a 0.93% decrease in certified accuracy (Section 1, contributions). The rotation matrix similarity is reported as rising from 77.8% to 95.6% (Section 5). These results, if verified, directly support the paper's central claim.

- **Practical low-rank approximation**: The method uses a low-rank approximation of the vanilla model's rotation matrices (Section 4.3), done offline, to reduce computational and storage overhead. This is a sensible design choice for making the approach more feasible.

## Weaknesses

### Fatal
None.

### Major

- **Very thin experimental evaluation relative to the claims**: The paper tests on only one dataset (CIFAR-10), one model architecture (six conv + two FC), and one perturbation radius ($\epsilon = 36/255$ for $l_2$). There are no results on SVHN, Tiny ImageNet, or other common certified robustness benchmarks. No variation of perturbation radii is tested. This makes it impossible to assess generalization of the method.

- **No proper results table with absolute numbers and baselines**: The key quantitative claims — 3.76% clean accuracy improvement, 0.93% certified accuracy decrease — appear only in the contributions list (Section 1, line 23) and the abstract. There is no table or panel in the experimental section that presents clean accuracy, certified accuracy, and baseline numbers side by side. The paper's figures (Figure 2, 3) and Table 1 are images, making the core quantitative evidence difficult to verify from the text. This is the most critical missing element.

- **No ablation study isolating the mechanism**: The paper does not test whether the improvement comes from the rotation matrix similarity loss versus simply initializing the certification model from the pre-trained vanilla model. An ablation comparing (a) certified training from scratch, (b) certified training initialized from the vanilla model *without* the similarity loss, and (c) the full Duet method is essential to establish that the proposed mechanism, not just pretrained initialization, drives the improvement.

- **Method underspecified in key details**: (1) The full training objective is not stated — the paper never writes $\mathcal{L}_{total} = \mathcal{L}_{cert} + \lambda \mathcal{L}_{sim}$ or specifies $\lambda$ or its schedule. (2) The rank $r$ for low-rank approximation is never specified, and no analysis of how $r$ affects the clean-accuracy/computation trade-off is provided. (3) The algorithm is presented only as an image (Figure 2 / Algorithm 1). (4) The certified robustness training loss $\mathcal{L}_{cert}$ is not explicitly defined — the paper references prior work but does not state how the certified loss is combined with the similarity loss.

- **"On par with local Lipschitz" claim is unsubstantiated**: The paper states it "performs on par" with local Lipschitz regularization (Huang et al., 2021) but provides no numerical comparison for this claim. Without numbers, this claim is unverifiable.

### Minor

- **The similarity metric is not defined**: The paper reports "average similarity" between rotation matrices as 77.8% and 95.6% but never defines the metric. Is it cosine similarity between subspaces? Frobenius norm of the difference? Angular distance between corresponding singular vectors? This makes the central quantitative claim about similarity improvements ambiguous.

- **No error bars or multiple runs**: The paper reports single-run results without any measure of variance. While single runs are not uncommon in this area, the lack of any error reporting weakens confidence.

- **The central intuition (rotation → clean accuracy, singular values → certified robustness) is plausible but unsubstantiated**: Section 4.2 provides intuitive reasoning but no formal argument or empirical analysis showing that rotation matrices causally determine clean accuracy independently of singular values. A direct analysis showing that layers with higher rotation similarity correspond to higher clean accuracy would strengthen the paper significantly.

- **No computational cost comparison**: The paper criticizes local Lipschitz regularization for "significant computational and memory costs" but does not report training time or memory usage for Duet versus the baselines. Since Duet requires storing a second model and computing SVD decompositions, its own overhead should be quantified.

### Trivial

- **The related work section (Section 3) is largely a listing of prior methods without critical positioning relative to the proposed approach.**
- **Section 4.2 contains some redundant text.**

## Nice-to-Haves

- A controlled experiment comparing: (a) certified training from scratch, (b) certified training with vanilla-model initialization but no similarity loss, (c) certified training with vanilla-model initialization + similarity loss (Duet).
- Results on additional datasets (e.g., SVHN, Tiny ImageNet) and perturbation radii.
- An analysis of how rotation similarity evolves over training and how it correlates with clean accuracy at the layer level.
- A specification of the similarity metric and the rank $r$ used.
- A quantitative table comparing clean accuracy, certified accuracy, and training time for all methods.

## Removed Points

- **"Rota_van and Rota_cer are never explained"**: The paper explicitly defines $Rota_{van} = U_{van}^l (V_{van}^T)^l x$ and $Rota_{cer} = U_{cer}^l (V_{cer}^T)^l x$ in the equations directly preceding the Loss_sim formula (Section 4.4, line 144-145). The critic missed these definitions.
- **"The equation ∑_{i≤r} u_i v_i^T = U V^T is algebraically incorrect"**: The critic misunderstands the paper. The paper is approximating the *rotation matrices* (U, V^T), not the full weight matrix W = U Σ V^T. If U and V^T on the RHS are the rank-r truncated matrices (standard interpretation in context), the equation U V^T = Σ_{i≤r} u_i v_i^T is correct. There is no missing singular value diagonal because the paper is not reconstructing W — it is approximating the rotation component itself.
- **"Ball_p appears garbled"**: This is a PDF-parser artifact; the original submission renders $Ball_p$ properly.
- **"Figures are not visible"**: Parser artifact — figures are present in the original submission.
- **"M(F,x) is used inconsistently"**: The paper uses both $M_{F,x}$ and $M(F,x)$; this is a trivial notational variation, not a substantive weakness.
- **"Too many related works, not enough positioning"**: While the related work section is list-like, this is a presentation preference, not a factual error.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a proper results table** presenting clean accuracy, certified accuracy, and (ideally) certified robustness radius for Duet, the global Lipschitz baseline, and the local Lipschitz baseline, with standard deviations over 3–5 runs. This is the single most important fix.

2. **Write the full training objective** as $\mathcal{L}_{total} = \mathcal{L}_{cert} + \lambda \mathcal{L}_{sim}$, specify $\lambda$ (and whether it is scheduled), and define $\mathcal{L}_{cert}$.

3. **Run the missing ablation**: compare certified training from scratch, certified training with vanilla-model initialization (no similarity loss), and full Duet. Report results in a table.

4. **Define the similarity metric** explicitly. If it is cosine similarity averaged over layers, say so.

5. **Extend experiments** to at least one additional dataset (e.g., SVHN) and one additional perturbation radius to demonstrate generalization.

6. **Specify the rank $r$** used for low-rank approximation and discuss how it was chosen.

7. **Provide the algorithm** in textual pseudocode (not just an image) so the method is reproducible.

8. **Report training time/memory** for Duet versus the baselines to substantiate efficiency claims.

## Score and Decision

The paper proposes a genuinely novel approach to the clean accuracy vs. certified robustness trade-off, with a well-motivated SVD-based decomposition of weight matrices into rotation and scaling components. However, the experimental evaluation is insufficient to support the claimed contributions: only one dataset and architecture are tested, there is no ablation isolating the core mechanism, key results are presented only as percentages in the introduction without a proper table, the method is underspecified (no $\lambda$, no rank $r$, algorithm in an image only), and the "on par with local Lipschitz" claim is unsubstantiated. The contribution is interesting and may be publishable after substantial revision, but in its current form the evidence is too thin.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>