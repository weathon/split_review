Now I have a thorough understanding of the paper and the anchor landscape. Let me compose the final consolidated review.

## Final Review

## Summary
This paper presents the first systematic empirical study of benchmark contamination detection in Large Reasoning Models (LRMs), structured around two realistic contamination scenarios: (I) when a base model is contaminated during SFT and then undergoes RL training (GRPO), and (II) when an already-trained LRM receives final-stage SFT contamination with chain-of-thought data. Across 10 detection methods, multiple base models, and 6 reasoning benchmarks, the paper demonstrates that (a) GRPO training on clean data can conceal initially detectable SFT contamination, with PPO-style importance sampling and clipping identified as the root mechanism, and (b) CoT contamination of advanced LRMs leaves detection methods performing near random chance due to generalization rather than memorization.

## Strengths

1. **First systematic evaluation of contamination detection failures on LRMs across two practical training scenarios.** The paper tests 10 representative detection methods (generation-based, perturbation-based, reference-based, reference-free) on multiple base models (Qwen2.5-7B, Llama-3.1-8B, DeepSeek-R1-Distill variants, OpenThinker) across 6 benchmarks. The results in Table 2 show consistent AUROC drops after GRPO (e.g., Loss detector from 75.48% to 61.26% average), and Table 5 shows near-random detection (AUROC ~50–60%) for Stage II. This comprehensive evidence directly supports the fragility claim.

2. **Theoretical identification and causal isolation of PPO-style importance sampling/clipping as the concealment mechanism.** Theorem 3.1 decomposes the NLL drift into a mean and a covariance term, and the analysis across RAFT, RAFT++, and GRPO correctly predicts that clipping drives the member/non-member gap contraction. The ablation study in Table 3 provides direct causal evidence: removing clipping in GRPO restores detection (Δ = −2.20 vs. −14.22 with clipping), and RAFT++ with clipping drops 17.91 AUROC while RAFT++ without clipping drops only 1.09. This goes beyond prior work by explaining *why* RL hides contamination, not just that it does.

3. **Rigorous controlled experiments ruling out forgetting as an alternative explanation.** The paper explicitly tests whether further training simply makes the model forget contamination: Figure 2 shows that additional SFT on clean data does **not** conceal contamination (unlike GRPO), and Table 1 confirms that performance inflation persists after GRPO. These controls isolate the RL objective itself as the cause of concealment.

4. **Novel finding that CoT contamination on LRMs inflates performance via generalization, not memorization.** Figure 4 shows that after contamination, log-probability distributions of both members and non-members increase at a similar margin, indicating the model generalizes to distributionally similar unseen samples. This challenges the memorization-driven assumption underlying most prior detection methods and is a conceptually important observation for the field.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The theoretical analysis assumes RL training on benchmark data, but the strongest concealment result uses clean data.** Section 3.2 states: "We assume that the RL training is performed on the benchmark data (i.e., training data is the combination of members M and non-members N)." However, the key demonstration in Table 2 ("RL w/ Clean") shows concealment when GRPO is trained on *clean* (non-benchmark) data. The paper does not explicitly acknowledge this mismatch. The experimental ablations (Table 3, RAFT vs. RAFT++ vs. GRPO) and the "further SFT" control provide strong empirical evidence that the mechanism is real, and the theoretical story about gradient clipping plausibly extends to clean-data updates via global parameter effects. But the theory as written analyzes gradient updates on benchmark samples, leaving a gap between the theorem's assumptions and the experiment's setup. Adding a paragraph that bridges this gap would strengthen the paper's central claim.

2. **Stage II lacks a systematic clean-model detection baseline.** Table 5 reports near-random AUROC for contaminated LRMs, and Figure 4 provides clean-model AUROC for two models and two benchmarks (~0.48–0.50). However, a full clean-model column in Table 5 (showing detection AUROC on the *same models before any contamination*) would clarify whether detection methods already fail on LRMs in general—due to their long CoT and strong generalization—or whether the failure is specific to the contamination being concealed. The paper's discussion (Section 4) already argues that detectors lack access to training CoT and that LRMs generalize, so the overall finding stands, but a systematic baseline would sharpen the narrative and preempt this interpretive ambiguity.

3. **The Stage I experiments are confined to math/reasoning domains, leaving generalizability across domains unexamined.** The RL training uses DeepMath-103K (math data), and all six benchmarks are math/reasoning datasets. While this is a natural choice given the paper's focus on LRMs, the observed concealment could partly be an artifact of training on a distributionally similar domain. Testing on a non-math RL dataset (e.g., coding data) with a non-math benchmark would strengthen the generality claim. This is a scope limitation rather than a flaw, but it should be acknowledged.

4. **Several implementation details are deferred to the appendix.** The main text does not specify (a) the exact teacher model used for CoT distillation in Stage I, (b) the reward verifier used for GRPO, or (c) the number of RL steps typical in production LRMs for comparison. While these details are standard for appendix placement, including brief mention in the main text would improve readability and reproducibility for a paper making such strong claims about real training pipelines.

### Trivial
None.

## Nice-to-Haves
- **Report member/non-member pass@1 separately for Stage II (Table 4).** Showing whether the contaminated model improves more on members than non-members would directly test the generalization hypothesis. Currently Table 4 reports only overall pass@1.
- **Ablate the number of rollouts used for detection scoring.** The paper uses 8 rollouts per question; varying this number could reveal whether detection improves with more rollouts, which would be practically relevant for practitioners.
- **Quantify typical RL steps for comparison.** The paper states 156 steps is "far fewer than the steps used in some advanced open-sourced reasoning models" but does not give a typical number. A brief comparison (e.g., "production LRMs often use 1000+ steps") would calibrate the severity.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Critique of theoretical simplifications (tabular setting, small gradient steps, omitted std dev term):** The paper explicitly acknowledges these simplifications. The key prediction (clipping drives concealment) is empirically verified in Table 3. Expecting quantitative bounds or covering all real-world complexity is not standard for this type of theoretical analysis. This point was removed as generic/overly demanding.
- **Missing teacher model specification:** The paper defers implementation details to the appendix. Per policy, appendix-stripped content should not be treated as missing.
- **Formatting nitpicks and missing related works:** Per policy, these are not valid weaknesses.
- **"Missing appendix" or "missing proofs":** Per policy, the parser strips these sections from all papers.
- **Strength Finder claim about "rigorous controlled experiments ruling out forgetting":** This strength is retained as valid. The paper does indeed test this with two experiments (Tab. 1, Fig. 2, extra SFT).

## Novel Insights
None beyond the paper's own contributions. The review corpus did not surface observations that significantly reframe or extend the paper's findings.

## Suggestions
- Add a discussion paragraph in Section 3.2 acknowledging that the theorem assumes benchmark-data RL while the key experiment uses clean data, and provide a plausible extension (e.g., that policy updates on clean data affect the parametric policy globally, and the importance-sampling/clipping mechanism still adjusts relative gradient contributions in ways that reduce member/non-member discriminability).
- Add a "clean model" baseline column to Table 5 (or an equivalent supplementary table) showing detection AUROC on the uncontaminated LRMs. This would clarify whether the detection failure is inherent to LRMs or specific to contamination concealment.
- Explicitly state the teacher model used for CoT distillation and the reward verifier configuration in the main text.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:** Search for "benchmark contamination detection in large language models" across three score bands:

| Band | Anchor | Avg Score | Comparison |
|------|--------|-----------|------------|
| Weak (< 3.5) | RuY1r1PDdQ | 3.00 | Unrelated paper (instruction following evaluation) |
| Weak (< 3.5) | ly10tMV6cD | 3.25 | Unrelated (structure-rich text benchmark) |
| Middle (3.5–7.5) | Nk1MegaPuG | 4.25 | "Evading Data Contamination Detection" — similar topic but much weaker execution; lacks theoretical analysis and comprehensive experiments. **Current paper is substantially stronger.** |
| Middle (3.5–7.5) | zWqr3MQuNs | 6.25 | "Detecting Pretraining Data" — introduces Min-K% Prob detection method. Comparable rigor and impact. **Current paper comparable or slightly stronger** (more comprehensive evaluation, theoretical analysis). |
| Middle (3.5–7.5) | m2NVG4Htxs | 6.75 | "To the Cutoff... and Beyond?" — longitudinal contamination analysis. Similar quality. **Current paper comparable.** |
| Middle (3.5–7.5) | rAylWUIKtu | 4.25 | "Benchmark Inflation" — narrow scope (TruthfulQA only). **Current paper significantly stronger.** |
| Strong (> 7.5) | syThiTmWWm | 7.75 | "Cheating Automatic LLM Benchmarks" — different topic (benchmark gaming via output manipulation). **Current paper weaker in impact.** |
| Strong (> 7.5) | jOmk0uS1hl | 8.00 | "Training on the Test Task" — different contribution type. **Current paper weaker.**

**Bracket:** 5.5 – 7.5

**Round 2 — Narrowing within bracket:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| 4eJDMjYZZG — "Language Model Detectors Are Easily Optimized Against" | 6.00 | Similar negative-result paper showing detector fragility. The current paper is **stronger** — more comprehensive (10 detection methods vs. 3–4), includes theoretical analysis, and covers two distinct contamination scenarios. |
| Nsms7NeU2x — "How much can we Forget about Data Contamination?" | 6.75 | Similar contamination study with theoretical analysis. **Current paper comparable** — both have extensive experiments and theory, but the current paper's theory is more directly verified by ablations (Tab. 3). |
| sKYHBTAxVa — "LiveBench" | 7.33 | Constructive contribution (new contamination-free benchmark). **Current paper weaker** in terms of direct practical utility, though the contribution type differs (diagnostic vs. constructive). |
| zWqr3MQuNs — "Detecting Pretraining Data" (revisited) | 6.25 | **Current paper is stronger** — more comprehensive experimental design and direct mechanistic verification. |

**Final score determination:** The paper sits above the 6.00 anchor (Language Model Detectors) and is comparable to the 6.25–6.75 anchors. It does not reach the impact level of the 7.33+ papers, which typically provide constructive solutions (new benchmarks, new detection methods) rather than diagnostic findings. The weaknesses identified (theory-clean data gap, Stage II clean baseline) are real but minor and do not invalidate the core contributions. The comprehensive evaluation, theoretical mechanism identification, and controlled experiments make this a solid empirical contribution that clearly exceeds the 4.25 "Evading Data Contamination" paper on the same topic.

**Score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>