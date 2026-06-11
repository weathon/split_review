Now I have a clear picture. Let me finalize the review.

**Round 1 bracket:** 6.0–7.5 — the paper is clearly stronger than the 4.25 anchor (Nk1MegaPuG, "Evading Data Contamination Detection") and at least comparable to the 6.75 anchors (m2NVG4Htxs "Longitudinal Perspective" and Nsms7NeU2x "How much can we Forget").

**Round 2 narrowing:** The most relevant anchors in the 6.0–6.75 range are:
- 4eJDMjYZZG (6.00): RL-evading LLM detectors — current paper is substantially more thorough and has causal evidence this one lacks.
- zWqr3MQuNs (6.25): Min-K% detection method — current paper has broader evaluation and more novel findings.
- 9QPH1YQCMn (6.25): Infilling Score — marginal improvement paper; current paper has stronger contribution.
- m2NVG4Htxs (6.75): Longitudinal contamination analysis — comparable quality; current paper has cleaner causal evidence and broader detection coverage.
- Nsms7NeU2x (6.75): Forgetting contamination — comparable; both have theory with limitations and strong empirical work.

The current paper edges ahead of the 6.75 anchors due to its causal ablation evidence (Table 3), which isolates the mechanism with rare clarity. However, the overstated "near random" claims and unverified theoretical assumptions keep it from reaching the 7.0+ tier.

**Final score:** 6.5 — Accept.

---

## Summary
This paper presents the first systematic study of whether benchmark contamination detection methods remain effective for Large Reasoning Models (LRMs). It investigates two contamination scenarios: (Stage I) SFT contamination during base-model-to-LRM conversion, where subsequent GRPO training on clean data systematically degrades AUROC across all 10 evaluated detection methods; and (Stage II) SFT contamination with chain-of-thought applied to advanced LRMs as a final training step, which inflates benchmark performance substantially while detection methods are weakened to near-chance levels. Through causal ablations (Table 3), the paper identifies PPO-style clipping — not RL training in general — as the root mechanism of concealment in Stage I, and argues that Stage II contamination evades detection because LRMs generalize reasoning capabilities rather than memorizing specific sequences.

## Strengths
- **Convincing causal isolation of clipping as the concealment mechanism (Table 3):** The paper cleanly isolates the PPO-style clipping term as the causal factor. RAFT (no clipping, rejection sampling only) preserves Loss-detector AUROC at 77.51%, while RAFT++ (same reward signal plus importance sampling and clipping) drops to 57.58%. Removing clipping from GRPO restores AUROC from 61.26% to 73.28%. This controlled comparison — where the only difference is the importance-sampling/clipping term — is the paper's strongest piece of evidence and represents a genuinely novel finding.
- **Well-controlled experimental design ruling out alternative explanations:** The paper explicitly tests and eliminates the forgetting hypothesis: (a) GRPO-trained contaminated models retain 7.14% average performance inflation over clean baselines (Table 1), and (b) further SFT on clean data does *not* conceal contamination (Fig. 2), confirming that RL specifically — not additional training per se — drives concealment.
- **Comprehensive and consistent Stage I results:** Table 2 demonstrates systematic AUROC drops after GRPO across all 10 detection methods spanning 4 methodological categories (generation-based, perturbation-based, reference-based, reference-free) and all 6 benchmarks — no cherry-picking. The dose-response relationship in Fig. 2 (monotonic decline across 64, 110, and 156 GRPO steps) strengthens the finding.
- **Practically important Stage II results:** Table 4 shows SFT contamination on advanced LRMs yields substantial performance inflation (e.g., +11.76 points for DeepSeek-R1-Distill-Llama-8B), and Table 5 demonstrates that detection methods are substantially weakened. The log-prob distribution analysis in Fig. 4 provides a plausible mechanistic explanation: both members and non-members shift upward by similar margins, suggesting the model generalizes reasoning rather than memorizing specific trajectories.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **"Near random" claims overstated relative to Stage II data:** The abstract and Section 4 claim detection methods "perform near random guesses" for Stage II, but Table 5 shows several method–model pairs achieve AUROC in the 60–65% range (e.g., Loss on DS-Llama-8B at 62.59%, LiRA on DS-Qwen-14B at 65.55%, Min-K% on DS-Llama-8B at 62.42%). These values, while substantially degraded, are not indistinguishable from random guessing. The prose should be calibrated to match the actual numbers, e.g., "substantially degraded" or "approaching random."
- **Unverified variance claims in the theoretical analysis (Section 3.2):** The theory asserts that non-member correct trajectories exhibit "much higher variance in loss and probabilities" (line 204) and that the covariance term "is much more prominent in non-members due to high variance" (lines 218–219) without measuring or reporting these quantities. These claims are not load-bearing — the empirical ablations in Table 3 independently establish the clipping mechanism — but the theory would be substantially stronger if the variance assumptions were verified.
- **Only math reasoning benchmarks evaluated:** The paper's claims about "LRMs" broadly would be strengthened by including at least one coding benchmark (e.g., LiveCodeBench), given that coding is the other primary domain where LRMs are prominent. This limits the generality of the findings somewhat.
- **Absence of variance reporting for detection metrics:** All AUROC values are point estimates. While point-estimate reporting is standard practice in this subfield, the paper makes specific claims about detection "failure" and values being "near random" that would benefit from bootstrap confidence intervals to distinguish genuine degradation from sampling noise, particularly for small Δ values (e.g., Verbatim in Table 2 dropping from 52.76% to 52.16%).

### Trivial
- Embedding-based detection methods are listed in the Related Work taxonomy (line 44) but are not included in the evaluation; the paper should either include them or briefly justify the exclusion.

## Nice-to-Haves
- The "broad class of RL methods" claim (line 33, line 255) is supported only by testing GRPO and RAFT++ (both PPO-family variants). Testing a non-PPO RL algorithm would strengthen the generalization claim.
- Extending the GRPO step-count curve beyond 156 steps to convergence would make the extrapolation claim ("would render all existing detection methods to near-random performance eventually," line 91) concrete rather than projected.
- A clearer discussion of what a realistic adversary actually does would sharpen the threat-model narrative.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic — "The theoretical analysis substitutes qualitative intuition for formal proof (structural)":** The harsh critic frames the theory as lacking rigor. While the variance claims are unverified (retained as a Minor weakness above), the harsh critic's framing that this is "structural" is too strong. Theorem 3.1 provides a principled decomposition, and the paper uses the theory to identify the mechanism — which is then verified empirically. The paper does not claim the theory proves concealment must occur. Removed the "structural"/"fatal" framing; retained only the verified portion (unverified variance assumptions) as Minor.
- **Harsh Critic — Threat model concern (developers would contaminate during RL, not SFT):** This is speculative and depends on unstated assumptions about adversary behavior. The paper explicitly tests both SFT and RL contamination (Table 1), showing RL contamination yields negligible gain — which is itself an informative finding. The Stage I pipeline is a valid contamination pathway. Removed.
- **Harsh Critic — "Detection method configuration details are in the appendix" / "extent of SFT contamination not quantified":** The paper references appendix sections (D.1, D.3, D.4, E.2) for implementation details. The appendix was stripped in the provided version. These are not paper flaws. Removed.
- **Strength Finder — "Theoretical framework that decomposes the gap-contraction mechanism":** The theory is referenced as a strength. Its limitations (unverified variance assumptions) are addressed in the Minor weaknesses above. Kept as part of the broader empirical contribution rather than as a standalone strength.

## Novel Insights
The paper's most novel contribution is the discovery that PPO-style clipping — commonly viewed as a training stabilizer — is the root mechanism by which RL conceals contamination signals. This is demonstrated through a clean causal comparison (RAFT vs. RAFT++, Table 3) where the *only* algorithmic difference is the importance-sampling/clipping term, yet detection AUROC drops from 77.51% to 57.58%. The finding that removing clipping from GRPO nearly fully restores detection (61.26% → 73.28%) provides converging evidence. This insight has implications beyond contamination detection: it suggests that RL training objectives can systematically reshape output distributions to erase membership signals, which connects to broader questions about memorization, privacy, and RL training dynamics in language models.

## Suggestions
- Calibrate "near random" claims in the abstract and Section 4 to accurately reflect Table 5 values. For Stage II, describe detection as "substantially degraded" or "approaching random" rather than "near random," since several method–model pairs achieve 60–65% AUROC.
- Verify the theoretical variance claims by reporting actual loss-variance measurements for members vs. non-members on correct trajectories.
- Consider adding bootstrap confidence intervals on AUROC values to strengthen the statistical grounding of the degradation claims.
- Either include embedding-based methods in the evaluation or add a sentence explaining their exclusion.

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Round | Comparison to Current Paper |
|--------|-----------|-------|-----------------------------|
| Nk1MegaPuG ("Evading Data Contamination Detection") | 4.25 | R1 | Current paper is substantially stronger on every dimension: methodology, causal evidence, evaluation breadth |
| rAylWUIKtu ("Benchmark Inflation") | 4.25 | R1 | Current paper has more experimental control and causal findings |
| 4eJDMjYZZG ("LM Detectors Are Easily Optimized Against") | 6.00 | R2 | Similar spirit (RL weakens detectors), but current paper has far more comprehensive evaluation, causal ablations, and theoretical analysis |
| zWqr3MQuNs ("Detecting Pretraining Data from LLMs") | 6.25 | R1/R2 | Current paper is broader in scope and has cleaner causal evidence |
| 9QPH1YQCMn ("Infilling Score") | 6.25 | R2 | Current paper has more novel contribution and broader evaluation |
| m2NVG4Htxs ("Longitudinal Perspective on LLM Data Contamination") | 6.75 | R1/R2 | Comparable empirical quality; current paper has stronger causal evidence but more limited domain coverage (math only) |
| Nsms7NeU2x ("How much can we Forget about Data Contamination?") | 6.75 | R1/R2 | Comparable; both have theory with limitations and strong empirical work; current paper's causal ablations are cleaner |

**Round 1 bracket:** 6.0–7.5. **Round 2 narrowed to:** 6.5, positioned between the 6.25 method-proposing papers (which the current paper exceeds in breadth and causal rigor) and the 6.75 anchors (to which it is comparable but slightly edges ahead due to its cleanest causal evidence in Table 3). The "near random" overstatement and unverified theory claims keep it from the 7.0+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>