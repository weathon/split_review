- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a complete understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper presents Batch Calibration (BC), a zero-shot, inference-only method for calibrating LLM predictions in in-context learning. BC works by estimating the "contextual bias" — the mean model output over a test batch — and subtracting it from individual predictions as an additive correction in log-probability space. The paper first provides a systematic analysis of prior calibration methods (CC, DC, PC) through the lens of decision boundaries, identifying failure cases that motivate BC. Experiments on 13 NLU tasks with PaLM 2 (S, M, L) and 3 image tasks with CLIP show that BC improves average accuracy over uncalibrated ICL and prior calibration methods while requiring no additional forward passes. The paper also introduces BCL, an adjustable variant that learns a single strength parameter from labeled data.

## Strengths

- **Consistent accuracy gains across diverse NLU tasks (Table 1).** BC achieves the highest average accuracy on both PaLM 2-S (74.41% vs 67.65% for PC, the best prior method) and PaLM 2-L (81.09% vs 77.83% for CC). These gains are substantial and consistent across 13 tasks spanning sentiment, NLI, paraphrasing, and commonsense reasoning. The improvements are 8% and 6% over uncalibrated ICL on S and L respectively.

- **Zero-shot inference with no additional forward passes.** Whereas CC requires 1+1 forward passes and DC requires 20+1, BC uses the single forward pass already computed for ICL (Table 1, analysis table). The computation is a simple additive correction on the output logits — negligible overhead.

- **Systematic decision-boundary analysis of prior methods (Section 3).** The paper derives CC as a rotation, DC as a translation, and PC as a non-linear boundary of the ICL decision boundary, then visually demonstrates failure cases (e.g., content-free tokens causing bias in multi-sentence tasks like QNLI). This analysis is clear and genuinely motivates the design of BC (linear boundary + content-based bias estimation).

- **Sample efficiency (Figure 5/fig:batch).** BC achieves strong performance with ~10 unlabeled samples, while PC requires over 500 samples to stabilize. This is a significant practical advantage.

- **Robustness to prompt engineering (Figure 4).** BC maintains consistent accuracy across different ICL choices, orders, prompt templates, and unconventional verbalizers (e.g., emojis). The paper convincingly shows that BC reduces prompt brittleness and makes prompt engineering easier.

- **Cross-modal generalization to vision-language models (Figure 3).** BC improves zero-shot CLIP by 12% on average over the uncalibrated baseline across SVHN, EuroSAT, and CLEVR, demonstrating that the method transfers from language-only to vision-language settings without modification.

## Weaknesses

### Fatal

None.

### Major

- **The CLIP experiments lack calibration baselines.** BC is compared only against raw, uncalibrated zero-shot CLIP. Established calibration techniques for vision-language models exist (e.g., learned temperature scaling, prompt ensembling, CoOp/CoCoOp, contextual optimization). Without any comparison to VLM-specific calibration methods, the VLM results are suggestive but not conclusive — the 12% improvement could partly reflect that raw CLIP has high bias and any reasonable calibration helps. This gap weakens the claim that BC is a "generalizable solution" across modalities.

- **The "unifies prior approaches" claim (abstract, line 4) is misleading.** The paper shows that CC performs a rotation of the decision boundary, DC performs a shift, and BC also performs a shift. That does not constitute "unification" — BC is one specific calibration strategy (additive shift using the batch mean), not a framework that subsumes CC or DC. The systematic analysis provides a unified *perspective* on prior methods, which is a separate contribution. The abstract's phrasing should be corrected.

### Minor

- **No discussion of BC's own limitations or failure regimes.** The paper thoroughly analyzes failure cases of CC, DC, and PC, but never discusses when BC might hurt. Since BC subtracts the batch mean from every sample, it relies on the assumption that the test batch's class distribution approximately reflects the unbiased LLM's predictions. This assumption can fail under severe class imbalance, out-of-distribution test sets, or very small batches. The paper would benefit from honest acknowledgment of these boundary conditions.

- **Statistical significance is not assessed.** Results are reported as means and standard deviations over 5 seeds. On several tasks, BC's performance overlaps with baselines within one standard deviation (e.g., SST-2, BoolQ on PaLM 2-S; QQP, COPA on PaLM 2-L). Without significance tests or confidence intervals, it is unclear whether improvements on individual tasks are reliable or due to random variation in the few-shot example selection.

- **"Zero-shot" terminology should be qualified.** BC requires a batch of test samples to compute the mean correction term. The paper does discuss a running estimate (lines 149-153), but the standard usage of "zero-shot inference" typically implies per-instance prediction without any batch-level statistics. Practitioners deploying BC on a single test sample would need to accumulate samples first. Clarifying this as batch-level zero-shot would prevent confusion.

- **The "state-of-the-art" claim is based on average rank, not uniform superiority.** On several tasks in Table 1 (SST-2, MRPC, BoolQ on PaLM 2-S; QQP, BoolQ, COPA on PaLM 2-L), a baseline ties or exceeds BC's accuracy. The paper appropriately uses average rank, but the framing as "state-of-the-art" (used in the abstract and conclusion) could be read as stronger than the evidence supports.

### Trivial

- None that are worth listing. (The critic's note about axis-label clarity in the batch-size figure is addressed by the caption stating "different sizes of an initial unlabeled set.")

## Nice-to-Haves

- A synthetic or controlled experiment that isolates the effect of class-imbalanced test batches on BC's performance, to honestly delineate the method's failure regime.
- A comparison with a "class prior" correction baseline (subtracting the training label distribution) on the NLP side, to test whether BC's batch-mean does more than just correct for class imbalance in the demonstrations.
- Details on how the 5 in-context examples were selected for each task (e.g., random with a fixed seed, stratified by class).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The core assumption of additive constant bias is never explicitly stated"** — Reduced scope. The assumption is implicit in the method (subtracting the batch mean from every sample is indeed an additive, input-independent correction). The paper's mathematical formulation in Eq. 1–2 and the decision-boundary derivation in Section 3 make this clear. The real issue is the absence of *discussion* of when this assumption breaks, which is kept as a minor weakness above.

2. **"PC boundary analysis missing hard evidence"** — The paper explicitly says "We hypothesize" (line 106), and the hypothesis is validated by the empirical results in Table 1 (PC exhibits large standard deviations). This was never presented as a proven claim, so it is not a weakness.

3. **"Batch size axis missing units"** — The caption says "different sizes of an initial unlabeled set," which clearly states what the axis represents. This is a parser artifact or an overly picky reading.

4. **"BCL shows minimal gains"** — The paper describes BCL gains as "further slight gains, 1% on average" and does not present BCL as a core contribution. This is an accurate self-assessment, not a weakness.

5. **"Missing related works"** — Cannot be verified without external sources. Removed per instructions.

6. **"Missing appendix/reproducibility details"** — The paper reports mean and std over 5 random seeds. The exact selection of ICL examples is not detailed, which is noted as a Nice-to-Have rather than a weakness.

## Novel Insights

Beyond the paper's own contributions, the reviews reveal an interesting tension: the paper's central strength (simplicity and generality of the batch-mean correction) is also the source of its least-examined vulnerability. The method works because it trades theoretical guarantees for empirical robustness — the batch mean is an unbiased estimator of the contextual bias only under strong assumptions (additive, input-independent bias) that are never verified. Yet the empirical evidence across 16 tasks, two model families, and two modalities is strong enough to suggest that either these assumptions hold approximately in practice, or the method is robust to their violation. A clearer articulation of which regimes cause BC to fail would sharpen the paper's contribution significantly and is the single most impactful thing the authors could add.

## Suggestions

1. **Add at least one VLM-specific calibration baseline** (e.g., temperature scaling on CLIP's logits, or prompt ensembling) to the CLIP experiments. This would substantiate the claim of cross-modal generality.
2. **Correct the "unifies prior approaches" framing** — tone it down to: BC extends the linear-decision-boundary family that CC and DC belong to, while avoiding their content-free-token pitfalls.
3. **Add a Limitations subsection** explicitly discussing when BC might degrade performance (e.g., skewed test distributions, OOD batches, very small batches).
4. **Report statistical significance** (e.g., bootstrap confidence intervals or paired t-tests over the 5 seeds) for the average improvement, especially on tasks where standard deviations overlap.
