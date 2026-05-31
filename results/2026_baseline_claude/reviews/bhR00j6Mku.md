## Summary

This paper presents the first systematic study of benchmark contamination detection fragility in Large Reasoning Models (LRMs). It identifies two practical scenarios where contamination evades detection: (1) Stage I, where SFT contamination in a base model transitioning to an LRM via RL is initially detectable but becomes concealed after even brief GRPO training, and (2) Stage II, where contamination with chain-of-thought (CoT) applied to advanced LRMs as a final SFT step leaves virtually no detectable signal. The paper provides empirical evidence across 10 detection methods and 6 benchmarks, paired with a theoretical analysis attributing concealment to PPO-style importance sampling/clipping.

---

## Strengths

- **Timely, high-impact problem with comprehensive experimental coverage.** The paper evaluates 10 representative detection methods spanning generation-based, perturbation-based, reference-based, and reference-free families across 6 hard reasoning benchmarks (OlympiadBench, GPQA, AIME, Minerva, AMC), with two base models (Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) and four LRM targets. This breadth makes the findings credible and generalizable.

- **Controlled ablation rules out trivial confounders.** The paper carefully distinguishes RL-based concealment from simple "forgetting via more training." Table 3 and Figure 2 show that continued SFT on clean data does not reduce AUROC, but GRPO does—and AUROC decays monotonically with GRPO steps. This isolates the algorithmic effect cleanly.

- **The theoretical analysis is mechanistically precise.** Theorem 3.1 decomposes the NLL drift into a mean term and an importance-sampling/clipping covariance term, and traces contamination concealment specifically to the clipping-induced compression of the covariance gap between members and non-members. The ablation in Table 3 directly validates this: removing clipping from GRPO or RAFT++ largely restores AUROC, while plain RAFT (no clipping) leaves detection intact.

- **Key insight about LRM generalization undermines the memorization assumption.** Figure 4 and the associated analysis show that after CoT contamination on LRMs, log-probability distributions of members *and* non-members shift upward together by similar margins. This empirically grounds the claim that LRMs generalize reasoning patterns to distributionally similar unseen samples, rendering memorization-based detectors ineffective—a non-obvious and important finding.

- **Two-stage framing is clear and actionable.** Distinguishing Stage I (base→LRM transition) from Stage II (final SFT on an already-capable LRM) cleanly identifies two distinct real-world threat models. The resulting recommendations (release intermediate checkpoints; move beyond memorization-based detection) are concrete and appropriate.

---

## Weaknesses

### Fatal
None. The core claims are empirically supported and the theory aligns with experimental findings.

### Major

1. **LiRA performance in Stage II is not near-random.** The paper repeatedly states that all detection methods "perform near random guesses" in Stage II, but LiRA achieves 61.34% (DS Llama-8B), 62.74% (OpenThink-7B), and 65.55% (DS Qwen-14B) AUROC—meaningfully above random, especially for the 14B model. Treating LiRA as failing equally to the others is a notable overstatement. The paper should acknowledge LiRA as a relative bright spot in Stage II and discuss why it partially survives.

2. **Why does RL contamination fail to inflate performance (Table 1)?** Table 1 shows that using benchmark questions during RL training (with rewards from generated responses) provides negligible performance gain over clean RL. The paper attributes contamination inflation primarily to SFT, but does not explain this RL result in depth. A reader might wonder whether RL contamination is simply ineffective because the benchmark distribution is already well-covered, or whether the training setup suppresses it. This gap weakens the interpretation of Stage I.

3. **The "broad class of RL methods" claim outpaces the evidence.** The paper argues that any PPO-style method with clipping will exhibit concealment, but only GRPO and RAFT++ are tested empirically. Other popular methods (e.g., DAPO, Dr. GRPO, ReMax) are not evaluated. The theoretical argument is suggestive but relies on a tabular, simplified advantage setting. Softening this claim or adding even one additional RL variant would strengthen it considerably.

### Minor

1. **Theoretical analysis makes strong simplifying assumptions.** The proof operates in a tabular MDP with a simplified advantage (no standard-deviation normalization), and the analysis of GRPO reduces to an idealized form. The connection to actual GRPO is argued informally. This is not fatal—the empirical ablation validates the mechanism—but the limitations of the theory should be stated more explicitly.

2. **No discussion of detection methods that bypass log-probability.** The paper evaluates only methods grounded in token-level statistics. Behavioral methods (e.g., exact answer memorization probing, rephrased question consistency tests, timing/token-length anomalies) are not covered. Even a brief remark on why these would or would not work under the two-stage framework would be valuable.

### Trivial

- The AUROC claim "performing close to random guessing" is stated inconsistently across tables and text; some configurations reach 65–75% AUROC, which warrants qualified language.

---

## Nice-to-Haves

- An experiment probing whether behavioral detection methods (e.g., identical-answer reproduction under re-phrasing) survive Stage II contamination, given that log-prob-based methods fail.
- A brief experiment with at least one other clipping-based RL algorithm (e.g., DAPO) to strengthen the "broad class" claim.
- Explicit quantification of how much contamination inflation is preserved after GRPO concealment (currently only shown aggregated in Tab. 1), alongside a direct AUROC comparison at equivalent performance levels.

---

## Novel Insights

The most substantive novel finding is the mechanistic identification of PPO-style clipping as an unintended contamination concealer. The decomposition in Theorem 3.1 shows that clipping selectively damps high-variance trajectories from non-members (which exhibit more extreme successes under contaminated models), thereby compressing the log-probability gap that all major detectors rely on. This has a clean algebraic consequence: RAFT (no clipping) cannot conceal contamination, while RAFT++ and GRPO (with clipping) can—validated cleanly in Table 3. This is an algorithmic insight with implications beyond contamination: it suggests that RL stabilization mechanisms systematically alter the membership footprint in model weights in ways that were not previously recognized. The second key insight—that LRMs' strong CoT generalization causes distributional neighbors of contaminated members to achieve similar log-probability, confounding the member/non-member signal—is a compelling explanation for Stage II failure and challenges the foundational assumption of memorization-centric contamination detection.

---

## Suggestions

- Requalify the Stage II conclusion to acknowledge LiRA's partial effectiveness (especially for the 14B model), and discuss what about LiRA's design provides even limited signal.
- Add a paragraph explaining why RL contamination (benchmark questions used as RL prompts) produces minimal performance inflation, since this is empirically shown in Table 1 but not well-explained.
- Add at least one additional RL algorithm to the ablation (Table 3) to substantiate the "broad class" claim.
- Make explicit in the theory section the gap between the tabular idealization and actual GRPO, and note how the empirical ablation bridges that gap.

---

## Score and Decision

The paper addresses a genuinely important and timely problem, provides both rigorous empirical evaluation and a clean theoretical mechanism, and delivers findings with direct practical consequence for the research community. The main limitations are an overstatement of Stage II failure rates (LiRA partially survives), a gap in explaining the RL contamination null result, and extrapolation of the "broad class" claim beyond the tested methods. None of these are fatal. The contribution merits acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>