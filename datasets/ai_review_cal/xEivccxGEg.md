- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the evidence I need from the paper itself. Let me produce the consolidated review.

---

## Summary

This paper proposes CMIMP, a population-based training framework for zero-shot coordination (ZSC) in multi-agent reinforcement learning. Its key idea is a meta-agent with shared observation/LSTM layers and separate "sub-decision modules" (one per population member), enabling all K policies to be computed in one forward pass. A surrogate conditional mutual information objective penalizes the Q-values of non-selected modules for the taken action to enforce diversity. Experiments on Hanabi show improvements in zero-shot coordination scores and training efficiency over TrajeDi, MEP, and OBL baselines.

## Strengths

1. **Novel parameter-sharing architecture for population training.** Section 3.1 proposes a hierarchical meta-agent where the observation encoder and LSTM are shared across all K sub-decision modules, while only the small output heads are separate. This design reduces both parameters and per-step computation compared to training K independent agents. Table 4 (visible only as an image) reports training speed improvements and memory reduction that are consistent with this architectural advantage.

2. **Tractable diversity objective for value-based methods.** Section 3.2 introduces a surrogate objective \(\bar{I}(A;U|H)\) (Equation 8) that operates on raw Q-values rather than action probabilities. This circumvents the gradient problem that prevents value-based methods from being used with prior diversity objectives like TrajeDi and MEP, which require differentiable action distributions. The paper identifies a real limitation of prior work and provides a practical solution.

3. **Ablation validates the necessity of the regularizer.** Section 4.4 (Figure 4, described in text) compares \(\alpha=0, 1, 10\). With \(\alpha=0\), Diff Prob rises to 1 (all sub-policies collapse to identical behavior) and Intra-XP drops to 13.44. With \(\alpha=1\), Diff Prob stays low and scores improve. This directly demonstrates that the mutual information term is responsible for diversity and that diversity is necessary for good zero-shot coordination.

4. **Scalability evidence.** Section 4.3 and Figure 3 (image) show that CMIMP's training time and memory remain nearly constant as population size grows, while TrajeDi and MEP scale linearly. This supports the scalability claim and distinguishes the method from prior work.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core empirical claims (efficiency, improved ZSC scores, scalability) are supported by the evidence present, and no verified weakness invalidates them.

### Minor

1. **Notation error in the surrogate objective.** Equation (8) (line 100) and the meta-agent loss (line 138) sum over \(i=1,i\neq j\) where \(j\) is the transition index (\(1\ldots N\)) and \(i\) is the sub-module index (\(1\ldots K\)). The paper defines \(u_j\) as the sub-decision module index for transition \(j\) (line 83). The intended meaning is clearly \(i \neq u_j\) — i.e., exclude the module that produced the action — but the notation conflates a transition counter with a module index. If the implementation literally uses \(i \neq j\), the behavior would be wrong for \(N \neq K\) or when the selected module index does not equal the transition index. This does not affect the conceptual contribution but must be corrected for reproducibility.

2. **Theoretical guarantee does not fully align with the actual surrogate.** Theorem 1 (line 110) proves that decreasing the *chosen* module's Q-value for the taken action (while keeping other modules unchanged) increases mutual information. The actual surrogate objective (Equation 8) penalizes Q-values of *other* modules for the taken action. These are related but not identical operations — the theorem proves the opposite direction from what the loss implements. The paper asserts that increasing \(\bar{I}\) increases \(\hat{I}\) (property 2, line 95) and claims Theorem 1 as support, but the theorem does not directly address the objective being optimized. The diversity mechanism is intuitively reasonable and empirically validated by the ablation study (Figure 4), but the theoretical framing is incomplete where it claims formal justification.

3. **Evaluation limited to a single environment.** All experiments are conducted on Hanabi. While Hanabi is the standard ZSC benchmark and the paper's results are clean within that setting, the paper's claims (e.g., "superiority," generality of CMIMP) would be strengthened by at least one additional environment (e.g., Overcooked, Melting Pot). This limits the breadth of conclusions that can be drawn from the current evidence.

### Trivial

1. **No significance testing or seed variance breakdown.** Table 3 reports standard errors over 5 seeds but does not discuss statistical significance of the differences. The variance for MEP (1ZSC-XP: 14.09 ± 0.38) is substantially larger than for CMIMP (15.73 ± 0.03). A brief discussion of whether the advantage is statistically robust would strengthen the claims.

2. **Exploration asymmetry between CMIMP and baselines.** Section 4.3 notes that TrajeDi and MEP use Boltzmann action selection (because they require differentiable action distributions), while CMIMP uses \(\epsilon\)-greedy. The paper does not discuss whether this asymmetry could affect relative performance. A brief comment justifying why this comparison is fair would be helpful.

## Nice-to-Haves

- Provide wall-clock training time (in addition to environment steps) for a direct practical comparison.
- Release code to close reproducibility gaps (hyperparameters, architecture details would typically reside in an appendix that the parser stripped).
- Add a limitations section discussing: (a) the meta-agent outputs K actions per forward pass, which could become a memory bottleneck for very large K; (b) the surrogate objective is heuristic and may not guarantee diversity in all settings.

## Removed Points

These points were present in the reviewer inputs but are removed after cross-checking against the paper:

1. **"Efficiency comparison is potentially misleading / disingenuous."** — Removed. The harsh critic claimed the 5× reduction in environment steps is "apples-to-oranges." This is incorrect: in traditional population-based training, each of K agents collects its own experience, requiring K× the environment interactions. With CMIMP, the meta-agent plays as a single agent and all K sub-modules learn from the same experience, yielding a real ~K× reduction in total environment steps. The paper's efficiency claim is legitimate and explained by the architecture.

2. **Missing reproducibility details (network architecture, hyperparameters, training schedule).** — Removed. These details would be in the appendix, which the PDF parser strips from all papers. The original submission almost certainly contains them.

3. **Missing related works / code release / limitations section.** — Removed per hard rules: (a) missing related works cannot be asserted without external sources; (b) code release is not required; (c) a limitations section is a presentation choice, not a methodological flaw.

4. **Garbled tables/figures mentioned as issues.** — Removed. Tables 2, 4, 5 and Figures 1–3 are images that the parser cannot render. The authors included them in the original submission; these are parser artifacts.

5. **"Overstates efficiency gain" in introduction.** — Removed. This is a subjective framing judgment, not a verified flaw. The paper's claims about "almost no additional training costs" are contextualized by the experimental results in Table 4.

6. **"The comparison is unfair" regarding Boltzmann vs \(\epsilon\)-greedy.** — Demoted from a serious concern to a trivial mention (kept above). The asymmetry is noted and addressed by the paper (line 208), and for the methods that require differentiable distributions, Boltzmann is the natural choice.

7. **Strength Finder strengths that are generic or conflict with verified weaknesses** — Removed generic strengths ("addressed an important problem," "compatibility evidence") that lack specific, concrete evidence citations.

## Novel Insights

The most interesting pattern across the reviews is the tension between the *conceptual* contribution (the meta-agent design is clean and the efficiency gain is structurally real) and the *presentation* of the formal support (the notation error and mismatch between Theorem 1 and the actual objective). This is a paper whose empirical contribution is stronger than its theoretical framing. The central architectural insight — that sharing the observation/sequence-processing backbone while keeping separate output heads can serve as a population — is straightforward and effective. The surrogate diversity objective is a practical engineering solution to a real gradient problem. The main gap is not in the method's validity but in how carefully the formal apparatus was written up.

## Suggestions

1. Fix the notation in Equation (8) and the meta-agent loss: change \(\sum_{i=1,i\neq j}^{K}\) to \(\sum_{i=1,i\neq u_j}^{K}\) where \(u_j\) is the module index that produced action \(a_j\).

2. Either adjust the statement of Theorem 1 to match the actual objective (or add a second theorem showing that penalizing other modules' Q-values also increases MI), or explicitly acknowledge that the surrogate is heuristic and rely on the empirical ablation for validation.

3. Add at least one additional environment (Overcooked or Melting Pot) to support the generality claims.

4. Include a brief discussion of whether the CMIMP vs. baseline differences in Table 3 are statistically significant given the observed variances.
