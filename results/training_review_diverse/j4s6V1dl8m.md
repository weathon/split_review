## Summary

This paper proposes a checkability training method based on the Prover-Verifier Game (PVG) to improve the legibility of LLM chain-of-thought solutions for grade-school math problems. The approach iteratively trains: (1) a small verifier to predict solution correctness, (2) a "helpful" prover to produce correct solutions that the verifier accepts, and (3) a "sneaky" prover to produce incorrect solutions that fool the verifier. The paper shows that direct RL for correctness degrades human legibility, while the proposed checkability training (using an SRC reward) maintains legibility while improving accuracy. The key claim is that legibility to small verifiers transfers to time-constrained humans.

## Strengths

- **Identifies and empirically documents a "legibility tax" — a trade-off between accuracy and human legibility — and shows the proposed method partially resolves it.** Direct RL for correctness (Section 4.1, Fig. 3) yields high accuracy but causes human accuracy to drop and evaluation time to increase. The checkability training achieves intermediate accuracy while maintaining or improving human legibility (Fig. 1, Fig. 4). This provides a concrete, measurable tension that prior work on LLM legibility had not systematically characterized.

- **Systematic ablation studies across reward formulations (SRC, CGC, goodharting) and verifier sizes reveal algorithmic sensitivities.** The paper tests three reward variants and shows that SRC reward yields the best dynamics (Fig. 2), CGC reward leads to worse convergence (Fig. 7), and goodharting does not improve human legibility (Fig. 8). Varying verifier capability gaps ($10^{-4}$ to $10^0$ times prover compute) shows that checkability training is robust across a range but breaks down at extreme sizes. This analysis helps practitioners understand which design choices matter.

- **Provides theoretical grounding connecting the Prover-Verifier Game to completeness and soundness via verifier-leading Stackelberg equilibrium (Theorem 1).** This formal link distinguishes the paper from purely empirical approaches and gives principled justification for the iterative training algorithm, even though the paper candidly acknowledges the gap between theoretical assumptions and neural network practice (lines 130–131).

- **Demonstrates that verifier robustness increases across multiple attack types and that sneaky prover flaws become more subtle over rounds.** The paper evaluates verifiers against SRC, CGC, and goodharting adversaries (Fig. 6a), showing increasing steps-to-exploit across rounds. The GPT-4-based analysis of sneaky solutions (Fig. 5a) and human evaluation (Fig. 5b) both indicate increasingly subtle flaws, providing converging evidence for the training dynamics.

## Weaknesses

### Fatal

None.

### Major

- **Human evaluation lacks essential statistical reporting, undermining the paper's central claim that legibility transfers to humans.** The headline finding rests on human accuracy and timing data (Figs. 3b–d, 5b, 4b–c), yet the paper never reports: the number of contractors, how many solutions each evaluated, recruitment or screening procedures, whether the same contractors judged all conditions, or how the 45-second time limit was chosen. No error bars, confidence intervals, or significance tests accompany any human-judgment result. The differences across conditions appear visually modest (e.g., ~5–10 percentage points in Fig. 4b), and without variance estimates or significance tests the reader cannot assess whether these differences are reliable. The paper's otherwise thorough automated evaluations do not substitute for rigorous human-subject reporting when the claim is specifically about *transfer to humans*. This weakness is the most consequential and will require substantial additional reporting (and possibly additional data collection) to address.

### Minor

- **The verifier's increasing robustness is measured with indirect metrics, and a direct accuracy evaluation is missing.** The paper uses step-to-exploit (which conflates attack difficulty with verifier robustness) and balanced best-of-n (which only uses helpful-prover solutions). A standard verifier accuracy metric (e.g., AUC or accuracy on a held-out balanced test set of correct vs. incorrect solutions from diverse prover sources) would provide a cleaner, more interpretable measure of soundness improvement.

- **No controlled comparison between checkability and correctness-only at matched accuracy.** The correctness-only baseline is evaluated at high-accuracy checkpoints (3k, 7k steps) where legibility is poor, while the checkability-trained prover operates at lower accuracy. Without human evaluation at approximately matched accuracy, the claimed legibility gain could partially reflect that lower-accuracy provers solve easier problems whose correct solutions are inherently easier to check. The paper partially acknowledges this (lines 343–344) but does not provide the controlled comparison needed to resolve the concern.

- **The ratio hyperparameter for mixing previous-round prover data into verifier training is reported as "tuned" but the value is not disclosed.** Lines 144–145 state the mixture "is tuned as a hyperparameter" and line 350 says it was tuned for one verifier size and reused for others, but the actual ratio is never given. This hinders reproducibility of a key algorithmic detail.

### Trivial

- The paper uses GPT-4 to evaluate step-by-step validity (Fig. 5a) without explicitly noting that GPT-4 may share failure modes with the prover/verifier (all are GPT-family). A brief caveat would strengthen the presentation.

## Nice-to-Haves

- A per-solution correlation analysis between verifier score and human judgment accuracy would directly test the transfer claim at the individual-solution level.
- A qualitative rubric-based analysis of what makes checkability-trained solutions more legible (e.g., solution structure, step granularity) would deepen understanding of the mechanism.
- Reporting the rationale for the 45-second time limit would help readers assess task difficulty.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The three data points in Figure 1 are composites from different training runs (Section 4 and Section 4.3)."* — This is standard practice for a summary figure comparing different methods. The caption clearly describes what each point represents. No misrepresentation exists.

- *"Missing related works."* — I cannot verify the existence of missing citations without external sources. The paper's related work coverage of debate, critique, scalable oversight, and CoT is thorough.

- *"Theorem 1 does not provide algorithmic guidance."* — The theorem provides conceptual grounding; the paper explicitly acknowledges the gap between theory and practice (lines 130–131). Conceptual theorems are not expected to provide algorithmic recipes.

- *"Formatting and style nitpicks"* (typos, grammar, capitalization artifacts) — These are parser artifacts from PDF extraction, not author errors.

- *"Missing appendix content, proofs in appendix, or absent references."* — These sections exist in the original submission; the parser strips appendices.

- *"The paper should also cover other domains / additional tasks."* — Scope creep beyond the paper's stated focus on grade-school math.

- *"The paper should report inter-rater reliability."* — Not standard for time-limited binary correctness judgments; a nice-to-have at most.

## Novel Insights

The most notable insight from the review process is that the paper's strongest contribution may not be the human-transfer claim (which is under-supported) but rather the systematic characterization of the legibility tax itself and the demonstration that adversarial training against small verifiers produces qualitatively different solutions — more structured, more checkable — at moderate accuracy levels. The finding that SRC reward works better than CGC or goodharting rewards is practically valuable and suggests that the *relative* (not absolute) convincingness signal and the early penalty for unconvincing solutions are important design choices. The observation that the goodharting baseline does not improve human legibility (Sup. Fig.) is an important negative result that strengthens the case for the role-conditioned training approach.

## Suggestions

1. **Report basic human evaluation statistics** — number of contractors, number of solutions per condition, and error bars (or individual data points) for all human accuracy plots. This is essential for the central claim of human transfer.
2. **Add a direct verifier accuracy metric** — e.g., AUC or accuracy on a balanced held-out test set of correct/incorrect solutions from diverse prover sources, to complement the existing indirect robustness metrics.
3. **Address the matched-accuracy concern** — either by evaluating an earlier, less-accurate checkpoint of the correctness-only baseline with humans, or by explicitly discussing why such a comparison is infeasible and how the current design controls for the concern.
4. **Disclose the mixture ratio hyperparameter value** used for verifier training data, and briefly justify the 45-second time limit choice.

## Score and Decision

The paper addresses a well-motivated and practically important problem. The automated experiments — training dynamics across rounds, verifier robustness against multiple attack types, and the comparison of reward variants — are thorough and provide reasonable evidence that checkability training works as designed. The legibility tax is a useful conceptual contribution, and the ablation studies are valuable for practitioners. However, the paper's central claim about human transfer is weakened by inadequate reporting of the human evaluation: no sample sizes, no error bars, no significance tests. This gap means the most important result is not yet convincingly established. The paper would be significantly strengthened by addressing this before publication. Given the strength of the automated results and the conceptual contributions, and the fact that the human evaluation weakness is addressable (not a fatal flaw in the method itself), the paper merits a borderline-to-accept score.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>