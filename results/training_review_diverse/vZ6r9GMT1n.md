Now I have the full paper text from my earlier successful read. Let me provide my consolidated review.

---

## Summary

This paper proposes adding independent Gaussian noise to hidden feature representations at inference time as a defense against query-based black-box attacks (both score-based and decision-based). The contribution includes: (1) a theoretical analysis (Theorem 1) connecting the probability of misleading the attacker to the ratio of defense noise to attack noise and the ratio of feature-space to input-space gradient norms, (2) a simple plug-in algorithm (Algorithm 1) that requires no retraining, and (3) extensive empirical evaluation across CIFAR-10 and ImageNet using multiple architectures (VGG19, ResNet50, ViT, DeiT) against five attack types and adaptive EOT adversaries. The empirical results consistently show that feature-level noise outperforms input-level noise, often by large margins (e.g., VGG19 on CIFAR-10 under Square attack: 62.8% vs. 39.8% robust accuracy).

---

## Strengths

1. **Consistent and sizable empirical improvement over input-noise defenses across diverse settings.** On ImageNet VGG19, feature defense achieves 22.2% robust accuracy under Square attack (10k queries) vs. 17.8% for input defense (Table 1); on CIFAR-10 VGG19, 62.8% vs. 39.8% (Table 2). These gains hold across CNN and transformer architectures and across score-based (NES, SignHunt, Square) and decision-based (RayS) attacks (Table 4, e.g., VGG19 RayS: 15.4% vs. 8.1%). The evaluation covers 6 model architectures and 5 attack types, making the empirical claim well-supported.

2. **Robustness against adaptive EOT attacks.** Table 5 shows that feature defense retains a meaningful advantage even when the attacker averages over M=5 or M=10 queries to cancel randomness (e.g., VGG19 vs. Square at M=5/QC=1000: 53.0% vs. 24.2%). This is important because many randomized defenses are trivially bypassed by EOT.

3. **Simple, practical design with compatibility for adversarial training.** Algorithm 1 adds only Gaussian noise to hidden layers at inference without retraining. It can be applied to any pre-trained model and combined with adversarial training (Ours+AT achieves 77.8% robust accuracy vs. 37.6% for feature defense alone and 32.5% for AT alone on CIFAR-10/ResNet20 under Square attack — Table 3).

4. **Analysis of gradient-ratio dynamics during attack.** Figure 1 demonstrates that the ratio of feature-space to input-space gradient norms increases as the attacker perturbs the input, which explains why feature perturbation becomes more effective as the attack progresses — a non-trivial insight grounded in the theoretical framework.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 is imprecisely stated for a claimed theoretical contribution.** The theorem states that "the probability that the attacker chooses an opposite action positively correlates with" an arctan expression. The phrase "positively correlates with" is vague — it gives no explicit bound, inequality, or precise functional form. A properly stated theorem would provide a lower bound on the probability of misleading the attacker (e.g., `Pr(opposite action) ≥ 1 - ε(ν/μ, gradient ratio)`) or at least an explicit monotonicity guarantee. The paper explicitly contrasts itself with prior randomized defenses that "solely rely on empirical evaluations" (line 13), claiming theoretical confirmation, but the theorem as stated in the main text does not rise to the level of a rigorous theoretical guarantee. (Note: the reviewer's claim that "a probability cannot be an arctan value" partially misreads the theorem — the paper says "positively correlates with," not "equals." The core concern about imprecision, however, is valid.)

### Minor

2. **The decision-based attack analysis (Section 3.3) is heuristic and acknowledged as such, but the framing overclaims.** The paper acknowledges "the distribution of g(d) does not have an analytical form" and resorts to a linearization argument to show that noise increases the variance of the loss, making the attacker "more likely to misjudge the direction." This is plausible and intuitive, but it does not constitute an analysis of the actual binary-search procedure used by RayS or SignFlip, and the paper does not derive any concrete bound or guarantee. The empirical results (Table 4) show the defense works, so this is a framing gap rather than an empirical one — but the abstract's claim of theoretical analysis for "both score-based and decision-based attacks" overstates what Section 3.3 delivers.

3. **The evaluation protocol for the stochastic model is underspecified.** Definition 1 defines adversarial examples based on the *expected* argmax (`arg max E[f_rand(x')] ≠ y`), but in practice, the attacker queries the *randomized* model and receives a single stochastic sample per query. The paper does not clarify whether robust accuracy in the tables is computed as (a) the accuracy of the expected decision (requiring multiple forward passes to estimate the argmax of expectations) or (b) the accuracy against an attacker querying the random model (which is the practical setting but does not directly match Definition 1). This should be clarified for reproducibility.

4. **Which specific layers are perturbed in the main experiments is not reported.** Algorithm 1 accepts a set of perturbed layers `H`, and Table 6 shows per-layer results. But the main tables (Tables 1, 2, 4, 5) do not state which layer(s) were chosen for the "Feature" defense for each model. The paper says the method works with "a set of perturbed layers" but does not document the actual configuration used to produce the headline numbers. This is essential for reproducibility.

### Trivial

5. **Computational cost of the defense is not quantified.** The paper claims the method is "lightweight" but does not report latency or memory overhead per forward pass compared to the undefended model or the input-noise baseline. This is easy to add.

---

## Nice-to-Haves

- An analysis of how noise inflates the variance of the finite-difference gradient estimator (Equation 4) used by score-based attackers would deepen the theoretical contribution without requiring a new theorem.
- A concrete empirical study of how noise affects the binary-search trajectories in decision-based attacks (e.g., the distribution of `g(d)` under noise) would strengthen the decision-based section more than the current linearization.

---

## Removed Points

- *"Theorem 1 is not a well-formed theorem because a probability cannot be an arctan value."* — Removed because it partially misreads the paper. The theorem states the probability "positively correlates with" arctan, not that it equals arctan. The core concern about imprecision is kept in Major Weakness 1 above.
- Generic strengths from the Strength Finder that were superficial or redundant have been consolidated into the Strengths section above.

---

## Novel Insights

The reviews do not surface a genuinely novel observation beyond the paper's own contributions. The key insight — that the ratio of feature-space to input-space gradient norms controls the effectiveness of feature noise and increases during an attack — is already presented by the paper.

---

## Suggestions

1. Restate Theorem 1 as a concrete inequality or bound on the probability of misleading the attacker, or if the proof does not yield one, explicitly downgrade the claim from "theoretical confirmation" to "theoretical intuition/insight."
2. Clearly state in the experimental section which specific layers were perturbed for each model in each main table.
3. Clarify the evaluation protocol: is robust accuracy measured against Definition 1 (expected argmax) or against the practical random model? If the latter, state it explicitly and consider adjusting Definition 1 to match practice.
4. Add a brief table or sentence quantifying the per-forward-pass latency and memory overhead of the defense.

---

## Score and Decision

The paper makes a solid empirical contribution: a simple, well-evaluated defense that consistently outperforms the input-noise baseline across models, attacks, and datasets. The main weakness is in the theoretical framing — Theorem 1 is too imprecisely stated to count as "theoretical confirmation," and the decision-based analysis is heuristic. However, the empirical evidence is strong enough to support the method's effectiveness independently of the theory. With revisions to tighten the theoretical claims and clarify experimental details, the paper would be suitable for acceptance. In its current form, the imprecision in Theorem 1 and the underspecified experimental protocol (layer selection, evaluation metric) are real but addressable limitations that do not undermine the core empirical finding.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>