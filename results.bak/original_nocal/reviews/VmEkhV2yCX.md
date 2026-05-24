Now I have all the information needed to construct the final review.

## Summary

This paper systematically investigates when and how reasoning data should be injected into LLM training, spanning pretraining, SFT, and RL. Through large-scale experiments (8B models, 1T tokens, 80B fixed reasoning-token budget), the authors propose an asymmetric data allocation principle: diversity and scale drive pretraining effectiveness, while quality dominates SFT. Key results include a +19% RL-stage advantage from front-loaded reasoning pretraining, the failure of SFT-only catch-up attempts, and evidence that naive SFT scaling with mixed-quality data harms math reasoning.

## Strengths

- **Durable front-loading advantage demonstrated across the full pipeline (Table 3).** After RL, the reasoning-pretrained model (M_LMQ+SFT_SHQ+RL) achieves 56.66% vs. the baseline (M_base+SFT_SHQ+RL) at 37.92%, an 18.74% absolute lead on expert-level benchmarks. This directly supports the claim that early reasoning injection creates a compounding advantage through post-training.

- **Catch-up hypothesis convincingly refuted within tested scope (Table 4).** Doubling SFT epochs for the baseline (M_base+SFT_SHQ with 2× epochs = 34.01%) still fails to match even the weakest reasoning-pretrained model (M_SHQ+SFT_SHQ = 37.33%). This is a clean experimental design (same SFT data, same model size, increased epochs only) that shows SFT cannot fully compensate for a reasoning-deficient pretraining foundation.

- **Evidence that naive SFT scaling with mixed-quality data is harmful (Table 8).** Scaling SFT with 2× mixed-quality LDQ data reduces MATH_SFT AVG from 28.38 to 23.46, while a marginal addition of high-quality filtered data (ALF) consistently improves performance. This finding has practical value for practitioners and is not widely documented in prior work.

- **Full training pipeline evaluated from scratch.** By training models from scratch through pretraining, SFT, and RL, the paper provides a complete picture that most prior work (limited to mid- or post-training) cannot offer. The fixed 80B reasoning-token budget across all pretraining variants is a clean methodological choice.

- **Latent effect discovery (Table 4).** M_LMQ+SFT_SHQ (50.95%) outperforms M_LDQ+SFT_SHQ (46.70%) by 4.25%, despite M_LMQ and M_LDQ having similar pretraining performance. This suggests that high-quality pretraining data can instill latent potential activated only after alignment — a novel and interesting finding even if preliminary.

## Weaknesses

### Fatal
None.

### Major

1. **The core claim that "diversity drives pretraining" is confounded with the number of unique examples.** The key pretraining comparison supporting this claim is M_LDQ (268M unique examples, diverse, mixed-quality) vs. M_SHQ (1.2M unique examples, less diverse, high-quality). Because D_SHQ is repeated ~67× to match the 80B token budget while D_LDQ needs little to no repetition, the experiment cannot separate whether M_LDQ's advantage comes from diversity of reasoning patterns or simply from having 200× more unique training examples. The paper consistently attributes the gain to "diversity" (abstract, line 14: "pretraining benefits most from broad diversity in reasoning patterns (11% average gain)"), but no condition controls for the number of unique examples (e.g., a random subset of D_LDQ matched in size to D_SHQ). This confound runs through Sections 2.2, 4 (Table 1), and 5. It does not invalidate the overall front-loading finding, but it substantially weakens the specific asymmetric principle claim about what property of pretraining data drives the gain.

2. **The headline "19% average gain" rests on a single RL condition (Table 3).** Only one RL comparison is reported: M_LMQ+SFT_SHQ+RL vs. M_base+SFT_SHQ+RL. No other pretraining variants (M_LDQ, M_SHQ) or SFT datasets are carried through RL. The abstract and introduction foreground this number as a central result, yet it comes from a single pair of conditions with no replication or sensitivity checks. While RL is expensive, the strength of the claim ("pretraining strategy dictates final accuracy on expert-level tasks") would be significantly bolstered by even one additional RL condition (e.g., M_LDQ+SFT_SHQ+RL). As it stands, the 19% figure could be partially driven by the specific SFT data (D_SHQ) or RL recipe, not purely by the pretraining strategy.

### Minor

3. **No uncertainty quantification reported.** All tables present only point estimates with no standard errors, confidence intervals, or significance tests. The paper does run multiple evaluations (16 runs for AIME, 4 runs for most other benchmarks per Section 3.2) but reports only the mean. Several comparisons involve small differences — e.g., the +4.25% latent effect of M_LMQ over M_LDQ (Table 4), the -4.92% math drop from scaling SFT (Table 8) — that could plausibly fall within evaluation noise, especially on high-variance benchmarks like AIME and LiveCodeBench.

4. **Only one SFT catch-up intensity tested (Table 4).** The catch-up experiment doubles SFT epochs to 2×, but the paper's claim that SFT "cannot fully replicate" pretraining foundations is tested at only this single intensity. Whether 3× or 4× epochs, or a different SFT dataset, could close more of the gap remains untested. The claim is appropriately qualified ("cannot be fully replicated by *simply* scaling the SFT phase"), but the strength of the evidence is proportionate to the single multiplier tested.

5. **Domain composition differences across reasoning datasets are not controlled.** D_SHQ is 71% math / 21% code / 8% science, while D_LDQ is 56% math / 17% code / 27% science. The paper attributes M_LDQ's science gains to "abstract and logical structures" learned from diverse reasoning patterns, but the larger fraction of science data in D_LDQ (27% vs. 8%) is a viable alternative explanation for some of the cross-domain generalization effects observed (Section 4, Table 1). This is a secondary confound that doesn't undermine the main findings but warrants caution in the specific mechanism claimed.

### Trivial
None.

## Nice-to-Haves

- Run RL on at least one additional condition (e.g., M_LDQ+SFT_SHQ+RL) to verify that the pretraining→RL advantage is not specific to the M_LMQ/SFT_SHQ combination.
- Disentangle diversity from example count in pretraining by training M_LDQ-subset (a random subset of D_LDQ matched to D_SHQ's 1.2M unique examples, repeated to 80B tokens).
- Report variance or confidence intervals for key comparisons, particularly the latent effect (+4.25%) and SFT scaling drops, using the multiple runs already collected.
- Analyze the effects of extreme repetition in D_SHQ (e.g., loss curve divergence, held-out set evaluation) to rule out overfitting as a factor in M_SHQ's underperformance.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The +4.25% latent effect shown only with SFT_SHQ, may be a SFT-data-specific artifact"** (Harsh Critic, Missing Experiments #3). The paper's design systematically varies both pretraining and SFT conditions; showing the latent effect with all SFT variants would be exhaustive but is not necessary to establish the finding within the scope of the paper's controlled setup. The claim is appropriately qualified.

- **"Table 5 confound between quality, size, and domain composition"** (Harsh Critic, Section-by-Section notes on Table 5). While the confound exists descriptively, D_SHQ (small, high-quality) outperforms D_LDQ (large, mixed-quality) across all base models. If "smallness" alone were responsible, smaller datasets would generally underperform larger ones, so the direction of evidence favors a quality interpretation. The criticism overstates the concern.

- **"The paper could strengthen Table 5 by using a large, high-quality SFT dataset"** (Harsh Critic, Table 5 note). This is a suggestion for future work, not a weakness of the existing experiment.

- **"Averaging across categories mutes domain-specific stories"** (Harsh Critic, Table 2 notes). The paper provides per-benchmark breakdowns in the appendix (Table 13, removed by parser). Standard practice.

- **Various generic suggestions about deploying on larger scales (30-70B), more systematic ratio sweeps, and qualitative case studies** (Harsh Critic, "Missing Parts and Places to Improve"). These are directions for future work, not shortcomings of the current paper.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a tension that is worth articulating: the paper's main strength — conducting large-scale pretraining experiments that are rare in the literature — also imposes a practical constraint that limits the breadth of controlled comparisons (only 4 pretraining variants, 1 RL condition, 1 catch-up intensity). The "diversity vs. example count" confound and the single RL condition are not oversights; they reflect the genuine difficulty of running many ablations at this scale. However, the paper's claims are more assertive than the experimental coverage warrants — the abstract states "diversity drives pretraining effectiveness" as a settled principle when the data equally supports "more unique examples drive pretraining effectiveness." The key insight from the meta-review is that the paper's evidence best supports the front-loading claim (reasoning in pretraining > no reasoning in pretraining), moderately supports the SFT quality claim, and most weakly supports the specific attribution of the pretraining advantage to diversity rather than to example count.

## Suggestions

1. **Acknowledge the confound between diversity and unique-example count explicitly.** Add a paragraph discussing this limitation and either (a) provide a control experiment with a matched-size subset of D_LDQ, or (b) soften the claim from "diversity drives pretraining" to "scale and diversity (which are naturally correlated) drive pretraining, with the mechanisms to be disentangled in future work."

2. **Run RL on at least M_LDQ+SFT_SHQ to extend Table 3.** A single additional condition would significantly strengthen the headline result and address the concern that the 19% gain is specific to the M_LMQ pretraining variant.

3. **Report standard deviations or confidence intervals** for key comparisons, using the multiple evaluation runs already performed (16 for AIME, 4 for other benchmarks). At minimum, note for small-gap comparisons (e.g., the +4.25% latent effect) that the gap is within the range of typical evaluation noise and should be interpreted cautiously.

## Score and Decision

The paper makes a genuine contribution by demonstrating that front-loading reasoning data into pretraining provides a durable advantage through SFT and RL — a finding that is practically important and supported by large-scale experiments. The catch-up experiment and the SFT scaling harms are convincing. However, two major weaknesses prevent full acceptance: (1) the central claim attributing the pretraining advantage specifically to "diversity" (rather than to the number of unique examples) rests on a confounded comparison, and (2) the headline 19% RL-stage gain is supported by only a single experimental condition. These do not invalidate the paper but mean the evidence does not match the strength of the claims as currently written. With explicit acknowledgment of the confound, softened claims, and at least one additional RL condition, the paper would be a strong contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>