Now I have a clear picture. Let me write the final consolidated review.

## Summary

This paper studies Learning from Imperfect Human Feedback (LIHF) by modeling it as a continuous-action dueling bandit problem with corrupted utilities. The authors prove a tight regret lower bound of Ω(d max{√T, T^ρ}) for learning from a ρ-imperfect user (where corruption decays as t^{ρ-1}), even when ρ is known. They then analyze gradient-based algorithms (DBGD and NC-SMD) under arbitrary, agnostic corruption, characterizing a smooth efficiency-robustness tradeoff achievable by tuning the learning rate. As a corollary, they establish the first tight lower bound of Ω(T^{3/4}) for standard DBGD, resolving an open question. Experiments on synthetic and Spotify recommendation data support the theory.

## Strengths

- **Fundamental hardness result for decaying-corruption settings.** Theorem 1 provides a regret lower bound of Ω(d max{√T, T^ρ}) for LIHF with ρ-imperfect users, even when ρ is known. This is the first result showing that decaying (structured) corruption is not fundamentally easier than arbitrary corruption in this setting. The matching upper bound (up to log factors) via a refined NC-SMD analysis with an induction argument demonstrates tightness.

- **Novel analytical framework for gradient-based dueling algorithms under corruption.** The regret decomposition lemma (Lemma 4 in the paper) separates regret into a "regret of decision" component and an "observation error" component by quantifying the gradient bias b_t caused by corruption. This technique, adapted from decision-making in RL, is novel for dueling feedback and may be of independent interest for future research on corrupted dueling bandits.

- **First tight lower bound for standard DBGD.** Corollary 1 (Ω(T^{3/4})) resolves an open question about the minimax optimality of DBGD. The proof constructs a hard instance with linear utility and uses a parallel-world contradiction argument that is both clean and insightful.

- **Efficiency-robustness tradeoff characterization.** The paper rigorously quantifies how DBGD's learning rate controls the tradeoff: decreasing α yields worse corruption-free regret (from O(T^{3/4}) to O(T)) but higher corruption tolerance (from O(T^{3/4}) to O(T)). This is the first formal analysis of such a tradeoff in online learning.

- **Experiments on real-world data.** The Spotify recommendation experiments (17×10^4 songs, d=15) demonstrate that DBGD's performance aligns with theoretical predictions even on discrete, nonconvex action spaces, and that the algorithms are robust to ρ-imperfect user corruption.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Abstract imprecision on the lower bound.** The first abstract states a lower bound of Ω(max{T^{1/2}, C}) (omitting the dimension d) and says it holds "even when the total corruption C is known." The main text (Theorem 1) correctly gives Ω(d max{√T, T^ρ}) for the ρ-imperfect user setting where ρ — not C — is known. While C = Θ(T^ρ) in this setting, the abstract's wording conflates the ρ-imperfect (known ρ) setting with the arbitrary corruption (known total budget C) setting and drops the dimension-dependent factor. This could mislead a reader about the scope of the lower bound. Easily fixable, but reflects imprecision in the contribution framing.

- **DBGD lower bound proof sketch is too terse.** The main-text proof sketch for Corollary 1 (lines 178–180) is only 5 lines and relies on an intuition ("parallel world" contradiction) that would not be convincing without consulting the appendix (Section 8.3). While the appendix contains a thorough version, the main text should give a more self-contained argument.

- **Proof sketch for Lemma 1 (lower bound) is confusing as written.** The corruption strategy in lines 102–114 is described as if the adversary knows θ (which is standard for lower bounds), but the notation and the transition from the KL divergence to the final bound could be clarified. The reader must work through the appendix to fully parse the argument.

### Trivial

- The "efficiency-robustness tradeoff" figures (wrapfigures) are poorly placed and hard to read in the extracted text.
- The appendix redundantly restates definitions already in the main text (e.g., Section 10 repeats corruption and ρ-imperfect definitions from Section 3).

## Nice-to-Haves

- A brief paragraph in Section 4 bridging the lower bound (ρ-imperfect users, known ρ) to the positive results (arbitrary corruption, unknown C) would help readers understand the logical flow: the lower bound shows even the easier setting is hard, motivating algorithms that handle the harder setting.
- Explicitly distinguishing the algorithmic contribution (none — standard DBGD and NC-SMD) from the analytical contribution (the new decomposition and tradeoff quantification) earlier in the paper would improve framing. The current text does this in Section 5 but could do it more prominently.

## Removed Points

- **"Second abstract / foreign content (RoSMID)"** — Removed as a formatting artifact. The extracted text shows a second abstract block at the very end of the file (after all sections, without a closing `\end{abstract}`), mentioning an algorithm "RoSMID" never discussed in the body. This is a parser artifact from extraction of marginal/background content. The paper's body is entirely self-contained and coherent (it analyzes DBGD and NC-SMD, which are correctly defined and referenced throughout). The first abstract accurately describes the paper's content.

- **"Efficiency-robustness tradeoff is just a consequence of tuning existing algorithms"** — Removed because the paper itself acknowledges this: "The key novelty in our results is not about the development of fundamentally new algorithmic techniques, but rather the conduct of more fine-grained analysis" (lines 123–124). This is an analytical contribution, and the paper is upfront about it.

- **Generic strength about "addressing an important problem"** from Strength Finder — Removed as superficial.

## Novel Insights

The reviews collectively surface an interesting observation: the paper's lower bound is proven for a *weaker* corruption model (ρ-imperfect, known ρ) while its positive results apply to a *stronger* model (arbitrary, unknown C). This asymmetry is actually the paper's deepest structural insight — it shows that even under benign, structured, known corruption, the problem remains as hard as the worst-case arbitrary corruption scenario. The fact that the DBGD lower bound (Corollary 1) falls out as a byproduct of the efficiency-robustness tradeoff (rather than a separately constructed hard instance) is also noteworthy and conceptually elegant.

## Suggestions

- Fix the abstract to include the dimension d and clarify that the lower bound is for ρ-imperfect users with known ρ (not arbitrary corruption with known total budget C).
- Expand the proof sketch for the DBGD lower bound (Corollary 1) in the main text to a few more paragraphs, making the parallel-world argument self-contained.
- Add a short bridging paragraph in Section 4/5 explaining why the lower bound (easy corruption) motivates the positive results (hard corruption).

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>