---
job_id: 5dcd42db-4fcd-4123-a444-2875a18b0ccf
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: lbLAgGF8OO.pdf
paper: An Improved Model-Free Decision-Estimation Coefficient with Applications in Adversarial MDPs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in reinforcement learning and learning theory, with a focus on regret analysis, structured exploration, and decision-estimation coefficients for stochastic and adversarial MDPs.

## Minimum Quality
Pass ✅. Although the paper is quite dense and the presentation has real issues, it contains the core ingredients of a serious theory submission, namely a clear problem setup, formal assumptions, algorithmic framework, theorem statements, quantitative result tables, and a conclusion; I did not find a desk-reject-level flaw or missing scientific core section for a learning-theory paper.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect any hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces Dig-DEC, a model-free decision-estimation coefficient that replaces optimism with a purely information-gain-based objective. The framework is used to obtain improved regret guarantees in stochastic MDP settings and, more importantly, the first model-free regret bounds for hybrid MDPs with stochastic transitions, adversarial linear rewards, and bandit feedback. The paper also develops refined online estimation procedures for average estimation error and squared estimation error, leading to improved rates over prior DEC-based methods.

## Strengths
1. The paper tackles a meaningful open problem in theory-oriented RL. In particular, the hybrid setting with stochastic transitions, adversarial rewards, and bandit feedback is a natural and nontrivial regime, and the paper gives a model-free result there, which the introduction correctly positions as missing in prior DEC-based work.

2. The central conceptual move, replacing optimism by a dual information-gain objective, is interesting and well motivated. The discussion around Eq. (7) and Eq. (8) on Page 7 makes clear that the proposed divergence combines posterior information gain with an explicit estimation term \(\overline{D}^{\pi}(\phi\|M)\), and this is more than a cosmetic rewrite of earlier objectives.

3. The framework is broad. The same meta-algorithmic template, Algorithm 1 on Page 6, is instantiated for both stochastic and hybrid settings, and for two different estimation regimes, average-error and squared-error. This kind of unification is valuable in a literature that can otherwise become a zoo of setting-specific arguments.

4. The regret decomposition around Eq. (5) and Eq. (6) is one of the stronger parts of the paper. The decomposition isolates the minimax complexity term and the estimation term \(\mathbf{Est}\), which makes the subsequent structure of the paper natural. Even if some details are deferred, this is a sensible organizing principle for the theory.

5. The paper claims clear rate improvements over prior model-free DEC work, and the summary tables are useful for seeing the intended scope. In particular, **Table 1** on Page 9 and **Table 2** on Page 10 show that the authors are not selling a single isolated theorem, but a family of consequences across bilinear classes, Bellman-eluder style settings, and coverability-based settings, in both stochastic and hybrid regimes. Even though the tables have formatting problems, they still convey the breadth of the applications.

6. The comparison with prior complexity notions in Section 6 is a real strength. **Theorem 13** gives a generic relation between Dig-DEC and optimistic DEC, while **Theorem 14** gives a toy separation showing that the extra KL information-gain term can matter qualitatively, not just by lower-order constants. This helps the paper make the case that the new complexity is not merely another notation layer.

7. The paper does include an explicit visual aid for the hybrid partitioning story. **Figure 1** in Appendix B is simple, but it does help interpret Assumption 2: infosets are policy-specific slices that group transitions while ranging over all rewards. This is exactly the kind of picture the main text needs, because the hybrid partitioning over \(\mathcal{P}\times\mathcal{R}\times\Pi\) is easy to get lost in otherwise.

## Weaknesses
1. The presentation in the main paper is substantially weaker than the technical ambition of the work, and at several points the paper becomes harder to evaluate than it should be. A concrete example is **Algorithm 1** on Page 6, where the update is written as \(\rho_{t+1}=\textsc{PosteriorUpdate}(\nu_t,\rho_t,\pi_t,o_t)\) and is described as “Eq. (4)”, but **Eq. (4) does not actually appear in the main paper**. This is not a cosmetic typo, because the posterior update is central to the whole method and to the meaning of the estimation term in Theorem 6. Similarly, **Theorem 7** on Page 7 is stated for “Algorithm 4 with Algorithm 2 as PosteriorUpdate,” but **Algorithm 4 is only in the appendix**, not the main paper. For a theory paper, deferring long proofs is fine, but deferring the operative algorithmic object is much less fine.

2. There is a nontrivial mismatch between the headline claim and the theorem actually stated in the main paper. The abstract says, “**Dig-DEC is always no larger than optimistic DEC**,” which is a very strong dominance statement. However, the main comparison theorem, **Theorem 13** on Page 10, only states
\[
\mathrm{dig\text{-}dec}_{\eta}^{\Phi,\overline{D}} \le \mathrm{o\text{-}dec}_{\eta}^{\Phi,\overline{D}} + \eta.
\]
That is an additive-\(\eta\) comparison, not “always no larger” in the literal sense. Maybe the authors intend this as effectively equivalent after tuning \(\eta\), but that is not what is written. For a paper whose central selling point is a new complexity notion, this distinction matters. At minimum, the abstract and introduction should be made mathematically precise and consistent with the theorem statement.

3. There are notation and definition inconsistencies in the core formal development. In **Eq. (8)** on Page 7, the definition of Dig-DEC first writes \(\max_{\nu\in\Delta(\Phi)}\), and then in the next line rewrites the objective with \(\max_{\nu\in\Delta(\Psi)}\). This is not a harmless detail, because \(\Phi\) and \(\Psi\) are different objects, the former being infosets and the latter the union of pairs \((M,\pi)\). The world distribution \(\nu\) is a central player in the minimax problem, so ambiguity about its domain muddies the meaning of the complexity itself. There are similar rough edges elsewhere, for example **Definition 9** on Page 8 ends with “\(M\in\mathcal{M}^3\),” which appears to be a typo but again affects readability in a section defining Bellman completeness.

4. The assumptions for the hybrid setting are strong and the main paper does not do enough to help the reader understand the scope. **Assumption 2** and **Assumption 3** on Pages 4 to 5 are the backbone of the hybrid result, yet they are hard to parse from the main text alone. The authors explicitly say that **Figure 1** helps understand Assumption 2, but that figure is in the appendix, not in the main paper. Since the final judgment should rest on the main paper, this is a problem: the hybrid contribution is one of the main advertised outcomes, but its key structural assumption is explained in a way that is too compressed for a broad ICLR audience. This matters scientifically because the practical meaning of the partition \(\Phi\), and what classes it truly covers or excludes, is part of the contribution.

5. The results tables are useful, but the formatting is bad enough that they undercut the paper’s empirical-summary role. For example, in **Table 1** on Page 9, several regret expressions appear mangled, such as entries resembling \(T^{5/3}\), \(T^{1/9}\), or \(T^{3/3}\) in places where, from the surrounding text, one strongly suspects the intended rates are \(T^{2/3}\), \(T^{7/9}\), or \(\sqrt{T}\). **Table 2** on Page 10 has similar issues. Since these tables are the main compact summary of the paper’s applications, poor formatting here is not a minor LaTeX nuisance. It materially hinders checking which rates are actually proved in which setting, and therefore weakens the paper’s ability to communicate its claimed improvements over prior work.

6. The paper is theory-heavy, which is fine for ICLR, but the experimental or illustrative validation is still fairly minimal relative to the boldness of some claims. Beyond the toy separation in **Theorem 14** on Page 10, there is no computational experiment, numerical study, or even a worked small-scale example demonstrating how the Dig-DEC-driven policy differs behaviorally from optimistic E2D in a more realistic MDP. I am not asking for benchmark RL experiments if the submission is intended as pure theory, but some additional concrete illustration in the main paper would have made the claims much more digestible and credible to non-specialists. Right now, the results are almost entirely theorem-and-table based.

7. The mathematical role of the estimator terms is not always as transparent as it should be. For example, in **Theorem 7** on Page 7, the estimation divergence is defined as
\[
\overline{D}^{\pi}_{\mathrm{av}}(\phi\|M)
=
\max_{j\in[N]}\frac{1}{B^2H}\sum_{h=1}^H
\left(\mathbb{E}^{\pi,M}[\ell_h(\phi;o_h)_j]\right)^2,
\]
while the update procedure later uses aggregated estimators \(L_k(\phi)\) built from split batches. The connection is there, but it is hard to follow in the main text because the authors mix the high-level regret statement with objects whose precise statistical behavior is mostly postponed. Likewise, **Assumption 6** on Page 8 is rather intricate, involving \(\xi_h\), \(\mathcal{T}_M\), and a quadratic dominance condition, but the paper gives limited intuition for why this assumption is the right one and in what sense it is close to standard Bellman completeness rather than a specially engineered device for the proof.

8. The computational status of the algorithm is largely abstracted away. The paper is upfront that “model-free” does not mean computationally efficient, which is good, but **Eq. (3)** on Page 6 still requires solving a minimax problem over \(\Delta(\Pi)\) and \(\Delta(\Psi)\), and the paper gives little guidance about whether this is purely existential, oracle-based, or reducible in common settings. That does not invalidate the theory, but it does limit the practical reach and should be discussed more candidly in the main paper, especially because the term “algorithm” can otherwise be misleading to readers outside the immediate theory community.

9. The comparison to prior work is generally solid, but some claims would benefit from tighter attribution and sharper boundary-setting. For instance, the paper repeatedly contrasts Dig-DEC with optimistic DEC and model-based DEC, but the exact source of each improvement sometimes blends together two distinct contributions: the new complexity notion and the improved estimation procedure. In **Section 6**, the comparison to optimistic DEC is conceptually about the complexity, while several entries in **Table 1** and **Table 2** reflect gains that also come from the new estimator analysis. The paper should separate these more cleanly; otherwise readers may over-credit Dig-DEC itself for improvements that partly come from better control of \(\mathbf{Est}\).

## Questions
1. The abstract says Dig-DEC is always no larger than optimistic DEC, but **Theorem 13** only shows
\[
\mathrm{dig\text{-}dec}_{\eta}^{\Phi,\overline{D}}
\le
\mathrm{o\text{-}dec}_{\eta}^{\Phi,\overline{D}} + \eta.
\]
Can the authors clarify whether a true pointwise inequality without the additive \(\eta\) term is intended, or should the abstract/introduction be weakened?

2. Please clarify the domain of \(\nu\) in the Dig-DEC definition in **Eq. (8)**. The equation appears to switch between \(\Delta(\Phi)\) and \(\Delta(\Psi)\). Which one is correct, and does any theorem depend on this choice?

3. Can the authors make the main-paper algorithm self-contained? In particular, **Algorithm 1** references an absent “Eq. (4)” and **Theorem 7** relies on **Algorithm 4**, which is only in the appendix. A rebuttal clarifying the exact main-text update rule and how Algorithm 1 specializes in Theorem 7/Theorem 11 would increase my confidence.

4. For the hybrid setting, can the authors provide a more explicit main-text interpretation of **Assumption 2** and **Assumption 3**? A concrete two-state or linear-MDP example showing exactly what belongs to one infoset \(\phi_{\pi,f}\) would help a lot. Right now, the theory may be correct, but the scope is too opaque.

5. Please provide a cleaned and unambiguous version of **Table 1** and **Table 2** in the rebuttal, with all \(T\)-dependences typeset correctly. These tables are central to understanding what is actually improved.

6. In the comparison with prior work, could the authors disentangle which gains come from the new complexity notion versus which gains come from the improved estimator bounds on \(\mathbf{Est}\)? A short “source of improvement” table would be useful.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The technical direction appears sound and the claims are backed by substantial formal development, but there are enough presentation-level ambiguities in the core definitions and theorem-to-algorithm mapping that I cannot rate soundness as excellent from the main paper alone.

## Presentation Rating
2: fair. The paper is readable for experts, but several important definitions, algorithmic details, and even headline tables are insufficiently polished, and some main-text dependencies are pushed to the appendix in a way that hurts self-containedness.

## Contribution Rating
3: good. The hybrid bandit-feedback result and the Dig-DEC perspective make this a meaningful contribution to DEC-style RL theory, though the paper stops short of the level of clarity and crispness that would make the contribution feel fully convincing to a broader ICLR audience.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is a strong theory paper with a real contribution, especially for model-free learning in hybrid MDPs, but the main-paper exposition is rougher than it should be and some core claims are stated more strongly than the theorems shown. I lean positive because the underlying contribution seems meaningful and technically substantive, but I do not think this is an easy accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main technical concerns I raised, though this is a dense theory paper and I did not line-by-line verify every appendix proof.