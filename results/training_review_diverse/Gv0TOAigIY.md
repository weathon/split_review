I have all the paper content from my initial read. Let me now synthesize the final review.

I have thoroughly verified each reviewer claim against the paper text. Let me now produce the consolidated review.

---

## Summary

This paper studies how discrete reflection symmetries in neural network loss functions cause models to get trapped in low-capacity states (collapses), and proposes *syre* — a simple technique of adding a fixed random bias to the parameters together with standard weight decay — that provably removes all such symmetries without needing any knowledge of their structure. The paper provides theoretical guarantees (symmetry removal with probability 1, quantitative bounds on breaking strength), validates the method on a controlled symmetry benchmark, and demonstrates improved performance across posterior collapse in VAEs, self-supervised learning, and continual learning.

## Strengths

1. **Rigorous theoretical connection between symmetries and capacity loss.** Propositions 1 and 2 (Section 4) formally prove that reflection symmetries cause the neural tangent kernel to be masked by a projection matrix and force the model into a strictly lower-dimensional effective parameter space throughout training. This provides a principled foundation for why symmetries lead to collapses.

2. **Simple, theoretically grounded method with provable guarantees.** Theorem 1 (Section 5.1) proves that adding a single random static bias (Gaussian) with weight decay removes *all* finite reflection symmetries from the loss with probability 1, without requiring any knowledge of the symmetry structure. This is a remarkably clean result — a one-line code change suffices. Theorems 2–4 extend this to infinite symmetry groups and general finite groups, with quantitative bounds on breaking strength.

3. **Controlled benchmark directly measuring symmetry control.** Figure 3 (Section 6.2) shows that *syre* is the only method among vanilla training, weight decay, dropout, and W-fix that smoothly interpolates between low-symmetry and well-optimized solutions for both structured and unstructured symmetry spectra. This directly validates the claimed mechanism.

4. **Demonstrated effectiveness across diverse collapse-prone settings.** The method improves performance in posterior collapse in VAEs (Section 6.4), removes low-rankness in SSL projection heads recovering ~50% of the representation gap (Table 1, Section 6.5), and maintains rank and accuracy in continual learning for both supervised and reinforcement learning settings (Section 6.6).

5. **Compatibility with standard training.** The ResNet18/CIFAR-10 experiment (Figure 2, mid) shows that for small bias ($\sigma_0<0.2$), *syre* matches vanilla performance, confirming the method does not degrade standard training while providing symmetry removal when needed.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental evidence does not fully isolate symmetry removal as the causal mechanism.** The controlled benchmark (Figure 3) directly measures symmetry degree, but the real-world experiments (VAE, SSL, continual learning) rely on rank of representations or test accuracy as proxies. These metrics could also improve because *syre* acts as a shifted L2 regularizer rather than specifically breaking symmetries. The paper would benefit from at least one realistic experiment that measures a *direct* indicator of symmetry (e.g., gradient asymmetry from Theorem 5, $\Delta = \Omega(\gamma\sigma_0)$) and shows it correlates with performance gains beyond what a simple L2 shift would produce. This would tighten the causal narrative considerably.

### Minor

2. **Assumption 1 (countably many linearized symmetries) is stated but not verified.** The paper asserts Assumption 1 "is satisfied by common neural networks with standard activations" (line 122) and provides a footnote about pathological linear objectives that violate it. However, no verification, proof sketch, or argument is given for why the specific losses (cross-entropy, MSE) and activations (ReLU, SiLU, tanh) used in the experiments actually satisfy this assumption. While the assumption is plausible, the theoretical guarantee of Theorem 1 is not fully grounded for the paper's own experimental setups.

3. **Advanced removal method (ℓ_ar, Eq. 4) for infinite symmetries is proposed but not evaluated.** The paper motivates the advanced method for rotation and double-rotation symmetries but states "we always set σ_D = 0 as we find only introducing σ_0 to be sufficient for most tasks" (line 223). This is an empirical claim without theoretical justification — the SSL experiment (Section 6.5) involves rotation symmetry yet uses only the simple *syre*. Evaluating the advanced method on a synthetic rotation-symmetric objective, or at least explaining why the simpler method handles these cases, would strengthen the paper.

4. **Some figures lack error bars or confidence intervals.** The input dimension experiment (Figure 2, line 217) validates a theoretical prediction but shows single trajectories without variance estimates. The benchmark (Figure 3) does not report run-to-run variability either. Given stochastic initialization and data sampling, showing variance would strengthen confidence.

5. **Margin over weight decay alone in the RL continual learning experiment.** In Figure 4 (right), the return curves for *syre* and weight decay are reported to overlap at many points. The paper notes "Each trajectory is averaged over 5 different random seeds" but does not discuss statistical significance of the difference. Given that weight decay alone also substantially helps, it is unclear whether the additional improvement from *syre* is significant.

### Trivial
None beyond those listed above.

## Nice-to-Haves

- **Ablation of weight decay.** The paper claims weight decay is essential (line 133: "using a static bias along with weight decay is essential"). The VAE experiment (Figure 7) partially addresses this by showing reconstruction with and without weight decay, but a dedicated controlled experiment directly comparing *syre* with and without weight decay (same bias, same setting) would cleanly verify the theoretical claim.
- **Sensitivity analysis of σ₀.** The paper recommends $\sigma_0 = 0.01/\sqrt{d}$ and shows some robustness (SSL with $\sigma_0=0.1$ and $0.01$), but a more systematic sweep across tasks would provide practical guidance on the trade-off encoded in Theorem 5.
- **Discussion of alternative capacity-control methods.** Spectral regularization and orthogonal regularization also control model capacity — a brief discussion of why these are not substitutes (e.g., they require knowledge of the symmetry) would clarify the paper's contribution.

## Removed Points

- **"Notation inconsistency between ℓ_r and ℓ_ar, Section 4.3 refers to both as syre."** — REMOVED as factually wrong. The paper clearly defines *syre* as Eq. (3) (ℓ_r) only (line 133). Section 4.3 says "two ways to implement **the method**" (not "syre"), and explicitly states "we stick to the definition of Eq. (3)" (line 223). The notation is consistent throughout.
- **"The paper should discuss or test whether syre works through a mechanism other than symmetry breaking"** as a weakness. — This is a reasonable suggestion but more of a nice-to-have than a weakness. The benchmark (Figure 3) directly validates the symmetry-control mechanism, and the theory provides the link. Moved to the spirit of Nice-to-Haves above.
- **"Missing baseline: spectral regularization"** cast as a weakness. — This is a discussion suggestion, not a weakness of the paper's method. Moved to Nice-to-Haves.
- **"Ablation of weight decay"** as a required experiment. — The VAE experiment (Figure 7) actually compares syre with and without weight decay ("Left: No weight decay. Right: γ=1000"), partially addressing this. Moved to Nice-to-Haves for a more controlled version.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves have not already identified.

## Suggestions

1. **Add a direct symmetry measurement in a realistic setting.** In the VAE or SSL experiment, compute $\Delta$ from Theorem 5 (the loss asymmetry under reflection) for suspected symmetries (e.g., per-neuron sign flips) and show it decreases under *syre* compared to vanilla training. This would directly connect the theoretical mechanism to the observed performance gains.

2. **Provide a brief justification of Assumption 1 for the experimental setups.** Even a paragraph explaining why the ReLU/SiLU networks with cross-entropy/MSE losses used in the experiments satisfy the assumption would significantly improve the paper's theoretical grounding.

3. **Include variance estimates** for the input dimension experiment (Figure 2) and the benchmark (Figure 3) by running multiple random seeds.

4. **Dedicate a small experiment to the advanced removal method** (ℓ_ar) on a synthetic rotation-symmetric objective to demonstrate its behavior, or provide a theoretical argument why the simple *syre* suffices for the rotation symmetries in the SSL setting.

## Score and Decision

**Originality:** High. The idea of using a static random bias to break symmetries is simple, novel, and not obvious.

**Importance:** High. The paper addresses a fundamental problem (symmetry-induced capacity loss) that manifests across many deep learning settings.

**Claims:** Generally well-supported, with the caveat that the causal chain from symmetry removal to performance gains is not perfectly isolated in real-world experiments.

**Soundness:** The theory is sound given its assumptions; the experiments are consistent with the theory but could be strengthened with direct symmetry measurements.

**Clarity:** Well-written and well-organized.

**Value to community:** High — the proposed method is simple, model-agnostic, and theoretically grounded, making it easy to adopt and hard to misuse.

**Overall:** This is a strong paper with a clean theoretical contribution, a practical method, and broad empirical validation. The main weakness is that the real-world experiments do not fully isolate symmetry removal as the causal mechanism, and Assumption 1 is not verified for the experimental setups. These are significant but not fatal — they can be addressed with additional analysis and clarification. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>