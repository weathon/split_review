Now I have a thorough understanding of both the paper and the calibration landscape. Let me synthesize my final review.

---

## Summary

This paper presents an automated pipeline that extracts linear "persona vectors" from LLM activation space given only a natural-language trait description. The authors demonstrate that these vectors enable: (1) monitoring and controlling trait expression at deployment time, (2) predicting finetuning-induced persona shifts (r up to 0.97), (3) a novel "preventative steering" method that mitigates undesirable trait acquisition during training while preserving general capabilities, and (4) pre-finetuning screening of training data to flag samples likely to induce problematic persona changes. Results are validated across two model families (Qwen-2.5-7B, Llama-3.1-8B), multiple traits, and both designed and emergent-misalignment-like datasets.

## Strengths

- **Strong, multi-faceted empirical evidence.** The finetuning shift correlations (Figure 4, r = 0.76–0.97 across Qwen and Llama) and projection-difference predictions (Figure 7, r = 0.88–0.95) provide unusually tight quantitative validation that persona vectors capture meaningful directions of personality change. These correlations hold across models, traits, and dataset types.

- **Preventative steering is a genuinely novel and practically valuable contribution.** Adding the persona vector *during* training (rather than subtracting it at inference) mitigates trait acquisition while substantially better preserving general capabilities (Figure 5) and domain-specific knowledge (Figure 6). This is demonstrated with an elegant hallucination-while-learning-facts case study where inference-time steering destroys both MMLU and fact accuracy, but preventative steering preserves both.

- **Pipeline automation and breadth of applications.** The extraction pipeline requires only a trait name and description—no manual prompt engineering. A single persona vector then supports five distinct applications: deployment monitoring, deployment steering, finetuning shift prediction, preventative steering, and pre-finetuning data screening. The data-screening application (Section 6) is particularly compelling, showing that harmful samples can be flagged *before training occurs*, including samples that escape LLM-based filters.

- **Generalization across models, traits, and dataset types.** The same pipeline succeeds on two different model families, three negative traits in the main text (plus four additional traits in the appendix), and both explicitly trait-eliciting and emergent-misalignment-like datasets where trait shifts are unintended side effects.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **LLM-judge reliance without robustness analysis across judge models.** The extraction pipeline uses GPT-4.1-mini both to filter contrastive responses and as the evaluation metric throughout the paper. The paper does reference human-agreement validation and external benchmark comparisons (Appendix D), which is encouraging. However, without any analysis of how results change under a different judge model or extraction LLM, the robustness of the pipeline to these choices remains unquantified. This does not invalidate the core results—the steering experiments provide causal evidence independent of the judge—but it limits confidence in the precise trait scores reported and in the reproducibility of the pipeline when using different LLMs.

- **Monitoring framing in the abstract is slightly broader than the evidence.** The abstract states the vectors can "monitor fluctuations in the Assistant's personality at deployment time." Section 3.3 appropriately acknowledges that the correlations arise primarily from distinguishing between different prompt types, with more modest within-prompt-type correlations. The paper's own framing in Section 3.3 is appropriately cautious; the abstract could be tightened to match.

- **No quantitative precision/recall analysis for sample-level flagging.** Section 6.2 shows histograms demonstrating clear distributional separation between trait-inducing and control samples (Figure 8), but does not report threshold-based precision, recall, or F1 metrics. Adding these would make the data-screening story more concrete for practitioners.

- **Pipeline sensitivity to artifact-generating model unexplored.** The pipeline uses Claude 3.7 Sonnet to generate contrastive prompts and evaluation materials. No analysis or discussion addresses how sensitive the extracted persona vectors are to this choice—for instance, whether a different frontier model would produce systematically different vectors. This is a practical concern for reproducibility.

### Trivial

None.

## Nice-to-Haves

- A direct measurement of whether preventative steering actually reduces the internal activation shift along the persona vector (analogous to Figure 4 but for preventatively steered models) would strengthen the mechanistic interpretation of why preventative steering works.

- A brief discussion of compute cost for the projection-difference metric (which requires generating baseline responses for every training sample) and when the approximation strategies in Appendix K are acceptable.

- Clarifying in the main text that CAFT comparison findings are nuanced (the main text states CAFT is "ineffective for hallucinations" while Appendix L.4 discusses circumstances where each method is preferred).

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"I assume the appendices exist in the original submission... the current extraction strips them, so I cannot verify the human-agreement data or the extended experiments."** — Removed per hard rule: the parser strips appendices from all papers; they exist in the original submission. Criticisms about missing or unverifiable appendix content are parser artifacts, not paper flaws.

- **"The paper does not give a quantitative precision/recall evaluation of the sample-level flagging, only histograms."** — This one was kept (moved to Minor), as it is a legitimate observation about what the paper actually contains, not speculation about missing material.

## Novel Insights

The paper's most striking finding goes beyond the individual applications: persona vectors extracted purely from contrastive prompts (without any finetuning data) can predict *which training datasets will cause persona shifts before any training occurs* (r = 0.88–0.95, Figure 7). This suggests that the relevant activation directions are already present in the base model and that finetuning primarily shifts representations along these pre-existing axes. The fact that projection *difference* (training response minus base-model response) works better than raw projection (Appendix J) elegantly captures the intuition that a sample only shifts the model if it differs from what the model would naturally produce—not merely because it contains trait-expressive content.

## Suggestions

- Add a small robustness experiment varying the judge model (e.g., GPT-4.1-mini vs. a different LLM) on a subset of the evaluation to quantify how sensitive trait scores are to judge choice.
- Tighten the abstract's monitoring claim to "detect large prompt-induced persona shifts" rather than "monitor fluctuations" generally, matching the evidence in Section 3.3.
- Report a simple threshold-based precision/recall for the sample-level flagging histograms in Figure 8.
- Add a paragraph discussing how pipeline outcomes may depend on the artifact-generating model (Claude 3.7 Sonnet) and the judge model, and what practitioners should consider when replicating with different LLMs.

## Score and Decision

**Calibration round 1**: Searched for activation steering / representation engineering papers across three bands. Low band (<3.5): reject-level papers (avg 2.5–3.0) on related topics with significant methodological weaknesses. Middle band (3.5–7.5): "Steering Language Models with Activation Engineering" (5.0), "Improving Instruction-Following through Activation Steering" (7.0), "Programming Refusal with CAST" (7.33). High band (>7.5): "Sparse Feature Circuits" (8.0), "Linear Representations of Political Perspective" (7.5), "TopoLM" (8.0).

**Initial bracket**: The paper is clearly above the 5.0 and 7.0 middle-band anchors and comparable to or slightly above the 7.33–7.50 anchors. Preliminary bracket: 7.0–8.0.

**Calibration round 2**: Narrowed with queries in (5.5–7.5) and (7.0–8.5). Retrieved anchors at 7.33 (CAST), 7.50 (Political Perspective), 7.33 (Linearity of Relation Decoding), 8.0 (Sparse Feature Circuits), 7.50 (Bilinear MLPs).

**Anchor comparisons**:
- "Improving Instruction-Following" (7.00): Our paper has broader scope, more applications, and stronger quantitative evidence. **Our paper is stronger.**
- "Programming Refusal with CAST" (7.33): Novel conditional steering, but limited to ≤8B models, missing baselines, narrow evaluation. Our paper has broader applications and more comprehensive evaluation. **Our paper is stronger.**
- "Linear Representations of Political Perspective" (7.50): Clean linear-probe methodology, but reviewers noted limited novelty (linear separability is expected), US-centric scope, LLM-evaluator concerns. Our paper has broader scope, more applications, and stronger quantitative correlations. **Our paper is comparable or slightly stronger.**
- "Sparse Feature Circuits" (8.00): Fundamentally novel SAE-based circuit discovery method, well-executed with SHIFT application. Our paper's core extraction method is more incremental (automating established contrastive-activation approaches), but our paper offers more diverse practical applications and more comprehensive empirical validation. **Our paper is slightly below this in core novelty, but comparable in overall quality and significance.**

**Final score**: The paper sits between the 7.50 and 8.00 anchors. It is clearly stronger than the 7.33–7.50 anchors in breadth and evidence, but the core pipeline is a systematization of existing methods rather than a fundamentally new technique, and the robustness gaps (LLM judge sensitivity, pipeline model-dependence) are real though minor. **Score: 7.5.**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>