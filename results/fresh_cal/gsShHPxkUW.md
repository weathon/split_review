Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes a causal mediation analysis framework to assess whether LLMs comprehend "deep structure" (core semantics) or merely rely on "surface structure" (linguistic presentation). The authors introduce ADCE (Approximated Direct Causal Effect) and AICE (Approximated Indirect Causal Effect) as metrics to quantify deep vs. surface structure reliance. Empirically, they evaluate 12 LLMs across 5 tasks, finding that most models exhibit positive ADCE (indicating deep structure comprehension), that closed-source models rely more on deep structure than open-source models, and that ADCE can reveal degradation in deep-structure dependence that accuracy misses under spurious correlations. The paper also theoretically connects ADCE to probability of necessity and sufficiency.

## Strengths

1. **Principled causal mediation formalism for deep structure assessment.** The paper operationalizes the abstract notion of "deep structure comprehension" as a direct causal effect question, going beyond prior heuristic surface-sensitivity tests (lines 135–148). The derivation from unobservable DCE/ICE to estimable ADCE/AICE is clearly motivated by the known unobservability problem (lines 151–156).

2. **Theoretical connection between ADCE and necessity/sufficiency (Theorem 1).** Proving that ADCE is a weighted combination of probability of necessity and probability of sufficiency provides formal grounding that ADCE captures bidirectional causation from deep structure to output — a genuine theoretical contribution absent from prior accuracy-based evaluations (lines 218–228).

3. **Broad empirical scope across 5 tasks and 12 models.** The evaluation spans mathematics (2-digit multiplication, GSM8k), logic (Word Unscrambling, Analytic Entailment), and commonsense (CommonsenseQA), testing four model families (Llama, Mistral, GPT, Claude) of varying scales (lines 239–247). This breadth substantially exceeds prior work restricted to specific tasks or small models.

4. **Spurious correlation experiment demonstrates practical diagnostic value of ADCE.** The CivilComments experiment (Section 4.5, lines 299–304) shows that as spurious correlation increases, accuracy remains misleadingly high while ADCE declines — a concrete scenario where the proposed metric reveals a failure mode that accuracy hides. The contrast between majority (spurious) and minority (non-spurious) groups strengthens the argument.

5. **Discovery of differential deep/surface reliance across model families.** The ADCE vs. AICE comparison reveals that closed-source models (GPT, Claude) exhibit greater reliance on deep structure, while open-source models show higher surface sensitivity that decreases with scale (Figure 5, lines 277–278). This is a specific, non-obvious empirical finding.

## Weaknesses

### Fatal

None.

### Major

1. **The AICE approximation is central to the method but lacks validation.** ADCE is defined as TE − AICE (Eq. 5, line 195), so any systematic bias in AICE propagates into all main results. The paper acknowledges this is an approximation and states that intervention strategies "minimize the discrepancy" (lines 185–190), but provides no formal bound, sensitivity analysis, or empirical validation of how close AICE is to the oracle ICE. For example, the Mask strategy for AICE masks a non-core word near the masked core word — but the paper does not assess whether different choices of which non-core word to mask change ADCE estimates in ways that could alter qualitative conclusions. Without some form of stability check (e.g., comparing multiple AICE variants, or validating on a synthetic task where ground truth is known), the metric's reliability is uncertain. The empirical patterns (positive ADCE, zero for random baseline) provide indirect support, but direct validation of the approximation is missing.

2. **Claims about ADCE "superiority" over accuracy are overstated.** The paper frames ADCE as "a more comprehensive assessment criterion" (abstract, lines 69, 216) and "superior" (line 229). The spurious correlation experiment shows one scenario where ADCE reveals a failure mode that accuracy misses, which is valuable. But accuracy and ADCE measure different things — raw performance vs. sensitivity to deep structure changes — and the paper does not establish that ADCE is generally "more comprehensive." The framing should position ADCE as a complementary diagnostic tool for assessing deep-structure reliance, not a replacement or general improvement over accuracy. Several instances of "superiority" language should be softened to reflect what the evidence actually supports.

### Minor

3. **The closed-source vs. open-source comparison is partially confounded by accuracy.** ADCE is strongly correlated with accuracy across models (R² > 0.7, Fig. 4, line 258). Closed-source models generally have higher accuracy than open-source models, so their higher ADCE is partly expected from this correlation. The more interesting finding — the ADCE/AICE balance shift (Fig. 5) — is less affected by this confound because it compares within-model ratios. However, the paper's claim that "closed-source LLMs comprehend deep structure better" (line 278) should acknowledge the accuracy confound explicitly. Controlling for accuracy (e.g., by matching on accuracy bins, or showing the ADCE/AICE balance at comparable accuracy levels) would strengthen the claim.

4. **No error bars, confidence intervals, or statistical significance reported.** All figures (Figs. 2–6) present point estimates without variance. Since ADCE is an average over samples and outputs are stochastic (especially for smaller models and under different intervention realizations), readers cannot assess whether observed differences between models or tasks are statistically reliable. This is especially important for Figure 5 (model comparisons) and the spurious correlation experiment (Figure 6).

5. **The spurious correlation experiment (CivilComments) does not specify how deep/surface structure is operationalized for this task.** The paper explains that identity information is a spurious surface attribute (line 229, 304), but does not describe how TE and AICE interventions are constructed for CivilComments — i.e., what constitutes a deep structure intervention vs. a surface structure intervention in this setting. The main text references the appendix for details, but the description in the main text is insufficient for a reader to assess what ADCE measures here. The deep-to-surface mapping for each task should be explicit in the main paper.

6. **The SFT experiment is suggestive but limited.** It uses a single model (Llama-3-8b), single task (Analytic Entailment), and single fine-tuning run (lines 274). While the paper hedges appropriately ("may rely on activating"), the experiment would be stronger with multiple models, tasks, or seeds to rule out the alternative explanation that ADCE increased simply due to improved accuracy.

7. **Using Claude-3.5-Sonnet to generate rephrase interventions introduces an unexamined confound.** A third-party model generates the surface-structure variants that are used to evaluate other models (line 212). The paper mentions a self-checking mechanism but provides no statistics on intervention quality (e.g., rejection rate, token-level similarity between TE and AICE rephrasings). This is a standard practice, but its impact on the downstream evaluations is not discussed.

### Trivial

8. **The ideal definition of deep structure comprehension (Eq. 1) is a strong deterministic condition, while ADCE measures something probabilistic and approximate.** The paper presents Eq. (1) as motivation ("This inspires a causal effect estimation perspective," line 95) and does not claim ADCE satisfies it exactly, but the gap between the idealized framing and the actual metric is not clearly acknowledged. This could cause confusion about what exactly ADCE certifies.

## Nice-to-Haves

- A sensitivity analysis for the AICE approximation would significantly strengthen the paper. For example: compare ADCE computed using different non-core word mask choices, or validate on a synthetic task where the true deep/surface decomposition is known.
- A table summarizing how deep structure and surface structure are operationalized (intervention type, what gets masked/rephrased) for each of the 5 tasks would aid reproducibility and cross-task comparison.
- The paper could report accuracy values alongside the spurious correlation figure to help readers assess ceiling effects.

## Removed Points

These points were identified by reviewers but are removed from the main review for the reasons stated:

- **Motivation experiment framing (Fig. 1):** The critic argued the experiment over-generalizes. The paper explicitly presents this as a motivating observation on a specific task (lines 57–58) and later acknowledges task-specific patterns (line 264). Not a valid weakness.
- **Theorem 1 presentation "incomplete" without proof sketch:** The hard rules disallow penalizing missing appendix content. The theorem statement and its implications are fully presented in the main text.
- **Missing discussion of prior causal approaches in related work:** The hard rules disallow penalizing missing related works.
- **Claim that "ADCE measures something different from Eq. (1)":** The paper uses Eq. (1) as a motivating ideal, not as a definition that ADCE must satisfy. The gap is implicitly acknowledged through the approximation framework. At worst a trivial presentation issue (retained above point 8).
- **Claim about "closed/open-source difference is expected":** The ADCE/AICE balance comparison (Fig. 5) is not reducible to accuracy differences. The accuracy confound point is valid and retained (weakness #3), but dismissing the finding as fully expected is too strong.

## Novel Insights

The integration of the two reviewers' perspectives surfaces a pattern not fully articulated in the paper itself: the ADCE metric simultaneously measures two distinct notions — (a) the model's *sensitivity* to deep structure changes, and (b) the model's *reliance* on deep structure relative to surface structure. These are conflated in the paper's narrative. The high correlation between ADCE and accuracy (R² > 0.7) suggests that ADCE largely tracks model capability (better models are more sensitive to core semantics), while the more novel information lies in the ADCE/AICE *difference*, which controls for overall capability to some degree. The paper's strongest findings — the open-vs-closed contrast and the spurious correlation diagnosis — rely on this differential, not on raw ADCE. Future work could formalize this distinction and develop a metric that explicitly normalizes for accuracy.

## Suggestions

1. **Validate the AICE approximation.** Add a sensitivity analysis comparing ADCE under different AICE construction choices (e.g., masking different non-core words, using different rephrase prompts). If feasible, construct a synthetic task where ground-truth deep/surface decomposition is known to directly measure the approximation error.
2. **Add error bars or bootstrap confidence intervals** to all main figures (especially Figs. 2, 5, 6). This would let readers assess whether observed differences are reliable.
3. **Rephrase "superiority" claims** about ADCE vs. accuracy. Position ADCE as a complementary diagnostic that reveals a specific failure mode (overreliance on surface/spurious correlations) that accuracy misses. The spurious correlation experiment already makes this case effectively without overclaiming.
4. **Acknowledge the accuracy confound** in the closed-source vs. open-source comparison explicitly, and consider showing ADCE/AICE balance for accuracy-matched subsets.
5. **Specify the deep/surface decomposition for each task** in the main paper, especially for CivilComments where the mapping is least obvious.
6. **Expand the SFT experiment** with additional models or random seeds to increase confidence in the "knowledge activation" narrative.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>