## Summary

The paper introduces an automated pipeline that, given only a natural-language trait description (e.g., "evil"), extracts a linear *persona vector* from a target model's activation space via contrastive generation with a frontier LLM. It then demonstrates four applications of these vectors: (1) monitoring prompt-induced behavioral shifts via projection, (2) predicting finetuning-induced persona shifts with high correlation ($r=0.76$–$0.97$), (3) mitigating those shifts during finetuning through a new *preventative steering* method that adds the undesired vector during training rather than subtracting it at inference, and (4) pre-finetuning data screening via a projection-difference metric that achieves $r \geq 0.88$ correlation with post-finetuning trait expression. Experiments span two 7B–8B models and three negative traits (evil, sycophancy, hallucination), with additional traits in the appendix.

## Strengths

- **Preventative steering preserves general capabilities substantially better than inference-time steering.** Figures 5–6 show that adding the undesired persona vector during finetuning reduces undesirable trait expression while MMLU accuracy and newly-learned-fact retention remain near baseline, whereas inference-time steering with comparable coefficients degrades both capability metrics sharply. The hallucination case study (Section 5.2, Figure 6) is particularly clean and compelling.

- **Projection difference on training data predicts post-finetuning trait expression before training begins.** Section 6.1 and Figure 7 report $r=0.88$–$0.95$ correlations across two models and three traits, and Section 6.2 (Figure 8) shows individual-sample separability. This enables practitioners to flag problematic data without running the finetuning procedure itself — a practically useful capability.

- **The automated extraction pipeline is a practical contribution that reduces manual engineering.** Previous work required hand-crafted contrastive pairs; this paper provides a single generic template that yields system prompts, evaluation questions, and a rubric from just a trait name and description (Section 2). The approach is straightforward for others to adopt.

- **The paper honestly acknowledges limitations of the proposed methods** (weaker within-type monitoring correlation in Section 3.3, cross-trait correlations in Appendix I.2). This transparency strengthens the credibility of the claims that are well-supported.

- **Experimental scope is broad for this type of work:** two model families (Qwen2.5-7B, Llama-3.1-8B), three traits in depth, four additional traits in appendix, both intentionally trait-eliciting and EM-like datasets, and multiple steering configurations compared against inference-time steering, CAFT, and regularization baselines.

## Weaknesses

### Fatal
None.

### Major

- **The mechanistic explanation for preventative steering is incomplete.** The paper states that adding the undesired vector during training "counteracts the finetuning objective's tendency to push the model along that direction" (line 180), but does not measure weight-space movement, gradient alignment, or activation dynamics to verify this account. The behavioral evidence is strong, but the method risks being a black-box trick whose generalizability to new settings and traits is uncertain without some internal analysis. The paper compares to CAFT and regularization (Appendix L.4–L.5), but a direct measurement of whether preventative steering actually *reduces the parameter shift* along the persona direction would substantially strengthen the contribution.

- **The correlation analyses in Figures 4 and 7 rest on a small number of independent observations.** Each point is one finetuned model aggregated over many responses. With roughly 8 datasets × 3 severity levels = 24 points per plot, the reported $r$ values are driven largely by coarse separation between Normal (low trait) and Type II (high trait) groups. A single dataset-specific effect could meaningfully change the correlation. This does not invalidate the findings — the consistency across two models and three traits is reassuring — but it makes the "prediction" claim more coarse than the high $r$ numbers alone suggest. A leave-one-dataset-out analysis or per-sample prediction would strengthen the evidence.

- **The claim that data screening "enables fine-grained data filtering" (Section 6) is supported only by sample-level separability, not by a demonstration that filtering actually prevents persona shifts.** Figure 8 shows that trait-inducing samples are separable from control samples, but the paper does not train on a filtered dataset and measure whether trait expression is reduced. Appendix N mentions real-world validation, but the main text lacks this crucial experiment. The claim is weaker than the contribution framing suggests.

### Minor

- **The LLM judge (GPT-4.1-mini) is the evaluation instrument for every quantitative result, but its validation is entirely deferred to the appendix.** The paper states that validation against human evaluators and external benchmarks exists (Section 2.1, "see Appendix D"), which is standard practice for main-text length constraints. However, a one-sentence summary of the agreement level (e.g., Pearson correlation or Cohen's κ) in the main text would give readers confidence without requiring them to locate the appendix. This is a presentation issue, not a fatal omission.

- **Training data amount and number of steps are not controlled across datasets.** Different finetuning datasets (evil, sycophancy, hallucination, medical, code, math, opinions) may vary in size or difficulty, which could affect the magnitude of finetuning shifts independently of the persona vector hypothesis. The paper does not discuss whether results are robust to varying dataset sizes.

- **The monitoring correlations (Section 3.3, $r=0.75$–$0.83$) are honestly acknowledged to arise mainly from distinguishing trait-encouraging vs. trait-discouraging system prompts, with more modest within-type correlation.** This limitation is well-stated, but it means the monitoring application is primarily useful for detecting *explicit* prompt-based shifts rather than subtle behavioral changes.

- **The comparison to CAFT (Casademunt et al., 2025) is mentioned but deferred to the appendix** with no summary of results in the main text. The main text says CAFT is "effective at preventing evil and sycophancy, but ineffective for hallucinations" (line 198), which gives a partial picture. A brief quantitative comparison in the main text would help readers assess preventative steering's relative merit.

### Trivial

None.

## Nice-to-Haves

- A measurement of weight-space movement along the persona direction comparing standard finetuning with and without preventative steering, to validate the claimed mechanism.
- A demonstration of the full filtering pipeline: filter training data using persona vector projections, then finetune on the filtered set and measure whether trait expression is reduced (the obvious next experiment from Section 6).
- Testing on larger models (e.g., 70B+) to verify that persona vectors remain linear and effective at scale.

## Removed Points

- *"The paper overclaims generality ('any personality trait of interest') but only studies three negative traits in depth."* — The paper explicitly studies three traits in the main text and four more (including positive traits like optimism and humor) in Appendix I, which the parser strips. This is a reasonable scope.
- *"The pipeline dependency on a specific frontier LLM (Claude 3.7 Sonnet) for artifact generation is a practical limitation not acknowledged."* — Every method paper relies on specific infrastructure. This is a generic limitation of all such work and not a meaningful weakness to weigh against the paper.
- *"Filtering of refusals and low-scoring responses introduces selection bias."* — This is standard practice for contrastive extraction and acknowledged in the description; it's not a flaw unique to this paper.
- *"Preventative steering's effect could have alternative explanations (e.g., different effective steering strength)."* — The paper controls for this by comparing against inference-time steering at matching coefficients; the behavioral evidence is clear.
- *Strength Finder generic strengths removed:* "The experimental scope is broad" was kept; strengths about "important problem" or "interesting question" without concrete evidence were dropped.
- *"Weak correlation may be due to a lack of proper confound control"* — speculation without specific evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a one-sentence summary of LLM judge validation in the main text (e.g., "GPT-4.1-mini scores correlate with human judgments at $r=X$ on a held-out set, and correlate with [External Benchmark] at $r=Y$").
2. Include a leave-one-dataset-out analysis for the correlation plots in Figures 4 and 7 to show robustness to individual dataset effects.
3. Add the obvious follow-up experiment for Section 6: train on filtered vs. unfiltered data and compare post-finetuning trait expression.
4. Add a measurement (even a simple one) showing that preventative steering reduces gradient magnitude or weight-space movement along the persona direction, to support the mechanistic claim.
5. Train on at least one real-world dataset in the main text for the data screening application (currently in Appendix N).

## Score and Decision

**Calibration anchors** (retrieved batch, all listed):

| Path | Avg Human Score | How it compares |
|---|---|---|
| 0DZEs8NpUH (Personality Alignment) | 6.00 (Accept) | Similar topic; current paper has stronger methodology and broader contributions |
| DXaUC7lBq1 (Low-empathy LLM Personality) | 3.00 (Reject) | Weaker problem framing and experimental rigor; current paper substantially stronger |
| rKMQhP6iAv (Personas as Truthfulness) | 4.25 (Reject) | Related "persona" concept but vague hypothesis and weaker evidence; current paper stronger |
| 2XBPdPIcFK (Steering Language Models / ActAdd) | 5.00 (Reject) | Similar activation steering, but narrower scope (inference-time only); current paper adds training-time intervention and data screening |
| LYHEY783Np (Neuron-based Personality Traits) | 6.67 (Accept) | Comparable quality; current paper has broader application scope |
| YGoFl5KKFc (SafetyLock) | 4.75 (Reject) | Related fine-tuning safety; current paper has more diverse contributions |
| kUH1yPMAn7 (Safety Layers) | 6.00 (Accept) | Comparable quality; both present clear empirical contributions |
| CvttyK4XzV (GCS / Concept Subspace) | 6.75 (Accept) | Stronger on technical depth of concept representation; current paper stronger on practical applications |
| sYJQEgkkaI (CARE / RepE Reliability) | 5.25 (Reject) | More methodologically focused but incremental; current paper has broader empirical contribution |

The paper under review sits comfortably above the rejected anchors (3.00–5.25) and is comparable to accepted papers at 6.00–6.75. It has clear, well-supported contributions (preventative steering, data screening, automated pipeline) with thorough empirical evaluation across two models and multiple traits, and honestly acknowledges its limitations. The main weaknesses — incomplete mechanistic analysis of preventative steering, small-N correlation plots, deferred judge validation — are real but not fatal and can be addressed. On balance, the paper merits acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>