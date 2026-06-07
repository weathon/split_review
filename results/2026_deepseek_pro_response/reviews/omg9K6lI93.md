Now I have enough calibration data. Let me make my final comparison and determination.

**Round 2 comparison:**

- **"Elephants Never Forget" (4.75, Reject)**: Similar profile — novel probing methods for contamination, but execution issues (speculative without ground-truth training data, some experimental gaps). My paper has a more underexplored research angle (multilingual contamination) and the choice-reordering TS-Guessing is more novel, but my paper also has more severe internal problems (training on test data, internal contradiction, inconsistent probe results).

- **"Generalization v.s. Memorization" (5.00, Accept)**: Has a stronger, cleaner methodological contribution (task-gram LM) and internally consistent results, despite being limited to one training corpus. My paper's execution is weaker — the training-on-test-data issue, the Section 4.1/4.2 contradiction, and the inconsistent TS-Guessing results prevent it from reaching this level. This paper is clearly better executed.

- **"Evading Data Contamination Detection" (4.25, Reject)**: My paper is clearly stronger than this — broader experiments, more novel methodological contribution.

**Final score determination**: The paper sits between the 4.25 and 5.00 anchors but closer to the lower end due to three significant execution issues that undermine the core claims. I assign **4.5**.

Now let me finalize and write the complete review.

Let me also re-read the draft review and update it before finalizing.Now let me finalize the review with the calibration results incorporated.

---

## Summary

This paper investigates whether translating benchmarks into Arabic can conceal data contamination in LLM evaluation. The authors fine-tune four open-weight models on varying proportions (0%, 10%, 50%, 100%) of Arabic-translated benchmark data (MMLU, XQuAD, MLQA) alongside English data, then evaluate on the original English benchmarks. They extend the TS-Guessing method with a choice-reordering strategy to probe memorization independently of reasoning, and propose a Translation-Aware Contamination Detection (TACD) framework.

## Strengths

- **Genuinely important and underexplored research question.** Whether translation can mask contamination is a practically significant problem for multilingual LLM evaluation. The paper targets a real blind spot in current English-centric contamination detection, and the core intuition — that semantic content survives translation — is plausible and worth investigating.

- **Clever methodological extension: choice-reordering TS-Guessing.** Shuffling MCQ answer choices before masking and then measuring whether the model reproduces the pre-shuffle answer letter (Index-Recall Rate, IDR) is a smart probe design. It provides a contamination signal that cannot be explained by reasoning alone — a model must have memorized original answer positions to succeed. This extends prior TS-Guessing work (Deng et al., 2024) in a non-obvious direction.

- **Well-structured contamination-gradient design with multi-model coverage.** The four discrete contamination levels (0%, 10%, 50%, 100%) with identical LoRA/PEFT settings across runs create a causally interpretable setup. Testing across four model families (1B–7B parameters) strengthens generalizability of any observed patterns.

- **The MMLU results in Table 2 show a clear upward signal.** Mistral rises from 0.577→0.690, LLaMA from 0.332→0.431 — monotonic gains with increasing Arabic contamination that are broadly consistent with the hypothesis that Arabic-translated test data provides usable signal for English evaluation.

## Weaknesses

### Fatal

None.

### Major

- **All models are trained on English MMLU test items at p=0, meaning the baseline is already contaminated by design.** Section 3.1 explicitly defines D_EN^d for MMLU as "English test items formatted as MCQ." This means every model, including the p=0 "EN-only" baseline, is fine-tuned directly on the English test set it is later evaluated on. As a result, the paper cannot cleanly assess whether Arabic translation masks contamination versus whether Arabic translations add marginal contamination on top of an already-contaminated model. The comparison across p levels remains informative (showing Arabic translations provide additional benefit), but the paper's framing — investigating whether translation acts as a "barrier to contamination" — is undermined when the baseline condition already trains on the evaluation data. This design decision requires explicit justification and a careful narrowing of claimed conclusions, neither of which appears in the paper. The issue is specific to MMLU (for XQuAD/MLQA, "English QA" may refer to training rather than test data), but since MMLU is the dataset where the clearest contamination signal appears, the problem is consequential.

- **Internal contradiction between Sections 4.1 and 4.2 in how results are characterized.** Section 4.1 states that "MMLU exhibits a generally monotonic increase as contamination rises from 0% → 100%" and provides specific evidence (e.g., Mistral: 0.577→0.690). Section 4.2 then claims "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks. This near-flat trend indicates that Arabic → English translation is effectively masking contamination effects." These two descriptions of the same MMLU data are directly contradictory — the scores cannot be both monotonically increasing and near-flat. The contradiction is neither acknowledged nor reconciled. Section 4.2's "near-flat" characterization may be intended to describe XQuAD/MLQA only, but the text unambiguously applies it to "all evaluated benchmarks." This undermines confidence in the paper's interpretation of its own results and weakens the central thesis.

- **The TS-Guessing probe results in Table 3a do not provide clean, consistent evidence for memorization.** Several patterns directly conflict with the contamination narrative: (a) LLaMA's IDR is non-monotonic (0.287→0.643→0.410) — there is no straightforward mechanism where 50% contamination produces stronger memorization than 100%; (b) Qwen's IDR decreases with contamination (0.261→0.251→0.208); (c) Gemma's IDR collapses from 0.350 at 10% to near-zero (0.005) at 100%; (d) Mistral shows IDR near zero at all contamination levels (0.000, 0.000, 0.001). ROUGE-L F1 scores are uniformly negligible (0.001–0.059 across all models and conditions). The paper does not address or explain any of these anomalies. While the choice-reordering TS-Guessing is a clever idea, the empirical results do not support the interpretation that it is reliably capturing contamination-driven memorization at the levels the paper claims.

### Minor

- **The "stronger Arabic capabilities" claim is unsupported.** Both the abstract and introduction claim that models with stronger Arabic capabilities benefit disproportionately, but the paper provides no Arabic benchmark scores, tokenizer analysis, or pretraining data estimates to substantiate which models have stronger Arabic capabilities. This is presented as a key finding without evidence.

- **The TACD framework (Section 5) is proposed but not evaluated, and adds limited value to an empirical paper.** The paper explicitly acknowledges TACD as "a forward-looking blueprint rather than a complete implementation" (line 252). While the transparency is appreciated, Section 5 proposes three components (cross-translation benchmarking, TS-Guessing across variants, back-translation consistency) without implementing or validating any of them. In a paper whose primary contribution is empirical, a purely speculative framework section reads as padding.

### Trivial

None.

## Nice-to-Haves

- Zero-shot baselines (model performance without any fine-tuning) would help contextualize the absolute magnitude of contamination effects and distinguish fine-tuning gains from contamination-driven gains.
- The embedding analysis referenced in Section 4.3 ("The embedding figure shows that Arabic→English translations remain close to their English originals") could provide useful mechanistic evidence. Including concrete numbers in the main body would strengthen this argument.
- Calibration of the TS-Guessing probe on a verifiably contaminated model (trained directly on English test data with no translation) would establish that the probe works as intended before interpreting results on Arabic-contaminated models.
- Statistical significance measures (confidence intervals) would help distinguish signal from noise, particularly given the non-monotonic patterns in XQuAD/MLQA and TS-Guessing results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic claim that the experimental design is a "structural flaw that invalidates the contribution" requiring the "entire experimental architecture to be rebuilt"** — REMOVED as overly extreme. The design has a real limitation (training on English test data for MMLU), but the comparison across p levels still provides useful signal about the marginal effect of Arabic translations. The flaw narrows interpretation rather than invalidating the work entirely. Downgraded to Major.

- **Harsh Critic claim that "this is not a contamination study — it is a study of what happens when you train directly on the evaluation set"** — REMOVED as overstated. For XQuAD/MLQA, the English split may be training data (not test data). For MMLU, the English test data training is a real design limitation but doesn't make it "not a contamination study" — it makes it a study of additional contamination through translation on top of English contamination.

- **Strength Finder claim that "translation compresses but does not eliminate contamination effects is well-substantiated"** — WEAKENED. The TS-Guessing results do not cleanly support this interpretation, and the Section 4.1/4.2 contradiction undermines the consistency of the evidence. The MMLU results in Table 2 do show clear gains, but the claim of evidence being "well-substantiated" across all datasets and probes is not supported.

- **Strength Finder claim about "controlled contamination-gradient design isolates causal effects cleanly"** — WEAKENED. The training-on-test-data issue (for MMLU) means the causal interpretation is more limited than claimed — the design isolates the causal effect of adding Arabic translations to an already-contaminated baseline, not the effect of contamination itself.

- **Harsh Critic complaint about missing embedding figure** — REMOVED. This is a PDF parser artifact; the figure exists in the original submission.

- **Harsh Critic complaint about Appendix being stripped** — REMOVED per instructions (parser issue, not author error).

- **Harsh Critic claim that the literature review is "thin" on multilingual contamination** — REMOVED. The literature review is adequate in scope and correctly identifies the gap the paper addresses. This is a subjective nitpick.

- **Harsh Critic speculation about what the Appendix "may" contain** — REMOVED. Cannot evaluate stripped content.

- **Strength Finder claim that the paper "addressed an important problem" / "targeted an interesting question"** — REMOVED as generic/superficial. These are not concrete, evidence-backed strengths.

- **Harsh Critic demand that the paper address problems outside its scope (e.g., disentangling cross-lingual transfer from contamination)** — REMOVED as scope creep. The paper's stated scope is investigating translation as a contamination mask, not building a complete taxonomy of cross-lingual effects.

## Novel Insights

None beyond the paper's own contributions. The core observation — that translation perturbs surface forms while potentially preserving enough semantic content to create a blind spot in contamination detection — is the paper's contribution and is a genuinely underexplored angle within the contamination literature. However, the empirical evidence presented does not cleanly establish this insight due to the design and consistency issues identified above.

## Suggestions

- **Restructure the training setup** so that the p=0 baseline does not include English test items (for MMLU). Use the MMLU dev/validation set or an alternative non-overlapping English dataset for the baseline training data, reserving the test set exclusively for evaluation. This would allow clean assessment of whether Arabic translations independently provide contamination signal.
- **Reconcile or resolve the contradiction** between Sections 4.1 and 4.2. If MMLU shows monotonic increases, the "near-flat" characterization in Section 4.2 must be qualified (e.g., restricted to XQuAD/MLQA) or the claim must be revised entirely.
- **Address the non-monotonic TS-Guessing patterns explicitly.** Provide a mechanistic explanation for why IDR decreases or fluctuates with higher contamination for several models, or acknowledge the probe's limitations and the uncertainty this introduces for the paper's central claims.
- Either **implement and evaluate one component of TACD** (e.g., run TS-Guessing on a second translated language beyond Arabic) or remove Section 5 and deepen the existing empirical analysis.

## Calibration Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Evading Data Contamination Detection (Nk1MegaPuG) | 4.25 | 1,2 | My paper is stronger — broader experiments, more novel probe design |
| Benchmark Inflation (rAylWUIKtu) | 4.25 | 1,2 | My paper is stronger — broader experimental coverage, more novel methodology |
| Elephants Never Forget (lwtaEhDx9x) | 4.75 | 2 | Comparable quality; my paper has a more novel angle but more severe internal problems |
| Generalization v.s. Memorization (IQxBDLmVpT) | 5.00 | 2 | My paper is weaker — this paper has cleaner methodology, internally consistent results |
| Memorization in In-Context Learning (vl8VpW2niQ) | 5.40 | 2 | My paper is weaker — this paper has more consistent evidence for its claims |
| To the Cutoff... and Beyond? (m2NVG4Htxs) | 6.75 | 1 | My paper is clearly weaker — cleaner methodology, stronger evidence |
| How much can we Forget? (Nsms7NeU2x) | 6.75 | 1 | My paper is clearly weaker — extensive experiments, theoretical framework |

Round 1 bracket: 4.5–6.0. Round 2 narrowed to 4.5–5.0. The paper lands at 4.5: it has genuine strengths (important problem, clever probe, well-structured design) but three significant execution issues (training on test data for MMLU, internal contradiction, inconsistent probe results) prevent it from making its case convincingly and place it below the 5.0 acceptance threshold.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>