- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8
Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces ACE and ACE+, targeted adversarial attacks that protect images against unauthorized diffusion customization (LoRA and SDEdit). The key insight is replacing the untargeted *maximization* of score-function error (used in prior work) with a *minimization* toward a fixed chaotic target pattern. Experiments show ACE achieves a Face Detection Failure Rate of 1.00 (all generated images evade face detection) and consistently outperforms untargeted baselines on all quality metrics for both LoRA and SDEdit under a small perturbation budget (4/255). A user study with 1,304 artists and evaluations of transferability and robustness to purification further support the method's effectiveness. The paper also proposes a hypothesis explaining why targeted attacks outperform untargeted ones.

## Strengths

- **Clear and consistent quantitative superiority over baselines.** Table 1 shows ACE achieves FDFR of 1.00 (meaning 0% of customization images are recognized as faces) and outperforms all baselines (AdvDM, PhotoGuard, ASPL) on CLIP-IQA, MS-SSIM, and CLIP-SIM for both LoRA and SDEdit. The improvement is consistent across metrics and settings.

- **Visual results are dramatically better.** Figure 1 shows that ACE/ACE+ cover the entire output image with chaotic patterns, while baselines only add partial patterns, leaving the main content intact. This directly supports the claim that targeted attacks make customization images unusable.

- **User study with 1,304 real artists.** Section 4.3 reports that ACE produces the worst-quality customization image in 55% of pairwise comparisons against the strongest baseline ASPL. This provides ecologically valid evidence from the target domain (graphic art industries).

- **Comprehensive evaluation of practical robustness.** Transferability experiments (Table 2) show ACE/ACE+ remain effective across different backbone/victim model combinations (SD1.4, SD1.5, SD2.1). Robustness to purification (Table 3) shows ACE survives Gaussian, JPEG, Resizing, and SR purification.

- **Ablation confirms target selection is robust, not overfitted.** ACE* (a second target with a different motif) performs similarly or better than ACE/ACE+, demonstrating that the method's success is not specific to one target design.

## Weaknesses

### Fatal
None.

### Major
- **The mechanism hypothesis (Section 5) is supported by thin evidence.** The hypothesis—that targeted attacks unify the score-function error pattern, inducing a consistent reversal bias—is based on a single visualization example (Figure 3) with a cosine similarity of only -0.3044 between ε_adv and B_spl. The paper frames this as a "surprising" and "obvious reversal relationship," but -0.3044 is a weak correlation. The hypothesis is plausible but is not rigorously tested; no quantitative validation, controlled experiments, or ablation studies are provided to confirm the causal chain it proposes. Since the hypothesis is presented as a core contribution ("Second, we propose a hypothesis on how attack-based protections work"), this gap weakens the paper's second claimed contribution.

### Minor
- **The user study result (55%) is modest in magnitude.** While 1,304 respondents provide ample statistical power, the paper does not report confidence intervals, p-values, or effect sizes. A 55% preference rate means ACE was preferred (as worst quality) in only a slim majority of comparisons. This is consistent with the quantitative results (ACE outperforms baselines) but the magnitude of improvement in user preference is smaller than the quantitative metrics might suggest.

- **Robustness evaluation uses a different perturbation budget without justification.** The main experiments use ζ = 4/255, but the purification robustness experiments (Section 4.5) use ζ = 8/255. The paper does not explain why the budget was doubled for these experiments, making direct comparison with the main results difficult. If the goal was to test robustness under stronger protection, this should be stated; if the budget was increased because 4/255 was insufficient to survive purification, this should also be acknowledged.

### Trivial
None.

## Nice-to-Haves

- **Ablation isolating the effect of the targeted loss from the fine-tuning steps.** The paper includes fine-tuning steps (following ASPL) in both ACE and the baselines, so the main comparison is fair. However, an additional ablation showing ACE's targeted objective alone (without fine-tuning steps) versus an untargeted objective alone would more cleanly isolate the benefit of targeting per se, independent of the well-known benefits of fine-tuning steps for adversarial attacks on diffusion models. This would strengthen the paper's first contribution claim.

## Removed Points

- *"The hypothesis relies on a single example with a weak correlation"* — This is kept as a Major weakness above (it is factually correct and substantive).
- *"Missing ablation isolating fine-tuning steps from targeted loss"* — Moved to Nice-to-Haves because both ACE and ASPL use fine-tuning steps, so the main comparison already controls for this factor. The requested ablation would be informative but is not necessary to validate the core claim.
- *"User study shows only 55% preference (barely above chance)"* — Kept as a Minor weakness above but rephrased to note the large sample size (1,304) makes the 55% result statistically meaningful, not "barely above chance."

## Novel Insights

None beyond the paper's own contributions. The paper's primary advance—replacing untargeted with targeted attacks for this specific protection task—is clearly stated and well-executed. The reviews did not surface insights that the paper itself does not articulate, beyond confirming that the core empirical claim holds up under scrutiny.

## Suggestions

- **Strengthen the hypothesis evidence.** Either provide more examples of the ε_adv / B_spl relationship across diverse images, or run a controlled experiment (e.g., train a model on protected images and measure the correlation between the learned bias and the attack error quantitatively). If the hypothesis is intended as a speculative discussion, frame it more tentatively rather than as a core contribution.
- **Report confidence intervals or statistical significance** for the user study result (Section 4.3) to clarify the strength of the 55% finding.
- **Justify or align the perturbation budget** in the purification robustness experiments (Section 4.5) with the main experiments, or explicitly state why a different budget was used.
