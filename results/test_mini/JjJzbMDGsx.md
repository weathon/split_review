## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight two-layer MLP that operates at decoding time to mask tokens from unintended language families in multilingual LLMs, without modifying the base model. The gate is trained via norm-adjusted self-distillation: the authors first show that output token embedding norms are biased toward high-resource languages (CJ, Latin), which inflates their logits; they then debias the model's own logits via norm adjustment and use the debiased top-k/p predictions as pseudo-targets to train the gate. Experiments across Qwen3, Llama3.1, Gemma3, and GPT-OSS show order-of-magnitude reductions in CJ and Latin confusion on FLORES-NO-LATIN (e.g., Qwen3-30B: CJ from 1.0%→0.0%, Latin from 4.4%→0.4%) with negligible BLEU degradation and only 0.4% overhead in per-step generation time.

## Strengths

- **Mechanistically motivated and clean method.** The paper identifies a specific, measurable cause of language confusion—token embedding norm imbalance favoring high-resource languages—and uses it directly to construct pseudo-targets via norm-adjusted self-distillation. This is a precise, falsifiable contribution: Table 1 quantifies the imbalance (e.g., CJ tokens occupy 10.74% of top-5%-norm slots in Qwen3-8B vs. 0.14% for Low-Res), and Table 3 validates that the norm-adjusted gate (LCG-adjusted) consistently outperforms the unadjusted version (e.g., Latin% on Llama3.1-8B drops from 5.7% to 2.9%).

- **Strong and consistent empirical results across multiple model families.** LCG reduces confusion by an order of magnitude on Qwen3-8B, Qwen3-30B, Llama3.1-8B, and Gemma3-12B (Table 3), holds on thinking models on Humaneval-XL (Table 4), and maintains task performance (BLEU, INCLUDE accuracy, Pass@1/Pass@10). The intervention rate is sparse (0.33–0.38% of tokens), confirming the claim that LCG only fires at genuine confusion points.

- **Practical efficiency and plug-in design.** LCG adds 0.4% per-step overhead (15.95ms → 15.99ms on Qwen3-30B in production) and requires no base-model modification or retraining. The method is compatible with speculative decoding (noted in Appendix F). This makes the contribution immediately deployable.

- **Honest treatment of code-switching.** The paper explicitly acknowledges that rule-based single-language constraints would suppress legitimate code-switching and provides quantitative evidence that LCG preserves it: 86.7% token-level retention on human-validated code-switch points, and post-intervention code-switch rates on FLORES-WITH-LATIN remain close to ground-truth answer rates.

## Weaknesses

### Fatal

None.

### Major

- **Missing comparison with relevant post-hoc methods.** The paper cites Nie et al. (2025) (neuron suppression during inference) and Ji et al. (2025) (post-hoc smoothing to suppress Chinese tokens) in Related Work, both of which are *inference-time, no-retraining* interventions—the exact same class as LCG. Yet neither is included as a baseline. The paper also does not include a simple rule-based heuristic (e.g., "allow only the language family of the previous non-symbol token"), which would isolate whether the learned gate adds value over a static policy. Without these comparisons, the paper's positioning ("our work addresses gaps where existing approaches...") is asserted rather than demonstrated. The claim is not invalidated, but the reader cannot assess *how much better* LCG is than natural lightweight alternatives.

- **No confidence intervals or sample sizes for confusion rates.** Confusion rates in Tables 2, 3, and 4 are reported as single point estimates (e.g., CJ% = 0.0%, Latin% = 0.4%). When rates are very low (e.g., Gemma3-12B CJ: 0.2%→0.1%), a single differently-scored response could change the rate meaningfully. The paper does not report the number of responses per condition, Wilson/Clopper-Pearson intervals, or any measure of uncertainty. For a paper whose headline claim is "reduces language confusion," the reader needs to know the precision of these estimates. (The token-level intervention counts—e.g., 523/139,354—are helpfully provided for the intervention-rate analysis, but not for the confusion-rate metric itself.)

### Minor

- **Human evaluation for code-switch preservation is underspecified.** The paper reports that LCG allows English tokens at 86.7% of human-validated code-switch points, but provides no information about the number of annotators, the number of examples judged, or inter-annotator agreement. The evaluation is also limited to a single model (Qwen3-8B) and a single dataset (FLORES-WITH-LATIN). The result is promising but lacks the detail needed to assess reliability or generality.

- **No per-language breakdown of confusion rates.** The FLORES-NO-LATIN results in Table 3 are aggregated across Arabic, Hebrew, Korean, and Thai. Some languages may be more prone to CJ or Latin confusion than others, and LCG's effectiveness may vary. Reporting per-language rates would strengthen the evaluation and help identify failure modes.

- **ORPO hyperparameter configuration is not reported.** The paper compares against ORPO on two models but does not state the learning rate, number of epochs, batch size, or validation procedure used. This makes it difficult to assess whether the comparison is fair or whether ORPO could be tuned to better results. (Training details may be in the appendix, which was stripped from the accessible copy.)

### Trivial

- Figure 2's "After Norm Adjustment" column shows almost all tokens as "n" — this appears to be a rendering artifact; the original figure likely shows distinct Hebrew tokens.

## Nice-to-Haves

- An analysis of cases where the gate incorrectly masks or fails to mask (false positive/negative analysis) would help diagnose failure modes.
- A reasoning task beyond coding (e.g., math in Thai, scientific explanation in Arabic) would broaden the evidence for thinking-model compatibility.
- A simple heuristic baseline (previous-token language-family rule) would be easy to implement and would strengthen the claim that the learned gate adds value.

## Removed Points

These points were flagged in the inputs but were removed with justification:

- **"The baseline comparison is too narrow — missing post-hoc methods"** → Kept in Major (it is a real weakness). But the additional claim that the paper's tone implies it "outperforms existing approaches" was removed as an overstatement; the paper's actual language ("addresses gaps") is more measured.
- **"ORPO results are fragile / may be sensitive to hyperparameters"** → Removed. The paper's transparent reporting that ORPO degrades INCLUDE accuracy is a feature, not a flaw. The paper does not claim ORPO is optimally tuned; the comparison is between LCG (which maintains accuracy) and an alternative training-based method (which doesn't). This asymmetry favors the paper, not the baseline (see Hard Rules).
- **"Circularity concern: gate is trained on model's own biased distribution"** → Removed. The critic themselves acknowledges "this concern is not critical in practice" and the empirical results directly refute it. The norm adjustment is explicitly designed to debias the distribution.
- **"No evaluation on long-form generation beyond translation"** → Removed. This is scope creep; the paper evaluates on translation (FLORES), knowledge/reasoning (INCLUDE), and coding (Humaneval-XL), which are reasonable coverage for a plug-in intervention.
- **"Missing training details from main paper"** → Removed per Hard Rules (appendix stripped from parser).
- **"Missing error analysis of gate predictions"** → Removed. This is a nice-to-have, not a weakness; the paper already provides extensive ablation (LCG-unadjusted vs LCG-adjusted, No Rule) that serves as indirect validation.
- Strength Finder strengths about "the problem being important" → Removed as generic/superficial.
- Strength Finder's claim about "outperforms both decoding-based and training-based baselines" → Kept substantively but reframed since the baseline comparison gap is itself a weakness.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's concern about missing post-hoc baselines is valid but conventional; the strength finder's observations of consistency are faithful to what the paper reports.

## Suggestions

1. **Add at least one lightweight baseline.** The simplest option: a rule that allows only the language family of the previous non-symbol token + Symbols at each step. This is free to implement and would cleanly separate the value of the learned gate from the value of any language-constraint intervention. If space permits, implement a simplified version of Ji et al. (2025)'s post-hoc smoothing as a second baseline.
2. **Report confusion rates with sample sizes and confidence intervals.** Provide the number of responses per condition and Wilson intervals (especially important for the near-zero entries in Table 3). This can be done as a supplementary table or as parenthetical ranges in the main table.
3. **Expand the human evaluation for code-switching.** Report the number of examples judged, number of annotators, and inter-annotator agreement (Cohen's κ or Fleiss' κ). Ideally include a per-language breakdown of code-switch rates for FLORES-WITH-LATIN.
4. **Provide per-language confusion rates** for the FLORES-NO-LATIN results in the main paper or appendix, to show whether LCG's effectiveness varies by language.

## Score and Decision

**Bracketing (Round 1):** Three calibration queries on related topics established that the paper sits well above the <3.5 band (weak papers on multilingual confusion/reasoning, scored 2.67–3.33) and well below the 7.5+ band (top papers on unrelated topics, scored 8.0). Initial bracket: **4.5–7.0**.

**Narrowing (Round 2):** Two additional queries inside the bracket found anchors more closely matched to the paper's topic and quality level:
- **SASFT** (5.50, Accept Poster): Addresses the same problem (unexpected code-switching) via SAE-guided fine-tuning. Similar limitations on baseline comparison. LCG is stronger: tests more models (7 vs. 5), has cleaner mechanistic analysis, and is a more practical plug-in (0.4% overhead vs. SAE + fine-tuning). → LCG is above 5.50.
- **LinguaMap** (5.33, Accept Poster): Layer-localization of language control + selective fine-tuning on 2 models. LCG has broader model coverage, a different and complementary contribution. → LCG is above 5.33.
- **"How Do Languages Speak Languages"** (4.50, Reject): Mechanistic circuit analysis with limited mitigation (20.8% reduction). LCG has far stronger mitigation. → LCG is well above 4.50.
- **"Multilingual Routing in MoE"** (5.50, Accept Poster): Analysis of routing patterns with 1-2% gains. LCG's practical contribution is stronger.

The paper's core contribution—a mechanistically-motivated, plug-in gate that reduces confusion by an order of magnitude with 0.4% overhead—is clearly demonstrated. The main factors preventing a higher score are (a) missing comparisons with related post-hoc baselines and (b) lack of statistical confidence intervals, both of which limit how conclusively the advantage over alternatives can be assessed. Relative to the anchors, the paper is stronger than SASFT (5.50) but not at the 6.5+ level of papers on unrelated topics that address their completeness concerns more fully. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>