Now I have enough context. Let me synthesize the final review.

Based on my analysis:

**Round 1 bracket**: (4.5, 7.5) — I compared against "Evading Data Contamination Detection" (4.25), "How much can we Forget" (6.75), "To the Cutoff... and Beyond?" (6.75), and "Persistent Pre-training Poisoning" (5.75).

**Round 2 narrowing**: I pulled anchor papers between (4.5, 5.5) and (5.5, 7.5). The most relevant comparisons are "Persistent Pre-training Poisoning" (5.75) and "Detecting Pretraining Data from LLMs" (6.25). The current paper is stronger than the former (better controlled experiments, more novel findings) and comparable to the latter (both have strong empirical components with some theory gaps).

**Final score**: 6.0 — The paper makes genuine contributions but has a real scope gap between theory and clean-RL experiments, plus some overstatement. It's a solid empirical study with partial theoretical support.

Now let me write the consolidated review.

Let me carefully evaluate each of the Harsh Critic's points against the actual paper:

**Critic Point 1: Theory-Experiment mismatch**

The paper's Section 3.2 states: "We assume that the RL training is performed on the benchmark data (i.e., training data is the combination of members M and non-members N)."

The main empirical results in Table 2 include both "RL w/ Clean" and "RL w/ Clean&Mem". Both show concealment.

The critic says: "the theoretical mechanism of clipping reweighting trajectories from contaminated data simply does not operate when the contaminated data is never fed into the RL objective."

Verdict: This is a valid concern. The theory IS explicitly scoped to the contaminated-RL case. The clean-RL case is empirically observed but not directly explained by the presented theory. However, the paper does have Table 3 (ablation studies removing clipping from RAFT++ and GRPO) that supports the mechanism more generally. And the key insight is that the paper identifies PPO-style clipping as the root cause through controlled experiments, with theory supporting the contaminated case. The clean-RL concealment is a separate empirical finding.

I'll keep this as a Major weakness but note that it doesn't invalidate the paper's contributions — it just means the theory is more narrowly scoped than initially presented.

**Critic Point 2: Overstatement of Stage II results**

The paper says "almost all the detection approaches consistently perform near random guesses (i.e., AUROC ≈ 50%)."

Looking at Table 5: LiRA on DS Qwen-14B achieves 65.55% on average. LiRA on DS Llama-8B 61.34%. Min-K% on DS Llama-8B 62.42%. Some individual benchmark scores reach 75-77%.

65% AUROC is substantially above random (50%). The claim "near random guess" IS overstating. But the core finding (severe degradation from Stage I levels of 89%) is valid.

I'll keep this as a Minor weakness — it's about precision of language, not the validity of the result.

Now let me also check whether the critic's other points about Table 3 not specifying RL data are valid. Looking at the paper, Table 3 caption says "SFT contaminated model further trained with different RL objectives" and doesn't specify clean vs contaminated data. Without the appendix, I can't verify what was used. But this is a legitimate concern for reproducibility. I'll note this as a Minor weakness.

Let me now draft the full review.

For the Strength Finder, let me evaluate each claimed strength:

1. "Systematic empirical evaluation across 10 detection methods and 6 benchmarks" - CONCRETE, well-supported by Tables 2, 5.
2. "Theoretical analysis identifying PPO-style importance sampling/clipping as the root cause" - PARTIALLY supported (scope limitation as noted). But the theorem and empirical validation (Table 3) are there.
3. "Controlled experiments isolating the concealment effect from mere additional training" - STRONG, Figure 2 and Table 23 show further SFT doesn't conceal.
4. "Demonstration that contamination with CoT on advanced LRMs yields large performance inflation yet near-random detection" - SUPPORTED by Tables 4 and 5 (though the "near-random" language is imprecise as noted).
5. "Broad coverage of model families and sizes" - SUPPORTED.

Let me keep all of these with some nuance.

Now, let me finalize the score. Based on my calibration:
- The paper is clearly stronger than "Evading Data Contamination Detection" (4.25) 
- Comparable to "Persistent Pre-training Poisoning" (5.75) - both have solid empirical work with some limitations
- Slightly below "Detecting Pretraining Data from LLMs" (6.25) - that paper had a cleaner contribution (new method + benchmark)
- The "How much can we Forget" (6.75) and "To the Cutoff" (6.75) are probably stronger papers with clearer contributions

I'll go with 5.5 or 6.0. Let me settle at 6.0. The paper has a novel angle (LRM contamination detection), strong empirical evidence, and a theoretical attempt that, while scope-limited, is partially validated by ablation experiments. The weaknesses are real but not fatal.

Actually, let me reconsider. 6.0 seems fair. The paper does several things well and has clear empirical contributions. The main weakness (theory scope) is a limitation of the explanation, not of the empirical findings themselves.

Let me finalize at 6.0.Now I have all the information I need. Let me synthesize the final review.

## Summary of Calibration

**Round 1 bracket**: (4.5, 7.5). Compared against anchors: "Evading Data Contamination Detection for Language Models is (too) Easy" (4.25, Reject), "How much can we Forget about Data Contamination?" (6.75, Reject), "To the Cutoff... and Beyond?" (6.75, Accept), "Persistent Pre-training Poisoning of LLMs" (5.75, Accept).

**Round 2 narrowing**: Read "Detecting Pretraining Data from LLMs" (6.25, Accept) and "Persistent Pre-training Poisoning" (5.75, Accept) in full. The current paper is stronger than the latter (better controlled experiments, more novel findings) and comparable to the former.

**Final score**: 6.0 — genuine empirical contributions with a partial theory gap that weakens but does not invalidate the core claims.

---

## Summary
This paper presents the first systematic study of benchmark contamination detection in Large Reasoning Models (LRMs), examining two realistic contamination stages: (I) SFT contamination that is initially detectable but can be concealed by subsequent GRPO/RL training, and (II) final-stage SFT contamination with CoT on advanced LRMs that leaves minimal detectable evidence. The paper evaluates 10 detection methods across 6 benchmarks and multiple model families, providing theoretical analysis linking PPO-style importance sampling/clipping to contamination concealment.

## Strengths
- **Systematic empirical evaluation across 10 detection methods, 6 benchmarks, and multiple model families (Qwen2.5, Llama-3.1, DeepSeek-R1-Distill, OpenThinker).** The breadth of this evaluation provides concrete evidence that existing detection methods are fragile in LRM settings. For example, after GRPO training, Min‑K% AUROC drops from 74.96% to 61.27% (Table 2), and after extensive SFT contamination with CoT, most methods hover near 55–65% AUROC compared to Stage I levels of ~89% (Table 5).

- **Controlled experiments isolating the concealment effect from mere additional training.** The paper convincingly shows that further SFT on clean data preserves detection AUROC (Figure 2), while GRPO and RAFT++ cause monotonic decline, and plain rejection sampling (RAFT) without importance sampling/clipping does not conceal contamination (Table 3). This rules out a "forgetting" explanation and directly supports the claim that the RL objective itself drives concealment.

- **Theoretical decomposition identifying PPO-style importance sampling/clipping as a key mechanism.** Theorem 3.1 decomposes the NLL gap change into mean and covariance terms, with analysis showing that the covariance term driven by clipping contracts the membership gap. This is empirically validated: removing clipping from GRPO restores Loss detector AUROC from 61.26% to 73.28% (Table 3), quantitatively matching the theoretical prediction for the contaminated-RL setting.

- **Novel finding on Stage II CoT contamination.** Table 4 shows that contaminating advanced LRMs with CoT yields substantial performance inflation (~12% average pass@1 increase), while Table 5 and Figure 4 demonstrate that existing detection methods fail to distinguish members from non-members because LRMs generalize to distributionally similar unseen samples. This challenges the core memorization assumption underlying many detection methods.

## Weaknesses

### Fatal
None.

### Major
- **Scope mismatch between theoretical analysis and primary experimental setting.** The theory in Section 3.2 assumes "the RL training is performed on the benchmark data" (i.e., prompts from the evaluation benchmarks themselves). However, the paper's headline evidence (Table 2, "RL w/ Clean") uses RL training on *clean* data (DeepMath-103K), where the model never sees the contaminated benchmark prompts during RL. The theory's mechanism (clipping reweighting trajectories from contaminated data) does not directly operate in this setting. The paper blurs this distinction by presenting the theory as the general explanation — e.g., "theoretical analysis indicates that PPO-style importance sampling and clipping objectives are the root cause" — without explicitly scoping the theory to the contaminated-RL case and giving a separate account for why clean RL also conceals contamination. The clean-RL concealment is a reproducible empirical finding but lacks the mechanistic explanation the paper claims. The authors should either (a) explicitly scope the theory to the contaminated-RL setting and present clean-RL as a separate empirical finding needing a distinct explanation, or (b) extend the theory. (The ablation experiments in Table 3 do partially bridge this gap by showing clipping removal prevents concealment, but the theoretical foundation for clean-RL remains absent.)

### Minor
- **Overstatement of Stage II detection failure.** The paper states that after extensive SFT contamination with CoT, "almost all the detection approaches consistently perform near random guesses (i.e., AUROC ≈ 50%)." However, Table 5 shows that several methods achieve meaningfully above-chance performance: LiRA on DeepSeek-R1-Distill-Qwen-14B averages 65.55% (individual benchmarks reach 75.56%), Min-K% on DS Llama-8B averages 62.42%, and Loss on DS Llama-8B averages 62.59%. While detection is *severely degraded* compared to Stage I (89%+ LiRA), characterizing AUROC in the 60–65% range as "near random" is imprecise and overstates the result. The core finding — that detection is substantially less reliable — remains valid with more precise language.

- **Missing data specification for the controlled experiments in Table 3.** The caption does not state whether the RL training in these ablations used clean data or contaminated data. This is important both for reproducibility and for connecting the ablation results to the theoretical analysis. (The appendix, which would likely contain this detail, was stripped by the PDF parser.)

- **Theoretical analysis is limited to a tabular setting with a small gradient step assumption.** The paper acknowledges this but does not discuss whether the result is expected to hold in the neural network regime with practical step sizes. While the empirical validation in Table 3 provides some reassurance, the gap between theory and practice is notable.

### Trivial
- None beyond the above, which are already captured.

## Nice-to-Haves
- An ablation on the *amount* of contamination in Stage II (e.g., how detection degrades with the number of contaminated samples or training steps) would strengthen generalizability.
- A more nuanced discussion of the generalization hypothesis in Stage II — the paper suggests LRMs "internalize" rather than "memorize" contamination data, but provides no controlled test (e.g., comparing performance on near-duplicate vs. novel questions).
- Considering whether RL-based contamination at Stage II (rather than SFT-only) would behave differently.

## Removed Points
- **Harsh Critic's claim that the paper "overstates" the Stage II conclusion as a fatal flaw**: Removed. The overstatement is real but minor; the core finding (severe degradation) is solid.
- **Harsh Critic's suggestion that the theory is "zero" applicability to clean-RL**: Weakened to Major. The empirical ablation (Table 3) does validate the mechanism partially, even if the theory doesn't fully cover the clean-RL case.
- **Strength Finder's claim that "the single most important piece of evidence is the sharp, consistent degradation"**: Kept in spirit but not included verbatim — this is better expressed through the specific strengths listed above.
- **Various style/formatting nitpicks from both reviewers**: Removed per instructions (parser artifacts).
- **Generic strengths about "important problem" or "timely topic"**: Removed per instructions.

## Novel Insights
The paper's most novel insight is the identification of a specific algorithmic mechanism (PPO-style importance sampling and clipping) as the driver of contamination concealment. While prior work on contamination has focused on data-level manipulations (rephrasing, augmentation) or forgetting through continued pre-training, this paper shows that the RL optimization objective itself — independent of data content — can suppress the statistical signals that detection methods rely on. The Stage II finding — that LRMs generalize to distributionally similar unseen samples after CoT contamination, undermining the memorization assumption behind most detectors — is also novel but follows more directly from known properties of LRMs' long-CoT capabilities.

## Suggestions
1. **Clarify the scope of the theoretical analysis explicitly.** State in Section 3.2 that Theorem 3.1's assumptions match the "RL w/ Clean&Mem" condition, and provide a separate, heuristic explanation for why clean-RL also conceals contamination (e.g., global policy changes from GRPO training transfer to the benchmark distribution, and the clipping mechanism operates on whatever data the model trains on).
2. **Replace "near random guess" with precise characterizations** (e.g., "average AUROC drops to 55–65%, far below the 89% achieved by LiRA in Stage I"). The interesting finding is severe degradation, not total failure.
3. **Specify the RL training data used in Table 3's caption** for reproducibility.
4. **Add an ablation on contamination amount in Stage II** to strengthen the generalizability claim.
5. **Discuss the limitations of the tabular/small-step assumptions** more directly, and note whether the theoretical result is expected to extend to practical neural network training.

## Score and Decision
**Score: 6.0**

**Decision: Accept**

**Calibration detail:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Evading Data Contamination Detection for LMs is (too) Easy (Nk1MegaPuG) | 4.25 | R1 | **Weaker** — less thorough evaluation, unclear methodology |
| How much can we Forget about Data Contamination? (Nsms7NeU2x) | 6.75 | R1, R2 | **Slightly stronger** — cleaner theoretical story, but different topic (forgetting vs. RL concealment) |
| To the Cutoff... and Beyond? (m2NVG4Htxs) | 6.75 | R1, R2 | **Slightly stronger** — cleaner methodology, but limited to longitudinal analysis of two datasets |
| Persistent Pre-training Poisoning of LLMs (eiqrnVaeIw) | 5.75 | R2 | **Comparable** — both have empirical contributions with some scope/novelty limitations |
| Detecting Pretraining Data from LLMs (zWqr3MQuNs) | 6.25 | R2 | **Comparable** — method paper with clean contribution; current paper has broader scope but a theory gap |
| DfPO: Degeneration-free Policy Optimization (6UQaXJm53B) | 5.25 | R2 | **Weaker** — different topic, less relevant |
| On Designing Effective RL Reward (F0GNv13ojF) | 5.17 | R2 | **Weaker** — different topic |

The paper sits between 5.75 and 6.25 on the anchors' scale: it has genuine empirical novelty and breadth that exceeds the "Evading" paper, but the theory-experiment scope gap prevents it from matching the cleaner contributions of the 6.75 papers.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>