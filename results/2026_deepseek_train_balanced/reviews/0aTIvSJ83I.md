## Summary

This paper proposes Agnostic-SAM, an optimization algorithm that draws inspiration from both Sharpness-Aware Minimization (SAM) and Model-Agnostic Meta-Learning (MAML). At each step, the method uses two mini-batches from the training set: one provides the primary gradient for SAM-style worst-case perturbation, while the other provides an auxiliary gradient signal that steers the perturbed model toward regions where training and validation gradients are aligned. The paper provides a gradient congruence theorem, an ablation study, and experiments spanning from-scratch classification, transfer learning, noisy-label training, and meta-learning across a range of architectures and datasets.

## Strengths

1. **Gradient congruence theorem (Theorem 2).** The paper proves that the Agnostic-SAM update preserves gradient alignment by at least a factor of 1/2 when the two gradients are already aligned, and amplifies it by at least 3/2 when they are opposed. This is a non-trivial theoretical result that goes beyond a simple heuristic combination of SAM and MAML, and it is empirically validated in Figure 1.

2. **Broad and systematic experimental campaign.** The paper evaluates Agnostic-SAM across four distinct settings (from-scratch classification, transfer learning, noisy labels, meta-learning) using multiple architectures (ResNet-18/34/50, WideResNet-28×10, PyramidNet-101, DenseNet-121, EfficientNet-B2/B3/B4) and 12 datasets ranging from small (Omniglot) to large (ImageNet). The coverage is comprehensive relative to typical optimization-method papers.

3. **Strong results on noisy-label benchmarks.** At 80% symmetric label noise on CIFAR-10, Agnostic-SAM achieves 70.02% vs. SAM's 61.69% (+8.33% absolute); Agnostic-ASAM achieves 73.25% vs. ASAM's 64.82% (+8.43%). These improvements are large, consistent across noise levels from 20% to 80%, and replicate on CIFAR-100. This is the paper's most compelling empirical contribution.

4. **Generality as a plugin.** The method improves ASAM as well as SAM, showing the gradient-correction mechanism is broadly applicable beyond the original SAM formulation (Tables 2, 5).

## Weaknesses

### Fatal

None.

### Major

1. **Empty sensitivity analysis for the method's key hyperparameters.** Lines 418–422 contain only a paragraph header ("Validation batch size |B^v| and complexity; sensitivity of perturbation radius ρ1 and ρ2") with zero content. The paper introduces two new hyperparameters (ρ1, ρ2) and a validation batch size that jointly control the method's behavior; the ablation study does not analyze their effect at all. For a method where the "two-batch" design and perturbation radii are the central novelty, this omission is a significant gap — without it, neither reviewers nor practitioners can assess how sensitive the reported results are to these choices.

2. **Overclaimed framing around distributional shift robustness.** The abstract claims Agnostic-SAM produces minima "less vulnerable to data distributional shift problems," and the conclusion states it "demonstrates enhanced robustness against data shift issues." However, no experiment tests resilience to an actual input-distribution shift (e.g., corrupted test sets, domain generalization benchmarks). The experiments cover IID classification, transfer learning (which involves a domain change between *training* sets, not a test-time shift), symmetric label noise, and meta-learning — none of which directly test the claimed property. This claim should either be substantiated with appropriate benchmarks or removed.

3. **Meta-learning comparison does not control for computational budget.** In Section 4.4, Agnostic-SAM uses two batches per update (one for training, one for validation, both from the duplicated meta-training set) while MAML and SHARP-MAML use one batch per inner-loop step. The results are mixed: +0.36% over SHARP-MAML on Mini-ImageNet 5w1s, and −0.23% *below* SHARP-MAML on Omniglot 20w1s. Without controlling for the number of gradient evaluations per step, the small positive result cannot be confidently attributed to the algorithm's mechanism rather than to additional gradient computations.

### Minor

1. **Several improvements on saturated benchmarks are within noise.** On CIFAR-10 (Table 2), Agnostic-SAM improves over SAM by +0.01% on WideResNet28×10 (96.87→96.88, with both standard deviations ~0.03) and +0.03% on DenseNet121 (91.28→91.31, where Agnostic-SAM's std of 0.707 exceeds the improvement). These results do not provide meaningful evidence of improvement.

2. **Missing baselines in Table 1.** The ImageNet/Food101 from-scratch results compare only SAM and Agnostic-SAM, omitting SGD and ASAM. Without these baselines, it is impossible to assess whether the benefit is specific to Agnostic-SAM or simply reflects a different effective perturbation radius relative to SAM.

3. **Theoretical guarantees with impractical conditions.** Theorem 2's bounds depend on quantities involving Hessian-vector products (e.g., ∇θLBv(θ̃_lv)^T H_Bt(θ_l) ∇θLBt(θ_l)) that are never computed or checked during training. The theorem therefore provides no practical guarantee about the algorithm as actually run.

4. **Momentum ablation shows β=0 (71.14%) slightly outperforms the chosen default β=0.9 (70.91%).** The paper states β "does not significantly affect model performance," which is reasonable, but the choice of β=0.9 over β=0 is not explained.

### Trivial

1. The sensitivity-analysis subsection (lines 418–422) is a header with no body text — appears to be an incomplete section.

## Nice-to-Haves

- Compare Agnostic-SAM against a control variant that uses two gradient evaluations per SAM step *without* the gradient-correction subtraction, to isolate whether improvement comes from alignment or from more gradient evaluations.
- Report wall-clock time or per-iteration computational cost, since the method doubles gradient computations per step.
- Include a corruption benchmark (e.g., CIFAR-10-C, ImageNet-C) to directly test distributional-shift robustness.
- In the meta-learning section, add a controlled experiment where baselines receive two gradient evaluations per meta-update.

## Removed Points

These points were removed from the reviewer inputs per the filtering rules. They are listed for completeness:

- **"The practical algorithm collapses the claimed agnostic principle — structural flaw"** (Harsh Critic, point 1). The paper explicitly acknowledges setting S^t = S^v = S (line 112) as a practical simplification to avoid reducing training data. The method still uses two distinct mini-batches with different computational roles. This is a framing issue, not a structural collapse. The substantive concern (overclaimed distributional-shift claims) is retained under Major #2.
- **"The cosine similarity analysis is circular"** (Harsh Critic). The analysis empirically validates Theorem 2's prediction, which is the standard role of an ablation. The fact that the method explicitly maximizes this dot product is the point being validated.
- **"No wall-clock time comparison"** moved to Nice-to-Haves — a reasonable request but not a core flaw.
- **"No comparison with WaM, ESAM, or other SAM variants"** — removed; the paper compares with SAM, ASAM, and FSAM, which are the most relevant baselines.
- **"Several improvements are marginal"** preserved under Minor #1 but calibrated to note only the truly marginal ones (CIFAR-10 saturated setting).
- Formatting/style nitpicks and speculative criticisms removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The paper itself draws the SAM–MAML connection and provides the gradient congruence theorem; these are the novel elements.

## Suggestions

1. Fill the empty sensitivity analysis before any final publication — the effects of ρ1, ρ2, and validation batch size on performance and stability must be documented.
2. Remove or substantiate the "distributional shift" claims in the abstract and conclusion unless direct experiments on test-time input distribution shift are added.
3. Add SGD and ASAM baselines to Table 1 to complete the comparison.
4. In the meta-learning section, either equalize the computational budget across methods or add a controlled experiment and discuss the discrepancy.
5. Explain the choice of β=0.9 given that β=0 performs marginally better in the ablation.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>