Now I have a solid calibration picture. Let me finalize the review.

## Summary

This paper proposes the Fast and Slow Effect (FSE) framework, a fully automated method to evaluate whether LLM/VLM-generated concept annotations are sufficient for class discrimination. The framework uses a five-stage concept refinement process (Background → Superclass → Salient Features → Detailed Features → Auxiliary Features) and the Class Representation Index (CRI) metric to quantify how well accumulated concepts support classification among semantically similar candidates. Experiments across six models and five datasets reveal that on fine-grained datasets (CUB-Bird, Cars, Flowers), concept-only ("slow mode") prediction underperforms direct visual ("fast mode") prediction by 25–30% CRI, while on general recognition datasets the trend reverses. The paper also demonstrates that high end-to-end utility (fused mode ≈ 90% CRI) does not imply annotation sufficiency (slow mode ≈ 50% CRI), challenging a common assumption in the field.

## Strengths

1. **Fully autonomous evaluation framework for annotation sufficiency** — The FSE framework (Section 4) is the first to assess whether automated concept-class annotations are *sufficient* according to a clear formal definition (Definition 3.1) without requiring human supervision. This directly addresses a gap where prior validation relied on costly human evaluation or the questionable utility-as-proxy assumption.

2. **Empirical discovery that concept-based (slow) mode underperforms visual (fast) mode on fine-grained tasks** — Table 2 reports CRI gaps between slow mode (t=5) and fast mode (t=0) averaging −25% to −27% across all six models on fine-grained datasets. Figure 3 shows consistent trends across model families and sizes, contradicting the expected "Slow Mode Superiority" (Section 4.2).

3. **Demonstration that the utility-as-proxy assumption is misleading** — Table 4 shows that fused (fast + slow) mode CRI reaches ≈90% while slow mode alone achieves only ≈50% under identical conditions. This quantitative discrepancy directly supports the paper's claim that high downstream accuracy does not imply annotation sufficiency.

4. **Rigorous distractor selection methodology** — Section 5.3 systematically compares random vs. semantically related distractor strategies (Table 1), showing that random selection yields low contradiction rates (14–20%) while semantic selection raises them to 34–45%, ensuring the candidate set realistically challenges annotators.

## Weaknesses

### Fatal
None.

### Major

1. **The CRI metric conflates concept quality with the model's text-only reasoning capability** — The paper interprets low CRI in slow mode as evidence that "current annotation methods fail to provide sufficient semantic coverage" (Abstract) and that concepts "fail to provide sufficient semantic coverage" (line 085). However, CRI is operationalized by having the *same model* that generated the concepts also classify from them in a text-only setting. A low CRI could equally arise if the concepts are perfectly sufficient but the model's *text-only classification ability* is poor relative to its heavily optimized visual pipeline — especially for fine-grained distinctions requiring integration of multiple subtle cues. The paper provides no experiment that disentangles these two factors (e.g., an external evaluator baseline using humans or a different LLM to classify from the same concepts). While the paper occasionally hedges ("challenging for them to conceptualize this knowledge," line 087), the headline claims overreach relative to what CRI actually measures. The framework is still useful as a diagnostic, but the core interpretive claim needs either (a) a resolving experiment that isolates concept quality or (b) honest reframing around the joint limitation.

2. **No analysis of the generated concepts themselves** — The paper treats the concept chain as a black box and reports only aggregate CRI scores. There is no characterization of the concepts: how many per class/image, how much overlap between semantically similar classes, whether they are visual vs. functional vs. ecological, or whether critical discriminative attributes are systematically missing. Without this analysis, the reader cannot assess *why* concepts fail, and the paper's diagnostic value is limited. A few examples in the removed appendix are insufficient — a table or analysis quantifying concept properties would substantially strengthen the paper.

### Minor

1. **CRI formula (Equation 2) contains an apparent indexing error** — The formula writes `(1/t) Σ_{i=1}^{t} 𝟙[y_i^t = y_i]`, where `t` is the annotation step (1–5). The sum should run over test set instances `i = 1…l` and divide by `l`. The reported results (e.g., 94.07% CRI) are clearly computed correctly, so this is a typo — but as written it is formally wrong and undermines reproducibility.

2. **Preliminary contradiction test (Section 5.3) does not report initial visual accuracy** — The contradiction rate measures whether `y^init ≠ y^con`, but without knowing whether `y^init` was correct, a contradiction could indicate that the concept-based prediction *corrected* a visual mistake — which would actually *support* annotation sufficiency. Reporting the full confusion matrix or the accuracy of each prediction would resolve this ambiguity.

3. **Statistical significance is not formally tested** — Standard deviations over three seeds are reported and appear small, but there is no formal test (e.g., McNemar's test or confidence intervals) for whether the CRI gap between modes is significant. Given that only three runs were conducted, the reader cannot fully assess reliability.

### Trivial
- Equation (2) uses `t` as both annotation step and (incorrectly) as the summation bound/denominator. Fix to sum over test instances `i = 1…l` and divide by `l`.

## Nice-to-Haves
- **Sensitivity analysis on candidate set size**: Using exactly 4 distractors is motivated (Section 5.3) but testing 1, 2, or 8 distractors would demonstrate CRI robustness.
- **Ablation of concept refinement stages**: Showing CRI after removing each of the five stages would validate whether the five-stage design is optimal or whether fewer stages suffice.
- **Comparison against ground-truth concept vocabularies**: For CUB-200-2011, which has human-annotated part-attribute vocabularies, reporting concept overlap or coverage would provide direct evidence of what high-quality concepts look like.
- **More explicit discussion of the t=0 to t=1 collapse**: The massive CRI drop (from ~90% to ~30%) on fine-grained datasets is striking but not discussed in depth; noting that first-stage concepts (Background+Superclass) are inherently unhelpful for fine-grained discrimination would strengthen the narrative.

## Removed Points

These points were raised in the reviews but are removed or downgraded for the reasons stated:

- **"The five-stage refinement feels arbitrary"**: The paper explicitly maps prior work (1-stage: Yuksekgonul et al., Yang et al.; 2-stage: Sun et al., Panousis et al.; 3-stage: Oikarinen et al.) and positions the 5-stage design as an extension. A sensitivity analysis would be nice but the design is not arbitrary.
- **"Utility-as-proxy experiment is not surprising because the model may ignore concepts"**: This is a plausible interpretation but is speculation, not a concrete weakness. The experiment still cleanly demonstrates the discrepancy.
- **"Common datasets 'opposite trend' claim is overstated"**: Table 3 shows slow mode at t=5 outperforms fast mode on CIFAR-100 (94% vs 85%) and Caltech-101 (94% vs 91%). The claim is supported.
- **"Section 4.1 lacks explicit mapping to prior stage structures"**: The paper does provide this mapping (prior work cited with their stage counts).
- **"Post-hoc results on common datasets not reported"**: The post-hoc scenario inherently lacks fast-mode comparison, making it less informative for this analysis. A minor omission at most.
- **Formatting/style nitpicks**: Parser artifacts, not author errors.
- **Reproducibility concerns about released code/data**: The paper states "code and data at here" — the parser likely stripped the link.
- **"Missing appendix content"**: Stripped by parser.

## Novel Insights

The most interesting observation from the reviews is the parallel between this paper's sufficiency problem and a similar issue in the "Sufficient Context" paper (Jjr2Odj8DJ, score 6.25). Both papers define a notion of "sufficiency" and build evaluation frameworks around it, and both face the core challenge that the sufficiency judgment depends on the evaluator's capability. The "Sufficient Context" paper partially addresses this by using a separate autorater model that was validated on hand-labeled data, whereas this paper uses the same model for both concept generation and evaluation. This comparison suggests a concrete path for resolving the main weakness: introducing a separate evaluator (human or different model) validated on a small labeled set would significantly strengthen the claim that concepts themselves (not reasoning) are the bottleneck.

## Suggestions

1. **Disentangle concept quality from reasoning capability** by adding an external evaluator baseline. Have humans (even a small set, N=50–100 samples) or a completely different LLM (e.g., GPT-4o classifying concepts generated by Llama, and vice versa) classify from the generated concepts alone. If external evaluators achieve significantly higher accuracy than the original model's slow mode, the concepts are sufficient and the original model's reasoning is the bottleneck — which would actually be an *even more* interesting finding.

2. **Reframe the headline claims** to acknowledge explicitly that CRI measures a joint property of concept quality × textual reasoning capability. The paper's contribution does not depend on proving that concepts alone are insufficient; the gap observation is valuable regardless of where the bottleneck lies.

3. **Add a concept content analysis** quantifying concept properties (number, overlap, type distribution) for at least one dataset. This would help explain *why* slow mode fails — e.g., are concepts too generic, overlapping too much between similar classes, or missing key visual attributes?

4. **Fix the CRI formula typo** and report formal significance tests (e.g., paired McNemar's test for the fast vs. slow comparison).

## Score and Decision

**Round 1 bracket**: After the first calibration pass, the initial bracketing placed this paper between the weak anchors (avg 3.0–3.4, clearly rejected papers with limited novelty/conceptual fallacies) and the strong anchors (avg 8.0, unrelated topics). The middle-band anchors (3.5–7.5) included ConLUX (4.67, reject), CB-LLM (5.75, accept), and "Automating High-Quality Concept Banks" (3.4, reject).

**Round 1 bracket stated**: Between 4.5 and 6.0.

**Round 2 narrowing**: Retrieved anchors in (4.5, 6.0) yielded "Automated Knowledge Concept Annotation" (5.33, reject), "LLMs are Demonstration Pre-Selectors" (5.25, reject), "Measuring LLM Uncertainty with Internal Concepts" (5.60, reject), and "Boosting Concept Bottleneck Models" (5.00, reject). Anchors in (6.0, 7.5) yielded "Sufficient Context" (6.25, accept), "PretexEval" (7.00, accept), "SePer" (7.25, accept), and "Beyond Single Concept Vector" (6.75, accept).

**Comparisons to specific anchors read in full**:
- vs. **"Evaluating the Unseen"** (3.0, reject): This paper is substantially stronger — the FSE framework is better motivated, experiments are broader (6 models vs. 2, 5 datasets vs. 3), and the methodology is cleaner.
- vs. **"Automating High-Quality Concept Banks"** (3.4, reject): Significantly stronger — more novel framework, broader evaluation, and the utility-as-proxy finding is a genuine insight.
- vs. **ConLUX** (4.67, reject): Comparably solid methodology, but the current paper has broader experiments and a clearer evaluation target. However, ConLUX had no comparable confound issue.
- vs. **CB-LLM** (5.75, accept): Both papers have genuine contributions. CB-LLM has clearer novelty (first concept bottleneck for LLMs) while this paper has broader experiments. The current paper is held back by the interpretive overreach (unresolved confound) that CB-LLM did not share.
- vs. **"Sufficient Context"** (6.25, accept): Both papers define sufficiency evaluation frameworks. The SC paper is stronger because it validates its autorater on hand-labeled data and cleanly separates the sufficiency measurement from the model's reasoning ability. This paper's analogous issue (failing to separate concept quality from reasoning) is its main weakness.
- vs. **"Automated Knowledge Concept Annotation"** (5.33, reject): Similar applied framing but this paper has a more generalizable framework and more surprising empirical findings.

The paper is clearly above the 3–4 range and below the 6.25+ range. Within (4.5, 6.0), it sits closer to CB-LLM (5.75, accepted) than to ConLUX (4.67, rejected). However, the confound issue prevents me from rating it at the CB-LLM level. The paper's genuine contributions (autonomous framework, CRI metric, utility-as-proxy debunking, broad experiments) justify a score above 5, but the interpretive overreach pulls it down. 

**Final score**: 5.0 / 10. **Decision**: Reject, with the recommendation that the authors address the core confound (via an external evaluator baseline or honest reframing) and resubmit.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>