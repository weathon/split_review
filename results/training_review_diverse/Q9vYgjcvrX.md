Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper explores semi-supervised instruction data generation using only open-source models, proposing the SASS framework. It systematically compares Self-Training (generating responses for instructions) vs. Instruction-Generation (generating instructions for responses), finding IG significantly better. Two strategies are proposed to improve IG: (1) **instruction filtering** — generating multiple candidate instructions per response and selecting via lowest perplexity, and (2) **extract-then-generate** — using extracted fragments (keywords, random sentences, or LLM-extracted fragments) instead of full documents as responses. Experiments on LongForm and AlpacaEval show SASS-generated data outperforms baselines (including those using closed-source models like Alpaca and LLaMAGPT4) and that weaker models can self-generate data comparably to using data from another 7B model.

## Strengths

1. **Systematic comparison of self-training vs. instruction-generation strategies (Figure 1).** The paper clearly demonstrates that generating instructions for existing responses (IG) is more effective and robust than generating responses for instructions (ST) across different seed datasets and data amounts, with minimal fluctuation. This is a practical finding for the field.

2. **Instruction filtering strategy shows clear improvement (Figure 4a).** The PPL-based selection from multiple candidate instructions yields a visible performance gain over the unfiltered baseline, confirming the value of tight instruction-response alignment.

3. **Extract-then-generate strategy demonstrably improves diversity and performance (Figures 4b, 5).** LLM extraction outperforms keyword and random-sentence extraction, and combining origin documents with extracted fragments achieves the best results. The diversity visualization (Figure 5) provides qualitative support.

4. **SASS data outperforms all baselines on LongForm, including methods using GPT-4 (Table 1).** The proposed framework achieves the best METEOR scores across 8 sub-tasks, directly supporting the paper's central claim that high-quality instruction data can be generated without closed-source models.

5. **Practical motivation and clearly scoped problem.** The paper explicitly identifies the legal/usage restrictions of closed-source models and makes a well-reasoned case for self-alignment, giving the work clear practical significance.

## Weaknesses

### Major

1. **No variance reporting or significance testing across any experiment.** No confidence intervals, standard deviations, or significance tests are reported for any result (Table 1, Figures 1, 3, 4, 6). Given that several key comparisons appear visually close — SASS vs. Alpaca in Figure 3, and "Self" vs. "LLaMa" in Figure 6 — it is impossible to assess which differences are meaningful and which reflect noise. This weakens the evidential weight of the paper's central comparative claims.

2. **Overclaimed weak-model comparison (Figure 6 and Section 5.5).** The paper states that "the performance of generating data for themselves is on par with distilling from the more powerful model LLaMa-7B." However, no evidence is provided that LLaMA-7B is actually "more powerful" than Baichuan2-7B or BLOOMZ-7B1 on the relevant task — all are 7B models. Without benchmark comparisons establishing a capability hierarchy, the "more powerful model" framing is misleading. The experimental observation that self-generation works comparably to cross-generation from another 7B model is still interesting, but the claim should be reframed accurately.

3. **LLM extraction model training is critically underspecified (Section 4.1).** The paper states: "We use the Dolly to train an extracted model to extract informative and self-contained fragments as the selected response." No details are provided about model architecture, training data preparation, training procedure, or inference-time extraction behavior. Since extract-then-generate is one of the paper's two main contributions, this gap makes a significant component non-reproducible as described.

### Minor

4. **Instruction filtering ablation is confounded (Figure 4a).** The "w/o instruction filtering" condition is not clearly specified: does it use the first generated instruction, a random candidate, or something else? Without controlling for the number of candidates, the measured improvement could stem from sampling multiple candidates rather than from the PPL-based selection criterion. This does not invalidate the filtering strategy but weakens the isolate-it contribution.

5. **Data quantity is a confound in the main comparison (Table 1).** Baseline dataset sizes vary widely (Lima: 1K, Dolly: 15K, Alpaca: 52K, LongForm: 17K). The paper does not discuss how data quantity might affect results or provide a size-matched comparison, making it unclear how much of SASS's advantage comes from method quality vs. data volume.

6. **"Origin + LLM Extraction" composition is underspecified (Figure 4b).** The paper reports that combining origin documents with LLM extraction achieves the best performance, but does not specify how many samples come from each source or the mixing ratio. This hinders reproducibility.

7. **No justification for weak model selection (Figure 6).** The paper chooses Baichuan2-7B and BLOOMZ-7B1 without reporting their baseline task performance or explaining why they are representative "weak models." Contextualizing their capability would strengthen the comparison.

8. **Evaluation relies primarily on METEOR for LongForm.** While the GPT-4 evaluation on AlpacaEval partially compensates, relying on a single n-gram metric on the main benchmark is a relatively narrow evaluation signal.

### Trivial

None beyond issues already captured above.

## Nice-to-Haves

- A size-matched ablation where the best competitor is downsampled to SASS's data quantity (50K).
- A quantitative diversity measure (e.g., unique verb-noun pair counts, entropy of instruction types) to complement the qualitative parse-tree visualization in Figure 5.
- A brief limitations section discussing the scope of the study (7B models only, known metric weaknesses, reliance on seed data).

## Removed Points

- **"Introduction overstates potential risks of closed-source model usage"** — This reflects the reviewer's opinion on legal framing, not a paper flaw. The paper's usage-restriction motivation is standard in the literature.
- **"Only one n-gram metric" as a standalone criticism** — The paper also uses GPT-4 evaluation on AlpacaEval, so the concern is already partially addressed. Kept in Minor as a limited criticism.
- **"The paper should discuss domain analysis of instructions"** — This is a nice-to-have, not a weakness. The paper already provides a diversity analysis (Figure 5).
- **"The paper lacks a limitations discussion"** — The paper explicitly calls itself "a preliminary study" (Conclusion), which signals limitations. Moved to Nice-to-Haves.
- **"Data size control demand"** — This is addressed in Minor as a confound, but the demand for a full downsampled comparison is scope-creepy given the paper already covers multiple baselines and ablations.
- **Any criticism about missing appendix content, formatting artifacts, or parser issues** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add error bars** — Even simple bootstrap confidence intervals over evaluation instances would transform the credibility of all comparative claims. This is the single highest-leverage improvement.
2. **Fix the filtering ablation** — Add a control condition that randomly selects one candidate from the generated set (without PPL scoring) to isolate whether filtering criterion adds value beyond multiple sampling.
3. **Clarify "w/o" conditions** — Explicitly state what the "w/o instruction filtering" baseline uses (e.g., first candidate, random candidate).
4. **Provide full LLM extraction details** — At minimum, specify the base architecture, training data format, and extraction inference procedure.
5. **Reframe weak-model claims** — Describe the comparison as "self-generation vs. cross-generation from another 7B model" rather than "on par with distilling from a more powerful model."
6. **Discuss data quantity effects** — Acknowledge the size confound in Table 1 and provide a matched-size comparison if possible.

## Score and Decision

The paper makes a practical contribution — systematic exploration of semi-supervised instruction generation with two verifiably useful strategies — and the core claim (SASS data outperforms baselines on LongForm) is supported by the results. However, the evaluation lacks statistical rigor, the weak-model comparison is overclaimed, and the LLM extraction component is underspecified to the point of non-reproducibility. These issues are addressable in revision but weaken the paper in its current form.

**Originality**: Moderate. The IG vs. ST comparison is systematic but incremental; the specific strategies (PPL filtering, fragment extraction) are novel in combination.

**Importance**: High. Self-alignment without closed-source models is practically important.

**Claims support**: Moderate. Core results are directionally clear but lack statistical grounding; one claim is overframed.

**Soundness**: Moderate. Methodological gaps (underspecified ablation, missing extraction details) reduce confidence.

**Clarity**: Good. The paper is clearly written and well-structured.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>