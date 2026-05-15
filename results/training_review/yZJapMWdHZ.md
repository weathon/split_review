Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper identifies "generative inequalities" in LLM uncertainty estimation—where semantically unimportant tokens and sentences receive equal weighting to critical ones in entropy-based UQ—and proposes Shifting Attention to Relevance (SAR), a method that re-weights token-level and sentence-level entropy contributions using semantic relevance scores. The token-level relevance is measured by the semantic change when a token is removed; sentence-level relevance is measured by semantic consistency with other generations. Experiments across 5 model families (up to 33B), 5 datasets, and 48 evaluation settings consistently show AUROC improvements over existing methods including Semantic Entropy.

## Strengths

- **Well-motivated observation of generative inequalities**: The paper provides systematic evidence (Section 3.4, Figures 2–3) that most tokens have low relevance scores and that irrelevant tokens dominate the total uncertainty volume. This directly challenges the uniform-weighting assumption underlying existing entropy-based methods like Predictive Entropy and Length-Normalized PE. The analysis is clear, quantitative, and replicable.

- **Consistent empirical gains across broad scope**: SAR outperforms baselines (PE, LN-PE, Semantic Entropy, Lexical Similarity) on nearly all of 48 model-dataset combinations (Tables 1–3). On instruction-tuned LLMs (Table 2), SAR beats SE by an average of 7.1% AUROC. The breadth—5 model families up to 33B, 5 datasets spanning general QA, science, and medicine—provides reasonable evidence of generalizability.

- **Demonstrated synergy of token- and sentence-level shifting**: The modular design (TOKENSAR, SENTSAR, SAR) allows clean ablation. On OPT-30b + CoQA (Table 1), TOKENSAR and SENTSAR each achieve 0.723 AUROC but their combination (SAR) reaches 0.748, indicating the two components capture complementary sources of information.

- **Generation efficiency analysis**: Figure 4 shows SAR achieves strong AUROC (0.750) with only 5 generations and continues improving with more, while some baselines plateau or degrade—a practical advantage for resource-constrained deployment.

## Weaknesses

### Fatal

None.

### Major

- **The token-level relevance metric (Eq. 2) lacks direct validation.** The metric computes the semantic similarity between the original sentence and the sentence with a single token removed, using a Cross-Encoder trained on full, well-formed sentences. Removing a single token often produces grammatically incomplete fragments (e.g., "density of" instead of "density of an object"), and the paper provides no evidence that the similarity model produces meaningful scores on such corrupted inputs. While the downstream empirical success of SAR provides indirect validation—if the metric were random noise, SAR would not consistently outperform baselines—the paper would be strengthened considerably by a direct validation against human judgments of token importance or an alternative functional importance measure (e.g., leave-one-out on meaning preservation). This is the most significant methodological gap.

- **The differentiation from Semantic Entropy at the sentence level is supported by weak evidence.** The paper claims SE's entailment-based approach is "undesirable" for long generations, citing a manual examination where 36.7% of entailment predictions were undesirable (on 120 questions with >20 tokens). No details are provided on sampling strategy, annotation criteria, annotation instructions, or inter-annotator agreement. Since the sentence-level component (SENTSAR) is functionally similar to SE (using soft similarity instead of entailment), this evidence is insufficient to establish that SAR's variant is meaningfully superior. A systematic head-to-head comparison of failure cases would substantially strengthen this claim.

### Minor

- **No variance or significance information on main results.** Tables 1–3 report single AUROC values per setting without error bars, confidence intervals, or statistical significance tests. The improvements over the best baseline are often 1–4 percentage points, which could theoretically fall within random seed variation. While single-run evaluation is the norm in LLM UQ papers (e.g., the Semantic Entropy paper itself), and the consistency of gains across 48 settings mitigates this concern, adding error bars over multiple seeds (or bootstrapped intervals) for a representative subset of settings would substantially increase confidence.

- **Temperature hyperparameter (t=0.001) is unsupported.** The temperature in Eq. 9 controls the strength of sentence-level relevance shifting, but no sensitivity analysis or tuning rationale is provided. Given that the paper includes sensitivity analyses for other design choices (sentence similarity models in Table 4, correctness thresholds in Figure 5), the omission of temperature sensitivity is noticeable.

- **The generative inequality analysis (Section 3) is conducted on a single dataset (CoQA) and model (OPT-13b).** While the main experiments broaden the scope, the core analytical motivation—which frames the relevance-uncertainty disconnect as a general phenomenon—is only validated on one configuration. The conclusions about "considerable irrelevant tokens" and "irrelevant tokens dominate total volume" would be stronger if replicated across at least one additional model and dataset.

- **Limitations section is sparse.** The paper briefly mentions latency and logit-access requirements but does not discuss the computational cost of token-level relevance (requiring N similarity evaluations per sentence, each running a RoBERTa-large model), the risk of domain mismatch for the similarity model, or the assumption that semantic similarity models are reliable on LLM-generated text.

### Trivial

- None.

## Nice-to-Have Suggestions

- Adding a comparison with a weaker similarity model (e.g., BERTScore) to test the sensitivity of SAR's gains to similarity quality, complementing the existing comparison with SimCSE and LLM-as-judge.
- Including concrete examples of (question, generation) pairs with token-level relevance scores and uncertainty proportions visualized side by side, to help readers assess whether the relevance judgments are semantically sensible.
- Analyzing cases where TOKENSAR underperforms PE to understand failure modes of the relevance metric.

## Removed Points

- **Criticism about "unfair comparison" / omission of other UQ methods** (degree-based consistency, alternative entropy decompositions): Removed per instruction not to mention missing related works. The paper cites Manakul et al. (2023b) in related work, and the four baselines used (Lexical Similarity, SE, PE, LN-PE) are the standard and most directly relevant comparisons.
- **Criticism that normalization in Eq. 6 "destroys any absolute scale of relevance"**: The paper explicitly states the normalization is intended to "mitigate the bias posed by sentence length" and make tokens comparable across sentences. This is a deliberate design choice analogous to length normalization in LN-PE, not an oversight.
- **Criticism that the temperature t=0.001 "essentially makes the relevance term dominate"**: This is by design—the sentence-level component is meant to shift attention toward relevant sentences. The concern is better framed as a missing sensitivity analysis (already captured in Minor weaknesses).
- **Criticism about the 0.5 Rouge-L threshold being "somewhat arbitrary"**: The paper provides sensitivity analysis for this threshold (Figure 5), showing consistent gains across different thresholds. This directly addresses the concern.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a recurring theme: **the paper's core methodological contribution (token-level relevance weighting) and its strongest empirical finding (~7.1% average improvement on instruction-tuned LLMs) are asymmetrically validated.** The token-level metric is intuitive but unvalidated against ground truth, while the sentence-level component improves on SE with only anecdotal evidence of SE's failures. This creates an epistemic mismatch—the most novel part of the method has the weakest direct evidence, while the better-supported part (sentence-level shifting) is closer to existing work. Future work extending this line would benefit from validating the relevance metric independently of the downstream UQ task, and from a more rigorous characterization of when and why SE's entailment predictions fail.

## Suggestions

1. **Validate the token-level relevance metric** by (a) comparing against human-annotated token importance on a sample of generations, or (b) comparing against an alternative functional importance measure (e.g., leave-one-out on meaning preservation as judged by humans). This would address the most substantive concern about the paper's foundation.

2. **Add error bars or confidence intervals** for a representative subset of the main experimental settings (e.g., 3 random seeds). This is particularly important for the settings where improvements over the best baseline are in the 1–2% range.

3. **Provide a more rigorous comparison with Semantic Entropy's entailment approach** by systematically sampling failure cases and evaluating both methods on them, rather than relying on a 120-question manual examination with undocumented methodology.

4. **Include a sensitivity analysis for the temperature parameter t** in Eq. 9, which controls the strength of sentence-level relevance shifting, consistent with the sensitivity analyses already provided for other design choices.

The paper identifies a genuine problem, proposes a straightforward and well-motivated solution, and supports it with an extensive experimental evaluation. The weaknesses are substantive but fixable, and they do not invalidate the core contribution.

## Score and Decision

**Originality**: The token-level relevance weighting for UQ is novel; the sentence-level component builds on SE but with a different mechanism.

**Quality of research question**: Important—trustworthy LLM behavior is a central concern in the field.

**Claims support**: Claims are largely supported by consistent empirical evidence across many settings, though the token-level metric itself lacks direct validation and no variance estimates are provided.

**Soundness of experiments**: Broad scope is a strength; the main gap is the lack of statistical rigor (error bars, significance tests) and the under-validated relevance metric.

**Clarity of writing**: Clear motivation and method description. The limitations section is minimal.

**Value to community**: Moderate—the generative inequality observation is practically useful, and the method is simple enough to adopt. The lack of validation on the core metric tempers the contribution somewhat.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>