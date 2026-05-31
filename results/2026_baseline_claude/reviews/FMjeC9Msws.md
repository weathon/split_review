Now let me write the review based on my full reading of the paper.

---

## Summary

This paper presents the first large-scale systematic study of RL scaling laws for LLMs, spanning over 400,000 GPU-hours. The authors propose a sigmoidal compute-performance framework that fits reward versus log-compute curves and decomposes recipe quality into two interpretable axes: asymptotic performance (*A*) and compute efficiency (*B*). Through extensive ablations of common design choices, they derive SCALERL—a best-practice recipe combining PipelineRL, CISPO loss, FP32 logit precision, batch-level advantage normalization, zero-variance filtering, and no-positive-resampling. They then validate predictable scaling of SCALERL on a single 100,000 GPU-hour run, where curves extrapolated from early training closely match the final observed performance.

---

## Strengths

- **Scale and rigor of the empirical study.** 400k+ GPU-hours of controlled ablations across a consistent 8B base model and identical infrastructure is a genuinely extraordinary contribution. Each design choice is analyzed through the lens of (A, B) rather than a single-point metric, which is methodologically sound and reveals distinctions (e.g., loss aggregation and normalization shift *B* but not *A*) that smaller-scale studies would miss entirely.

- **Predictive framework well-suited to the domain.** The choice of a sigmoidal curve over a power law is well-motivated: pass rate is bounded in [0,1], so saturation is expected. The four-parameter form (A, B, C_mid, R_0) is interpretable, and the paper explicitly validates its extrapolative power—fitting on the first half of training and confirming alignment with the second half in every LOO experiment, as well as the flagship 100k run.

- **High-impact, concrete engineering finding.** The FP32 precision fix at the LM head is a remarkable result: changing precision at a single layer raises the asymptote from 0.52 to 0.61 (a +17% relative gain). This finding is independently actionable and likely transferable to any async RL pipeline where generators and trainers use different inference kernels.

- **Disentangling asymptote-shifters from efficiency-shifters.** The key insight—that most popular interventions (loss aggregation, advantage normalization, length penalty, curriculum) primarily modulate *B* rather than *A*—directly challenges the prevailing community assumption that these choices determine peak performance. This reframing has substantive value for how the community prioritizes future algorithmic work.

- **Leave-one-out ablations at 16k GPU-hours.** Rather than forward ablations alone, the LOO design (Figure 5) validates that each component of SCALERL remains beneficial in the presence of all others, lending credibility to the recipe as a unified whole rather than a collection of individually cherry-picked options.

- **Broader generalization of the framework.** The sigmoid framework extends cleanly to multiple scaling axes (model size, batch size, generation length, multi-task), and the extrapolations are consistently verified by extended runs (Figures 1, 6). In particular, the 17B×16 MoE run shows model-scale invariance of the methodology.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Extrapolation reliability is understated.** The paper's central claim is that curves fit from early training reliably extrapolate to large compute. However, the paper reports no uncertainty quantification (e.g., confidence intervals on A, B, predictions) for its fitted curves. The robustness discussion is deferred to appendices that are not accessible in this submission. Given that extrapolation is the core scientific claim, at least a brief quantification of prediction error as a function of the fraction of compute used for fitting would substantially strengthen the paper's empirical case.

2. **Cross-recipe comparison in Figure 2 may conflate recipe and data effects.** The figure compares SCALERL against DeepSeek (GRPO), Qwen-2.5 (DAPO), Magistral, and MiniMax-M1 recipes, all apparently reimplemented on the same base model. However, it is unclear whether the training *data* is also held constant across recipes (e.g., the MiniMax recipe may specify data-mixing strategies or curriculum choices beyond loss/normalization). If any recipe comparison incorporates data-specific choices from the original papers, differences in A could partially reflect data rather than algorithmic choice.

### Minor

1. **Fitting window sensitivity.** The paper states fits begin after ~1.5k GPU-hours to avoid the "warm-up" regime, but the sensitivity of A and B to this threshold is not reported in the main text. Whether A is stably estimated after 4k, 8k, or 16k GPU-hours is important for practitioners wanting to use early-stopping as a proxy for scalability.

2. **CISPO vs. GSPO interpretation.** Figure 4b shows CISPO is only "marginally better" than GSPO late in training, yet CISPO is selected. The justification is thin; a more principled explanation of *why* CISPO's prolonged near-linear phase is preferable (e.g., resistance to premature saturation) would help practitioners choose between the two.

3. **Downstream generalization gap.** The paper honestly notes (Section 7) that generalization from in-distribution validation to held-out benchmarks is not fully characterized. Some choices (e.g., batch size, generation length) seem to help downstream performance more than the in-distribution metric suggests, which hints at a systematic discrepancy the framework does not currently address.

### Trivial

- The SCALERL objective in Equation (5) uses `sG` (stop-gradient) notation inconsistently with the earlier `sg` in Equation (4).
- The LOO table in Figure 5 labels the midpoint parameter as `C_mad` rather than `C_mid`.

---

## Nice-to-Haves

- A brief analysis of how many GPU-hours of early training are *needed* to reliably predict A within, say, ±2 percentage points would make the framework immediately actionable for groups operating at academic scales.
- An investigation into whether the FP32 precision fix is specific to the generator/trainer split in async pipelines or whether it also matters in synchronous setups (e.g., PPO with vLLM rollouts).

---

## Novel Insights

The most genuinely novel insight in this paper—beyond the recipe itself—is the *asymptote-efficiency decomposition* applied to the RL design space. Pre-training scaling studies optimize for a single trajectory; this paper shows that in RL, two methods can follow qualitatively different trajectories where the better-performing method at low compute is eventually overtaken ("embracing the bitter lesson," Figure 2). Detecting this crossover early via sigmoidal fits is non-obvious and practically important: it means that standard benchmarking practices in RL (compare methods at matched compute) systematically biases toward methods with high B at the expense of methods with high A. Separately, the FP32 precision result demonstrates that numerical housekeeping at the IS ratio level is a first-order concern for RL scaling—an insight that is not present in any prior RL-for-LLM study at this scale.

---

## Suggestions

- Report 95% bootstrap confidence intervals on fitted A and B for at least the main SCALERL run and Figure 2 comparisons, so readers can assess extrapolation uncertainty.
- Provide a brief table or figure in the main paper showing how A and B estimates stabilize as more training compute is included in the fit (addressing the fitting-window sensitivity concern).
- Clarify in the Figure 2 caption whether training data and data-sampling strategies are also held constant across all recipe comparisons.

---

## Score and Decision

The paper addresses a genuine and pressing gap in the RL-for-LLMs literature: unlike pre-training, no principled scaling methodology existed for RL compute. The study is executed at impressive scale with rigorous leave-one-out validation, the sigmoid framework is well-motivated and practically validated, and the FP32 precision finding alone represents a significant empirical contribution. The main limitation—absent uncertainty quantification on extrapolated predictions—is a substantive but correctable omission. The recipe novelty is modest (SCALERL combines existing components) but the *methodology* for identifying and validating scalable recipes is the primary contribution, and it is solidly established. This work will have direct impact on both industrial RL practitioners and academic researchers trying to compare RL methods cost-effectively.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>