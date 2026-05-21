Now I have sufficient calibration. Let me write the consolidated review.

**Round 1 bracket:** 4.5 – 7.0 (clearly above weak papers scoring 2-4, below elite papers at 7.5+).

**Round 2 narrowing:** The paper is consistently above the 4.25-5.25 band (RaR, LaTRO, Rational Metareasoning, Faithful CoT, Implicit CoT), comparable to 5.75-6.00 accepted papers (CoTFormer, Chain-of-Embedding), but not at the 6.67-7.00 level of higher-impact CoT analyses.

**Final score: 6.5** — above CoTFormer (5.75, Accepted) and CoE (6.00, Accepted) due to broader evaluation, but below the 6.67-7.00 papers which have higher-impact or more theoretically grounded findings.

---

## Summary

This paper introduces SWIREASONING, a training-free inference framework that dynamically alternates between explicit chain-of-thought reasoning and latent (soft-embedding) reasoning based on block-wise entropy-derived confidence. A switch count controller further caps the number of mode transitions to suppress overthinking. The method is evaluated across 11 benchmarks spanning math, STEM, coding, and general reasoning, using four model families (DeepSeek-R1-Distill, Qwen3-1.7B/8B/32B). SWIREASONING consistently improves accuracy by 1.8%–3.1% under unlimited budgets and achieves 57%–79% average token efficiency gains under constrained budgets, with Pareto-dominant frontiers across nearly all settings.

## Strengths

- **Broad and consistent empirical validation across scales and domains.** Table 1 shows +2.03% (Qwen3-8B), +2.68% (Qwen3-1.7B), and +1.80% (DeepSeek-R1-Distill-8B) average accuracy gains on math/STEM benchmarks. Table 4 extends to Qwen3-32B (+1.92%), and Table 5 to coding, multi-hop QA, and commonsense reasoning (+2.70% average). Gains are larger on harder problems (e.g., +5.00% on AIME24/25 for Qwen3-1.7B), consistent with the motivation that switching is most beneficial under high uncertainty.

- **Pareto-dominant token efficiency.** Figure 4 shows SWIREASONING achieves the highest token efficiency across 13/15 evaluations, with average AUC improvements of +84% over CoT. Peak per-token efficiency reaches 4.6×–6.8× over CoT (Figure 2). These results are substantial and are the paper's strongest evidence that the switch count control mechanism effectively curbs overthinking.

- **Thorough ablation studies.** The paper systematically ablates the switch window size (Table 3, optimal W=512), the signal-mixing coefficients α₀ and β₀ (Table 2, showing β₀ is critical and peaks at 0.7), and the maximum switch count C_max (Section 4.5, with monotonic efficiency gains as C_max decreases). The Pass@k analysis (Figure 5) provides an additional lens showing faster convergence to peak accuracy with 72% fewer samples on AIME24.

- **Clear motivation and design.** The paper's core insight — that reasoning should switch modes based on confidence — is well-motivated. The asymmetric dwell window design (\(W_{L→E}=0\), \(W_{E→L}>0\)) is grounded in the different roles of latent (exploratory/divergent) versus explicit (convergent/stabilizing) reasoning, and the ablation confirms this design choice.

## Weaknesses

### Fatal
None.

### Major

- **No statistical uncertainty reported.** The paper reports single-point Pass@1 numbers without confidence intervals, standard deviations, or multiple-seed runs. Given the modest absolute gains (1.8%–3.1% on average, with some individual benchmarks as low as +0.39% on GSM8K for Qwen3-1.7B), it is impossible to assess whether the improvements are statistically meaningful or reflect noise in the stochastic decoding process. This is the paper's most significant weakness. The consistency across many settings is suggestive but not sufficient without uncertainty quantification, especially since both CoT sampling and the switch decision depend on stochastic next-token distributions. *(Applies to Tables 1, 4, 5 and all reported accuracy numbers.)*

### Minor

- **Token efficiency metric framing could be complemented by raw accuracy-vs-token curves.** The primary efficiency metric \(E_m(\ell)\) normalizes against CoT's per-token accuracy at its *peak accuracy point* (Acc*_{CoT}/ℓ*_{CoT}). While this is a defined and internally consistent metric, normalizing against a single CoT operating point means the reported "79% average improvement" could appear inflated relative to what a reader would see in a head-to-head accuracy-vs-tokens comparison. The Pareto plots in Figure 4 already show the relevant curves, but they are labeled with this normalized efficiency metric rather than raw accuracy—reporting both would be more transparent. *(Applies to Section 4.1 metric definition and Figure 4.)*

- **No analysis of switching behavior.** The paper never reports descriptive statistics about the switching dynamics: how many switches occur per problem on average, how switches distribute across easy vs. hard tasks, or how often the entropy criterion triggers versus the dwell window expiry. Such analysis would strengthen the causal narrative — e.g., showing that AIME problems trigger more latent-mode switches than GSM8K would directly support the claim that the method adapts to difficulty. *(Relevant to Section 3.3 and Section 4.5.)*

- **Relative contributions of dynamic switch and count controller could be more explicitly isolated for accuracy.** The accuracy results in Table 1 are obtained with C_max set large enough that further increases do not change accuracy (Section 4.5: "maximum accuracy is reached at saturation"). This implicitly shows that the dynamic switch alone — without the count controller constraining behavior — already produces the accuracy gains. However, the paper would be strengthened by an explicit ablation row (e.g., "SwiR (C_max = ∞)") to make this attribution unambiguous. *(Applies to Section 4.5, third paragraph.)*

### Trivial
None.

## Nice-to-Haves

- **Comparison to early-stopping baselines.** The token efficiency gains could partly be replicated by taking vanilla CoT and forcing it to answer early (e.g., "CoT + forced answer at a fixed token budget"). Comparing against such baselines would clarify that the specific switching mechanism — not merely the ability to stop early — drives the efficiency gains.
- **Difficulty-aware β₀ scheduling.** The ablation shows β₀ is critical and optimal at 0.7 on average, but different problems may benefit from different values. The paper notes this as a "promising improvement direction" — operationalizing it would strengthen the method.
- **Robustness analysis of the entropy criterion.** The single-reference-entropy design (\(\bar{H}\) set at block start) could be compared against alternatives (running-window average, trend slope) in an additional ablation to show the current simple design is adequate.

## Removed Points

- *Criticism that the baseline set is too narrow (missing Wu et al. 2025b).* The paper's core claim is that *switching modes* outperforms single-mode reasoning (explicit-only or latent-only). The three baselines (CoT sampling, CoT greedy, Soft Thinking) adequately cover this claim. Adding another latent-only method would not change the single-mode vs. dual-mode comparison.
- *Criticism that signal mixing is "ad-hoc" / "not principled."* The mixing is explicitly motivated as aligning mode-switch boundaries with the model's learned token patterns. The ablation confirms it works as designed. This is a design choice, not a flaw.
- *Criticism that the switch criterion is fragile / entropy can fluctuate spuriously.* This is speculative — the paper provides no evidence of instability, and the empirical results show the method works consistently.
- *Criticism that β₀ ablation reveals the latent mode "would not naturally conclude."* The exit bias *is* the mechanism designed to signal conclusion. Calling this a weakness is like calling attention "ad-hoc" for a transformer — it's a designed component validated by ablation.
- *Criticism about duplicate Qwen3-8B row.* Parser artifact from PDF extraction; the original table likely has sub-rows for different benchmarks within the General category.
- *Speculation about benchmark-specific hyperparameter tuning.* The paper states consistent settings were used; the appendix (stripped by the parser) contains details.
- *Several other speculative or scope-creep concerns* that are either addressed in the paper or ask for analysis outside the stated scope.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths and weaknesses, with the harsh critic providing detailed methodological scrutiny and the strength finder cataloging the empirical evidence. No reviewer introduced a fundamentally new perspective on the work.

## Suggestions

1. **Add uncertainty quantification as a priority.** Run each method 3–5 times with different random seeds (or use bootstrapping over the benchmark instances) and report mean ± std for the main accuracy tables. This single addition would address the most serious weakness.
2. **Add a brief analysis of switching behavior.** Report the average number of switches per problem on easy vs. hard benchmarks, e.g., GSM8K vs. AIME24, to empirically confirm that the method adapts its behavior to difficulty.
3. **Show raw accuracy-vs.-tokens plots** alongside or instead of the normalized efficiency curves in Figure 4, to complement the normalized metric.
4. **Explicitly state in the ablation that C_max → ∞ preserves accuracy gains** (i.e., the dynamic switch alone is responsible for the accuracy improvements), making the attribution crystal clear.

## Score and Decision

**Final score: 6.5**  
**Decision: Accept**

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| RaR (ElYRG3pJcv, inference-time reasoning) | 4.25 | R1 | SWIREASONING is clearly stronger — broader evaluation (11 vs. 3 benchmarks), cleaner methodology, thorough ablations. |
| LaTRO (4Po8d9GAfQ, latent reasoning optimization) | 3.80 | R1 | SWIREASONING is much stronger — only 2 datasets vs. 11, weaker baselines, no error bars either but smaller scope. |
| Rational Metareasoning (jRZ1ZeenZ6) | 5.00 | R2 | SWIREASONING is stronger — training-free vs. training-based, broader evaluation, more convincing ablations. |
| Faithful CoT (1OyE9IK0kx) | 5.00 | R2 | SWIREASONING is stronger — positive constructive contribution vs. negative results, broader evaluation. |
| Implicit CoT (fRPmc94QeH) | 4.75 | R2 | SWIREASONING is stronger — more comprehensive evaluation across more models and tasks. |
| CoTFormer (7igPXQFupX) | 5.75 (Accept) | R2 | SWIREASONING is slightly stronger — broader evaluation (11 benchmarks × 4 model families vs. limited perplexity/downstream), though CoTFormer has architectural novelty. |
| Chain-of-Embedding (jxo70B9fQo) | 6.00 (Accept) | R2 | Comparable — both have broad evaluation, but CoE's self-evaluation application is more novel while SWIREASONING has more thorough ablations. SWIREASONING slightly ahead in empirical rigor. |
| To CoT or not to CoT (w6nlcS8Kkn) | 6.67 (Accept) | R2 | SWIREASONING is slightly weaker — the meta-analysis paper has broader scientific impact and more rigorous statistical methodology, setting a high bar. |

The paper presents a well-motivated, training-free framework with compelling empirical evidence across 11 benchmarks and 4 model families. The main weakness — lack of error bars — is addressable and does not invalidate the core claims given the consistency across many settings. The Pareto dominance across nearly all evaluations provides strong evidence that the method is genuinely effective.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>