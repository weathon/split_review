Now I have sufficient calibration. Let me construct the final review.

## Summary

This paper investigates whether translating evaluation benchmarks into Arabic can mask data contamination while still allowing models to benefit from exposure to contaminated data. The authors fine-tune four open-weight LLMs on English splits plus varying proportions (0-100%) of Arabic-translated test items from MMLU, XQuAD, and MLQA, then evaluate on the original English benchmarks. They extend TS-Guessing with a choice-reordering trick to probe memorization. The key findings are: (1) English MMLU accuracy rises monotonically with contamination level across all models, suggesting contamination leaks through translation; (2) XQuAD/MLQA show non-monotonic trends consistent with overfitting to surface quirks; (3) TS-Guessing yields mixed results — some models show near-zero signal while LLaMA-3.2-1B reaches 64.3% IDR at 50% contamination, indicating index-level memorization survives translation for some models. The paper also proposes a Translation-Aware Contamination Detection (TACD) framework as a conceptual blueprint.

## Strengths

- **Novel investigation of translation as a contamination mask.** The paper is, to my knowledge, the first to systematically test whether translating benchmarks into a non-English language (Arabic) conceals contamination signals while preserving performance benefits. This directly addresses a gap identified in Section 2.4: prior contamination research is overwhelmingly English-centric. The experimental design (Section 3.1) — fine-tuning on English plus Arabic-translated test sets and evaluating on English — is a clean way to test this.

- **TS-Guessing with choice-reordering detects meaningful memorization for some models.** The adaptation of TS-Guessing with choice reordering (Section 3.3, Figure 1) isolates memorization of answer-index patterns even after translation alters surface forms. LLaMA-3.2-1B-Instruct at 50% contamination achieves IDR=0.643 (Table 3a), meaning 64.3% of predictions recall the original answer letter after shuffling — a strong contamination signal that would not be detectable by English-only methods. This is direct evidence that the probe can detect contamination through translation for at least one model.

- **Monotonic MMLU accuracy increase across all models.** Table 2 shows MMLU accuracy rising monotonically with contamination for every model (Mistral: 0.577→0.690; Gemma: 0.220→0.284; LLaMA: 0.332→0.431; Qwen: 0.553→0.581). This trend is inconsistent with genuine generalization and consistent with contamination-driven memorization. This is the paper's cleanest and most reproducible finding.

- **Non-monotonic QA results provide a nuanced picture.** The finding that XQuAD/MLQA often peak at 10% contamination and then decline (e.g., Qwen MLQA: 0.162→0.409→0.157→0.153, Table 2) reveals that contamination effects are not simply inflationary — they can harm extractive QA at higher doses. The paper's discussion of "fragile transfer" (Section 4.1) is a thoughtful interpretation of this pattern.

## Weaknesses

### Major

- **No positive control for the TS-Guessing probe.** The TS-Guessing results are the paper's primary tool for distinguishing contamination from genuine generalization, but the probe is never calibrated on a condition where contamination is known to be detectable in a same-language setting. Without seeing what TS-Guessing looks like when contamination is present in English (where surface forms are preserved), the near-zero results for many model-dataset combinations (e.g., Mistral IDR consistently ≤0.001, XQuAD EM ≤0.018 for most models) are uninterpretable. They are equally consistent with (a) no contamination, (b) a probe that is too weak to detect whatever contamination exists, or (c) a probe that primarily works on English surface forms and loses sensitivity after translation. This undermines the paper's core argument that "translation masks contamination" rather than a weaker claim that the probe fails to detect it. (*Verifiable from paper: Table 3a shows near-zero values for several conditions; no English-only TS-Guessing baseline exists in the paper.*)

- **Potential confound between contamination and cross-lingual transfer/task familiarity.** Models are fine-tuned on English splits *plus* Arabic-translated test sets. The English evaluation gains could partially reflect domain adaptation — exposure to similar English questions and answer patterns during fine-tuning — without any contamination via Arabic. The Arabic data itself provides exposure to question formats and answer structures that could transfer to English reasoning. The paper attempts to use TS-Guessing to isolate memorization, but the probe is uncalibrated as noted above. Without a control condition (e.g., fine-tuning on Arabic translations where answers are scrambled or replaced), the performance gains on MMLU could partly reflect better task familiarity rather than contamination. (*Verifiable from paper: Section 3.1 describes training conditions; no ablation isolating contamination from domain adaptation is presented.*)

- **Imprecise and self-contradictory reporting in Section 4.2.** The text states: "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks." This directly contradicts Table 2, where Mistral's MMLU jumps from 0.580 to 0.690 between 10% and 50% contamination — a 19% relative increase. LLaMA rises from 0.381 to 0.431 (13% relative). The text then says this "near-flat trend indicates that Arabic → English translation is effectively masking contamination effects." The data does not support this characterization for several model-benchmark combinations. The authors may have intended to refer only to the TS-Guessing scores, but the text as written conflates accuracy and probe results and misrepresents Table 2. This is a clear writing/analysis error that must be fixed. (*Verifiable from paper: Compare line 203-206 ("approximately equal performance") with Table 2 data.*)

### Minor

- **TACD framework is a blueprint without implementation or validation.** Section 5 describes a "Translation-Aware Contamination Detection" framework entirely at the conceptual level. The paper does not run TACD, does not compare it to existing methods, and does not demonstrate that it would detect contamination missed by standard checks. The paper acknowledges this ("forward-looking blueprint rather than a complete implementation," line 256), but given that the central claim is about a detection blind spot, leaving the proposed solution unimplemented weakens the contribution. This is a missed opportunity to close the loop on the paper's motivating problem.

- **No information about translation quality or verification.** The paper does not specify how Arabic translations were obtained (machine-translated? human-translated?), whether quality checks were performed, or whether answer semantics were verified after translation. If translations are noisy or corrupt some answers, the flat performance trends could reflect data quality issues rather than contamination masking. (*Verifiable from paper: Section 3 describes training setup but omits any detail on translation sourcing or verification.*)

- **Missing variance or statistical significance estimates.** Every reported number is a point estimate. Given the modest model sizes (1B–7B parameters) and fine-tuning setup, it is unclear whether the observed differences (e.g., MMLU changes of 0.01–0.02) are stable or within noise. This is standard practice for this type of benchmark evaluation, so it is minor, but it limits confidence in the fine-grained comparisons.

### Trivial

- **Unsupported embedding similarity claim in Section 4.3.** The paper states "Arabic→English translations remain close to their English originals in representation space, with high cosine similarity" but provides no quantitative evidence — no figures, no numbers, no method description. This is a dangling assertion that should either be supported with data or removed. (*Verifiable from paper: lines 228-232.*)

## Nice-to-Haves

- **English-only contamination condition.** Running the same TS-Guessing probes on a model fine-tuned on English test items (with identical contamination levels) would provide the positive control needed to interpret the probe's sensitivity. If probes detect contamination clearly in English but fail in Arabic, that directly supports the "masking" narrative. If they also fail in English, the probes are simply insensitive.

- **Comparison with existing detection methods (e.g., Min-K% Prob, guided prompting) on the translated data.** The paper argues that current methods are English-centric but does not test whether any of them actually fail on Arabic-translated benchmarks. Demonstrating that established methods miss contamination that TS-Guessing or TACD catches would directly support the claim of a blind spot.

- **Deeper analysis of the MLQA non-monotonic trends.** The peak-at-10% followed by decline at higher contamination is the paper's most intriguing finding, but it receives only brief qualitative discussion. A more systematic analysis (e.g., per-question analysis of what changes at 50% vs. 10%) could reveal the mechanism behind the "fragile transfer" pattern.

## Removed Points

These points from the inputs are removed with justification:

- **"TS-Guessing probes provide no positive evidence of contamination (uniformly near-zero)"** — Factually inaccurate. LLaMA-3.2-1B achieves IDR of 0.643 at 50% contamination on MMLU (Table 3a). The critic's characterization of results as "uniformly near-zero" ignores this. The broader concern about lack of calibration is retained as a Major weakness, but the "uniformly near-zero" framing is removed.

- **"Sloppy references (Fraser et al. 2025)"** — The critic notes this is a preprint from June 2025 which is "post the current review date of May 2026." This is irrelevant — preprints can be cited. Remove per hard rule: do not question cited references.

- **"Missing related works"** — Removed per hard rule (you cannot verify this).

- **"Missing hyperparameters/TS-Guessing prompt template"** — These are likely in the stripped appendix. Removed per hard rule about missing appendix content.

- **"Literature review is considerably longer than necessary"** — Subjective formatting/stylistic opinion. Removed.

- Various generic criticisms about "the evaluation lacks rigor" without specific anchors — Removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the Section 4.2 wording is at odds with Table 2 is a genuine finding, but it is a reporting error in the paper, not a novel scientific insight. The strength finder correctly identifies the choice-reordering extension to TS-Guessing and the MMLU monotonic trend as concrete contributions.

## Suggestions

1. **Fix the Section 4.2 wording.** Clarify whether "approximately equal performance" refers to the TS-Guessing metrics specifically, or revise the claim to acknowledge the clear accuracy trends in Table 2. The current wording undermines reader trust.

2. **Run a positive control experiment.** Fine-tune models on English-only contamination at the same levels and run the same TS-Guessing probes. This would calibrate the probe and could single-handedly validate the central claim if probes detect contamination in English but not Arabic.

3. **Add translation quality information.** State how the Arabic data were created and verified. If available, report BLEU/COMET scores or human evaluation results. This addresses a natural reader question about data quality.

4. **Quantify the embedding similarity claim** in Section 4.3 with actual cosine similarity numbers or a figure, or remove the claim.

**Score and Decision**

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| LogProber | WERLf030OU | 3.00 | R1 | Weaker — limited experiments, weaker novelty |
| Auditing Test Data Contamination | YsoabhpS7z | 3.00 | R1 | Weaker — flawed assumption about reference distribution |
| Post-training Contamination | GFDSGlEks2 | 4.67 | R1 | Slightly stronger — cleaner experimental design, but less novel question |
| SLM Contamination | x4vwdjckZ6 | 4.00 | R1 | Comparable — interesting but incomplete evidence |
| CoDeC | YlpaaYxx4t | 5.33 | R1 | Stronger — validated method with extensive empirical results |
| Watermarking | WFGxFzFDmQ | 5.00 | R2 | Stronger — has theoretical guarantees and validated implementation |
| Poly-FEVER | l9jJYx9tnl | 5.00 | R2 | Stronger — substantial multilingual benchmark contribution |
| Benchmark Publishing | 29ETLxTQAN | 5.50 | R2 | Stronger — validated mitigation approach |

**Round 1 bracket:** Between weak anchors (~3.00) and strong anchors (8.00). Plausible range: 3.5–5.5.

**Round 2 narrowing:** Compared against R2 anchors scoring 4.00–5.50. The paper's experimental findings are interesting and the question is novel, placing it above the 3.0-level papers. However, the lack of a positive control for the TS-Guessing probe, the unresolved confound with cross-lingual transfer, and the unvalidated TACD framework place it below the 5.0-level papers (which offer validated detection methods or substantial benchmarks). The paper is most comparable to the SLM contamination paper (4.00) and the Post-training contamination paper (4.67), but the former has more extensive model coverage and the latter has cleaner experimental controls. Given the paper's novel question but incomplete evidence, the score sits slightly below the middle of these.

**Final Score:** 4.0

**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>