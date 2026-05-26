Now I have a thorough understanding of the paper. Let me compose the final consolidated review, applying the filtering discipline carefully.

---

## Summary

This paper presents the first systematic study of benchmark contamination detection in Large Reasoning Models (LRMs). It identifies two practical contamination scenarios: (Stage I) contamination introduced during SFT can be concealed by subsequent RL training (GRPO), and (Stage II) contaminating advanced LRMs with chain-of-thought (CoT) data via SFT yields large performance gains while leaving detection methods performing near random. The paper evaluates 10 detection methods across 6 reasoning benchmarks and 2 base models, and provides theoretical analysis attributing Stage I concealment to PPO-style importance sampling and clipping objectives.

## Strengths

1. **Comprehensive and well-designed empirical study.** The paper evaluates 10 detection methods (spanning generation-based, perturbation-based, reference-based, and reference-free approaches) across 6 benchmarks with 2 base models in Stage I and 4 LRMs in Stage II. The two-stage framing (pre-LRM and post-LRM) captures realistic contamination pipelines that prior work did not systematically examine. Tables 2 and 5 provide clear, across-the-board evidence that existing detection methods are fragile under both scenarios.

2. **Controlled experiments rule out alternative explanations.** The paper convincingly shows that the concealment in Stage I is not due to forgetting or merely training on more clean data: further SFT on clean data does *not* conceal contamination (Figure 2, Table 23), and the concealment grows monotonically with GRPO steps while performance inflation persists. This cleanly isolates the RL objective as the driver.

3. **Ablation studies causally identify the clipping mechanism.** Table 3 provides strong empirical evidence that removing the clipping term from GRPO or RAFT++ almost entirely restores detector performance (e.g., Loss detector AUROC drops only 2.20% without clipping vs. 14.22% with clipping in GRPO). This causal identification — not just a correlation — is the paper's most compelling mechanistic contribution.

4. **Stage II detection failure is robust across models and methods.** Table 5 shows that all 10 detection methods perform near random across 4 different LRMs after contamination with CoT. Even LiRA, the previous best method, averages only 58.74% AUROC. The log-prob visualization (Figure 4) explains why: both members and non-members shift upward together, breaking the separability that detectors rely on.

## Weaknesses

### Fatal
None.

### Major

1. **Theory assumes RL on benchmark data; main experiments use RL on clean data.** Theorem 3.1 explicitly assumes "the RL training is performed on the benchmark data (i.e., training data is the combination of members M and non-members N)" (line 188). However, the principal Stage I results (Table 2, Figure 2) are obtained from GRPO training on *clean, non-benchmark* data (DeepMath‑103K). The theoretical derivation — particularly the covariance terms that drive the gap contraction — uses properties of \(p_k(s)\) and advantages computed from the training distribution, which are not the same distribution when RL is on clean data. The "RL w/ Clean & Mem" condition in Table 2 is closer to the theory's assumption, but the paper's narrative emphasizes the clean-RL scenario as the primary threat model. The ablation studies in Table 3 empirically validate that clipping is the cause, but they likely also use clean data, which means the empirical support does not directly test the theory's stated assumptions. This disconnect between the theory's scope and the main experimental setup weakens the paper's claimed identification of the root cause. The authors should either extend the theory to cover off-distribution training, or clearly delimit which experiments the theory addresses and provide a separate explanation for concealment under clean-RL.

### Minor

1. **Stage II evaluation lacks a clean-training control for the performance inflation claim.** Table 4 shows that contamination with CoT yields large pass@1 gains, but there is no comparison with SFT on an equivalent amount of *clean* (non-benchmark) CoT data. Without this control, it is unclear how much of the observed improvement is attributable to contamination specifically versus additional training on reasoning traces. This does *not* undermine the paper's main Stage II finding — that detection methods fail — which stands independently. However, it weakens the subsidiary claim that "extensive SFT Contamination with CoT results in a huge performance inflation" since some of that gain may also be achievable through legitimate continued training. Adding an appropriate clean-SFT baseline would clarify the threat model.

2. **Uncertainty estimates for AUROC values would strengthen the analysis.** The reported AUROC values are averaged over 8 rollouts (line 55) but no variance or confidence intervals are reported. Given that some detection methods hover near 50% (random guess), bootstrapped CIs would help readers assess whether small differences are meaningful or simply noise. This is not a fatal omission — single-run evaluation at scale is standard in this field — but it would improve the paper's rigor.

### Trivial
- The "Clean" label in Tables 1–2 is later identified as DeepMath‑103K; stating this explicitly at first presentation would improve clarity.
- The paper could state more directly in Section 4 where the CoT responses for Stage II contamination come from (the appendix likely contains this, but it would help readers in the main text).

## Nice-to-Haves
- A side-by-side comparison of loss dynamics or gradient statistics for further SFT vs. GRPO on the same contaminated model, to deepen the mechanistic understanding of why RL conceals but SFT does not.
- Extending the evaluation beyond mathematical reasoning (e.g., coding benchmarks) would strengthen generality, though math is the primary domain of current LRMs and the paper's scope is already well-defined.

## Removed Points
These points from the inputs were removed because they are either factually inaccurate, already addressed in the paper, scope creep, or unverifiable from the available text:

- **"Training data for RL is not explicitly stated in the main text"** — The paper does state that GRPO uses 10K questions from DeepMath‑103K (line 91). The "Clean" label is explained later. This is a clarity preference, not a missing fact.
- **"Empirical support in Table 3 is convincing provided the RL algorithms were trained on the same clean data—yet this is not stated"** — While not stated with full explicitness in the captioned text, the ablation study is conducted in the same experimental context as the GRPO experiments (DeepMath‑103K). A minor clarification would help but the information is inferable.
- **"Source of CoT data for Stage II contamination should be specified"** — The paper references Appendix D.4 for additional implementation details (line 312). Since the appendix is parsed-stripped from this version, this may already be specified. I cannot verify it is missing.
- **"Evaluation is limited to mathematical reasoning benchmarks"** — This is a scope choice, not a weakness. The paper focuses on LRMs whose primary domain is math and science reasoning.
- **"More thoroughly analyze why further SFT on clean data does not reduce detectability while RL does"** — The paper already addresses this with the controlled experiment (Figure 2, Table 23 showing further SFT does not conceal). Deeper analysis would be nice but its absence is not a flaw.
- **"Report variance or confidence intervals"** — Downgraded from minor weakness to nice-to-have, as single-run benchmark evaluation is standard practice in this community.

## Novel Insights
None beyond the paper's own contributions. The paper's own findings — that RL conceals SFT contamination traces via PPO-style clipping, and that final-stage CoT contamination evades detection through generalization rather than memorization — are themselves the novel insights.

## Suggestions for Improvement
1. **Reconcile theory with experiments.** Either extend the theoretical analysis to the off-distribution (clean-RL) setting or clearly delineate which experimental condition the theory covers, and provide an alternative explanation for concealment under clean-RL. Given that the empirical ablation (Table 3) already demonstrates clipping's causal role, the paper could simply acknowledge that the theory most directly applies to the "RL w/ Clean & Mem" condition while the clean-RL concealment is an additional empirical finding.
2. **Add a clean-training control for Stage II.** Fine-tune the same LRMs on an equal number of non-benchmark CoT examples to isolate the contamination-specific component of performance inflation.
3. **Clarify the RL data used in Table 3.** Explicitly state whether the ablation experiments use the same DeepMath‑103K data or a different setup.

## Score and Decision
MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>