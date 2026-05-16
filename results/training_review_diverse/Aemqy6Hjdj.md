Now I have all the information I need. Let me carefully synthesize the final review, verifying every claim against the paper.

---

## Summary

This paper addresses the understudied problem of Compositional Generalization (CG) — generalizing to unseen domain-class combinations in multi-domain multi-class settings. It proposes Compositional Feature Alignment (CFA), a two-stage finetuning method that (i) learns two orthogonal linear heads (class and domain) on a frozen pretrained encoder, and (ii) finetunes the encoder with these heads frozen. The paper also contributes CG-Bench, a suite of CG evaluation splits derived from four existing DG datasets (OfficeHome, DomainNet, iWildCam, FMoW), and provides theoretical analysis using the unconstrained feature model (UFM) showing that CFA induces a compositional feature structure. Experiments on CLIP ViT-B/16 and DINOv2 ViT-B/14 show CFA improves OOD accuracy on most benchmarks.

## Strengths

1. **Well-motivated problem formulation**: The paper clearly distinguishes CG from both domain generalization and compositional zero-shot learning, and provides a formal definition (Definition 1) of the desired compositional feature structure. The motivating analysis (Fig. 3) showing that pretrained models struggle on sparse domain-class combinations is empirically grounded.

2. **Theoretical alignment guarantee**: Theorem 1 proves that under the UFM with orthogonal normalized heads and sufficiently large inverse temperatures, the global optimum of the stage-2 objective yields features decomposable into orthogonal class-dependent and domain-dependent components — directly aligning with the compositional structure in Definition 1. This provides a principled foundation for why freezing orthogonal heads should work.

3. **Consistent OOD improvement across most settings**: CFA (especially with WiSE-FT) achieves the best or near-best OOD accuracy on most benchmarks. For CLIP+WiSE: OfficeHome OOD 56.9% (vs. 53.4% best baseline), DomainNet OOD 9.2% (vs. 8.7%), iWildCam OOD F1 32.5% (vs. 28.7%). For DINOv2+WiSE: iWildCam OOD F1 33.4% (vs. 31.0%). The improvement on FMoW is the main exception where CFA does not achieve the best OOD result.

4. **Practical robustness to limited domain labels**: Table 2 shows CFA remains effective with as few as 10% of domain labels (OOD 53.4% vs. full finetuning 51.0%) and even with zero-shot-predicted domain labels (OOD 52.0%), greatly increasing practical applicability in settings where domain metadata is scarce.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-practice gap undermines the theoretical justification**. The paper's core Theorem 1 is proven under a joint objective that includes both class and domain losses (Eq. 4, with λ>0). However, the actual implementation deviates in two significant ways: (a) Stage-1 trains the two heads *sequentially* (first W2, then W1 with an ℓ2 orthogonality regularizer) rather than jointly as stated in Eq. (1)–(2) (line 209); (b) Stage-2 sets **λ=0**, completely removing the domain-prediction loss from the encoder finetuning (line 211). The authors remark these simplifications are "empirically sufficient" and "reduce compute cost," but provide **no ablation study** in the main paper comparing joint vs. sequential head training or λ>0 vs. λ=0. Because the theorem's guarantee rests on a specific joint objective, the practical algorithm is only loosely connected to the analysis. This is a methodological gap: the paper claims theoretical backing, but the actual procedure does not correspond to the analyzed objective, and the effect of the deviation is unquantified.

2. **Experimental results lack statistical rigor and are sometimes marginal**. Table 1 reports only point estimates with no confidence intervals, standard deviations, or significance tests. Several gains are small: e.g., CLIP on DomainNet CFA+WiSE OOD 9.2% vs. FT+WiSE 8.7% (0.5%), DINOv2 on DomainNet CFA+WiSE OOD 6.4% vs. LP-FT+WiSE 6.2% (0.2%), and on FMoW CFA+WiSE (36.6%) underperforms Reweight-E (41.8%) by a large margin. Without error bars, it is impossible to assess whether these differences are reproducible or noise. The paper's central claim that CFA "outperforms common finetuning techniques" is true in aggregate but would be more convincing with variance estimates and a discussion of failure cases (particularly FMoW).

3. **Missing relevant baselines**. The paper compares against full finetuning, LP-FT, and reweighting schemes but omits several relevant finetuning methods: (a) FLYP (cited in the paper on line 111 and line 280) — a contrastive-style finetuning method for CLIP targeting OOD robustness; (b) domain-adversarial finetuning (DANN-style) — a natural baseline given the two-head architecture (mentioned on line 31); (c) the CG-specific approach of Sivaprasad et al. (2022) (cited on line 283). Given that the claimed contribution is improved CG performance, the absence of these comparisons weakens the evidence that CFA is state-of-the-art.

### Minor

1. **Benchmark construction is somewhat model-dependent**. CG-Bench defines the OOD set as the 20% of domain-class combinations with the lowest zero-shot CLIP accuracy (Section 3.1). This makes the split dependent on a single pretrained model (CLIP ViT-B/16). While using CLIP's weaknesses to identify hard combinations is a reasonable heuristic, the paper does not validate whether the resulting splits isolate compositional generalization cleanly rather than conflating it with "hard examples for CLIP." The same splits are used for DINOv2 evaluations without analysis of whether they remain meaningful for a self-supervised model. This does not invalidate the benchmark, but it limits its generality.

2. **Feature visualization is purely qualitative**. Figure 4 shows features for only 2 domains and 3 classes, with no quantitative metric (e.g., cosine similarity between class and domain prototype vectors, subspace distance) to measure the degree of feature alignment. This limits the strength of the claim that CFA induces the compositional structure in practice.

3. **Comparison asymmetry for DINOv2 experiments**. For DINOv2, WiSE-FT is applied to LP-FT and CFA but not to full finetuning or reweighting baselines (because DINOv2 lacks zero-shot classification heads, line 206). While this follows from the method's design, it makes the DINOv2 comparisons asymmetric — CFA's best results use a postprocessing technique unavailable to some baselines. The paper should discuss this asymmetry explicitly.

4. **The sequential training of heads in Stage-1 uses a soft ℓ2 penalty** ($\|W_1^\mathrm{T} W_2\|_F^2$) rather than the hard orthogonality constraint $W_1 W_2^\mathrm{T} = \mathbf{0}$ stated in Eq. (2). The effect of this relaxation is not discussed or ablated.

### Trivial
- The paper uses "WiSE-FT" and "Wise-FT" inconsistently.
- Figure 3 caption refers to "CLIP" and "CFA" but could more clearly label which panel corresponds to which method.

## Nice-to-Haves
- An ablation of the loss coefficient λ in Stage-2 (the paper mentions it was studied but defers to the appendix, which was stripped).
- Computational overhead comparison (training time, memory) between CFA and standard finetuning.
- Analysis of when WiSE-FT helps vs. hurts ID performance across methods.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism about missing appendix content** (ablation studies referred to appendix): The parser strips appendix sections from all papers; they exist in the original submission. Removed per policy.
- **Criticism about missing hyperparameter details**: Hyperparameters (learning rate, epochs, batch size) are likely in the appendix, which the parser strips. Removed per policy.
- **Cherry-picked numerical comparisons** (critic comparing CFA without WiSE against LP-FT+WiSE for DINOv2 on OfficeHome and DomainNet): When comparing methods with the same postprocessing, CFA+WiSE outperforms LP-FT+WiSE (40.4% vs. 39.7% on OfficeHome, 6.4% vs. 6.2% on DomainNet). The critic's framing was asymmetric. This does not invalidate the broader point about marginal gains but the specific comparisons were misleading.
- **Criticism that the benchmark procedure for other datasets is insufficiently described**: The paper explicitly states it elaborates on DomainNet as an example "due to the page limit" (line 140). The procedure for other datasets follows the same template. Removed as a scope nitpick.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Bridge the theory-practice gap**: Provide an ablation comparing joint vs. sequential head training in Stage-1 and λ>0 vs. λ=0 in Stage-2. If the simplified variant works as well, this is an interesting finding that should be demonstrated explicitly. If not, the paper should align its implementation with the theory or adjust the theoretical claims.
2. **Add error bars**: Report means and standard deviations over 3-5 random seeds for all main results. This would allow readers to assess whether the small improvements (0.2–1.5% on several datasets) are reproducible.
3. **Add at least one external baseline**: FLYP is the most natural comparison for CLIP finetuning, and domain-adversarial training is natural for the two-head architecture. Even a simplified comparison would substantially strengthen the empirical positioning.
4. **Acknowledge and discuss the FMoW failure case**: CFA underperforms simple reweighting on FMoW by ~5 points. Analyzing why would provide useful insights into when the method does and does not work.
5. **Quantify the feature alignment**: Supplement the feature visualization with a quantitative metric (e.g., subspace distance between class and domain feature spans) to support the claim that CFA induces compositional structure.

## Score and Decision

This paper tackles a genuinely understudied problem and proposes a method that is well-motivated, theoretically grounded (with caveats), and shows consistent (if often small) improvement. However, the gap between the theoretical analysis and the actual implementation, the lack of statistical rigor, and the omission of relevant baselines collectively prevent the paper from being convincing in its current form. The core idea has merit and the contributions (CG-Bench, CFA) are useful to the community, but the evidence is too weak to support publication at a top venue. I recommend rejection with encouragement to revise and resubmit.

**Originality**: Good — the CG problem formulation is novel and the method combines existing ideas (two-head architecture, neural collapse, head freezing) in a new way.
**Importance of research question**: High — compositional generalization is realistic and understudied.
**Claims supported**: Partially — the theoretical claim is weakened by the theory-practice gap; the empirical claim would be stronger with error bars and more baselines.
**Soundness of experiments**: Moderate — reasonable breadth but lacks statistical rigor.
**Clarity of writing**: Good — the problem is clearly motivated and the method is well explained.
**Value to community**: Potentially high — CG-Bench could be a useful resource if its construction is validated further.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>