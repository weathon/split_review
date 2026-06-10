## Summary

NeurRev proposes a Dynamic Sparse Training (DST) framework that identifies and selectively prunes large negative weights associated with "dormant neurons" (convolution filters whose negative weighted sum produces all-zero post-ReLU outputs, blocking gradient flow). The paper shows that dormant neurons emerge under sparsity and persist under standard DST, then presents a pruning strategy that reduces their population. The method is evaluated on CIFAR-10/100 and ImageNet, with additional hardware measurements on a Samsung Galaxy S21 demonstrating 12–96× fewer topology updates and 1.8–2.1× end-to-end training acceleration over dense training.

## Strengths

- **Identifies and empirically documents a genuine failure mode in DST.** The paper shows (Figure 1b, 1c) that dormant neurons emerge as sparsity increases and actually *grow* in population under standard DST, while NeurRev demonstrably reduces their count. The mechanistic explanation — zero post-ReLU activations blocking gradient flow (Eq. 1, line 58) — is sound and connects directly to why DST requires high update frequencies. This diagnosis is a real contribution to the DST literature.

- **Hardware evaluation on a real mobile device with measured system overhead.** Section 3.2 reports actual training acceleration (1.8–2.1× vs. dense) and overhead reduction (12–96× fewer topology updates) on a Samsung Galaxy S21, including recompilation overhead. This moves beyond the algorithmic FLOP-counting typical of DST papers and directly addresses the practical deployment problem that motivates the work.

- **Demonstrates stability at low update frequencies.** Figure 7b tests NeurRev across update frequencies from 100 iterations to 10 epochs per update and shows it maintains accuracy even at very low frequencies. This is a direct head-to-head contrast with standard DST's fragility (Figure 1a) and provides controlled evidence that the method addresses the stated motivation.

## Weaknesses

### Fatal
None.

### Major

- **Disconnect between claimed mechanism and actual implementation.** The introduction (line 23) states that the method prunes "based on the post-ReLU feature map" and calls it "essentially a data-driven approach, different from earlier heuristic pruning techniques." However, Section 2.2.2 (line 67) explicitly says that evaluating dormant neurons via layer output is "computationally intensive" and instead proxies them using weight changes (Δθ) over time, selecting negative weights with minimal change. The actual algorithm does *not* use post-ReLU feature maps. The proxy (Δθ) is a reasonable heuristic and is motivated by the observation that dormant neurons have zero gradients, but the paper's framing overstates what is implemented. This is not fatal — the method as described is coherent on its own terms — but the claims in the introduction should be aligned with what the algorithm actually does.

- **The critical ablation isolating the proposed mechanism is absent.** The method performs prune-grow at a relaxed sparsity (s-p, i.e., more active weights) and then prunes specifically negative weights with small Δθ back to sparsity s. This introduces a confound: any improvement could come from the temporary sparsity relaxation (which allows broader topology exploration) rather than from the negative-weight selection criterion. The ablation studies (Section 3.4, Figure 7) test update ratios and frequencies, but never compare NeurRev against a version that uses the same temporary sparsity relaxation but prunes random weights (or standard small-magnitude weights) instead of negative weights with small Δθ. Without this ablation, the paper cannot support its central causal claim that "pruning negative weights awakens dormant neurons" — the observed gains could be driven entirely by the temporary relaxation. This is the most significant evidential gap.

### Minor

- **Reference to non-existent Section 2.2.1.** Line 69 states "which proves our prior analysis in Section 2.2.1," but the section numbering jumps from 2.1 directly to 2.2.2. The referenced analysis is not present in the extracted text. This may be a formatting artifact, but as written it is a missing link in the paper's reasoning chain.

- **No analysis of the parameter p (pruning ratio for negative weights).** The method prunes p·‖θ‖₀ negative weights per step, but p receives no ablation. It is unclear how sensitive NeurRev is to this hyperparameter or whether there is a principled way to set it. This is the key tuning knob of the method and should be characterized.

- **No per-neuron revitalization analysis.** Figure 1c shows aggregate dormant neuron counts decreasing under NeurRev, but the paper does not analyze the mechanism at the neuron level: how many dormant neurons actually flip to active after pruning, and how many remain dormant? The "revitalization" claim rests on aggregate statistics, not per-neuron evidence.

### Trivial
None.

## Nice-to-Haves

- A one-time validation that the Δθ proxy actually correlates with true dormant-neuron status (measured via feature-map analysis on a single trained model) would substantially strengthen the paper.
- Analysis of whether dormant neurons re-emerge after being revitalized would clarify whether the effect is a one-time fix or a sustained improvement.

## Removed Points

These points from the input reviews were removed after verification against the paper:

- **Harsh Critic: "The causal logic connecting pruning to revitalization is incomplete... pruning *some* negative weights does not guarantee the neuron ceases to be dormant."** This is a speculative criticism that asks for a theoretical guarantee not required for an empirical heuristic method. The paper's aggregate evidence (Figure 1c) is the appropriate level of evaluation for this type of method. Removed as overly demanding of a systems/empirical paper.

- **Harsh Critic: "This is not a data-driven approach... it is a heuristic based on weight staleness, no different in kind from the heuristics used by prior DST methods."** The critic overstates: the Δθ proxy is specifically motivated by the dormant-neuron diagnosis (zero gradients → no weight changes), and the criterion of *negative* weights with small Δθ is genuinely different from standard magnitude-based pruning. The disconnect between the intro's "post-ReLU feature map" claim and the actual proxy is real (kept as a Major weakness above), but calling it "no different from prior heuristics" is inaccurate.

- **Strength Finder: "Systematic software-hardware co-design evaluation of activation functions."** The activation function comparison (Section 2.3, Figure 6) shows that ReLU outperforms alternatives in sparse training, but this is a general observation about ReLU-based networks, not a specific validation of NeurRev. The connection to the paper's contribution is weak. Moved here.

- **Harsh Critic: "Section 2.3 is largely orthogonal to the method... reads as background motivation rather than a contribution."** This is an opinion about framing, not a factual weakness. Removed.

- **Harsh Critic: "Figures are embedded as images, so numerical values cannot be verified from the text."** This is a formatting artifact common to PDF-extracted text. Removed per hard rules.

- **Harsh Critic: "The paper does not discuss whether dormant neurons re-emerge."** Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Align the introduction's claims with the actual algorithm: remove or qualify the "post-ReLU feature map" framing, and present the Δθ proxy transparently as a computationally efficient surrogate.
2. Add the critical ablation: compare NeurRev against a version that uses the same s-p sparsity relaxation but prunes random weights (or standard magnitude-based weights) instead of negative weights with small Δθ. If the gain disappears, the negative-weight criterion is validated; if it persists, the temporary relaxation is the driver.
3. Characterize the sensitivity of the method to the hyperparameter p (fraction of negative weights pruned).
4. Provide a one-time validation (even on a single model) that weights with small Δθ indeed belong to neurons with zero post-ReLU output.
5. Add a reference or remove the dangling reference to the non-existent Section 2.2.1.

## Score and Decision

This paper identifies a genuinely interesting and overlooked phenomenon in DST (dormant neurons), and the hardware evaluation is a practical strength that many DST papers lack. However, the paper suffers from two significant weaknesses: (a) a disconnect between the claimed mechanism (post-ReLU feature maps) and the actual proxy (Δθ), and (b) a missing ablation that would isolate whether the improvement comes from the novel negative-weight selection or merely from the temporary sparsity relaxation. Without this ablation, the paper's central causal claim is not adequately supported. The method shows clear empirical benefits over baselines, but the attribution of those benefits to the specific proposed mechanism is uncertain. The paper is revisable but in its current form falls short of the evidentiary bar for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>