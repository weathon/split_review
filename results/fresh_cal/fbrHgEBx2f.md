Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes "diminishing exploration" (DE), a mechanism for piecewise-stationary multi-armed bandits that reduces the exploration rate within a stationary segment as time progresses. The key insight is that by spacing exploration rounds further apart within a segment, the algorithm avoids needing to know the number of change points \(M\) — a requirement of prior active methods. When combined with M-UCB or GLR-UCB change detectors, the paper proves \(\tilde{\mathcal{O}}(\sqrt{KMT\log T})\) regret bounds and provides simulations showing competitive or better empirical regret against uniform-exploration baselines and against MASTER (another \(M\)-agnostic method). An extension to track only optimal-arm changes (replacing \(M\) with \(S\)) is also provided theoretically.

## Strengths

1. **Near-optimal regret without knowledge of \(M\) and low complexity.** Table 1 shows that M-UCB(DE) achieves \(\tilde{\mathcal{O}}(\sqrt{MKT})\) regret, requires no knowledge of \(M\), and maintains \(\mathcal{O}(KT)\) complexity — matching the best active methods while being segment-knowledge-free.

2. **Provable \(\tilde{\mathcal{O}}(\sqrt{KMT\log T})\) regret for both M-UCB and GLR-UCB with DE.** Corollaries 1 and 2 provide rigorous theoretical guarantees that the diminishing exploration mechanism yields near-optimal regret when paired with two different change detectors, without requiring \(M\) as input.

3. **Consistently lower regret and computation time than MASTER (another \(M\)-agnostic method).** The "Regret and Execution Time" experiments (Figures ComM50, ComM5, ComBigT) show that M-UCB(DE) achieves lower regret than MASTER across all three scenarios tested, and the computation-time ratio grows faster than \(0.5\log T\) and appears linear in \(T\) (Figure ratio_plot).

4. **Works with multiple change detectors.** The paper demonstrates empirically (Figures 3a–d) and theoretically that DE can be combined with M-UCB, GLR-UCB, and CUSUM-UCB, showing the mechanism is not tied to a specific detection method.

5. **Empirical validation on a real-world dataset.** Figure 3d shows competitive performance on the Yahoo! benchmark with \(M=9\) and \(K=6\), supporting practical relevance.

6. **Robustness when segment-length assumptions are violated.** The paper explicitly tests scenarios violating Assumptions 2 and 3 (e.g., \(M=100\) in Figure 3b) and shows DE still outperforms uniform-exploration baselines, which is a nontrivial stress test.

## Weaknesses

### Fatal
None.

### Major
1. **Baseline tuning details are underspecified, undermining the empirical comparison.** The paper states that "adjustments to the exploration parameter settings are required based on the size of \(M\) when using a constant exploration rate" (Section 6), implying that the baselines (M-UCB, CUSUM-UCB, GLR-UCB) were not re-tuned per \(M\) value. Since these baselines are *designed* to use knowledge of \(M\) to set their exploration rates, comparing them with a fixed (suboptimal) exploration rate against DE (which adapts automatically) stacks the deck. The paper does not clarify how baselines were configured for each \(M\), making it impossible to tell whether DE's advantage reflects genuine algorithmic superiority or simply poor baseline tuning. This is the most significant weakness because the paper's headline empirical claim — that DE matches or beats methods that *know* \(M\) — depends on this comparison.

### Minor
1. **"Minimal knowledge" claim is slightly overstated.** The abstract and introduction emphasize that the algorithm "eliminates the need for knowledge about \(M\)" and operates with "minimal knowledge of the environment." However, the M-UCB integration requires **Assumption 1** (knowledge of a lower bound \(\delta\) on the minimum change magnitude) to set detection parameters \(w\) and \(b\) (lines 238–247). The paper does disclose this in Section 4.1 and notes \(\delta\) may be derived from historical data, but the front matter does not qualify the claim with this requirement. A reader could reasonably infer that *no* prior knowledge beyond \(T\) and \(K\) is needed. This is a presentation gap, not a technical flaw.

2. **Regret comparisons against AdSwitch, ArmSwitch, and META are entirely absent.** The paper positions these as competing \(M\)-agnostic methods in the introduction and Table 1, but the only \(M\)-agnostic method compared in regret is MASTER. The paper acknowledges they are too slow for large \(T\) (line 437), but does not provide results for smaller \(T\) (e.g., 5000, 10000) where they might be tractable. Without any regret comparison, the claimed superiority over these methods is unsupported.

3. **Extension to optimal-arm switches (\(S\)) is introduced but never empirically evaluated.** Section 5 provides a skipping mechanism and proves regret bounds scaling with \(S\) instead of \(M\) (Corollaries 3, 4). No simulation results are provided for this variant, making the extension feel incomplete. Even a simple synthetic experiment comparing the basic version with the skipping version would substantiate the claim that the theoretical improvement translates to practice.

4. **The pseudocode (Algorithm 1) references "if CD = True" without specifying the detection rule inline.** The reader must consult the separate detector algorithms (Algorithms for CD_alg and GLR CD_alg). While these are in the paper, the main algorithm's presentation is less self-contained than it could be.

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis for the parameter \(\alpha\) would help practitioners understand its empirical effect.
- Variance bands or error bars on the regret plots would strengthen confidence given the 100-trial design.
- The CUSUM-UCB variant with DE is evaluated empirically but not theoretically analyzed; noting this explicitly would clarify the theoretical scope.

## Removed Points
These points were identified by the reviewers but are removed for the reasons stated:
- **"MASTER is included only in computation-time plots, not regret plots"** (Harsh Critic Point 3, sub-claim): Removed because the paper's "Regret and Execution Time" section explicitly states "our algorithm almost always achieves the lowest computation time **and regret** in all the scenarios" when compared to MASTER (line 393). Figure 4 (ComM50, ComM5, ComBigT) shows regret alongside computation time. The critic was incorrect on this specific point.
- **"Complexity column uses inconsistent units"** (Section-by-Section notes): Removed. The values \(\mathcal{O}(KT^4)\) for AdSwitch, \(\mathcal{O}(K^2T^2)\) for ArmSwitch are cited directly from the respective papers and are standard in the literature.
- **"Algorithm's detection subroutine not defined"** / **"reproduction difficult"**: Removed. Algorithm 1 explicitly references the CD subroutine; the CD algorithms (M-UCB detector, GLR detector) are described in separate algorithms in the paper. This is standard practice.
- **"Statistical significance or variance bands not reported"**: Removed. 100-trial average plots are standard in this literature; error bars would be a nice addition but are not a deficiency.
- **"Paper does not discuss how to set \(\alpha\) in practice"**: Removed as a weakness; the theoretical guarantee holds for any \(\alpha\), and a sensitivity analysis is a nice-to-have, not a required element.
- **Pure formatting/style nitpicks and missing-appendix concerns**: Removed per hard rules (parser artifacts).
- **Strength Finder generic/superficial strengths**: All strengths listed were concrete and specific to the paper, so none were removed for being generic.
- **"The paper does not revisit the \(\delta\) knowledge requirement in concluding remarks"**: Removed; Section 4.1 discusses it honestly, and the conclusions mention the segment-length limitation, which is the paper's self-identified primary limitation.

## Novel Insights
None beyond the paper's own contributions. The harsh critic's observation about the asymmetry between the "minimal knowledge" rhetoric and the actual dependency on \(\delta\) is the most useful meta-commentary, but it is a presentation issue rather than a novel insight about the field.

## Suggestions
1. **Clarify baseline tuning in experiments.** Explicitly state for each baseline (M-UCB, CUSUM-UCB, GLR-UCB) whether the exploration rate was tuned per \(M\) value or held fixed. Ideally, provide both comparisons: (a) baselines optimally tuned per \(M\) (i.e., using their knowledge of \(M\)), and (b) baselines with a single fixed setting. This would cleanly separate DE's ability to avoid needing \(M\) from any effects of poor parameter choice in baselines.

2. **Provide regret comparisons for AdSwitch/ArmSwitch/META at small \(T\).** Even \(T=5000\) or \(T=10000\) results would give readers some empirical signal about how DE compares to these methods, making the claim of superiority credible.

3. **Add a simulation for the skipping-mechanism extension (Section 5).** A simple synthetic comparison between the basic DE (detecting all changes, bound in \(M\)) and the skipping version (bound in \(S\)) would demonstrate the practical benefit of the theoretical extension.

4. **Rephrase front-matter claims.** Change "operates with minimal knowledge of the environment" to something like "operates without knowledge of \(M\), though it inherits from the change detector a mild assumption about the minimum change magnitude \(\delta\) (see Assumption 1)."

## Score and Decision

**Originality**: Good. The diminishing exploration schedule is a clean conceptual idea that differs from prior uniform-exploration approaches.  
**Importance of research question**: High. Removing the need for \(M\) in piecewise-stationary bandits is a well-motivated problem.  
**Claims supported**: Partially. The theoretical claims are rigorous, but the empirical support is weakened by underspecified baseline tuning and missing comparisons.  
**Soundness of experiments**: Adequate but needs improvement. The main concern is whether baselines were fairly configured.  
**Clarity of writing**: Reasonable. The paper is generally well-organized, though the wrapfigure placement and cross-referencing of separate detection algorithms could be smoother.  
**Value to the research community**: Moderate. If the empirical concerns are resolved, this would be a useful addition to the piecewise-stationary bandit literature.

The paper has a sound theoretical core and a genuinely clean idea. However, the empirical evaluation has a significant gap in how baselines were configured for the scaling-in-\(M\) experiments, and the missing comparisons against other \(M\)-agnostic methods further weaken the empirical claims. These are fixable in revision. In its current form, the evidence does not fully support the strong empirical claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>