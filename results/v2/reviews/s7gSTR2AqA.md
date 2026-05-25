Now I have sufficient calibration data. Let me synthesize the final review.

---

## Summary

This paper investigates whether LLMs exhibit a human-like inductive bias toward Information Bottleneck (IB) efficiency in semantic categorization. The authors conduct two studies in the color domain: (1) an English color-naming experiment across 39 LLMs, finding that larger instruction-tuned models achieve better alignment with English and IB-efficiency, and (2) an Iterated In-Context Language Learning (IICLL) experiment on 4 high-performing models, showing that over generations initially random category systems converge toward the IB bound. Only Gemini 2.0 recapitulates the full complexity range of human languages; the other three converge to lower-complexity solutions. A preliminary Shepard circles experiment suggests possible domain generality.

## Strengths

1. **Large-scale, systematic evaluation of color naming across 39 LLMs from 6 families (Figure 2).** The paper tests models varying in size, training stage (pre-trained vs. instruction-tuned), and modality (text-only vs. multimodal), providing the most comprehensive LLM color-naming assessment to date. The finding that many state-of-the-art models fail to align with English, while larger instruction-tuned models succeed, is a clear and useful empirical result.

2. **Introduction of IICLL and demonstration of convergence toward the IB bound (Figures 3, 4).** Adapting iterated language learning to LLMs is a creative methodological contribution. The result that IICLL chains from all four tested models move toward IB-efficient solutions provides experimental evidence linking LLM behavior to a principle that organizes human semantic systems. The convergence is particularly striking for Gemini 2.0, which recapitulates the full complexity range observed across human languages.

3. **Rotation analysis (Appendix H, Figure 11) confirms non-trivial structure in Gemini's emergent systems.** Randomizing the hue mapping of evolved systems significantly decreases both IB-efficiency and human alignment for Gemini, showing that the observed structure is not an artifact of random fluctuation or a trivial property of any partition.

## Weaknesses

### Major

1. **The central claim that LLMs exhibit a "human-like inductive bias toward IB-efficiency" is not adequately separated from the training data confound.** The IICLL experiment shows that LLMs restructure random systems toward the IB bound, but an equally parsimonious explanation is that the models draw on training data statistics of human languages (which are themselves IB-efficient). The paper uses pseudo words and does not tell the model the stimuli are colors, which helps, but this does not rule out the model generalizing from category structures seen in training. The rotation analysis (the main control) is only conclusive for Gemini 2.0 — the paper itself states results are "less conclusive for the other models." A direct control condition (e.g., testing whether a model trained on non-IB-efficient distributions also converges to IB efficiency) would be needed to substantiate the strongest version of the claim. Without it, "mimicking training data statistics" and "abstract inductive bias" remain confounded.

2. **The IICLL framework's theoretical grounding for eliciting inductive biases in LLMs is not formally established.** The paper invokes Griffiths & Kalish (2007) — where IL converges to the prior under Bayesian assumptions — but LLMs are not Bayesian learners. The paper does not provide a formal argument or empirical validation that the IICLL chain's stationary distribution corresponds to the model's prior over category systems. While IICLL is a reasonable adaptation, the interpretive leap from "IICLL produces IB-efficient systems" to "LLMs possess an inductive bias for IB-efficiency" goes beyond what is demonstrated. The paper would benefit from an explicit acknowledgment of this gap and, ideally, from measuring the model's one-shot prior (e.g., prompting the model to generate systems from scratch) to compare with IICLL outcomes.

3. **The IB-efficiency evaluation mixes human perceptual geometry with LLM input representations.** The IB bound used to compute efficiency loss was derived using CIELAB distances and Gaussian belief states optimized for human perception (Zaslavsky et al., 2018). Text-only LLMs receive sRGB coordinates, and the paper shows that switching to CIELAB actually *worsens* alignment. This means the near-optimal efficiency the models achieve is measured against a bound computed in a perceptual space the models demonstrably do not share. The finding that models map sRGB to human-aligned categories is interesting in its own right, but the IB-efficiency framing as evidence for a shared principle is weakened by this mismatch. The paper should discuss this limitation more directly and consider evaluating against bounds computed under alternative similarity spaces.

### Minor

4. **The Shepard circles experiment (Section 4.3) is too thin to support domain-generality claims.** Only one model (Gemini), one k value (4), no quantitative IB-efficiency evaluation, no comparison to human data or random baselines. The paper appropriately calls this "preliminary" and "initial evidence," but including it among the main contributions in the abstract and introduction invites over-interpretation. Either quantitative evidence or relocation to an appendix with a caveat would be appropriate.

5. **IICLL results are fully conclusive for only one model (Gemini 2.0).** Of the four models tested, only Gemini captures the full complexity range. The other three converge to low-complexity solutions, and the rotation analysis is inconclusive for them. This limits the generality of the central claim. The narrative would benefit from more precise language about which findings hold for which models.

6. **No statistical significance testing for generation-over-generation trends.** The paper shows trajectories with 95% confidence intervals but does not report whether the improvements in efficiency loss, IB-alignment, or WCS-alignment are statistically significant (e.g., via permutation tests or mixed-effects models). Given the modest number of chains, this matters for assessing reliability.

7. **Only instruction-tuned models that already perform well on English naming are tested in IICLL.** While the paper acknowledges this selection and shows that smaller models struggle (Appendix L), the possibility that the observed behavior is an artifact of instruction-tuning rather than a fundamental LLM property is not resolved. Testing a large base model (even one that fails the English naming task) would clarify this.

### Trivial

8. The abstract and introduction use phrasing that conflates correlation with causation ("the same fundamental principle that underlies semantic efficiency in humans"—the paper shows correlation with the IB bound, not that the IB principle drives LLM behavior). The discussion should more carefully separate observation from interpretation.

## Nice-to-Haves

- A control condition testing IICLL on a domain clearly absent from training data (e.g., a synthetic feature space with arbitrary geometry) with quantitative evaluation.
- Direct measurement of the model's one-shot prior over category systems (generate from scratch, no iteration) for comparison with IICLL outcomes.
- Testing at least one large base model (not instruction-tuned) in IICLL to assess whether instruction-tuning is necessary for the effect.
- Cross-dataset validation using non-WCS color stimuli.

## Removed Points

*Removed: "IICLL requires strong ICL which may explain differences"* — The paper explicitly acknowledges this ("the IICLL task requires very strong in-context learning") and discusses it as a factor. This is a valid observation, not a weakness the paper ignores.

*Removed: "Paper should state whether IB bounds are recomputed or taken from prior work"* — The paper states "we use the previously published IB color naming model from Zaslavsky et al. (2018)" and shows a reproduction of their bound. This is sufficiently clear.

*Removed: "NID may not be proper when k differs significantly"* — NID (based on variation of information) is a standard clustering comparison metric that handles different numbers of clusters. The paper follows established methodology from Zaslavsky et al. (2018). No evidence of a problem is provided.

*Removed: "The CIELAB finding is not analyzed further"* — The paper does discuss it: "This reveals a key difference between how LLMs represent color and how humans do." A fuller analysis would be nice but its absence is not a weakness given the paper's scope.

*Removed: "Missing models in IICLL — test smaller models"* — The paper includes Appendix L on this and acknowledges the limitation. The critic suggests testing more models in IICLL, which is scope expansion, not a flaw.

*Removed from Strengths: Overly generic or conditional praise* — Some strength-finder points were filtered per instructions (e.g., those praising general problem importance without specific paper evidence).

## Novel Insights

The key novel observation is that iterated in-context learning with LLMs (IICLL) produces convergence toward near-optimal IB tradeoffs in color categorization, mirroring human iterated language learning dynamics. This is particularly striking because the models receive no feedback and use pseudo-words — the structure emerges purely from transmission through the LLM's learned representations. The finding that only the strongest in-context learner (Gemini) recaptures the full human complexity range, while other capable models collapse to low complexity, is a noteworthy and non-obvious result that raises questions about what specific model properties (scale, instruction-tuning quality, ICL capacity) enable this behavior. The English naming study's finding that many current LLMs fail to align with a seemingly simple perceptual task is also a practically useful contribution.

## Suggestions

1. **Tone down the "inductive bias" language** in favor of more precise descriptions of what the experiments show: IICLL produces convergence toward IB-efficient systems that align with human languages. Reserve "inductive bias" claims for cases where the training data confound is explicitly controlled.

2. **Add a control experiment** where IICLL chains are seeded with non-IB-efficient systems (e.g., shuffled human systems) to test whether the model actively pushes toward the bound from any starting point.

3. **Quantify the Shepard circles result** or move it to an appendix. A simple quantitative measure (e.g., category compactness, entropy, or alignment with optimal partitions) would substantially strengthen the domain-generality claim.

4. **Report permutation tests** for the generation-over-generation trends in Figure 4 to establish statistical significance.

5. **Explicitly discuss the sRGB/CIELAB mismatch** as a limitation in the main text, not just as a finding about model behavior. Acknowledge that the IB bound used may not be the appropriate reference for models operating on sRGB input.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>