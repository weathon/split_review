Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a data-driven approach to estimating question complexity in VideoQA by leveraging generated visual programs. The core idea is to convert natural language questions into executable Python code (via ViperGPT-style generation), then analyze the code's structure (AST subtrees) to predict which questions models will find difficult. The paper introduces **CodePlexity** — a logistic regression model over AST subtree features that predicts model failure — and shows it outperforms both human judgments and text-based complexity metrics at forecasting model performance on held-out models. Using CodePlexity, the paper identifies interpretable shared failure patterns (e.g., reasoning about event ordering) across diverse architectures, and constructs a new benchmark, **CodePlex-QA**, which is claimed to be 1.9× harder than NExT-QA for existing VideoQA models.

## Strengths

1. **Code-based metrics correlate with model performance much more strongly than human estimates.** Figure 3 provides a clean visual demonstration: human-ranked difficulty shows a weak, non-monotonic trend with actual model accuracy, while even a simple code metric (cyclomatic complexity) produces a clear monotonic relationship. This directly validates the paper's central premise.

2. **CodePlexity achieves the highest predictive power on held-out models.** Table 1 reports mPEG scores showing CodePlexity outperforms all text-based metrics (dependency tree depth, BERT, GPT-4) and all non-learning code metrics (Lines of Code, Cyclomatic Complexity) on every held-out model (HGA, SeViLA-ZS, InternVideo, Tarsier). For instance, on SeViLA-ZS, CodePlexity achieves mPEG 0.320 vs. Cyclomatic Complexity 0.241.

3. **Clean evaluation protocol with diverse model coverage.** The paper splits 7 models into training (4) and held-out (3+1 zero-shot) sets, and splits NExT-QA's validation questions into 80% train / 20% test for learnable metrics. This reduces overfitting concerns compared to evaluating on the same models used for training.

4. **Subtree analysis yields interpretable, cross-architecture findings.** The Venn diagram (Figure 4) identifies 8 subroutines statistically correlated with failures across VIOLET, SeViLA, and ViperGPT. The paper provides concrete examples (e.g., "For loops with complex control flow" corresponding to event-ordering questions) that translate opaque model behavior into human-understandable patterns — a genuinely useful output.

5. **The human study is carefully designed.** 30 subjects recruited via Prolific, consistency checks via repeated comparisons, ELO-based ordering — this is a rigorous setup for a study of its size and provides reasonable evidence that humans are poor estimators of model difficulty.

## Weaknesses

### Fatal
None.

### Major

1. **The CodePlex-QA generation pipeline lacks a controlled within-pool validation, making the 1.9× hardness claim uninterpretable.** CodePlex-QA is constructed by (a) generating questions from new videos (MOMA, ActivityNet, Charades) using GPT-4, (b) converting them to code via the ViperGPT pipeline, and (c) selecting the hardest questions using CodePlexity trained on NExT-QA. The hardness comparison is between CodePlex-QA (new videos, LLM-generated questions, CodePlexity-selected) and NExT-QA (different videos, human-written questions). This conflates at least three confounds: different video sources, different question-writing styles (LLM vs. human), and CodePlexity selection. The paper does **not** include an ablation where a *random* subset of candidate questions from the same pipeline is compared against the CodePlexity-selected subset within the same video pool. Without this, the 1.9× gap cannot be attributed to CodePlexity-based selection — it could simply reflect that LLM-generated questions are harder than human-written ones for unrelated reasons. This is the most significant weakness because it directly undermines the paper's third claimed contribution.

2. **The "1.9× harder" computation is not clearly defined or verifiable.** The paper states: "dataset complexity estimated by taking the average performance of the 5 methods and subtracting random chance" (line 194). It does not provide the formula for how this gap is converted to a multiplicative ratio. Using the numbers the authors appear to report in Table 2 (average accuracy ~49.2% on NExT-QA vs. ~31% on CodePlex-QA, both at 20% random chance), the ratio of above-chance performance gaps is roughly (49.2−20)/(31−20) ≈ 2.65×, not 1.9×. Without a transparent derivation, the 1.9× number — which is featured centrally in the abstract and contributions — cannot be independently verified. The paper should either clarify the exact computation or replace it with a more transparent metric.

### Minor

1. **CodePlexity is a learned predictor of model failure, not a discovered measure of intrinsic complexity, and the paper's framing conflates these.** Equation 3 defines CodePlexity(z) = −σ(wx_i + b), i.e., the negative predicted probability of model success from a logistic regression trained on model outcomes. This is a perfectly valid approach, but the paper throughout describes it as "estimating question complexity," "capturing the elusive complexity," and "a complexity metric." The distinction matters because CodePlexity does not tell us whether a question is *intrinsically* complex — it tells us how well its AST subtree features discriminate success/failure given the training data and model set. A question deemed "hard" by CodePlexity might be trivial for a system with different inductive biases. The paper would be strengthened by acknowledging this more explicitly and reframing CodePlexity as a learned predictor of model difficulty rather than a measure of complexity per se.

2. **The subtree analysis lacks multiple testing correction and basic descriptive statistics.** Section 3.3 tests each subtree at p < 0.01 per model. The paper does not report how many subtrees were tested (the size of |S_merged(D)|), the number per model that passed the significance filter, or apply any correction (Bonferroni, FDR). The intersection across 3 models (yielding 8 shared subtrees) provides some protection but is not a substitute for proper reporting. Without knowing the total pool tested, it is impossible to assess whether the 8 shared subtrees represent a meaningful discovery or could arise by chance under the null. Reporting the total tested, the counts per model, and a permutation-based null would substantially strengthen this analysis.

3. **The human study's claim that "humans struggle to accurately estimate which questions are hard" is supported only by visual evidence without quantitative rigor.** Figure 3 shows the human trend visually, but no correlation coefficient, R², or statistical test is reported. The adjacent dependency-tree and cyclomatic-complexity plots are on different x-axes (human ranking vs. metric value), making a formal comparison of their predictive strengths difficult. The claim is plausible and consistent with prior work, but the paper's specific evidence is weaker than the strength of the claim warrants.

4. **No analysis of how code generator quality affects the results.** The entire pipeline rests on ViperGPT's code generation quality. If the code generator produces incorrect or nonsensical programs for certain questions (which is known to happen for complex queries), the AST features may reflect code generation artifacts rather than question difficulty. A basic analysis — e.g., reporting the fraction of NExT-QA questions where ViperGPT produces non-executable or demonstrably wrong programs, and showing robustness to removing these cases — would improve confidence in the findings.

5. **The multi-stage LLM pipeline (LLaVA captioning → GPT-4 question generation → ViperGPT code generation → CodePlexity scoring) introduces compounding error sources.** The 12% manual filtering rate for answerability is modest, suggesting ~88% of automatically generated questions were answerable — this seems high for an LLM-only pipeline. Some validation of answer quality (e.g., human accuracy on a sample) would strengthen the benchmark's credibility.

### Trivial

- The paper refers to prompts and a formal merging definition in "Section 7" (the appendix), which is not present in the main text. Details deferred to appendix are fine, but key numbers (total subtrees tested, merging criteria summary) should be in the main paper.
- The computation of "1.9× harder" should be accompanied by a clear formula, not just a prose description.

## Nice-to-Haves

- A within-pool validation experiment: generate candidate questions from the same video pool, split into CodePlexity-selected and random subsets, and show that models perform significantly worse on the selected subset while human performance stays comparable. This would isolate the effect of complexity selection from dataset confounds.
- Report correlation coefficients and confidence intervals for the human study (Figure 3) rather than only binned averages.
- A failure analysis of the code generator: report the fraction of questions where ViperGPT produces non-executable or incorrect code, and show that results are robust to removing those cases.
- Report the total number of AST subtrees mined, the number significant per model, and a permutation-based null to assess whether the intersection of 8 is unlikely by chance.
- A discussion of whether CodePlexity captures information beyond model-specific failure patterns — e.g., correlation with question length, answer entropy, or visual ambiguity.

## Removed Points

These points from the reviewers were removed or downgraded per the meta-review instructions:

- **"CodePlexity is circularly defined"** — Removed as an overstatement. Training on model outcomes and testing on held-out models is standard supervised learning, not circular reasoning. The valid concern about framing is retained in Minor Weakness #1.
- **"The comparison between BERT and code-based metrics is confounded"** — Removed. Training BERT on programs as well would be a different experiment. The paper's comparison is standard for this type of analysis.
- **"The logistic regression is a black box"** — Removed. The paper explicitly provides the interpretable output (significant subtrees) and discusses them. The complexity score is a linear combination, which is by construction more interpretable than non-linear methods.
- **"The paper does not discuss negative weights in logistic regression"** — Removed as a generic criticism that does not affect the paper's core claims.
- **"Dataset release lacks license, format, or quality assurance details"** — Downgraded to removed. The paper states "Our dataset will be released" which is sufficient for a submission; details are standard for the camera-ready version.
- **Strength Finder claim about human study being "carefully controlled"** — Kept in strengths but qualified, as the reviewer correctly notes the study is limited in size.

## Novel Insights

The meta-review process surfaces one insight beyond the paper's own contributions: the paper's central tension between "complexity as a property of the question" vs. "complexity as a learned predictor of model behavior" mirrors a broader issue in the field's benchmark design philosophy. Top-down approaches start from an expert definition of hardness and validate it. This paper starts from model failure patterns and works backwards toward human-interpretable labels. The reviews reveal that the authors are closer to the latter framing than the paper's language suggests, and the paper would be stronger if it leaned into this distinction explicitly — positioning CodePlexity as an empirical model-failure predictor that happens to yield interpretable insights, rather than claiming to measure "complexity." This framing would inoculate against philosophical objections while preserving all technical contributions.

## Suggestions

1. **Add a within-pool ablation for CodePlex-QA.** Generate ~2000 candidate questions from the same video pool, split into CodePlexity-selected (hardest quartile) and unselected (easiest quartile), and show that models perform significantly worse on the selected subset. This is the single most impactful experiment the authors could add.

2. **Clarify the 1.9× computation.** Provide the exact formula and individual model accuracies used, or switch to a more transparent metric (e.g., the absolute gap in above-chance accuracy).

3. **Reframe CodePlexity throughout** as a learned predictor of model difficulty rather than a measure of "complexity." The technical content is unchanged, but this framing is more precise and avoids philosophical objections.

4. **Report multiple testing statistics for the subtree analysis:** total subtrees tested, count significant per model at p<0.01, and a permutation-based null showing the 8-way intersection is unlikely by chance.

5. **Add a code generator quality analysis:** report the fraction of NExT-QA questions with non-executable or obviously wrong programs, and show that results are robust to excluding them.

## Score and Decision

The paper presents a clever and well-motivated idea with several genuinely interesting findings: code-based metrics (even simple ones) dramatically outperform human estimates of model difficulty; the AST-subtree approach yields interpretable cross-architecture failure patterns; and CodePlexity generalizes to held-out models. The main empirical claims about CodePlexity's predictive power on NExT-QA (Table 1) are solid and well-evaluated.

However, the paper's most prominent claimed contribution — the automatically generated CodePlex-QA benchmark being "1.9× harder" — rests on a comparison that is not adequately controlled. Without a within-pool validation (selected vs. unselected questions from the same pipeline), the hardness gap cannot be attributed to CodePlexity-based selection, and the 1.9× computation itself is unclear. These are substantial gaps, but they are fixable with additional experiments rather than reflecting a fundamentally flawed approach.

The paper has real value — particularly the finding that code structure predicts model difficulty, and the interpretable subtree analysis — but the benchmark claim is currently overclaimed relative to the evidence. With the suggested additions (especially the within-pool ablation and clearer computation), this would be a strong paper. In its current form, the contributions are partially supported.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>