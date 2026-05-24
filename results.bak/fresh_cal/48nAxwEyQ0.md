Here is the consolidated final review.

---

## Summary

This paper presents FAVEN, an architecture for audio-visual embodied navigation that integrates audio and visual data from the earliest processing layers via learnable fusion tokens and multi-modal cross-attention blocks, with an additional Mamba-based fusion extension. The approach is evaluated on two standard benchmarks (Replica and Matterport3D), showing improvements in SR, SPL, and SNA over prior methods (AV-Nav, AV-WaN, ORAN), alongside a single-trial real-world demo and ablation studies.

---

## Strengths

1. **Strong quantitative results on two benchmarks.** The paper reports consistent improvements across all three metrics (SR, SPL, SNA) for both heard and unheard sound settings on Replica and Matterport3D. Specific numbers are given in-text — e.g., on Matterport3D unheard sounds, FAVEN achieves SPL 51.9 vs. AV-WaN's 37.1 (line 153). Gains are reported against multiple baselines (AV-Nav, AV-WaN, ORAN).

2. **Ablation studies confirm each component's contribution.** Table 3 (described in text, line 163) shows that removing learnable fusion tokens (LFT) drops SPL Heard from 83.8 to 72.3, removing multi-modal interaction blocks (MIB) drops it to 73.5, and removing Mamba drops it to 76.9 on Replica. This provides causal evidence that all three architectural components contribute to the reported performance.

3. **Systematic analysis of design choices.** Table 4a (line 178) analyzes fusion token count — 3 tokens yields peak SPL Heard 83.8 vs. 75.1 with 1 token. Table 4b (line 180) analyzes early fusion depth — 9 layers is optimal. These ablations offer practical design guidelines beyond the main results.

4. **Quantified search time reduction.** Section 4.2 (line 155) reports up to 88.8% decrease in search time on Replica relative to the best baseline, with visual confirmation in Figure 1. This directly supports the "fast" claim in the title.

---

## Weaknesses

### Fatal
None.

### Major

1. **Abstract SPL numbers do not match body text.** The abstract claims SPL improvements of "10.4 and 6.5 on heard and unheard sounds" (line 4). However, the body reports: Replica vs. ORAN: Heard 9.3, Unheard 3.6 (line 147); Matterport3D vs. AV-WaN: Heard 11.3, Unheard 14.8 (line 153); Matterport3D vs. ORAN: Heard 9.9, Unheard 4.9 (line 153). None of these pairs matches 10.4/6.5. It is unclear which baseline/dataset the abstract numbers refer to, or how they were computed. This is a significant reporting inconsistency that undermines trust in the results.

2. **Mamba efficiency claim is completely unsubstantiated.** The Mamba-based fusion is presented as a contribution (listed in contributions, line 17, described in Section 3.4) with the theoretical claim of reducing complexity from O(n²) to O(n). Yet **no runtime, inference time, or throughput measurement appears anywhere in the experiments**. The ablation in Table 3 tests "w/o Mamba" but only reports SR/SPL/SNA — never speed. The paper's central claim of "fast" navigation rests partly on this component, but there is zero empirical evidence that Mamba actually improves efficiency in this context.

3. **SNA metric is not formally defined.** "Success weighted by Number of Actions" (line 136) receives only a qualitative description: "penalizing excessive rotations or unnecessary movements." No formula is given. Since SNA is not a standard metric in navigation literature and is used as a primary evaluation criterion alongside SR and SPL, the lack of a precise definition makes the results impossible to interpret or reproduce.

4. **Real-world evaluation is anecdotal.** Section 3.5 reports a single trial in one apartment (agent navigates to a clock on a Mac computer in 21 seconds). The paper claims previous methods "failed to reach the sound source" but provides zero quantitative comparison — no SR, SPL, search time, or error bars for baselines. No multiple trials, no different sound sources, no different environments. The paper positions this as demonstrating "generalization" (line 19) but a single successful trajectory is insufficient evidence for that claim.

### Minor

5. **Notation inconsistencies in the method equations.** Several issues are verifiable from the text:
   - Line 68 introduces φ_f^v̅ (bar over v), but Eq. (3) on line 71-72 uses plain φ_f^v — the bar notation is never explained.
   - Lines 65-66 use φ_f^a for both audio and visual processing in Eq. (2), when the second should presumably be φ_f^v.
   - Line 83 (Eq. 5) uses φ_ef^av, line 89 (Eq. 6) uses φ_f^av, and line 80 uses φ̅_f^av — three different names for what appears to be the same operator.
   - Line 68 introduces x̂_i^av ∈ ℝ^{1×D} without clearly connecting it to the preceding equations, which produce {x̂_i^a} and {x̂_i^v}.
   These issues make the architecture description harder to follow than necessary.

6. **Missing RL training details.** The paper mentions "reinforcement learning (RL) strategies" (line 15) and Figure 2 labels a "Critic" and "Decision Making" module, but the method section never specifies the RL algorithm (PPO? A2C?), reward function, or training procedure. This is a significant reproducibility gap for an RL-based navigation system.

7. **No statistical significance or variance reporting.** No standard deviations, confidence intervals, or error bars are reported for any result. Given that the method uses RL (which is inherently stochastic), the absence of variance reporting makes it difficult to assess whether the claimed improvements are robust or could arise from random seed variation.

8. **Motivational gap.** The related work (line 47) cites prior findings that "mid-level fusion outperforms early fusion in tasks without a strong requirement for fine-grained multi-modal integration," but never explains why embodied navigation *does* have such a requirement. The motivation for early fusion over mid-level fusion in this specific setting is asserted rather than argued.

### Trivial
None.

---

## Nice-to-Haves

- **Comparison to a visual-only baseline** would help quantify the value added by audio in the early fusion context. Currently, only audio-visual methods are compared.
- **Absolute model performance (not just gains over baselines)** should be reported in text rather than solely in image-based tables, to aid readability and verification.
- **A visual-only or late-fusion variant of the same architecture** would strengthen the Mamba ablation by providing a reference point without any of the three components.

---

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Experimental results are unverifiable because tables are images"** — The key numbers (gains over baselines, ablation results) are reported in the body text. The tables-as-images issue affects the full per-method breakdown but does not make the central claims unverifiable.
- **"93.6% vs. 88.8% search time inconsistency"** — The abstract says 93.6% reduction "across various benchmarks," while the body reports 88.8% "on the Replica dataset" (line 155). These could refer to different benchmarks; no clear contradiction is present.
- **"Mamba ablation does not isolate Mamba's contribution"** — Comparing full model vs. w/o Mamba (while keeping LFT and MIB constant) is a standard ablation design that does isolate Mamba's marginal contribution. This criticism is incorrect.
- **"Depth Anything integration is unclear"** — The paper states "we adopted Depth Anything models to extract depth maps" (line 111). This is sufficiently clear for a real-world demonstration.
- **No access to appendix/supplementary** — The parser strips these; they exist in the original submission. Not a criticism of the paper.
- **Formatting, typo, or garbled-text criticisms** — Parser artifacts, not author errors.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews converge on the same set of issues (unsubstantiated Mamba efficiency, anecdotal real-world evaluation, missing SNA definition) and the same strengths (interesting early fusion mechanism, solid ablations). No cross-cutting observation emerged that the paper itself does not already surface.

---

## Suggestions

1. **Fix the abstract-body number mismatch.** Clarify which baseline/dataset the abstract's SPL gains of 10.4 and 6.5 refer to, or correct them to match the body text.
2. **Provide runtime measurements for the Mamba variant.** Without wall-clock time per step, total episode time, or throughput, the efficiency claim is unsupported. Even a single table comparing FAVEN with and without Mamba on inference speed would address this.
3. **Define SNA with a formula.** A one-line equation would resolve the ambiguity about how actions are weighted and whether the metric has any pathological behavior.
4. **Expand the real-world evaluation.** Report multiple trials, multiple sound sources/environments, and at least one baseline comparison with SR/SPL/search time, even if the setup is modest.
5. **Add the RL training details.** Specify the algorithm, reward function, learning rate schedule, and any training tricks in the method section or a dedicated implementation details paragraph.

---

## Score and Decision

**Originality:** The early fusion token mechanism is a genuine architectural contribution, though the individual components (cross-attention, fusion tokens, Mamba) are all known techniques — the novelty lies in their combination for this task.

**Importance of research question:** Audio-visual embodied navigation is a relevant problem. Faster navigation has practical value.

**Claims supported:** Partially. The performance gains over baselines are plausible, but the Mamba efficiency claim is unverified, the abstract numbers are inconsistent with the body, and the real-world generalization claim rests on a single anecdote.

**Soundness of experiments:** Adequate for the core ablation but weakened by missing SNA definition, no variance reporting, and no runtime experiments for the Mamba contribution.

**Clarity of writing:** Acceptable overall, but notation inconsistencies in the method section reduce clarity.

**Value to community:** Moderate. The early fusion architecture and ablation findings (optimal token count, fusion depth) are useful design insights, but the unverified claims and reporting issues reduce confidence.

**Overall:** The paper has a meaningful core idea and solid ablation evidence, but the presentation is compromised by an abstract-body number inconsistency that erodes trust, an unverified Mamba efficiency contribution, an undefined metric, and an anecdotal real-world evaluation. These issues are fixable but substantial.

**Score: 4.5**

**Decision: Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>