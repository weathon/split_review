Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final review.

## Summary

This paper proposes JoMA, a mathematical framework that derives closed-form invariants integrating out the self-attention layer from the joint training dynamics of MLP and attention in Transformers. For linear and exp attention, the invariant is exact; for softmax, it is approximate under stated assumptions. Using this invariant, the paper predicts that under nonlinear activations, attention undergoes a sparsity-then-density transition (salient tokens learned first, less salient ones later), and provides a qualitative explanation of how this enables hierarchical feature learning in multilayer Transformers. Experiments on Wikitext2/Wikitext103 with models trained from scratch and on pre-trained OPT/Pythia models are presented.

## Strengths

1. **Novel mathematical invariant (Theorem 1).** The paper derives a clean closed-form relationship between attention logits and MLP lower-layer weights. For linear and exp attention, the invariant is exact ($\vz_m(t) = \frac12 \sum_k \vv_k^2(t)$ for exp attention under zero initialization), which is non-trivial and genuinely novel. This goes beyond prior work (Scan\&Snap) by incorporating residual connections and MLP nonlinearity.

2. **Prediction of sparsity-to-density attention dynamics (Theorem 4).** From the invariant, the paper derives that under nonlinear activations with exp attention, salient components of $\vv$ converge exponentially faster than non-salient ones, modulated by $\exp(\mu_j^2/2)$. This predicts attention entropy first drops (sparsifies on salient tokens) then rebounds (redistributes to less salient ones). The from-scratch experiments on Wikitext2/Wikitext103 (Fig. 4) show this pattern clearly, lending empirical support.

3. **Addresses key prior limitations.** Compared to Scan\&Snap, JoMA incorporates residual connections, MLP nonlinearity, and joint training of MLP and attention. The paper also covers a broader spectrum of tokens beyond the distinct/common dichotomy of prior work (line 201-202), connecting token discriminancy and frequency.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-experiment gap: nonlinear analysis uses exp attention, experiments use softmax.** The core theoretical result for nonlinear dynamics (Eqn. 10, Theorem 4) is explicitly derived for **exp attention** (line 287: "we use exp attention"), where the invariant is exact. However, all real-world experiments use softmax attention (standard in OPT, Pythia, and the Wikitext-trained models). The invariant for softmax is only approximate and relies on two untested assumptions (stationary $\bar\vb_m$, factorized cross-moment). The paper does not discuss this gap or explain why results derived for exp attention should transfer to softmax. While the from-scratch experiments do show the predicted pattern, the theoretical justification for why softmax attention should behave the same way is not provided.

2. **Hierarchical learning story (Section 5) is qualitative and not derived from the dynamics.** The paper states upfront that it "qualitatively explains" hierarchical learning (abstract), but the gap between the claim and the analysis is significant. Section 5 presents a latent tree generative model (HBLT) and Theorem 5 gives token co-occurrence probabilities — a data property, not a dynamics result. The actual mechanism connecting attention dynamics to hierarchical feature learning is described in prose (~7 lines, lines 345-348) with no theorems, dynamics equations, or controlled experiments that manipulate attention behavior to verify causation. The correlation experiment (Table 1) shows that hidden nodes align with latent variables, but this is an existence result, not a demonstration that the sparse-then-dense attention dynamics drives hierarchical learning.

3. **Pre-trained model evidence is weak for the paper's central claim.** The paper's main theoretical prediction is about attention behavior (entropy drop-and-bounce). For pre-trained OPT and Pythia models (Fig. 5), the paper acknowledges that "the attention patterns show less salient drop-and-bounce patterns" (line 359) and switches to stable rank dynamics of MLP weights. While the stable rank is loosely connected to the theory via the joint dynamics (line 314), this shift of metric when the primary prediction is not clearly observed weakens the empirical case for the paper's central claim. The pre-trained model setting is the most practically relevant test, and the evidence there is inconclusive.

### Minor

4. **Softmax invariant validated only under linear activation on synthetic data.** The empirical check of the softmax invariant (Fig. 2) uses linear MLP activation ($\phi(x)=x$) and synthetic token distributions, not nonlinear activations on real data. Since the nonlinear case is the paper's main focus, direct validation of the invariant's accuracy under nonlinear activations on real training runs would substantially strengthen confidence.

5. **Assumption 1 (stationary backpropagated gradient) is acknowledged but its impact is not quantified.** The assumption that $\mathbb{E}[g_{h_k}\mathbf{x}]$ remains constant (line 120-123) is recognized as approximate for joint training (line 125), but the paper provides no analysis or experiment quantifying the error this introduces. Given that gradient statistics of early layers change significantly when later layers update, this is a non-trivial gap.

6. **Latent-neuron alignment in deeper layers is modest.** Table 1 reports normalized correlations for layer 1 (second layer in a 3-layer model) ranging from 0.55 to 0.81, degrading with model complexity. While the paper acknowledges degradation, calling these "high normalized correlations" overstates the evidence — correlations in the 0.55-0.69 range for the more complex settings are moderate at best, which weakens the claim that hidden nodes reliably learn latent variables in deeper layers.

### Trivial

None.

## Nice-to-Haves

- Validate the softmax invariant directly on a small Transformer trained from scratch with nonlinear activations, tracking both sides of Theorem 1 over time.
- Derive at least a two-layer analysis under simplified assumptions (e.g., frozen first layer) to give a formal foundation for the hierarchical claims, rather than relying on purely qualitative reasoning.
- Discuss the gap between exp attention (used in theory) and softmax (used in experiments) explicitly, and justify the transferability.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh critic's claim that "the invariant for softmax attention (Theorem 1) rests on two strong, unvalidated assumptions that are central to all later analysis."** — This is factually incorrect for the nonlinear dynamics analysis (Section 4), which explicitly uses **exp attention** where the invariant is *exact* (Theorem 1, bullet 2). The softmax case is only one of the three attention forms analyzed and is not the basis for Theorem 4 or Eqn. 10. Removed per "REMOVE criticisms that are factually wrong or misunderstand the paper."

2. **Harsh critic's claim that the nonlinear dynamics analysis "is never bridged to realistic Transformers" and that the entropy plot in Fig. 3 is "from a simulation that matches the toy model, not from real data."** — The paper bridges the theory to practice via Fig. 4, which shows experiments on Wikitext2/Wikitext103 with realistic Transformers trained from scratch, matching the predicted pattern. The paper does not claim Fig. 3 is from real data; it is clearly a simulation of the theoretical dynamics. The bridging occurs through the experimental validation in Fig. 4. Removed as the criticism ignores the paper's own experimental bridge.

3. **Harsh critic's characterizations of the shift to stable rank as a "bait-and-switch" and "not derived from the theory."** — The paper explicitly derives the connection (line 314: "Since MLP and attention layer has joint dynamics... this also suggests that in the MLP layer, the rank... will first drop... and then bounce back"). The paper also acknowledges the attention patterns are less clear for pre-trained models (line 359). The criticism is overblown; however, the underlying concern about weaker pre-trained model evidence is retained as a Major weakness (point 3 above).

## Novel Insights

None beyond the paper's own contributions.

The primary insight from synthesizing the reviews is that the paper has two separable contributions of different strength: (1) the exact invariant for linear/exp attention, which is mathematically clean and supported by from-scratch experiments, and (2) the qualitative hierarchical learning story, which is speculative and unsupported by formal analysis. These should be evaluated separately, and the paper's framing could benefit from more clearly distinguishing what is rigorously proven from what is hypothesized.

## Suggestions

1. Explicitly validate the invariant (Theorem 1) on a small Transformer with nonlinear activations trained on real data. Track both $\vz_m(t)$ and $\frac12\sum_k\vv_k^2(t)$ over time and report the prediction error. This single experiment would address the most serious sources of skepticism.

2. Acknowledge the exp-attention/softmax gap explicitly. Either justify why the exp attention analysis transfers to softmax (e.g., via similarity in the dynamics near the critical point), or derive the analogous result for softmax under bounded approximation error.

3. If the hierarchical story is intended as a central contribution, at minimum provide a controlled synthetic experiment where the attention dynamics are manipulated (e.g., using linear vs nonlinear activations) and the resulting hierarchical structure in representations is measured, to show causation rather than correlation.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>