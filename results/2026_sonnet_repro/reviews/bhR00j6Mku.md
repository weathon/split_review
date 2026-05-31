Now let me run calibration searches to score the paper accurately.Now I have enough information to write the final review. Let me verify one more key claim about the clean-model AUROC in Figure 4 before writing.Now I have everything I need to write the final review. Let me compile it.

---

## Summary

This paper presents the first systematic study of benchmark contamination detection applied to Large Reasoning Models (LRMs), framed around two scenarios. In Stage I, SFT contamination of a base model is initially detectable but can be progressively concealed by subsequent GRPO training on clean data—a mechanism linked via Theorem 3.1 to the PPO-style importance sampling/clipping gate and confirmed through a clean RAFT/RAFT++/GRPO ablation (Table 3). In Stage II, extensive CoT-SFT contamination applied directly to advanced LRMs leaves nearly no detectable trace because these models generalize to non-members, making existing memorization-based detectors fundamentally inapplicable.

---

## Strengths

- **GRPO demonstrably and consistently degrades detection across most methods.** Table 2 shows that after only 156 GRPO steps on clean data, Loss drops from 75.48% to 61.26%, Min-K% from 74.96% to 61.27%, Max-K% from 69.83% to 52.35%, and reference-free methods fall to near random (AUROC ≈ 50%). Figure 2 confirms a monotonic, step-by-step decline, and further SFT on the contaminated model does *not* replicate this effect—isolating the GRPO objective as the causal factor.

- **The RAFT/RAFT++/GRPO ablation in Table 3 is a clean causal isolation of the clipping mechanism.** RAFT (no clipping): Loss AUROC is essentially unchanged (+2.03%). RAFT++ with clipping: −17.91%. RAFT++ *without* clipping: −1.09%. GRPO with clipping: −14.22%. GRPO without clipping: −2.20%. This experiment directly validates the paper's theoretical prediction that the PPO-style clipping gate is the driver of concealment.

- **Figure 4 provides explicit clean-model baselines for Stage II.** The paper plots log-prob density distributions for clean advanced LRMs and reports AUROC: R1 Distill LLaMA (Clean) 0.497, R1 Distill Qwen (Clean) 0.479. Contaminated models only reach 0.579 and 0.498, respectively—barely above the clean-model floor and confirming that the Stage II near-random detection finding is not an artifact of a missing comparison point.

- **Comprehensive evaluation design.** The study covers 10 detection methods from five categories, six reasoning benchmarks, two base models for Stage I, and four advanced LRMs for Stage II—providing robust evidence across a wide surface area.

- **First systematic treatment of contamination concealment at the algorithmic level.** The paper identifies two distinct failure modes of existing detectors in the LRM setting—one mechanistic (RL shrinks the NLL gap) and one structural (LRM generalization undermines the memorization assumption)—and provides a clear two-stage framing of where contamination can enter the pipeline.

---

## Weaknesses

### Fatal
None.

### Major
None. The core empirical claims (Stage I concealment by GRPO, Stage II near-undetectability) are well-supported by the experiments as presented.

### Minor

- **Stage I speculative extrapolation for LiRA.** After 156 GRPO steps, LiRA degrades from 89.13% to 80.14%—a real and meaningful drop but still well above random. The paper states (line 91): "we expect that extensive GRPO training would render all existing detection methods to near-random performance eventually." This is a plausible and well-motivated conjecture, but it is a projection beyond the 156-step evidence. The reference-free methods (Loss, Min-K%, Max-K%) already fall to ~50% at 156 steps; LiRA does not. The paper should distinguish more carefully between what is shown and what is extrapolated for the strongest existing detector.

- **Theoretical treatment of GRPO involves an informal step.** The GRPO analysis in Section 3.2 concludes with "By similar argument, we know that the μ term does not contribute significantly to the concealment. The covariance term can be analyzed similarly to show that the concealment also happen on GRPO thanks to the importance sampling and clipping term" (line 245). This is asserted rather than derived. Additionally, the key inequality for RAFT—that the covariance gap offsets the mean gap—is stated as empirical ("Empirically, the covariance gap offsets the mean gap, yielding Δ_N − Δ_M ≥ 0," line 208) rather than analytically established. Table 3 provides strong empirical support for the overall claim, but the theory section provides intuition and partial formal structure, not complete proofs. The paper would be more precise in characterizing which inequalities are theoretical versus empirical.

- **"Consistent decrease across all detection methods" is imprecise for methods already near 50%.** Table 2 shows that Verbatim (52.76%), Min-K%++ (49.61%), and Neighbor (50.71%) already start near random *before* GRPO. The reported drops for these methods are within noise (−0.60, −6.02, −0.28, respectively for clean RL). While technically every method shows some directional drop, the claim of "consistent decrease" is most meaningful for the subset that has signal to lose (LiRA, Loss, Min-K%, Max-K%, Ref).

- **Unremarked asymmetry in Stage II inflation.** Table 4 shows that DeepSeek-R1-Distill-Qwen-7B achieves only 2.68% average performance lift from "extensive SFT contamination" (54.42% → 57.10%), while the 14B model achieves 9.4% (59.83% → 69.24%). The paper does not discuss why the 7B model inflates so modestly. While the detection failure point holds regardless of the inflation magnitude, this asymmetry deserves acknowledgment.

### Trivial
None.

---

## Nice-to-Haves

- Extending GRPO training well beyond 156 steps for at least one detection method (ideally LiRA) and one benchmark to directly demonstrate whether the degradation toward random continues or plateaus, rather than relying on extrapolation.
- Varying the contamination fraction in Stage II (e.g., 25%, 50%, 75% of members) to test whether AUROC eventually separates at lower contamination densities, which would clarify whether detection failure is absolute or a function of contamination intensity.
- Reporting variance estimates (e.g., standard deviation across benchmarks) for AUROC values to allow readers to gauge which differences in Table 2 and Table 5 are reliable rather than noisy.
- A brief sketch in Section 5 of what properties a contamination detector would need to be robust to *both* Stage I and Stage II failure modes (beyond the two high-level directions proposed).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Missing clean-model AUROC baselines."** For Stage II, this criticism is factually incorrect—Figure 4 explicitly reports AUROC for clean advanced LRMs (0.479–0.497, effectively random), directly establishing the floor against which contaminated-model AUROCs are compared. For Stage I, the reference-free detectors already produce near-random AUROC on non-contaminated inputs by design (the member/non-member split is random when there is no contamination), so the before-RL row in Table 2 itself serves as the relevant baseline. **REMOVED** as substantially addressed by the paper.

- **Harsh Critic: "Stage II conflates LRM generalization with contamination concealment."** The paper's Discussion section (lines 329–330) explicitly introduces the generalization explanation: "LRMs internalize the underlying knowledge and reasoning process during the contamination with CoT data, enabling generalization to distributionally similar questions." It labels this a "confounding factor… not accounted for by existing detection approaches." The paper then cites this as a fundamental challenge to memorization-based detection assumptions. The framing throughout Section 4 could more consistently distinguish Stage II (detection infeasibility due to generalization) from Stage I (algorithmic concealment), but the paper does not ignore this distinction. **DEMOTED** from weakness to nice-to-have clarification.

- **Harsh Critic: "Table 1 underplays the observation that contamination SFT without RL yields highest performance (47.23%)."** This is a valid secondary observation—for Qwen2.5-7B, adding RL after contaminated SFT reduces average pass@1 from 47.23% to 45.55%/44.96%. However, for Llama-3.1-8B the pattern reverses (contaminated SFT + clean RL = 41.68% > contaminated SFT alone = 40.68%). The paper's threat model assumes RL is applied regardless because it is needed for overall reasoning ability, which is a plausible and stated justification. **DEMOTED** to a minor contextual nuance, not a weakness.

- **Harsh Critic: Reproducibility/variance concerns.** The paper delegates detailed generation setup justification to an appendix. Criticism about undisclosed hyperparameters is not actionable given that appendices are stripped. **REMOVED** per hard rules.

---

## Novel Insights

The paper's most genuinely novel observation is the mechanistic link between PPO-style clipping and contamination concealment: clipping asymmetrically penalizes high-variance, off-policy updates from non-members more than members, contracting the NLL gap that detectors rely on. The controlled RAFT vs. RAFT++ vs. GRPO ablation is a particularly clean demonstration of this, and the fact that removing clipping alone restores near-baseline detection performance (Table 3) provides a clear path for future detector designs that could exploit this asymmetry. The Stage II finding—that contamination with CoT on advanced LRMs raises non-member log-probabilities nearly as much as member log-probabilities—reframes the detection problem: the enemy is not memorization per se but the generalization capacity of LRMs, which obsoletes the key assumption behind virtually all existing methods.

---

## Suggestions

1. Run GRPO for 400+ steps on the LiRA detector (single model/benchmark pair) to show whether the 80% floor continues declining, rather than asserting the extrapolation speculatively.
2. In Section 3.2, explicitly label which derivation steps are analytically proven and which are empirically supported. A sentence like "The following inequality is established empirically via Table 3 rather than derived analytically" would improve scientific precision without weakening the contribution.
3. Add a brief paragraph clarifying the asymmetry in Stage II: for some models (e.g., Qwen-7B with only 2.68% inflation), contamination provides little practical benefit even if it evades detection.
4. In the conclusion, make the framing distinction between Stage I (algorithmic concealment) and Stage II (generalization-induced detection infeasibility) explicit, since the remedies are different—one calls for clipping-aware detectors, the other calls for abandoning the memorization paradigm entirely.

---

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Evading Data Contamination Detection | Nk1MegaPuG.md | 4.25 | R1 | Much weaker: no LRM focus, poor presentation, no theory, rejected |
| Benchmark Inflation via Retro-Holdouts | rAylWUIKtu.md | 4.25 | R1 | Narrower scope, no mechanism analysis, rejected |
| Detecting Pretraining Data (Min-K%) | zWqr3MQuNs.md | 6.25 | R1 | Proposes a new method; simpler setup; comparable scope |
| To the Cutoff... and Beyond? | m2NVG4Htxs.md | 6.75 | R1 | First systematic contamination analysis; elegant design; only 2 datasets; no theory |
| Language Model Detectors Easily Optimized | 4eJDMjYZZG.md | 6.00 | R2 | Similar spirit (RL fools detectors); accepted; no theory; narrower evaluation |
| Amplifying Training Data Exposure | jx6njBKH8E.md | 5.75 | R2 | Fine-tuning amplifies memorization; rejected; less comprehensive |
| Low-Cost High-Power MIA (RMIA) | dRel8fuUK4.md | 6.00 | R2 | New MIA attack; rejected; proposes method vs. diagnosis |

**Round 1 bracket:** 5.0–7.0

**Round 2 narrowing:** The most topically similar anchors in range are "Language Model Detectors Easily Optimized Against" (6.00, accepted) and "To the Cutoff... and Beyond?" (6.75, accepted). The paper under review is clearly stronger than the 6.00 anchor—it adds theoretical analysis, covers 10 detection methods across 6 benchmarks and 4 advanced LRMs, and cleanly ablates the mechanism. Compared to "To the Cutoff..." (6.75), the paper under review has broader experimental scope and supporting theory, but "To the Cutoff..." has a more elegant natural-experiment design with cleaner ground truth. The paper is approximately comparable to, perhaps slightly above, the 6.75 anchor on scope and depth, with minor deductions for the informal GRPO theoretical step and the 156-step Stage I limitation. It clearly exceeds the 6.00 anchors. Score: **6.5**.

**Axis evaluation:**
- *Originality:* High — first systematic study of contamination detection in LRMs; novel identification of clipping as the concealment mechanism.
- *Importance of research question:* High — leaderboard integrity and evaluation fairness for LRMs is an urgent, timely concern.
- *Claims well-supported:* Mostly well-supported; Stage II claim backed by Figure 4 baselines; Stage I supported by Table 2 and Figure 2; mechanism supported by Table 3 ablation. Minor gap for LiRA speculative extrapolation.
- *Soundness of experiments:* Good — controlled for training duration (SFT vs. GRPO), ablated key components (clipping removal), evaluated multiple models and benchmarks.
- *Clarity of writing:* Good — clear two-stage framing, but Stage I/II distinction could be reinforced in framing of Section 4.
- *Value to the research community:* High — identifies mechanism, provides actionable directions, raises important alarm about LRM evaluation integrity.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>