Now I have enough context to write the review. Let me verify the most central concerns once more.## Summary
The paper investigates whether translating English benchmarks (MMLU, XQuAD, MLQA) into Arabic conceals data-contamination signals. The authors LoRA-fine-tune four small open-weight LLMs (Llama-3.2-1B, Mistral-7B-Instruct-v0.2, Gemma-3-1B-it, Qwen3-1.7B) on mixtures of English and Arabic-translated test items at p ∈ {0, 10, 50, 100}% and evaluate on the original English benchmarks. They apply a TS-Guessing variant with choice-reordering (Index-Recall Rate, IDR) and sketch a "Translation-Aware Contamination Detection" (TACD) framework, which they explicitly describe as a blueprint rather than an implementation.

## Strengths
- The core question — whether translation acts as a barrier to contamination or merely masks it — is timely and under-studied, and the cross-lingual fine-tune-then-evaluate-in-English setup is a reasonable way to probe it (§3.1).
- The choice-reordering extension to TS-Guessing for MCQ (§3.3) is a concrete, testable probe: a model that recovers a pre-shuffle answer letter after reordering is exhibiting index-level memorization independent of surface text. LLaMA-3.2-1B at 50% reaches IDR = 0.643 (Table 3a), which is a real positive signal in at least one model.
- The MMLU gains with increasing Arabic-translated contamination (Table 2: Mistral 0.577 → 0.690; LLaMA 0.332 → 0.431; Gemma 0.220 → 0.284; Qwen 0.553 → 0.581) demonstrate that translated benchmark exposure can still inflate closed-book accuracy on the English original.

## Weaknesses

### Fatal
None that are unambiguously fatal from what is on the page. Several of the structural concerns below would be fatal if the paper actually has the design problem described, but the wording in §3.1 leaves room for a charitable reading; I therefore demote them to Major.

### Major
- **Internal contradiction between §4.1 and §4.2.** §4.1 explicitly states "MMLU exhibits a generally monotonic increase as contamination rises from 0% → 100%" with quantified jumps (e.g., Mistral 0.577 → 0.690). §4.2 then claims "the models exhibit approximately equal performance on all evaluated benchmarks" and labels this "near-flat" — and uses the alleged flatness as the primary evidence that "Arabic → English translation is effectively masking contamination effects." Both readings cannot be true of the same Table 2 data. The headline interpretation that translation "masks" contamination rests on the §4.2 reading, but the data shown clearly contains the monotonic gains §4.1 describes. The thesis is therefore not supported by a coherent reading of the authors' own results.

- **The setup is ambiguous about what $\mathcal{D}_{\text{EN}}^d$ contains, and the interpretation hinges on this.** Equation 1 defines $\mathcal{D}_{\text{train}}^d(p) = \mathcal{D}_{\text{EN}}^d \cup \mathcal{D}_{\text{AR}}^d(p)$, with $\mathcal{D}_{\text{EN}}^d$ described as "English test items formatted as MCQ" for MMLU. If those are literally the items used to compute Table 2's English MMLU accuracy, then every condition — including p = 0 — is already maximally contaminated through direct English exposure, and the experiment cannot isolate what translation alone does. If a held-out English split is meant, the paper does not say so or describe its overlap with the eval split. A clean Arabic-only condition (no English exposure, evaluated in English) is the missing control that would isolate cross-lingual contamination transfer, which is what the abstract claims to study.

- **TS-Guessing IDR results partly contradict the contamination narrative.** Table 3a's IDR — the probe the paper itself frames as "a strong contamination signal" — moves the wrong way for three of four models as p grows: Gemma 0.350 → 0.029 → 0.005, Qwen 0.261 → 0.251 → 0.208, Mistral ≈ 0 throughout. LLaMA peaks at 50% (0.643) then drops to 0.410 at 100%. The paper treats this as further evidence that translation masks contamination, but the more parsimonious reading is that the probe is unreliable in this LoRA-fine-tuning regime, or that index-style memorization is not what the experiment induces. The discussion does not address the inconsistency.

- **TACD (§5) is described by the authors as a "forward-looking blueprint rather than a complete implementation."** No component is implemented, validated, or compared to alternatives — neither Cross-Translation Benchmarking, nor TS-Guessing across variants, nor Back-Translation Consistency. If the paper is read as introducing TACD, the contribution does not yet exist. If it is read as an empirical study, the experimental scope (one target language, four small models, three benchmarks) is narrow for the generality of the conclusion.

### Minor
- **No reported variance or multiple seeds.** Several of the trends interpreted as findings depend on differences in the 0.003–0.03 range (e.g., Qwen MMLU 0.553 → 0.560 → 0.562 → 0.581) that fall plausibly within seed-to-seed noise for LoRA on 1B-class models. Without seed averaging or error bars, the "monotonic increase" claim for some models is weakly supported even if the larger Mistral and LLaMA jumps are real.

- **Mistral's XQuAD collapse (0.455 → 0.272 → 0.114) is rationalized post hoc.** §4.1 calls this "consistent with memorization that helps option selection while harming calibration and span localization under distribution shift," but a memorization-driven inflation story does not naturally predict a 4× collapse on the same English split the model was trained on. Treating monotonic increases, non-monotonic curves, and collapses all as compatible with the thesis makes the claim hard to falsify.

- **§4.3 references an "embedding figure" that does not appear in the body** and gives no numbers. Either the figure and quantitative cosine similarities should be presented, or the claim should be softened.

- **Body should specify headline hyperparameters (LoRA rank, learning rate, epochs).** These govern how much memorization the model can absorb and therefore how the trends in Table 2 should be interpreted; deferring everything to the appendix is fine, but headline values belong in §3.1.

- **Lopsided length distribution.** Sections 2.1–2.4 occupy roughly five pages of background while the methodology and results that constitute the actual contribution span ~2 pages. §2.4 in particular paraphrases prior work without connecting to the paper's own findings.

### Trivial
- §4.1 reports MLQA numbers to four decimals (0.4936, 0.4109) while Table 2 reports three (0.494, 0.411); be consistent.
- §5's "Back-Translation Consistency" component is under-specified: for MCQ the output is a label and for extractive QA a short span, so it is unclear what "back-translating outputs" buys.

## Nice-to-Haves
- A clean 2×2 ablation — (Arabic-only vs. English-only fine-tuning) × (English vs. Arabic eval), plus a no-fine-tune baseline, with multiple seeds — would directly answer the cross-lingual transfer question the abstract poses.
- Applying at least one additional detection probe besides TS-Guessing (e.g., Min-K% Prob, guided prompting) to the same fine-tuned models would substantiate the claim that "current detection methods" generally fail under translation rather than only the one probe tested.
- A small TACD pilot — TS-Guessing across, say, three translated variants on one fine-tuned model, showing that aggregating across languages recovers a signal the English-only probe misses — would convert §5 from blueprint to evidence.

## Removed Points
*These points are flagged as removed; treat them with caution.*

- **"Conflation of deliberate fine-tuning with unintended pretraining-corpus contamination" (from harsh critic).** This is a fair framing observation but it is a scope/positioning concern, not a verifiable error in the paper. The paper's experiments do what they say (fine-tune on translated items, evaluate in English). Demoted to a phrasing concern rather than a substantive weakness.
- **Strength: "Causal evidence that translation masks contamination" (Strength Finder).** Overstated — it conflicts with the verified §4.1/§4.2 contradiction (Major weakness). The MMLU gains are real, but the claim that English-only checks are "near-flat" while Arabic exposure rises is exactly what Table 2 does not show. Kept the narrower MMLU-gain observation as a strength.
- **Strength: "Multiple models and benchmarks demonstrate generality of masking effect" (Strength Finder).** Partially preserved as a strength but trimmed — the effect is model- and dataset-specific (Mistral's XQuAD collapses; Gemma/Qwen IDR decreases with more contamination), so "generality" is not what the data shows.
- **Strength: "Non-monotonic trends reveal task-dependent contamination" (Strength Finder).** The non-monotonicity is real, but the paper's interpretation of it is post-hoc; it does not on its own count as a positive contribution.

## Novel Insights
None beyond the paper's own contributions. The observation that benchmark exposure in a translated form can still inflate English MMLU is a real (if limited) empirical point, but the broader claim — that translation masks contamination from standard probes — is not cleanly demonstrated by the experiments as reported.

## Suggestions
- Disambiguate $\mathcal{D}_{\text{EN}}^d$ in §3.1: is it the same items used at eval, a disjoint English split, or something else? Add an Arabic-only fine-tuning condition with no English exposure as the missing control.
- Reconcile §4.1 (monotonic) and §4.2 (near-flat) — pick one description of Table 2 and adjust the contamination-masking argument accordingly. If the claim is that some signals flatten while others (e.g., MMLU accuracy) inflate, say so explicitly.
- Run ≥3 seeds for each (model, p) cell and report standard deviation or 95% CIs; this is the single change with the highest payoff for the credibility of Table 2.
- Either implement a minimal pilot of TACD or rebrand §5 as a discussion section so the paper's contributions are not framed around an unimplemented framework.
- Add a second contamination probe (Min-K% Prob or guided prompting) to corroborate the false-negative claim about English-only detection.
- Produce the embedding figure referenced in §4.3 with cosine numbers, or remove the reference.
- Compress §2; merge §2.1–§2.4 into ~2 pages focused on what is needed to position the contribution.

## Evaluation by axis
- **Originality:** moderate — the multilingual angle on contamination is under-studied, and the choice-reordering probe is a small but genuine methodological extension.
- **Importance of research question:** real and timely.
- **Whether claims are well supported:** weak — the headline claim depends on a §4.2 reading that the §4.1 narrative and Table 2 contradict, and the TS-Guessing probe behaves inconsistently across models.
- **Soundness of experiments:** weak — ambiguous control structure, single runs, no variance, embedding figure asserted but not shown, narrow model/language coverage.
- **Clarity of writing:** acceptable but lopsided (heavy lit review, thin experimental section, internal contradiction).
- **Value to the research community:** modest — the MMLU exposure result and the IDR probe are useful seeds, but the paper does not yet deliver a clean experimental demonstration or a usable detection framework.

## Calibration

Anchors retrieved:

- `MyotJECv0D.md` — avg 2.50, Round 1 (weak band). MT-evaluation correlation paper, unrelated except for translation framing; much weaker contribution than this paper.
- `JQbqaQjV7D.md` — avg 3.00, Round 1 (weak band). Industrial LLM benchmark with cross-lingual angle; similar narrow empirical-study profile.
- `OdoS6cH8MP.md` — avg 2.00, Round 1 (weak band). Textual data valuation paper, off-topic.
- `RuY1r1PDdQ.md` — avg 3.00, Round 1 (weak band). Intent hallucination evaluation; off-topic but a similar small-experimental-paper profile.
- `Nsms7NeU2x.md` — avg 6.75, Round 1 (middle band). "How much can we Forget about Data Contamination?" — much stronger: theoretical bounds + extensive scaling experiments. Significantly above this paper.
- `lwtaEhDx9x.md` — avg 4.75, Round 1 (middle band). "Elephants Never Forget" — contamination for tabular data with multiple memorization tests; broader and better executed than this paper.
- `Nk1MegaPuG.md` — avg 4.25, Rounds 1 & 2. Closest topical match: proposes Evasive Augmentation Learning as a concrete contamination attack with implemented attack and detection-evasion evidence. Better-defined contribution than this paper, no §4.1/§4.2-style contradiction.
- `m2NVG4Htxs.md` — avg 6.75, Round 1 (middle band). Longitudinal contamination analysis using GPT cutoffs; much more careful experimental design.
- `syThiTmWWm.md` — avg 7.75, Round 1 (strong band). "Cheating Automatic LLM Benchmarks" — much stronger empirical demonstration with broader impact.
- `jOmk0uS1hl.md` — avg 8.00, Round 1 (strong band). "Training on the Test Task" — well above this paper.
- `z8sxoCYgmd.md` — avg 8.00, Round 1 (strong band). LOKI synthetic data benchmark; off-topic but indicative of strong-band quality.
- `YrycTjllL0.md` — avg 9.00, Round 1 (strong band). BigCodeBench; off-topic strong anchor.
- `GVNYi74t5L.md` — avg 4.25, Round 2. M4U multilingual eval; broader empirical scope than this paper.
- `JL42j1BL5h.md` — avg 3.50, Round 2. XSafety multilingual safety — small empirical multilingual study, similar profile to this paper.
- `DPynq6bSHn.md` — avg 4.33, Round 2. EMMA-500 multilingual model — broader contribution than this paper.
- `8uXkyWFVum.md` — avg 4.20, Round 2. Amuro & Char fine-tune analysis — 18 datasets, better executed empirical study.
- `28gMnEAgl9.md` — avg 5.33, Round 2. Abstract reasoning benchmark — broader experimental scope.
- `VoHJTTA2MB.md` — avg 4.33, Round 2. Finance multi-task fine-tuning case study; similar narrow case-study profile.
- `abRWxnjMIz.md` — avg 4.00, Round 2. Circuit-breakers scoping; methodology more developed.

Round-1 bracket: between ~3 and ~4.5. The paper is clearly weaker than any middle-band contamination anchor (Nsms7NeU2x at 6.75, m2NVG4Htxs at 6.75, lwtaEhDx9x at 4.75) and slightly weaker than Nk1MegaPuG at 4.25 because (a) Nk1MegaPuG has an implemented attack while this paper offers an unimplemented TACD blueprint, and (b) this paper contains the §4.1/§4.2 internal contradiction.

Round 2 narrowed the comparison to anchors in (2, 4.5) and (3.5, 5.5). The closest comparables are Nk1MegaPuG (4.25, closest topical match, somewhat stronger), JL42j1BL5h (3.50, similar narrow-scope multilingual empirical study), and JQbqaQjV7D (3.00). The paper sits below Nk1MegaPuG and roughly with JL42j1BL5h — around 3.0–3.5.

Putting weight on (1) the internal contradiction between §4.1 and §4.2 in the prose summary of the same Table, (2) the inconsistent TS-Guessing signal that the paper does not address, (3) the explicitly-unimplemented TACD framework, and (4) the ambiguous control structure — but also acknowledging that the MMLU-exposure-via-translation gains are a real positive finding and the IDR probe is a sensible idea — I land at 3.0.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>