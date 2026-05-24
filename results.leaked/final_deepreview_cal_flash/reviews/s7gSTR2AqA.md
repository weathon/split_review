Now I have a thorough understanding of the paper. Let me write the final consolidated review.

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

Let me compose the review carefully, verifying each claim against the paper text.

---

The paper makes a substantial contribution: it introduces IICLL, a novel paradigm for studying cultural transmission in LLMs, and provides evidence that LLMs exhibit an inductive bias toward IB-efficient categorization. The weakest part is the Shepard circles section which lacks quantitative support. The Discussion slightly overstates the generality of the findings. The CIELAB finding is acknowledged but not fully reconciled with the central claim. None of these are fatal.

Scoring: I'll place this at **6.5**, above the Telephone Game anchor (6.0) because the paper is more systematic, theory-driven, and evaluates more models, but below the 8.0-level papers which are more tightly argued and have fewer framing issues.

Now let me write the full review.## Summary

This paper combines the Information Bottleneck (IB) framework for semantic systems with iterated learning to investigate whether LLMs exhibit a human-like inductive bias toward efficient categorization. The authors introduce Iterated In-Context Language Learning (IICLL), a paradigm that simulates cultural transmission in LLMs by having models iteratively learn and transmit pseudo-color-naming systems from random initializations. In a large-scale evaluation spanning 39 models across 6 families, they show that instruction-tuned LLMs restructure random category systems toward greater IB-efficiency and human-alignment, with Gemini 2.0 recapitulating the full range of complexity–accuracy tradeoffs observed across human languages and human iterated learning chains.

## Strengths

1. **IICLL is a novel and well-motivated paradigm for studying inductive biases in LLMs.** The paper bridges cognitive science (iterated language learning, IB principle) with LLM evaluation in a way that goes beyond existing work. The IICLL framework (Section 4.2, Figure 1c) leverages LLM in-context learning to replicate human iterated learning experiments, enabling direct comparison of inductive biases between LLMs and humans.

2. **The core result—that IICLL drives random category systems toward IB-efficiency—is supported by converging quantitative evidence.** Figure 3 shows trajectories of four models converging toward the IB bound on the information plane. Figure 4 provides three complementary metrics (efficiency loss decreasing, IB-alignment increasing, WCS-alignment increasing) over generations, all with 95% confidence intervals. The rotation analysis (Appendix H) confirms that for Gemini, the emergent structure is non-trivially efficient and aligned, and a baseline clustering algorithm (Appendix M) further supports the finding.

3. **The paper carefully controls for the possibility that LLMs merely mimic training data.** The IICLL experiment starts from random partitions of the color space (black dots in Figure 3) and uses pseudo-words never seen in training data (Appendix J). The fact that models reorganize these random systems into near-optimal IB solutions rules out simple memorization of English or other languages in the training corpus.

4. **The English color naming study provides a valuable, large-scale empirical contribution in its own right.** Testing 39 models across 6 families with controlled variation in size, instruction-tuning, and input modality (Table 1, Figure 2c) reveals systematic relationships between model properties and alignment. The finding that instruction-tuning and larger size predict better alignment, while some large models (e.g., Llama 3.3 70B) still struggle, is informative for the field.

5. **Theory-driven quantitative metrics** ground the evaluation in the IB framework (Section 2.2, Equation 1). Using efficiency loss (ε) and Normalized Information Distance (NID) with IB-alignment and WCS-alignment provides a principled bridge between LLM behavior and cognitive science theory.

## Weaknesses

### Fatal
None.

### Major

1. **The Discussion overstates the generality of the central claim.** The final sentence of the Discussion states that "LLMs are capable of evolving perceptually grounded, human-like semantic systems, guided by the same IB-efficiency principle that underlies human languages" without adequately carrying forward the qualification that only Gemini 2.0 recapitulates the full human complexity range. The abstract is carefully qualified ("only a model with strongest in-context capabilities (Gemini 2.0) is able to recapitulate the wide range..."), but the Discussion drops this nuance. Since the core evidence for the strongest form of the claim (spanning the full human complexity range) rests on a single model, the overarching narrative needs to be more consistently tempered.

### Minor

2. **The CIELAB failure (Section 4.1) is acknowledged but not reconciled with the paper's central argument.** The paper finds that "all models, including the best performing ones, struggled to align with English naming when colors are presented in CIELAB" and calls this "a key difference between how LLMs represent color and how humans do." However, because the IB bound itself is computed from CIELAB perceptual distances, this finding creates a tension for the claim that LLMs and humans are guided by "the same fundamental principle." The paper correctly notes the empirical result but does not discuss how this tension should be resolved—e.g., whether the IB principle is an abstract mathematical optimum that can be reached via different routes (text statistics vs. perception), or whether the claim is meant to imply shared cognitive machinery. A brief discussion would strengthen the paper.

3. **The Shepard circles experiment (Section 4.3) lacks quantitative analysis and does not directly support the paper's core claims.** The paper is transparent that this is "initial evidence" and notes that "an important direction for future work is to test whether this emergent structure also supports greater IB-efficiency." But in a results section, qualitative visual inspection of four chains (Figure 5b) provides little evidential weight. Given that the section does not include IB analysis, human comparison, or any quantitative metric, it would be better placed in an appendix or substantially strengthened before inclusion in the main text.

4. **IICLL protocol details are underspecified in the main text.** The paper mentions "84 examples for k=14" in passing (Section 4.2) but does not state the number of in-context examples for each k condition (2–6, 14) or describe how the training set d_{t-1} is sampled from the previous generation's language. These parameters are the key determinants of ICL load and directly affect the interpretation of why some models converge to low-complexity solutions. The paper should state the number of chains per model (appears to be 24 = 6 conditions × 4 replications) and the sampling strategy explicitly in the main text.

5. **No sensitivity analysis of the ICL factors claimed to drive model differences.** The paper attributes the difference between Gemini and the other models to "limited ICL capacity" (Section 4.2) but performs no controlled manipulation of context size, number of in-context examples, or example ordering to test this hypothesis. While this does not invalidate the results, the paper's central explanatory variable (ICL capacity) is not explicitly tested.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis that varies ICL factors (context length, number of shots, example ordering) to substantiate the claim that ICL capacity is the key factor differentiating Gemini from other models.
- Statistical tests comparing whether the final-generation IICLL systems of Gemini are statistically distinguishable in structure from the human IL systems (beyond confidence intervals on aggregate metrics).
- Moving the Shepard circles section to an appendix with the current qualitative presentation, or strengthening it with quantitative IB analysis.

## Removed Points

These points were raised in the source reviews but are removed for the reasons given:

- **"The claim that the IB-efficiency bias is a general property of LLMs is misleading because 3/4 strong models converge to low-complexity solutions."** — This is factually incorrect as a reading of the paper. The abstract explicitly states that "only a model with strongest in-context capabilities (Gemini 2.0) is able to recapitulate the *wide range* of near-optimal IB-tradeoffs" while all models still converge toward IB-efficiency. The core claim is about IB-efficiency as an attractor, not about the full complexity range.
- **"The CIELAB finding shows models and humans reach the optimum via fundamentally different paths, undermining the 'same principle' claim."** — The claim is about an abstract mathematical principle (IB-efficiency), not shared perceptual machinery. The paper acknowledges this difference ("reveals a key difference"). The criticism conflates mechanism with outcome. However, the paper would benefit from a more explicit discussion (kept as Minor #2 above).
- **"Missing experimental details (chains per model, sample size) are critical for evaluating the ICL load claim."** — This is fair and kept as Minor #4, but the harsh critic's framing that this is a serious omission is overstated. The appendix likely contains these details (the parser stripped appendices).
- **"The Shepard circles section should be removed entirely."** — It should be moved to an appendix or strengthened, but a preliminary exploration of domain generality is reasonable and the paper appropriately hedges its claims. Kept as Minor #3.

The following strengths from the Strength Finder were removed because they are generic, conflict with verified weaknesses, or are unsupported:

- **"Domain generality test with Shepard circles"** — The strength finder claimed this as a supporting strength, but the section lacks quantitative metrics, IB analysis, and human comparison. It provides no evidential weight for the paper's core claims. Downgraded; see Minor #3.

## Novel Insights

The key insight that emerges from combining the two reviewer perspectives is that the paper's true contribution is more interesting than either its strongest or weakest framing suggests: the IICLL paradigm reveals that IB-efficiency operates as an *attractor* in LLM cultural evolution, but the basin of attraction differs across models. All tested models move toward the IB bound, yet only Gemini maintains high-complexity solutions. This pattern—where the inductive bias is present across models but only the most capable can sustain the full complexity range—points toward a deeper question about the relationship between in-context learning capacity and the fidelity of cultural transmission that the paper identifies but does not fully explore. The partial convergence of weaker models is itself a meaningful result: it shows IB-efficiency is a robust attractor even when ICL capacity is limited.

## Suggestions

1. **Recalibrate the Discussion to match the evidence.** Replace the blanket "LLMs are capable of evolving..." claim with language that consistently carries forward the qualification from the abstract. For example: "These findings demonstrate that cultural transmission via IICLL can guide LLMs toward IB-efficient semantic systems, with the most capable models (exemplified by Gemini 2.0) spanning the full human complexity range."

2. **Address the CIELAB tension explicitly in the Discussion.** Add a paragraph that explains how the CIELAB finding relates to the core claim—e.g., noting that IB-efficiency is an abstract mathematical property, that LLMs can achieve it via text statistics even without perceptual grounding, and that this convergence (rather than the route) is the shared principle.

3. **Move or strengthen the Shepard circles section.** Either relocate it to an appendix with its current qualitative form, or add quantitative analysis (IB efficiency evaluation, comparison to a null model, or at minimum a quantitative measure of partition compactness) to support the claim of domain generality.

4. **Specify IICLL protocol details in the main text.** Add a sentence stating the number of in-context examples per k value and the sampling procedure for d_{t-1}, to allow readers to assess the ICL demands of each condition without searching the appendix.

5. **Add an ICL sensitivity experiment.** A minimal experiment varying the number of in-context examples or context window length for one of the collapsing models (e.g., Llama 3.3 70B) would directly test whether ICL capacity is the bottleneck, significantly strengthening the paper's central interpretation.

## Score and Decision

**Round 1 (Bracketing):** Three queries across topical similarity retrieved anchors in three bands. The strongest topic match ("When LLMs Play the Telephone Game," avg 6.0) sits in the middle band, while topically related but weaker papers (e.g., "ELCC," avg 4.0) anchor the lower band. The upper band (>7.5) contained papers on different subproblems (training on test task, function vectors) that are not directly comparable in methodology or scope. Based on this, I set the initial bracket to **5.0–7.0**.

**Round 2 (Narrowing):** Two focused queries inside the bracket retrieved "When LLMs Play the Telephone Game" (6.0, scores 3/8/8/5) and "Attributing Culture-Conditioned Generations" (7.0, scores 5/6/8/8/8) as the most topically relevant anchors. Reading both in full:

- **Telephone Game (6.0):** Studies iterated LLM text transmissions but uses a smaller set of models (no Gemini), less theory-driven metrics, and a less diverse evaluation. The current paper is more systematic (39 models vs. ~5), uses cognitively grounded metrics (IB-based), and has direct human comparisons. The current paper is clearly stronger.
- **Attributing Culture-Conditioned Generations (7.0):** Well-executed analysis of cultural biases but limited to one model (OLMo-7B). The current paper tests 39 models and has a novel experimental paradigm (IICLL), giving it broader scope, but it also has more framing issues (overclaiming in Discussion, weak Shepard section). The papers are comparable in overall quality, with the current paper being more ambitious and slightly less polished in its narrative.

**Final score:** The paper is stronger than the 6.0 anchor (more systematic, theory-driven, broader evaluation) and comparable to the 7.0 anchor (both have genuine contributions and identifiable weaknesses). I place it at **6.5**. The core empirical work and IICLL paradigm are valuable contributions. The weaknesses (Discussion overgeneralization, unreconciled CIELAB finding, thin Shepard section) are real but addressable and do not undermine the central results.

**Anchors consulted:**
- `KLUDshUx2V` / 3.40 — Weak anchor; concept bottleneck automation, low topical relevance.
- `z3DMFpaP6m` / 3.00 — Weak anchor; LLM semantic entropy, low relevance.
- `f7aWmxgSN4` / 3.00 — Weak anchor; knowledge graph learning.
- `fN8yLc3eA7` / 6.00 — Round 1&2; Telephone Game (iterated LLM transmissions). Current paper is stronger.
- `Sy8upuD6Bw` / 6.33 — Round 1&2; emergent communication with repair. Different methodology.
- `X8Mhumi52G` / 4.00 — Round 1; emergent language corpus. Current paper is substantially stronger.
- `HC0msxE3sf` / 6.00 — Round 1; signaling game as beta-VAE. Theoretical, less empirical scope.
- `XrsOu4KgDE` / 7.00 — Round 2; culture-conditioned generations. Comparable overall quality.
- `YzXPU3QRnL` / 5.80 — Round 2; ICL with flipped labels. Different focus.
- `I7kpf3mZ4n` / 5.25 — Round 2; meta-out-of-context learning. Synthetic experiments.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>