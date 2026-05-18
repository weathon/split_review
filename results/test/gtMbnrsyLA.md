Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper introduces SMAAT, a scalable adversarial training method for encoder-based LLMs that generates adversarial perturbations at the last layer (the classifier layer) rather than at the input layer. The approach is motivated by three empirical observations: (1) layer representations in BERT/RoBERTa exhibit monotonically decreasing intrinsic dimensionality, (2) off-manifold examples tend to persist across layers, and (3) perturbing at the lowest-ID layer yields both shorter backpropagation chains (scalability) and a higher proportion of off-manifold adversarial examples (robustness). SMAAT is evaluated on AGNEWS, IMDB, and YELP datasets with BERT-base and RoBERTa-base, showing 3× training speedup over PGD-based adversarial training and robust accuracy improvements of 8.6–28.8% over prior SOTA against word-substitution attacks.

## Strengths

- **State-of-the-art robustness across multiple datasets and models**: SMAAT improves average robust accuracy over prior best baselines by 8.6%, 15.7%, and 28.8% for BERT, and 6.0%, 5.8%, and 19.0% for RoBERTa on AGNEWS, IMDB, and YELP, respectively (Table 1). These gains are consistent across three attack types (PWWS, TextFooler, BERT-Attack).

- **Substantial reduction in training cost**: Per-epoch training time is ~3× faster than FreeLB++ and comparable to standard training; inference is 4.6× more efficient (Table 2). This supports the scalability claim.

- **Ablation study confirms the layer-selection hypothesis**: Figure 4 shows that applying AT at progressively higher layers (0, 2, 4, 6, 8, 10, 11, 12) yields monotonic improvements in robustness on YELP, directly supporting the paper's core assumption about higher layers being more beneficial for AT.

- **Robustness to stronger attacks**: Table 3 demonstrates SMAAT outperforms FreeLB++ under 50-step targeted PGD on token embeddings and targeted "feature-level" attacks, showing the method is not limited to weak threat models and works within the continuous-embedding threat model it is designed for.

- **Generalization maintained**: Clean accuracy is comparable to standard training and often higher than other robust baselines, with only a 0.5% drop in one of six model–dataset pairs (Table 1).

- **Empirical validation of decreasing ID**: Figure 3 convincingly shows that BERT and RoBERTa exhibit monotonically decreasing intrinsic dimensionality across layers on all three datasets, providing an empirical foundation for the layer-selection strategy.

## Weaknesses

### Fatal
None. The paper's core empirical findings (SMAAT improves robustness and reduces training cost) are supported by evidence, even if the theoretical justification is flawed and some comparisons are confounded.

### Major

**1. Theorem 3.1's condition contradicts the paper's own empirical observation.**  
The theorem states: *"If f is differentiable with Lipschitz continuous gradients, and the intrinsic dimension across layers i∈[1,n] satisfies k_{i-1} < k_{i} (ID INCREASES with depth)..."* But the entire paper's motivation is that ID *decreases* monotonically—deeper layers have *lower* ID (Section 3.3, Figure 3, and observation (ii) in the abstract: "deeper layers ... have much lower intrinsic dimensionality"). The condition should be k_{i-1} > k_i for decreasing ID. The text immediately after the theorem interprets it as "if the ID of the input space exceeds the ID of the output space" (decreasing ID), which directly contradicts the mathematical statement. This is not a mere typo—it makes the theoretical argument incoherent. A reader cannot evaluate whether the claimed guarantee holds. The paper relies on this theorem to justify the method, yet the core logical link is broken.

**2. Missing ablation confounds the source of speedup and robustness.**  
SMAAT trains only the last (classifier) layer (Section 4.1: "We train the last layer of f_θ for ten epochs"), while baselines like FreeLB++ train all layers. This means:
- The runtime comparisons (Table 2) are confounded: speedup could come from training fewer parameters, not from the short forward-backward chains that the paper emphasizes. Training 1 layer instead of 12 trivially reduces compute, regardless of where perturbations are applied.
- The robustness comparisons (Table 1) are also hard to interpret: training fewer parameters may act as an implicit regularizer.

The paper needs an ablation that trains *all layers* but generates perturbations only at the last layer, isolating the effect of layer choice from parameter reduction. Without this, the claimed "3× speedup" and the robustness improvements could be driven by a confound rather than by the proposed mechanism.

**3. Threat-model gap between training and primary evaluation.**  
SMAAT generates adversarial examples by adding a continuous perturbation to the [CLS] representation at the last hidden layer (Section 4.1), yet the main robustness claims (Table 1) are evaluated against *input-space word-substitution attacks* (PWWS, TextFooler, BERT-Attack)—a fundamentally different type of perturbation. The paper does not provide a rigorous argument that robustness to last-layer continuous perturbations implies robustness to discrete token-level substitutions at the input. Table 3 partially addresses this by evaluating against embedding-space PGD (matching the training threat model), and these results are positive, but the headline claims (8.6–28.8% improvements) are based on the input-space attacks where the theoretical link is weakest. The paper should either lead with the threat-model-matched results or provide a bridge argument for why these evaluations are meaningful.

### Minor

**1. SVD-based ID estimation assumes linear manifolds.**  
The paper uses SVD with a fixed cosine-similarity threshold (0.1) to estimate intrinsic dimension, which assumes the data manifold is approximately linear. Transformer hidden states are known to be highly non-linear. The sensitivity of the method to this threshold and to the linearity assumption is not discussed.

**2. ID stability during training is not examined.**  
The search for l* is performed once at the start of training, but the intrinsic dimension of layers may shift as parameters are updated (especially if all layers were being trained, though here only the last layer is trained). The paper does not examine whether the monotonic ID property is stable during adversarial training.

**3. Hyperparameter asymmetry in comparisons.**  
SMAAT uses higher epsilon values (0.1–0.8) than standard AT, and the paper states these are higher "as we are only training the network with one layer" (Section 4.1). This makes direct comparison with baselines using different epsilon budgets difficult to interpret. A sensitivity analysis over epsilon would strengthen the claims.

### Trivial

- The complexity analysis in Section 3.4 uses notation that is difficult to parse (e.g., parser artifacts in the runtime formula). The core claim—that shorter forward-backward chains yield speedup—is clear, but the derivation could be presented more cleanly.

## Nice-to-Haves

- Robustness curves over a range of perturbation budgets (epsilon) would be standard practice in adversarial robustness literature and would strengthen the claims.
- An ablation comparing SMAAT to standard AT applied to the same subset of layers (e.g., only the last 2–3 layers, with no layer-perturbation trick) would help distinguish the benefit of the perturbation strategy from the benefit of training fewer layers.
- A comparison between the FGSM-based scalable AT methods and SMAAT in terms of both runtime and robustness would provide a more complete picture.

## Removed Points

- **Threat model mismatch as a fatal flaw** (from Harsh Critic): Downgraded from fatal to major. The paper does evaluate against its own threat model in Table 3 (embedding-space PGD), which shows strong results. The primary evaluation against input-space attacks is a gap in argument but not evidence that the method fails. The positive results in Table 1 and Table 3 together provide meaningful empirical support.
- **"Unfair comparison" framing** (from Harsh Critic): Re-framed as a missing ablation confound. The asymmetry (SMAAT trains fewer parameters) actually favors the baseline in terms of model capacity being compared against, so the robustness comparison is not "unfair"—it's confounded. The runtime comparison is genuinely hard to interpret without the ablation.
- **Ambiguity in what is trained** (from Harsh Critic): Downgraded to trivial. The paper is internally consistent: Section 4.1 says "train the last layer" and the complexity analysis describes forward-backward passes through layers l* to n. If l*=n (the last layer), both statements describe training only the classifier. The critic's concern about inconsistency is based on a misreading.
- **Complexity derivation notation issues** (from Harsh Critic): These are parser artifacts, not author errors. The intended meaning—that shorter forward-backward chains yield speedup—is clear.
- **Missing proof of Theorem 3.1** (from Harsh Critic): Per policy, missing appendix/proof content is a parser-stripping artifact and is not considered a weakness.
- **Strength about "Novel theoretical grounding"** (from Strength Finder): Downgraded in scope. The empirical ID measurement (Figure 3) is valid, but the theoretical argument via Theorem 3.1 is confused as noted in Weakness #1.

## Novel Insights

Beyond the paper's own contributions, the multi-reviewer analysis surfaces an interesting tension: SMAAT's empirical success is robust (it works across models, datasets, and attack types), but the paper over-claims the theoretical foundation while under-delivering on controlled comparisons. The monotonic-ID phenomenon is a genuinely useful empirical observation regardless of the confused theorem, and the paper would be stronger if it leaned on the ablation evidence (Figure 4) as its primary argument rather than the garbled theory. The most novel insight from synthesis is that SMAAT's combination of (a) very few trainable parameters, (b) perturbation at a low-ID layer, and (c) strong empirical results suggests that the last-layer classifier is the critical bottleneck for robustness in fine-tuned encoder LLMs—a finding that is interesting whether or not the manifold argument is formally airtight.

## Suggestions

1. **Fix Theorem 3.1** by correcting the condition to k_{i-1} > k_i (decreasing ID) and providing a proof sketch that connects to the off-manifold persistence claim. If the theorem cannot be cleanly stated, drop it and rest the argument on the empirical observations plus heuristic reasoning (which are already strong).
2. **Add the critical ablation**: train all layers while still generating perturbations only at the last layer. This isolates the effect of layer choice from parameter-count effects on both runtime and robustness.
3. **Lead with the embedding-space PGD results (Table 3)** as the primary robustness evaluation aligned with the threat model, and treat the word-substitution results as an additional stress test rather than the headline claim.
4. **Discuss the linearity assumption** of the SVD-based ID estimation and its potential limitations. Report sensitivity to the cosine threshold.
5. **Add a sensitivity analysis** over the perturbation budget epsilon.

## Score and Decision

The paper introduces an interesting and empirically effective approach. The core observations (monotonic decreasing ID, higher-layer AT being more beneficial) are empirically validated and practically useful. The robustness and efficiency gains are substantial. However, the theoretical justification is broken at a critical point (Theorem 3.1 condition contradicts the paper's premise), the primary evaluation is mismatched with the training threat model in a way that weakens the headline claims, and the missing ablation makes it impossible to attribute improvements to the proposed mechanism versus trivial parameter-count effects. These are major issues that cannot be resolved in a short rebuttal. The paper makes real contributions, but in its current form the argument is not coherent enough to support the claimed contributions.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>