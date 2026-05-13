Now I have a thorough understanding of the paper. Let me synthesize the final review.

Let me verify the mathematical derivation issue more carefully. The paper's derivation goes:

1. $\log p(y|x) = \sum_t \log p(y_t|y_{<t}, x)$ — this is just the chain rule, correct.

2. $\propto \sum_t \log(p(y_t|y_{<t}) * p(x|y_{<t}))$ — This step claims that $\sum_t \log p(y_t|y_{<t}, x) \propto \sum_t \log(p(y_t|y_{<t}) \cdot p(x|y_{<t}))$. This is indeed problematic. By Bayes rule, $p(y_t|x, y_{<t}) \neq p(y_t|y_{<t}) \cdot p(x|y_{<t})$ in any standard sense. The joint $p(y_t, x|y_{<t}) = p(y_t|y_{<t}) p(x|y_{<t})$ only makes sense if $y_t$ and $x$ are conditionally independent given $y_{<t}$, which is generally false. And even then, this doesn't give you $p(y_t|x, y_{<t})$. So this step is indeed mathematically unjustified.

3. $\approx \sum_t \log(p(y_t|y_{<t}, x) * p(C(x)|y_{\leq t}))$ — Here they change $p(x|y_{<t})$ to $p(C(x)|y_{\leq t})$, dropping the conditioning on $y_t$ from the first term (switching from $y_{<t}$ to $y_{<t}, x$ in the first factor and $y_{<t}$ to $y_{\leq t}$ in the second). And they introduce $C(x)$ as a "verbalization" of the constraint. This is a heuristic substitution.

4. Then they replace $\log p(C(x)|y_{\leq t})$ with $R(y_{\leq t}, C(x))$ defined as $\frac{\log p(C(x)|y_{\leq t}, <SEP>)}{|C(x)|}$ — adding a SEP token and normalizing.

So the derivation is indeed not a valid mathematical derivation. The harsh critic is right about this. The steps contain unjustified approximations/proportionalities. However, the paper actually does acknowledge this to some degree — it uses $\propto$ and $\approx$ signs, which signal these aren't exact equalities. The paper claims to "formalize" the problem, but what it really does is provide a motivational derivation that leads to a heuristic.

The claim that $R$ doesn't actually measure future constraint satisfaction is also valid. Computing $p(\text{"This will be a rude, disrespectful comment"} | \text{prefix})$ measures the probability the model generates that literal meta-statement, not whether the prefix leads toward a toxic continuation. However, the paper does note (line 72) that "this might not always yield precise estimations" and the ranking benchmarks show this. The correlation argument (that the proxy works despite the mismatch) is partially addressed by the ranking benchmarks showing above-chance accuracy.

For the missing baselines issue: The paper compares against greedy decoding, nucleus sampling, beam search, and NeuroLogic Decoding (for CommonGen). It does not compare against FUDGE, GeDi, PPLM, or DAPT. The paper discusses these methods in related work but dismisses them as having "limited" control types. However, for a paper claiming a general framework, comparison with these controllable generation methods (especially FUDGE, which is most similar in spirit) would be important. This is a legitimate concern.

For the ELI5 filtered evaluation: The paper does report results on the full ELI5 dataset in Table 8 (line 189) and acknowledges that "the absence of high-quality supported documents leads to a substantial decrease in the average performance." So they do report full results, but the main table (Table 3) only shows the filtered subset.

For the "surpass" claim: The paper says Falcon-40B-Instruct "surpasses" Text-Davinci-003. Looking at the context, the paper says the constraint satisfaction coverage scores are "significantly higher" and that the results "surpass" those of Text-Davinci-003. But the paper also notes BLEU scores are presumably lower. This claim is somewhat misleading if only one metric is considered.

Now let me compose the final review.</think>Now I have read the full paper carefully. Let me compose the final consolidated review.

## Summary

The paper proposes a training-free, decoding-time method for constraining LLM text generation. It introduces a "future constraint satisfaction score" estimated via LLM log-likelihood over a natural-language verbalization of the desired constraint, and integrates this score into a beam-search objective (Equation 2–3). The method is evaluated on three tasks: keyword-constrained generation (CommonGen), toxicity reduction (REALTOXICITYPROMPTS), and factual QA (ASQA/ELI5).

## Strengths

- **Unified, training-free framework across three diverse tasks.** The same mechanism—verbalize the constraint in natural language, estimate satisfaction via LLM conditional probability, and integrate into beam search—is applied without task-specific architectural changes to keyword inclusion, toxicity reduction, and factual correctness. This generality is a genuine advantage over methods like PPLM/GeDi/FUDGE that require trained auxiliary models (Section 5 acknowledges these methods and differentiates the approach).

- **Empirical improvements over basic decoding baselines on all three tasks.** On CommonGen, constraint coverage increases substantially (Table 1). On REALTOXICITYPROMPTS, maximum toxicity decreases (e.g., Falcon-7B-Instruct from 0.45 to 0.33, Table 2). On factual QA, both EM/Recall (ASQA) and claim-level correctness (ELI5) improve over greedy and beam search baselines (Table 3). The human evaluation on ELI5 (Table 7, 30 samples) corroborates the automatic metrics.

- **Transparent diagnostic evaluation of the core proxy mechanism.** The ranking benchmarks (Figures 2a, 2b, Figure 4, Table 4) directly test whether LLMs can discriminate constraint-satisfying from constraint-violating outputs. The paper honestly reports that prefix-pair accuracy is only moderately above chance (often ~55–65%), which is a valuable diagnostic. The method works despite this noisy signal, and the paper does not hide this limitation.

## Weaknesses

### Fatal

**The mathematical derivation in Section 2 is invalid and misrepresents a heuristic as a formalization.** The paper's central conceptual claim is to "formalize text generation as a future-constrained generation problem" (abstract). The derivation from $\log p(\mathbf{y}|\mathbf{x})$ to the final objective contains multiple unjustified steps:

- The transition $\sum_t \log p(y_t|y_{<t}, x) \propto \sum_t \log(p(y_t|y_{<t}) \cdot p(x|y_{<t}))$ has no basis in standard probability theory. This would require conditional independence of $y_t$ and $x$ given $y_{<t}$ (generally false) and does not yield $p(y_t|x, y_{<t})$ via any standard identity.

- The substitution $p(x|y_{<t}) \approx p(C(x)|y_{\leq t})$ simultaneously changes the conditioning variable, introduces a verbalization $C(x)$, and shifts the index—none of which are justified.

The paper presents these as mathematical derivations (using $\propto$ and $\approx$ in displayed equations), but they are post-hoc rationalizations of a heuristic scoring function. This matters because "formalizing" the problem is the paper's primary conceptual contribution. Without a valid derivation, the contribution reduces to "add a heuristic reward term to beam search decoding," which has substantial prior art (noted in the paper's own related work, Section 5).

### Major

- **$R(\mathbf{y}_{\leq t}, C(\mathbf{x}))$ does not reliably measure future constraint satisfaction; it measures the LLM's probability of generating the literal text of the constraint verbalization.** For toxicity, $p(\text{"This will be a rude, disrespectful comment"} \mid \text{prefix})$ measures the probability that the next tokens literally spell out that meta-statement—not that the prefix is heading toward a toxic continuation. For keywords, $p(\text{"This will be a sentence with concepts: car, drive, snow"} \mid \text{prefix})$ does not directly measure whether "snow" will appear later. The paper acknowledges this approximation works through correlation via the LLM's internal model, but the ranking accuracy on operationally relevant prefix pairs is only ~55–65% (Figures 2b, 4b), and the paper provides no analysis of failure modes or how generation quality degrades when the proxy is wrong. The method's reliability is fundamentally limited by this gap.

- **Missing comparisons with directly relevant controllable generation baselines.** Across all three tasks, directly comparable prior methods—FUDGE (Yang & Klein, 2021), GeDi (Krause et al., 2021), PPLM (Dathathri et al., 2020)—are discussed in related work but never compared against experimentally. For toxicity reduction specifically, no comparison is made with methods specifically designed for that task (e.g., DAPT, whose experimental setup the paper adopts). Without these baselines, it is impossible to determine whether the proposed method offers any advantage over existing controllable generation techniques, particularly FUDGE, which is the most similar in spirit (using a future-aware signal to guide decoding).

- **The factual QA results in Table 3 are reported on a filtered subset rather than the full dataset, with the full results relegated to an appendix table.** Line 174 explicitly states: "We consider samples for which the retrieved documents support the answers." Table 8 shows substantial performance degradation on the full ELI5 dataset. This selective reporting inflates apparent effectiveness. While the paper does include Table 8, the main results in Table 3 are the filtered ones, and the fraction of data retained is not disclosed.

### Minor

- **Hyperparameter $\lambda$ is selected on extremely small dev sets** (50 samples for toxicity, "a few samples" for QA, per lines 138 and 166), with no cross-validation, sensitivity analysis on held-out data, or confidence intervals. This raises concerns about robustness and overfitting to the dev set, though it is unlikely to invalidate the overall findings entirely.

- **The claim that Falcon-40B-Instruct "surpasses" Text-Davinci-003 (line 130) is selective.** The paper highlights coverage improvements without equally emphasizing that BLEU scores may decrease (as suggested by Figure 3's tradeoff pattern), framing the comparison in an asymmetric way.

- **The binary Yes/No formulation for estimating constraint scores (Section 2.1, from Scheurer et al., 2023) is mentioned as an alternative but never compared experimentally.** This is a natural ablation since it represents a more direct estimation method; comparing it against the log-likelihood approach would clarify which proxy is more effective.

### Trivial

- None worth noting beyond what's above.

## Nice-to-Haves

- Ablation comparing the log-likelihood score vs. the binary Yes/No formulation for estimating $R$.
- Failure case analysis: examples where the proxy incorrectly ranks prefixes and leads to degraded generation.
- Explicit Pareto analysis of the coverage-vs-fluency tradeoff on CommonGen.
- Robustness analysis for $\lambda$ selection (cross-validation or confidence intervals).

## Removed Points

- **Claim that FUDGE/GeDi/PPLM/DAPT are "not yet released" or unavailable for comparison.** The paper cites these methods; they exist. The missing comparison is a real issue (kept above), but not because they're unavailable.

- **Ambiguity about $\mathcal{V}_t$ definition** (top $2k$ candidates in cumulative probability mass). This is a minor formulation detail, not a substantive weakness. The paper clarifies it adequately.

- **The abstract's claim about "no guarantee of complete prevention" being a straw man.** This is a factual observation about LLMs and serves as motivation; it does not undermine the paper.

- **The speed comparison showing ~$k\times$ slowdown.** This is already acknowledged in the paper (Table 6 and accompanying discussion), and is inherent to any beam-based method. Not a novel weakness.

- **Strength claims about the A* analogy and human evaluation.** The A* connection is mentioned but not developed rigorously—it's a loose analogy. The human evaluation is on only 30 items with low agreement bounds—this is a real limitation but not fatal. Kept the human eval concern minor.

- **Strength claiming Falcon-40B "surpasses" Text-Davinci-003.** This is partially misleading (only on coverage, not fluency); moved to minor weaknesses instead.

## Novel Insights

The paper's key insight—that LLM conditional probabilities over natural-language constraint verbalizations can serve as a *proxy* for future constraint satisfaction during decoding, achieving above-chance but far from perfect correlation—is genuinely interesting. The ranking benchmarks reveal an important finding: LLMs can discriminate *complete-sentence* constraint satisfaction (70–80% accuracy) far better than *prefix* satisfaction (~55–65%), yet the method still works in practice because even a weak signal, when applied consistently at every decoding step, accumulates into meaningful steering. This gap between the proxy's discriminative accuracy and the method's empirical success deserves deeper analysis.

## Suggestions

- Present the derivation in Section 2 honestly as a *motivation* for the heuristic rather than a formal derivation. Use language like "inspired by" rather than "derived from." This would eliminate the fatal issue without changing the method.
- Add experimental comparisons with at least FUDGE (most similar prior work) on one task (ideally toxicity reduction, where FUDGE is directly applicable).
- Report the fraction of ELI5 samples retained in the filtered subset and move the full-dataset results to the main table or give them equal prominence.
- Add a failure-case analysis showing what happens to generation quality when the proxy makes wrong discriminations.

---

**Overall assessment:**

*Originality*: The idea of using LLM log-probability on verbalized constraints as a proxy for future constraint satisfaction is simple and novel. The unified framework is appealing. However, the "formalization" in Section 2 is not valid, which weakens the conceptual contribution significantly.

*Importance*: Controlling LLM outputs at decoding time is an important problem. The method is practical (no training required) and broadly applicable. But without comparisons to existing controllable generation methods, its practical advantage is unclear.

*Soundness*: The mathematical derivation is invalid (major issue). The proxy mechanism is conceptually acknowledged but its limitations are underexplored. The evaluation has gaps (missing baselines, filtered dataset).

*Clarity*: The paper is generally well-written and the three-task evaluation structure is clear. The ranking benchmarks are a transparent diagnostic contribution.

*Value*: The method shows promise as a simple, training-free approach. However, the gap between claimed formalization and actual heuristic, combined with missing baselines, limits the ability to assess its true contribution.

## Score and Decision

The invalid derivation is a significant problem because it undermines the paper's stated conceptual contribution. The missing baselines and selective evaluation compound this. However, the method itself is simple, practical, and shows real empirical improvements. The ranking benchmarks are an honest diagnostic contribution. These are legitimate empirical results that could form the basis of a solid paper if the framing were corrected and baselines added. As it stands, the paper claims too much (formalization) for what it delivers (a heuristic with promising but incompletely validated results).

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>