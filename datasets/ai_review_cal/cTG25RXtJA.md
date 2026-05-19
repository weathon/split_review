- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3
Now I have a complete picture of the paper. Let me produce the consolidated review.

**Key observations from cross-checking:**

1. **Missing Section 3.3**: The paper announces Section 3.3 (Knowledge-Enhanced Prompt Learning) in line 57, but the provided text jumps directly from Section 3.2 to Section 4 (line 92). However, line 103 shows clear parser artifacts: "324 325 326 327 328..." embedded inline as text. This is undeniable evidence of a corrupted PDF extraction. Consistent with instructions to treat formatting/parser artifacts as not the authors' fault, I will **REMOVE** this as a weakness.

2. **Knowledge input not ablated (training-time)**: The paper's Figure 4 already evaluates "prompts without knowledge" at inference time, showing performance degrades. The critic asks for a training-time ablation. This is partially addressed — the paper does show knowledge matters, just at inference rather than training time. **WEAKEN** to minor/nice-to-have.

3. **Asymmetric comparison**: The critic says KEEP uses external knowledge that baselines don't. This is partially true — some baselines (KgCoOp, LASP, TCP) also use class-level knowledge, just not image-wise. Still, KEEP has access to more information. **KEEP** as a genuine concern but note nuance.

4. **Interpretability claims**: The paper provides faithfulness via knowledge intervention (Figure 4) and attention visualizations (Figure 5). No quantitative XAI metrics (insertion/deletion, concept sensitivity). **KEEP** as a minor weakness.

Let me write the review.## Summary

This paper proposes KEEP, a framework that enhances VLM (CLIP) adaptation by generating image-wise knowledge-enhanced prompts using retrieval-augmented generation (RAG) and domain-specific foundation models, then learns semantic correspondences between images and these prompts via an attention mechanism. The key idea is moving beyond class-level coarse prompts to per-image fine-grained knowledge (e.g., clinical concepts for medical images). Experiments on 8 datasets (4 medical, 4 natural) show consistent gains (≈3.2% on medical, ≈2.6% on natural) over existing prompt-learning baselines, with particular strength in low-data regimes.

## Strengths

1. **Novel integration of RAG and domain-specific FMs for image-wise prompt generation.** The paper is the first to combine retrieval-augmented generation (MEDRAG, PMC-LLaMA, MedCPT) with domain-specific vision-language models (KAD, BiomedCLIP) to produce per-image knowledge prompts rather than class-level templates. This is a concrete, non-obvious extension of prior work (KgCoOp, LASP, TCP) and is clearly described in Section 3.2 (Algorithm 1, Equation 2, and the clinical concept extraction pipeline).

2. **Consistent and significant empirical gains across diverse domains.** Across all 8 datasets (Tables 1, 2), KEEP outperforms every baseline (CoOp, CoCoOp, Tip-Adapter, KgCoOp, LASP, GraphAdapter, TCP) with average relative improvements of ~3.2% on medical and ~2.6% on natural domains. The gains are not concentrated on one modality — they hold for dermoscopic, chest X-ray, brain MRI, objects, aircraft, flowers, and textures.

3. **Robust data efficiency, explicitly demonstrated.** Table 3 shows that on medical datasets, KEEP maintains strong performance even with 10–50% of training labels (e.g., nearly no drop on Pneumonia from 100% to 50% data). Figure 3 shows consistent few-shot superiority across 1, 2, 4, 8, 16 shots on natural datasets. This directly supports the claim that injected domain knowledge compensates for scarce annotations.

4. **Component ablation validates the proposed learning modules.** Table 4 shows that removing the image-prompt attention logit (−1.6% medical, −1.3% natural) and the image-prompt matching loss (−1.1% medical, −1.0% natural) both degrade performance, confirming that each designed component contributes.

5. **Quantitative faithfulness evaluation via knowledge intervention.** Figure 4 measures accuracy under five prompt conditions (no knowledge, random, general, fine-grained, intervened semantics). Performance degrades systematically when knowledge is corrupted, providing objective evidence — beyond qualitative visualizations — that the knowledge prompts reflect the model's reasoning.

## Weaknesses

### Fatal

None.

### Major

1. **Asymmetric comparison: KEEP leverages external knowledge sources unavailable to baselines.** KEEP generates image-wise prompts using domain-specific foundation models (KAD, BiomedCLIP) and RAG (MEDRAG corpus, PMC-LLaMA, MedCPT). The baselines (CoOp, CoCoOp, Tip-Adapter, KgCoOp, etc.) use only generic prompts like "a photo of a [class]" or class-level descriptors. This asymmetry means the reported gains (~3.2% medical, ~2.6% natural) may partly reflect the value of the external knowledge itself rather than the specific prompt learning framework (attention module, losses). The paper does not include a controlled variant — e.g., feeding the same knowledge-enhanced prompts into a simpler baseline like CoOp (without the attention mechanism) — to isolate the contribution of the learning framework from the contribution of the richer input. This limits the conclusiveness of the head-to-head comparisons. *Why it matters*: Without this control, a reader cannot determine whether any existing method would also benefit from simply having better input prompts, or whether KEEP's specific architectural innovations are responsible for the gains.

### Minor

2. **Interpretability evaluation, while present, lacks quantitative rigor for a framework branded "Explainable."** The faithfulness test (Figure 4) is a necessary sanity check — it shows the model is sensitive to its knowledge input — but it does not measure explanation quality. No standard XAI metrics are used (e.g., insertion/deletion curves for attention, pointing game for localization, concept sensitivity scores, or human evaluation of plausibility). The textual/visual explanations (Figure 5) are purely qualitative, and while the highlighted concepts appear domain-reasonable, this does not distinguish whether the attention reflects genuine reasoning or learned prompt artifacts. *Why it matters*: The paper's title and framing center on explainability as a core contribution, but the evidence provided is thinner than what the XAI community expects for a method claiming to "enhance trustworthiness in high-risk domains."

3. **The accuracy of concept predictions from domain-specific FMs is not evaluated.** Section 3.2 describes using KAD and BiomedCLIP to predict the presence/absence of clinical concepts (Equation 2). Errors in these predictions propagate directly into the knowledge-enhanced prompts, affecting both classification accuracy and the quality of explanations. No analysis is provided (e.g., precision/recall of concept prediction on held-out data, examples of correct vs. incorrect predictions). *Why it matters*: The framework's reliability in practice depends on these upstream predictions being accurate, yet the paper treats them as a fixed, unexamined input.

### Trivial

None.

## Nice-to-Haves

- **A training-time ablation that isolates the knowledge source from the learning framework.** The paper could train KEEP's full pipeline (attention module, L_IPM, L_CLS) with generic prompts ("a photo of a [class]") instead of knowledge-enhanced prompts. This would directly quantify what the knowledge contributes vs. what the learning framework contributes. Figure 4's inference-time intervention partially addresses this, but a training-time version would be cleaner.
- **Larger-scale medical benchmarks** (e.g., ChestX-ray14, MIMIC-CXR) would strengthen generalizability claims beyond the relatively small datasets used (Derm7pt, Open-i, CCBTM).
- **Statistical significance tests** (e.g., corrected t-test across runs) would confirm gains are beyond random variation, though the 3-run means and consistent pattern partially mitigate this concern.

## Removed Points

- **Missing Section 3.3 (Knowledge-Enhanced Prompt Learning) as a fatal weakness.** The paper announces this section (line 57) and the ablation study (Table 4) references components from it (logit_IPA, L_IPM, L_CLS). However, line 103 shows obvious PDF extraction artifacts ("324 325 326 327 328..." embedded as inline text), confirming the content was lost during parsing, not omitted by the authors. Per the instructions, formatting artifacts from PDF extraction are not author errors and should not be treated as weaknesses.

- **Criticism about GPT-4 being a proprietary API and reproducibility concerns from LLM stochasticity.** Per the hard rule: "REMOVE any criticism that questions the existence, release status, or availability of any model, tool, benchmark, dataset, or reference cited in the paper." The paper cites GPT-4 and MiniGPT-4; their existence is not in question.

- **Criticism about missing large-scale medical datasets (ChestX-ray14, MIMIC-CXR).** The paper scoped its evaluation to 4 medical datasets covering 3 modalities (dermoscopic, chest X-ray, brain MRI). Requesting specific additional datasets is scope creep; the existing coverage is reasonable for a conference submission.

- **Criticism about the "first to incorporate RAG" claim being overstated.** The hard rule states: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up." I cannot verify whether prior work exists that also does this.

- **Criticism about baselines not being equally tuned.** The paper states grid search was used for hyperparameter selection (Section 4.1). Without evidence of unfair tuning, this is speculative.

- **Generic strengths** from the Strength Finder about the problem being important or the paper being well-written — these are removed as they lack specific, concrete evidence.

## Novel Insights

The harsh critic and strength finder collectively surface a tension that the paper itself does not fully resolve: KEEP has two intertwined contributions — (a) generating richer image-wise prompts via RAG+domain-specific FMs, and (b) a novel prompt learning framework (attention module, logit fusion, losses) designed to exploit those prompts. The evaluation treats (a)+(b) as a package, but the reviewer analyses correctly note that the paper never cleanly separates them. This is the central open question for future iterations. A secondary insight from the meta-analysis is that the faithfulness intervention (Figure 4), while limited, is actually more informative than the critic gives it credit for: testing "without knowledge," "random knowledge," "general knowledge," "fine-grained knowledge," and "intervened knowledge" as a spectrum establishes a monotonic relationship between knowledge quality and accuracy, which is a non-trivial sanity check that goes beyond a single binary comparison.

## Suggestions

1. **Add a controlled baseline**: Apply CoOp or KgCoOp with the same knowledge-enhanced prompts KEEP uses, but without the attention module and image-prompt matching loss. If KEEP still outperforms this variant, the gains are attributable to the learning framework; if not, they come from the richer prompts. This single experiment would address the most serious evaluation concern.

2. **Evaluate concept prediction quality**: Report precision/recall or F1 of the domain-specific FM's concept predictions (Equation 2) against human annotations on at least one medical dataset. This grounds both the performance and interpretability claims.

3. **Strengthen the XAI evaluation with at least one quantitative metric**: For example, compute deletion/insertion AUC using the attention weights from the image-prompt attention module. This is standard in the attribution literature and would substantially raise the bar for the interpretability claim without requiring additional data collection.

4. **Complete Section 3.3 with formal equations** for the attention mechanism, the logit fusion, and both loss functions (L_IPM, L_CLS) — as intended.
