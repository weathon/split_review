Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes FAB (Foundation Acoustic model Backdoor), a task-agnostic backdoor attack against acoustic foundation models (AFMs). The attack injects a backdoor into a pre-trained AFM using only an auxiliary dataset (not the original pre-training data), without access to the codebook or projection matrix. The backdoor is designed to preserve benign performance while degrading performance on any downstream task when a physically realizable, sync-free, input-agnostic trigger (e.g., a siren or bark) is played alongside the input. The paper evaluates FAB on two AFMs (HuBERT, WavLM), nine downstream tasks from the SUPERB benchmark, four trigger sounds, and two defenses, including a small physical over-the-air experiment.

## Strengths

- **Task-agnostic degradation across nine diverse downstream tasks.** Table 1 evaluates FAB on content tasks (ASR, PR, KS), speaker tasks (SID, ASV, SD), semantics tasks (IC, ST), and paralinguistics (ER) — substantially broader than prior acoustic backdoor work, which typically tested only one or two tasks. The attack degrades triggered performance sharply across all tasks while benign performance remains broadly comparable to the unbackdoored AFM.

- **Physically realizable, sync-free, input-agnostic triggers under a realistically constrained threat model.** The paper demonstrates that triggers remain effective in over-the-air recordings (Table 2: WER ≥71%) even when played at random offsets (sync-free) and superimposed on arbitrary inputs (input-agnostic). The threat model is genuinely weaker than prior work: the adversary has no access to pre-training data, codebook, projection matrix, or pseudo-labels, and uses only a small auxiliary dataset (~8% of pre-training size).

- **Weak threat model assumptions validated against a permissive baseline.** The paper shows (Appendix C.2) that the constrained attack achieves success comparable to a knowledgeable adversary who has full access to the codebook, projection matrix, and pre-training pseudo-labels, demonstrating that the practical constraints do not fundamentally limit attack effectiveness.

- **Comprehensive ablation studies.** The paper systematically varies trigger type, AFM architecture (HuBERT vs. WavLM), auxiliary dataset size, SNR, layer choice, and loss function design, providing evidence that FAB's success is not narrowly dependent on a single configuration.

## Weaknesses

### Fatal

None.

### Major

- **"Benign performance preservation" claim is overstated relative to the evidence.** The paper repeatedly claims FAB "preserves" benign performance, yet Table 1 shows non-trivial degradation on several tasks. ASR WER increases from 4.99 (benign AFM) to 5.93 (backdoored AFM) — a ~19% relative increase. PR PER rises from 11.7 to 14.8 — a ~26% relative increase. While these numbers may still be "comparable" in a loose sense, a downstream developer choosing between a model with WER 4.99 and one with WER 5.93 (or PER 11.7 vs 14.8) would notice the difference. The paper provides no threshold or criterion for what level of degradation constitutes "preserved" performance. This is the most significant weakness because attack plausibility hinges on the backdoored model being indistinguishable from a benign model in practice.

- **No error bars, variance, or statistical significance across any main result.** Every number in Tables 1–4 is reported as a single point with no indication of variance. Downstream fine-tuning is inherently stochastic (random seeds, data shuffling, optimization noise). Without multiple seeds or confidence intervals, the reader cannot assess whether observed differences between benign and backdoored AFMs (e.g., ASR 4.99 vs 5.93) are stable or merely noise. This is a standard expectation for experimental ML papers and weakens all quantitative claims, particularly those about benign performance preservation.

- **Physical realizability experiment is too limited to robustly support the claim.** The physical evaluation (Section 6.2) uses 23 samples, one task (ASR), one device setup (MacBook microphone, iPhone speaker at 1m), one environmental condition (~62 dB ambient). No variation in distance, background noise, microphone quality, or speaker type is tested. The gap between digital WER (99.67) and physical WER (71.47–77.75) is large and unaddressed. Given that physical realizability is a headline contribution distinguishing FAB from prior work (Koffas et al. 2022), this evidence base is too thin. The paper acknowledges the labor cost but does not discuss what the digital-to-physical gap implies about robustness.

### Minor

- **Defense evaluation is limited in scope and could be more carefully interpreted.** Only two defenses (fine-pruning and input filtration) are tested, on only one task (ASR), with no justification that these are representative defenses for speech/backdoor contexts. The interpretation in the paper ("they fail to decrease the attack success") is not wrong, but the more informative finding is that the defenses cannot remove the backdoor without destroying benign performance (e.g., at 50% pruning, benign WER jumps to 89.89). This is a different (and weaker) claim than "FAB is robust to defense." Adaptive or FAB-aware defenses are not discussed.

- **The "inconspicuous" trigger claim is asserted without any perceptual evaluation.** The paper describes triggers (siren, bark, oboe, flute) as "mundane" and "inconspicuous" but provides no user study, SNR-based perceptual metric, or even a discussion of contexts where a siren would be conspicuous (e.g., quiet office vs. urban street). This is a framing gap rather than a fatal flaw, since the paper primarily focuses on the technical attack properties.

- **Only the frozen-AFM fine-tuning paradigm (SUPERB) is tested; full fine-tuning is not evaluated.** The SUPERB benchmark uses frozen AFM + lightweight prediction heads. Many real-world deployments fine-tune the full model end-to-end. If full fine-tuning removes the backdoor, the attack's practical relevance is reduced. The paper should either test this or explicitly discuss the limitation.

- **The backdoor causes performance degradation (denial-of-service), not targeted misclassification.** This is a fundamentally different threat model from most prior backdoor work (which causes targeted misclassifications). The paper never explicitly positions this design choice, making it harder to compare with the broader backdoor literature. A brief discussion would clarify the contribution.

- **Ambiguity about whether the main HuBERT results use from-scratch pre-trained or publicly downloaded weights.** The paper states it pre-trained HuBERT from scratch "for ablation tests" but also says "unless otherwise mentioned, we report results on HuBERT" — it is ambiguous whether Table 1 uses the from-scratch model or a downloaded checkpoint. The paper should clarify this, since the threat model assumes downloading published weights.

- **The computational cost of backdoor injection is not reported.** Wall-clock time, GPU hours, and hardware used would strengthen the practicality claims.

### Trivial

None.

## Nice-to-Haves

- A proper physical experiment with 50–100 samples, 2–3 triggers, 2–3 noise conditions, and 2 distance settings, with mean ± std across conditions.
- Error bars (≥3 seeds) for Table 1 to establish which benign-performance differences are stable.
- An explicit threshold for "benign performance preservation" (e.g., within X% relative of the benign AFM on each task), with a discussion of which tasks pass and which do not.
- Testing on one additional downstream fine-tuning paradigm (e.g., full fine-tuning of the AFM).
- A brief discussion of adaptive defenses aware of FAB's mechanism (e.g., detecting representations collapsing toward a fixed vector).
- Reporting GPU hours and hardware for the backdoor injection process.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about Appendix C.7 being "referenced but not available in the parsed text":** The parser strips appendix content from all papers; these sections exist in the original submission. Per Rule 9, this is not a valid weakness.
- **The reviewer's demand to "verify against specific references" the claim that "past input-agnostic attacks only apply to task-specific models":** The paper clearly cites and categorizes prior work (Koffas et al. 2022 as input-agnostic, task-specific). Without external access to Koffas et al. 2022, neither I nor the reviewer can independently verify the claim, and the rule against missing-related-works criticisms applies. The paper's positioning is internally consistent.
- **Criticism that the paper should discuss "perceptual inconspicuousness" via SNR or user study at length:** While not entirely removed, this was downgraded from the reviewer's framing as a central weakness to a minor point. The paper's primary contribution is technical, and the triggers (siren, bark, oboe, flute) are plausibly mundane sounds; a full perceptual study would strengthen the paper but is not essential to its core technical claims.
- **"The paper should test whether FAB survives full fine-tuning"** is moved from a major criticism to a minor limitation, since the paper explicitly follows the SUPERB evaluation paradigm (frozen AFM + lightweight heads), which is the standard evaluation protocol for AFMs. Full fine-tuning is a reasonable extension but not a scope violation.
- **Strength Finder's strength about "Resistance to established defenses"** is retained but qualified: the defense evaluation shows these defenses cannot remove the backdoor without destroying the model, which is a real result but weaker than "FAB is robust to defense."

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same set of strengths (broad task coverage, weak threat model, physically realizable triggers) and weaknesses (thin physical experiment, missing error bars, overclaimed benign preservation) without introducing fundamentally new analytical perspectives beyond what the paper itself provides. The most notable cross-review insight is that the benign performance gap on ASR and PR (~19–26% relative) is large enough to plausibly deter adoption, which the paper glosses over in its "preserves benign performance" framing.

## Suggestions

1. **Define and rigorously evaluate benign performance preservation.** Establish an a priori threshold (e.g., "within 5% relative of the benign AFM on each task") and honestly report which tasks pass and which do not. If ASR and PR fail the threshold, either improve the method or revise the claim from "preserves" to "largely preserves with modest degradation on content tasks."

2. **Add error bars to all main results (Table 1) by running fine-tuning with at least 3 random seeds.** This is the single highest-leverage improvement — it would clarify whether the observed differences between benign and backdoored AFMs are real or noise.

3. **Expand the physical experiment to at least 50 samples with basic variation in conditions (2 distances, 2 noise levels) and report mean ± std.** Acknowledge and discuss the digital-to-physical performance gap rather than presenting it without commentary.

4. **Clarify the HuBERT setup:** explicitly state whether Table 1 uses the from-scratch pre-trained HuBERT or the publicly downloaded checkpoint, and clarify that the from-scratch model was used only for ablation comparisons.

5. **Discuss the denial-of-service nature of the attack** explicitly and position it relative to targeted misclassification backdoors in the broader literature.

## Score and Decision

This paper addresses a timely and well-motivated problem with a technically creative approach (codebook approximation via k-means under a weak threat model is neat). The breadth of the evaluation across 9 tasks is a clear strength. However, the evaluation has three significant gaps that prevent the paper from fully supporting its claims: (1) the "benign performance preservation" claim is contradicted by non-trivial degradation on ASR and PR, (2) no statistical variance is reported anywhere, and (3) the physical realizability experiment (a headline contribution) is based on only 23 samples with no variation. These are addressable with additional experiments and more careful presentation, but in the current form the contribution is overstated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>