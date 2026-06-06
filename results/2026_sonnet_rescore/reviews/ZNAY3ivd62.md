## Summary
GUI-Spotlight is a visual grounding model for GUI interfaces that trains a policy to iteratively invoke three specialized visual tools (*crop*, *extract*, *find\_color*) to progressively narrow focus to a target screen element. It is trained in three stages — SFT warm-up on 2,561 multi-turn tool trajectories, followed by two phases of reinforcement learning with a modified GSPO objective that adds an auxiliary cross-entropy loss on tool-filtered positive samples to prevent training collapse. The main empirical claim is 52.8% accuracy on ScreenSpot-Pro using 18.5K total training samples, outperforming 7B-scale baselines trained on orders of magnitude more data.

---

## Strengths

- **RL stabilization via auxiliary CE loss is a concrete, validated contribution.** Variant ⑦ (tool-filtered positives with auxiliary cross-entropy) reaches 47.6% at 400 RL steps, while all other GRPO/GSPO variants fall between 35.8%–39.5% (Figure 3). The training dynamics (right panel of Figure 3) confirm that vanilla GSPO/GRPO oscillates and collapses around 300 steps while the modified objective remains stable. This directly validates the core technical claim about training stability.

- **State-of-the-art on ScreenSpot-Pro at 7B scale, with far less data than comparable models.** GUI-Spotlight (UI-TARS backbone) achieves 52.8% versus V2P-7B (50.6%, 9.6M samples), GTA-1-7B (50.1%, 1.56M samples), and GUI-Actor-2.5VL-7B (44.6%, 9.6M samples) — all from Table 3. The result is reproducible against a publicly maintained leaderboard.

- **Transparent documentation of negative results.** The paper explicitly reports that strategy ① (multi-turn conversational inference without training) achieves only 7.6%, that the Stage 1 SFT drops accuracy from 39.3% to 17.8%, and that several RL variants underperform vanilla GRPO. This strengthens the community value of the empirical findings.

- **Backbone generality demonstrated.** Starting from non-UI-specific Qwen2.5-VL-7B-Instruct, the method raises ScreenSpot-Pro accuracy from 26.8% to 38.7% (+11.9 pts, Table 3) and OSWorld-G from 31.4% to 35.6% (+4.2 pts, Table 5), showing the RL objective is not solely a UI-specialized model fine-tuning artifact.

---

## Weaknesses

### Fatal
None.

### Major

- **The 5.2-point margin over a zero-shot fixed-crop heuristic understates how much work the RL pipeline is doing.** Figure 5 shows that a training-free, repeated single-turn inference baseline (Strategy ②) — crop a fixed 700×450 pixel region centered on the predicted click, re-infer — achieves **47.6%** on ScreenSpot-Pro. GUI-Spotlight's full three-stage trained system achieves 52.8%, a margin of 5.2 points. The paper's framing in Section 5.4 emphasizes the failure of Strategy ① (7.6%) to argue "the base model has virtually no think-with-image capability," but this rhetorical move obscures that the relevant zero-shot competitor is ②, not ①. A 5.2-point gain from three stages of training (SFT + two RL phases, 18.5K samples) over a naive fixed-crop heuristic is modest. The paper should squarely address *when and why* the trained policy outperforms ② — e.g., whether the gain comes from adaptive tool selection on hard cases where a fixed crop fails, or from better coordinate recovery on icon-heavy professional UIs. Without that characterization, the trained multi-tool coordination story is not fully convincing.

- **The data-efficiency claim in the abstract and Section 5.1 is overstated relative to SE-GUI-7B in Table 3.** The abstract states GUI-Spotlight's 18.5K samples as evidence of "strong data efficiency," comparing against V2P-7B (9.6M) and GTA-1-7B (1.56M). However, Table 3 lists SE-GUI-7B at 47.2% with only **3K training samples** — one-sixth of GUI-Spotlight's sample count — and this baseline is never discussed in the efficiency narrative. GUI-Spotlight is +5.6 points better in accuracy but uses 6× more training data. Whether this tradeoff constitutes "efficiency" depends on sample cost; the paper does not engage with this comparison at all, which is a conspicuous omission given the data appears in the paper's own table.

- **OSWorld-G gains are nearly negligible for the UI-TARS backbone, and GUI-Spotlight underperforms GTA1-7B.** Table 5 shows GUI-Spotlight (UI-TARS) at 62.7% versus the base model UI-TARS-1.5-7B at 61.9% — a gain of only +0.8 percentage points. Meanwhile, GTA1-7B achieves 67.7% on the same benchmark. The paper's Section 5.3 frames this as "competitive with much larger models," which is accurate for 72B comparison, but glosses over the fact that another 7B model (GTA1-7B) substantially outperforms it. The near-zero improvement from the base model on OSWorld-G raises genuine questions about generalization beyond the ScreenSpot-Pro distribution, and the discussion should acknowledge this limitation explicitly rather than presenting a uniformly positive narrative.

### Minor

- **The Qwen-initialized GUI-Spotlight underperforms specialized 7B baselines on UI-Vision.** Table 4 shows GUI-Spotlight (Qwen) at 8.3% versus OS-Atlas-7B (9.0%) and UGround-V1-7B (12.9%). The UI-TARS-initialized variant does substantially better (23.4%) and outperforms its base model, but the Qwen variant's below-baseline performance on UI-Vision is not discussed. The paper's Section 5.2 narrative describes the Qwen variant in terms of improvement over its own raw baseline (+7.4 pts over Qwen2.5-VL-7B's 0.9%), but fails to note it remains below other tuned 7B models. This selective framing should be corrected.

- **The Stage 1 SFT accuracy collapse (39.3% → 17.8%) is acknowledged but inadequately explained.** Figure 2 clearly shows the 21.5-point regression from the base model to post-SFT. The paper gives one sentence of explanation ("the model learns to invoke multiple tools but remains under-aligned") and implicitly treats it as expected. A more detailed analysis of whether this collapse is inherent to the tool-invocation format or could be partially mitigated would be valuable. It is the most alarming single data point in the paper, and the current one-sentence treatment is insufficient.

- **The hidden compute cost of 72B-scale generation for training data.** Section 3.2.1 reveals that Qwen2.5-VL-72B is used both to generate Stage 1 multi-turn trajectories and to audit every training sample through three filter criteria. The paper's data-efficiency argument is framed purely in terms of sample count, but the actual compute cost of running a 72B model as a data generator and quality auditor is substantial and invisible in this accounting. This should be acknowledged when making efficiency comparisons.

### Trivial

- **Unexplained duplicate Qwen2.5-VL-72B-Instruct rows in Table 3.** The table contains two rows labeled "Qwen2.5-VL-72B-Instruct" in the same 72B open-source block, with overall scores of 1.0% and 53.3% respectively. No explanation appears in the table, caption, or text. This is likely a prompted vs. unprompted configuration difference, but it must be annotated.

- **Figure 2 stage labeling offset.** Figure 2 labels the x-axis as Stages 0–3, with "Stage 0" appearing to be the untrained base model. However, the text in Section 3.2.2 refers to Stages 1–3 for the three training phases. The table under Figure 2 assigns 2561 samples to "Stage 0" and 12K to "Stage 1," which does not match the textual description where 2561 samples correspond to Stage 1 (SFT warm-up). This off-by-one labeling should be harmonized.

---

## Nice-to-Haves

- A stratified breakdown of cases where GUI-Spotlight succeeds over Strategy ② versus where both fail or both succeed would make the 5.2-point margin interpretable and the contribution of trained adaptive tool selection much more compelling. This would directly address the main evidential gap.
- An empirical analysis of tool usage distribution (how often each of *crop*, *extract*, *find\_color* is invoked, and in which benchmark subcategories) would validate the design choices for each tool and sharpen the thesis about coordinated tool use. If *find\_color* accounts for only a small fraction of successful tool calls, its inclusion as a first-class tool needs separate justification.
- Reporting inference-time cost (average number of tool calls per query, total wall-clock time versus single-pass models) would allow readers to assess the practical deployment tradeoff of iterative inference.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Improvement over UI-Venus-7B is only 2 points" as a framing criticism** (harsh critic, Introduction section): The paper does not claim to outperform UI-Venus-7B by a large margin; the comparison with V2P-7B and GTA-1-7B for the data-efficiency argument is the paper's stated framing. Noting the +2 gap over UI-Venus-7B is fair context, but not a standalone weakness of the paper's logic since the paper does not suppress the UI-Venus-7B number from Table 3. *Merged into the data-efficiency major weakness where SE-GUI-7B is the more pointed concern.*

- **"Reward component ablation trends may not persist at full training"** (harsh critic, Section 4.2): The critic notes the 400-step ablation may not settle to the same ranking at full training. This is speculative — the paper cannot be faulted for using a consistent ablation budget — and without specific evidence that the trends reverse, this is an unfounded conjecture. Removed.

- **"Base model has virtually no think-with-image capability" is a misleading framing** (harsh critic, framing): This criticism is partially subsumed by the Major weakness about Strategy ②. However, the critic's version of this framing suggests this alone invalidates the contribution — it does not. Removed as standalone; incorporated appropriately above.

- **Strength: "the paper addresses an important problem"** (strength finder, generic): Removed as generic — does not add specificity over citing actual results.

- **Strength: "reward design provides concrete guidance"** (strength finder): The reward ablations in Figure 4 are informative, but the findings ("sparse is marginally better," "higher Extract weight improves accuracy") are narrow claims derived from 400-step runs. Borderline; retained in reduced form above as part of the documented insights observation, not as a standalone strength.

---

## Novel Insights

The most genuinely novel observation in this paper is that standard GRPO/GSPO training collapses in multi-turn tool-use settings (Figure 3, right panel) in a distinctive and recoverable way: the model begins generating syntactically malformed tool calls around 300 steps, which triggers sparse and volatile rewards, inducing gradient instability and eventual divergence. The auxiliary cross-entropy loss applied specifically to tool-filtered positive examples directly addresses this collapse mode and yields a stable training curve. This failure mode — and the targeted fix — may transfer to other RL-trained, tool-augmented models beyond GUI grounding, representing the paper's most broadly applicable technical contribution. The finding that a fixed-window heuristic (Strategy ②) achieves 47.6% without any training is also a useful calibration point for the field, implying that the bar for a "trained" iterative inference system must be measured against such a simple baseline.

---

## Suggestions

1. **Restructure Section 5.4 to center Strategy ②.** Make the trained vs. training-free comparison the headline comparison for the ablation, rather than the comparison against Strategy ①. Characterize when and why trained tool coordination wins over the fixed crop heuristic — this is the crux of the contribution.
2. **Address SE-GUI-7B directly** in the data-efficiency discussion. Acknowledge that the sample count advantage over million-sample methods does not extend to SE-GUI-7B (3K), and frame the efficiency claim more precisely (e.g., relative to the specific baseline class the method targets).
3. **Add a sentence to the OSWorld-G discussion** that honestly acknowledges the near-zero gain of +0.8 points over the UI-TARS-1.5-7B base model and GTA1-7B's 67.7% on that benchmark.
4. **Annotate the two Qwen2.5-VL-72B-Instruct rows** in Table 3 with a footnote explaining the configuration difference.
5. **Align stage labels** between Figure 2 and the text (Stages 0–3 vs. Stages 1–3).
6. **Briefly analyze tool usage distribution** — at minimum, report the empirical frequency of each tool type across ScreenSpot-Pro evaluation to validate the design of all three tools.

---

## Score and Decision

**Originality:** The iterative focus refinement idea for GUI grounding is a reasonable extension of attention-inspired mechanisms and not a radical novelty, but the specific combination of RL-trained multi-tool coordination with an auxiliary CE loss to prevent format collapse is a concrete and new methodological contribution. **Score: 3/5**

**Importance:** GUI grounding accuracy at 7B scale is an active bottleneck for GUI agent deployment; achieving SOTA on a high-resolution professional benchmark is meaningful for the community. **Score: 3/5**

**Claims Supported:** The main accuracy claim (52.8% ScreenSpot-Pro SOTA at 7B scale) is well supported. The RL stability claim is well supported by Figure 3. The data-efficiency claim is overstated relative to SE-GUI-7B. Generalization claims are overstated on OSWorld-G. **Score: 3/5**

**Soundness:** The three-stage training pipeline is clearly described; the modified GSPO objective is well-formulated and ablated; reward components are systematically studied. Selective narrative framing around the training-free baseline and OSWorld-G results is the main soundness concern. **Score: 3/5**

**Clarity:** Generally clear, with some presentation issues (duplicate table rows, stage label misalignment, selective framing in results). **Score: 3/5**

**Community Value:** The transparent documentation of failure modes (Strategy ①, Stage 1 collapse, discarded RL variants) and the practical recipe for multi-tool RL stabilization have genuine community value beyond the benchmark result. **Score: 4/5**

The paper makes a real and transparent contribution at 7B scale on ScreenSpot-Pro, with a technically novel RL stabilization mechanism. The weaknesses are primarily presentation and framing issues rather than fundamental methodological flaws. The core results are reproducible against a public leaderboard. Despite the overstated data efficiency claim and the modest margin over the training-free baseline, the work clears the bar for a weak accept with revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>