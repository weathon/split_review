Now I have a solid calibration picture. Let me compile the final review.

**Round 1 bracket:** 6.0 – 8.0 (the paper is clearly stronger than the telephone game paper at 6.00 but not quite at the 8.00 level of analytically tight papers).

**Round 2 narrowing:** Compared against Tn8EQIFIMQ (7.00) and VEqPDZIDAh (7.25), this paper is comparable — it has a richer theoretical framework (IB) and a more novel paradigm (IICLL), but the central interpretive claim faces a similar level of scrutiny about alternative explanations. I place it near **7.0**.

---

## Summary

This paper investigates whether LLMs possess a human-like inductive bias toward Information Bottleneck (IB)-efficient categorization. The authors conduct two studies in the color domain: (1) an English color-naming experiment across 39 LLMs evaluating IB-efficiency and human alignment, and (2) an Iterated In-Context Language Learning (IICLL) paradigm that simulates cultural transmission of artificial color-naming systems. The results show that larger instruction-tuned models approach English-like color naming, and in IICLL, LLMs (especially Gemini 2.0) iteratively restructure initially random category systems toward near-optimal IB tradeoffs that mirror the range observed across human languages and human iterated-learning experiments. A preliminary extension to Shepard circles suggests domain-generality of the approach.

## Strengths

- **Novel experimental paradigm (IICLL).** The paper introduces Iterated In-Context Language Learning, extending Zhu & Griffiths (2024)'s iterated in-context learning to the domain of language learning with pseudo-terms. This paradigm cleanly adapts the human iterated-learning experimental design to LLMs, enabling direct comparison of inductive biases between humans and models (Section 2.3, Figures 3–4).

- **Comprehensive and systematic model sweep.** The English naming study evaluates 39 models across 6 families (Gemini, Gemma, Llama, Qwen, Olmo, GPT-2), varying size, instruction-tuning status, and input modality (text vs. image). This reveals clear scaling trends: larger instruction-tuned models achieve higher English-alignment and IB-efficiency (Figure 2, Section 4.1).

- **Rich theoretical grounding in the IB framework.** The paper builds on Zaslavsky et al. (2018)'s IB model of semantic systems, providing a principled quantitative framework for evaluating both human languages (WCS, English) and LLM outputs on the same complexity-accuracy plane. The use of efficiency loss, IB-alignment, and WCS-alignment as converging metrics strengthens the results (Section 2.2, Figures 3–4).

- **Direct comparison with human behavioral benchmarks.** By plotting LLM IICLL trajectories against WCS languages, English naming, and human IL data on the information plane, the paper provides a precise quantitative link between model behavior and decades of cognitive science research (Figures 3, 4b–c).

- **Rotation analysis confirms sensitivity to genuine color structure.** Rotating the label-to-color mapping along the hue dimension significantly degrades efficiency and alignment for Gemini, ruling out trivial clustering and demonstrating that the emergent systems reflect structured, non-arbitrary categorization (Section 4.2, Appendix H).

- **Training-checkpoint analysis reveals the role of instruction-tuning.** The analysis of Olmo 2 across training stages shows that English-alignment improves primarily during instruction-tuning, not pretraining, providing causal evidence for how alignment emerges (Section 4.1, Appendix F).

## Weaknesses

### Fatal

None.

### Major

- **The central interpretive claim faces a residual alternative explanation.** The paper argues that LLMs exhibit a "human-like inductive bias toward IB-efficiency" — that the IICLL paradigm reveals an endogenous compression bias rather than merely reflecting color-similarity structure acquired during pre-training. The evidence is substantial (pseudo-terms, random initializations, rotation analysis, clustering baseline in Appendix M), but the gap between "LLMs converge to IB-efficient systems in IICLL" and "LLMs have an intrinsic bias toward compression" is not fully closed. A reader could reasonably argue that LLMs leverage pre-learned color similarity (itself IB-efficient because human language is) and that IICLL's iterative dynamics simply surface this pre-existing structure rather than revealing a separate inductive bias. The baseline in Appendix M partially addresses this but is only mentioned in one sentence of the main text (line 153). This does not invalidate the results — which are independently interesting — but it means the paper's strongest interpretive claim requires additional support or more careful qualification.

### Minor

- **IICLL design details are deferred to the appendix.** The main text does not summarize key protocol parameters (number of in-context examples per generation, sampling strategy, temperature), referencing Appendix G instead (line 137). While the appendix exists in the full submission, a brief summary in the main text would improve self-contained readability and allow readers to assess the design without cross-referencing.

- **Only four models tested in IICLL.** The choice is explicitly justified — "We considered only large, instruction tuned models that performed well in the English color naming task" (line 136) — and is reasonable. However, given the paper's claim about the generality of the efficiency bias, testing a broader set of models (including some that performed poorly on English naming) could have strengthened or qualified the finding.

- **The Shepard circles extension is preliminary.** The paper appropriately labels this as "initial evidence" (Section 4.3). The results are suggestive but limited to one model (Gemini) and one category-size condition (k=4), and IB-efficiency is not evaluated in this domain. The claims are appropriately cautious.

### Trivial

- The paper uses 12 IICLL generations while Xu et al. (2013) used 13; this minor difference in chain length does not affect the substantive comparison but could be noted.

## Nice-to-Haves

- A main-text presentation of the clustering baseline (currently Appendix M) would directly address the alternative-explanation concern at the point where readers are most likely to raise it.
- Measuring chain-level statistics (auto-correlation, distance to a stationary distribution) would strengthen the link to the Bayesian IL framework and the interpretation of IICLL as recovering a model's implicit prior.
- Extending the rotation analysis to all four IICLL models would clarify whether sensitivity to genuine color structure is a general property or unique to Gemini.

## Removed Points

These points are flagged as removed; treat them with caution.

- **"No baseline that decouples LLM's pre-existing color knowledge from iterative dynamics."** The paper does include a baseline (feature-based clustering, Appendix M, referenced at line 153). This criticism is factually inaccurate.
- **"The paper does not discuss the implications of the CIELAB/sRGB discrepancy."** The paper explicitly discusses this: "we tested the impact of using CIELAB coordinates instead of sRGB… we find that all models… struggled… This reveals a key difference between how LLMs represent color and how humans do" (lines 127–129). The paper not only discusses the issue but frames it as a finding. This criticism is factually wrong.
- **"The paper would benefit from reporting variability across multiple prompt draws."** The paper reports 95% confidence intervals across chains and conditions (Figure 4). This criticism is already addressed.
- **"The comparison to human IL data should align generation counts (12 vs. 13)."** The paper compares final-generation systems, not per-generation trajectories, making the exact chain length irrelevant. This is a nitpick without substance.
- **"The paper should acknowledge that the tested models are heavily shaped by English training data."** The paper studies this explicitly — the entire English naming experiment (Section 4.1) is about evaluating models against English, and the paper notes that "a surprising number of state-of-the-art models fail to capture the English color naming system" (line 31).

## Novel Insights

The most genuinely novel insight emerging from this synthesis is that the IICLL paradigm may serve as a general method for eliciting implicit categorization biases from LLMs, independent of the specific categories they were trained on. The fact that models using pseudo-terms and uninformed about the stimulus domain (told only they have "features") still converge toward human-aligned, efficient systems suggests that IICLL could be applied as a diagnostic tool across semantic domains — potentially revealing whether LLMs have internalized the structural principles that govern human semantic organization, rather than just surface statistical patterns. This methodological contribution may prove more durable than the specific color-domain findings.

## Suggestions

- Bring the clustering baseline (Appendix M) into the main text, even in abbreviated form. This would directly address the most significant interpretive concern at the point where readers are evaluating the central claim.
- Add a brief summary of IICLL protocol parameters in Section 4.2 (e.g., "each generation used N in-context examples sampled from the previous generation's system, with temperature T").
- Consider adding a paragraph discussing what it would mean for the IICLL results if LLMs' efficiency bias originates entirely from pre-training on efficient human languages — this framing distinction (learned vs. intrinsic bias) matters for the paper's theoretical contribution and could be addressed through discussion rather than additional experiments.

---

### Calibration Report

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| KLUDshUx2V | 3.40 | 1 (low) | LLM concept banks — rejected with limited novelty; this paper is far stronger |
| fN8yLc3eA7 | 6.00 | 1 (mid), 2 | LLM telephone game — iterated transmission but simpler design; this paper is clearly better |
| Sy8upuD6Bw | 6.33 | 1 (mid), 2 | Emergent communication with repair — narrower scope; this paper is stronger |
| 7LGmXXZXtP | 6.67 | 2 | Political stereotypes in LLMs — single context; this paper has richer theoretical grounding |
| Tn8EQIFIMQ | 7.00 | 2 | Arithmetic-GPT as cognitive model — comparable creativity but narrower scope; this paper is similar in quality |
| VEqPDZIDAh | 7.25 | 2 | Multilingual trolley problems — large-scale evaluation; this paper has a more novel paradigm contribution |
| uAFHCZRmXk | 8.00 | 1 (high) | Modality gap analysis — tighter analytical contribution; this paper is below this level |

Bracket from Round 1: 6.0–8.0. Round 2 narrowed this to approximately 6.67–7.25, with the paper sitting near the upper-middle of this range due to its combination of a novel paradigm, rich theoretical framework, comprehensive experiments, and strong empirical results, tempered by the interpretive gap around the "inductive bias" claim.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>