Now I have all the information needed to finalize the review. Let me write the consolidated review.

## Calibration Summary

**Round 1 bracket:** Between ~2.0–3.0 (weak rejection anchors: ETe03Iyluy avg 3.0, QA4wj30Bhf avg 2.5) and ~8.0 (strong accept anchors: VKGTGGcwl6 avg 8.0, DM0Y0oL33T avg 8.0). The paper clearly falls in the middle band (3.5–7.5).

**Round 2 narrowing anchors read in full:**
- **gdEWoxhb70** (avg 5.50, Accept Poster) — CBM paper with SAE concept extraction. More severe methodological concerns (data leakage, proprietary dependencies). Current paper is cleaner methodologically.
- **BQ0jaVCZRK** (avg 4.50, Reject) — Concept probing paper with no human ground truth, LLM-as-judge circularity. Current paper is significantly stronger.
- **dIzJ5tjHf4** (avg 4.50, Reject) — Competency gap paper, only 2 small models, validation issues. Current paper is stronger.
- **hxGdAUn3sB** (avg 6.00, Accept Poster) — GNN self-consistency paper. Cleaner execution but simpler contribution. Current paper comparable in quality.
- **1bKvM7Ay9G** (avg 5.00, Reject) — Concept-based explanations. Had motivation/novelty issues. Current paper is stronger.
- **jPOecVdGG7** (avg 5.00, Reject) — Image-caption evaluation framework. Similar framing but the current paper has a clearer, more impactful finding.

**Final score:** 5.5. The paper sits between the 5.00 reject anchors (stronger than those) and the 6.00 accept anchor (comparable but with some framing imprecision). It is most similar in quality to gdEWoxhb70 (5.50, Accept Poster) — both have real contributions and clean experiments but contain interpretive issues that prevent a uniformly enthusiastic reception.

---

## Summary

This paper proposes the Fast and Slow Effect (FSE) framework and the Class Representation Index (CRI) to automatically evaluate whether LLM/VLM-generated concept annotations are semantically sufficient for accurate concept-to-class mapping in XAI. By comparing a *fast mode* (direct visual classification) against a *slow mode* (concept-only classification), the paper finds a negative CRI gap of 25–27% on fine-grained datasets — the slow mode underperforms the fast mode, contradicting the expectation that explicit concepts should aid classification. The most striking result is Table 4: the fused (vision+concepts) mode achieves ~90% CRI while the slow mode alone scores ~50%, directly demonstrating that high downstream accuracy does not imply sufficient concept annotations.

## Strengths

1. **Direct empirical challenge to the utility-as-proxy assumption.** Table 4 shows fused-mode CRI (~90%) vs. slow-mode CRI (~50%) under identical conditions, proving that strong end-to-end performance can coexist with insufficient concept annotations — a clean counterexample to a widespread evaluation practice in concept-based XAI.

2. **Novel, principled, and automated evaluation framework.** Definition 3.1 provides a clear formal criterion for annotation sufficiency, and the CRI metric (Eq. 2) operationalizes it via controlled comparison against semantically similar distractors. The entire framework requires no human supervision, addressing a practical bottleneck in annotation validation.

3. **Broad and consistent experimental coverage.** Six models from three families (GPT-4o, Qwen2-VL, Llama-3.2), three fine-grained datasets (CUB, Cars, Flowers) and two general datasets (CIFAR-100, Caltech-101), with three runs showing negligible standard deviation. The negative CRI gap is consistent across models and fine-grained datasets, and the recovery on general datasets (Table 3) provides an informative contrast.

4. **Counter-intuitive and timely finding.** The result that LLMs systematically fail to externalize their implicit expertise into explicit textual concepts — despite having that knowledge (as shown by fast-mode performance) — is a documented limitation that the community needs to confront.

## Weaknesses

### Fatal
None.

### Major

1. **Interpretive framing outpaces what the evidence cleanly supports.** The paper concludes that "current annotation methods fail to provide sufficient semantic coverage" (abstract, conclusion), but the CRI measures a *joint* property: whether the model can infer the class *given the concepts*. Definition 3.1 correctly defines sufficiency this way — concepts must "enable accurate inference" — so the CRI gap genuinely measures insufficiency *per the paper's own definition*. However, the framing consistently emphasizes annotation quality ("semantic coverage") over the equally plausible interpretation that models struggle to reason from textual concepts even when the concepts contain adequate information. The fused-mode experiment (Table 4) shows the concepts *can* be useful when combined with vision, but does not disentangle whether the concepts themselves are semantically incomplete or simply hard for the model to integrate in purely textual reasoning. The paper would be stronger if it acknowledged this ambiguity more centrally and framed its contribution as measuring *operational sufficiency* (concepts + reasoning pipeline) rather than asserting a clean diagnosis about annotation quality alone.

### Minor

2. **The five-stage concept-gathering hierarchy is not validated against alternatives.** The paper extends prior hierarchical extraction practices (Oikarinen et al., 2023's three-tier; Sun et al., 2024's two-level) into a five-stage design (Background → Superclass → Salient Features → Detailed Features → Auxiliary Features). While this is grounded in prior work, the paper never ablates whether the five-stage structure itself drives the negative CRI gap. A simpler or differently-ordered prompt could yield different results. Since the FSE framework generates concepts using this specific hierarchy, the generality of the finding that "current annotation methods" produce insufficient annotations is partially contingent on this unvalidated design choice.

3. **No formal statistical significance testing.** The paper reports negligible standard deviations across three runs, which is good, but does not report confidence intervals, paired tests, or effect sizes for the CRI gaps. Formal significance testing would strengthen confidence in the observed trends, especially for cases where the gap is small (e.g., Llama-3.2-vision-90b on Flowers in Table 2: −1.66%).

4. **Equation (2) contains a notation error.** The CRI formula uses `t` as both the annotation step parameter and the upper bound of the summation over instances, where it should use `l` (the number of test instances). This is likely a parsing/formatting artifact but should be corrected.

### Trivial
None.

## Nice-to-Haves

- **Small human evaluation:** Even 50–100 samples where humans classify from the generated concepts would directly validate whether the concepts themselves are insufficient or just hard for LLMs to reason from.
- **Ablation of the prompting strategy:** Testing a simpler (e.g., single-stage or two-stage) prompt structure would clarify whether the findings are robust to prompt design.
- **Analysis of why recovery happens on general datasets:** The CIFAR-100/Caltech-101 reversal (Table 3) is interesting but underexplored. A systematic analysis (e.g., class granularity vs. CRI gap correlation) would deepen the contribution.
- **Verification of concept usage in fused mode:** Testing whether corrupting or removing textual concepts changes fused-mode performance would confirm that models actually use (or ignore) the concepts in that setting.

## Removed Points

- The harsh critic's claim about "distractor selection validation being circular relative to the main CRI evaluation" is removed. The SSD is built from ResNet-18 predictions identifying visually similar classes to each *ground truth* class. The preliminary experiment validates that such distractors raise contradiction rates (34–45% vs. 14–20% for random). In the main CRI evaluation, the same distractors are used to challenge the model to pick the ground truth. The validation task (predicting y\_init vs. y\_con) and the main task (predicting y\_i from concepts) differ in target but both test whether distractors are effective — the finding that semantically similar distractors are harder is directly transferable.
- The strength finder's generic strengths (e.g., "the paper addressed an important problem") are removed as they lack concrete anchors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Reframe the headline claim slightly.** Replace "annotation methods fail to provide sufficient semantic coverage" with a more precise formulation such as "the combination of current annotation methods and LLMs' textual reasoning produces annotations that are operationally insufficient for concept-only inference." This accurately reflects what CRI measures and avoids over-attributing the failure to annotation quality alone.
- **Add formal significance tests** (confidence intervals or paired comparisons) for the CRI gaps in Table 2.
- **Add a brief ablation** comparing the five-stage prompt against a simpler two-stage variant on one dataset to probe prompt sensitivity.
- **Fix the notation in Equation (2)** to use `l` instead of `t` as the summation bound.

## Score and Decision

**Score:** 5.5  
**Decision:** Accept

The paper makes a genuine contribution: it challenges a widely-used evaluation assumption (utility-as-proxy) with clean empirical evidence, introduces a novel automated metric (CRI), and documents a systematic limitation of LLMs as XAI annotators across diverse models and datasets. The main weakness — imprecise framing that conflates annotation quality with joint concept+reasoning insufficiency — is real but not fatal, as it reflects a nuance in presentation rather than a flaw in the metric or experiments. The paper should be accepted conditional on the authors clarifying the interpretive scope of their claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>