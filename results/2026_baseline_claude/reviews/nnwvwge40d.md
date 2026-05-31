## Summary

VeriFree addresses a key limitation of DeepSeek-R1-Zero-style RL training—its restriction to domains with rule-based verifiable rewards—by deriving an equivalent objective that eliminates verifiers entirely. Under the unique-correct-answer assumption, the expected binary reward E_y[1_{y≡y*}] given a reasoning trace z collapses to π_θ(y*|x,z), the model's own likelihood of the reference answer. This yields a continuous, verifier-free reward signal that matches RLVR in expectation while provably reducing gradient variance via Rao-Blackwellization. Empirical evaluation across MMLU-Pro, GPQA, SuperGPQA, and math benchmarks at 1.7B–8B scale shows VeriFree matches or outperforms verifier-based training while requiring no external model during training.

---

## Strengths

- **Principled and clean derivation.** The reduction from the verifier objective to π_θ(y*|x,z) (Eq. 4) is a direct algebraic consequence of the law of total expectation under the unique-answer assumption—not an ad hoc design choice. This makes the method easy to trust and extend.

- **Formal variance reduction guarantee.** Theorem 1 proves that VeriFree's gradient estimator has lower variance via Rao-Blackwellization, which analytically marginalizes out the answer sample. This directly explains empirical observations of faster convergence (Fig. 4, Left).

- **Distinguishes itself from prior work with the same surface form.** The comparison to JEPO and LaTRO (Sec. 2.3) is one of the paper's strongest contributions. Both prior works optimize variational lower bounds and consistently underperform RLVR; the paper identifies that their use of log π_θ(y*|x,z) as reward (rather than π_θ(y*|x,z)) and fixed-weight supervised terms break the exact equivalence with RLVR and can reinforce flawed reasoning traces. This mechanistic explanation is well-argued.

- **Non-trivial engineering insight on tokenization.** Sec. 2.4 identifies a subtle but real off-policy inconsistency when splitting reasoning trace z via text-matching at `<answer>`, and proposes a precise token-level fix. The ablation (Fig. 6, Left) quantifies the instability caused by ignoring this—this is the kind of detail that is easy to miss and matters in practice.

- **Comprehensive empirical validation.** Tables 1–2 cover three model sizes (1.7B, 4B, 8B), two model families, 14+ subject categories in MMLU-Pro, and additional math benchmarks. The transfer experiment (training on no-math data, evaluating on math; Fig. 5) provides evidence for domain-general skill acquisition.

- **Significant practical benefits.** No verifier model in memory, no reward hacking surface, no reference model needed (KL-free). These advantages are real engineering wins that matter for practitioners training on 8 GPUs.

---

## Weaknesses

### Fatal
None.

### Major

- **Weak verifier baseline.** The primary baseline uses Qwen2.5-Math-1.5B fine-tuned on Gemini-generated equivalence data as the verifier. This is a relatively weak verification signal. The paper's claim that "VeriFree matches or surpasses verifier-based methods" may not generalize to scenarios where a strong verifier (e.g., a 70B+ model) is available. The advantage of VeriFree over a strong verifier is currently unestablished and would substantially strengthen (or qualify) the contribution.

- **Margins are small and lack statistical uncertainty.** Many pairwise differences between Verifier and VeriFree are 0.5–1.5 percentage points (e.g., 63.0 vs. 63.5 on MMLU-Pro 4B; 37.1 vs. 38.0 on SuperGPQA 8B). No confidence intervals, standard deviations, or significance tests are reported. Given evaluation stochasticity in LLM benchmarks, several reported improvements could plausibly be within noise, making it hard to conclude definitively that VeriFree *surpasses* rather than *matches* verifier-based training.

### Minor

- **Unique-answer assumption restricts scope.** The exact equivalence between VeriFree and RLVR in Eq. (4) holds only when there is a single correct answer. In general reasoning domains (law, economics, biology), multiple equivalent phrasings or partial-credit answers are common. The equivalence-class ablation (Sec. 3.3, Fig. 6 Right) shows modest gains from incorporating equivalent answers, but this is evaluated only on MATH-12k—not on the general domains that motivate the paper. It remains unclear how well VeriFree handles multi-answer settings in open-domain tasks.

- **No negative result or failure mode.** The paper consistently shows VeriFree performing well, but there is no discussion of conditions under which VeriFree would fail (e.g., very noisy reference answers in WebData, very low initial model confidence on hard problems where π_θ(y*|x,z)≈0, rendering the gradient signal nearly zero). This gap limits the understanding of when VeriFree should or should not be preferred.

### Trivial

- The model confidence correlation (ρ=0.82, Fig. 4 Right) is interesting but only shown for one model/benchmark.

---

## Nice-to-Haves

- Report evaluation with a much stronger verifier (e.g., Qwen2.5-72B or comparable) as an upper-bound baseline; this would clarify how much of the claimed advantage is method quality vs. weak baseline.
- Include confidence intervals (or at minimum, report over two random seeds) for Tables 1–2 to support claims of VeriFree "surpassing" baselines.
- Extend the equivalence-class study to general (non-math) domains to assess whether that missing signal is consequential outside math.
- Investigate behavior in the very-low-confidence regime (π_θ(y*|x,z) ≈ 0) to characterize potential failure modes.

---

## Novel Insights

The most genuinely novel conceptual contribution is the mechanistic explanation for *why* JEPO and LaTRO underperform standard RLVR despite having a superficially similar structure. By aligning the gradient expressions side-by-side (Sec. 2.3), the paper shows that both methods use a fixed weight of 1 on the supervised term ∇_θ log π_θ(y*|x,z), which unconditionally increases the probability of y* regardless of reasoning trace quality—potentially reinforcing incoherent reasoning. VeriFree instead weights this term by π_θ(y*|x,z), automatically suppressing supervision from low-quality traces. This distinction—which falls out naturally from exact derivation of the original RLVR objective rather than a variational lower bound—is a crisp and practically consequential theoretical observation that may influence how future verifier-free RL methods are designed.

---

## Suggestions

1. **Stronger verifier ablation**: Add one experiment where the verifier is a much larger/stronger LLM (e.g., Qwen3-72B or equivalent) to bound the regime where VeriFree's practical simplicity comes with a performance cost.
2. **Error bars**: Report at least one repeated run or bootstrap confidence interval for headline numbers, especially where margins are <1.5%.
3. **Failure characterization**: Add a brief analysis of cases where VeriFree's reward signal (π_θ(y*|x,z)) stays near zero throughout training—what happens to those examples, and does the model diverge or stagnate?
4. **Equivalence class for general domains**: Apply the equivalence-class construction to a general (non-math) domain in WebData (e.g., chemistry or law) to validate whether incorporating answer equivalence matters in those settings.

---

## Score and Decision

VeriFree is a clean, principled, and practically motivated paper. The core derivation is correct, the theoretical analysis is sound, and the empirical coverage is among the broadest for this class of method. The key weakness is that comparisons are made against a weak verifier, leaving open the question of whether VeriFree's advantages persist against strong verifiers. The improvements are real but often narrow. Nonetheless, the method is valuable for practitioners (no verifier overhead), the mechanistic contrast with JEPO/LaTRO is a genuine intellectual contribution, and the engineering insight on tokenization-aware splitting is directly useful. The paper belongs in the accepted category.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>