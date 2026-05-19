- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 6, 5, 5
Now I have all the evidence I need. Let me construct the final consolidated review by carefully filtering each claim against the paper text.

---

## Summary

The paper proposes AutoCode4Math, an EM-based framework for math LLMs to autonomously learn when to use chain-of-thought reasoning versus code execution, rather than relying on externally dictated methodology choices. The E-step computes a reference methodology-selection strategy via self-exploration (Monte Carlo rollouts), and the M-step updates the model via off-policy RL on synthesized data. Experiments on three 7B model families (Llama-3.1, Qwen2Math, DeepseekMath) report substantial accuracy gains (e.g., +20% absolute on MATH for DeepseekMath) alongside reduced code execution frequency.

## Strengths

- **Novel EM formulation for autonomous methodology selection**: The paper formalizes the absence of reliable supervision for methodology selection as a latent-variable problem and derives an EM framework (Section 2.2, Eqs. 4–6). This provides a principled alternative to the externally dictated SFT used in prior tool-integrated math LLMs, enabling a self-taught approach where the model learns its own strategy through exploration and refinement. The framing is well-motivated by concrete limitations of existing methods.

- **Large accuracy gains verified by reported numbers**: On MATH, AutoCode4Math raises DeepseekMath-7B from 45.04% to 65.28% (Table 1); on GSM8K from 82.4% to 89.38%. Similar improvements are shown across three model families, with absolute code rates reported alongside accuracy. These improvements are substantial by the standards of math reasoning benchmarks.

- **Ablation studies isolate the EM contribution from RL**: The comparison against "Standard RL" (AutoCode minus the EM formulation, starting from the same checkpoint) shows that AutoCode achieves sustained improvement and higher final accuracy, while Standard RL converges to suboptimal performance with higher code usage (Table 2, Fig. 3). This controlled comparison demonstrates that the EM structure, not just RL, drives the improvement. The standard RL baseline description (line 178) confirms it uses the same off-policy RL approach for parity.

- **Self-reflective synthesis is shown to be important**: The NO REFL ablation (Fig. 2) significantly underperforms the full system, establishing that multi-round responses are a key component of the data synthesis strategy.

- **Analysis of learned strategy provides mechanistic insight**: Section 3.3 introduces an alignment metric comparing the model's methodology choices against an oracle. AutoCode achieves higher strict alignment than standard RL (Fig. 4), explaining the dual benefit of higher accuracy and lower code usage.

## Weaknesses

### Fatal
None.

### Major

- **Main results do not fully disentangle SFT preconditioning from the EM framework.** The paper applies SFT preconditioning (creating "Code4Math" models) to Llama-3.1 and Qwen2Math before applying AutoCode, yet the headline comparisons (Table 1) report improvements against the *original base models*, not against the Code4Math intermediate. This makes it impossible to determine, from the main table alone, how much of the gain comes from the additional SFT data versus the EM loop. The ablation study (Table 2) partially addresses this by comparing AutoCode vs. Standard RL from the same starting checkpoint, and for DeepseekMath (which already natively supports code) the baseline comparison is direct. However, the main results table would be significantly strengthened by including the Code4Math baseline numbers so readers can attribute the gains transparently. This does not invalidate the paper's contribution (the ablation shows the EM effect), but it weakens the headline evidence.

### Minor

- **Gap between theoretical EM guarantees and the practical implementation is not bridged.** The paper claims monotonic improvement via the ELBO (Section 2.2, Eq. 6 and line 86), but the practical implementation replaces the E-step with a hard-max approximation (temperature α=∞, line 160) and modifies the M-step with off-policy corrections and importance-weight clipping (Eq. 10, lines 141–149). The derivation from Eq. 6 to the implemented objective is not provided, and no argument is given that the modified objective still increases the ELBO. This is not unusual for applied ML papers (practical approximations are standard), but the paper should either derive the modified objective as a proper bound or explicitly characterize the method as EM-inspired and remove the unsubstantiated monotonic-improvement claim.

- **Code execution reduction claim lacks explicit baseline code rates.** The paper reports "reducing code executions by up to 90% on GSM8k and 65% on MATH" (line 169) and provides absolute code rates for AutoCode models in parentheses (line 165), but the reader cannot verify the relative reduction without the base model's code execution rate. For models like DeepseekMath that use code by default, the base rate is presumably near 100%, making the relative reduction interpretable. However, the paper should state this explicitly. Other tool-integrated models' code rates are also absent, limiting comparability.

- **Hyperparameter sensitivity is not explored.** No analysis is provided for key hyperparameters: the temperature α (set to ∞, hard-max), the number of rollouts K (=5), or the number of EM iterations. The paper acknowledges this in its limitations (line 219: "we did not extensively explore the influence of hyperparameters related to RL iterations"), but a basic sensitivity analysis would strengthen the claims of robustness.

- **No variance or multi-seed results reported.** Results are reported as single-run point estimates without variance. While single-run evaluation is common in large-scale math LLM benchmarks, reporting at least 2–3 seeds or a note on stability would improve reliability.

### Trivial
- Line 160 contains a typographical issue in the temperature parameter notation ("$x=\infty$" instead of "$\alpha=\infty$").
- The oracle analysis (Section 3.3) defines the oracle post-hoc on the test set—this is acknowledged and used only for analysis, but the discussion of MisAlign cases (line 206) could benefit from concrete examples rather than remaining at the level of abstract reasoning.

## Nice-to-Haves
- Including Code4Math baseline numbers in the main results table (Table 1) for Llama-3.1 and Qwen2Math would fully resolve the attribution concern.
- Adding an ablation that removes the self-exploratory synthesis (keeping only self-reflective) would help isolate each synthesis strategy's contribution.
- A tighter derivation showing the off-policy M-step objective (Eq. 10) as an approximate lower bound on the ELBO, rather than claiming monotonic improvement for the implemented algorithm.
- Explicit discussion of the base code rate used for computing the "reduction" percentages.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

1. **"Existing models lack autonomy claim is overstated"** — The paper's framing of the limitation is reasonable; the distinction between training methodology and capability is precisely the contribution being argued.
2. **"Factorisation assumes conditional independence"** — The paper explicitly discusses (line 37) that methodology selection can be implicit and the factorization is a modeling choice; this is not a weakness.
3. **"How 'native' solutions are generated is unclear"** — The paper clearly defines "native" as "generating complete responses without guiding methodology" (line 132–133).
4. **"Standard RL baseline is unclear"** — The paper states (line 178): "standard RL without explicit methodology-selection, employing an off-policy RL approach for computational parity." Table 2 description confirms it's AutoCode minus EM.
5. **"Standard RL dropping from 82.4% to 80.43% is suspicious"** — I cannot verify the exact number from the text (Table 2 is an image), but even if true, this is not suspicious; standard RL can converge to suboptimal policies — this is precisely the paper's argument for the EM framework.
6. **"Oracle is defined post-hoc"** — The paper explicitly states this (line 200) and uses it only for analysis; this is standard practice and not a weakness.
7. **"Missing related works"** — Per the review guidelines, missing related works are not to be mentioned.
8. **"Practical implementation matches the theory"** (from Strength Finder) — Overstated; the implementation deviates substantially from the theory. Removed from strengths.
9. **"Paper addresses an important problem"** (generic strength) — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The core tension (SFT preconditioning vs. EM contribution) is an experimental design question, not a novel observation about the problem itself. The reviewers' inputs surface useful clarification requests but do not reveal a cross-cutting insight absent from the paper.

## Suggestions

1. **Add Code4Math baseline to Table 1**: Report the accuracy of Code4Math-[ModelFamily] (the SFT-tuned checkpoint before AutoCode training) alongside the original base model and AutoCode. This single change would resolve the main attribution concern and make the contribution of the EM framework fully transparent.

2. **Tighten the theory–practice connection**: Either (a) provide a derivation showing that the off-policy M-step with importance-weight clipping (Eq. 10) approximates a lower bound on the original ELBO, or (b) explicitly drop the "monotonic improvement" claim for the implemented variant and characterize the method as EM-inspired. Option (b) is simpler and more honest.

3. **Report explicit base code rates**: State the code execution rate of each baseline model (e.g., DeepseekMath's code usage rate under its default inference) so that the "reduction" percentages in the abstract and Section 3.1 can be verified directly from the table.

4. **Add hyperparameter sensitivity**: At minimum, show the effect of varying α (the reference strategy temperature) from soft sampling to hard-max, and report results for at least 2 random seeds for the main experiment.
