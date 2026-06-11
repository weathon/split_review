Now I have sufficient calibration data. Let me finalize the review.

**Round 1 bracket:** Based on comparison with anchors, I bracket this paper between 5.5 and 6.5:
- Clearly above rejected evaluation framework papers (3.0-5.5 range): more systematic evaluation, novel utility-as-proxy finding, better written
- Comparable to accepted papers at 5.75-6.25 range: CB-LLM (5.75), Enhancing Cognition (6.00), Faithful CBMs (6.25)
- Similar quality to lHbLpwbEyt (6.00): both have clear contributions and solid experiments but notable methodological limitations

**Round 2 narrowing:** The paper's genuine contribution (utility-as-proxy critique via Table 4) is important and well-supported. The weaknesses (theoretical overclaiming, self-evaluation circularity) are interpretive, not empirical. The paper is clearly above the rejected evaluation frameworks. I'll settle on **6.0**.

---

## Summary
This paper proposes the Fast and Slow Effect (FSE) framework for evaluating the sufficiency of LLM/VLM-generated concept annotations in concept-based Explainable AI. It introduces the Class Representation Index (CRI) metric and a five-stage progressive concept refinement process, finding that concept-only ("slow mode") classification drops ~25% below direct visual ("fast mode") classification on fine-grained datasets. Critically, the paper demonstrates that fused multimodal inference masks this insufficiency, challenging the utility-as-proxy assumption in XAI evaluation.

## Strengths
- **Empirical refutation of the utility-as-proxy assumption (Table 4):** The fused mode (image + concepts) achieves ~90% CRI while concept-only mode achieves only ~50-60% on the same datasets (e.g., GPT-4o on Car: Fuse=93.08% vs Slow=60.82%). This directly demonstrates that strong downstream task performance can mask fundamentally insufficient textual annotations—a significant and actionable finding for the XAI community that challenges a widespread evaluation practice.
- **Well-defined, unsupervised evaluation metric (CRI):** The Class Representation Index (Equation 2) provides a simple, interpretable metric measuring whether generated concepts alone can distinguish correct classes from semantically similar alternatives, with diagnostic granularity via marginal CRI increments at each refinement step.
- **Systematic empirical breadth:** Evaluation spans 6 LLMs (GPT-4o, GPT-4o-mini, Llama-3.2-vision-90b/11b, QwenVL2-72b/7b), 5 datasets (3 fine-grained, 2 general), 2 annotation paradigms (post-hoc and visual-grounded), and 3-seed repetitions with negligible variance, providing generalizable findings.
- **Cross-dataset contrast reveals specificity of failure:** Table 3 shows slow-mode CRI exceeds 90% on CIFAR-100 and Caltech-101 (with slow outperforming fast), while fine-grained datasets see CRI below 60% with negative CRI-Gaps. This pinpoints that the insufficiency is specifically a fine-grained discrimination problem, which is more informative than a uniform failure.
- **Validated distractor selection methodology (Table 1):** A dedicated preliminary experiment shows semantically related distractors (via ResNet-18 SSD) yield 2-3x higher contradiction rates than random selection, ensuring the evaluation meaningfully challenges the annotators.

## Weaknesses

### Fatal
None.

### Major
- **Theoretical framing overclaims relative to evidence.** The paper attributes the ~25% CRI gap between fast and slow modes to LLMs' inability to "externalize their implicit expertise" and invokes Kahneman's dual-process theory (Section 4.2, lines 163-167: "According to the dual-process theory... fast mode serves as a 'black box' approach... Slow mode involves a detailed, conceptual, and multi-step reasoning process... We expect this CRI gap to be non-negative"). However, the slow mode explicitly removes the visual input (lines 140-143: "the original input X_i is no longer required, and the prediction relies solely on the high-level conceptual annotations"), while the fast mode retains it. In Kahneman's theory, both systems operate on the *same* input; here the inputs fundamentally differ (image vs. text). The simpler explanation—that text descriptions are inherently lossy for fine-grained visual discrimination—is directly supported by the paper's own results showing slow mode *outperforms* fast mode on general datasets where text carries enough discriminative information (Table 3). The central narrative of "opaque expertise" is not disambiguated from this alternative interpretation. This matters because the paper's framing drives its conclusions and presentation, even though the empirical findings (concepts are insufficient, utility-as-proxy is flawed) remain valid regardless.

- **Self-evaluation circularity limits the strength of conclusions.** The framework uses the same LLM to both generate concept annotations and evaluate their sufficiency via CRI (acknowledged at line 9 as "self-evaluate annotations"). If the model has systematic blind spots in verbalizing its visual knowledge, those same blind spots affect its ability to classify from the generated concepts—conflating "the concepts are insufficient" with "this particular model cannot use text concepts as well as it uses images." Without cross-model or human validation, the paper cannot distinguish whether the insufficiency lies in the annotations themselves or in the evaluator model's text-processing limitations.

### Minor
- **No justification for five refinement stages.** The paper extends prior 2-3 stage approaches to 5 stages (line 117: "The choice of five stages *reflects* and builds upon established methodologies") but provides no ablation showing that 5 is optimal or necessary. An ablation over stage count would strengthen the framework design.
- **ResNet-18 for distractor selection lacks justification for this specific context.** The semantic similarity dictionary is built from ResNet-18 confusion patterns (Section 5.3, line 197), but no argument is given for why ResNet-18's failure modes represent the most challenging distractors for LLM/VLM annotators specifically.
- **Limitations section (Section 8) is generic and misses core methodological concerns.** The limitations section discusses dataset generalization and societal impact but does not acknowledge the information-modality confound or self-evaluation circularity, which are the most significant methodological limitations of the framework.

### Trivial
None.

## Nice-to-Haves
- Cross-model evaluation (Model A generates concepts, Model B classifies from them) would disentangle annotation quality from evaluator limitations.
- Human classification from generated concepts would ground-truth the CRI metric.
- Qualitative analysis of what specific discriminative concepts are missing in failure cases would make findings more actionable for improving annotation methods.
- Testing concept-mediated reasoning (image → concepts → class) vs. direct reasoning (image → class) while keeping the image present in both would better isolate the effect of conceptual mediation, addressing the modality confound.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **CRI formula notation error (Eq. 2):** The harsh critic flagged that Eq. 2 sums from i=1 to t (the step index) instead of i=1 to l (total instances), which would divide by zero at t=0 and use only 5 instances at t=5. This is almost certainly a parser artifact—the empirical results (CRI values in the 50-95% range across hundreds of instances) are impossible if computed over only 5 instances. The intended formula is clearly CRI(t) = 100% × (1/l) Σ_{i=1}^l 𝟙[y_i^t = y_i].

## Novel Insights
The most genuinely novel observation from this paper is the demonstration (Table 4) that multimodal fusion can achieve near-perfect CRI (~90%) while concept-only evaluation shows severe insufficiency (~50-60%), empirically invalidating the widely-used utility-as-proxy assumption in XAI evaluation. This finding—that downstream task accuracy improvements can coexist with fundamentally insufficient conceptual annotations—is a concrete, actionable contribution that challenges a pervasive evaluation practice in the concept-based XAI literature, independent of the contested theoretical framing around dual-process theory.

## Suggestions
- Restructure the central fast-slow comparison to acknowledge that the modality difference (image vs. text) is an inherent confound, and reframe the finding as "LLM-generated textual concepts are insufficient for fine-grained visual discrimination" rather than "LLMs cannot externalize their implicit knowledge."
- Add a cross-model validation experiment where a different model evaluates the generated concepts, to separate annotation quality from evaluator quality.
- Include an ablation over the number of concept refinement stages to justify the 5-stage design.

## Reporting

**Round 1 anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 5kMwiMnUip (Jailbreaking LLMs) | 1.40 | 1 | Completely different topic; weak paper |
| 8QTpYC4smR (Systematic Review of LLMs) | 1.00 | 1 | Survey paper, not comparable |
| kTjEPEy96Q (Evaluating Unsupervised CBMs) | 3.00 | 1 | Most comparable rejected paper; same evaluation-for-CBMs niche but had conceptual fallacy |
| KLUDshUx2V (Automating Concept Banks) | 3.40 | 1 | Similar topic (LLM concepts + evaluation) but low novelty, poor writing |
| J0qgRZQJYX (Axiomatic Concept Explanations) | 3.00 | 1 | Concept explanations, rejected |
| wZiH43e5Ah (CAN Concept Extraction) | 3.00 | 1 | Concept extraction framework, rejected |
| 0qrTH5AZVt (ConLUX) | 4.67 | 1 | Concept-based local explanations, rejected |
| todLTYB1I7 (Principled Evaluation for Neuron Explanations) | 5.00 | 1 | Similar evaluation-framework focus; rejected despite being well-written |
| zp88xOXAfS (Linearly Interpretable Concept Embedding) | 4.80 | 1 | Concept embedding model, rejected |
| TdyfmCM8iR (Latent Concept-based Explanation) | 4.33 | 1 | Concept-based NLP explanation, rejected |
| RC5FPYVQaH (CB-LLM) | 5.75 | 1 | Accepted; novel CBM for LLMs, comparable quality |
| ARFRZh6pzI (CLEAR Metacognitive LLM) | 6.00 | 1 | Accepted; metacognitive LLM evaluation |
| VvAiCXwPvD (Counterfactual Simulatability) | 5.67 | 1 | Rejected; XAI evaluation paper |
| lHbLpwbEyt (Enhancing Cognition LMMs) | 6.00 | 1 | Accepted; closest accepted anchor in quality |
| Q9Z0c1Rb5i (SupCBM) | 5.00 | 2 | CBM with hierarchical concepts, rejected |
| 5Aem9XFZ0t (Z-CBMs) | 4.83 | 2 | Zero-shot CBMs, rejected |
| WqsYs05Ri7 (Uncertainty-aware Concept Explanations) | 5.20 | 2 | Concept explanations with uncertainty, rejected |
| rp0EdI8X4e (Faithful CBMs) | 6.25 | 2 | Accepted; faithful concept bottleneck, comparable |
| xrgXaOV6dK (LLM Annotation Quality) | 5.50 | 2 | LLM annotation evaluation, rejected |
| 9OevMUdods (Factual Knowledge of LLMs) | 6.75 | 2 | Accepted; LLM knowledge benchmark |
| Q5eo3VMxF6 (MisAttributionLLM) | 5.75 | 2 | LLM evaluation framework, rejected |
| 0sJ8TqOLGS (LLM SPARK) | 5.25 | 2 | LLM evaluation framework, rejected |

**Round 1 bracket:** 5.5–6.5. The paper is clearly above rejected evaluation frameworks (3.0–5.5) due to its systematic evaluation and novel utility-as-proxy finding, and comparable to accepted papers at 5.75–6.25.

**Round 2 narrowing:** After comparing with rp0EdI8X4e (6.25, accepted, strong formal contribution) and lHbLpwbEyt (6.00, accepted, similar experimental scope), I narrow to **6.0**. The paper has genuine, impactful contributions (utility-as-proxy critique, CRI metric, systematic evaluation) but the theoretical framing overclaims and self-evaluation circularity is unaddressed. The empirical core is solid; the interpretation needs refinement.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>