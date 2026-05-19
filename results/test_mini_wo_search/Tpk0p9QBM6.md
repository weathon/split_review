Here is my consolidated final review.

## Summary

This paper unifies existing iterative minimum-entropy coupling (IMEC) algorithms (TIMEC, FIMEC) under a partition-based formalism where different instances are defined by different sets of partitions over the sample space. From this framework the authors derive ARIMEC, which uses a prefix-tree partition set to handle arbitrary discrete distributions without requiring factorability, and introduce "merging," a technique that mitigates entropy waste when partition sets are suboptimal. Experiments in Markov coding games and steganography (both information-theoretic and linguistic) demonstrate that ARIMEC enables coupling with non-factorable priors (e.g., GPT-2) and that merging improves robustness.

## Strengths

- **Clean unification of prior IMEC algorithms.** Section 3 formalizes TIMEC and FIMEC as special cases of a single partition-based algorithm (Alg. 3) and proves that the unified form inherits coupling and greediness guarantees (Propositions 3.1–3.2). This provides a principled toolkit for deriving new IMEC variants.

- **ARIMEC is the first IMEC algorithm that handles arbitrary discrete distributions.** The prefix-tree partition set (Section 4.1) aligns with the output structure of autoregressive models and does not require the factorability assumption that limited FIMEC. The MCG experiments (Fig. 2) and linguistic steganography experiment (Fig. 4) show that ARIMEC substantially outperforms the previously available (uniform-prior) FIMEC baseline when the message distribution is non-factorable, directly demonstrating the value of this extended applicability.

- **Merging improves robustness to suboptimal hyperparameter choices.** The merging technique (Section 5) groups realizations that induce identical posterior updates and performs additional couplings on multi-element groups. The experiment in Fig. 6 shows that merging dramatically reduces the entropy growth that FIMEC otherwise suffers as the dimension of \(X\) increases, validating the claim of improved robustness.

- **Efficient implementation techniques for posterior updates.** The paper provides a polynomial-time procedure for lazily computing posteriors of neighboring partitions (Proposition 4.2) and a search algorithm using entropy-based pruning (Proposition 4.3, Alg. 4). These are necessary enablers for ARIMEC given the exponential worst-case size of prefix trees.

- **Honest discussion of limitations and unexpected results.** The paper transparently acknowledges that (a) it does not prove the search procedure's runtime complexity, (b) in the information-theoretic setting FIMEC achieves lower joint entropy than ARIMEC, and (c) the explanation for ARIMEC's lower error rate in that setting is speculative. This candor is commendable.

## Weaknesses

### Fatal
None.

### Major

- **No systematic empirical evidence for ARIMEC's scalability.** The paper claims ARIMEC is "the first algorithm for computing low-entropy couplings for large-support distributions," yet it provides no runtime measurements, node-visit counts, or scaling experiments. The search procedure for maximum-entropy partitions is acknowledged to lack a runtime guarantee (l.364: "we do not formally prove its runtime complexity"). The prefix tree can grow exponentially, and while the paper asserts that the search "often only requires the evaluation of one or two nodes" in practice, no evidence (e.g., plots of nodes visited vs. sequence length \(n\), or vs. alphabet size) supports this claim. Without such data, a reader cannot assess whether ARIMEC is genuinely usable for truly large supports or whether the experiments (\(n=100\), GPT-2) operate in a regime where the search happens to be easy. This gap weakens the paper's central practical claim.

### Minor

- **Merging evaluation is limited.** Merging is tested only with FIMEC on a single synthetic task (transmitting 10 bytes of ciphertext through GPT-2 stegotext, Fig. 6). The paper does not test merging with ARIMEC, nor on the MCG or linguistic steganography tasks. The claim that merging makes IMEC "robust to suboptimal hyperparameter settings" would be stronger with broader validation.

- **The information-theoretic steganography result is not fully reconciled with the paper's narrative.** In this setting (where both methods use the same uniform ciphertext prior), FIMEC achieves strictly lower joint entropy than ARIMEC (Fig. 3). The paper offers a plausible but untested explanation (ARIMEC focuses on early-byte certainty). While the honest reporting is welcome, the fact that ARIMEC is worse on the primary MEC objective (joint entropy) in a setting where it applies merits deeper analysis or a clearer statement of when ARIMEC should be preferred over FIMEC.

- **No limitations section or discussion of failure modes.** The paper would benefit from a brief limitations subsection discussing when ARIMEC might struggle (e.g., distributions with very long-range dependencies where the working prefix rarely concentrates, or settings with extremely large alphabets where the prefix-tree search may visit many nodes).

### Trivial
None.

## Nice-to-Haves

- **Report runtime and node-visit statistics** for ARIMEC across varying sequence lengths \(n\) (e.g., 50, 100, 200, 500) to substantiate the scalability claim.
- **Test merging with ARIMEC**, not just FIMEC, ideally on a realistic task such as the MCG or linguistic steganography setting.
- **Include additional baselines** that also attempt to handle the non-factorable distribution, such as rejection-sampling-based coupling or approximate MEC on a subsampled/aggregated space, to further isolate ARIMEC's algorithmic advantage.
- **Provide a theoretical analysis of merging** that states conditions under which it does not increase joint entropy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Experimental comparisons are not controlled fairly; baselines are straw men"** (Harsh Critic's Issue 2). This criticism claims that comparing ARIMEC (with correct prior) against FIMEC (with uniform prior) is unfair because the improvement could be due to the prior, not the algorithm. However, FIMEC requires factorability of the prior (Assumption 1), and GPT-2 is not factorable — FIMEC *cannot* use the correct prior. The comparison demonstrates the practical impact of ARIMEC's central contribution (extending IMEC to arbitrary distributions) and is therefore appropriate. The information-theoretic steganography result showing FIMEC with lower joint entropy is also honestly reported and does not "undermine" the paper's claims as the critic asserts; the paper never claims ARIMEC dominates FIMEC in all settings. **Reason for removal:** criticism misunderstands the paper's contribution and the constraints on FIMEC.

- **"Overstated gap in Abstract/Introduction"** and **"Section 3 max-entropy intuition is a heuristic"** — The critic suggests alternative heuristics (1-bit approximation on aggregated support, Poisson-process approach) that the paper should have compared against, and notes that the max-entropy selection criterion is heuristic. The paper's claim is about *low-entropy coupling for arbitrary large-support distributions*, which prior work explicitly did not address (as cited). The heuristic nature of the partition selection is also acknowledged in the paper. **Reason for removal:** speculative alternatives and criticism of an acknowledged heuristic.

- **"The prefix tree has O(|X|) edges, making polynomial-time claim questionable"** — The paper's Proposition 4.2 concerns polynomial-time *posterior updates* for neighboring partitions, which is separate from the search procedure's complexity (which the paper does not claim is polynomial). The critic conflates these two claims. **Reason for removal:** misreading of the paper's complexity statements.

- **Various section-by-section nitpicks** (wide confidence intervals despite bootstrap being standard, "no comparison to non-MEME baselines" which is out of scope, "Section 7 conclusion undermined" which is an opinion not a factual error). **Reason for removal:** speculative or scope-creep criticisms.

- **Strength Finder's generic strengths** (e.g., "this paper addresses an important problem") — removed because they are superficial and lack specific evidence. **Reason for removal:** generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the information-theoretic steganography result (ARIMEC achieving lower error rate despite higher joint entropy) is an interesting angle, but the paper already discusses this.

## Suggestions

1. **Add a scalability experiment.** Report the number of partitions evaluated per iteration, the time per iteration, and total coupling time for ARIMEC. Vary the sequence length \(n\) (e.g., 50, 100, 200, 500) and/or the effective alphabet size to demonstrate that the search procedure does not blow up in practice.
2. **Test merging with ARIMEC** on at least one task to establish that the technique works beyond FIMEC.
3. **Add a brief limitations paragraph** acknowledging that ARIMEC's search efficiency is empirical rather than proven, and discussing settings where it may struggle.
4. **Deepen the discussion of the information-theoretic steganography results** — e.g., provide a decomposition of where ARIMEC's conditional entropy is concentrated or test a hypothesis about why its error rate is lower.

## Score and Decision

**Originality:** The unification is novel and the prefix-tree partition set is a clever design that directly addresses an identified limitation.  
**Importance of research question:** Low-entropy coupling has applications in steganography, causal inference, and beyond; extending it to arbitrary distributions is a well-motivated problem.  
**Claims support:** The main claim (ARIMEC handles arbitrary distributions) is supported by experiments, though scalability evidence is weaker than desired.  
**Soundness of experiments:** Experiments are functional but have gaps (no scalability data, limited merging evaluation). Baselines are appropriate given the constraints of prior methods.  
**Clarity of writing:** Clear exposition with helpful visualizations (Fig. 3–6 in the paper).  
**Value to community:** The unified framework and ARIMEC enable new applications, and the code release would facilitate adoption.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>