## Summary

This paper proposes ACE/ACE+, a targeted adversarial attack method to protect images from unauthorized diffusion customization (LoRA+DreamBooth, SDEdit). The key idea is to use a consistent target pattern rather than maximizing the score-function error as in prior untargeted attacks. The method achieves FDFR of 1.00 on LoRA-based face customization (0% face detection in outputs), outperforming existing untargeted baselines (AdvDM, PhotoGuard, ASPL) across quantitative metrics and a large-scale user study (1,304 artists). The paper also proposes a hypothesis about reversal bias as the mechanism underlying attack-based protections.

## Strengths

- **Decisive quantitative improvement on a hard threshold**: ACE achieves FDFR of 1.00 on LoRA customization (CelebA-HQ), meaning 0% of generated face images are detected as faces — a strict threshold that none of the untargeted baselines reach at the same 4/255 perturbation budget (Section 4.2, Table 1).

- **Cross-model transferability demonstrated systematically**: Protection effectiveness is evaluated across 3 backbone × 3 victim model combinations (SD 1.4, SD 1.5, SD 2.1), showing that degradation persists even when the attack and victim models differ (Section 4.4, Table 2).

- **Ablation with alternative target (ACE*) supports robustness of design**: Changing the motif of the target pattern while keeping its chaotic design philosophy (high-contrast, repeating, Moire-like) produces similarly strong results, indicating the method does not overfit to a single hand-picked pattern (Section 3.2, Section 4.2).

- **Smaller perturbation budget than prior work**: The budget of 4/255 is explicitly smaller than the 8/255 or 16/255 used in prior work, making the evaluation more realistic for practical deployment where imperceptibility matters (Section 4.1).

- **Interesting mechanistic hypothesis**: The reversal-bias story (Section 5) provides a conceptually clear account of why targeted attacks might systematically degrade fine-tuning outputs, even though the supporting evidence is preliminary.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against ASPL-T, the most relevant baseline for the paper's causal claim.** The paper acknowledges ASPL-T as a prior targeted attack that "failed in beating untargeted attacks" (Section 3.3), making it the single most informative baseline for evaluating whether ACE's success comes from being *targeted* vs. from specific design choices (target design, objective formulation, fine-tuning pipeline). Without this comparison, the paper's headline claim — that "targeted attacks significantly outperform untargeted attacks" — conflates the concept of targeting with ACE's particular implementation. The practical finding that ACE beats ASPL is valid, but the broader attribution is unsupported.

- **Absence of statistical reporting in quantitative results.** Tables 1–3 report single-point estimates without standard deviations, confidence intervals, or significance tests. Given that the attack is stochastic (PGD with random starts), the customization pipeline has inherent randomness, and metrics are computed over sampled images, single numbers are uninformative about the reliability of the reported differences. The FDFR of exactly 1.00 particularly demands error characterization to rule out chance or data-split artifacts. This gap weakens the credibility of all comparative claims.

- **User study results are overclaimed relative to the evidence.** With 1,304 participants, ACE produces the worst-quality image in only 55% of examples vs. ASPL (Section 4.3). This is presented as validation of superiority, yet 55% is close to chance (50%), and no confidence interval or effect size is reported. The practical significance of a 55% preference rate in a forced-choice paradigm is unclear, especially without an absolute evaluation of whether ACE's outputs are genuinely "unusable."

### Minor

- **Target design space is under-explored given the weight placed on it.** The paper states that "the selection of the target has great impacts on the performance of ACE" (Section 3.2), yet the ablation (ACE*) only varies the motif while keeping the same design template (high-contrast, repeating, Moire-like). There is no experiment testing different target types (random noise, natural images, uniform targets) or demonstrating what happens with a "bad" target. The claim that target design drives performance is not validated by the presented evidence.

- **The α hyperparameter in ACE+ (Equation 5) is not specified anywhere in the paper**, creating a reproducibility gap.

- **The mechanistic hypothesis (Section 5) has minimal supporting evidence.** The only quantitative support is a single cosine similarity of -0.3044 between ε_adv and B_spl for ACE, with no comparative numbers for untargeted baselines (which the paper likely computes but does not report). A correlation of -0.3044 is weak, and without baseline comparisons, it cannot support the claim that targeting *causes* a more unified reversal bias.

- **Overstated novelty claim.** The paper claims to be "the first to both reveal the vulnerability of diffusion models to targeted attacks and leverage targeted attacks" for protection (abstract, Section 3.3). Given the explicit acknowledgment of ASPL-T (a prior targeted attack), the "first to leverage" framing is inaccurate. The legitimate claim is being the *first targeted attack to succeed*, not the first attempt.

- **DiffPure robustness reasoning is incomplete.** The paper argues that even when DiffPure removes the protection, it "also greatly degrades the performance of diffusion customization" (Section 4.5). While this is a valid practical observation, the logic assumes the adversary will always use a purification that damages image quality — which is not a generalizable defense.

### Trivial
- Table 1 is presented as an embedded image rather than text, making precise values difficult to parse.
- The transition at the end of Section 3.3 contains a typographical artifact ("5.1" dangling after a period).

## Nice-to-Haves
- Reporting the relative ordering of methods at larger perturbation budgets (8/255, 16/255, as in prior work) would clarify whether the advantage of ACE is robust to budget changes.
- The cosine similarity values for untargeted baselines in the Section 5 analysis would immediately strengthen the hypothesis evidence.
- A systematic sweep over target types (random noise, natural images, uniform, etc.) would validate or refine the target design claims.

## Removed Points
*These points were flagged during review processing but removed for the following reasons:*
- *Criticism about missing PGD iteration numbers and fine-tuning step counts* — These ARE specified in the main text (line 144: PGD = 50 steps, step length 5×10⁻³; line 119: fine-tuning = 5 steps per iteration). Removed as factually incorrect.
- *Criticism that the DiffPure reasoning is "circular"* — The logic is a practical observation (not circular), though it has a limitation. Repositioned to Minor.
- *Speculation that FDFR=1.00 "could indicate a ceiling effect or idiosyncratic data split"* — Speculative without evidence. Removed; note on missing error bars retained.
- *Criticism that "the hypothesis should not be presented as a contribution"* — A hypothesis is a legitimate contribution; the issue is with the evidence strength. Repositioned to Minor and reframed.
- *Strength Finder's claim that the hypothesis is "grounded in empirical observation" as a strong point* — The empirical support (single weak correlation) is too thin to constitute a strong point. Retained as a minor conceptual strength.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a comparison against ASPL-T to directly test whether "being targeted" drives the improvement vs. ACE's specific design choices.
2. Report standard deviations or confidence intervals across multiple random seeds/runs for all main quantitative results (Tables 1–3).
3. Provide confidence intervals for the user study preference rate and discuss its practical (not just statistical) significance.
4. Specify the α value for ACE+ and report sensitivity to this parameter.
5. Report the cosine similarity values for untargeted baselines to give the Section 5 hypothesis a proper baseline comparison.
6. Add at least one experiment with a clearly suboptimal target to demonstrate that target selection matters in the claimed direction.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>