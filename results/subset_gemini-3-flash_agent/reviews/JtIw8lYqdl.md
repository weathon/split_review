The paper investigates whether power-law scaling governs predictive uncertainty in deep learning, paralleling known scaling laws for test loss. Through extensive experiments on vision (ResNet, ViT, WideResNet) and language (GPT-2, Phi-2) tasks, the authors demonstrate that uncertainty metrics—specifically Total (TU), Aleatoric (AU), and Epistemic (EU) uncertainty—generally follow predictable decay patterns as the dataset size $N$ increases. These findings are supported by a theoretical derivation connecting generalization error in Singular Learning Theory (SLT) to uncertainty contraction in linear models.

## Strengths
- **Empirical demonstration of uncertainty scaling:** The paper provides strong empirical evidence that predictive uncertainty metrics follow power-law decay relative to dataset size $N$ across multiple modalities (vision and language) and architectures.
- **Evaluation across diverse UQ methods:** The study includes a wide range of uncertainty quantification techniques, including MC Dropout, Deep Ensembles, MCMC, and Variational Inference (IVON), showing that the scaling phenomenon is not an artifact of a specific approximation method.
- **Theoretical connections:** The paper offers a formal bridge between information-theoretic uncertainty decomposition and generalization error within the framework of SLT, providing a principled basis for the observed empirical results (Section 5).
- **OOD behavior analysis:** The authors extend their scaling analysis to out-of-distribution scenarios (CIFAR-10-C), demonstrating that while uncertainty is higher OOD, it still follows a predictable decay as the training set size increases.

## Weaknesses

### Major
- **Inconsistency in Model Size ($P$) Scaling:** While dataset size ($N$) scaling is robustly demonstrated, the evidence for model size scaling is significantly weaker. Section 4.1.1 and Figure 7 show that EU does not scale predictably with $P$ for MC Dropout and increases for IVON. The authors attribute this to parameter permutation symmetries and redundancy, but this discrepancy suggests that the title "Scaling Laws for Uncertainty" is primarily supported for $N$, not for $P$, which is a major component of standard scaling law literature.
- **Conceptual Ambiguity in Aleatoric Uncertainty (AU) Scaling:** By definition, AU represents irreducible data noise and should remain constant for a sufficiently expressive model of $p(y|x)$. The finding that AU scales with $N$ (Figures 2 and 8) implies the paper is actually measuring the *convergence of the AU estimator*. The paper does not sufficiently distinguish between the learning of the conditional distribution and the intrinsic noise of the data generating process, which muddies the conceptual definition of an AU scaling law.

### Minor
- **Lack of precision in Power Law fitting for TU/AU:** Standard scaling laws include an irreducible term $\mathcal{L}_\infty$. Since TU and AU converge to a non-zero constant (the true label noise/AU) as $N \to \infty$, fitting a simple $N^{-\gamma}$ power law on a log-log plot (as seen in Figures 1, 2, and 3) is mathematically imprecise unless the "floor" is accounted for. This likely affects the reported exponents $\gamma$.
- **Sensitivity to Optimization Trajectories:** As shown in Figure 4 and Figure 3, uncertainty scaling behavior (slopes and convergence speed) varies significantly with learning rate schedules and optimization choices (e.g., SAM). This suggests the observed exponents might be properties of specific training paths rather than fundamental constants of the model or data.
- **Speculative link to SLT for Deep Models:** While the mathematical link is rigorously derived for linear models in Section 5.2, the extension to deep over-parameterized models remains admitted by the authors as speculative. The paper does not provide a concrete bridge showing how the Real Log Canonical Threshold ($\lambda$) from SLT specifically predicts the $\gamma$ observed in the ResNet/GPT experiments.

### Trivial
- **Narrow scope for language experiments:** The GPT-2 experiment (Section 4.2.1) is limited to an algorithmic dataset and only uses MC Dropout, in contrast to the broader methodological sweep in the vision experiments.

## Nice-to-Haves
- A table comparing the scaling exponents $\gamma$ across different architectures and modalities to identify potential universal constants.
- Quantitative evaluation of extrapolation power (e.g., using 10-20% data to predict uncertainty at 100%).
- An analysis of the ratio of $\text{EU} / \text{Error}$ as a function of $N$ to investigate "Epistemic Uncertainty Collapse" and model overconfidence.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Missing related works:* (Hard Rule: External sources for citations cannot be verified).
- *Reproducibility/Hyperparameter concerns:* (Hard Rule: These are not grounds for rejection per area-of-concern sweeps).
- *Typos/Formatting:* (Hard Rule: Parser errors are not author errors).

## Novel Insights
This paper provides the first systematic empirical characterization of power-law behaviors in predictive uncertainty for deep neural networks. Its most significant insight is that the reduction in functional diversity (EU) follows a predictable trajectory relative to dataset size across diverse UQ methods. Furthermore, it identifies that while $N$ drives uncertainty down predictably, model size $P$ often adds redundancy rather than diverse hypotheses due to parameter permutation symmetries, explaining why uncertainty does not always "scale up" with model capacity in the way accuracy does.

## Suggestions
- Revise the AU scaling formulation to account for the irreducible floor (e.g., $|AU_N - AU_{true}| \propto N^{-\gamma}$) to clarify that the law governs the *estimate* convergence.
- Temper the claims regarding model size ($P$) scaling in the abstract to reflect the empirical inconsistencies observed in the results.

## Score and Decision
The paper resides in a competitive bracket of 5.5 to 7.0. It is stronger than `xGM5shdGJD` (5.2) and `ewZSzO6bts` (3.75) due to its broader experimental sweep across diverse UQ methods and architectures. Compared to `I4YU0oECtK` (6.0), which focuses on Bayesian ICL, this paper offers a more general empirical discovery for UQ that is useful for practitioners, though it shares similar issues regarding the "sudden" appearance of some theoretical links and sensitivity to optimization. It is not as polished as 8.0-level scaling law papers (`wg1PCg3CUP`, `pISLZG7ktL`) because the model size scaling is inconsistent and the conceptual distinction between AU estimator convergence and data noise is not fully resolved.

| Anchor Paper | Score | Round | Comparison |
| :--- | :--- | :--- | :--- |
| `MNGMpHxi1I` | 3.0 | 1 | Much stronger than this; the current paper has much more extensive empirical validation. |
| `xGM5shdGJD` | 5.2 | 1 | Stronger; more novel empirical discovery compared to a "guide" to existing laws. |
| `ewZSzO6bts` | 3.75 | 1 | Stronger; this paper's evidence for N-scaling is much more robust than the unified law there. |
| `I4YU0oECtK` | 6.0 | 2 | Similar; both tackle Bayesian scaling, but the current paper covers more UQ methods. |
| `pISLZG7ktL` | 8.0 | 1 | Weaker; the robotics paper has more extensive real-world validation and clearer scaling impacts. |

**Round 1 Bracket:** 4.5 to 7.5
**Round 2 Selection:** 6.0
The paper is conceptually sound and provides valuable empirical findings. The inconsistency in P-scaling is its main drawback.

Originality: High.
Importance: High for Bayesian DL and safety.
Soundness: High for N-scaling, Medium for P-scaling and theoretical bridge.
Clarity: Good.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>