Now let me write the final consolidated review.

## Summary

The paper proposes the Fast and Slow Effect (FSE) framework, an automated approach to evaluate whether LLM/VLM-generated concept annotations are "sufficient" (self-contained enough to support classification from text alone). FSE collects concepts through a five-stage hierarchical process and measures the Class Representation Index (CRI) — the fraction of correct class predictions using only accumulated concepts. The key finding is that on fine-grained datasets (CUB-200, Cars-196, Flowers-102), slow-mode (concept-based) CRI is substantially lower than fast-mode (visual) CRI, with a negative CRI-Gap of −25% to −27% on average. On coarse datasets (CIFAR-100, Caltech-101), the opposite holds. The paper also shows that fused (multi-modal) prediction achieves ~90% CRI while slow mode alone scores ~50%, challenging the utility-as-proxy assumption.

## Strengths

1. **Fully automated evaluation framework for annotation quality**: FSE requires no human supervision, whereas prior work relied on expensive human evaluation or downstream accuracy as a proxy. The framework is fully specified with a five-stage concept collection process (Section 4) and operationalizes a clear definition of sufficiency.

2. **Striking and robust empirical finding**: Across 6 models from 3 families and 3 fine-grained datasets, the CRI-Gap is uniformly negative, averaging −25% to −27% (Table 2). This is a genuine observation about LLM behavior — they can classify visually but struggle to convert that knowledge into text that supports the same classification. Error bars are negligible, so the pattern is reliable.

3. **Utility-as-proxy analysis (Table 4) is informative**: The finding that fused mode achieves ~90% CRI while slow mode alone scores ~50% provides concrete evidence that strong downstream task performance does not guarantee that the underlying concept annotations are sufficient on their own. This is a useful cautionary result for the field.

4. **Broad evaluation scope**: 6 models from 3 families, 5 datasets (3 fine-grained, 2 general), two annotation scenarios (post-hoc, visual-grounded), with consistent results. This breadth supports the generalizability of the findings (Section 5, Figure 3, Table 3).

5. **Fine-grained vs. coarse contrast is revealing**: The finding that slow mode underperforms fast mode on fine-grained but *outperforms* on coarse datasets (Table 3) adds precision to the paper's conclusions — the limitation is specific to fine-grained discrimination, not a universal phenomenon.

## Weaknesses

### Major

1. **CRI measures self-consistency, not annotation quality per se**: The CRI uses the same model to both generate and evaluate annotations (Equation 2). A low CRI could mean (a) the annotations are genuinely poor, (b) the model's text-to-class mapping ability is brittle, or (c) the prompting strategy forces the model to surface non-discriminative features. The paper does not disentangle these. This is not a fatal flaw — the paper defines sufficiency as self-consistency (Definition 3.1) — but it means the central claim ("annotations are insufficient") conflates annotation quality with the model's ability to reason from text. A control condition with human-written gold-standard concepts would clarify whether low CRI reflects poor annotation quality or inherent difficulty of text-only fine-grained classification. (Section 4.2, lines 155-161)

2. **The five-stage prompt structure is not validated or ablated**: The paper presents the five-stage process (Background, Superclass, Salient, Detailed, Auxiliary) as an extension of prior work (lines 117-131), but there is no ablation showing that this specific ordering, number of stages, or category definitions matter. The "slow mode" finding could partially reflect properties of this particular prompting design rather than something fundamental about LLM annotation quality. For instance, forcing the model to produce "Background" and "Superclass" information before "Salient" features may surface generic information that is not helpful for fine-grained discrimination.

### Minor

3. **No human baseline**: The paper claims its framework is fully automated (a strength), but for evaluating whether annotations are "insufficient," a human baseline would help interpret the CRI scores. If humans also fail to classify from the same LLM-generated concepts on fine-grained datasets, this would validate the CRI metric. If humans succeed, it would reveal that the metric is capturing a model-specific reasoning limitation rather than annotation quality. Without this, the paper cannot fully distinguish between "annotations are insufficient" and "the model cannot effectively reason from its own text."

4. **No analysis of annotation content**: The paper treats annotations as a black box and relies entirely on CRI scores. A qualitative analysis showing whether generated concepts are accurate, discriminative, or contain errors would strengthen the claims. Without this, the paper cannot distinguish between "annotations are wrong" and "annotations are correct but the model cannot use them in text-only mode." (The Appendix is cited for visual examples, but these are not accessible.)

5. **No statistical significance testing**: The paper reports CRI-Gaps (Table 2) and standard deviations (negligible, which is good) but does not test whether observed differences are statistically significant. Given the modest number of datasets (3-5) and the high per-dataset variance in CRI-Gap (e.g., ranging from -57.44% to +7.50% across models on CUB-Bird), some of the trends may be driven by specific dataset-model combinations.

### Trivial

6. **Equation (2) indexing issue**: The CRI formula sums over *i=1 to t* where *t* is the annotation step, but the notation appears to intend averaging over the number of test cases *l*, not the step number. This is a minor presentation error that does not affect the experimental results (which clearly use the intended computation).

## Nice-to-Haves

- A control experiment where human-written gold-standard concepts replace LLM-generated ones in the CRI evaluation, to isolate whether low CRI reflects annotation quality or inherent text-only classification difficulty.
- An ablation of the five-stage prompt structure (vary number of stages, reorder stages) to verify the finding is robust to prompting design choices.
- A qualitative error analysis showing examples of what kinds of annotation failures drive the CRI-Gap.

## Removed Points

- **"Straw man evaluation"** (Harsh Critic #1): Removed. The paper's definition of sufficiency (text-only inference) is a deliberate, well-justified operational choice. The paper explicitly examines the multi-modal case in the fuse experiment (Table 4) and does not claim annotations are useless in practice. The critic's framing ignores the paper's self-consistent definition and the fuse experiment.

- **"Contradiction experiment invalidates CRI assumption"** (Harsh Critic #3): Removed. The contradiction experiment (Section 5.3) serves only to validate distractor selection strategy. The paper does not use it to make claims about annotation quality. This reflects a misunderstanding of the experimental design.

- **"Definition 3.1 is question-begging"**: Removed. The definition is a deliberate operational choice that the paper explicitly motivates (Section 3, "Towards Rigorous Criteria for Annotation Sufficiency"). A definition cannot "beg the question" — it defines terms for the purpose of analysis.

- **"Coarse results undermine central claim"**: Removed. The paper treats the coarse vs. fine-grained contrast as a *finding* (lines 223-227, Table 3), not a contradiction. The claim is specifically about fine-grained datasets, and the coarse results provide an informative boundary condition.

- **"Cherry-picked motivating example"**: Removed. Motivating examples are by nature illustrative; the paper provides aggregate quantitative results (Table 2, Figure 3) as the actual evidence.

- **"Missing appendix/implementation details"**: Removed per guidelines — the parser strips these sections; they exist in the original submission.

- **Various formatting and presentation nitpicks**: Removed per guidelines.

- **Several generic strength-finder "strengths"** (e.g., "addressing important problem"): Removed as they are superficial or not sufficiently specific to the paper's actual contributions.

## Novel Insights

The most interesting pattern emerging from the paper, though not fully articulated as such, is the "verbalization gap": models possess discriminative visual knowledge (evidenced by high fast-mode CRI) yet the same concepts they generate do not support text-only re-classification. The fuse experiment (Table 4) shows this is not because the concepts lack useful information — since fused multi-modal prediction works well — but because the model cannot effectively reason from its own text in isolation. This suggests a fundamental asymmetry between visual recognition and verbal explanation in current LLMs/VLMs, reminiscent of the intuition/knowledge gap in cognitive science. The finding has implications for concept-based XAI: explanations that appear plausible and even carry useful information may not be usable for class-level reasoning in the same way the model's internal representations are.

## Suggestions

1. Add a control condition where human-written gold-standard concepts replace LLM-generated concepts in the CRI evaluation, to isolate whether low CRI reflects poor annotation quality or inherent difficulty of text-only fine-grained classification.
2. Ablate the five-stage prompt structure (vary number of stages, reorder them) to verify the finding is robust to prompting design choices rather than an artifact of the specific hierarchy.
3. Include a qualitative content analysis showing specific examples of annotation failures — e.g., what kinds of errors (overly generic, factually wrong, hallucinated) drive the CRI-Gap.
4. Report confidence intervals or statistical tests (e.g., paired bootstrap) for the main CRI-Gap results.
5. Consider reframing the paper's contribution more precisely around the "verbalization gap" finding (models cannot externalize their visual knowledge into text that supports re-classification), which is well-supported, rather than the broader "annotation insufficiency" framing, which conflates multiple interpretations.

## Score and Decision

**Calibration Summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| KLUDshUx2V | LLM concept banks paper | 3.40 | R1 (low) | Significantly weaker — limited novelty, insufficient experiments. Our paper is clearly better. |
| kTjEPEy96Q | Unsupervised CBM evaluation | 3.00 | R1 (low) | Significant conceptual fallacy (evaluator does not match task). Our paper avoids this. |
| J0qgRZQJYX | Axiomatic concept explanations | 3.00 | R1 (low) | Narrow contribution, limited experiments. Our paper is stronger. |
| wZiH43e5Ah | Concept extraction framework | 3.00 | R1 (low) | Limited scope. Our paper offers broader evaluation. |
| tZk3LnvVtK | LLM uncertainty with concepts | 5.60 | R1 (mid) | Well-received but had clarity issues. Our paper has clearer contribution. |
| wk77w7DG1N | LLM consistency evaluation | 4.67 | R1 (mid) | Framework-type paper. Our paper has a more novel finding. |
| kJgi5ykK3t | LLM logical consistency | 5.60 | R1 (mid) | Strong framework paper. Comparable in quality. |
| M4fhjfGAsZ | Automated KC annotation | 5.33 | R1 (mid) | This paper has weaker experimental breadth. Ours is stronger. |
| UnstiBOfnv | Evaluation biases for LLMs | 3.67 | R2 | Limited novelty. Our paper is stronger. |
| dZsjj4vQjl | Multi-grained concept annotations | 4.50 | R2 | Dataset paper with mixed reviews. Our paper has more novel methodology. |
| w49jlMWDSA | GIST: image-specific text | 5.33 | R2 | Similar quality. Our paper has a more novel finding but similar methodological concerns. |
| RC5FPYVQaH | CB-LLM | 5.75 | R2 | This accepted paper has comparable rigor. Our paper has broader evaluation but similar-level methodological concerns. |
| kFALGqLp46 | LLM self-correction | 5.33 | R2 | Similar quality tier. |
| todLTYB1I7 | Principled evaluation framework | 5.00 | R2 | Directly comparable as an evaluation framework paper. Similar strengths and weaknesses. |

**Round 1 Bracket:** The paper clearly falls in the middle band (3.5–7.5). It is substantially better than the 3.0–3.4 anchors (which had limited novelty or fundamental flaws) and substantially below the 8.0 anchors (which are strong accept papers with rigorous validation).

**Round 2 Narrowing:** The closest comparisons are the 5.0–5.75 range papers. Compared to GIST (5.33) and CB-LLM (5.75), our paper has a more novel framework and a striking empirical finding, but also has notable interpretability concerns (what CRI actually measures, unablated prompt design). It is comparable in quality to CB-LLM and slightly better than GIST. The "Principled Evaluation Framework for Neuron Explanations" (5.00) is the closest conceptual match — both propose evaluation frameworks with clear limitations in what they can claim.

**Final Score: 5.0.** This is a solid paper with genuine contributions — an automated evaluation framework and a striking, well-documented empirical finding — but the interpretability limitations of the CRI metric and the unablated prompting design keep it from being a clear accept. The paper would benefit from tighter framing around the "verbalization gap" finding and additional validation experiments.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>