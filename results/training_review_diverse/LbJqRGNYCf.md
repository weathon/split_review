Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes JoMA (Joint MLP/Attention), a mathematical framework for understanding the joint training dynamics of the self-attention and MLP layers in Transformers. The core idea is to "integrate out" the attention layer, producing a modified MLP-only dynamics via closed-form invariants that relate attention logits to MLP weights. Using these invariants, the paper predicts that under nonlinear activations, attention first becomes sparse (learning salient/frequent co-occurrences) and then becomes denser (incorporating less salient co-occurrences)—a pattern confirmed on trained-from-scratch and pretrained models. The paper also gives a qualitative explanation of how this dynamics enables hierarchical concept learning in multilayer Transformers.

## Strengths

1. **Exact invariants for linear and exp attention (Theorem 1).** The JoMA framework derives closed-form, provably exact time-invariant relationships between attention logits and MLP weights for linear and exp attention. This lets the paper reduce the joint dynamics to an MLP-only system, removing prior restrictive assumptions (e.g., fixing MLP weights, as in Scan&Snap, or omitting residual connections). These exact results for two attention variants are a genuine theoretical contribution.

2. **Prediction and empirical demonstration of a "sparse-then-dense" attention pattern under nonlinear activations.** Theorem 4 (convergence-speed) shows theoretically that under nonlinear MLP activations, salient token components converge much faster than non-salient ones, causing attention entropy to first drop and then rebound. This prediction is supported by experiments on Wikitext2/Wikitext103 (Figure 4, 1-layer setting), where the attention entropy curve closely matches the theoretical shape. The effect is also visible in top layers of multilayer models.

3. **Unified treatment spanning three attention variants and multiple validation scales.** The paper handles linear, exp, and softmax attention within the same framework, validates on trained-from-scratch models (Wikitext2/103) and pretrained models (OPT-2.7B, Pythia-70M/1.4B/6.9B), and includes synthetic hierarchical-data experiments. This breadth of validation across regimes strengthens the empirical case.

4. **Synthetic hierarchy experiment validates latent-to-neuron alignment (Table 1).** Using the HBLT generative model, the paper shows high normalized correlation (0.94–1.00 at layer 0, 0.55–0.81 at layer 1) between latent variables and hidden MLP nodes across a range of model complexities. This supports a prerequisite of the hierarchical learning story—that MLP nodes learn latent representations.

## Weaknesses

### Fatal
None.

### Major

1. **Softmax attention invariance rests on unverified assumptions whose error is uncharacterized.** Theorem 1's result for softmax attention (the practically relevant case) depends on two strong assumptions: (i) constant $\bar\vb_m$ (expected attention output) over time and (ii) a factorization condition $\EEE{q=m}{\sum_k g_{h_k}h_k' \vb\vb^\top} = \bar\vb_m\EEE{q=m}{\sum_k g_{h_k} h_k' \vb}$. The paper provides no theoretical justification for when these assumptions approximately hold, nor any characterization of the approximation error. The empirical validation (Figure 2, showing high correlation between predicted and actual $\vz_m$) is limited to two synthetic settings with linear MLP activation—it does not systematically test robustness when the assumptions are violated or with nonlinear activations. Since the paper's main claims about sparse-then-dense attention and hierarchical learning depend on the softmax case being approximately correct, this gap is significant.

2. **The nonlinear dynamics derivation contains an unfilled gap between the general setting and the specific equation used for analysis.** Theorem 3 (dynamics with uniform attention under mixture-of-isotropic-distributions) is derived in a generic setting without attention. The paper then abruptly transitions to equation (14): $\dot \vv \propto (\vmu - \vv) \circ \exp(\vv^2/2)$, stating it "use[s] close-form simplification of JoMA to incorporate self-attention" (line 287). The steps connecting the uniform-attention dynamics (Theorem 3) to this specific self-attention-included equation are not shown. The subsequent analysis (Theorem 4, convergence speed, sparse-then-dense pattern) is built entirely on equation (14), making it unclear whether the claimed pattern follows from the full coupled dynamics or from the specific toy simplifications (unit-vector constraint, single-cluster alignment, exp attention).

3. **The experiments do not provide controlled evidence that the JoMA mechanism specifically causes the observed patterns, rather than other factors.** (a) For multilayer trained-from-scratch models (Figure 4), bottom layers are suppressed with the explanation "due to layer interactions," but the paper provides no theoretical analysis of such interactions—the cited reference is to a figure about single-layer dynamics. (b) For pretrained models (Figure 5), attention entropy shows no clear drop-and-bounce; the paper shifts to "stable rank of MLP lower layer" as the metric, but the theoretical connection between stable rank and the JoMA dynamics is asserted in a single sentence (line 314) rather than derived. (c) The synthetic hierarchical experiment (Table 1) validates that hidden nodes correlate with latents, but does not test whether the attention dynamics *drives* this learning—no baseline with frozen/fixed attention is provided. These issues weaken the claim that the observed dynamics uniquely reflects the JoMA mechanism.

### Minor

1. **The hierarchical learning analysis (Section 5) is entirely qualitative and not formally linked to the JoMA dynamics.** Theorem 5 computes token co-occurrence probabilities under HBLT, but no equation connects JoMA dynamics to the formation of latent-feature representations across layers. The narrative about attention first picking up strong co-occurrences and then weaker ones is plausible but untested against alternatives. The paper acknowledges this ("qualitatively give a learning mechanism"), but the gap between the formal JoMA results and the hierarchical story remains large.

2. **Missing experimental details limit reproducibility.** The paper does not report the number of layers, heads, hidden dimensions, or other architectural details for the Wikitext2/103 trained-from-scratch experiments. It also does not specify how attention entropy is averaged (over heads, tokens, or sequences) in these experiments.

3. **The connection between attention entropy (used in experiments) and the theory's $\vz_m$ (logits) is not fully spelled out.** The theoretical figure (Figure 3, right) computes $\mathrm{entropy}(\mathrm{softmax}(\vv^2))$, which is a specific choice. The paper does not discuss whether entropy of the softmax over logits is monotonic in the underlying dynamics, or whether other measures of sparsity would behave differently.

### Trivial
None.

## Nice-to-Haves

- A controlled synthetic experiment where data matches the theoretical assumptions (e.g., mixture of isotropic Gaussians with known co-occurrence) and the full trajectory of $\vz_m$, $\vv_k$, and attention entropy is tracked and compared to JoMA predictions.
- A baseline with frozen/fixed attention for the hierarchical synthetic experiment to test whether dynamic attention causally drives latent learning.
- A derivation (or at least a sketch) of how the stable-rank dynamics emerges from the JoMA framework.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that the softmax invariance validation is "circular in spirit."** Computing $\hat\vz_m$ from ground-truth $\vv_k$ and testing correlation is the correct functional test of the invariant—it only appears "circular" if one mistakes testing a predicted relationship for using the relationship to predict something it was derived from. Removed as a misunderstanding.
- **Harsh Critic's claim that "correlation is not validation."** Correlation between predicted and ground-truth dynamics is a legitimate form of empirical validation. The issue is one of scope (limited settings, linear activation only), not of circularity or invalidity. This framing is downgraded and absorbed into Major weakness #1.
- **Criticism that the paper does not compare with Scan&Snap in the experiments.** The paper's introduction states that for linear activation JoMA coincides with Scan&Snap. This is a theoretical comparison; demanding experimental re-implementation of an existing method for comparison is excessive for a paper whose primary contribution is theoretical. Moved to Nice-to-Haves.
- **Strength Finder's claimed strength about "Theorem 5" showing convergence speed under nonlinear activations.** While the convergence-speed result (Theorem 4 in the paper's numbering) is a genuine contribution, the Strength Finder's framing as "Theorem 5" has a numbering mismatch. The substance of the strength is valid and already captured in Strengths #2.
- **Strength Finder's claim about "three common attention variants within a unified framework."** This is retained (Strengths #3) but the Strength Finder's phrasing about "robustness of the approach" for softmax overstates the case given the unverified assumptions. The strength is correctly retained in a qualified form.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Characterize the approximation error for softmax attention.** Provide bounds or conditions under which the JoMA softmax invariant approximately holds (e.g., in terms of the rate of change of $\bar\vb_m$, or a small parameter). Alternatively, re-center the paper's theoretical claims around the exact results for linear/exp attention and frame the softmax case as an empirically validated conjecture.
2. **Fill the derivation gap in Section 4.** Show the steps connecting the uniform-attention dynamics (Theorem 3) to the self-attention-included equation (14), or at minimum state clearly which approximations are being made at each step.
3. **Add a controlled synthetic experiment** where the data matches the theoretical assumptions (known co-occurrence structure, mixture of isotropic distributions) and track $\vz_m$, $\vv_k$, and attention entropy explicitly against JoMA predictions.
4. **Report full architecture details** (layers, heads, hidden dimensions) for the trained-from-scratch experiments, and clarify how attention entropy is computed (averaging scheme).

## Score and Decision

The paper presents a theoretically principled and creative framework for understanding joint attention-MLP dynamics. The exact invariants for linear and exp attention are genuine contributions, and the sparse-then-dense prediction is empirically supported in the 1-layer setting. However, the paper has significant gaps: the softmax attention result (central to the paper's claims) relies on uncharacterized approximations, the nonlinear dynamics derivation has an unfilled step, and the experiments lack controls to distinguish the JoMA mechanism from alternatives. The hierarchical learning story is qualitative and not formally connected to the dynamics.

The paper is not fatally flawed—the exact results for linear/exp attention have standalone value—but the overclaiming on the softmax case and the derivation gaps prevent acceptance at the current level of rigor. A major revision that either rigorously characterizes the softmax approximation error or honestly repositions the contribution around exact results + empirical conjectures could be competitive.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>