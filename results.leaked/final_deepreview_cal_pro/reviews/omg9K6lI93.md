Now I have a solid picture. Let me compose the final review.

## Summary

This paper investigates whether translating benchmark data into Arabic can mask data contamination while still providing models with an unfair advantage. The authors fine-tune four open-weight LLMs on varying proportions of Arabic-translated MMLU, XQuAD, and MLQA test data (mixed with an English split), evaluate on the original English benchmarks, and probe memorization using an extended TS-Guessing method with choice reordering. They find that MMLU accuracy increases with Arabic contamination while extractive QA shows non-monotonic patterns, and propose a Translation-Aware Contamination Detection framework as a forward-looking blueprint.

## Strengths

- **Novel research question on cross-lingual contamination.** Investigating whether translation can act as a veil for data contamination is a genuinely important and underexplored problem. The paper makes a concrete empirical contribution by testing this with Arabic, a lower-resource language.

- **Choice-reordering TS-Guessing probe (Section 3.3).** Extending the TS-Guessing method for MCQ benchmarks by shuffling answer options and measuring the index-recall rate (IDR) is a clean, well-motivated methodological addition. Table 3a provides direct evidence that models rely on memorized answer-position patterns rather than reasoning (e.g., LLaMA IDR = 0.643 at 50% contamination), which is a stronger contamination signal than accuracy alone.

- **Task-dependent contamination dynamics.** The paper reveals a clear divergence: closed-book MMLU improves monotonically with Arabic contamination across all models (Table 2), while extractive QA (XQuAD/MLQA) shows non-monotonic and sometimes harmful effects (e.g., Mistral XQuAD collapses from 0.455 to 0.114). This finding usefully complicates the simple narrative that contamination always helps, showing it can degrade span-localization capabilities under distribution shift.

## Weaknesses

### Major

- **Internal contradiction between results sections.** Section 4.1 acknowledges that "MMLU exhibits a generally monotonic increase as contamination rises from 0% → 100%," but Section 4.2 then claims that across p ∈ {10, 50, 100}% "models exhibit approximately equal performance" and a "near-flat trend." The data in Table 2 contradicts this flatness claim: MMLU shows clear increases for all models (e.g., LLaMA: 0.381 → 0.389 → 0.431; Mistral: 0.580 → 0.690 → 0.690). XQuAD also increases for three of four models. The paper cannot simultaneously assert monotonic gains and near-flat trends; this undermines the central argument that translation "compresses" or "masks" contamination signals in a detectable way. The discussion needs to reconcile these contradictory claims or acknowledge that the masking effect is weaker than the narrative suggests.

- **Ambiguous training data specification (Section 3.1).** The training mixture is defined as D_EN^d ∪ D_AR^d(p), where D_EN^d is described as "English test items formatted as MCQ" for MMLU and D_AR^d(p) as "Arabic translations of the test items." The paper never specifies whether D_EN^d and the evaluation split are disjoint. If D_EN^d overlaps with the evaluation data, the p=0 baseline is already contaminated and the experiment measures only the marginal effect of Arabic translations on top of English test items — a much narrower question than the paper claims. If they are disjoint (e.g., D_EN^d is from the MMLU dev set), this needs to be stated explicitly with split sizes and provenance. As written, the setup is unreproducible and the interpretation of results is ambiguous.

- **Missing p=0 baseline for TS-Guessing probes (Table 3).** TS-Guessing results are reported only for p ∈ {10, 50, 100}%. Without the p=0 (EN-only) reference, we cannot determine whether the observed memorization indices (e.g., LLaMA IDR = 0.287 at 10%) arise from the English training data alone or are genuinely boosted by Arabic translations. This omission makes the contamination probes difficult to interpret as evidence for translation-mediated leakage specifically.

### Minor

- **The TACD framework (Section 5) is an unimplemented sketch.** The proposed Translation-Aware Contamination Detection framework is presented as a conceptual blueprint with no implementation, empirical validation, or connection to the preceding experiments. While forward-looking proposals can add value, here the section reads as decoupled from the paper's empirical contribution and does not strengthen the core claims. The paper would be stronger if this section were cut or significantly condensed in favor of addressing the methodological issues above.

- **No same-language contamination baseline.** The experimental design compares Arabic contamination levels against an EN-only baseline but never includes an English-contamination condition. Without showing what happens when English test items themselves are used as contamination, the paper cannot quantify how much translation specifically "masks" contamination relative to same-language leakage. The absence of this baseline weakens the central comparative claim.

### Trivial

- The embedding/cosine-similarity discussion in Section 4.3 references a figure that does not appear to render in the main text, relying on it for a key argument about semantic preservation across translation.

## Nice-to-Haves

- Including the p=0 condition in TS-Guessing would make the memorization probes self-contained and interpretable without reference to the accuracy trends.
- A same-language (English) contamination arm would allow direct quantification of translation's masking effect relative to baseline leakage.
- Reporting per-subject MMLU breakdowns could reveal whether contamination effects concentrate in specific knowledge domains, strengthening the analysis.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh critic's claim that training on evaluation data is a "structural flaw that undermines the paper's main empirical contribution."** While the ambiguity about D_EN^d is a genuine weakness (retained above as Major), the harsh critic's framing as definitively fatal is speculative — the paper may be using a disjoint split but simply failed to specify it. The weakness is in the *reporting*, not necessarily in the design itself. Kept as a major weakness requiring clarification rather than a fatal flaw.

- **Harsh critic's claim about the embedding figure being absent.** This appears to be a parser artifact (figures are commonly stripped). The original submission likely has this figure. Removed as a criticism.

- **Strength finder's claim #3 ("Empirical demonstration that Arabic translation masks contamination").** This cherry-picks Qwen XQuAD as evidence of flatness while ignoring the broader data showing clear trends. The masking claim is contradicted by the paper's own MMLU results. Removed as a misleading strength.

- **Strength finder's generic framing of "controlled cross-lingual contamination experiment."** Retained in modified form under the novelty strength; the generic phrasing was removed.

- **Harsh critic's note about missing appendix content.** The parser strips appendix sections. Removed.

## Novel Insights

The finding that contamination effects are strongly task-dependent — monotonic gains for closed-book multiple choice (MMLU) versus non-monotonic, sometimes harmful effects for extractive QA (XQuAD/MLQA) — is the most genuinely novel empirical contribution. It suggests that contamination-driven memorization helps option selection while degrading span localization under distribution shift. This has practical implications for contamination auditing: a model that passes an MMLU-based contamination check may still suffer degraded extractive capabilities, and vice versa. The choice-reordering TS-Guessing probe also provides a template for future MCQ contamination studies that goes beyond simple accuracy comparisons.

## Suggestions

- Clarify the exact composition and provenance of D_EN^d. If it is a disjoint split (e.g., MMLU dev set), state this explicitly with sizes. If it overlaps with evaluation data, acknowledge the limitation and reframe the contribution accordingly.
- Reconcile Sections 4.1 and 4.2. Either drop the "approximately equal performance" claim and discuss the observed monotonic trends honestly, or provide statistical evidence (e.g., confidence intervals) showing that the increases are not significant at a given threshold.
- Add the p=0 TS-Guessing results to Table 3 so the probes are interpretable.
- Consider dropping or drastically shortening Section 5 (TACD) in favor of addressing the above issues, which would strengthen the empirical core of the paper.

---

Now let me report the calibration.

**Round 1 bracketing:** The paper falls in the 4.5–6.5 range based on comparison with "Evading Data Contamination Detection" (4.25 — our paper has clearer methodology and more empirical substance), "Elephants Never Forget" (4.75 — similar, our paper has better experimental control), and "How much can we Forget about Data Contamination?" (6.75 — stronger methodology, cleaner contribution, our paper is weaker) and "Training on the Test Task" (8.0 — substantially stronger).

**Round 2 narrowing:** Within the 4.5–6.5 bracket, I compared against "Detecting Pretraining Data from LLMs" (zWqr3MQuNs, 6.25) — this paper has a clear method with strong validation; ours has more methodological issues. Compared to "Dissecting learning and forgetting in LM finetuning" (tmsqb6WpLz, 5.75) — similar caliber: novel methodology, interesting findings, but with limitations and somewhat expected outcomes. Our paper has a more novel research question (cross-lingual contamination) but more significant internal contradictions.

**Final score:** The paper is comparable to or slightly below tmsqb6WpLz (5.75). The internal contradiction in claims and the training data ambiguity are meaningful weaknesses that prevent a higher score. I assign **5.0**.

### Calibration anchors referenced:

| Anchor ID | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| OdoS6cH8MP | Data Valuation | 2.00 | R1 | Significantly weaker; different topic |
| RuY1r1PDdQ | Instruction Following | 3.00 | R1 | Weaker; less empirical substance |
| ly10tMV6cD | Knowledge Inference | 3.25 | R1 | Weaker |
| Nk1MegaPuG | Evading Contamination Detection | 4.25 | R1/R2 | Our paper has clearer methodology, more empirical contribution |
| lwtaEhDx9x | Elephants Never Forget | 4.75 | R1/R2 | Our paper has better experimental control |
| hPk92D2GJV | BALCONI | 5.25 | R2 | Comparable, different topic |
| BCyAlMoyx5 | Crosslingual Capabilities | 5.67 | R2 | Comparable in quality |
| tmsqb6WpLz | Dissecting Learning/Forgetting | 5.75 | R2 | Our paper has slightly more significant methodological issues |
| zWqr3MQuNs | Detecting Pretraining Data (Min-K%) | 6.25 | R2 | Stronger; cleaner contribution and better validation |
| Nsms7NeU2x | Forget about Contamination | 6.75 | R1/R2 | Clearly stronger; more thorough experiments, theoretical analysis |
| m2NVG4Htxs | To the Cutoff... and Beyond | 6.75 | R1/R2 | Stronger; cleaner methodology |
| jOmk0uS1hl | Training on the Test Task | 8.00 | R1 | Much stronger; clear methodology, strong implications |
| syThiTmWWm | Cheating Auto Benchmarks | 7.75 | R1 | Stronger |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>