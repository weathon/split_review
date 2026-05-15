Now I have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes CIPHER, a communication protocol for multiagent LLM debate where models communicate via expected token embeddings (probability-weighted averages over the full vocabulary) rather than sampled tokens. The motivation is that token sampling discards distributional information that could be useful for debate, and the paper shows consistent accuracy improvements (0.5–5.0%) over natural language debate across five reasoning tasks and multiple open-source LLMs (LLaMA-2-70B, LLaMA-65B, Falcon-40B-Instruct, MPT-30B, WizardMath-70B-V1.0), without any weight modification.

## Strengths

- **Novel and well-motivated approach to a genuine problem**: The paper identifies a real limitation of natural language debate — information loss from token sampling — and proposes an elegant alternative. The concrete example (Fig. 1a) where LLaMA-2-70B generates "9" while the correct token "6" had substantial probability mass is compelling motivation. Replacing token sampling with the expectation over the full embedding space is a creative solution that addresses this specific bottleneck.

- **Consistent empirical gains across diverse settings**: CIPHER outperforms natural language debate (NLD) on all five reasoning datasets (Table 1), with improvements also holding across Falcon-40B-Instruct, MPT-30B, and WizardMath-70B-V1.0 (Fig. 2). The cross-model debate result (LLaMA-65B improving from 35% to 62.5% on Arithmetic when paired with LLaMA-2-70B, Table 2) is particularly striking and demonstrates a practical benefit beyond what NLD provides.

- **Strong ablation study with mechanistic insight**: The partial CIPHER experiment (Fig. 7) is the most illuminating part of the analysis. Applying CIPHER only at high-uncertainty steps (measured by entropy or max probability) closely matches full CIPHER performance, while the reversed policy (CIPHER only at low-uncertainty) causes large performance drops. This directly supports the claim that CIPHER's benefit comes from preserving distributional information precisely when the model is uncertain.

- **Temperature sensitivity analysis provides practical guidelines**: The contour plots (Fig. 6) reveal a clear and interpretable strategy: pair a low-temperature agent (for reliable, human-interpretable final answers) with a high-temperature agent (to convey less-confident, complementary information). This is a non-obvious finding that gives practitioners a concrete configuration rule.

- **No weight updates required**: CIPHER works with frozen, off-the-shelf models, making it immediately applicable without additional training or fine-tuning.

## Weaknesses

### Fatal

None. The paper's core claim — that CIPHER improves debate accuracy — is supported by consistent empirical evidence across multiple tasks and models. While some concerns about statistical rigor and cost accounting are significant, they do not invalidate the central finding.

### Major

- **No confidence intervals, standard deviations, or significance tests for any result.** The paper acknowledges that baseline methods exhibit "high variance (0.5–3.0% across datasets)" (line 182), yet reports CIPHER improvements in the range of 0.5–5.0% with no quantification of uncertainty. For large datasets (GSM8K, Professional Psychology, Arithmetic), evaluation is conducted on only 200 test questions (line 174), which is far below the full dataset sizes. Without error bars or significance tests, it is impossible to determine which of the reported gains are statistically reliable and which may reflect sampling noise. This is the most significant weakness of the paper.

- **Computational cost is not discussed and the primary comparison to Self-Consistency is not cost-matched.** The paper claims that CIPHER debate matches Self-Consistency (Major@5) at five responses per setting (line 182), but the inference budgets are fundamentally different. Self-Consistency generates five independent single-model responses, while CIPHER uses 2 agents × 3 debate rounds = 6 generations per debate run, plus the cost of computing a weighted average over the full vocabulary (V ≈ 32k–100k) at every decoding step. The paper neither acknowledges nor analyzes this discrepancy. The CIPHER vs. NLD comparison *is* cost-matched (same debate structure), which partially mitigates this concern, but the claim of "fair comparison" to Self-Consistency is overstated.

- **Optimal temperatures selected via Bayesian optimization are not reported anywhere in the paper.** The paper describes using Bayesian optimization for temperature tuning (line 152, line 239), which is good practice, but never reports the chosen temperature values. This makes it impossible for other researchers to reproduce the results or apply CIPHER without re-running the optimization.

### Minor

- **The claim about generalizing to "smaller open-source models" is not tested on the model sizes referenced in the motivation.** The introduction motivates the work by noting that prior debate methods fail on models like Vicuna-13B (13B parameters), and claims that CIPHER "can generalize across a wide array of LLMs, enabling even smaller LLMs to unlock the benefits of debate" (line 31). However, the smallest model tested is MPT-30B (30B parameters). While 30B is "smaller" than 70B in relative terms, the claim about generalizing to models in the 7B–13B range is unsubstantiated by the current experiments. This does not undermine the paper's core contribution but would strengthen it.

- **No analysis of how LLMs internally process expected embeddings.** The paper notes that weighted averages lie in the convex hull of the embedding space and "might be graspable" by LLMs (line 84), but provides no direct analysis (e.g., perplexity comparisons, hidden state similarity, attention pattern analysis) of whether the model's internal representations remain coherent under this non-standard input. The empirical task accuracy is indirect evidence, but the paper would be stronger with additional sanity checks showing that the model's internal processing does not degenerate. This is a gap in the theoretical grounding rather than a flaw in the experimental results.

- **The EOS stopping heuristic is not evaluated for reliability.** The generation stops when "the EOS token embedding becomes the nearest neighbor of the newly generated embedding" (line 92). Since embeddings are continuous and the EOS embedding is unlikely to be the nearest neighbor of most generated vectors, the reliability of this stopping criterion is unclear. No analysis or ablation of this design choice is provided.

- **The Expected SARSA analogy is decorative** (line 153). The paper draws a connection to Expected SARSA but conducts no experiments or analysis that leverage this framing. It serves only as intuition and could be removed without affecting the paper's contributions.

### Trivial

- None that survive filtering. Formatting artifacts in the extracted text (e.g., `\#` in equations, stray braces) are parser issues, not author errors.

## Nice-to-Haves

- Report confidence intervals or bootstrap estimates for all main results.
- Include a compute-matched baseline (e.g., compare CIPHER debate to Self-Consistency with the same number of total forward passes).
- Report the optimal temperatures found via Bayesian optimization in a table.
- Test on genuinely small models (7B–13B range) to support the generalization claim.
- Run a perplexity or next-token-prediction sanity check comparing expected-embedding inputs vs. discrete-token inputs on a held-out corpus.
- Explore partial CIPHER (high-uncertainty only) as a practical, cheaper alternative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The method's core assumption is entirely unvalidated"** (Harsh Critic, Critical Issue #1): This is inaccurate — the entire experimental section validates the approach by showing consistent accuracy improvements across 5 datasets and multiple models. The reviewer's request for perplexity/hidden state analysis is reasonable but calling the assumption "unvalidated" ignores the primary evidence in the paper. Moved to Minor weakness (tempered).

- **"LLMs are trained exclusively on discrete token sequences"** (Harsh Critic, Critical Issue #1 supporting argument): Factually incorrect — LLMs receive continuous token embeddings (dense vectors) as input, not discrete tokens. Their internal processing operates entirely in continuous vector spaces.

- **"Rigorous experimental design ensures fair comparisons"** (Strength Finder, strength #4): Conflicts with verified weaknesses about lack of statistical rigor and cost-matching issues. While temperature tuning via Bayesian optimization is good practice, the overall experimental design has significant shortcomings that prevent calling it "rigorous."

- **"The comparison is systematically unfair"** regarding the five-response setup: The CIPHER vs. NLD comparison is cost-matched (same debate structure). The issue is only with the CIPHER vs. Self-Consistency comparison, which is a secondary baseline.

- **Criticism about missing Vicuna-13B testing**: The paper mentions Vicuna-13B in the introduction to motivate the problem, not as a claim that CIPHER was tested on it. This is scope creep — the paper tests on available open-source models (30B–70B range) and claims generalization to "smaller" models relative to 70B, not specifically 13B.

- **Expected SARSA criticism**: The paper presents this as intuition and decorative analogy, not as a formal claim. Not a genuine weakness.

## Novel Insights

The reviews surface an interesting tension: the partial CIPHER ablation (Fig. 7) is simultaneously the strongest evidence *for* the method and a hint at its biggest limitation. It shows that CIPHER's benefit is concentrated at high-uncertainty steps, which validates the information-preservation hypothesis, but also suggests that full-sequence CIPHER is computationally wasteful. The paper's own evidence implies that a hybrid strategy (CIPHER only at uncertain positions, greedy otherwise) could achieve nearly the same gains at fraction of the cost — yet the authors do not explore this practical variant. This omission is noteworthy because it would address the cost concerns the paper otherwise ignores. A follow-up study that quantifies the exact trade-off between the fraction of CIPHER steps and accuracy could turn this paper's insight into a deployable system.

## Suggestions

1. **Add confidence intervals or standard deviations to all main results.** Report bootstrapped 95% CIs for accuracy on the held-out test sets. This is the single most impactful change the authors could make.

2. **Report the optimal temperature values discovered by Bayesian optimization** in a small table so that practitioners can reproduce the results without re-tuning.

3. **Add an analysis or at minimum a discussion of computational cost.** Compute the cost of the weighted average over V tokens vs. a single token lookup, and report total inference FLOPs or wall-clock time per response for CIPHER debate vs. NLD vs. Self-Consistency.

4. **Test on at least one model in the 7B–13B range** (e.g., LLaMA-2-7B, Vicuna-13B) to substantiate the claim about enabling debate benefits for smaller open-source models.

5. **Explore the partial CIPHER variant** as a practical method, reporting accuracy vs. cost trade-offs.

## Score and Decision

The paper proposes a genuinely novel and well-motivated communication protocol for LLM debate. The core idea is creative, the empirical signal is consistent across diverse settings, and the ablation study provides mechanistic insight. However, the evaluation lacks statistical rigor (no confidence intervals, small test sets), omits any discussion of computational cost, and does not report key hyperparameters (selected temperatures). These weaknesses are substantive but addressable and do not invalidate the paper's central contribution.

**Score: 6.5** — a solid paper with an interesting contribution that would benefit from strengthening the experimental rigor before final publication.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>