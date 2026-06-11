Now I have all the calibration data I need. Let me finalize the review.

**Calibration Summary:**

**Round 1 (Bracketing):** Initial bracket: between 4 and 6.
- Weak anchors (<3.5): Papers at 2.33-3.00 — clearly below GHPO in relevance and quality.
- Middle anchors (3.5-7.5): Papers at 3.75-5.50 — most relevant comparison zone.
- Strong anchors (>7.5): WizardMath (8.00) — clearly stronger, with SOTA results and thorough evaluation.

**Round 2 (Narrowing within 4-6.5):**
- "On Designing Effective RL Reward at Training Time" (5.17) — most directly comparable. Similar evaluation gaps (missing baselines, marginal gains). GHPO's idea is more novel but evaluation is less complete. GHPO ≈ slightly below this.
- "RLSF" (4.50) — weaker methodology and evaluation. GHPO is clearly stronger.
- "Hint Marginalization" (5.75) — better evaluation. GHPO is weaker.
- "Leveraging Imitation Learning and LLMs for HRL" (4.75) — conceptual overlap (hybrid imitation+RL). Some evaluation gaps. GHPO is slightly stronger.
- "Formal Theorem Proving" (5.50) — stronger evaluation but polarized scores. GHPO ≈ comparable.

**Final score: 5.0** — The paper has a well-motivated core idea and consistent positive results against GRPO, but is missing critical SOTA comparisons (DAPO, LUFFY — methods discussed in the paper itself), lacks any variance reporting for high-variance RL, and makes unsupported efficiency claims. These gaps are too large for acceptance at ICLR but the underlying approach is sound.

---

## Summary

This paper proposes GHPO, a framework that augments GRPO-based RLVR with adaptive hint injection: when the model fails all G sampled responses for a problem (all-zero rewards), it appends part of the ground-truth solution to the prompt, converting that training step from pure RL into a hybrid of imitation and RL. The method is evaluated on math reasoning benchmarks with Qwen2.5-7B and Qwen2.5-Math-7B.

## Strengths

- **Empirically grounded problem identification:** Section 2.3 rigorously shows that all-zero group rewards produce zero advantages in GRPO, and quantifies the severity (even Qwen2.5-7B-Instruct fails 52% of NuminaMath-1.5 problems). GHPO's difficulty detection directly targets this concrete failure mode.

- **Consistent gains across models and benchmarks with informative ablation:** Tables 1 and 2 show GHPO outperforming GRPO on 5/6 benchmarks (Math dataset) and all 6 benchmarks (Mixed dataset) with Qwen2.5-Math-7B. The GRPO-CL-H(0.5) ablation (fixed 50% hints + curriculum learning, avg 0.422 vs. GHPO's 0.442) helps isolate that the *adaptive* hinting mechanism (rather than simply having hints available) drives the improvement.

- **Training dynamics analysis provides mechanistic support:** Figure 4 shows GHPO maintains consistently smaller gradient norms than GRPO alongside higher accuracy rewards and longer response lengths. The gradient norm comparison concretely supports the claimed stability benefit beyond reporting only final accuracy numbers.

- **Clean cold-start design:** Section 3.5 identifies that early formatting failures can cause false-positive difficulty detection, and the 20-step GRPO warm-up is a simple, well-motivated fix.

## Weaknesses

### Major

- **Missing comparisons with directly relevant SOTA methods:** The paper discusses DAPO (Yu et al., 2025), LUFFY (Yan et al., 2025), VAPO, and Dr. GRPO in Related Work (Section 5), and claims GHPO "outperforms state-of-the-art RL methods" (Section 1). Yet none of these appear as experimental baselines. The comparison set consists only of GRPO and self-constructed variants (GRPO-CL, GRPO-CL-H(0.5)). LUFFY, which also hybridizes imitation and on-policy RL for reasoning, is the most directly comparable approach. Without these comparisons, the paper cannot substantiate its central claim of advancing the SOTA. *(Verified: paper discusses these methods on page 8 but Tables 1-2 include none of them.)*

- **No statistical significance or variance reporting:** All results in Tables 1 and 2 are single numbers per benchmark with no standard deviations, confidence intervals, or indication of multiple seeds. RL training for LLMs is high-variance, particularly in the sparse-reward regime that the paper itself characterizes. Single-run results make it impossible to assess whether the reported improvements (e.g., 0.442 vs. 0.398 avg) are reliable or within noise. *(Verified: Tables 1-2 contain only point estimates; no std/error bars anywhere.)*

- **Efficiency claims are asserted but not measured:** The title ("Stable and Efficient") and abstract position efficiency as a contribution. The cold-start strategy is motivated as conserving compute, and the conclusion describes GHPO as "data-efficient." However, no wall-clock time, GPU-hours, FLOPs, or convergence-step measurements are provided anywhere. Since GHPO injects ground-truth traces into prompts for ~60% of problems (Figure 3), the per-step cost likely increases; without measurements, the net efficiency effect is unknown. *(Verified: no efficiency metrics in Sections 3-4.)*

### Minor

- **The binary difficulty criterion is not ablated:** The detection mechanism classifies a problem as "difficult" iff all G responses have zero reward (Section 3.3). Problems where 1/G responses are correct still produce non-zero group advantages but may plausibly benefit from guidance. The paper does not explore or justify this threshold choice. *(Verified: Section 3.3 lines 133-139.)*

- **GPQA-Diamond is mislabeled as a "mathematics benchmark":** The abstract describes "six challenging mathematics benchmarks" and Section 4.1 lists GPQA-Diamond among "standard mathematical reasoning benchmarks." GPQA-Diamond is a graduate-level science Q&A dataset covering physics, chemistry, and biology. The cross-domain transfer result (GHPO's 39.4% vs. GRPO's 30.8%) could actually be a strength, but the mislabeling obscures rather than highlights this. *(Verified: abstract line 9, Section 4.1 line 157.)*

- **Table 1 vs. Table 2 dataset labeling is unclear:** Table 2 is labeled "Mixed dataset" but the text immediately below describes results on "NuminaMath-S." The relationship between "Mixed dataset" and NuminaMath-S is not explained in the main text. *(Verified: Table 2 heading vs. Section 4.2 lines 188-189.)*

- **Figure 3 shows ~60% of problems persistently require hints, with no comparable GRPO plot:** The proportion of problems detected as difficult fluctuates around 60% without a clear downward trend. The paper interprets this as showing "the pervasive nature of the reward sparsity problem," but without the corresponding plot for GRPO (where zero-reward problems remain zero-reward), the reader cannot assess whether GHPO is reducing or merely coping with the sparsity. *(Verified: Figure 3 and surrounding text on page 7.)*

- **Gradient norm interpretation has an alternative explanation:** Section 4.4 interprets smaller gradient norms in GHPO as evidence of "a smoother and more stable optimization process." An alternative reading is that guided data provides weaker learning signals (because the model is being led toward known-good answers). The current interpretation is not unreasonable, but connecting gradient norms to downstream generalization would strengthen the argument. *(Verified: page 7-8, Figure 4d discussion.)*

### Trivial

None.

## Nice-to-Haves

- An SFT baseline (training on ground-truth traces for hard problems + RL for easy problems) would isolate whether GHPO's gains come from the RL+imitation hybrid or simply from having more training data with solutions.
- Tracking whether specific problem types migrate from "hint" to "no-hint" categories over training would directly test whether GHPO expands the model's independent capability.
- An analysis of reasoning chain quality (e.g., correctness-conditioned length) would strengthen the argument about long CoT generation.

## Removed Points

The following points from the inputs were filtered:
- **"Assumption 1 is circular framing":** Factually wrong. The paper states a hypothesis and then tests it empirically — standard scientific practice.
- **"Multi-stage guidance details relegated to appendix":** The parser strips appendix content; these details exist in the original submission.
- **Missing related works:** Rule prohibits fabricating missing references without external sources.
- **Formatting/style nitpicks and speculations about unreleased methods:** Removed per filtering rules.
- **Strength Finder's generic/sycophantic strengths:** Removed strengths like "this paper addresses an important problem" that lacked specific, verifiable evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add DAPO and LUFFY as experimental baselines.** These are the most directly comparable methods and are already discussed in the related work. Without them, the claim of outperforming "state-of-the-art RL methods" is unsubstantiated.

2. **Report mean ± std over at least 3 random seeds** for all main results. This is the single highest-leverage addition for establishing reliability in high-variance RL.

3. **Provide computational cost measurements** (wall-clock time, GPU-hours, or convergence steps to a given accuracy threshold) to substantiate the efficiency claims in the title and abstract.

4. **Ablate the binary difficulty threshold** (e.g., trigger hints when ≥50% of responses fail or when average reward is below a threshold) to justify the all-or-nothing criterion.

5. **Correct the GPQA-Diamond description** or explicitly discuss the cross-domain transfer in the interpretation.

## Score and Decision

**Round 1 bracket:** The paper sits between the weak anchors (2.33–3.00, clearly below) and strong anchors (8.00, clearly above), in the 4–6 range.

**Round 2 narrowing:** Compared to the most topically similar anchors:
- *"On Designing Effective RL Reward at Training Time"* (5.17): GHPO has a more novel core idea but a weaker evaluation (no SOTA baselines, no variance). Comparable overall.
- *"RLSF"* (4.50): GHPO is clearly stronger in methodology and evaluation breadth.
- *"Hint Marginalization"* (5.75): GHPO is weaker in evaluation completeness.
- *"Leveraging Imitation Learning and LLMs for HRL"* (4.75): GHPO is slightly stronger.

**Final position:** The paper has a well-motivated core idea and consistent positive results against GRPO, but the evaluation gaps (missing SOTA comparisons for methods discussed in the paper, no variance reporting, unsupported efficiency claims) are substantial. This places it at the lower end of the 4–6 bracket.

**All anchors retrieved:**
| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| 28TLorTMnP.md | 2.50 | 1 | Weaker — different topic (soft alignment) |
| ZK1NnjpjEs.md | 3.00 | 1 | Weaker — NLU with RL, less relevant |
| zEhTnQZB3D.md | 2.33 | 1 | Weaker — continual RL |
| fBSc0c1IXJ.md | 3.00 | 1 | Weaker — remote RL |
| F0GNv13ojF.md | 5.17 | 1,2 | Comparable — same domain (RL for LLM reasoning) |
| zZU69H8tcr.md | 3.75 | 1 | Different domain (LLM pruning) |
| YW79lAHBUF.md | 3.75 | 1 | Different framing (in-context RL) |
| BGnm7Lo8oW.md | 5.50 | 1 | Stronger — better evaluation |
| mMPMHWOdOy.md | 8.00 | 1 | Stronger — WizardMath, SOTA results |
| DzKdjWe59v.md | 5.75 | 2 | Stronger — better evaluation of inference-time hints |
| D23JcXiUwf.md | 5.50 | 2 | Comparable — polarized scores |
| gdzpnRBP4F.md | 4.50 | 2 | Weaker — RLSF, less rigorous |
| 6y00rooi7i.md | 4.75 | 2 | Comparable — hybrid imitation+RL |
| wPyTeUMRgh.md | 4.25 | 2 | Different domain |
| mBrAuyd26J.md | 4.33 | 2 | Different domain |
| TWC4gLoAxY.md | 6.25 | 2 | Different domain (logic-guided reasoning) |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>