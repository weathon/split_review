- Decision: Reject
- Avg Score: 3.60
- Scores: 3, 3, 6, 3, 3
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary
This paper provides the first theoretical convergence analysis for Cyclic Hierarchical Federated Learning (CHFL) under standard assumptions, deriving rates of $\tilde{\mathcal{O}}(1/MNRKT)$ for strongly convex objectives and $\mathcal{O}(1/\sqrt{MNRKT})$ for general convex and non-convex objectives — showing speedup from all hyperparameters ($M$ edge servers, $N$ clients per edge, $K$ local steps, $R$ edge rounds). It also provides insights into optimal client clustering policies based on system settings, and gives partial-participation bounds. Experiments on MNIST demonstrate CHFL's practical performance under controlled heterogeneity.

## Strengths
1. **First theoretical convergence analysis for CHFL** — The paper provides the first convergence guarantees for Cyclic HFL under standard assumptions (strongly convex, general convex, and non-convex), stated explicitly in Theorem 4.1 and Corollary 4.2. This fills a genuine gap: prior work on cyclic patterns was limited to two-layer FL (Li & Lyu 2024; Cho et al. 2023), not the three-layer hierarchical setting.
2. **Convergence rates exhibit joint speedup from $M$, $N$, $R$, $K$** — Corollary 4.2 shows dominant terms with $\tilde{\mathcal{O}}(1/(M N R K T))$ for strongly convex. This is strictly better than prior HFL results (Liu et al. 2020, 2022, 2023) which lacked $M$ and $N$ in the dominant term, as discussed in Section 4.5.
3. **Actionable clustering policy derived from theory** — Section 4.2 provides explicit conditions (e.g., $M < N$ for general convex; $M R^2 < N K^2$ for strongly convex) under which reducing inter-edge heterogeneity $\sigma_g$ is more beneficial than reducing intra-edge heterogeneity $\sigma_c$. This reconciles contradictory prior recommendations (Liu et al. 2020 vs. Mhaisen et al. 2021) and is a concrete, practically useful insight.
4. **Partial-participation analysis** — Section 4.4 derives explicit convergence bounds for randomly selected subsets of edges and clients (Equations 7–8), with sampling-induced terms that are a natural addition to the three-level hierarchical setting.
5. **Honest discussion of limitations** — Section 4.5 acknowledges the synchronous assumption and notes that asynchronous FL in the edge server would be more practical, clearly scoping the contribution.

## Weaknesses

### Fatal
None.

### Major
1. **"Optimal" convergence claim is unsubstantiated** — The paper repeatedly states "our convergence rate is the optimal" (line 72), "achieves the optimal rate" (line 170), and "optimal to date" (line 219), but provides no matching lower bound. The claim conflates "better than existing methods" (which may be true) with "optimal" (which requires a lower-bound proof). Without a lower bound, this is rhetorical overreach. The comparison in Table 1 (not accessible in the extracted text) and the discussion in Section 4.5 relative to prior HFL works are appropriate ways to position the contribution; the "optimal" language goes beyond what the evidence supports.

2. **Experiments do not quantitatively validate the claimed convergence rates** — The paper states in the abstract and Section 5.1 that experiments "validate our theoretical findings," but the experiments:
   - Only report test accuracy, not the optimality gap $f(\mathbf{x}^T)-f(\mathbf{x}^*)$ or gradient norm $\|\nabla f(\mathbf{x}^{(t)})\|^2$, which are the quantities the theory bounds.
   - Vary only $p_c$, $p_g$, and $R$ while fixing $M=10$, $N=50$, $K=2$. The key theoretical speedup in $M$, $N$, and $K$ is not tested.
   - Only show MNIST results in the main text. CIFAR-10 and Shakespeare are listed in the setup (line 182) but no results appear.
   - Lack error bars or multiple-trial statistics.
   
   The experiments demonstrate that CHFL achieves competitive accuracy and that $R$ and heterogeneity levels affect convergence as the theory qualitatively predicts. However, they do not constitute a quantitative validation of the $\tilde{\mathcal{O}}(1/MNRKT)$ rate, which the paper's rhetoric suggests.

3. **Assumption labeling is inconsistent and confusing** — Assumption 3.3 is titled "for Convex Objectives" but the accompanying text (line 58) says it "is used for non-convex cases." Assumption 3.4 is titled "for Non-Convex objective" but the text says it is "for the convexcase" and bounds gradients only at the optimum. The actual assignments in Theorem 4.1 are mathematically correct (weaker assumption for convex settings, stronger for non-convex), but the labels are contradictory, making the paper appear to contain a logical error. This presentation flaw undermines reader trust and needs correction.

### Minor
1. **Notation inconsistency for selected edges/clients** — In Section 4.4, $S$ is the number of selected edges and $P$ is the number of selected clients per edge. However, line 182 writes "selected edges $P=2$" which uses $P$ for edge selection, conflicting with the theory. More critically, the experiments fix the *total number of clients* at 500 with $M=10$ edges, making $N=50$, and use $P=2$ — but it's unclear whether $P=2$ refers to selected clients per edge (2 of 50) or selected edges (2 of 10). The notation is ambiguous.
2. **Limited comparative evaluation** — The experiments compare CHFL against SFL, CFL, HFL, and vanilla FL on MNIST, but only under one setting of $R=2$, $K=2$. The theoretical advantage in $M$, $N$, $R$, $K$ speedup would be far more convincing with experiments showing performance across different values of these parameters.
3. **No statistical uncertainty reported** — Given the stochastic nature of mini-batch SGD and random client/edge selection, results without error bars or confidence intervals make it impossible to assess whether observed differences are significant.

### Trivial
- Several sentences in the extracted text exhibit garbled formatting (e.g., "woconstonts" in Assumption 3.4, "lefean" in theorem statement). If these reflect the original submission, they should be corrected.

## Nice-to-Haves
- An experiment measuring optimality gap or gradient norm under varying $T$ for different $M$, $N$, $K$ values would substantially strengthen the validation of the theory.
- An ablation varying $M$ and $N$ (not just $R$) would demonstrate the claimed joint speedup effect.
- Including results for CIFAR-10 and Shakespeare (which are listed in the setup) would make the experimental section complete.

## Removed Points
These points from the reviewers are removed because they do not withstand verification against the paper:
- **"Partial participation terms are non-standard/suspect"** (Harsh Critic point 4): The critic claims these terms "appear non-standard" and "suspect." In fact, $(N-P)\sigma_c^2/(\mu T P(N-1))$ and $(M-S)\sigma_g^2/(\mu T S(M-1))$ are standard finite-population correction terms arising from sampling without replacement, directly analogous to those in Li & Lyu (2024) and Yang et al. (2021) which the paper cites. There is no basis to call them suspect beyond unfamiliarity.
- **"Assumption–theorem mismatch is a fatal structural error"** (Harsh Critic point 1, fatal framing): The critic claims a "logical contradiction" that would "invalidate the core results." Verified: the mathematical assignments in Theorem 4.1 are correct — the weaker assumption (at optimum, Assumption 3.4) is used for convex cases and the stronger assumption (at all points, Assumption 3.3) for the non-convex case, which is the correct mathematical choice. Only the *titles* of the assumptions are confusing. This is a presentation issue, not a structural error. Downgraded to Major weakness #3.
- **"Algorithm 1 not in main text"**: The appendix is stripped by the parser; this is a known artifact, not a paper deficiency.
- Generic "missing related work" concerns: I cannot verify these without external sources.
- **Strength Finder's generic strengths** about "important problem" and "timely" — these are superficial and removed.
- **Strength Finder's supporting strengths** about "clear separation" and "honest discussion" — these are substantive but too minor to feature as separate strengths.

## Novel Insights
None beyond the paper's own contributions. The critical insight that emerges from synthesizing the reviews is that the paper's theoretical contribution is sound and fills a genuine gap, but is packaged with rhetorical overreach ("optimal") and insufficient evidential support in the experiments. The disconnect between the strength of the theory and the weakness of the empirical validation is the meta-pattern.

## Suggestions
1. **Remove or qualify all "optimal" claims** — replace with "state-of-the-art" or "better than existing methods" unless a matching lower bound is provided. This does not diminish the contribution and avoids a credibility issue.
2. **Fix the assumption labels** — rename Assumption 3.3 as "Bounded heterogeneity at all points (used for non-convex)" and Assumption 3.4 as "Bounded heterogeneity at optimum (used for convex)" so the titles match both the text description and the theorem assignments.
3. **Add at least one quantitative experiment** that measures optimality gap (or at least plots final accuracy vs. varying $M$, $N$, $K$) to demonstrate the claimed speedup. If this is not feasible, soften the "validate our theoretical findings" language to reflect that the experiments verify qualitative predictions rather than the exact rate.
4. **Fix the notation inconsistency** between theoretical $P$ (clients per edge) and experimental "$P=2$" (used for selected edges). Clarify the experimental setup for partial participation.
