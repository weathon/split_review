## Summary

This paper conducts a systematic ablation study of GRPO (Group Relative Policy Optimization) for LLM post-training on mathematical reasoning. The authors isolate three components — negative feedback, advantage estimation, and PPO-style clipping — and find that: (1) negative feedback is essential (training with only positive advantages collapses), (2) group-relative advantage estimation is crucial (raw REINFORCE is unstable), and (3) PPO-style clipping is not necessary. They propose REINFORCE with Group Relative Advantage (RGR/RGRA), which removes the clipping and policy ratio terms while keeping group-relative advantage estimation, and show it outperforms GRPO in 17 of 27 benchmark settings across three small models.

---

## Strengths

- **Clean ablation methodology**: The decomposition into three independent axes (negative feedback, advantage normalization, PPO clipping) is logically organized and the experimental design is principled — each variant targets exactly one component change.
- **Multi-lingual, multi-benchmark evaluation**: Testing on nine benchmarks across English, Chinese, and STEM domains provides richer evidence of generalization than a single-benchmark study. The consistent advantage of RGR over GRPO on Qwen2.5 models in both Chinese and English math is encouraging.
- **Concrete training-dynamic evidence**: The training curves in Figure 1 clearly show the collapse of positive-only methods and raw REINFORCE, providing mechanistic support for the paper's central claims about negative feedback and advantage estimation.

---

## Weaknesses

### Fatal
None that completely invalidate the conclusions, though scale concerns severely limit their scope (see Major below).

### Major

1. **Extremely small experimental scale limits generalizability of claims**: All experiments use 1,800 GSM8K training samples, models of at most 1.5B parameters, a maximum output length of 512 tokens, and approximately 70 training steps. The paper makes sweeping statements like "PPO-style constraints are not required to improve mathematical reasoning" and "simpler REINFORCE-based approaches can effectively enhance reasoning in LLMs," but these claims are only grounded in a regime far removed from where GRPO is practically deployed (e.g., 7B–70B models, tens of thousands of training samples, multi-thousand token reasoning chains). At the paper's scale, the differences between clipped and unclipped objectives may be negligible simply because the training distribution shift is tiny and gradient variance is low. The paper acknowledges hardware constraints prevent testing larger models, but this constraint fundamentally limits what can be concluded.

2. **No statistical significance testing or variance estimation**: All benchmark comparisons involve single-seed results with no error bars, confidence intervals, or multi-seed averaging. Many of the margins between GRPO and RGR are very small (e.g., 20.1 vs. 20.2 on Llama3.2 English math average; 22.5 vs. 24.9 on STEM). Mathematical benchmark accuracy at these scales can vary by 1–3% across different evaluation seeds. The claim that "RGR outperforms GRPO in 17/27 settings" cannot be trusted without variance estimates — many of those 17 wins may be within noise.

3. **Limited novelty relative to prior work**: The core finding — that simple REINFORCE with a group baseline can match or beat GRPO — directly echoes Ahmadian et al. (2024) "Back to Basics," which already argued for simpler policy gradient methods over PPO for pre-trained LLMs. RGR is the most natural simplification of GRPO one would attempt after reading that prior work. The paper does not clearly articulate what is conceptually new beyond the ablation confirmation and the group-relative advantage as a specific baseline choice.

4. **70-step training runs are too short to draw stable conclusions**: Training curves (Figure 1) show only ~70 update steps per run. Many RL methods, including PPO-style ones, are known to exhibit transient instability early in training that resolves with more updates. Conclusions about stability and collapse drawn from such brief runs may not reflect steady-state behavior with longer training.

### Minor

- The "REINFORCE" baseline in the paper uses raw rewards (not group-relative advantages), which conflates two changes simultaneously (removing clipping AND removing advantage normalization) relative to RGR. A standalone "REINFORCE with group-relative advantages but without clipping" is RGR itself, so the naming is somewhat circular and the ablation tree is not fully exhaustive between the presented variants.
- The 512-token maximum generation limit artificially suppresses reasoning chain exploration and may systematically disadvantage PPO-style clipped methods (which can penalize large distribution shifts more aggressively when exploration is truncated), potentially inflating the apparent advantage of RGR.
- The reproducibility statement contains an empty code link ("The link to our code is ."), which is a practical barrier to replication.
- The emergent reasoning evidence (Figure 2) is a single anecdotal example from a Countdown dataset not used in training — stronger evidence would aggregate over many examples.

### Trivial

- The method is called "RGR" in the abstract/title and "RGRA" in the conclusion and Table 1–3 (and referred to as "RGR A" in the method description). This inconsistency makes reading harder.

---

## Nice-to-Haves

- A plot showing sensitivity of the GRPO vs. RGR gap as a function of training data size or model size would greatly strengthen the generalizability claim.
- Statistical testing (e.g., bootstrap confidence intervals on benchmark scores across multiple evaluation seeds) would solidify the 17/27 win rate claim.
- Ablating the KL regularization coefficient β independently would complete the picture of GRPO component analysis (the paper mentions KL in the loss but does not isolate its effect).

---

## Novel Insights

The paper's most concrete novel insight is the interaction between negative feedback and training collapse: removing negative advantages causes reward hacking toward short outputs even in models as large as 1.5B, suggesting that group-relative normalization functions primarily as a mechanism to prevent degeneracy rather than merely as a variance-reduction tool. The observation that this collapse occurs even with PPO-style clipping present (positive-only GRPO still collapses) specifically isolates the feedback sign as the critical factor rather than the clipping range. This is a clean and useful experimental result, though its significance is bounded by the small experimental scale.

---

## Suggestions

- Replicate the key GRPO vs. RGR comparison at 3B or 7B scale on a broader dataset (e.g., MATH or a mixed reasoning corpus) to substantiate the central claim at a practically relevant scale.
- Include multi-seed evaluation (at minimum 3 seeds) for the key benchmark comparisons and report mean ± std.
- Extend training to at least 200–500 steps to verify that instability findings are stable and not early-phase artifacts.
- Add an ablation that removes only KL regularization (with clipping intact) to complete the component isolation.

---

## Score and Decision

The research question is well-motivated and the ablation structure is clean. However, the experimental scale is insufficient to support the broad claims made: tiny models, tiny datasets, very short training, 512-token output limit, and no statistical testing together prevent drawing reliable conclusions that would generalize to settings where GRPO is actually used. The core finding is also closely anticipated by Ahmadian et al. (2024). The paper is useful as a preliminary investigation but does not yet provide the evidence needed for confident conclusions at ICLR.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>