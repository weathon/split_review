Now I have the full paper. Let me synthesize the final review.

---

## Summary

SteadyThought (ST) addresses "under-thinking" in Large Reasoning Models (LRMs) — the phenomenon of abandoning promising reasoning trajectories too early in favor of repeated, often fruitless thought switching. The framework operates in three stages: entropy-based thought segmentation, thought completion (forcing each segmented thought to completion by suppressing trigger-word logits), and a SimPO-inspired thought-level preference optimization (STPO) conditioned on the shared promising-thought prefix. Experiments on three model scales and four benchmarks (including an OOD code benchmark) show consistent accuracy gains of +1.9% to +3.12% and token reductions of 17–39%.

---

## Strengths

- **Consistent accuracy gains and token reduction across diverse models and tasks (Table 1):** ST improves average accuracy by +1.9%, +3.12%, and +2.52% on DeepSeek-R1-Distill-Qwen-1.5B, Qwen3-8B, and DeepSeek-R1-Distill-Qwen-14B respectively, while cutting average token counts by 17–25%. Crucially, gains hold on the out-of-distribution LiveCode benchmark (+5.3% accuracy, −19.0% tokens for Qwen3-8B), providing strong evidence of transferable learning rather than data memorization.

- **STPO objective well-motivated and ablation-validated (Table 4):** The STPO loss (Eq. 7) conditions preference optimization on the shared promising-thought prefix and uses length-normalized rewards to avoid DPO's length bias. Table 4 directly shows STPO outperforms both SFT (memorizes specific patterns, poor on OOD and hard tasks) and DPO (fails to reduce tokens: 4273 vs. 2809 on MATH500) — the ablation is the most technically sound portion of the paper and the reasoning is convincing.

- **Formal and principled problem framing (Section 2.1):** The Bradley-Terry formulation of commit vs. switch trajectories as a preference optimization problem provides a clean mathematical grounding that motivates the entire pipeline.

- **Compelling OOD generalization evidence:** ST is trained solely on omni-math, yet LiveCode results in Table 1 show consistent gains across all three model sizes (e.g., +4.2% accuracy and −14.2% tokens for the 14B model), supporting the claim that ST teaches a transferable reasoning commitment pattern.

- **Entropy-threshold sensitivity analysis (Table 3):** The paper explicitly studies the threshold trade-off (2.8, 3.0, 3.2) and shows that 3.0 optimally balances segmentation granularity with data availability, with performance monotonically degrading in both directions.

---

## Weaknesses

### Fatal
None.

### Major

- **The Thought Completion stage mechanically replicates the same global suppression the paper criticizes, without acknowledgment.** Section 3.2 states: *"During decoding, we then sharply decrease the logits for these words, effectively suppressing their selection by driving their prediction probability close to zero."* This is applied to every segmented thought indiscriminately — i.e., global suppression regardless of whether the thought is promising. This is functionally identical to NOWAIT applied at training-data generation time. The paper's central distinction over NOWAIT/SEAL is that ST is *selective* rather than globally suppressive, but that selectivity only emerges from what STPO subsequently learns — not from Stage 2's construction logic. The paper presents the pipeline as inherently selective when in fact Stage 2 is blunt. This mechanistic inconsistency in the narrative should be acknowledged and explained: the preference optimization stage converts global-suppression-generated data into selective post-training behavior; this is a real claim that requires justification rather than elision.

- **Anomalous AIME2024 behavior on the 1.5B model partially contradicts the stated mechanism.** The data in Figure 2 shows that for DeepSeek-R1-Distill-Qwen-1.5B on AIME2024, the average number of thoughts *increases* from 12.87 to 18.21 after ST training, while the proportion of last thought *decreases* from 18.96% to 15.66%. The paper attributes this to "smaller models tackling high-difficulty problems tend to increase thought transitions," but this is precisely counter to the claimed mechanism of "commit to promising thoughts." If the method works by reducing unnecessary switching, thought count should not increase in any configuration. The hand-wavy explanation amounts to "the method does something different on different settings" without specifying a governing principle. The accuracy gain (27.5% → 31.2%) and length decrease (11273 → 8606) on this dataset can be accounted for by shorter individual thoughts rather than fewer switches, which raises the question of whether ST's benefit in this regime is really about commitment or about writing more concise chains. This specific case deserves trajectory-level analysis rather than a brief aside.

### Minor

- **The PCT (Proportion of Correct Thoughts) evaluation uses the same tools that define it.** Section 4.4.2 evaluates the training effect via PCT computed using the methods from Sections 3.1 and 3.2 — i.e., the same segmentation logic and trigger-word completion used to construct training data. This creates a partial circularity: changes in PCT after training may partly reflect how the model's outputs interact differently with the measurement tools, rather than purely changed reasoning behavior. The correctness signal (final answer check) is externally grounded, but the "thought count" and "correct intermediate thought" definitions are self-referential. This does not invalidate the finding, but the paper should acknowledge the circularity and explain why the absolute PCT drop (e.g., 54.90% → 40.40%) is nonetheless interpretable.

- **No explicit acknowledgment of the training-time vs. inference-time comparison asymmetry.** Table 1 compares ST (which requires fine-tuning on curated preference data from omni-math) against NOWAIT, SEAL, and NoThink (which are zero-training inference-time interventions). The paper treats all methods as symmetric comparisons throughout Section 4.3 without noting that ST's advantage over NOWAIT/SEAL includes the benefit of domain-relevant fine-tuning. A natural ablation would be: does NOWAIT or SEAL applied *after* fine-tuning on the same omni-math data close the gap? Without this control, it is not possible to attribute ST's improvement cleanly to the thought-level construction vs. the act of fine-tuning itself. Table 4's ablation addresses SFT/DPO/STPO but all are STPO-pipeline methods — it does not isolate the contribution of the thought-level preference structure versus simply having been trained.

- **The trigger word list is never fully specified.** Section 3.2 gives "wait" and "alternatively" as examples but the complete list is not provided in the main text. Without this, Stage 2 cannot be reproduced. The authors note that Appendix E discusses computational cost but the trigger word list is a methodological detail, not a cost discussion. The paper should include the full list in the main text or a table, especially given that Qwen3-8B and DeepSeek-R1-Distill-Qwen models may have different switching vocabularies.

### Trivial

- The paper does not specify precisely how many "initial tokens" at the start of a candidate step are checked for entropy in the segmentation procedure (Section 3.1), which is a minor reproducibility gap.

---

## Nice-to-Haves

- A trajectory-level case study comparing base model vs. ST model on identical prompts where the base model switches after a correct thought — showing that ST commits while the base model does not — would directly test the mechanism and is the most natural extension of the paper's own thesis.
- The NOWAIT failure on Qwen3-8B (13,274 tokens vs. 4,724 vanilla on MATH500 — a nearly 3× *increase*) is a striking result not discussed in the main text. This actively supports the paper's argument (global suppression can be harmful for some model architectures) and deserves explicit discussion rather than silent appearance in a table.
- Extending threshold analysis (Table 3) to Qwen3-8B and 14B models in the main text rather than deferring to the appendix would strengthen confidence in generalizability.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"Figure 1a/1b could reflect genuine rechecking rather than waste"** (Harsh Critic, Introduction notes): This is a plausible alternative interpretation but it is a scope-creep concern. The paper's claim is statistical — many responses switch after the first correct thought — and the entire paper addresses this population-level observation. Individual cases of genuine rechecking are not claimed to be absent.

- **"Training data size missing from main text"** (Harsh Critic): The paper says the training set is sampled from omni-math and specifies the models used for inference. The number of successful thought completions is a hyper-detail that would affect interpretation only marginally; the appendix likely covers this.

- **Strength: "Formal problem framing"** — Retained as minor strength but the Bradley-Terry instantiation is standard and not itself a contribution; it is a framing choice.

- **"Threshold generalizes across model families"** concern: The paper explicitly notes that Appendix D contains multi-model threshold results. Since appendices are stripped in parsing, this criticism is REMOVED per rules.

---

## Novel Insights

The paper's most interesting empirical observation — that NOWAIT *dramatically increases* token usage for Qwen3-8B (13,274 vs. 4,724 baseline tokens on MATH500) while *harming* accuracy — suggests that inference-time trigger suppression interacts non-monotonically with model architecture and training provenance. This implies that thought-switching vocabulary and the entropy landscape at switching points differ substantially across model families, and that a method calibrated for one architecture (NOWAIT was likely developed for DeepSeek-R1 distillations) may actively disrupt another (Qwen3-8B with its thinking-mode toggle). The ST framework's training-based approach is inherently architecture-agnostic in this respect, since the model learns from its own thought completions. This finding is underexplored in the paper but has independent value for the community.

---

## Suggestions

1. Explicitly acknowledge in Section 3.2 that Stage 2 uses global trigger-word suppression (same as NOWAIT inference-time), and add a paragraph explaining why the trained model generalizes this into *selective* behavior rather than globally suppressed switching.
2. Add a brief analysis of the 1.5B/AIME2024 case (more thoughts, shorter responses, higher accuracy) to either refine the mechanism claim or propose an alternative account of how ST helps when thought count increases.
3. Include the full trigger word list as a table, noting whether it differs across model families.
4. Add a footnote to Table 1 clarifying the training vs. inference-time distinction between ST and the baselines.
5. Discuss the NOWAIT token explosion on Qwen3-8B in Section 4.3 — it actively supports the paper's argument and is currently invisible.

---

## Evaluation on Key Axes

- **Originality:** The combination of entropy-based thought segmentation, logit-controlled completion, and SimPO-inspired thought-level preference optimization is novel as an integrated pipeline. Individual components are adapted from prior work, but the assembly and the STPO objective are genuinely new.
- **Importance:** Under-thinking in LRMs is a real and practically relevant problem; the paper addresses a well-motivated gap.
- **Claims supported:** Core empirical claims (accuracy + token reduction) are well-supported by Table 1. The mechanistic claims about *why* ST works are supported only indirectly and have the AIME2024 anomaly as a counterexample.
- **Soundness:** The training pipeline is methodologically sound. The mechanism story has the inconsistency identified above. The PCT evaluation has a partial circularity.
- **Clarity:** Writing is generally clear; the three-stage framework is well-presented. Missing trigger word list and per-model entropy threshold details reduce reproducibility.
- **Community value:** Strong. The results are reproducible in principle, the method is applicable to any LRM, and the code + training pipeline (if released) would be directly usable by the community.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>