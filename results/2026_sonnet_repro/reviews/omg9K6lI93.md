Now let me perform calibration searches to score the paper appropriately.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary
This paper investigates whether translating English benchmark datasets into Arabic can obscure data contamination while preserving the performance benefits of memorization. The authors fine-tune four open-weight LLMs on varying proportions of Arabic-translated benchmark data (MMLU, XQuAD, MLQA), evaluate on the original English benchmarks, and extend the TS-Guessing contamination detection method with a choice-reordering strategy to measure memorized index recall. They additionally propose a Translation-Aware Contamination Detection (TACD) framework as a forward-looking blueprint.

---

## Strengths

- **Novel TS-Guessing extension with choice-reordering (Section 3.3, Figure 1, Table 3a):** The MCQ protocol—shuffling answer options before masking one—is a genuine methodological contribution that disentangles positional letter recall from content reasoning. The resulting Index-Recall Rate (IDR) values substantially above the 0.25 chance baseline for LLaMA (0.287–0.643) and Gemma (0.350 at 10%) provide a real contamination signal that persists even when surface forms are translated.

- **Multi-model empirical scope under controlled conditions (Section 3.1):** Fine-tuning four open-weight models (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) across four contamination levels under identical LoRA/PEFT hyperparameters and the same evaluation harness gives the results a degree of cross-model generalizability that is appropriate for an empirical study of this type.

---

## Weaknesses

### Fatal

**None that fully invalidate all results.** However, the following Major flaw structurally limits the interpretability of the primary claim.

### Major

- **The p=0 baseline is not a clean control — it is already contaminated (Section 3.1).** The training set is defined as $\mathcal{D}_{\text{train}}^d(p) = \mathcal{D}_{\text{EN}}^d \cup \mathcal{D}_{\text{AR}}^d(p)$, with $\mathcal{D}_{\text{EN}}^d$ being the English test items present in every condition, including p=0. This means every trained model — including the purported "baseline" — has been fine-tuned on the English benchmark test data. The paper's stated question is whether Arabic translation *conceals* contamination, but the experiment cannot isolate this: all it can measure is the marginal effect of adding Arabic translations on top of a universally contaminated English fine-tune. Without a truly uncontaminated baseline (no benchmark data in training) and an Arabic-only condition, the central claim — that translation masks contamination while preserving its performance benefits — cannot be cleanly attributed to translation-mediated concealment rather than the uniform English contamination baseline. This is a structural flaw in the experimental design.

- **Sections 4.1 and 4.2 make directly contradictory claims about the same data.** Section 4.1 characterizes MMLU as showing "a generally monotonic increase as contamination rises" and attributes this to "contamination-driven memorization" (Mistral: 0.577→0.690; LLaMA: 0.332→0.431). Section 4.2 then states "the models exhibit approximately equal performance on all evaluated benchmarks" and uses the "near-flat trend" as evidence that translation is "effectively masking contamination effects." These two readings are incompatible with the same set of numbers. Table 3a further undermines the "near-flat" characterization: LLaMA's IDR jumps from 0.287 at 10% to 0.643 at 50% — more than a two-fold increase. The paper does not reconcile this internal contradiction.

- **The claim that "models with stronger Arabic capabilities benefit more" (abstract and Section 4.1) is unsupported.** No measurement of Arabic capability is reported anywhere. There is no ranking of models by Arabic proficiency, no Arabic evaluation benchmark results, and no analysis that directly tests this interaction. This is a hypothesis presented as a finding in the abstract and body text.

### Minor

- **XQuAD/MLQA performance gains are conflated with contamination rather than cross-lingual transfer (Section 4.1).** XQuAD and MLQA are parallel cross-lingual benchmarks whose Arabic and English splits share underlying passages. Training on Arabic XQuAD and seeing performance changes on English XQuAD is consistent with cross-lingual transfer — a well-documented phenomenon independent of contamination. The paper notes non-monotonic MLQA trends and the Mistral collapse but does not attempt to separate transfer from contamination effects for these two datasets. The MMLU results (same-language, closed-book MCQ) are more defensible as contamination probes; the QA results carry interpretive ambiguity.

- **Near-zero XQuAD TS-Guessing EM (Table 3b) is interpreted as masking but may reflect method failure.** LLaMA EM values of 0.001, 0.005, 0.008 across contamination levels are interpreted as evidence that translation conceals contamination. An equally plausible explanation is that the masked-token TS-Guessing method is unsuitable for extractive QA — predicting a masked question word from a context is a fundamentally different task than fill-in-the-blank. The paper does not establish a positive control showing that this method fires in settings where contamination is known to be present.

### Trivial

- The literature review (Section 2) is lengthy and reads as background survey rather than focused motivation; the connection to the paper's multilingual angle is not made explicit until the end of Section 2.4.

---

## Nice-to-Haves

- An Arabic-only fine-tuning condition (no English benchmark data) would cleanly isolate the translation-mediated contamination effect the paper aims to study.
- A non-benchmark Arabic fine-tuning control (e.g., Arabic Wikipedia) would distinguish contamination from generic cross-lingual transfer for XQuAD/MLQA.
- Reporting performance on Arabic benchmarks (e.g., ALGHAFA, AraBench) would substantiate the "stronger Arabic capability" moderator hypothesis.
- Establishing a positive control for the XQuAD TS-Guessing method (a setting where contamination is known and EM should be non-trivial) would resolve the method-failure ambiguity in Table 3b.
- TACD would be substantially more persuasive as a contribution if even a small pilot validation were provided.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: IDR measures positional bias rather than memorization.** Partially valid as a concern, but IDR values well above the stated 0.25 chance baseline (LLaMA 0.643) make pure positional bias an insufficient explanation. Demoted to minor concern rather than retained as a flaw.

- **Strength Finder: "Rigorous experimental design" as a standalone strength.** Using identical LoRA settings across models is appropriate methodology, not a distinguishing contribution. Removed as generic.

- **Strength Finder: TACD as a forward-looking contribution.** The paper itself describes TACD as "a forward-looking blueprint rather than a complete implementation." A blueprint without validation cannot be a core strength. Removed.

- **Strength Finder: "Empirical demonstration that translation conceals contamination while models still benefit."** This is the paper's central claim, but it is undermined by the contaminated baseline (all conditions include English benchmark data). Cannot be certified as a clean demonstration. Removed from strengths per filtering rules — when a strength and a verified weakness disagree, the weakness wins.

---

## Novel Insights

The choice-reordering extension to TS-Guessing (masking an answer option *after* shuffling) is a methodologically clean way to detect whether a model memorized index–letter associations from a specific question presentation, since it would be unrecoverable by content reasoning alone. The IDR signal it produces is relatively robust to translation because it probes structural memory rather than surface form recall. If the experimental design were fixed, this probe could be an important building block for multilingual contamination audits.

---

## Suggestions

1. **Fix the baseline:** Run a condition with no benchmark data in fine-tuning (neither English nor Arabic) to obtain a clean reference point, and an Arabic-only condition (no English benchmark data) to isolate translation-mediated contamination.
2. **Reconcile Sections 4.1 and 4.2:** The paper cannot simultaneously claim monotonic MMLU gains are "contamination-driven memorization" (4.1) and that performance is "approximately equal" and "near-flat" (4.2). Choose one consistent interpretation of Table 2 and support it.
3. **Establish a TS-Guessing positive control for extractive QA** before interpreting near-zero EM as concealment.
4. **Report Arabic benchmark performance** to test whether "stronger Arabic capabilities" moderates contamination effects.
5. **Pilot TACD with at least one component** (e.g., back-translation consistency on a single benchmark) to give it evidential weight.

---

## Score and Decision

**Originality:** Moderate. The multilingual angle on contamination masking is fresh and underexplored. The TS-Guessing extension is a concrete methodological contribution.

**Importance of research question:** High. Translation-mediated contamination is a real and growing blind spot as multilingual evaluation expands.

**Claim support:** Poor. The central claim (translation masks contamination) cannot be cleanly read from the data due to the contaminated baseline in all conditions. The "stronger Arabic capabilities" moderator claim is entirely unsupported.

**Soundness of experiments:** Weak. The structural flaw in condition formulation is not a gap that can be papered over; the $p=0$ baseline is contaminated. The internal contradiction between Sections 4.1 and 4.2 suggests the authors did not fully reconcile their own results.

**Clarity of writing:** Adequate. The paper is readable but the analysis sections are inconsistent with each other.

**Value to research community:** Limited in current form; higher potential if the experimental design is corrected.

---

**Round 1 Bracket:** Based on retrieval, my initial bracket is 3.0–4.5.

**Round 2 Anchors retrieved:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Nk1MegaPuG.md` — avg 4.25, round 1 & 2 — "Evading Data Contamination Detection." More technically concrete, has a working attack technique. The paper under review is weaker: its design flaw is more serious than the weaknesses in this anchor.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rAylWUIKtu.md` — avg 4.25, rounds 1 & 2 — "Benchmark Inflation." Has actual methodology (retro-holdouts) with statistical validation. Stronger than the paper under review.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lwtaEhDx9x.md` — avg 4.75, round 2 — "Elephants Never Forget." Multiple validated memorization tests on tabular data, clear methodology. Stronger than the paper under review.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/m2NVG4Htxs.md` — avg 6.75, round 1 — "To the Cutoff." Uses a natural experiment; cleaner methodology. Substantially stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/JL42j1BL5h.md` — avg 3.50, round 2 — "All Languages Matter." Rejected multilingual LLM safety benchmark. Closer in scope to the paper under review; rated 3.5 with similar issues of limited contribution and methodological constraints.

**Narrowing:** The paper under review is comparable to the 3.5 anchor ("All Languages Matter") and weaker than all the 4.25+ anchors. The contaminated-baseline flaw is structural and not speculative. The internal contradictions in 4.1 vs 4.2 are verifiable from the text. The unimplemented TACD is the paper's stated "framework contribution." I land on **3.0**, below the 3.5 multilingual-LLM anchor because the experimental design flaw is more fundamental than scope limitations in that paper.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>