Now I have a thorough understanding of the paper and can verify the reviewer claims directly. Let me produce the consolidated review.

---

## Summary

This paper proposes UGDA (Uncertainty-Gradient based Data Augmentation), a three-stage method to mitigate reward model off-distribution in RLHF. UGDA (1) trains reward LoRA ensembles to capture uncertainty, (2) selects interaction samples using both reward variance (uncertainty) and gradient-based influence scores, and (3) refines the reward ensembles via MSE loss on expert-relabeled (GPT-4 or human) rewards. The claimed contribution is a data selection mechanism that picks the most valuable on-distribution samples for reward model retraining.

## Strengths

- **Novel combination of uncertainty and gradient-based selection for reward refinement**: The paper introduces a two-stage data selection (uncertainty thresholding, then gradient influence scoring) specifically designed for the off-distribution problem in RLHF. The ablation study (Figure 4) confirms that removing either component partially hurts performance, providing evidence that both contribute.

- **Broad evaluation across multiple metrics and benchmarks**: The paper evaluates on Llama2-13B judge scores (Avg_Reward, Var_Reward), GPT-4 pairwise comparisons, AlpacaEval, Arena-Hard, MT-Bench, RewardBench, and accuracy — providing a reasonably thorough assessment of both policy and reward model quality.

- **Robustness evaluation under noisy preference data**: The paper explicitly tests robustness by corrupting 20% of preference labels (Table 3, Figure 5). UGDA suffers less degradation than baselines and even outperforms clean-data baselines in some GPT-4 evaluations, suggesting practical resilience.

- **Reward model evaluation disentangled from policy**: Figure 6 (RewardBench) and Figure 7 (accuracy) evaluate the reward model directly, not just the downstream policy, which helps isolate the benefit of better reward modeling from policy optimization effects.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled comparison inflates the headline claim (overclaiming SOTA)**. The paper claims to "surpass the state-of-the-art methods" (abstract, conclusion) and Table 2 compares UGDA against LCB and UWO. However, line 243 makes clear that "0% represents the baselines without data augmentation" — so LCB and UWO appear under the 0% column without any GPT-4 relabeled data. UGDA, by contrast, uses 25% GPT-4 relabeled data for reward model refinement. Comparing UGDA (augmented) against LCB/UWO (unaugmented) conflates the benefit of the selection mechanism with the benefit of having 25% additional GPT-4 supervision. The **only controlled baseline** is RLR (random selection with the same 25% GPT-4 budget). This overclaiming is a serious framing issue: the paper should either qualify that its SOTA claim is relative to non-augmented baselines, or provide LCB/UWO variants augmented with the same GPT-4 data. Without this, the central contribution is not properly scoped.

2. **No cost-efficiency analysis undermines the practical value proposition**. The paper motivates UGDA by stating that "collecting new preference data...is costly" and that UGDA can improve the reward model "without the costly human preference data collection." However, UGDA still requires an expensive oracle (GPT-4 or human) to relabel 25% of interaction data. The paper compares UGDA (25% selection) against RLR (25% random) — showing selection beats random at the *same* budget — but never demonstrates that the selection mechanism *saves labeling cost*. It does not test whether UGDA at 25% matches the performance of random selection at a larger budget (e.g., 50% or 100%), nor does it compare against using *all* interaction data with GPT-4 labels. Without such analysis, the claim that UGDA reduces the amount of labeling needed is unsubstantiated.

### Minor

1. **No sensitivity analysis for selection thresholds**. The thresholds γ=0.5 and η=0.5 (lines 135, 173) are chosen to fix the selected subset at 25% of interaction data, but the paper provides no ablation on varying these thresholds. It is unclear whether 25% is optimal, or how performance degrades with different selection ratios. This is important because the fixed size means the ablation (Figure 4) swaps selection variants at the same size but never asks whether the selection mechanism's value changes at different budgets.

2. **No discussion of computational overhead**. The method requires storing multiple policy checkpoints (for trajectory influence), computing Adam gradient buffers, running random projections of LoRA gradients per token, and scoring the entire interaction dataset against validation subtasks. This overhead is never quantified. For a method whose value proposition includes practical deployability, this is a notable omission.

3. **Missing error bars / statistical significance in key results**. Figure 3 (instruction-following benchmarks) and Table 2 report single-run results without error bars or significance tests. Given the stochasticity in PPO training and data selection, it is difficult to assess whether the reported improvements are reliable.

4. **Limited robustness evaluation scope**. The robustness experiment (Section 5.3, RQ3) only tests label flipping (swapping 20% of preference pair positions). Other realistic noise forms (e.g., noisy preference scores, partial mislabeling, annotation inconsistency) are not considered, limiting the generality of the robustness claims.

5. **Weak explanation for RewardBench reasoning gap**. The paper notes that UGDA underperforms on the Reasoning category of RewardBench (Figure 6) and dismisses this with "there are only few samples about the reasoning task" without supporting evidence. This is a superficial explanation.

### Trivial

1. **Ambiguous description of baseline augmentation status**. The text in lines 216–217 ("for the baselines, without loss of generality, we conduct experiments by randomly select 25% of the interaction data with GPT-4 annotator for the reward model refining") is ambiguous about which baselines received this treatment, making Table 2 difficult to interpret. Combined with line 243 ("0% represents the baselines without data augmentation"), the reader cannot easily determine which methods used augmentation. This should be clarified with explicit column headers or a footnote.

## Nice-to-Haves

- Sensitivity analysis for the number of ensemble members k (currently fixed at k=3).
- Validation of the method using self-consistency or model-generated critiques (self-rewarding) to reduce oracle dependence.
- Qualitative examples showing selected vs. rejected samples to build intuition about what UGDA chooses.

## Removed Points

Points flagged to be removed — treat with caution:

- Harsh critic's point about "Comparison to LCB/UWO lacks clarity on augmentation status (Structural)" — folded into Major weakness 1 above (uncontrolled comparison). Keeping the substance while avoiding duplication.
- Harsh critic's note about "Table 2 formatting is confusing" — a pure formatting issue given the table is embedded as an image; the parser strips table formatting from all papers. Removed as formatting nitpick.
- Harsh critic's "Missing Experiments" about broader RLHF tasks (summarization, dialogue beyond HH dataset) and about testing more noise types — these are scope creep; the paper focuses on the HH dataset and a specific noise type. Not core to evaluating the method's contribution.
- Harsh critic's note about "quantile projection validation" — the paper already provides Table 1 (~95% similarity between human and GPT-4 relabeling), which is a reasonable validation.
- Harsh critic's note about "gradient-based influence derivation not fully justified for RLHF" — the derivation follows Xia et al. (2024) with standard influence function machinery; the adaptation is straightforward and the paper explains the validation set choice.
- Strength Finder's claim about "consistent empirical improvement over strong baselines on multiple metrics" overstated due to the uncontrolled comparison issue noted above. Kept as a qualified strength but note the caveat.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a standard pattern — a method with a reasonable core idea but overclaimed comparisons and insufficient cost analysis — but do not generate a novel insight that the paper itself does not contain.

## Suggestions

1. **Reframe the central claim.** The paper should clearly separate the controlled comparison (UGDA vs. RLR: both at 25% GPT-4 budget) from the uncontrolled comparison (UGDA vs. LCB/UWO: with vs. without augmentation). The paper's contribution is a selection mechanism that improves over random selection at the same budget; this is a meaningful result and should be stated honestly without implying SOTA over non-augmented methods.

2. **Add a cost-efficiency experiment.** Compare UGDA (25% selection) against RLR with larger budgets (e.g., 50%, 100% of interaction data with GPT-4 labels). If UGDA at 25% matches or exceeds RLR at 50%, this would strongly substantiate the practical value proposition.

3. **Run LCB and UWO augmented with GPT-4 relabeled data if feasible.** If these methods can incorporate the GPT-4 data (e.g., by retraining their ensemble members), this would make the headline comparison fair. If not, the paper should explicitly explain why and qualify the comparison.

4. **Add sensitivity analysis for γ and η thresholds** to show how performance varies with the selection ratio, and add error bars for key results.

5. **Quantify computational overhead** (checkpoint storage, projection computation time, influence scoring cost) to help readers assess practical deployability.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>