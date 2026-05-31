## Summary

MobileLLM-R1 is a series of sub-billion-parameter reasoning language models trained using a fully open-source data-centric recipe. The central claim is that strong reasoning abilities can emerge with far fewer training tokens than commonly assumed: the 950M-parameter flagship model, trained on 4.2T tokens drawn from ~2T curated open-source data (11.7% of Qwen3's 36T corpus), matches or surpasses Qwen3-0.6B on multiple reasoning benchmarks. The authors contribute (1) a leave-one-out (LOO) analysis to identify which data sources are most impactful per reasoning domain, (2) a cross-capability self-influence framework for principled dataset-level sampling-ratio assignment, and (3) a mid-training data-model co-evolution paradigm that iteratively filters low/negative-influence samples.

---

## Strengths

- **Token-efficiency claim is well-supported:** The AIME 2024 score of 15.5 for MobileLLM-R1-950M against 0.6/0.3 for OLMo-2-1.48B and SmolLM2-1.7B (both larger models trained on more data) is striking. The FLOP comparison in Figure 1 reinforces this: MobileLLM-R1-950M reaches ~45% HumanEval at ~25×10¹⁴ FLOPs while Qwen2.5-1.5B reaches ~38% at ~150×10¹⁴ FLOPs.

- **Principled and systematic methodology:** The LOO + influence-function pipeline is grounded in formal tools (Eq. 1–5), extends the AutoMixer framework in a non-trivial direction (cross-capability, multi-checkpoint influence weighting), and avoids any leakage of benchmark data during data selection. Convergence of influence scores to zero provides an elegant stopping criterion.

- **Table 2 is particularly convincing:** By fixing the SFT corpus for all models, Table 2 cleanly isolates the contribution of pre-training/mid-training quality from post-training. MobileLLM-R1-950M* (57.8 MATH, 68.5 GSM8K, 13.7 LCBv6) outperforms both OLMo-2-1.48B (53.0 / 58.8 / 11.4) and SmolLM2-1.7B (41.4 / 50.5 / 7.4) with fewer parameters.

- **Fully open-source release:** Weights, code, and all curated datasets are disclosed, which is a genuine service to the community and contrasts sharply with closed competitors.

- **Unexpected finding on code–math transfer:** The observation that StarCoder benefits math more than OpenWebMath benefits code (Section 2.1.2) is non-obvious and is a substantive empirical contribution worth investigating further by the community.

---

## Weaknesses

### Fatal
None.

### Major

- **Parameter count asymmetry in headline comparison:** The headline result is that MobileLLM-R1-**950M** "matches or surpasses Qwen3-**0.6B**." At 1.6× more parameters, a match is arguably expected and the comparison risks overstating token efficiency. The FLOP-adjusted framing in Figure 1 is the honest one; the abstract and Section 4 should consistently lead with FLOPs rather than token count alone when comparing against a model of different size.

- **Computational overhead of the influence pipeline is uncharacterized:** The methodology requires (a) 7 LOO training runs, (b) 3 separate domain-specialized model trainings to serve as "capability-checkpoints," (c) influence computation at T=10 checkpoints per model, and (d) two rounds of mid-training with re-scoring. The total wall-clock or GPU-hour budget for the data-selection phase is never stated. If this overhead is comparable to simply training on more tokens with a simpler mixing strategy, the practical token-efficiency argument weakens considerably.

- **Influence-based mixing lacks a head-to-head ablation on final benchmark scores:** Figure 4 shows perplexity improvements from Datamix vs. uniform sampling, but perplexity is a proxy. The paper does not report final MATH/AIME/LCBv6 numbers for a model trained with uniform mixing, making it hard to quantify how much of the end-result improvement is attributable to the influence-based resampling vs. the quality of the curated ~2T data pool itself.

### Minor

- **Convergence as a stopping criterion is somewhat tautological:** The claim that influence scores concentrating near zero signals "dataset information exhaustion" (Section 3) is intuitive but not rigorously distinguished from the model simply over-fitting the training distribution or from diminishing marginal returns at any training stage. A controlled experiment (e.g., comparing stopping at convergence vs. an earlier/later stage) would sharpen this claim.

- **Evaluation protocol for AIME not stated:** Whether scores use pass@1 with greedy decoding or majority voting (e.g., maj@16, maj@32) is not specified. For competition benchmarks like AIME where scores are small integers, the number of samples matters enormously.

- **Knowledge distillation baseline (Figure 6):** The KD experiments use LLaMA3-8B as a teacher. Given that the paper's primary framing is about fully open-source training, a more appropriate comparison would be to also show distillation from a fully open-source teacher, or to justify why the KD experiment is included given that the final pipeline does not use a teacher model.

### Trivial

- The per-row alignment in the parsed Figure 8/9 tables is clearly a PDF-extraction artifact and should not affect evaluation.

---

## Nice-to-Haves

- A model-size-matched comparison (e.g., MobileLLM-R1-360M vs. Qwen3-0.6B at similar parameter counts) would make the token-efficiency story cleaner.
- Reporting the total GPU-hours for the influence-selection pipeline vs. the pretraining stage would help practitioners assess adoption cost.
- An ablation showing final benchmark results for the pipeline with vs. without the mid-training co-evolution (just pretraining → SFT) would isolate that component's contribution.

---

## Novel Insights

The most genuinely novel insight is the application of cross-capability influence scoring to sub-billion-model pretraining data selection, extended to a multi-checkpoint, multi-domain formulation that operates on compact representative subsets of each corpus. The finding that StarCoder benefits math capability more than OpenWebMath benefits coding—inverting a common assumption (Lewkowycz et al., 2022)—is a concrete, reproducible empirical claim that challenges received wisdom about the code-math transfer direction. The self-evolving mid-training paradigm, where influence convergence to zero serves as a principled termination criterion without touching any benchmark, is a clean methodological contribution even if the convergence phenomenon itself is expected in hindsight.

---

## Suggestions

- Add a table with explicit GPU-hour costs for each stage of the data-selection and influence-computation pipeline to enable practitioners to assess adoption feasibility.
- Report final MATH/AIME/LCBv6 scores for a baseline trained with uniform sampling over the same ~2T curated pool, to quantify the marginal value of influence-based reweighting.
- Clarify AIME evaluation protocol (pass@k, temperature, number of samples) explicitly in the main text.
- Frame the headline comparison as "5× fewer training FLOPs to match Qwen3-0.6B" rather than emphasizing token count alone, since the 950M vs. 600M parameter gap makes token-count comparisons slightly misleading without FLOP normalization.

---

## Score and Decision

The paper addresses a practically important and timely question—how to train strong small reasoning models efficiently using only open data—and provides a principled, reproducible answer with compelling empirical evidence. The token and FLOP efficiency results are striking; the code, math, and knowledge benchmark results under controlled SFT (Table 2) are the cleanest evidence. The primary weaknesses (parameter-count asymmetry in comparisons and missing overhead characterization) are significant but do not invalidate the core claims. The open-source contribution alone adds meaningful value to the community.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>