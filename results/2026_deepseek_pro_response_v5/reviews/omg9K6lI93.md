Now I have a clear picture across all anchors. Let me finalize.

**Round 1 bracket**: Based on comparison against anchors across bands, this paper sits roughly between 3.5–5.0. The strong reject anchors (1.50–2.00) are clearly worse — they lack experiments or have fundamental flaws. The strong accept anchors (7.5+) are clearly stronger — they have rigorous methods and well-supported claims. The paper under review has real contributions (novel IDR metric, systematic multi-model experiments) but is dragged down by the 4.1/4.2 contradiction and design limitations.

**Round 2 narrowing**: Comparing against the 4.25 anchors ("Evading Data Contamination Detection" — similar topic, similar level of issues), my paper is comparable but with the additional internal contradiction. Comparing against the 4.75 anchor ("Elephants Never Forget" — more comprehensive methods), my paper is weaker. The 5.00 anchor ("Understanding Memorisation Mechanics") has stronger methodology.

**Final score**: 4.0 — reject.

---

## Summary
This paper investigates whether translating benchmarks into Arabic can conceal data contamination in LLM evaluation. The authors fine-tune four open-weight models (Llama-3.2, Mistral-7B, Gemma-3, Qwen3) on mixtures of English and Arabic-translated benchmark data at controlled contamination proportions (0%, 10%, 50%, 100%) and evaluate on the original English benchmarks. They extend the TS-Guessing method with a choice-reordering strategy (yielding the IDR metric) to probe memorization of answer-position patterns across languages. The paper finds that contamination leaks through translation — MMLU accuracy rises with Arabic contamination — and proposes a Translation-Aware Contamination Detection (TACD) framework.

## Strengths
- **Novel choice-reordering extension to TS-Guessing**: The IDR metric — shuffling answer choices, masking one incorrect choice's text, and checking whether the model reproduces the pre-shuffle letter — is a creative probe that disentangles memorized answer-position patterns from content-based reasoning (Section 3.3). The variation in IDR across models and contamination levels (Table 3a) provides genuine signal, and the method is a transferable contribution beyond this paper.
- **Controlled experimental design across four model families**: Rather than post-hoc contamination detection, the paper actively introduces contamination at four controlled levels and measures downstream effects. Testing across Llama, Mistral, Gemma, and Qwen families (spanning 1B–7B parameters) provides cross-architecture evidence that the phenomenon generalizes beyond a single model family.
- **Clear evidence that translation ≠ decontamination**: Table 2 shows that MMLU accuracy on English test sets consistently rises as Arabic contamination increases (e.g., LLaMA: 0.332→0.431, Mistral: 0.577→0.690). This cross-lingual, cross-model pattern is the paper's strongest empirical finding and directly supports the claim that translated contamination still leaks through to benefit model performance.

## Weaknesses

### Fatal
None.

### Major
- **Internal contradiction between Sections 4.1 and 4.2**: Section 4.1 (line 189) documents "a generally monotonic increase" in MMLU as contamination rises and reports specific gains (Mistral: 0.577→0.690). Two paragraphs later, Section 4.2 (line 201) claims that across contamination levels the models show "approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend." These claims cannot both be true, and Table 2's data unambiguously supports Section 4.1 — MMLU rises for every model, XQuAD shows clear upward trends for 3 of 4 models, and several MLQA rows show dramatic collapses (Qwen: 0.409→0.157). The "near-flat" claim in 4.2 is directly contradicted by the paper's own data. This undermines the paper's interpretive claim that Arabic translation specifically "masks" or "conceals" contamination effects in a way that compresses observable performance differences.

- **Experimental design cannot cleanly isolate the "concealment" effect**: The training setup D_train(p) = D_EN ∪ D_AR(p) keeps English contamination constant across all conditions. This design can demonstrate that adding Arabic data provides performance benefits (supporting "translation ≠ decontamination"), but it cannot demonstrate that Arabic translation specifically conceals contamination signals relative to same-language contamination. Without a same-language contamination comparison condition or an Arabic-only condition, the claim that translation "masks" contamination (prominent in the abstract and Section 4.2) is asserted rather than experimentally isolated.

### Minor
- **No statistical rigor**: All results in Tables 2 and 3 are single point estimates with no standard deviations, confidence intervals, or multiple seeding runs. For LoRA fine-tuning on relatively small datasets, run-to-run variance can be substantial. This is especially relevant for claims built on small fluctuations (e.g., Gemma MLQA: 0.474→0.494→0.411→0.471) where the differences could fall within noise. While single-run reporting is not uncommon in the field, the paper's interpretive claims about specific trend shapes ("peak-at-10%," monotonic vs. non-monotonic) would be substantially strengthened by variance estimates.

- **TS-Guessing IDR variation is inadequately explained**: The IDR shows large, non-monotonic variation with contamination proportion (LLaMA: 0.287→0.643→0.410; Gemma: 0.350→0.029→0.005). Since D_EN is present in all conditions, the mechanism driving this variation is unclear. The paper does not offer an adequate account of why adding Arabic data causes IDR to first spike and then drop for some models but monotonically decline for others, leaving the TS-Guessing results suggestive but incompletely interpreted.

- **TACD framework (Section 5) is a sketch without empirical validation**: The paper acknowledges TACD is "a forward-looking blueprint rather than a complete implementation." While framing future directions is reasonable, devoting a full section to an untested framework adds length without evidential weight and does not function as a standalone contribution.

### Trivial
- **Embedding figure claim in Section 4.3 is unverifiable in the main text**: The paper states "The embedding figure shows that Arabic→English translations remain close to their English originals in representation space, with high cosine similarity" (line 224), but no such figure appears in the main body. If the figure is in the appendix, the claim should be referenced accordingly; if not, it is unsupported.

## Nice-to-Haves
- Running actual detection methods (Min-K% Prob, guided prompting) on the Arabic-contaminated models would directly test the claim that translation evades standard detection tools — a claim the paper makes but does not experimentally validate.
- A same-language English contamination condition (e.g., training on English paraphrases of test items) would provide a reference point for whether Arabic translation specifically compresses performance differences relative to within-language contamination.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *Harsh Critic claim that the experimental design completely fails to test the paper's central claim*: The design does test part of the central claim — that translation doesn't prevent contamination from leaking through. The limitation (kept as a Major weakness above) is specifically about isolating the "concealment" sub-claim, not about the entire paper being untestable.
- *Harsh Critic concerns about missing appendix content (Appendices A and B)*: Per review guidelines, the parser strips appendices; references to Appendix A (hyperparameters) and Appendix B (dataset statistics) are assumed to exist in the original submission.
- *Harsh Critic claim about "no discussion of pre-existing model exposure to benchmarks"*: The fine-tuning design partially controls for this since all conditions share the same base model. This is speculative and not a concrete identified problem in the paper.
- *Harsh Critic claim that TACD "is not a contribution"*: The paper explicitly frames TACD as a "blueprint," not an empirical contribution. The weakness is retained at Minor level for taking space without evidence, but the framing is honest.
- *Strength Finder claim about "well-structured literature review" as a core strength*: The literature review is competent but standard; it does not constitute a novel contribution and is common across most papers in this area.

## Novel Insights
The paper's extension of TS-Guessing with choice-reordering (IDR) for MCQ benchmarks is genuinely novel and could be useful beyond this study — it provides a way to detect answer-position memorization that survives translation. The finding that IDR varies non-monotonically with contamination proportion (peaking at 50% for LLaMA at 0.643 while declining for Gemma from 0.350 to 0.005) is an interesting empirical observation that, if verified with statistical rigor, could reveal cross-lingual interference dynamics in memorization that deserve further study.

## Suggestions
- Resolve the 4.1/4.2 contradiction by either removing the "near-flat" claim or substantially qualifying it. The data clearly shows trends — acknowledge them honestly and reframe the "masking" interpretation around what the data actually supports. If the intended claim is that Arabic translation compresses differences relative to what same-language contamination would produce, this needs a same-language baseline to support.
- Add at minimum 3-seed runs with reported standard deviations, particularly for the MLQA results where interpretive claims rest on small fluctuations.
- Either add the embedding figure to the main text or remove the claim that depends on it.
- Consider either removing Section 5 (TACD) to make space for deeper analysis of the existing results, or shortening it to a paragraph in the discussion.

## Score and Decision

**Anchor comparison summary (all rounds)**:

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Evading Data Contamination Detection (Nk1MegaPuG) | 4.25 | R1, R2 | Similar topic, similar issues; paper under review has more concrete experiments but also the 4.1/4.2 contradiction |
| Pre-Memorization Train Accuracy (OegBJMucyM) | 4.25 | R2 | Similar score level; our paper's contradiction is a more clearly identifiable flaw |
| Elephants Never Forget (lwtaEhDx9x) | 4.75 | R1, R2 | More comprehensive methods; our paper is weaker |
| Understanding Memorisation Mechanics (ILStlRb1Sp) | 5.00 | R2 | Stronger systematic methodology; our paper is weaker |
| How much can we Forget about Data Contamination? (Nsms7NeU2x) | 6.75 | R1 | Much stronger; large-scale experiments with theoretical grounding |
| To the Cutoff... and Beyond? (m2NVG4Htxs) | 6.75 | R1 | Much stronger; thorough longitudinal analysis |

**Round 1 bracket**: 3.5–5.0. **Round 2 narrowed**: The paper is comparable to the 4.25 anchors but has the additional verifiable problem of the 4.1/4.2 contradiction, placing it slightly below. It is clearly weaker than the 4.75+ anchors which have more rigorous methodology and fewer interpretive errors.

**Final score**: The paper has a real contribution (novel IDR metric, systematic cross-lingual contamination experiments, clear evidence that translation ≠ decontamination) but is undermined by an internal contradiction in its results interpretation, an experimental design that cannot fully support its "concealment" claims, and a lack of statistical rigor. These issues are addressable in revision but are significant enough to warrant rejection in current form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>