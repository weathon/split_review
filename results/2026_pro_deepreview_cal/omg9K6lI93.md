Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary
This paper investigates whether translating benchmarks into Arabic can obscure data contamination in LLMs. The authors fine-tune four open-weight models on mixtures of English and Arabic-translated test sets across three benchmarks (MMLU, XQuAD, MLQA), evaluate on the original English versions, and use an extended TS-Guessing probe with choice-reordering to detect memorization. They find that translation masks contamination signals while models still benefit from exposure — particularly on MMLU — and propose a forward-looking Translation-Aware Contamination Detection (TACD) framework.

## Strengths
- **Novel multilingual angle on contamination.** Investigating whether translation into a morphologically distant language (Arabic) can act as a contamination barrier is a genuinely underexplored question. The paper's core finding — that translation masks but does not eliminate contamination — is supported by the MMLU monotonic accuracy gains across all four models (Table 2: e.g., Mistral 0.577→0.690, LLaMA 0.332→0.431).

- **Extended TS-Guessing with choice-reordering is a useful methodological contribution.** Masking an incorrect choice *after* shuffling answer positions (Section 3.3) and checking whether the model reproduces the pre-shuffle letter provides a clean way to disentangle index-level memorization from content reasoning in MCQ settings. The probe reveals model-specific patterns (e.g., LLaMA reaches IDR 0.643 at 50% contamination, while Mistral stays near zero; Table 3a) that a content-only probe would miss.

- **Broad experimental coverage.** Four models spanning different sizes (1B–7B) and architectures, three diverse datasets (MCQ + extractive QA), and four contamination levels (0%, 10%, 50%, 100%) reduce the risk of idiosyncratic artifacts. The non-monotonic "peak-at-10%" MLQA behavior (Table 2: Gemma, LLaMA, Qwen) is an interesting secondary finding that the paper identifies and discusses.

## Weaknesses

### Fatal
None.

### Major
- **The "approximately equal / near-flat" claim in Section 4.2 is inconsistent with the paper's own data for several model–dataset pairs.** Section 4.2 states that "across contamination levels $p \in \{10, 50, 100\}\%$, the models exhibit approximately equal performance on all evaluated benchmarks" and that the trend is "near-flat." While MMLU changes across these levels are modest for some models (e.g., Qwen: 0.560→0.562→0.581), other trajectories are not flat at all: Mistral XQuAD drops from 0.455→0.272→0.114, Qwen MLQA drops from 0.409→0.157→0.153, and Gemma XQuAD rises from 0.481→0.577→0.606. The paper's own Section 4.1 acknowledges these non-monotonic patterns in detail, but Section 4.2's blanket "approximately equal" language contradicts the very data the paper presents. The core thesis (translation masks but does not eliminate contamination) does *not* require the "flatness" claim to hold — the MMLU monotonic results and the TS-Guessing IDR values are sufficient — but this overstated narrative undermines the credibility of the interpretation and should be corrected.

- **The "broadly stable" claim for TS-Guessing results (Section 4.2) is similarly overstated.** Table 3a shows Gemma IDR plummeting from 0.350→0.029→0.005 and LLaMA IDR peaking at 0.643 then dropping to 0.410. These are not "broadly stable." The paper never analyzes the disconnect between Gemma's collapsing IDR and rising MMLU accuracy — a model that demonstrably benefits from contamination without showing a consistent index-memorization signal is informative but is left unexamined.

### Minor
- **The 0% training condition already includes the English test set ($\mathcal{D}^d_{\text{EN}}$).** As defined in Section 3.1, even $p=0$ trains on the English test items, so any improvement beyond 0% measures incremental benefit from adding Arabic translations on top of an already-contaminated model. The paper frames this as evidence about translation masking contamination in general, but the design does not examine the arguably more realistic case where a model encounters *only* translated contamination. This limitation is not discussed and should be acknowledged.

- **The embedding similarity claim in Section 4.3 lacks quantitative support.** The paper asserts "high cosine similarity" between Arabic→English translations and English originals but provides no numerical values, no description of the embedding space or layer used, and no methodological detail. The stripped figure cannot rescue this — the written claim is an assertion, not evidence. If this is central to the explanation of why translation masks contamination, it needs substantiation.

- **The TACD proposal (Section 5) is purely aspirational.** It offers no implementation, no proof-of-concept, and no empirical validation. The paper itself calls it a "forward-looking blueprint." While this does not harm the empirical contribution, it also does not add weight to it and reads as padding.

### Trivial
None.

## Nice-to-Haves
- A direct analysis of *why* Gemma's IDR collapses while its MMLU rises — this disconnect is interesting and would deepen the paper's contribution.
- Analysis of translation quality, lexical overlap, or dataset difficulty differences between Arabic translations and English originals to explain uneven contamination effects.
- Quantitative rather than qualitative description of the embedding overlap analysis.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic Claim 3: "The experimental design (0%) already contaminates the test set" characterized as a fatal invalidation.** This is a legitimate limitation (retained above as Minor) but is not fatal. The 0% condition is transparently described in Section 3.1, and the paper's comparisons across contamination levels are still informative about the *incremental* effect of Arabic translation.
- **Harsh Critic assertion that the paper's entire thesis collapses because of the "approximately equal" overstatement.** Overstated but not fatal — the MMLU monotonic results and TS-Guessing IDR data independently support the core thesis that translation masks but does not eliminate contamination.
- **Harsh Critic Claim 2 demanding the probe explain all accuracy-IDR disconnects.** The probe was designed to detect index-level memorization, not to explain all accuracy gains. That Gemma's IDR drops while accuracy rises is actually *consistent* with the paper's thesis (models memorize content, not index patterns, when contamination is masked by translation) — the paper simply fails to make this connection explicit.
- **Strength Finder: generic strengths about "important problem" / "interesting question."** Removed as too generic.
- **Harsh Critic: "TS-Guessing probing results further undermine the masking story."** As noted above, the diverse IDR patterns are not contradictory to the thesis — they reflect model-specific memorization strategies.
- **Harsh Critic: "The experimental baseline… does not examine the case where a model encounters only translated contamination without the original English."** Retained in weakened form as Minor, but the claim that this is the "more realistic setting" is debatable — real-world contamination often involves both English and translated versions.

## Novel Insights
The paper provides concrete evidence that contamination is not purely a surface-form phenomenon: semantic content survives translation into a morphologically distant language like Arabic. This implies that multilingual evaluation pipelines cannot assume that translating benchmarks into lower-resource languages provides a decontamination guarantee. The observed model-specific divergence between IDR and accuracy (e.g., Gemma's IDR collapse despite MMLU gains) suggests that contamination manifests differently across model architectures and language capabilities — a dimension that existing English-only contamination detection methods are blind to.

## Suggestions
- Rewrite Section 4.2 to drop the "approximately equal" / "near-flat" framing and instead honestly characterize the observed patterns: MMLU shows modest contamination-driven gains, while XQuAD/MLQA exhibit model-specific, often non-monotonic responses. The masking narrative can be supported without claiming flatness.
- Explicitly discuss the 0% baseline limitation: what can and cannot be inferred when the control condition already includes English test items.
- Either provide quantitative embedding similarity values (cosine scores, layer used, model used) or remove the unsupported claim from Section 4.3.
- Consider shortening or moving the TACD section to a discussion/future work paragraph — as a purely aspirational section it dilutes rather than strengthens the paper.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| MyotJECv0D (MT evaluation correlation) | 2.50 | R1 | Much weaker — unrelated topic, thin contribution |
| JQbqaQjV7D (Industrial benchmarking LLMs) | 3.00 | R1 | Weaker — limited novelty |
| rAylWUIKtu (Benchmark Inflation) | 4.25 | R2 | Weaker — single dataset, methodological gaps |
| Nk1MegaPuG (Evading Contamination Detection) | 4.25 | R1/R2 | Weaker — lacks technical depth, unclear methodology |
| lwtaEhDx9x (Elephants Never Forget) | 4.75 | R2 | Weaker — narrower scope (tabular data only) |
| vl8VpW2niQ (Memorization in ICL) | 5.40 | R2 | Our paper is stronger — broader model coverage, more diverse experiments |
| zWqr3MQuNs (Detecting Pretraining Data / Min-K% Prob) | 6.25 | R2 | Slightly stronger — cleaner method, well-executed, accepted |
| Nsms7NeU2x (How much can we Forget?) | 6.75 | R1/R2 | Stronger — thorough theoretical + empirical, though rejected |
| m2NVG4Htxs (To the Cutoff... and Beyond?) | 6.75 | R1/R2 | Stronger — cleaner methodology, accepted |
| jOmk0uS1hl (Training on the Test Task) | 8.00 | R1 | Clearly stronger — polished, persuasive |
| syThiTmWWm (Cheating Automatic Benchmarks) | 7.75 | R1 | Clearly stronger — well-executed |

**Round 1 bracket:** 4.5–6.5

**Round 2 narrowing:** The paper is stronger than the 4.25–5.40 anchors (Memorization in ICL, Elephants Never Forget, Benchmark Inflation, Evading Contamination Detection) and slightly weaker than the 6.25 anchor (Detecting Pretraining Data / Min-K% Prob). The key differentiator: the Min-K% Prob paper introduced a clean, well-validated method that became influential; our paper has a novel angle but its empirical presentation contains overstated claims that weaken its persuasiveness.

**Final score:** 5.0 — a borderline paper with genuine novelty in its multilingual contamination investigation and a useful methodological extension (choice-reordering TS-Guessing), pulled down by overstated claims in the results interpretation, missing quantitative evidence for the embedding analysis, and an undisclosed baseline limitation. The core thesis is supported by the MMLU data, but the paper's credibility is undermined by how it characterizes its own results.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>