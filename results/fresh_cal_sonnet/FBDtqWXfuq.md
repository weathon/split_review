Now let me run calibration search to score the paper.Now I have enough to write the final consolidated review. Let me synthesize everything.

---

## Summary

The paper introduces Modality-Collaborated Federated Learning (MCFL), a new federated learning setting in which each client holds uni-modal data of a single modality (e.g., vision or language only), and the goal is to improve performance for each modality individually through collaboration. To address challenges of model heterogeneity and modality bias in this setting, the paper proposes FedCola, a framework built on a modality-agnostic transformer with three components: Attention Sharing (sharing self-attention layers across modalities), Modality Compensation (padding missing-modality weights from the previous global model during aggregation), and Modality Warm-up (warming shared parameters with one modality before multi-modal training). Evaluations across 12 FL configurations and two dataset pairs show FedCola consistently outperforms the Uni-FedAVG baseline and an adapted CreamFL, with no additional computation or communication cost.

---

## Strengths

1. **Clearly differentiated new setting (MCFL)**: Section 2 formally defines MCFL as distinct from Federated Multi-Modal Learning (FMML), which requires multi-modal clients for alignment. The distinction is principled — MCFL requires no multi-modal data, no alignment labels, and no public dataset — and is practically motivated by scenarios like hospitals with uni-modal imaging vs. text records. Figure 1 illustrates the contrast clearly.

2. **Consistent improvements across 12 FL configurations**: Table 4 shows FedCola achieving the highest averaged accuracy in all 12 settings (four client configurations × three data situations), covering both a low-correlation general domain (CIFAR-100/AGNEWS) and a high-correlation medical domain (OrganAMNIST/MTSamples). The improvements over Uni-FedAVG are notable (e.g., medical N=4, α=0.5, r=0.5: 65.79% vs. 57.23%).

3. **No additional computation or communication cost**: Section 6.3 and Figure 6 show FedCola maintains the same resource footprint as Uni-FedAVG, while CreamFL requires 1.97× the computation per round. This is a concrete efficiency advantage, and the elimination of a public dataset reduces privacy-leakage exposure.

4. **Empirical verification of cross-modal transfer**: Figure 7 shows a positive correlation between increased capability in one modality and improved performance in the other — providing direct, albeit correlational, evidence that FedCola's parameter-sharing achieves genuine cross-modal knowledge transfer rather than simply training modalities independently.

---

## Weaknesses

### Fatal
None.

### Major

- **Circular evaluation design**: All three design choices (Attention Sharing in §5.1, Modality Compensation in §5.2, and vision Modality Warm-up in §5.3) were derived empirically on CIFAR-100/AGNEWS. These same datasets then form the primary basis for FedCola's final evaluation (Table 4) and the only dataset used for the ablation in Table 5. The medical domain is present in Table 3 (warm-up) and Table 4 (final evaluation), but the full ablation of AS+MC+MW is not reported on the medical pair. As a result, the selected configuration is optimized to the same distribution used for reporting. This does not invalidate FedCola's advantage over baselines (since those baselines are external), but it inflates confidence in the specific component design and prevents establishing whether the design generalizes across dataset pairs.

- **No variance or significance reporting**: Across all tables, no standard deviations, confidence intervals, or significance tests are reported. The FL setup involves Dirichlet-partitioned data (α=0.5 or 0.1) with random client sampling, both of which introduce meaningful run-to-run variance. The paper explicitly claims Modality Compensation and Modality Warm-up provide "marginal but crucial" improvements of approximately 0.5% and 0.3% respectively (Table 5). Without variance estimates, these gains cannot be distinguished from noise. This is a genuine evidential gap, not a presentation issue.

### Minor

- **Attention Sharing dominates; co-equal framing of all components is unsupported**: Table 5 shows vision accuracy rises from 3.58% to 56.17% upon adding Attention Sharing — the paper correctly acknowledges this is "the most significant impact." However, the paper then frames MC and MW as co-equal innovations that are "marginal but crucial," when their contributions (≈0.5% and ≈0.3%) are unverifiable without variance data. In one imbalanced ablation (footnote 2), MC shows a larger gain (71.41%→73.01%), which is a useful supporting point — but it appears only in a footnote and only for one configuration. The paper should either restrict claims for MC and MW to the imbalanced regime where their effect is clearer, or provide ablations across both dataset pairs.

- **Vanilla MAT failure framed as modality-specific when it is a general FedAVG imbalance artifact**: Section 4.1 attributes the "catastrophic failure" of Vanilla MAT to a modality gap, but the paper itself concedes: "the total number of training samples in the language modality (120,000) far exceeds that in the vision modality (50,000). This imbalance causes the default inter-modality aggregation to weigh the parameters based on the number of samples." Data-weighted FedAVG producing bias under group-size imbalance is a well-known pathology in any FedAVG scenario, not a modality-specific phenomenon. The observation is real and the solution (Attention Sharing) is valid, but the framing slightly overstates the novelty of the failure-mode diagnosis.

- **Vision warm-up advantage may be confounded by ViT-Small pretraining**: Section 5.3 concludes that "vision knowledge provides better initialization for the shared parameters during the warm-up," but the paper uses a pre-trained ViT-Small backbone already trained on ImageNet-scale visual data. This means the shared attention layers already encode vision-friendly features before any FL round. The paper does not rule out that the vision warm-up advantage derives from this pre-existing bias rather than from any domain-agnostic initialization property.

- **Figure 7 (modality collaboration verification) is insufficiently detailed**: The figure shows a positive correlation between "increased capability of one modality" and "the other modality's performance," but the experimental setup is not described clearly enough to interpret the result. Specifically: how is "increased capability" operationalized? If it is done by increasing training data for one modality, this simultaneously changes aggregation weights (data-weighted FedAVG), which could independently explain the performance change in the other modality.

### Trivial

- The Rademacher complexity bound cited in Section 5.2 to motivate Modality Compensation — $\mathcal{O}(\sqrt{d_s + \log(1/\delta)} / |\mathcal{D}|)$ — reduces to "more data → better generalization," which is trivially true. The formal connection between this bound and the specific design of Modality Compensation (padding with previous global model weights) is not established. This motivational argument is decorative rather than substantive.

---

## Nice-to-Haves

- Including the full ablation (Table 5 equivalent) on the medical dataset pair (OrganAMNIST/MTSamples) would establish whether AS dominates and MC/MW contribute similarly in the high-correlation domain — addressing both the circular evaluation concern and the generalizability question.
- A brief sensitivity analysis of warm-up duration and which modality is selected for warm-up would make FedCola more actionable for practitioners deploying it in new settings (currently these choices are inherited from CIFAR-100/AGNEWS experiments).
- Probing the shared attention layers after FedCola training — e.g., comparing attention patterns to those of a centralized multi-modal model — would strengthen the cross-modal transfer claim in Section 7 beyond a correlational argument.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **CreamFL comparison is "structurally compromised"** (Harsh Critic): The critic notes that adapting CreamFL to MCFL via a public dataset operates outside CreamFL's design intent and the comparison is thus unfair. However, per review policy, weaknesses about unfair baseline comparisons are removed when the asymmetry hurts the baseline method (CreamFL), not the paper's method. The paper itself notes "CreamFL cannot always outperform Uni-FedAVG, demonstrating the difficulty of MCFL" — this framing is transparent about CreamFL's limitations in this adapted setting.

- **Missing >2-modality experiments** (Harsh Critic): The paper explicitly scopes to two modalities and states in Section 5.4 "We regard further studies with more modalities as our future work." Demanding out-of-scope experiments violates the soft rule against scope creep.

- **Modality Compensation's unacknowledged connection to FedProx** (Harsh Critic): Potentially an interesting observation, but confirming that this connection constitutes a scholarly omission would require external sources; per review policy this is removed.

- **Strength: "Systematic empirical study that answers three key research questions"** (Strength Finder): This is accurate but largely generic as a strength claim since it is equivalent to saying "the paper has an ablation study." The more specific content of that study (AS dominance) is already captured in the weaknesses.

- **Strength: "Comprehensive evaluation across practical challenges"** (Strength Finder): Partially valid — the paper does evaluate 12 configurations. However, "comprehensive" is somewhat overstated given that all configurations use only two dataset pairs and two modalities. Retained in spirit under Strength #2 with more measured language.

---

## Novel Insights

The core novel observation of this paper — that multi-modal knowledge can be obtained by aggregating parameters from independent uni-modal clients, rather than requiring aligned multi-modal data on individual clients — is genuinely interesting and underexplored. The attention-sharing mechanism echoes VLMo in the centralized setting, but its application in a federated context with entirely disjoint modalities per client is a non-trivial adaptation. The finding that attention layers serve as a natural cross-modal "meeting point" while modality-specific FFN layers preserve unimodal performance provides a concrete, implementable insight for the FL community. The analysis is currently limited to two modalities and correlational evidence, but the principle is worth developing.

---

## Evaluation Axes

- **Originality**: Moderate-high. MCFL is a clearly differentiated new setting, not simply an incremental refinement of FMML. The component designs borrow from centralized multi-modal learning (VLMo) but their federated application is novel.
- **Importance of research question**: High. MCFL addresses a practical gap — enabling hospitals or other domain-specific institutions with heterogeneous uni-modal data to collaborate.
- **Claims well supported**: Moderate. The main claim (FedCola > baselines) is well supported by Table 4. The subsidiary claims (MC and MW are "crucial") are inadequately supported without variance data.
- **Soundness of experiments**: Moderate. Comprehensive in terms of FL configurations but marred by the circular evaluation design and absence of variance reporting.
- **Clarity of writing**: Good. The paper is well-organized; the research question framing in Section 5 is clear.
- **Value to research community**: Good. As a well-characterized new setting with a strong baseline framework, this provides a useful foundation for future work.

---

## Suggestions

1. Run the full ablation (Table 5) on the medical dataset pair; report results alongside CIFAR-100/AGNEWS.
2. Report standard deviations (or at minimum, repeat each experiment 3 times and report mean ± std) for all entries in Tables 3–5.
3. Reframe the claims about MC and MW — either restrict them to the imbalanced regime where their effect is clearer (as in footnote 2), or acknowledge that their isolated contributions are small and their value is incremental.
4. Add a brief discussion of the ViT-Small pretraining confound in the vision warm-up analysis; this is a one-paragraph acknowledgment that costs nothing and improves intellectual honesty.
5. Describe the Figure 7 experiment operationally: what mechanism is used to vary "modality capability," and how are aggregation dynamics controlled?

---

## Score and Decision

**Round 1 bracket**: 5–7, based on comparisons to rejected FL papers scoring 3–5 and strong papers scoring 8+.

**Round 2 anchors examined:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| TKDwsJmrDJ | 6.00 | R1 | Heterogeneous NLP FL — similar new-setting motivation; paper under review has cleaner contributions but circular evaluation. Rejected. |
| 7pDI74iOyu | 6.00 | R2 | Language-driven FL for non-IID — similar image-text transformer FL, comparable evaluation scope, accepted. Similar quality to paper under review. |
| U0P622bfUN | 5.25 | R2 | Federated Generative Learning — paper under review is stronger (more novel setting, better evaluation). Rejected. |
| Nb7Akh3SjN | 4.25 | R1 | Data disentanglement FL — weaker contribution, limited evaluation. |
| 44hcrfzydU | 6.67 | R2 | FedTMOS one-shot FL — specialized to Tsetlin Machine, limited scope. Accepted. |
| NW31gAylIm | 5.75 | R2 | Federated text-driven prompt generation — comparable evaluation quality, slightly narrower scope. Accepted. |
| jhiByZpuIS | 4.67 | R1 | MSfusion for resource-constrained large model FL — weaker novelty. Rejected. |
| BKinRUoBN9 | 5.50 | R2 | Cross-modal KD under distribution shifts — narrower scope, no new setting. Rejected. |
| XKv29sMyjF | 5.60 | R2 | Query-based Knowledge Transfer — different angle but comparable FL heterogeneity scope. Accepted. |
| C7XoUdJ5ZC | 3.00 | R1 | FL with feature augmentation — clearly weaker. Rejected. |

**Bracket narrowing**: Round 2 anchors cluster around 5.5–6.5. The paper under review is clearly stronger than U0P622bfUN (5.25) and comparable to 7pDI74iOyu (6.0, Accepted) and NW31gAylIm (5.75, Accepted). Its circular evaluation and missing variance are real concerns at the level that held the TKDwsJmrDJ (6.0, Rejected) back, but the MCFL setting contribution is more novel and the evaluation is more comprehensive (12 configurations across two domains). The paper sits at the 6.0 level — a borderline accept with substantive revision needs.

**Final score: 6.0 — Marginal Accept**

The setting contribution is genuine, the framework is consistently effective, and the paper is well-motivated. The major issues (circular evaluation design and absent variance reporting) are resolvable in revision and do not invalidate the core claims. The paper fits the standard of a solid new-setting paper that serves as a useful baseline for future work in this direction.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>