Now let me run the calibration search:Now I have sufficient context to write the final review.

---

## Summary

This paper extends Jenner et al. (2024) in their investigation of look-ahead behavior in the Leela Chess Zero policy network. The authors introduce a puzzle set notation that disentangles position types by the pattern of square overlap across moves, extend activation patching and probing analyses to the 5th and 7th future moves, provide evidence for a time-insensitive AAC pattern mechanism in attention head L12H12, and show that the model differentially processes checkmate vs. non-checkmate scenarios through specialized heads (L12H12 and L12H17). A secondary analysis examines whether the model considers alternative move sequences.

---

## Strengths

- **Novel puzzle set notation (Section 2.4)** resolves an analytical ambiguity in Jenner et al. (2024) by explicitly separating puzzle types based on the pattern of square reuse across moves (e.g., 11223 vs. 11233). This allows the key finding that patching effects vary systematically by pattern type — strong for 11223 (AAC), moderate for 11234 (ABC), weak for 11233 (ACC) — something that was obscured in prior work by bundling higher-move squares.

- **Time-insensitive AAC pattern hypothesis (Section 3)** is a concrete, falsifiable mechanistic claim: the paper demonstrates that L12H12 responds to the AAC structural pattern regardless of whether it occurs at moves 1-2-3, 3-4-5, or 5-6-7, suggesting a general learned rule rather than timing-specific heuristics. This goes meaningfully beyond what Jenner et al. reported.

- **Checkmate/non-checkmate specialization** (Figures 4, 5, Section 3) is a clean empirical finding: L12H12 shows stronger responses to checkmate-ending sequences while L12H17 is more active for non-checkmate scenarios, revealing emergent division of labor without explicit architectural provision.

- **Complementary use of three interpretability techniques** (probing, activation patching, ablation) is well-motivated. The paper correctly identifies what each technique can and cannot tell us — for example, noting that probing reveals opponent-move encoding that activation patching does not find causally necessary, demonstrating why a single method would give an incomplete picture.

---

## Weaknesses

### Fatal
None.

### Major

- **7-move look-ahead claim is overstated relative to evidence.** The abstract states the model "can process information about board states up to seven moves ahead" without qualification, yet Figure 3 and the main text describe the 7th-move probe accuracy as "considerably low, but still non-negligible when compared with the probe's accuracy for a random model." While the conclusion (Section 5) does hedge — "though this capability becomes progressively weaker for more distant moves" — the abstract and main-text framing present this as a positive result rather than as weak, marginal evidence. No exact probe accuracy values for each move index appear in the main text, no effect sizes are reported, and the gap from random is not quantified. A "considerably low" signal barely above a random baseline does not establish 7-move look-ahead; it establishes that some faint signal exists at that horizon. The claim should be calibrated accordingly.

- **Probing does not disentangle look-ahead from co-occurrence statistics.** The paper uses linear probe accuracy as positive evidence that the model "encodes" future move information. However, in a curated Lichess puzzle dataset, future move squares are statistically correlated with current board configurations due to recurring tactical patterns (pins, forks, checkmate motifs). A probe trained on the residual stream could be predictive of future move squares simply because those squares are statistically predictable from the current position, without the model performing any planning. The paper mentions a "random model" as baseline in Figure 3, but does not specify what this random model is. If it is a randomly initialized version of the same architecture, it is not the right null for the co-occurrence hypothesis — the correct control would be a model trained on single-move prediction only (no multi-move puzzle-solving context). Without this, the distinction between "the model plans" and "these positions have predictable future moves" is not established.

### Minor

- **Alternative move analysis is restricted and may not generalize.** The claim that "the model considers multiple move sequences" rests on 609 puzzles filtered to cases where Leela assigns approximately 50% probability to each of two branches. This is an unusual, possibly unrepresentative regime (positions where the engine is maximally uncertain). The paper acknowledges this restriction but does not address whether the multi-branch behavior holds in more typical confidence regimes. The dataset size and the selection criterion together limit the generalizability of the conclusion.

- **Lack of quantitative specificity in the main text.** Key results are presented with references to figures and appendices but without explicit numbers: no exact probe accuracy values per move index, no p-values, and the confidence interval choice (50% and 90%) is unusual and not justified. Readers cannot fully evaluate whether reported effects are scientifically meaningful from the main text alone.

- **Zero ablation of entire attention heads is methodologically coarse.** The ablation methodology conflates which squares an attention head attends to with its value computation. This makes it difficult to precisely interpret ablation results as evidence for specific attention patterns. More targeted ablation (e.g., zeroing attention weights to specific squares) would sharpen the mechanistic claims.

### Trivial
None worth singling out beyond the quantitative reporting gap noted above.

---

## Nice-to-Haves

- Report exact probe accuracy for each move index (1st through 7th) and the random-model baseline directly in the main text, with the nature of the random model specified.
- Test the time-insensitive AAC hypothesis on a held-out puzzle set not used during hypothesis formation, to guard against in-sample pattern discovery.
- Extend the alternative move analysis to non-50/50 splits (e.g., 70/30) to show the multi-branch behavior is not restricted to the uncertainty regime.
- Include a worked example tracing a single puzzle through all three analysis techniques (patching, probing, ablation) to make the mechanistic narrative concrete.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **"Finetuning peculiarities may confound results" (Harsh Critic, Section 2.1):** The paper explicitly states it uses the same finetuned model as Jenner et al. (2024), which is prior published work. Criticizing a modeling choice inherited from an established baseline is out of scope; the comparison is consistent with the prior work, not introducing a new confound.

- **"609-puzzle dataset too small / selection criterion unfair" as a fatal concern:** The Strength Finder correctly identifies that patching the alternative move squares has a consistent directional effect (Figure 6). The limitation is real but falls to a minor concern rather than a structural one; the paper does not overclaim generalizability here.

- **All mentions of missing appendix content:** The reviewer notes inability to evaluate figures/appendices referenced in the text. Per policy, the parser strips appendices from all papers; they exist in the original submission. These are not weaknesses.

- **Claim that the dataset selection (puzzles solvable for Leela but hard for weaker models) creates unfair selection bias:** This is a methodological inheritance from Jenner et al. (2024) and is appropriate for studying the behavior of Leela specifically. It does not constitute a weakness in the paper's scope.

- **"Opponent moves do not contribute to patching" needs more explanation:** Raised as a missing analysis, but this is a finding the paper correctly reports and leaves open for future work — a nice-to-have at most.

---

## Novel Insights

The puzzle set notation is a standalone methodological contribution whose usefulness will extend to future interpretability studies of any game with a principal variation. The time-insensitive AAC pattern hypothesis — that L12H12 applies the same backward-in-time information movement rule regardless of whether the AAC triple occurs at moves 1-2-3, 3-4-5, or 5-6-7 — is the most genuinely novel mechanistic claim in the paper, suggesting the model learned a compositional pattern-matching circuit rather than a depth-specific heuristic. However, this remains a hypothesis supported by correlational patching evidence rather than a circuit-level verification.

---

## Suggestions

1. Rewrite the abstract's 7-move claim to reflect the actual evidence: "We find marginal but non-negligible evidence of encoding up to seven moves ahead, with signal quality decreasing substantially at the 7th move."
2. Specify what "random model" baseline means in Figure 3 and add quantitative values for probe accuracy at each move index.
3. Conduct a proper co-occurrence control — compare probe accuracy against a model trained only on next-move prediction — to sharpen the distinction between statistical predictability and active planning.
4. Validate the AAC pattern hypothesis on a held-out puzzle set to move it from hypothesis to confirmed finding.

---

## Score and Decision

**Axes:**
- *Originality:* Low-to-moderate. Same model, same techniques, same puzzle source as Jenner et al. (2024). The puzzle notation and time-insensitive AAC hypothesis are the main new ideas.
- *Importance of research question:* High in principle (understanding look-ahead in chess AI), but the specific contributions are narrow extensions.
- *Claims well-supported:* Mixed. The checkmate/non-checkmate specialization and AAC pattern are reasonably supported. The 7-move claim and the alternative-move generalization are overstated.
- *Soundness of experiments:* Adequate for most findings; the probing analysis lacks a proper co-occurrence control.
- *Clarity:* Acceptable but thin on quantitative detail in the main text.
- *Value to community:* Modest; the notation and head-specialization findings are useful additions.

**Anchor comparisons:**

| Path | Avg Human Score | Comparison to Paper Under Review |
|---|---|---|
| DzGe40glxs.md | 8.00 | First mechanistic evidence of planning in model-free RL; much stronger methodological novelty, causal verification, and first-in-field claim. Clearly superior. |
| bc2H72hGxB.md | 6.80 | Human-aligned chess AI; broader in scope, more novel framing, accepted. Stronger contribution than this paper. |
| 8xxEBAtD7y.md | 7.33 | Mechanistic interpretability of group operations; cleaner mechanistic account with verifiability guarantees. Stronger. |
| agEy9hliY1.md | 5.25 | Probing for neural combinatorial optimization; similarly incremental probing paper, rejected, comparable scope. |
| FnIRtzK5wX.md | 4.25 | Go game disentangling; similar level of interpretability study, rejected. Comparable contribution level. |
| vNkUeTUbSQ.md | 3.67 | Maze-solving policy interpretability; incremental mechanistic analysis rejected. This paper has slightly more structured contributions. |
| Wxl0JMgDoU.md | 2.50 | Chess interpretability (SAEs on Maia-2); rejected for being too incremental and lacking novel insights. This paper is more rigorous and structured. |
| eks3dGnocX.md | 4.50 | Mechanistic analysis of transformer solving logic problems; similarly mixed evidence-to-claim match. |

The paper under review sits between vNkUeTUbSQ (3.67) and agEy9hliY1 (5.25). Its contributions are real but incremental; the headline 7-move claim is overstated; the probing analysis has an unaddressed confound; and the alternative-move analysis is narrow. It outperforms Wxl0JMgDoU through better structure and more concrete findings. Calibrating against these anchors, I settle on **4.5**.

## Score and Decision

**Final Score: 4.5**

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>