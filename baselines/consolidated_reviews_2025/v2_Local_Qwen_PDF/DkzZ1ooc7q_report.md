## Summary
# Final Review Report

## Summary
This paper introduces OmniSep, a unified omni-modal sound separation framework capable of handling text, image, and audio queries, as well as multi-modal composed queries. The authors propose three key components: (1) Query-Mixup, a training strategy that linearly blends cross-modal query features to enable concurrent optimization; (2) Negative Query, a mechanism to eliminate interference sounds by subtracting their embeddings from the target query; and (3) Query-Aug, a retrieval-augmented method that maps unrestricted natural language descriptions to in-domain class embeddings for open-vocabulary separation. Experiments on MUSIC and VGGSOUND-CLEAN+ datasets demonstrate that OmniSep achieves state-of-the-art performance across Text-Queried (TQSS), Image-Queried (IQSS), and Audio-Queried Sound Separation (AQSS) tasks. The paper provides a solid empirical validation of multi-modal joint training for sound separation, though the novelty of the components is incremental, relying heavily on the pre-aligned space of ImageBind.

## Strengths
1. **Unified Omni-Modal Framework:** The paper successfully integrates text, image, and audio queries into a single sound separation model, addressing a clear limitation in prior work where methods were siloed by modality.
2. **Effective Query-Mixup Strategy:** The proposed Query-Mixup training strategy effectively bridges modality gaps, allowing the model to generalize well to single-modal queries at inference time despite being trained on mixed embeddings.
3. **Practical Negative Query Mechanism:** The introduction of negative queries provides a simple yet effective way to enhance separation flexibility by actively suppressing interference sounds, with robust performance across different weight settings.
4. **Comprehensive Empirical Validation:** The experiments cover multiple datasets (MUSIC, VGGSOUND-CLEAN+) and tasks (TQSS, IQSS, AQSS), demonstrating consistent state-of-the-art performance and providing detailed ablations for each component.
5. **Open-Vocabulary Capability:** Query-Aug offers a practical solution for handling unrestricted natural language descriptions by leveraging embedding-space retrieval, significantly improving robustness to out-of-domain text.

## Weaknesses
1. **Incremental Novelty of Components:** The core contributions (Query-Mixup, Negative Query, Query-Aug) are largely incremental adaptations of existing techniques (feature mixing, negative prompting, nearest-neighbor retrieval) rather than fundamentally new mechanisms. The heavy reliance on ImageBind's pre-aligned space means the "unified" capability is inherited rather than learned from scratch.
2. **Training-Inference Distribution Mismatch:** The Query-Mixup strategy creates mixed embeddings during training but uses pure single-modal queries at inference. The paper lacks a theoretical or empirical discussion on how the Separate-Net generalizes across this distribution shift, and the random weight sampling could lead to degenerate cases or gradient instability.
3. **Factual Inconsistency in Results Analysis:** The manuscript claims that Experiment #11 (Query-Aug) achieves "superior performance" compared to Experiment #7 (predefined labels), but Table 3 shows 6.32 SDR vs 6.70 SDR, which is actually lower. This undermines confidence in the results interpretation.
4. **Limited Generalization Validation:** Experiments are confined to VGGSOUND and MUSIC datasets. The model's performance on more complex, real-world audio mixtures with abstract sounds or significant domain shifts is not evaluated, limiting the claim of broad omni-modal applicability.
5. **Deployment Feasibility of Query-Aug:** The Query-Aug method requires access to a full index of training set embeddings at test-time for retrieval. This dependency is not explicitly discussed, potentially impacting the practicality of the open-vocabulary claim in resource-constrained settings.

## Key Issues
1. **Query-Mixup Generalization Mechanism (Major):** The paper does not explain how the Separate-Net learns to handle pure modality queries at inference when trained on linearly mixed embeddings. Clarifying the sampling distribution of weights $w_a, w_v, w_t$ and discussing the modality-invariant representation learning is essential for validity.
2. **Factual Error in Table 3 Analysis (Major):** The claim that OmniSep+Query-Aug (#11, 6.32 SDR) outperforms OmniSep with predefined labels (#7, 6.70 SDR) is mathematically incorrect. This must be corrected to "comparable performance" or "gap narrowing" to maintain scientific integrity.
3. **Tensor Broadcasting Ambiguity in Eq. (2) (Minor):** The equation for predicted masks $\hat{M}_i$ lacks explicit tensor shape definitions for $w_i$, $q_i$, and $\tilde{M}_j$, making reproducibility difficult. Broadcasting dimensions across frequency and time axes should be specified.
4. **Reliance on Pre-trained Alignment (Minor):** The ablation shows a massive performance drop without ImageBind pretraining. The paper should explicitly frame OmniSep as an adapter for pre-aligned multi-modal spaces rather than a standalone unified learner, to avoid overstating novelty.
5. **Missing Variance Discussion (Minor):** OmniSep exhibits higher variance (std) than some baselines in Table 1. Acknowledging this trade-off and attributing it to the broader omni-modal optimization would improve objectivity.

## Actionable Suggestions
1. **Clarify Query-Mixup Sampling and Generalization:** Explicitly state the distribution from which weights $w_a, w_v, w_t$ are sampled (e.g., Dirichlet or uniform with constraints). Add a paragraph explaining how the Separate-Net learns modality-invariant features to generalize from mixed training embeddings to pure inference queries.
2. **Correct Table 3 Analysis:** Revise the text claiming "superior performance" for Experiment #11 to accurately reflect the data (6.32 vs 6.70 SDR). Use phrasing like "highly comparable performance" or "narrows the performance gap significantly."
3. **Specify Tensor Shapes in Eq. (2):** Update Equation (2) to explicitly define the shapes of $w_i \in \mathbb{R}^k$, $q_i \in \mathbb{R}^k$, and $\tilde{M}_j \in \mathbb{R}^{F \times T}$, and clarify that $w_{ij}q_{ij}$ acts as a scalar weight broadcasted across the mask dimensions.
4. **Acknowledge ImageBind Dependency:** In the Method and Conclusion sections, explicitly frame OmniSep as an effective adapter for pre-aligned multi-modal spaces. Acknowledge that the unified capability is inherited from ImageBind, which strengthens the paper's scientific honesty.
5. **Discuss Query-Aug Deployment Constraints:** Add a brief note in Section 3.4 or the Limitations section clarifying that Query-Aug requires access to a compact index of training set embeddings at inference time, and discuss potential mitigations for resource-constrained deployment.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Query-based sound separation (QSS) isolates target signals using semantic queries, but existing methods are siloed within single-modal paradigms (text, image, or audio).
- **S2 (Significance/Challenge):** Real-world audio mixtures require leveraging heterogeneous information across modalities, yet current models lack the flexibility to handle composed multi-modal queries or open-vocabulary descriptions.
- **S3 (Prior Gap):** Prior multi-modal approaches suffer from unfixed training objectives and rely on predefined class labels, limiting generalization and manipulation flexibility.
- **S4 (Proposed Method):** We introduce OmniSep, a unified framework that employs Query-Mixup to blend cross-modal features during training, negative queries to actively suppress interference, and Query-Aug for retrieval-based open-vocabulary separation.
- **S5 (Key Result & Implication):** Experiments on MUSIC and VGGSOUND-CLEAN+ demonstrate state-of-the-art performance, improving Mean SDR by up to 4.36 dB and enabling robust separation with unrestricted natural language queries.

### Introduction Outline (Complete)
- **P1 (Big Picture & Evolution):** Introduce sound separation's evolution from domain-specific (music/speech) to universal query-based methods (TQSS, IQSS, AQSS), highlighting the semantic advantage of queries.
- **P2 (Concrete Gap & Challenges):** Identify three critical limitations of current single-modal silos: (1) inability to handle composed multi-modal queries, (2) lack of flexibility in removing undesired interference, and (3) restriction to predefined class labels.
- **P3 (Proposed Solution & Intuition):** Present OmniSep as a unified solution. Explain the intuition behind Query-Mixup (bridging modality gaps via mixed embeddings), negative queries (vector subtraction for interference removal), and Query-Aug (embedding-space retrieval for open vocabulary).
- **P4 (Evidence Preview):** Summarize key empirical outcomes: consistent SOTA across TQSS/IQSS/AQSS, robust negative query manipulation, and significant performance recovery for out-of-domain text.
- **P5 (Contribution Summary):** List the four main contributions clearly, focusing on the unified framework, the three novel mechanisms, and the comprehensive empirical validation.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Correct factual error in Table 3 analysis (6.32 vs 6.70 SDR). | Restores scientific integrity and prevents reviewer rejection for inaccuracy. | Low |
| **P0** | Clarify Query-Mixup weight sampling distribution and generalization mechanism. | Validates the core training strategy and addresses distribution mismatch concerns. | Medium |
| **P1** | Specify tensor shapes and broadcasting in Eq. (2) and Eq. (3). | Improves reproducibility and implementation clarity. | Low |
| **P1** | Acknowledge ImageBind dependency and frame OmniSep as an adapter. | Strengthens scientific honesty and bounds novelty claims appropriately. | Low |
| **P2** | Discuss deployment constraints of Query-Aug (training set index access). | Enhances practical applicability discussion. | Low |
| **P2** | Add variance discussion for higher std in Table 1 results. | Improves objectivity and result interpretation. | Low |

**Revision Order:** Start with P0 items to fix critical validity and factual issues. Then proceed to P1 items for methodological clarity. Finally, address P2 items for completeness and practical framing.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | OmniSep vs Baselines | MUSIC, VGGSOUND-CLEAN+ | SDR, Med SDR | OmniSep achieves SOTA across TQSS, IQSS, AQSS. | Unified omni-modal capability. | Higher variance in some settings. |
| E2 | Query-Mixup Ablation | VGGSOUND-CLEAN+ | Avg SDR | Mixup outperforms single-modal and joint training. | Query-Mixup effectiveness. | Lacks theoretical generalization proof. |
| E3 | Negative Query Analysis | MUSIC-CLEAN+, VGGSOUND-CLEAN+ | SDR vs $\alpha$ | Proportional weighting is robust and effective. | Negative query flexibility. | Requires manual $\alpha$ selection. |
| E4 | Query-Aug Open-Vocab | VGGSOUND-CLEAN+ (GPT-rewritten) | SDR | Query-Aug recovers performance for unrestricted text. | Open-vocabulary capability. | Requires training set index at test-time. |
| E5 | ImageBind Ablation | VGGSOUND-CLEAN, MUSIC | SDR | Performance drops significantly without pretraining. | Reliance on pre-aligned space. | Confirms incremental novelty. |

### Research-Theme Gap Diagnosis
The core research value lies in adapting pre-aligned multi-modal spaces for sound separation. However, the causal link between Query-Mixup and improved generalization is not fully established, and the open-vocabulary claim is bounded by retrieval dependencies.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Query-Mixup Generalization | Mixed embeddings force modality-invariant features. | Train with Dirichlet vs Uniform weights. | Single-modal training. | SDR, Variance | Stable SDR across weight distributions. | Low | Validates training mechanism. |
| Query-Aug Independence | Retrieval can be approximated without full index. | Use k-NN on a subset of class embeddings. | Full index retrieval. | SDR drop | <0.5 SDR drop with 10% index. | Low | Improves deployment feasibility. |
| OOD Robustness | OmniSep generalizes to unseen sound categories. | Evaluate on AudioSet subset not in VGGSOUND. | CLIPSEP, AudioSEP. | SDR, SI-SDR | Competitive performance on OOD data. | Medium | Strengthens generalization claims. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
**Post-Revision Target:** [7.5, 8.5]/10

**Scoring Rationale:** The paper presents a solid and well-executed unified framework for omni-modal sound separation with strong empirical results. The score is moderated by the incremental novelty of the core components (largely adapting ImageBind's alignment), the training-inference distribution mismatch in Query-Mixup, and a factual inconsistency in the results analysis. Addressing the P0/P1 revision items, particularly clarifying the generalization mechanism and correcting the Table 3 analysis, would significantly improve the paper's scientific rigor and defensibility, justifying the higher post-revision target.