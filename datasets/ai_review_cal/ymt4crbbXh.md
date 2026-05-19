- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6
Confirmed. The candidate LM is never specified anywhere in the paper. Now I have a complete picture. Let me synthesize the final review.

## Summary

AutoBencher proposes a declarative framework for automatic benchmark construction: given user-specified desiderata (novelty, difficulty, separability for capability evaluation; harmfulness and attack success rate for safety), the framework operationalizes each as a quantitative metric and uses an LM (GPT-4-0125-preview) augmented with privileged information to iteratively search over dataset descriptions and generate questions. The resulting datasets (~4000 examples across 6 domains) achieve a 27% reduction in rank correlation (more novel) and 22% lower best-model accuracy (more difficult) than human-constructed benchmarks like MMLU, and uncover specific model vulnerabilities (e.g., Gemini Pro's weakness on Fordism, GPT-4 Turbo on reproducing harmful events).

## Strengths

1. **Clean, explicit operationalization of benchmark desiderata.** The paper defines novelty, difficulty, and separability as closed-form functions of model accuracy vectors (Section 3.1), enabling direct optimization. Table 1 (though an image) reports concrete metrics showing AutoBencher achieves a 27% reduction in rank correlation and 22% greater difficulty over human benchmarks. The ablation of adaptive search (AUTOBENCH-AS) further confirms that these gains are not trivial.

2. **Privileged-information asymmetry is a well-motivated mechanism for generating harder-but-correct questions.** By augmenting the evaluator LM with external sources (Wikipedia, Python libraries, translation systems) that candidate LMs cannot access, AutoBencher produces questions that are substantially more difficult than prior LM-based generation (ChatGPT achieves 97%+ on LM-Examiner vs. ~60% on AutoBencher; Section 2). Human evaluation (Section 6.4) confirms a low ~5% error rate, supporting that the difficulty does not come at the cost of correctness.

3. **Adaptive search demonstrably improves topic quality over naive generation.** The ablation in Table 1 shows that removing adaptive search (AUTOBENCH-AS) degrades both novelty and difficulty scores, isolating the contribution of the iterative proposal mechanism. This is a clean experimental design.

4. **Genuinely interesting qualitative findings.** The paper surfaces concrete, previously undocumented model weaknesses: Gemini Pro drops from rank 6 to 16 on Fordism; GPT-4 Turbo fails to decline prompts about replicating airport attacks (Section 6.3). These specific discoveries demonstrate that the method yields actionable insights beyond aggregate metrics.

5. **Low operational cost.** The paper reports ~$15 per run (750K tokens), making the approach practical for routine use by academic labs.

## Weaknesses

### Fatal
None.

### Major

1. **The candidate LM used in adaptive search is never specified.** Algorithm 1 (lines 1–7) iteratively proposes dataset descriptions and "compute[s] the accuracy of a candidate LM" to guide subsequent proposals. The paper explicitly names the evaluator LM (GPT-4-0125-preview in §5.2) but never states which model serves as the candidate LM. This is not a minor omission: the adaptive search engine is the mechanism that steers the proposal distribution toward challenging topics. The discovered topics and final metrics depend on which model provides the difficulty signal. If the candidate LM is GPT-4 (the same as the evaluator), the search risks circularity; if it is a weaker model, the search favors topics that are hard for that model but not necessarily for strong models. This missing detail prevents full reproducibility of the core mechanism and makes the reported improvements partially uninterpretable. **This does not invalidate the contribution** — the ablation shows AutoBencher outperforms human benchmarks even without adaptive search — but it is a concrete, verifiable gap in experimental specification that needs to be closed.

### Minor

2. **Missing LM-Examiner baseline in Table 1.** The paper acknowledges LM-Examiner as the most similar prior work (Section 2) and provides a single accuracy comparison (ChatGPT 97% vs. ~60%), but does not include LM-Examiner in Table 1 with the same novelty, difficulty, and separability metrics used for all other comparisons. While the paper's main claim (advantage over human-constructed benchmarks) does not hinge on this, including LM-Examiner would more rigorously substantiate the claim that the *approach* — privileged information + adaptive search — advances over simply prompting an LM for questions.

3. **Novelty metric protocol for human benchmarks is ambiguous.** The paper states: "For calculating NOVELTY, we set D_prev as the aggregate of all datasets in HUMANBENCH" (§5.1, line 151). When computing novelty for a human benchmark (e.g., MMLU history), it is unclear whether that dataset is included in its own prior set. If it is, the regression can approximately predict v_c from itself, artificially lowering the novelty of human benchmarks and inflating the reported improvement. The paper does not describe a leave-one-out procedure. The authors should clarify the exact protocol.

4. **Human evaluation lacks sample sizes and inter-annotator agreement.** The correctness evaluation reports a 5% error rate (Section 6.4) and the salience evaluation states questions are "similarly salient to MMLU" — but neither reports how many examples were annotated, how many annotators were used, or any inter-annotator agreement metric. These details are standard for rigorous human evaluation and would significantly strengthen credibility.

5. **Qualitative discoveries are highlighted without prevalence statistics.** Section 6.3 presents compelling failure cases (Fordism, Permian Extinction, airport attacks) but does not report what fraction of the ~4000 generated examples or ~80 dataset descriptions reveal such unexpected patterns. The novelty metric is supposed to capture this systematically, but the narrative relies heavily on a few hand-picked examples. Reporting the fraction of descriptions that yield "surprising" rankings would substantiate the claim that the method systematically uncovers novel trends.

6. **Salience filtering for math and safety is by "manual judgment" without documentation.** Section 5.2 mentions: "For math and safety domains, we manually judge the salience of the dataset descriptions and remove the non-salient or non-harmful ones." The criteria, number of topics removed, and inter-judge agreement are not reported, making this step unreproducible.

### Trivial

None.

## Nice-to-Haves

- **Ablation on the choice of candidate LM.** Showing how discovered topics and final metrics change when using a weak model (e.g., LLaMA-2-7B) vs. a strong model (GPT-4) as the candidate would validate that the adaptive search is robust and not artifactually dependent on a specific model choice.
- **Per-category breakdown of safety ASR.** Reporting attack success rate per model or per harmful category (rather than averaging over all models) would strengthen the safety analysis and reveal which categories are most vulnerable.
- **Discussion of data contamination risk.** The evaluator LM (GPT-4-0125-preview) generates questions using Wikipedia pages that may overlap with its training data. While this does not invalidate the results (the candidate LMs answer without privileged information), acknowledging the limitation would preempt a common concern.
- **Statistical significance for novelty/difficulty reductions.** Bootstrapped confidence intervals on the rank-correlation reductions would add rigor to the headline claims.

## Removed Points

- *"Linear regression in accuracy space may miss non-linear shifts"* — This is a methodological design choice, not a flaw. Every approximation makes assumptions; the paper uses a reasonable linear predictor and the rank correlation evaluation is standard. Removed as a methodological preference, not a concrete shortcoming.
- *"Mathematics Dataset is synthetic / has limited headroom"* — Speculative concern about a specific baseline domain; the paper reports aggregate improvements across all domains. Removed for lacking concrete evidence tied to the paper's reported numbers.
- *"Two-stage design needs justification"* — The paper already provides justification (Section 4.2: novelty/separability require evaluating all models, which is expensive during search). Removed as already addressed.
- *"Data contamination should invalidate results"* — Speculative; no evidence that contamination affects the specific findings. The candidate LMs answer without privileged information, so the asymmetry is the point. Moved to Nice-to-Have.
- *"Cost of evaluating candidate LMs is not accounted for"* — The paper reports 147K tokens for evaluating candidate LMs (§5.2). This is accounted for. Removed as factually incorrect.
- *"Safety evaluation should report per-model ASR"* — Reasonable suggestion but not a weakness; moved to Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions. The reviews independently converge on the same core findings (the declarative framing is thoughtful, the privileged-information mechanism is effective, the qualitative discoveries are genuinely interesting) and the same main gaps (unspecified candidate LM, missing LM-Examiner baseline, ambiguous novelty protocol). No reviewer offered a novel analysis or reinterpretation of the results that the paper itself does not already contain.

## Suggestions

1. **Specify the candidate LM** used in adaptive search (e.g., GPT-3.5-Turbo, or whichever model was actually used) and, ideally, ablate this choice with at least one alternative model.
2. **Clarify the leave-one-out protocol** for the novelty metric, or if none was used, re-run the analysis with proper leave-one-out and confirm the reported numbers still hold.
3. **Include LM-Examiner as a baseline** in a quantitative comparison table (even a small one) with novelty, difficulty, and separability computed on its generated datasets.
4. **Report sample sizes and inter-annotator agreement** for the human evaluation in Section 6.4.
5. **Report the fraction** of dataset descriptions that yield "surprising" model rankings (i.e., where novelty exceeds some threshold) to accompany the qualitative examples.
