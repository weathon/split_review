Now I have all the calibration data I need. Let me synthesize the comparisons and produce the final review.

**Anchor comparisons:**

| Anchor | Score | How our paper compares |
|--------|-------|------------------------|
| BGnm7Lo8oW | 5.50 (Reject) | Our paper is much stronger — actual scale (8B, 1T tokens), systematic controlled experiments, clear findings |
| GtpubstM1D | 5.71 (Accept) | Our paper is cleaner, more systematic, covers 3 stages including RL |
| eENHKMTOfW | 6.00 (Accept) | Our paper is more innovative with the asymmetric principle and catch-up refutation |
| 1hQKHHUsMx | 6.75 (Accept) | Our paper is broader, more systematic, larger scale |
| KIPJKST4gw | 7.25 (Accept) | Very similar "at which stage" question. Our paper more comprehensive (3 stages, RL, larger scale) but shares the no-variance issue and has a specific diversity/repetition confound weakening one headline claim |
| NGKQoaqLpo | 7.50 (Accept) | Different topic. Methodologically cleaner. Our paper doesn't quite reach this level |

**Final score: 7.0** — stronger than the 5.5-6.75 anchors, comparable to KIPJKST4gw (7.25) but slightly lower due to the diversity/repetition confound that weakens a headline claim.

---

## Summary
This paper presents a systematic empirical study investigating how reasoning data should be allocated between the pretraining and SFT phases of LLM training. Using controlled experiments on 8B-parameter hybrid models trained from scratch for 1T tokens, the authors vary the stage at which reasoning data is introduced and the properties (diversity, quality, quantity) of that data. The central findings are: (1) front-loading reasoning data into pretraining creates durable, compounding advantages that SFT alone cannot recover; (2) an asymmetric allocation principle — diversity matters most in pretraining, quality dominates in SFT; (3) high-quality pretraining data can have latent benefits activated only after SFT; and (4) naive scaling of noisy SFT data is harmful. The paper's strongest contribution is the empirical demonstration of this asymmetric allocation principle, backed by a well-controlled cross-product experimental design and a compelling catch-up refutation experiment.

## Strengths
- **Well-controlled experimental design with fixed token budgets.** The paper keeps reasoning token budgets constant across conditions (80B tokens during pretraining, 4.8M SFT samples) and crosses four pretrained model variants against multiple SFT datasets (producing 12 SFT models), enabling clean isolation of *when* reasoning data is introduced rather than confounded by *how much*. This is clearly specified in Section 2.3 and underpins all comparative claims in Tables 1–5.
- **Compelling catch-up refutation experiment.** Doubling SFT epochs on the baseline model (M_base + SFT_SHQ, 2× epochs → 34.01 average) still fails to match the weakest reasoning-pretrained model with standard SFT (M_SHQ + SFT_SHQ → 37.33). This clean head-to-head comparison in Table 4 provides direct, falsifiable evidence that SFT cannot substitute for reasoning exposure during pretraining — the paper's central thesis.
- **Asymmetric allocation principle grounded in cross-table evidence.** Table 1 shows diversity/scale drive pretraining gains (M_LDQ at 64.09 vs. M_SHQ at 54.98), while Table 5 shows the opposite in SFT — fine-tuning on small high-quality D_SHQ (44.99) dramatically outperforms fine-tuning on large diverse D_LDQ (31.54). The inversion of which data property matters at each phase is a concrete, actionable finding.
- **Three-stage pipeline demonstrates compounding effects.** Table 3 traces the advantage gap from PT → SFT → RL, showing the gap widens from +9.3% after SFT to +18.74% after RL, with dramatic gains on AIME competition math (+39.32%). This validates that pretraining advantages compound rather than wash out.
- **Careful dataset curation along orthogonal axes.** The four reasoning datasets (D_SHQ, D_LDQ, D_LMQ, D_ALF) independently vary quality, diversity/scale, and answer complexity, enabling disentanglement of these confounded properties.
- **Comprehensive benchmark coverage across phases.** Evaluations span math (GSM8K, MATH-500, AIME24/25), science (MMLU, MMLU-Pro, GPQA-Diamond), code (HumanEval+, MBPP+, LiveCodeBench), general reasoning (ARC, HellaSwag, WinoGrande, RACE), and instruction-following (IFEval), reducing the risk of benchmark-specific results.
- **Practical ablations address natural follow-up questions.** The reasoning ratio sensitivity analysis (Tables 6–7) and SFT scaling analysis (Table 8) provide actionable guidance beyond the main experiments.

## Weaknesses

### Fatal
None.

### Major
- **The "diversity matters in pretraining" claim is confounded with data repetition frequency.** The comparison that supports this headline claim — M_LDQ (268M diverse samples) vs. M_SHQ (1.2M high-quality samples) — equalizes *token count* (80B reasoning tokens each) but not *unique example count*. D_SHQ's 1.2M samples are repeated many times (~67x) while D_LDQ's 268M samples are seen at most once. The paper acknowledges repetition (line 93: "When a reasoning dataset is small, it is repeated") but never discusses how this confound affects interpreting the result. The observed advantage of M_LDQ could be driven by diversity, by avoiding harmful overfitting from excessive repetition, or by the sheer number of unique examples. The experimental design cannot distinguish these, weakening the central claim that "diversity matters most in pretraining."
- **No variance or confidence intervals reported anywhere.** The paper reports point estimates throughout — single accuracy numbers per benchmark per model — with no confidence intervals, standard deviations, or any measure of variance. The paper mentions using multiple evaluation runs (16 for AIME, 4 for others, line 148), but no variance is reported from these runs. Without variance estimates, the reader cannot assess whether narrow margins (e.g., M_LDQ at 64.09 vs. M_LMQ at 64.07 in Table 1) are signal or noise. This is a significant omission for an empirical paper.

### Minor
- **The headline +19% claim rests on a single RL comparison between two extreme models.** The abstract prominently features a "+19% average gain" but the RL phase (Table 3) compares only M_base vs. M_LMQ (both with SFT_SHQ). No RL results are reported for M_SHQ or M_LDQ, so the "compounding through RL" claim is supported by only one pairwise comparison.
- **The "latent effect" interpretation is underdetermined by the evidence.** The paper claims high-quality pretraining data has a "latent effect" unlocked only after SFT, based on M_LMQ outperforming M_LDQ by +4.25% after SFT despite near-identical pretraining scores (64.07 vs. 64.09). But M_LMQ = D_LDQ + D_SHQ during pretraining — it saw D_SHQ examples that M_LDQ never saw. The post-SFT advantage could reflect direct transfer of those examples rather than a "latent" effect. The latent-effect framing is speculative without additional controls.
- **Reasoning data injected only in the final 40% of pretraining tokens.** The paper injects reasoning data for only the final 400B out of 1T tokens (lines 93-94), which is closer to a mid-training intervention than "front-loading from the beginning." The paper discusses mid-training in related work (lines 272-273) but does not acknowledge how its own protocol relates to it.
- **No limitations section.** The paper lacks an explicit limitations discussion. Key limitations (diversity/repetition confound, single architecture family, narrow RL evaluation, mid-training-like protocol, lack of variance reporting) should be acknowledged directly.

### Trivial
- **IFEval included in SFT evaluation average.** The inclusion of instruction-following (IFEval) alongside math/science/code benchmarks in the SFT aggregate metric (Table 2, Table 4, Table 5) dilutes the "reasoning" signal. A separate reasoning-only average would provide cleaner results.

## Nice-to-Haves
- A compute cost trade-off analysis: whether 80B reasoning tokens in pretraining is more cost-effective than 80B more base pretraining tokens plus heavier SFT would help practitioners adopt these recommendations.
- RL results for the full set of pretraining conditions (M_SHQ, M_LDQ) to test whether the pretraining advantage genuinely compounds or merely persists.
- An additional pretraining control disentangling diversity from repetition (e.g., subsampling D_LDQ to match D_SHQ's unique-sample count while preserving domain breadth).

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Architecture concern (hybrid Mamba-attention, limited to one architecture family).** The Harsh Critic noted the unusual architecture choice and questioned generalizability to pure transformers. The paper references a 1.2B Transformer validation experiment (Table 14) which is in the stripped appendix. Per rules, criticism of missing appendix content is removed. Furthermore, the architecture choice is a legitimate design decision used consistently across all conditions — internal validity is preserved.
- **Demand for larger-scale transformer experiments.** The Harsh Critic noted that a small 1.2B transformer experiment "cannot fully address the concern at 8B scale." This demands experiments beyond what is feasible in a single paper and is scope creep.
- **"First systematic study" phrasing flagged as overstated.** The paper is genuinely systematic in its controlled comparisons — this is a reasonable claim within its stated scope.

## Novel Insights
The most novel insight from synthesizing the reviews is the identification of the diversity/repetition confound in the pretraining comparison. The paper's experimental design equalizes token counts but not unique example counts, making the core question of "does diversity drive pretraining gains, or does avoiding harmful repetition?" unanswerable from the current data. This is a subtle methodological point that, if addressed with additional controls or qualifed interpretation, would substantially strengthen the paper's headline claim.

## Suggestions
- Report standard deviations across evaluation runs for all main tables. The data likely already exists given 4-16 runs per benchmark.
- Add an explicit limitations section acknowledging the confounds and scope boundaries.
- Qualify the diversity claim in pretraining to acknowledge the repetition confound, or run a control that subsamples D_LDQ to match unique-sample count while preserving domain breadth.
- Expand the RL evaluation to include M_SHQ and M_LDQ conditions to substantiate the compounding claim.
- Separate reporting of a reasoning-only average (excluding IFEval) alongside the full average for clarity.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>