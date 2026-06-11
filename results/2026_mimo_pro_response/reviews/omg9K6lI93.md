Good. I now have a clear picture. Let me finalize the review.

**Round 1 bracket**: 3.5–5.0, anchored by:
- "Evading Data Contamination Detection" (4.25, reject) — similar topic, demonstrates vulnerabilities in detection; comparable novelty but cleaner than our paper in some respects
- "Benchmark Inflation" (4.25, reject) — contamination measurement; narrower scope but similar methodological gaps
- "Elephants Never Forget" (4.75, reject) — memorization testing; broader methodology
- "Detecting Pretraining Data" (6.25, accept) — introduces Min-K% Prob, a validated method with cleaner results; clearly above our paper
- "How much can we Forget about Data Contamination?" (6.75, reject despite high avg) — theoretical + empirical; stronger contribution

**Round 2** confirmed: 4.0–4.5 range. The paper under review has a more novel angle than the 4.25 anchors (multilingual dimension) but has worse internal consistency (narrative-data contradiction) and a missing control condition that those papers don't have.

**Final score: 4.0** — the novel multilingual angle and factorial design place it above generic rejects, but the missing control, narrative-data contradiction, and absence of statistical rigor place it clearly below the accepted contamination papers (6.25+).

## Summary
This paper investigates whether translating benchmark data into Arabic can mask data contamination signals in LLMs. The authors fine-tune four open-weight models (1B–7B) on varying proportions (0%, 10%, 50%, 100%) of Arabic-translated benchmark data from MMLU, XQuAD, and MLQA, evaluate on the original English benchmarks, and apply an extended TS-Guessing probe (with choice-reordering) to detect memorization. They conclude that translation conceals traditional contamination signals while not eliminating performance benefits, and propose a Translation-Aware Contamination Detection (TACD) framework as a future direction.

## Strengths
- **Novel multilingual angle on contamination**: The paper fills a genuine gap by studying cross-lingual contamination dynamics. Prior work (reviewed in Section 2) overwhelmingly focuses on English; extending the analysis to Arabic translation is a meaningful and underexplored direction.
- **Clear evidence of MMLU performance inflation from translated contamination (Table 2)**: Across all four models, MMLU accuracy increases monotonically with Arabic contamination proportion (e.g., Mistral: 0.577→0.690, LLaMA: 0.332→0.431, Gemma: 0.220→0.284), directly demonstrating that translated benchmark content inflates English evaluation scores.
- **Controlled factorial experimental design**: The 4 models × 4 contamination levels × 3 datasets design with consistent LoRA/PEFT fine-tuning settings (Section 3.1) cleanly isolates the effect of Arabic contamination proportion on downstream performance.
- **Extension of TS-Guessing with choice-reordering for MCQ**: The addition of shuffling answer choices before masking one and checking index-recall (IDR) is a methodologically interesting probe targeting memorized answer-key patterns (Section 3.3, Figure 1).
- **Transparent acknowledgment of TACD limitations**: The paper honestly states TACD is "a forward-looking blueprint rather than a complete implementation" (Section 5.3), which is preferable to overclaiming.

## Weaknesses

### Fatal
None

### Major
- **Missing control condition for multilingual fine-tuning effects**: The design compares English-only fine-tuning (p=0%) vs. English + Arabic-translated-benchmark fine-tuning (p>0%). Without a control that fine-tunes on equivalent amounts of Arabic non-benchmark text (e.g., Arabic Wikipedia), the observed performance changes cannot be cleanly attributed to contamination versus general multilingual adaptation. Adding any Arabic data during fine-tuning could shift model behavior through cross-lingual transfer or distributional mixing. The training equation D_train^d(p) = D_EN^d ∪ D_AR^d(p) (Section 3.1) only varies the Arabic benchmark proportion without controlling for Arabic data volume per se, leaving the contamination-vs-transfer distinction ambiguous.

- **Narrative-data tension on "near-flat" TS-Guessing characterization**: Section 4.2 claims "the models exhibit approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend." This does not match Table 3a's MMLU IDR data: LLaMA shows 0.287→0.643→0.410 (a 2.2× peak at 50%), Gemma shows 0.350→0.029→0.005 (a 70× collapse), and Mistral is flat at ~0.000 (no signal, not "masking"). Meanwhile, Table 2 shows clear monotonic MMLU accuracy increases that Section 4.1 itself acknowledges. The paper cannot simultaneously claim MMLU "exhibits a generally monotonic increase" (Section 4.1) and that models show "approximately equal performance on all evaluated benchmarks" (Section 4.2). The actual data tells a heterogeneous, model-dependent story that the paper's narrative oversimplifies.

### Minor
- **Unsubstantiated claim about "stronger Arabic capabilities"**: Both the abstract and introduction assert models "still benefit from exposure to contaminated data, particularly those with stronger Arabic capabilities." The paper never measures Arabic proficiency for any model, nor presents any correlation analysis between Arabic capability and contamination benefit. This claim is asserted without support.
- **Translation method not specified**: For MMLU, the paper describes "Arabic translations of the test items" (Section 3.1) but never specifies how these translations were generated—machine translation (which system?) or human translation. This matters because translation quality directly affects whether the finding generalizes. For XQuAD/MLQA, the existing Arabic dataset splits are used, which is clearer.
- **No statistical rigor**: All results are single-run numbers with no variance estimates, confidence intervals, or significance tests. Differences between contamination levels are often small (e.g., Qwen MMLU: 0.553→0.581, a 2.8-point gain) and could easily fall within noise from different random seeds.
- **Missing MLQA TS-Guessing results**: Section 3.3 states TS-Guessing is applied to "d ∈ {MMLU, XQuAD, MLQA}" but Table 3 only reports results for MMLU and XQuAD, omitting MLQA without explanation.

### Trivial
- Table 2's 12-column layout per model is hard to read; splitting by dataset would improve clarity.

## Nice-to-Haves
- A wider range of model sizes (e.g., 13B+) where cross-lingual transfer is more pronounced would strengthen claims about Arabic capability effects.
- Specifying and varying the translation method (e.g., multiple MT systems, human translation) would test generalizability.
- Implementing TACD on at least one language pair with experimental validation would transform the section from a discussion into a contribution.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **"Unfalsifiable interpretive framework"** — While the paper interprets every pattern as consistent with contamination, this is partly a natural consequence of analyzing multiple datasets with different characteristics. The framework would benefit from specifying falsification criteria, but calling it strictly unfalsifiable overstates the issue. The Gemma IDR collapse (0.350→0.005) does present a specific pattern that the paper could have engaged with more honestly rather than subsuming under "masking." Demoted to a presentation concern.
- **"TACD is unvalidated conceptual sketch"** — The paper already acknowledges this explicitly (Section 5.3). While TACD adds limited scientific value, the paper's honesty about its scope means this is more of a nice-to-have than a weakness.

## Novel Insights
The central novel observation is that translated (Arabic) benchmark contamination produces measurable English performance gains (monotonic MMLU inflation across all four models in Table 2) while standard English-only contamination detection methods would fail to flag this exposure. This "translation ≠ decontamination" finding is practically important for the LLM evaluation community and addresses a genuine gap in the predominantly English-centric contamination literature. However, the strength of this insight is tempered by the absence of a multilingual fine-tuning control and the heterogeneous, poorly characterized TS-Guessing results.

## Suggestions
1. Add a control condition: fine-tune on equivalent amounts of Arabic non-benchmark text (e.g., Arabic Wikipedia) to isolate contamination effects from general multilingual fine-tuning.
2. Report results over 3–5 random seeds with mean ± standard deviation, especially for small-effect comparisons like Qwen MMLU.
3. Reconcile the Section 4.2 narrative with the actual data: characterize the heterogeneous model-dependent patterns honestly rather than forcing a "near-flat" summary.
4. Specify the MMLU Arabic translation method and include MLQA TS-Guessing results in Table 3.
5. Either substantiate or remove the "stronger Arabic capabilities" claim.

## Reporting

### Anchors retrieved

**Round 1 (bracketing):**
- `8QTpYC4smR.md` — avg 1.00 (generic survey, all-1 scores) — far below our paper
- `5kMwiMnUip.md` — avg 1.40 (jailbreaking LLMs) — far below
- `gwZ90hFSL2.md` — avg 1.00 (cross-lingual robots) — far below
- `nSDOkm0SKo.md` — avg 1.00 (financial NN) — far below
- `OdoS6cH8MP.md` — avg 2.00 (textual data valuation) — below our paper
- `JQbqaQjV7D.md` — avg 3.00 (industrial benchmarking) — below
- `RuY1r1PDdQ.md` — avg 3.00 (LLM evaluation) — below
- `BltaWJZMeR.md` — avg 3.20 (DataSciBench) — below
- `Nk1MegaPuG.md` — avg 4.25 (evading contamination detection, reject) — closest match, similar topic
- `rAylWUIKtu.md` — avg 4.25 (benchmark inflation, reject) — similar topic, narrower scope
- `lwtaEhDx9x.md` — avg 4.75 (elephants never forget, reject) — memorization testing, more methods
- `QiyQJqpcYe.md` — avg 4.75 (Linguini benchmark, reject) — different focus
- `m2NVG4Htxs.md` — avg 6.75 (longitudinal contamination, accept) — stronger design, above our paper
- `Nsms7NeU2x.md` — avg 6.75 (forgetting contamination, reject despite high score) — theoretical + empirical, above
- `zWqr3MQuNs.md` — avg 6.25 (Min-K% Prob, accept) — validated method, clearly above
- `sKYHBTAxVa.md` — avg 7.33 (LiveBench, accept) — different focus, above
- `z8sxoCYgmd.md` — avg 8.00 (LOKI) — far above
- `jOmk0uS1hl.md` — avg 8.00 (training on test task) — far above
- `GGlpykXDCa.md` — avg 8.00 (MMQA) — far above
- `XmProj9cPs.md` — avg 8.00 (Spider 2.0) — far above

**Round 2 (narrowing):**
- `Nk1MegaPuG.md` — avg 4.25 (re-retrieved) — confirmed as closest anchor
- `lwtaEhDx9x.md` — avg 4.75 (re-retrieved) — similar topic, broader methods
- `rAylWUIKtu.md` — avg 4.25 (re-retrieved) — confirmed comparable
- `QiyQJqpcYe.md` — avg 4.75 (re-retrieved) — different focus
- `UnstiBOfnv.md` — avg 3.67 (style over substance, reject) — evaluation bias, below our paper

**Round 1 bracket**: 3.5–5.0. The paper is above generic/broken submissions (1–3) and comparable to the 4.25 contamination-focused rejects, with a more novel angle but worse internal consistency. Below accepted papers in this space (6.25+).

**Final score**: 4.0. The novel multilingual angle and factorial design push it above 3.5, but the missing control condition and narrative-data contradiction hold it below the 4.25 anchors that at least had cleaner internal logic. The paper needs substantial revision (adding controls, reconciling narrative with data, adding statistical rigor) before it could approach the accept threshold.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>