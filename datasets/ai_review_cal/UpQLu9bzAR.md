- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information I need to verify every claim. Let me write the final consolidated review.

## Summary
VICtoR introduces a hierarchical reward model for vision-instruction correlation (VIC) in long-horizon manipulation. It decomposes tasks into stages (via a learned stage detector using MDETR + object state classifier) and motions (via a Motion Progress Evaluator trained with contrastive objectives on short motion videos), then uses potential-based shaping to produce dense rewards for RL policy training. The key claim is that this hierarchical structure allows VICtoR to provide informative rewards for unseen long-horizon task compositions without requiring long-horizon demonstrations, outperforming prior VIC methods by 25% average (43% on harder tasks).

## Strengths

1. **Quantitative superiority over prior VIC methods on long-horizon tasks**: VICtoR achieves a 43% improvement on the most challenging tasks (top half by motion count) and a 25% average gain across all ten tasks (Section 5.2, lines 181–182). The ablation in Section 5.3 further confirms that each hierarchical level (stage, motion, progress) contributes to the gain, with the progress signal being especially beneficial.

2. **Generalization from motion-level videos to unseen long-horizon compositions**: VICtoR is trained exclusively on action-free motion videos (short-horizon) and used to provide rewards for novel long-horizon tasks composed of those motions in arbitrary sequences, without requiring task-level demonstrations (Section 4 overview, line 26). This is a practical data-efficiency advantage over methods that require full task demos.

3. **Well-designed contrastive objectives with discriminative embedding validation**: The three contrastive losses (time, motion, language-frame) in Section 4.4 are clearly motivated by specific capabilities needed for in-motion progress assessment. The t-SNE visualization (Section 5.5, line 201) confirms that motion embeddings form distinct clusters, directly validating the motion contrastive objective.

4. **Real-world potential function validation on XSkill**: Figure 5 (Section 5.4, lines 190–198) shows that VICtoR's potential increases for correct real-world action sequences and decreases for incorrect actions — a capability not matched by the LIV baseline in the same setting. This provides evidence beyond simulation that the learned reward signal behaves sensibly.

## Weaknesses

### Fatal
None.

### Major
None. The harsh critic raised a critical concern about the stage detector potentially using ground-truth perception in simulation, but after careful verification this does not hold as a verified flaw: the paper states ground-truth is used "For policy training in this environment" (line 178) — i.e., for the RL policy's state input to speed up training — while the method section (lines 79–80) describes the Stage Detector as a fully learned pipeline using MDETR + classifier on image observations. These are separate systems. However, the ambiguity in the phrasing warrants clarification (see Minor weakness #1 below).

### Minor

1. **Ambiguity about the perception pipeline during simulation RL training**: Line 178 states "For policy training in this environment, we use a ground-truth object detector to speed up the process." While the method section (Section 4.2) clearly describes a learned Stage Detector (MDETR + classifier) that processes images, the experiments section never explicitly states that the reward model's stage detector uses this learned pipeline rather than the ground-truth detector during the RL experiments. The paper should clarify: "The ground-truth detector is used only for the policy's state input; the reward model independently processes images through its learned Stage Detector and MPE." This clarification is needed to remove any doubt about whether the learned stage detector is actually being evaluated in the main results.

2. **Baseline training data not fully specified**: LOReL and LIV are described as "finetuned on target-domain data" (line 179), but the paper does not specify whether this consists of long-horizon task demonstrations or the same motion-level videos used for VICtoR. Since VICtoR(task) — ablated on task-level data — still outperforms other baselines, the comparison is informative regardless. But without explicit data specifications, the reader cannot fully assess whether the 25%/43% improvements reflect algorithmic superiority, training data granularity differences, or both.

3. **Real-world evidence is limited to potential curve visualization**: The real-world experiments (Section 5.4) only show potential function plots on pre-collected XSkill videos, not actual RL policy training achieving task completion. The conclusion (line 216) claims VICtoR "successfully operates in both simulated and real-world environments," which overstates the real-world evidence — what is shown is that the reward model's outputs behave reasonably, not that it successfully drives a policy to complete real-world tasks.

4. **Confidence threshold λ_c not analyzed**: The motion confidence threshold λ_c (Eq. 5–7, lines 130–144) is a key hyperparameter that determines whether the MPE's motion selection is trusted or defaults to the first motion. No sensitivity analysis or ablation of λ_c is provided, making it unclear how robust the method is to this choice across different tasks.

5. **No evaluation of stage detector accuracy**: The paper evaluates end-to-end policy success rates but never reports the stage detector's per-frame classification accuracy or analyzes how errors in stage detection (e.g., false detections or missed transitions) propagate to the shaped reward signal. An oracle-stage ablation would isolate the perception gap from the reward architecture gap.

6. **GPT-4 output reliability not discussed**: Task knowledge (stage decomposition, required motions, object states) is generated by GPT-4 with no analysis of consistency across queries, hallucination risks, or sensitivity to prompt phrasing. This is a gap in understanding the method's robustness.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the learned Stage Detector (MDETR + classifier) against an oracle stage oracle (ground-truth stages) would directly quantify the perception gap and strengthen the claim that the full learned pipeline works end-to-end.
- Hyperparameter sensitivity analysis for λ_c (confidence threshold) and λ₁, λ₂, λ₃ (loss weights) would improve reproducibility.
- A real-world RL policy learning experiment demonstrating task completion (even on one task) would substantiate the real-world operational claim.

## Removed Points
These points are flagged to be removed — treat them with caution:

- **"Stage detector may use ground-truth in simulation" as a fatal/structural flaw**: The harsh critic framed this as a critical issue that "undermines the central claim." After verification, the paper's text states ground-truth is for "policy training" speed (line 178), while the method section (lines 79–80) describes the Stage Detector as a learned pipeline (MDETR + classifier) on images. There is no statement in the paper that ground-truth replaces the learned stage detector. The concern conflates the policy's state input with the reward model's perception pipeline, which are separate systems. Removed because it is a misinterpretation of the paper's intent, though the ambiguity is noted as a Minor clarity weakness (see Minor #1 above).

- **"Tables are missing from extracted text"**: The tables are included via \input{tables/...} commands that reference separate files not captured in the plain text extraction. The original submission contains these tables. This is a parser artifact, not a paper flaw.

- **"Object state categories not specified how they are obtained"**: The paper states (Section 4.1, line 73) that GPT-4 generates task knowledge including "the specific conditions or states of each object at these stages." The source of state categories is addressed.

- **Missing related works**: Removed per rule — cannot confirm existence of external sources.

- **Formatting/style/typo nitpicks**: All parser artifacts.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface a genuinely novel observation that the authors missed. The harsh critic's identification of the ground-truth perception ambiguity is a reasonable reading concern but, upon verification, reflects a conflation of the policy's state input and the reward model's perception pipeline rather than an actual flaw in the evaluation design.

## Suggestions
1. Add a sentence in Section 5.1 explicitly stating: "The ground-truth object detector is used only to provide state observations for the RL policy. The reward model (VICtoR) independently processes rendered images through its learned Stage Detector (MDETR + classifier) and MPE."
2. Specify what data LOReL and LIV were fine-tuned on (task-level demonstrations or motion-level videos) to remove ambiguity.
3. Report the stage detector's per-frame accuracy and add an ablation replacing it with an oracle to separate perception errors from reward architecture.
4. Tone down the real-world claim in the conclusion, or add a real-world RL experiment.
