Now let me perform calibration searches to anchor the score.Now let me narrow within my initial bracket of 6–7.5:Now I have enough information to write the final review. Let me compile everything.

---

## Summary

This paper conducts the first systematic, large-scale empirical study of how reasoning data—varying in scale, diversity, and quality—affects LLM performance when injected at different training stages (pretraining, SFT, RL). Training four 8B hybrid Mamba-2/attention models from scratch on 1T tokens using 512 H100s, the authors find: (1) front-loading reasoning data into pretraining creates durable, compounding advantages that SFT alone cannot replicate; (2) an asymmetric allocation principle holds—diversity/scale dominate pretraining while quality governs SFT; (3) high-quality pretraining data has latent effects activated only after SFT; and (4) naively scaling SFT with mixed-quality data is harmful.

---

## Strengths

- **Compounding advantage of front-loading, strongly supported by Tables 2–4.** Models pretrained with any reasoning data (M_res) outperform the baseline after SFT by 9.3% on average (Table 2). Doubling SFT epochs for M_base gains +4.09% but still falls 3.32% behind the weakest reasoning-pretrained model M_SHQ (Table 4). The RL phase amplifies the gap to 18.74% overall, with +39.32% on AIME-24/25 (Table 3). This refutes both the catch-up hypothesis and the overfitting hypothesis in a systematic way across all training stages.

- **Asymmetric allocation principle: diversity drives pretraining, quality governs SFT, with clear quantified evidence.** M_LDQ beats M_SHQ by +9.09% average post-pretraining (Table 1), with +28.4% in math. At the SFT stage, fine-tuning on diverse D_LDQ degrades reasoning-pretrained models by 13.45% versus fine-tuning on high-quality D_SHQ (Table 5). The directional asymmetry is consistent across all model variants.

- **Discovery of latent gains from high-quality pretraining data, activated only after SFT (Table 1 vs. Table 4).** M_LMQ and M_LDQ are virtually tied at pretraining (64.07 vs. 64.09, Table 1), but after identical SFT on D_SHQ, M_LMQ leads by +4.25% (50.95 vs. 46.70, Table 4). This is the paper's most novel finding: high-quality tokens embedded in a diverse pretraining mix act as a latent amplifier whose value only manifests during alignment.

- **Quantified harm of naive SFT scaling, with Table 8 as concrete evidence.** Doubling D_LDQ in SFT yields negligible average gain but -4.92% in math accuracy (Table 8, rows 1–2). Adding 0.4% high-quality D_ALF* improves average and math, showing quality-driven micro-expansion beats quantity-driven bulk scaling.

- **Unusually large-scale, carefully controlled experimental design.** All three reasoning-pretrained models receive a constant 80B reasoning tokens during pretraining (via the 80/20 ratio on the last 400B tokens), and all SFT runs use a uniform 4.8M samples. Four 1T-token pretraining runs on 512 H100s represent a significant and reproducible resource commitment. Results on a 1.2B Transformer (Table 14) confirm the front-loading effect generalizes across architectures.

---

## Weaknesses

### Fatal
None.

### Major

- **Repetition confound undermines the pretraining quality-vs-diversity comparison.** D_SHQ contains 1.2M samples. The paper states explicitly (Section 2.3): *"When a reasoning dataset is small, it is repeated so that the model still observes the same total volume of reasoning tokens."* At 80B reasoning tokens and ~1K tokens/sample, D_SHQ must be repeated roughly 50–70×, while D_LDQ (268M samples) requires far fewer repetitions to fill the same token budget. This means M_SHQ is trained on massively repeated data while M_LDQ is not—an independent variable that correlates perfectly with the quality/diversity distinction. The paper's central pretraining conclusion—"diversity matters more than quality"—cannot be cleanly attributed to diversity alone when the alternative explanation is that repetition rates are wildly unequal. The paper mentions repetition as an implementation detail but never acknowledges or discusses this as an experimental confound. To isolate the diversity effect, either D_SHQ should be scaled up to avoid heavy repetition, or D_LDQ should be subsampled to equalize repetition rate before comparison.

- **Budget-equivalence framing (Eq. 2) is not fulfilled by the actual experiments.** The paper frames its core optimization in Eq. 2 with a total reasoning budget constraint B = |D_res^PT| + |D_res^SFT|. In practice, all reasoning-pretrained models receive 80B reasoning tokens in pretraining, and the "catch-up" experiment simply doubles SFT epochs (approximately 9.6M samples), which represents a far smaller token intervention than 80B pretraining tokens. The evidence therefore shows that doubling SFT steps cannot compensate—which is still a useful finding—but it does not demonstrate the stronger claim implied by the budget framing: that an equal-token reallocation from pretraining to SFT would fail to close the gap. The framing overpromises what the experiments actually test.

### Minor

- **Variance and statistical significance are absent throughout.** The paper reports pass@1 averaged over 16 runs for AIME and 4 runs for other benchmarks (Section 3.2), but provides no confidence intervals, standard deviations, or significance tests anywhere. The latent effect—the paper's most novel claim—rests on a single +4.25% difference between M_LMQ and M_LDQ after SFT (Table 4). On AIME, where pass@1 scores are low and run-to-run variance is high, differences of 2–5% may not be reliably distinguishable from noise. Variance reporting is necessary to assess which findings are robust.

- **RL comparison uses only two extreme models.** Table 3 compares only M_LMQ + SFT_SHQ + RL versus M_base + SFT_SHQ + RL. Intermediate models (M_LDQ, M_SHQ) are excluded. The claim that "pretraining strategy dictates the final accuracy ceiling" is an extrapolation from a two-point comparison; whether the relationship is monotonic or has diminishing returns across the four pretraining configurations is unknown.

- **SFT repetition confound in Table 5.** D_SHQ has 1.2M samples but SFT runs use 4.8M total samples, implying ~4× repetition when D_SHQ is used alone. The degradation observed with D_LDQ in SFT could partly reflect appropriate dataset scale (D_LDQ subsampled, not repeated) versus the repetition of D_SHQ. The conclusion "SFT is dominated by data quality, not diversity" is directionally plausible but shares the same confound as the pretraining comparison.

### Trivial
- The abstract's "11% average gain" for diversity is computed across different conditions (base model evaluations) without a precise definition in the abstract itself. Similarly, "19% average gain" refers to a single model pair (M_LMQ + SFT_SHQ + RL vs. M_base + SFT_SHQ + RL) rather than an average across pretraining strategies. The phrasing could be more precise.

---

## Nice-to-Haves

- A budget-controlled catch-up experiment where M_base receives the same total reasoning token count as M_LDQ (shifting 80B tokens from pretraining to SFT) would make the core argument unambiguous and fulfill the Eq. 2 framing.
- The latent effect finding (§5, Table 4) deserves deeper treatment: benchmark-level breakdown of where the +4.25% appears, and whether it is concentrated in math, science, or code would help characterize its scope.
- Table 6 shows 60/40 pretraining outperforms 80/20. A fuller interaction test—does the optimal SFT recipe change under 60/40 pretraining?—would strengthen robustness of the asymmetric principle.
- Section 4 briefly mentions the 1.2B Transformer result (Table 14) as confirming the front-loading effect but does not discuss it in the main text. Even a sentence on the qualitative agreement would strengthen the generalizability claim beyond the hybrid Mamba-2 architecture.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"M_LMQ as balanced diversity with quality" mischaracterizes the data (Harsh Critic, Section 2.2):** The critic notes D_LMQ is 99.6% D_LDQ and calls the "balanced" framing debatable. While technically accurate that D_SHQ is only 0.4% of D_LMQ, the paper itself eventually clarifies this and the description serves to communicate the intent of the mix, not a precise ratio. The paper does not seriously mislead readers here; this is a mild presentation imprecision, not a substantive misrepresentation.

- **Related work on "math-centric" RL evaluation (Harsh Critic, Section 6):** The critic notes the paper's own RL results are also primarily evaluated on math (AIME). However, the RL comparison in Table 3 also includes MMLU, MMLU-Pro, GPQA-Diamond, LiveCodeBench—it is not exclusively math. The criticism is weakened by the actual breadth of RL evaluation.

- **Strength: "controlled experimental design with fixed budget"** (Strength Finder, supporting strength 1): While the pretraining token budget per reasoning dataset is indeed fixed, as noted above this framing is partially undercut by the budget equivalence gap in the SFT catch-up experiment. This strength is partially retained but should be understood as "controlled pretraining token budget."

- **Strength: "broad evaluation coverage across training stages"** (Strength Finder, supporting strength 2): Retained in modified form—coverage is genuinely broad and includes math, science, code, general reasoning, and instruction-following. However, the RL evaluation is thinner (two models only) relative to what the SFT analysis covers.

---

## Novel Insights

The latent amplification effect—where high-quality pretraining tokens embedded in a diverse mix yield no immediate benefit but unlock a measurable advantage (+4.25%) only after SFT alignment—is the paper's most genuinely novel observation. It suggests that pretraining and SFT do not merely sum their effects additively, but that pretraining can install latent capacity that SFT then "keys into." If confirmed with statistical significance and mechanistic probing, this has important implications: the optimal pretraining corpus cannot be evaluated by base-model performance alone, and the value of data quality at pretraining stage is systematically underestimated by checkpoint-time evaluation. The asymmetric principle (diversity early, quality late) is a clean and practically actionable distillation supported across the full pipeline.

---

## Suggestions

1. Report confidence intervals or standard deviations alongside all main results, especially for AIME-based scores where pass@1 variance is high.
2. Add a token-matched catch-up experiment: give M_base a proportionally larger SFT budget (matching 80B pretraining reasoning tokens) and test whether the gap closes—this is the experiment that Eq. 2 actually promises.
3. Explicitly discuss the repetition rate disparity between D_SHQ and D_LDQ in the pretraining comparison, and include a qualitative analysis of its likely impact (or run a smaller-scale controlled replication with equalized repetition rates).
4. Include intermediate models (M_LDQ, M_SHQ) in the RL comparison table to characterize whether the pretraining quality–RL performance relationship is monotonic.

---

## Score and Decision

**Round 1 bracket:** Based on the closest anchors, the paper sits between 6 and 7.5. KIPJKST4gw.md (7.25, "At Which Training Stage Does Code Data Help LLMs Reasoning?") is nearly identical in spirit but uses smaller models without RL; GtpubstM1D.md (5.71) covers similar ground with more confined scope and higher variance reviews.

**Round 2 narrowing:** Within 5.5–8: 3OyaXFQuDl.md (7.00, "Smaller, Weaker, Yet Better") is a methodologically tight compute-optimal sampling study; oqsQbn4XfT.md (5.80, "Diversity of Synthetic Data") is lower-scale with smaller models. The paper under review exceeds 5.80 clearly on scale, novelty (latent effect), and the RL compounding result. It is comparable to KIPJKST4gw (7.25) in scope and contribution, but the repetition confound and missing variance reporting are more significant issues than KIPJKST4gw's weaknesses. The paper is slightly below 3OyaXFQuDl (7.00) in methodological tightness but broader in scope.

**Anchor comparisons:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| KIPJKST4gw.md | 7.25 | 1 | Most similar question; paper under review is larger scale/more novel but has confounds → slightly below |
| GtpubstM1D.md | 5.71 | 1 | Narrower scope, more review variance; paper under review is clearly better |
| 1hQKHHUsMx.md | 6.75 | 1,2 | Different method (influence functions) but related question; paper under review has larger practical scope |
| 3OyaXFQuDl.md | 7.00 | 2 | Tight methodology but narrower; paper under review is more ambitious but has confounds → comparable |
| oqsQbn4XfT.md | 5.80 | 2 | Smaller scale, similar diversity question; paper under review is clearly better |
| eNbA8Fqir4.md | 6.00 | 2 | Different domain (data management), lower contribution |

**Final score rationale:** The paper makes a real and unusually large-scale contribution to an important question. The asymmetric principle and latent effect are novel. The RL compounding result is practically significant. The major confound (repetition rate) and missing variance reporting prevent a score in the 7–7.5 range; the paper's scale and coherence push it above 6.0. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>