Now I have a thorough understanding of the paper and all claims. Let me produce the consolidated review.

## Summary

This paper proposes MC-SMoE, a framework for compressing Sparse Mixture-of-Experts (SMoE) models by (1) merging redundant experts guided by routing-policy statistics (activation frequencies and router logits), and (2) further compressing the merged experts via low-rank decomposition. The core idea — that routing decisions encode meaningful expert relationships that can guide merging — is novel. The main empirical result is impressive: MC-SMoE achieves up to 80% memory and 20% FLOPs reduction on the switch-base-32 model with less than 1% performance drop across five of eight benchmarks, outperforming six existing merging/pruning baselines.

## Strengths

- **Routing-statistic-guided grouping systematically outperforms alternative similarity measures.** The paper compares eight grouping methods (Table: grouping-method) and shows that router-logit-based similarity consistently yields the highest accuracy across four benchmarks (e.g., +6 points on COPA over the next-best variant), directly validating that routing decisions capture meaningful expert relationships.

- **Merging-then-compressing (MC-SMoE) preserves accuracy while cutting memory by 80% and FLOPs by 20%.** Table 1 shows MC-SMoE (381M params, 3.83 TFLOPs) suffers less than 1% performance drop on five of eight tasks compared to the full 2B-parameter SMoE, establishing a strong efficiency-quality trade-off. M-SMoE alone achieves 60% memory reduction with performance matching or exceeding the full model on multiple tasks.

- **Empirical demonstration that merging lowers weight dimensionality, enabling extra compression.** Figure 2 (stable-rank change ratio) shows consistent decreases across SMoE layers after merging, and Table "merging-and-decomposition" directly validates that MC-SMoE (merge+compress) outperforms C-SMoE (compress-only) while using 33% fewer parameters (381M vs. 570M).

- **Comprehensive ablations isolate each algorithmic component's contribution.** Separate studies confirm the necessity of permutation alignment (Table: perm-ablation, +1–2.4 points), frequency-weighted averaging over uniform or Fisher-weighted (Table: merging-strategy, +3–4 points on COPA), adaptive layer-wise merging ratios over uniform (Table: uniform-adaptive, +5 points on COPA), and router-logits over seven other grouping methods (Table: grouping-method). These controlled experiments show no single design choice is gratuitous.

- **Superiority over six existing merging/pruning baselines.** Table 1 shows M-SMoE achieves the best or tied-best performance on 5 of 8 tasks versus Averaging, ZipIt, REPAIR, Git Re-basin, and two pruning methods, often recovering or exceeding the full SMoE's accuracy (e.g., 90.69 vs. 90.20 on MRPC). This demonstrates that off-the-shelf merging techniques are inadequate for SMoE and that the proposed routing-guided approach is both novel and necessary.

## Weaknesses

### Fatal

None.

### Major

- **Zero-shot evaluation results are promised but absent.** The paper states in Section 4.1 that decoder-only models (fairseq-moe-15b) are evaluated in a zero-shot setting and that three benchmarks (MRPC, WinoGrande, OpenBookQA) are selected. However, no zero-shot results table appears anywhere in the paper. Given that the paper's stated scope (§4.1) includes zero-shot evaluation for decoder-only models and mentions it in the contributions, this is a concrete missing piece that affects completeness. The authors should either present these results or clearly scope the paper to only supervised fine-tuning.

### Minor

- **Knowledge distillation applied uniformly but KD benefit for baselines is not demonstrated.** The paper correctly applies KD to *all* compared methods uniformly (line 268: "we by default use KD for all merged and compressed SMoEs, including our M-SMoE, MC-SMoE, and all baselines"), so the comparison is fair. However, the KD ablation (Table: kd-ablation) is only shown for M-SMoE, not for any baseline. Since the reviewer correctly notes that M-SMoE shows substantial KD gains (e.g., COPA +4 points, SQuAD EM +2.41), it would be informative to verify that baselines also benefit comparably from KD — otherwise the relative ranking could shift in a non-KD setting. This is a completeness concern, not a fatal flaw.

- **Task-Specific pruning baseline performs anomalously poorly.** In Table 1, Task-Specific pruning (Chen et al. 2022) achieves 52.00 on COPA vs. simple one-shot pruning at 63.00, and 53.63 on MultiRC vs. 75.13. The gap is unusually large, raising the question of whether this baseline was properly tuned or adapted for this setting. The paper does not describe the adaptation or hyperparameter search for this baseline. While this does not affect comparisons against the stronger baselines (ZipIt, REPAIR, etc.), it weakens the claim that M-SMoE improves over *all* prior expert-reduction methods.

- **Weight-matching procedure in Algorithm 1 aligns all experts to a single reference before grouping.** The algorithm (line 116) aligns every expert to expert E₁^t via weight-matching, then groups and merges. If experts end up in different groups, aligning them all to the same reference before grouping may be suboptimal — within-group alignment after grouping is an alternative the paper does not discuss or ablate. This is a methodological gap: the algorithm as described may not achieve the claimed optimal permutation alignment benefit.

- **Frequency threshold / sensitivity analysis is missing.** The paper uses activation frequencies to determine dominant experts but reports only "an average of 8 experts" kept per layer. No sensitivity analysis is provided on (a) the random subset size used for frequency estimation, (b) the batch size for router-logit computation, or (c) how results vary with different frequency thresholds for selecting dominant experts.

- **Router-logit batch is not specified as held-out vs. training data.** The router-logit similarity (Equation 1) is computed from "a randomly picked subset of training data" (line 82). If the same data is used for both frequency estimation and logit computation, this could introduce bias. Clarifying whether these are disjoint subsets would strengthen the methodology.

### Trivial

- **Equation 1 uses W_r(X^T) with transposition notation that could be clarified.** While not incorrect, specifying the dimensions of X (number of tokens × hidden size) explicitly would improve readability.

- **The first SMoE layer is skipped for all merging/compression methods** (Table 1 caption). The paper justifies this by noting the first layer's "profound impact" and cites prior work (ma2023llmpruner). This is a reasonable design choice, but an ablation showing the degradation from merging the first layer would be a useful addition for practitioners.

## Nice-to-Haves

- A sensitivity study varying the frequency threshold for dominant expert selection, and reporting the variance in kept experts across layers and tasks, would strengthen the adaptive claim.
- An ablation comparing the current single-reference alignment strategy with within-group alignment would resolve the methodological ambiguity in Algorithm 1.
- Including a table of zero-shot results (even if in supplementary) would fulfill the stated experimental scope.

## Removed Points

- **"KD puts baselines at unfair disadvantage"** — The paper applies KD uniformly to all methods. The concern about disproportionate benefit is speculative without evidence. Kept only as a minor completeness concern (KD benefit for baselines not demonstrated).
- **"\colorbox{cyan!30}{blue} is a typo"** — This is standard LaTeX formatting for a colored box in the table caption, not a typo.
- **"TFLOPs is an unusual measure"** — The paper clearly specifies how TFLOPs are computed (batch of 64 SQuAD samples). This is a standard reporting practice.
- **"Stable-rank figure is extraneous"** — This is an opinion; the figure supports the motivation for post-merging compression.
- **"Equation 1 notation issue"** — The notation is standard and correct given standard matrix multiplication conventions.
- **"Table numbering confusion"** — The reviewer's references to "Table 5" and "Table 6" do not correspond to the paper's actual table labels, which are consistent within the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews corroborate the paper's claims rather than revealing new perspectives.

## Suggestions

1. **Include the zero-shot evaluation results** promised in Section 4.1, or explicitly re-scope the paper to supervised fine-tuning.
2. **Show a KD ablation for at least one baseline method** (e.g., ZipIt or Averaging) to demonstrate that the relative ordering is robust to KD's presence.
3. **Add a sensitivity study** on the frequency threshold / subset size for dominant expert selection.
4. **Clarify the weight-matching step** in Algorithm 1: discuss whether alignment to a single reference vs. within-group alignment is preferred, and ideally ablate both strategies.
5. **Provide a brief description of how the Task-Specific pruning baseline was adapted**, including any hyperparameter search, or replace it with a stronger, more standard pruning baseline.

## Score and Decision

The paper presents a novel, well-motivated approach with strong empirical results and thorough ablations. The core claims — that routing statistics can guide expert merging and that merging reduces weight dimensionality enabling further compression — are well-supported. The main weaknesses are (1) the missing zero-shot results promised in the paper, and (2) some methodological ambiguities (weight-matching strategy, single-seed sensitivity). None of the identified issues invalidate the central contribution. The paper is above the acceptance threshold with room for improvement through the suggested additions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>