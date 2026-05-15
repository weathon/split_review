Now I have sufficient information to write the consolidated review. Let me synthesize everything.

## Summary

This paper introduces "checkability training," an iterative Prover-Verifier Game (PVG) approach that trains small LLM verifiers and role-conditioned provers (helpful/sneaky) to produce chain-of-thought solutions that are more legible to both small verifiers and time-constrained humans. The core insight is that optimizing LLM outputs solely for correctness degrades their legibility (a "legibility tax"), and that iterative adversarial training between provers and verifiers can partially recover legibility while maintaining reasonable accuracy. The paper evaluates verifier robustness across multiple attack types and reward formulations, and provides human evaluation data suggesting that legibility transfers from small verifiers to humans.

## Strengths

- **Well-motivated, novel training framework with clear practical relevance.** The iterative PVG algorithm with role-conditioned provers (helpful/sneaky) and a verifier trained on a diverse mixture of past-round solutions is clearly described and addresses a real problem in scalable oversight. The paper compares three reward variants (SRC, CGC, goodharting) and convincingly shows that only SRC produces consistent improvements in both legibility and verifier robustness.

- **Systematic analysis of verifier robustness across multiple independent attack types.** The paper evaluates verifiers against three distinct reward-based adversaries (SRC, CGC, goodharting), showing that the number of RL steps needed to find exploits increases across training rounds (Fig. 6a). The use of sneaky-only provers (without weight sharing with the helpful prover) strengthens the claim that verifier robustness genuinely improves rather than being an artifact of shared weights.

- **Scalability analysis across varying verifier-to-prover compute ratios.** The paper varies verifier size from 10⁻⁴ to 10⁰ times the prover's compute (Fig. 2c, Sup. Figs.), demonstrating that intermediate verifier sizes yield stable checkability training while very small or very large verifiers fail. This provides practical guidance for deploying the method and goes beyond prior PVG work that used fixed model sizes.

- **Empirical characterization of training dynamics.** The observation that sneaky prover exploits become harder to find across rounds, that the helpful prover's accuracy increases, and that balanced best-of-n verifier accuracy improves (Fig. 6b) are solid, well-documented findings that do not depend on human evaluation.

## Weaknesses

### Fatal
None.

### Major

- **Human evaluation data lacks statistical grounding, weakening the paper's headline claim.** The central claim that legibility training "transfers to time-constrained humans" rests entirely on human accuracy data presented in Figs. 1b–d, 3b, and 5b–c. Across all these figures, only mean accuracy values are reported. No error bars, confidence intervals, statistical significance tests, measures of inter-annotator agreement, or sample sizes (number of contractors, solutions per condition, judgments per condition) are provided anywhere in the paper. The observed trends (e.g., ~20pp improvement in human accuracy on helpful solutions, ~10pp decrease on sneaky solutions) are suggestive and the magnitudes are nontrivial, but without uncertainty quantification the reliability of these differences cannot be assessed. This is the single most significant weakness because the paper's title and abstract foreground the human legibility result.

- **The comparison between the correctness-only baseline and checkability training uses different stopping criteria and total optimization budgets that are not fully reported.** The correctness-only prover is trained for a fixed 8k RL steps; the checkability prover uses early stopping that varies by round. The total number of RL steps the checkability prover receives across all rounds is never stated. The paper acknowledges this heterogeneity in its limitations paragraph ("Heterogeneous experiment set-ups") and notes they "do not observe qualitative different between early stopping and non early stopping rounds," but the lack of controlled comparison makes it difficult to disentangle whether the legibility tax reflects a genuine trade-off or simply a difference in total optimization. Reporting total compute/step budgets would substantially strengthen the comparison.

### Minor

- **The synthetic GSM augmentation (100k ChatGPT-generated problems) may affect legibility in ways not validated.** The paper validates that test accuracy is unaffected by synthetic vs. real data, but legibility to humans — which the paper treats as sensitive to solution style and naturalness — is never compared on real-only vs. augmented data. While this is a reasonable concern, it is partially addressed: the paper acknowledges the possibility of incorrect labels in the limitations and notes that verifier accuracy is unaffected.

- **The theoretical result (Theorem 1) assumes an unrestricted class of deterministic mappings, which LLMs do not satisfy.** The authors acknowledge this gap, but the theorem therefore provides limited insight into why the practical algorithm works. The connection between the idealized equilibrium and the empirical coordinate-descent procedure is largely intuitive rather than formally grounded.

- **The SRC reward's -1 penalty for below-average verifier scores is motivated only as "practically useful for convergence" without a targeted ablation.** A systematic study isolating the effect of this design choice (vs. simply using the normalized score without clamping) would clarify whether this is essential to the method's success or a minor implementation detail.

- **Several explanations for observed phenomena are acknowledged as post-hoc hypotheses.** The explanation for CGC underperformance ("spurious statistical clues") and the claim that the helpful prover's end-of-round accuracy drop is "potentially due to weight sharing" are explicitly hedged but not supported by targeted analysis. These do not undermine the paper's empirical findings but leave causal mechanisms unclear.

### Trivial
- The claim that the helpful prover's end-of-round accuracy decrease is "potentially due to weight sharing" (Sec. 4.2) is speculation without supporting analysis (e.g., checking whether the helpful prover's correct solutions are being penalized by the verifier). The paper uses "potentially" which appropriately hedges, but the statement adds little without evidence.

## Nice-to-Haves
- A direct head-to-head comparison of human accuracy on solutions from the correctness-only baseline vs. the final-round helpful prover on matched problem sets with the same annotator pool would be the cleanest test of the paper's central claim.
- A qualitative analysis of what makes a solution "legible" to humans (e.g., examining solutions that humans find easy vs. hard to evaluate) would strengthen the claim that verifier score is a meaningful proxy for human legibility.
- Evaluation on a second dataset (e.g., MATH) would address concerns about generality beyond augmented GSM.

## Removed Points

These points were flagged by reviewers but removed per policy; they should be treated with caution.

- **Strength: "Transfer of legibility from small verifiers to human judges"** — This strength from the Strength Finder conflicts with the verified weakness that human evaluation data lacks statistical grounding. The weakness wins per policy: the evidence for transfer exists but is not rigorous enough to bear the weight of this claimed strength. The underlying observation (human accuracy trends in Figs. 3b, 5b) is reported in the paper but the strength as stated overstates the conclusiveness of the evidence.

- **"The comparison is uncontrolled because human data come from separate experiments with potentially different contractor pools"** (from Harsh Critic Critical Issue 2) — This is speculative. The paper does not state or imply that different contractor pools were used; assuming different pools without evidence is not a valid criticism.

## Novel Insights

The most interesting observation across the reviews — one not fully articulated by the paper itself — is the asymmetry between the helpful and sneaky training dynamics and what it reveals about the nature of legibility. The helpful prover becomes both more accurate and more legible simultaneously, while the sneaky prover becomes less detectable by both verifiers and humans. This suggests that "legibility" is not a single property of the prover but an interaction effect between the prover's output distribution and the verifier's (or human's) discrimination ability. The verifier's increasing robustness seems to drive *both* effects: it forces the helpful prover toward cleaner reasoning (because only clean reasoning consistently earns high verifier scores) while forcing the sneaky prover toward subtler errors (because obvious errors are easily caught). This dual dynamic is the paper's deepest finding and deserves more emphasis than it currently receives.

## Suggestions

1. **Report error bars or confidence intervals for all human evaluation data.** At minimum, report the number of contractors, number of solutions per condition, and whether the observed trends exceed the bootstrap 95% CI. Without this, the human legibility results are not interpretable as evidence.
2. **Report the total number of RL steps (or total compute) used for each training scheme** to allow readers to assess whether the legibility tax reflects a genuine trade-off or a disparity in optimization budget.
3. **Add a targeted ablation of the -1 penalty in the SRC reward** to verify that this design choice is necessary for convergence, or clarify if a simpler reward suffices.
4. **Evaluate on a second dataset** (e.g., GSM8K original without augmentation, or a subset of MATH) to test whether the legibility improvements generalize beyond the specific synthetic-augmented distribution.

## Score and Decision

The paper makes a meaningful contribution: the checkability training framework is novel and well-motivated, the dynamics analysis and multi-attack robustness evaluation are solid, and the concept of a legibility tax is empirically grounded. However, the headline claim about transfer to humans is seriously weakened by the absence of any statistical rigor in the human evaluation. This is not a fatal flaw — the trends are suggestive and the paper's non-human contributions are substantial — but it prevents the paper from fully delivering on its central promise. With strengthened human evaluation and better-controlled comparisons, this would be a strong paper.

**Originality:** 7/10 — PVG for legibility is a novel application; the reward design and iterative training are extensions of prior work.  
**Importance of research question:** 8/10 — scalable oversight is a critical problem; improving legibility is well-motivated.  
**Claims well-supported:** 5/10 — the verifier robustness and dynamics claims are well-supported; the human legibility claim is not.  
**Soundness of experiments:** 6/10 — solid for non-human experiments; human evaluation is weak.  
**Clarity of writing:** 8/10 — well-structured and clear despite parser artifacts.  
**Value to community:** 7/10 — the framework, dynamics analysis, and negative results (CGC, goodharting) are useful.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>