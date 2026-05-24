Now I have all the calibration data I need. Let me synthesize the final review.

## Summary of calibration

**Round 1 bracket**: 4.5–6.5 (above weak 2.5–3.0 anchors, below strong 8.0 anchors)

**Round 2 narrowing**:
- *On the Hardness of Faithful CoT* (5.0, Reject): Similar topic, but criticized for incremental methodology. The current paper's deletion-based probing is more novel, giving it a modest edge. However, both share metric concerns.
- *Physics of Language Models* (6.0, Accept Poster): Strong controlled experiments with synthetic data and probing. The current paper is less controlled and has a weaker evaluation metric, making it somewhat weaker overall.
- *FLARE* (5.75 avg, Reject): Different contribution type (method for faithful reasoning). Not directly comparable.
- *SciBench* (5.6, Reject): Benchmark paper with mixed reviews. The current paper has clearer methodological novelty but also clearer evaluation weaknesses.

The paper lands at **5.5** — it has genuine methodological novelty and interesting empirical findings, but the evaluation relies on an LLM judge for physics correctness, the cramming interpretation needs stronger controls, and several methodological details are underspecified. This is above the 5.0 "Hardness of Faithful CoT" anchor (more novel methodology) but below the 6.0 "Physics of Language Models" anchor (weaker experimental controls).

---

## Summary

This paper introduces a deletion-based probing framework to test whether LLMs faithfully use chain-of-thought reasoning in physics problem solving. By intercepting CoT mid-generation and removing tokens under end, random, and physics-aware strategies, the authors measure downstream effects on accuracy, answer length, and information overlap across three models (Magistral, Phi-4, Qwen-A3B) and three physics benchmarks. The central finding is that accuracy remains stable under moderate deletion (40–60%), while answer length increases — a compensatory "cramming" behavior where models appear to reconstruct missing reasoning steps directly in the final answer.

## Strengths

1. **Novel deletion-based probing methodology.** The paper introduces a clean, systematic framework for testing CoT dependence: intercept the scratchpad during generation, delete tokens under controlled strategies, and measure downstream effects. This is more targeted than prior faithfulness evaluations that only compare with/without CoT or early-stopping. The three strategies (end, random, physics-aware) are well-motivated and provide complementary views. Evidence: Section 2 description and Figures 4–6.

2. **Consistent empirical "cramming" pattern.** Across all three models, all three datasets, and all three deletion strategies, the final answer length increases as CoT is deleted — an "X-shaped" pattern in the length plots (Figure 5). This is an objective, metric-independent observation (character counts do not rely on the LLM judge). It reveals a robust behavioral phenomenon worthy of further investigation. Evidence: Section 4.1, Figures 5–6.

3. **Multi-dimensional evaluation.** Rather than relying on accuracy alone, the paper tracks three axes (accuracy, answer length, information overlap using Jaccard/Manhattan metrics in Figure 7). This provides a richer picture than accuracy-only evaluations and partially decouples the claims: the length and overlap findings are independent of the LLM judge used for scoring.

4. **Physics-aware manipulation.** The domain-specific deletion strategy — using Claude-4 Sonnet to identify equations, constants, and unit conversions — leverages the structured nature of physics to target content that should matter most. This goes beyond generic deletion and adds a useful methodological dimension. Evidence: Section 3.2.

## Weaknesses

### Major

1. **LLM-as-judge evaluation undermines confidence in the accuracy claims.** The paper scores solutions using Claude-4 Sonnet on a 0–1 scale based on "correctness, derivation accuracy, logic, formatting, and clarity." Physics problems have determinate answers (numerical values, symbolic expressions) that could be checked more deterministically. The composite scoring criteria mix correctness with style, making it unclear what drives the scores. Because the central claim "accuracy remains stable under 40–60% deletion" (Abstract, line 13) depends entirely on this judge, the reliability of every quantitative accuracy result is uncertain. The paper does not validate the judge against a ground-truth set, nor does it report agreement rates. This issue is partially mitigated by the independent length and overlap findings, but the accuracy-based claims — which are central to the paper's framing — are weakened. The paper acknowledges several limitations but does not mention this evaluation concern (Section 4.4).

2. **The "cramming" interpretation needs stronger evidence.** The paper concludes that increased answer length reflects models "reconstructing lost reasoning" (Section 4.1). But the evidence — increased length and bag-of-words overlap between deleted CoT and final answers — does not uniquely support this interpretation. (a) The bag-of-words overlap metrics (Jaccard, Manhattan) are applied without controlling for the baseline topical overlap that naturally exists between any CoT and final answer about the same physics problem (both inevitably share terms like "force," "mass," "kg"). The paper does not subtract the overlap between the *full original* CoT and the final answer to isolate a "reconstruction" component. (b) Increased length alone could reflect the model padding output or rephrasing the prompt rather than genuinely reconstructing reasoning steps. A targeted analysis examining whether specific *reasoning steps* (equations, substitutions, algebraic manipulations) reappear would strengthen the claim substantially.

3. **No token-length control in deletion experiments.** When tokens are deleted from the input, the input becomes shorter. Observed effects could partly reflect length reduction rather than the specific removal of reasoning content. A control condition — replacing deleted tokens with neutral filler (e.g., repeated periods or newlines) to hold input length constant — is needed to separate the effect of content removal from the effect of shortened context. This is not acknowledged as a limitation (Section 4.4).

### Minor

4. **The faithfulness framing is imprecise.** The paper defines faithfulness as whether the CoT "explicitly reflects the internal computations" (Section 4.3) but the deletion experiments test *dependence* — whether the model needs the CoT to produce correct answers. A model could faithfully represent internal computations while still being able to solve the problem without CoT (because the computation was already performed). The paper conflates these two concepts at several points, e.g., "not all intermediate steps in the scratchpad are faithfully required for correct answers" (Section 4.3, line 201). The overall implications for faithfulness are thus weaker than claimed, though the paper's cautious language in parts of Section 4.3 partially addresses this.

5. **Missing statistical significance tests.** Many claims about accuracy "remaining stable" (e.g., "until approximately 40% deletion" in Section 3.2, line 134) are supported only by visual inspection of plots with overlapping error bars. No formal paired significance tests (e.g., comparing 0% vs. 40% deletion) are reported. This is particularly important for the core stability threshold claims.

6. **Deletion implementation details are underspecified.** The paper describes intercepting CoT "mid-generation" and deleting tokens, but key details are absent: at what point in generation is the scratchpad intercepted? How is the boundary between CoT and answer identified? What tokenization granularity is used for deletion (word-level, subword, character)? For physics-aware deletion, the tagging prompt, thresholds, and accuracy verification for Claude-4 Sonnet's annotations are not described. These details are essential for reproducibility.

7. **No discussion of equation tokenization for overlap metrics.** Physics equations use notation (e.g., "F=ma," "kg·m/s²") that may be tokenized unpredictably by different tokenizers. The bag-of-words overlap metrics (Jaccard, Manhattan) are applied to "all tokens" without discussing how mathematical notation is handled — whether equations are broken into subword units that inflate or deflate overlap scores.

### Trivial

8. **Figure 3 caption confuses deletion "types" with later-described "strategies."** The caption labels columns "None, Annotated, Non-Annotated" while the text later describes three deletion *strategies* (end, random, physics-aware). These are different categorizations; the mismatch can confuse readers. (The paper text itself clearly explains the annotated vs. non-annotated comparison in lines 120–121; the caption alone is the issue.)

## Nice-to-Haves

- **No-CoT baseline in deletion experiments:** The paper establishes that CoT helps (Section 3.1) but does not compare deletion accuracy (e.g., 60% deletion) to accuracy with *no CoT at all*. This would bound how much CoT is actually needed.
- **Failure mode analysis:** Characterizing what kinds of errors occur under deletion (wrong numerical values, wrong equations, non-physical units) would strengthen the cramming and recovery analysis.
- **Replace filler control:** As noted in weakness #3, using filler tokens to hold input length constant.
- **Baseline overlap subtraction:** As noted in weakness #2, subtracting the full-CoT/final-answer overlap to isolate reconstruction.

## Removed Points

The following points from the inputs are removed with justification:

- **"Appendix materials are stripped by the parser"** — REMOVED per hard rules: the parser strips appendices from all submissions; they exist in the original.
- **"Missing related works"** — REMOVED per hard rules: I cannot verify the existence of missing references with external sources.
- **"Reproducibility: hyperparameters not disclosed"** — REMOVED: most relevant details (temperature, top-p, models, datasets) are provided; minor omissions are easily addressable and not structural.
- **"Strength: addressed an important problem"** (from Strength Finder) — REMOVED: generic, not specific to this paper's concrete evidence.
- **"Strength: calibration study"** — REMOVED as strength: it's a standard practice, not a distinctive contribution, though it's fine as part of the methodology description.
- **"No analysis of failure modes"** (from Harsh Critic) — MOVED to Nice-to-Have: genuinely useful suggestion but not a weakness — the paper makes no claim to analyze failure modes.
- **Criticism about Figure 2 interpretation** (the plot shows Reason scores increasing, not Final Answer scores) — DEMOTED to a note: the paper's text says "higher reasoning explicitness yields more reliable solutions" and Figure 2 plots both Reason and Final Answer scores. The text is about overall quality, and the figure does show both series. The observation that Reason scores drive the trend is correct but not a flaw in the paper's presentation — it's describing the expected effect of prompt manipulation.
- **"The paper does not discuss how deletion interacts with the model's tokenization"** — MERGED with weakness #7; kept the more specific point about equation tokenization in overlap metrics.

## Novel Insights

A genuinely novel observation emerges from the contrast between the three deletion strategies. Under end deletion, information overlap rises smoothly and consistently — models can systematically reconstruct truncated reasoning. Under random deletion, overlap grows only beyond ~60% deletion, suggesting scattered removals are harder to recover from. Under physics-aware deletion, overlap stays flat until 70–80% deletion, then spikes sharply. This differential pattern is more informative than any single metric: it suggests that the *structure* of what is removed (contiguous text vs. scattered tokens vs. domain-critical content) determines the model's compensatory strategy, and that cramming is not a monolithic behavior but depends on what information is missing. This observation goes beyond the paper's own framing of "cramming" as a single phenomenon and points toward a more nuanced understanding of how models repurpose their outputs.

## Suggestions

1. **Replace or augment the LLM judge with deterministic answer checking.** For numerical answers, use tolerance-based exact match; for symbolic answers, use SymPy equivalence checking. Report agreement rates between the judge and deterministic checking to validate the scoring procedure. At minimum, add a controlled subset where answers are evaluated both ways.

2. **Add a baseline subtraction for the overlap analysis.** Compute Jaccard/Manhattan overlap between the *full original* CoT and the final answer (no deletion). Subtract this from the deletion-condition overlap to isolate the reconstruction component from mere topical overlap.

3. **Run a token-length control experiment.** Replace deleted tokens with neutral filler (e.g., repeated "." tokens) to hold input length constant, and compare the resulting accuracy/length curves to the current deletion-only condition.

4. **Report paired significance tests.** For the "stable until 40%" claim, compare accuracy at 0% vs. 40% deletion using a paired test (e.g., Wilcoxon signed-rank) across problems to confirm non-significance formally.

5. **Specify deletion implementation details.** Add a clear description of: scratchpad interception point, CoT/answer boundary detection method, tokenization granularity for deletion, and the physics-aware tagging prompt with accuracy verification.

## Score and Decision

**Bracket (Round 1):** 4.5–6.5  
**Narrowing (Round 2):** Anchors at 5.0 (Hardness of Faithful CoT, Reject), 5.6 (SciBench, Reject), 5.75 (FLARE, Reject), 6.0 (Physics of Language Models, Accept Poster). The current paper has more methodological novelty than Hardness of Faithful CoT (5.0) but weaker experimental controls than Physics of Language Models (6.0). The evaluation metric and undersupported cramming interpretation place it below the acceptance-level Physics of Language Models paper but above the incremental Hardness of Faithful CoT paper. **Final score: 5.5** — borderline, with genuine contributions tempered by significant evaluation concerns that need addressing before the findings can be trusted fully.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>