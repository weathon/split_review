Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Selective Knowledge Transfer (SKT), a framework for few-shot continual learning (FSCL) with language models that uses transferability measures (LogME) to select the most relevant prior tasks and aggregate their parameters via weighted averaging. The authors instantiate SKT as Log-evidence Progressive Prompts (LePP), an enhancement of Progressive Prompts. Experiments on short-stream and long-stream NLP benchmarks across BERT, T5-small, and T5-large show consistent improvements over existing baselines, with gains of 1–4.5% in average accuracy.

## Strengths

- **First principled application of transferability measures to task selection in continual learning with LMs.** The paper is the first to leverage LogME — or any transferability estimator — to select prior tasks for forward transfer in prompt-based CL. This is a well-motivated departure from prior work that treats all prior tasks equally or requires training per-task keys/probe prompts (Section 1, Section 5).

- **Consistent and non-trivial performance gains across multiple backbones, dataset sizes, and task orders.** The improvements hold across BERT-base, T5-small, and T5-large with 10, 20, and 100 samples per class, and across both short and long task streams (up to 4.46% over Progressive Prompts on T5-small, 1.73% on T5-large). All results are averaged over 5 runs with random task orders.

- **Computationally efficient selection mechanism.** Unlike prior methods that require training task-specific representations (e.g., probe soft prompts or task keys with backward passes), LePP computes transferability scores via a single forward pass per trained prompt (Section 3.2). This design choice directly addresses a scalability bottleneck in prior PEFT-based CL approaches.

- **Comprehensive ablation studies validate each design choice.** Figure 3a shows that selecting the *most transferable* tasks outperforms random, most-recent, and least-transferable selection. Figure 3c demonstrates that using an appropriate number of prompts (K ≈ 5–7) outperforms using all prompts, confirming the core motivation that irrelevant prior tasks degrade performance. These ablations directly support the paper's central claims.

- **Automatic discovery of interpretable task correlations.** Table 3 shows that LogME autonomously identifies meaningful task similarities (e.g., the same-domain tasks being selected more frequently for related target tasks) that align with human intuition. This provides a useful interpretability axis beyond raw accuracy gains.

## Weaknesses

### Fatal

None.

### Major

- **No error bars, confidence intervals, or significance tests for any result.** Tables 1 and 2 report averages over 5 runs but provide no standard deviations. The claimed improvements range from 1% to 4.5% — a meaningful range but precisely the regime where run-to-run noise could affect conclusions, especially in few-shot settings (10–100 samples per class) where small training set fluctuations can shift outcomes. Without variance estimates, the reader cannot assess whether the margins are systematic or stochastic. This is the single most impactful missing piece: it prevents the central claim ("surpassing existing baselines") from being fully supported.

- **Selective omission of closely related baselines (AdapterCL, PTCC).** The paper mentions AdapterCL (Madotto et al., 2021) and PTCC (Zhang et al., 2024b) in Section 5 as PEFT-based CL methods and even critiques their limitations, but neither is included as an experimental baseline in Section 4.1 or Tables 1–2. PTCC is particularly relevant because it also uses task similarity to recalibrate prompt weights — the closest competitor to LePP's own motivation. Excluding these methods leaves a gap in the evidence that LePP advances the SoTA. The authors should either include them or provide a concrete argument (e.g., incompatible evaluation settings) for why fair comparison is infeasible.

- **Unsupported claim about cross-modality / image data.** The contributions list (Section 1) states "we show that SKT can work with different data modalities including images," and the Conclusions claim the framework works for "NLP and CV." However, the paper presents zero experiments on image data. The Limitations section does not qualify this claim either. This overstates the paper's demonstrated scope and should be either removed or accompanied by experimental evidence.

### Minor

- **LogME reliability on few-shot training sets is not analyzed.** The transferability score for each prior prompt is computed on the current task's tiny training set (10, 20, or 100 samples per class). LogME is designed for feature-label compatibility estimation, but its stability and accuracy in such small-sample regimes are not established. The paper provides no analysis (e.g., comparing selections made with 10 vs. 100 samples, or training vs. validation data) to show that the top-K prompts identified are robust. If the selection is noisy, the weighted aggregation step inherits that noise. This is a methodological gap that should be addressed or at least acknowledged as a limitation — it is currently absent from the Limitations section.

- **No analysis of forgetting / Backward Transfer.** The paper reports only Average Accuracy (AA). Since Progressive Prompts is already strong at preventing forgetting, showing that LePP does not harm BWT (or improves it) would significantly strengthen the paper. Reporting BWT is standard practice in CL and would give a more complete picture of the method's behavior.

- **No compute cost comparison despite efficiency claims.** The paper repeatedly claims computational efficiency (Section 1, Section 3.1) but provides no wall-clock time, FLOPs, or parameter-count comparison against baselines. A brief table showing training time per task would make the efficiency claim concrete and verifiable.

- **Independence assumption in prompt selection not discussed.** Transferability scores are computed for each prior prompt independently, but during training the selected prompts are aggregated via weighted averaging. The paper does not discuss whether two individually high-scoring prompts might have overlapping information, reducing the marginal benefit of including both. This is a caveat worth acknowledging.

### Trivial

None.

## Nice-to-Haves

- Report Backward Transfer (BWT) in addition to AA to quantify forgetting.

- Provide a wall-clock time or FLOPs comparison to substantiate the efficiency claims.

- Conduct a stability experiment for LogME-based selection across different training set sizes (10 vs. 100 samples) to show that the selected top-K prompts are consistent.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Incomplete Algorithm 1"** (harsh critic, Section-by-Section Notes): The parsed text truncates Algorithm 1 after line 2, but this is a parser formatting artifact — the full algorithm exists in the original PDF. Removed per rule on parser artifacts.

- **"No standard deviations in Tables" already covered** — kept as the first major weakness, reformatted appropriately.

- **"Figure 3 analysis" and "Table 3 content garbled"** — these are parser artifacts affecting figures/tables that exist in the original PDF.

- **Strength Finder's claim about "generality across modalities"** — the architectural generality (BERT, T5) is valid, but the claim about image/cross-modality generality is unsupported and conflicts with the verified weakness above. Modified to remove the unsupported modality claim.

- **Strength Finder's claim that "All results are averaged over 5 runs, demonstrating robustness"** — averaging over 5 runs without reporting variance does not by itself demonstrate robustness. Adjusted to note this limitation.

## Novel Insights

None beyond the paper's own contributions. The two independent reviews converge on the same assessment: the core idea is novel and well-motivated, but the empirical validation has significant gaps (no error bars, missing baselines, unsupported cross-modality claim) that prevent full confidence in the results.

## Suggestions

1. **Add standard deviations (or confidence intervals) to all main results (Tables 1, 2, Figure 2).** This is the single highest-impact fix. Running 3–5 additional seeds (or using the existing 5 runs) and reporting mean ± std would transform the paper from "potentially correct" to "convincingly demonstrated."

2. **Include AdapterCL and PTCC as baselines, or provide a concrete justification for omission.** These are the most closely related methods, and the paper currently critiques them without comparing against them.

3. **Remove or substantiate the cross-modality/image claim.** Either provide image experiments or drop the claim — the paper's NLP contributions stand on their own.

4. **Add a brief analysis of LogME stability on few-shot data** (e.g., the overlap of top-K prompts selected with 10 vs. 100 samples per class, or using training vs. held-out data).

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>