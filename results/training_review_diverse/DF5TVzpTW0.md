Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper introduces DPPN (Defense through Perturbing Privacy Neurons), a method that (1) identifies a small subset of embedding dimensions ("privacy neurons") correlated with a sensitive token via differentiable mask learning, and (2) perturbs only those dimensions using a one-sided (neuron-suppressing) directional noise. The goal is to defend against embedding inversion attacks while preserving downstream utility. Experiments across six datasets, multiple attack models, and embedding models show improved privacy-utility tradeoffs compared to isotropic noise baselines.

## Strengths

1. **Differentiable neuron mask learning for targeted privacy-neuron identification.** Unlike prior work that adds uniform noise to all embedding dimensions, DPPN learns a binary mask per sensitive token via a HardConcrete distribution, enabling selection of only the top-k privacy-sensitive dimensions. Figure 2 validates that these top neurons have significantly higher sensitivity (avg. 0.04) than tail neurons (near zero), with a Wilcoxon p-value of 1.30e−21.

2. **Neuron-suppressing perturbation demonstrably outperforms isotropic noise on the same dimensions.** Table 2 is the critical ablation: when LapMech and PurMech are applied *only to the same top-k privacy neurons* detected by DPPN, they produce negligible leakage reduction (even slight increases). In contrast, DPPN's suppress perturbation applied to the same neurons reduces leakage by 15.44% and improves downstream performance by 45.12% at r=10%. This cleanly isolates the benefit of the suppress direction from the benefit of selective targeting — directly addressing the confounded-comparison concern.

3. **State-of-the-art privacy-utility tradeoff across datasets.** On STS12 at ε=2, DPPN reduces Leakage from 60% (unprotected) to 13%, while baselines only reach 22% (Table 1). This pattern holds across FIQA, PII-Masking300K, and MIMIC-III datasets.

4. **Black-box defense approaches white-box performance.** The black-box detection method (DPPN) performs within 3–6% absolute Leakage difference of the white-box Oracle (FGSM-based) at ε=2 (Figure 4) and achieves 32–51% neuron overlap with the Oracle for top 10–20% neurons (Figure 5). This demonstrates the learned mask effectively approximates ground-truth neurons without access to the attack model.

5. **Robust across multiple attack models and embedding models.** Table 3 shows consistent gains against Vec2text, GEIA, and MLC (e.g., 88% relative leakage reduction under Vec2text at ε=1). Table 5 confirms similar gains on GTR-base, Sentence-T5, and SBERT.

6. **Effectiveness on real-world sensitive data.** On MIMIC-III clinical notes, DPPN lowers sex information leakage from 88% (unprotected) to 17%, whereas baselines only reach 43% (Table 4). The case study (Table 6) shows DPPN preserves 62% semantic similarity while protecting sensitive tokens, compared to 11% for baselines at the same perturbation level.

## Weaknesses

### Fatal
None.

### Major
None. The reviewer's primary concern (confounded comparison) is substantially addressed by the existing ablation in Table 2, which shows LapMech and PurMech applied to the same top-k privacy neurons produce negligible benefit while the suppress method produces large gains. The remaining issues are at the minor/trivial level.

### Minor

1. **Privacy metrics lack full operational precision.** "Leakage" is defined as "the attack model's accuracy in predicting sensitive tokens" and "Confidence" as "the attack model's maximum probability of predicting sensitive tokens." For sentence-level attacks (Vec2text, GEIA) that reconstruct full sentences, it is unclear how token-level accuracy is computed — exact match, substring match, or position-independent detection. The paper should specify the exact protocol for extracting and evaluating predicted sensitive tokens from reconstructed sentences. While the relative comparisons are internally valid, absolute numbers are difficult to reproduce without this detail.

2. **Architecture of the classifier Pθ is underspecified.** The paper mentions "a multi-layer neural network parameterized by θ" (line 102) but provides no details on the number of layers, hidden dimensions, activation functions, optimizer, or training hyperparameters. This affects reproducibility of the mask learning component.

3. **Scaling of ε in Table 2 is not explicitly clarified.** The caption states "ε=2" but does not say whether the √(k/d) scaling (described in Section 4.1 for DPPN) is also applied when LapMech and PurMech perturb only the top-r% neurons in Table 2. Since the interpretation of the ablation depends on whether total noise variance is held constant, this needs explicit clarification.

4. **The external embedding model used for semantic similarity (Section 7) is not named.** The paper assesses reconstructed sentence fidelity "using cosine similarity from an external embedding model" (line 243) but does not identify which model. This should be specified for reproducibility.

5. **Variance/standard deviations are not reported for all experiments.** While Tables 1 and 5 mention standard deviations over 5 runs, Tables 2, 3, 4, and 6 do not include variance information. Given the method involves multiple stochastic components (concrete distribution sampling, noise injection), confidence intervals would strengthen reliability claims.

6. **The method's token-specific nature and scaling receive limited discussion.** The defender must pre-specify sensitive tokens T, construct D⁺/D⁻ for each, and learn a separate mask per token. The paper acknowledges this scope (Goal 1 in Section 2.2) and provides partial evidence for implicit generalization to semantically similar words (Section 5.3, Figure 6). However, practical questions about scaling to many tokens and generalization to unknown sensitive tokens are not discussed. This limits the applicability discussion but does not invalidate the core contribution.

### Trivial

- The claimed ranges in the abstract ("5-78% privacy leakage reduction, 14-40% downstream improvement") are wide and presented without immediate context. While the full paper contextualizes them, including a median or representative setting in the abstract would improve communication.
- Figure 5 shows 51% top-20% neuron overlap between black-box and white-box detectors, meaning nearly half the selected neurons differ. The paper notes DPPN's performance remains competitive despite this, but the observation warrants a brief explanation (e.g., whether mismatched neurons are functionally similar).

## Nice-to-Haves

- A formal or geometric argument for why one-sided suppression outperforms isotropic noise would strengthen the paper beyond the intuitive 2D visualization (Figure 3). Showing, for example, that the suppress direction reduces the expected distance between D⁺ and D⁻ embedding means more than isotropic noise at equal variance.
- An ablation of k (the number of perturbed neurons) to justify the default choice of 20% and show sensitivity.
- A comparison with a simple adversarial training baseline (e.g., Coavoux et al. 2018) would broaden the evaluation, though the paper's focus on perturbation-based methods makes this optional.

## Removed Points

- **"Confounded comparison as a fatal structural issue"** — This overstates the problem. Table 2 in the paper already provides the controlled ablation the reviewer demands, applying LapMech and PurMech to only the top-k privacy neurons (with the same detection method). The results show these baselines produce negligible effect while DPPN's suppress method produces large gains. The reviewer's concern about ε scaling clarity in Table 2 is valid (kept in minor), but the claim that the evaluation "confounds two design choices" without separation is inaccurate given the existing Table 2.
- **"Missing adversarial training comparison"** — The paper scopes itself to noisy embedding methods and explicitly discusses adversarial training as a separate line of work in Section 8. Criticizing its absence evaluates the paper against a standard it never set.
- **"Missing code availability"** — While listed by the reviewer, code availability is not a standard requirement for conference submissions and does not weaken the paper's claims.

## Novel Insights

The reviews surface one genuinely useful observation: the paper's core contribution is the *combination* of selective neuron detection and one-sided noise injection, and the existing Table 2 already separates these factors reasonably well. The main gap is not in the evaluation design but in the clarity of reporting (scaling, metric definition, architecture details). The semantic grouping of privacy neurons (Figure 6: semantically similar words share neuron indices, providing implicit protection for related tokens) is an interesting qualitative finding that the paper could develop further — it partially mitigates the token-specificity concern.

## Suggestions

1. Clarify whether the √(k/d) scaling is applied to *all* methods in Table 2 (LapMech, PurMech, and Suppress) when they operate on only the top-k neurons, or only to DPPN's suppress method. State this explicitly in the caption.
2. Provide the exact operational definition of Leakage for sentence-level attacks (Vec2text, GEIA): how is the predicted sensitive token extracted from the reconstructed sentence, and what constitutes a "correct" prediction?
3. Specify the architecture, training hyperparameters, and optimizer for Pθ in Section 3.2.
4. Name the external embedding model used for semantic similarity in the case study (Section 7).
5. Add standard deviations or confidence intervals to Tables 2, 3, 4, and 6 for completeness.
6. Add a brief discussion of practical considerations when protecting many tokens (e.g., computational cost, shared neurons between related tokens), leveraging the semantic grouping finding from Figure 6.

## Score and Decision

The paper presents a well-motivated idea with a clean two-component design (neuron detection + directional perturbation) and provides reasonably thorough experimental validation. The primary concern raised by the harsh critic — that the evaluation confounds two design choices — is addressed by the existing Table 2, which separates them and clearly demonstrates the advantage of the suppress perturbation. The remaining weaknesses are in clarity and completeness of reporting, not in the soundness of the core claims. The paper makes a genuine contribution to privacy-preserving text embeddings.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>