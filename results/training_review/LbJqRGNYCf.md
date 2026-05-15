I've read and cross-checked the paper thoroughly against the reviewer claims. Here is the consolidated review.

---

## Summary

This paper proposes **JoMA** (Joint MLP/Attention), a framework that derives a first integral (invariant) connecting the dynamics of a Transformer's lower MLP layer weights and its self-attention logits during gradient-based training. By "integrating out" the attention, the authors obtain a modified MLP-only dynamics. For nonlinear activations, this predicts a non-monotonic pattern: attention first becomes sparse (focusing on salient, high-co-occurrence tokens) and then becomes denser (including less salient tokens). The paper leverages this prediction to give a qualitative explanation of hierarchical feature learning in multilayer Transformers. Experiments on Wikitext2/103 and pretrained OPT/Pythia models provide partial support.

## Strengths

- **The JoMA invariant is a genuine theoretical contribution.** Theorem 1 derives closed-form relationships between $\mathbf{z}_m(t)$ (attention logits) and $\sum_k \mathbf{v}_k^2(t)$ (projected MLP weights) for linear, exp, and softmax attention. This is the first result that integrates the two components into a single joint dynamics, going beyond prior work (e.g., Scan\&Snap) that treated them separately.

- **The sparse-then-dense prediction under nonlinear activation is novel and interesting.** Theorem 3 shows that, because convergence speed scales as $\exp(\mu_j^2/2)$, salient components (large $\mu_j$) are learned first and non-salient components catch up later. This qualitative prediction — attention entropy dips, then rebounds — is a genuine departure from the strictly-sparsifying behavior of linear activations.

- **The paper addresses limitations of prior theoretical frameworks.** JoMA incorporates residual connections and MLP nonlinearity, and it analyzes joint training of attention and MLP rather than fixing one layer. Section 4 explicitly shows that for linear activations the framework recovers Scan\&Snap as a special case, demonstrating that it subsumes and extends prior results.

- **The HBLT alignment experiment (Table 1) provides tangible evidence for the hierarchical learning story.** Layer 0 correlations between hidden neurons and ground-truth latents are consistently high (0.94–1.00 across diverse settings with 5 seeds), confirming that MLP nodes do learn the latent structure predicted by the qualitative multilayer analysis.

## Weaknesses

### Fatal
None.

### Major

- **The core theoretical prediction is derived using exp attention, but all real-world experiments use softmax attention.** The nonlinear dynamics with attention (Eq. 13) is explicitly derived under exp attention ("we use exp attention"). The JoMA invariant for softmax requires the additional assumption that $\bar{\mathbf{b}}_m$ (the expected attention distribution) is constant. The only direct validation of the softmax variant of the invariant (Fig. 2) is for **linear** MLP activation, not the nonlinear case where the main prediction lives. No experiment tests the theory under the exact conditions where it applies (exp attention + nonlinear activation). This gap is partially acknowledged in the paper but is not experimentally bridged.

- **Experimental support for the central sparse-then-dense claim is weaker than ideal.** The attention entropy curves in Fig. 3 are reported without error bars, statistical significance tests, or controlled baselines (e.g., training with linear activation or without the proposed dynamics). The pretrained-model experiments (Fig. 4) switch from attention entropy (the theory's prediction target) to stable rank of MLP weights without proving that stable rank should follow the same qualitative dynamics. The paper acknowledges that "attention patterns show less salient drop-and-bounce patterns" in these models, which tempers the strength of the evidence.

- **The switch from attention entropy to stable rank in the pretrained-model experiments lacks theoretical justification.** The paper argues that stable rank "may be more reliable" and shows V-shaped curves, but there is no theorem connecting stable-rank dynamics to the JoMA-derived attention sparsity prediction. This weakens the link between theory and the largest-scale experiments.

### Minor

- **The title and abstract overclaim relative to what is rigorously demonstrated.** The paper's title promises "Demystifying Multilayer Transformers," but the core mathematical framework (Theorems 1–3) is derived for a **single** Transformer block. Section 5 provides a qualitative, intuitive story for multilayer learning — the paper consistently labels it as "qualitative" — but there is no theorem analyzing how gradients backpropagate across layers or how inter-layer interactions affect the joint dynamics. The paper would be more accurately framed as a single-block analysis with a qualitative multilayer extension.

- **The derivation of the key nonlinear-dynamics-with-attention equation (Eq. 13) is compressed.** The paper states "we use close-form simplification of JoMA to incorporate self-attention, which leads to (we use exp attention):" without showing the intermediate steps. While the result is plausible, the reasoning from the uniform-attention dynamics (Eq. 9) to Eq. 13 via the JoMA invariant could be made more explicit.

- **The constant-$\bar{\mathbf{b}}_m$ assumption for softmax attention is strong and unchecked in the nonlinear regime.** The paper validates this assumption only for linear MLP activations (Fig. 2). Whether it holds during real training with nonlinear activations and softmax attention is not quantified. Measuring $\|\bar{\mathbf{b}}_m(t) - \bar{\mathbf{b}}_m(0)\|$ over training would help bound the error.

### Trivial
None beyond parser-induced artifacts.

## Nice-to-Haves

- Test the sparse-then-dense prediction on a small Transformer with **exp attention** (or linear attention) on synthetic data matching the theoretical assumptions (orthogonal embeddings, independent $z_{ql}$). This would directly validate the theory in the regime where it applies exactly.
- Add error bars / confidence intervals to the attention entropy plots (Fig. 3) and report the variation across random seeds, as is done in Table 1.
- Run an ablation removing residual connections to verify the paper's claim that their inclusion changes the attention dynamics.
- Quantify how much $\bar{\mathbf{b}}_m$ varies over training in the Wikitext experiments to empirically bound the error introduced by the constant-$\bar{\mathbf{b}}_m$ assumption.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Circular dependency undermines nonlinear analysis"** (Harsh Critic Issue 4): The critic claims that assuming $\bar{\mathbf{b}}_m$ constant "freezes the attention pattern." This is a misunderstanding: $\bar{\mathbf{b}}_m$ is the *expected* attention distribution across samples; treating it as constant is a first-order approximation, not a freezing of individual attention scores. The paper acknowledges this assumption and validates it empirically for the linear case (Fig. 2). The criticism is factually overstated.
2. **"No comparison with existing theoretical frameworks"** (Harsh Critic Issue 5): The paper is primarily a theoretical contribution. Requesting an experimental comparison with Scan\&Snap's predictions is a reasonable suggestion but not a weakness — the paper shows it subsumes Scan\&Snap in the linear case (a direct theoretical comparison). Moved to Nice-to-Haves.
3. **"Theorem 2 is restricted to $K=1$"**: This is standard practice in theoretical analysis to derive clean closed forms. The paper is transparent about the simplification. Not a genuine weakness.

## Novel Insights

The most interesting observation from the reviewer discussion is the **contrast between the clean theoretical framing and the messier empirical validation**. The paper's core move — integrating out attention to obtain a MLP-only dynamics — is a genuinely useful theoretical tool because it shifts analysis from the highly complex attention-MLP interaction to a simpler dynamical system on MLP weights. The non-monotonic sparsity prediction (sparse → dense) is a direct consequence of the interplay between the exponential modulation from attention ($\exp(v_j^2/2)$) and the saturating nonlinearity of activation functions. What the reviews collectively highlight is that this prediction, while appealing, has not been tested in the exact setting where the theory applies (exp attention + nonlinear activation), and the softmax experiments, while suggestive, leave room for alternative explanations (e.g., learning rate effects, optimization artifacts). The hierarchical learning story is similarly appealing but would benefit from a direct mathematical link between the HBLT co-occurrence formula (Theorem 4) and the multi-layer gradient dynamics.

## Suggestions

1. **Add a controlled experiment with exp attention.** Train a small Transformer (or even a single-block model) with unnormalized exp attention on synthetic data matching the theoretical setup. Plot attention entropy over training and verify the drop-then-rebound directly — this would close the central gap between theory and experiments.
2. **Include error bars and baseline comparisons for Fig. 3.** Show attention entropy curves for linear-activation baselines (which should not rebound) and report standard deviations across multiple runs.
3. **Quantify the constant-$\bar{\mathbf{b}}_m$ assumption.** Measure $\|\bar{\mathbf{b}}_m(t) - \bar{\mathbf{b}}_m(0)\|$ over training in the Wikitext experiments to bound the approximation error for the softmax attention case.
4. **Retitle to reflect the single-block scope.** A title like "JoMA: Joint Dynamics of MLP and Attention in Transformer Blocks" with the abstract noting the qualitative multilayer extension would be more accurate and avoid overclaiming.

## Score and Decision

The paper presents a genuine theoretical insight (the JoMA invariant) and a novel qualitative prediction (sparse-then-dense). However, the experimental validation has significant gaps: the theory is derived for exp attention but tested on softmax, the main experiments lack error bars and controls, and the pretrained-model evidence uses a different metric (stable rank) without theoretical justification. The multilayer framing overclaims relative to what is mathematically demonstrated. These weaknesses do not invalidate the core contribution but substantially reduce confidence in the empirical support. The paper needs major revisions — particularly a controlled exp-attention experiment and stronger validation — to fully establish its claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>