Now I have all the verification I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes an "inverted Forward-Forward" algorithm — a local contrastive learning rule where layer activity is minimized for positive (matched) data pairs and maximized for negative (mismatched) pairs. The authors demonstrate that this simple learning rule produces spatiotemporal activation patterns resembling hierarchical predictive coding: bottom-up surprise cascades for mismatched inputs and bottom-up cancellation cascades for matched inputs. The paper also derives an equivalence between the algorithm's gradient update and three-factor Hebbian plasticity. The work connects local contrastive learning to cortical predictive computations, offering a hypothesis about how such properties might emerge from simple learning principles.

## Strengths

- **Demonstrates hierarchical surprise and cancellation cascades (Figs. 3a–3c):** The paper shows that the inverted Forward-Forward model produces a clear bottom-up ordering for both surprise signals (negative data, activation increases) and cancellation signals (positive data, activation decreases), with early layers diverging faster despite label introduction at the top. This spatiotemporal ordering is a nontrivial emergent property of the learning rule and is the paper's most striking empirical finding.

- **Derives equivalence to three-factor Hebbian plasticity (Section 3.5, Eq. 8):** The paper provides a mathematical derivation showing that the gradient update for each layer's weights decomposes into a gated three-factor Hebbian rule — combining a contrastive sign flip, a threshold-passing gate, and a self-gain term. This establishes a concrete theoretical link between the model's learning dynamics and biologically plausible plasticity mechanisms without weight transport.

- **Bidirectional decodability cascades reveal information flow structure (Section 3.3, Fig. 4b):** The decoding analysis with trained MLPs on layer-wise latents is the most quantitative result in the paper. It shows two distinct temporal cascades of information flow — bottom-up during the presentation phase (image-driven) and top-down during the processing phase (label-driven) — consistent with the architecture's bidirectional design.

- **Achieves reasonable accuracy under biological constraints:** The model reaches 95% test accuracy on MNIST while using only local learning (no backpropagation through the network, no weight symmetry, stopgrad-enforced locality). This demonstrates that the proposed learning rule is functionally effective while respecting biological constraints, even if the accuracy itself is not state-of-the-art.

## Weaknesses

### Fatal

None.

### Major

- **Core empirical evidence for surprise/cancellation cascades is qualitative, without error bars or statistical validation.** The paper's central claims — hierarchical emergence of surprise and cancellation signals (Section 3.1), dynamical ordering of cascades (Section 3.2) — rest almost entirely on visual inspection of activation norm plots (Figs. 2b–2d, 3a–3c). No error bars across random seeds are reported, no statistical significance tests are conducted, and no null-model comparisons are provided (e.g., random weights, trained with a different objective). The decoding analysis (Fig. 4b) is more rigorous, but it does not directly quantify the surprise/cancellation phenomena themselves. A reader cannot assess how robust or reliable these patterns are across different runs, hyperparameters, or network initializations.

- **Comparison with predictive coding networks (PCNs) lacks implementation detail, making it difficult to evaluate.** Section 3.4 contrasts the Forward-Forward model with "established predictive coding networks (Rao & Ballard, 1999)" and claims that PCNs do not produce the surprise/cancellation cascades. However, the paper provides no details of the PCN implementation used: number of layers, training procedure, hyperparameters, weight initialization, or dataset. Figure 5 shows PCN activation plots, but without knowing whether the PCN was reasonably configured or optimized, the comparison cannot be assessed as fair. This undermines one of the paper's key differentiators.

### Minor

- **Gap between theoretical Hebbian derivation and actual training procedure.** Section 3.5 derives that the gradient update can be expressed as a three-factor Hebbian rule — a valuable theoretical contribution. However, the actual experiments use gradient-based optimization (RMSProp with autodiff on local losses) rather than implementing the Hebbian rule directly. The paper also uses stopgrad to make gradients local, which is consistent with the Forward-Forward philosophy, but the experiments never verify whether the three-factor Hebbian rule produces the same dynamics when implemented directly. Closing this gap would substantially strengthen the bio-plausibility claims.

- **Derivation of the stationary condition is thin and does not address trivial solutions.** The paper states that a stationary condition for the learning rule is $W_i\hat{x}_i + F_i\hat{x}_{i-1} + B_i\hat{x}_{i+1} = 0$ (line 165), but does not show that gradient descent actually drives weights toward this condition, nor does it discuss why the network avoids the trivial solution where all weights are zero (which would also satisfy the equation while making all activities zero). The paper acknowledges there are "a number of conditions" for gradient zeroing but does not elaborate.

- **Limited task/dataset scope.** All experiments are on MNIST, a simple dataset without strong hierarchical structure (edges, shapes, objects). Demonstrating hierarchical predictive processing on a dataset with genuine hierarchical features (e.g., CIFAR-10, or a synthetic hierarchical dataset) would strengthen the claim that the model reproduces *hierarchical* cortical computations rather than merely reflecting MNIST's flat structure.

### Trivial

- Several minor notational issues (e.g., Equation 8 has a typesetting artifact with `_{,\vec{\cal S}}` subscripts that is difficult to parse; Section 3.5 interleaves analysis and methods in a way that is sometimes hard to follow).

## Nice-to-Haves

- A null-model analysis (e.g., comparing cancellation/surprise magnitudes against networks with random weights or trained with a different objective) would substantially strengthen the evidence.
- A discussion of how the network avoids degenerate solutions (all weights → zero) would clarify the theoretical framing.
- More detail on the rationale behind the specific timestep counts (10 presentation, 15 processing) would be helpful for reproducibility.

## Removed Points

These points were raised by reviewers but are removed after verification:

1. **"Bio-plausibility claim undermined by actual training procedure (global error signals, backpropagation)"** — REMOVED. This criticism misreads the paper. The paper explicitly states (line 66) that a stopgrad operation is applied to all adjacent layer activations, preventing gradient flow between layers. Each layer's loss is local (Eq. 1), making gradient computation local. The paper avoids the weight-transport problem that defines backpropagation's non-locality. The critic's framing of the training as "global error signals" is incorrect given the stopgrad mechanism.

2. **"95% accuracy on MNIST is not competitive"** — REMOVED. The paper does not claim state-of-the-art performance; the accuracy is presented as evidence that the model *works* under biological constraints. The comparison to "simple MLPs" ignores that those MLPs use backpropagation and weight symmetry, which the paper explicitly avoids.

3. **"The comparison is staged to make the Forward-Forward model look better"** — REMOVED. This is an unsupported assertion about author intent. The valid concern (lack of implementation details for the PCN) is already captured as a Major weakness above.

4. **"The derivation assumes the derivative of the softplus is saturated"** — REMOVED. The derivation (Eq. 8) includes σ′ as an explicit factor; it does not assume saturation. The critic reads assumptions into the derivation that are not present in the equation.

5. **Strength: "Explicitly contrasts with predictive coding networks"** — REMOVED because it conflicts with a verified weakness (the PCN comparison lacks implementation detail, so claiming it as a strength is unsupported).

## Novel Insights

The most interesting observation emerging from these reviews is that the harsh critic and the paper's own claims agree on a key point: the inverted Forward-Forward algorithm produces *qualitatively different* dynamics from standard predictive coding networks. The harsh critic takes this as evidence the comparison is unfair (since the PCN might not be properly tuned), but it also highlights a genuine scientific question: *if* the dynamics are truly different, what does this tell us about the relationship between local contrastive learning and predictive coding? The paper's derivation of the third-factor difference (Section 4.1, Eq. 10) — contrastive supervision + activity gating vs. prediction error — is a useful conceptual framing that deserves more empirical scrutiny. A systematic comparison controlling for network size, training budget, and architecture would be valuable future work.

## Suggestions

1. **Add error bars and multi-seed statistics** to all core empirical figures (activation norms, cascade orderings, cosine similarities) to establish robustness.
2. **Provide full implementation details for the PCN comparison** (layers, hyperparameters, training procedure, initialization) so the reader can assess fairness.
3. **Test on a dataset with richer hierarchical structure** (e.g., CIFAR-10, or a synthetic dataset with compositionality) to strengthen the "hierarchical" claim.
4. **Either implement the three-factor Hebbian rule directly** or clearly acknowledge that the current training uses gradient-based optimization as a proxy, and discuss whether the equivalence has been empirically verified.
5. **Address the trivial-solution problem** by explaining what prevents the network from driving all weights to zero (e.g., the contrastive objective requiring differentiation between positive and negative data).

## Score and Decision

**Originality:** The paper proposes an interesting inversion of the Forward-Forward objective and connects it to predictive coding phenomena — a novel conceptual bridge.  
**Importance of research question:** Understanding whether cortical-like predictive dynamics can emerge from local learning is a timely and significant question.  
**Claims support:** The central claims are supported by qualitative visual evidence from a single dataset without error bars, which is insufficient for the strength of the conclusions drawn.  
**Soundness of experiments:** The decoding analysis is solid; the cascade/surprise analysis needs statistical validation; the PCN comparison lacks transparency.  
**Clarity of writing:** Generally well-structured but some derivations are hard to parse (Eq. 8 typesetting, interleaved theory/empirics in Section 3.5).  
**Value to community:** The conceptual contribution and Hebbian derivation are valuable; with stronger empirical validation this could influence work on biologically plausible learning.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>