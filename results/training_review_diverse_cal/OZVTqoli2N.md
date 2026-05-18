Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper studies model compositionality in non-linear deep networks through a second-order Taylor approximation of the loss around pre-training weights. It derives a theoretical condition (staying in the "pre-training basin") for composability and proposes two incremental learning algorithms — ITA (individual training with EWC-like regularization anchored to pre-training) and IEL (ensemble training with pairwise task-vector alignment) — both grounded in the same second-order formulation. Empirical evaluations on class-incremental benchmarks show strong results, and the paper demonstrates appealing skills like specialization and unlearning via simple addition/subtraction of task vectors.

## Strengths

- **Generalized theoretical perspective on compositionality beyond linearized networks.** The paper derives an upper bound (Eq. 6) relating the composed model's risk to individual risks under a second-order approximation, explicitly extending prior work that applied only to tangent-linearized models (Liu et al., 2023). The paper correctly notes that its inequality "applies to *any* fine-tuning strategy (e.g., LoRA, adapters, etc.)" (Section 2.1), which is a genuine generalization.

- **Two dual algorithms (ITA and IEL) derived from a common framework.** ITA and IEL approach compositionality from complementary angles — individual vs. ensemble training — yet both flow from the same second-order formulation. The closed-form gradient for IEL (Eq. 15) maintaining constant complexity w.r.t. task count is a non-trivial technical contribution.

- **Strong empirical results on multiple class-incremental benchmarks.** Both ITA and IEL match or exceed state-of-the-art methods (EWC, LwF, L2P, CODA, SEED, InfLoRA, APT, TMC) on Split ImageNet, Split CIFAR, Split CUB, Split Caltech, and Split MIT, with especially large margins over the linearization-based TMC. The methods also perform well on low domain-similarity datasets (Split Resisc45, Split CropDiseases), suggesting robustness when the pre-training optimality assumption is challenged.

- **Demonstration of specialization and unlearning via simple task-vector arithmetic.** Section 5 and Table 2 show that ITA supports targeted editing (boosting or removing particular tasks) via addition/subtraction of task vectors, with better disentanglement than TMC. This is arguably the paper's most distinctive practical contribution and directly validates the compositional framing.

- **Figure 1 provides direct empirical validation of the theoretical motivation.** The paper plots the empirical upper bound and composed-model risk with and without the proposed EWC-like regularization, confirming that ITA "significantly tightens the upper bound" (Section 5). This bridges the theory and experiments concretely.

- **Compatibility with multiple fine-tuning strategies (full fine-tuning, LoRA, IA³)** is demonstrated, showing that the regularization benefits both full and parameter-efficient fine-tuning. The ablation (Table 2) further teases apart the effect of regularizing all layers vs. only the classification head.

## Weaknesses

### Fatal
None.

### Major

- **The central theoretical assumption — that pre-training weights are a local minimum of the combined-task empirical risk — is unsubstantiated, weakening the claimed theoretical guarantees.**  
  The Jensen inequality (Eq. 6) requires the Hessian to be positive semidefinite, which relies on the assumption that θ_ptr is a local minimum of the empirical risk across *all tasks*. The paper points to linear probing of the classification head (pre-consolidation) as a practical way to enforce this condition. However, linear probing only optimizes the classification head — the backbone weights remain at their pre-trained initialization. There is no justification that this fixed backbone constitutes a local minimum of the combined-task empirical risk. The footnote claim that "such a condition can be easily satisfied with over-parameterized deep learning models" (Section 2.1) is unsupported hand-waving: over-parameterization does not make an arbitrary initialization a local minimum of a new objective.  
  Without this assumption, the Hessian could be indefinite, the second-order approximation may not be convex, and the Jensen bound could reverse direction. The paper acknowledges the limitation in Section 6, and importantly states that the *full* loss (not the approximation) is used in the actual algorithms (line 161). Nevertheless, the theoretical framing is presented as providing "guarantees" (line 61) which overstates its rigor. The authors should either (a) provide direct empirical validation (e.g., measure the smallest eigenvalue of the empirical Hessian after linear probing, or compare the actual loss to the bound), or (b) explicitly reframe the theory as a heuristic analogy/approximation rather than a guarantee. The empirical contributions are strong enough to stand on their own even with a humbler theoretical framing.

### Minor

- **No diagnostic analysis of the second-order approximation error as task vectors grow.**  
  The paper relies on the Taylor expansion around θ_ptr and explicitly notes (Section 6) that it may become inaccurate as parameters drift. However, no quantitative diagnostics are provided — e.g., the norm of task vectors over the sequence, or the relative error between the second-order approximation and the true loss. While the EWC-like term is designed to keep task vectors small, a sensitivity analysis showing that the approximation remains faithful throughout training would substantially strengthen the paper. This is a reasonable request that would not require new experiments on all benchmarks (a single representative dataset would suffice).

- **The novelty of ITA relative to standard EWC anchored at θ_ptr (rather than the previous task) is modest when considered in isolation.**  
  The paper correctly notes this difference (line 103: "while our anchor is fixed at θ_ptr, the anchor of EWC instead shifts"), but the core idea of regularizing toward pre-training weights is conceptually similar to existing methods. The paper's more original contributions are: (i) the second-order theoretical justification for *why* the fixed anchor at pre-training is beneficial for compositionality, and (ii) the ensemble training variant (IEL) with closed-form gradients. The authors should more clearly emphasize that the theoretical framing — not just the regularizer — is the novel element.

- **The specialization/unlearning analysis (Section 5) is suggestive but shallow.**  
  The finding that IEL fails at specialization while ITA succeeds is interesting and potentially important, but the paper does not analyze *why*. A simple diagnostic — e.g., measuring the cosine similarity between task vectors under ITA vs. IEL, or the norm of individual task vectors — would provide mechanistic insight into why ensemble training pools knowledge so thoroughly that individual experts cannot be isolated. This is not a fatal gap, but a deeper analysis would significantly strengthen this distinctive result.

### Trivial

- The "constant memory" claim (line 163) is qualified with "provided we are not interested in… model customization and unlearning." The paper does make this caveat explicit; however, a casual reader might miss it. Consider making this qualification more prominent when the constant-complexity claims are first introduced (Section 3).

## Nice-to-Haves

- An ablation of the cross-task dot-product term in IEL (the τ_t^⊤ term in Eq. 15). Removing it would clarify whether the pairwise alignment is actually beneficial or whether the EWC-like component alone drives the gain.
- A controlled experiment isolating the effect of parameter distance from θ_ptr on composition accuracy (e.g., training individual models with varying regularization strengths and plotting composition accuracy vs. parameter distance). This would directly test the paper's central thesis that staying in the pre-training basin is what enables compositionality.

## Removed Points

These points were flagged by reviewers but were removed after verification against the paper:
- **"Constant memory claim contradicted by specialization/unlearning experiments"** — Removed because the paper explicitly qualifies the claim: "provided we are not interested in more complex forms of composition… (as required for model customization and unlearning)" (line 163). The paper already makes this distinction.
- **"L2-SP is not cited"** — Removed per the rule about not demanding missing related works (cannot verify relevance without external sources).
- **"Typos/formatting issues"** — Removed per instructions about parser artifacts.
- **Several generic strengths from the Strength Finder** were removed (e.g., "addresses an important problem") as they are not specific to this paper's content.

## Novel Insights

The most interesting observation emerging from the reviews — beyond the paper's own contributions — is the tension between the two algorithms on specialization. ITA succeeds at specialization while IEL fails, despite both achieving comparable overall accuracy (Table 1). This suggests that optimizing the composed model as a whole (IEL) causes individual task vectors to become entangled in a way that prevents their clean separation, even when the closed-form gradient in Eq. 15 explicitly encourages pairwise alignment. This finding has practical importance for any application requiring post-hoc model editing (e.g., forgetting copyrighted data, customizing for a subset of tasks), and it challenges the common assumption in ensemble learning that individual components remain interpretable and separable. The paper hints at this but does not fully explore the underlying mechanism; a deeper analysis of why ITA preserves modularity while IEL does not would be a valuable follow-up.

## Suggestions

1. **Empirically validate the local-minimum assumption** on at least one representative benchmark: measure the gradient norm and smallest Hessian eigenvalue of the combined-task loss at θ_ptr after linear probing. If the Hessian is indeed positive semidefinite near θ_ptr, this would directly support the theory. If not, reframe the theory as a heuristic approximation and remove the language of "guarantees."
2. **Add a diagnostic plot** (for e.g., Split ImageNet) showing the norm of task vectors and/or the relative second-order approximation error over the course of training, to confirm that the Taylor expansion remains faithful.
3. **Deepen the specialization/unlearning analysis** by measuring the cosine similarity and norm of task vectors under ITA vs. IEL, to explain mechanistically why IEL cannot separate individual experts.
4. **Consider an ablation of the cross-task dot-product term** in IEL to disentangle the contribution of pairwise alignment from the EWC-like regularization.

## Score and Decision

This is a solid paper with strong empirical contributions, a novel algorithmic framework, and an ambitious theoretical perspective. The main weakness — the unverified local-minimum assumption — is real but not fatal: the algorithms are well-motivated even as heuristics, and the empirical results stand on their own. The paper would be strengthened by either validating the assumption or honestly lowering the theoretical ambition. With minor revisions to address the theoretical framing and add supporting diagnostics, this is a clear acceptance. In its current form, the overclaimed theoretical "guarantees" are the main concern, but the empirical and algorithmic contributions outweigh this issue.

**Originality**: Good — the second-order perspective on compositionality and the dual-algorithm framework are novel.
**Importance**: Good — incremental learning and model compositionality are timely and practically relevant.
**Claims support**: Adequate — empirical claims are well-supported; theoretical claims are overstated relative to their support.
**Soundness**: Good — experiments are thorough and well-controlled (same backbone, careful hyperparameter tuning).
**Clarity**: Good — well-structured, though some technical passages are dense.
**Value**: High — both algorithms are practical and the specialization/unlearning results are distinctive.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>