Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper introduces the difference-of-submodular Bregman divergence (DBD), generalizing submodular-Bregman divergences to arbitrary set functions via the strong DS decomposition (f = f¹ - f² with f¹, f² strictly submodular). The authors prove that DBDs satisfy the divergence axioms for any generating set function (Theorem 3.1′), show that richer generating function classes yield strictly more expressive divergence classes (Theorem 3.4), and propose a learnable DBD using ε-PointNet to parameterize f¹ and f². Experiments on ModelNet40 set clustering and retrieval show that learned DBDs substantially outperform fixed submodular-Bregman baselines.

## Strengths

- **Novel and well-motivated formulation.** Extending Bregman divergences from submodular to arbitrary set functions via the strong DS decomposition is a natural and interesting generalization. The paper clearly identifies the two limitations of prior submodular-Bregman divergences (identifiability and limited expressiveness) and addresses both in a unified framework.

- **Expressive power theorem (Theorem 3.4).** The proof that expanding the generating function class strictly expands the divergence class is clean and correct. This provides a principled justification for learning DBDs with flexible neural network architectures rather than relying on handcrafted submodular functions.

- **Strong empirical improvement over fixed baselines on ModelNet40 clustering (Table 2).** Learned DBDs (with DS decomposition, grow supergradient) achieve a Rand index of 0.878, compared to 0.554 for the best fixed submodular-Bregman baseline (Dice coefficient). The gap of over 32 points is substantial, and the paper reports standard deviations over 10 trials, showing robustness. The ablation (w/ vs w/o DS decomposition) consistently favors the decomposition, supporting the paper's design choice.

- **The learnable framework via ε-PointNet is practical.** The architecture guarantees strict submodularity (ε>0) while being compatible with standard metric learning objectives (triplet loss), making the theoretical framework implementable.

## Weaknesses

### Major

- **Theoretical gap: strict supergradients for f² in the DS decomposition are not shown to exist.** Theorem 3.1′ claims that for any set function f (via DS decomposition f = f¹ − f²), proper divergences can be defined using strict subgradients/supergradients of f¹ and f². Proposition 2.5 proves that the three specific supergradients (grow, shrink, bar) are *strict supergradients only when f is strictly supermodular*. However, in the DS decomposition, f² is strictly submodular — not supermodular. The paper never proves that strict supergradients exist for strictly submodular f², nor does it offer an alternative construction. Line 188 directly asserts existence without proof: *"the strict subgradients of f at Y ⊆ V can be constructed by h_Y = h_Y¹ − g_Y² ∈ ∂̃_f(Y) with h_Y¹ ∈ ∂̃_{f¹}(Y), g_Y² ∈ ∂̃^{f²}(Y)"*. The existence of g_Y² ∈ ∂̃^{f²}(Y) (strict supergradient of a strictly submodular function) is not established. This gap undermines the completeness of Theorem 3.1′. The empirical method still works (and may not require strictness in practice), but the paper's central theoretical claim is not fully supported as written.

### Minor

- **Experimental comparison is limited to fixed baselines.** The paper compares learned DBDs only against fixed handcrafted submodular-Bregman divergences. While these are the natural baselines from the prior work this paper extends, the abstract and conclusion claim to "significantly improve the performance of existing methods" without comparing against *any* other learnable set-distance method (e.g., a Siamese network with a DeepSets encoder and a learned Mahalanobis distance, or another permutation-invariant metric learning approach). A single additional learnable baseline would substantially strengthen the claim that DBD's Bregman structure matters beyond "learning helps."

- **Greedy subgradient strictness for f¹ is also unverified.** The paper uses the extreme-point subgradient (Edmonds' greedy algorithm) for f¹ but does not verify that this yields a *strict* subgradient (as required by Theorem 3.1). While this is less concerning than the supergradient gap (subgradients for submodular functions are well-studied), it compounds the theoretical uncertainty.

- **Set retrieval experiment is qualitative only.** The retrieval results (Figure 2) show visually reasonable retrievals but no quantitative metrics (e.g., recall@k, precision@k). This limits the strength of the retrieval evidence.

- **The claim of approaching SOTA (line 276) is unsubstantiated.** The paper states that DBD "closely approaches the state-of-the-art method (Hamdi et al., 2021)" without reporting Hamdi et al.'s numbers or showing a direct comparison. This claim should be removed or quantified.

### Trivial

- None that are parser-independent.

## Nice-to-Haves

- Report quantitative retrieval metrics (recall@k, precision@k) for the set retrieval experiment.
- Add a baseline: a learned Mahalanobis distance on DeepSets embeddings, trained with the same triplet loss, to disentangle "learning helps" from "Bregman structure helps."
- Discuss the disconnect between the theory (which assumes a decomposition of a given f) and the method (which directly learns f¹ and f² without decomposition).

## Removed Points

- **Strength: "Theorem 3.1′ shows DBDs are proper divergences for any set function"** — This strength asserts that the proof is given in Section 3.2. However, a verified weakness shows the proof has a gap (strict supergradient existence for f² is not established). Following the policy that when a strength and weakness conflict, the weakness wins, this strength is moved here.
- **Harsh critic point about Proposition 2.5 supergradients being strict for strictly supermodular** — This is factually correct but is a known, acknowledged limitation; the point of contention is what happens when f is strictly submodular, not the correctness of Proposition 2.5 itself.
- **Harsh critic point about "experiments are too weak, straw-man comparison"** in its most extreme framing — The comparison against fixed submodular-Bregman divergences is the natural baseline given the paper's lineage (Iyer & Bilmes 2012b). Calling it a "straw man" overstates the problem. The weakness is real but more modest: the baseline set could be expanded. Rephrased as Minor weakness above.
- **Criticism about missing confidence intervals / statistical significance** for clustering — The paper reports means and stds over 10 trials, which is standard practice for this type of experiment.
- **Strength Finder's supportive strengths about qualitative evidence and Proposition 2.5** — The MNIST example (Figure 1) is illustrative but minimal; Proposition 2.5 is standard and doesn't directly support the paper's main claim. These are moved here as not rising to the level of core strengths.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface a perspective that the paper itself does not present.

## Suggestions

1. **Close the strict supergradient gap:** Either prove that the grow/shrink/bar supergradients are strict for *strictly submodular* functions (by adapting the proof of Proposition 2.5), or provide an alternative construction of strict supergradients for strictly submodular f². This is the single most important revision.
2. **Add a learnable baseline:** A simple DeepSets encoder + learned Mahalanobis distance would make the experimental comparison much more informative.
3. **Quantify the SOTA comparison or remove the claim.** If Hamdi et al. (2021) numbers are available, add a row to Table 2. Otherwise, remove line 276.
4. **Add quantitative retrieval metrics** to the set retrieval experiment.

## Score and Decision

**Calibration details:**

Round 1 bracket: 4.5 – 6.0 (between UST at 4.5/Reject and SFM Dueling at 6.0/Accept).

Round 2 anchors read in full:
- *Improving Set Function Approximation with QUANNs* (5.50, Accept Poster) — Topically similar (set functions + neural architectures). This paper has cleaner theory but comparable experimental scope. The present paper has a more novel problem formulation (extending Bregman divergences) but a theoretical gap that QUANN doesn't have. Slightly weaker overall.
- *Submodular Function Minimization with Dueling Oracle* (6.00, Accept Poster) — Strong theory with optimality guarantees, limited experiments. This paper has weaker theory but more empirical validation. Less strong overall.
- *Universal Set Transformer* (4.50, Reject) — Missing comparisons, limited evaluation. This paper has stronger theory and more concrete experiments. Clearly stronger.
- *Efficient SE(p)-Invariant Transport Metric* (5.60, Accept Poster) — Mix of theory and experiments, accepted despite some reviewer concerns about evaluation scope. Comparable ambition level. This paper has a more interesting theoretical gap, making it slightly weaker.
- *Efficient Submodular Maximization for SCMs* (5.00, Accept Poster) — Strong approximation guarantees, solid but unexciting. Comparable overall strength, though with different strengths (solid theory vs. novel framework + empirical results).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>