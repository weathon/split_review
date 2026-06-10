## Summary

This paper analyzes the origins of the self-play to cross-play (SP-XP) performance gap in the Overcooked benchmark and argues it is primarily driven by poor state coverage rather than genuine coordination challenges. Through a state augmentation mechanism that exposes agents during self-play training to states from partner interactions, the authors nearly close the SP-XP gap across all Overcooked layouts. To address Overcooked's limitations, they introduce OvercookedV2 — a new environment adding partial observability, asymmetric information, stochasticity, and three handcrafted layout classes targeting distinct coordination challenges (Grounded Coordination, Test-Time Protocol Formation, Demo Cook).

## Strengths

- **Causal evidence that Overcooked's SP-XP gap is primarily a state-coverage problem**: Section 5.2 (Table 1) shows that a state augmentation mechanism — exposing agents during self-play to states they might encounter in cross-play — nearly closes the SP-XP gap across all original Overcooked layouts. In the Counter Circuit layout, average XP scores reach 140 with no total failures, versus many zero-score pairings in standard self-play. Because agents train independently (no shared conventions), this is causal evidence that state coverage, not coordination incompatibility, drives the gap.

- **Contrastive validation that OvercookedV2 introduces genuine coordination challenges**: Table 2 directly benchmarks the same state-augmented training on OvercookedV2 and shows it does NOT close the SP-XP gap. SP scores remain high in OvercookedV2, so agents master the perceptual/representational demands; the failure is specifically in cross-play. This contrast between Table 1 and Table 2 is the cleanest evidence that OvercookedV2 requires coordination beyond mere state generalization.

- **Three handcrafted layout classes that probe distinct, previously-unaddressed ZSC challenges**: Section 6.3 introduces Grounded Coordination (extending the Cat-Dog problem into a temporally extended layout), Test-Time Protocol Formation (requiring agents to form protocols at test time from delivery feedback alone), and Demo Cook (requiring implicit communication through action interpretation). The Test-Time Protocol layouts are particularly noteworthy: even Other-Play produces large SP-XP gaps there, confirming a genuinely new and unsolved challenge.

- **Principled theoretical grounding via Dec-POMDP analysis**: Section 3 grounds the critique in the Dec-POMDP formalism, arguing from Ellis et al. (2023) that deterministic, fully observable environments admit open-loop policies that render partial observability irrelevant. This provides a formal basis for why Overcooked is inadequate as a ZSC benchmark, going beyond empirical results.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient baseline evaluation to support claims about OvercookedV2's hardness.** The paper's central claim about OvercookedV2 is that it "presents a hard ZSC challenge" and "none of the evaluated methods solve successfully." But only three methods are benchmarked: standard self-play PPO, state-augmented PPO, and other-play (Hu et al., 2021b). Of these, only Other-Play is a ZSC-specific method. No FCP (cross-play training), no MEP, no population-play, no diversity-enforcing methods are tested. For a benchmark paper whose main rationale is that existing benchmarks are inadequate and a new one is needed, the validation must show that the field's existing arsenal of ZSC methods — not just one — fails on the new scenarios. If Other-Play partially improves XP scores while leaving a gap, the reader cannot tell whether the remaining gap is intrinsic to OvercookedV2 or specific to Other-Play's known limitations (requiring a priori specification of symmetries, which the paper acknowledges). This directly limits confidence in the paper's headline claims about OvercookedV2. *(Verified: Section 7 tests only self-play PPO, state-augmented PPO, and Other-Play; Section 7, final paragraph: "Overall, OvercookedV2 presents a challenging ZSC environment that none of the evaluated methods solve successfully.")*

### Minor

- **Coordination difficulty is not fully disentangled from perceptual/representational difficulty.** OvercookedV2 introduces partial observability (view radius), dynamic recipes, multiple ingredients, and stochasticity. The original Carroll et al. architecture "did not learn under the additional complexity" (Section 7), necessitating three added 1×1 convolutions plus a recurrent layer. While the high SP scores in OvercookedV2 (Table 2 caption: "Both self-play and state augmented agents perform well in SP") mitigate this concern — agents do master the perceptual task — the paper lacks a control experiment isolating coordination from perception (e.g., a fully-observable variant to check whether the XP gap shrinks when the perceptual burden is removed). This makes it harder to attribute the XP failures specifically to coordination.

- **The claim that Overcooked is "not suitable" as a ZSC benchmark is stronger than the evidence warrants.** The abstract states "The Overcooked environment is therefore not suitable as a ZSC benchmark" and Section 1 says "Overcooked is therefore inadequate for benchmarking ZSC algorithms." The evidence shows the SP-XP gap can be substantially closed through better state coverage. Many useful benchmarks have properties that allow special-purpose methods to close gaps — that does not make them "unsuitable" for all use. A more precise conclusion — that Overcooked tests generalization more than coordination, so ZSC results must be interpreted with this in mind — would be better aligned with the evidence.

- **Insufficient reproducibility details.** The state augmentation algorithm (Section 5.1) leaves key parameters unspecified: the number of rollout episodes *r* per pairing, the size of the state buffer, and how initial policies (before the first iteration) are obtained. The OvercookedV2 experimental setup (Section 7) describes the architecture only as "adding three 1×1 convolutions" and "a recurrent layer" with no hyperparameters, training lengths, optimizer settings, or architectural specifics. These gaps make it difficult to reproduce the analysis or build on the benchmark.

### Trivial
- The Button Game example (Section 4, Figures 2–3) serves its motivational purpose but the reasoning is slightly imprecise: SP agents fail because they overfit to specific bulb IDs rather than learning the parity rule — the example illustrates state coverage, not a clean logical argument about coordination vs. generalization.

## Nice-to-Haves
- Adding a human baseline or simple scripted/heuristic policy for OvercookedV2 layouts would help readers calibrate what "good" and "bad" absolute performance means, rather than relying only on relative SP-XP gaps.
- A fully-observable variant of OvercookedV2 as a control experiment would cleanly separate coordination from perceptual difficulty.
- Statistical significance testing (e.g., confidence intervals across the 10 seeds) would strengthen the quantitative claims.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Button Game example is "puzzling" (Harsh Critic)** — The critic claims Bob should learn the parity function, but this misses the paper's point: the example shows SP agents fail because they overfit to specific stimulus IDs, not because of coordination. The BR agent's success confirms the failure is about state coverage, not coordination. **Removed: misreads the example.**
- **"Human evaluation missing"** — Asking for human experiments in a benchmark introduction paper is scope creep. **Removed: outside stated scope.**
- **Table 2 is an inaccessible image** — This is a parser artifact, not the authors' fault. **Removed: parser issue.**
- **"Missing appendix/related work"** — Parser strips these; they exist in the original submission. **Removed: parser artifact.**

## Novel Insights

The merged reviews surface a nuanced tension: the paper's strongest evidence (the Table 1 vs. Table 2 contrast) and its weakest link (narrow OvercookedV2 baselines) are the same experiment. The state augmentation closing the gap in Overcooked but failing in OvercookedV2 supports the core thesis about state coverage, but the claim that OvercookedV2 is a *hard ZSC challenge* specifically requires more ZSC methods to fail on it than the paper tests. This reveals a mismatch between the strength of the paper's diagnostic contribution (strong) and its benchmarking contribution (promising but incompletely validated). A more impactful framing might split these contributions: present the Overcooked critique as the main result with thorough evidence, and offer OvercookedV2 as a community resource with preliminary validation, explicitly calling for more ZSC method evaluations.

## Suggestions
1. **Evaluate at least 2–3 additional ZSC methods (FCP, MEP, or population-play)** on OvercookedV2 layouts, particularly the Test-Time Protocol and Demo Cook layouts. This is the single highest-leverage improvement.
2. **Run a control experiment with full observability** (no view radius) on OvercookedV2 to measure whether the XP gap persists when the perceptual burden is removed. If it shrinks, attribute the residual gap more precisely.
3. **Add a simple heuristic or scripted baseline** for each OvercookedV2 layout to provide an absolute performance anchor.
4. **Specify all hyperparameters, architecture details, the value of *r* (rollout episodes), buffer size, and initial policy acquisition** for both the state augmentation experiments and OvercookedV2 experiments.
5. **Calibrate the language** about Overcooked's unsuitability — replace "not suitable" with "tests generalization more than coordination, requiring careful interpretation of ZSC results."

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>