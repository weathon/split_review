Now I have all the information I need. Let me compile the final consolidated review.

**Calibration Anchor List:**

*Round 1 - Topic low (<3.5):* cya3eEczAx (1.67) - P+O optimizer with flawed proofs, much weaker than Ano; MpA6HMD7Wq (3.00) - learned optimization, different scope; YGWGhdik6O (3.00) - optimizer search, different scope.

*Round 1 - Topic mid (3.5-7.5):* GGZISiwgNt (5.57) - non-stationary RL policy gradient, different framing; ZJ9LglIakj (5.25) - constrained MDPs; LWuYsSD94h (6.00) - multi-agent RL.

*Round 1 - Topic high (>7.5):* l6QnSQizmN (7.25) - online RL, much stronger paper overall; 5t57omGVMw (8.00) - linear systems solver selection.

*Round 1 - Weakness queries:* FZa1UCC9SC (5.00, signSGD risk curves) - theoretical analysis without strong experiments; JslyktsKMY (5.75, theory-practice gap) - directly discusses the theory-practice mismatch issue; cCcaJzPAnb (3.80, concavity-aware optimizer) - overclaimed theory without practical viability; 1NYhrZynvC (2.50, adaptive stepsize) - fundamentally flawed theory; CYa4FKjYM9 (6.00, optimizer stability) - closer optimizer paper, less empirical breadth than Ano; zCZnEXF3bN (6.00, double momentum - accepted) - novel gradient estimator with strong theory, comparable quality.

*Round 2:* TBJCtWTvXJ (6.20, SoftSignSGD - rejected) - new optimizer with theory + experiments across CV/NLP, most directly comparable to Ano; CIqjp9yTDq (6.25, heavy ball - accepted) - focused theoretical analysis; tznvtmSEiN (6.67, momentum frequency - accepted) - theoretical analysis with moderate experiments; nuX2yPejiL (7.00, Polyak step-sizes - accepted) - stronger theory and experiments; ww3CLRhF1v (7.00, adaptive methods SDEs - accepted) - deeper theoretical treatment with cleaner writing.

**Round-1 Bracket:** The weakest comparable papers (signSGD at 5.0, optimizer stability at 6.0, SoftSignSGD at 6.2) suggest a bracket of [5.0, 6.5]. The low-band topic anchors are irrelevant (different subfields). The weakness-anchored papers (theory-practice mismatch at 5.75, optimizer papers at 5.0-6.2) reinforce this bracket.

**What the low-band anchors failed at:** The signSGD paper (5.0) lacked strong empirical validation across domains; the theory-practice gap paper (5.75) was a critique of the field, not a method; the stability optimizer paper (6.0) had narrower evaluation. Ano does NOT share these failures: it has strong empirical validation especially in RL, it proposes a concrete method with theory, and its evaluation is broad. However, Ano does share the theory-practice schedule mismatch that JslyktsKMY (5.75) critiques — the theory uses β₁,k = 1 - 1/√k while the evaluated algorithm uses fixed β₁ = 0.92. This is a real gap, and the score must reflect it.

**Round 2 narrowing:** Comparing to SoftSignSGD (6.20, rejected): Ano has stronger RL validation but weaker CV/NLP scaling, and more presentation issues. Compared to Double Momentum (6.00, accepted): Ano has broader empirical coverage but less polished theory-practice alignment. Final score: 6.0.

---

## Summary

This paper proposes Ano, an optimizer that decouples update direction (momentum sign) from step magnitude (instantaneous gradient norm) to improve robustness in noisy and non-stationary optimization landscapes. A variant called Anolog uses a logarithmic momentum schedule to reduce hyperparameter sensitivity. The paper provides non-convex convergence guarantees (Õ(K^{-1/4}) rate matching sign-based methods) and evaluates across CV (CIFAR-100), NLP (GLUE), and deep reinforcement learning (MuJoCo SAC, Atari PPO).

## Strengths

1. **Strong and consistent gains in reinforcement learning, the paper's target regime.** In MuJoCo SAC (Table 4), Ano achieves the best mean rank (1.6) and normalized average score (99.16) across 5 environments, improving over Adam by ~9% and Lion by ~18% in normalized score. Figure 2 shows Ano reaching Adam's final performance with 50–70% fewer training steps. In Atari PPO (Table 5), Ano again obtains the best mean rank (1.8) with ~6–7% improvement over RMSprop. These results directly validate the central design claim in the intended high-variance, non-stationary regime.

2. **Controlled noise-robustness experiment shows the decoupling benefit clearly.** Section 5.2 (Table 1) injects Gaussian noise into CIFAR-10 gradients and shows Ano's advantage widening with noise level: at σ=0.20, Ano achieves 59.54% vs Adam's 52.46% (7.08pp gap) and Lion's 56.82% (2.72pp gap). This provides direct causal evidence that the decoupled design stabilizes learning under high gradient variance.

3. **Theoretical convergence guarantee for the decoupled update structure.** Section 5.1 derives a Õ(K^{-1/4}) non-convex convergence rate under standard assumptions (L-smoothness, bounded variance, unbiased gradients), matching the rates of established sign-based methods (Lion, Signum). This provides formal backing that the decoupled sign-magnitude design does not sacrifice convergence guarantees.

4. **Comprehensive evaluation across domains confirms no degradation in stable settings.** On CIFAR-100 (Table 2) and GLUE (Table 3), Ano matches or slightly exceeds strong baselines (Adam, Adan, Lion, Grams), demonstrating that the RL gains do not come at the cost of poor behavior in low-noise supervised tasks.

## Weaknesses

### Major

1. **Inconsistency between the update rule in the algorithm box and the text description.** The text in §3 (Sign-Magnitude Decoupling) explicitly states the update uses |g_k|·sign(m_k) — the magnitude is the instantaneous gradient norm. However, Algorithm 1 writes g_k·sign(m_k) instead. These are not equivalent: g_k·sign(m_k) = sign(g_k)·|g_k|·sign(m_k), which differs from |g_k|·sign(m_k) when sign(g_k) ≠ sign(m_k). The text description and design motivation consistently describe the |g_k|·sign(m_k) version, so this is most likely a typo in the algorithm box, but it creates genuine ambiguity about what was actually implemented. The authors must clarify which update was used in experiments and correct the inconsistency.

2. **Theory does not cover the empirically evaluated algorithm.** The convergence analysis (§5.1) assumes a scheduled momentum coefficient β_{1,k} = 1 - 1/√k and learning rate decay η_k = η/k^{3/4}. The core Ano algorithm (§3) uses a fixed β₁ = 0.92 and domain-typical schedules (constant/cosine) in experiments. The Anolog variant uses a logarithmic schedule, not the square-root schedule from the theory. While this kind of gap is common in optimization papers, the paper would be stronger if it either analyzed the practical algorithm or evaluated the theoretically analyzed variant.

### Minor

3. **Second-moment update can technically produce negative values.** The variance update v_k = β₂ v_{k-1} - (1-β₂)·sign(v_{k-1} - g_k²)·g_k² can theoretically become negative when a large gradient follows a period of small gradients, because the subtraction (1-β₂)·g_k² could exceed β₂·v_{k-1}. With β₂=0.99, this requires g_k² > 99·v_{k-1}, which is unlikely in practice but not impossible at initialization or during gradient spikes. The paper neither discusses this possibility nor describes any safeguards (clipping, absolute value, etc.). The authors should either prove positivity or describe the mitigation.

4. **Duplicate "Adam" entries in GLUE results (Table 3).** In both the Default and Tuned blocks of Table 3, there are two rows labeled "Adam" with different scores. Based on the experimental design (§6.2) and the presence of Adan in Table 2, the second "Adam" entry in each block is almost certainly meant to be "Adan." This needs correction.

5. **Ablation table column headers are underspecified (Table 6).** The columns "Grad. Norm.", "Mom. Norm.", "Mom. Dir.", "Decoup. WD" use checkmarks to indicate which components are active, but the mapping between these columns and the actual optimizer design choices is not explained. For instance, the "Adam" row has checkmarks in all four columns, which is confusing because standard Adam does not use decoupled weight decay (that is AdamW) and does not use gradient norm for scaling. A clarifying caption or footnote is needed.

### Trivial

6. The hardware specification ("RTX 5090, CUDA 12.9, PyTorch 2.9.0") is plausible as of the current date (May 2026) and not an error — remove this concern.

7. Some entries in the Anolog ablation (Table 6, "Ano √k") show negative DRL scores (-221.45) and near-random classification accuracy, indicating the square-root schedule collapses completely. While this supports the logarithmic schedule choice, the paper could briefly explain why the theoretically motivated schedule fails so dramatically in practice.

## Nice-to-Haves

- **Wall-clock runtime comparison.** The title says "Faster is Better" but the paper only shows sample efficiency (steps to convergence), not runtime per step. A wall-clock comparison would strengthen the title claim.
- **Larger-scale experiments.** The paper acknowledges this limitation (§8), but assessing Ano on larger models (e.g., ImageNet-scale vision, LLM fine-tuning) would broaden the contribution's significance.
- **Additional noisy supervised benchmarks.** The noise robustness experiments (Table 1) are convincing but limited to injected Gaussian noise on CIFAR-10. Adding CIFAR-100 with label noise or other natural noise sources would strengthen the evidence.

## Removed Points

- **Criticism about hardware specs being "not yet released"** (harsh critic #10): Removed because RTX 5090, CUDA 12.9, and PyTorch 2.9.0 are all plausible as of May 2026. The reviewer's comment was based on an incorrect temporal assumption.
- **Criticism about missing comparison to Sophia/MARS** (harsh critic): Removed per hard rule — missing related works cannot be flagged as a weakness without external confirmation of their existence.
- **Criticism about theory not covering Ano being "fundamental"** (harsh critic #3): Demoted from Critical to Major. While the theory-practice schedule gap is real, it does not invalidate the theoretical contribution — many optimization papers prove guarantees under schedules that differ from practical use. The paper also contains Anolog (time-varying β₁) which partially bridges the gap.
- **Criticism about ablation table being "largely uninterpretable"** (harsh critic #4): Demoted from Critical to Minor. The table is interpretable with context, though the column headers are underspecified.
- **Criticism about Anolog underperformance being insufficiently discussed** (harsh critic): Partially addressed — the paper acknowledges Anolog's "slightly lower peak performance" (§4). The gap is indeed notable (64.84 vs 70.31 on CIFAR-100) and could use more discussion, but the paper does acknowledge it.

## Novel Insights

The harsh critic's observation that g_k·sign(m_k) ≠ |g_k|·sign(m_k) is a genuinely important catch — it reveals an ambiguity in the algorithm specification that could affect how readers interpret the decoupling claim. Beyond this, the strengths identified (strong RL gains, noise robustness validation) align well with the paper's own claims. The theory-practice schedule mismatch observation is standard in optimization paper reviews but worth noting.

## Suggestions

1. **Correct the algorithm box** to show |g_k|·sign(m_k) (or confirm g_k·sign(m_k) is what was implemented and explain the discrepancy).
2. **Discuss the v_k positivity issue** — either prove v_k stays positive given β₂=0.99, describe a clipping mechanism, or acknowledge the edge case.
3. **Align theory closer to practice** — either analyze Ano with fixed β₁ under a different set of assumptions, or run experiments with the β_{1,k}=1-1/√k schedule used in the theory and compare performance.
4. **Fix the duplicate "Adam" entries** in Table 3 (second entry should be "Adan").
5. **Add a footnote to Table 6** explaining what each column header means and how checkmarks should be interpreted.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>