Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

The paper proposes Fuzzed Randomized Smoothing (FRS), a defense against textual backdoor attacks injected during pre-training. FRS combines (1) biphased model parameter smoothing — adding Gaussian noise to the top-H layers during fine-tuning and inference — with (2) MCTS-guided fuzzed text randomization that identifies vulnerable trigger-containing segments and concentrates randomization probability on them. The paper provides a theoretical analysis of the certified robustness radius and validates the method across three datasets, three attack methods, and five victim models (BERT-base/large, RoBERTa-base/large, LLaMA3-8B), showing consistent improvements over baselines including TextGuard.

## Strengths

- **Novel integration of MCTS-guided fuzzing with randomized smoothing for textual backdoor defense.** The paper proposes using Monte Carlo tree search to proactively identify vulnerable text segments (trigger-prone areas) and then applies probability-weighted randomization concentrated on those segments (Section 4.3). This differs from prior randomized smoothing defenses (e.g., TextGuard) that use uniform randomization and from empirical defense methods that lack theoretical guarantees.

- **Consistent state-of-the-art defense across diverse model architectures, scales, and attack strategies.** Table 1 shows FRS achieving the highest clean accuracy (CA) and poisoned accuracy (PA) and lowest attack success rate (ASR) among both empirical defenses and the certified baseline TextGuard across three datasets and three attack methods. Table 4 extends this to five victim models (BERT-base/large, RoBERTa-base/large, LLaMA3-8B), showing FRS consistently outperforms TextGuard in CA, PA, and ASR — including on the billion-parameter LLaMA3-8B.

- **Biphased model parameter smoothing to reduce computational overhead.** Instead of fine-tuning K separate models on K randomized datasets, FRS performs parameter smoothing on a single fine-tuned model by adding noise only to the top-H output-proximal layers during both fine-tuning and inference (Section 4.2). This avoids the prohibitive training cost of prior methods while still providing certified guarantees — a practical contribution for large PLMs.

- **Theoretical analysis of a broader certified robustness radius from non-uniform text randomization.** Corollary 1 (Eq. 18) formally shows that concentrating randomization probability on vulnerable areas (ω_H > ω_M) yields a larger radius: R_r^new = (log(ω_M)/log(ω_H)) × R_r^old > R_r^old. Table 2 empirically validates this with average radius improvements of 25.72%–34.87% over TextGuard.

- **Ablation study confirms both components contribute positively.** Table 3 shows that removing either the biphased model parameter smoothing (BMPS) or fuzzed text randomization (FTR) degrades PA and ASR across all three datasets and attack methods, demonstrating the complementary value of each component.

- **Addresses the underexplored post-attack scenario.** The paper focuses on backdoors injected during pre-training (not fine-tuning), where defenders have no access to poisoned data and must defend after the fact — a more challenging and realistic setting than assumed by prior randomized smoothing defenses that require access to training data.

## Weaknesses

### Fatal
None. While the paper's theoretical framework has gaps, they do not invalidate the core empirical contributions or the overall approach.

### Major

- **Assumption 1 is stated without rigorous justification, weakening the certified robustness claim.** The paper's theoretical framework (Section 4.4) relies on Assumption 1 — that the smoothed model's output on benign inputs matches the clean fine-tuned model. The paper asserts this is "approximately guaranteed" with a small learning rate η but provides no proof, sketch, or formal argument (Section 4.4, paragraph after Eq. 15). Since the certification guarantee depends on this assumption holding, the lack of rigorous justification means the claimed "certified robustness" is conditional on an unverified premise. To be clear: the theory about radius improvement from non-uniform text randomization (Corollary 1) is coherent on its own terms; the gap is in connecting the parameter-level smoothing to the base model quality required by that theory.

### Minor

- **No undefended baseline in the experimental evaluation.** Tables 1, 3, and 4 report defense performance (CA, PA, ASR) against various attacks but never show the attacked model's performance *without any defense*. Without this, it is impossible to assess the severity of the attacks or the absolute magnitude of improvement provided by FRS. For example, FRS achieves ASR 3.91% on SST-2 with RIPPLe_a — but if the undefended ASR is already low (e.g., <20%), the result is less impressive. This baseline is standard in the backdoor defense literature and its absence is a notable omission.

- **Key hyperparameter values for the FRS-specific components are not reported.** The paper introduces ω_H, ω_L, ω_M (text randomization probabilities), Λ (Damerau-Levenshtein distance threshold), C (MCTS exploration constant), and the MCTS iteration budget — but none of these are given numerical values in Section 5.1 or anywhere else. The MCTS iteration budget is especially important because Corollary 1's promise of ω_H→1 depends on having sufficient budget. Without these values, the method cannot be reproduced and the theoretical radius formula cannot be evaluated against the empirical setup.

- **The certified robustness radius computation (Table 2) is not described as a reproducible algorithm.** The paper states: "for each test sample, we find the maximum percentage of tokens that can be perturbed while the model still maintains correct prediction with high probability (e.g., 95% confidence)." This describes the *goal* but not the procedure — e.g., how the search is performed, what hypothesis test is used, what values of α and K are used in the binomial/Beta test, or how the confidence intervals from the Monte Carlo voting are mapped to a radius. This makes the central empirical claim in RQ2 difficult to verify or reproduce.

- **MCTS identification accuracy is not validated.** The method's key claim is that MCTS-guided fuzzing successfully identifies trigger-containing segments. However, the paper never reports what fraction of test samples this identification is correct, nor does it analyze how identification failures affect the effective ω_H and the resulting radius. The ablation study (Table 3) partially addresses this by showing that removing FTR degrades performance, but a direct validation of the MCTS component's accuracy is missing.

- **No confidence intervals or variance reported for radius results (Table 2).** The radius improvements are reported as single values (e.g., 25.72%–34.87% improvement). Given that the radius is computed via Monte Carlo sampling with K=20, variance is expected. Reporting only point estimates without standard deviations or confidence intervals makes it unclear whether the improvements are statistically significant.

- **The biphased parameter smoothing is only justified for top-H layers.** The paper adds noise to the top H output-proximal layers, citing (Kurita et al., 2020) that these layers are most vulnerable. However, the paper does not discuss whether this holds for all attack types evaluated (RIPPLe_a, LWP, BadPre), and does not report whether the choice H=10 was validated or how sensitive results are to this choice.

### Trivial

- The statistical significance markers (asterisks in Tables 1 and 4) are explained as t-test at p<0.01, but the reference comparison (compared to which baseline?) is not specified.

- The paper states in the abstract and introduction that FRS "achieves a broader certified robustness radius" before presenting the evidence — standard framing, but slightly premature.

- The evaluation in Section 5.2.3 (ablation) shows that removing BMPS improves CA slightly (because smoothing degrades benign accuracy), which is a known trade-off that the paper acknowledges.

## Nice-to-Haves

- A discussion of computational cost. The method requires K=20 forward passes per test sample plus the overhead of MCTS search. The paper claims "efficient" but provides no runtime or memory figures.
- A sensitivity analysis for key hyperparameters: σ, H, K, MCTS iteration budget, Λ, ω_H/ω_L.
- A dedicated limitations section discussing the dependence on MCTS accuracy, the assumption about trigger location, and the diminishing returns for large models.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Abstract claim is stated as fact before evidence"** — Removed per formatting/style nitpick rule. Standard abstract framing, not a substantive weakness.
- **"Missing comparison to concurrent randomized-smoothing defenses (denoised smoothing, word-substitution smoothing)"** — Removed per hard rule about not mentioning missing related works. These methods target evasion attacks, not backdoors, and the paper's scope is clearly scoped to backdoor attacks.
- **"Statistical significance asterisk not explained"** — Partially removed. The paper does explain it's a t-test at p<0.01 in the table captions. The question of "compared to what baseline" is fair but trivially addressed.
- **"No sensitivity analysis"** — Downgraded to Nice-to-Have. Standard practice but not a core flaw.
- **"Section 4.1 'abandons' its approach in Section 4.2"** — Overstated severity. Section 4.1 presents a general framework and Section 4.2 develops a practical scheme. The two are connected via Assumption 1; the gap is that Assumption 1 lacks proof (kept as Major weakness above), not that the approaches are disconnected.
- **"No computational cost discussion"** — Moved to Nice-to-Have.
- **"Ablation magnitude is modest"** — Removed. The paper doesn't claim each component provides huge improvements; it claims they contribute positively, which the data supports.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper's strongest selling point (certified robustness) hinges on an unproven assumption about parameter smoothing, yet the empirical results may be strong enough to stand on their own as a heuristic defense. This suggests the paper could benefit from either (a) a formal proof connecting parameter smoothing to input-level smoothing, or (b) an honest reframing as an effective empirical defense with a theoretically-motivated radius formula, rather than a fully certified approach. The consistent performance across diverse settings (5 models, 3 datasets, 3 attacks) indicates the core idea has merit regardless of the theoretical framing.

## Suggestions

1. **Tighten the theoretical framework.** Either prove Assumption 1 formally (perhaps relating parameter noise variance σ² and learning rate η to the approximation error) or reframe the contribution as an empirically effective defense with a theoretically-motivated heuristic, dropping the pretense of formal certification for the practical algorithm.

2. **Add a no-defense baseline** to all experimental tables with the attacked model's CA, PA, and ASR without any defense applied.

3. **Report all missing hyperparameters** — ω_H, ω_L, Λ, MCTS iteration budget, C — in the implementation details section.

4. **Describe the radius computation algorithm** as a reproducible procedure (e.g., binary search over perturbation radii, using a binomial test with α=0.05 and K=20, etc.).

5. **Validate MCTS identification accuracy** by reporting the overlap between identified vulnerable areas and true trigger positions (when known from the attack configuration), perhaps broken down by attack type and model.

6. **Add confidence intervals or standard deviations** to Table 2, computed over the five runs mentioned in Section 5.1.

## Score and Decision

The paper addresses an important and underexplored problem: certified defense against textual backdoor attacks injected during pre-training. The MCTS-guided fuzzing approach is novel and the empirical results are consistently strong across diverse settings. However, the paper suffers from a significant gap in its theoretical grounding (Assumption 1 is unproven), which undermines the central "certified robustness" claim, and the experimental evaluation is missing key baselines and implementation details needed for proper assessment and reproducibility. The paper also presents some results (radius improvements, attack success rates) without critical context (no-defence baseline, confidence intervals).

These weaknesses are addressable in revision. The core empirical finding — that FRS consistently outperforms existing defenses — is likely robust. I would support acceptance if the authors can either provide rigorous justification for Assumption 1 or honestly reframe the contribution, and fill in the missing baselines and implementation details.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>