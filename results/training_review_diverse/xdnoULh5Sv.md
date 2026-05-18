Now I have a thorough understanding of the paper and all claims. Let me write the final consolidated review.

## Summary

This paper proposes CARSO, a defence method that blends adversarial training and purification by conditioning a VAE-based purifier on the internal (layerwise) representations of an adversarially-trained classifier. At inference time, multiple purified reconstructions are sampled and classified, and their outputs are aggregated via a custom robust aggregation function. The method is evaluated on CIFAR-10, CIFAR-100, and TinyImageNet-200 under $\ell_\infty$ AutoAttack (randAA for stochastic defences), reporting robust accuracy improvements over the base classifier (+8.4%, +27.47%, +22.26% respectively) and surpassing published state-of-the-art adversarial training and purification results.

## Strengths

- **Novel synergistic architecture design.** CARSO is — to the best of the reviewers' knowledge — the first method to condition a generative purifier on the *internal representations* of the adversarially-trained classifier itself, rather than stacking a purifier before a classifier. The first-principles motivation (Section 4.2) that the layerwise activation trace is a richer characterisation of the perturbation than the input alone is conceptually sound and distinct from prior work.

- **Consistent and substantial robust accuracy improvements across three datasets.** The improvements over the base classifier are large and consistent: +8.4% (CIFAR-10), +27.47% (CIFAR-100), +22.26% (TinyImageNet-200) under randAA (Table 2). On CIFAR-10, CARSO (using a 3× smaller classifier) surpasses the best AT-only model (76.13% vs. 71.07%). These results support the paper's central claim that the approach is effective.

- **Careful design to avoid gradient obfuscation.** The paper deliberately chooses a conditional VAE as the purifier because it is exactly differentiable end-to-end (Section 4.1), avoiding the robustness-evaluation pitfalls of diffusion-based purification. The authors verify the absence of gradient obfuscation via the standard high-epsilon test (Table 3, Section 5.2), where accuracy drops below random chance at $\epsilon=0.95$. This methodological care strengthens confidence in the evaluation.

- **Detailed engineering and reproducible specification.** The paper provides thorough architectural descriptions (Appendix A), hyperparameters (Appendix A.2), training schedules, and the exact list of 26 classifier layers used as conditioning (Table 5). The adversarially-balanced batch composition, hierarchical encoding, and robust aggregation strategy are each motivated with preliminary experiments (Appendix C) or heuristic justification (Appendix D). The computational cost is also reported (2–3.5 hours on multi-GPU setups).

- **Architecture-agnostic framing.** The paper correctly notes that the VAE is a choice driven by evaluation transparency, and that the CARSO framework is compatible with any conditional generative model. This positions the contribution as a general recipe rather than a one-off architecture (Section 4.1, Section 6).

## Weaknesses

### Fatal

None.

### Major

- **Missing control baseline for the ensemble effect.** CARSO uses 8 reconstructed samples with a custom aggregation function. The reported gains conflate two effects: (1) the purification of the input via representation-conditional VAE reconstruction, and (2) the ensembling of multiple classifications. A critical missing baseline is the same base classifier evaluated with 8 forward passes of the *original* (unpurified) input, or the input with small noise, using the same aggregation. Without this control, it is unclear whether the internal-representation conditioning and reconstruction are the source of robustness, or whether the benefit primarily comes from the stochastic sampling + aggregation alone. Since the paper's central claim is a *synergistic* blend of the two paradigms, this gap directly weakens the causal attribution. The paper does not provide any ablation to isolate the purification effect from the ensemble effect.

- **Attack strength validation is insufficient to fully support the scale of claimed gains.** The improvement on CIFAR-100 (+27.47% absolute over the base classifier, surpassing the best AT model by +23.98%) is unusually large for a purification-based method. While the paper uses the standard randAA evaluation (AutoAttack for stochastic defences with 20 EoT iterations, 100 gradient steps), several validations are absent: (a) no ablation varying the number of EoT iterations (e.g., 50, 100, 200) to verify that 20 is sufficient for low-variance gradient estimation given the VAE's stochasticity; (b) no deterministic evaluation (e.g., fixing the latent code $\mathbf{z}=\mathbf{0}$, the prior mean) to compare against a non-stochastic version; (c) the number of restarts used in the randAA attack is not reported. These omissions leave open the possibility that the adaptive attack is not fully optimised, which would inflate the reported numbers. The concern is heightened precisely because the gains are so large — they warrant stronger attack validation than what is currently provided.

### Minor

- **Pgd+EoT re-evaluation is only shown for CIFAR-10.** The paper re-evaluates CARSO under the Pgd+EoT pipeline (developed for diffusion purifiers) for CIFAR-10 (Table 2), but does not provide this evaluation for CIFAR-100 or TinyImageNet-200. Since the paper uses the Pgd+EoT numbers for comparing against diffusion-based purification on CIFAR-10, the same comparison is not available for the other datasets.

- **Comparison with purification baselines on CIFAR-100 relies on a known overestimated number.** The paper acknowledges (Section 5.2, scenario b) that the best purification-based method (Lin2024Robust) reports 46.09% under an overestimated AA evaluation, and no reliable Pgd+EoT re-evaluation is available. CARSO's claimed advantage over purification methods on CIFAR-100 (+20.25% over the overestimated number) is therefore not a direct comparison — a stronger purification baseline under proper evaluation could narrow the gap.

- **Training ablation for adversarial batch composition is based on smaller-scale datasets.** The ablation justifying the specific mixture of FGSM and PGD attacks at two strengths (Appendix C) was performed on MNIST/Fashion-MNIST with smaller networks. The paper does not confirm on CIFAR-10 that removing any component of the batch composition significantly degrades robustness. The training procedure is intricate and may be dataset-dependent.

### Trivial

- The number of restarts used within the randAA AutoAttack configuration is not explicitly reported (though standard defaults are assumed).
- No sensitivity analysis for the number of reconstructed samples ($N=8$ fixed; a curve over $N \in \{1,2,4,8,16\}$ would be informative).

## Nice-to-Haves

- A deterministic evaluation of CARSO (fixing $\mathbf{z}=0$ or using the mean reconstruction) to isolate the effect of stochasticity on robustness.
- A sensitivity curve of robust accuracy vs. number of reconstructed samples to assess whether $N=8$ saturates the benefit.
- An analysis of why the CIFAR-100 gain is so large — e.g., visualising VAE reconstructions of adversarial examples to show selective attenuation of perturbations, or identifying which perturbation types the base classifier fails on that CARSO recovers.
- Clean accuracy of the best AT model when used with the CARSO ensemble+aggregation (without VAE reconstruction) to separate the effect of the VAE bottleneck from the ensemble size.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the high-epsilon gradient obfuscation check "does not rule out weaker-than-expected attacks at ε=8/255".** The paper presents the high-epsilon check for exactly what it is: a test for gradient obfuscation (Section 5.2), which it passes. The critic framed this as though the paper used it to validate attack strength. Removing as a strawman: the paper makes no such claim.

- **Criticism about "model choice for the purifier" (VAE limitations).** The paper explicitly acknowledges this trade-off (Section 4.1, Section 6) and defends it as a deliberate choice for evaluation transparency. Removing because the paper already addresses this.

- **Criticism about "generalisability to other architectures" (layer selection).** The paper lists the 26 layers used and discusses improved scalability as future work (Section 6). Removing as scope creep: the paper's contribution is the framework itself, not an automated layer-selection algorithm.

- **Suggestion to "use BPDA by replacing the VAE with a deterministic approximation".** The VAE is exactly differentiable; BPDA is unnecessary. The underlying idea (evaluate on a deterministic version) is valid and kept as a nice-to-have, but framed as a standard deterministic evaluation rather than BPDA.

- **Criticism that the paper "does not offer a mechanistic explanation for why such a large improvement should occur" on CIFAR-100.** The paper provides a first-principles justification in Section 4.2. A deeper empirical analysis would strengthen the paper but its absence is not a flaw in the presented work; moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface expected tensions between a novel defence method and the strength of its evaluation, but no single observation reframes the paper's contribution in an unexpected way.

## Suggestions

1. **Add the ensemble control baseline.** Evaluate the base classifier with 8 forward passes of the original (unpurified) input using the same robust aggregation. This is the single most important experiment to attribute the gain to purification vs. ensembling.
2. **Strengthen attack validation.** Report robustness under randAA with increased EoT iterations (50, 100) and with a deterministic evaluation (latent code fixed to prior mean). Explicitly state the number of restarts used.
3. **Provide the Pgd+EoT evaluation for CIFAR-100** so the comparison against diffusion-based purification is on equal footing.
4. **Add a sensitivity curve** for the number of reconstructed samples $N \in \{1,2,4,8,16\}$ to demonstrate the ensemble effect and check for saturation.
5. **Run the training ablation for adversarial batch composition** on CIFAR-10 (not just MNIST/Fashion-MNIST) to confirm that each component is necessary at the intended scale.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>