- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6
Now let me write the consolidated review.

## Summary

This paper identifies and characterizes "two-faced attacks"—verification-time perturbations that inflate the apparent adversarial robustness of adversarially trained models. The attack is formulated as a bi-level optimization (minimize the chance that an adversarial perturbation causes misclassification) and evaluated across 4 datasets, 5 training methods, multiple architectures, and several verification algorithms. The key empirical finding is a trade-off: models with *lower* adversarial risk (more robust) tend to exhibit *higher* two-faced risk, meaning two-faced attacks are more effective precisely when models are otherwise strong.

## Strengths

- **Concrete demonstration of a previously uncharacterized vulnerability.** The paper shows that PGD-AT–trained ResNet-18 on CIFAR-10 has true adversarial accuracy of only 51.72%, which inflates to 82.81% under a two-faced attack (Figure 1b). This 31-point gap provides unambiguous evidence that robustness measurements can be fraudulently inflated in the verification pipeline.

- **Comprehensive and systematic validation.** The effect is verified on CIFAR-10, SVHN, CIFAR-100, and Tiny-ImageNet; across PGD-AT, TRADES, MART, FAT, THRM, and RobustBench models; with ResNet-18 and WideResNet-28-10; and using four different verification methods (DI-FGSM, APGD_CE, FAB, Square) including a black-box attack. The paper also demonstrates transferability across models (Table 5). This breadth rules out the possibility that the observed inflation is an artifact of a single setup.

- **Clean formalization of two-faced risk.** The definition of two-faced risk (Eq. 5) and the data partition into correctly-and-robustly-classified vs. correctly-but-not-robustly-classified subsets provide a clear analytical vocabulary for the phenomenon. The partition itself yields the observation that only correctly classified examples contribute to two-faced risk, which is useful for understanding where the attack operates.

- **Identification of a non-trivial trade-off.** The empirical finding (Figure 2) that models with lower adversarial risk tend to have higher two-faced risk is well-supported across both a parametric sweep (TRADES λ) and independently trained RobustBench models. This inverts the natural expectation and suggests the vulnerability is structurally linked to robust optimization itself, not a surface artifact.

## Weaknesses

### Fatal
None.

### Major

- **Insufficiently grounded threat model.** The paper states (Sec. 4, line 141) that it "assume[s] that the adversary has access to the trained model and verification dataset to craft two-faced examples," but it never explains *why* this is a realistic scenario or *who* the adversary would be in practice. The introduction and conclusion claim the threat "could cause unpredictable security issues when deploying substandard models in reality," yet no concrete deployment pipeline is described. A dishonest model submitter providing a manipulated test set to a certification authority is one plausible scenario, but the paper does not articulate it. Without this grounding, the practical significance of the attack — the paper's main motivator — rests on an implicit and unexamined assumption. This is the single most important gap to address, as clarifying the threat model would directly elevate the contribution from an interesting formal exercise to an actionable warning.

### Minor

- **Theorem 1 is a direct algebraic consequence of the definitions, not a non-trivial theoretical result.** The paper claims to "theoretically establish the relationship between two-faced risk and adversarial risk," but Eq. (6) follows straightforwardly from partitioning the data into misclassified / cr / cnr subsets and applying the definitions of adversarial risk and natural risk. There is no inequality, no bound, and no non-trivial trade-off derived—the contrasting trend in Figure 2 is discovered empirically, not predicted by Theorem 1. The paper would be more honest if it presented the theorem as a decomposition identity rather than implying it is a substantive theoretical contribution.

- **Countermeasure analysis is shallow.** The proposed defense (enlarging the training perturbation budget) is acknowledged as "simple," but it is essentially a standard robustness knob rather than a targeted countermeasure. The paper makes no attempt to detect two-faced examples, analyze why the attack succeeds geometrically, or leverage the structure of the bi-level attack for defense. The observation that residual risk remains non-negligible (Sec. 3.3) is left as a loose end. A deeper analysis — even a negative result about detection difficulty — would have strengthened the contribution.

- **Missing hyperparameters for the two-faced attack.** Algorithm 1 specifies an iteration count N and alternates inner/outer PGD steps, but the paper never reports the value of N used, the number of inner PGD steps per outer step, or the step sizes. The training and verification PGD iterations are given (10/20), but these govern evaluation-time adversarial accuracy computation, not the attack generation itself. This is a reproducibility gap for a paper whose central contribution is an attack.

- **No error bars or uncertainty estimates.** All results (Tables 1–6, Figures 2–4) are reported as single numbers. Given the stochastic nature of adversarial training, PGD-based optimization, and the bi-level structure of the attack itself, readers cannot assess whether observed differences (e.g., the "better trade-off" claimed in Section 3.3) are significant or within noise. This weakens confidence in the fine-grained comparisons.

- **"Attack success rate" (Figure 4) is not explicitly defined.** The text and figure caption use this term without stating whether it is example-level, whether it uses a threshold, or how it relates to the formal two-faced risk. From context it appears to be the proportion of examples where the two-faced attack inflates robustness, but a formal definition is needed.

### Trivial
- A random-noise baseline (perturbing the verification set with random ε-bounded noise) would help distinguish the structural effect of the two-faced attack from mere stochastic degradation of the verification signal. This is a small addition that would sharpen the empirical story.

## Nice-to-Haves
- A brief paragraph describing a specific deployment pipeline (e.g., model developer → verification authority) would transform the practical relevance argument without requiring new experiments.
- Visualizing the decision boundary geometry around two-faced examples (e.g., measuring curvature or feature-space displacement) could illuminate *why* the attack succeeds, which would be more valuable than the current shallow defense analysis.
- Removing or re-framing Theorem 1 as a decomposition identity rather than a "theoretical establishment" would eliminate the mismatch between the paper's rhetoric and the result's substance.

## Removed Points
*These points were flagged by the reviewers but are removed (moved here) with justification:*

1. **"The claim of being 'first to show' should be softened given hypocritical examples."** The paper clearly distinguishes its contribution: hypocritical examples inflate *natural accuracy*, while two-faced examples inflate *adversarial accuracy* (robustness). This is a different attack surface with a different optimization objective. The claim is appropriately scoped and supported.

2. **"At no point does it explicitly state who the adversary is."** The paper explicitly states its threat model assumption in Section 4, line 141: "we assume that the adversary has access to the trained model and verification dataset to craft two-faced examples." The criticism that the threat model is *absent* is factually incorrect. (The *weakened* version — that the scenario is not connected to a realistic deployment pipeline — is retained as a Major weakness.)

3. **"No convergence discussion is provided for the bi-level optimization."** The bi-level attack is an alternating PGD approximation; convergence analysis for such procedures in deep learning is an open research problem, not a standard expectation for an empirical security paper. Demanding it exceeds community norms.

4. **Various formatting/style nitpicks and pure speculation.** Several of the harsh critic's "strengthening" suggestions are speculative or reflect personal preferences (e.g., requesting user studies or theoretical proofs inappropriate for this paper type). These are not included as weaknesses.

## Novel Insights
The review process surfaces one observation that goes slightly beyond the paper's own framing: the trade-off between standard adversarial robustness and two-faced vulnerability may emerge because more robust models place decision boundaries further from natural data, increasing the "margin volume" available for a two-faced perturbation to operate within. A larger boundary separation means there is more room for the outer (minimizing) perturbation δ to maneuver before triggering a misclassification under the inner (maximizing) perturbation t. This mechanistic hypothesis — which the paper does not discuss — could explain why the trade-off is not merely empirical noise but potentially a structural consequence of robust optimization. Investigating this would make a natural follow-up.

## Suggestions

1. **Anchor the threat model in a concrete scenario.** Add one paragraph in Section 1 or 3 describing a specific pipeline: e.g., "Consider a model developer who submits a trained model plus a held-out verification set to a certification body. If the developer can perturb the verification set before submission, they can inflate the reported adversarial accuracy, causing a substandard model to pass certification." This directly answers the "who and why" question without requiring new experiments.

2. **Re-frame Theorem 1 as a decomposition identity.** Remove the language of "theoretically establishing" and present Eq. (6) as what it is: an exact decomposition that connects two-faced risk to the partition of the data. This better aligns the paper's claims with the result's substance.

3. **Report attack-generation hyperparameters.** State the value of N (outer iterations), the number of inner PGD steps, and the step sizes used for Algorithm 1 across all experiments. This is essential for reproducibility.

4. **Add error bars for key claims.** At minimum, report standard deviations over 3–5 random seeds for the primary result (e.g., CIFAR-10 PGD-AT in Table 1) and the trade-off curves (Figure 2). This is standard practice for adversarial robustness papers.

5. **Define "attack success rate" formally.** Either link it to the two-faced risk definition (Eq. 5) or provide a separate formal definition in the figure caption or main text.
