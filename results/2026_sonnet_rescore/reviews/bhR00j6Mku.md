Now I have everything I need to write the final review. Let me synthesize the inputs against the paper content.

---

## Summary

This paper presents the first systematic study of benchmark contamination detection in Large Reasoning Models (LRMs), structured around two practical contamination scenarios. Stage I shows that SFT contamination is initially detectable but can be concealed by subsequent GRPO (or RAFT++)-style RL training, with an empirically-validated theoretical explanation tracing the effect to PPO-style importance sampling and clipping. Stage II shows that extensive SFT contamination with CoT applied directly to advanced LRMs leaves almost no signal for any of 10 evaluated detection methods, because LRM generalization causes both members and non-members to shift together in log-probability space.

---

## Strengths

- **GRPO's concealment effect is causally isolated.** Figure 2 shows a monotonic decline in AUROC with more GRPO steps, while continuing SFT on the same contaminated model does not degrade detection. This rules out "more training = forgetting" and points squarely at the RL objective.

- **Clean ablation of the clipping mechanism (Table 3).** RAFT leaves the Loss detector essentially unchanged (77.51% AUROC, +2.03 vs. baseline). RAFT++ with clipping drops it to 57.58% (−17.91). Removing clipping from RAFT++ restores it to 74.39% (−1.09). The same pattern holds for GRPO (73.28% without clipping vs. 61.26% with). This is an unusually clean mechanism isolation and directly validates Theorem 3.1's decomposition.

- **Theorem 3.1 provides a useful organizing decomposition.** The NLL drift is decomposed into a mean term µ(x) and a covariance term β(x). For RAFT the cancellation is shown formally; for RAFT++ the sign change in the covariance term is traced analytically to the clipping gate. Even where the GRPO case is argued informally, the decomposition gives practitioners a precise target for designing clipping-resistant detectors.

- **Stage II diagnosis: generalization, not memorization, is the failure mode.** Figure 4 shows that for clean LRMs the member/non-member AUROC is already approximately 50% (R1 Distill LLaMA clean: 0.497; R1 Distill Qwen clean: 0.479). After extensive contamination, both member and non-member log-probabilities rise at similar margins, confirming the paper's explanation that LRMs internalize knowledge rather than memorize sequences.

- **Comprehensive evaluation across diverse baselines.** 10 detection methods spanning 5 methodological categories, 6 reasoning benchmarks, 2 base models (Stage I), 4 advanced LRMs (Stage II).

---

## Weaknesses

### Fatal
None.

### Major

- **The Stage I claim of "consistent decrease across all detection methods" is overstated for methods already at random-guessing.** In Table 2 (Qwen2.5-7B-Instruct), Verbatim starts at 52.76%, Neighbor at 50.71%, and Min-K%++ at 49.61% — all essentially at chance before RL. For these methods, the reported "decreases" (−0.60, −0.28, −6.02 pts) are either trivially small or already in the noise floor. The genuine concealment effect is concentrated on LiRA (−9 to −14 pts), Min-K% (−14 to −16 pts), Max-K% (−17 to −20 pts), and Loss (−14 to −17 pts). The paper should distinguish between methods for which concealment is material versus those that were never effective to begin with, to avoid overclaiming breadth.

### Minor

- **The GRPO step in the theoretical analysis is argued informally.** Theorem 3.1 and the RAFT/RAFT++ cases are worked out explicitly. But for GRPO the paper states: "By similar argument, we know that the μ term does not contribute significantly to the concealment. The covariance term can be analyzed similarly…" (Section 3.2). This step is asserted rather than derived, and the formal closure that is provided for RAFT++ does not carry over automatically to GRPO's more complex advantage structure. The theory is still useful as an organizing framework, and Table 3 provides strong empirical support; but the paper should clearly state that the GRPO case is empirically confirmed rather than fully proved.

- **The extrapolation beyond 156 training steps is speculative.** The text reads: "we expect that extensive GRPO training would render all existing detection methods to near-random performance eventually" (Section 3.1). At 156 steps, Loss/Min-K/Max-K have already fallen below 50%, but LiRA remains at 80.14%. The paper presents a clear monotonic trend in Figure 2 that supports the direction of the claim, but the endpoint is a projection. The caveat "we expect" is present but could be made more prominent.

- **Table 1 shows that SFT-only contamination (no RL) yields the best benchmark inflation for Qwen2.5-7B (47.23% avg. vs. 45.55% with RL), yet the Stage I threat model assumes RL is applied.** The paper briefly notes that RL contamination adds no measurable gain over clean RL, but does not address why a developer who wants to maximize inflation while still deploying an LRM might have less incentive to run RL on top of contaminated SFT. The paper's Stage I finding remains important (developers *do* run RL for capability reasons), but the implicit assumption deserves a sentence of explicit justification.

- **Stage II framing blurs "active concealment" and "fundamental infeasibility."** Throughout Section 4, contamination with CoT on advanced LRMs is characterized as leaving "little detectable evidence," but Figure 4 makes clear the mechanism is *distributional generalization*, not developer strategy. The Discussion does acknowledge this, but the body text and conclusion continue to use framing that implies the developer is concealing something, when the more precise statement is that memorization-based detection paradigms are inapplicable to LRMs regardless of developer intent. Separating these two framings would sharpen the paper's actionable conclusion.

### Trivial
None beyond what's noted above.

---

## Nice-to-Haves

- A brief mention in the main text (not just Appendix E.2) motivating the 8-rollout averaging choice for detection scores, particularly for generation-based methods where verbatim repetition may appear in only a subset of rollouts.
- For Stage II, exploring whether AUROC separates as the contamination fraction decreases (e.g., 25% vs. 50% vs. 100% member contamination) would test whether detection is absolutely infeasible or a function of contamination density.
- Extending GRPO training beyond 156 steps on at least one detector/benchmark to confirm the projected convergence to random guessing, rather than relying on extrapolation.
- A brief sketch in the Conclusion of what properties a detector would need to resist both Stage I (clipping-induced convergence) and Stage II (generalization-induced baseline shift) failure modes.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Missing clean-model AUROC baselines — Stage II claim may not hold."** Figure 4 directly reports clean-model AUROC values for both LRMs used in the density plot analysis (0.497 and 0.479, essentially 50%). This substantially addresses the concern. Retained as a minor note only for Stage I, where such a baseline is implicitly present in the before-RL values in Table 2.

- **Strength Finder: "Comprehensive evaluation design" as a standalone strength.** Retained only in service of concrete evidential points (breadth of Table 2 and Table 5 supporting the main claims). Generic comprehensiveness is not a stand-alone strength.

- **Strength Finder: "This paper addresses an important problem."** Generic; removed per filtering rules.

---

## Novel Insights

The paper's most novel observation is that the clipping gate in PPO-style algorithms — typically treated as a training-stability device — mechanically induces membership-inference evasion as a side effect, because it preferentially damps the high-variance, high-loss correct trajectories that occur on non-member samples, compressing the member/non-member NLL gap. The RAFT → RAFT++ ablation (Table 3) is a uniquely clean demonstration of this: the only difference between the two algorithms is the addition of importance sampling/clipping, and that single change swings AUROC from 77.51% to 57.58%. This result carries implications beyond contamination: it suggests that any audit procedure relying on log-probability separation between seen and unseen data will degrade after PPO-style training, regardless of whether contamination is intentional.

---

## Suggestions

1. In Table 2's summary claims, explicitly restrict "consistent decrease" to the subset of methods that had signal above random (LiRA, Min-K%, Max-K%, Loss, Ref, Zlib) rather than all 10.
2. In Section 3.2, mark the GRPO derivation clearly as "by analogy, empirically confirmed in Table 3" rather than implying full analytical closure.
3. In Section 4, add a single paragraph explicitly contrasting "developer-active concealment" (Stage I) versus "detector-paradigm breakdown due to LRM generalization" (Stage II), so the two stages have cleanly different policy implications.
4. In Table 1, add one sentence explaining why the Stage I threat model includes RL even though SFT-only achieves peak contamination inflation for Qwen — e.g., that RL is necessary for deploying a competitive LRM, so developers cannot simply skip it.

---

## Assessment Across Axes

**Originality:** The two-stage framing and the mechanism-level attribution to PPO clipping are novel. The problem itself (contamination detection) is not new, but this study's angle — focusing specifically on the LRM training pipeline and isolating the algorithmic component responsible — is original and insightful.

**Importance of research question:** Very high. Leaderboard contamination in LRMs is an active and practical concern; the finding that RL training inherently degrades detection (even when applied on clean data) and that CoT-based contamination leaves no detectable trace is directly actionable for the evaluation community.

**Whether claims are well supported:** Mostly well-supported. The Stage I concealment mechanism is backed by solid ablations. The Stage II finding is backed by consistent near-random AUROC across 40 model–detector combinations. Some Stage I claims are slightly overstated (the "all methods" framing for methods already at chance). The GRPO theoretical case has an informal step.

**Soundness of experiments:** Strong. The controlled comparison of RAFT / RAFT++ / GRPO with and without clipping is particularly rigorous. The use of 8 rollouts and averaging across benchmarks is reasonable, if underdescribed in the main text.

**Clarity of writing:** Good. The two-stage structure is clear and the figures map well onto the claims.

**Value to research community:** High. This paper should redirect contamination detection research away from memorization-based assumptions and toward approaches tailored to LRM generalization, and it provides a concrete algorithmic target (PPO clipping) for future work.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>5</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>5</community_value>
</subscores>