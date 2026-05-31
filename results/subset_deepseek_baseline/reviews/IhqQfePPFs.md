## Summary

This paper proposes an unsupervised framework for deformable 3D shape matching that combines a dual-layer attention mechanism for feature extraction, a hybrid spectral space using both Laplace-Beltrami and elastic eigenmodes, and Sinkhorn optimal transport for post-processing. The method aims to improve robustness under complex geometric deformations by learning more discriminative descriptors and leveraging complementary spectral representations. Experiments on near-isometric (FAUST, SCAPE, SHREC'19), non-isometric (SMAL), and topologically noisy (TOPKIDS) datasets show competitive or state-of-the-art performance.

## Strengths

- **Comprehensive experimental evaluation**: The paper evaluates on multiple challenging benchmarks covering near-isometric, non-isometric, and topologically noisy scenarios, with thorough comparisons against a wide range of baselines including axiomatic, supervised, and unsupervised methods.
- **Novel combination of existing components**: The integration of dual-attention feature extraction, hybrid spectral bases (LBO + elastic), and Sinkhorn optimal transport into a unified unsupervised framework is a reasonable design choice that addresses known limitations of prior work.
- **Competitive results on challenging benchmarks**: The method achieves strong performance, particularly on the SMAL dataset (4.3 geo. error) and TOPKIDS (4.9 geo. error), demonstrating robustness to non-isometric deformations and topological noise.
- **Ablation studies**: The paper includes ablation experiments on the SMAL dataset that validate the contribution of each key component (spectral mixture space, attention, optimal transport).

## Weaknesses

### Fatal
None.

### Major
- **Inconsistent and potentially misleading results in Table 1**: Several entries in Table 1 show suspiciously poor performance for the proposed method. For example, when trained on FAUST and tested on SCAPE, the method achieves 8.5 (worse than many baselines), and when trained on SCAPE and tested on FAUST, it achieves 10.0 (far worse than almost all unsupervised methods). These results are not discussed or explained in the text, and they contradict the claim of "substantial improvements." The paper selectively highlights only the best results (e.g., 1.4 on FAUST→FAUST) while glossing over these failures.
- **Missing standard deviations and statistical significance**: No error bars, confidence intervals, or standard deviations are reported for any experimental results. Given the variability in shape matching, this makes it impossible to assess whether improvements are statistically significant.
- **Unclear training details and hyperparameters**: The paper does not specify key training details such as the number of training iterations, learning rate, batch size, optimizer, or the annealing schedule for α in the loss function. The ablation study uses "one epoch" of training, but the main results do not specify training duration.
- **Limited novelty in components**: The dual-attention mechanism appears to be a straightforward combination of DiffusionNet, channel attention, and cross-attention (Predator-style), all of which are existing techniques. The hybrid spectral space is directly adopted from Bastian et al. (2024). The Sinkhorn post-processing is similar to Le et al. (2024). The paper's main contribution is the integration of these components rather than any fundamentally new algorithmic insight.

### Minor
- **Incomplete ablation study**: The ablation only evaluates on SMAL and only reports results after one epoch of training. It would be stronger to show ablations on multiple datasets and with full training.
- **Missing runtime/computational cost analysis**: The paper does not discuss the computational overhead of the dual-attention mechanism, hybrid spectral space, or Sinkhorn optimization compared to baselines.
- **Figure quality**: Figure 1 is difficult to read due to small font size and dense information. The qualitative results in Figures 2 and 5 would benefit from higher resolution and clearer annotations.

### Trivial
- The paper uses "Sinkhorn" and "Sinkhorn" inconsistently (should be "Sinkhorn").
- Some references appear to have formatting issues (e.g., "Roufousse et al." vs "Roufosse et al.").

## Nice-to-Haves

- Analysis of failure cases: When and why does the method perform poorly (e.g., SCAPE→FAUST with 10.0 error)?
- Comparison on additional non-human datasets (e.g., DT4D, TOSCA) to demonstrate generalizability beyond human and quadruped shapes.
- Investigation of the sensitivity to the number of eigenfunctions (k) and the annealing schedule.

## Novel Insights

None beyond the paper's own contributions. The paper demonstrates that combining existing techniques (attention-based features, hybrid spectral bases, Sinkhorn OT) in an unsupervised framework yields competitive results, but does not provide new theoretical understanding or surprising empirical findings that would fundamentally change how the community thinks about shape matching.

## Suggestions

- **Address the inconsistent results**: Provide a clear explanation for why the method performs poorly in certain cross-dataset settings (e.g., SCAPE→FAUST, FAUST→SCAPE). If these are due to specific failure modes, discuss them honestly. If they are artifacts of the evaluation protocol, clarify this.
- **Add statistical significance**: Report results over multiple runs with standard deviations or at minimum show error bars on the PCK curves.
- **Provide complete training details**: Include all hyperparameters, training schedules, and implementation specifics to ensure reproducibility.
- **Strengthen the ablation**: Run ablations on at least two datasets (e.g., FAUST and SMAL) with full training, not just one epoch.
- **Clarify the novelty**: Explicitly state which components are novel contributions versus adaptations of existing work, and what specific design choices were made to integrate them.

## Score and Decision

The paper presents a reasonable engineering contribution by combining existing techniques into an unsupervised shape matching framework with competitive results on several benchmarks. However, the inconsistent results in Table 1 (particularly the poor cross-dataset performance) are a major concern that is not addressed, and the lack of statistical significance reporting weakens the claims. The novelty is limited to the integration of known components. Given these issues, the paper is at the borderline of acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>