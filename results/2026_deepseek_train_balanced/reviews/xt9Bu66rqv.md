## Summary

This paper presents a dual-RL framework that unifies a broad class of offline RL and imitation learning algorithms (IQLearn, XQL, CQL, SMODICE, etc.) under Lagrangian duality of regularized policy optimization. Leveraging this unification, the paper identifies two limitations and proposes fixes: (1) ReCOIL, a discriminator-free offline IL method that removes the coverage assumption required by prior methods, and (2) $f$-DVL, a family of offline RL methods that replace XQL's unstable Gumbel loss with more stable polynomial surrogates. ReCOIL shows strong empirical gains in low-coverage and high-dimensional manipulation settings; $f$-DVL is competitive with prior RL methods while improving training stability.

## Strengths

- **Genuine unification of diverse algorithms under dual RL**: The paper systematically shows that IQLearn, IBC, CQL, XQL, OPOLO, SMODICE, DemoDICE, and others are instances of dual formulations of regularized policy optimization. Table 1 provides a structured taxonomy mapping each method's dual variable type, gradient strategy, and off-policy data handling. This goes beyond prior unification work (Nachum et al., 2020) by incorporating XQL and CQL/ATAC — methods whose connection to regularized policy optimization had been unrecognized.

- **ReCOIL decisively solves a real problem in offline IL**: The paper identifies that prior off-policy IL methods (SMODICE, DemoDICE) rely on a restrictive coverage assumption and a learned discriminator. ReCOIL eliminates both through a mixture-distribution matching objective (Theorem 1). The empirical validation is compelling: in the challenging random+few-expert setting where the coverage assumption breaks down, SMODICE collapses to 2.28 on halfcheetah while ReCOIL achieves 76.92; on dexterous manipulation tasks (pen, door, hammer, relocate), ReCOIL achieves 67–125 where all baselines score below 35.

- **$f$-DVL provides a principled fix for XQL's training instability**: Proposition 3 identifies XQL as a dual-V problem using reverse KL divergence (exponential Gumbel loss). By substituting low-order polynomial surrogate functions corresponding to other $f$-divergences, $f$-DVL eliminates the instability while retaining strong performance. Proposition 4 provides a theoretical guarantee that this family of implicit maximizers converges to the supremum as $\lambda\to 1$.

- **Identification of evaluation inconsistency in prior XQL work**: The paper notes that the original XQL paper reported best-average-return during training rather than the standard last-iterate evaluation, and provides corrected results under the standard protocol. This is a useful methodological correction for the community.

## Weaknesses

### Fatal

None.

### Major

1. **Structural duplication across Sections 4–6 and 7–8**: Sections 4.1 and 7.1 cover identical theoretical ground — same equations, same derivation of IQLearn, same discussion of the coverage assumption. Sections 5 and 7.2 both describe ReCOIL, including the same restatable theorem. Sections 6 and 8.1 both describe $f$-DVL, including the same proposition and surrogate function choices. The exact same results appear as "proposition" in Sections 4–6 and "lemma" in Sections 7–8. A reader encountering the same derivations twice will reasonably question whether the paper is padded. This needs major restructuring: merge into a single coherent exposition.

2. **Overstated claims about $f$-DVL's RL performance**: The conclusion states "$f$-DVL and ReCOIL both outperform previous methods in online/offline RL and offline IL domains." ReCOIL's IL results strongly support outperformance, but the $f$-DVL RL results in Table 2 are mixed. On hopper-medium-v2, XQL(r) scores 68.5 while $f$-DVL ($\chi^2$) scores 63.0 — XQL(r) is clearly better. On antmaze-medium-diverse, IQL scores 70.0 vs. $f$-DVL (TV) 60.2. Many results are essentially tied (halfcheetah-medium-v2: all methods 47.4–48.3). $f$-DVL is competitive and improves stability, but the claim of uniform outperformance is not supported. The abstract's more measured phrasing is accurate; the conclusion should be calibrated.

3. **CQL/ATAC unification — a headline contribution — is not stated in the main paper body**: Line 216 claims CQL and ATAC can be cast as dual-Q problems via Proposition thm:CQL, but this proposition appears nowhere in the main text (deferred entirely to the appendix). Since bringing together pessimistic value learning under the dual-RL umbrella is one of the paper's advertised contributions, the main paper should at minimum state the proposition. Deferring a headline claim entirely to the appendix undermines a core contribution.

### Minor

1. **Online experimental results are incompletely presented**: The "Additional Experiments" subsection (lines 658–666) begins describing an online comparison but the sentence is truncated mid-phrase. Since the paper focuses primarily on offline settings this is not fatal, but the presentation should be finished.

2. **No ablation on the mixture ratio $\beta$ in ReCOIL**: The hyperparameter $\beta \in (0,1)$ controls the mixture between the policy's visitation and the suboptimal data. The paper provides no analysis of its sensitivity, making it difficult to assess whether ReCOIL's strong results are robust to this choice.

3. **No guidance on choosing between $\chi^2$ and TV variants of $f$-DVL**: The two variants perform similarly on most tasks but diverge on some (e.g., hopper-medium-expert: $\chi^2$ = 105.8 vs. TV = 93.3; antmaze-large-play: TV = 41.7 vs. $\chi^2$ = 36.0). The paper presents them as interchangeable without analysis of when one should be preferred.

### Trivial

None.

## Nice-to-Haves

- An ablation on $\beta$ sensitivity would strengthen ReCOIL's empirical evaluation.
- A deeper analysis of *why* ReCOIL succeeds where discriminator-based methods fail — e.g., a controlled experiment isolating the coverage-assumption failure from finite-sample discriminator error.
- Including DEMODICE directly (the paper justifies its absence, making this scope creep, but a direct comparison would strengthen the evaluation).
- Analyzing the regimes where $\chi^2$ vs. TV divergence is preferable for $f$-DVL.
- Varying the number of expert trajectories in the few-expert setting to further characterize ReCOIL's data efficiency.

## Removed Points

- **"ReCOIL = dual-RL objective + existing optimization tools"** — This is a characterization, not a weakness. Using standard optimization machinery for a new objective is standard practice.
- **"Fig 6 referenced but not visible"** — The figure exists in the paper; the image is not extractable from the text dump. Not a weakness.
- **"Missing DEMODICE baseline"** — The paper justifies this via citation to prior results; per scope rules this is not a valid weakness.
- **"Notational inconsistency"** — Too vague and unspecified to constitute a concrete weakness.
- **"The few-expert setting is under-analyzed"** — Moved to Nice-to-Have; it is an interesting direction for further study, not a flaw in the present analysis.
- **Generic sycophantic strengths** about "addressing important problems" — Removed as non-specific.

## Novel Insights

None beyond the paper's own contributions. The most interesting observation from synthesizing the reviews is an asymmetry: ReCOIL (offline IL) shows decisive, unambiguous wins across the board, while $f$-DVL (offline RL, where the field is more mature) is competitive but not clearly superior. This suggests the dual-RL framework's main impact may be in IL, where the coverage-assumption bottleneck was real and restricting, while in RL the existing methods were already close to optimal within the regularized-policy class. The paper would benefit from explicitly acknowledging this pattern.

## Suggestions

1. **Major structural revision**: Merge Sections 4–6 into Sections 7–8, keeping only the fuller treatment. Remove duplicate restatable environments.
2. **Calibrate the conclusion**: Soften the claim about $f$-DVL to reflect that it is competitive with prior RL methods while being more stable.
3. **Add the CQL proposition to the main text** or at minimum state the result explicitly rather than deferring it entirely to the appendix.
4. **Complete the online experiments section** — the truncated sentence suggests the paper was submitted in draft form.
5. **Add a $\beta$ sensitivity analysis** for ReCOIL, even if brief.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>