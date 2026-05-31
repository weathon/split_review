## Summary

The paper introduces **Ano** (A New Optimizer), which decouples direction and magnitude in gradient updates: the sign of the EMA momentum vector provides directional stability, while the instantaneous gradient norm provides reactive magnitude. A modified Yogi second-moment estimator with explicit β₂-decay controls variance memory. The paper also proposes **Anolog**, which replaces the fixed momentum coefficient with a logarithmic schedule to remove the need to tune β₁. Non-convex convergence at O(K^{-1/4}) is established under standard assumptions, and empirical results are reported across RL (SAC/MuJoCo, PPO/Atari), CV (CIFAR-100), and NLP (GLUE/BERT).

---

## Strengths

- **Principled design with clear motivation.** The direction–magnitude split is well-motivated by Balles & Hennig (2018)'s insight that momentum sign captures most directional information, while instantaneous gradient norm provides reactive scaling. The resulting update has a natural SNR-like interpretation: large-step when the current gradient is strong relative to the running variance.
- **Strong, consistent RL results.** Across five MuJoCo tasks (SAC, 1M steps, 10 seeds), Ano achieves ~10% higher normalized score than Adam under both default and tuned settings, ranking first in 4/5 and 3/5 tasks. On Atari-5 (PPO, 10M steps), Ano obtains a 95.99 normalized average versus 87.54 for Adam and 90.09 for RMSprop. These gains are consistent across environments and seeds, which is exactly the intended use case.
- **Honest, asymmetric framing of claims.** The paper explicitly labels CV/NLP experiments as "diagnostic checks" rather than claiming state-of-the-art, and openly attributes Ano's limitations in stationary settings to its design favoritism toward larger steps. This epistemic transparency strengthens credibility.
- **Ablation study is systematic.** Table 6 isolates the contribution of each component across both RL and supervised domains, confirming that the gradient-norm scaling and the β₂-decay Yogi modification each contribute positively in DRL, while neither degrades supervised performance significantly.
- **Hyperparameter robustness.** Figure 3 shows that Ano maintains near-optimal performance over a wider range of learning rates and betas on HalfCheetah than Adam, which is practically significant in RL where tuning budgets are often small.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theory–practice mismatch.** The convergence proof (Section 5.1) uses both β_{1,k} = 1 − 1/√k and η_k = η/k^{3/4}, but the practical default uses a fixed β₁ = 0.92 and the Anolog variant uses β_{1,k} = 1 − 1/log(k+2). No convergence analysis is provided for the logarithmic schedule or the constant-β₁ case. The theoretical guarantees therefore do not directly validate the recommended practical algorithm.

2. **O(K^{-1/4}) convergence is confirmed slower than Adam.** The paper acknowledges this openly, attributing it to the sign-based structure. However, the theoretical step-size schedule η_k = O(k^{-3/4}) is far more aggressive than what is used in practice, and the paper does not address whether an optimally-tuned step schedule could close this gap. For a method claiming to be "competitive" in supervised settings, the gap between its theoretically motivated schedule and Adam's O(K^{-1/2}) rate deserves deeper discussion.

3. **YogiSignum catastrophic failure is unexplained.** In the ablation (Table 6), YogiSignum (Yogi + β₂-decay second moment, sign-direction, sign-magnitude) achieves −285 in DRL with near-chance accuracy in supervised tasks. This complete collapse is a concerning edge case of the algorithm family and suggests potential numerical instability when combining Yogi-style second moments with pure sign magnitude. The paper notes the failure but provides no explanation or guards against it.

### Minor

1. **Scale of experiments.** CV experiments stop at CIFAR-100/ResNet-34 and NLP at BERT-base fine-tuning. The paper's framing is honest about this limitation, but it prevents drawing conclusions about whether Ano's benefits extend to non-stationary behaviors that also appear in large-scale pretraining (e.g., loss spikes in LLM training).

2. **Table 3 (GLUE) has two rows both labeled "Adam"** in both the default and tuned sections, making it impossible to tell which baseline is actually compared. One row is presumably AdamW, but this is unclear.

3. **Figure 3's x-axis label says "beta" but shows values {1e-05, 1e-04, 1e-03}**, which are learning rate values, not β values. The axis labeling is inconsistent with the described sensitivity study.

4. **RMSprop unexpectedly competitive in Atari.** RMSprop achieves a mean rank of 2.4 vs Ano's 2.2, and outperforms Ano in Phoenix and DoubleDunk. Since RMSprop has no momentum (or β₁ = 0 equivalent), this baseline is informative and somewhat underanalyzed relative to the paper's motivation.

### Trivial

- β₁ = 0.92 is unusual (vs typical 0.9 or 0.95) and left unexplained beyond "stable convergence."

---

## Nice-to-Haves

- A convergence proof for the fixed-β₁ case and/or the logarithmic schedule (Anolog) would close the theory–practice gap.
- A brief analysis or safeguard for the YogiSignum failure mode would strengthen the ablation narrative.
- A wall-clock comparison would clarify whether "fewer steps" in Figure 2 translates to actual speedup, given any per-step overhead from the modified update.

---

## Novel Insights

Ano's core novelty is the observation that decoupling the *direction* from the *magnitude* of adaptive updates, rather than both being momentum-derived, improves robustness in high-variance settings. Specifically, using sign(m_k) for direction retains the variance-reduction benefit of momentum while using |g_k| for magnitude retains reactivity to current signal strength. This is complementary to Grams (which uses gradient sign + momentum norm) and Lion (which uses pure sign updates), occupying a distinct point in the design space. The modified Yogi second-moment estimator that introduces explicit forgetting via β₂-decay provides further control over variance memory, and the ablation confirms this modification alone yields ~16% DRL improvement over standard Yogi. Together, these design choices constitute a principled, empirically validated strategy for building optimizers that are specifically robust to non-stationarity and high-gradient-variance regimes.

---

## Suggestions

- Provide convergence analysis under a constant or logarithmic β₁ schedule, or clearly state that the current bounds are only for Anolog-sqrt and leave the gap for future work.
- Investigate and explain the YogiSignum collapse in the ablation; determine whether it can occur for intermediate design choices and what hyperparameter range is safe.
- Correct the ambiguous "Adam" duplicate rows in Table 3 and fix the axis label in Figure 3.
- Evaluate on at least one non-stationary supervised setting (e.g., continual learning or online learning), which would bridge the gap between RL claims and supervised claims without requiring ImageNet-scale compute.

---

## Score and Decision

Ano presents a principled and well-executed optimizer paper. The core design idea is original, the RL results are consistently strong, the paper is honest about its scope, and the ablation study adequately supports the design choices. The weaknesses—primarily the theory–practice mismatch, worse theoretical convergence rate, and limited supervised-learning scale—are real but do not invalidate the main claims. The paper targets the right niche and delivers convincing results within it. This clears the bar for a borderline accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>