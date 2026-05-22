Now I have a good picture. Let me write the consolidated review.

**Round-1 bracket:** Between the weak anchors (~3.0) and the strong anchors (~8.0), the paper clearly sits in the upper-middle band. The ActAdd paper (5.0, rejected) is less comprehensive, while the instruction-following steering paper (7.0, accepted) is comparable.

**Round-2 narrowing:** The paper is stronger than the neuron-based personality paper (6.67) and comparable to the instruction-following steering paper (7.0) and the CAST paper (7.33), with a broader scope but some minor methodological gaps.

---

## Summary

This paper introduces *persona vectors* — linear directions in LLM activation space corresponding to traits like evil, sycophancy, and hallucination — extracted via a fully automated pipeline that takes only a natural-language trait description. The authors validate these vectors across several applications: monitoring prompt-induced behavioral shifts (r=0.75–0.83), predicting finetuning-induced trait shifts (r=0.76–0.97), a novel *preventative steering* method that adds the vector during training to block drift while preserving capabilities, and pre-training data screening via "projection difference" (r=0.88–0.95). The strongest single result is the fact-acquisition case study (Section 5.2) where preventative steering suppresses hallucination side-effects without the catastrophic capability degradation caused by inference-time steering.

## Strengths

- **Preventative steering is a novel and practically superior intervention.** The case study in Section 5.2 (Figure 6) is the paper's clearest win: both inference-time and preventative steering reduce hallucination to baseline, but inference-time steering destroys MMLU and newly-learned fact accuracy while preventative steering preserves both. This is a concrete, non-obvious improvement over the standard baseline.

- **Strong, consistent correlations across models and traits.** The finetuning-shift analysis (Section 4.2, Figure 4) reports r=0.76–0.97 across two models (Qwen2.5-7B, Llama-3.1-8B) and three traits, all p<0.001. The data-screening correlation (Section 6.1, Figure 7) similarly yields r=0.88–0.95. The cross-trait baselines (r=0.34–0.86, Appendix I.2) further confirm that the signal is trait-specific.

- **The extraction pipeline is genuinely automated and reusable.** Section 2 describes how a frontier LLM generates contrastive system prompts, evaluation questions, and a scoring rubric from a single sentence. This means the method can be applied to any new trait of concern without manual curation — a practical contribution for safety monitoring.

- **Honest discussion of limitations.** The paper transparently notes that monitoring correlations weaken when controlling for prompt type (Appendix E.2), that cross-trait correlations exist (Appendix I.2), and that preventative steering does not fully block trait acquisition in single-layer form. This candor increases trust in the claims that are strongly supported.

## Weaknesses

### Fatal
None.

### Major
- **LLM judge validation is stated but not summarized in the main text.** The paper's entire empirical apparatus rests on GPT-4.1-mini as a judge scoring trait expression (0–100). Section 2.1 states that validation was performed against human evaluators and external benchmarks (deferred to Appendix D). While the validation presumably exists in the full submission, the main text provides no headline statistic (e.g., human–judge correlation or agreement rate). Given that subjective traits are being evaluated by an LLM, this is a nontrivial gap for a reader who cannot check the appendix. The authors should move a key validation number into the main paper.

- **No error bars or confidence intervals on steering experiments.** Figures 2, 5, and 6 show point estimates without variance. For the preventative-steering vs. inference-time-steering comparison (Figure 5), which is the paper's central practical claim, the absence of error bars makes it impossible to assess whether the differences are reliable. Multiple finetuning seeds or bootstrapped intervals would significantly strengthen the evidence.

### Minor

- **Shared evaluation prompts for finetuning-shift analysis (Section 4.2).** Both the finetuning shift (x) and the trait expression score (y) are computed on the same set of evaluation prompts. While they measure different quantities (internal activation shift vs. behavioral score), using disjoint prompt sets for extraction and evaluation would rule out the possibility that the correlation is inflated by prompt-specific artifacts. This is a methodological tightening, not a fatal flaw — the relationship holds across 8+ datasets and two models, which limits the scope for spurious correlation.

- **MMLU is the sole general capability benchmark for preventative steering.** The paper evaluates capability preservation via MMLU accuracy, which is a standard but narrow metric. Testing on one or two additional benchmarks (e.g., GSM8K, HellaSwag, or TruthfulQA) would strengthen the claim that preventative steering preserves "general capabilities."

### Trivial
None.

## Nice-to-Haves

- Test whether the finetuning-shift correlation (Section 4.2) holds when using disjoint prompt sets for activation extraction and trait scoring.
- Ablate the pipeline's sensitivity to the choice of generator model (Claude 3.7 Sonnet) — e.g., using GPT-4 or human-written prompts to see if persona vectors change.
- Report per-dataset breakdowns of the finetuning-shift correlations (currently pooled across dataset types).
- Add a brief discussion of computational cost for practitioners.

## Removed Points

These points are flagged to be removed, treat them with caution:
- The harsh critic's claim about "preventative steering comparison not fully controlled (steering coefficient ranges not matched)" — this is a misunderstanding. The two methods use different coefficient ranges because they are different interventions (inference-time subtraction vs. training-time addition); comparing at the same coefficient value would not be meaningful. The comparison is about whether each method achieves its intended effect, not whether they use the same α.
- "The paper does not discuss the computational cost of the pipeline" — a nice-to-have but not a weakness.
- "Many-shot monitoring results are only shown in Appendix E.1" — the main text (Section 3.3) summarizes the system-prompt results and notes that many-shot results are similar, which is standard practice.
- Strength Finder claimed strengths that are too generic or conflict with verified weaknesses: removed.
- "FUNDAMENTAL ISSUES" triggered? No. None of the verifiable weaknesses threaten the core claims.

## Novel Insights

The key insight that emerges across the paper — and is not stated in any single sentence — is that the *same* linear persona vector serves as a unifying measurement instrument across four distinct regimes: deployment-time monitoring (prompt-induced), training-time monitoring (finetuning-induced), pre-training prediction (data screening), and training-time intervention (preventative steering). This is unusual: most activation-steering papers focus on one or two applications. The fact that one direction works for all four suggests that persona vectors are capturing something structurally fundamental about how these traits are encoded, rather than being a fragile artifact of a specific extraction procedure. The finding that preventative steering at training time can absorb the drift that would otherwise require destructive inference-time correction (Section 5.2) is the most practically significant result in the paper and deserves highlighting beyond its current presentation.

## Suggestions

- Add a single headline validation statistic for the LLM judge (human–judge Spearman correlation or agreement rate, by trait) to Section 2.1 of the main text. This single addition would substantially raise confidence in every subsequent quantitative claim.
- Add error bars (e.g., bootstrapped 95% CIs or results across multiple finetuning seeds) to Figures 5 and 6. The preventative-steering vs. inference-time-steering comparison is the paper's strongest applied result; it deserves a variance estimate.
- Run the finetuning-shift analysis (Section 4.2) with one additional control: compute finetuning shift on prompt set A and trait expression on prompt set B, to confirm the correlation is not an artifact of shared prompts.

## Score and Decision

**Round-1 bracket:** The weak anchors (scores ~3.0, papers on related personality/steering topics that were rejected) are clearly inferior to this paper. The strong anchors (scores ~8.0, papers on LLM safety control) are on different problems. The middle band anchors (scores 5.0–7.33) are the relevant comparison set.

**Round-2 anchors used for calibration:**
- *Improving Instruction-Following through Activation Steering* (avg 7.00, accept): Similar methodology, narrower scope. Our paper is broader in application scope and comparable in execution quality.
- *Neuron-based Personality Trait Induction* (avg 6.67, accept): Similar topic (personality in LLMs), but uses neuron manipulation rather than activation directions. Our paper has more diverse validation and cleaner methodology.
- *Programming Refusal with CAST* (avg 7.33, accept): Cleaner technical contribution in a narrower scope. Our paper has more breadth and practical applications.
- *Semantics-Adaptive Activation Intervention* (avg 6.40, accept): Related activation steering work. Our paper is stronger in evaluation breadth.
- *Identifying and Tuning Safety Neurons* (avg 6.20, accept): Related but different methodology. Our paper is at least comparable.

The paper is a strong contribution with clear practical value, novel preventative steering, and thorough empirical validation across multiple applications. The main weaknesses (deferred LLM judge validation, no error bars, shared-prompt concern) are addressable and do not undermine the core claims. Relative to the round-2 anchors, the paper is stronger than the 6.67 personality paper and comparable to the 7.0–7.33 steering papers, with broader scope but slightly less polish on the evaluation details.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>