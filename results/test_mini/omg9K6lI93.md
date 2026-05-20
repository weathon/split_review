Now I have thorough calibration. Let me synthesize the final review.

**Round 1 bracket:** This paper is most similar to contamination detection papers in the 3.0–4.0 range. The weak anchors (<3.5) include "Fighting Fire with Fire" (3.33), "Detecting Variant Contamination" (3.00), and LogProber (3.00) — all share the same "fine-tuning on test data simulates contamination" paradigm. The middle anchors (3.5–7.5) include "Impact of Post-training" (4.67) and "Sensitivity of SLMs" (4.00), which have cleaner experimental designs. Initial bracket: 2.5–4.5.

**Round 2 narrowing:** The most topically comparable paper, "Fighting Fire with Fire" (3.33), shares the same fundamental realism concern (SFT on test data ≠ pretraining contamination) but validates its proposed detection method. This paper does not validate TACD. The "Detecting Variant Contamination" paper (3.00) has a similar gap between problem framing (variant contamination) and experiment design (fine-tuning). This paper additionally suffers from a verifiable textual contradiction in Section 4.2, a flawed baseline (p=0 already contaminated with English test data), and no testing of existing detection methods — issues the anchor papers do not have.

**Final score: 3.0/10 — Reject.**

---

## Summary

This paper studies whether translating evaluation benchmarks into Arabic can obscure signals of data contamination. The authors fine-tune four open-weight LLMs on Arabic-translated versions of MMLU, XQuAD, and MLQA test sets mixed with the original English test data, then evaluate on English benchmarks and probe memorization via a TS-Guessing extension with choice-reordering. They propose TACD, a blueprint for translation-aware contamination detection. The research question—whether translation masks contamination—is interesting and practically relevant, but the execution has multiple issues that prevent the paper from supporting its central claims.

## Strengths

1. **Novel research angle with practical relevance.** Studying how translation across languages can obscure contamination signals is a direction the community needs to explore, especially as multilingual evaluation becomes standard. The paper is among the first to empirically investigate this specific problem.

2. **Choice-reordering extension to TS-Guessing for MCQ.** The extension of TS-Guessing (Section 3.3, Figure 1) with random choice shuffling and answer-masking provides a finer-grained probe for memorization of positional patterns in multiple-choice benchmarks. This is a genuine methodological contribution that goes beyond the original TS-Guessing.

3. **Multi-model, multi-dataset design.** The paper covers four models (LLaMA-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) and three datasets spanning closed-book MCQ (MMLU) and extractive QA (XQuAD, MLQA). The task-dependent effects observed (monotonic MMLU gains vs. non-monotonic XQuAD/MLQA trends in Table 2) are interesting empirical observations worth reporting.

## Weaknesses

### Fatal
None.

### Major

1. **Section 4.2 makes a claim directly contradicted by the paper's own Table 2 data.** The text states that "the models exhibit approximately equal performance on all evaluated benchmarks" and "scores remain broadly stable as p increases" (lines 205–220), citing Tables 2 and 3a together. Yet Table 2 shows MMLU accuracy increasing monotonically: Mistral 0.577→0.690 (20% relative gain), LLaMA 0.332→0.431 (30% gain). These are large, clear improvements, not stability. This is not a minor phrasing imprecision — it is a factual contradiction between the paper's interpretive narrative and its own presented data. The central "masking" argument rests on this misreading. (Verifiable: compare lines 205–220 with Table 2 data on lines 180–184.)

2. **Baseline (p=0) already includes fine-tuning on the English test set.** The training condition is defined as 𝒟_EN^d ∪ 𝒟_AR^d(p) (Section 3.1, line 134), meaning even the p=0 baseline has seen the English test set. The paper therefore never establishes a clean baseline. The comparisons between p=0 and p>0 are between "contaminated with English test data" and "contaminated with English test data plus some Arabic test data," not between clean and contaminated conditions. This undermines any claim about what translation does to contamination, since contamination is already present at the reference point.

3. **No existing detection method is tested to demonstrate the claimed "blind spot."** The paper asserts that "translation into Arabic conceals traditional contamination signals" and that current methods would miss this. But it never applies Min-K% Prob, guided prompting, or any other existing detection method to its Arabic-translated data to verify this claim. A single experiment showing that, say, Min-K% Prob on Arabic items yields low scores despite measurable English performance gains would directly support the core narrative. Its absence is the most consequential empirical gap. (This is acknowledged indirectly as motivation for TACD but never executed.)

4. **TACD is presented as a contribution but is not validated.** Section 5 describes TACD as a "forward-looking blueprint rather than a complete implementation" (line 256). The paper therefore has two disconnected parts: an empirical study with methodological problems, and a proposed framework with zero experimental validation. The title and abstract frame TACD as a core output, but it contributes nothing that can be evaluated. (Confirmed: no TACD experiments exist in the paper.)

5. **TS-Guessing results do not clearly support the "masking" interpretation.** Table 3a shows erratic IDR values that are hard to interpret as "near-flat" (line 205): LLaMA IDR goes 0.287→0.643→0.410 (a swing), Gemma goes 0.350→0.029→0.005 (a clear decrease). The ROUGE-L-F1 values are near-zero across all conditions. The paper's claim that these trends indicate "masking" is not justified by the data — the probe may simply be insensitive to the contamination modality used (Arabic→English), not "masked" by translation.

### Minor

1. **No statistical significance or variance reported for any result.** Tables 2 and 3 present single numbers per condition. Given the observed non-monotonic trends in XQuAD/MLQA, reporting variance across multiple fine-tuning runs would substantially strengthen the claims.

2. **Limited dataset scope.** Only three benchmarks are used, all knowledge/QA tasks. The paper would benefit from at least one reasoning or generation benchmark (e.g., GSM8K, HumanEval) to test whether translation-masked contamination generalizes beyond factual recall and extractive QA.

3. **Embedding analysis mentioned but not shown.** Section 4.3 mentions an "embedding figure" showing high cosine similarity between Arabic→English translations and English originals, but no quantitative results (cosine similarity values, variances, or figures) appear in the main text. This is a missing piece of evidence for the claim that translation preserves semantics while perturbing surface forms.

### Trivial

None.

## Nice-to-Haves

- Applying existing detection methods (Min-K% Prob, guided prompting) on the Arabic data would directly test the "blind spot" claim.
- A truly clean baseline (no English test set exposure) would isolate the effect of Arabic contamination without confounding.
- Validating TS-Guessing on *Arabic* items (not English) would clarify whether the probe works for the intended modality and whether the English probe is the one that fails.
- Confidence intervals or standard deviations across multiple runs would improve interpretability.

## Removed Points

The following points from the harsh critic review have been removed with justifications:

- **"Mismatch between stated problem (pretraining contamination) and experimental design (fine-tuning)"** — Removed as an overreach. The literature review does discuss pretraining detection methods, but the paper's stated goal (Abstract, Section 1) is to study contamination dynamics *in general*, not specifically pretraining. The paper frames the fine-tuning setup honestly. The mismatch claim is a scope critique, not a factual error. (That said, the baseline flaw in point #2 of Major Weaknesses above is real and related but distinct.)

- **"The 'masking' claim is not supported because evaluation shows clear gains"** — Partially removed and reframed. The critic's version conflated two things: (a) the valid point that the *paper's own text* claims flat trends (which I verified and kept as Major Weakness #1), and (b) the separate point that "masking means no performance difference." The paper's actual claim is that TS-Guessing (a detection probe) doesn't pick up contamination, not that evaluation scores are flat. However, the paper's Section 4.2 does explicitly claim flat evaluation scores (which is wrong), so this is already covered in Major Weakness #1.

- **"TS-Guessing is inapplicable to Arabic modality"** — Removed. The probe is applied to English items, which tests whether the model memorized the Arabic content in a way that surfaces in English recall. This is a valid design choice, even if the results turn out to be noisy.

- **Pure formatting/style nitpicks** — Removed per instructions.

- **Strength Finder's claim that "demonstration that translation masks conventional contamination signals while preserving performance gains"** — Partially demoted. The TS-Guessing results are too noisy to support a clean "masking" narrative. LLaMA's IDR at 50% being 0.643 and Gemma's dropping from 0.350 to 0.005 are not "near-flat trends." This strength is not fully supported by the evidence.

## Novel Insights

The reviews surface two observations worth noting beyond the paper's own contributions. First, the *pattern* of results across tasks (monotonic MMLU gains vs. non-monotonic XQuAD/MLQA trends with a "peak at 10%" pattern) may itself be a finding worth deeper investigation: it suggests contamination effects are qualitatively different for closed-book MCQ versus extractive QA, potentially because MCQ reward answer-recognition while extractive QA requires span localization that overfitting disrupts. Second, the erratic TS-Guessing results across models (LLaMA swings, Gemma collapses, Mistral flat at zero) hint that surface-form memorization probes like TS-Guessing may have model-specific calibration issues that are poorly understood, which is a methodological finding for the contamination detection community regardless of this paper's specific claims.

## Suggestions

1. **Correct the Section 4.2 contradiction** by removing the claim that evaluation results (Table 2) show "approximately equal performance" and reframing the masking argument around TS-Guessing only — but then honestly acknowledge that the TS-Guessing data are noisy and do not cleanly support the narrative.

2. **Add a single experiment applying an existing detection method** (e.g., Min-K% Prob) on the Arabic-translated items. This would directly demonstrate whether current methods fail on translated data, which is the core premise of the paper.

3. **Retrain with a cleaner baseline** — either (a) remove the English test set from the p=0 condition and train only on unrelated data, or (b) include a no-fine-tuning control.

4. **Report variance** across at least 3 independent fine-tuning runs with different random seeds to assess stability of results.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Score | Round | Comparison |
|------|-------|-------|-----------|
| /home/wg25r/review_agent/human_reviews_2026/jCkmwIN9kz.md | 3.33 | R1 | "Fighting Fire with Fire" — same "SFT on test data" paradigm, validates its method → slightly stronger |
| /home/wg25r/review_agent/human_reviews_2026/Ubi631nNbI.md | 3.00 | R1 | "Variant Contamination" — similar gap between problem framing and experiment → comparable |
| /home/wg25r/review_agent/human_reviews_2026/WERLf030OU.md | 3.00 | R1 | LogProber — proposes detection method with limited experiments → comparable |
| /home/wg25r/review_agent/human_reviews_2026/GFDSGlEks2.md | 4.67 | R1 | "Impact of Post-training" — cleaner design, pretraining contamination → stronger |
| /home/wg25r/review_agent/human_reviews_2026/x4vwdjckZ6.md | 4.00 | R1/R2 | "Sensitivity of SLMs" — broader systematic study → stronger |
| /home/wg25r/review_agent/human_reviews_2026/A5cvMnKUpJ.md | 4.00 | R2 | "Rote Learners" — validated detection framework → stronger |
| /home/wg25r/review_agent/human_reviews_2026/zHjNmKiJCS.md | 2.00 | R1 | Translation errors in multilingual eval — weak anchor, less relevant |
| /home/wg25r/review_agent/human_reviews_2026/fkyebMiRHv.md | 2.67 | R2 | SLMs for low-resource MT — weak anchor, less relevant |

**Round 1 bracket:** 2.5–4.5  
**Round 2 narrowing:** The paper sits at the lower end of this band. Compared to the 3.0–3.33 anchors ("Fighting Fire with Fire," "Variant Contamination," LogProber), this paper has a verifiable textual contradiction in Section 4.2, a methodologically flawed baseline, and an unvalidated proposed framework — issues the comparable papers do not have. However, it has a more novel research question (translation masking) and broader model coverage. Score: 3.0.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>