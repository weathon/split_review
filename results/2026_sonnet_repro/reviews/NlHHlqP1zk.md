Now let me run calibration searches to determine the appropriate score range.**Round 1 bracket: 3.5 – 6.0** (similar XAI/concept-annotation evaluation papers score 3.0–5.75; strong anchors are unrelated topics)

Let me narrow with round 2.Let me read the most directly comparable anchor papers.Now I have sufficient calibration to write the final review. Let me synthesize all findings.

## Summary

The paper proposes the Fast and Slow Effect (FSE) framework for automatically evaluating whether LLM/VLM-generated concept annotations are *sufficient* to support accurate concept-class reasoning in XAI, without human supervision. FSE introduces the Class Representation Index (CRI) metric, which measures how well incrementally accumulated text concepts allow a model to select the correct class against semantically similar distractors. Experiments across five datasets and six LLMs show that slow (text-only) mode consistently underperforms fast (vision-based) mode on fine-grained datasets by over 25% on average, and that fused (vision+text) evaluation closely tracks vision-only performance—undermining the widely used utility-as-proxy assumption for validating annotations.

---

## Strengths

1. **Identifies a genuine gap and provides a concrete evaluation protocol**: The paper formalizes the notion of *sufficient concept-class annotation* (Definition 3.1) and shows systematically that existing annotation validation practices (human evaluation and utility-as-proxy) are either costly or misleading. The FSE framework fills this gap with an automatic, scalable alternative.

2. **The utility-as-proxy critique (Table 4) is the paper's strongest finding**: The experiment directly shows that fused fast+slow mode achieves ~90% CRI while slow mode alone reaches only ~50% across all three fine-grained datasets and both GPT-4o and GPT-4o-mini. This is a clean, practically important result: downstream task accuracy improves by incorporating visual signal while the concept text contributes almost nothing, meaning high utility scores can persist even when annotations are semantically vacuous from an interpretability standpoint. This finding challenges a common evaluation practice in the CBM community.

3. **Broad experimental scope**: Five datasets (three fine-grained + two general), six LLMs spanning three model families and two scales, and both post-hoc and visual-grounded annotation scenarios. The three-run error bars (Figure 3) show negligible variance, so the main trends are robust.

4. **General vs. fine-grained comparison sheds light on task difficulty**: Table 3 shows that slow mode surpasses fast mode on CIFAR-100 and Caltech-101 (>90% CRI at t=5), while failing substantially on fine-grained datasets. This cross-dataset contrast is informative and suggests the framework captures meaningful variation in annotation quality rather than a constant artifact.

5. **Preliminary contradiction test (Table 1) validates the distractor strategy**: The semantically related selection strategy yields 34–45% contradiction rates vs. 14–20% for random selection, confirming the chosen distractor construction is non-trivial and adds rigor to the pipeline.

---

## Weaknesses

### Fatal

None that unambiguously invalidate all results from the paper as written.

---

### Major

**1. Formula error in the CRI definition (Equation 2) — the primary metric is ill-defined as stated.**

The paper defines:

> *CRI(F, t; D_test, D_cls) := 100% × (1/t) × Σᵢ₌₁ᵗ 𝟙[yᵢᵗ = yᵢ]*

This sums over i from 1 to t and divides by t, conflating the annotation step index t with the instance count. The paper separately defines l as "the total number of cases" (Section 4.1), and the prose definition immediately above Eq. 2 states CRI is "the proportion of correctly predicted labels y_iᵗ compared to the ground-truth labels y_i from D_cls" — which clearly means summing over all l instances and dividing by l. At t = 0 (fast mode), Eq. 2 is undefined (1/0 × empty sum), yet CRI(0) is computed and reported throughout Tables 2, 3, and 4. The correct formula should use l as the denominator with the sum running from 1 to l. As the paper's primary measurement instrument, this must be corrected and the actual operationalization used in experiments stated unambiguously.

**2. Interpretive ambiguity: modality gap vs. annotation insufficiency is not controlled.**

The paper's headline claim is that the CRI gap (slow mode ≪ fast mode on fine-grained datasets) reveals annotation failure. However, slow mode removes the image and operates purely on text, making the gap potentially attributable to a general text-visual modality limitation for fine-grained tasks, not the LLM annotations specifically. The paper never runs a control: if *human-authored, ground-truth* textual descriptions of fine-grained classes (e.g., CUB-200 part annotations) were fed to the same slow-mode pipeline and also produced low CRI, the finding would implicate the modality rather than the LLM. Without this control, both interpretations remain consistent with the data. The paper partially mitigates this via Table 3 (slow mode succeeds on general datasets), which is suggestive but not conclusive, since the general/fine-grained distinction conflates task difficulty, number of classes, and inter-class similarity. This ambiguity is specifically relevant to the paper's main framing ("Are Large Language Models Good XAI Annotators?") and the conclusion that current LLMs fail.

---

### Minor

**3. The t=1 CRI collapse is not explained and represents a structural artifact.**

Table 3 shows that for GPT-4o on CIFAR-100, CRI drops from 84.84% (fast) to 29.23% at t=1, then recovers to 94.07% at t=5. This pattern is consistent across all models (Table 3, FineGrained-Avg: from 92.97% at t=0 to 27.67% at t=1). The cause is structurally apparent: Stage 1 provides only "Background" context (e.g., "ocean scene"), which carries no discriminative signal for a five-way choice among similar classes. The paper does not explain this and presents the t=1 collapse without comment, which could mislead readers into interpreting it as meaningful evidence about annotation failure at a critical early stage. The paper should acknowledge this as an expected artifact of the coarse-to-fine stage design rather than leaving it unexplained.

**4. Circular self-evaluation design.**

In the post-hoc scenario especially, the same model (e.g., GPT-4o) both generates concept annotations and evaluates whether those concepts suffice for classification. The model's internal associations between concept language and class names could create systematic consistency bias that is internal to the model's own embedding space — not a general sufficiency property. This limitation is not acknowledged in the paper and is relevant for interpreting the post-hoc results.

**5. ResNet-18 distractor selection is not fully characterized.**

Section 5.3 states the Semantic Similarity Dictionary is built from "a pretrained ResNet-18." It is unclear whether this model was fine-tuned on the target datasets or used as a generic ImageNet-pretrained feature extractor. For CUB-200, a generic ResNet-18 may not reliably identify the most visually confusable species. This affects what the candidate set is actually testing and should be clarified.

---

### Trivial

- The Conclusion (Section 7) is generic ("We encourage future work...") and does not engage with the paper's most striking finding — that slow mode uniformly underperforms fast mode on fine-grained datasets, or what this implies for concept-based XAI in specialized domains. A more substantive conclusion is warranted.

- The dual-process theory (Kahneman, 2011) motivation for Slow Mode Superiority (Section 4.2) is strained: replacing the image with text is not an instance of deliberate reasoning outperforming intuitive reasoning; it is a modality substitution. This should be framed more precisely.

---

## Nice-to-Haves

- Run slow-mode evaluation with human-authored or dataset-provided textual descriptions (e.g., CUB-200 part annotations) as a reference point. If expert text also fails slow mode, it is a modality finding; if it succeeds, annotation insufficiency is confirmed.
- Extend the utility-as-proxy critique (Table 4) to all six models, not just GPT-4o and GPT-4o-mini. This is the paper's cleanest finding and broader coverage would make it more impactful.
- Provide a mechanism explanation for Table 4: why does the model ignore informative concept text when vision is available? This could be connected to attention routing or modality dominance literature.
- The paper samples 100 images per dataset in Section 5.3 to build the SSD; with 200 classes in CUB-200, coverage is thin. Discussing the reliability of distractor assignment under this constraint would strengthen the methodology.

---

## Removed Points

*These points are flagged as removed; treat with caution.*

- **Harsh Critic's "structural underdetermination" framing of the modality gap**: Retained as a Major weakness, but the claim that it makes the paper "unfixable" was demoted because Table 3 partially addresses it (slow mode succeeds on general datasets). The weakness stands but is not fatal.
- **Strength Finder: "CRI-gap of −25.2% to −27.1% directly proves insufficiency"**: Removed as a strength because the same figures are subject to the modality gap concern raised as a Major weakness. A finding that is contested cannot be listed as an unqualified strength.
- **Strength Finder: "The experimental design is thorough including a preliminary contradiction test"**: Partially retained (the preliminary test adds rigor), but the claim that it "validates the semantically related distractor strategy" is a reasonable strength since it shows a 2.4× increase in contradiction rate over random selection.
- **Harsh Critic's concern about Kahneman dual-process analogy leading readers astray**: Retained as a Trivial point but not Major — the analogy is strained but does not invalidate any result; it only provides flawed motivation for an expected phenomenon.

---

## Novel Insights

The paper's most genuinely novel insight is not the main CRI-gap finding but the utility-as-proxy decomposition (Table 4): the observation that joint visual+text evaluation achieves ~90% CRI while text-only evaluation achieves ~50% reveals that concept text is functionally inert once visual input is present. This makes "high downstream accuracy" a *necessary but insufficient* signal for annotation quality, and the gap between fused and slow-only CRI serves as a direct measure of how much the model relies on visual shortcut vs. conceptual supervision. This has a concrete implication: any evaluation protocol that assesses annotation quality by plugging annotations into an end-to-end pipeline with visual input is almost certainly measuring vision quality, not annotation quality. This finding is actionable and deserves more prominence.

---

## Suggestions

1. Fix Equation 2 to use l as both denominator and upper summation bound; separately define and handle the t=0 fast-mode case, which must be stated explicitly since it does not fit the t > 0 formula.
2. Add a "ground-truth text" control condition on CUB-200 using part-level annotations; this either confirms the main finding or reframes it as a modality limitation.
3. Move the utility-as-proxy experiment (Table 4) to the primary results section and extend it to all six models. This is the most unambiguous contribution.
4. Explain the t=1 collapse explicitly as a consequence of the Stage 1 design (background context only), not as evidence of early-stage annotation failure.
5. Acknowledge the circular self-evaluation limitation in Section 8 (Ethics and Limitations) and discuss whether cross-model evaluation (generate with one model family, evaluate with another) changes the findings.

---

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| `KLUDshUx2V.md` — Automating High-Quality Concept Banks (LLMs + CBMs) | 3.4 | R1/R2 | Very similar topic; weaker on experiments (2 datasets, 1 evaluator), poor writing. The paper under review is substantively stronger. |
| `kTjEPEy96Q.md` — Evaluating Unsupervised CBMs | 3.0 | R1 | Similar evaluation-framework scope; also rejected. Paper under review has broader coverage and a cleaner key finding. |
| `0qrTH5AZVt.md` — ConLUX: Concept-Based Local Unified Explanations | 4.67 | R1 | Proposes a new method (not just evaluation), rejected. Comparable complexity to the paper under review. |
| `zp88xOXAfS.md` — Linearly Interpretable Concept Embedding (Text CBMs) | 4.8 | R1/R2 | New method + experiments; also rejected. Paper under review is comparable in novelty. |
| `Q9Z0c1Rb5i.md` — Boosting CBMs with Hierarchical Concept Learning | 5.0 | R2 | New method (SupCBM), rejected. Narrower scope than FSE's 6 models × 5 datasets. |
| `RC5FPYVQaH.md` — Concept Bottleneck LLMs | 5.75 | R1/R2 | Proposes CB-LLM (new method), accepted. More novel than an evaluation framework. |
| `L9U5MJJleF.md` — Concept Bottleneck Generative Models | 6.0 | R2 | New generative method; accepted. Different contribution type. |
| `c7DND1iIgb.md` — Democratizing FGVR with LLMs (FineR) | 6.67 | R2 | New training-free FGVR method using LLM world knowledge; accepted; strong soundness score. More novel than a pure evaluation framework. |

**Round 1 bracket**: 3.5 – 6.0

**Round 2 narrowing**: The paper under review is stronger than the two rejected evaluation-framework papers (3.0–3.4) in experimental scope and finding quality, and it contributes a cleaner insight than the rejected method papers at 4.67–4.8. However, it sits below the accepted method papers (5.75–6.67) because it does not propose a new classification method and its central interpretive claim (annotation insufficiency) has a genuine uncontrolled confound. The utility-as-proxy finding is strong but occupies only one experiment (Table 4, two models only). The CRI formula error is a real issue that must be corrected. This places the paper at the lower end of the 4.0–5.0 range — meaningfully above the 3.0–3.4 papers but clearly below acceptance-level work.

**Final score: 4.5 — Reject.** The paper addresses a real and important question, the experimental scope is commendable, and the utility-as-proxy critique is a genuine contribution. However, the primary metric (CRI) is defined by a formula that is undefined at t=0 and conflates annotation step with instance count; the central interpretive claim (CRI gap = annotation insufficiency) is not disentangled from a modality gap confound; and the circular self-evaluation design is unacknowledged. These are not presentation issues — they are methodological and definitional weaknesses that require substantive revision before the paper's core claims can be trusted.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>