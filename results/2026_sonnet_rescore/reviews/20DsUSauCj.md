## Summary

This paper introduces *persona vectors* — linear directions in LLM activation space corresponding to specific personality traits (evil, sycophancy, hallucination) — extracted via a fully automated pipeline that takes only a natural-language trait description as input. The authors validate four practical applications: (1) deployment-time monitoring of prompt-induced behavioral shifts, (2) inference-time steering to suppress unwanted traits, (3) a novel *preventative steering* method that steers activations toward a trait during finetuning to preemptively limit its acquisition, and (4) pre-finetuning data screening at both dataset and sample level. The strongest contribution is preventative steering: adding the persona vector during training reduces undesired trait acquisition while substantially better preserving general capabilities (MMLU, new-fact recall) than post-hoc inference-time steering.

---

## Strengths

- **Fully automated, scalable extraction pipeline.** The pipeline requires only a trait name and description; a single generic prompt template generates contrastive system prompts, evaluation questions, and a rubric, yielding a persona vector without per-trait manual effort. Figure 2 confirms that steering with extracted vectors reliably elevates trait expression across layers for evil, sycophancy, and hallucination.

- **Strong empirical coupling between finetuning-induced activation shifts and behavioral change.** Figure 4 reports within-trait correlations of r = 0.76–0.97 across Qwen and Llama for finetuning shift vs. post-finetuning trait expression, covering both explicitly trait-eliciting datasets and emergent-misalignment-like datasets that were not designed to induce those traits. This tight coupling is the empirical backbone of the paper's framing.

- **Novel preventative steering with compelling capability-preservation results.** Steering the model *toward* the persona vector during training (Section 5) reduces undesired trait acquisition while maintaining MMLU accuracy, in contrast to inference-time steering which degrades both MMLU and task performance. The fact-acquisition case study (Figure 6) concretely illustrates the trade-off: preventative steering eliminates hallucinatory side effects of training on 1,000 post-cutoff facts while preserving new-fact recall; inference-time steering destroys both.

- **Pre-finetuning data screening at dataset and sample level.** Figure 7 shows projection-difference predicts post-finetuning trait expression with r = 0.88–0.95 before any training is run. Figure 8 demonstrates that individual trait-inducing samples are cleanly separable from control samples via projection alone, even for EM-like datasets that induce traits implicitly. The complementarity with LLM-judge filtering (Appendix M, referenced in Section 6.2) adds practical value.

- **Generalization across models and positive traits.** Experiments span Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, and Appendix I extends to positive traits (optimism, humor), demonstrating the pipeline is not confined to a single model family or polarity.

---

## Weaknesses

### Fatal
None.

### Major

- **Cross-trait specificity is weaker than the framing implies, and the paper underquantifies this.** Figure 4 reports within-trait correlations of r = 0.769–0.967, but footnote 6 acknowledges that "negative traits (and, surprisingly, humor) tend to shift together," and cross-trait baselines reach r = 0.34–0.86 (Appendix I.2). The ranges overlap: Qwen's sycophancy within-trait correlation (r = 0.769) is lower than the upper cross-trait baseline (r = 0.86). This means a portion of the reported signal may be captured by a shared "negativity direction" rather than trait-specific information. The paper acknowledges the overlap in a footnote but does not decompose shared versus trait-specific variance, nor does it test whether a generic "negative trait" vector would perform comparably for steering and prevention tasks. Since the paper's central framing is that *trait-specific* persona vectors enable targeted monitoring and control, the gap between this claim and the evidence is a real evidentiary issue, not just a framing quibble. The authors should either decompose the shared component (e.g., via PCA of the three vectors) or explicitly reframe around a "negativity-direction" framework.

### Minor

- **Within-prompt-type monitoring correlations are acknowledged but not quantified in the main text.** Section 3.3 states: "These correlations arise primarily from distinguishing between different prompt types…with more modest correlations when controlling for prompt type (Appendix E.2)." Without actual within-type r values in the main text, the abstract's claim that persona vectors "can be used to monitor fluctuations in the Assistant's personality at deployment time" is incomplete. If within-type correlations are near zero, monitoring reduces to detecting coarse prompt-level shifts rather than fine-grained behavioral drift. A single sentence with actual numbers would resolve this.

- **The real-world dataset filtering result (Appendix N) is absent from the main text.** Section 6.2 concludes: "In Appendix N, we show this method works on real-world datasets to select samples that induce or suppress a given trait, even escaping LLM filters." This is arguably the most practically significant data-screening result; the claim that projection-based filtering complements LLM-based filters is a concrete selling point. Yet no magnitude, false-positive rate, or example appears in Section 6.2. Moving even a headline number into the main text would substantially strengthen Section 6.

- **Preventative steering mechanism is asserted but not mechanistically validated.** The paper's stated mechanism — that adding the persona vector during training "counteracts the finetuning objective's tendency to push the model along that direction" (Section 5.1) — is plausible but untested. A cross-vector control (e.g., does using the sycophancy vector also prevent evil acquisition?) would either validate trait-specific mechanism or reveal that general activation perturbation is responsible. This would sharpen both theoretical understanding and practical guidance for new settings.

- **Potential layer-selection and evaluation data overlap (Section 2.2 / Section 3).** Layer selection is performed by testing steering effectiveness across layers (Appendix D.4). The 40 questions are split into extraction (20) and evaluation (20) sets, but it is unclear from the main text whether the evaluation set used in Appendix D.4 for layer selection is the same set used to report results in Figure 2 and Section 3. If so, the reported steering performance is partially confounded by model selection. Clarification is warranted.

- **Statistical independence assumption in Figure 4.** The scatter plots include approximately 24 data points (8 datasets × 3 versions each). The three versions of each dataset (Normal, I, II) share a common construction and are thus not independent. Effective degrees of freedom are closer to 8 per plot, which weakens the inferential force of p < 0.001 computed on n ≈ 24 points. This doesn't invalidate the trend but the p-value should be interpreted with this caveat.

### Trivial

- **Copy-paste duplicate paragraphs in Section 5.1.** The paragraphs beginning "We compared preventative steering against alternative training interventions…" appear twice in Section 5.1 in nearly identical form (comparing CAFT and regularization). One should be removed.

- **MMLU as the sole capability measure.** MMLU is a coarse benchmark that may miss behavioral degradation on the target domain. Including at least one domain-specific or instruction-following metric alongside MMLU would give a more complete picture of capability preservation, especially for the finetuning experiments in Section 5.

---

## Nice-to-Haves

- A targeted decomposition experiment: extract the first principal component of the three persona vectors (evil, sycophancy, hallucination), project each onto the shared component and its residual, and test which component drives finetuning correlations and prevention results. This would either validate or reframe the trait-specificity claim cleanly.
- A cross-vector preventative steering control condition: apply the sycophancy vector to prevent evil acquisition and vice versa. If only the matched vector works, the mechanism is confirmed. If any vector works, the contribution should be reframed as "activation perturbation during training limits persona drift."
- Explicit scale limitations discussion in main text (the paper covers only 7–8B instruction-tuned models; practitioners applying this to much larger models or different alignment procedures should be cautioned).
- Quantitative summary from Appendix M (complementarity of persona-vector and LLM-judge filtering) in Section 6.2.

---

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **"Copy-paste artifact that should be removed" (Section 5.1, style/formatting note):** Retained as Trivial, not removed — it is a real editing artifact visible in the paper text that affects readability.

- **Scope criticism about scale (only 7–8B models):** The paper explicitly focuses on these models and discusses limitations in Appendix B (stripped). Demoted to Nice-to-Have rather than a Weakness, as this is a scope limitation the paper acknowledges, not a methodological flaw.

- **Demand for user studies or theoretical proofs for the activation steering mechanism:** Standard practice in empirical LLM safety papers does not require mechanistic proofs; moved to Nice-to-Have.

- **"High-precision correlation numbers should be interpreted cautiously" (evaluation circularity):** The paper's own Appendix D validates LLM judge scoring against human evaluators and external benchmarks; the concern is partially addressed. Retained as Minor rather than Major given the partial mitigation.

---

## Novel Insights

The reviewers' synthesis surfaces one genuinely instructive observation beyond the paper's own contributions: the cross-trait correlation overlap (r = 0.34–0.86 cross-trait vs. r = 0.76–0.97 within-trait, with ranges overlapping) implies that a substantial fraction of "persona shift" may be attributable to a shared negativity direction rather than trait-specific geometry. If true, this would mean the real engineering contribution is not the existence of distinct trait vectors per se, but the discovery that *any* directional signal in activation space can serve as a proxy for the shared negativity shift underlying finetuning-induced misalignment. This reframing — from "trait-specific persona vectors" to "linear proxies for finetuning-induced negativity drift" — is actually more powerful and practically actionable, and deserves explicit treatment.

---

## Suggestions

1. Report within-prompt-type monitoring correlations numerically in the main text of Section 3.3, alongside the Appendix E.2 reference.
2. Move at least one headline result from Appendix N (real-world dataset filtering) into Section 6.2.
3. Remove one of the two nearly identical paragraphs in Section 5.1 comparing CAFT and regularization.
4. Add a brief decomposition (or cross-vector control) experiment to address shared vs. trait-specific variance in Section 4 or Section 5.
5. Acknowledge scale limitations (7–8B models) explicitly in the main text or conclusion, not only in the appendix.

---

## Evaluation Along Key Axes

**Originality:** The automated pipeline for persona-vector extraction is a meaningful systematization of existing steering/probing ideas. The preventative steering contribution (adding the vector during training) is genuinely novel and not a straightforward extension of prior work. Moderate-to-high originality.

**Importance of research question:** Finetuning-induced and prompt-induced persona drift are concrete, high-stakes problems (as illustrated by the GPT-4o sycophancy incident and the Grok examples). High practical relevance.

**Claims well-supported:** The core empirical claims (monitoring correlations, finetuning correlations, preventative steering efficacy, data screening) are consistently supported across two models and multiple traits. The one gap is the "trait-specific" framing, which is weaker than presented given cross-trait correlation overlap.

**Soundness of experiments:** Generally sound, with the caveats noted above (effective degrees of freedom in Figure 4, within-type monitoring not quantified, layer-selection potential overlap). The fact-acquisition case study (Figure 6) is the cleanest and most convincing experiment.

**Clarity of writing:** Clear and well-organized through Section 6. The duplicate paragraphs in Section 5.1 and the buried within-type correlation caveat are the main clarity issues.

**Value to the research community:** High — the automated pipeline is directly usable, the preventative steering method is novel and practically motivated, and the data screening results are actionable. Multiple concrete tools are delivered.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>5</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>