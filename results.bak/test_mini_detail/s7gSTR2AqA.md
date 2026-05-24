## Summary

This paper investigates whether large language models exhibit a human-like inductive bias toward Information Bottleneck (IB) efficiency in categorization, using color naming as a primary testbed. The authors conduct two studies: an English color-naming experiment across 39 LLMs (finding that only larger instruction-tuned models approximate English naming), and an Iterated In-Context Language Learning (IICLL) paradigm that simulates cultural transmission of artificial category systems. The main finding is that LLMs restructure random initial systems toward greater IB-efficiency across generations, with Gemini 2.0 recapitulating the full range of near-optimal IB tradeoffs observed across human languages, while other frontier models converge to low-complexity but still IB-efficient solutions. The paper provides initial evidence for domain generality via Shepard circles.

## Strengths

1. **Comprehensive and well-designed empirical study across 39 models.** The English color-naming evaluation (Figure 2) systematically varies model family, size, and instruction-tuning, providing clear evidence that only larger instruction-tuned models approach English-aligned color categories. The inclusion of Olmo training checkpoints (Appendix F) further strengthens the causal claim about instruction-tuning's role.

2. **IICLL paradigm is a thoughtful adaptation of human iterated learning to LLMs.** The experimental design closely mirrors the human study of Xu et al. (2013), enabling a direct behavioral comparison. The results (Figures 3–4) convincingly show that over generations, all four tested LLMs restructure random category systems toward greater IB-efficiency, increasing alignment with both optimal IB systems and human WCS languages. This is the paper's strongest contribution.

3. **Rotation analysis (Appendix H) and baseline comparisons (Appendix M) provide empirical validation** that the emergent systems are non-trivially efficient. The finding that rotating the color-label mapping significantly decreases efficiency and alignment for Gemini, and that emergent systems outperform a clustering baseline, supports the claim that the bias toward IB-efficiency is genuine rather than a trivial artifact of the setup.

4. **Intellectually honest presentation of scope.** The paper explicitly acknowledges that only Gemini 2.0 recapitulates the full human range of IB tradeoffs (abstract, Section 4.2), that the Shepard circles result is preliminary (Section 4.3), and that the precise origins of the efficiency bias in LLMs are unclear (Discussion). This candor is a strength.

## Weaknesses

### Major

1. **The theoretical link between IICLL and "inductive bias" is under-justified for LLMs.** The paper invokes the Bayesian iterated learning result (Griffiths & Kalish, 2007) which states that under certain conditions, IL chains converge to the learners' prior. However, the paper does not argue that LLMs—which perform in-context learning via forward passes on prompts, not Bayesian inference over hypotheses—satisfy these conditions. The paper states that IICLL "enables a direct comparison to LLMs of their respective inductive biases" (Section 2.3) without bridging this theoretical gap. The observed convergence could arise from properties of the in-context learning setup itself (regularization from limited exemplars, pattern completion favoring low complexity) rather than a true model-internal prior over category structures.

   The paper partially addresses this through empirical validation (rotation analysis, baselines), which show the emergent systems are non-trivial. However, the paper never clarifies what "inductive bias" means mechanistically in an LLM, and the framing risks over-interpreting the results. The theoretical ambition of the paper would be better served by either (a) explicitly qualifying that IICLL reveals a *behavioral* bias in the LLM's input-output mapping rather than a learner-internal prior, or (b) providing a clearer argument for why the Bayesian convergence result might extend (e.g., citing work on in-context learning as implicit Bayesian inference). **This matters because it affects how the paper's central claim should be interpreted—the claim that LLMs "have" an inductive bias for IB efficiency is stronger than what the data can uniquely establish.**

### Minor

1. **Statistical tests are absent for the IICLL convergence.** Figure 4 shows confidence intervals for efficiency loss, IB-alignment, and WCS-alignment over generations. The confidence intervals overlap initially and then separate, but no formal statistical test (e.g., mixed-effects model testing the effect of generation on efficiency loss with post-hoc comparisons) is reported. Formal inference would strengthen the claim that the trends are significant rather than driven by a few chains.

2. **The Shepard circles experiment (Section 4.3) is too preliminary to support the claim of "domain-general bias."** The experiment uses only one model (Gemini), one label count (k=4), and no quantitative IB efficiency measure. The paper itself calls this "initial evidence" and a "preliminary investigation," but the conclusion that this "suggests that LLMs potentially have a domain-general bias" overstates what the data show. The section adds limited weight to the paper's core argument and could be condensed or moved to future work without weakening the main contribution.

3. **No analysis of whether low-complexity IICLL systems are degenerate (single-label) or genuinely multi-category.** The paper reports that Gemma, Llama, and Qwen converge to low-complexity solutions (Figure 3), and Appendix L reportedly addresses that smaller models struggle to produce non-degenerate systems. However, for the four tested models, the paper does not explicitly report the number of distinct labels used by the final generation of each chain, making it difficult to assess whether these systems are substantively interesting or trivial.

### Trivial

- Figure 4 would benefit from explicit labeling of whether the confidence intervals are bootstrap-based or parametric.

## Nice-to-Haves

- Testing whether explicitly telling the model that the stimuli are "colors" (vs. "features") changes IICLL behavior would clarify the role of prompt framing.
- Ablating the number of in-context examples to test whether the observed convergence depends on prompt length would strengthen the analysis.
- The reproducibility statement says data is "available upon request"; public hosting would better serve the community.

## Removed Points

These points were raised by reviewers but are removed from the main review for the reasons stated:

1. **"Only one model recapitulates the full human range—framing overclaims."** The paper's abstract explicitly states: "However, only a model with strongest in-context capabilities (Gemini 2.0) is able to recapitulate the wide range... while other state-of-the-art models converge to low-complexity solutions." The title ("Evolution and Compression in LLMs") refers to LLMs broadly, and the finding that *all* four models restructure systems toward IB efficiency is supported. The paper is appropriately specific about which claims apply to which models. Removed because the paper already addresses this.

2. **"Theoretical gap is not addressed."** This is retained as Major Weakness 1 (the critic was correct about this point, and it survives verification). However, the critic also suggested that the paper "relies on empirical sanity checks rather than a mechanistic explanation" — this is accurate but not fatal, since the paper is an empirical study, not a mechanistic analysis. The weakness is about framing, not about flawed experiments.

3. **"Missing related works."** Removed per instructions (I cannot verify which related works are missing).

4. **Certain reproducibility concerns** (undisclosed hyperparameters, implementation details). Removed per instructions — these are standard for empirical papers at this venue.

5. **Generic formatting/style criticisms** from the strength finder. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The calibration search did not surface any review that offered a perspective not already present in the paper or the critiques already listed.

## Suggestions

1. Add a paragraph in Section 2.3 or the Discussion explicitly addressing the theoretical gap between Bayesian iterated learning and IICLL with LLMs. Even a concise acknowledgment that "the convergence guarantee does not directly extend to transformer-based in-context learners, but the rotation analysis and baselines provide empirical support that the observed convergence reflects genuine structure" would substantially strengthen the paper's theoretical framing.

2. Report the number of distinct labels used by the final generation of each IICLL chain across models, to clarify whether low-complexity solutions correspond to degenerate (single-label) or multi-category systems.

3. Add formal statistical tests (e.g., mixed-effects models or permutation tests) comparing efficiency loss at early vs. late generations in Figure 4.

4. Either strengthen the Shepard circles experiment with quantitative IB efficiency measures and a human/random baseline comparison, or reduce it to a one-paragraph mention in the Discussion.

## Score and Decision

**Calibration procedure.** Three queries were used for Round 1 (bracketing): (1) `high_score=3.5` returned papers averaging 2.3–3.4 (all reject); (2) `low_score=3.5, high_score=7.5` returned papers averaging 6.0–6.75 (mixture of poster/oral accepts and one reject); (3) `low_score=7.5` returned papers averaging 8.0–9.0 (all oral accepts). This placed the paper in the middle band. Initial bracket: 5.5–7.5.

Round 2 (narrowing) queried `(5.5, 7.5)` and `(4.5, 6.5)` with more topically specific queries. Anchors retrieved:

| Anchor | Avg Score | Round | Comparison to current paper |
|--------|-----------|-------|-----------------------------|
| bVTM2QKYuA (Geometry of Concepts in LLMs) | 6.75 | R1,R2 | Stronger theoretical contribution with formal proofs; similar empirical scope but different topic. The current paper has more comprehensive behavioral experiments but weaker theoretical grounding. Slightly weaker than this anchor. |
| Zh2iqiOtMt (Fundamental Limits of Knowledge Transfer) | 6.50 | R2 | Theory paper on knowledge transfer rates; different topic but similar overall rigor. The current paper has broader empirical scope. Comparable. |
| RFqeoVfLHa (Self-Improvement Reversal) | 6.50 | R2 | Thorough empirical study on LLM post-training with clear findings. Similar empirical rigor; both have well-defined contributions. Comparable. |
| HC0msxE3sf (Signaling Game as beta-VAE) | 6.00 | R1,R2 | Emergent communication paper with theoretical framing but more mixed reviews (one strong reject). The current paper has more comprehensive experiments and fewer fundamental concerns. Better than this anchor. |
| Sy8upuD6Bw (Emergent Communication with Repair) | 6.33 | R1,R2 | Well-executed but modest contribution. The current paper has broader scope and more significant findings. Slightly better than this anchor. |
| hKMPz3wkPV (Formal Theory of Compositionality) | 6.75 | R1 | Strong theoretical paper but rejected due to fundamental formal concerns raised by one reviewer. The current paper is more empirically grounded and has fewer foundational issues. Comparable in overall quality. |

The paper compares favorably to the poster-level anchors in the 6.0–6.33 range and is slightly below the oral-level anchor at 6.75. Given its genuine empirical contributions tempered by the theoretical framing gap and the limited number of models showing the full effect, the paper is a solid accept near the upper end of the poster range.

**Score:** 6.5 — Accept. The paper makes a clear, well-executed empirical contribution with a novel paradigm (IICLL) applied to an important question (human-aligned categorization in LLMs). The weaknesses are addressable and do not undermine the core findings.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>