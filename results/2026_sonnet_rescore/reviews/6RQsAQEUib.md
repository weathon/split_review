## Summary

GHPO (Guided Hybrid Policy Optimization) addresses reward sparsity in RLVR training of LLMs by dynamically detecting "difficult" queries (those yielding all-zero group rewards across G rollouts) and adaptively injecting partial ground-truth solution traces into the prompt for those queries. The framework thus alternates between standard on-policy RL (for manageable queries) and hint-conditioned imitation learning (for hard ones). Experiments across two datasets, two model families (Qwen2.5-Base-7B and Qwen2.5-Math-7B), and six math benchmarks show a consistent ~5% average accuracy improvement over GRPO.

---

## Strengths

- **Consistent empirical gains across benchmarks and model families**: Table 1 shows GHPO (0.442 avg) vs. GRPO (0.398 avg) on Math3to5; Table 2 shows 0.442 vs. 0.409 on NuminaMath-S. The improvement holds on both Qwen2.5-Base-7B and Qwen2.5-Math-7B (0.5076 vs. 0.4728). The cross-model consistency strengthens the evidence.

- **Adaptive guidance demonstrably beats static/curriculum alternatives**: GHPO (0.442) outperforms GRPO-CL-H(0.5) (0.422) and GRPO-CL (0.415) in Table 2, directly validating that automatic difficulty detection is more effective than fixed-hint or manually-scheduled hinting strategies.

- **Training dynamics evidence supports stability claims**: Figure 4 shows GHPO achieves higher accuracy reward, significantly smaller and more stable gradient norms, and longer (more elaborate) reasoning trajectories throughout training — directly supporting the stability narrative.

- **Reward sparsity problem is concretely quantified**: Section 2.3 reports that even Qwen2.5-7B-Instruct fails on 52% of NuminaMath-1.5 problems; Figure 3 shows ~60% of mini-batch problems remain "difficult" throughout training. This is specific, falsifiable evidence motivating the approach.

- **Practical, no-auxiliary-model design**: GHPO uses ground-truth solution traces already present in math datasets. No auxiliary LLM is needed, directly contrasting with LUFFY-style methods and lowering deployment cost.

---

## Weaknesses

### Fatal
None.

### Major

- **Unacknowledged compute overhead undermines efficiency claims.** When a query is flagged as difficult, GHPO discards the first-pass G rollouts and samples a fresh group of G responses from the hint-augmented prompt q\*. With ~60% of queries flagged as difficult (Figure 3), GHPO incurs roughly 1.6× the per-step generation compute of GRPO. Yet the abstract and Section 6 describe GHPO as "scalable and efficient," and Section 3.2 claims "significantly enhancing training efficiency." No wall-clock comparison, FLOPs accounting, or compute-matched ablation is provided. Without this, it is unclear whether the ~5% performance improvement survives a compute-budget-controlled comparison, making the efficiency framing partially overclaimed.

- **Train-test distribution shift is unanalyzed.** For difficult queries, the policy is optimized on responses conditioned on q\* = q + ω·h (hint-augmented prompt), but evaluated at inference time on q alone (no hint). The paper trains a policy π_θ(o | q\*, …) but tests π_θ(o | q, …). This distributional gap is real and entirely unaddressed — the paper provides no ablation comparing "hint at train time only" vs. "hint at train and test time." The empirical results show the scheme works, but the mechanism by which hint-conditioned training improves unconditional inference is left unexplained.

- **All results are single-run, yet several benchmark numbers are marginal.** AIME2024 in Table 1 moves from 0.131 to 0.133 — effectively no change. OlympiadBench in Table 2 slightly *regresses* (0.396 → 0.389). GPQA-Diamond (198 problems) has high per-question variance. Without multiple seeds or confidence intervals, it is impossible to determine which observed improvements are robust signal versus variance, especially on small-sample competition benchmarks where each problem represents ~0.5–1% of accuracy.

### Minor

- **DAPO absent from experimental comparison.** DAPO is prominently discussed in related work (Section 5) as directly addressing reward sparsity via dynamic sampling. The paper explains that GHPO is more data-efficient than DAPO (which discards hard/easy problems), but this argument is not empirically tested. Even one direct comparison row would substantially clarify where GHPO sits in the landscape.

- **GPQA-Diamond gain from math training is unexplained.** GHPO achieves ~8.6% absolute improvement on GPQA-Diamond (30.8% → 39.4%, Table 1) — a science reasoning benchmark — from math-only training. Whether this gain is attributable to GHPO's mechanism or is incidental to training dynamics is not discussed.

- **All-zero-reward difficulty threshold is unjustified.** Section 3.3 defines difficulty as "all G individual rewards are zero." This misses queries where 1/G responses is correct but the model consistently struggles. The asymmetric DAPO criterion (filter pass rates of 0 or 1) is more principled, but the paper does not discuss the tradeoffs of the all-zero threshold or what occurs at the boundary (e.g., 1/G correct).

### Trivial

- **Response length as "sophisticated reasoning" proxy.** Section 4.4 interprets GHPO's longer mean response lengths as evidence of "more detailed and elaborate reasoning processes." An equally valid explanation is that hint-conditioned training exposes the model to long ground-truth solution traces, directly inflating generation length as a stylistic artifact rather than a capability improvement.

---

## Nice-to-Haves

- A compute-matched ablation (e.g., halving G for hint-guided steps or running GRPO with 1.6× budget) would directly validate the efficiency argument.
- A three-condition experiment — GRPO w/o hint, GHPO w/o hint at inference, GHPO with hint at inference — would reveal whether the policy is learning transferable reasoning or merely adapting to the hint-augmented format.
- Multi-seed reporting (3 seeds minimum) for Tables 1 and 2 would confirm robustness of the headline gains, particularly on AIME2024 and GPQA-Diamond.
- An ablation over fixed ω vs. the multi-stage adaptive schedule (deferred to Appendix B.3) would validate the "multi-stage" component as a distinct contribution.
- A cold-start ablation (N=0 vs. N=20 steps) would confirm the strategy is necessary.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic §Sec. 3.2 — missing hint-ratio details in main text**: The paper explicitly says details are in Appendix B.2–B.3. Per the rules, appendices exist in the original submission; this is not a weakness.
- **Harsh critic — LUFFY absent from comparison**: The paper directly acknowledges LUFFY's cost disadvantage (requires auxiliary LLM) in Section 1, providing a reasonable justification. The absence is discussed, not silently omitted; this reduces the criticism to Nice-to-Have.
- **Harsh critic — cold-start makes early GRPO comparison non-trivial**: Running 20 GRPO warm-up steps before enabling GHPO is an engineering choice disclosed in Section 3.5. It is not experimentally deceptive; any difference in early training is downstream of the methodology, not hidden. Moved to Nice-to-Have.
- **Strength finder — "scalable and practical approach"**: Generic framing without specific evidence; absorbed into the verified concrete strengths above.

---

## Novel Insights

GHPO's central empirical finding — that ~60% of training problems remain "difficult" for the model even deep into RLVR training (Figure 3) — is itself a notable observation about the persistent capacity-difficulty mismatch during on-policy LLM RL, beyond what is typically documented. The method's demonstration that adaptive, *online* difficulty-gated imitation outperforms *offline* curriculum scheduling (Table 2: GHPO 0.442 > GRPO-CL-H(0.5) 0.422) concretely quantifies the value of dynamic as opposed to static guidance. The key open question the paper raises but does not resolve — how hint-conditioned policy updates generalize to unconditional inference — is a genuinely interesting mechanistic puzzle for follow-up work.

---

## Suggestions

1. **Compute analysis**: Add a Table/Figure comparing total GPU-hours (or token budgets) for GHPO vs. GRPO for the same number of optimization steps, and consider reporting a compute-matched variant.
2. **Seed variance**: Report mean ± std across ≥3 seeds for at least the primary Table 1 and Table 2 comparison rows.
3. **Train-test hint ablation**: Add a single experiment evaluating the GHPO-trained checkpoint with hints at inference time to isolate whether the gain comes from unconditional generalization or hint-conditioned adaptation.
4. **Difficulty threshold ablation**: Include a small ablation varying the difficulty detection threshold (all-zero, ≤1/G, ≤2/G correct) to empirically justify the all-zero design choice.
5. **GPQA-Diamond discussion**: Briefly contextualize the ~9-point science benchmark improvement from math training to help readers calibrate how much is attributable to GHPO vs. general reasoning transfer.

---

## Score and Decision

**Originality**: The core idea — online difficulty detection + conditional hint injection within GRPO — is a sensible and implementable combination of existing concepts (DAPO's filtering, imitation learning) rather than a fundamentally novel mechanism. The adaptive, multi-stage guidance schedule adds a degree of novelty. (3/5)

**Importance of research question**: Reward sparsity in RLVR is a well-identified, practically significant challenge, especially for smaller LLMs. The problem is genuinely important. (4/5)

**Claims supported**: The performance gains are real and consistent, but the efficiency framing is partially unsupported due to the unacknowledged compute overhead. Single-run results on high-variance benchmarks leave some uncertainty. (3/5)

**Soundness**: The methodology is reasonable and clearly motivated, but the train-test distribution shift goes unanalyzed and no seed variance is reported. (3/5)

**Clarity**: The paper is generally well-written and the motivation is clear. Key algorithmic details (hint extraction, ω schedule) are deferred to the appendix. (3/5)

**Community value**: Provides a practical improvement over GRPO with replicable gains across two model families and two datasets. The code-light nature of the approach (no auxiliary models) is useful for the practitioner community. (4/5)

Overall, GHPO is a solid empirical paper with genuine and consistent improvements over GRPO, but falls short of strong acceptance due to the uncontrolled compute overhead, absence of seed variance, and unexplained mechanism for hint-conditioned generalization. It sits in borderline territory.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>