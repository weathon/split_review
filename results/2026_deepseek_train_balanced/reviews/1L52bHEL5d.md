Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper formulates the missing-modality problem in multimodal recognition as a test-time adaptation (TTA) task, eliminating the need for retraining. MiDl minimizes the mutual information between model predictions and modality type (to build invariance) while using KL self-distillation against the original model (to preserve performance on complete-modality inputs). The method is self-supervised, online, and architecture-agnostic. Experiments on Epic-Kitchens and Epic-Sounds with MBT and self-attention backbones show consistent improvements (e.g., 5–7% on Epic-Kitchens at 50–75% missing rates) over non-adapted baselines and existing TTA methods.

## Strengths

- **Novel problem formulation with clean theoretical grounding**: The paper is the first to formulate missing modality as a TTA problem. The objective (Eq. 1) directly connects MI minimization to the desired invariance property — if MI($f_\theta(x;m), m)=0$, the output is provably independent of the modality present (Section 4, line 50). This goes beyond heuristic design.

- **Controlled ablation proves both components are necessary**: Section 6.4 (Table 6) isolates each loss term. KL-only yields no adaptation (the model doesn't change). MI-only causes significant degradation at low missing rates. Only the full MiDl (MI + KL) delivers consistent gains across all missing rates. This provides direct causal evidence for the design.

- **Consistent generalization across architectures and missing-modality types**: Section 6.1 (Table 3) replicates all experiments with a vanilla self-attention architecture and shows consistent improvements (e.g., 1.1% at 50% missing rate). Section 6.2 (Table 4) shows gains when the non-dominant modality is missing. Section 6.3 (Table 5) demonstrates a 9.5% improvement on the Omnivore backbone under 25% missing rate, showing pretraining-agnosticism.

- **Long-term adaptation yields increasing returns**: Section 5.3 (Table 2) shows that as the adaptation stream lengthens, MiDl's gains grow — improving the baseline by 4.3% on Epic-Sounds and 8.8% on Epic-Kitchens at 75% missing rate. This contrasts with prior TTA methods that plateau.

- **Warm-up on out-of-domain data further boosts performance**: Section 5.4 shows that pre-adapting on 5,000 unlabeled Ego4D clips yields further gains, including 8% on Epic-Kitchens at 100% missing rate, demonstrating practical utility when auxiliary unlabeled data is available.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Structural limitation: adaptation requires complete-modality samples.** MiDl explicitly skips adaptation on incomplete samples (line 75: "If $x_t$ is with complete modalities then $g$ adapts … else set $\theta_{t+1}=\theta_t$"; line 71: "propose to conduct our adaptation step only when $S$ reveals $x_t$ with complete modalities"). At $p_{AV}=0$ (100% missing rate) in the standard online evaluation (Section 5.2), the method performs zero adaptation and yields the same results as the non-adapted baseline. Gains at 100% missing rate reported in Table 2 come from the Long-Term Adaptation setup where adaptation is performed on a separate stream of training data with complete modalities *before* evaluation. While the paper states this fact clearly in the body (lines 71, 75, 77–78), it does not discuss this as a limitation in the conclusion. The inability to extract *any* learning signal from the test distribution when it contains no complete-modality samples is an inherent constraint that should be acknowledged as a limitation rather than simply noted as a design choice.

- **Absolute gains are modest in some settings and computational cost is high.** On Epic-Sounds at 50% missing rate, MiDl improves from 37.1% to 38.8% (1.7 pp). On Epic-Kitchens at 50% missing rate, the gain is 5 pp (50.2% to 55.2%). Meanwhile, inference cost increases by 5× (3 forward passes + 1 forward through frozen model + backward pass), reduced to 2× with parallelism (Section 6.5). For the motivating use case of wearable devices (lines 10, 20, 73), this latency increase is substantial, and the paper does not discuss the practical cost-benefit tradeoff. A practitioner evaluating deployment needs to know whether the modest accuracy improvements justify the added computation and latency.

- **Generalization claims are broader than the experimental evidence.** The paper claims MiDl is "agnostic to the pretrained model architecture, the dataset, and the specific type of missing modality" (lines 21, 79, 199). The evidence covers two datasets from a single domain (egocentric cooking footage — Epic-Kitchens and Epic-Sounds share the same video collection), two transformer-based architectures (MBT and vanilla self-attention), and one additional pretraining strategy (Omnivore). Testing on a non-egocentric multimodal benchmark (e.g., Kinetics-Sounds) or a non-transformer architecture would substantially strengthen the "agnostic" claims. The claims are not false but over-extend relative to the experimental scope.

- **"First" claims could be presented more cautiously.** The paper asserts it is the "first" TTA method for missing modalities in the abstract, line 21, and line 79. While plausible, verifying a negative claim about the literature is inherently difficult, and softer wording would better reflect this uncertainty.

- **No empirical verification that MI actually decreases during adaptation.** The method's theoretical motivation (Section 4) centers on minimizing MI between predictions and modality type, but no direct measurement of MI values over the course of adaptation is provided. Reporting this would strengthen the connection between the theoretical justification and empirical results.

### Trivial

- **No error bars in the main tables.** Standard deviations are deferred to Table 11 in the appendix. For improvements as small as 1.1–1.7 pp, showing variance alongside the main results would help readers assess significance.

- **Section organization.** The MiDl method is introduced within Section 3.2 ("Evaluation Protocol") rather than having its own dedicated section, making the exposition slightly harder to follow.

## Nice-to-Haves

- Testing on a non-egocentric multimodal benchmark (e.g., Kinetics-Sounds) would strengthen the generalization claims.
- An analysis of what the adapted model learns (e.g., attention patterns, feature importance, or representation similarity before/after adaptation) would deepen the empirical contribution.
- A discussion of whether MiDl could be extended to extract a learning signal from incomplete-modality samples — even a negative result showing why this fails would help define the boundaries of what is possible without complete-modality data.

## Removed Points

- **Criticism about baseline comparison being "staged" (Harsh Critic, Issue 2).** The critic argued that comparing against Shot and ETA is uninformative because they are not designed for missing modality. However, the paper explicitly acknowledges this (line 108: "TTA methods are designed to tackle covariate domain shifts and, thus, are not tailored to enhance performance under this specific type of domain shift"). The baseline set appropriately demonstrates that this is a *different* shift from standard covariate shifts. The critic's proposed alternatives (random modality-dropout at test time, learned priors from training data) either require training data (violating the TTA premise) or are already implicitly covered by the reported unimodal baselines. Per the guidelines: (a) any asymmetry favors the baselines, not the authors' method; (b) the critic's suggestions demand methods outside the paper's stated scope; and (c) the paper already includes unimodal rows as reference points. Removed.

- **Various speculative concerns from the harsh critic's section-by-section notes.** Generic concerns about "could the metric be measuring a proxy" and "are confounders controlled" that are not anchored in specific paper content are removed per the filtering guidelines. These are areas-of-concern sweeps, not identified problems.

- **Generic strengths from the Strength Finder.** Generic statements like "this paper addressed an important problem" are removed per the filtering guidelines. Only strengths that are concrete, specific to this paper, and grounded in evidence are retained.

- **Demand for comparing against adapted missing-modality methods requiring retraining.** Removed because it contradicts the paper's premise of test-time-only adaptation without access to training data.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add an explicit limitations paragraph to the conclusion discussing the requirement for complete-modality samples during adaptation and the computational cost.
- Measure and report mutual information values over the course of adaptation to directly verify the claimed mechanism.
- Include a cost-benefit analysis (accuracy gain vs. latency at different missing rates) to help practitioners assess deployment tradeoffs.
- Include error bars or confidence intervals in the main accuracy tables rather than deferring them entirely to the appendix.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>