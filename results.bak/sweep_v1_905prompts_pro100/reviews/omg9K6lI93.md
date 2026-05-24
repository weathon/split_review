Now I have a clear calibration picture. Let me assemble the final review.

**Round 1 bracket:** The paper sits between the weak anchors (~2.5–3.0, irrelevant topics) and the strong anchors (7.75–8.0, substantially stronger papers). Within contamination-specific anchors: stronger than Nk1MegaPuG (4.25, rejected for unclear methodology and lack of novelty) and lwtaEhDx9x (4.75, rejected for insufficient validation), but weaker than m2NVG4Htxs (6.75, accepted, clean methodology and thorough experiments) and zWqr3MQuNs (6.25, accepted, the Min-K% Prob paper with clear contribution). Initial bracket: **4.5–6.0**.

**Round 2 narrowing:** Within the bracket, I compared against lwtaEhDx9x (4.75), zWqr3MQuNs (6.25), and X8dzvdkQwO (6.25). Our paper has a more systematic design than lwtaEhDx9x (clearer hypothesis, controlled contamination levels, multi-model) but is weaker than zWqr3MQuNs (less methodological clarity, more speculative components) and somewhat weaker than X8dzvdkQwO (similar idea-driven contribution but with more ambiguous methodology descriptions). Final placement: **~5.0**, leaning slightly below the 5.25–5.40 rejected anchors due to the D_EN^d ambiguity and lack of key baselines.

---

## Summary

This paper investigates whether translating English benchmarks into Arabic can mask data contamination in LLM evaluation. The authors fine-tune four open-weight instruction-tuned models on varying proportions of Arabic-translated MMLU, XQuAD, and MLQA test data, then evaluate on the original English benchmarks. They extend the TS-Guessing method with a choice-reordering strategy to probe for index-level memorization (IDR) as distinct from genuine reasoning. Key findings: MMLU accuracy increases monotonically with Arabic contamination while extractive QA shows non-monotonic, model-specific patterns; TS-Guessing reveals substantial index recall despite translation (e.g., LLaMA IDR=0.643 at 50% contamination with near-zero ROUGE-L), indicating that translation conceals but does not eliminate contamination. A speculative Translation-Aware Contamination Detection (TACD) framework is outlined.

## Strengths

- **TS-Guessing with choice reordering is a genuinely clever contamination probe.** The index-recall rate (IDR) metric — measuring whether a model predicts the pre-shuffle answer letter after choices are reordered — cleanly disentangles rote index memorization from content-based reasoning. The result for LLaMA-3.2-1B-Instruct (IDR=0.643 at 50% contamination with ROUGE-L=0.006, Table 3a) is striking and constitutes the paper's strongest empirical finding.

- **Systematic multi-model, multi-dataset, multi-contamination-level design.** Varying contamination proportion across four models, three datasets, and four levels (0%, 10%, 50%, 100%) provides a controlled framework for isolating contamination effects that prior English-only studies lack. This design enables the paper's most interesting observation: the divergence between monotonic MMLU gains and non-monotonic extractive QA patterns.

- **Nuanced model-specific analysis reveals non-trivial contamination dynamics.** The Mistral collapse on XQuAD beyond 10% (0.455→0.114, Table 2) while MMLU rises (0.577→0.690), and the frequent "peak-at-10%" pattern in MLQA followed by decline, are genuinely informative. These observations demonstrate that memorization can harm span localization while inflating closed-book scores — a finding with implications beyond the paper's specific translation focus.

- **Timely and well-motivated research question.** The paper identifies a clear gap: prior contamination research is English-centric, and the interaction between translation and contamination has been overlooked. The motivating question — whether translation acts as a barrier or merely a mask — is well-posed.

## Weaknesses

### Major

- **Ambiguous description of D_EN^d undermines confidence in the experimental design.** Section 3.1 states that D_EN^d is "the English split (MMLU: English test items formatted as MCQ; XQuAD/MLQA: English QA)." If interpreted literally, all models — including the p=0 (EN-only) condition — are fine-tuned on the exact English test items subsequently used for evaluation, which would render the study circular. The empirical evidence (p=0 MMLU scores in Table 2 match expected un-contaminated performance, e.g., Mistral 0.577, Gemma 0.220) suggests this literal reading is incorrect and the description is poorly worded. However, the ambiguity itself is a serious problem: the paper's central experimental setup cannot be evaluated with confidence. The authors must clarify exactly what data D_EN^d comprises and confirm that no evaluation data appears in English form during training.

- **No control for training data quantity.** The p>0 conditions add increasing amounts of Arabic data on top of the English data, meaning total training examples grow with p. Observed performance changes could reflect additional training data, cross-lingual transfer, or general fine-tuning effects rather than contamination-specific phenomena. Without a volume-matched control (e.g., Arabic data from a non-benchmark source at equivalent quantities), contamination effects cannot be isolated from data-quantity effects. This weakens attribution of the MMLU gains specifically to contamination.

- **Missing TS-Guessing baseline at p=0.** The TS-Guessing probes are only evaluated at p∈{10,50,100}% (Table 3). Without a p=0 baseline, we cannot verify that the IDR signal is near zero when no Arabic leaked data exists in training. The paper argues that translation "conceals" contamination, but cannot establish what the probe looks like in a clean setting, making it harder to interpret the reported IDR values as contamination-driven rather than, e.g., artifacts of the fine-tuning process or the base model's pre-existing behaviors.

### Minor

- **Section 4.2 "broadly stable" claim conflicts with Section 4.1 and the data.** Section 4.1 correctly describes MMLU as "generally monotonic" (Mistral: 0.577→0.690; LLaMA: 0.332→0.431). Section 4.2 then claims "scores remain broadly stable as p increases" when restricting to p∈{10,50,100}%. Even within that restricted range, Mistral MMLU nearly doubles its gain from p=10 to p=50 (0.580→0.690), and LLaMA rises steadily. The "broadly stable" framing is inconsistent with the paper's own earlier analysis and the reported numbers. The paper should resolve this internal tension.

- **No statistical measures reported.** No confidence intervals, standard deviations, or significance tests accompany any table. For the non-monotonic QA patterns — where fluctuations could reflect noise from small datasets or training variance — this absence makes it difficult to distinguish signal from noise. This is a standard expectation for empirical ML work.

- **Section 5 (TACD) is purely a vision statement with no experimental contribution.** The paper acknowledges this ("a forward-looking blueprint rather than a complete implementation"), and the section is brief, but it occupies space that could strengthen the empirical story. It is not evaluable as a contribution.

### Trivial

- The paper does not report the number of training examples per condition, making it difficult to assess the scale of each fine-tuning run (relegated to Appendix B, which is stripped).

## Nice-to-Haves

- A volume-matched control using Arabic non-benchmark data would substantially strengthen the attribution of effects to contamination rather than data quantity.
- Reporting TS-Guessing at p=0 would anchor the probe results and strengthen the paper's core claim.
- Statistical significance testing or confidence intervals would improve trust in the non-monotonic QA trends.
- A clearer separation between Sections 4.1 and 4.2 — or merging them — would resolve the current tension between "monotonic increase" and "broadly stable."
- Moving TACD to a brief discussion paragraph rather than its own section would keep focus on the empirical contribution.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Fatal: D_EN^d includes English test items making experiments circular"** — DEMOTED from Fatal to Major. The literal text is concerning, but the empirical evidence (p=0 scores in normal ranges) strongly contradicts the circular-experiment interpretation. This is a presentation/clarity issue requiring author clarification, not a verified fatal design flaw.

- **"TACD is a strength / contribution"** (from Strength Finder) — REMOVED. The paper itself describes TACD as "a forward-looking blueprint rather than a complete implementation." A purely speculative framework with no implementation or validation cannot be counted as a contribution.

- **"Comprehensive literature synthesis establishing a clear gap"** — WEAKENED and folded into the research-question strength. The literature review is competent but not exceptional; it is largely a catalog of prior work rather than a synthesis that generates new insights.

- **Harsh critic's "no control for data quantity — fatal" framing** — RETAINED but demoted from fatal to Major. The confound is real, but this type of control is uncommon in contamination probing studies and the effect direction (more data → better performance) is known; the more specific contamination probes (IDR) partially mitigate this concern.

- **Harsh critic's speculation about "training steps not balanced across p"** — REMOVED. The paper states "identical optimizer, schedule, context length, and batch policy across models and conditions." Without specific evidence of imbalance, this remains a speculative concern.

- **Harsh critic's claim that "the evidence presented cannot support the paper's conclusions"** — OVERSTATED and folded into specific Major/Minor weaknesses. The paper does provide suggestive evidence for its central claim (translation masks but does not eliminate contamination), particularly through the IDR results.

## Novel Insights

The most genuinely novel insight from this paper is the dissociation between index-level memorization and content-level reproduction under translation. The LLaMA result — IDR=0.643 but ROUGE-L=0.006 at 50% contamination — suggests models can learn to map Arabic-translated questions to specific answer-letter positions in the original English ordering without being able to reproduce the answer content. This implies a form of "structural leakage" where the ordinal structure of a benchmark (which answer is A, B, C, or D) is more easily transferred across languages than the semantic content of the answers themselves. This is a subtle and non-obvious contamination pathway that English-only probes would miss entirely.

## Suggestions

- The single most impactful revision would be clarifying the D_EN^d composition. If it is non-test English data (e.g., MMLU auxiliary training data, or unrelated English QA pairs), state this explicitly and explain the motivation for including it. If it does include test items, explain why p=0 scores remain in normal ranges (e.g., limited LoRA capacity, few epochs) and discuss the implications for interpreting results.
- Consider adding a data-quantity control experiment with at least one model and dataset: fine-tune with equivalent amounts of Arabic non-benchmark data and compare. This would directly address the most significant confound.
- Add TS-Guessing at p=0 for at least one model to establish the baseline IDR in the absence of Arabic contamination.
- Resolve the Section 4.1 vs. 4.2 tension: either remove the "broadly stable" framing or restrict it to specific model-dataset pairs where it actually holds.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Nk1MegaPuG ("Evading Data Contamination Detection") | 4.25 | R1 | Our paper has clearer research question and more systematic experiments |
| lwtaEhDx9x ("Elephants Never Forget") | 4.75 | R2 | Our paper has stronger experimental design; anchor criticized for insufficient validation |
| vl8VpW2niQ ("Memorization in In-Context Learning") | 5.40 | R2 | Similar level of empirical contribution but our paper has more methodological ambiguity |
| X8dzvdkQwO ("Fine-tuning can Help Detect Pretraining Data") | 6.25 | R2 | Our paper is weaker: less methodological clarity, more speculative sections, less thorough evaluation |
| zWqr3MQuNs ("Detecting Pretraining Data from LLMs" / Min-K% Prob) | 6.25 | R2 | Clearly stronger: introduced widely-adopted method with benchmark; cleaner experiments |
| m2NVG4Htxs ("Longitudinal Perspective on LLM Data Contamination") | 6.75 | R1 | Clearly stronger: cleaner methodology, thorough experiments, clear contribution |
| Nsms7NeU2x ("How much can we Forget about Data Contamination") | 6.75 | R1 | Clearly stronger: rigorous experiments + theory, though rejected on reviewer split |
| jOmk0uS1hl ("Training on the Test Task Confounds Evaluation") | 8.00 | R1 | Much stronger: clear methodology, important findings, well-executed |

The paper has a genuinely interesting and timely research question, a clever probing method (IDR with choice reordering), and reveals non-trivial contamination dynamics. However, the ambiguous description of the training data composition, lack of data-quantity controls, missing TS-Guessing baseline at p=0, and internal inconsistencies in result interpretation collectively prevent it from landing in the accept range. It is comparable to, and somewhat above, the lower-end rejected anchors (4.25–4.75) but falls short of the 6.25+ accepted anchors due to weaker methodological rigor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>