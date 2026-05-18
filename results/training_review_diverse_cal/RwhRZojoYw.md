Now I have all the information I need. Let me synthesize my final consolidated review.

---

## Summary

This paper investigates whether random dropping methods (DropEdge, DropMessage) genuinely mitigate oversmoothing in GNNs. It provides empirical evidence that these methods have limited effect on test-time oversmoothing, and that DropEdge's performance benefits stem from stochasticity (data-augmentation-like noise) rather than from oversmoothing reduction. The paper then proposes Learn2Drop — a learned dropping method motivated by the information bottleneck principle — and shows it can reduce oversmoothing at test time and improve deep GNN performance. The strongest contributions are the critical analysis of existing methods in Section 3, while the proposed Learn2Drop method has a notable gap between its claimed theoretical foundations and the actual derivation.

## Strengths

- **Empirical demonstration that random dropping methods have limited test-time oversmoothing reduction (Section 3.2, Figure 1):** The paper carefully measures Dirichlet energy and MAD at both training and test time, showing that DropEdge and DropMessage do not prevent exponential convergence of these metrics during inference. This directly challenges the widely held assumption that these methods alleviate oversmoothing.

- **Causal separation of stochasticity from oversmoothing via controlled randomness experiments (Section 3.3, Figure 2):** By systematically varying the stochasticity of DropEdge while keeping the edge-drop condition that supposedly reduces oversmoothing fixed, the paper shows that performance degrades as randomness is reduced — even though the DropEdge theorem is still satisfied. This provides strong evidence that DropEdge's benefit comes from data-augmentation-like noise, not from oversmoothing reduction. This is the single most important experimental contribution.

- **Critical analysis of oversmoothing metrics (Section 3.1):** The paper identifies limitations of both Dirichlet energy (sensitivity to scaling, relevant for methods like DropMessage that rescale embeddings) and MAD (non-zero at complete smoothing, ineffective for scalar embeddings), providing useful methodological guidance for future empirical studies.

- **Nuanced take on the oversmoothing–performance relationship:** The paper repeatedly notes that oversmoothing reduction alone does not guarantee better performance (Sections 3.3, 5.2, 6), and that random test-time dropping reduces smoothing but hurts accuracy. This aligns with and empirically supports theoretical work (Keriven, 2022), offering a valuable caution against oversimplified views of oversmoothing.

## Weaknesses

### Fatal

None.

### Major

- **The KL divergence derivation for Learn2Drop (Section 4.2, Equation 8) is not mathematically rigorous.** The paper computes a KL divergence between a spike-and-slab distribution where one component is a Dirac delta at a learned value \(l\) (for \(\mathbb{P}_\phi\)) and a distribution with a continuous uniform density (for \(\mathbb{R}\)). The KL between a point mass and a continuous density is not well-defined in the standard sense — it would be infinite, as the point mass is singular with respect to the Lebesgue measure. Additionally, the paper mentions using the Gumbel-Sigmoid trick (a continuous relaxation) for gradients, but the KL derivation is presented for the original discrete distributions, creating a mismatch between theory and implementation. While similar approximations appear in the variational inference literature, the paper frames Learn2Drop as a "principled" information-theoretic method, and this gap between framing and rigor is significant. The empirical results for Learn2Drop may still stand on their own, but the theoretical justification as presented is unsound.

### Minor

- **The randomness experiment (Section 3.3) uses shallow 3-layer GCNs** while the oversmoothing analysis uses 128-layer models. The paper justifies this with "in order to obtain stable results," but the disconnect limits the strength of the claim that "a GNN with reduced oversmoothing does not necessarily generalize better" in the deep regime where oversmoothing is most relevant. The experiment's core finding (importance of randomness) is valid regardless, but the generalization to deep models is less firmly supported.

- **The information bottleneck framing is asserted but never empirically verified for Learn2Drop.** No experiment measures whether the IB objective is actually being optimized (e.g., by estimating \(I(X,Z)\) and \(I(Z,Y)\) before and after training) or whether the learned dropping probabilities correlate with task relevance. The paper partially acknowledges this ("we emphasize that this is merely a hypothesis" in Section 5.2), but the IB framing is used as a key selling point in the abstract and introduction without direct validation. Combined with the KL derivation issue, the claimed IB foundations rest on weak ground.

- **The oversmoothing comparison in Figure 3 compares Learn2Drop (with test-time dropping) against baseline methods (without test-time dropping).** The paper states it uses "the same methodology as in 3.2," where test-time evaluation for baselines is explicitly done without dropping. This is a transparent and defensible comparison — the paper's thesis is precisely that Learn2Drop enables informed test-time dropping while baselines cannot — but the asymmetry could be stated more explicitly in the Figure 3 caption and surrounding text to avoid confusion.

### Trivial

- Some notation inconsistencies in the spike-and-slab derivations (e.g., the parameter \(p\) in the expression for \(\mathbb{R}(Z)\) in line 170 appears to conflate different probability values).

## Nice-to-Haves

- An ablation study for Learn2Drop components (varying \(\beta\), comparing with fixed dropping probabilities, testing different MLP architectures) would strengthen the understanding of which design choices drive improvements.
- More explicit training details for Learn2Drop (MLP layers, hidden dimensions, Gumbel temperature annealing schedule) would aid reproducibility.
- Adding a curve in Figure 3 showing DropEdge/DropMessage with forced test-time dropping (similar to the \(^*\) variants in Table 1) would make the asymmetric comparison more explicit, even if those baselines perform poorly as noted.
- Running the randomness experiment (Section 3.3) at moderate depths (e.g., 8–16 layers) would better connect to the oversmoothing analysis.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about Table 1 averaging being unclear** — The critic claimed the paper "never makes clear whether the vanilla and DropEdge (default) baselines are also averaged over 10 forward passes," but the paper explicitly states on line 203 that only the \(^*\) test-time versions use 10-forward-pass averaging. Removed as factually incorrect.

- **Criticism about the oversmoothing comparison being "invalid" or "unsubstantiated"** — The critic claimed the comparison in Figure 3 uses asymmetric protocols without specification. The paper actually states "using the same methodology as in 3.2" and Section 3.2 clearly describes the evaluation protocols (test-time = without dropping for baselines). The comparison is between different operational regimes, which is the paper's intended contribution. Removed as a misunderstanding of the paper's methodology.

- **Criticism about missing appendix content (A.2, A.3)** — Removed per parser artifact rule.

## Novel Insights

The most interesting observation that emerges from synthesizing the paper's analysis across Sections 3.2 and 3.3 is this: the DropEdge theorem (which states that edge-dropping pushes the \(\epsilon\)-smoothing layer deeper) makes no assumption about how edges are removed, yet the method's empirical success is almost entirely contingent on *randomness* in the selection process, not on the theoretical condition itself. This reveals an underappreciated gap between the theoretical guarantees of random dropping methods and their practical behavior — a gap that suggests the field may have been attributing gains to the wrong mechanism for years.

## Suggestions

- **Revise the IB derivation.** Either (a) adopt a simpler regularized objective without claiming rigorous IB foundations, or (b) provide a correct variational bound over the continuous relaxation (e.g., Concrete/Gumbel-Sigmoid distributions) where the KL is well-defined. The empirical results for Learn2Drop can stand without an elaborate theoretical apparatus.

- **Add explicit disclaimers in Figure 3** stating that baseline curves are evaluated without test-time dropping (their intended use) while Learn2Drop uses learned test-time dropping, to prevent reader confusion.

- **Extend the randomness experiment** to at least one moderately deep setting (16–32 layers) to strengthen the claim that the findings about stochasticity generalize beyond 3-layer models.

- **Add a simple Learn2Drop ablation** varying the KL regularization strength \(\beta\) to show how the IB tradeoff affects oversmoothing and accuracy.

## Score and Decision

**Originality:** Good — the critical analysis questioning whether random dropping methods actually reduce oversmoothing is timely and novel. The proposed Learn2Drop method is less novel in its individual components (spike-and-slab, IB, Gumbel-Sigmoid) but the combination is new.

**Importance of research question:** High — oversmoothing is a central problem in deep GNNs, and understanding whether widely-used methods actually solve it is of broad interest.

**Claims support:** Mixed — the critical analysis claims are well-supported. The Learn2Drop empirical results are promising, but the theoretical IB framing is not properly supported by the derivations.

**Soundness of experiments:** Adequate overall, though the randomness experiment would benefit from deeper models and Learn2Drop would benefit from ablations.

**Clarity:** Generally clear, though some details about the KL derivation could be better explained.

**Value to community:** High for the critical analysis of existing methods; moderate for Learn2Drop as a practical technique.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>