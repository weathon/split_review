Now I have sufficient calibration data. Let me compile the final review.

**Calibration Summary:**

Round 1 bracket: **6.0 – 7.5**

Anchors across all rounds:
| Path | Avg Score | Round | Comparison to Paper |
|------|-----------|-------|---------------------|
| `v3DwQlyGbv` (Paramanu-Ganita) | 2.33 | R1 | Much weaker — narrow evaluation, poor methodology, no ablations |
| `Fq8tKtjACC` (phi-1) | 6.00 | R1/R2 | Weaker — single domain (code only), proprietary data details, lower methodological rigor |
| `1hQKHHUsMx` (What Kind of Pretraining Data) | 6.75 | R2 | Similar but narrower — interesting analysis but only 80 questions, blog-like style |
| `5BjQOUXq7i` (RegMix) | 7.20 | R2 | Comparable — cleaner method but narrower scope; our paper has broader contributions with slightly more loose ends |
| `KIPJKST4gw` (At Which Training Stage) | 7.25 | R2 | Similar level — focused analysis, clean but narrow; our paper is more ambitious |
| `07yvxWDSla` (Synthetic continued pretraining) | 8.00 | R1 | Stronger — cleaner contribution, better theoretical grounding |

**Final Score: 7.0 — Accept.** The paper sits between phi-1 (6.0) and RegMix (7.20), with broader contributions than phi-1 and comparable depth to RegMix. The methodological rigor (LOO analysis, influence scores, controlled comparison) and full open-source commitment are genuine strengths. The limitations (Qwen3 comparison asymmetry, limited mid-training evaluation) prevent it from reaching the 7.5+ tier but are addressable and do not undermine the core contributions.

---

## Summary
This paper presents a data-centric framework for training sub-billion-parameter language models with strong reasoning capabilities, using only ~4.2T pretraining tokens. The core contributions are: (1) a leave-one-out (LOO) analysis to identify which pretraining datasets most benefit reasoning, measured via curated capability-probing datasets; (2) an influence-score-based dataset re-weighting scheme extending AutoMixer to allocate token budgets across heterogeneous data sources; and (3) a data-model co-evolution strategy during mid-training that iteratively filters out low-influence samples. The resulting MobileLLM-R1 models (140M, 360M, 950M) are compared against OLMo, SmolLM, Qwen3, Gemma, and LLaMA baselines on reasoning benchmarks including MATH, AIME, GSM8K, HumanEval, and LiveCodeBench.

## Strengths
- **Rigorous leave-one-out (LOO) experimental design for isolating dataset contributions (Section 2.1.2, Figure 3):** The paper trains separate models from scratch, each excluding one candidate dataset, and measures NLL changes on curated capability-probing datasets. This is an expensive but scientifically clean design yielding interpretable, causal evidence. The finding that FineWeb-Edu (general web data) causes the largest cross-domain degradation while StarCoder benefits math more than OpenWebMath benefits code challenges commonly held views about data utility.
- **Benchmark-free data mixture optimization via cross-capability influence scores (Section 2.2, Figure 4, Equations 2–5):** The paper extends AutoMixer to compute influence scores linking training samples to capability-probing datasets built from training corpora, not benchmark test sets. Figure 4 demonstrates the resulting Datamix consistently achieves lower perplexity than uniform sampling across code, math, and knowledge benchmarks.
- **Controlled comparison isolating pre-training/mid-training from post-training effects (Table 2):** By fine-tuning all models on the identical joint reasoning SFT corpus, the paper cleanly disentangles the contribution of data curation from post-training data quality. MobileLLM-R1-950M achieves 57.8 MATH / 68.5 GSM8K / 13.7 LCBv6, substantially outperforming OLMo-2-1.48B (53.0 / 58.8 / 11.4) and SmolLM2-1.7B (41.4 / 50.5 / 7.4) despite having fewer parameters. This is the paper's single strongest piece of evidence.
- **Self-terminating data-model co-evolution with empirical convergence evidence (Section 3, Figure 5):** During mid-training, the paper iteratively discards samples with negative influence scores. Figure 5 shows influence score distributions narrowing dramatically from Stage 1 to Stage 2 with most samples converging to near-zero or negative values, providing a natural stopping criterion.
- **Commitment to full open-source reproducibility:** The paper discloses the complete set of open-source datasets used, releases trained model checkpoints and code, and describes the full training pipeline.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The comparison to Qwen3-0.6B confounds pretraining data efficiency with post-training recipe differences.** The headline claim is that MobileLLM-R1-950M matches Qwen3-0.6B on 11.7% of pretraining tokens, but Qwen3 likely uses a different (possibly RL-based) post-training pipeline. The controlled comparison in Table 2 — the paper's best evidence — does not include Qwen3. The paper should be more explicit about this limitation rather than treating the end-to-end comparison as evidence specifically about pretraining data efficiency. This does not invalidate the results but qualifies the strongest framing.
- **Mid-training evaluation is limited to MMLU (Figure 6).** Given the paper's central goal is reasoning, evaluating the mid-training data curation methodology only on MMLU (a factual knowledge benchmark) is narrow. Showing mid-training's effect on GSM8K, MATH, or HumanEval would directly support the claim that mid-training data curation specifically benefits reasoning.
- **Model architecture is not described in the main body.** For a paper emphasizing full reproducibility, the main body should at minimum state the architecture family, parameter counts per size, and reference the original MobileLLM architecture. All architectural details are deferred to Appendix A, leaving a gap in the main text.

### Trivial
- The distinction between ~2T unique tokens and 4.2T training tokens (due to resampling/reweighting) is stated in the abstract but could be presented more clearly and consistently throughout to avoid confusing readers about the data-efficiency argument.

## Nice-to-Haves
- The capability-probing datasets are constructed using Ask-LLM filtering from training corpora. While this genuinely avoids benchmark test-set contamination, the filtering model introduces an indirect optimization signal. A brief discussion of sensitivity to the choice of filtering model and threshold would strengthen the "benchmark-free" framing.
- Adding a clean summary table in the main body comparing MobileLLM-R1-950M directly to Qwen3-0.6B on all reasoning benchmarks, with tokens-trained clearly indicated, would anchor the paper's central thesis more firmly.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "benchmark-free" framing is misleading / creates train-test leakage:** The paper is transparent about constructing capability-probing datasets from training corpora via LLM filtering, and the probing datasets genuinely do not contain benchmark test questions. The concern about indirect supervision through the Ask-LLM filtering model is a reasonable subtlety but does not constitute a methodological flaw or misleading framing — the paper explicitly states the construction process in Section 2.1.1. Moved to Nice-to-Haves.
- **Harsh Critic: "R1" branding mismatch with SFT-based post-training:** The paper never claims to use RL; it explicitly describes an SFT-based post-training pipeline. The "R1" in the model name is branding, not a methodological claim. The paper's contribution is clearly about data curation for pre-training and mid-training. This is a naming nitpick, not a substantive weakness.
- **Harsh Critic: parser-garbled tables in Figures 8-9:** The garbled tables are parser formatting artifacts, not problems with the original paper. The original PDF submission would have clean, readable bar-chart figures and tables. This criticism is invalid.
- **Harsh Critic: influence-score methodology has unresolved circularity:** The concern that influence scores are computed from models trained on the domains being weighted is not a genuine circularity — it is how influence functions and AutoMixer work: you train reference models to compute influence. The paper uses separate domain-specialized models, not the main model. This is standard practice, not a flaw.
- **Harsh Critic: convergence claim is interpretively ambiguous / model may have overfit:** This is speculative. The paper shows empirical convergence in Figure 5 and downstream benefit in Figure 6. Alternative explanations are possible but the critic provides no evidence that overfitting rather than convergence is the correct interpretation. Removed as speculative.
- **Harsh Critic: missing related works (Phi, data pruning literature):** Removed per hard rules — cannot verify missing related works.
- **Harsh Critic: "no discussion of mid-training evaluation beyond MMLU":** Kept as a minor weakness in a more precise form above.
- **Harsh Critic: HumanEval is "not a reasoning benchmark per se":** The paper treats coding benchmarks as part of reasoning evaluation, consistent with common practice in the field (e.g., DeepSeek-R1, Qwen3 evaluations). Removed as scope nitpicking.
- **Strength Finder: generic strengths about "important problem" or "interesting question":** Removed as superficial — these do not cite specific paper content.
- **Harsh Critic: 4.2T vs 2T token confusion:** Kept as a Trivial weakness above.

## Novel Insights
The leave-one-out analysis in Section 2.1.2 produces a genuinely non-obvious finding: StarCoder (a code dataset) benefits math capability more than OpenWebMath (a math dataset) benefits code capability. This challenges the commonly held view that mathematical data disproportionately contributes to coding ability (cf. Lewkowycz et al., 2022) and has practical implications for how practitioners allocate training data budgets across domains.

## Suggestions
- Produce a clean summary table in the main body comparing MobileLLM-R1-950M directly to Qwen3-0.6B on all reasoning benchmarks, with pretraining tokens clearly indicated.
- Include at minimum the architecture family and parameter counts in the main body rather than deferring entirely to the appendix.
- Add a mid-training ablation on a reasoning benchmark (e.g., GSM8K or MATH) to complement the MMLU results in Figure 6 and directly support the paper's reasoning-focused claims.


MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>