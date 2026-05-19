- Decision: Accept
- Avg Score: 5.50
- Scores: 3, 3, 8, 8
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper evaluates 10 open-source LMMs (OpenFlamingo and IDEFICS, 3B–80B) on five alignment-relevant axes—object hallucinations, abstention, compositionality, explainability, and instruction following—finding that scaling alone does not resolve these flaws. It then studies how in-context learning (ICL) affects each axis, showing nuanced effects (improves abstention/explainability, amplifies hallucinations, has no effect on compositionality). Finally, it proposes three training-free ICL variants (CoH-ICL, SC-ICL, MT-ICL) with mixed empirical results.

---

## Strengths

1. **Systematic multi-axis evaluation across model scales.**  
   The paper evaluates 10 models from 3B to 80B on five distinct axes using established benchmarks (COCO/CHAIRₛ, TDIUC, CREPE/SugarCREPE, VQA-X, LLaVA-w/GPT-4 judge). Figures 2–6 consistently show that even the largest models perform poorly in zero-shot, supporting the claim that "scaling alone is not enough" with concrete evidence across multiple metrics.

2. **Nuanced documentation of ICL's differential effects.**  
   Rather than a simple "ICL helps" narrative, the paper shows contrasting effects: ICL improves abstention F1 and explainability CIDEr, amplifies hallucinations beyond 4 shots (Finding 1), has near-zero effect on atomic compositionality (Finding 3), and only marginally improves instruction following. This set of findings (Findings 1–5) is a useful empirical contribution that goes beyond task-accuracy evaluation.

3. **Simple, training-free ICL variants with measurable gains in several configurations.**  
   CoH-ICL improves CIDEr by +9.33 (OFv2-9B, 4-shot, Table 2), SC-ICL boosts abstention F1 by +19.07 (OFv2-9B, 4-shot, Table 3), and MT-ICL improves both accuracy and CIDEr for explainability in several settings. These are modifications to the ICL input format only, making them directly applicable.

4. **Honest documentation of ICL's limited effectiveness.**  
   The conclusion explicitly states "the improvements coming from ICL are limited, and more complex ICL variants or other strategies, such as RLHF might be required" (line 394), which tempers the paper's stronger framing.

---

## Weaknesses

### Fatal
None.

### Major

1. **Hallucination amplification finding is confounded by caption length.**  
   The paper uses CHAIRₛ (proportion of hallucinated objects *among all mentioned objects*) to claim that ICL amplifies hallucinations beyond 4 shots. However, CHAIRₛ can increase simply because longer captions mention more objects—some of which may be hallucinated at a constant rate—rather than reflecting a higher *rate* of hallucination per noun. The paper does not report CHAIRᵢ (which normalizes by ground-truth objects) or control for caption length/CIDEr. This is stated at line 119 and Figure 2: "CIDEr (↑) for captioning and CHAIRₛ (↓) for hallucination." Without this control, Finding 1 ("increasing [shots] exacerbates the problem") is ambiguous: it could be that ICL makes models talk more, which naturally surfaces more hallucinated mentions. This is the paper's strongest behavioral claim and needs to be robust.

2. **Framing mismatch between "promising" ICL variants and mixed empirical results.**  
   The abstract and title present the ICL variants as effective solutions: "The proposed ICL variants are promising as post-hoc approaches to efficiently tackle some of those flaws." In practice, several configurations show degradation. For example:
   - CoH-ICL degrades CIDEr for OFv2-9B at 32 shots (−6.29, Table 2).
   - MT-ICL degrades CIDEr for IDEFICS-9B at 16 shots (−4.56) and 32 shots (−4.32, Table 2).
   - SC-ICL's abstention F1 gains shrink from +19.07 (4-shot) to −1.64 (32-shot, OFv2-9B, Table 3).
   The paper's own conclusion acknowledges "limited effectiveness," which conflicts with the aspirational framing. This overclaiming weakens the paper's credibility even though the evaluation itself is honest.

3. **Single architecture family limits generality of LMM claims.**  
   All 10 models are from the OpenFlamingo and IDEFICS families, which share the same core architecture (frozen LLM + frozen ViT + Perceiver Resampler + gated cross-attention), as described at lines 85–86. The title and abstract make claims about "large multimodal models" broadly, but it is unclear whether the findings generalize to other architectures (e.g., Q-Former in BLIP-2, vision-LLM concatenation in LLaVA). The limitation section (line 392) mentions "limited range of abilities" but does not explicitly scoped the architecture concern.

### Minor

4. **Missing standard deviations/reliability estimates.**  
   The paper states each experiment is repeated 3 times with different demonstrations (line 93) but reports only means in all figures and tables. For claims about small differences between ICL variants and baselines (e.g., +0.17 CIDEr for MT-ICL at 8-shot, Table 2), readers cannot assess whether the difference is meaningful. This is critical for an empirical evaluation study.

5. **SC-ICL shot imbalance not ablated in the main text.**  
   SC-ICL always uses 32-shot correction in step 2 regardless of the number of shots in step 1 (line 318). The paper mentions "we consider a smaller number of shots in \Cref{app:xicl_abs}" but does not report this ablation in the main paper. Performance gains could partly come from the total shot count being higher than the baseline, rather than from self-correction per se.

6. **CoH-ICL's "bad response" source is underspecified.**  
   Line 313 states: "previous model's generation (with ICL 32-shot) as the bad response." It is not clear whether this refers to the *same* model under the *same* ICL setting, or a different model/iteration. This matters for reproducibility.

---

### Trivial
None.

---

## Nice-to-Haves

- **Simple prompt engineering baseline.** The paper could compare ICL against prompting the model with an explicit textual instruction (e.g., "If the question cannot be answered from the image, say 'doesnotapply'"). The paper mentions "results with task instructions are in \Cref{app:task_inst}" but this analysis is deferred to the appendix.
- **Computational cost analysis.** SC-ICL runs the model twice per example and CoH-ICL uses longer contexts; reporting additional FLOPs or latency would strengthen the efficiency argument.

---

## Removed Points

These points were flagged by the reviewers but are removed with justification:

- *"The ICL variants lack theoretical justification"* — The paper is an empirical study; theoretical justification is not expected for simple ICL variants in this setting. Removed as a generic criticism.
- *"Axes not derived from a framework"* — The paper motivates the axes from the HHH (helpful/honest/harmless) framework in lines 37–41. Removed as factually incorrect.
- *"Does not survey concurrent benchmarks"* — The Related Work section (lines 377–385) discusses concurrent benchmarks (MMBench, MME, SEED-Bench). Removed as factually incorrect.
- *"Variants not tested on other axes"* — The paper explicitly scopes each variant to specific axes as a design choice. This is scope creep. Removed.
- *"2-shots without images concern not explored further"* — The paper raises this as a qualitative caveat (line 266); exploring further is outside the paper's scope. Removed.
- *"CoH-ICL degrades IDEFICS-9B at 16/32 shots"* — The critic attributed MT-ICL's degradation (−4.56, −4.32) to CoH-ICL. CoH-ICL on IDEFICS-9B is consistently positive across all shot counts (Table 2). The critic misread the table. Removed with correction.
- *"No comparison with simple prompt engineering"* — Moved to Nice-to-Haves.
- *"No computational cost evaluation"* — Moved to Nice-to-Haves.
- *"Conclusion's final sentence is not earned"* — This is a subjective assessment of a standard concluding statement. Removed.

---

## Novel Insights

The core novel observation from the review is the **CHAIRₛ/CHAIRᵢ confound analysis**: the paper's strongest behavioral claim (Finding 1) depends on a metric that is sensitive to caption length, and without controlling for this, the "ICL amplifies hallucinations" conclusion is weaker than presented. A secondary insight is that **the ICL variants' apparent value is inversely correlated with shot count** — improvements are largest at low shot counts (4–8) and often vanish or reverse at 32 shots — which suggests the variants are not scaling-robust solutions but rather compensate for insufficient demonstrations at low shot counts. This pattern is visible in both Tables 2 and 3 but is not discussed in the paper.

---

## Suggestions

1. **Address the CHAIR confound.** Report CHAIRᵢ alongside CHAIRₛ in the hallucination experiments, or plot CHAIRₛ against caption length. If CHAIRᵢ also increases with shots, the amplification claim is robust; if not, reframe Finding 1 as "ICL improves caption informativeness (CIDEr) at the cost of mentioning more hallucinated objects, but the per-object rate is stable."

2. **Tone down the ICL variant framing.** Revise the abstract and title to match the mixed results. Replace "promising" with a more neutral characterization (e.g., "we investigate whether simple ICL variants can address these flaws" and report the mixed outcomes). This would eliminate the framing mismatch.

3. **Explicitly scope architecture generality.** In the abstract, state that the study focuses on Flamingo-like architectures. Add a sentence in the limitations section noting that generalizability to other LMM families (e.g., Q-Former, LLaVA-style) is untested.

4. **Report standard deviations.** For the 3 repeated experiments, add error bars to all figures and ± ranges to all tables, especially for the ICL variant comparisons where differences are small.

5. **Ablate SC-ICL shot distribution.** Compare (N-shot ICL + 32-shot correction) vs. (N+32-shot ICL directly on the task) in the main text to isolate whether gains come from self-correction or from more total shots.

6. **Clarify CoH-ICL "bad response" construction.** Specify which model and which ICL setting produced the negative examples used as "bad responses."

---
