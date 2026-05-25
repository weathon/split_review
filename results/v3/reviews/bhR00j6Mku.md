Now I have all the information I need. Let me synthesize the review.

**Anchor Summary (all retrieved anchors across rounds):**

**Round 1 - Topic Low:**
- SaOxhcDCM3 (3.20) - self-consuming training loop. Unrelated topic, not comparable.
- RuY1r1PDdQ (3.00) - instruction following evaluation. Unrelated.
- YrycTjllL0 (3.00) - code generation benchmark. Unrelated.
- lUyYX9VFgA (3.00) - AI safety prompting. Unrelated.

**Round 1 - Topic Mid:**
- Nk1MegaPuG (4.25) - "Evading Data Contamination Detection for Language Models is (too) Easy". Most topically similar (evading detection). The current paper is significantly stronger: more thorough experiments, theoretical grounding, clearer presentation.
- zWqr3MQuNs (6.25) - "Detecting Pretraining Data from Large Language Models". Proposed new detection method + benchmark. Accepted. Current paper has comparable empirical rigor.
- m2NVG4Htxs (6.75) - "To the Cutoff... and Beyond?" Longitudinal contamination analysis. Accepted. Similar level of empirical depth.
- rAylWUIKtu (4.25) - "Benchmark Inflation". Limited scope (one benchmark). Current paper is broader and more thorough.

**Round 1 - Topic High:**
- All 8.00 papers. Different topics (training on test task, reward models, synthetic data detection). Current paper is not at this contribution level.

**Round 1 - Weakness Queries:**
- Nk1MegaPuG (4.25) - already covered.
- Nsms7NeU2x (6.75) - "How much can we Forget about Data Contamination?" Different focus (forgetting vs. concealment). Strong but rejected.
- EE2tIwKhSW (5.50) - "Real-World Benchmarks Make MIAs Fail on Diffusion Models". Similar message (methods fail under realistic conditions). Current paper has deeper analysis (theory + ablation) and is stronger.
- Various unrelated papers (3.00-5.33).

**Round 2:**
- hpeyWG1PP6 (5.75) - "TDDBench". Benchmark paper, different contribution.
- 9QPH1YQCMn (6.25) - "Infilling Score". New detection method, different contribution.
- 6bcAD6g688 (5.75) - Data credibility. Different topic.
- lwtaEhDx9x (4.75) - Memorization of tabular data. Different topic.

**What did low-band anchors fail at, and does the paper share those failures?** The most comparable low-band anchor (Nk1MegaPuG, 4.25) failed due to unclear presentation, insufficient experiments, and lack of technical depth. The current paper does NOT share these failures: it has clear presentation, extensive experiments across 10 detection methods × 6 benchmarks × multiple model families, and substantive theoretical analysis with controlled ablations.

**Initial bracket:** 5.5–7.0. **Final score after narrowing:** 6.5.

Now I'll write the complete review.

One final check on weaknesses I want to include vs. move to Removed Points:

**KEEP as Minor:**
1. "Near random" overstatement - The paper says "AUROC ≈ 50%" but Table 5 data shows individual methods reaching 70-79% on specific benchmarks. The overall point stands but the wording overstates.

2. Missing variability estimates - No confidence intervals or error bars across different member/non-member splits. AUROCs averaged over 8 rollouts but split sensitivity unreported.

3. Stage II generalization hypothesis indirectly supported - The explanation (internalization of reasoning patterns rather than memorization) is plausible but not directly tested.

**MOVE to Nice-to-Have:**
1. Include additional RL algorithms (e.g., PPO)
2. Stage II analysis with embedding similarity
3. Detection methods based on generated CoT structure

**REMOVE (to Removed Points):**
1. Implementation details in appendix - Parser artifact.
2. Theoretical analysis simplified - Paper explicitly acknowledges this.
3. Computational cost confound - Speculative, no evidence.
4. Theoretical analysis limitations acknowledgement - Already in paper.

Now writing the review.## Summary

This paper presents the first systematic study of benchmark contamination detection in Large Reasoning Models (LRMs), examining two practical contamination scenarios: (I) contamination introduced during SFT that is initially detectable but can be concealed through subsequent RL (GRPO) training, and (II) contamination with chain-of-thought (CoT) applied to advanced LRMs that barely leaves detectable evidence. Through extensive experiments across 10 detection methods, 6 reasoning benchmarks, and multiple model families (Qwen2.5, Llama-3.1, DeepSeek-R1-Distill, OpenThinker), the authors demonstrate that existing contamination detection methods are critically fragile under LRM contamination. The key mechanistic finding — that PPO-style importance sampling and clipping objectives drive the concealment in Stage I — is supported by both theoretical analysis and controlled ablations.

## Strengths

1. **First systematic demonstration that RL training (GRPO) conceals SFT contamination evidence in LRMs.** Table 2 shows a consistent and substantial AUROC drop across all 10 detection methods after GRPO (e.g., Loss detector drops from 75.48% to 61.26%), while Table 1 shows the model retains inflated performance. Figure 2 confirms a monotonic decrease with more GRPO steps, and controls (further SFT, RL on clean&mem) rule out the forgetting hypothesis.

2. **Pinpoints PPO-style importance sampling and clipping as the root cause through theory + controlled ablation.** Theorem 3.1 provides formal analysis showing why the membership gap contracts under PPO-style objectives. Table 3 validates this: removing clipping from GRPO or RAFT++ eliminates concealment (AUROC returns to near no-RL levels), while plain RAFT (no clipping/importance sampling) does not conceal — a clean causal identification.

3. **Demonstrates that CoT contamination on advanced LRMs yields large performance inflation with near-random detection performance.** Table 4 shows performance gains of 7.76–15.76% after SFT contamination with CoT, yet Table 5 shows all detection methods performing near random (average AUROC ~55-60%). Figure 4 shows member/non-member log-prob distributions overlap, indicating LRMs generalize to unseen samples rather than memorizing — undermining the core assumption of existing detectors.

4. **Comprehensive and well-controlled evaluation.** The study covers 10 detection methods spanning generation-based, perturbation-based, reference-based, and reference-free approaches, across 6 diverse reasoning benchmarks and multiple base models / LRM families. Controlled experiments (further SFT, RL on clean&mem, removing clipping) systematically exclude alternative explanations.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"Near random" claim slightly overstated for Stage II.** The paper states detection methods "perform near random guesses (i.e., AUROC ≈ 50%)" in Stage II (abstract, Table 5 caption, Section 4). However, Table 5 shows several method/benchmark combinations reaching 70–79% AUROC (e.g., LiRA at 75.56% on AIME25 with DS Qwen-14B; Min-K% at 77.33% on AIME24 with DS Qwen-14B; Loss at 77.56% on AIME24 with DS Qwen-14B). The average across all methods and models is approximately 55–60%, not 50%. The core finding — that detection is substantially degraded relative to standard LLM contamination scenarios — remains valid, but the "≈50%" framing overreaches. The authors should qualify this claim more precisely.

2. **No variability estimates on AUROC values.** The reported AUROCs are means over 8 rollouts, but there are no confidence intervals, error bars, or sensitivity analysis across different random splits of members/non-members. Given that the core claims rest on AUROC comparisons (e.g., before vs. after RL, across detection methods), readers cannot assess whether the observed differences are robust to the specific member/non-member split. This is a standard expectation for comparative claims.

3. **Stage II generalization hypothesis is indirectly supported.** The paper argues that LRMs internalize reasoning patterns rather than memorizing, causing non-members to also show increased confidence. This explanation is plausible and consistent with Figure 4, but a more direct test (e.g., quantifying embedding similarity between member and non-member questions and showing that confidence increase correlates with similarity) would substantially strengthen the argument.

### Trivial
None.

## Nice-to-Haves

- **Add PPO to the Stage I RL algorithm zoo.** The paper tests GRPO and RAFT++, claiming the mechanism applies to "a broad class of RL methods." Directly testing standard PPO (with clipped surrogate) would make the generality claim more concrete.
- **Explore detection methods that analyze the structure of generated CoTs.** The paper focuses on log-prob, verbatim, and membership inference methods but does not consider detectors that analyze reasoning trace structure (e.g., repetition patterns, token entropy within CoT, self-consistency). A brief discussion of why these are unlikely to succeed would be helpful.
- **Stage II generalization test via embedding similarity.** A direct analysis showing that confidence increase on non-members correlates with their embedding similarity to members would confirm the internalization hypothesis.

## Removed Points

These points were raised by reviewers but are not included as weaknesses in the main review (with justification):

1. **"Implementation details relegated to appendix"** — The paper refers to the appendix for hyperparameters, contamination splits, etc. The harsh critic acknowledged this is standard practice, and the parser strips appendix content. Not a paper flaw.
2. **"Theoretical analysis is simplified (tabular setting)"** — The paper explicitly states "We assume...tabula setting for simplicity" (line 188) and "To ease the analysis, we consider an idealized setting" (line 241). The simplification is transparently scoped, and the empirical ablation (Table 3) is the primary evidence. The critic also noted this is acceptable as intuition-building.
3. **"Computational cost confound"** — The suggestion that GRPO may be computationally heavier per step and thus the concealment could be an artifact of "more effective optimization" is speculative. The paper controls for number of training steps, and there is no evidence presented that this confound exists.
4. **"Theoretical analysis limitations could be more explicit"** — Already adequately acknowledged in the paper as noted above.

## Novel Insights

The merger of the two reviewer inputs surfaces an observation not explicitly stated in the paper: the two stages represent qualitatively different failure modes for detection. Stage I shows that an *algorithmic property* of the training procedure (PPO clipping) actively destroys the signal that detectors rely on, even though the signal was present after contamination. Stage II shows that the *model's generalization capacity* itself prevents the signal from forming in the first place. Together, these reveal that detection is fragile for orthogonal reasons — one about training dynamics, one about model capability — suggesting that a single detection strategy is unlikely to be robust against both. This dual fragility is a deeper finding than either stage in isolation and could inform the design of more principled detection approaches.

## Suggestions

1. Qualify the Stage II AUROC claims: replace "near random guesses (i.e., AUROC ≈ 50%)" with a more precise statement such as "detection performance is substantially degraded, with average AUROC of 55–60% across settings and individual methods occasionally exceeding 75%."
2. Add error bars or confidence intervals to the AUROC values in Tables 2 and 5, at minimum by bootstrapping over different member/non-member splits.
3. Include a direct test of the generalization hypothesis in Stage II by analyzing whether confidence gains on non-members correlate with embedding similarity to the member set.
4. Add a brief section or paragraph discussing what alternative detection approaches (e.g., analyzing CoT structure) might look like and why the paper's findings suggest they would face similar challenges.

## Score and Decision

**Round-1 bracket:** 5.5 – 7.0. Based on comparison with anchors: clearly stronger than Nk1MegaPuG (4.25) and EE2tIwKhSW (5.50); comparable to zWqr3MQuNs (6.25) and m2NVG4Htxs (6.75); well below 8.00 papers. **Round-2 narrowing:** Within the bracket, the paper is strongest among mid-5.x anchors and sits comfortably with 6.25–6.75 anchors. The paper does not share the core failures of the low-band anchor (unclear presentation, insufficient experiments, lack of depth). The minor weaknesses (overstated "near random" claim, missing error bars) prevent it from reaching 7+, but the strong empirical design, causal identification through ablation, and timely significance of the findings support a score of 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>