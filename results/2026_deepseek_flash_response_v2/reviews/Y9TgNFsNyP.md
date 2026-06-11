Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper introduces FF-Erase, the first machine unlearning method designed for Forward-Forward (FF) models, along with G-MIA, a membership inference attack for verifying unlearning in FF models. FF models train via layer-wise greedy optimization of "goodness" scores rather than backpropagation, and the paper identifies why standard gradient-ascent unlearning fails (layer-wise divergence and inconsistent forgetting across layers). FF-Erase addresses this via KL-divergence minimization toward a guidance model's goodness distributions, stabilizing layer-wise updates. Experiments across CIFAR-10, CIFAR-100, MNIST, and Fashion-MNIST with various architectures show speedups of 1.9–3.1× over retraining with minor accuracy degradation.

## Strengths

1. **First principled mechanistic diagnosis of why GA unlearning fails on FF models**: Section 1 (lines 38–41) identifies two concrete failure mechanisms — (a) FF layers do not update toward a consistent direction (unlike BP), so naive gradient ascent causes layers to diverge, and (b) independent layer-wise training makes it unclear how much each layer should be penalized, causing some layers to over-forget while others retain residual effects. Section 6.3 (Figure 5) confirms this empirically via a systematic λ sweep showing GA either collapses utility (test acc < 60 for λ ≥ 0.1) or fails to unlearn (G-MIA scores ~0.6 vs RE's 0.55 for λ ≤ 0.01).

2. **KL-divergence guided forgetting (Equation 5) demonstrably prevents collapse**: Rather than directly maximizing loss on forgetting data, FF-Erase minimizes KL divergence toward a guidance model's distribution. The ablation (Table 1, R.G.M row) provides strong causal evidence: substituting a randomly initialized guidance model collapses forget-accuracy to 51.18% and test-accuracy to 55.53%, confirming the guidance model is necessary for stability.

3. **Analytical efficiency model with validated speedup bounds**: Equation 9 decomposes unlearning time into guidance-model acquisition and goodness-decrease phases. Table 1 validates this concretely: retraining takes 1107s, while FF-Erase configurations range from 353.7s to 583.5s, with component-wise breakdowns that make the speedup claim decomposable and testable.

4. **Systematic two-dimensional guidance model ablation**: Table 1 varies α₁ (data fraction ∈ {0.3, 0.5}) and α₂ (epoch fraction ∈ {0.1, 0.2, 0.5}) for both mini-retrained and fast-distilled strategies, showing consistent monotonic trade-offs that provide actionable guidance for practitioners.

5. **Two complementary guidance strategies**: Mini-retraining (when sufficient remaining data exists) and fast-distillation (when remaining data is scarce) cover different data-scarcity regimes, and the ablation shows both are viable (e.g., D-(0.3,0.5) achieves G-MIA ACC 0.568 while R-(0.3,0.5) achieves 0.569).

## Weaknesses

### Major

1. **G-MIA's weak discriminative power and absence of confidence intervals undermine the central effectiveness claim**: All G-MIA scores across every condition (RE, FF-Erase, GA variants, R.G.M) fall within the narrow range of 0.52–0.61. Critically, GA(λ=0) — where the forgetting data is still in the training set and the model is effectively unchanged on it — achieves only 0.605, barely distinguishable from the collapsed R.G.M model's 0.553. RE's score of 0.551 is nearly identical to R.G.M's 0.553. **No confidence intervals or error bars are reported anywhere in the paper.** Given that the key claim of FF-Erase approaching retraining-level effectiveness rests on G-MIA differences of ~0.01–0.03, these differences may lie within the noise floor of a weak attack. This is the paper's most consequential weakness because it affects both contributions simultaneously — G-MIA is proposed as an accurate verification tool, and FF-Erase's effectiveness is primarily measured by it.

2. **Only one baseline (gradient ascent) is compared against**: The paper claims existing unlearning methods are "not feasible for FF models" (line 60) but tests only naive GA. While the mechanistic argument for why BP-based methods fail is principled, no adapted versions of influence-function methods, teacher-student approaches (e.g., SCRUB, BadTeacher), or Fisher-based calibration are attempted — even with minimal architecture adaptation for FF models. The claim is broader than the evidence.

3. **G-MIA's access-level framing is potentially misleading**: The paper calls G-MIA a "black-box" attack throughout and claims it operates under a "strict black-box constraint" (line 62), while acknowledging that standard black-box MIAs "only use the model's final prediction output." G-MIA requires per-layer goodness vectors, which in standard privacy literature constitutes gray-box access. While FF models natively expose per-layer goodness for inference (line 88), the terminology overstates the attack's practical applicability relative to standard API-level access assumptions.

### Minor

1. **No class-wise forgetting experiment**: The paper unlearns a random 20% subset where forgetting and remaining data share the same distribution. Class-wise forgetting (removing all instances of one class) is a standard stress test in the unlearning literature (Bourtoule et al. 2021, Tarun et al. 2023) and would provide more unambiguous evidence of genuine forgetting. The near-identical Acc_on_D_forget between RE (81.61) and FF-Erase (81.31) is consistent with an alternative explanation where the model simply generalizes from remaining similar data rather than truly forgetting.

2. **Guidance model behavior on forgetting data is not diagnosed**: FF-Erase's key step minimizes KL divergence toward guidance model distributions on forgetting data (Equation 5). The paper does not verify that these guidance distributions are appropriately neutral rather than confidently wrong. If the guidance model (trained on similar-distribution remaining data) produces confident misclassifications on forgetting data, the KL minimization could steer toward confident wrongness rather than genuine forgetting. The ablation shows the guidance model is necessary but does not reveal what the guidance is actually doing.

3. **Fast-distillation guidance model may indirectly encode forgetting information**: The fast-distilled guidance model (Section 4.2) is trained by distilling the original model's outputs on remaining data. Since the original model was trained on the full dataset (including forgetting data), its representations may indirectly encode information about forgetting data that transfers through distillation. This partially undermines the claim that the guidance model is "ignorant of the forgetting data."

4. **Main text shows only one architecture/dataset combination**: Only VGG13 on CIFAR-10 appears in the main text (line 242); other combinations are deferred to the appendix. This limits the force of the "extensive evaluation" claim within the main paper.

### Trivial

None.

## Nice-to-Haves

- Confidence intervals or error bars for G-MIA scores and accuracy metrics across multiple runs would substantially strengthen the quantitative claims.
- Analyzing the actual goodness distributions produced by the guidance model on forgetting data to verify they are appropriately neutral.
- Testing at least one more adapted baseline (e.g., a simplified influence-function or teacher-student variant adapted for FF layers) would strengthen the claim about existing methods' infeasibility.
- Class-wise forgetting experiments would provide stronger evidence of genuine forgetting.

## Removed Points

These points from the inputs were flagged for removal; treat them with caution:

- **"G-MIA is not a black-box attack" (Harsh Critic's stronger framing)**: The critic claimed this is "wrong" and "inflates practical relevance." The paper's defense is that FF models natively output per-layer goodness vectors as part of their inference (line 88), making this a domain-specific access model. However, the terminology tension is real — retained in weakened form as Major #3. The stronger claim that this invalidates contributions was removed.
- **"Circularity concern" (using G-MIA to evaluate FF-Erase)**: This is standard practice in the unlearning literature. The paper also uses accuracy on D_forget, accuracy on D_test, and time efficiency as metrics. Removed as a misunderstanding of standard evaluation practice.
- **"Efficiency claims are misleading" (about the 3.1× end requiring accuracy trade-offs)**: The paper's Table 1 presents all trade-offs transparently. The headline 1.9–3.1× range is accurate for the configurations tested, and the ablation makes the trade-offs explicit. Removed.
- **"Only one architecture/dataset shown" (Harsh Critic's stronger framing)**: The paper explicitly references appendix results for other combinations. Mitigated but kept in Minor form because the main text alone does not support the "extensive evaluation" claim.
- **Strengths from Strength Finder about G-MIA being "black-box" and "strictly more informative"**: These conflict with verified weaknesses about G-MIA's access-level terminology and discriminative power. The G-MIA strength is retained in modified form (#3 in Strengths) — the evidence that goodness vectors carry membership information is valid, but the "black-box" characterization is not.

## Novel Insights

The key novel observation emerging from the reviews is that the paper's two contributions are more tightly coupled than is desirable: G-MIA is both a proposed contribution and the primary quantitative tool for evaluating FF-Erase's effectiveness, but its discriminative power across all conditions is narrow (0.52–0.61). This means the central claim — that FF-Erase approaches retraining-level forgetting — rests on differences of ~0.01–0.03 that may reflect the noise floor of a weak attack rather than genuine forgetting equivalence. Without confidence intervals, this cannot be resolved from the data presented. The efficiency and utility claims are on firmer ground (larger, more interpretable differences with clear trade-offs visible in Table 1), but the effectiveness claim is less secure than presented.

## Suggestions

1. **Report confidence intervals or error bars** for all G-MIA scores and accuracy metrics across multiple random seeds/initializations.
2. **Add a class-wise forgetting experiment** to provide unambiguous evidence of genuine forgetting.
3. **Re-frame G-MIA's access level** more precisely (e.g., "layer-wise" or "gray-box" attack) and discuss what access assumptions are realistic for FF model APIs in practice.
4. **Verify the guidance model's output distributions** on forgetting data to confirm the KL minimization achieves genuine forgetting rather than steering toward confident misclassification.
5. **Include at least one more adapted baseline** (e.g., a simple influence-function or teacher-student variant) to strengthen the claim about existing methods' infeasibility.
6. **Discuss the potential encoding of forgetting information** through fast-distillation as a stated limitation.

## Calibration Report

**Round 1 (Bracketing)**: Three queries spanning score bands:
- Weak band (high_score=3.5): "Pseudo-Probability Unlearning" (3.00), "MASIMU" (2.50), "Forward Explanation" (1.50), "Pan for gold" (2.20) — clearly weaker papers.
- Middle band (low=3.5, high=7.5): "Deep Unlearning" (5.25), "Unlearning via Sparse Representations" (5.25), "Structure-Aware Parameter-Efficient MU" (5.00), "SUN" (4.00) — comparable papers.
- Strong band (low=7.5): "How much of my dataset did you use?" (7.60), "GNNCert" (8.00) — substantially stronger papers.

**Initial bracket**: 4.5–6.5

**Round 2 (Narrowing)**:
- Query 1 (low=4.5, high=6.5, MIA verification): "Unlearning Mapping Attack" (4.80), "Rethinking Adversarial Robustness" (5.75), "Adversarial Machine Unlearning" (5.33), "Forget Vectors at Play" (4.80)
- Query 2 (low=5.5, high=7.5, gradient/guidance methods): "Oblivious Unlearning by Learning" (5.67), "Rethinking LLM Unlearning Objectives" (6.00, Accept), "Label-Agnostic Forgetting" (6.00, Accept), "Decoupling Class Label" (5.75)

**Full anchor list**:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Pseudo-Probability Unlearning | 3.00 | R1 | Significantly weaker — vague contributions |
| MASIMU | 2.50 | R1 | Much weaker — unclear methodology |
| Forward Explanation | 1.50 | R1 | Much weaker — not a standard ML paper |
| Deep Unlearning | 5.25 | R1 | Comparable novelty but mixed reviews |
| Unlearning via Sparse Repr. | 5.25 | R1 | Narrower evaluation (only ViT); comparable |
| Structure-Aware MU | 5.00 | R1 | Comparable; narrower focus on Transformers |
| SUN | 4.00 | R1 | Weaker — instance-unlearning limitations |
| How much of my dataset… | 7.60 | R1 | Substantially stronger — rigorous theory+experiments |
| Unlearning Mapping Attack | 4.80 | R2 | Narrower focus; comparable quality |
| Rethinking Adversarial Robustness | 5.75 | R2 | Comparable; narrower but cleaner evaluation |
| Adversarial MU (Stackelberg) | 5.33 | R2 | Comparable; missing theoretical analysis |
| Forget Vectors at Play | 4.80 | R2 | Slightly weaker; narrower scope |
| Oblivious Unlearning by Learning | 5.67 | R2 | Comparable; different problem framing |
| Rethinking LLM Unlearning | 6.00 | R2 (Accept) | More polished; but different domain (LLMs) |
| Label-Agnostic Forgetting | 6.00 | R2 (Accept) | Stronger evaluation; supervision-free novelty |
| Decoupling Class Label | 5.75 | R2 | Comparable; different problem framing |

The paper sits between the 5.0–5.33 papers (which have clearer gaps) and the 6.0 accepted papers (which are more polished). Its genuine novelty (first FF unlearning) is a strength, but the G-MIA discriminative power issue and missing confidence intervals are significant evaluation weaknesses. Positioned near "Rethinking Adversarial Robustness" (5.75) in quality but with a more impactful problem statement and slightly more evaluation concerns.

**Final score**: 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>