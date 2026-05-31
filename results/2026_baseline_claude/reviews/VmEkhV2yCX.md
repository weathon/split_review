## Summary
The paper conducts a large-scale empirical study of how reasoning data—varying in scale, diversity, and quality—should be allocated between pretraining and supervised fine-tuning (SFT) stages of LLM training. Training 8B hybrid Mamba2-Transformer models from scratch for 1T tokens on 512 H100 GPUs, the authors find that front-loading reasoning data during pretraining yields durable and compounding advantages (+18.57% after RL vs. the baseline), and that the optimal strategy is asymmetric: diversity drives pretraining effectiveness, while quality governs SFT. Additional findings include a latent effect of high-quality pretraining data activated by SFT and harm from naive SFT data scaling.

## Strengths

- **Genuine pretraining experiments at scale**: Training 4 separate 8B models from scratch for 1T tokens on 512 H100s is an expensive and rare experimental contribution; most comparable work starts from already-pretrained checkpoints. This makes the front-loading claim uniquely credible.
- **The asymmetric principle is well-supported and novel**: Tables 4 and 5 together provide a clean demonstration that diversity matters in pretraining (LDQ >> SHQ when kept at 80B reasoning tokens) while quality dominates in SFT (SHQ > LDQ/LMQ in SFT). The reversal is striking and practically useful.
- **Latent effect finding (Table 4)**: The observation that M_LMQ's high-quality data shows minimal benefit over M_LDQ immediately after pretraining (+0.02%) but a +4.25% boost after SFT is a nuanced, previously unreported phenomenon with real design implications.
- **SFT scaling harm (Table 8)**: Doubling mixed-quality SFT data yields −4.92% on math while marginal quality-targeted expansion (+0.4% samples) improves it; this is a clean, actionable negative result that challenges common scaling intuitions.
- **Full-pipeline evaluation through RL**: Extending the comparisons through GRPO-based RL (Table 3) demonstrates that the pretraining gap compounds rather than closes, making the compounding-returns argument concrete and compelling.

## Weaknesses

### Fatal
None.

### Major

1. **Repetition confound in diversity-vs.-quality comparison**: D_SHQ has 1.2M samples while D_LDQ has 268M. With a fixed 80B reasoning token budget, the model trained on D_SHQ must see the data roughly 66× (assuming ~1K tokens/sample), while D_LDQ is seen roughly once. The paper acknowledges the repetition but does not control for it or discuss the well-known degradation from high repetition rates. The observed inferiority of M_SHQ over M_LDQ may thus primarily reflect memorization/degradation from 66-fold repetition rather than a principled diversity vs. quality trade-off. This confound weakens the central asymmetric principle claim—though it does not fully invalidate the practical recommendation.

2. **Weak test of the "catch-up" hypothesis**: The catch-up hypothesis is tested by doubling SFT *epochs* (not tokens or unique samples) for M_base. Repeating the same SFT data more epochs is known to cause overfitting; a fairer test would be to provide M_base with 80B additional SFT tokens from D_SHQ, matching the token budget invested in pretraining reasoning data. The current test thus under-estimates the catch-up potential.

3. **RL comparison uses only two extreme models**: Table 3 reports RL results only for M_base+SFT_SHQ and M_LMQ+SFT_SHQ, omitting M_LDQ and M_SHQ variants. Since the main pretraining experiment trains four models, restricting the RL analysis to two extremes limits understanding of the RL phase and makes the +18.57% headline cherry-picked in the best-vs-worst sense.

### Minor

1. **No variance or confidence intervals reported**: With 16 or 4 evaluation runs per benchmark, standard deviations are available but never shown. For closely-spaced results (e.g., M_LMQ 64.07 vs. M_LDQ 64.09 in Table 1), knowing variance would distinguish signal from noise.

2. **Headline percentages are inconsistent with tables**: The abstract claims "+11% average gain" for diversity in pretraining, yet the most relevant comparison (M_LDQ 64.09 vs. M_SHQ 54.98 in Table 1) yields +9.11%. The provenance of the 11% figure is unclear.

3. **ALF as a quality proxy is ad hoc**: Filtering by answer length > 4096 tokens conflates verbosity with reasoning depth; no validation of this proxy against human-judged quality or model-judged correctness is provided.

4. **Architecture generalizability is narrow**: The 1.2B Transformer ablation (Table 14, mentioned but not shown in the reviewed text) is the only evidence outside the hybrid Mamba model, and it only verifies pretraining effects, not the asymmetric SFT finding.

### Trivial
None worth noting.

## Nice-to-Haves
- Ablation controlling repetition count independently of dataset size (e.g., compare D_SHQ with no repetition vs. D_LDQ sampled to the same 1.2M unique samples).
- Catch-up test with equivalent unique-token budgets rather than doubled epochs.
- RL results for all four pretraining variants to characterize whether the RL phase consistently amplifies the pretraining rank ordering.

## Novel Insights
The paper's most genuinely novel insight is the *latent activation* phenomenon: high-quality pretraining data whose immediate post-pretraining benefit is negligible (+0.02% for M_LMQ vs. M_LDQ) re-emerges as a +4.25% post-SFT advantage. This suggests that pretraining can install representational infrastructure that requires a targeted alignment signal to become behaviorally visible—a finding that cannot be attributed to conventional "more data is better" explanations and merits follow-up mechanistic analysis. The asymmetric diversity-vs.-quality principle (while confounded by repetition) also provides a concise and operationally useful heuristic for practitioners navigating data budget allocation across training stages.

## Suggestions
- Run a controlled repetition experiment: train M_SHQ-norep (D_SHQ seen once, remaining reasoning token budget filled with D_base) vs. M_SHQ-rep (current, 66× repetition) to isolate repetition from quality effects.
- Present the catch-up baseline with equal *unique reasoning tokens* (e.g., fine-tune M_base on 80B tokens of D_SHQ) to provide an apples-to-apples comparison.
- Add variance across benchmark runs in tables, even as ± std.
- Explore the latent effect mechanistically: do probing classifiers or activation norms differ between M_LDQ and M_LMQ before and after SFT?

## Score and Decision

The paper addresses a practically consequential question with unusually expensive end-to-end experiments and produces actionable findings across a well-designed ablation grid. The core narrative is broadly correct and supported by converging evidence, and the latent-effect and SFT-scaling-harm findings are novel. The major methodological concerns—the repetition confound and the weak catch-up test—reduce confidence in precise quantitative claims but do not invalidate the overall picture. For an empirical study paper at ICLR, the experimental investment and the directional robustness of the findings place this above the acceptance threshold.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>