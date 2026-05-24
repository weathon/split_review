Now let me compile the final review.

---

## Summary

This paper introduces FF-Erase, the first machine unlearning framework designed for Forward-Forward (FF) trained neural networks. FF models use layer-wise greedy optimization of "goodness" scores rather than backpropagation, and existing unlearning methods (e.g., gradient ascent) cause model collapse when applied naively. FF-Erase uses a guidance model to steer layer-wise goodness distributions during unlearning, avoiding instability. The paper also proposes G-MIA, a goodness-based membership inference attack for verifying unlearning effectiveness. Experiments across four image benchmarks and multiple architectures show FF-Erase achieves retraining-level unlearning at 1.9–3.1× faster speed.

## Strengths

- **First unlearning method for FF models with genuine novelty.** The paper identifies and formalizes a genuinely unexplored problem: FF models' sensitivity to parameter tuning and layer-wise independent training make standard unlearning methods (gradient ascent) infeasible. The goodness-guided strategy with a separate guidance model is a creative solution tailored to FF architectures.

- **Convincing failure analysis of gradient ascent on FF models.** Figure 5 systematically varies the utility-effectiveness weight λ across six orders of magnitude (10¹ to 0). The results clearly show that gradient ascent either collapses the model (λ ≥ 0.1) or fails to remove membership information (λ ≤ 0.01), providing concrete evidence that standard approaches are insufficient for FF models.

- **FF-Erase achieves retraining-level unlearning with substantial speedups.** Figure 4 shows FF-Erase(D) achieves a G-MIA score of 0.5245 versus retraining's 0.5320 (near-random at 0.5), with forget-set accuracy matching retraining (81.31% vs 81.61%). Table 1 documents total unlearning times of 353–584 seconds versus 1107 seconds for retraining (1.9–3.1× faster).

- **G-MIA outperforms existing black-box MIAs on FF models.** Figure 3 demonstrates that G-MIA consistently beats the final-layer black-box MIA (FL) across all architectures and datasets, and on VGG13 with CIFAR-100 even surpasses white-box gradient-based (GR) and statistics-based (ST) attacks. This is credited to the richer membership signal in FF-specific goodness vectors.

- **Well-designed ablation on guidance model acquisition.** Table 1 systematically varies data fraction α₁ and epoch fraction α₂ for both mini-retrained and fast-distilled guidance models, revealing clear efficiency–effectiveness–utility trade-offs. The random-guidance baseline (R.G.M) demonstrates that a stable guidance model is essential, collapsing accuracy to ~55%.

- **Evaluation across diverse settings.** Experiments cover CIFAR-10, CIFAR-100, MNIST, and Fashion-MNIST with TinyCNN, AlexNet, and VGG13 architectures trained via both CwComp and Deeperforward FF algorithms.

## Weaknesses

### Major

- **G-MIA threat model is mischaracterized as "black-box."** The paper repeatedly labels G-MIA as a black-box attack (Abstract, §5, §6.1), yet G-MIA requires access to layer-wise goodness vectors—internal signals that a standard black-box API returning only final predictions would not expose. The paper notes that "FF models output the goodness vectors from all layers for inference" (§3.1), which is true for FF architecture, but whether a deployed model exposes these vectors or only final class predictions determines whether the attack is black-box or gray-box. The paper should explicitly define the access model (e.g., "intermediate-output" or "gray-box") and clarify when an external verifier would realistically obtain goodness vectors. This also weakens the comparison with the final-layer black-box MIA (FL), since G-MIA exploits a richer information stream.

- **Missing pre-unlearning membership inference baseline.** The unlearning verification in §6.2 reports only post-unlearning G-MIA scores (Figure 4c). Without showing the attack's accuracy on the forgetting data *before* unlearning, a post-unlearning score near 0.5 cannot be confidently attributed to effective unlearning—it could reflect that G-MIA was never strong on those particular samples. The paper does evaluate G-MIA on held-out member/non-member sets in §6.1, but these are not the actual forgetting samples used in §6.2. Reporting the drop in G-MIA accuracy from the original model to the unlearned model on the same forgetting data would directly demonstrate the amount of membership information removed.

- **Overbroad claim about infeasibility of all prior unlearning methods, tested against only one baseline.** The paper asserts that existing unlearning methods are infeasible for FF models (§1, §2), but the experimental evidence is limited to gradient ascent (GA). While Figure 5 convincingly shows GA fails, the paper does not test even simple alternatives such as fine-tuning on the remaining data alone, which is a common and inexpensive approximate unlearning baseline. Demonstrating that such baselines also fail on FF models—or that FF-Erase outperforms them—would substantially strengthen the claim that a specialized FF method is necessary.

### Minor

- **No error bars or variability measures.** All reported numbers (Figure 4, Figure 5, Table 1) appear to come from single runs. Given the sensitivity of FF training to initialization and the 20% random forgetting split, reporting means and standard deviations over multiple seeds would improve confidence in the results.

- **Abstract's accuracy degradation range not directly supported in main body.** The abstract states "1.6–3.3% degradation in accuracy," but the main text shows results for only one configuration (VGG13 on CIFAR-10). The full range presumably draws on appendix results; a summary table in the main text would help readers assess generality without consulting stripped material.

### Trivial

- The discrepancy between the projected unlearning time (25–35% of retraining in §4.3) and measured times (32–53% in Table 1) should be briefly discussed or the projection should be updated to reflect empirical reality more accurately.

## Nice-to-Haves

- **Sensitivity to forgetting set size.** The evaluation uses a fixed 20% forgetting ratio. Realistic unlearning requests often involve much smaller fractions; an ablation varying β would show whether FF-Erase remains effective for small-batch deletion requests.

- **Acknowledgment of limitations.** The guidance model itself requires training on remaining data (which may still be costly for very large models), no formal privacy guarantee is provided, and the evaluation is limited to small-scale image benchmarks. A limitations section would contextualize these trade-offs.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"G-MIA's access to goodness vectors cannot be realized by model inversion techniques"* — The harsh critic incorrectly claimed the paper says model inversion recovers goodness vectors. The paper actually uses model inversion only for synthetic data generation for shadow model training (§5), which is a standard MIA technique and unrelated to obtaining goodness vectors.

- *"The paper must report what G-MIA achieves on forgetting data before unlearning"* — This is already captured as a Major weakness above but without the harsh critic's incorrect framing about what must be done.

- *"The workflow assumes the attacker can obtain the output of the target model... This is a strong assumption"* — The harsh critic's emphasis on this being impossible is weakened by the fact that FF models' standard inference output IS the goodness vectors (§3.1). The issue is about clarity of the threat model, not impossibility of access.

- *"The paper omits key details such as how synthetic shadow-model data is generated"* — These details are likely in the stripped appendix. Not appropriate to flag as a weakness without seeing the appendix.

- *Strength Finder's "G-MIA delivers a practical, accurate black-box verification"* — This strength is retained but qualified by the threat model concern. The core claim that G-MIA outperforms other MIAs is supported by Figure 3.

## Novel Insights

The paper makes an interesting architectural observation: the layer-wise independent training of FF models, which causes instability under gradient ascent during unlearning, is also what makes their goodness vectors highly informative for membership inference. This creates a natural pairing where the same structural property that necessitates a specialized unlearning method also enables a stronger verification tool. This bidirectional relationship between FF training characteristics and both unlearning and verification is a genuinely novel insight beyond the paper's stated contributions.

## Suggestions

- Clarify the G-MIA access model: explicitly state that it requires goodness vectors (the standard FF model output) and frame it as a "gray-box" or "intermediate-output" attack rather than "strict black-box." This small reframe would resolve the main threat-model concern without changing any technical content.

- Add the pre-unlearning G-MIA score on the forgetting data to Figures 4(c) and 5(c), or include it in a table. This is a low-effort addition (the data already exists; it just needs to be computed and reported) that would close the most significant evidential gap.

- Add one additional classical baseline, such as fine-tuning on remaining data alone. Even if it performs poorly on FF models, demonstrating that would substantiate the claim that FF-Erase is necessary.

## Score and Decision

### Calibration anchors used:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Xagys9QD3T (Pseudo-Probability Unlearning) | 3.00 | R1 | Current paper substantially stronger — more novel, better experiments |
| 85X9awoVtv (Auditing Data Controller) | 2.50 | R1 | Current paper much stronger |
| Uv7bWrIucU (Auditing Privacy Protection of MU) | 4.20 | R1 | Current paper stronger — clearer contributions, more comprehensive |
| xmQuUqSynb (Rethinking Adversarial Robustness) | 5.75 | R1/R2 | Comparable novelty but current paper has more complete evaluation |
| dYTjB86pcT (System Aware Unlearning) | 5.50 | R2 | Current paper has better empirical validation |
| wAemQcyWqq (Oblivious Unlearning by Learning) | 5.67 | R2 | Current paper has broader evaluation and clearer contributions |
| oe51Q5Uo37 (Scalable Exact Unlearning with PEFT) | 6.75 | R2 | S3T has stronger experimental rigor (error bars, more baselines); current paper has more novelty in problem setting but less polish |
| EUSkm2sVJ6 (Quantitative Data Usage Inference) | 7.60 | R1 | High-band anchor clearly stronger — crisper formalization, better evaluation |

**Round 1 bracket:** 5.0–7.0. The paper is clearly above the low-band (2.5–3.0) and above weak middle anchors (4.20), but not as polished as top accept papers (7.6+).

**Round 2 narrowing:** The paper sits between the 5.75 anchor (similar novelty but less complete evaluation) and the 6.75 anchor (more rigorous but less novel problem). The current paper's genuine novelty as the first FF unlearning method and comprehensive experimental coverage are offset by the G-MIA threat model clarity issue, missing pre-unlearning baselines, and limited classical baselines.

**Final score:** 6.0 — a solid contribution with genuine novelty and reasonable empirical support, but several addressable gaps in verification protocol and threat model framing prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>