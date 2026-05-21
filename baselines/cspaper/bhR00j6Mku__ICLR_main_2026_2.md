---
job_id: 858c1f47-8d95-4936-9f90-2f9d9d2287db
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: bhR00j6Mku.pdf
paper: On The Fragility of Benchmark Contamination Detection in Reasoning Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly within ICLR scope, at the intersection of reinforcement learning, LLM/LRM evaluation, privacy-style membership inference, and trustworthy ML.

## Minimum Quality
Pass ✅ The submission contains the required scientific components, including abstract, introduction, related work, methodology/theoretical analysis, experiments, quantitative results, and conclusion. While I have technical and positioning concerns, the work is complete enough and sufficiently substantive to warrant full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, manipulative instructions, or suspicious text aimed at influencing automated review.

# Expected Review Outcome:
## Summary
This paper studies benchmark contamination detection for large reasoning models under two practical scenarios: contamination introduced during the SFT-to-RL pipeline when a base model becomes an LRM, and contamination applied as a final CoT-SFT stage to an already strong LRM. The main empirical claim is that SFT contamination can often be detected initially, but subsequent PPO-style RL, especially GRPO, substantially reduces the effectiveness of many existing detectors, while final-stage CoT contamination on advanced LRMs often leaves only weak member versus non-member signals. The paper also provides a theoretical argument that importance sampling and clipping in PPO-style objectives are central to the concealment effect, and supports this with RAFT/RAFT++/GRPO ablations.

## Strengths
1. The paper asks an important and timely question. Benchmark contamination is already a serious concern for LLM evaluation, and the paper sharpens this into a more specific concern for LRMs, where long CoT outputs and post-training pipelines make contamination detection meaningfully harder than in standard next-token settings. That problem formulation is useful and relevant to the ICLR community.

2. The empirical coverage in the main paper is fairly broad. The authors evaluate **10 contamination detection methods** across multiple categories, including generation-based, perturbation-based, reference-based, and reference-free approaches, and do so across six reasoning benchmarks and multiple model families. This breadth gives the paper more value than a narrow “one detector, one dataset” study.

3. **Table 2** is one of the strongest pieces of evidence in the paper. The systematic AUROC drop after GRPO is not an isolated anecdote, it appears across nearly all detector families, with especially sharp declines for reference-free methods such as Loss, Min-K%, and Max-K%. For example, the average AUROC for Loss drops from **75.48** before RL to **61.26** after RL with clean data, and Max-K% drops from **69.83** to **52.35**. This broad degradation pattern supports the central claim much better than a single benchmark would.

4. The paper does a good job using figures to tell the story. **Figure 2** is particularly effective because it shows the trend over RL steps rather than only before/after snapshots. The monotonic decline for GRPO and RAFT++, contrasted with the relative stability of RAFT and further SFT, makes the “concealment is tied to PPO-style RL rather than merely more training” claim substantially more convincing. Likewise, **Figure 3** gives a concrete visual explanation for why log-probability-based detectors degrade, the member and non-member distributions become much closer after RL.

5. The RAFT versus RAFT++ versus GRPO comparison is a meaningful strength. The paper does not stop at “RL makes detection worse,” it tries to isolate which part of the RL objective matters. **Table 3** is useful here: clipping-enabled RAFT++ and GRPO show large AUROC drops, while removing clipping leaves detector performance much closer to the pre-RL baseline. Even if I have reservations about the theorem, this ablation is informative.

6. The Stage II result is interesting and potentially unsettling for current practice. **Table 4** shows that final-stage SFT contamination with CoT can substantially inflate pass@1 for already-strong LRMs, for example DeepSeek-R1-Distill-Qwen-14B improves from **59.83** to **69.24** average pass@1. At the same time, **Table 5** shows that many detectors sit only modestly above chance, which supports the paper’s broader argument that memorization-style contamination detection may not transfer cleanly to LRM settings.

7. The paper is generally readable, and **Figure 1** is a helpful framing device. The two-stage contamination taxonomy, pre-LRM versus post-LRM, makes the paper easier to follow and helps separate two distinct failure modes that could otherwise be conflated.

## Weaknesses
1. The strongest weakness is overclaiming relative to the experimental scope. The paper repeatedly argues that “existing contamination detection methods are fragile” and sometimes implies a broad failure of contamination detection in LRMs, but the evaluated methods are still heavily concentrated around output-level memorization, log-probability, calibration, and diversity signals. This is a meaningful slice of the literature, but not the whole detection space. In particular, the paper does not evaluate performance-based contamination detectors, gradient-based detectors, or other non-memorization-centric approaches. Because of that, the conclusion should be narrowed to something like: *many commonly used output-based detectors degrade badly under these LRM settings*. As written, the claim reads broader than the evidence supports.

2. Relatedly, the paper’s literature positioning is incomplete in a way that matters scientifically, not cosmetically. The experimental benchmark omits some relevant families of contamination detection methods that could challenge the headline. A concrete example is **ConStat** (Dekoninck et al., 2024), a performance-based contamination detection method that does not rely on exactly the same member versus non-member loss separation that the paper argues RL collapses. This matters because the entire paper is framed around the fragility of “contamination detection,” but most tested methods share a similar statistical backbone. Without stress-testing stronger or orthogonal detection paradigms, the paper risks proving fragility of one family and then rhetorically extending it to the full problem.

3. The theoretical analysis is interesting but considerably weaker than the prose suggests. In **Section 3.2** and **Theorem 3.1**, the derivation relies on a highly idealized setting: tabular model, small natural-gradient step, success-conditioned expectations, and assumptions about member versus non-member success rates and variance structure. That is already a fairly narrow regime. More importantly, the central experimental setup in **Table 2** emphasizes **RL w/ Clean**, where RL is run without member benchmark samples, while the theory explicitly assumes “the RL training is performed on the benchmark data (i.e., training data is the combination of members \(M\) and non-members \(N\))” on **Page 7**. That mismatch is not small. If the theorem is meant to explain the main phenomenon under clean RL, the paper needs to explain why an analysis assuming RL on \(M \cup N\) still illuminates the reported clean-RL concealment effect.

4. There are several mathematical notation and derivation issues that reduce confidence in the theorem. In **Equation (4)**, the paper defines token-level weights \(w_t=\rho_t m_t\), yet in the GRPO objective in Appendix B the importance ratio is written at the sequence level, \(\pi_\theta(o_i\mid q) / \pi_{\theta_{\text{old}}}(o_i\mid q)\), while the main theorem reasons token-by-token. The correspondence between these two objects is not made explicit. Also, the masking variable \(m_t \in \{0,1\}\) is introduced as if clipping simply turns gradients on or off, but the PPO clipped objective is sign-dependent in the advantage and is not generally captured by a binary “no gradients if clipped” mask in such a simple way. This simplification shows up already in Appendix C, **Equation (8)**. The resulting derivation may still capture intuition, but the current mathematical presentation is too loose for the paper’s “root cause” claim.

5. The Stage II setup is somewhat extreme and may overstate practical vulnerability. On **Page 8-9**, the paper defines “extensive contamination with CoT” as **SFT exclusively on the member data** for the final stage. That is a strong and arguably unrealistic intervention. In real post-training pipelines, one would usually mix benchmark-like data with broader clean instruction/reasoning data, not train exclusively on the benchmark members. The appendix even suggests that mixing clean and member data can lead to smaller inflation for some LRMs. So the main-paper claim that post-LRM contamination “barely leaves evidence” should be qualified as holding under an intentionally aggressive contamination recipe, not necessarily under realistic fine-tuning mixtures.

6. Some of the textual claims are too strong relative to the actual numbers in **Table 5**. The paper says that “almost all detection approaches consistently perform near random guess in all the benchmarks,” but the table includes several results that are meaningfully above chance. For instance, LiRA on DS Qwen-14B averages **65.55** AUROC, and Loss on DS Llama-8B averages **62.59**. These are not great, but they are not “near random” in the ordinary sense either. This matters because the paper is making a fragility argument, and exaggerating the degree of failure weakens credibility.

7. The evaluation protocol for detectors is not fully satisfying in the main paper. On **Page 3**, each question is scored by averaging detector values over **8 generated responses**. That choice can materially affect AUROC, especially for stochastic reasoning models with long CoT. The authors defer much of the rationale to the appendix. I do not object to the choice itself, but if the main claims depend on rollout-averaged detector scores, the main paper should more directly justify why 8 rollouts is appropriate, whether results are stable to 1, 4, 16 rollouts, and whether some detectors benefit disproportionately from this averaging.

8. The core mechanism analysis leans heavily on log-probability distributions, but the argument that concealment is specifically about clipping rather than broader calibration or entropy reduction is still somewhat incomplete. **Figure 3** is a useful diagnostic, and **Figure 2** supports the trend, but these figures mainly show distribution convergence, not causal attribution. The authors do run RAFT/RAFT++/GRPO ablations, which helps, but the paper still bundles together several possible effects, entropy reduction, changes in response style, reward-conditioned trajectory selection, and clipping-based reweighting. The “root cause” language should be softened to “a plausible primary driver supported by theory and ablation” unless the mechanism is isolated more cleanly.

9. The paper’s practical recommendations in **Section 5** are weaker than the strength of the empirical findings. “Release more intermediate checkpoints” is reasonable but not likely to be adopted by the very actors whose incentives are being questioned, and “develop detectors beyond memorization” is directionally correct but underspecified. Since the paper is framed as exposing a serious evaluation vulnerability, it would benefit from at least one more concrete protocol-level mitigation in the main paper, for example hidden test sets, time-shifted benchmarks, confidential evaluation, or benchmark refresh procedures.

10. The work is mainly concentrated on reasoning-heavy math/science benchmarks in the main text. That is defensible for LRMs, but it limits how broadly the conclusions should be read. The appendix includes non-math domains, but the main paper itself gives a much narrower view. In particular, the Stage II “generalization washes out member/non-member separability” story may depend strongly on benchmark homogeneity and the nature of long-form reasoning tasks.

## Questions
1. The theory in **Section 3.2** assumes RL training on a benchmark data mixture containing both \(M\) and \(N\), but the main empirical punchline in **Table 2** is that even **RL w/ Clean** degrades detectability. Can the authors explain more directly why the theorem should be viewed as explanatory for the clean-RL case? A concise argument connecting the assumptions to the experimental regime would increase my confidence.

2. Can the authors clarify the token-level versus sequence-level treatment of the importance ratio? In Appendix B, GRPO is written with a sequence-level ratio \(\pi_\theta(o_i\mid q)/\pi_{\theta_{\text{old}}}(o_i\mid q)\), while the theorem uses token-level \(w_t=\rho_t m_t\). Please explain the exact mapping used in the analysis, and whether any approximation is involved.

3. The clipped PPO gradient in Appendix C, **Equation (8)**, appears simplified. Is the binary mask \(m_t\) intended as an exact gradient representation or only a notational convenience under additional assumptions on the sign of \(A_t\)? Please state this explicitly. If approximate, the theorem statement should probably be toned down.

4. Could the authors provide a more direct comparison to at least one contamination detector outside the log-probability / memorization family, ideally a performance-based or gradient-based method? This would significantly sharpen the scope of the “fragility” claim.

5. For Stage II, how sensitive are the conclusions in **Table 4-5** to the contamination recipe? In particular, what happens if the final SFT stage mixes clean data with member CoT rather than using member-only SFT? If the effect weakens substantially, the practical claim should be narrowed.

6. The paper often describes Stage II detector performance as “near random.” Would the authors consider revising this language to reflect the actual spread in **Table 5**, where several results are still in the low-to-mid 60s? A more calibrated statement would improve credibility.

7. Since **Figure 2** suggests a monotonic degradation trend, can the authors quantify the trade-off between leaderboard inflation and detectability as RL steps increase? A plot of pass@1 improvement versus AUROC drop would make the practical implications much clearer.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper identifies concrete ways in which model developers could contaminate benchmarks while reducing the effectiveness of current detection methods, especially through PPO-style RL and final-stage CoT SFT. This is scientifically important, but it also has a dual-use aspect: the methodology could help bad actors game public leaderboards while leaving weaker traces. The public code release mentioned on **Page 1** and in the reproducibility section may increase that risk if not handled carefully. I do not view this as a reason to reject the paper, but it does merit ethics attention and a more explicit discussion of safeguards or responsible release choices.

## Soundness Rating
3: good. The empirical evidence is substantial and supports the main descriptive claim that many tested detectors degrade under the studied LRM contamination settings. However, the theoretical “root cause” claim is not as airtight as the paper suggests, due to assumption mismatch and derivational simplifications.

## Presentation Rating
3: good. The paper is generally well organized, and the figures and tables are helpful, especially Figure 1, Figure 2, Figure 3, Table 2, and Table 3. Still, several claims are overstated, and the mathematical exposition in Section 3.2 / Appendix C is not as clean as it should be.

## Contribution Rating
3: good. The paper makes a useful empirical contribution by highlighting a real evaluation vulnerability in LRMs and by distinguishing two contamination stages with different failure modes. I do not think the contribution reaches the level suggested by the broadest claims, partly because the benchmark of detection methods is narrower than the rhetoric.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem, presents substantial empirical evidence, and contains a genuinely useful cautionary message for LRM evaluation. I am positive overall, but only marginally so, because the “existing methods are fragile” claim is broader than what is actually tested, and the theoretical mechanism analysis is more suggestive than definitive.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main empirical and mathematical claims carefully, though I am less convinced by the theorem than by the experiments.