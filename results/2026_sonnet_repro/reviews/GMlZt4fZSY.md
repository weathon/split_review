Now let me run calibration searches to establish the score range.**Round 1 bracket: 5.0 – 7.0**

The paper is most similar to the "Textbooks Are All You Need" (phi-1) class of papers — data-centric training recipes for small/efficient models, scores around 6.0. Strong anchors (score 8) are more foundational or cleaner methodological contributions. Let me narrow within the bracket.Now I have enough to write the final review. Let me synthesize all findings.

---

## Summary

MobileLLM-R1 presents a data-centric framework for training competitive sub-billion-parameter reasoning models under a constrained token budget. The approach introduces (1) a benchmark-free, leave-one-out influence-scoring procedure to curate and weight pretraining datasets across code, math, and knowledge domains, and (2) an iterative data-model co-evolution strategy for mid-training compression using sample-level rejection sampling and dataset-level reweighting. The resulting MobileLLM-R1 model series substantially outperforms prior fully open-source models (OLMo, SmolLM) and is reported to match Qwen3-0.6B while training on only 11.7% of its token budget; full models, code, and data are released.

---

## Strengths

- **Token-efficient training with compelling benchmark results**: MobileLLM-R1-950M achieves AIME scores of 15.5 and strong MATH/LiveCodeBench-v6 numbers, compared to 0.6 for OLMo-2-1.48B and 0.3 for SmolLM-2-1.7B (Abstract, Figure 9). The improvement over fully open-source baselines of comparable or larger parameter counts is real and substantial, not just a marginal gain.

- **Rigorous leave-one-out dataset analysis**: Figure 3 presents a systematic ablation across seven pretraining datasets — StarCoder, OpenWebMath, FineWeb-Edu, Wikipedia, ArXiv, StackExchange, and Algebraic Stack — measuring NLL on held-out capability-probing sets at multiple training steps. The finding that FineWeb-Edu provides the largest cross-domain benefit, and the surprising reversal (StarCoder benefits math more than OpenWebMath benefits code), are specific and well-supported observations.

- **Clean post-training ablation isolating base model quality**: Table 2 applies identical SFT datasets to baseline instruct checkpoints and MobileLLM-R1's intermediate checkpoints, directly demonstrating that stronger pre-training/mid-training leads to better reasoning elicitation. MobileLLM-R1-950M achieves 57.8% MATH vs. 53.0% for OLMo-2-1.48B-SFT (a larger model) under the same SFT. This is a well-designed controlled comparison.

- **Full open-source release**: Complete models, code, data sources, hyperparameters, and training recipes are committed to public release (Reproducibility Statement, Section A). For the sub-billion reasoning model community, this alone carries significant practical value.

- **Training dynamics insight**: Figure 7 tracks perplexity on HumanEval and GSM8K across training stages, revealing that math knowledge acquired during pre-training Phase 2 later facilitates coding improvement during mid-training. This is a concrete empirical observation about cross-capability transfer in small models.

---

## Weaknesses

### Fatal
None.

### Major

- **Parameter mismatch in headline claim**: The paper's most prominent result — "MobileLLM-R1-950M matches or surpasses Qwen3-0.6B across multiple reasoning benchmarks using only 11.7% of its training tokens" (Abstract, Introduction Section 1) — compares a ~950M-parameter model against a ~600M-parameter baseline, a ~58% parameter advantage. The paper frames this as pure token efficiency, but model capacity is a first-order determinant of performance; the token-efficiency argument conflates token savings with parameter savings. An honest framing would either acknowledge this parameter asymmetry explicitly, or provide a parameter-controlled comparison at ~600M scale. As written, the flagship claim overstates what can be attributed to the data curation methodology.

- **Core datamixing contribution validated only via perplexity, not downstream accuracy**: The central algorithmic contribution — influence-score-guided data mixing (Section 2.2) — is evaluated in Figure 4, which shows lower perplexity for "Datamix" vs. "Original" (uniform sampling) on code, math, and knowledge probing sets. However, there is no ablation that compares influence-based mixing vs. uniform sampling over the same quality-filtered data pool in terms of final downstream benchmark scores (MATH, AIME, HumanEval, LCBv6). Table 2 establishes that MobileLLM-R1 outperforms OLMo and SmolLM, but this comparison cannot isolate the influence-score machinery: it conflates data quality curation, data selection, and mixture optimization simultaneously. Without a clean control — same filtered data pool, same total tokens, uniform vs. influence-based mixing, evaluated on final benchmarks — the specific value of the influence-score mechanism is not demonstrated. The perplexity gap in Figure 4 is encouraging but insufficient as the sole evidence for the paper's core methodological claim.

### Minor

- **Data repetition unacknowledged**: The abstract states "~2T tokens of high-quality data are sufficient" yet training involves "4.2T tokens on the dataset resampled from these ~2T tokens" (Abstract). This means approximately 2× corpus repetition during pre-training. Repeated data exposure carries documented risks (memorization, sharpened domain distribution, potential over-fitting to the curated proxy). For a paper whose thesis centers on data-token sufficiency, the distinction between 2T unique tokens and 4.2T training tokens deserves explicit discussion.

- **Compute cost of the influence pipeline unquantified**: Training three domain-specialized models (for C, M, K) to convergence and computing influence scores at 10 checkpoints each (Section 2.2, Eq. 3) is a non-trivial overhead. For a paper claiming efficiency, omitting this cost from the efficiency analysis is a gap — the methodology may add substantial preprocessing compute relative to the training budget it optimizes.

- **Stopping criterion for mid-training convergence is underspecified**: Section 3 presents "convergence to zero influence" (Figure 5) as evidence that data is exhausted and that two stages suffice. However, this criterion could equally reflect model insensitivity to the remaining data, not genuine knowledge absorption. No ablation demonstrates that additional stages yield no further improvement.

### Trivial

- The linearly increasing checkpoint weighting $\alpha_{c,t} \propto t$ in Eq. 4 is stated without justification or ablation; it would strengthen the paper to provide even a brief empirical rationale.

---

## Nice-to-Haves

- **Parameter-controlled comparison**: Training a ~600M version of MobileLLM-R1 and reporting its benchmarks vs. Qwen3-0.6B would allow the token-efficiency claim to stand cleanly without the parameter-mismatch confound.

- **Direct downstream ablation for datamixing**: An ablation showing influence-based mixing vs. uniform sampling over the same 2T quality-filtered pool, measured on final benchmark accuracy (not just perplexity), would directly validate the paper's core contribution and distinguish the influence-score mechanism from generic data quality improvements.

- **Variance estimates on AIME**: Sub-billion models near the zero-performance floor on AIME can exhibit high run-to-run variability; multi-run averages would strengthen the headline numbers.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Convergence-to-zero means exhaustion" framing**: The harsh critic flagged that Figure 5's convergence criterion could reflect model insensitivity rather than information absorption. This is elevated only to Minor (not Major) because it concerns the *interpretation* of a convergence signal, not the validity of the empirical results, and the paper's practical two-stage setup is still well-supported by Figure 6.

- **Figure 1 mid-training FLOPs exclusion**: The critic speculated mid-training FLOPs might be excluded from Figure 1's x-axis. Verification shows MobileLLM-R1-950M is plotted at ~25×10¹⁴, consistent with 0.95B × 4.2T × 6 ≈ 24×10¹⁴ (i.e., 4.2T includes both pre-training and mid-training tokens). This concern is factually incorrect and is removed.

- **Benchmark proximity in capability-probing datasets**: The critic speculated that filtering via FineWeb-Edu classifiers and Ask-LLM "may preferentially retain data that resembles benchmark-relevant distributions." This is a speculative concern with no specific evidence from the paper; removed per filtering discipline.

- **Strength: cross-capability transfer insight (Figure 7)** is retained as a genuine supporting strength — math → code transfer during mid-training is a concrete, specific empirical finding, not generic.

- **Strength: "benchmark-free data optimization is important/novel"** — generic significance claims are filtered. Retained only in the specific form: the LOO analysis and influence-based mixing avoid using held-out benchmark sets during construction, which is a concrete, methodologically sound design decision.

---

## Novel Insights

The most interesting observation in the paper is the cross-capability reversal: StarCoder (code data) benefits math performance more than OpenWebMath (math data) benefits code (Figure 3). If replicated, this challenges the widely-held view (Lewkowycz et al., 2022) that mathematical data disproportionately improves coding ability, and suggests that high-quality structured code corpora may be more broadly informative than domain-specific math corpora for small models with limited capacity. The implicit explanation — that code's syntactic structure and step-by-step exposition transfers well to mathematical reasoning — is worth deeper investigation.

---

## Suggestions

1. **Add one downstream ablation for datamixing**: Train a control using the same quality-filtered 2T pool with uniform sampling vs. influence-based mixing and report MATH/HumanEval/LCBv6 accuracy after full post-training. This is the single change that would most strengthen the paper's core claim.
2. **Acknowledge parameter asymmetry explicitly**: Add one sentence in Section 4.1 noting that the 950M–600M comparison is not parameter-controlled, and that the token-efficiency claim is orthogonal to model size.
3. **Discuss data repetition**: Add a brief discussion (2–3 sentences) on the implications of 2× corpus repetition, including what safeguards (if any) were applied.
4. **Report LOO result as quantitative table**: Figure 3's trajectories are informative but a summary table of ΔL values (Eq. 1) at training end would make the dataset utility analysis more readable and citable.

---

## Score Calibration

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `v3DwQlyGbv.md` (Paramanu-Ganita math LM) | 2.33 | R1 | Clearly weaker — no systematic curation, no open release, limited scope |
| `Fq8tKtjACC.md` (phi-1 / Textbooks Are All You Need) | 6.00 | R1 | Strong comparator — similar spirit (data-centric small model), but MobileLLM-R1 is more open, more principled, and multi-domain |
| `UNxCphTxWp.md` (ProX / Programming Every Example) | 6.00 | R1 | Data refinement at scale; similar practicality, MobileLLM-R1 is broader |
| `4xBew7kuYB.md` (Studying Effects of Training Data on SLMs) | 5.50 | R1 | Less principled, narrower contribution |
| `07yvxWDSla.md` (Synthetic continued pretraining) | 8.00 | R1 | Cleaner theory and evaluation; substantially stronger |
| `f4gF6AIHRy.md` (DiSF submodular file selection) | 8.00 | R1 | More rigorous methodology; clearly stronger |
| `sZGZJhaNSe.md` (Aioli data mixing framework) | 6.25 | R2 | Most directly comparable — data mixing optimization; Aioli more rigorous but MobileLLM-R1 broader |
| `aP3OBwf8dk.md` (Need a Small Specialized LM?) | 6.00 | R2 | Similar resampling ideas; MobileLLM-R1 more complete and empirically richer |
| `3uITarEQ7p.md` (DP Model Compression via Selective Pretraining) | 5.50 | R2 | Different setting (privacy), less relevant |
| `mao3y822aM.md` (NanoLM / loss prediction across scales) | 5.50 | R2 | Different contribution; not directly comparable |
| `3OyaXFQuDl.md` (Smaller, Weaker, Yet Better: LLM Reasoners) | 7.00 | R2 | Closer comparator — small reasoning models; cleaner methodology and tighter claim validation; above MobileLLM-R1 |
| `eENHKMTOfW.md` (Training Mice to Compete with Elephants) | 6.00 | R2 | Small model customization; similar scale of contribution |

**Round 1 bracket**: 5.0 – 7.0

**Round 2 narrowing**: The paper sits below "Smaller, Weaker, Yet Better" (7.0) due to the parameter-mismatch framing issue and the missing downstream ablation for datamixing. It is comparable to phi-1 (6.0) and "Need a Small Specialized LM?" (6.0) — both data-centric small-model contributions — but MobileLLM-R1 is more principled and fully open-source. It is comparable to or slightly below Aioli (6.25) since Aioli provides a cleaner theoretical framework and validating methodology. The open-source commitment, multi-domain breadth, and genuine empirical advances push the paper above the 5.5 floor.

**Final score: 6.0**

---

**Axis Ratings (language)**

- **Originality**: Moderate. The influence-score data mixing extends AutoMixer; the LOO analysis and co-evolution mid-training paradigm are incremental but combine existing ideas in a useful, practical way.
- **Importance of research question**: High. Training efficient small reasoning models is increasingly critical for on-device AI deployment.
- **Claims well-supported**: Mixed. The model's empirical performance is strongly supported (Table 2, Figures 8-9). The core methodological claim (influence-based mixing adds value) is supported only by perplexity, not downstream accuracy.
- **Soundness of experiments**: Generally sound; the Table 2 controlled comparison is well-designed. The flagship Qwen3 comparison has a parameter mismatch that should be acknowledged.
- **Clarity of writing**: Good. The training pipeline is clearly described, and the rationale for each design choice is articulated.
- **Value to research community**: High, due to full open-source release of models, code, and data.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>