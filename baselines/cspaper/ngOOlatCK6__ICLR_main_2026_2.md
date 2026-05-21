---
job_id: dd58f8f5-30c8-4944-bd7c-b0fde391cc5b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ngOOlatCK6.pdf
paper: The Minimal Search Space for Conditional Causal Bandits
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within causal reasoning and bandit-based decision making, both well within ICLR scope.

## Minimum Quality
Pass ✅. The submission contains the expected core components, presents a nontrivial theoretical contribution with accompanying proofs and experiments, and while there are notable clarity and evaluation limitations, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies single-node conditional causal bandits, where an agent chooses a node \(X\) and a policy \(g(\mathbf{Z}_X)\) to intervene on that node based on observed context. The main contribution is a graphical characterization of the minimal set of nodes guaranteed to contain an optimal conditional intervention target, called the mGISS, together with a linear-time algorithm, C4, that computes this set from the DAG. The paper also provides proofs connecting conditional-intervention superiority to deterministic atomic-intervention superiority, and reports empirical results showing search-space pruning and improved regret when the pruning is used before a UCB-style node-selection procedure.

## Strengths
1. **The paper tackles a meaningful problem that is distinct from the standard hard-intervention causal bandit setup.**  
   The focus on conditional interventions is well motivated in Sections 1 and 2. In many realistic decision problems, one does not commit to a fixed intervention value in advance, but rather chooses it as a function of observed variables. The paper makes a reasonable case that this setting is not a cosmetic variant of existing causal bandit formulations.

2. **The main structural result is conceptually clean.**  
   The identification of the mGISS through the LSCA closure of \(\mathrm{Pa}(Y)\), stated in **Theorem 13** on Pages 6 and 22, is elegant. The auxiliary characterization via \(\Lambda\)-structures in **Theorem 12** is also helpful, because it gives a more visually interpretable graph property than the recursive closure definition alone.

3. **The algorithmic contribution is simple and potentially useful.**  
   **Algorithm 1 (C4)** on Page 7 is easy to state and, at least at the level of the presented reasoning, plausibly implementable as a preprocessing primitive for larger causal-bandit pipelines. A linear-time routine for extracting the guaranteed-relevant intervention nodes is practically attractive.

4. **Some figures are genuinely helpful for understanding the graph-theoretic intuition.**  
   In particular, **Figure 1(a)-(d)** on Page 5 does useful conceptual work. Figure 1(a) and Figure 1(b) illustrate why merely checking parents of \(Y\) is insufficient, while Figure 1(d) is important because it prevents the reader from collapsing the result to ordinary LCA heuristics. This figure-level progression makes the motivation for introducing strict common ancestors and recursive closure much clearer than the definitions alone.

5. **The connector view gives a nice bridge between theorem and algorithm.**  
   **Figure 2(b)** together with **Definition 14** and **Lemma 15** gives intuition for why C4 can detect closure membership locally through child connectors. This is one of the better-presented parts of the paper, because it explains not just what the algorithm does, but why the local criterion should correspond to the global closure.

6. **The empirical direction is aligned with the paper’s stated goal.**  
   The paper does not try to sell a new bandit algorithm as the main contribution; rather, it argues that search-space reduction is a graph-based preprocessing step. In that sense, the experiments in Section 6 are at least directionally appropriate, especially **Figure 3**, which shows the intended downstream effect of pruning when combined with a simple UCB-style node selector.

## Weaknesses
1. **The mathematical formulation of conditional-intervention superiority has a quantifier/type mismatch that needs to be fixed explicitly.**  
   In **Definition 1, Equation (1)** on Page 4, the paper writes that “for all SCM with causal graph \(G\) there is a policy \(g\) for \(X\) such that for every observable conditioning sets \(\mathbf{Z}_X\) and \(\mathbf{Z}_W\) ...”. As written, this is awkwardly typed: a policy \(g\colon R_{\mathbf{Z}_X}\to R_X\) depends on the chosen conditioning set \(\mathbf{Z}_X\), so \(g\) cannot be existentially quantified before \(\mathbf{Z}_X\) unless the authors formalize a family of policies indexed by the conditioning set. Right now, the definition mixes “there exists a policy” with “for every observable conditioning set” in a way that is not formally well formed. This matters because the whole superiority preorder rests on this definition. If the quantifier order is not precise, then later equivalence and minimality statements are harder to interpret rigorously.

2. **Several mathematical statements in the main text contain notation errors or substitutions that are not minor, because they occur inside central proofs.**  
   A few examples:
   - In **Definition 2, Equation (2)** on Page 4, the quantifier uses \(w \in R_w\), which should presumably be \(w \in R_W\).  
   - In **Theorem 13 proof, part (i)** on Page 22, the line “\(\bar f_Y[B](b,\mathbf n)=\bar f_Y[Z](\bar f_Y[B](b,\mathbf n),\mathbf n)\)” appears malformed. The substituted argument for the blocked assignment at \(Z\) should presumably be something like \(\bar f_Z[B](b,\mathbf n)\), not \(\bar f_Y[B](b,\mathbf n)\).  
   - In Appendix proofs around **Lemma 22** and related notation on Pages 14 and 22, blocked-unrolled-assignment expressions are sometimes written in compressed forms such as \(\bar f_YB\) or \(\bar f_YZ\), which is readable informally but contributes to ambiguity when those equalities are then used in key proof steps.
   
   None of these automatically invalidates the result, but they do reduce confidence in the precision of the theorem statements as presented in the main paper. For a theory-heavy submission, this matters.

3. **The proof strategy relies on existence of maximizers over unrestricted policy classes without stating conditions under which those maximizers exist.**  
   In Section 2, the paper says “We do not impose any restrictions on the function \(g\)” for conditional interventions. But later, in the proof of **Proposition 4** in Appendix D, the argument explicitly introduces \(g^*=\arg\max_g \mathbb E_{\mathbf n}\bar f_Y^{do(X=g(\mathbf Z_X))}(\mathbf n)\). If \(g\) ranges over an unrestricted function class on arbitrary domains, existence of an \(\arg\max\) is not automatic. One can often rescue the argument by replacing argmax with supremum or by restricting to finite domains, but neither is done in the main paper. This is not just pedantry, because the equivalence between conditional and deterministic atomic superiority is one of the core simplifications used to make the rest of the theory go through.

4. **The paper’s treatment of the bandit problem is much less complete than the theory suggests, because the action space induced by conditional policies is effectively infinite, while the experiments instantiate a much narrower setting.**  
   Section 2 defines arms as interventions \(do(X=g(\mathbf Z_X))\) and explicitly imposes no restrictions on \(g\). But the empirical algorithm in Section 6, CondIntUCB, is described as “one UCB per context,” which implicitly assumes discrete contexts and a finite action set \(R_X\). That is a much smaller setting than the one suggested by the formal problem statement. The paper is allowed to evaluate on a restricted case, of course, but then it should be more explicit that the practical experiments only cover finite, tabular conditional policies, not the full class of policies introduced in the theory. Otherwise the experimental support appears broader than it actually is.

5. **The empirical evaluation is directionally supportive but still too thin for the strength of the practical claims.**  
   The main text in Section 6 gives only limited quantitative detail and relies heavily on appendix figures for the broader search-space reduction story. In the main paper, the most visible practical evidence is **Figure 3** on Page 8, which compares cumulative regret curves for “mGISS” versus “brute-force.” These curves do show a consistent separation, and that is a positive sign, but the evaluation has several limitations:
   - It compares only against brute-force search over nodes, not against any stronger or more informed baseline for node elimination.
   - The regret is computed only with respect to **node choice**, as the paper explicitly states on Page 8, not the full conditional intervention including policy quality. This makes the empirical claim much narrower than “better conditional interventions are found faster.”
   - There is no quantitative table in the main paper summarizing regret reductions, convergence time, or confidence intervals numerically across datasets, which makes it hard to judge effect size beyond visual inspection of Figure 3.
   
   In short, the experiment demonstrates that pruning can help a simple procedure, but it does not yet establish a robust downstream benefit across realistic conditional-bandit solvers.

6. **The practical relevance of the conditioning-set assumptions is questionable, and the paper does not stress enough how restrictive they are.**  
   On Pages 3 and 4, the paper assumes observable conditioning sets satisfying
   \[
   \operatorname{An}(X)\setminus\{X\}\subseteq \mathbf Z_X \subseteq \mathbf V\setminus \operatorname{De}(X),
   \]
   together with monotonicity of available context over time, \(W\in \operatorname{An}(X)\Rightarrow \mathbf Z_W\subseteq \mathbf Z_X\). This assumption is convenient for the proofs, but it is much stronger than what many real applications permit. In many domains, not all ancestors are observed, observed values are delayed, or some variables are costly to measure. Since the notion of conditional superiority in **Definition 1** quantifies over “every observable conditioning set,” the result is tied fairly tightly to this observability regime. The theory may still be valid, but the paper should be more candid that the characterization is for a favorable information structure rather than for conditional interventions in general.

7. **The literature positioning is somewhat narrow for a paper that claims to be the first full characterization for non-hard interventions.**  
   The related work section mentions several causal bandit papers, but it gives limited discussion of more recent work on richer intervention classes and broader causal-bandit settings. That does not necessarily invalidate the novelty claim, since the paper’s exact graph-theoretic objective is specialized, but it does make the positioning feel a bit self-contained. In particular, because the paper emphasizes conditional interventions as a major departure from hard interventions, I would have liked a sharper comparison to work handling generalized or soft interventions and a clearer statement of exactly which aspects of those settings remain incomparable to the present characterization.

8. **The exposition in the main paper is reasonably readable at a high level, but the theorem-to-proof pipeline is still harder to follow than it should be.**  
   The intuition on Page 5 is good, but once the paper moves into the proof-heavy appendices, many arguments depend on a dense web of specialized notation: unrolled assignments, blocked unrolled assignments, connectors, \(\Lambda\)-structures, LSCA closure, and multiple superiority relations. A theory paper can of course be technical, but here the accumulation of machinery makes it difficult to verify which assumptions are actually needed for each result. This is exacerbated by occasional notation slips. My concern is not that the paper is too mathematical, but that the mathematical presentation is not yet polished enough for the central claims to be as easy to audit as they should be.

9. **Some practical claims are stronger than the visible evidence.**  
   The abstract says the algorithm “substantially accelerates convergence rates when integrated into standard multi-armed bandit algorithms.” Based on **Figure 3**, the curves do improve, but the experiments only use one fairly simple UCB-style procedure tailored to the authors’ finite-context setup. So “integrated into standard multi-armed bandit algorithms” reads broader than what is directly shown in the paper. A more accurate claim would be that the pruning helps the specific simple node-selection procedure tested here, and is likely compatible with other methods.

## Questions
1. **Please clarify the exact quantifier structure in Definition 1.**  
   Do you mean
   \[
   \forall \mathbf Z_X,\mathbf Z_W,\ \exists g_{\mathbf Z_X}\ \forall h_{\mathbf Z_W},
   \]
   or a single universal policy object that somehow subsumes all admissible \(\mathbf Z_X\)? This needs to be made formally precise because the current statement in **Equation (1)** is not well typed.

2. **Can you explicitly address the existence issue for policy maximizers in Proposition 4?**  
   If the policy class is unrestricted, how do you justify the use of \(g^*=\arg\max_g\)? If the intended setting is finite \(\mathbf Z_X\) and finite \(R_X\), please say so. Otherwise, a supremum-based version of the argument may be needed.

3. **Please check and correct the proof of Theorem 13 in the main text, especially the blocked-assignment substitution.**  
   In the current statement on Page 22, the expression
   \[
   \bar f_Y[B](b,\mathbf n)=\bar f_Y[Z](\bar f_Y[B](b,\mathbf n),\mathbf n)
   \]
   appears inconsistent. If this is just a typographical mistake, please rewrite the step cleanly, because it sits at the core of the superiority argument outside the closure.

4. **How much of the theory truly depends on the strong observability assumption for \(\mathbf Z_X\)?**  
   If \(\mathbf Z_X\) contains only a subset of observed ancestors, or if some ancestors are unavailable at intervention time, does Proposition 4 or Theorem 13 still hold, perhaps with a different minimal set? A careful discussion here would increase confidence in the scope of the result.

5. **Can you provide a more quantitative summary of the empirical gains in the main paper?**  
   For example, for each dataset in **Figure 3**, what is the reduction in regret at fixed horizons, or the reduction in rounds needed to identify the best node with high confidence? A compact table in the main paper would help substantiate the practical claim.

6. **Why is the regret evaluated only for node choice rather than the full conditional intervention?**  
   I understand the desire to isolate the effect of node pruning, but that also narrows the experimental conclusion. If you have results on end-to-end reward or regret over full node-plus-policy decisions, that would strengthen the empirical story materially.

7. **Can you compare against a stronger baseline than brute-force node search?**  
   Even a heuristic baseline based on parents of \(Y\), LCAs, or shallow ancestors would help show whether the exact mGISS characterization is necessary in practice, rather than merely sufficient.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work is primarily theoretical and algorithmic, and the experiments use graphical models and standard benchmark-style datasets.

## Soundness Rating
3: good. The core graph-theoretic idea appears solid and the paper provides substantial formal development, but there are enough definition-level and proof-level imprecisions that I cannot rate the technical presentation as excellent.

## Presentation Rating
2: fair. The intuition and some figures are helpful, but central definitions and proof steps are not polished enough, and several notation inconsistencies make the paper harder to audit than it should be.

## Contribution Rating
3: good. The problem formulation is worthwhile and the mGISS characterization plus linear-time computation are useful contributions, even though the empirical validation is modest and the practical scope is narrower than the strongest claims suggest.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The theoretical contribution is interesting and, if cleaned up, likely worth sharing, but the current version has enough formal imprecision and limited empirical support that I am only weakly positive.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some parts or missed some related work.