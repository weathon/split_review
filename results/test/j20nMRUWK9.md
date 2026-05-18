Now I have all the information needed. Let me construct the consolidated review.

---

## Summary

This paper proposes an explicit knowledge transfer framework for Generalized Category Discovery (GCD), structured as three stages: knowledge generation (pre-training on known classes), knowledge alignment (adapter layer + channel selection matrix), and knowledge distillation (maximizing mutual information between representation spaces via a contrastive loss). The paper also introduces the iNat21 benchmark with four difficulty splits. Empirical results on six datasets show consistent improvements over prior methods, and ablations confirm the contribution of each component.

## Strengths

1. **State-of-the-art performance across diverse benchmarks.** The method surpasses prior SOTA on all six datasets tested (Table 2), including +2.3% novel class accuracy on CIFAR100-80, +1.4% on ImageNet100-50, and at least +3% overall accuracy on fine-grained datasets (CUB, Scars, Aircraft). These gains are consistent and non-trivial.

2. **Ablation confirms each component's contribution.** Table 4 shows that adding the naive mutual information loss, adapter layer, and channel selection matrix progressively improves accuracy (e.g., +1.3% on CUB novel classes from the adapter layer; +0.8% on Scars novel classes from channel selection). This evidence directly supports the three-component design.

3. **Robustness when the number of novel classes is unknown.** Table 7 shows significant improvements over the baseline on all three fine-grained datasets under a realistic unknown-Cⁿ setting (e.g., +5.8% all-class on CUB), demonstrating practical applicability beyond an idealized setup.

4. **Versatility with different unsupervised losses.** Table 8 shows that the proposed \( \mathcal{L}_{akt} \) consistently improves performance across different choices of \( \mathcal{L}_u \) (pairwise loss, optimal transport loss), indicating the framework is not tied to a specific unsupervised loss formulation.

5. **Quantitative comparison of transfer variants.** Table 6 shows that the proposed nMI outperforms both KL-based and MSE-based explicit transfer (e.g., +1–2% on all-class accuracy across fine-grained datasets), establishing the superiority of the mutual-information formulation.

6. **Ablation of adapter layer depth.** Table 5 shows that a single-layer adapter outperforms deeper variants (e.g., 61.5% novel on CUB with 1 layer dropping to 51.9% with 4 layers), justifying the lightweight design choice.

## Weaknesses

### Fatal

None.

### Major

1. **Critical implementation details of the negative sampling scheme are missing.** The introduction states that the method "adopt[s] a mixed-up negative sample generation scheme in the contrastive learning," and Section 3.3 mentions a "negative sample generator" and negatives stored "in memory." However, the paper provides no details on what "mixed-up" means, how the memory bank is populated and updated, how negatives are sampled (batch vs. full bank), or what the negative set composition is. Since these details are necessary for reproducibility and the InfoNCE-style loss (Eq. 4) depends on negative quality, this omission is significant. *(Note: this is the single highest-leverage fix the authors should address.)*

2. **The two-stage training procedure within the second stage is underspecified.** Section 3.4 describes learning the adapter layer *first* (with \( f_\phi \) fixed) using \( \mathcal{L}_{base} \), and *then* training the joint model \( f_\theta \) with \( \mathcal{L}_{base} + \beta\mathcal{L}_{akt} \). Several critical questions are unresolved: how the 100 training epochs are split between the adapter-learning sub-stage and the joint-model sub-stage; whether the adapter is frozen during joint model training; and whether the channel selection matrix \( \mathbf{W}_s \) is captured once after adapter learning or updated during joint training. These ambiguities make the training dynamics unclear and the design hard to assess or reproduce.

### Minor

3. **The promised \( \beta \) sensitivity analysis is missing.** Section 4.1 states: "For the hyperparameter \( \beta \) that we introduced, we set it to 0.1 for all datasets. We then validate its sensitivity in the ablation study." However, the ablation study (Section 4.3) contains no sensitivity analysis for \( \beta \). Since \( \beta \) controls the strength of the explicit knowledge transfer relative to the base loss, this missing analysis is a gap the paper itself committed to filling.

4. **The iNat21 benchmark is evaluated against only one baseline.** Table 3 compares the proposed method only to SimGCD on the four iNat21 splits. For a benchmark intended to assess the framework's generalization across difficulty levels, comparisons against additional recent GCD methods (e.g., DCCL, PromptCAL, or others from Table 2) would strengthen the benchmark's utility and better demonstrate the method's advantage across difficulty splits.

5. **Standard deviations over multiple runs are not reported.** GCD methods can exhibit variability due to clustering initialization and unsupervised learning. Reporting results from multiple seeds would strengthen the reliability claims, though single-run evaluation is common in the GCD literature.

6. **The number of known and novel classes per iNat21 split is not reported.** This information would aid reproducibility and interpretation of the benchmark results.

### Trivial

7. The baseline experiment numbers in Table 1 ("BL" and "Clu.") are only shown in a figure; including the actual numbers in the text or caption would be helpful for quick reference.

## Nice-to-Haves

- Adding NMI or ARI as complementary metrics would provide a more complete picture, though clustering accuracy is the standard metric in the GCD literature.
- A simple ablation comparing sequential training (as done) vs. joint training of the adapter with the joint model would strengthen the design argument.
- The channel selection matrix mechanism could be better motivated (e.g., as a sparsity-inducing mechanism), though the empirical results already support its utility.

## Removed Points

- **"Channel Selection Matrix is redundant when applied to v"** — This observation is technically interesting but is not a weakness. The reviewer correctly notes that the actual effect of \( \mathbf{W}_s \) is to mask the joint model representation \( \mathbf{u} \) with the same binary mask, which is the intended design. The paper could motivate this better, but the mechanism has clear empirical support (Table 4). Removed because it is not a genuine weakness.

- **"Missing related works"** — Removed per instruction: I cannot verify existence of missing citations from external knowledge.

- **"Formatting/style nitpicks"** — None present in the reviewer's text that need removal.

- **"Missing appendix/structural format complaints"** — The reviewer did not raise these; the parser-stripped sections issue does not apply here.

## Novel Insights

The most interesting observation from the reviewer interactions that goes beyond the paper's own contributions is the implicit tension in the two-stage design: the adapter is trained without any awareness of the distillation objective, yet the joint model is then forced to align to the adapter's output space. Whether this sequential design is intentionally beneficial (e.g., preventing the adapter from collapsing under the distillation objective) or accidentally suboptimal is an open question the authors should address explicitly. The paper's ablations do not currently resolve this, and a comparison with joint training would be illuminating for the community.

## Suggestions

1. **Fully specify the negative sampling scheme**: define the "mixed-up" generation process, memory bank size and update rule, batch construction, temperature role, and negative set composition. This is the single most important fix for reproducibility.
2. **Clarify the two-stage training**: state explicitly whether the adapter is frozen during joint training, how many epochs each sub-stage uses, and why sequential training was chosen over joint optimization.
3. **Add the promised \( \beta \) sensitivity analysis** on at least one dataset (e.g., CUB or Aircraft).
4. **Expand the iNat21 evaluation** to include at least 2–3 additional recent GCD methods (e.g., DCCL, PromptCAL) to strengthen the benchmark's evidence base.
5. Report the known/novel class counts per iNat21 split and add standard deviations over multiple runs where feasible.

## Score and Decision

The paper makes a clear, well-motivated contribution with strong empirical support. The weaknesses are real but addressable — they concern missing implementation details and a gap in the promised analysis, not flaws in the core methodology or evidence. With the suggested clarifications, the paper would be a solid and reproducible contribution to GCD. The missing details in the current form prevent full assessment and reproduction, warranting conditional acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>