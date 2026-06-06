Now I have everything I need. Let me verify the key arithmetic claim about the SD-LoRA average.

Looking at Table 1, SD-LoRA's available T1–T22 values: 68+22+52+63+32+48+71+74+63+62+42+75+56+72+50+49+69+64+52+55+59+56 = **1254**, giving a 22-task average of **57.0%**. The paper claims a 52% average for SD-LoRA, but for 24 tasks to average 52%, T23 and T24 would need to sum to (52×24 − 57×22×1) = (1248 − 1254) = **−6**, i.e., negative values — arithmetically impossible. This means the "52%" figure in the paper text is incorrect given the published per-task numbers.

---

## Summary

This paper formalizes All-Day Multi-Scenes Lifelong VLN (AML-VLN), proposes Tucker Adaptation (TuKA) — a 4th-order tensor adapter that decouples shared core navigation knowledge, scene experts, and environment experts — and a Decoupled Knowledge Incremental Learning (DKIL) strategy applying EWC, consistency, and orthogonality losses to each subspace. AllDayWalker is evaluated on a 24-task benchmark (AllDay-Habitat), reporting 65% average SR. The rebuttal honestly acknowledges all major weaknesses but provides no new experimental evidence; it only promises revisions.

---

## Rebuttal Assessment

**Weakness:** Incomplete Table 1 averages; unverifiable SD-LoRA "52%" average
**Author's response:** Acknowledge
**Assessment:** Unconvincing — The author promises revision but provides no data. Critically, the arithmetic is self-refuting: the 22 available SD-LoRA values already average **57.0%**, yet the paper claims a 52% full-task average. T23+T24 would need to be negative to produce 52%, which is impossible. The rebuttal says "52–57% depending on what T23/T24 contribute" without catching this error, suggesting the authors did not verify their own claim. The gap between AllDayWalker (65%) and SD-LoRA is real but smaller than stated — approximately 5–8%, not 13%.
**Score impact:** Weakness upgraded (arithmetic impossibility makes the stated headline comparison actively misleading)

---

**Weakness:** Missing independent scene-LoRA + environment-LoRA baseline
**Author's response:** Acknowledge
**Assessment:** Unconvincing — The author provides a theoretical argument (shared core tensor 𝒢 captures cross-mode interactions that two independent matrices cannot), but this is exactly the claim requiring empirical validation. No new ablation is offered. The rebuttal admits the gap straightforwardly.
**Score impact:** Weakness unchanged

---

**Weakness:** Inference-time expert retrieval uncharacterized
**Author's response:** Partially address
**Assessment:** Partially convincing — The mechanism in §3.4 is confirmed (CLIP-based two-step nearest-neighbor matching), and Figure 7's five comparison strategies are confirmed as retrieval ablations pointed to Appendix K. However: (a) the main text never names or explains these five strategies, leaving Figure 7 effectively uninterpretable standalone; (b) no per-environment retrieval accuracy is reported anywhere. The "task-id agnostic at inference" property — a major claimed advantage — remains quantitatively unvalidated.
**Score impact:** Weakness partially downgraded (mechanism is described; ablation exists in appendix) — but not removed

---

**Weakness:** Formal definition vs. DKIL inconsistency (§2 non-overlap condition)
**Author's response:** Partially address
**Assessment:** Partially convincing — The author correctly explains the intended semantics: the (S, E) *pair* must be novel, not individual S or E values. §3.3 (consistency losses with α/β = 1 when same scene/environment recurs) is indeed consistent with this interpretation. The formal definition as written ({S_t, E_t} ∩ ∪{S_j, E_j} = ∅) is genuinely ambiguous. The paper does not correct this in the current submission.
**Score impact:** Weakness downgraded (intent is clear from §3.3; revision needed but not a fundamental flaw)

---

**Weakness:** Mechanical zero at T24 in forgetting metrics
**Author's response:** Acknowledge
**Assessment:** Partially convincing — The author correctly explains why T24 F-SR is structurally 0 by definition. The paper data largely confirms this (Seq-FT, Lwf-LoRA, EWC-LoRA, Dense MoLE, Sparse MoLE, MoLA, HydraLoRA, BranchLoRA, SD-LoRA, AllDayWalker all show T24=0). Interestingly, the O-LoRA row appears to show T24=20 (non-zero), suggesting either a data formatting error in that row or a subtle difference in how O-LoRA's metric is computed — this is unexplained. The paper does not acknowledge the T24 artifact.
**Score impact:** Weakness unchanged

---

**Weakness:** Figure 7 methods unexplained in main text
**Author's response:** Partially address
**Assessment:** Partially convincing — Author confirms these are retrieval-strategy ablations (Ours, BaseModel, Recall, Task2Vec, CLIP) detailed in Appendix K. The §5.2 text does include "For detailed quantitative results, please refer to our Appendix §K," but neither §5.2 nor §5.3 names or describes these strategies, making Figure 7 essentially uninterpretable in the main paper. Promise to fix in revision.
**Score impact:** Weakness unchanged in current submission

---

**Weakness:** Duplicate rows in Table 3
**Author's response:** Acknowledge
**Assessment:** Confirmed — Table 3 contains two rows both showing ✓✓✓ for (Sd-𝒢, Sd-U¹, Sd-U²) with identical SR/F-SR/SPL/F-SPL but OSR differing by 1 (69 vs. 68). Author confirms copy-paste error.
**Score impact:** Trivial; acknowledged

---

**Weakness:** Notation inconsistency in §3.4 (M vs. N)
**Author's response:** Acknowledge
**Assessment:** Confirmed — §3.4 writes environment candidate set as {Fe_{e1}, …, Fe_{eM}} using M (scene count) instead of N (environment count). Typographic error confirmed.
**Score impact:** Trivial; acknowledged

---

## Strengths

1. **Principled multi-hierarchical decomposition**: TuKA's 4th-order tensor (Eq. 2–3) explicitly separates core skills (𝒢), shared encoder/decoder (U¹, U²), scene experts (U³), and environment experts (U⁴). This is well-motivated and goes beyond the 2-dimensional matrix form of LoRA/HydraLoRA.

2. **Demonstrated catastrophic forgetting motivation**: Figure 2 shows sequential fine-tuning yields up to 79% forgetting across 10 tasks; Table 2 shows DKIL achieves 11% average F-SR vs. 18% for SD-LoRA and 23% for O-LoRA.

3. **Comprehensive experimental setup**: 24 sequential tasks across 5 simulation × 4 environment + 2 real-world × 2 environment; 11 baselines evaluated across SR, SPL, OSR, F-SR, F-SPL, F-OSR.

4. **Generalization beyond training tasks**: Table 5 confirms AllDayWalker achieves 55% average SR on 6 unseen scenarios vs. 39% for SD-LoRA — a substantial margin on out-of-distribution tasks.

5. **Fourth-order vs. third-order tensor ablation (Figure 8)**: 4th-order TuKA consistently outperforms 3rd-order across all 20 simulation tasks, validating the benefit of decoupled scene/environment representation.

---

## Weaknesses

### Fatal
- None.

### Major

1. **Arithmetically impossible SD-LoRA average claim**: The "52%" headline figure for SD-LoRA in the paper text is mathematically impossible given the per-task values in Table 1 (22-task average = 57.0%; T23+T24 would need to be negative to produce 52%). The true AllDayWalker advantage over SD-LoRA is real but approximately 5–8%, not the claimed 13%. The rebuttal failed to identify this error. Tables for Seq-FT, Lwf-LoRA, EWC-LoRA, O-LoRA, and FeedTTA also lack Avg. columns.

2. **Missing direct architectural validation**: No ablation tests two independent LoRA adapters (one scene-specific, one environment-specific) with the same EWC + orthogonality + consistency losses. Without this, the gains could plausibly come from the DKIL regularizers rather than the Tucker structure. Table 3 ablates *which shared components within TuKA* matter; Figure 8 compares 3rd-order vs. 4th-order — neither tests the structural claim. The rebuttal acknowledges this gap without providing evidence.

3. **Inference-time retrieval accuracy unreported**: The "task-id agnostic at inference" property is a central claim. Section 3.4 describes the CLIP-based nearest-neighbor mechanism but no retrieval accuracy statistics appear anywhere in main text or accessible appendix. Figure 7's five strategies are not explained in the main text, making the retrieval comparison nearly uninterpretable.

### Minor

1. **Formal definition ambiguity**: §2 writes {S_t, E_t} ∩ (∪{S_j, E_j}) = ∅ as written prohibiting individual scene or environment recurrence, contradicting §3.3's explicit reuse mechanism (α=1, β=1 when same scene/environment recurs). Intended meaning is clear from context but definition should be corrected.

2. **Misleading T24 column in Table 2**: F-SR at T24 is 0 by metric construction for almost all methods (M-SR₂₄ = SR₂₄ by definition). The paper does not flag this, creating an impression of zero forgetting on the final task. O-LoRA's T24 entry also appears anomalous (non-zero, possibly a formatting error).

3. **Figure 7 strategies unexplained**: Five retrieval comparison models (Ours, BaseModel, Recall, Task2Vec, CLIP) are named in Figure 7 but never introduced in §5.2 or §5.3, making the figure nearly uninterpretable from the main paper alone.

4. **Duplicate Table 3 rows**: Two rows with identical ✓✓✓ configuration, differing only in OSR (69 vs. 68) — confirmed copy-paste error.

### Trivial

1. **§3.4 notation**: Environment candidate set written as {Fe_{e1}, …, Fe_{eM}} using M (scene count) instead of N (environment count).

---

## Nice-to-Haves

- Full corrected Table 1 with all averages populated and SD-LoRA T23/T24 data; reconcile the "52%" text claim with actual computable average.
- Independent scene-LoRA + environment-LoRA ablation to isolate Tucker structure contribution from DKIL regularization.
- Per-environment retrieval accuracy statistics (e.g., % of inference steps where correct expert is selected) added to either §5.3 or an appendix clearly referenced from main text.
- Figure 7 explained inline in §5.3 (one paragraph naming and defining each retrieval strategy).

---

## Novel Insights

TuKA's key insight — that Tucker decomposition lifts LoRA-family adapters from 2D matrices into a 4th-order tensor, enabling an explicit inductive bias where scene and environment knowledge occupy orthogonal subspaces while sharing a common core — is genuinely novel in the continual VLN literature. The pairing with targeted DKIL (EWC on shared subspaces, consistency and orthogonality on specific expert rows) is architecturally principled and well-motivated. The 3rd-order vs. 4th-order ablation (Figure 8) provides direct empirical support for the value of decoupled rather than coupled expert representations, and the result generalizes naturally to any multi-hierarchical PEFT setting. The AllDay-Habitat benchmark, grounded in physics-based imaging models (Eq. 10–12), is a reproducible and extensible contribution.

---

## Suggestions

1. Recompute SD-LoRA's average from the paper's own Table 1 values; the published "52%" is arithmetically impossible given the 22 available per-task entries averaging 57.0%. Report the correct figure and reconcile the gap claim.
2. Add independent scene-LoRA + environment-LoRA + DKIL baseline to Table 3 to directly validate Tucker structure's contribution.
3. Report per-environment retrieval accuracy (§5.3) to substantiate the task-id-agnostic inference claim.
4. Correct the formal non-overlap condition in §2 to specify that the (S, E) *pair* must be new.
5. Add a short paragraph in §5.3 naming and explaining the five retrieval strategies in Figure 7.
6. Add a footnote to Table 2 noting T24 F-SR is 0 by metric construction (not a model achievement).

---

## Score and Decision

**Original score**: 5.5 (Reject)

**Rebuttal impact**: The rebuttal is honest and thorough in acknowledging weaknesses but provides zero new experimental evidence. More concerningly, the rebuttal fails to catch that the headline comparison ("65% vs. 52%") is arithmetically impossible — the SD-LoRA 22-task average already equals 57.0%, and no non-negative T23/T24 values can bring the 24-task average to 52%. This means the paper's most prominent quantitative claim is incorrect in the current submission. The actual advantage over SD-LoRA is real but smaller (~5–8%), and both major ablation gaps (independent adapter baseline, retrieval accuracy) remain entirely unresolved. Promises of revision do not count as addressing weaknesses.

The paper retains genuine contributions (Tucker formulation, DKIL strategy, AllDay-Habitat benchmark, real-world results), but the evidentiary incompleteness — now compounded by an unacknowledged arithmetic error in the central comparison — warrants rejection pending substantial revision.

**Final score**: 5.5 — weak reject.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>