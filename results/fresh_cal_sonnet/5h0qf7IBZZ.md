Now let me run the calibration search to anchor the score. I'll do a bracketing pass first.Let me read the most relevant anchor papers:Good. Initial bracket: 6–8. MiniLLM is clearly stronger than the rejected 6.0 LLM distillation anchor but the training-regime/divergence conflation and lack of critical ablation keeps it from the top. Let me narrow.I now have enough to write the review. Let me compile everything.

---

## Summary

MiniLLM proposes replacing forward KL divergence (KLD) with reverse KLD as the training objective for white-box knowledge distillation of generative large language models. The method derives a policy-gradient optimizer for this reverse KLD objective, incorporating three stabilization strategies (single-step decomposition, teacher-mixed sampling, length normalization), and evaluates the approach on instruction-following tasks across GPT-2, OPT, and LLaMA model families (120M–13B parameters) on five datasets with both automated and human evaluation.

---

## Strengths

- **Principled, well-supported motivation.** Figure 2's Gaussian-mixture toy experiment concretely illustrates how minimizing reverse KLD produces mode-seeking behavior while minimizing forward KLD assigns probability mass to void regions. This directly motivates the proposed divergence switch and goes beyond prior white-box KD work for LLMs, which typically offers no such analytic grounding.

- **Three ablation-validated optimization strategies.** The single-step decomposition, teacher-mixed sampling, and length normalization components are each tested in Table 5 (Section 3.3). The ablation shows that removing any one strategy materially degrades performance—removing length normalization drops validation Rouge-L from 27.4 to 17.4 and increases reverse KLD throughout training—providing direct evidence that each component is necessary, not merely heuristic decoration.

- **Consistent empirical gains across three model families and multiple scales.** Table 1 reports results for GPT-2 (120M–760M), OPT (1.3B–6.7B), and LLaMA (7B) on five instruction-following datasets, using both Rouge-L and GPT-4 feedback. MiniLLM outperforms all baselines (SFT, word-level KD, SeqKD) in almost every setting. In several cases (e.g., OPT 1.3B DollyEval: 52.6 → 60.7 GPT-4 score) gains are large; across OOD datasets (S-NI, UnNI) gains are especially clean, undercutting an in-distribution familiarity explanation. Figure 1 further shows this trend holds across size scaling.

- **Multi-faceted evaluation.** The paper includes Rouge-L for precision, GPT-4 feedback for overall quality, and human evaluation (Figure 6, LLaMA family, SelfInst) that corroborates GPT-4 rankings. Additional analyses of exposure bias, calibration (ECE on SST2 and BoolQ), generation diversity (Distinct-4), and long-text performance on S-NI subsets strengthen confidence in the results.

---

## Weaknesses

### Fatal
None.

### Major

- **Training regime and objective are conflated; the central ablation does not isolate the divergence choice.** MiniLLM changes two things simultaneously relative to all baselines: (a) forward KLD → reverse KLD, and (b) teacher-forcing / static-data training → on-policy sampling from the student at each step. Critically, the paper itself attributes part of the gains to on-policy training: Section 3.2 explicitly states that "MiniLLM is optimized with policy optimization methods, which samples responses from student models during training and thus alleviates exposure bias," and Figure 4 (exposure bias) quantifies this effect. A forward-KLD objective trained with the same on-policy policy-gradient procedure would also eliminate exposure bias while varying only the divergence. The ablation in Section 3.3 tests only whether the three engineering tricks help; it does not test "on-policy forward KLD vs. on-policy reverse KLD." As a result, the paper's title-level claim—that reverse KLD *specifically* is the right divergence for LLM distillation—is not cleanly supported by the evidence presented. The results are real and consistent, but they do not cleanly attribute the gains to the divergence choice rather than the training regime. This is an evidential gap, not a structural flaw in the method.

### Minor

- **The importance-weight approximation is a significant design decision that receives no bias analysis.** In Section 2.2, after deriving an unbiased importance-weighted estimator with $w_t = \prod_{t'=1}^{t} q_\theta(y_{t'})/\widetilde{p}(y_{t'})$, the paper immediately truncates to $w_t \approx q_\theta(y_t)/\widetilde{p}(y_t)$, discarding up to $T-1$ per-token ratio terms and rendering the estimator biased. The paper justifies this with "reduces variance" and cites deep RL papers, but provides no analysis of the resulting bias magnitude, no ablation comparing full vs. truncated importance weights, and no discussion of how the approximation error scales with sequence length. This widens the gap between the theoretical derivation and the practical algorithm without adequate accounting.

- **Calibration analysis lacks procedural specification.** Section 3.2 reports ECE for generative LLMs (LLaMA-7B) on SST2 and BoolQ without describing how class probabilities are extracted—a non-trivial step for decoder-only models (e.g., comparing log-likelihoods of "Yes"/"No" at the output position). Different extraction procedures yield materially different ECE values. This secondary claim is interesting but cannot be properly evaluated or reproduced as written.

- **Computational overhead of MiniLLM is not discussed.** MiniLLM requires sampling full responses from the student at every training step, analogous to RLHF, which is substantially more expensive than training on a static dataset (SFT, word-level KD, SeqKD). For configurations where the GPT-4 gain is modest (e.g., GPT-2 340M on DollyEval: 51.9 → 52.2), practitioners need this information to make an informed deployment choice.

### Trivial

- **$\alpha = 0.2$ for teacher-mixed sampling is fixed without ablation.** Section 3.1 states "We set the teacher-mix-in strength $\alpha=0.2$ throughout the experiments" with no sensitivity analysis. Given that this hyperparameter directly controls the shift toward the teacher distribution, and that student capacity varies from 120M to 13B, its robustness is a legitimate open question.

---

## Nice-to-Haves

- The most actionable improvement would be adding a baseline: forward KLD optimized on-policy (sampling from the student, computing the forward gradient). This would directly isolate whether the reverse divergence or the on-policy training regime drives the gains, and would make the paper's central claim verifiable.

- An ablation on the full vs. truncated importance-weight product—even at one model scale—would substantially clarify the bias-variance trade-off of the approximation in Section 2.2.

- Reporting wall-clock or GPU-hour comparisons versus SeqKD/word-level KD would help practitioners assess the method's cost-benefit profile.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "GPT-4 systematically favors MiniLLM's output style."** While plausible in principle, this concern is substantially weakened by the paper's use of Rouge-L as a complementary metric and human evaluation (Figure 6). Both metrics point in the same direction. Downgraded to not worth listing as a weakness, since the multi-metric design largely addresses the concern.

- **Harsh Critic: "DollyEval in-distribution gains may reflect format familiarity."** The paper itself notes that "MiniLLM generally works much better on datasets other than Dolly compared with the baselines, indicating its good out-of-distribution generalization" (Section 3.1). The concern is partially acknowledged and the OOD results are the more important evidence. Downgraded; not a weakness to retain.

- **Harsh Critic: "Toy Gaussian-mixture example is too stylized."** While the example cannot *prove* the effect is severe in practice, it correctly illustrates the mode-averaging vs. mode-seeking distinction and provides appropriate intuition. No specific paper claim is invalidated. Removed as scope-creep speculation.

- **Harsh Critic: "Length normalization theoretical justification is imprecise."** The ablation in Table 5 (validation R-L drops from 27.4 to 17.4 without it) provides empirical grounding. The critic's question about whether it introduces non-uniform reward scaling is an interesting open question but is not shown to cause observable harm. Removed as speculative.

- **Strength Finder: "Important problem" / "interesting research direction."** Generic; removed per filtering rules.

---

## Novel Insights

The paper's most under-appreciated observation is that policy-gradient-trained student models can *surpass* their teachers on Rouge-L for some datasets (marked ★ in Table 1, e.g., GPT-2 760M on SelfInst: student 44.6 vs. teacher 42.9). This is directly attributable to the on-policy training regime eliminating the teacher model's own exposure bias—a consequence of teacher-forcing fine-tuning that the teacher model itself suffers from. This suggests that teacher-forcing fine-tuning is a performance bottleneck for teacher models as well, and that policy-gradient distillation may effectively correct the teacher's own systematic generation errors, yielding students that outperform teachers on certain metrics. This insight extends beyond knowledge distillation to question the standard evaluation assumption that a teacher trained with teacher-forcing is a reliable upper bound.

---

## Suggestions

1. **Run forward KLD on-policy as a baseline.** This is the most impactful single experiment the paper is missing. Sample from the student, compute the forward KLD gradient, and compare to the full MiniLLM. This directly tests whether the divergence or the training regime drives the gains.

2. **Add a truncation ablation for importance weights.** Compare the single-step approximation against the full product (or at least a partial $k$-step product) on one model pair to characterize the bias-variance trade-off.

3. **Describe the calibration extraction procedure.** Add one sentence to Section 3.2 specifying exactly how class probabilities are extracted from the generative model for ECE computation on SST2 and BoolQ.

4. **Report training time comparisons.** A wall-clock table relative to SeqKD would let practitioners weigh the performance-compute trade-off.

---

## Score and Decision

**Round 1 Bracket:** Based on the three anchor bands:
- Weak (≤3): Rejected low-quality KD/alignment papers with fundamental flaws.
- Middle (4–7): LLM distillation papers ranging from narrow/marginal (4.0) to multi-family, solid evaluation (7.0). The 6.0 anchor (Multi-Granularity LLM distillation) is REJECTED and has marginal, complex results. The 7.0 anchor ("False Promise") is accepted analysis work.
- Strong (≥8): Typically clean methodology, strong evaluation, excellent presentation (Self-Alignment at 8.0).

**Initial bracket: 6.5–8.0.** MiniLLM is clearly better than the rejected 6.0 KD anchor and the 5.67 anchor; it is likely below the 8.0 Self-Alignment anchor (which has cleaner methodology and 4/4 soundness ratings).

**Round 2 Narrowing (within 6–8):**
- **Ixi4j6LtdX (6.75)** – Teacher-Student Collaborative KD, accepted. Smaller scale, meta-learning approach. MiniLLM has broader experiments and more principled motivation. MiniLLM is better than this anchor.
- **8wjWm5jr1w (6.0)** – Multi-Granularity LLM distillation, REJECTED. Marginal improvements, overly complex, only Rouge-L evaluation, no human eval. MiniLLM is clearly stronger.
- **Kz3yckpCN5 (7.0)** – "False Promise," accepted. Analysis paper with broad experiments but no new method. MiniLLM proposes a new method with more comprehensive evaluation (3 families, 5 datasets, human eval) and consistent improvements. Comparable in terms of contribution significance.
- **1oijHJBRsT (8.0)** – Self-Alignment, accepted. 4/4 soundness, novel method, clean claims, comprehensive evaluation. MiniLLM is below this due to the major evidential gap on the divergence/training-regime conflation.

**Final comparison:** MiniLLM is better than the 6.0–6.75 anchors (broader scope, human eval, non-marginal gains). It is comparable to the 7.0 "False Promise" anchor—arguably stronger as a new method contribution, but offset by the training-regime conflation. It is meaningfully below the 8.0 anchor in terms of methodological cleanness. Score: **7.0**.

**Anchor summary (all retrieved):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 8TbqoP3Rjg | 2.0 | R1 | Rejected KD paper; far below MiniLLM |
| Wv9Gl1bFbc | 3.0 | R1 | Rejected self-distillation; below MiniLLM |
| ijwYWoChN9 | 3.0 | R1 | Rejected domain-shift tuning; unrelated |
| 28TLorTMnP | 2.5 | R1 | Rejected alignment; unrelated |
| 1TJSnL3ywS | 4.0 | R1 | Rejected MCQA distillation; below MiniLLM |
| 8wjWm5jr1w | 6.0 | R1/R2 | Rejected LLM distillation; MiniLLM clearly stronger |
| uZ5K4HeNwd | 7.0 | R1 | Accepted self-distillation for speed; different problem |
| IcVSKhVpKu | 5.67 | R1 | Accepted hidden-state KD; narrower scope |
| 1aF2D2CPHi | 8.0 | R1 | Accepted data-free KD for CLIP; different domain |
| tyEyYT267x | 8.0 | R1 | Accepted diffusion language models; different problem |
| f4gF6AIHRy | 8.0 | R1 | Accepted pre-training data selection; unrelated |
| 51WraMid8K | 8.0 | R1 | Accepted probabilistic evaluation; unrelated |
| XnX7xRoroC | 6.25 | R2 | Rejected RL dataset distillation; unrelated |
| Ixi4j6LtdX | 6.75 | R2 | Accepted meta-policy KD; MiniLLM stronger |
| e2NRNQ0sZe | 6.25 | R2 | Accepted RL+LLM priors; unrelated |
| tr0KidwPLc | 7.33 | R2 | Accepted LLM evaluation; different problem |
| Kz3yckpCN5 | 7.0 | R2 | Accepted "False Promise"; comparable importance, MiniLLM more constructive |
| 1oijHJBRsT | 8.0 | R2 | Accepted self-alignment; above MiniLLM in methodological cleanness |
| sGqd1tF8P8 | 6.8 | R2 | Accepted weak LLM as teacher; different approach |

**Originality:** High — proposes a principled divergence switch backed by theoretical and empirical motivation for a largely unaddressed problem (white-box KD of LLMs).  
**Importance:** High — LLM compression is a pressing practical problem; the method works broadly.  
**Claim support:** Moderate — the gains are real and consistent, but the attribution to reverse KLD specifically is not clean.  
**Experimental soundness:** Good — 3 model families, 5 datasets, 3 metrics including human eval, meaningful ablations.  
**Clarity:** Good — method is well-described; calibration procedure underspecified.  
**Community value:** High — practical method readily applicable; concurrent work (GKD, f-div-kd) validates timeliness.

**Final score: 7.0 (Accept)**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>