Now I have thoroughly verified all claims against the paper. Let me write the consolidated review.

**FINAL CONSOLIDATED REVIEW**

---

## Summary

This paper investigates whether training language models to win debates via self-play improves the accuracy of an AI judge in a scalable oversight setting. Using information-asymmetric debates on QuALITY-Hard reading comprehension questions, the authors train Llama3-8B models with SFT + a novel DPO variant and find a 4% absolute increase in judge accuracy after debate training (p < 10⁻⁶), with a positive skill–accuracy trend. By contrast, non-adversarial consultancy training shows no such trend. The paper introduces ensembled and double consultancy baselines to isolate mechanisms and provides evidence that debate encourages more evidence-based argumentation while consultancy models become repetitive and learn idiosyncratic persuasiveness.

## Strengths

- **First empirical demonstration that debate training (not just inference-time optimization) improves judge accuracy.** Prior work by Radhakrishnan et al. (2023) failed to find this effect; the paper provides clear evidence of a positive skill–accuracy trend across training checkpoints (Figure 3), with the fully DPO-trained debate model achieving 67% win rate vs. 31% for the SFT model, alongside rising judge accuracy.

- **Carefully designed non-adversarial baselines that isolate the mechanisms behind debate's advantage.** Ensembled consultancy (72% accuracy) and double consultancy (75% accuracy) are well-motivated controls. The finding that double consultancy nearly matches debate (77%) but fails to show a positive skill–accuracy trend is informative: it suggests that the adversarial *training* process (not just side-by-side comparison at evaluation) discourages non-truth-seeking strategies.

- **Converging evidence from policy analysis.** The paper shows that debate models learn to use 96% more quoted words, while consultancy models become repetitive (98% quote repetition in second speech). The transfer experiment with GPT-4o (Pearson r = 0.98 for debate vs. 0.51 for consultancy) further supports that debate training produces more robust, generalizable argumentation strategies rather than judge-specific exploitation.

- **Judicious judge finetuning.** The authors finetune GPT-4T on human judgments from Michael et al. (2023) and Khan et al. (2024) to mitigate sycophancy and calibration issues. An untrained GPT-4T agreed with consultants 72% of the time; the finetuned judge is calibrated to the 50/50 prior, making the consultancy baseline a fairer and more challenging comparison.

- **Honest and thorough discussion of limitations.** The paper transparently acknowledges that explicit refutation does not yet drive judge decisions, that results are limited to one domain, and that obfuscated arguments remain a risk.

## Weaknesses

### Fatal

None.

### Major

None that are fatal to the paper's core claims. The most significant limitation is described below under Minor — it is substantive but does not invalidate the paper's central comparative findings.

### Minor

- **Single judge, distribution shift, and limited accuracy generalization evidence.** The judge is a finetuned GPT-4T trained on human/GPT-4 debate transcripts but used to evaluate Llama3-8B debates. The paper's key trend relies on this one judge. The GPT-4o transfer experiment (Figure 5, right) validates that debate win-rate rankings transfer (r = 0.98), but this is a measure of *persuasiveness*, not accuracy — it does not show that a different judge would exhibit the same accuracy trend. A held-out judge (e.g., a smaller model finetuned on Llama3-8B transcripts) or a small human evaluation of the same transcripts would substantially strengthen the claim. The paper's central comparison (debate vs. consultancy within the same judge) is internally valid, but the generality of the accuracy finding across judges remains uncertain.

- **No confidence intervals or error bars on accuracy estimates.** The paper reports a 4% absolute increase and p < 10⁻⁶ without describing the statistical test or accounting for temporal autocorrelation between checkpoints from the same training run. The 2 percentage-point gap between debate (77%) and double consultancy (75%) — a key comparison — cannot be assessed for reliability without error bars. Bootstrapping over questions would be informative and is standard practice.

- **Single training run with only two DPO iterations and no seed variation.** All analysis comes from one run, making it impossible to assess variance. Two iterations is modest; the paper's speculation that "further optimization should yield more accurate outcomes" would be better supported by evidence of non-saturating trends. Multiple seeds or more iterations would increase confidence in the finding.

- **Small absolute effect size.** The 4% improvement (SFT to full DPO) and the 2% gap between debate and double consultancy are modest. While meaningful in a scalable oversight context — where even small improvements matter if they scale with capability — the paper would benefit from a clearer discussion of practical significance.

### Trivial

- The term "consultancy" is used for both the training objective (single consultancy) and the evaluation protocols (ensembled/double). The authors are explicit about this distinction, but it creates momentary confusion.
- The DPO variant's similarity to concurrent work (Nemotron-4 340B) is acknowledged but could be stated more prominently to avoid any perception of omitted prior art.

## Nice-to-Haves

- A breakdown of judge errors by question type (e.g., does accuracy vary with question difficulty, or are errors correlated with debater confidence?) would enrich the analysis.
- A full-information baseline (judge accuracy when reading the full story) would calibrate the scale of improvement — how much room for improvement remains?
- Training a consultant with the same *evaluation* protocol as double consultancy (i.e., training on double consultancy win rate rather than single) would more directly test whether the adversarial training component is necessary.
- Testing more DPO iterations (4–5) to see if the accuracy trend continues or saturates.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the consultant is not trained with the same DPO procedure (from Harsh Critic #2):** The paper explicitly trains both debaters and consultants with the same DPO variant (Section 3.2, line 159: "We train the debater and consultant using multiple iterations of our variant of DPO"). The suggestion "train a consultant with the same DPO procedure used for debate, but without an opponent" is exactly what the paper already does. This criticism is factually incorrect and removed.

- **Criticism about missing human evaluation / full-information baseline / analysis of mistakes (from "Missing Parts"):** A human evaluation of hundreds of transcripts is practically infeasible for an academic submission. The full-information baseline and error analysis are reasonable suggestions but are wishlist items, not flaws that undermine the paper's claims. Moved to Nice-to-Haves.

- **Criticism about the DPO variant lacking novelty (from "Other Observations"):** The paper acknowledges the concurrent work (line 139). The contribution is the application to self-play debate training, not the loss function itself. This is not a weakness — it is proper attribution.

- **Criticism demanding tests on other tasks/domains (implicit in "Missing Parts"):** The paper is scoped to reading comprehension; demanding broader task coverage is scope creep. The paper discusses this limitation honestly (lines 239–240).

## Novel Insights

The most striking observation emerging from the reviews is that the paper's strongest contribution is not just the positive skill–accuracy trend for debate, but the *negative finding* for consultancy despite significant optimization pressure. The consultancy model convinces the judge with increasing frequency (36% → 52% win rate) while judge accuracy remains flat — this is precisely the pathology debate is meant to prevent, and the paper documents it with concrete mechanistic evidence (quote usage, repetition, low transfer to GPT-4o). The double consultancy baseline further sharpens the picture: when the same trained consultant argues both sides in the same context, the judge's accuracy rises to near-debate levels (75% vs 77%), but the *trend* with training is still absent. This implies that the value of adversarial debate lies less in refutation at inference time and more in shaping the *training* distribution to discourage cheap persuasive strategies — a nuanced finding that future work should build on.

## Suggestions

1. **Add error bars or confidence intervals** for the accuracy estimates in Figure 4, using bootstrapping over questions. This would clarify whether the 2% debate–double consultancy gap is reliable.

2. **Validate the accuracy trend with a second judge.** The most impactful single addition would be finetuning a smaller, more accessible model (e.g., Llama-3-8B) on the same human-judgment data and replicating the accuracy analysis. Even if the absolute accuracy differs, observing the same positive trend would substantially strengthen the claim.

3. **Report the statistical test used for p < 10⁻⁶.** Clarify whether it accounts for autocorrelation between checkpoints from the same run, or re-run with at least one additional seed.

4. **Run at least one additional DPO iteration** to confirm the trend has not saturated and that the positive slope is robust.

## Score and Decision

**Originality:** 7/10 — First training-time positive result for debate accuracy; novel baselines.  
**Importance of research question:** 8/10 — Scalable oversight is a central challenge for AI safety.  
**Claims well supported:** 6/10 — Core claim supported but weakened by single judge, no CIs, single run.  
**Soundness of experiments:** 7/10 — Careful design with well-motivated controls; statistical rigor could be stronger.  
**Clarity of writing:** 8/10 — Well-structured, honest about limitations, figures clearly described.  
**Value to the research community:** 7/10 — Useful finding and baselines for the debate/scalable oversight community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>