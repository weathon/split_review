Now I have a strong calibration set. Let me synthesize my final review.

**Round 1 Bracket:** I placed the paper between 5.5 and 8.0 based on the bracketing anchors.

**Round 2 Narrowing:** Comparing against:
- KIPJKST4gw.md (7.25, "Code Data at Which Stage"): Very similar research question, but uses a smaller model (2.6B), has token-count confounding issues. The current paper is comparable in contribution quality but slightly cleaner in design. The current paper has some overclaiming that the code paper mostly avoids.
- 1hQKHHUsMx.md (6.75, "What Pretraining Data for Reasoning"): Narrower scope (80 queries, influence functions), but deeper analysis. The current paper is broader in scope.
- GtpubstM1D.md (5.71, "Advancing Math Reasoning"): Also about CPT vs SFT, but highly split reviews (1 to 8). The current paper is more systematic and has clearer results.
- 3OyaXFQuDl.md (7.00, "Smaller Weaker Yet Better"): Tight, well-executed paper on synthetic data. The current paper is comparably well-executed but broader.

**Final Score: 7.0** — Between the code paper (7.25, slightly stronger execution) and the pretraining-data paper (6.75, narrower scope). The paper makes a real empirical contribution with a large-scale, systematic study. The main weaknesses (limited catch-up test, latent-effect confound) are significant enough to mention but don't invalidate the core findings.

Now let me write the review.## Summary

This paper presents the first large-scale systematic study of how reasoning data—varying in scale, diversity, and quality—should be allocated across pretraining, supervised fine-tuning (SFT), and reinforcement learning (RL) to maximize LLM reasoning performance. Training 8B models from scratch on 1T tokens, the authors find that front-loading reasoning data into pretraining creates a durable advantage (+19% on expert benchmarks after RL), that diversity matters more in pretraining while quality dominates in SFT (an "asymmetric" allocation principle), that naive scaling of mixed-quality SFT data can be actively harmful, and that high-quality pretraining data can exhibit "latent" benefits only activated after SFT. The experiments are carefully controlled and include multiple ablations that isolate the roles of data properties across the full training pipeline.

## Strengths

- **Front-loading reasoning creates a compounding advantage verified through RL.** Table 3 shows that the reasoning-pretrained model (ℳ_LMQ + SFT_SHQ + RL) achieves a full 18.57% absolute lead over the baseline (56.66 vs. 37.92) on expert-level benchmarks, with a 39.32% improvement on AIME problems. This is direct evidence that the pretraining advantage persists and widens through the entire alignment pipeline, not just immediately after pretraining.

- **Asymmetric allocation principle is well-supported by controlled phase-specific experiments.** Table 1 shows diverse data (ℳ_LDQ) outperforms high-quality small data (ℳ_SHQ) by +9.09% in pretraining, while Table 5 shows the reverse in SFT — models fine-tuned on high-quality data beat those fine-tuned on large diverse data by +13.45%. The paper cleanly demonstrates that "diversity matters for pretraining, quality matters for SFT" using parallel experimental arms.

- **The finding that naive SFT scaling actively harms math reasoning is striking and well-documented.** Table 8 shows that doubling the diverse but mixed-quality SFT dataset drops MATH SFT AVG from 28.38 to 23.46 (−4.92%), while a marginal (+0.4%) addition of high-quality filtered data (ℳ_LDQ + SFT_ALF*) improves overall accuracy. This directly challenges the prevailing "more is better" mindset for SFT data.

- **Systematic, large-scale experimental design.** The paper trains 8B models from scratch at 1T tokens with controlled token budgets (80B reasoning tokens across all conditions), uses a fully crossed design across pretraining and SFT conditions (4 × 3 = 12 models for the SFT analysis), and includes an RL phase. This is a substantial empirical investment that yields clean comparisons.

- **Multiple ablations that probe the sensitivity of key design choices.** The reasoning-ratio sensitivity (Tables 6–7) and the SFT scaling contrast (Table 8) provide actionable calibration data for practitioners, showing how the reasoning proportion in pretraining affects downstream behavior and how different SFT scaling strategies produce opposite outcomes.

## Weaknesses

### Fatal
None.

### Major

- **The "catch-up" test is narrower than the claim it supports.** The paper asserts that SFT "cannot be fully replicated by later-stage SFT, even with more data" (abstract), but the primary evidence for this (Table 4) only tests 2× epochs on the same 4.8M SFT samples. This tests one specific scaling strategy (repeating the same data), not whether a genuinely scaled SFT effort with more unique samples, higher diversity, or different data sources could close the gap. The claim is partially supported by converging evidence (Table 5 shows even different SFT datasets can't close the gap for M_base; Table 3 shows the gap widens under RL), but the headline claim exceeds what the single 2×-epoch experiment demonstrates. The authors should either (a) add SFT scaling experiments at multiple data quantities (e.g., 5× or 10× more samples from high-quality pools) or (b) reframe the claim to match what was tested: "With SFT budgets common in the literature (~5M samples), pretraining with reasoning data provides an advantage that cannot be overcome by simply training longer on the same data."

- **The "latent effect" of high-quality pretraining data is confounded by experimental design.** The paper argues that ℳ_LMQ (which includes both ℳ_LDQ and ℳ_SHQ) shows a "latent" advantage over ℳ_LDQ after SFT (+4.25%), attributing this to D_SHQ quality in the pretraining mix. However, ℳ_LMQ is a superset of ℳ_LDQ with 269.2M unique samples vs. 268M. Since both are trained with the same 80B reasoning token budget, ℳ_LMQ repeats each of its samples fewer times. The observed difference could therefore be driven by (a) D_SHQ's quality, (b) lower repetition rate of the diverse D_LDQ samples, (c) an interaction between these factors, or (d) training stochasticity (4.25% on a single configuration with no confidence intervals). The claim is plausible and interesting, but the paper does not run the controlled ablation needed to disentangle these factors (e.g., adding matching D_SHQ tokens to ℳ_LDQ while reducing repetition of D_LDQ to hold total tokens constant).

### Minor

- **No confidence intervals or measures of variability.** The paper reports averages over multiple runs only for AIME (16 runs) and a few other tasks (4 runs), but the main comparison tables (1, 2, 4, 5, 8) report point estimates without standard deviations or confidence intervals. For comparisons where key differences are 3–5% (e.g., the latent effect of +4.25%), readers need to assess whether these gaps are reliable. Reporting bootstrapped 95% CIs would substantially strengthen credibility.

- **Token budget for SFT is not reported.** The paper states SFT uses 4.8M samples but never reports the corresponding token count. Since the pretraining reasoning budget is 80B tokens, knowing the SFT token budget is important context for evaluating the "catch-up" claim and understanding the asymmetry in resource allocation between phases.

- **The budget-constraint framing (Eq. 2) is conceptually useful but not enforced experimentally.** The paper sets up an optimization problem where total reasoning data |D_res^PT| + |D_res^SFT| is bounded by B, but the experiments do not test trade-offs under a fixed total budget. Pretraining uses 80B tokens of reasoning data while SFT uses a much smaller budget. This should be acknowledged, as the budget framing is a helpful conceptual device rather than an operational constraint in the experiments.

- **The reasoning-ratio sensitivity study (Tables 6–7) is limited to two data points (80/20 and 60/40) plus one at 90/10 for pretraining only.** The paper does not explore other ratios (e.g., 50/50) or assess diminishing returns beyond 40% reasoning data. The observed decline in instruction-following at 60/40 is attributed to "breadth-alignment trade-off," but with only two post-SFT data points this remains speculative.

### Trivial
- The abstract's "19% average gain" should clarify that this is an absolute gain (18.57 percentage points from Table 3) to avoid ambiguity with relative improvement.

## Nice-to-Haves
- Controlled ablation for the latent effect: add matching D_SHQ tokens to ℳ_LDQ while reducing repetition of D_LDQ to maintain the 80B token budget. If the latent effect persists, the quality explanation is supported; if it disappears, the effect is due to reduced diversity repetition.
- SFT scaling experiments with more unique data (not just repeated epochs) to strengthen the catch-up claim.
- Per-task breakdowns for the SFT scaling ablation (Table 8), which the paper notes as one of its strongest findings.
- Discussion of why the baseline model drops so sharply from 52.70 (Table 1, base evaluation) to 29.92 (Table 4, after SFT_SHQ) — even accounting for different benchmarks, this large decline warrants diagnosis (e.g., overfitting, catastrophic forgetting).

## Removed Points

The following points from the input reviews are removed as non-substantive, factually incorrect, or beyond scope:

- **"Different benchmarks for base vs SFT evaluation making drops an artifact"** — The paper explicitly acknowledges this in Section 3.2 ("unlike in base model evaluations, where mostly focus on the generalizability of the LLM"). This is by design, not an oversight.
- **"M_LDQ and M_LMQ are tied after pretraining and not discussed"** — The paper does discuss this (Section 5, line 216: "scaling D_LDQ with D_SHQ... provides minimal further benefit"). Factually incorrect.
- **"Missing related works"** — As per instructions, I cannot evaluate missing citations.
- **"Missing appendix details / reproducibility concerns about cited datasets"** — The parser strips appendix sections. Cited datasets are assumed to exist per protocol.
- **"Formatting/style nitpicks"** — These reflect parser artifacts, not submission quality.
- **"Budget constraint not enforced"** — Retained as minor weakness above rather than a major issue, since the framing is acknowledged as conceptual.
- **Strength Finder's generic strengths** (e.g., "the paper addresses an important problem") — Removed as generic/superficial. Only concrete, evidence-grounded strengths are retained.
- **Strength Finder's claim about "doubling SFT cannot compensate"** — Retained as a core finding but weakened in severity given the limited scope of the test.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond the paper's own explicit findings — is that the harmful effect of naive SFT scaling (Table 8) combined with the asymmetric allocation principle creates a surprising inversion: the data strategy that works best for pretraining (large, diverse, mixed-quality) is actively counterproductive for SFT, where small, curated, high-quality data dominates. This suggests a two-phase strategy that directly opposes the simplistic "more data is better" narrative. The finding that even adding 0.4% high-quality data while holding total size nearly constant yields measurable improvement further underscores that SFT effectiveness is driven by data selection, not volume.

## Suggestions

1. **Run (or at minimum explicitly acknowledge the limits of) a stronger catch-up test.** If feasible, fine-tune M_base on 5× or 10× more unique high-quality SFT samples to demonstrate saturation. If not feasible, reframe the claim precisely: "With standard SFT budgets (~5M samples), repeated-epoch training cannot close the pretraining gap."

2. **Disentangle the latent effect confound.** Add D_SHQ tokens to M_LDQ's pretraining while reducing D_LDQ repetition to maintain the 80B token budget. If the advantage persists, the quality story is clean; if not, attribute it to repetition effects.

3. **Add bootstrapped 95% confidence intervals** to the main result tables (especially Tables 1, 4, 5, 8) for the multi-run benchmarks. Report token counts for the SFT phase alongside sample counts.

4. **Soften the abstract's "cannot be fully replicated by later-stage SFT, even with more data"** to match what was actually tested, e.g., "cannot be fully recovered by standard SFT budgets or by simply increasing training epochs on the same data."

## Score and Decision

**Comparison to calibration anchors:**
- *KIPJKST4gw.md* (avg 7.25, Accept): "At Which Training Stage Does Code Data Help LLMs Reasoning?" — Very similar question about inserting reasoning (code) data at different stages. Uses a smaller 2.6B model and had a significant confound (not controlling token counts between code and NL conditions). The current paper is cleaner in design and broader in scope (diversity × quality × scale vs. just code vs. NL), making it comparable in quality. Slightly lower score reflects the catch-up and latent-effect overclaiming.
- *1hQKHHUsMx.md* (avg 6.75, Accept): "What Kind of Pretraining Data Do LLMs Rely on When Doing Reasoning?" — Narrower analysis (80 queries via influence functions on 5M docs) but deeper mechanistic insight. The current paper is broader and more practically actionable.
- *3OyaXFQuDl.md* (avg 7.00, Accept): "Smaller, Weaker, Yet Better" — Tightly executed study on synthetic data generation, fewer overclaiming issues. The current paper is comparable in quality but has slightly more overclaiming relative to evidence.
- *GtpubstM1D.md* (avg 5.71, Accept): "Advancing Mathematical Reasoning" — Also studies CPT vs. SFT for math, but highly split reviews (1 to 8) with concerns about proprietary data and insufficient rigor. The current paper is more systematic and better controlled.

**Final assessment:** This is a solid empirical paper that makes a genuine contribution. The core findings (front-loading matters, asymmetric allocation, harmful SFT scaling) are well-supported by large-scale experiments. The two main weaknesses (limited catch-up test and confounded latent-effect analysis) are real but don't invalidate the paper's central thesis — they primarily affect the strength of specific sub-claims. The paper is most comparable to the 7.0–7.25 range anchors in the calibration set.

**Score: 7.0 — Accept.** The paper provides a valuable systematic study that will inform how practitioners allocate reasoning data across training stages. The authors should address the overclaiming on the catch-up and latent-effect claims in the final version, but the core empirical contributions are sound.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>