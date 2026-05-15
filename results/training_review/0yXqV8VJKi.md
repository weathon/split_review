Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes using generated code (from ViperGPT) as a proxy for question complexity in VideoQA. The authors introduce CodePlexity, a metric that mines AST subtrees from generated programs and correlates them with model failures, enabling interpretable analysis of difficulty sources. They further use this metric to filter LLM-generated questions, creating CodePlex-QA — a benchmark reported to be 1.9× harder than NExT-QA for zero-shot models.

## Strengths

- **Generated code as a complexity proxy is a novel and intuitively compelling direction.** The shift from analyzing natural-language questions to their code translations is well-motivated and opens a new axis for automated benchmark analysis. The paper correctly identifies that humans are poor judges of machine difficulty and that code structure captures reasoning demands that surface-level text features miss.

- **CodePlexity's subtree mining provides interpretable insights into model failure modes.** The approach identifies 8 shared AST subtrees whose presence correlates with performance degradation across multiple architectures (Section 4.3, Figure 4). This moves beyond black-box complexity scores toward actionable, human-readable diagnostics about which reasoning patterns (e.g., event ordering, fine-grained object analysis) challenge current models.

- **The human study and clear demonstration that simple code metrics (LoC, cyclomatic complexity) outperform human judgment and text-based baselines.** Even if CodePlexity's advantage over cyclomatic complexity is partially due to being trained, the overall trend — code > text > humans — is robustly supported by Table 1 and Figure 3. The controlled Prolific study (30 subjects, ELO-based ranking) provides reasonable evidence for the motivating claim.

## Weaknesses

### Fatal
None. The core approach is valid and no single flaw invalidates the paper's entire contribution.

### Major

- **The 1.9× hardness claim for CodePlex-QA is weakened by potential overlap between models used to train CodePlexity and models evaluated on the generated benchmark.** CodePlexity was trained on outcomes from M_tr = {VIOLET, SeViLA, ViperGPT, ATP} on NExT-QA. Table 2 evaluates "zero-shot baselines from our pool" and the discussion mentions VIOLET (a training-set model) alongside InternVideo (held-out) to support the claim. While the questions are entirely new (LLM-generated) — so there is no data leakage — the hardness comparison is more convincing for held-out models. The paper should report results separately for models whose outcomes were used to train CodePlexity versus those that were completely unseen during metric development. The current pooling of all 5 methods for the 1.9× calculation conflates in-distribution and held-out evidence.

- **The core assumption that ViperGPT-generated code complexity reflects question-level reasoning difficulty (rather than generator idiosyncrasies) is not validated against a second code generator.** CodePlexity could be capturing patterns specific to ViperGPT's API design, prompting template, or programming style rather than the genuine reasoning demands of the question. The paper acknowledges this only in passing ("videos also contribute to complexity, code is imperfect") without any experiment showing that a different code generator (e.g., VisProg, CodeVQA) would yield a similar complexity ranking. Since CodePlexity's training features come exclusively from ViperGPT's AST, this dependency is a real threat to the generality of the claimed insights.

- **The logistic regression treating each (question, model) pair as an independent instance violates independence assumptions.** With N questions and K models, the training effectively uses N×K instances where the same question with the same code features appears K times. This inflates the effective sample size and could overstate the statistical significance of identified subtree features. The paper justifies this by the goal of finding "universal" patterns, but the statistical machinery does not correct for the clustered structure of the data.

### Minor

- **The human study (150 questions, 30 subjects) reports no quantitative correlation measure.** The paper states the trend is "very weak" based on Figure 3 (left) but does not report a correlation coefficient, confidence interval, or test against the null hypothesis. This makes the claim that "humans struggle to accurately estimate" somewhat informal relative to the rigor applied elsewhere.

- **The interpretation of the 8 shared subtrees in Section 4.3 is speculative.** The paper asserts they correspond to "reasoning about the order of events" and "detailed analysis of specific elements" without showing the actual AST patterns or code snippets. The reader cannot verify whether these patterns map to the claimed semantic categories or are superficial syntactic artifacts of the ViperGPT API. Showing concrete examples would substantially strengthen this analysis.

- **The comparison of CodePlexity to baselines in Table 1 is somewhat asymmetric:** CodePlexity is a trained logistic regression on structured code features, while the LoC and cyclomatic complexity baselines are untrained. A fairer comparison would train linear models on these simple features too, to isolate whether CodePlexity's advantage comes from its structured representation or simply from having trainable parameters. (Note: the paper does include a trained BERT text baseline, which partially addresses this concern.)

### Trivial

- None.

## Nice-to-Haves

- Validate the core assumption by running the same complexity analysis with a different code generator (e.g., VisProg, CodeVQA) and measuring convergence of question complexity rankings across generators.
- Report zero-shot accuracy numbers separately for models whose outcomes were used to train CodePlexity versus completely held-out models.
- Report Pearson/Spearman correlation with confidence intervals for the human study.
- Show actual AST fragments or code snippets for the 8 identified shared subtrees.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Implausibly low NextQA accuracy numbers"** — The critic cites specific numbers (25.8%, 12.3%) and compares them to fine-tuned SotA. The paper explicitly states Table 2 evaluates "zero-shot baselines," making the comparison to fine-tuned performance apples-to-oranges. Zero-shot performance on a challenging 5-way spatio-temporal QA task can legitimately fall near or below chance. Removed as the critic misunderstands the evaluation setting.

- **"Circular evaluation... tautology"** — The critic claims this is a "tautology" where the result is guaranteed. This is incorrect: CodePlexity was trained on NExT-QA outcomes and applied to entirely new LLM-generated questions. The selection function does not guarantee poor performance on unseen questions. The overlap concern is real (moved to Major above) but the characterization as "circular" and "tautological" is overstated. Removed as hyperbole and replaced with a precise description of the actual issue.

- **"Biased toward CodePlexity because baselines are untrained"** — The paper includes a trained BERT text baseline trained on the same data, so the comparison is not purely trained-vs-untrained. The suggestion to train linear models on LoC/cyclomatic features is reasonable but falls into the "nice-to-have" category rather than being a fatal flaw. Moved to Minor and Nice-to-Have.

- **"Missing appendix details" and "deferred to appendix"** — The appendix exists in the original submission; the parser strips these sections. Removed per instructions.

- **"Generically weak strengths"** from the Strength Finder: The claim that the paper has "rigorous evaluation protocol with held-out models and a unified metric" conflicts with the verified weakness about model overlap in Table 2. Removed.

- **"Does not adequately distinguish from prior code-based complexity metrics (Eyzaguirre & Soto 2020)"** — The paper explicitly discusses this prior work in Section 2 and clarifies its differentiating claim: "without needing expensive annotations and generalizing to more question types." The critic's claim that this work also requires annotations (model predictions) is addressed by the paper's methodology (using existing model checkpoints). Removed as the paper already addresses this.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **For the hardness claim (Table 2):** Recompute the 1.9× factor using only models whose outcomes were NOT used to train CodePlexity (HGA, SeViLA-ZS, InternVideo, Tarsier). Report this separately from the full 5-model average. If the gap remains substantial on held-out models alone, the claim is much more convincing.

2. **For the core assumption:** Run a small-scale validation using a second code generator (e.g., VisProg or a prompted CodeVQA-like approach) on a subset of NExT-QA. Show that the complexity rankings produced by the two generators correlate strongly — this would directly address the concern that results are ViperGPT-specific.

3. **For the human study:** Report Spearman's rank correlation between human-estimated difficulty and average model performance, with a 95% confidence interval. This would make the "humans struggle" claim quantitatively crisp.

4. **For subtree interpretability:** Show at least 2–3 concrete code/AST patterns corresponding to the "shared 8 subtrees" in Figure 4, with question examples, so readers can verify the claimed semantic interpretation.

## Score and Decision

The paper presents a genuinely novel approach with a well-structured pipeline from complexity analysis to benchmark generation. The strengths are real and the weaknesses are addressable. The two major concerns — partial model overlap in the hardness evaluation and lack of cross-generator validation — do not invalidate the contribution but do limit the strength of the current claims relative to the paper's ambitious framing.

The paper should be conditionally accepted with the expectation that the authors address the evaluation overlap concern (which is straightforward to fix by reporting held-out numbers separately) and add some form of cross-generator validation. The core idea is worth pursuing and the methodological framework is solid.

**Score:** 6.5 — A solid paper with novel ideas and credible preliminary results, held back by one significant evaluation design gap and one missing validation experiment. Both are fixable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>