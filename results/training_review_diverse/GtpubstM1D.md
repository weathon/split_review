Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper investigates how to improve mathematical reasoning in LLMs by strategically using **problem-solving data** (questions + reasoning steps) during **continued pre-training (CPT)** rather than reserving it all for supervised fine-tuning (SFT). Through controlled experiments on Llama2-7B, it establishes three main findings: (1) problem-solving data in CPT significantly outperforms general math corpora of the same size; (2) among four data synthesis methods, Tutorship Amplification (simulating a teacher correcting a student's mistakes) is most effective; and (3) CPT develops stronger mathematical reasoning from the same problem-solving data than SFT, particularly on hard multi-step problems. These insights culminate in JiuZhang-8B, a math-specific model trained on ~100B math tokens that matches or exceeds models trained on 1T tokens.

## Strengths

- **Systematic, well-scoped empirical investigation of problem-solving data in CPT (RQ1, Section 3):** The comparison between Base1 (math corpus only) and Test1–3 (mixture of math corpus + problem-solving data) holds total math tokens fixed and convincingly shows that problem-solving data yields substantially higher accuracy. The paper tests multiple mixture ratios, and the results are consistent across checkpoints with converging validation loss. This is the cleanest experiment in the paper and its main empirical contribution.

- **Meaningful comparison and identification of the best data synthesis method (RQ2, Section 4):** The paper implements four synthesis methods (Response Diversification, Query Expansion, Retrospective Enhancement, Tutorship Amplification) and compares them under the same CPT training setup. Tutorship Amplification achieves the highest accuracy across all four evaluation sets (average 47.0 vs. Base2's 44.0), and the gap is large enough (especially on Gaokao: 11.1 vs. 7.4) to be practically meaningful despite variable token counts. This provides a useful result for practitioners.

- **Detailed breakdown of CPT vs. SFT differences by data distribution and difficulty level (Section 5.2–5.3):** The paper goes beyond a single-number comparison, dissecting where CPT's advantage comes from. The finding that CPT's advantage over SFT is largest on hard multi-step problems (Table 3: Hard-CPT +4.47 on hard subset vs. Hard-SFT +1.99), and that both stages primarily improve easy-problem performance, gives actionable guidance for data preparation (prioritize challenging data for CPT).

- **JiuZhang-8B validates the paradigm's practical value (Section 6):** The resulting model matches or exceeds Qwen2.5-Math-7B (trained on 10× more tokens), DeepSeek-Math-7B, and even 70B-parameter models on multiple benchmarks, while maintaining general knowledge (MMLU 0.622 vs. Llama3-8B's 0.621). This demonstrates that the proposed CPT-focused strategy is more token-efficient than scaling up generic math pre-training data.

- **Careful decontamination and dataset selection:** The paper uses MinHash deduplication, removes contaminated documents, and selects evaluation sets (GAOKAO, ZHONGKAO) released after the base model's training cutoff, strengthening the validity of the reported results.

## Weaknesses

### Fatal

None. The reviewer's central claim that the CPT vs. SFT comparison is confounded by data repetition (that "CPT exposes problem-solving data ~14× vs. SFT 3×") is **factually incorrect**. In the CPT setup, the model processes ~105B total tokens across a mixture where problem-solving data constitutes only ~11.4% of the 63B unique tokens (48.3B general + 7.5B math + 7.2B problem-solving), yielding ~1.66 epochs of problem-solving data. Meanwhile, SFT trains for 3 full epochs (21.6B tokens) of problem-solving data alone. **SFT actually sees more problem-solving data than CPT**, so if anything, the data-repetition asymmetry understates CPT's advantage, not overstates it. The critic's "14×" figure arises from dividing total processed tokens (105B) by problem-solving tokens (7.2B) while ignoring that problem-solving data is only one component of the training mixture.

### Major

None. The remaining issues are addressable and do not threaten the paper's core claims.

### Minor

- **Unusual evaluation metric hinders external comparability (Section 2):** The paper selects the higher of zero-shot and few-shot accuracy per dataset, then averages these per-dataset maxima. This is applied consistently within the paper's own controlled experiments, so internal comparisons are valid. However, comparisons with external models in Table 4 (Qwen2.5-Math-7B, DeepSeek-Math-7B, etc.) may be inflated if those models were evaluated under a single standard protocol. Table 4 should clarify which prompting mode was used for each baseline or report both zero-shot and few-shot separately.

- **CPT vs. SFT comparison uses different hyperparameters (Section 5.1 vs. Section 3):** CPT uses batch size 1024 and LR 1e-4→1e-5, while SFT uses batch size 256 and LR 1e-5→1e-6. These differences are inherent to the stages being compared (CPT typically uses higher LR/larger batch than SFT), and the finding that CPT yields ~60% larger capability gain is practically meaningful. But a cleaner control (e.g., a grid over SFT learning rates) would strengthen the claim that the training stage itself, rather than hyperparameter selection, drives the difference. The paper should at minimum discuss whether SFT hyperparameters were tuned or whether the chosen ones are standard.

- **Synthetic data experiments lack a quantity-controlled baseline within the same method (Section 4):** The experimental groups add synthetic data on top of Base2, so each method group has more total tokens than the control. The comparison *across methods* (Tutor-Amp 30B vs. Retro-Enh 26B vs. Query-Exp 17B vs. Res-Div 10B) is informative, and Tutor-Amp's large advantage (47.0 avg. vs. Retro-Enh's 44.5 despite similar token counts) suggests genuine quality differences. However, adding an equivalent quantity of genuine (non-synthetic) problem-solving data as a control would make the "efficiency" claim about the synthesis method itself (vs. simply having more data) more robust.

- **Difficulty-level analysis lacks statistical testing (Section 5.3):** Key claims (e.g., Hard-CPT's +4.47 on the hard subset vs. Hard-SFT's +1.99) are based on single-run accuracy differences without significance tests or confidence intervals. Given the number of experimental conditions, some form of uncertainty quantification (even bootstrap estimates from multiple checkpoints) would strengthen the evidence.

### Trivial

- The SFT data-volume analysis (Figure 6, described in line 121) is referenced but the figure itself is not visible in the provided text.
- Some claims about "SFT is more susceptible to disturbances from data distribution" (Result 4) are presented as conclusions despite the paper itself acknowledging the conclusions are "less clear."

## Nice-to-Haves

- **Quantity-controlled baseline for synthetic data:** Adding an equivalent amount of real problem-solving data (or a random augmentation) as a control would cleanly separate the benefit of the synthesis *method* from the benefit of additional *quantity*.
- **Ablation over SFT hyperparameters:** A small grid over SFT learning rates and epochs would help rule out the possibility that SFT's underperformance is due to suboptimal tuning rather than the stage itself.
- **General-domain evaluation for all controlled experiments:** MMLU is reported only for JiuZhang-8B; reporting it for Base1/Test groups would confirm that math gains don't come at the expense of general ability in the controlled setting.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"CPT exposes problem-solving data ~14× vs. SFT's 3 epochs"** — REMOVED as factually wrong. The correct calculation: CPT processes ~105B total tokens across a mixture where problem-solving data (7.2B) is ~11.4% of the 63B unique tokens, yielding ~1.66 epochs. SFT trains for 3 full epochs (21.6B tokens of problem-solving data alone). SFT sees *more* problem-solving data, not less.

2. **"Straw-man: existing work focuses only on memorizing math knowledge"** — REMOVED. The paper characterizes the *prevalent paradigm* as focusing on math corpora during pre-training and reasoning during post-training (line 16). This is a reasonable characterization of the dominant approach; the paper does not claim no prior work uses problem-solving data in pre-training.

3. **"Missing limitations discussion"** — REMOVED. Section 7 explicitly acknowledges limitations: synthesis methods are "relatively naive" and alignment was not explored. The CPT/SFT confounding concern is addressed by the factual correction above.

4. **"Hyperparameter searches for SFT"** — MOVED from Harsh Critic's framing ("critical") to Minor/Nice-to-Have. The observation that SFT might underperform due to suboptimal hyperparameters is speculative and the paper's hyperparameter choices are standard for each stage.

5. **"Statistical significance or variance"** — DOWNGRADED to Minor. Single-run results are the norm for LLM training experiments at this scale due to cost, but the paper's multiple experimental conditions make the absence of any uncertainty quantification a genuine limitation.

6. **"General knowledge retention for controlled experiments"** — MOVED to Nice-to-Have. The paper reports MMLU for the final model; requesting it for all controlled experiments is reasonable but not essential.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel synthesis: the data-repetition asymmetry between CPT and SFT actually *favors the null hypothesis* (SFT sees more problem-solving tokens), making CPT's advantage *more* striking, not less. This reverses the critic's claimed fatal flaw into an argument that strengthens the paper. Additionally, the observation that both CPT and SFT primarily improve performance on easy problems regardless of training data difficulty (Section 5.3) is an interesting finding that deserves more attention than the paper gives it — it suggests that different mechanisms may be needed to improve hard-problem performance beyond simply providing more data.

## Suggestions

1. **Fix the evaluation metric for external comparisons:** Report both zero-shot and few-shot accuracy separately (or clarify which mode each baseline in Table 4 uses) so readers can make fair comparisons.
2. **Add an ablation experiment for synthetic data quantity:** Include a control that adds the same number of tokens as the best synthetic method (Tutor-Amp) using randomly augmented or duplicated real problem-solving data.
3. **Run a small grid over SFT learning rates** (e.g., 5e-6, 1e-5, 2e-5) to ensure the CPT vs. SFT comparison is not driven by suboptimal hyperparameters.
4. **Provide confidence intervals or bootstrap estimates** for at least the main comparisons (CPT vs. SFT overall, difficulty-level breakdowns).

## Score and Decision

This is a solid empirical paper that conducts a systematic investigation of an important question. The three research questions are well-motivated, the experimental design (particularly RQ1 and the synthesis method comparison) is sound, and the practical validation via JiuZhang-8B is convincing. The main weaknesses — an unusual evaluation metric that complicates external comparisons, a lack of full hyperparameter control between CPT and SFT, and the absence of quantity-controlled baselines for synthetic data — are meaningful but do not invalidate the core claims. None of the verified weaknesses are fatal; the claimed "fatal" confound about data repetition is mathematically incorrect. The paper makes a genuine contribution to understanding how to allocate problem-solving data across training stages.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>