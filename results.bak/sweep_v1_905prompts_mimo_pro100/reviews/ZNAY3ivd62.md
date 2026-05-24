Now I have all the data I need. Let me write the final review.

## Summary

GUI-Spotlight introduces a multi-tool reinforcement learning framework for iterative GUI visual grounding, teaching a 7B model to progressively narrow its focus using crop, extract, and find-color tools. The model is trained in three stages (SFT warm-up, RL with a stabilized GSPO objective, high-resolution refinement) on only 18.5K curated samples, achieving 52.8% on ScreenSpot-Pro—surpassing models trained on orders of magnitude more data. The paper also contributes a modified RL objective with a tool-filtered cross-entropy loss that prevents training collapse and documents several negative results on RL variants and reward design choices.

## Strengths

- **Exceptional data efficiency with strong results**: GUI-Spotlight achieves 52.8% on ScreenSpot-Pro with 18.5K samples, surpassing V2P-7B (50.6% with 9.6M samples) and GTA-1-7B (50.1% with 1.56M samples). This is a concrete, verifiable achievement (Table 3) demonstrating that well-curated small-scale training can beat massive data scaling.

- **Stabilized RL training via tool-filtered positive CE loss (Equation 1, Figure 3 right)**: The auxiliary cross-entropy term $\mathcal{J}'(\theta)$, computed only over format-valid and result-correct samples, prevents the RL collapse observed in vanilla GRPO/GSPO. The right panel of Figure 3 clearly shows vanilla methods oscillating and degrading around 300 steps while the proposed method continues improving. This is a genuinely useful contribution for multi-turn tool-use RL.

- **Consistent improvements across backbones and benchmarks**: On ScreenSpot-Pro, the UI-TARS variant improves across all six domains over its base (Table 3); the Qwen variant gains +11.9 points over its raw baseline. On UI-Vision (Table 4), gains of +5.3 and +7.4 over respective bases. On OSWorld-G (Table 5), the UI-TARS variant reaches 62.7%, matching UI-TARS-72B.

- **Transparent documentation of negative results**: Section 4.1 reports that retaining top-p% uncertain prompts and continuously updating the reference policy both degrade accuracy (variants ④ and ⑥ in Figure 3 left). Section 4.2 shows that dense Answer rewards perform marginally worse than sparse ones (Figure 4 left). This level of transparency about what didn't work is valuable for practitioners.

- **Well-designed ablation on reward composition**: Figure 4 right demonstrates that adjusting the Crop/Extract ratio from 0.15/0.15 to 0.25/0.05 yields a 10.5% accuracy gap, with a plausible explanation (Extract is easier to use than Crop since it only requires indicating approximate location rather than precise bounding box coordinates).

## Weaknesses

### Fatal
None

### Major

- **Selective comparison that obscures a stronger 7B baseline on OSWorld-G**: The paper states that "the 7B-scale GUI-Spotlight remains competitive with 72B-scale models" on OSWorld-G (Section 5.3). While this is technically true against the 72B entries, Table 5 shows that GTA1-7B achieves 67.7% average—5 points higher than GUI-Spotlight's 62.7%. GTA1-7B also dominates on Element Recognition (82.1% vs 60.6%), Layout Understanding (74.2% vs 63.2%), and Fine-grained Manipulation (70.5% vs 45.6%). The paper omits this comparison, which is the most relevant 7B baseline on this benchmark and significantly weakens the "competitive with larger models" narrative.

- **Weak absolute performance of Qwen variant on UI-Vision undermines the "generality" claim**: GUI-Spotlight initialized from Qwen2.5-VL-7B achieves only 8.3% on UI-Vision (Table 4), despite a +7.4 gain over the raw Qwen baseline (0.9%). The paper uses this as evidence that "our RL objective and multi-tool coordination transfer beyond UI-specialized backbones" (Section 5.1). However, 8.3% is far below the UI-TARS variant (23.4%) and below even basic models like OS-Atlas-7B (9.0%) or UGround-V1-7B (12.9%). The cross-backbone claim would be much stronger if the Qwen variant achieved competitive absolute numbers; the current results mostly confirm the Qwen backbone is weak at GUI grounding, not that the training framework transfers robustly.

### Minor

- **Stage labeling is confusing in Figure 2**: The figure shows a progression from Stage 0 (39.3%) to Stage 1 (17.8%) to Stage 2 (49.6%) to Stage 3 (52.8%), but Stage 0 corresponds to the base model before any training, Stage 1 is SFT, Stage 2 is RL, and Stage 3 is high-res refinement. The text at line 140 uses different numbering: "Stage 1: We perform one epoch of SFT... Stage 2: We train on 12K examples with RL... Stage 3: we then introduce additional 4000 samples." The figure's zero-indexed numbering versus the text's one-indexed numbering creates inconsistency.

- **ScreenSpot-Pro results mix self-evaluated and leaderboard numbers**: Table 3 footnote states "Besides GUI-Spotlight, we evaluated UI-TARS-1.5-7B using its official GitHub instructions... results for the other models are taken from the ScreenSpot-Pro leaderboard." This means some baselines may have been evaluated under different prompting or evaluation protocols than GUI-Spotlight. While this is common practice, it introduces potential inconsistency in the comparison.

- **The find_color tool's practical utility is unclear**: The find_color tool requires a target RGB value as input (Table 1), but the paper never explains how the model learns to determine the appropriate RGB value for a given instruction during inference. While the tool functions, the paper would benefit from analysis of how frequently it is invoked and whether it meaningfully contributes to final accuracy compared to crop and extract.

### Trivial
None

## Nice-to-Haves
- A latency analysis comparing GUI-Spotlight's multi-turn inference (potentially 3+ forward passes per sample) versus single-pass baselines would strengthen the practical utility discussion.
- Analysis of failure cases on ScreenSpot-Pro (e.g., what types of elements does the model still fail on?) would guide future work.

## Removed Points
These points are flagged to be removed, treat them with caution.

- "Weaknesses about missing related works" — removed per hard rules, as external existence cannot be confirmed.
- "Reproducibility concerns about hyperparameters in appendix" — removed per hard rules; appendix is stripped by parser but exists in the original.
- "Formatting/style nitpicks" — removed per hard rules; these are parser artifacts.

## Novel Insights

The paper's most novel insight is the tool-filtered positive cross-entropy loss ($\mathcal{J}'(\theta)$) for stabilizing multi-turn tool-use RL. The key observation—that broad autonomous exploration causes format violations in structured tool calls, leading to sparse rewards, high-variance gradients, and training collapse—is specific to the multi-tool RL setting and the proposed solution of filtering to format-valid, result-correct samples for the auxiliary loss is elegant. The negative results about top-p% filtering and continuous reference-policy updates being counterproductive in this setting are also genuinely useful for the community. The paper also provides a compelling case study in data efficiency: careful curation of 18.5K samples via a multi-stage quality filter can beat training on millions of samples, which has broader implications for GUI grounding research.

## Suggestions
- On OSWorld-G, explicitly compare against GTA1-7B and discuss why GUI-Spotlight falls short on this benchmark despite strong ScreenSpot-Pro results. This would make the paper more honest and help identify where multi-tool RL is less beneficial.
- Clarify the stage numbering to be consistent between Figure 2 and the text (either zero-index or one-index both).
- Add a small analysis of tool usage frequency: how often does the model invoke each tool, and does the tool distribution shift across benchmarks?

## Anchor Comparison Summary

| Anchor | Avg Score | Round | Comparison to GUI-Spotlight |
|--------|-----------|-------|-----------------------------|
| UGround (kxnoqaisCT) | 7.75 | 1 | Foundational paper with massive data scale and novel problem framing; GUI-Spotlight builds on UGround data and is more targeted but less foundational |
| OS-Atlas (n9PDaFNi8t) | 7.50 | 2 | Large-scale data/model with comprehensive cross-platform toolkit; GUI-Spotlight has narrower scope but interesting methodological innovation |
| AgentTrek (EEgYUccwsV) | 7.33 | 2 | Trajectory synthesis for GUI agents; different contribution type but similar venue quality |
| Policy-aware Reward (iamWnRpMuQ) | 7.00 | 2 | RLHF reward modeling; less related but sits at score boundary |
| Grounding MLLM (M9iky9Ruhx) | 6.00 | 1 | GUI grounding with data collection and lightweight module; GUI-Spotlight has more methodological novelty and better data efficiency |
| Reinforced UI Grounding (nNyjIMKGCH) | 5.75 | 1 | RL for UI grounding; GUI-Spotlight has stronger results and more thorough ablations |
| Aguvis (FHtHH4ulEQ) | 5.50 | 1 | Vision-only GUI agent framework; GUI-Spotlight more focused on grounding with stronger results |
| SpiritSight (jY2ow7jRdZ) | 5.25 | 1 | Curriculum learning for GUI agent; GUI-Spotlight has more targeted contribution |
| UI-Pro (5wmAfwDBoi) | 4.25 | 1 | Design-space recipe for GUI grounding; GUI-Spotlight clearly stronger with novel method |

Round-1 bracket: 5.5–8.0. Round-2 bracket: 6.0–7.5. GUI-Spotlight is clearly stronger than Grounding MLLM (6.0) due to its more novel method (multi-tool RL) and better data efficiency story, but falls below UGround (7.75) and OS-Atlas (7.50) due to the selective OSWorld-G comparison, the weak Qwen variant absolute numbers, and narrower scope. The score settles near 6.5, between the 6.0 anchor and the 7.0+ anchors.

## Score and Decision

GUI-Spotlight presents a well-executed contribution to GUI visual grounding with genuinely novel methodological elements (the tool-filtered CE loss for RL stabilization, multi-tool iterative refinement) and impressive data efficiency. The experimental evaluation is generally thorough, with comprehensive ablations on RL variants and reward design. However, the selective OSWorld-G comparison (hiding GTA1-7B's superior 7B performance) and the weak absolute numbers of the Qwen variant on UI-Vision are substantive concerns that prevent the paper from reaching the top tier. The paper is clearly above the 6.0 anchor (Grounding MLLM) and sits below the 7.0+ anchors (UGround, OS-Atlas) that have broader scope and more rigorous comparison practices.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>