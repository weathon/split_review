Now I have sufficient calibration information. Let me write the consolidated review.

## Summary

This paper proposes MiniLLM, a knowledge distillation method for large language models that replaces the standard forward KL divergence objective with reverse KL divergence, which is more suitable for generative LM distillation because it avoids the student overestimating low-probability regions of the teacher's distribution. The authors derive a policy-gradient-based optimization framework with three stabilization strategies (single-step decomposition, teacher-mixed sampling, length normalization) and evaluate across three model families (GPT-2, OPT, LLaMA) from 120M to 13B parameters on five instruction-following datasets, with human evaluation as well.

## Strengths

1. **Well-motivated theoretical contribution.** Section 2.1 clearly articulates why forward KL is problematic for generative LLM distillation (mode-covering forces the student to overestimate void regions of the teacher distribution) and why reverse KL is more suitable (mode-seeking focuses on the teacher's major modes). The toy illustration in Figure 2 concretely demonstrates this difference.

2. **Consistent and broad empirical gains.** Table 1 reports results across 3 model families, 5 datasets, and student sizes from 120M to 13B parameters. MiniLLM outperforms SFT, word-level KD, and SeqKD in nearly every setting, and in several cases the student surpasses the teacher. The improvement is often substantial (e.g., 25.3 vs. 16.4 on S-NI with GPT-2-120M; 35.5 vs. 32.4 on S-NI with LLaMA-7B). This breadth of evaluation — covering multiple architectures and scales — convincingly demonstrates generalization.

3. **Practical optimization framework with clean ablations.** Section 2.2 introduces three strategies (single-step decomposition, teacher-mixed sampling, length normalization) to address variance, reward hacking, and length bias. The ablation in Table 4 and Figure 8 isolates each component: removing length normalization collapses validation R-L from 27.4 to 17.4, and removing teacher-mixed sampling drops it to 22.3. This confirms that each strategy is necessary and that the implementation is non-trivial.

4. **Informative supporting analyses.** The exposure bias analysis (Figure 6) shows MiniLLM maintains near-zero excess error even at long generation lengths (250 tokens) while baselines accumulate 15–40% error, directly supporting the claim that self-generated training samples alleviate training-inference mismatch. The teacher scaling experiment (Figure 5) demonstrates that MiniLLM benefits from larger teachers while SeqKD plateaus, which is a practically important finding.

## Weaknesses

### Fatal
None.

### Major

- **Lack of variance or confidence intervals on the main quantitative results.** The paper states it reports average Rouge-L scores across 5 random seeds (Section 3.1), but Table 1 provides only point estimates with no standard deviations, confidence intervals, or significance tests. Several comparisons involve small margins (e.g., OPT-2.7B on Dolly: MiniLLM 27.4 vs. SeqKD 27.5; GPT-2-340M on Dolly: MiniLLM 25.4 vs. SFT 25.5). Without variance estimates, it is impossible to determine whether these differences are meaningful or attributable to seed variation. This weakens the evidential force of the paper's central claim that MiniLLM "consistently outperforms" baselines. The human evaluation (Figure 4) provides stronger evidence but covers only one dataset and one model family.

- **Over-reliance on Rouge-L as the primary automatic metric.** Rouge-L measures n-gram overlap and is known to be an imperfect proxy for response quality in open-ended instruction following, particularly for creative or reasoning tasks. The paper acknowledges this by including human evaluation and GPT-4 feedback, but the human eval is limited to a single setting (SelfInstruct, LLaMA family) and the GPT-4 evaluation is relegated to the appendix (removed by the parser). The bulk of the paper's analysis — exposure bias, scaling laws, response length splits, ablations — relies exclusively on Rouge-L. A method that improves n-gram overlap could still produce less helpful or less factual responses in settings not covered by the human evaluation.

### Minor

- **Calibration evaluation is on classification, not generation.** Table 2 reports ECE scores on SST-2 and BoolQ using zero-shot classification instructions. While this is a valid sanity check, calibration on classification tasks is tangential to the paper's main focus on open-ended generation. The claim that "MiniLLM produces better-calibrated generations" is not directly supported by these experiments.

- **Teacher-mixed sampling approximation is acknowledged but not analyzed.** Equation (5) uses an importance-sampling approximation where the per-step weight is set to the ratio of single-step probabilities rather than the full product over previous steps. The authors note this reduces variance (citing Serban et al. 2017; Levine et al. 2020), but provide no empirical or theoretical analysis of the resulting bias in the gradient estimate. A small-scale diagnostic comparing the approximate and exact estimators would strengthen confidence in the optimization.

- **The training cost and computational overhead are not reported.** MiniLLM involves multiple forward passes (student sampling, teacher scoring, importance weight computation) relative to baselines. Reporting training time, memory usage, or FLOPs would help practitioners assess the practical trade-off.

- **The concurrent work GKD (Iyer et al., 2023) appears in the references but is not discussed in the related work section.** Since GKD also addresses distribution discrepancy in autoregressive KD and has design similarities (on-policy sampling from the student), a brief discussion contrasting the two approaches would clarify the paper's positioning.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis of the teacher-mix strength α (currently fixed at 0.2) would be informative, particularly since α directly controls how much the teacher guides sampling.
- Concrete failure case examples (the paper mentions without the tricks the model produces "repeated, short, or meaningless strings" in Appendix E, which is inaccessible) would help illustrate the practical benefit of the optimization strategies.
- A brief discussion of how MiniLLM relates to RLHF (the training pipeline is described as similar) would clarify the novelty beyond using the teacher distribution instead of a reward model.

## Removed Points

**Harsh Critic Critical Issue 3 (SeqKD baseline may be understated):** The critic speculates that "on-policy sampling, soft label smoothing, or data augmentation" could close the gap with MiniLLM. This is a strawman — the paper implements SeqKD in its standard, widely-used form. The critic provides no evidence that these variants would improve results, and the suggestion amounts to "maybe a stronger baseline exists." Removed as speculative and unanchored to any specific content in the paper.

**Section-by-Section comments about missing appendix content (ExAccErr definition in appendix C.5, GPT-4 evaluation in appendix D.1, failure examples in appendix E):** These reflect the parser stripping appendix content from the extracted text, not a flaw in the original submission. The appendix exists in the original paper. Removed per parser-artifact rule.

**Section-by-Section note about "the paper does not compare to these concurrent methods" regarding GKD:** Reduced to a minor point in the main review. The paper does cite GKD in its reference list; the lack of discussion is a minor oversight, not a major weakness.

**Section-by-Section note about "the ExAccErr metric... we cannot verify its soundness":** The metric is from Arora et al. (2022), a published Findings of ACL paper. Removed as a non-issue — the metric is defined in the cited work and defined in the (parser-removed) appendix.

## Novel Insights

None beyond the paper's own contributions. The two review inputs largely agree on the paper's strengths and weaknesses; no reviewer detected a hidden flaw that the paper itself does not address.

## Suggestions

1. **Add standard deviations or confidence intervals to Table 1 and Figures 5, 7.** This is the single highest-impact change and would substantially strengthen the paper's claims. Since the authors already run 5 seeds, this is straightforward to report.

2. **Extend human evaluation to at least one additional dataset** (e.g., Vicuna or S-NI) or to include the OPT family, to broaden the evidence base beyond the LLaMA/SelfInstruct setting.

3. **Include a small-scale diagnostic of the importance-sampling approximation.** Compare the approximate single-step weight estimator against the exact product estimator on a few training steps and report the bias/variance trade-off.

4. **Report training time and relative computational cost** compared to SFT, KD, and SeqKD, so practitioners can assess the practical overhead.

5. **Discuss how MiniLLM differs from GKD (Iyer et al., 2023)** in the related work section, since both target distribution discrepancy in autoregressive KD.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| QAq5JTFJmp.md (Entropy KD) | 3.00 | R1 (low) | Much weaker paper; withdrawn |
| 8TbqoP3Rjg.md (Model Collapse KD) | 2.00 | R1 (low) | Much weaker paper; withdrawn |
| Wv9Gl1bFbc.md (Dynamic Self-Distillation) | 3.00 | R1 (low) | Much weaker paper; withdrawn |
| 28TLorTMnP.md (Soft Alignment) | 2.50 | R1 (low) | Much weaker paper; withdrawn |
| aU63Ib07KJ.md (SALT) | 5.50 | R1 (mid), R2 | Weaker evaluation scope; rejected |
| tJHDw8XfeC.md (MiniPLM) | 6.40 | R1 (mid), R2 | Comparable contribution; accepted (poster) |
| p14iRzavpt.md (PTLoss) | 5.33 | R1 (mid), R2 | Weaker empirical scope; rejected |
| IcVSKhVpKu.md (Hidden State CKA) | 5.67 | R1 (mid), R2 | Narrower model/task scope; accepted (poster) |
| 3baOKeI2EU.md (UniCoTT) | 6.25 | R2 | Comparable quality; accepted (poster) |
| nrvoWOWcyg.md (CD-LM) | 6.50 | R2 | Comparable; accepted (poster) |
| g9diuvxN6D.md (Instruction Robustness) | 7.50 | R2 | Stronger paper; accepted (spotlight) |
| 1aF2D2CPHi.md (Open-Vocab CLIP KD) | 8.00 | R1 (high) | Stronger paper; oral |
| tPNHOoZFl9.md (Learning Dynamics) | 8.00 | R1 (high) | Stronger paper; oral |
| wPMRwmytZe.md (Progressive Distillation) | 7.60 | R1 (high) | Stronger paper; oral |

**Round-1 bracket:** This paper sits between the weak anchors (2.0–3.0, all withdrawn) and the strong anchors (7.5–8.0, orals/spotlight). The plausible range is 5.0–7.0.

**Round-2 narrowing:** Comparing against the middle-band anchors, MiniLLM is clearly stronger than SALT (5.50, rejected) and PTLoss (5.33, rejected) — it has broader experiments, human evaluation, and a more complete analysis suite. It is comparable to MiniPLM (6.40, poster), UniCoTT (6.25, poster), and CD-LM (6.50, poster). The main weaknesses (missing error bars, Rouge-L reliance) are genuine but evidential rather than structural. The paper is well-positioned among accepted posters in this space.

**Final score:** 6.0. This reflects a solid contribution with clear theoretical motivation, practical optimization techniques, and broad empirical evaluation, tempered by the lack of variance reporting on the central quantitative comparisons.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>