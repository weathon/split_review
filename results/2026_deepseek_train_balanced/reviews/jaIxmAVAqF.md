## Summary

ActionVerse proposes to treat actions as a modality for MLLMs by encoding action candidates (e.g., viewpoint navigation options) as visual tokens extracted by DINOv2, inserted between task-specific special tokens (&lt;Move&gt;...&lt;/Move&gt;), and aligned with the LLM via projection layers. The method is trained with a conversation-like multi-turn procedure that includes disturbance-based data augmentation for implicit self-correction. Experiments on R2R-VLN and Web-VLN show that ActionVerse outperforms zero-shot LLM-as-agent baselines (NavGPT, MapGPT) and achieves the best reported results on Web-VLN, while using efficient LoRA fine-tuning.

## Strengths

1. **Treating actions as a modality rather than text.** Prior methods (NavGPT, AppAgent) represent actions as text descriptions in system prompts, which breaks long action IDs into meaningless token fragments and inflates prompt length. ActionVerse instead encodes action arguments as tokenized visual features (DINOv2 crops of navigable regions) placed between special tokens, preserving semantic structure and avoiding complex system prompts. This is clearly described in Section 3.1.1 (lines 84–93) and contrasted against existing approaches.

2. **Conversation-like training with disturbance-based augmentation.** The paper casts sequential action planning as a multi-round dialogue between an observer and a planner, and augments training data with deliberately wrong steps (e.g., A→B→D→B→C) to teach the model to recover from errors. The ablation (Table 3, lines 163–167) provides concrete evidence: the disturbance-augmented variant achieves the best NE, OSR, SR, and SPL scores, with only a modest TL increase from backtracking.

3. **Best Web-VLN performance and strong efficiency profile.** On Web-VLN (Table 2, line 148), ActionVerse achieves the best results among all compared methods. On R2R-VLN (Table 1), it outperforms other LLM-as-agent methods (NavGPT, MapGPT) across all metrics. Unlike API-dependent baselines, ActionVerse is trained on 4 A100 GPUs in ~1 day (LoRA) and deploys on a single quantized A5000 GPU with no API costs (Section 4.4, lines 181–183).

4. **Systematic ablation.** Tables 3 and 4 cleanly disentangle the contributions of conversation-like data, depth information, disturbance augmentation, and context length, providing evidence for each design choice.

## Weaknesses

### Fatal
None.

### Major

1. **The core claim — that action token encoding drives improvement — is not isolated from fine-tuning.** ActionVerse is fine-tuned with LoRA on task-specific data, but the paper only compares against *zero-shot* API-based methods (NavGPT, MapGPT) that are *not* fine-tuned. That a fine-tuned model outperforms zero-shot methods is expected and does not validate the action token design. The paper lacks a controlled experiment that holds the training setup (Vicuna + LoRA + same data) constant and varies only the action encoding format (proposed token-based vs. text-based action descriptions). Without this ablation, the reported gains cannot be attributed to the action-as-modality innovation — they could come from simply fine-tuning on the task data. (See Section 4.2, Tables 1–2 for the comparisons; the missing ablation is not performed anywhere.)

2. **The abstract overclaims relative to the results.** The abstract states ActionVerse "achieves performance comparable to state-of-the-art methods." However, the paper explicitly acknowledges on R2R-VLN (line 138) that "there remains a performance gap between our approach and the expert models specifically tailored for this task." These expert models *are* the state-of-the-art on this benchmark. The claim of "comparable to SOTA" is therefore misleading — ActionVerse is competitive *among LLM-as-agent methods* (which are themselves behind specialized expert models), not with the true state-of-the-art. (Abstract, line 4; vs. line 138.)

### Minor

3. **The "action encoder" is visual, limiting the claimed generality.** The action encoding (Section 3.1.1) uses DINOv2 to extract visual features of viewpoint crops — i.e., it encodes the visual appearance of the *destination*, not a representation of the action itself. The paper claims this "can be seamlessly extended to more generalized scenarios" such as "buttons on smartphones" and "robotic arms." However, the method as described would not naturally handle non-visual action arguments (e.g., Turn(45°), SetTemperature(72°F), or categorical arguments without visual grounding). The examples given (smartphone buttons, robotic arms) remain visually grounded, so the claimed generality beyond vision-grounded actions is unsupported.

4. **Inconsistent NavGPT prompt length.** The paper states in Related Work (line 61) that NavGPT uses "prompts up to three thousand words," but in Section 4.4 (line 183) it claims "approximately 15,000 tokens per instruction." Even accounting for tokenization expansion (~1.3 tokens/word), these figures differ by a factor of ~4. The discrepancy should be reconciled.

### Trivial
None.

## Nice-to-Haves

- A proof-of-concept on a task with a non-visual action argument (e.g., a discrete categorical action or a numeric parameter) would substantially strengthen the generality claim.
- Reporting standard deviations or multiple-run statistics would improve confidence in the reported metrics.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **"The 'Plain' baseline is not clearly defined."** — The paper defines it explicitly: "processes single-step decisions using only RGB images and action candidates as input" (line 165). The definition is adequate.
- **"Missing implementation details (projection layer architecture, DINOv2 feature pooling method, training set size, hyperparameters)."** — These details were likely in the appendix, which the parser strips from all papers. Removing per the rule about missing appendix content.
- **"Should compare against LLaRP and RoboFlamingo."** — These address different task settings (online RL, video-conditioned POMDP) not directly comparable to VLN. Demanding these baselines is scope creep.
- **Strength Finder claim about "avoiding API dependence" as a core strength.** — This is a valid supporting point but is a consequence of fine-tuning, not a direct test of the action encoding contribution. Kept the efficiency point as a supporting strength; removed its positioning as a core contribution.
- **Complaints about missing statistical significance / variance.** — Single-run evaluation is standard practice for large-scale navigation benchmarks like R2R. Not a meaningful weakness absent evidence of variance problems.

## Novel Insights

The paper's design reveals an implicit assumption worth flagging: for visually-grounded action spaces (navigation, web clicking), action arguments can be encoded as visual features of the *outcome state* (e.g., the image of the destination viewpoint). This collapses the distinction between "action encoding" and "goal-state encoding" — the model learns to select the visual feature that matches the desired next observation, rather than learning an abstract action representation. This choice is well-suited to navigation and GUI tasks, but it means the "action encoder" is really a scene-content encoder, which structurally limits the framework to actions whose arguments are visually observable in the current context. The paper does not discuss this design constraint, instead claiming "seamless" extension to general action planning. Acknowledging this as a design choice — rather than a universally general action encoding — would better position the contribution.

## Suggestions

1. **Run the missing controlled ablation**: Train Vicuna+LoRA on exactly the same data, but replace the DINOv2 action tokens with a text-based representation of action candidates (e.g., "Move to viewpoint_14, Stop"). If the token-based variant outperforms text-based, the core claim is directly supported. This single experiment is the highest-priority fix.

2. **Tone down the abstract**: Replace "comparable to state-of-the-art methods" with phrasing that accurately reflects the results — e.g., "competitive with existing LLM-as-agent methods on R2R-VLN and achieves state-of-the-art on Web-VLN."

3. **Reconcile the NavGPT prompt length numbers** between Section 2 and Section 4.4.

4. **Clarify the generality claim**: Either (a) demonstrate at least one non-visual action argument encoding (e.g., a simple categorical or numeric action on a third task), or (b) explicitly scope the framework to "visually-grounded action spaces" and discuss how non-visual arguments could be handled (e.g., via other encoders).

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>