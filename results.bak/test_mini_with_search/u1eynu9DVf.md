## Summary

This paper defines a novel problem: forecasting which upstream pretraining examples will be forgotten when a language model is fine-tuned to correct a specific error. The authors propose two approaches — an interpretable logit-change transfer model derived from NTK theory (works on BART but fails on T5) and a black-box representation-based model that consistently outperforms baselines. They demonstrate practical utility by replaying forecast-forgotten examples in model refinement, showing small reductions in forgetting compared to random replay. The problem formulation is clean and the work is the first to tackle pairwise example-level forgetting prediction in LMs.

## Strengths

- **Novel problem formulation with clear formalization.** Section 2 defines forecasting forgetting as a binary classification task over example pairs (online-learned error, upstream pretraining example), with explicit metrics (EM Drop Ratio, Edit Success Rate) and a train/test split. This goes well beyond prior work that only characterized forgetting-prone examples (Toneva et al., Maini et al.) without predicting which specific upstream example will be forgotten due to a given correction.

- **Representation-based forecasting model consistently outperforms baselines across setups.** Table 1 shows the black-box model (Eq. 5) achieves the highest F1 on every configuration (e.g., 65.77 vs. 55.75 threshold on BART0 full FT). It also generalizes to continual model refinement (Figure 3, stable precision) and its ablation without the frequency prior confirms the added value of learned pairwise interactions.

- **Replaying forecast-forgotten examples reduces forgetting in practice.** The model refinement results (Table 5) show that replaying examples predicted by the representation-based model reduces EM Drop to 1.6 % on BART0 (full FT) and 0.1 % on T5-XL, outperforming random replay (2.3 %, 1.0 %) and MIR (2.1 %, 1.7 %). The forecasting approach is also substantially more efficient at inference than methods requiring LM forward passes (Table 6).

- **NTK-inspired logit-change analysis provides a mechanistic hypothesis for forgetting.** Section 3.2 derives the relationship between logit changes of the online example and the upstream example from first-order Taylor expansion. Even though the simplified trainable kernel fails on T5, the derivation itself is principled and the honest reporting of its failure is a scientific strength.

## Weaknesses

### Major

- **Modest improvement over random replay with no reported statistical significance.** The key model refinement results (Table 5) show small absolute gains: representation-based forecasting reduces EM Drop from 2.3 % to 1.6 % on BART0 (full FT) and from 0.9 % to 0.6 % on FLAN-T5-LoRA. On T5-XL full FT, random and forecast replay achieve the same 0.1 %. No standard deviations, confidence intervals, or multiple-seed runs are reported anywhere in the paper. The central claim of "practical utility" rests on these small differences, which could be noise. This is the most important weakness to address.

- **Baseline comparisons for model refinement are weaker than they could be.** MIR is described as retrieving from "only subsets of upstream training examples" (Sec. 4), which is a deliberately constrained version. The paper does not compare against standard continual-learning replay baselines such as Experience Replay with reservoir sampling or DER++ (Buzzega et al., 2020), which are common in rehearsal-based CL. The comparison set makes the proposed method appear stronger than a full evaluation would show.

- **Training-inference mismatch weakens the practical-utility narrative.** The paper acknowledges (Sec. 2) that training the forecasting model requires ground-truth forgetting labels, which are obtained by the expensive process of fine-tuning on each error and running inference over the upstream set. The OOD generalization experiment (Sec. 5.1) is designed to address this, but the OOD F1 of 49.73 is only 3.5 points above the threshold baseline (46.24) and far below in-domain performance (~65–79). This gap is too small to convincingly show that a forecasting model trained on one set of tasks transfers usefully to unseen tasks without recalibration.

### Minor

- **The "partially interpretable" claim for the trainable logit-change model is overstated.** The paper replaces the NTK kernel with a learned kernel $\tilde{\Theta}$ parameterized by a trainable encoder $h$, which is itself a black-box LM (Sec. 3.2). The interpretability is limited to the structural resemblance to Eq. 3; the actual similarity measure $\tilde{\Theta}$ is neither simpler nor more transparent than direct black-box classification. The method also fails on T5. The claim should be qualified more precisely.

- **No ablation on the number or frequency of replayed examples.** The paper replays 8 examples every 10 steps (or 4 every 5 steps for T5-XL). Without analysis of sensitivity to these hyperparameters, it is unclear whether the benefit of forecasting is robust or whether random replay with a larger buffer could match performance.

- **Missing specification of the representation encoder $h$.** The paper states that $h$ is "a trainable LM" (Sec. 3.2) but does not specify its architecture, size, or how it relates to the base PTLM. This affects reproducibility and the computational cost analysis (Table 6 assumes abstract $H$ without grounding).

### Trivial

- The paper references tables by number (e.g., Table 1, Table 2) but these are input files (`tables/fgt_head`, `tables/fgt_mtl`, etc.) and their content is not visible in the extracted text. This is a parsing artifact.

## Nice-to-Haves

- Report precision-recall curves or AUC-PR for the forecasting task. The positive class (forgotten examples) is a small minority (1–10 %), making F1 at a fixed threshold sensitive to calibration; AUC-PR would be a more informative metric.
- Include wall-clock time or inference cost benchmarks for the full pipeline to ground the theoretical complexity analysis (Table 6) in practice.
- The threshold baseline could be strengthened by using per-example frequency (some upstream examples are forgotten more often) rather than a global frequency threshold. This would be a stronger control.

## Removed Points

These points were flagged by the reviewers but are removed from the main weaknesses as per the filtering rules:

- *"Missing comparison to rehearsal-free methods (EWC, SI, GEM)."* — The paper explicitly scopes itself as improving replay (Sec. 1: "we show that we reduce forgetting...by replaying examples that are forecasted to be forgotten"). Asking it to also compare to methods that avoid replay entirely is scope creep.
- *"The paper would benefit from tightening its claims to match the evidence."* — This is a general recommendation, not a specific weakness.
- *"The paper should compare to Experience Replay with reservoir sampling"* — Random replay is the standard reservoir-sampling baseline, and it is included. DER++ is a reasonable suggestion but the absence of a single additional baseline is a minor point, not a major one.
- *"OOD results are weak"* — This is factually correct but already covered under the training-inference mismatch weakness above. Duplication removed.
- *"No analysis of computational cost in practice (wall-clock times)"* — Moved to Nice-to-Haves; it would strengthen the paper but is not a core flaw.
- *"The training of the representation encoder h is not specified"* — This is kept in Minor above with a softer framing.
- Various formatting, style, and typo complaints — these are parser artifacts.

## Novel Insights

The harsh critic's observation that the paper's core practical claim is undermined by the training-inference mismatch is not present in the strength finder and goes beyond what the paper's own limitations section discusses. The paper acknowledges the mismatch in the problem formulation but does not grapple with how severe it is: the OOD generalization results (only ~3.5 F1 above threshold) are too weak to salvage the claim that a forecasting model trained on one set of tasks would transfer to new tasks in deployment without expensive ground-truth labeling. This insight sharpens the paper's own limitations discussion: the training-inference mismatch is not just an engineering inconvenience but a fundamental obstacle to the claimed practical utility, and future work should focus more on few-shot or zero-shot forecasting to close this gap.

## Suggestions

1. **Report multiple seeds with standard deviations** for all model refinement results (Table 5). Without this, the small improvements over random replay cannot be distinguished from noise.
2. **Add stronger baselines** for model refinement: at minimum, Experience Replay (reservoir sampling) with the same budget, and DER++ if feasible. Remove the weakened MIR variant or match its budget.
3. **Tone down the "interpretability" claim** for the trainable logit-change model to reflect that the learned kernel is itself a black box; the structural analogy to NTK is an insight but not an interpretable explanation.
4. **Add an ablation on replay buffer size** to show that the gains are not simply replicable by random replay with more examples.
5. **Provide AUC-PR** in addition to F1 for the forecasting task to handle class imbalance more honestly.

## Score and Decision

**Round 1 — Bracketing.** I queried for topically similar papers in three bands:
- Weak band (score ≤ 3): e.g., "Stop Before You Forget" (3.00, withdrawn/reject) — NTK-based continual learning with weak experiments and missing baselines; "Towards Understanding Continual Factual Knowledge Acquisition" (3.00, reject) — theoretical analysis with limited empirical validation.
- Middle band (score 4–7): e.g., "SuRe: Surprise-Driven Prioritised Replay" (4.50, reject) — LLM continual learning replay method with novelty concerns; "Mapping Post-Training Forgetting" (5.00, accept poster) — large-scale forgetting measurement study; "Retaining by Doing" (5.33, reject) — SFT-vs-RL forgetting analysis; "RL's Razor" (6.00, accept poster) — strong theoretical+empirical analysis of RL forgetting.
- Strong band (score ≥ 8): e.g., "Energy-Regularized Sequential Model Editing" (6.50, accept) — strong but not in the same topic; "LLMs Get Lost In Multi-Turn Conversation" (8.00, oral) — unrelated topic.

My initial bracket: **[4.5, 6.0]**.

**Round 2 — Narrowing.** I retrieved additional anchors inside the bracket:
- "Retaining by Doing" (5.33, reject) — similar in that both identify a novel angle on forgetting (on-policy data / pairwise forecasting) with clean experiments but modest practical impact. The current paper has a more novel problem formulation but less comprehensive evaluation.
- "Mapping Post-Training Forgetting" (5.00, accept poster) — similar in overall contribution level but different in nature (measurement study vs. method proposal). The current paper has more novel methodology but smaller empirical scope.
- "RL's Razor" (6.00, accept poster) — stronger paper with clearer causal mechanism and broader validation. The current paper is not at this level.

**Final score:** 5.0. The paper is comparable to the 5.0–5.33 anchors: it defines a genuinely novel problem with a clean formalization and reasonable methods, but the empirical results are modest, the baselines are weaker than ideal, and the practical claims outstrip the evidence.

**Decision:** Accept. The paper introduces a new and well-motivated problem, proposes working methods, and demonstrates utility in a practical setting. The weaknesses are serious but addressable, and the core contribution — pairwise forecasting of forgotten examples in LM refinement — is novel enough to warrant publication. The authors should address the major weaknesses (statistical significance, stronger baselines, honest framing of the training-inference gap) in a revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>