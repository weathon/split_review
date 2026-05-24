Now I have sufficient calibration data. Let me synthesize the final review.

**Initial bracket (Round 1):** Based on the weak anchors (avg 2.5-3.33), middle anchors (avg 5.0-6.17), and strong anchors (avg 8.0), I place CoPrompt between 5.0 and 7.0. It is clearly stronger than the weak band (which had fatal flaws or very limited contributions) but far from the oral-level strong band.

**Narrowing (Round 2):** Comparing to specific anchors in the 4.5-7.5 range: ADAPT (avg 5.5, Reject) had less thorough experiments; CARPRT (avg 5.75, Reject) had similar modest gains; C-TPT (avg 6.0, Accept) had a more novel problem framing but less evaluation breadth; Self-TPT (avg 5.0, Reject) had fundamental flaws. CoPrompt sits between ADAPT/CARPRT and C-TPT — better experiments than the former, but more incremental contribution than the latter. Final score: **5.5**.

---

## Summary

This paper proposes CoPrompt, a consistency-guided prompt learning method for fine-tuning CLIP in few-shot settings. The core idea is to enforce a cosine-distance consistency constraint between the frozen pre-trained encoder outputs and the learnable (prompt + adapter) encoder outputs, combined with input perturbations (LLM-generated text descriptions and image augmentations) and the integration of adapters into a multi-modal prompt learning framework. The method is evaluated on base-to-novel generalization (11 datasets), cross-dataset transfer (10 datasets), and domain generalization, with extensive ablations. CoPrompt achieves a harmonic mean of 80.48% on base-to-novel, improving over PromptSRC by 0.51%.

## Strengths

1. **Thorough and well-designed ablation studies.** Table 4 systematically ablates each component (consistency, input perturbations, adapters) and shows that removing the consistency constraint causes performance to drop below even the MaPLe baseline (78.45 vs 78.55), directly supporting the paper's claim that consistency regularization enables the combination of prompts and adapters. Tables 5a–f further analyze design choices (modality-specific consistency, loss functions, LLM choices, augmentation types, adapter configurations), providing concrete evidence for each decision.

2. **Extensive evaluation across multiple protocols.** The paper evaluates on three distinct settings: base-to-novel generalization (11 datasets), cross-dataset evaluation (10 datasets), and domain generalization (4 ImageNet variants). This is the standard evaluation suite for this line of work and the coverage is thorough. CoPrompt achieves the best average on base-to-novel HM (80.48%) and cross-dataset (67.00%), and maintains competitive performance on domain generalization.

3. **Clear demonstration that consistency enables adapter+prompt combination.** The ablation shows that without consistency regularization, adding both prompts and adapters actually *worsens* performance (78.45 HM) compared to using neither (78.55 HM). With the consistency constraint, the combination achieves 80.48 HM. This is a clean empirical finding that validates the paper's core thesis.

4. **Computational overhead is honestly characterized.** Table 8 reports parameter counts, and Section 4.6 explicitly acknowledges ~2× training FLOPs and ~25% longer training time, while also showing that under an equal compute budget (fewer epochs), CoPrompt still outperforms MaPLe (80.01 vs 78.55). Inference cost is nearly identical to MaPLe.

## Weaknesses

### Fatal

None.

### Major

1. **Incremental novelty relative to PromptSRC.** The core idea of regularizing learnable parameters toward the frozen pre-trained model's outputs has been explored in PromptSRC through its "self-regulating" concept. While CoPrompt differs in specifics (cosine vs other distance, inclusion of adapters, input perturbations), the high-level mechanism is the same. The paper's claim that prior work "has not been able to successfully combine [prompts and adapters]" is supported by the ablation, but this is a relatively narrow contribution — the consistency constraint fixes overfitting from extra parameters, which is a well-understood role of regularization.

2. **PromptSRC's cross-dataset baseline is anomalously low and unexplained.** In Table 2, PromptSRC achieves 65.81% average on cross-dataset evaluation, which is *below* MaPLe (66.30%) and barely above Co-CoOp (65.74%). This is unusual given that PromptSRC is the previous SOTA on base-to-novel and outperforms MaPLe there by 1.42% HM. The paper notes that "PromptSRC's performance is considerably lower than CoPrompt" but does not discuss why PromptSRC underperforms MaPLe in this setting. If this is an artifact of hyperparameters or training setup, the cross-dataset comparison becomes unreliable. This needs to be addressed.

3. **Modest improvements despite added complexity.** The headline gain is +0.51% HM over PromptSRC on base-to-novel generalization (80.48 vs 79.97). While the improvement is consistent across datasets (better on 8/11), the margin is small given the added complexity: LLM calls, dual consistency losses, adapters on both modalities, and ~25% longer training time. The paper's framing as "considerable improvements" and "new state-of-the-art for a range of evaluation suites" overstates the actual margins.

### Minor

1. **Domain generalization is not SOTA.** On domain generalization (Table 3), CoPrompt (60.42%) underperforms PromptSRC (60.65%) and Bayesian Prompt (60.44%). The paper characterizes this as "comparable performance," which is accurate, but the introduction claims SOTA for "base-to-novel generalization and cross-dataset recognition" while omitting domain generalization. An honest discussion of where the method falls short would strengthen the paper.

2. **LLM generation details are underspecified in the main paper.** The paper states that it "follow[s] the training setup of KgCoOP" for LLM usage and compares GPT-2 vs GPT-3 in ablations, but does not specify the exact model version (e.g., text-davinci-003 vs GPT-3.5), prompt template used for generation, temperature, or output length control. These details are likely in the appendix (which the parser strips), so this is a minor presentation concern.

### Trivial

None.

## Nice-to-Haves

- An analysis of why the consistency constraint works better than PromptSRC's self-regulation (e.g., embedding space visualization, how cosine distance vs other criteria affects the learned features).
- Standard deviations or confidence intervals for the main results, since the margins are small.

## Removed Points

- **Criticism that "prior work has not been able to successfully combine them" is unsupported.** *Removed because the paper provides direct empirical evidence: ablation row (✗ ✓ ✓) shows HM 78.45, which is below the baseline of 78.55, confirming that without consistency the combination indeed hurts performance.*
- **Criticism about missing related works.** *Removed per hard rules (cannot verify existence of unmentioned works).*
- **Criticism about missing appendix content.** *Removed per hard rules (parser strips appendices from all papers; they exist in the original submission).*
- **Criticism about statistical significance / standard deviations.** *Removed because single-run evaluation is the accepted standard in this line of work (CoOp, CoCoOp, MaPLe, PromptSRC all report single runs).*
- **Reproducibility concerns about LLM details.** *The paper references KgCoOp's training setup and the ablation compares GPT-2/GPT-3; full details are deferred to the appendix (parser-stripped). This is a minor issue, moved to Minor.*
- **Strength about "state-of-the-art results across multiple benchmarks."** *This conflicts with verified weaknesses (domain generalization is not SOTA, cross-dataset PromptSRC baseline is anomalous). Modified to acknowledge SOTA on base-to-novel and cross-dataset with appropriate caveats.*
- **The harsh critic's claim that the consistency constraint is "simply compensating for overfitting introduced by the extra parameters."** *This is factually what the paper demonstrates — the ablation shows exactly this behavior. The critic frames it as a negative, but the paper's contribution is precisely the regularization that makes the combination work. This is a framing difference, not a weakness.*

## Novel Insights

The two reviews, taken together, surface an interesting tension: the paper's strongest evidence (ablation showing consistency prevents adapter+prompt collapse) is also its most damning limitation (this is regularization, not a new principle). The harsh critic correctly identifies that the paper's novelty is in the careful engineering and empirical validation, not in a novel theoretical insight. The strength finder correctly identifies that the ablation is exceptionally thorough. The synthesis reveals a paper that is technically competent and well-evaluated but makes an incremental contribution — a pattern common in the mature prompt-tuning literature where the low-hanging fruit has been picked.

## Suggestions

1. Address the PromptSRC cross-dataset discrepancy explicitly: retrain PromptSRC under identical conditions, or explain why its cross-dataset result is lower than MaPLe's. This is the most impactful action the authors can take.
2. Tone down the "considerable improvements" and "new state-of-the-art" framing, and instead highlight the specific contribution: a consistency-regularized framework that successfully combines prompts and adapters, with thorough empirical validation showing consistent (if modest) gains.
3. Add a brief discussion of why domain generalization does not see the same improvements as base-to-novel and cross-dataset evaluation.

## Score and Decision

**Calibration anchors used:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Multi-Vision Multi-Prompt | j1FLTvgyAh.md | 2.50 | R1 | Much weaker — fundamental issues with method and evaluation |
| Weak-to-Strong Generalization | FwkYeLovHk.md | 3.33 | R1 | Weaker — unclear contribution, not closely related |
| Prototypical Evolution | ZaudLwn0Hm.md | 2.50 | R1 | Much weaker — limited evaluation |
| PLPP | 2VAi5F9BOJ.md | 2.50 | R1 | Much weaker — niche problem, limited results |
| OpenPL | veiSkPqIXm.md | 5.00 | R1 | Comparable avg but different contribution type (benchmark vs method) |
| CARPRT | fRpAUgKJhT.md | 5.75 | R1 | Similar level — modest improvements, incremental method |
| AnomalyCLIP | buC4E91xZE.md | 6.17 | R1 | Stronger — more novel task framing, accepted |
| Prompt Reverse Learning | dsiwLm8yjz.md | 5.00 | R1 | Similar avg but less thorough evaluation |
| ADAPT | 1L9vdc7BB5.md | 5.50 | R2 | Similar quality but CoPrompt has more thorough ablation |
| C-TPT | jzzEHTBFOT.md | 6.00 | R2 | CoPrompt has broader evaluation, C-TPT has more novel problem framing |
| Self-TPT | NeVbEYW4tp.md | 5.00 | R2 | CoPrompt is stronger — Self-TPT has fundamental technical concerns |
| Vision-Language Synergy Continual Learning | 9aZ2ixiYGd.md | 5.00 | R2 | Different task (continual learning), comparable quality |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowing:** Compared against ADAPT (5.5, less thorough), CARPRT (5.75, similar incremental gains), and C-TPT (6.0, more novel angle). CoPrompt sits at the lower end of this range due to incremental novelty and the unaddressed PromptSRC cross-dataset anomaly, but is technically solid with thorough evaluation.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>