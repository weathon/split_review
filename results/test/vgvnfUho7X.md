## Summary

This paper applies Item Response Theory (IRT) to evaluate LLM performance on the ENEM (Brazilian college entrance exam), leveraging a 3PL IRT model pre-fitted by experts on over 5 million human test-takers. Rather than training a new IRT model on machine responses (as prior work does), the paper uses the human-calibrated model as a norm, deploying goodness-of-fit (l_z), Fisher Information, and discrimination indices to assess whether LLM response patterns are human-like and whether the exam provides reliable θ estimates for LLMs. Key findings include: (1) high accuracy can mask non-human-like response patterns (e.g., GPT-3.5 on Natural Sciences); (2) the Math exam is too difficult and provides unreliable measurement for the tested LLMs; (3) Humanities and Languages exams show better human-like fit. The core contribution is demonstrating how psychometric tools can go beyond accuracy-based evaluation of LLMs on human-designed exams.

## Strengths

- **Novel methodological approach using a human-calibrated IRT model to evaluate LLM response patterns.** Unlike prior work that trains IRT models on machine responses, this paper leverages a 3PL model pre-fitted by educational experts on 5M+ humans, enabling a direct comparison between LLM and human response patterns under the same measurement framework (Section 4.1, Section 2). This is a principled and well-motivated design choice.

- **Concretely demonstrates that accuracy can be misleading.** For the Natural Sciences exam, GPT-3.5 and Gemma-7B achieve high accuracy but exhibit l_z scores far outside the human distribution (Figure 3). This provides clear empirical evidence that accuracy alone does not capture human-like behavior and that IRT-based fit measures reveal meaningful discrepancies (Section 5.3).

- **Uses converging evidence from three distinct psychometric measures (l_z, Fisher Information, DI) to assess measurement reliability.** Rather than relying on a single metric, the paper triangulates across goodness-of-fit, Fisher Information (Section 5.3, Figure 4), and discrimination indices (Figure 5) to reach its conclusions about measurement quality for LLMs. The Fisher Information analysis quantitatively shows that the Math exam peaks around θ≈0 (human average) while all LLMs fall in the low-information tail, supporting the claim about limited utility for these models.

- **Systematic evaluation across multiple models, architectures, sizes, and languages.** The study covers 7+ LLMs (Mistral-7B, Gemma-7B, Llama2-7B/13B, Llama3-8B, GPT-3.5) with different architectures, training data, and instruction-tuning, tested on both Portuguese and English versions of the exam (Section 4.2, Section 5.1). This provides reasonable breadth for a study of this kind.

- **Reproducibility commitment.** Code and input files are included in supplementary material (Section 7).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The interpretation of l_z for LLMs could be more precisely scoped.** The paper treats low l_z under the heading "Reliability of IRT Scores for LLMs" (Section 5.3), stating that "low l_z scores suggest that the θ estimate of the model is less reliable." However, because the IRT model was fit to humans, a low l_z for an LLM could indicate either (a) the LLM truly has an unreliable θ estimate, or (b) the IRT model's assumptions (unidimensionality, local independence, logistic form) are partially violated for LLM response processes in a way that doesn't threaten θ estimation but does flag model misfit. The paper's framing slightly conflates these two interpretations. The paper's overall case is strengthened by converging evidence from Fisher Information and DI, but the l_z discussion would benefit from acknowledging this interpretive nuance more explicitly.

- **Some comparative claims lack statistical support.** The paper states that "GPT-3.5 tends to perform better in Portuguese compared to English" on certain exams (Section 5.1) without formal hypothesis tests or effect sizes. Given that 30 shuffles per model are available, standard errors or Bayesian credible intervals for these language comparisons would strengthen the claims beyond eyeballing scatter plots.

- **The Fisher Information threshold for "meaningful measurement" is not specified.** The paper concludes that the Math exam is "not appropriate to make meaningful measurements" of LLM ability because LLM θ values fall in the low-information tail (Figure 4), but does not define a quantitative threshold (e.g., SE > 0.5) for what counts as "not meaningful." Providing such thresholds would make the conclusion less vague and more actionable.

- **Training data leakage for the 2022 exam is acknowledged but not analyzed.** The paper notes that the 2023 exam (released November 2023) minimizes leakage risk, but the 2022 exam (results in appendix) and older ENEM exams are public and likely appeared in training data for models like GPT-3.5 and Llama2. A brief analysis comparing model performance on questions traceable to common web sources vs. novel questions would strengthen credibility (Section 4.1).

### Trivial
None.

## Nice-to-Haves

- A split-half or cross-validated reliability analysis for θ estimates of low-l_z LLMs would directly test whether their θ is less stable, strengthening the reliability claim beyond Fisher Information alone.
- A comparison of LLMs' l_z distributions to those of human subgroups with matched θ ranges would sharpen the "non-human-like" claim by distinguishing genuine LLM deviation from normal human variation.
- A categorical analysis (regression on item attributes like image presence, numeric content, etc.) to systematically explain which items show diverging discrimination for LLMs vs. humans, rather than the brief qualitative mention.

## Removed Points

These points were raised by reviewers but are flagged for removal with justification:

- **"The central conceptual conflation: 'human-like' is not a proxy for 'reliable IRT score'"** — The paper uses l_z as a standard psychometric person-fit index (citing De Ayala, 2013). In psychometrics, person-fit statistics are routinely used to flag potentially untrustworthy θ estimates. The paper additionally triangulates with Fisher Information and DI. There is no conflation; the critic misunderstands standard psychometric practice. The paper's framing is reasonable. A weakened version is kept as a Minor weakness above (interpretive nuance), but the "fatal conflation" claim is removed.

- **"Circularity in the discrimination index calculation"** — DI is computed per-population using each population's own θ estimates (humans from human θ, LLMs from LLM θ). This is standard practice. Using the same data to group and compute DI is typical; cross-validation would be more rigorous but is not standard and not required. This criticism is invalid.

- **"Lack of validation that the IRT model itself is appropriate for LLMs / should retrain model on LLM responses"** — The paper's explicit research question (Section 2, lines 33–34) is whether LLMs follow human-like patterns under the human-calibrated model. Retraining on LLM responses would change the research question entirely. The paper is transparent about this design choice. The unidimensionality check done by the ENEM team for humans is referenced (Section 4.1); expecting the same check for LLMs would be a different study.

- **"Limited model scope and prompt engineering"** — The paper appropriately scopes its conclusions to the tested models (7B-13B + GPT-3.5). The models tested provide diversity in architecture, training data, and size. Prompt variations (0-shot, 1-shot, 4-shot) are covered in the appendix.

## Novel Insights

The reviews collectively surface one genuinely interesting observation that goes beyond the paper's own contributions: the fact that the paper finds LLMs showing human-like l_z on the Math exam (where everyone is guessing) and non-human-like l_z on Natural Sciences (where high-accuracy models have unlikely patterns) suggests that the relationship between item difficulty, domain knowledge, and response consistency is not monotonic for LLMs. This creates an interesting tension: a test that is "too hard" may produce deceptively human-like patterns (because random guessing masks systematic deviations), while a test that LLMs partially understand but process differently (Natural Sciences, with its mix of text and image/numeric reasoning) exposes the deepest non-human-like patterns. This suggests that the most informative IRT-based evaluation for LLMs may come from exams where the models perform at intermediate levels, not from exams where they either fail entirely or succeed uniformly.

## Suggestions

1. Reframe the l_z discussion in Section 5.3 to more explicitly acknowledge that low l_z for LLMs under a human-calibrated model could reflect model misfit due to different response processes, not just unreliable θ estimation. This would strengthen the paper's rigor without weakening its conclusions.
2. Add standard errors or Bayesian credible intervals for the language-comparison claims (Portuguese vs. English performance) in Section 5.1.
3. Define a threshold for what constitutes "not meaningful measurement" based on Fisher Information (e.g., SE > 0.5 logits) to make the conclusion about the Math exam more precise and less subjective.
4. Add a brief analysis or at least a cautionary note about potential 2022 exam leakage, e.g., comparing LLM performance on questions with high vs. low web presence.

## Score and Decision

The paper contributes a novel, well-executed application of psychometric methods to LLM evaluation using a unique large-scale dataset. The core findings are sound and the converging evidence from multiple IRT-based measures strengthens the conclusions. The weaknesses are minor interpretive and presentational issues that do not threaten the paper's contribution. I recommend acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>