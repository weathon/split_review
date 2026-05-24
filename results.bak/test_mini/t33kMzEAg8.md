## Summary

This paper proposes SwiReasoning, a training-free inference framework that dynamically switches between explicit chain-of-thought reasoning and latent (soft-embedding) reasoning based on entropy trend signals, complemented by a switch-count controller that forces early answer generation to curb overthinking. The method is evaluated on 11 benchmarks across math, STEM, coding, and general reasoning, using four model families/scales (1.7B–32B). The reported gains are consistent in accuracy (≈1.8–3.1% absolute) and substantial in token efficiency (≈57–79%) under constrained budgets.

---

## Strengths

- **Consistent accuracy gains across model families and scales**: Table 1 reports Pass@1 improvements of +1.8% (DeepSeek-R1-Distill-Llama-8B), +2.03% (Qwen3-8B), +2.68% (Qwen3-1.7B), and Table 4 shows +1.92% on Qwen3-32B over standard CoT, demonstrating that the switching mechanism generalizes beyond a single model or size.

- **Large token-efficiency improvements under limited budgets**: Figure 2 and Figure 4 report peak efficiency gains of 4.6×–6.8× over CoT, with average efficiency improvements up to +79% across benchmarks, and the Pareto frontier advantage persists across a wide range of token budgets.

- **Pass@k evaluation shows faster convergence**: Figure 5 shows that on AIME24, SwiReasoning reaches its maximum Pass@k accuracy at k=13 vs. k=46 for CoT (72% fewer samples), and on AIME25 at k=16 vs. k=22, directly validating that the method produces higher-quality samples earlier.

- **Thorough ablation on signal-mixing hyperparameters**: Table 2 sweeps α₀ (entrance bias) and β₀ (exit bias) independently across 11 values, providing concrete evidence for the β₀=0.7 design choice and showing sensitivity (e.g., AIME24 drops to 8.33% at β₀=0.0).

- **Generalization to broader domains**: Table 5 shows SwiReasoning improves accuracy by +2.70% on average across coding (HumanEval, LeetCode-Contest, MBPP, LiveCodeBench), multi-hop QA, and commonsense reasoning, with the largest gain (+18.18%) on LeetCode-Contest Hard.

- **Asymmetric dwell-window design is well-motivated**: Section 3.3 provides a clear justification for W_{L→E}=0 (immediate switch when confidence rises) vs. W_{E→L}>0 (dwell required before exiting explicit mode), supported by ablation in Table 3.

---

## Weaknesses

### Fatal
None.

### Major

- **The entropy-confidence link at the heart of the method is not directly validated.** The entire switching mechanism rests on the assumption that local next-token entropy reflects global reasoning confidence, but the paper provides no qualitative analysis (e.g., case studies showing entropy trajectories alongside actual reasoning paths, with switch points annotated) demonstrating that this correlation actually holds. The ablation on dwell windows (Table 3) shows that W=512 works best, which is consistent with the entropy signal being noisy enough to require conservative engineering — but it does not substitute for direct evidence that low entropy corresponds to "converged reasoning" and high entropy to "productive exploration." This weakens the claimed insight that the dynamic switch is "guided by block-wise confidence estimated from entropy trends" (Sec. 3.3).

- **The efficiency gains under limited budgets are not properly disentangled from the early-stopping effect.** The switch count controller (Sec. 3.4) forces early answers at switch boundaries via C_max. Under limited budgets, smaller C_max truncates generation earlier, which naturally improves token efficiency compared to CoT baselines that are *not allowed to stop early*. The paper attributes these efficiency gains to "overthinking suppression" without separating (1) the benefit of switching between modes from (2) the benefit of early truncation per se. A CoT baseline with an analogous early-stopping mechanism (e.g., entropy-based or length-based) is needed to isolate the contribution of mode switching. As reported, the accuracy gains under unlimited budgets (where C_max is large enough to not force termination) are only ≈2% absolute, suggesting mode switching alone provides a modest benefit while the headline efficiency gains are inflated by the orthogonal early-stopping trick.

- **No variance or statistical significance reported for any accuracy numbers.** All tables show single point estimates with no confidence intervals, standard deviations, or multiple seeds. Given that several hyperparameters are swept and the gains are relatively small (1.8–3.1%), it is impossible to assess whether these improvements could be within the noise range of decoding randomness. This is especially concerning for comparisons where the margin over CoT is under 1% on individual benchmarks (e.g., GSM8K: +0.46% on Qwen3-8B, +0.39% on Qwen3-1.7B).

### Minor

- **Hyperparameter values for T_max and the dwell window W_{E→L} are not stated in the main experimental setup.** T_max (the maximum generation length used in the α_t/β_t scheduling in Eq. 4-5) is mentioned as "a predefined maximum generation length" but never given a concrete value. The dwell window W_{E→L}=512 appears only in the ablation (Table 3), not in the main experimental settings section. These details are necessary for reproducibility.

- **The Soft Thinking baseline's performance on DeepSeek-R1-Distill-Llama-8B is suspiciously low** (51.52% vs. 59.46% for CoT, a −7.94% gap), which is a much larger drop than the Soft Thinking paper typically reports on comparable models. The paper states baselines follow original-paper recommendations but does not report any hyperparameter search for Soft Thinking across tasks. If the baseline is not properly configured, the comparison tilts in SwiReasoning's favor.

- **Computational overhead of the switching logic is not discussed.** Computing per-step entropy during latent blocks requires a full softmax over the vocabulary, which has non-zero cost. Generation runtime or throughput comparisons between SwiReasoning and CoT are not reported, making it difficult to assess the practical overhead.

- **The fixed hyperparameter choices (β₀=0.7, W=512, C_max values) are used across all benchmarks without justifying whether they were selected on a held-out set or are model-specific.** Sensitivity across model sizes (e.g., does W=512 work equally well for 1.7B and 32B?) is not analyzed.

### Trivial
None.

---

## Nice-to-Haves

- Including a fixed-schedule baseline (e.g., alternate every K steps between explicit and latent) would strengthen the claim that entropy-based *dynamic* switching is actually better than a static pattern.
- The Pareto frontier plots (Fig. 4) compare SwiReasoning against individual baselines per panel. A single combined plot per model showing the Pareto frontier of *all* methods simultaneously would more cleanly demonstrate dominance claims.
- A qualitative analysis showing 2–3 reasoning examples with entropy trajectories and switch points would directly validate the core design assumption and strengthen the paper significantly.

---

## Removed Points

- **"No statistical significance" from harsh critic's "Missing Parts" section** → Already included as a Major weakness above (merged).
- **Criticism that the dwell window W=512 is "very large" for a 1.7B model** → Speculative; the ablation shows W=512 empirically works best across model sizes; removed as it contradicts the paper's evidence.
- **Criticism that the +18.18% gain on LeetCode-Contest Hard "could be an artifact of early stopping" helping answer extraction** → Speculative concern without evidence in the paper or from the reviewer.
- **Generic formatting/style nitpicks** from the harsh critic → Removed per instructions.
- **Strength Finder's claim about "well-motivated, asymmetric dwell-window design"** → Kept as a genuine strength (not removed).
- **Strength Finder's generic strength about "addressing an important problem"** → Removed (generic, not specific to this paper's content).
- **Criticism about missing appendix content or stripped sections** → Removed per instructions (appendix content exists in original submission, stripped by parser).

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the main strengths and weaknesses.

---

## Suggestions

1. **Add qualitative validation of the entropy-confidence link.** Plot 2–3 reasoning trajectories with per-step entropy, mark switch points, and demonstrate that switches align with meaningful changes in reasoning quality.
2. **Disentangle mode switching from early stopping.** Run an ablation where SwiReasoning uses unlimited switches (no forced early answer) and compare token efficiency against a CoT baseline that also uses a simple early-stopping rule (e.g., length threshold or entropy-based). This would isolate the benefit of mode switching per se.
3. **Report variance.** Run each experiment with at least 3 seeds and report means with standard deviations or confidence intervals.
4. **State all key hyperparameters (T_max, W_{E→L}) explicitly** in the main experimental settings section.
5. **Document the hyperparameter search for Soft Thinking** and report whether Soft Thinking's performance on DeepSeek-R1-Distill-Llama-8B is consistent with the original paper's reported ranges.

---

## Calibration

**Round 1 bracketing:** The topic "training-free inference method for LLM reasoning with explicit/latent switching" was queried in three bands. Weak anchors (<3.5) returned papers on unrelated topics (e.g., visual reasoning, diffusion LMs, in-context learning) with avg scores 2.0–3.0. Middle anchors (3.5–7.5) returned the most relevant comparisons: "Rethinking LLM Reasoning" (avg 5.0, Accept Poster), "Latent Reasoning as Vocabulary-Space Superposition" (avg 4.0, Reject), "HybridCoT" (avg 4.5, Reject), and "Fractional Reasoning" (avg 4.5, Reject). Strong anchors (>7.5) returned papers on unrelated topics (multimodal verification, multi-turn conversation, transduction, RL) with scores 8.0. Initial bracket: 4.5–6.5.

**Round 2 narrowing:** Two queries in the (4.5, 6.5) range returned highly relevant papers: "EAT: Entropy After /Think" (avg 5.0, Reject, scores: 6,8,2,4), "Deep Think with Confidence" (avg 5.5, Accept Poster, scores: 4,4,6,8), "Dynamic Early Exit/DEER" (avg 5.33, Accept Poster, scores: 6,4,6), "Explore Briefly, Then Decide/CER" (avg 5.0, Reject, scores: 8,4,2,6), and "First Try Matters" (avg 5.5, Reject, scores: 6,6,4,6).

**Anchor comparison:**
- **EAT** (avg 5.0, Reject): Similar entropy-based confidence signal with weaker validation, but SwiReasoning has broader evaluation (11 vs 4 benchmarks), more novel mechanism (mode switching vs simple early exit), and no pre-filtering issues. SwiReasoning is clearly stronger.
- **CER** (avg 5.0, Reject): Training-required RL method limited to math; SwiReasoning is training-free and covers more domains. SwiReasoning is stronger.
- **DEER** (avg 5.33, Accept Poster): Training-free early exit on 10 benchmarks/11 models; comparable in scope. SwiReasoning has more novel contribution (mode switching) and broader domains, but weaker validation of core mechanism. Roughly comparable, SwiReasoning slightly ahead in novelty.
- **DeepConf** (avg 5.5, Accept Poster): Confidence-based filtering for parallel traces; requires expensive K=512 rollouts. SwiReasoning operates on a single path. Comparable quality of work.

The paper is clearly stronger than the 5.0 anchors and comparable to the 5.33–5.5 anchors. Given the genuine novelty (mode switching is a genuinely new idea in this space), comprehensive evaluation, but notable gaps in validating the core entropy-confidence assumption and disentangling the two mechanisms, the paper sits at the upper end of this range.

---

## Score and Decision

**Score:** 5.5

**Decision:** Accept

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>