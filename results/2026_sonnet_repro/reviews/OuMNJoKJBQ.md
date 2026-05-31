Now let me do the calibration search to properly score this paper.Round 1 bracket: **5.0–7.0**. The paper is stronger than the 5.80 "Breach" paper in empirical scope but weaker than the 8.00 "Backtracking" paper in clarity, consistency, and mechanism. Let me narrow.Now I have sufficient calibration data. Let me write the final review.

**Round 1 bracket: 5.0 – 7.0**

The paper is clearly above the jailbreak attack papers (~2-4 range), clearly below the Backtracking paper (8.00), and sits near the Safety Neurons (6.20 accept), SafeDPO (6.40 reject), and SSAH (5.00 reject) anchors. The most topically comparable round-2 anchor is "Safety Neurons" (6.20, accepted), which has cleaner results with a comparable scope. The paper under review is slightly weaker due to inconsistent AW-DPO gains and the causal overstatement, pushing it below 6.20.

**Final score: 5.5, Reject**

---

## Summary

The paper argues that current LLM safety alignment is superficial — refusals are pattern-matched heuristics rather than outputs of genuine reasoning — and uses a probing-based causal intervention (deactivating reasoning-critical attention heads) as evidence. To improve alignment, the paper introduces (1) a new Chain-of-Thought (CoT) safety fine-tuning dataset mixing safety-critical and general prompts with reasoning traces, and (2) Alignment-Weighted DPO (AW-DPO), which assigns distinct DPO loss weights to the reasoning-trace and final-response components of each output, based on their relative harmfulness. Experiments span four model families (Llama-2-7B, Llama-3.2-3B, Llama-3.1-8B, Mistral-7B-v0.3) across 20 jailbreak attack types from SorryBench.

---

## Strengths

- **Broad empirical evaluation scope:** The method is evaluated on 20 jailbreak attack types across four categories and four model families, making it one of the more comprehensive evaluations in the safety alignment literature. The full pipeline (CoT SFT + AW-DPO) consistently achieves the lowest or near-lowest average ASR across all four models compared to prior SFT and DPO baselines (Table 1).

- **Cross-model transferability of the preference dataset (Table 3):** The AW-DPO preference dataset constructed using Llama-2-7B transfers effectively to three other architectures (Llama-3.2-3B, Llama-3.1-8B, Mistral-7B), offering meaningful time savings without large performance losses. This is a practically useful finding with independent value beyond the method itself.

- **Robustness to prefix attacks (Section 5.7):** AW-DPO maintains safety even when an adversarial prefix forces the model to skip its reasoning block entirely (`<think></think>`), demonstrating that the alignment improvement is not simply a structural artifact of the think token.

- **CoT dataset release:** The paper releases a long-form CoT safety dataset that mixes safety-critical and general utility prompts, addressing a gap in prior work (noted as a limitation of SAFECHAIN and others). This is a concrete community contribution.

- **Error-pattern-motivated method design:** The two salient failure modes identified in Section 4 — correct reasoning with unsafe answer, and incorrect reasoning with safe answer — provide a specific and quantified basis (≈15% of failures) for the design of AW-DPO's component-level weighting, even if the follow-through validation is incomplete.

---

## Weaknesses

### Fatal
None.

### Major

- **Causal interpretation is overstated** — The paper's central empirical claim — that "current alignment is superficial since refusals do not rely on reasoning ability" — rests on the finding that deactivating attention heads selected as reasoning-critical (by probing accuracy in layers 1–11) leaves alignment probing accuracy near 100%. This result is equally consistent with two interpretations: (a) alignment is shallow and independent of reasoning (the paper's interpretation), or (b) alignment and reasoning use largely separate circuits, so deactivating reasoning-selected heads simply does not touch the safety circuitry. The paper presents only interpretation (a) without ruling out (b). The causal inference claim would require showing that the identified heads are actually used during safety decisions — which probing accuracy alone cannot establish (Alain & Bengio, 2016, which the paper itself cites, documents this limitation). The phrase "principled reasoning approach" in the title and the framing throughout the introduction rest on this overclaimed result. Appendix D reportedly corroborates via benchmarks (stripped from review), but the main-body argument still falls short of establishing the causal directionality.

- **AW-DPO's gain over standard DPO is inconsistent across models** — Table 1 shows the following DPO → AW-DPO improvements in average ASR: Llama-2-7B: 9.11% → 3.41% (meaningful); Mistral-7B: 3.78% → 0.91% (meaningful, though the DPO baseline is highly unstable: ±14.08); Llama-3.2-3B: 1.04% → 0.58% (within uncertainty bands); Llama-3.1-8B: 1.00% → 0.81% (negligible, within uncertainty). For two of four models, the improvement over standard DPO is not statistically distinguishable. The claim that AW-DPO is "consistently" better than standard DPO is not supported. The paper does not discuss this inconsistency, examine whether ceiling effects explain it, or provide a direct comparison across categories for these models analogous to Figure 4.

- **The 15% failure analysis motivates but does not validate the mechanism** — Section 4 argues that AW-DPO works because it specifically addresses the ≈15% of failure cases involving reasoning-response mismatches that standard DPO misses. Table 1 reports only aggregate ASR, and no experiment identifies whether AW-DPO specifically reduces mismatch failures while DPO does not. The mechanism connecting the 15% observation to AW-DPO's aggregate performance improvement is asserted, not demonstrated.

### Minor

- **STAIR-DPO-3 comparison understated** — Table 2 shows STAIR-DPO-3 achieves 73.34% MMLU utility vs. 58.27% for "Ours (Base)" and 65.29% for "Ours (Instmct)." Neither proposed variant simultaneously dominates STAIR-DPO-3 on both safety and utility: "Ours (Base)" has lower safety (0.81% vs. 1.13% ASR) but substantially lower utility; "Ours (Instmct)" has worse safety (2.92%) and lower utility. The paper's defense — STAIR-DPO-3 uses three training rounds — is a valid framing difference, but the absolute ~8–15 MMLU gap is real and not minor.

- **Utility evaluation limited to MMLU** — MMLU is a multiple-choice knowledge benchmark that does not capture over-refusal of benign requests. A model that refuses all benign open-ended requests would still score approximately the same on MMLU since it is a multiple-choice format. The operationally important question — does the safety-aligned model unnecessarily refuse legitimate requests — is left unanswered. This limits the informativeness of the utility comparisons in Tables 1 and 2.

### Trivial

- **Notation collision** — The symbol γ is used for two distinct purposes: the KL-penalty scaling coefficient in Eq. 2 and the full-harmfulness-score threshold for preference-pair selection in Step 2 of Figure 2.

---

## Nice-to-Haves

- Supplement the probing-based causal experiment with a behavioral demonstration: take a fixed set of prompts, apply structural jailbreak variations (prefix injection, encoding attacks), and show CoT-finetuned refusals survive more often than SFT refusals, with failure correlated with reasoning quality degradation. This would ground the "alignment relies on reasoning" thesis behaviorally rather than representationally.
- Directly validate the 15% mechanism: categorize test failures post-AW-DPO training by whether they are reasoning-response mismatches, and show AW-DPO specifically reduces that category relative to standard DPO.
- Report over-refusal rates on benign prompts (AlpacaEval or MT-Bench) to complete the safety/utility picture.
- Characterize the judge LLM's calibration accuracy on the binary safety task, since its errors propagate directly into AW-DPO preference pair quality.
- Discuss why catastrophic utility collapse occurs at lr=5e-6 (MMLU drops from ~48% to 26%, Table 5) and provide practical guidance for learning rate selection.
- A brief sensitivity analysis on the 10% head threshold and 11-layer boundary used in the preliminary causal experiment would strengthen confidence in those choices.
- State explicitly whether Phi-4-Reasoning models received safety post-training (the referenced technical report suggests they did, making Section 5.3's comparison valid — this deserves a sentence of clarification).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic concern that alignment probing might pick up surface "sorry" tokens:** The paper uses hidden states at the last token from frozen representations, not surface token logits. This specific mechanistic concern is not clearly grounded in the paper's experimental setup. **REMOVED** as speculative/unsupported by paper text.

- **Harsh critic concern about the Phi-4-Reasoning comparison being unfair:** The paper cites Abdin et al. (2025), the Phi-4-Reasoning Technical Report, which describes models with safety-aware training. The comparison thus pits safety-trained reasoning models against AW-DPO safety-trained models — a fair test of the paper's claim that "reasoning alone is insufficient for alignment." **REMOVED** as factually incorrect criticism (the paper cites a real reference, and the referenced models have safety training).

- **Harsh critic's formulaic edge-case concern about weights when d_reasoning and d_response are near zero or have opposite signs:** While mathematically real, in practice pairs are selected only when the full harmfulness score difference exceeds threshold γ, which implies at least one of the two components has a meaningful gap. The concern is theoretical rather than grounded in a demonstrated failure mode. **DEMOTED** to Nice-to-Have.

- **Harsh critic's concern about "no reason to believe reasoning-critical heads overlap with safety circuits":** This is precisely the paper's empirical finding — they don't overlap — and the paper uses this to argue alignment is shallow. The critic's framing is circular. **REMOVED** as a strawman.

- **Strength Finder claim that the causal intervention "cleanly isolates" superficial alignment:** The Strength Finder overstates. The experiment is consistent with two interpretations (see Major weakness 1). **REMOVED** from strengths.

- **Strength Finder's generic strength about addressing an important problem:** Generic and non-specific. **REMOVED**.

- **Missing related work criticisms:** Per filtering rules, not included — no external sources to verify existence of additional references.

---

## Novel Insights

The paper's most actionable insight beyond its own stated contributions is the cross-model transferability of the AW-DPO preference dataset (Table 3): a preference dataset constructed using one model generalizes effectively to other architectures without per-model reconstruction. This suggests that safety preference signals may have sufficient universality across model families to enable economical one-time dataset construction. Additionally, the comparison with Phi-4-Reasoning models (Section 5.3) provides direct empirical evidence that general-purpose reasoning fine-tuning does not translate to alignment-specific reasoning robustness, sharpening the argument that safety alignment requires explicit reasoning-aware training rather than a side effect of improved general reasoning.

---

## Suggestions

1. Replace the probing-based causal claim with a behavioral intervention: show that CoT-finetuned models' refusals survive paraphrase/encoding attacks more often than SFT models' refusals, to make "reasoning grounds alignment" a behavioral rather than representational claim.
2. Add a targeted mismatch-failure experiment: for a fixed test set, compare DPO and AW-DPO on the subset of failures that exhibit reasoning-response decoupling, to validate the 15% mechanism directly.
3. Add an over-refusal evaluation on benign prompts (AlpacaEval or similar) alongside MMLU.
4. Resolve the γ notation collision in the method section.

---

## Score Calibration

**All retrieved anchors:**

| Path | Score | Round | Comparison |
|---|---|---|---|
| 5kMwiMnUip.md | 1.40 | R1 | Jailbreak attack paper, no defense — not comparable |
| BeOEmnmyFu.md | 2.50 | R1 | Jailbreak attack via language games — not comparable |
| lUyYX9VFgA.md | 3.00 | R1 | Prompting-based attack — not comparable |
| 1zt8GWZ9sc.md | 3.67 | R1 | Role-playing jailbreak automation — not comparable |
| wetJo6xXb1.md | 4.50 | R1 | Defensive Prompt Patch (defense method) — less comprehensive than paper under review |
| rgiIZ3pcZY.md | 4.75 | R1 | OOD jailbreak evaluation — not comparable |
| 8Rov0fjpOL.md | 5.80 | R1 | Information leakage threat model, mixed empirical quality — paper under review is broader |
| Bo62NeU6VF.md | 8.00 | R1 | Backtracking: cleaner idea, consistent results — paper under review clearly weaker |
| tTPHgb0EtV.md | 8.00 | R1 | Booster harmful fine-tuning — paper under review weaker |
| 9H91juqfgb.md | 5.00 | R2 | SSAH: causal analysis + safety components, no deployed method — paper under review stronger |
| sYJQEgkkaI.md | 5.25 | R2 | Rethinking RepE: causal analysis of safety representations — comparable in analysis, but paper under review adds a full method |
| CeJEfNKstt.md | 5.25 | R2 | Geometry of Truth: probing for truth — less topically relevant |
| 2Cg4YrsCMA.md | 5.25 | R2 | Rationale-enriched DPO: similar spirit, paper under review has broader safety evaluation |
| qBKA2844I4.md | 5.50 | R2 | HyperDPO: DPO extension for multi-objective — paper under review is comparably positioned |
| aJUuere4fM.md | 5.75 | R2 | Past Tense Jailbreak: simple finding, high impact, accepted — not directly comparable |
| hXA8wqRdyV.md | 6.14 | R2 | Adaptive jailbreaking attacks paper — not comparable (attack, not defense) |
| yR47RmND1m.md | 6.20 | R2 | Safety Neurons: neuron-based safety tuning, accepted — comparable scope and depth |
| pljYMCYDWJ.md | 6.20 | R2 | Logicbreaks: theoretical + empirical jailbreak analysis — less comparable |
| MoJSnVZ59d.md | 6.40 | R2 | SafeDPO: DPO variant for safety, rejected for incremental contribution — paper under review is broader |
| 9Hxdixed7p.md | 6.25 | R2 | 3D-Properties of DPO: analysis + fix, accepted — paper under review somewhat similar in spirit |
| r42tSSCHPh.md | 7.00 | R2 | Catastrophic Jailbreak via generation: clean empirical finding — paper under review is weaker on consistency |

**Round 1 bracket: 5.0–7.0**

**Round 2 narrowing:** The paper sits near the 5.25–6.20 cluster. It is stronger than SSAH (5.00) and Rethinking RepE (5.25) because it combines a causal analysis with an actual method and broader evaluation. It is comparable to Safety Neurons (6.20, accepted) and SafeDPO (6.40, rejected), but slightly below Safety Neurons because Safety Neurons has cleaner and more consistently large improvements, and slightly comparable to SafeDPO which was rejected for incremental contribution. The paper under review is more novel than SafeDPO (segment-weighted DPO with reasoning decomposition + CoT dataset release), but its method's core component (AW-DPO) shows inconsistent gains over DPO and the causal framing is overstated.

**Final score: 5.5, Reject.** The paper sits just at the rejection side of the acceptance boundary: genuine contributions (dataset, method, broad evaluation) are undercut by (a) the causal overstatement that is central to the paper's narrative, (b) AW-DPO's inconsistent gains over DPO on two of four models, and (c) the limited utility evaluation. The paper would strengthen considerably by validating the 15% mechanism and grounding the causal claim behaviorally.

---

**Evaluation axes:**
- **Originality:** Moderate. AW-DPO is a novel DPO variant; decomposing preference optimization by reasoning vs. response is new. The causal motivation, though imperfect, distinguishes the work from prior CoT safety papers.
- **Importance of research question:** High. Safety alignment robustness to jailbreak attacks is a critical open problem.
- **Claims vs. support:** Weak for the causal claim; adequate for the aggregate pipeline results; insufficient for AW-DPO's specific mechanism.
- **Soundness of experiments:** Moderate. Broad attack/model coverage, but incomplete for the core mechanism claim. Utility evaluation is narrow.
- **Clarity of writing:** Adequate. The pipeline is clearly presented; the theoretical framing overshoots what the experiments establish.
- **Value to the research community:** Moderate. The dataset release and transferability result have independent practical value; the method has promise.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>