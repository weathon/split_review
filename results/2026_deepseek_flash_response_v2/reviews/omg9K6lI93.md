**Round 1 bracket:** Based on initial queries, the paper sits between the weak band (avg < 3.5; contamination-adjacent papers scoring 2.5–3.2) and the strong band (avg > 7.5). The plausible range is 4.0–6.5.

**Round 2 narrowing:** Compared to "Evading Data Contamination Detection" (4.25, Reject), this paper has a more novel angle and better breadth but shares similar levels of overclaiming. Compared to "Crosslingual Capabilities and Knowledge Barriers" (5.67, Reject), the paper is similarly positioned — a worthwhile question with clear limitations. Compared to "Fine-tuning can Help Detect Pretraining Data" (6.25, Accept), this paper is notably weaker due to its internal contradictions and lack of a clean experiment disentangling transfer from memorization. Anchoring inside [4.25, 5.67] and closer to the lower end due to the §4.2 overstatement issue.

**Anchors retrieved (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| Nk1MegaPuG (Evading Data Contamination Detection) | 4.25 | R1 | Similar topic. This paper has a more novel angle (translation) but also has overclaiming issues. Slightly better. |
| rAylWUIKtu (Benchmark Inflation) | 4.25 | R2 | Similar quality level. Both have interesting ideas but limited scope. Comparable. |
| BCyAlMoyx5 (Crosslingual Capabilities) | 5.67 | R2 | Comparable quality. Both study cross-lingual phenomena with similar strengths and limitations. |
| X8dzvdkQwO (Fine-tuning can Help Detect Pretraining Data) | 6.25 | R2 | More rigorous experimental design and cleaner claims. This paper is weaker. |
| MyotJECv0D (MT Evaluation Metrics) | 2.50 | R1 | Unrelated topic, much weaker quality. |
| SaOxhcDCM3 (Self-Consuming Training Loop) | 3.20 | R1 | Tangential topic, lower quality. |
| zkNCWtw2fd (Cross-lingual IR) | 3.00 | R1 | Lower quality, different focus. |
| fSbPwHjdDG (Llama thinks in English) | 3.00 | R1 | Lower quality, different focus. |
| m2NVG4Htxs (To the Cutoff... and Beyond?) | 6.75 | R1 | Significantly stronger methodology and execution. |
| Nsms7NeU2x (How much can we Forget) | 6.75 | R1 | Stronger theoretical and empirical contribution. |
| jOmk0uS1hl (Training on the Test Task) | 8.00 | R1 | Much stronger — clean experiments, clear narrative. |
| 84n3UwkH7b (Diffusion Memorization) | 8.00 | R1 | Different topic. |
| SctfBCLmWo (Dataset Bias) | 8.00 | R1 | Different topic. |
| EUSkm2sVJ6 (Data Usage Inference) | 7.60 | R1 | Different topic. |
| QiyQJqpcYe (Linguini) | 4.75 | R2 | Lower quality than current paper. |
| o1SGGW53GF (NativQA) | 6.25 | R2 | Stronger execution. |
| n1X2n7MJ8L (CulturalBench) | 5.00 | R2 | Similar quality — interesting dataset paper with defined scope. |
| vl8VpW2niQ (Memorization in ICL) | 5.40 | R2 | Similar quality, different focus. |
| jx6njBKH8E (Amplifying Training Data Exposure) | 5.75 | R2 | Comparable quality. |
| vjel3nWP2a (Scalable Extraction) | 6.67 | R2 | Stronger execution. |

---

## Summary

This paper investigates whether Arabic translation of evaluation benchmarks masks data contamination in LLM evaluation. It fine-tunes four open-weight LLMs on varying proportions (0%, 10%, 50%, 100%) of Arabic-translated test data from MMLU, XQuAD, and MLQA, evaluates on the original English benchmarks, and employs TS-Guessing with a choice-reordering extension to probe memorization. The core finding is that MMLU accuracy rises substantially with contamination (e.g., Mistral: 0.577→0.690) while the TS-Guessing probe yields model-dependent results — strong signals for some models (LLaMA-3.2: 0.643 IDR) but near-zero for others (Mistral: 0.000). A Translation-Aware Contamination Detection (TACD) framework is proposed as a blueprint.

## Strengths

- **Novel and timely research question.** The idea that translation could obscure contamination signals while preserving their performance effects is genuinely interesting and underexplored. This addresses a real gap in the contamination literature.

- **Multi-model, multi-dataset design with systematic contamination variation.** Using four models (1B–7B) across three datasets covering both MCQ (MMLU) and extractive QA (XQuAD/MLQA) at four contamination levels (0%, 10%, 50%, 100%) provides broader coverage than a narrower study.

- **Choice-reordering extension to TS-Guessing.** Shuffling answer choices before masking and computing the Index-recall rate (IDR) is a clean methodological addition that detects index-based memorization (e.g., LLaMA-3.2 reaching IDR 0.643 at 50% contamination) in ways that exact-match approaches would miss.

- **Task-specific contamination dynamics.** Section 4.1's finding that MMLU shows monotonic gains while XQuAD/MLQA show non-monotonic patterns (e.g., "peak-at-10%") is a nuanced result that goes beyond the simple "contamination inflates everything" narrative.

## Weaknesses

### Fatal
None.

### Major
- **§4.2 overstates score stability, contradicting the paper's own Table 2.** The paper claims "across contamination levels p∈{10,50,100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and that "scores remain broadly stable as p increases" (lines 201, 216). Table 2 directly contradicts this: Mistral MMLU goes from 0.577→0.690, LLaMA from 0.332→0.431, and Gemma from 0.220→0.284. XQuAD/MLQA results also show systematic shifts rather than stability. The TS-Guessing probes (Table 3a) do show relative flatness for some models, but the §4.2 text incorrectly groups evaluation scores with probe results. This is a clear factual error in the paper's own analysis narrative. The core thesis (translation can obscure some detection signals) does not depend on evaluation scores being flat, so this is fixable, but as written it substantially undermines credibility.

- **Conceptual conflation of "contamination" with legitimate cross-lingual transfer.** The paper attributes all performance improvements from training on Arabic-translated data to "contamination," but the mechanism could be legitimate cross-lingual transfer (Arabic QA training genuinely improving Arabic→English reasoning). The TS-Guessing probe was designed to distinguish these, but yields contradictory signals across models: LLaMA's IDR of 0.643 suggests memorization, while Mistral's 0.000 IDR across all levels with simultaneous MMLU gains (0.577→0.690) strongly suggests a different mechanism. The paper does not run control experiments (e.g., fine-tuning on Arabic data with wrong answers) that could distinguish memorization from transfer learning, nor does it adequately discuss what drives improvements when probes are negative.

### Minor
- **Only one target language (Arabic).** The paper frequently generalizes to "multilingual" contamination, but Arabic is morphologically rich and uses a non-Latin script — findings may not transfer to languages sharing more surface form with English (e.g., French, Spanish).

- **No variance or statistical significance reported.** All results are single-run point estimates. With small models (1B–7B) and varying contamination proportions, variance could substantially affect trends — particularly the non-monotonic patterns in MLQA.

- **Ecological validity gap.** Fine-tuning directly on translated test sets is a much stronger intervention than incidental exposure during pretraining. The paper does not discuss how this paradigm relates to real-world contamination from web-crawl data.

- **Unsupported claim about Arabic proficiency.** The abstract asserts that models with "stronger Arabic capabilities" benefit more from contamination, but no Arabic-specific evaluation is provided.

- **TACD framework is a blueprint only.** Section 5 presents TACD as a "forward-looking blueprint" (line 252) with no implementation or validation experiments. It is appropriately caveated but does not constitute a substantive contribution.

### Trivial
None.

## Nice-to-Haves
- Run a control experiment with *incorrect* answers in the Arabic fine-tuning data to distinguish contamination from transfer learning.
- Add an English-only fine-tuning baseline to quantify the *attenuation* effect of translation on contamination.
- Report results with confidence intervals (≥3 seeds).
- Test at least one additional language from a different family (e.g., French or Chinese).

## Removed Points
These points were excluded after verification against the paper:

1. **"Central claim contradicted by primary results"** (harsh critic) — Demoted from fatal to a specific §4.2 weakness. The core thesis (translation obscures detection signals while preserving performance effects) is supported by the data: MMLU gains show contamination persists, and TS-Guessing mixed results show detection difficulty. The problem is a localized overstatement, not a structural contradiction.
2. **"TS-Guessing shows near-zero memorization across all models"** — Partially removed as factually wrong for MMLU: LLaMA-3.2 achieves IDR 0.643, Qwen3 achieves 0.251–0.261. The valid concern about distinguishing learning from contamination is retained in the major weaknesses.
3. **"Experimental setup lacks ecological validity"** — Demoted from major to minor; this paradigm is common in contamination research and is a reasonable first approximation.
4. **Missing related work / formatting nitpicks** — Removed per instructions.
5. **Generic strengths** (Strength Finder) — Removed unspecific claims like "addressed an important problem." Only evidence-grounded strengths with specific paper references retained.

## Novel Insights
The reviews reveal an interesting tension the paper does not fully confront: the divergence between MMLU (where contamination effects are clearly visible) and TS-Guessing (where signals are strongly model-dependent) suggests contamination under translation is not a monolithic phenomenon. Mistral's 0.000 IDR alongside large MMLU gains (0.577→0.690) is particularly striking — it could indicate genuine cross-lingual transfer, or a form of semantic contamination that existing surface-form probes simply cannot capture. Neither the paper's "translation masks everything" narrative nor a skeptical "it's just transfer learning" position fully explains this pattern. The paper would benefit from engaging directly with this ambiguity rather than treating all gains as contamination.

## Suggestions
1. **Correct §4.2** to distinguish between evaluation scores (which DO shift with contamination) and TS-Guessing probe results (which show mixed flatness). The current text is inaccurate.
2. **Add a control experiment** with intentionally wrong answers in the Arabic training data to disentangle memorization from transfer.
3. **Add an English-only fine-tuning comparison** to empirically measure how much translation attenuates (vs. eliminates) contamination effects.
4. **Acknowledge scope limitations** more explicitly — single language, fine-tuning paradigm, small models — rather than generalizing to "multilingual contamination."
5. **Add variance estimates** across at least 3 random seeds.
6. **Remove or substantiate** the unsupported "stronger Arabic capabilities" claim.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>