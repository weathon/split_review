Now I have all the information needed to write the final consolidated review. Let me produce it.

---

## Summary

This paper presents an empirical analysis of MLLM hallucinations, finding that models encode correct visual information in middle layers (20–28) but this signal is suppressed by language-model priors in the final layer. Based on this finding, the authors propose **Deco** (Dynamic Correction Decoding), a training-free method that dynamically selects an anchor layer from the preceding layers and adds its logits (scaled by a dynamic modulation coefficient) to the final layer's logits. The method is evaluated on four MLLMs (InstructBLIP, MiniGPT-4, LLaVA-1.5, Qwen-VL) with three decoding strategies across CHAIR, POPE, MME, and GPT-4o evaluations, showing consistent hallucination reduction with only ~1.2× latency overhead.

## Strengths

- **Empirical finding that MLLMs encode correct visual information in middle layers.** The probing experiment (Section 2.1) shows ~80% accuracy for object existence classification from hidden states, including for objects that are ultimately hallucinated. The resolution increase experiment (224px→336px improving accuracy for non-existing objects) provides suggestive evidence that this signal is visual in nature (lines 105–114). This finding directly motivates and grounds the proposed method, and is a useful standalone contribution to understanding MLLM hallucination mechanisms.

- **Consistent hallucination reduction across diverse models and decoding strategies.** The method is tested on four different 7B MLLMs under greedy search, beam search, and nucleus sampling. The text reports consistent improvements on CHAIR (the 10.8% average suppression rate), POPE (F1 across random/popular/adversarial splits), and MME (lines 269–285). The GPT-4o evaluation further confirms accuracy improvements with only slight (and acknowledged) decreases in detailedness (lines 287–291). This breadth of evaluation makes a strong case that the method generalizes.

- **Significant practical efficiency advantage.** The method introduces only ~1.2× latency overhead compared to basic decoding, versus 1.8× for VCD and 5.1× for OPERA (lines 303–308). Since the method is training-free and model-agnostic, this combination of effectiveness and efficiency is a clear practical advantage for real-world deployment.

- **The dynamic preceding-layer selection is validated by multiple converging analyses.** The early-exit experiment (Figure 2, line 145) shows activated ground truth tokens concentrated in layers 20–28. The hit-rate analysis (Table 1, 61.69% for layers 20–28) quantifies how often the anchor layer's top candidate is correct. The perturbation experiment (random shifts of -5 to +5, line 310–315) shows degradation when selection is perturbed. The ablation on layer intervals (lines 327–330) confirms that layers 20–28 are optimal and that the effect is not uniform across layers. These converging analyses strengthen the claim that the selection mechanism is meaningful.

## Weaknesses

### Fatal
None.

### Major

- **The anchor layer selection mechanism carries an unquantified risk of amplifying wrong tokens.** The paper's own data (Table 1, line 183) shows that the anchor layer's top candidate is the ground truth only 61.69% of the time (layers 20–28). In the remaining ~38% of cases, a non-ground-truth token is selected as the anchor. Because the correction adds the anchor layer's logits to the final layer (Eq. 7, lines 212–214), this can potentially boost hallucinated tokens in those individual cases. The dynamic soft modulation coefficient (max_prob, lines 200–201) mitigates this partially by scaling down contributions when the anchor layer's top probability is low, but the paper does not provide a per-token breakdown of when the correction helps vs. hurts. The perturbation experiment tests a different question (wrong layer interval, not wrong token within the correct interval). Without this analysis, readers cannot assess whether the overall improvement masks occasional localized harm, or whether the method is robust even in cases where the anchor token is wrong.

- **The probing experiment (Section 2.1) does not fully rule out that the classifier exploits language-model priors rather than visual information.** The authors train linear probes on hidden states to predict object existence and interpret high accuracy as evidence that MLLMs "see" objects. However, these probes could be learning from object co-occurrence statistics or typical caption patterns encoded in the LM, not from visual input. The resolution increase experiment (224px→336px, line 113) is offered as supporting evidence, but higher resolution could improve any signal, not just visual. The paper lacks a controlled baseline — e.g., training the same probe on the model run without image tokens, or comparing probe accuracy when visual tokens are ablated — that would cleanly separate visual from textual-prior sources. Since the paper's entire motivational narrative (visual information is present but suppressed by LM priors) depends on this interpretation, this methodological gap is significant.

### Minor

- **The headline "10.8% hallucination suppression rate" is not explicitly defined in the visible text.** The abstract (line 44) and conclusion (line 274) state this figure, but the text does not specify whether it refers to the average relative reduction in CHAIR_I, CHAIR_S, or an aggregate across these. The CHAIR results table is embedded as \input and is a parser-stripped artifact. While it is standard practice in the field to define such figures in the corresponding table, the reader of the visible text cannot verify what exactly this number represents. This is easily fixed but creates ambiguity in its current form.

- **The hit-rate analysis (Table 1) reports only aggregate percentages without per-model or per-object-type breakdowns.** The method's anchor selection procedure depends on this hit rate, but the paper shows only two aggregate numbers (61.69% for layers 20–28, 71.14% for layers 15–28). Different MLLMs or object categories may have substantially different hit rates, which would affect the method's reliability. Standard deviations or per-model detail would be informative.

- **The 91.05% overlap rate (line 145) is reported as a single point without variance.** The paper states that 500 images were used (line 131), so the sample size is known, but no confidence interval or error bound is provided for this central quantitative finding about the language-prior suppression mechanism.

### Trivial
None.

## Nice-to-Haves

- A per-token analysis showing the distribution of "correction helps / hurts / no change" when the anchor token is correct vs. incorrect. This would directly address the main unresolved concern about the anchor layer selection risk.
- Reporting confidence intervals or running multiple random subsets for the CHAIR evaluation to establish statistical significance of the improvements.
- A qualitative discussion or examples of cases where the method worsens output (the paper acknowledges a slight decrease in detailedness but does not illustrate it).
- A controlled probe experiment without image input to strengthen the claim that the probe captures visual rather than textual-prior information.

## Removed Points

These points were raised in the input reviews but are not included as weaknesses in the final review, with brief justification:

- *"The baselines may not be fairly compared because their hyperparameters could be tuned per model"* — The paper explicitly states (line 236) that "For all the baselines, we use the default hyperparameters from the source code for a fair comparison." This is standard practice. The proposed method's hyperparameters (α and layer interval) are novel parameters required by the method itself, not tuned to advantage. Removed per soft rule on scope-creep and because the paper already addresses this concern.

- *"The paper should report statistical significance tests"* — Generic request that does not correspond to a standard practice gap in this specific paper. Moved to Nice-to-Haves.

- *"The paper should include a failure case analysis"* — A reasonable suggestion but not a weakness of the current submission. Moved to Nice-to-Haves.

- *The Strength Finder's general framing* — References to "this paper addressed an important problem" are generic and removed. All concrete, evidenced strengths are retained.

## Novel Insights

The most interesting observation emerging from synthesizing the reviews is a tension between the paper's two main claims: (a) that MLLMs encode correct visual information in middle layers, and (b) that the anchor layer's top token is the ground truth only ~62% of the time. These two facts sit somewhat uneasily together. If the model genuinely "sees" objects in layers 20–28, why is the top token wrong nearly 40% of the time? This tension suggests that the visual signal, while present, is not always the dominant signal even in those middle layers — the LM priors may already be competing there. The paper's own evidence (91.05% overlap with no-image candidate tokens) supports this. A more nuanced interpretation might be that the method works not because middle layers are purely visual, but because they are *less dominated* by LM priors than the final layer, and the correction rebalances the two information streams. This framing could make the modest hit rate less puzzling and more central to understanding why the method works.

## Suggestions

1. **Define and contextualize the 10.8% figure explicitly** in the main text (e.g., "average relative reduction across CHAIR_I and CHAIR_S"). This is a one-sentence fix that removes ambiguity.

2. **Add a per-token analysis** of the correction outcome, partitioned by whether the anchor token was correct or incorrect. Even a small-scale analysis on, say, 100 captions would directly address the anchor-layer risk concern and would likely strengthen the paper (since the overall positive results suggest the dynamic modulation handles most of the problematic cases).

3. **Add a controlled probe experiment** without visual input. Training the same linear probe on hidden states from a text-only forward pass (or from a model where image tokens are zeroed out) would cleanly separate visual signals from LM-prior signals and substantially strengthen the paper's central motivational claim.

4. **Include per-model breakdowns** in the hit-rate analysis (Table 1) and the 91.05% overlap figure to show the variability across different architectures.

## Score and Decision

**Originality:** Good. The empirical analysis of where visual vs. linguistic signals reside across MLLM layers is a valuable addition to a growing literature, and the dynamic anchor-layer selection is a clean technical contribution.

**Importance of research question:** High. MLLM hallucination is a widely recognized bottleneck for deployment, and training-free mitigation methods with low overhead are practically valuable.

**Claims well supported:** Mostly yes. The empirical findings are supported by multiple converging analyses, but the headline 10.8% figure needs explicit definition, and the anchor-layer risk analysis is incomplete.

**Soundness of experiments:** Good across a diverse set of models and benchmarks. The main concerns are the unquantified anchor-layer risk and the confound in the probing experiment's interpretation.

**Clarity of writing:** Good. The paper is well-structured, the motivation is clear, and the method description is precise.

**Value to the research community:** Positive. The empirical findings about layer-wise behavior inform future hallucination research, and the method is practical enough for adoption.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>