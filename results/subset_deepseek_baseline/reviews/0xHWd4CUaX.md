## Summary

This paper proposes a reinforcement learning framework for automated code refactoring that combines contrastive pre-training of code graph embeddings with a composite reward function. The approach uses a syntax-guided contrastive encoder to learn structural invariant representations of code graphs, which are then integrated with traditional code quality metrics in a reward function for an RL agent. The policy network employs graph attention mechanisms to operate on the joint representation space, and the method is evaluated on multiple refactoring datasets, showing improvements over several baselines.

## Strengths

- The paper addresses a practically important problem (automated code refactoring) and proposes a novel combination of contrastive learning with RL for this domain, which is a reasonable research direction.
- The ablation study (Table 2) provides clear evidence that each component contributes to overall performance, with contrastive pre-training showing the largest individual impact.
- The cross-language generalization experiments (Table 3) demonstrate transferability beyond the training language, which is a valuable practical property.

## Weaknesses

### Fatal
None.

### Major
1. **The paper lacks a clear, formal definition of the action space and state space for the RL formulation.** The MDP is mentioned but never concretely specified: what exactly are the actions (specific refactoring operations like "extract method," "rename variable," etc.)? How is the state represented beyond the code graph? Without this, the RL framework is underspecified and the results are difficult to interpret or reproduce.

2. **The evaluation metrics are problematic.** "Syntactic Improvement" is defined as "percentage reduction in code smells (PMD/Checkstyle violations)" — but PMD and Checkstyle are rule-based tools that detect specific patterns. An RL agent could trivially "improve" by removing code that triggers these rules without actually improving code quality. The "Edit Distance" metric is presented as a quality metric, but lower edit distance is not inherently better; a trivial refactoring that changes nothing would have ED=0. The paper does not justify why lower ED is desirable.

3. **The baselines are weak or poorly matched.** The rule-based tools (PMD, Checkstyle) are not designed for automated refactoring — they are static analyzers that detect issues, not generate fixes. Comparing against them is not meaningful. The RL baselines (RLRefactor, GraphRL) are from 2024-2025 preprints/technical reports, not established peer-reviewed methods. The paper does not compare against any recent large language model-based code editing approaches (e.g., CodeLlama, StarCoder fine-tuned for code improvement), which are the current state-of-the-art for code transformation tasks.

4. **The semantic preservation mechanism is insufficiently validated.** The paper uses "differential test verification" via symbolic execution, but symbolic execution is notoriously limited in practice (path explosion, environment dependencies). The paper reports SP scores above 90% for the proposed method, but does not report how many test cases were generated, what coverage they achieved, or whether the symbolic execution actually terminated successfully for all refactored programs. The claim that this ensures "behavior preservation without expensive formal methods" is not supported by evidence.

5. **The paper contains numerous vague or unsupported claims.** For example: "Our approach is excellent in reducing the necessity of expert demonstration based learning" — but no comparison against methods that use expert demonstrations is provided. "The method maintains reasonable performance despite the domain shift" — but the cross-language results show a significant drop (e.g., SI from 83.7% on Java to 68.7% on Python and 63.5% on C++), which is not contextualized against any baseline that was actually trained on those languages.

### Minor
1. The paper does not report variance or statistical significance for any of the results in Tables 1-3. Given the stochastic nature of RL training, reporting single-point estimates without confidence intervals or standard deviations is insufficient.

2. The qualitative analysis (Section 5.5) provides only three brief examples without any systematic evaluation of whether the suggested refactorings are actually correct or beneficial.

3. The reward function (Equation 5) includes a term for "embedding dynamics" (Δh_t), but the paper does not provide a clear justification for why movement in latent space should be rewarded. The correlation in Figure 2 shows a relationship, but correlation does not imply causation.

### Trivial
None.

## Nice-to-Haves
- A formal definition of the MDP (state space, action space, transition dynamics) would greatly improve clarity.
- Comparison against LLM-based code editing approaches (e.g., fine-tuned CodeLlama for code improvement) would strengthen the evaluation.
- Reporting standard deviations and statistical significance tests for all experimental results.
- A more detailed analysis of the semantic preservation mechanism, including coverage statistics and failure cases.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
- Clearly define the action space (list of specific refactoring operations) and state representation in the RL formulation.
- Add comparison against at least one LLM-based code editing baseline to establish relevance to current state-of-the-art.
- Report variance/confidence intervals for all experimental results and perform statistical significance testing.
- Provide a more rigorous evaluation of the semantic preservation mechanism, including the number and coverage of generated test cases.

## Score and Decision

The paper proposes a reasonable combination of contrastive learning and RL for code refactoring, and the ablation study provides some evidence for the contribution of each component. However, the evaluation has significant weaknesses: the baselines are weak or inappropriate, the metrics are not well-justified, the RL formulation is underspecified, and the semantic preservation claims are not adequately validated. The paper does not compare against current state-of-the-art LLM-based approaches, which limits its relevance. The contribution is incremental and the experimental support is insufficient for acceptance at a top venue.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>