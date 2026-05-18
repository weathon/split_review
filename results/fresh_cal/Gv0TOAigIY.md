Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes *syre*, a simple method that adds a random static bias to model parameters combined with weight decay, to provably remove reflection symmetries from loss functions and thereby prevent capacity collapse during training. The paper provides theoretical analysis showing that (a) symmetries cause feature masking and effective dimension reduction, and (b) a static bias + weight decay eliminates almost all reflection symmetries without knowledge of their structure. Empirical validation spans supervised learning, self-supervised learning, VAEs, and continual/RL settings.

## Strengths

- **Provable removal of all reflection symmetries with a simple modification (Theorem 1):** Adding a static Gaussian bias and weight decay removes every reflection symmetry with probability 1, without requiring any knowledge of the symmetries. This is the paper's central theoretical contribution and is rigorously stated.

- **Theoretical characterization of how symmetries impair capacity (Propositions 1, 2):** The paper formally proves that reflection symmetries cause feature masking (Eq. 5) and effective parameter dimension reduction (Eq. 6), going beyond prior descriptive work to give explicit mechanisms linking symmetries to collapsed states.

- **Quantified escape gradient at symmetric points (Corollary 1):** After applying syre, the gradient component in the symmetry-broken subspace is at least Ω(γσ₀), ensuring that symmetric points are no longer stationary and the model is actively repelled from low-capacity states. This is a stronger guarantee than simple symmetry removal.

- **Model- and symmetry-agnostic design:** The method requires no architectural changes and no enumeration of symmetries, in contrast to the prior W-fix heuristic (Lim et al., 2024) which only handles permutation symmetries in fully connected layers.

- **Broad empirical validation:** The paper demonstrates syre's effectiveness across reparametrized linear regression (avoiding neuron collapse), VAEs (mitigating posterior collapse), SSL (removing low-rankness in projection head), continual learning (preserving rank and accuracy), and RL (outperforming weight decay alone). The benchmark experiment (Fig. 3) provides clean controlled evidence that syre uniquely interpolates between optimization quality and symmetry degree.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient weight-decay-only baselines in key experiments:** The reparametrized linear regression and VAE experiments compare syre (+ weight decay) to a "vanilla" baseline without clarifying whether vanilla includes weight decay. For the reparametrized regression (Fig. 3 right caption), "training with vanilla SGD... does not fix the problem" — if vanilla SGD does not use weight decay, the comparison conflates the effect of the bias with the effect of weight decay. For the VAE (Figs. 5–7), the comparison is vanilla (no weight decay, no syre) vs. syre+WD, with no weight-decay-only arm. This makes it difficult to attribute the observed improvement specifically to the bias component rather than to weight decay, which is known to regularize these settings. This is partially mitigated by the benchmark experiment (Fig. 3, which includes weight-decay-only) and the RL experiment (Fig. 8, which compares PPO+WD vs. PPO+syre with matched WD), but the gap remains for two of the main application experiments.

- **Theory-experiment gap for continuous symmetries:** Theorem 2 explicitly states that for uncountably many symmetries (e.g., rotation), the basic method (σ_D=0) is insufficient and one must use ℓ_ar with distinct diagonal D. However, the SSL experiment (Table 1) involves rotation symmetry of the projection head (acknowledged by the paper as "rotation symmetry of the last weight matrix in the SimCLR loss") yet applies the basic method with σ_D=0. The paper asserts "we find only introducing σ_0 to be sufficient for most tasks" (Section 5.4) without presenting controlled evidence or a theoretical justification for why the basic method suffices in this continuous-symmetry case. This creates a logical inconsistency: the theory says the basic method does not guarantee removal, but the experiments rely on it working anyway.

### Minor

- **"Super-Lipschitz" used informally:** Theorem 4's discussion invokes "super-Lipschitz" as a descriptive term without definition. The quantitative claim (Δ = Ω(γσ₀)) is clear, but the informal framing could mislead.

- **Incomplete statistical reporting:** The number of seeds and variance are reported for some experiments (ResNet: 10 trials; RL: 5 seeds) but not for others (VAE rank plot, reparametrized regression). Adding seed counts and error bars to all main figures would strengthen reliability claims.

### Trivial
None.

## Nice-to-Haves

- In the SSL experiment, applying the advanced method (ℓ_ar with σ_D>0) to the projection head and comparing with the basic method would directly test whether the advanced method yields additional gains for continuous symmetries, and would close the theory-experiment gap.
- A brief ablation exploring the joint effect of σ₀ and γ (beyond Theorem 4's scaling prediction) would help practitioners tune both hyperparameters.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Reparametrized linear regression as "continuous rescale symmetry":** The harsh critic claimed this involves a continuous rescale symmetry for which Theorem 1's guarantee does not apply. However, the relevant symmetry that creates the (u_i,w_i)=(0,0) collapse is the *discrete* reflection symmetry (u_i,w_i)→(-u_i,-w_i) (a Z₂ subgroup of the rescaling). Theorem 1 applies to this reflection symmetry. The full continuous rescaling is a separate symmetry; the paper's claims about reflection-symmetry removal are not invalidated by its presence. **Justification:** The criticism misidentifies which symmetry causes the collapse; the discrete reflection symmetry is sufficient to create the trap that syre removes.

- **"No methods known to enable full escape" overstated:** The harsh critic suggested this claim is too strong given W-fix. However, the paper qualifies the claim with "full escape" and later discusses W-fix's limitations (only permutation symmetries in fully connected layers). The claim is appropriately scoped. **Justification:** The paper's discussion of W-fix acknowledges it exists, and the claim is qualified by "provably" and "full."

- **Worst-case scaling of N in Theorem 5:** The harsh critic noted this is worst-case and may not apply in practice. The paper openly discusses this ("in general, without further assumptions there is no way to improve this scaling") and provides a heuristic justification. This is a technical discussion point, not a weakness. **Justification:** The paper is transparent about the worst-case nature of the bound.

- **Missing weight decay ablation for the 4-layer FCN experiment:** The critic grouped this with the VAE/reparametrized regression issues, but the 4-layer FCN experiment (Fig. 4) varies γ directly and compares vanilla (with matching γ) to syre, which effectively tests the bias contribution. **Justification:** This experiment does use weight decay in the vanilla baseline (the x-axis is γ), making the comparison fair.

## Novel Insights

The reviews surface a tension that the paper itself partly acknowledges but does not fully resolve: the theoretical guarantees of the basic method are limited to countable reflection symmetries, yet the method is applied to problems with continuous symmetries (SSL rotation symmetry) where only an empirical claim supports its efficacy. This gap suggests that either (a) the practical symmetry-breaking strength of the bias (Theorem 4's Ω(γσ₀) gradient) is sufficient even without the formal guarantee, or (b) the continuous symmetry is only approximately present and the residual discrete structure is what matters. The paper would benefit from explicitly acknowledging and testing these possibilities rather than relying on the blanket empirical statement that σ_D=0 is "sufficient for most tasks." Additionally, while the weight-decay ablation gap in the VAE and reparametrized regression experiments is real, the benchmark and RL experiments already provide credible evidence that the bias contributes beyond weight decay alone — the paper simply needs to extend those controls to the remaining experiments.

## Suggestions

1. **Add weight-decay-only baselines** to the reparametrized linear regression and VAE experiments, at the same γ used in syre. This is the single most impactful addition to cleanly establish that the bias component is the active ingredient.
2. **Apply the advanced method (ℓ_ar with σ_D>0) to the SSL projection head** and compare with the basic method (σ_D=0). If results are similar, add a discussion explaining why the basic method suffices empirically despite the theoretical gap for continuous symmetries. If the advanced method performs better, the theory is validated and the basic method's use should be qualified.
3. **Formally define "super-Lipschitz"** or replace it with a more precise description of Theorem 4's result.
4. **Report seed counts and variance** consistently across all main experimental figures.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>