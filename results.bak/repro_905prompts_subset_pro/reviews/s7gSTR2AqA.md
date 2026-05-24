Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper investigates whether LLMs exhibit a human-like inductive bias toward Information Bottleneck (IB)-efficient semantic categorization, focusing on the domain of color. The authors conduct two studies: (1) an English color-naming experiment across 39 LLMs, evaluating their IB-efficiency and alignment with human naming systems; and (2) an Iterated In-Context Language Learning (IICLL) paradigm that simulates cultural transmission of artificial color-naming systems, paralleling human iterated learning experiments. The key finding is that LLMs iteratively restructure initially random category systems toward greater IB-efficiency and human alignment across generations of cultural transmission, despite never being trained on the IB objective. Only Gemini 2.0 (among the four tested) recapitulates the full complexity range observed across human languages. A preliminary extension to Shepard circles suggests domain-generality.

## Strengths

- **Novel IICLL paradigm bridges cognitive science and LLM research:** The paper introduces Iterated In-Context Language Learning, a carefully designed paradigm that replicates the experimental conditions of human iterated language learning studies (Xu et al., 2013). This enables a direct, quantitative comparison of LLM inductive biases to human inductive biases — something no prior work has done in the context of semantic efficiency. The evidence is in Sections 3–4.2, where IICLL trajectories (Figure 3) show LLMs restructuring random color-naming systems toward IB-efficient solutions across generations.

- **Comprehensive and rigorous IB-based evaluation across 39 models:** The paper systematically evaluates English color naming in models varying in size, instruction-tuning status, and modality (text vs. image). The results (Figure 2, Appendix E) reveal that only the largest instruction-tuned models achieve high English-alignment and near-optimal complexity-accuracy tradeoffs, while many state-of-the-art models fail — a striking and important finding.

- **Converging evidence that IB-efficiency is an emergent property, not training-data mimicry:** The IICLL experiments, combined with the rotation analysis (Appendix H) and comparison against a baseline feature-based clustering algorithm (Appendix M), provide strong evidence that the emergent IB-efficient structure is non-trivial. The rotation analysis shows that rotating the color-label mapping degrades both efficiency and alignment for Gemini, ruling out the possibility that arbitrary label assignments would produce the observed fit.

- **Well-grounded in cognitive science theory and human data:** The paper directly replicates two influential human experiments (Lindsey & Brown, 2014; Xu et al., 2013) and uses high-quality human behavioral datasets (WCS, human IL) as benchmarks, making the claims about human alignment precise and falsifiable. This is not a paper that invents its own metrics in isolation — it connects to a rich empirical tradition.

- **Careful experimental controls:** The paper systematically varies input modality (text sRGB vs. images vs. CIELAB), constrains generation via log-probability scoring or API controls, and includes analyses of training checkpoints (Olmo 2, Appendix F). These controls reduce confounds and strengthen the validity of cross-model comparisons.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Abstract overstates the uniqueness of Gemini's capability:** The abstract states "only a model with strongest in-context capabilities (Gemini 2.0) is able to recapitulate the wide range of near-optimal IB-tradeoffs observed in humans" without the important hedge "among the models we tested" that appears in the introduction (line 31). Since only four instruction-tuned models were tested in IICLL, and other frontier models might also succeed, the abstract claim is slightly overbroad. This is a wording issue, not a scientific one — easily corrected.

- **The "same fundamental principle" framing is slightly stronger than the evidence directly supports:** The abstract and conclusion state that the emergent systems arise "via the same fundamental principle that underlies semantic efficiency in humans." What the experiments convincingly demonstrate is that LLM-evolved systems *converge toward IB-efficient outcomes that align with human systems*. Whether this is driven by an inductive bias *for the IB objective specifically*, versus a broader pressure toward coherent, compressible structure that happens to correlate with IB optimality, is not resolved. The Discussion appropriately acknowledges this uncertainty ("the precise origins of the bias we observe in LLMs toward efficiency are unclear," line 177), but the framing in the abstract and conclusion could be read as claiming a stronger mechanistic link than is established. This is an evidential nuance that does not require new experiments — more measured language would suffice.

### Trivial

- The Shepard circles section (4.3) is explicitly labeled as preliminary, with only four chains from one model. The paper appropriately hedges these results, but the claim that this "suggests" domain generality would benefit from at least reporting the IB-efficiency of the emergent Shepard circle systems, which the paper defers to future work.

## Nice-to-Haves

- **Quantitative per-language alignment for LLM-WCS comparison:** The paper notes that some LLMs (e.g., Olmo 2 32B inst., Qwen 2.5 VL 7B inst.) produce systems resembling low-resource WCS languages (Appendix Figure 9). Reporting per-language NID alignment rather than only the WCS average would strengthen this intriguing observation.

- **Ablation on number of in-context examples in IICLL:** The paper attributes Gemini's superior performance partly to stronger in-context learning capacity. Varying the number of in-context examples (especially for the high-$k$ conditions) could directly test this hypothesis and define boundary conditions more precisely.

- **IB-efficiency analysis for Shepard circles:** Even a preliminary IB-efficiency computation for the emergent Shepard circle systems would connect this demonstration more tightly to the paper's main thesis.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh critic: "the paper should avoid implying that this capacity is unique to a single model architecture."** REMOVED as a standalone weakness because the paper already hedges this in the introduction with "among the models we tested." The abstract omission of this hedge is captured above as a minor wording issue. The critic's deeper concern about uniqueness is addressed by the existing qualification.

- **Harsh critic: "including a model that performed poorly on the naming task would have been informative as a control."** REMOVED. The paper already notes (line 131 and Appendix L) that smaller models struggle in IICLL to produce non-degenerate category systems. This is scope creep — testing poorly-performing models would not strengthen the central claim about efficiency biases.

- **Strength Finder: "This paper addressed an important problem" or similar generic framings.** REMOVED as generic/superficial — only concrete, evidence-backed strengths are retained above.

- **Harsh critic: suggestion about statistical tests on rotation analysis for all models.** Moved to Nice-to-Haves as the paper already acknowledges the rotation results are "less conclusive for the other models" (line 153).

## Novel Insights

The most striking insight emerging from this work is that the IB-efficiency framework, which was developed to describe *human* semantic systems, can serve as a powerful diagnostic tool for LLM behavior without requiring the models to have been trained on the IB objective. The IICLL paradigm reveals that cultural transmission alone — implemented purely through in-context learning — exerts sufficient pressure to evolve random category systems toward near-optimal IB tradeoffs. This suggests an intriguing convergence: the structure that makes human semantic systems efficient may also emerge from the inductive biases that large transformer models acquire through next-token prediction on human-generated text, even though neither system is explicitly optimized for IB-efficiency. The finding that different LLMs plateau at different complexity levels along the IB bound (Gemini spanning the full human range, others at lower complexity) raises the further question of what architectural or training-data properties control where on the IB frontier a model converges.

## Suggestions

- Add "among the models we tested" to the abstract's claim about Gemini's unique capability.
- Soften the "same fundamental principle" language in the abstract and conclusion to something like "guided by the same structural tendencies toward efficient compression" to better reflect the descriptive (rather than mechanistic) nature of the finding.
- For the Shepard circles, if feasible, compute IB-efficiency of the emergent systems to tie the demonstration to the paper's main thesis, even if only in an appendix.

## Score and Decision

### Calibration anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| z3DMFpaP6m (Entropy of LLMs) | 3.00 | R1 | Substantially weaker — narrow metric proposal, limited validation |
| KLUDshUx2V (Concept Banks) | 3.40 | R1 | Substantially weaker — limited scope and evaluation |
| IqGVIU4rvM (Token Efficiency) | 2.50 | R1 | Substantially weaker — engineering contribution |
| f7aWmxgSN4 (Knowledge Graph) | 3.00 | R1 | Substantially weaker — preliminary findings |
| RC5FPYVQaH (CB-LLM) | 5.75 | R1 | Weaker — limited backbone models, incomplete experiments |
| YFOg1LUGG1 (Hallucination via SCAO) | 5.50 | R1 | Weaker — narrower contribution |
| GXzwq6waYb (Hallucination Detection) | 4.25 | R1 | Weaker — incremental |
| FxNNiUgtfa (Knowledge Capacity) | 7.25 | R1 | Comparable — novel info-theoretic framing, comprehensive experiments, some presentation issues |
| uAFHCZRmXk (Modality Gap) | 8.00 | R1 | Slightly stronger — uniformly high scores, no overclaiming |
| XrsOu4KgDE (Culture-Conditioned) | 7.00 | R2 | Slightly weaker — narrower scope |
| XgH1wfHSX8 (Algorithmic ICL Phases) | 7.50 | R2 | **Most comparable** — novel paradigm, comprehensive, minor framing issues but strong contribution |
| Tn8EQIFIMQ (Arithmetic-GPT) | 7.00 | R2 | Slightly weaker — limited experimental scope |
| WK6K1FMEQ1 (SPACE Benchmark) | 6.75 | R2 | Weaker — methodological concerns, limited models |

**Round 1 bracket:** 6.5–8.5. The paper is clearly above the middle-band reject/weak-accept anchors (3–6 range) and sits among the strong-accept anchors (7–8+ range).

**Round 2 narrowing:** The closest comparable anchor is XgH1wfHSX8 (Algorithmic Phases of ICL, 7.50), which shares key features: a novel experimental paradigm on a synthetic/semi-synthetic task, comprehensive analysis along multiple axes, strong theoretical grounding, and minor framing issues that prompted reviewer pushback. The current paper is slightly cleaner in its claims and has more direct practical relevance. It is comparable to uAFHCZRmXk (8.00) in execution quality but has the mild abstract overstatements noted above. It is clearly stronger than the 7.00 anchors (Tn8EQIFIMQ, XrsOu4KgDE).

**Final score: 7.5.** The paper makes a significant, well-executed contribution at the intersection of cognitive science and LLM research. The IICLL paradigm is genuinely novel, the experiments are thorough and well-controlled, and the findings are striking. The minor framing issues in the abstract are easily addressable and do not undermine the core contribution.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>