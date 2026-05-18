Now I have all the evidence I need. Let me produce the consolidated review.

---

## Summary

This paper introduces "Wigner kernels" — a new class of body-ordered, rotationally equivariant kernels for atomistic machine learning. The key innovation is the Wigner iteration (Eq. 4), which computes body-ordered kernels iteratively in kernel space, entirely avoiding the explicit basis expansion that causes exponential growth of the feature space in methods like ACE. The authors demonstrate state-of-the-art accuracy on the QM9 benchmark (4.3 meV test MAE for energies), systematic body-order convergence on gold clusters, and strong performance on random methane configurations and dipole moment prediction.

## Strengths

1. **Genuine algorithmic innovation.** The Wigner iteration (Eq. 4) is a fundamentally new way to compute body-ordered equivariant kernels. It eliminates the exponential scaling with body order ν that plagues feature-space models like ACE, replacing it with linear scaling in ν. The cost is also independent of the radial and chemical-element basis size, which makes the method naturally suited to multi-element datasets without bespoke truncation schemes. (Supported by Section 2.4 and the contrast with ACE's O((a_max n_max λ_max)^ν) scaling.)

2. **State-of-the-art accuracy on QM9.** On the full QM9 test set (110k training, 5 chemical elements), Wigner kernels achieve 4.3 meV test MAE (Table 1), outperforming Allegro (4.7 meV), PaiNN (5.9 meV), DimeNet++ (6.3 meV), and other equivariant neural networks. This is a striking result for a kernel method on a heavily benchmarked dataset and demonstrates that the theoretical advantages translate into practical predictive power.

3. **Systematic body-order convergence with clear evidence.** On the gold cluster dataset (Fig. 1), Wigner kernels show monotonic improvement from ν=2 through ν=6, with ν=4 already approaching ν=6 accuracy at the largest training set size. Crucially, a true ν=4 kernel substantially outperforms the squared-kernel model (which mixes orders non-systematically), directly validating that explicit body-ordering provides descriptive power that heuristic polynomial kernels cannot match.

4. **Insightful performance on challenging cases.** On random methane (Fig. 2), Wigner kernels with λ_max=3 outperform SOAP-GPR (l_max=6) and NICE (λ_max=10), and are competitive with LE-ACE (l=20 radial basis). The paper offers a well-reasoned explanation: the tensor-product structure of Wigner iterations inherently incorporates higher angular frequencies, and the multi-center ansatz provides resolution that a single-center expansion would miss.

5. **Effective handling of tensorial properties.** On QM9 dipole moments (Fig. 3), Wigner kernels avoid the saturation observed in λ‑SOAP models (Ref. 34), producing a learning curve that continues to decrease with training set size. This demonstrates the advantage of a full body-ordered equivariant kernel over the combination of linear covariant ν=2 kernels with non-linear scalar kernels used in prior SA-GPR work.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Abstract framing of scaling does not mention the λ_max^7 trade-off.** The abstract states that Wigner kernels "can be computed iteratively with a cost that is independent of the radial-chemical basis and grows only linearly with the maximum body-order considered." This is technically correct, but it omits the steep O(λ_max^7) per-iteration cost that the paper itself discusses in Section 2.4 (contrasting with O(λ_max^5) for conventional SO(3)-symmetrized products). A reader encountering only the abstract could reasonably infer the method is uniformly cheaper than existing approaches, when in fact it trades exponential scaling in ν for a steep polynomial in λ_max. The paper is honest about this trade-off in the body text, but the abstract should give readers a more balanced picture from the outset.

2. **No computational cost benchmarks.** The paper acknowledges that "inference is linear in n_train" (Section 2.4) and mentions sparse KRR as future work, but reports no wall times, memory usage, or scaling experiments. For a dataset of QM9's size (110k training points), the practical cost of full KRR inference is non-trivial. While this is a methods paper and not an engineering report, the concluding paragraph envisions use in "practical applications," making some efficiency data — even a simple timing breakdown for one or two representative cases — a reasonable expectation.

3. **Hyperparameter values and model configuration not reported.** The paper mentions cross-validation but does not list the chosen values of key hyperparameters (cutoff radius R_cut, Gaussian width σ, regularization strength α) for any of the reported experiments. Reporting these would substantially aid reproducibility and allow other researchers to build on the work.

4. **Two different fitting procedures for QM9 learning curves without validation.** The paper acknowledges a change from dual-annealing cross-validation to a 2D grid search (dashed line in Figs. 3 and 4) and asserts "the accuracy of the model does not seem to be affected by this change," but provides no quantitative comparison (e.g., both methods on the same split). Given that the SOTA claim (the last point) uses the second procedure, a consistency check on a subset would strengthen confidence that the result is not an artifact of the change.

### Trivial

None.

## Nice-to-Haves

- A brief sketch in the main text explaining why the Wigner iteration (Eq. 4) computes the same quantity as the defining integral (Eq. 3), even if the full derivation is in the appendix.
- A small experiment with higher λ_max (e.g., λ_max=6 on methane) to demonstrate the method remains feasible despite the λ_max^7 scaling, even if accuracy does not improve.
- A more extended comparison with LE-ACE on the gold cluster dataset, e.g., using the same radial transform and hyperparameter tuning for LE-ACE to disentangle the effect of the kernel-space basis.

## Removed Points

These points were raised by reviewers but are removed per the review guidelines:

- **"Derivation from Eq. 3 to Eq. 4 not given in the main text"** — The paper references Section app:implementation for supporting details; such appendix sections are stripped by the parser from all papers and exist in the original submission.
- **"Description of how ν=1 kernel integrals are computed"** — The formula is fully specified in Eq. 5 (lines 143–150); implementation details (e.g., analytic Gaussian overlap vs. quadrature) would be in the stripped appendix.
- **"Comparison with a simple message-passing NN"** — The paper already compares with Allegro, PaiNN, DimeNet++, SphereNet, ET, NoisyNodes, and others (Table 1). This request is already satisfied.
- **"Missing related works"** — Cannot be verified without external sources, per guidelines.
- **Formatting/typo criticisms** — These reflect parser artifacts, not author errors, and are excluded per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Revise the abstract to briefly acknowledge the λ_max^7 trade-off (e.g., "…with a cost that, for a given angular cutoff λ_max, scales as O(λ_max^7)"). This would provide readers an accurate picture from the start without sacrificing concision.
- Add a short table of hyperparameters (cutoff radius, Gaussian width, regularization strength) for each dataset/experiment to aid reproducibility.
- Include a brief wall-time comparison for at least one experiment (e.g., QM9 full training and inference), even if only a single configuration. This would address the practical feasibility question without requiring extensive engineering.

## Score and Decision

The paper makes a genuine and significant methodological contribution — the Wigner iteration is a novel way to compute body-ordered equivariant kernels while avoiding the exponential feature-space growth that limits existing approaches. The empirical validation is strong: SOTA results on QM9, systematic body-order convergence on gold clusters, and competitive performance on random methane. The weaknesses are all minor: an abstract that could be more balanced about the λ_max scaling, absence of timing data, unreported hyperparameters, and an unvalidated procedure change. None of these undermine the core contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>