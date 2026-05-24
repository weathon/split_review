## Summary

This paper investigates whether LLMs exhibit human-like inductive biases toward IB-efficient semantic categorization, using color naming as a testbed. Across 39 models, the authors conduct (1) an English color-naming study showing that larger instruction-tuned models approximate English naming and IB-efficiency, and (2) an Iterated In-Context Language Learning (IICLL) study that simulates cultural transmission of artificial color-naming systems. The key finding is that Gemini 2.0's IICLL trajectories converge to the same range of near-optimal IB solutions as human languages and human iterated-learning chains, while other state-of-the-art models converge to low-complexity solutions. The paper combines cognitive theory (Information Bottleneck principle, iterated learning) with a novel LLM adaptation (IICLL), providing a template for studying semantic category acquisition in LLMs.

## Strengths

- **IICLL recapitulates human cultural evolution on the information plane (Figure 3).** Gemini 2.0's IICLL trajectories converge to the same range of near-optimal IB solutions as both the World Color Survey languages and the human iterated-learning chains from Xu et al. (2013). This is the central quantitative evidence that emergent category systems from IICLL are both efficient and human-aligned, going beyond simple mimicry of training data.

- **Quantitative improvement over generations with 95% confidence intervals (Figure 4).** Across IICLL generations, efficiency loss decreases, IB-Alignment increases, and WCS-Alignment increases for all four models tested. Improvements occur rapidly (within ~4 generations), paralleling human iterated-learning dynamics, and Gemini even surpasses the human IL baseline on some metrics.

- **Rotation analysis confirms non-trivial structure (Appendix H).** Rotating the label mapping along the hue dimension significantly degrades both efficiency and alignment for Gemini, ruling out the possibility that emergent systems are simple or arbitrary. This provides a direct statistical test that the structure is genuinely aligned with the perceptual space and human naming patterns, and is complemented by a feature-based clustering baseline (Appendix M).

- **Systematic model comparison across 39 models (Figure 2).** The paper tests models from six families (Gemini, Gemma, Llama, Qwen, Olmo, GPT-2) with varying size, instruction-tuning, and modality. The finding that many state-of-the-art models fail to capture English color naming, while larger instruction-tuned models succeed, is a striking result that makes the IICLL findings more compelling by establishing a clear foundation.

- **Clear theoretical grounding and methodological transparency.** The paper bridges cognitive science (IB principle, iterated learning) and NLP evaluation in a way that is principled, well-motivated, and replicable. The honest discussion of the capacity confound in IICLL and the limitations of the Shepard circles experiment reflects thoughtful scholarship.

## Weaknesses

### Major

- **The IICLL efficiency bias is partially confounded with in-context learning capacity.** The paper's central claim is that LLMs exhibit an "inductive bias toward IB-efficiency" because IICLL trajectories converge toward the IB bound. However, for three of the four main models (Gemma 3 27B, Llama 3.3 70B, Qwen 2.5 32B), the trajectories converge at low complexity (≤~3 bits). The paper notes that in high-load conditions (e.g., k=14 with 84 in-context examples), these models "immediately converge to low-complexity solutions." This pattern is equally consistent with a simpler explanation: these models cannot integrate many in-context examples and default to broad categories that happen to score well on IB efficiency. The human IL chains (Xu et al., 2013) do not face this constraint because participants were trained on example sets before labeling the full space, making the comparison asymmetrical. The authors acknowledge this confound in Section 4.2 but do not resolve it — e.g., by systematically varying context size to show convergence is robust, or by demonstrating that even in low-complexity conditions (k=2,3) the non-Gemini models converge to IB-efficient solutions that are non-trivial (i.e., not the simplest possible partition). This interpretive ambiguity weakens the strongest claim about a domain-general inductive bias.

### Minor

- **Input modality for Gemini in the IICLL color experiment is not clearly specified.** For the English naming study, the paper states that multimodal models received images of color chips (Section 3). For IICLL, the paper says models were given "no indication that the stimuli are in fact colors, only that they have 'features'" (Section 4.2). It is unclear whether Gemini received images or text (sRGB coordinates) in the IICLL color condition. If it received images, it could infer the stimuli are colors, weakening the domain-agnostic claim. If it received text, its multimodal capabilities were unused. This matters for interpreting the comparison with Shepard circles (which used images) and should be stated explicitly in the main text.

- **The "low-resource language" claim about Olmo and Qwen (Section 4.1) lacks quantitative verification.** The paper states that some models produced systems "resembling... other, very low-resource languages from the WCS" and cites Figure 9 in Appendix E. This is an intriguing observation that would benefit from quantitative support: computing NID between the LLM system and every WCS language and reporting the best match(es). As presented, the claim is supported only by visual inspection of mode maps.

- **Number of IICLL chains per condition is not reported.** The paper describes "average across initializations and conditions" (Figure 4) and shows trajectories for k ∈ {2,3,4,5,6,14}, but does not explicitly state how many chains were run per model per k value. The confidence intervals in Figure 4 depend on this; knowing the sample size would help assess reliability.

- **The IB bound is derived from human-perceptual assumptions; the paper could more clearly distinguish alignment from mechanism.** The evaluation uses an IB bound computed from CIELAB space with Gaussian perceptual noise (the human model), yet LLMs perform worse with CIELAB than sRGB inputs (Appendix E), indicating they do not share human perceptual geometry. The paper's language sometimes slips from "these systems achieve near-optimal IB tradeoffs relative to the human model" to suggesting the models are "guided by the IB principle itself." The rotation analysis tests alignment, not mechanism, and the paper would benefit from a consistent terminological distinction.

### Trivial

None.

## Nice-to-Haves

- **Expand the Shepard circles experiment.** Section 4.3 tests only one model (Gemini), one condition (k=4), with no quantitative evaluation. If the domain-generality claim is to be retained in the abstract, this experiment should include multiple models, conditions, and quantitative efficiency/alignment measures. Alternatively, relegate it to a speculative future direction and soften the abstract accordingly.

- **Add a random-walk baseline for IICLL trajectories.** A null model where labels are randomly shuffled at each generation would provide a stronger statistical benchmark for whether convergence is faster than chance, complementing the rotation analysis.

- **Test whether the IB-efficiency trend in IICLL is robust to varying the number of in-context examples per generation** (beyond the fixed proportion used), to directly disentangle capacity from bias.

## Removed Points

These points were flagged for removal; treat them with caution:
- The harsh critic's argument about the Shepard circles being "too preliminary to support domain-generality" — retained but downgraded to Nice-to-Have; the paper appropriately calls this "initial evidence" and a "preliminary investigation," so the abstract's "potentially" qualifier is appropriate and not overclaimed.
- Request for statistical comparison between IICLL trajectories and random-walk baseline — moved to Nice-to-Have; a reasonable suggestion but not a flaw in the current paper.
- Concerns about prompt wording effects on IICLL outcomes — speculative; the paper's use of pseudo-labels follows the human experiment design closely.

## Novel Insights

The most interesting finding that goes beyond the paper's own framing is the stark asymmetry between the English naming task and the IICLL task. In English naming, multiple models (Gemini, Gemma, Llama, Qwen) achieve reasonable alignment. But in IICLL, only Gemini recapitulates the full complexity range of human languages, while the others collapse to low complexity. This suggests that what distinguishes these models is not their "knowledge" of color categories (which they all have from training data) but rather their *in-context generalization capacity* — the ability to integrate dozens of examples into a coherent structured system that generalizes across a large stimulus space. This points toward a more nuanced conclusion: the inductive bias for IB-efficiency may be latent in all sufficiently trained LLMs, but only models with strong ICL abilities can *express* it through cultural transmission. The bottleneck may be not in the bias itself but in the computational capacity to deploy it under the constraints of ICL.

## Suggestions

- Clarify the input modality used for Gemini in the IICLL color experiment (text vs. images) and discuss any implications for the domain-agnostic interpretation.
- Add a quantitative verification of the "low-resource language" claim by computing the best WCS match(es) for the relevant models' systems.
- Report the number of IICLL chains per condition per model explicitly.
- Add a control analysis that varies the number of in-context examples per generation to separate ICL capacity from the efficiency bias.
- Soften or expand the Shepard circles section — either add quantitative measures and more conditions, or relegate it to future work.

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Three queries on topics similar to this paper (color naming in LLMs, iterated learning, IB efficiency):
- Low band (< 3.5): Color naming in VLMs papers (avg ~2.0–3.0) — much narrower scope, no cognitive theory grounding.
- Middle band (3.5–7.5): "Is In-Context Learning Learning?" (4.80), "Iterative Amortized Inference" (6.00), "A Closer Look at ICL" (4.00).
- High band (> 7.5): Papers on multi-turn conversations, embodied navigation, transducing LMs — different topics, not directly comparable.

Initial bracket: 5.5–7.0.

**Round 2 — Narrowing.** Two queries targeting the 5.5–7.5 and 6.0–7.5 ranges with topical overlap (IB, semantic categories, LLM cognition):
- "From Tokens to Thoughts" (6.00) — Similar IB + LLM categorization topic. The current paper is stronger in experimental rigor, has a novel method (IICLL), uses human behavioral baselines rather than just embeddings, and has cleaner causal framing. Current paper is clearly better.
- "Cognitive models can reveal interpretable value trade-offs in language models" (7.00, scores: 4,8,8,8) — Interdisciplinary cognitive science + LLMs. Comparable ambition and interdisciplinary grounding. Current paper has stronger quantitative evaluation but less polished presentation of the generalization experiment.
- "Trained on Tokens, Calibrated on Concepts" (6.50, scores: 4,8,6,8) — Theoretical + empirical paper on LLM calibration. Current paper is comparable in quality but faces a more substantive unresolved confound (capacity vs. bias).
- "Language and Experience" (6.40) — Social learning framework with LLMs. Current paper has clearer experimental paradigm and more direct comparisons.

The current paper sits between 6.00 and 7.00. It is clearly stronger than "From Tokens to Thoughts" (6.00) in experimental design, novelty, and grounding. It is comparable to but slightly below "Cognitive models..." (7.00) due to the unresolved capacity confound and the thin Shepard experiment. The most appropriate position is 6.5.

**Final score: 6.5**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| mnfqJQSd6B | 2.00 | 1 | Narrower scope, no IB/iterated learning theory |
| crjpuxuvs6 | 3.00 | 1 | Different task (Stroop test), less theoretical depth |
| Zn18gRDxhF | 2.00 | 1 | Different task (color blindness), no cognitive theory |
| 1qLZsyJN2t | 2.00 | 1 | Different task (information game), unrelated |
| bIS0BbYjjd | 4.80 | 1 | ICL analysis but no cognitive theory; less novel |
| YKxiut90ju | 5.00 | 1 | ICL representation study; less ambitious |
| O40rfqDGm4 | 4.00 | 1 | ICL classification study; narrower scope |
| K8HpllWwE1 | 6.00 | 1 | Amortized inference framework; different topic |
| rkthPeHvAX | 6.00 | 2 | IB + LLM categorization but weaker experiments; current paper is stronger |
| cCIdxLoLJ5 | 5.60 | 2 | IB of CoT; different topic |
| 0sCyk9Tr5J | 6.50 | 2 | Semantic calibration; comparable quality |
| 11kPIEkj75 | 6.00 | 2 | Hallucination detection; different topic |
| SRn1MtMPRq | 5.00 | 2 | Multi-agent coordination; different topic |
| UxDu3RFuDV | 6.40 | 2 | Social learning; comparable quality |
| VCjlm003WL | 7.00 | 2 | Pattern matching; different topic |
| nM2QhvybwI | 7.00 | 2 | Cognitive models + LLM values; comparable interdisciplinary ambition; current paper slightly weaker on one dimension |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>