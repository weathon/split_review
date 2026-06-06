---

## Summary

The paper proposes **Copy-Paste**, a RAG faithfulness paradigm arguing that verbatim copying of contextual fragments reduces faithfulness hallucinations. It contributes: (1) three prompting methods (CP-Order, CP-Link, CP-Refine) that generate high-copying responses; (2) **CopyPasteLLM**, a DPO-trained model using these high-copying responses as preference data; and (3) **Context-Parameter Copying Capturing**, a token-level interpretability tool that measures contextual vs. parametric knowledge reliance during generation. The paper claims 12.2%–24.5% FaithEval accuracy improvements over the strongest baselines using only 365 training samples.

---

## Strengths

- **Stage 1 prompting methods are well-validated across four model families.** Table 2 systematically evaluates CP-Order, CP-Link, and CP-Refine against Attributed and Citations baselines across Mistral-7B, Llama-3.1-8B, Qwen2.5-72B, and DeepSeek-V3-0324. CP-Refine achieves the best hallucination reduction in 14/24 evaluation scenarios, with MiniCheck faithfulness gains of +10.9% to +19.1% over Attributed/Citations baselines. These results are clean, internally consistent, and require no training-data caveats.

- **Genuine data efficiency in Stage 2.** CopyPasteLLM uses 365 preference pairs (vs. 18,000 for Context-DPO, 10,000 for Canoe, 32,580 for ParamMute). Even accounting for the in-distribution FaithEval concern detailed below, the method's sample efficiency is noteworthy.

- **ConFiQA cross-domain generalization is a real result.** CopyPasteLLM (trained on FaithEval-sourced data, not ConFiQA) matches or surpasses Context-DPO on ConFiQA despite Context-DPO having been trained on ConFiQA (marked ᵀ). For Mistral-7B-v0.2, CopyPasteLLM achieves 80.8% on ConFiQA-MR and 82.5% on ConFiQA-MC, vs. Context-DPO's 81.3% and 80.4% (both trained on ConFiQA). This cross-benchmark transfer is substantive.

- **Novel interpretability contribution.** The Context-Parameter Copying Capturing algorithm extends Knowledge Token Capturing (Bi et al., 2024) to the full CoT trajectory rather than only short final answers. Figure 3 provides position-aware logits power distributions showing CopyPasteLLM achieves earlier and stronger contextual engagement, which is a methodologically interesting finding.

- **Non-counterfactual results (Table 3) confirm contextual faithfulness does not harm accuracy when context is correct.** CopyPasteLLM improves over base models by an average of 10% on challenging ConFiQA-MR/MC subsets (e.g., +20.67% for Mistral-7B-v0.2 on MR), demonstrating the benefit is not narrow to counterfactual settings.

---

## Weaknesses

### Fatal

None identified.

### Major

- **FaithEval evaluation is not an out-of-distribution comparison.** Table 1's caption explicitly states: *"We removed 241 samples used for training CopyPasteLLM from FaithEval, with the remaining samples used for testing."* Since CopyPasteLLM is trained on 365 samples total, approximately 241/365 ≈ 66% of its training data is drawn directly from the FaithEval distribution. Meanwhile, all competing fine-tuning baselines (Context-DPO, Canoe, ParamMute) are trained on ConFiQA (marked ᵀ), meaning FaithEval is genuinely out-of-distribution for them but in-distribution for CopyPasteLLM. The headline 12.2%–24.5% FaithEval accuracy improvements—featured prominently in the abstract and conclusion—cannot be cleanly attributed to the Copy-Paste approach; they are at least partly explained by distributional proximity. The paper should either (a) report FaithEval results using a version of CopyPasteLLM trained entirely on non-FaithEval data, (b) train baselines on the same FaithEval-sourced preference data, or (c) re-center the headline claims on ConFiQA and PubMedQA where the comparison is fair. In its current form, the primary headline result is not a fair apples-to-apples comparison.

- **Missing answer-stamping ablation in the main text.** Section 3.2 describes "gold answer stamping"—appending the correct answer to the top-ranked Copy-Paste candidate before DPO training. This is a distinct mechanism from the copying behavior itself: it can inject correct final-answer signal directly into training. Whether the observed counterfactual accuracy gains in Table 1 come from the copying preference, the stamped answer, or their interaction is the key internal validity question for Stage 2. The paper defers this to Appendix G (stripped in the reviewed version). An ablation removing stamping is essential to the main text, given it determines whether the contribution is "copying internalizes contextual trust" or "correct answer injection."

### Minor

- **Motivating correlation (Section 2.2) is cross-model, not within-model.** Figure 1's lower panel shows an inverse correlation between copying degree and hallucination density across six *different* models. These models (Mistral-7B, Llama-2-7b, 13b, 70b, GPT-3.5, GPT-4) differ systematically in scale, alignment, and training—all of which independently affect both metrics. The correlation may be confounded by model capability (e.g., GPT-4 hallucinates less and also tends to have different copying behavior for reasons unrelated to copying per se). Section 2.2 frames this as motivating evidence that copying *reduces* hallucinations, but it cannot support a causal reading. The Stage 1 within-model intervention evidence (Table 2) is far more compelling and should be foregrounded as the primary motivation.

- **UMAP mechanistic claim requires quantitative support.** Section 4.2 asserts that *"contextual knowledge representations in CopyPasteLLM remain nearly co-distributed with those in base models, while their parametric knowledge distributions differ substantially"* (the key mechanistic conclusion), supported by UMAP visualizations in Figure 4. UMAP is sensitive to n_neighbors, min_dist, and random seed and is not reliable for distributional comparisons. This claim should be corroborated with a quantitative test (e.g., MMD or KL divergence in the original representation space) rather than relying solely on visual inspection of 2D projections.

- **Fluency of CopyPasteLLM is not directly reported.** Table 2 shows that CP-Order and CP-Link sacrifice fluency substantially over baselines. Since DPO training is performed on high-copying candidates that include these extractive responses, whether DPO training preserves or repairs this fluency deficit is unaddressed in the main text. Section 2.1 identifies fluency as a key component of the Copy-Paste trade-off, making this gap notable for practical deployment claims.

### Trivial

None identified.

---

## Nice-to-Haves

- **Dual-metric evaluation across both stages.** Stage 1 uses faithfulness metrics (AlignScore, MiniCheck) while Stage 2 uses accuracy (Acc/Hit). Reporting both metric types in both stages would allow direct assessment of whether DPO training preserves the faithfulness gains demonstrated in Stage 1, or trades them away.
- **Filtering criterion transparency in Figure 3.** The logits power analysis filters to samples where CopyPasteLLM responses were shorter than base responses, which is a reasonable choice but could selectively sample toward harder base cases. Reporting the result for the full sample set alongside the filtered one would strengthen the analysis.
- **ConFiQA-QA vs. counterfactual subsets discussion.** The paper acknowledges that ConFiQA-QA improvements are modest (+1.01% average) while ConFiQA-MR/MC gains are large (+10%). A brief analysis of why the counterfactual subsets benefit more would strengthen the mechanistic narrative.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic – GPT-4o comparison in Section 4.1.2**: The paper explicitly frames this as a "reported" number and places it in the Appendix (Table 6), not as a direct apples-to-apples comparison. The in-distribution concern already covers the FaithEval issue more precisely.

- **Harsh Critic – LLM-as-Judge circularity**: This is a speculative concern dependent on unexamined judge behavior. There is no evidence in the paper that the judge favors copying responses as such; the judge is diagnosing "Twist" and "Causal" hallucination modes (Section 3.2). Without positive evidence of circularity, this is category-driven noise.

- **Harsh Critic – Medical framing assumes retrieval reliability**: The paper explicitly acknowledges this in Section 7 (Ethics Statement): *"The method's effectiveness depends on the quality and accuracy of the provided context, and users should exercise caution when applying this approach in sensitive applications."* The criticism is addressed.

- **Harsh Critic – Counterfactual accuracy as a problematic metric**: This is a philosophical concern about the counterfactual evaluation paradigm, not a specific flaw in this paper. FaithEval and ConFiQA are established benchmarks for RAG faithfulness research; criticizing their use here without a concrete alternative reflects scope creep.

- **Strength Finder – Motivating empirical foundation as a core strength**: Retained but demoted. The cross-model correlation is a reasonable qualitative observation but cannot support causal claims and is documented as a Minor weakness above.

- **Strength Finder – Generic claim about automated pipeline being "highly reproducible"**: This is not a specific evidenced strength — removed as superficial.

---

## Novel Insights

The most genuinely novel finding is the mechanistic dissociation revealed by Context-Parameter Copying Capturing: CopyPasteLLM recalibrates *parametric* confidence rather than enhancing *contextual* representations. Figure 3 shows earlier and stronger contextual logit engagement, while Figure 4 (with the noted UMAP caveat) suggests contextual hidden states remain similar to the base model but parametric representations diverge. If validated quantitatively, this "selective parametric suppression" mechanism offers a principled account of why high-copying training generalizes across benchmarks: it reduces the pull of internal priors rather than learning a new contextual processing routine, which would make the approach broadly applicable. This is a substantive insight that distinguishes the contribution from prior faithfulness fine-tuning work.

---

## Suggestions

1. **Re-run Stage 2 with a fully held-out training set for FaithEval.** Train CopyPasteLLM on 365 samples sourced only from non-FaithEval data, then evaluate on the full FaithEval test set. If the 12-25 point gains survive, the headline claim stands firmly. If they shrink, re-center the paper around ConFiQA and PubMedQA, where the comparison is already fair and the results are still competitive.

2. **Add a stamping ablation to the main text.** Report Table 1 results with stamping vs. without stamping (i.e., the top Copy-Paste candidate without the appended gold answer). This single ablation is the key internal validity check for Stage 2.

3. **Replace or complement UMAP in Section 4.2 with a quantitative distributional test** (e.g., Maximum Mean Discrepancy or a paired t-test on cosine similarities in the original embedding space) to put the "parametric suppression" mechanism claim on firm footing.

4. **Report fluency metrics for CopyPasteLLM outputs** (e.g., perplexity or human ratings), comparing to both the base model and the Stage 1 CP methods. This addresses the fluency-faithfulness trade-off that the paper identifies as a core concern in Section 2.1 but does not close in Stage 2.

---

## Score and Decision

**Originality**: The Copy-Paste paradigm is a natural and intuitive idea; the main novelty is the complete pipeline (three prompting methods, automated preference construction, DPO training, and interpretability tool) and the parametric-suppression mechanistic finding. Moderately original.

**Importance of research question**: RAG faithfulness is highly relevant. The data efficiency (365 samples) angle addresses a practical deployment barrier.

**Claims supported**: The Stage 1 claims are well supported. The headline Stage 2 FaithEval claims are substantially weakened by in-distribution training overlap. ConFiQA results partially rescue the generalization claim.

**Soundness of experiments**: Stage 1 experiments are sound. Stage 2 has a significant methodological gap that the paper discloses but does not fix. UMAP analysis is visually suggestive but not quantitatively rigorous.

**Clarity**: Writing is clear and the two-stage structure is well-organized. The training-data overlap issue, though disclosed in a table caption, is not prominently discussed.

**Value to the research community**: The prompting methods (Table 2) and interpretability tool are standalone contributions with value to RAG practitioners. The full two-stage system's value is contingent on resolving the evaluation issue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>