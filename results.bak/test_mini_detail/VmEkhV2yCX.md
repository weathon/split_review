Now I'll write the final consolidated review.

---

## Summary

This paper presents the first systematic, large-scale controlled study of how reasoning data — varying in scale, diversity, and quality — affects LLM performance when introduced at different training stages (pretraining vs. SFT). Training 8B models from scratch for 1T tokens with a controlled 80B reasoning token budget, the authors find that front-loading reasoning data into pretraining creates advantages that persist through SFT and RL, and that the optimal data strategy is asymmetric: diversity matters more in pretraining, while quality dominates in SFT. The paper also identifies a "latent effect" of high-quality pretraining data that emerges only after SFT, and warns against naive scaling of SFT data.

## Strengths

1. **First systematic, large-scale controlled study of reasoning data placement across the full training pipeline.** The paper trains 8B models from scratch for 1T tokens on 512 H100s with a fixed 80B reasoning token budget across all pretraining variants (Section 2.3). This is substantially larger in scale and more rigorously controlled than prior work, which has typically focused on post-training only or used smaller mid-training interventions.

2. **Conclusive refutation of the catch-up hypothesis with direct quantitative evidence.** Table 4 shows that even doubling SFT epochs for the baseline (M_base + 2× epochs) improves by only 4.09%, still underperforming the weakest reasoning-pretrained model (M_SHQ + SFT_SHQ) by 3.32%. This provides concrete evidence that SFT cannot substitute for an early reasoning-rich pretraining foundation.

3. **Discovery of an asymmetric allocation principle supported by domain-specific accuracy breakdowns.** Table 1 shows M_LDQ (diverse pretraining) outperforms M_SHQ (narrow, high-quality pretraining) by +9.09%, while Table 5 shows SFT with high-quality D_SHQ yields +44.99% average vs. only 31.54% for diverse D_LDQ. The contrast is consistent across math, science, and code domains, providing actionable heuristics for data allocation.

4. **Full pipeline validation through reinforcement learning.** Table 3 shows that the pretraining advantage is amplified after RL: M_LMQ + SFT_SHQ + RL achieves 56.66% vs. 37.92% for the baseline — an 18.74 pp gap that widens to +39.32% on AIME competition problems. This demonstrates that early reasoning investment yields compounding returns through the entire training chain.

5. **Systematic ablation of reasoning ratio and sensitivity analysis.** Tables 6–7 vary the pretraining reasoning ratio from 10% to 40%, showing monotonic improvements in reasoning benchmarks while documenting the trade-off with instruction-following. This gives practitioners a calibrated control knob rather than a binary recommendation.

## Weaknesses

### Fatal

None.

### Major

1. **The "latent effect" claim is confounded by data repetition.** The paper finds that M_LMQ + SFT_SHQ outperforms M_LDQ + SFT_SHQ by +4.25% (Table 4) and attributes this to a "latent effect" where high-quality pretraining data is "unlocked" by SFT. However, M_LMQ = D_LDQ ∪ D_SHQ, meaning M_LMQ has already seen the D_SHQ data during pretraining. When M_LMQ is SFT'd on the same D_SHQ data, the model has been exposed to it twice — a trivial explanation for the performance advantage that the "latent activation" framing does not rule out. A clean test would require SFT on different high-quality data than what was seen during pretraining. This weakness undermines one of the paper's four headline claims.

2. **The "naive SFT scaling is harmful" claim is overbroad relative to the evidence.** The abstract states that "naively scaling SFT data can be harmful" and the paper claims that "Blindly scaling SFT with mixed-quality data yields no average improvement and actively harmed mathematical reasoning by -5%." These claims are supported by only a single condition in Table 8: doubling D_LDQ (the mixed-quality dataset) during SFT of M_LDQ, which shows a -4.92% drop in math. Only one dataset type (D_LDQ), one scale factor (2×), and one base model (M_LDQ) are tested. The paper acknowledges that scaling *high-quality* SFT data (D_ALF) is beneficial, which undercuts the broad "harmful" claim. A more measured conclusion — that low-quality SFT data does not benefit from simple duplication — would be better supported.

### Minor

3. **The diversity/quality confound in the asymmetric principle is not fully disentangled.** The asymmetric principle claims that "pretraining benefits from diversity, SFT benefits from quality." The central comparison in Table 1 contrasts M_LDQ (268M samples, diverse, heterogeneous quality) with M_SHQ (1.2M samples, narrow, curated quality). These datasets differ on both diversity AND quality simultaneously, making it impossible to attribute M_LDQ's +9.09% advantage to diversity alone. The paper partially addresses this via the M_LMQ condition (adding D_SHQ to D_LDQ yields no pretraining improvement over M_LDQ), which suggests quality matters less than diversity at pretraining. However, the confound between repetition frequency and diversity in the M_LDQ vs. M_SHQ comparison remains unaddressed: M_SHQ's 1.2M samples are repeated ~67× to reach the 80B token budget, potentially causing overfitting on a narrow pattern set. The core empirical finding is genuine, but the attribution to "diversity" rather than "avoiding overfitting on narrow data" is underdetermined.

4. **The headline "19% average gain" is stated without specifying the reference conditions.** The abstract says "front-loading reasoning data into pretraining is critical (19% average gain)." This figure (18.74 pp) comes from a single comparison in Table 3: the best model (M_LMQ + SFT_SHQ + RL) vs. the baseline (M_base + SFT_SHQ + RL) at the RL stage. The "average" is across benchmarks within this one comparison, not across multiple experimental conditions. While technically accurate, the phrasing could lead readers to believe this is more comprehensive than it is. It should be clearly stated as the gain at the RL stage for the best-vs-baseline comparison.

### Trivial

5. **Only one RL configuration is reported.** Table 3 shows RL for just two conditions (best and baseline). Showing RL results for more model variants (e.g., M_LDQ + SFT_SHQ + RL, M_SHQ + SFT_SHQ + RL) would strengthen the claims about the RL phase, which anchors the paper's most striking result.

## Nice-to-Haves

- An experiment that holds the total reasoning token budget constant while allocating it entirely to SFT vs. partly to pretraining (testing the budget-constrained formulation in Equation 2 more directly).
- A control experiment for the latent effect that uses non-overlapping SFT data to rule out the repetition confound.
- Representation-level analysis (e.g., probing or representation similarity) to substantiate the "durable foundation" claim mechanistically.
- A discussion of the computational cost trade-off: does front-loading reasoning require more, less, or the same total compute for a given performance target?

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Scale and diversity confound" (Harsh Critic, point 1) — partially removed.** The claim that "scale is an equally plausible driver" is inaccurate: the paper explicitly controls for total reasoning token count (80B) across all pretraining variants (Section 2.3: "When a reasoning dataset is small, it is repeated so that the model still observes the same total volume of reasoning tokens"). What varies is unique sample count, which is essentially what diversity means here. The actual remaining confound (diversity vs. quality) is retained as weakness #3 above. The "scale" criticism is removed as it misunderstands the experimental control.

- **"Catch-up test is too narrow" (Harsh Critic, point 3) — removed.** The proposed alternative test (allocating all 80B reasoning tokens to SFT) is a different experiment testing a different question (budget-constrained allocation under Equation 2). The paper's catch-up test (doubling SFT epochs) directly answers the stated hypothesis: whether more intensive SFT can compensate for a missing reasoning foundation. The experiment as run supports the conclusion. The reviewer's suggestion would be a nice extension but is not a flaw in the existing experiment.

- **Strength: "Latent pretraining effects" (Strength Finder, supporting strength 1) — removed.** This strength conflicts with verified weakness #1 (data repetition confound). The finding is real but the interpretation is ambiguous, so it cannot be claimed as a strength without addressing the confound.

- **"Conclusive refutation" — slightly weakened.** The catch-up refutation is clean but the reviewer's point about alternative catch-up strategies (changing data composition, not just epochs) is a reasonable caveat. The paper's current wording ("cannot be fully replicated by simply scaling the SFT phase") is actually quite measured. No change needed beyond what's already stated.

- **Generic strengths from Strength Finder regarding "importance of problem" — removed.** Statements like "this paper addressed an important problem" are generic and not specific to this paper's evidence.

## Novel Insights

Beyond the paper's own contributions, the reviews surface two observations that the paper itself does not fully explore. First, the interaction between data repetition and diversity is a structural confound in the experimental design: when datasets of different sizes are token-budget-equalized via repetition, the cheaper-to-scale variable (more unique samples vs. more passes over fewer samples) is not separable from diversity per se. This suggests that the "diversity advantage" may partly be an "avoiding overfitting on narrow data" advantage — a distinction with practical implications for data collection strategies. Second, the latent effect story, despite the repetition confound, raises an interesting question about whether certain types of data are more effective as "priming" (seen once during pretraining for the model to build representations around) versus "training" (seen during SFT for direct behavioral cloning), which could motivate future work on curriculum design with non-overlapping data across stages.

## Suggestions

1. Clarify the "19% average gain" to state explicitly that it refers to the RL-stage comparison between the best pretrained model and the baseline, averaged across expert-level benchmarks.
2. Add a control experiment for the latent effect using non-overlapping high-quality SFT data (or explicitly discuss the repetition confound and temper the claim).
3. Narrow the "naive SFT scaling" claim to match the evidence: "scaling low-quality SFT data can harm math reasoning" rather than a general principle about SFT scaling.
4. Acknowledge the diversity/quality confound in the pretraining comparison and either add a controlling experiment (e.g., subsample D_LDQ to match D_SHQ's token count while keeping diversity) or reframe the finding.
5. Add RL results for at least one more model variant (e.g., M_LDQ + SFT_SHQ + RL) to strengthen the RL-phase claims.

## Score and Decision

**Rounds 1–2 calibration**: Compared against human-reviewed anchors, the paper sits between "Advancing Mathematical Reasoning" (avg 5.71, poster) — which is narrower and less controlled — and "At Which Training Stage Does Code Data Help LLMs Reasoning?" (avg 7.25, spotlight) — which is cleaner in its claims but less comprehensive. The key anchors used:

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| "At Which Training Stage Does Code Data Help LLMs Reasoning?" | 7.25 | 1, 2 | Similar question (code vs. reasoning data at different stages). Current paper is more comprehensive (multi-domain, data diversity/quality, RL) but has clearer overclaiming issues. Weaker overall. |
| "Procedural Knowledge in Pretraining Drives Reasoning" | 6.75 | 1, 2 | Different methodology (influence functions). Comparable scale of contribution. Current paper has stronger experimental control but less mechanistic insight. Slightly weaker. |
| "Advancing Mathematical Reasoning" | 5.71 | 2 | Similar focus on data strategy across stages, but math-only and less controlled. Current paper is stronger in scope and rigor. |
| "Revisiting SAH" | 5.75 | 2 | Different question (post-training scaling). Similar level of overclaiming issues. Current paper is stronger empirically. |
| "Math for AI" | 4.25 | 1 | Less rigorous, narrower scope. Current paper is clearly stronger. |

**Bracket**: Round 1 placed the paper between 3.5 (weak reject-level) and 8.0 (strong accept). Round 2 narrowed to 5.5–7.0. Within this bracket, the paper is stronger than the ~5.7 anchors (posters with narrower scope or weaker controls) but weaker than the ~7.25 anchor (spotlight with cleaner claims).

**Final score: 6.0.** The paper makes a genuine contribution — the first large-scale controlled study of reasoning data placement, with useful empirical findings — but the overclaiming on the latent effect, SFT scaling, and the diversity attribution require tempering. The core experiments are well-designed and the raw results are informative; with calibrated claims this would be a strong paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>