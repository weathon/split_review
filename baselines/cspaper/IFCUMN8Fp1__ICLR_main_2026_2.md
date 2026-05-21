---
job_id: b90e9224-d364-40a4-a881-8276213050c9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: IFCUMN8Fp1.pdf
paper: Towards Learning POMDPs Without Full Observability
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically reinforcement learning, probabilistic modeling, representation learning for partially observable systems, and planning under uncertainty.

## Minimum Quality
Pass ✅. The submission contains all core ingredients of a research paper, including abstract, introduction, methodology/theory, experiments with quantitative results, related work, and conclusion. While I have substantial concerns about clarity, generality, and empirical positioning, these are review-level weaknesses rather than desk-reject-level flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-targeting text, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies learning discrete POMDP parameters from a single action-observation trajectory collected under a memoryless exploration policy, when the agent knows the action and observation spaces but not the latent state space, transition model, or observation model. The core idea is to first learn a linear PSR from a Hankel matrix factorization, then recover a similarity transform via joint diagonalization over full-rank actions so that explicit transition and observation likelihoods can be estimated, in general up to a partition of states that share the same observation distributions over those actions.

The main theoretical claim is that, under ergodicity, rank assumptions on the forward/backward factors, and the existence of full-rank actions, the method recovers partition-level quantities corresponding to a "full-rank observability partition." Empirically, the paper evaluates parameter recovery and planning performance on Tiger, T-Maze, Sense-Float-Reset, and two hallway-style reward-specification domains, comparing against PSRs and an EM baseline.

## Strengths
1. The paper tackles a meaningful problem. There is real value in moving from black-box predictive models such as PSRs to explicit transition and observation likelihoods that can support downstream manipulation of the model, especially reward specification after model learning. That is a concrete and well-motivated gap.

2. The paper makes a nontrivial conceptual connection between two literatures that are often treated separately, spectral/PSR learning and tensor-style latent-state recovery. The framing in Sections 3 and 4, namely that PSRs recover \(O^{ao}T^a\) up to a similarity transform and that this transform can be partially resolved by joint diagonalization over full-rank actions, is technically interesting.

3. The partition-level recovery statement is one of the stronger parts of the paper. Theorem 1 on Pages 5-6 gives a precise target when state-wise identifiability is impossible, rather than overselling full recovery. I appreciated that the claim is explicitly phrased in terms of sums over partition indices in Eqs. (13)-(15), and that **Figure 2** helps make this interpretation concrete for Sense-Float-Reset. In particular, the figure clarifies that the learned coordinates are not state marginals in the usual sense, but quantities that only become probabilistically meaningful after summing over the appropriate block.

4. The running example is useful. **Figure 1** is a good choice because it visually illustrates exactly why the problem is hard: some actions are full-rank, some are not, and multiple states share indistinguishable observation behavior. The node shading for observability partitions is helpful, and it aligns well with the subsequent discussion of full-rank observability partitions in Section 4.1.

5. The empirical section does more than just plot one downstream reward curve. **Figure 3** reports estimated number of states, observation error, transition error, and planner reward across data scales, which is a more complete evaluation than many learning-and-planning papers provide. The comparison to PSR and EM is also sensible at a high level, because they represent predictive and latent-variable baselines with different modeling tradeoffs.

6. The reward-specification experiments in **Figure 4** are a useful attempt to demonstrate why explicit likelihood models matter beyond pure predictive accuracy. Even though I have concerns about the setup, the point being tested is relevant: if the user wants to specify rewards using latent-state semantics after learning, a PSR is awkward whereas an explicit POMDP estimate can support that operation more naturally.

## Weaknesses
1. **The notation and several core equations are inconsistent enough to undermine confidence in the technical presentation.** This is not a cosmetic issue, because the paper's main contribution is theoretical/algebraic. A few examples:
   - On **Page 3, Eq. (4)**, the backward recursion ends with \(T^{o_{t+n}}\cdot \mathbf{1}\), which appears to be a typo and should presumably be \(T^{a_{t+n}}\cdot \mathbf{1}\). As written, the symbol is wrong.
   - On **Page 4**, immediately after Eqs. (7)-(9), the text says the transformed initial belief is \(m_0 = b_0^T P\) and the final vector is \(m_\infty = P\mathbf{1}\), but **Proposition 1** then states \(m_0^T P = b_\pi\) and \(P^{-1}m_\infty=\mathbf{1}\). This flips conventions in a way that is hard to track.
   - The probability expression after Eq. (9), \(\text{P}(o_1,\ldots,o_n)a_1,\ldots,a_n)\), is malformed.
   - In **Theorem 1, Eq. (11)**, the paper writes \(\tilde{O}^{ao}\tilde{T}^{o}\), which appears dimensionally and semantically wrong, and should likely be \(\tilde{O}^{ao}\tilde{T}^{a}\).
   - In **Section 4.3**, the text says "we look to the final vector of the linear PSR after applying the transform \(P'\), e.g. \(Pm_0=P'^{-1}P\mathbf{1}\)," which mixes \(m_0\) and \(m_\infty\).
   
   For a paper whose value rests heavily on similarity transforms and block-structured identifiability, these slips matter. They make it difficult to verify whether the argument is merely badly typeset or whether some of the matrix manipulations are themselves confused.

2. **The statement of what is actually recovered is still murkier than it should be, especially when moving from theory to algorithm.** Theorem 1 says recovery is up to the full-rank observability partition, and Eqs. (13)-(15) carefully define what remains meaningful only after summing over partition blocks. However, the algorithm in **Algorithm 1** returns \(\hat b\) and \(\{\hat O^{ao}\hat T^a\}\) as if these were ordinary state-indexed objects. That is potentially misleading. In the nontrivial partition case, the learned coordinates are not canonical states, and entries within a block are only defined up to an invertible block transform before the final normalization trick. The paper should be much more explicit about what exactly downstream planners consume: true partition-level models, state-indexed surrogates with block-sum semantics, or projected pseudo-probabilities. Right now these are blurred together.

3. **The finite-sample story is underdeveloped, yet the experiments rely heavily on thresholding and heuristic post-processing.** The main results are asymptotic, but the practical method in Appendix B introduces several nontrivial choices: SVD truncation via reciprocal condition number, full-rank action detection via \(\sigma_{\min}\), partition detection via \(\tau_{\text{obs}}\), and a quadratic-programming projection back to probability simplices. These are not minor implementation details, they are part of the estimator. In fact, **Table 1** shows domain-specific parameter choices, and **Tables 2-4** reveal substantial sensitivity to rank thresholds and Hankel size. For example, in **Table 2**, small changes in \(1/\kappa\) can move the estimated rank from correct values to the hard cap of 20. This means the practical success of the pipeline depends quite strongly on hyperparameter tuning, while the main paper largely presents the method as if the algorithmic path from PSR to POMDP were straightforward. The paper needs a clearer separation between the clean asymptotic identification result and the much more heuristic finite-data procedure.

4. **The empirical comparison set is too weak to support broad claims about learning a broader class of POMDPs.** The introduction positions the work against tensor-based POMDP learning methods such as Azizzadenesheli et al. (2016) and Guo et al. (2016), and much of the claimed value is precisely that this method relaxes their uniqueness assumptions. But the experiments do not compare against those methods at all. As a result, the reader never sees whether the proposed method actually improves parameter recovery, robustness, or planning utility relative to the most relevant prior latent-state estimators. Comparing only to PSR and EM is not enough when the paper's main novelty is supposed to sit between PSR learning and tensor recovery.

5. **The experiments are small-scale and somewhat selective, which makes the practical significance hard to judge.** The main paper focuses on Tiger, truncated T-Maze, Sense-Float-Reset, and two three-state hallway variants. These are reasonable didactic domains, but they are all toy problems with tiny latent state spaces. The appendix runtime tables reinforce this concern. **Table 5** shows that for larger Hankel sizes, even T-Maze instances with 10-14 states already become quite expensive, with PSR/POMDP post-processing in the hundreds to \(10^3\) seconds and Hankel estimation itself around \(10^3\) seconds. This does not invalidate the theory, but it does weaken the practical punch of the paper. The current experiments do not show that the method is usable beyond pedagogical settings.

6. **The planning results do not convincingly establish that explicit POMDP recovery is better than PSRs for standard planning, only that it can sometimes support post hoc reward manipulation.** In **Figure 3**, the planner reward curves for learned PSRs and learned POMDPs are described as "similar across all models learned." That is fine, but it also means the paper's strongest practical claim is not standard planning performance. Then in **Figure 4**, the state-reward strategy is only evaluated for learned POMDPs, while observation-reward strategies are evaluated for both PSRs and POMDPs. This makes the comparison somewhat asymmetric: the experiment demonstrates an operation PSRs are not designed to do, rather than a head-to-head planning improvement on a shared task definition. That is a valid use case, but it is narrower than the rhetoric in the introduction suggests.

7. **Several assumptions are restrictive, and the paper does not do enough to delineate the real boundary of applicability.** Section 3.3 assumes ergodicity of the induced \((s_t,a_t,o_t)\) chain under a memoryless exploration policy, full rank of truncated forward/backward factors, and the existence of full-rank actions. Section 4.1.1 argues these can arise in robotics domains with action failure and passive sensing, but the discussion is more anecdotal than convincing. The method excludes many settings where no action has invertible \(T^a\), where informative observations are only available under history-dependent exploration, or where the relevant observability partition depends on actions that are not full-rank. This matters because the paper's title and framing are quite broad, while the actual learnable class remains rather special.

8. **The mathematical exposition around similarity transforms is hard to follow and occasionally appears to swap left/right conventions.** This comes up in Section 3.2 and Appendix A.2. For example, Eq. (7) on **Page 4** writes
   \[
   \mathcal H_{hists^{ao},:}=A_{hists^{-ao},:}\cdot P^{-1}O^{ao}T^aP\cdot V^T,
   \]
   whereas the surrounding text earlier suggests \(A=\textbf{Forw}\cdot P\) and \(P^{-1}\textbf{Back}=V^T\). One can derive the displayed equation, but the paper repeatedly alternates between whether \(P\) maps PSR coordinates to latent-state coordinates or vice versa. Because the recovery algorithm in Section 4 hinges on composing transforms \(P\), \(P'\), \(Q\), and \(R\), the presentation really needs a one-line "coordinate dictionary" to prevent readers from getting lost.

9. **The claim about learning the number of hidden states is not as clean empirically as the presentation suggests.** In **Figure 3**, rank recovery does converge in the shown small domains, but the appendix gives a more sobering picture. **Table 2** shows severe overestimation when the tolerance is even modestly mis-set, often saturating at the maximum number of computed singular values. Since the method uses the PSR rank as the number of states for both the proposed model and the EM baseline, this sensitivity directly affects fairness and interpretability of the downstream comparison. At minimum, the main paper should acknowledge more clearly that state-count estimation is brittle and threshold-dependent in finite samples.

10. **There are presentation issues beyond notation that make the paper feel less polished than it should.** Examples include typographical mistakes ("discuses" in the ethics statement on **Page 11**, "privelaged" on **Page 10**, "summery" in Appendix C.1, malformed indexing in several appendix equations), some confusing prose in the related work section, and occasional awkward phrasing such as "our method can correctly learn partition-level transitions and observations and that these likelihoods are necessary..." on **Page 9**, where the necessity claim is not really established. None of these alone is fatal, but together they add friction to an already dense technical paper.

## Questions
1. The main missing empirical piece for me is a comparison to the tensor-based POMDP learning methods most directly discussed in the introduction, especially Azizzadenesheli et al. (2016) and Guo et al. (2016). Can the authors provide either direct experiments or a careful explanation of why such a comparison is infeasible in the presented domains? A rebuttal that only says the assumptions differ would not fully resolve this, because the paper's contribution is precisely about assumption relaxation.

2. Please clarify the exact semantics of the learned model in the non-singleton partition case. After applying \(\hat P\), are \(\hat b\) and \(\hat O^{ao}\hat T^a\) intended to be interpreted entrywise, or only through block sums over a detected partition? If only through block sums, how is the planner guaranteed to use them correctly when the algorithm outputs state-indexed arrays rather than an explicitly quotient-state model?

3. Can the authors cleanly restate the transform conventions around \(P\), \(P'\), \(Q\), and \(R\), and address the apparent typos/inconsistencies in **Eq. (4)**, **Theorem 1 Eq. (11)**, and the paragraph after **Eq. (9)**? If these are indeed typographical rather than mathematical mistakes, the rebuttal should explicitly provide corrected formulas, because several of them occur at central points in the derivation.

4. The practical algorithm appears quite sensitive to \(1/\kappa\), Hankel size, \(\sigma_{\min}\), and \(\tau_{\text{obs}}\), as seen especially in **Tables 1-4**. How were these selected in the main experiments? Were they fixed per domain using prior knowledge, or chosen by a procedure available to a user who does not know the true number of states or partition structure? This matters for assessing how operational the method is.

5. In **Figure 4**, the state-reward strategy is only available to the learned POMDP model. Can the authors sharpen the claim here? Is the intended takeaway "explicit latent models enable a qualitatively different downstream operation" rather than "the learned POMDP plans better than PSRs"? I would encourage the authors to state this distinction explicitly.

6. The current experiments are all small. Do the authors have any evidence, even limited, on slightly larger synthetic problems where the state partition is nontrivial and at least one action is full-rank? Even one additional experiment beyond the canonical toy domains would increase confidence that the method is not too tightly tailored to the examples in the paper.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies model learning and planning in toy discrete POMDP domains and does not raise specific ethics concerns based on the presented experiments and claims.

## Soundness Rating
2: fair. The core technical idea is plausible and the paper contains substantial derivations and experiments, but the presentation of the math is inconsistent in several places, the finite-sample method relies on multiple heuristics, and the empirical evidence does not fully support the breadth of the claims.

## Presentation Rating
2: fair. The high-level motivation is clear, and some figures help, especially Figures 1 and 2, but the notation, equation consistency, and exposition need significant cleanup for a theory-heavy paper.

## Contribution Rating
2: fair. There is a meaningful idea here, namely recovering explicit POMDP parameters from PSRs up to an observability partition, but the empirical positioning against the most relevant prior methods is incomplete and the demonstrated practical impact remains limited to small domains.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has an interesting core idea and some technically substantive content, but in its current form it falls short of ICLR standards due to clarity issues in the derivations, restrictive assumptions, incomplete empirical positioning, and limited practical validation.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the PSR/POMDP learning area, though the paper's notation inconsistencies make parts of the derivation harder to verify than they should be.