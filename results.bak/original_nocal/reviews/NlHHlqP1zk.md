Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

The paper proposes the Fast and Slow Effect (FSE) framework, an autonomous evaluation protocol for assessing whether LLM/VLM-generated concept annotations for XAI are semantically sufficient to distinguish target classes from similar alternatives. FSE guides annotators through a five-stage concept refinement chain (from coarse background to fine-grained features), tracking the Class Representation Index (CRI) at each step. On three fine-grained datasets (CUB-Bird, Car, Flower), the authors find a systematic CRI drop of ~25% from fast mode (direct visual inference) to slow mode (concept-only reasoning), showing that current annotation methods fail to externalize sufficient discriminative knowledge. The paper further demonstrates that the common "utility-as-proxy" assumption is misleading: fused image+concept predictions reach ~90% CRI while concept-only predictions score ~50%.

## Strengths

1. **First fully autonomous framework for validating annotation sufficiency.** FSE requires no human evaluators, addressing a real bottleneck in XAI concept annotation pipelines. Definition 3.1 formalizes what "sufficient" means in this context, and the five-stage refinement process (Background → Superclass → Salient Features → Detailed Features → Auxiliary Features) builds naturally on prior hierarchical extraction methods (Oikarinen et al., 2023; Sun et al., 2024; Panousis et al., 2024).

2. **Strong empirical evidence of annotation insufficiency on fine-grained datasets.** Table 2 shows CRI-Gap values of −25% to −27% averaged across six LLMs on Car, Flower, and CUB-Bird datasets. The consistent direction and magnitude of this gap across model families (GPT-4o, Llama-3.2-vision, QwenVL2) makes it unlikely to be an artifact of a single annotator.

3. **Direct invalidation of the utility-as-proxy assumption.** Table 4 shows fused (image+concepts) CRI of ~90% while concept-only CRI is ~50%. This cleanly demonstrates that high downstream task accuracy can coexist with poor conceptual annotations, confirming a concern raised by prior leakage literature (Havasi et al., 2022) but without needing to train a CBM or manipulate concept labels.

4. **Carefully designed distractor selection.** The preliminary experiment (Table 1) shows that random distractor selection yields only 14–20% contradiction rates, while semantically related distractors (via SSD) raise this to 34–45%, establishing that the evaluation is diagnostically challenging rather than trivially easy.

5. **Nuanced dataset-dependent finding.** Table 3 reveals that on common datasets (CIFAR-100, Caltech-101), slow mode *outperforms* fast mode, while on fine-grained datasets the opposite holds. This boundary condition is important: it shows LLM annotations can be sufficient for broad categories but fail precisely where XAI matters most (specialized, fine-grained discrimination).

## Weaknesses

### Fatal
None. The core claims are supported by the experimental evidence as presented.

### Major
None. The paper has no verifiable flaw that threatens its central conclusions.

### Minor

1. **CRI formula contains a notational error (Eq. 2).** The equation writes `(1/t) Σ_{i=1}^{t} 𝟙[y_i^t = y_i]`, using the annotation step index *t* in place of the total number of test cases *l*. This makes the formula uncomputable for *t=0* (division by zero) and would incorrectly scale the denominator with the step index. The textual description ("the proportion of correctly predicted labels") and the actual experimental results (coherent CRI values across steps with error bars) make it clear that the implementation uses the correct computation `(1/l) Σ_{i=1}^{l} 𝟙[y_i^t = y_i]`. Nonetheless, this notational slip is confusing and should be corrected.

2. **The "slow mode superiority" hypothesis is conceptually debatable.** The paper expects slow mode (concept-only) to outperform fast mode (raw image), citing dual-process theory. But textual concept annotations are an inherently lossy compression of visual information. A gap between fast and slow modes partly reflects the information bottleneck of language, not necessarily annotation insufficiency. The paper's results are still informative—if the concepts *were* sufficient, the gap should shrink—but interpreting the gap solely as a failure of annotation quality is too strong. The paper would benefit from a discussion of this confound.

3. **Limited analysis of *why* slow mode fails.** The paper attributes the CRI gap to "insufficient semantic coverage" but does not analyze whether the problem is (a) missing concepts, (b) ambiguous concepts, (c) concepts that apply to multiple classes, or (d) the model's inability to reason over its own text (self-consistency). A failure-mode categorization (e.g., via human inspection of a sample of errors) would substantially strengthen the paper's diagnostic value.

4. **No human annotation baseline.** Without comparing CRI scores for human-written concepts (or oracle concepts), it is unclear whether the observed insufficiency is a property of LLMs specifically or of text-based annotations in general. If human concepts also score low on CRI, the metric may be too stringent rather than revealing an LLM-specific weakness. The paper acknowledges this implicitly (Section 8 mentions ethical limitations) but does not address it experimentally.

### Trivial

1. In Table 3, the "FineGrained-Avg" row for GPT-4o shows a fast-mode (t=0) CRI of **92.97**, while Figure 3(a) fast-mode values for the three fine-grained datasets individually are much lower (roughly 60–95% range across datasets, averaged should not be 92.97). This appears to be a labeling error — the table seems to show fine-grained averages that are inconsistent with Figure 3.

2. The paper states "three runs (with different seeds) were conducted" for Figure 3 but does not specify what is randomized across runs (model sampling temperature? subset selection?). The claim that standard deviations are "negligible" should be backed by reported numerical values.

## Nice-to-Haves

- **A proof-of-concept use of FSE as a training signal.** The paper critiques existing annotation methods but stops at evaluation. Showing that FSE can guide iterative refinement to improve annotation quality would significantly raise the contribution. For example, one could prompt the LLM with its CRI failures and ask it to rewrite concepts to resolve ambiguities.
- **Human annotation CRI comparison.** Comparing human-written vs. LLM-generated concepts on the same images would validate whether CRI captures something meaningful about annotation quality or is merely a stress test.
- **Test of utility-as-proxy in an actual concept bottleneck model.** The fusion experiment in Table 4 is valid for the claim it makes, but training a proper CBM that *forces* the classifier to use only concept scores (as in standard CBM training) and showing that high accuracy can coexist with poor concept quality would be a stronger refutation of the assumption.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"CRI metric is mathematically ill-defined / fatal"** — Removed. The notational error in Eq. (2) (using *t* instead of *l*) is real but cosmetic; the actual experimental implementation clearly computes the correct accuracy-like metric, as evidenced by coherent CRI values across steps and error bars from multiple runs. The intended definition is clear from the prose, and the error does not affect any reported result.

2. **"Distractor selection via ResNet-18 undermines the claim of no human supervision"** — Removed. Using a pretrained model (even one trained on human-annotated data) as a tool to construct the challenge set does not violate the claim of *autonomous evaluation* (no new human annotation required per test case). This standard applies to virtually all automated evaluation methods in the field.

3. **"Utility-as-proxy experiment does not test the assumption"** — Partially removed. The critic argues the fused mode lets the model ignore concepts. This misses the point: the experiment shows that end-to-end accuracy (~90% CRI) can be high while concept-only accuracy (~50%) is low, which *directly* demonstrates that utility is a poor proxy for annotation quality. A proper CBM test is nice-to-have but not required to make this valid point.

4. **"No justification given for five-stage refinement process"** — Removed. The paper explicitly justifies this in Section 4.1: it extends prior work (Yuksekgönül et al. single-level, Sun et al./Panousis et al. two-level, Oikarinen et al. three-level) into a five-stage hierarchy. The number of stages is a design choice justified by precedent.

5. **"No baseline comparing against human annotations or simpler automatic method"** — Moved to Nice-to-Haves. This is a genuine limitation but it's a suggestion for future work, not a flaw in what the paper does achieve.

6. **"Small sample sizes"** — Removed. The paper runs experiments on standard benchmark datasets (CUB-200, Cars-196, Flowers-102, CIFAR-100, Caltech-101) at their full test-set sizes and reports 3-run averages with negligible variance. There is no evidence of reliability concerns.

7. **"Ethics discussion is generic"** — Removed. This is a formatting nitpick; the ethics section is standard for the venue and engages with specific risks (biased annotations in sensitive domains).

8. Various speculative criticisms about prompt engineering quality, appendix availability, and generic "area-of-concern" framing — Removed per filtering rules.

## Novel Insights

The most interesting synthesis from the reviews is that the FSE framework reveals a *reverse* superiority of fast over slow mode specifically on fine-grained datasets, while the expected pattern holds on common datasets. This asymmetry is not predicted by dual-process theory (which motivated the Slow Mode Superiority hypothesis) and suggests that the bottleneck is not reasoning capability per se but the *precision of lexicalization* — LLMs know the difference between a Black-footed and Laysan Albatross when seeing the image (fast mode) but cannot produce textual features that capture the distinguishing cues. This points toward a fundamental limitation of current text-based concept annotations: they capture *typical* features but not *discriminative* ones, which is precisely what fine-grained XAI requires.

## Suggestions

1. **Fix Equation (2).** Replace `(1/t) Σ_{i=1}^{t}` with `(1/l) Σ_{i=1}^{l}` to match the intended definition and enable correct evaluation at t=0.

2. **Add a failure-mode analysis.** Sample ~50 errors from the slow mode, categorize them (missing concept, ambiguous concept, concept shared across classes, reasoning failure), and report distributions. This would greatly strengthen the diagnostic contribution.

3. **Clarify the relationship between Table 3's "FineGrained-Avg" row and Figure 3.** The fast-mode CRI of 92.97% for GPT-4o in Table 3 appears inconsistent with the individual fine-grained dataset values in Figure 3. Explain the discrepancy or correct the table.

4. **Discuss the information bottleneck of text explicitly** as a confound in interpreting the CRI gap, and explain why the gap cannot be entirely attributed to annotation insufficiency.

5. **Report numerical variance values** (standard deviations) for the CRI results rather than just stating they are "negligible."

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>