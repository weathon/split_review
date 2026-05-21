---
job_id: 76f32436-e617-4c43-b9b3-d4c1fc39bd71
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: b8TlYh6PN6.pdf
paper: Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically causal reasoning, learning theory, and general machine learning, with a strong methodological focus on identifiability and structure discovery.

## Minimum Quality
Pass ✅. The paper contains an abstract, introduction, substantial methodological development, algorithmic section, experiments/results, and conclusion/limitations; it is written in English and presents a technically serious, nontrivial contribution with supporting theory and empirical evaluation, even though some exposition and experimental choices are debatable.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, reviewer-targeted instructions, or suspicious manipulative text in the provided manuscript content.

# Expected Review Outcome:
## Summary
This paper studies distributional equivalence for linear non-Gaussian latent-variable causal models with arbitrary latent structure and cycles. The main claims are a graphical characterization of when two such models are observationally indistinguishable, the introduction of a new graphical/algebraic tool called edge ranks, a transformational characterization for traversing the equivalence class, and a proof-of-concept discovery algorithm, glvLiNG, that aims to recover the equivalence class from data.

At a high level, the paper builds a chain from distributional equivalence, to closure of mixing matrices up to scaling/permutation, to path-rank conditions, to edge-rank conditions, and finally to a local graphical criterion in terms of children bases in Theorem 2, plus admissible graph transformations in Theorem 3. The empirical section includes equivalence-class counting, runtime comparisons, benchmarking against prior latent-variable methods, simulations, and one real-data example.

## Strengths
1. **The scope of the theoretical contribution is unusually broad.**  
   The paper tackles a difficult regime, latent variables, non-Gaussianity, and cycles simultaneously, without the structural restrictions that many prior methods require. If the stated results hold as claimed, this is a meaningful step forward in latent-variable causal discovery, because the paper does not just give another identifiable subclass, it tries to characterize what is and is not recoverable in the unrestricted LiNG setting.

2. **The decomposition of the problem is intellectually clean and well organized.**  
   The progression from Definition 1 and irreducibility in Section 2, to equivalence via path ranks in Section 3.1, to the introduction of edge ranks in Section 3.3, and finally to the local criterion in Theorem 2 is well motivated. In particular, the move from the unwieldy global condition in **Lemma 3, Equation (11)** to the local characterization in **Theorem 2, Equation (19)** is conceptually elegant.

3. **The edge-rank formalism looks genuinely useful beyond this paper.**  
   The introduction of **Definition 4**, **Definition 6**, **Lemma 4**, and especially the duality in **Theorem 1, Equation (16)** is one of the strongest parts of the manuscript. This is not just a proof device. The paper makes a reasonable case that edge ranks provide a complementary graphical language to path ranks, and that this language is more local and more manipulable for equivalence arguments.

4. **There is a nontrivial bridge from theory to algorithms.**  
   Many theory-heavy causal papers stop at characterization. Here, the authors also provide an algorithmic pipeline in Section 5 and Appendix A. Even if glvLiNG is not yet practically mature, the paper at least attempts to operationalize the theory via rank realization and equivalence-class traversal.

5. **The figures help, especially where the theory is abstract.**  
   **Figure 2** is particularly useful. It makes the relationship between path ranks, edge ranks, and diagonal nonzeros in the support matrix concrete, and it directly supports the motivation for introducing edge ranks in Section 3.3. This figure does real explanatory work rather than decorative work.  
   **Figure 3** is also effective in illustrating that the equivalence class is not a tiny perturbation around one graph, but can contain multiple graphs connected by admissible edge additions/deletions and cycle reversals. That substantially clarifies the meaning of Theorem 3.

6. **The runtime results in Table 4 support at least one concrete claim.**  
   Whatever one thinks about the practical use of OICA, **Table 4** does support the narrower claim that the proposed constraint-based construction is much faster than the MILP baseline for the graph realization subproblem. The decomposition into Phase 1 and Phase 2 is also informative, showing that most time is spent in Phase 1, which helps readers understand the computational bottleneck.

7. **The manuscript has a commendable ambition to define the right target of discovery.**  
   I appreciated the repeated emphasis that, in the presence of latent variables, one should first understand the equivalence class before designing a discovery method. That framing is scientifically healthy and gives the work significance beyond the particular algorithm.

## Weaknesses
1. **The main theoretical chain is very dense, and some critical transitions are too compressed in the main paper to inspire full confidence.**  
   The central contribution depends on a long chain of nontrivial statements: **Lemma 1** on closure of mixing matrices, **Lemma 3** on equivalence via path ranks, **Theorem 1** on path-rank/edge-rank duality, **Lemma 5** on equivalence via edge ranks, and then **Theorem 2** and **Theorem 3**. For a paper making “if and only if” claims at this level of generality, the main text is frankly too terse on several crucial proof ideas.  
   The most important example is the jump from the global rank constraints in **Lemma 5, Equation (17)** to the local basis criterion in **Theorem 2, Equation (19)**. The paper says edge ranks “allow Lemma 5 to admit a nice local decomposition” and that it suffices to check singletons, but in the main paper this is asserted much more than explained. Yes, Appendix B ties this to **Lemma 9**, but the burden on the reader is high because Theorem 2 is one of the headline results, and its intuitive content is not unpacked sufficiently in the main text. Since Theorem 2 is the practical criterion replacing an exponential family of checks, this omission matters a lot.

2. **Several mathematical definitions and notational choices are harder to parse than they should be, and some are potentially misleading.**  
   A recurring issue is that the paper uses similar objects, matrix rank, matching rank, path rank, edge rank, bases of a matroid, and “children bases”, in rapid succession, with only limited intuitive separation. For instance, **Definition 6, Equation (14)** defines matching rank through diagonal nonzeros after a permutation, which is fine, but the connection to standard bipartite matching language could be made much more directly.  
   More seriously, **Theorem 2, Equation (18)** defines  
   \[
   \mathrm{bases}_{\mathcal G}(Y) \coloneqq \{Z \subseteq \mathrm{ch}_{\mathcal G}(Y)\cup Y : r_{\mathcal G}(Z,Y)=|Z|=|Y|\},
   \]
   and then uses equality of these families as the deciding criterion. This is a compact definition, but it is not very transparent what information these bases encode in graph terms once \(Y=L\) or \(Y=L\cup\{X_i\}\). The paper does not provide enough concrete worked examples to make this object feel operational rather than symbolic. For a criterion that is advertised as the clean local answer to equivalence, this is a presentation weakness with scientific consequences, because it makes it harder to assess how discriminative or intuitive the criterion really is.

3. **The theoretical assumptions needed by the learning algorithm are strong enough that the empirical claims should be framed more cautiously.**  
   Section 5 states that glvLiNG first runs OICA, then realizes ranks, then traverses the equivalence class, and that under an oracle OICA plus faithfulness it recovers the whole class. That is fair as a theorem statement, but then the practical algorithm inherits the well-known fragility of OICA estimation in finite samples. The paper itself acknowledges this in Section 6, but the empirical positioning still overreaches somewhat.  
   In particular, the paper says glvLiNG is the first structural-assumption-free method for latent-variable causal discovery. That is true in a formal sense under the model, but in practice the method is only as good as an overcomplete ICA step plus a sequence of rank decisions. The discussion of this gap between identifiability theory and realistic estimation is too brief in the main text. This matters because readers may otherwise infer a level of practical readiness that the evidence does not support.

4. **The empirical section is broad but not very sharp, and some evaluations are easier than they first appear.**  
   The paper has many empirical subsections, but several are more illustrative than probative.  
   - **Table 3** reports counts of equivalence classes over small graphs. This is interesting combinatorially, but it does not validate the learning method or the utility of the characterization in realistic settings. Also, the table is difficult to read, and the “stats of #digraphs per class” columns are almost uninterpretable in the current presentation. This is a case where the paper is showing a lot of numbers without extracting a clear scientific takeaway.  
   - **Table 4** demonstrates runtime gains against an MILP baseline, but this baseline addresses the graph-realization subproblem under oracle ranks, not end-to-end discovery from data. So the result is useful but narrower than the surrounding narrative suggests.  
   - **Table 5** evaluates existing methods under oracle access to their tests on arbitrary graphs outside their assumptions. Unsurprisingly, misspecified methods do badly. This does support the paper’s critique of structural assumptions, but it is also a somewhat stacked setup. A stronger comparison would separate “failure due to model misspecification” from “failure due to weaker algorithmic design” more explicitly.

5. **The simulations in the main paper are underspecified, with key details moved out of the main text, and the headline claims are therefore hard to calibrate.**  
   Section 5 only says “full setup and results are provided in Appendix D.4.” The main paper then summarizes trends verbally, for example that glvLiNG does better on denser graphs and is more robust to latent dimensionality. But without the actual full quantitative figure in the main text, or a compact summary table, the reader cannot easily assess how strong or stable these improvements are.  
   Since this is a theory-driven paper, I am not asking for a giant benchmark suite. But if the authors want the algorithmic contribution to count materially, the main paper should show more than one figure-level anecdote and verbal conclusions. The current empirical section feels split between many mini-stories rather than one convincing validation narrative.

6. **Some claims about simplicity and efficiency are a bit too rosy relative to the actual construction.**  
   The paper repeatedly emphasizes that the final criterion is “local” and that the algorithm is “efficient.” There is some truth here, but it risks overselling. Even after the singleton reduction, the algorithm still depends on querying many ranks from an estimated mixing matrix and then solving nontrivial matroid realization subproblems. The appendix makes clear that Phase 1 relies on fairly elaborate matroid machinery, including flats, \(\alpha\)-systems, and dual constructions in **Appendix A.3, Equations (A.17) to (A.19)**.  
   In other words, the criterion is more local than the original exponential characterization, but it is not simple in the way CPDAG criteria are simple. That distinction matters for practical adoption.

7. **The paper would benefit from stronger differentiation between the purely theoretical result and the proof-of-concept algorithm.**  
   Right now, the manuscript sometimes blurs these two contributions. The equivalence characterization is the real centerpiece; the algorithm is an existence proof that the theory can be used. But because Section 5 packages them closely together, readers may evaluate the whole paper through the lens of glvLiNG’s practical readiness, which is weaker. I think the paper would actually be stronger if it more explicitly said: the main contribution is characterization, the algorithm is a first implementation of the target it defines.  
   This matters because otherwise some claims about “recovery from data” sound more mature than the empirical evidence warrants.

8. **The figure-based exposition is helpful in places, but some figures expose how much intuition is still missing from the prose.**  
   **Figure 1** shows reduction to irreducible forms through simple examples. This is useful, but the main text surrounding **Proposition 2** does not fully explain why the specific edge additions in Step 4 preserve equivalence beyond the terse “merge proportional columns” explanation. The figure ends up carrying more intuition than the proposition statement.  
   Similarly, **Figure 3** shows a six-graph equivalence class connected by edge additions/deletions and cycle reversal. The figure supports Theorem 3, but the text does not analyze it deeply enough. For example, which edges are invariant across all six, and which transformations correspond directly to the criterion in **Lemma 7, Equation (20)**? A short worked walkthrough would have made the theorem substantially easier to trust and use.

9. **The real-data case study is interesting but scientifically limited as evidence.**  
   The Hong Kong stock example in Appendix D.5 produces plausible patterns, but plausibility is not validation. Without external ground truth, intervention evidence, or at least stability analyses across time windows and hyperparameters, this part mainly shows that the method can output a graph with a story attached. For a causal discovery paper, that is not enough to substantially increase confidence in practical usefulness.

10. **There are a few exposition and correctness-adjacent rough edges in the appendix that should be cleaned up carefully.**  
   I noticed several typographical or notation inconsistencies in the appendix, for example references like \(A_{X_+}\) in **Assumption 1** that seem underdefined, minor notation slips in basis/cocircuit formulas, and some awkward statements around inclusion/minimality. These may be harmless, but in a theorem-heavy paper they increase the cognitive load and make it harder to verify the argument cleanly. Since the core claims are exact characterizations, polish matters here more than usual.

## Questions
1. **Can the authors provide a more explicit main-text proof sketch of the step from Lemma 5 to Theorem 2?**  
   Concretely, I would like a crisp explanation of why checking \(\mathrm{bases}_{\mathcal G}(L)\) and \(\mathrm{bases}_{\mathcal G}(L\cup\{X_i\})\) for each singleton \(X_i\) is sufficient to capture all constraints in **Equation (17)**. If the essential reason is the matroid augmentation decomposition formalized by **Lemma 9** in the appendix, please explain this more directly in the main paper.

2. **How sensitive is glvLiNG to approximate rank mistakes from OICA?**  
   The appendix describes a sigmoid score based on the minimum singular value and a projection to a nearby valid transversal matroid. This is important, but currently underemphasized. A brief sensitivity study in the main paper, even synthetic, showing how often a few wrong rank decisions change the recovered equivalence class would increase my confidence.

3. **Can the authors sharpen the comparison in Table 5 to make the takeaway fairer?**  
   Since the baselines are intentionally run off-assumption, it would help to report one comparison where the data are within their structural assumptions, and another where they are not. That would clarify whether the paper is showing “our method handles generality” rather than merely “other methods fail when misspecified.”

4. **Can the authors give one end-to-end runtime or scalability summary including the OICA step?**  
   **Table 4** is useful but only isolates the graph-construction stage. Since OICA is a practical bottleneck, an end-to-end timing plot or at least a short discussion of where total runtime goes would make the algorithmic claims more honest and informative.

5. **For Theorem 3, can the authors provide one completely worked transformation sequence between two nontrivially equivalent graphs?**  
   A step-by-step example based on **Figure 3** would help substantially. In particular, I would like to see how one admissible edge addition is certified by **Lemma 7, Equation (20)** in an actual graph, not just in the abstract example text.

6. **What exactly is identifiable about observed-to-observed causal relations across the equivalence class?**  
   The appendix states that ancestral relations among observed variables are invariant. This is potentially a very useful practical takeaway. I suggest elevating this point to the main paper and clarifying whether direct edges among observed variables are ever identifiable beyond ancestry, and under what graphical patterns.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The work is methodological and theoretical. I do not see a paper-specific ethics concern that would require dedicated ethics review beyond standard caution that causal discovery tools can be overinterpreted in consequential domains.

## Soundness Rating
3: good. The paper appears technically serious and the central claims are plausibly supported, but the main-text exposition is too compressed for maximal confidence, and the empirical validation of the learning algorithm is less convincing than the theory.

## Presentation Rating
3: good. The paper is organized and ambitious, and some figures are genuinely helpful, but the exposition is mathematically dense, several key ideas are underexplained in the main text, and some tables are hard to interpret.

## Contribution Rating
4: excellent. The attempted equivalence characterization for linear non-Gaussian latent-variable cyclic models without structural assumptions is a substantial contribution, and the edge-rank perspective looks broadly valuable.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about accessibility and about how far the algorithmic evidence currently goes, but the theoretical contribution is strong enough and broad enough that I think this should be in the conference.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the surrounding causal discovery literature, though fully checking every appendix-level proof detail would require more time than a standard review allows.