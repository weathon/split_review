## Summary
This paper proposes the Fast and Slow Effect (FSE) framework for evaluating whether LLM-generated concept annotations are sufficient for XAI. It introduces a 5-stage coarse-to-fine concept gathering process and a Class Representation Index (CRI) metric, comparing "fast mode" (direct visual inference) with "slow mode" (prediction from accumulated textual concepts). Key finding: on fine-grained datasets (CUB-200, Cars-196, Flowers-102), slow mode CRI is ~25% lower than fast mode across six LLMs, while on general datasets (CIFAR-100, Caltech-101), slow mode recovers to >90%.

## Strengths
- **Well-quantified empirical finding**: Table 2 shows that slow mode consistently underperforms fast mode by 25–27% average CRI-Gap across all six LLMs and all three fine-grained datasets. Every cell in the table is negative, providing strong and uniform evidence for the central finding.
- **Compelling critique of utility-as-proxy assumption**: Table 4 shows fused mode (image + text) achieves ~90% CRI while slow mode alone scores ~50–60%, demonstrating that downstream task performance can mask insufficient conceptual annotations — a meaningful contribution to XAI evaluation methodology.
- **Calibrated preliminary experiment**: Table 1 demonstrates that semantically related distractors (from ResNet-18 confusion patterns) produce contradiction rates 2–2.5× higher than random distractors (34–45% vs. 14–20%), validating that the evaluation framework meaningfully challenges annotators.
- **Revealing fine-grained vs. general dataset contrast**: Table 3 shows slow mode does outperform fast mode on CIFAR-100 and Caltech-101 (CRI >90% at t=5), appropriately scoping the finding and demonstrating nuance — LLMs can generate sufficient concepts for coarse-grained tasks but not fine-grained ones.
- **Broad multi-model evaluation**: Experiments span six models from three families (GPT, Qwen, Llama) with both large and small variants, showing the limitations are systematic rather than model-specific.

## Weaknesses

### Fatal
None

### Major
- **Self-referential evaluation without external validation**: The CRI metric uses the same LLM (same model F with parameters Θ) to both generate concepts (Eq. 1: $c_i^t = \bigcup_{j=1}^{t-1} \mathcal{F}(c_i^j, X_i; \Theta)$) and evaluate them (Eq. 2: $y_i^t = \mathcal{F}(c_i^t; \Theta)$). This conflates two failure modes: (a) the concepts genuinely lack sufficient information, and (b) the LLM cannot effectively integrate its own textually expressed knowledge for classification. The paper's headline claims ("current annotation methods fail to provide sufficient semantic coverage") are stated as facts about the annotations, but they may partly reflect the annotating LLM's inability to reverse-engineer class labels from its own concept summaries. An independent classifier on the same concepts could reach different conclusions. The paper never validates CRI against any external measure — not human judgment, not an independent classifier, not a downstream CBM's performance.

- **No connection to actual XAI pipelines**: The paper frames itself squarely in XAI (title: "Are LLMs Good XAI Annotators?"), and the background Section 2 formally defines concept-based models with visual encoders $f_v$, concept mappings $f_c$, and prediction heads $f_p$. However, no actual concept-based model is ever trained or evaluated — no CBM, no interpretability metric, no downstream XAI task. A concept annotation could be perfectly sufficient for training a CBM even if the generating LLM cannot perform zero-shot classification from those concepts alone (concepts may be more useful as training signal than as standalone discriminators). This disconnect limits the paper's relevance to the XAI community despite its framing.

### Minor
- **CRI formula notation error**: Equation (2) defines $CRI(\mathcal{F}, t) := 100\% \times \frac{1}{t} \sum_{i=1}^{t} \mathbb{1}[y_i^t = y_i]$, where the sum runs from $i=1$ to $t$ (the step number, 0–5) with normalization $1/t$. Since the test set has $l$ total instances, this is clearly a notation error — the formula should sum over all $l$ instances with $1/l$ normalization. The actual computation must use the correct formula given the reported dataset-level percentages, but the notation as written is incorrect.

- **Weak analogy to dual-process theory**: The Slow Mode Superiority hypothesis borrows from Kahneman's System 1/System 2 theory, but System 1 and 2 describe distinct human cognitive processes, whereas the LLM is the same model receiving different inputs (image vs. text). The hypothesis itself is reasonable (concepts should help classification), but the cognitive-science theoretical grounding adds little.

- **Missing sample sizes for main experiments**: The preliminary contradiction test uses 100 images per dataset (Section 5.3), but the main CRI experiments' sample sizes are not clearly stated in the paper.

### Trivial
None

## Nice-to-Haves
- Adding an external validity check (e.g., training a simple text classifier or CBM on the generated concepts and checking whether CRI correlates with that model's performance) would substantially strengthen the sufficiency claims.
- Error analysis showing which concept stages help most, which classes are hardest, and systematic patterns in failures.
- Comparison with human-generated concept annotations (CUB-200 has extensive part annotations that could serve as a reference point).

## Removed Points
These points are flagged to be removed, treat them with caution:
- None — all major points from both reviewers were verified against the paper and retained or removed with justification during filtering.

## Novel Insights
The paper's most novel contribution is demonstrating a systematic "fast vs. slow" gap: LLMs that correctly classify images visually cannot reliably classify from their own textual concept descriptions of those same images. This gap holds uniformly across six LLMs and three fine-grained datasets (Table 2), but reverses on coarse-grained datasets (Table 3). The insight that fused-mode performance (image + text) masks concept insufficiency (Table 4) is a genuinely useful warning for the XAI community about the limits of utility-as-proxy evaluation.

## Calibration Anchors Retrieved

**Round 1 (bracketing):**
- KLUDshUx2V (avg 3.40, reject): LLM concept banks for CBMs. Similar topic but more limited execution. Paper under review is clearly stronger.
- kTjEPEy96Q (avg 3.00, reject): Evaluating unsupervised CBMs. Similar methodological flaw (evaluation doesn't measure what it claims). Paper under review is more thorough.
- RC5FPYVQaH (avg 5.75, accept): CB-LLM for text. More concrete contribution with actual model training. Paper under review is more diagnostic.
- ARFRZh6pzI (avg 6.00, reject): CLEAR metacognitive LLM. Similar cognitive analogy, more technical depth. Paper under review has broader evaluation.
- z8sxoCYgmd (avg 8.00, accept): LOKI benchmark. Clearly stronger — large-scale, well-validated benchmark.
- HnhNRrLPwm (avg 8.00, accept): MMIE benchmark. Clearly stronger.

**Round 2 (narrowing):**
- Q9Z0c1Rb5i (avg 5.00, reject): SupCBM with hierarchical concepts. Comparable quality — both have interesting contributions but significant methodological limitations.
- gYcft1HIaU (avg 4.33, reject): Clinical LLM knowledge evaluation. Similar self-evaluation pattern. Paper under review has stronger empirical evidence.
- 3UB4NaEb1g (avg 4.50, reject): Certifying LLM knowledge comprehension. Less empirical evidence. Paper under review is stronger.
- 9bmTbVaA2A (avg 5.75, accept): Concept-QA+V-IP. Accepted. Has actual model training and concrete contributions. Paper under review is less concrete.
- rp0EdI8X4e (avg 6.25, accept): FVLC faithful CBMs. Clearly stronger — formal definitions, actual training, stability guarantees.
- tZk3LnvVtK (avg 5.60, reject): Internal concepts for LLM uncertainty. Different focus but comparable quality.

**Bracketing**: Round 1 placed the paper between 3.5 and 6.5. **Narrowing**: Round 2 refined to 4.5–5.5, with the paper sitting closest to the rejected SupCBM (5.00) — both have interesting contributions in the concept evaluation space but with significant methodological limitations. The paper is clearly above the weak anchors (3.0–3.4) and below the accepted papers (5.75+) which have more concrete, validated contributions (actual model training, formal guarantees).

## Suggestions
- Add at least one external validity check: train a simple text classifier or CBM on the generated concepts and check whether CRI correlates with that model's performance. This single experiment would address both major weaknesses simultaneously.
- Revise the CRI formula in Equation (2) to correctly sum over all $l$ instances with $1/l$ normalization.
- Narrow the XAI framing: either connect the evaluation to actual CBM pipelines, or reframe the contribution as a diagnostic for LLM self-consistency in concept generation rather than a general claim about XAI annotation sufficiency.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>