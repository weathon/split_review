Now I have everything I need to write the consolidated review. Let me synthesize the inputs against the paper content I've verified.

---

## Summary

This paper proposes High-Entropy Sum (HES), a training-free metric for data selection in LLM reasoning training. HES sums the entropy values of only the top 0.5% highest-entropy tokens in each reasoning sample, motivated by the hypothesis that those tokens correspond to critical reasoning "forking points." The authors validate HES across three training paradigms—SFT, RFT, and RL—finding that selecting the top 80% of training data by HES consistently outperforms training on the full dataset, and that even the top 20% approaches or exceeds full-dataset performance in multiple settings.

---

## Strengths

- **Clear discriminative power of HES (Figure 1, Table therein):** The paper provides direct empirical evidence that HES distinguishes correct from incorrect samples far better than competing entropy-based metrics. For 512 responses per problem sampled from Qwen3-14B on AIME 2025, the normalized mean HES for correct samples is 0.29 vs. 0.68 for incorrect—a gap nearly absent in AvgE (0.52 vs. 0.53) and AvgHE (0.82 vs. 0.82). This is concrete and compelling motivation.

- **Strong, large-margin SFT results replicated across models and domains:** Table 1 (Qwen3-8B-Base, Open-Math-Reasoning) shows Highest-HES-80% at 35.36% avg vs. Full-Dataset at 32.61%; Table 2 (DeepSeek-R1-Distilled-7B, OpenR1-Math-220k) shows Highest-HES-20% at 34.61% vs. Full-Dataset at 30.22%—a 4.39-point gain. Tables 3–4 extend this to Code and STEM domains. These margins are large enough to be credible without formal significance tests.

- **The Lowest-HES control is unusually strong evidence:** Lowest-HES-20% achieves only 14.90% average (Table 1), far below Random-20% (25.89%), establishing that low-HES samples are actively harmful rather than merely uninformative. This provides a bidirectional validation of the metric rarely seen in data-selection papers.

- **Comprehensive baseline comparison:** The SFT study (Table 1) pits HES against difficulty, length, average entropy (AvgE), average high-entropy (AvgHE), total entropy sum (ES), and absolute-threshold HES (HES_absolute). HES consistently wins or ties for best, with the ablation set being among the more thorough for this class of paper.

- **Cost-effective cross-model transfer:** Using a Qwen3-0.6B proxy to score data for Qwen3-8B-Base training achieves 32.12% vs. 31.14% for self-selection (Table 1), reducing inference cost by over an order of magnitude while maintaining quality. This is a practically significant finding.

---

## Weaknesses

### Fatal
None.

### Major

- **The mechanistic interpretation overclaims what the data can isolate.** The paper's central narrative—that HES "focuses on critical forking points"—is asserted as the causal mechanism, but the experiments cannot cleanly separate this from a joint length × peak-entropy effect. $HES_{relative}$ selects the top 0.5% of tokens by entropy; for a sequence of N tokens, that is ⌊0.005 · N⌋ tokens, so HES grows roughly linearly with length when peak entropy intensity is similar across samples. The AvgHE baseline (which normalizes out the count of high-entropy tokens) performs substantially worse (27.97 vs. 31.14 for the 20% subset, Table 1), which the paper presents as a win for HES—but it equally supports the interpretation that the *sum* is capturing length-weighted entropy rather than purely qualitative complexity. HES does outperform the Length baseline (30.67 vs. 31.14), so the pure-length story is ruled out; however, a combination of "longer AND more intense at forking points" cannot be separated from "more complex forking structure" without a length-controlled ablation. The paper should either weaken the mechanistic claim to match the evidence ("HES correlates with reasoning quality") or add a length-controlled comparison.

- **No statistical significance reporting for the RFT and RL results where margins are modest.** AIME24 and AIME25 each contain only 30 problems. The RFT per-query improvements are +1.01, +1.69, and +0.97 points for k=2, 4, 8 respectively (Table 5). The RL headline improvement is +0.67 points average (20.63% → 21.30%, Table 6), with HMMT25 moving in the *wrong* direction (15.21% → 11.88%). No confidence intervals, bootstrapped estimates, or multiple seed results are reported anywhere. The SFT findings at the 80% level are large enough to be robust without this, but the RFT and RL claims—which are explicitly presented as validated wins—require at minimum a brief uncertainty quantification to be trusted.

### Minor

- **RL experiments are underpowered for the "unified" claim.** The RL section uses a single model (DeepSeek-R1-Distilled-Qwen-1.5B) on a single dataset (DeepScaleR). The headline result (Pos-High, Neg-Rand = 21.30%) beats Full-Batch (20.63%) by only 0.67 points average, with HMMT25 degrading by 3.33 points. The asymmetric sampling design is interesting and the reasoning is sound, but a single data point makes it difficult to assess generalizability; the RL claim should be framed more tentatively than the SFT claim in the abstract and conclusion.

- **Which model computes HES is never stated explicitly for the primary experiments.** Section 4.1.1 describes two model choices (Qwen3-8B-Base and DeepSeek-R1-Distilled-7B) and mentions cross-model transfer with 0.6B/1.7B proxies, but does not explicitly state that the base model being trained computes HES on its own training set before training begins. Readers attempting reproduction need to know this, especially since computing entropy over 100,000 long-CoT samples with an 8B model is a non-trivial step.

- **Figure 1's discriminative analysis uses a different distribution than the training data.** The motivation is built on 512 responses per problem from Qwen3-14B on AIME 2025—a high-density sample from a capable model on hard problems. The actual training data (Open-Math-Reasoning, OpenR1-Math-220k) comes from smaller/different models. A similar discrimination plot on one of the training datasets would make the motivating evidence much tighter.

### Trivial
None worth flagging.

---

## Nice-to-Haves

- **Length-controlled ablation:** Within a length-matched subset (e.g., responses between 2,000–3,000 tokens), compare HES-selected vs. random. If HES still wins meaningfully, the length confound interpretation is addressed. This single experiment would substantially strengthen the mechanism story.

- **Token-level qualitative analysis:** A small-scale analysis showing that the top-0.5% entropy tokens in high-HES samples cluster at genuine reasoning decision points (branching, strategy switches, self-correction) rather than at random linguistic positions would directly validate the "forking points" hypothesis the paper rests on.

- **Broader RL coverage:** Running the asymmetric sampling experiment on at least one additional model or dataset would transform the RL finding from "promising single observation" to "replicable result."

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Harsh Critic: Post-hoc rationalization of HES_relative's adaptive robustness (footnote 1).** The critic called the footnote's explanation "a post-hoc rationalization." While arguably true, this is a presentation-style concern rather than a substantive methodological flaw—footnotes regularly synthesize empirical observations. **Removed** as a pure style nitpick.

2. **Harsh Critic: Section 4.4 MMLU STEM / LiveCodeBench insensitivity as a limitation.** Figure 4 shows all four token ratios produce identical scores on MMLU STEM and LiveCodeBench. The critic suggests this should be noted as a limitation. While mildly interesting, this is actually consistent with the story that easier/less-reasoning-intensive benchmarks are less sensitive to the selection criterion. It doesn't undermine any core claim. **Removed** as scope creep; HES is framed around reasoning complexity.

3. **Strength Finder: "Training-free and lightweight" framing.** This is correct but generic—every paper claims its method is efficient relative to the prior work it defeats. **Removed** as a superficial strength without novel grounding.

4. **Strength Finder: "Well-structured experimental setup."** This is a generic procedural compliment, not a scientific contribution. **Removed**.

---

## Novel Insights

The most genuinely novel insight is the bidirectional validation structure: not only does high-HES selection improve performance, but low-HES data (14.90% for the lowest-20% subset) is shown to be actively *harmful* relative to random selection (25.89%). This two-sided result—combining positive gains from high-HES and documented harm from low-HES—creates much stronger evidence for the metric's validity than a one-sided comparison would. Combined with the asymmetric RL strategy (select high-quality positives, keep negative diversity), the paper implicitly argues that reasoning quality and reasoning failure have asymmetric selection needs: quality matters for positive examples but diversity matters for negative ones. This asymmetry is non-obvious and worth highlighting as a design principle.

---

## Suggestions

1. Add a brief length-controlled ablation (e.g., within a 2k–3k token window) in the SFT section to decouple the length × entropy confound and strengthen the mechanistic interpretation.
2. Report bootstrapped confidence intervals or at minimum standard deviations across the 16 sampling paths, specifically for AIME24/25 and for all RL results in Table 6.
3. Add one sentence in Section 4.1.1 specifying exactly which model computes HES for the main experiments and approximate the forward-pass overhead relative to training cost.
4. Either soften the RL conclusions ("preliminary evidence" rather than validated result) or add one more model/dataset run to the RL section to substantiate the "unified" framing.
5. Reframe the mechanistic claim in the abstract and introduction from "focuses on critical forking points" to "correlates with reasoning complexity at local uncertainty peaks"—more defensible given the current ablation set, and still captures the key insight.

---

## Score and Decision

**Originality:** 3/5 — Incremental but clear, principled improvement over prior entropy-based metrics; the relative percentile threshold and asymmetric RL strategy are novel design choices.
**Importance:** 4/5 — Data-efficient reasoning training is an actively important problem; a simple, training-free signal applicable across all three major paradigms has immediate practical value.
**Claims Supported:** 3/5 — SFT claims are strongly supported with large margins and multi-setting replication. RFT and RL claims are supported but margins are small and lack statistical quantification.
**Soundness:** 3/5 — Comprehensive SFT experimental design with multiple baselines. RL/RFT sections are underpowered. Length confound in mechanistic interpretation not fully resolved.
**Clarity:** 4/5 — Writing is clear, experimental design is well-described, metric definitions are precise.
**Community Value:** 4/5 — Practical, immediately reproducible, applicable to mainstream training pipelines without external dependencies.

The core SFT contribution is genuine and well-supported, the comprehensive baselines are a strength, and the training-free nature plus cross-model transfer make this practically valuable. The RL evidence is thin and the statistical reporting gap is real but addressable. The mechanistic overclaiming is the most substantive concern but does not invalidate the empirical results. This is a solid, publishable paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>