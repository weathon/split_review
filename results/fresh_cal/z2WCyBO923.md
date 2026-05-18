Now I have a thorough understanding of the paper. Let me write the consolidated review.

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

Let me construct this carefully.

---

Based on my thorough reading of the paper, here is my analysis:

**Verified facts from the paper:**
1. The paper does NOT state whether single-expert baselines use mixup during evaluation training. It says "differentiable augmentation strategies" were used broadly.
2. The paper uses easy-sample initialization for multi-expert (top 10-30% lowest loss samples). Single-expert initialization is not specified.
3. The paper reports all results as single numbers without error bars or variance estimates.
4. T_i ∩ T_j = ∅ for data partitioning, but class-level vs. sample-level partitioning is not clarified.
5. Table 2 ablates distance correlation and mixup-based fusion within the multi-expert framework.
6. Table 3 compares proposed cross-expert mixup vs vanilla mixup vs no mixup (all within multi-expert setting, IPC×NoE=5×2).

Let me write the review now.Now I have a comprehensive understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes a mixture-of-experts (MoE) framework for dataset distillation to improve cross-architecture generalization. The approach splits the IPC budget across multiple expert models (each distilling a disjoint subset of real data), uses a distance correlation minimization loss to encourage diversity across experts, and applies a mixup-based fusion strategy during evaluation to combine information from different experts. Experiments on CIFAR-10/100 and ImageNette using IDC, IDM, and MTT as surrogate methods show that the multi-expert framework generally improves cross-architecture performance over single-expert baselines.

## Strengths

1. **Well-motivated and clearly articulated problem.** The paper correctly identifies that cross-architecture performance degradation is a real limitation of existing dataset distillation methods (Section 1). The intuition that splitting the distillation budget across multiple experts can capture more diverse information is sensible and grounded in the observation that distilled datasets overfit the distillation architecture.

2. **Distance correlation ablation provides clear evidence of its benefit.** Table 2 isolates the effect of the distance correlation loss within the multi-expert framework and shows consistent improvements across three distillation methods (IDC, IDM, MTT) and multiple IPC settings. The paper's description of how distance correlation is computed on feature representations from a pretrained model is technically sound.

3. **Cross-expert mixup outperforms vanilla mixup.** Table 3 demonstrates that the proposed expert-specific mixup (mixing images across different experts' subsets) consistently beats both no-mixup and vanilla mixup applied to the same multi-expert distilled data. This provides evidence that the complementary information across experts is meaningful and can be leveraged during evaluation.

4. **Evaluation across multiple surrogate methods and architectures.** The framework is tested with three fundamentally different distillation methods (gradient matching / IDC, trajectory matching / MTT, distribution matching / IDM) and four target architectures (ConvNet-3, VGG-11, ResNet-18, AlexNet). This breadth strengthens the generality of the findings.

5. **Analysis of the number of experts.** Table 4 systematically varies the number of experts (1, 2, 3) with fixed total IPC, showing diminishing returns beyond 2 experts. This provides practical guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baseline: single-expert with vanilla mixup.** The main comparison in Table 1 contrasts multi-expert (with mixup-based fusion) against single-expert baselines. The paper does not specify whether single-expert baselines use any form of mixup during evaluation. Since Table 3 shows that even vanilla mixup provides a non-trivial gain over no-mixup (e.g., ResNet-18 improves from ~39.8% to ~40.7% on the multi-expert data), the improvement attributed to the MoE framework in Table 1 could be partly or largely driven by the mixup augmentation rather than the multi-expert structure itself. The paper should include a baseline where single-expert distilled data is trained with vanilla mixup during evaluation, then compare that to the multi-expert setup with proposed fusion. Without this control, the central claim is only partially supported.

2. **No variance estimates.** All results in Tables 1–5 are reported as single numbers without error bars, confidence intervals, or multiple seeds. Dataset distillation is known to have non-trivial variance due to random initialization, data subset selection, and optimization stochasticity. The reported improvements are often modest (1–3 percentage points), and without variance estimates the reader cannot assess whether these differences are reliable or within noise.

3. **Potential initialization confound between single- and multi-expert.** The paper states that for multi-expert with IDC and IDM, synthetic data is initialized from "easy samples" (top 10–30% lowest-loss real samples selected by a pretrained model). The initialization strategy used for single-expert baselines is not specified. If single-expert baselines use standard random initialization while multi-expert uses curated easy-sample initialization, this asymmetry could explain some of the observed gains independent of the MoE framework.

### Minor

4. **Unclear data partitioning across experts.** The paper specifies that real data subsets are disjoint (T_i ∩ T_j = ∅) but does not clarify whether this means (a) each expert receives different samples from each class (stratified per-class splitting), or (b) different experts receive different classes entirely. This distinction matters for the diversity argument and for whether distance correlation minimization between experts is sensible — if experts see completely different classes, trivial diversity arises from the label difference alone. The use of distance correlation on features (rather than labels) partially addresses this, but the partitioning scheme should be stated.

5. **Missing direct comparison of "splitting alone" vs. single-expert.** Table 2 includes a "w/o DistCorr & w/o Fusion" row (multi-expert without either proposed component), but the paper never explicitly compares this row to the single-expert baseline from Table 1. Such a comparison would isolate whether simply distributing the IPC across two independent distillation runs (without any diversity loss or mixup) already improves cross-architecture performance. This is a simple analysis that would strengthen the attribution of gains to specific components.

### Trivial
None.

## Nice-to-Haves

- Report the computational cost trade-off: training K experts multiplies the distillation cost by roughly K (whether run sequentially or in parallel). Discussing this would give practitioners a fuller picture.
- Add a simple analysis of the diversity achieved — e.g., visualize the distance correlation between expert subsets before and after training, or show example synthetic images from different experts.
- Discuss limitations (e.g., when the method might not help — high IPC regimes, or when the surrogate method is already very strong). Some hints of this exist in Table 1 (e.g., the paper notes "most of" the multi-expert results built by IDM and MTT outperformed baselines, implying some did not).

## Removed Points

These points from the reviewer inputs are removed with justification:

- **Claim that IDC on CIFAR-10 IPC=10 shows a decrease on ConvNet-3**: The paper text states "consistent performance improvements in multi-experts built by IDC over single-expert baselines" — this is unverifiable from the extracted text alone (table images are not readable), and the paper's textual description contradicts the claimed decrease. Removed as potentially a misread of the table.
- **"The paper cannot separate the benefit of having multiple experts from the benefit of mixup augmentation" framed as a fatal structural flaw**: The paper's ablation in Table 2 does partially address this by showing multi-expert w/o fusion vs. w/ fusion. The missing baseline (single-expert+vanilla mixup) is a real gap, but it does not invalidate the paper's core claim that the full framework works. Downgraded from "fatal/structural" to Major.
- **Reproducibility nitpicks about omitted implementation details**: The paper provides sufficient implementation detail (optimizer, learning rate, augmentation, Beta distribution parameters, selection strategy). Removed as a strawman.
- **Calling SupCon results "invalid" due to the same confound**: The SupCon experiment shows multi-expert (mixup during SupCon training) vs. single-expert. The same confound concern applies, but "invalid" is too strong — it's an uncontrolled comparison that would be clarified by the same missing baseline. The generalization to new tasks is still informative.
- **Strength Finder generic strengths**: Claims that the paper "addressed an important problem" or "targeted an interesting question" are dropped as generic/superficial. Only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a meaningful experimental gap (missing single-expert+vanilla-mixup baseline) that the authors should address, but this is a standard methodological concern rather than a novel observation about the paper's approach.

## Suggestions

1. **Run the critical missing baseline**: Report single-expert (IPC=10, NoE=1) with vanilla mixup during evaluation training, and compare it to multi-expert (IPC=5×2) with proposed cross-expert mixup. Place this as the primary comparison in the main table. This cleanly separates the MoE benefit from the mixup benefit.

2. **Report error bars**: Run each experiment for at least 3 seeds and report mean ± std. This is important given the modest effect sizes (1–3 pp).

3. **Clarify the initialization**: Specify the synthetic data initialization method used for single-expert baselines. If they use random initialization while multi-expert uses easy-sample initialization, either align the initialization methods or discuss the potential confound.

4. **Specify the data partitioning scheme**: State clearly whether each expert receives different samples from each class (stratified) or different classes entirely.

5. **Add a direct comparison**: Explicitly compare the "w/o DistCorr & w/o Fusion" row from Table 2 to the single-expert baseline from Table 1 in the text, to isolate the effect of simply splitting the budget.

## Score and Decision

The paper proposes a novel and well-motivated approach to a real problem in dataset distillation. The framework is clearly described, the distance correlation and mixup components are technically sound, and the evaluation spans multiple distillation methods and architectures. However, the experimental evaluation has a meaningful gap: the main comparison conflates the multi-expert structure with the use of mixup-based fusion, and the missing control (single-expert + vanilla mixup) weakens the core claim. The lack of variance estimates further limits the reliability assessment of the modest reported gains. These are addressable issues — the paper does not have fatal flaws — but they should be resolved before the contribution can be fully assessed.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>