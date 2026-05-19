- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 1, 3, 3
Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final review.

## Summary

This paper proposes a framework for evaluating unsupervised concept bottleneck models (CBMs) — a genuine gap since unsupervised CBMs lack ground-truth concept labels. The framework introduces ConceptScore (cosine similarity between image and predicted concept embeddings using Long-CLIP), Ref-ConceptScore (harmonic mean of ConceptScore and concept-concept similarity with ground-truth), adapts NLP metrics (BLEU, METEOR, ROUGE) for concept evaluation, and validates against human and GPT-4v judgments. Experiments on CIFAR-10/100 and CUB-200 with supervised and unsupervised CBM variants show moderate correlations between automatic metrics and human/GPT evaluations.

## Strengths

1. **Novel use of Long-CLIP for multi-concept evaluation (Section 3.2)**: The paper identifies that standard CLIP's 77-token limit is insufficient for multi-concept descriptions and employs Long-CLIP to support longer context and finer-grained feature alignment. This is a concrete, justified technical choice that directly addresses a limitation of prior CLIP-based evaluation approaches.

2. **Sensitivity analysis demonstrates metric discriminability (Section 4.6, Figure 2)**: Replacing correct concepts with incorrect ones causes ConceptScore to drop from 0.5625 to 0.3811 and Ref-ConceptScore from 0.6958 to 0.5297. This controlled experiment provides direct evidence that the metrics respond meaningfully to concept quality, going beyond mere correlation reporting.

3. **Quantified inter-rater reliability (Section 4.3)**: Krippendorff's alpha of 0.7405 for five human raters is reported, establishing a measurable level of agreement that strengthens the credibility of the human judgment reference. This level of rigor is often absent in interpretability evaluation work.

4. **Multi-dimensional evaluation design**: The framework cross-validates automatic metrics (ConceptScore, Ref-ConceptScore, and NLP-based metrics) with both human and GPT-4v scores, and reports a correlation matrix covering all dimensions (Section 4.3.1). This provides a richer picture of concept quality than metrics like concept accuracy alone.

## Weaknesses

### Fatal
None. The core contribution — proposing evaluation metrics for unsupervised CBMs — addresses a genuine gap, and the proposed metrics are mathematically well-defined. The issues below are substantive but correctable.

### Major

1. **Over-claiming correlation strength with no statistical inference (Section 4.3, 4.3.1)**: The paper claims "strong certain alignments" (Abstract) and "strong correlations with human judgments" (Conclusion), but the reported Kendall τ values are moderate: Human vs. ConceptScore = 0.42, Human vs. Ref-ConceptScore = 0.47, Human vs. GPT = 0.47. No confidence intervals, p-values, or standard errors are provided. The sample size (100 per dataset for human/GPT evaluation) amplifies uncertainty, and the paper does not acknowledge this. This is not a fatal flaw — moderate correlations are still meaningful — but the language misrepresents the evidence.

2. **Undefined and unablated weight parameter ω (Section 3.2, Eq. 1)**: The ConceptScore formula introduces ω as "a weight factor... to adjust the significance of the similarity score," but its value is never specified, ablated, or justified anywhere in the paper. If ω=1 (implicit default), it is vacuous; if ω≠1, its setting is critical and should be explained. As written, the reader cannot determine whether ω is a free hyperparameter or a trivial constant.

3. **Sensitivity experiment disconnected from the defined metrics (Section 4.6)**: The sensitivity analysis modifies concept weights and reorders the top-k concepts, then reports changes in ConceptScore and Ref-ConceptScore. However, ConceptScore as defined in Eq. 1 is a per-concept cosine similarity with no aggregation mechanism that would incorporate model-assigned concept importance weights or ordering. The paper does not define how multiple concepts are combined into a single score, so it is unclear how reordering or weight changes affect the reported numbers. This makes the second part of the sensitivity analysis (reordering and weight modification) difficult to interpret.

4. **No ablation of Long-CLIP vs. vanilla CLIP (Section 3.2)**: The paper motivates the use of Long-CLIP by arguing that standard CLIP's 77-token limit and coarse feature discrimination are insufficient. However, no experiment compares the two — e.g., does Long-CLIP produce meaningfully different ConceptScores than vanilla CLIP? Without this ablation, the choice remains unvalidated.

### Minor

1. **Incorrect description of harmonic mean behavior (Section 3.3)**: The paper states the harmonic mean "gives more weight to lower values, ensuring that a single low ConceptScore does not dominate the overall evaluation." This is backwards — the harmonic mean is **more** sensitive to low values, so a single low score **does** dominate. The formula is correct, but the textual justification contradicts the mathematical property actually exploited. Additionally, the double `max(max(cos(...),0),0)` in Eq. 2 is redundant (the outer max is vacuous). No justification is given for choosing the harmonic mean over arithmetic or geometric alternatives.

2. **Ambiguity in correlation analysis scope (Section 4.3 vs. 4.4/4.5)**: The correlation analysis reports correlations for BLEU, METEOR, and ROUGE alongside ConceptScore and Ref-ConceptScore. However, it is not stated which dataset(s) these correlations are computed on. NLP metrics require ground-truth concept references (only available for CUB-200), so the reader must infer the scope. This ambiguity should be resolved explicitly.

3. **No limitations section**: The paper does not discuss that the metrics inherit biases from CLIP/Long-CLIP, that the human evaluation is small (5 raters, 100 samples per dataset), or that the moderate correlations may not generalize to other domains or model types.

4. **GPT-4 scoring prompt conflates features and weights (Section 3.5)**: The GPT-4 prompt asks raters to evaluate "the combination of features and weights as a unit," combining two attributes (which concept is present vs. how important it is) into a single score. This makes the score ambiguous and harder to interpret as a validation target.

### Trivial
- The double `max(max(cos(...),0),0)` in Eq. 2 is mathematically redundant.
- The NLP metrics applied to short concept phrases (often single words or two-word phrases) may have degenerate behavior for n-gram overlap, and this is not discussed.

## Nice-to-Haves
- Comparison with existing evaluation approaches (e.g., concept accuracy or intervention accuracy on supervised baselines) would help contextualize whether ConceptScore offers advantages beyond conventional metrics.
- Ablation of the prompt design *P(ĉ)* — how were concepts turned into sentences, and how sensitive are results to prompt phrasing?
- Reporting confidence intervals or bootstrapped error bars for the reported Kendall τ values would strengthen the correlation analysis.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"Invalid application of NLP metrics on unsupervised data (Table 1)"**: The reviewer claimed BLEU/METEOR/ROUGE are applied to CIFAR without reference. **Removed.** The paper's Section 4.4 ("Without Reference" evaluations for CIFAR) only discusses ConceptScore, human, and GPT-4v scores — no NLP metrics are mentioned for CIFAR. NLP metrics are explicitly described in Section 4.5 for CUB-200 where ground-truth concept annotations exist. The correlation section (4.3) is ambiguous about scope but does not claim NLP metrics were applied to CIFAR. The criticism reflects a misreading of the paper.

2. **"No comparison with existing evaluation metrics"** (from "Missing Parts"): The paper proposes new metrics for unsupervised CBMs where conventional metrics (concept accuracy) are inapplicable by design. While a comparison on supervised data would be informative, the absence is not a weakness — the contribution is a new evaluation framework, not a claim that it outperforms existing metrics on their own terms.

3. **"Missing related works"** about CLIP-Score in image generation: Removed per policy — I cannot confirm the existence or absence of specific related works without external sources.

4. Various formatting/style nitpicks and reproducibility criticisms about large-scale artifacts are removed per policy.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Correct the harmonic mean description**: Replace the wrong explanation with an accurate one (the harmonic mean penalizes imbalance between the two terms, ensuring both image-concept alignment and concept-concept consistency are simultaneously high). Also simplify the redundant `max(max(...))` and justify why harmonic mean is preferred over arithmetic/geometric.
2. **Either fix ω or remove it**: If ω=1 is the default, simplify the formula; if ω is a tunable parameter, ablate it across a range of values and report sensitivity.
3. **Clarify the sensitivity experiment**: Define how multiple concept scores are aggregated so that reordering or weight changes can affect the output. Alternatively, redesign the experiment to test what the metrics actually measure (e.g., replacing correct concepts with incorrect ones — which the first part already does well).
4. **Add a Long-CLIP vs. vanilla CLIP ablation** to validate the design choice.
5. **Tone down the correlation claims**: Replace "strong certain alignments" with "moderate correlations" and report confidence intervals or p-values. The contribution is in proposing a usable evaluation system, not in achieving human-level agreement.
6. **Explicitly state which dataset(s) the correlation analysis uses** and how NLP metrics (which require ground-truth concepts) are handled for samples without concept annotations.
7. **Add a limitations section** acknowledging CLIP/Long-CLIP biases, the small human evaluation scale, and the moderate correlation values.
