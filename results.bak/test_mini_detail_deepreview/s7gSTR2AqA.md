Now I have sufficient calibration data. Let me synthesize the final review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths

- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review now.

---

**Final calibration summary:**

**Round 1 bracket** (wide): The paper sits above weak anchors (~3.0–3.4, all rejected) and below the strongest anchors (8.0). Initial bracket: 4.5–7.5.

**Round 2 narrowing**: 
- *Telephone Game* (avg 6.00, accepted): Very similar topic (iterated LLM cultural transmission). Current paper is stronger — 39 models vs. few, stronger theoretical grounding (IB), better controls. Current paper ≈ 0.5 pts stronger → ~6.5.
- *Emergent Communication with Repair* (avg 6.33, accepted): Clean, scoped emergent communication paper. Current paper is more ambitious with broader scope. Comparable quality.
- *CtD* (avg 6.67, accepted): Strong emergent communication paper with clear method contribution. Current paper has broader experiments and more models, but weaker theoretical depth. Slightly below or comparable.
- *Percolation Model* (avg 7.00): Stronger theoretical contribution. Current paper is more empirical with less theoretical depth.

**Final score**: 6.5. The paper makes a substantial empirical contribution with a well-executed multi-experiment design, strong theoretical framing (IB), and novel methodology (IICLL). It sits firmly in the strong-accept range but the main theoretical conclusion is slightly overstated given the human-centric evaluation metric.

---

## Summary

This paper investigates whether LLMs can develop human-aligned semantic categories that are efficient under the Information Bottleneck (IB) principle. Focusing on color categorization, the authors conduct two experiments: (1) an English color-naming study across 39 LLMs from 6 families, showing that larger instruction-tuned models best approximate human-like IB-efficient systems; and (2) Iterated In-Context Language Learning (IICLL), a novel paradigm simulating cultural transmission, showing that LLMs restructure random pseudo-category systems toward greater IB-efficiency. Only Gemini 2.0 recapitulates the full range of near-optimal IB tradeoffs observed in human languages, while other models converge to lower-complexity solutions.

## Strengths

1. **Large-scale systematic evaluation across 39 LLMs, 6 families, varied along size, instruction-tuning, and modality** — This provides robust evidence for the conditions under which human-aligned color categories emerge (Figure 2c). The finding that many state-of-the-art models fail to capture English naming despite massive English training data is striking and novel (lines 101–113).

2. **Novel IICLL paradigm enabling direct comparison to human iterated language learning experiments** — By simulating cultural transmission with pseudo-words and comparing to the human IL data of Xu et al. (2013) on the IB information plane (Figure 3), the paper shows convergence from random starting points toward near-optimal systems, going beyond simple mimicry of training data.

3. **Use of the established IB framework with quantitative, theory-driven metrics** — The IB efficiency loss, NID-based alignment, and comparison to the theoretical IB bound (Zaslavsky et al., 2018) provide a principled evaluation that goes beyond ad-hoc accuracy scores. The metric is applied consistently across LLMs, human languages (WCS), and human IL data.

4. **Well-designed controls** — The rotation analysis (Appendix H, Figure 11) demonstrates non-trivial efficiency for Gemini: random hue rotation significantly decreases efficiency and alignment. A feature-based clustering baseline (Appendix M) provides an additional lower bound. These strengthen the argument that the observed convergence is meaningful.

5. **Intellectually honest framing of limitations** — The paper acknowledges that "the precise origins of the bias we observe in LLMs toward efficiency are unclear" (Section 5), and transparently reports that rotation results are "less conclusive" for non-Gemini models (Section 4.2).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The IB metric is defined relative to human perception (CIELAB Gaussian model), so the central theoretical inference about a "domain-general IB-efficiency principle" is slightly overreaching.** The metric measures how well LLM categories align with an optimal encoding *for human perception*, not for the LLM's own internal representations. The paper's key results — that LLMs produce human-aligned categories that are IB-efficient with respect to human perception — stand on their own and are important. But the claim that LLMs are "guided by the same IB-efficiency principle" (Discussion) conflates human-centric measurement with LLM-internal computation. The IICLL experiment partially mitigates this (random starting points + pseudo-words + convergence suggests a real bias), but the evaluation still uses the human IB model. The paper should more cleanly separate "LLMs produce human-aligned efficient categories" (well-supported) from "LLMs optimize the IB objective as a general principle" (speculative given the current evaluation).

2. **The IICLL paradigm differs from human iterated language learning in important, underexplored ways.** Human ILL involves genuine learning with weight updates over limited training examples; IICLL is a chain of single forward passes with in-context examples. The paper cites Griffiths & Kalish (2007) on Bayesian convergence, but does not verify whether a transformer's in-context behavior satisfies the required conditions (shared likelihood, Bayesian updating). The observed convergence is still informative, but interpreting it as revealing "inductive biases" in the same sense as human IL is somewhat overstated. The paper would benefit from a more explicit discussion of this gap.

3. **The rotation analysis is only conclusive for Gemini; for other models the results are "less conclusive" (as stated).** This limits the non-triviality argument to a single model. While the paper is transparent about this, the theoretical conclusion about "LLMs" more broadly would be stronger if the rotation result held across multiple models.

4. **The Shepard circles experiment (Section 4.3) is purely qualitative** — no IB analysis, no quantitative alignment metric, only one model (Gemini) with one category count (k=4). The paper appropriately frames this as "initial evidence," but it is too thin to contribute substantively to the central claims.

### Trivial

None.

## Nice-to-Haves

- Running a comparison version of the IICLL experiment where the IB efficiency is computed using sRGB-based distances (the representation the LLM actually receives) rather than CIELAB would strengthen the claim about a domain-general compression bias beyond human-alignment.
- Including a model that performs poorly on English naming in the IICLL experiment (as a control) could help disentangle whether convergence to efficient systems requires English-like semantic knowledge or reflects a more general bias.
- A brief discussion connecting the findings back to practical implications (e.g., image generation consistency) would strengthen the applied motivation.

## Removed Points

These points from the input reviews were removed with justification:

- **"Appendix F not visible" / missing appendix content** — Parser issue; rule says to remove.
- **"IICLL results could be an artifact of the prompting strategy"** — Speculative claim without grounding in the paper.
- **"Risk from missing related work"** — The paper already cites the relevant prior work (Ren et al., 2020; Carlsson et al., 2024; Zhu & Griffiths, 2024).
- **Request to compute IB efficiency using the LLM's own embedding space** — This would be a different research question; the paper is explicitly about *human-aligned* categorization, so using the human perceptual IB model is appropriate.
- **"Practical implications not revisited"** — Trivial scope criticism; the paper is not an applied systems paper.
- **Various formatting/presentation nitpicks** — Parser artifacts or reviewer preferences.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a genuinely novel insight not foregrounded by the paper: the asymmetry between models' ability to perform English color naming and their ability to evolve efficient systems in IICLL. The paper notes that Gemini captures the full range while others converge to low-complexity solutions, but an alternative interpretation is that **the IB-efficiency pressure in IICLL is weaker than the training-data imprinting of English** — models that can't reproduce English naming still converge to *some* efficient system (just at lower complexity), suggesting the bias toward efficiency may be separable from the particular semantic content of English. This is hinted at in the finding that some models (Olmo 2 32B, Qwen 2.5 VL 7B) produce systems resembling low-resource WCS languages rather than English (Section 4.1). If weaker IICLL models converge to structurally different but still IB-efficient systems, it would suggest the bias is toward *some* efficient partition rather than toward the *English* partition specifically, which is a more nuanced claim than the paper currently makes.

## Suggestions

1. **Sharpen the theoretical framing**: Replace "guided by the same IB-efficiency principle" (Discussion) with more precise language such as "LLMs produce categories that, when evaluated against a human perceptual model, achieve near-optimal IB tradeoffs — suggesting that their representational biases overlap with the human drive for efficient categorization." This is equally strong as a finding but more precise.

2. **Add a limitations paragraph on IICLL methodology**: Explicitly discuss that IICLL involves prompting rather than weight updates, and that the Bayesian convergence theorem (Griffiths & Kalish, 2007) may not directly apply to in-context learning. This would preempt the main methodological concern.

3. **Quantify the non-Gemini rotation results**: Even if "less conclusive," report effect sizes or confidence intervals for the other models' rotation analyses rather than leaving them qualitatively described.

4. **Strengthen the Shepard circles experiment** with at least a simple IB alignment metric or remove it — in its current form it adds little.

## Score and Decision

**Calibration details**: 

Round 1 bracketing placed the paper between weak anchors (~3.0–3.4) and strong anchors (8.0). Round 2 narrowing compared against:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| When LLMs Play the Telephone Game (fN8yLc3eA7) | 6.00 | R2 | Very similar topic (iterated LLM cultural transmission). Current paper is stronger: 39 models vs. few, stronger theoretical grounding (IB), better controls. Current paper ≈ 0.5 pts above. |
| Emergent Communication with Repair (Sy8upuD6Bw) | 6.33 | R2 | Clean, well-scoped emergent communication paper. Current paper is more ambitious with broader experiments. Comparable quality. |
| CtD: Composition through Decomposition (KlalQu2423) | 6.67 | R2 | Strong method paper in emergent communication. Current paper has broader model coverage and multiple experiments but less methodological depth. Slightly below or comparable. |
| Percolation Model of Emergence (0pLCDJVVRD) | 7.00 | R2 | Stronger theoretical contribution. Current paper is more empirical. Below this anchor. |

Score positioned relative to round-2 anchors: above Telephone Game (6.00), comparable to CtD (6.67) and below Percolation Model (7.00).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>