Now I have a thorough understanding of the paper. Let me compile the final consolidated review, carefully cross-referencing each claim against the actual paper content.

## Summary

The paper presents R-HORIZON, a method that composes existing single-horizon reasoning problems into multi-step, interdependent tasks by linking problem answers to key variables in subsequent problems. The method serves a dual purpose: (1) as a benchmark for evaluating LRMs' long-horizon reasoning, and (2) as training data for RL. Benchmark evaluation across 26 models and 6 datasets reveals severe performance degradation as the reasoning horizon increases, with diagnostic analysis showing bounded effective reasoning length, localized reflection, and poor thinking budget allocation. RL training on R-HORIZON data (n=2, n=4) on R1-Qwen-7B shows improvements on both multi-horizon and single-horizon tasks compared to training on single-problem data.

## Strengths

1. **Composition pipeline is clean, scalable, and well-specified.** The two-stage construction (seed filtering via key-variable extraction and dependency-chain composition via Algorithm 1) is clearly explained and automatable. The use of integer key variables and linear dependency functions is simple but sufficient for creating math problems with sequential dependencies. This directly supports the paper's claim of a "scalable, controllable, and low-cost" approach.

2. **Comprehensive evaluation reveals a critical and consistent limitation.** All 26 evaluated LRMs, including frontier models (DeepSeek-R1, Qwen3-235B-Thinking, o4-mini, Gemini-2.5-Pro), suffer substantial accuracy degradation as the number of composed problems increases. The gap between actual and expected accuracy widens consistently across 6 datasets spanning math, code, and agentic tasks (Figures 1 and 3). This is strong, direct evidence that current LRMs lack robust long-horizon reasoning capabilities, as claimed.

3. **Diagnostic analysis goes beyond aggregate accuracy to identify specific failure modes.** The paper isolates four error categories (Problem Reasoning Error, Dependency Reasoning Error, Early Stop, Output Truncation) and shows that the dominant failure is problem reasoning errors, not dependency errors. The effective-reasoning-length analysis (Figure 6) identifies concrete token-length boundaries (~4-6k for 7B, ~8-10k for 32B on MATH500). The thinking-budget and reflection analyses (Figures 7 and 8) provide behavioral explanations for performance degradation. These analyses are grounded in data and support the paper's claims about LRMs' limitations.

4. **RL with R-HORIZON data demonstrates tangible improvements on both multi-horizon and single-horizon tasks.** In Table 1, training with n=2 composed queries yields +7.5 on AIME24 (single) and +17.4 on AIME24 (n=2) relative to single-problem training. Training with n=4 composed queries improves MATH500 n=8 from 11.8% to 50.6%. These are substantial gains that support the claim that R-HORIZON data enhances long-horizon reasoning and generalizes to standard tasks.

5. **Training with composed data also improves reasoning efficiency.** Models trained on R-HORIZON data generate shorter responses, allocate thinking budget more evenly across multiple problems, and show increased long-range reflection (Figure 9). The rollout efficiency analysis (Figure 10) shows ~20% more effective samples per batch. These behavioral improvements directly address the limitations identified in the evaluation.

6. **Broad coverage across tasks, models, and scales.** The benchmark spans 6 datasets (MATH500, AIME24, AIME25, AMC23, LiveCodeBench, WebShaper) covering math, code, and agentic domains. The 26 LRMs range from 1.5B to 235B parameters, supporting the generality of the observed degradation and the utility of R-HORIZON across diverse settings.

## Weaknesses

### Fatal

None.

### Major

1. **Data quantity confound in the RL training comparison.** The paper compares training on single problems (n=1) with training on composed problems (n=2, n=4) but does not report whether the number of training samples or the number of atomic problem instances was matched across conditions. A composed sample of n=2 contains two distinct atomic problems; if the same number of training samples is used for both conditions, the composed condition exposes the model to roughly twice as many atomic problems per step (or per epoch). Improvements on both single-problem and multi-problem evaluations could therefore be driven by increased exposure to more problem content rather than by the compositional dependency structure. The paper never acknowledges this confound or describes any control (e.g., halving the number of composed samples to equalize atomic counts, or including a condition with the same atomic problems presented independently). This weakens the claim that "R-HORIZON data" specifically—as opposed to simply more multi-problem content—is responsible for the training improvements. (See Section 4.3, Table 1; no mention of sample counts or matching.)

2. **Missing baseline without dependencies.** The benchmark evaluation and RL training lack a condition where multiple problems are concatenated *without* explicit dependencies (analogous to NEST; discussed in Section 2.2 but not included as a baseline). The error-type analysis in Figure 5 shows that Dependency Reasoning Errors are consistently rare, while Problem Reasoning Errors dominate—suggesting that most of the difficulty comes from processing multiple problems in sequence, not from the dependency structure per se. Without an independent-concatenation baseline, it is unclear whether (a) the performance degradation in evaluation and (b) the training improvements are attributable to the dependency structure or simply to the increased number of problems / total output length. This is especially important for the training claims: training on concatenated independent problems might yield similar benefits without requiring dependency modeling. (See Figures 3, 5; Section 4.3.)

3. **Limited scope of RL validation.** All RL experiments are conducted on a single small model (R1-Qwen-7B) with no repeated runs or confidence intervals. While single-model RL experiments are common in this space due to compute constraints, the paper states that "R-HORIZON mitigates the current limitations of long-horizon reasoning in training and evaluation paradigms" and claims it is a "scalable, controllable, and low-cost paradigm for enhancing...long-horizon reasoning capabilities." Generalizability to larger or differently trained LRMs is unknown. The paper should explicitly acknowledge this limitation or provide evidence from at least one additional model scale. (See Section 4.3, Table 1, Figure 4.)

### Minor

1. **Expected accuracy metric assumes independence without discussion.** The expected accuracy (Equation 4) is defined as the product of atomic pass rates, which assumes errors are independent across sub-problems. In practice, errors are likely correlated (e.g., a mistake on problem 1 propagates, or the model's attention degrades across a long response). The gap between actual and expected accuracy therefore conflates dependency effects with the general difficulty of solving multiple problems in one pass. While the expected accuracy is a useful reference point, this assumption should be explicitly discussed as a limitation.

2. **Verification model M is unspecified.** The key-variable verification step (Equation 2) uses a model M to determine whether removing an integer renders a problem unsolvable. The paper does not specify which model M is used or report its accuracy. This is needed for reproducibility, as the selection of key variables directly affects the quality of composed problems.

3. **Training data statistics are missing.** The paper does not report the size of the filtered data pool, how many composed samples were generated per condition, or the number of training steps / samples used. These details are needed to assess the fairness of the comparison and to enable reproduction. The paper states "Details are in Appendix F," but those details are not accessible in this version.

4. **"Avg. Multi" in Table 1 averages across inconsistent n values.** The "Avg. Multi" column combines MATH500 (n=8), AIME24 (n=2), AIME25 (n=2), and AMC23 (n=2). Averaging across different n-values and tasks could obscure per-dataset patterns. The selection and aggregation should be justified.

5. **Error-type categories are manually defined without inter-rater reliability.** The error categorization in Figure 5 relies on manual labeling. No inter-rater reliability is reported, and the categories (e.g., "Problem Reasoning Error" vs. "Dependency Reasoning Error") may have ambiguous boundaries. This is a minor concern given the clear qualitative trends but should be noted.

### Trivial

1. The title asks "How far can your large reasoning model really go in breadth and depth?" but "breadth" is never defined and the paper focuses entirely on depth (sequential multi-step problems). The title is slightly broader than the scope.

## Nice-to-Haves

- A direct comparison with independent multi-problem concatenation (no dependencies) as a baseline for both evaluation and training would substantially strengthen the paper and isolate the effect of dependency structure.
- Training results on a second model (e.g., a 32B variant) or with repeated runs / confidence intervals would increase confidence in generalizability.
- Reporting the number of training examples, steps, and whether atomic problem counts were matched across conditions would address the data quantity confound.
- A discussion of the computational cost of the composition pipeline (model M inference calls, etc.) would support the "low-cost" claim.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that "breadth" is undefined:** This is a minor presentation issue but the critic's framing was somewhat exaggerated. The paper's title is slightly broader than its scope, but this is a trivial observation, not a substantive weakness. **Reason:** It's a trivial framing nitpick that doesn't affect the paper's technical contribution.
- **Criticism about linear shift dependency function limiting generality:** The paper presents a method; it does not claim to cover all possible dependency types. This is scope creep. **Reason:** The paper's method uses a specific dependency function for math problems; demanding coverage of all possible complex dependencies is beyond scope.
- **Strength Finder's generic claim that the paper "addresses an important problem":** This is a generic, superficial strength not specific to this paper. **Reason:** Every paper in a competitive venue addresses an important problem; this is not a distinctive strength.
- **Strength Finder's claim about "rollout efficiency gains" being a core strength:** This is a valid supporting analysis but not a core strength of the paper. It's retained as a minor supporting point.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective that the paper itself does not already articulate.

## Suggestions

- **In the rebuttal / revision, address the data quantity confound explicitly.** Either report that atomic problem counts were matched across conditions (if they were), or include a controlled experiment that equalizes atomic exposures. This is the most impactful change the authors could make.
- **Add a multi-problem baseline without dependencies** (concatenated independent problems) for at least one dataset and training condition, to disentangle the effect of dependency structure from the effect of multi-problem length.
- **Specify the verification model M** (e.g., "we used Qwen3-235B-Instruct") and report its agreement with human judgment on a sample of key-variable annotations.
- **Report the number of training samples and steps** used for each condition, and clarify whether the total number of atomic problems was kept constant across n=1, n=2, n=4 conditions.
- **Acknowledge the independence assumption of the expected accuracy metric** and discuss its implications for interpreting the gap.
- **Clarify the "Avg. Multi" column** in Table 1 by stating the n values used per dataset and the rationale for averaging across them.

## Score and Decision

The paper makes a solid contribution with a well-specified composition method, a comprehensive evaluation that convincingly demonstrates LRMs' limitations in long-horizon reasoning, and insightful diagnostic analysis. The RL training results are promising but weakened by the data quantity confound and the absence of an independent-concatenation baseline, which prevent strong conclusions about the specific benefit of the dependency structure. The core benchmark and evaluation contributions are independently valuable and would likely be accepted even without the training experiments being fully resolved. With the training claims appropriately tempered and the confound addressed, this would be a strong paper. I recommend acceptance with the expectation that the confound and missing baselines are addressed in the final version.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>