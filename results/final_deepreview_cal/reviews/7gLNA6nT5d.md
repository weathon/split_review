Now I have enough context to write the consolidated review. Let me compile and calibrate my assessment.

**Calibration Summary:**

Round 1 bracketing: Three queries spanning (0-3.5), (3.5-7.5), (7.5+). Weak band anchors averaged 3.0-3.4 (papers with thin/incorrect contributions). Middle band anchors averaged 4.0-5.6 (papers with real but flawed contributions). Strong band anchors averaged 7.6-8.7 (accepted papers with clean evidence). The paper under review clearly falls in the middle band.

Round 2 (narrowing within 4.0-6.5):
- **Memory-Efficient AD (5.50)**: Most directly comparable — also modifies AD's architecture, same environments, same issues (limited baselines, narrow scope). The paper under review has more architectural novelty (n-gram heads from NLP) but similar experimental limitations. Slightly stronger than this anchor. 
- **Actions Speak Louder (4.75)**: ICRL analysis paper with fundamental issues about the ICRL framing itself. Paper under review is cleaner methodologically. Stronger than this anchor.
- **ReLIC (4.67)**: Embodied ICRL. Interesting but limited validation on simple sim environments.
- **RA-DT (4.67)**: Retrieval-augmented ICRL. Similar level of contribution.

The paper under review's architectural novelty (bringing n-gram heads from language to RL) is genuine, and the empirical evidence shows consistent gains across environments. But the 27× data-efficiency claim is not supported by a controlled comparison, some ablation conditions are unreported, and only AD is used as baseline. I place the paper at **5.0** — a methodologically sound but incompletely supported contribution that would benefit from revision.

---

## Summary

This paper proposes integrating n-gram induction attention heads into transformers for in-context reinforcement learning (ICRL), adapting a mechanism previously shown to benefit in-context learning in language models. The authors build on Algorithm Distillation (AD), replacing one of the transformer's attention layers with an n-gram layer that explicitly computes match statistics over discrete states (or quantized image observations). Experiments on Dark Room, Key-to-Door, and Miniworld (pixel-based) environments show that the n-gram variant reaches near-optimal performance with fewer hyperparameter search iterations and less training data than the standard AD baseline.

## Strengths

- **First adaptation of n-gram induction heads to decision-making / ICRL.** The paper brings a well-motivated architectural modification from the language in-context learning literature (Akyürek et al., Edelman et al.) into the reinforcement learning setting. This is a genuine novelty and the paper demonstrates it is non-trivial (requiring vector quantization for pixel observations, designing matching strategies for RL sequences).

- **Consistent reduction in hyperparameter search cost across environments.** The paper uses random search with Expected Maximum Performance (EMP), a sound evaluation protocol. Across Dark Room, Key-to-Door, and Miniworld, the n-gram model reaches high EMP with substantially fewer hyperparameter assignments than the baseline (e.g., ~20 assignments vs. ~400 for Dark Room with 1K histories, Figure 2). This is the most solidly supported claim.

- **The permuted-mask control experiment (Table 1c) is well-designed.** By randomly shuffling the n-gram attention matrix, the paper shows that a broken n-gram head does not degrade performance (0.51±0.03 vs. baseline 0.52±0.02). This addresses the concern that the n-gram layer might harm performance when matching fails, especially relevant for the VQ-based image setting.

- **Ablations on n-gram length and layer position (Tables 1a, 1b) suggest these hyperparameters are not sensitive**, so the method does not introduce burdensome new tuning requirements.

## Weaknesses

### Major

1. **The "27× data efficiency" claim is not supported by a controlled experiment.** The paper asserts this number in the abstract and in Section 4.2, citing Appendix B. The claim appears to compare the n-gram method's data (100 goals, ~750 histories) against the original AD paper's published configuration (2048 goals, 2048 histories). This is an apples-to-oranges comparison: different experimental setups, different data pipelines, and no evidence that the same AD baseline, run under the paper's own conditions with 2048 goals, would match the original AD paper's results. The paper does include a controlled scaling experiment (Figure 1) showing that n-gram outperforms baseline at every goal count — this evidence supports a qualitative claim of "better data efficiency" but not the specific factor of 27×. The 27× number should either be removed or re-derived from a direct scaling experiment where both methods are trained on matched datasets of varying sizes and the n-gram method demonstrably matches AD's peak at a quantified fraction of the data.

2. **The experimental conditions for the ablation experiments (Section 4.4, Table 1) are unreported.** The paper states it "conducted six random hyperparameter searches in Miniworld-Dark" but does not specify the number of training goals, number of learning histories, batch size, or evaluation protocol used. This creates a disconnect: in Figure 5 (Miniworld-Dark, 30 goals, 50 histories) the baseline reaches EMP ≈ 0.85, while in Table 1(c) the baseline EMP is only 0.52 ± 0.02 for the same environment. Without knowing the data conditions for Table 1, it is impossible to tell whether the results reflect properties of the n-gram method or simply a weaker baseline due to different data conditions. The paper must report the full experimental setup for each ablation table.

### Minor

3. **The hyperparameter sensitivity comparison is asymmetric.** The random search for the main results (Section 4.1) covers "core transformer hyperparameters" while fixing the n-gram-specific ones (length, position). The separate ablations (Section 4.4) show these are insensitive, which partially addresses the concern. However, the comparison would be cleaner if the n-gram HPs were included in a single unified search alongside the core HPs, to measure whether the overall search budget required by the n-gram method still wins when its own HPs are included.

4. **Only one ICRL baseline (AD) is compared.** The paper does not compare against other ICRL methods such as Lee et al. (2023) or retrieval-augmented variants. While building on AD makes this a natural choice, the claim that n-gram heads "improve ICRL" broadly is weaker without evidence that the benefit extends beyond the specific AD implementation.

5. **No analysis of what n-gram patterns are actually learned.** For a method built on explicit sequence matching, the paper would benefit from qualitative analysis — e.g., what fraction of n-gram matches are found in the data, whether the model focuses on repeated states or action sequences, and whether the VQ indices for Miniworld observations reliably group semantically equivalent states.

### Trivial

6. The caption of Figure 5 refers to "Miniworld-Dark" while the text at line 190 mentions "Miniworld-Dark (Room, omitted for brevity)" — minor inconsistency in naming.

## Nice-to-Haves

- Validate VQ reconstruction accuracy for the Miniworld setting: report how often valid n-gram matches are found, and whether small visual perturbations change the VQ indices.
- Include confidence intervals or error bars on the EMP curves (e.g., across random search seeds).
- A controlled data-scaling experiment on Key-to-Door where both methods are trained on varying dataset sizes (e.g., 100, 250, 500, 1000 goals) and the dataset size at which n-gram matches AD's peak is identified, would directly support any quantified data-efficiency claim.

## Removed Points

These points from the harsh critic were removed or demoted for the reasons stated:

- **"Internal inconsistency between ablation conditions and main results — the narrative coherence across experiments is broken."** This is real but the critic framed it as a "structural issue" that makes the permuted-mask control "uninterpretable." It is actually a reporting gap (conditions unreported), not a structural flaw. Demoted to Major weakness 2 above.
- **"Hyperparameter-sensitivity comparison is not a fair test of ease of training" in its original framing.** The critic claimed the search excluded n-gram hyperparameters. This is true but the paper separately addresses this in Section 4.4. The core concern merged into Minor weakness 3 above. The framing that the comparison is "asymmetric" is softened to a minor recommendation.
- **"No comparison to other ICRL methods"** — weakened to Minor weakness 4. The paper explicitly builds on AD and the scope is reasonable; this is a nice-to-have, not a gap.
- **"No analysis of what n-gram patterns are learned"** — moved to Minor weakness 5 (and is a nice-to-have, not a core flaw).
- **"Statistical significance" and "VQ validation"** — moved to Nice-to-Haves.
- The Strength Finder's claim about "27× data efficiency" as a core strength is downgraded in the review because the claim is not well-supported. The underlying observation (better data efficiency in controlled experiments) is retained in Strengths but qualified.

## Novel Insights

The paper provides a demonstration that architectural inductive biases shown to help in-context learning in language (explicit n-gram matching) also transfer to the RL setting, where sequences consist of state-action-reward triples rather than tokens. This is non-obvious because RL sequences have fundamentally different structure (policy improvement trajectories rather than natural language n-gram statistics). The key insight is that replacing soft attention with hard n-gram pattern matching provides a stronger learning signal in low-data ICRL regimes without degrading performance when the matching is ineffective. None of the reviewers captured this transfer perspective beyond noting it as a "first application."

## Suggestions

1. **Fix the 27× claim.** Either add a controlled data-scaling experiment (train both methods on identical datasets at multiple sizes and show n-gram reaches AD's peak performance at a measured fraction of the data) or drop the specific number in favor of a qualitative claim with Figure 1 as evidence.
2. **Report all experimental conditions for the ablations (Table 1).** Specify the number of goals, histories, batch size, and evaluation protocol for each ablation so readers can reconcile them with the main results.
3. **Unify the hyperparameter search** by including n-gram length and layer position in the random search alongside core HPs, or at minimum justify why the separate ablation is sufficient.
4. **Add at least one additional ICRL baseline** (e.g., the supervised pretraining method of Lee et al. 2023) to show the benefit is not AD-specific.
5. **Add qualitative analysis** of matched n-gram patterns in discrete and visual environments to build intuition about what the model exploits.

## Score and Decision

**Score:** 5.0  
**Decision:** Reject

The paper proposes a genuinely novel architectural modification for ICRL and provides consistent positive evidence across multiple environments. However, the strongest quantitative claim (27× data efficiency) is not supported by a controlled comparison, key ablation conditions are unreported, and the evaluation is limited to a single baseline. These issues are addressable through additional experiments and clearer reporting, but in its current form the paper's conclusions are not adequately justified.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>