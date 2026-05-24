Now I have all the information needed to produce the final consolidated review. Let me construct it carefully.

## Summary

The paper addresses the problem of OOD detection under long-tailed (imbalanced) in-distribution data. It proposes ImOOD, a probabilistic framework that identifies a class-aware bias term between balanced and imbalanced OOD detection, and derives a training-time regularization to correct this bias. Experiments on CIFAR10-LT, CIFAR100-LT, and ImageNet-LT show consistent improvements over baselines including PASCL and COCL, and the method generalizes across multiple OOD detection backbones (OE, Energy, Mahalanobis).

## Strengths

1. **Consistent SOTA improvement across three long-tailed benchmarks.** Tables 1 and 2 show that ImOOD + COCL achieves 93.55% AUROC on CIFAR10-LT (+0.27 over COCL), 78.50% on CIFAR100-LT, and 75.84% on ImageNet-LT (+1.97 over COCL), outperforming all prior methods. The improvements over PASCL are larger (e.g., +1.94 AUROC on CIFAR10-LT, +6.69 on ImageNet-LT). The gains are directionally consistent across all three benchmarks.

2. **Generalization to diverse OOD detection backbones.** Table 5 (exp_abl_ood_method) demonstrates that ImOOD's training regularization improves not only BinDisc but also OE (+1.61 AUROC), Energy (+1.14), and Mahalanobis-distance-based detectors (+1.04). This is a genuine advantage over prior works (e.g., PASCL, COCL) tied to specific contrastive architectures.

3. **Well-designed ablation validates the role of γ_y(x).** Table 4 (tab:abl_gamma_train) systematically ablates γ estimates: constant (89.75 AUROC) → class-dependent (92.04) → input-dependent (92.23), cleanly showing that both class- and input-dependence matter. Figure 2 (exp_stat) further visualizes the learned γ, β, and Δ distributions, confirming they behave as the intuition predicts (higher γ for head-class ID samples, etc.).

4. **Empirical diagnosis of two distinct failure modes.** Figure 1(a) provides concrete statistics on CIFAR10-LT showing that (i) ID samples from tail classes are disproportionately flagged as OOD, and (ii) OOD samples are disproportionately predicted as head-class ID. This joint characterization is more complete than prior works that focused only on tail-class confusion.

5. **Robustness across diverse OOD test scenarios.** Table 6 shows ImOOD improves over PASCL on far-OOD (+0.87 AUROC), near-OOD (+2.18), and spurious-OOD (+4.27), demonstrating the correction is not sensitive to a particular OOD distribution.

## Weaknesses

### Fatal
None.

### Major

1. **Missing standard deviations from main tables.** The paper states (line 262) that mean and standard deviation over six runs are reported, yet Tables 1, 2, and 3 contain only single numbers — no standard deviations, confidence intervals, or error bars appear anywhere in the main paper. Several gains are small (e.g., COCL+Ours vs. COCL on CIFAR10-LT: 93.55 vs. 93.28, a +0.27 AUROC difference). Without variance information, it is impossible to assess whether these gains are statistically reliable. This is the most significant evidential weakness and must be addressed for the paper to be convincing.

2. **The theoretical framing overstates what is actually derived.** The claim of a "generalized statistical framework" is inflated relative to what is delivered. The paper introduces the notation P^bal(x|y) in Lemma 1 (γ_y(x) = (1/K) · P^bal(x|y)/P(x|y)) without defining it separately — in standard probabilistic formulations, the class-conditional density P(x|y) does not change with the prior, so P^bal(x|y) = P(x|y) and γ would be 1/K (constant). The paper's key insight — that the scaling factor between P^bal(i|x) and P(i|x) depends on the class prior — does not require this distinction and can be derived more cleanly from the standard logit-adjustment relationship P^bal(y|x) ∝ P(y|x)/P(y) (Menon et al. 2021). The current framing creates unnecessary confusion. The method itself is valuable; the theory is better presented as providing intuition for why a class-aware correction is needed, not as a formal derivation from first principles.

### Minor

1. **The Δ(x) truncation is a heuristic patch.** The paper truncates Δ(x) to be non-negative for ID samples and non-positive for OOD samples (line 229) to "alleviate optimization difficulty." While this is a reasonable engineering choice, it is not derived from the theory. This weakens the claim that the loss is theoretically grounded rather than empirically motivated. The paper would benefit from acknowledging this more explicitly.

2. **Ablation shows γ = 1/K hurts performance, which is not discussed.** Table 4 shows that setting γ to the theoretically-derived constant (1/K) produces worse AUROC (89.75) than using no γ at all (90.06). The paper mentions this briefly but does not discuss why the "theoretically correct" constant setting underperforms even the baseline. This gap between the idealized theory and empirical reality deserves commentary.

3. **Inference-time application section is exploratory and acknowledges its own limitations.** Section 4.4 shows marginal gains (90.06→90.86 AUROC) and concedes that estimating γ without training is difficult. This section does not detract from the main contribution but also does not add much. It could be shortened or moved to the appendix.

### Trivial
None.

## Nice-to-Haves
- A discussion of how much the learned γ network affects training stability and runtime compared to baselines.
- An ablation on the effect of auxiliary OOD dataset quality (e.g., TinyImages80M), since the method relies on such data.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"COCL numbers differ from original paper"** (Harsh Critic): The critic claims COCL was reported as 93.77% in the original paper vs. 93.28% here. Without access to the cited paper to verify the exact setting, and given that different random seeds, data splits, or augmentation choices produce small numerical differences, this is not a verifiable weakness. The paper follows the same evaluation protocol as prior work in this line (Wang et al. 2022, Miao et al. 2023). Removed per the rule about not questioning cited references.

- **"The proposed correction is purely heuristic"** (Harsh Critic, partial): The core Δ(x) derivation from Eq. 6 to Eq. 7 is algebraically sound. The truncation is a practical choice common in deep learning. The critic's framing that "if the theory were correct, such clipping would not be needed" is speculation. Demoted to Minor (point 1 above) rather than left as a structural indictment.

- **"The γ ablation contradicts the theory"** (Harsh Critic): The critic claims the ablation showing γ=1/K hurts performance "directly contradicts the theoretical claim that γ should be 1/K under balanced conditions." But the paper's theory states γ = 1/K under *balanced* data; on imbalanced data (which is what is tested), γ is not expected to be 1/K. The ablation is actually consistent with the paper's narrative. Retained as Minor point 2 above but in corrected framing.

- **"Inference-time section is weak"** (Harsh Critic): The paper itself acknowledges this is an exploratory attempt. This is not a weakness of the core contribution. Moved to Minor for completeness.

- **Strength: "Inference-time applicability"** (Strength Finder): Table 7 shows a gain of 90.06→90.86, but the paper acknowledges this is limited. This is not a core strength. Removed.

- **Strength: "Theoretical identification of a class-aware bias term"** (Strength Finder): Partially retained in the strengths as it supports the intuition, but qualified in weaknesses since the formalism is sloppy.

## Novel Insights
The most interesting observation emerging from the reviews is the disconnect between the paper's theoretical framing and its empirical method. The harsh critic correctly identifies that the distinction between P^bal(x|y) and P(x|y) is not formally justified — but the ablation study (Table 4) simultaneously shows that a learned, input-dependent γ_y(x) substantially outperforms a constant γ = 1/K. This creates an informative tension: the paper's theory cannot rigorously derive γ's class/input dependence, yet the empirical evidence strongly suggests such dependence exists and matters. Rather than a weakness being papered over, this is a genuine discovery that the paper under-exploits. The fact that the learned γ behaves differently on head vs. tail classes (Figure 2) and that this correlates with improved performance is a solid empirical finding that stands independently of the contested formalism. The paper would be stronger if it leaned into this finding directly rather than wrapping it in a derivation that doesn't quite hold.

## Suggestions
1. Add standard deviations (±) to all main tables. If some numbers are in an appendix, move key ones to the main paper. At minimum, show error bars for the key comparisons (ImOOD vs. COCL) to establish statistical significance.
2. Re-frame the theoretical contribution: present it as an intuitive motivation explaining why a class-prior-aware correction is needed, rather than a formal derived framework. Remove the undefined P^bal(x|y) notation and replace with the standard logit-adjustment relation P^bal(y|x) ∝ P(y|x)/P(y), which is cleaner and sufficient.
3. Discuss why γ = 1/K underperforms the no-γ baseline in the ablation — this is informative about how the idealized theory breaks down in practice and would strengthen the paper's empirical contribution.
4. Clarify that the Δ(x) truncation is a practical optimization choice and not derived from the theory.

## Score and Decision

Assessment by specific axes:
- **Originality:** Good. The problem formulation (joint head/tail failure modes) and the proposed correction are novel relative to prior work that only focused on tail-class confusion.
- **Importance of research question:** High. OOD detection under realistic imbalanced distributions is practically important and under-studied.
- **Claims supported:** Partially. The empirical claims are broadly supported by consistent results, but missing standard deviations weaken the small-margin comparisons. The theoretical claim is overstated relative to what is actually delivered.
- **Soundness of experiments:** Solid experimental design with comprehensive benchmarks, ablations, and generalization tests. Main weakness is missing variance reporting.
- **Clarity of writing:** Good overall, though the theoretical section could be much clearer.
- **Value to community:** Positive. The method is practical, general, and shows consistent gains. The formulation of the problem (two-sided failure) is useful framing.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>