Now I have a thorough understanding of both the paper and the calibration anchors. Let me write the final review.

---

## Summary

This paper proposes OML, a brain-inspired online multimodal learning network with a hierarchical architecture of feature neurons, unimodal association neurons, and multimodal association neurons connected by ascending, descending, and lateral pathways. The network supports continuous learning of new multimodal concepts without forgetting, detects conflicts between new inputs and prior knowledge, and interactively resolves them through simulated user questions. A key technical contribution is a reference extraction algorithm that uses the coefficient of variation of descending signals to autonomously determine which visual features a word refers to. Experiments on small vision-audition-taste datasets demonstrate stability under open-world evaluation and superiority over existing online methods.

## Strengths

- **Novel reference extraction algorithm grounded in signal stability**: The method (Section 3.4, Eq. 7) uses the coefficient of variation of descending signals over time to identify which feature dimensions a word actually refers to — e.g., distinguishing that "red" refers to color features while "apple" refers to shape+color. The precise referring experiment (Table 2) shows OML maintaining 87.8% V→A accuracy on E-Fruits in the open environment, while offline methods drop 6–25 points from their baseline performance. This is a genuinely under-explored problem in multimodal learning and the proposed solution is elegant.

- **Architecture with ascending, descending, and lateral pathways that enable bidirectional cross-modal recall and conflict detection**: The network design (Section 3, Figure 2) supports four learning scenarios (Section 3.5) based on whether each channel recognizes its input, with conflict detection emerging naturally from mismatches between ascending and descending activation patterns. The modality extension experiment (Table 3) shows that frequency-based routing via the λ parameter allows OML to correctly route taste-concept words (e.g., "tián") to the taste channel and color words to the visual channel, while AEN cannot distinguish between them.

- **Stable online learning under open-world evaluation**: In open-environment experiments (Tables 1–3), OML maintains stable accuracy while offline methods (DAE, DBM, DJSRH, NRCH, FUME) suffer catastrophic drops — e.g., DAE drops from 67.0 to 52.3 V→A on Fruits while OML achieves 89.8%. This validates the claimed resistance to catastrophic forgetting in a streaming setting.

## Weaknesses

### Fatal

None. The core contributions are conceptually sound, and while the experiments are limited, they do not invalidate the method's claims. The weaknesses below are serious but addressable with additional experiments.

### Major

- **No ablation studies to isolate contributions of individual components**: The paper claims four key innovations — conflict detection, reference extraction, lateral connections, and human-in-the-loop interaction — but presents no experiment that isolates any of them. Without ablations, it is impossible to tell whether the reported gains come from the claimed innovations or from simpler aspects of the architecture (e.g., the hierarchical structure alone, or just having more parameters). For instance, disabling the reference extraction algorithm and using all feature dimensions would directly test whether the coefficient-of-variation method actually matters. This is a standard expectation for any paper proposing multiple architectural components, and its absence substantially weakens the evidentiary support for the paper's claims.

- **Human-in-the-loop interaction is simulated, not evaluated**: The paper states (Section 4) that "if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive." This means the entire interactive loop — which is one of the two defining attributes the paper claims for its model (Introduction, attribute 2) — is reduced to a timeout that defaults to "yes." There is no experiment varying the quality or availability of feedback, no measurement of how often conflicts are correctly vs. incorrectly resolved, and no evaluation with actual human users. The claim of human-like interactive learning is therefore asserted rather than demonstrated.

- **Experiments conducted on tiny datasets with handcrafted features, limiting generalizability**: The Fruits and HomeF datasets contain a small number of classes (fruit/home objects) paired with a handful of words (names, colors, tastes). Features are handcrafted (Fourier descriptors for shape, color means, MFCCs for audio). This is far from the complexity of modern multimodal data, and no experiment demonstrates that the method scales beyond a few dozen classes or works with learned backbones (e.g., CLIP-style encoders). The paper's claims of "human-like lifelong learning" are not supported by evidence at a meaningful scale.

- **Conflict detection is not quantitatively evaluated**: The paper reports anecdotally that "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions." No precision, recall, or false-positive rate is reported, no controlled corruption study with varying noise levels is provided, and no analysis of the types of conflicts detected vs. missed is included. This makes the conflict detection claim unverifiable.

### Minor

- **Accuracy metric not explicitly defined**: The paper reports accuracy percentages in Tables 1–3 but never defines what "accuracy" means — is it top-1 classification, retrieval recall@1, or something else? The evaluation procedure (Section 4.1) states "we use one channel input to get outputs from other channels on the testing dataset" but does not specify how many candidates are considered, how ties are handled, or whether the task is ranking, classification, or generation.

- **No standard deviations, confidence intervals, or statistical tests are reported**: Given the small dataset scale, variance could be a serious concern. Single-number results without error bars make it impossible to assess whether performance differences (e.g., 89.8 vs. 86.5 in open V→A on Fruits) are statistically meaningful.

- **Online baselines are limited**: The only online competitors are ART and AEN (2019–2021), which are task-specific methods from the same research lineage. While the offline baselines span a reasonable range (DAE, DBM, DJSRH, NRCH, FUME from 2011–2025), the online comparison set is narrow. This makes it harder to assess OML's standing relative to the broader online learning landscape.

- **The gap between offline methods' close-environment performance and OML's is not discussed**: In the close environment, offline methods like DJSRH (91.8), NRCH (92.3), and FUME (92.1) outperform OML (89.2) on Fruits V→A. The paper correctly notes that offline methods degrade in the open environment, but does not acknowledge or explain why OML underperforms in the close setting where forgetting isn't a factor.

### Trivial

- Hyperparameter values (θ, ϑ, r) are stated but not explored or justified through sensitivity analysis.
- The number of free parameters in the network is not disclosed, making it hard to assess whether OML benefits from simply having more capacity than competitors.

## Nice-to-Haves

- A forgetting metric (e.g., backward transfer, forgetting rate) to quantitatively measure how well OML retains knowledge of earlier classes, rather than relying on aggregate accuracy comparisons.
- Integration with learned visual/text backbones (e.g., CLIP) to test whether the architecture is compatible with modern feature extractors.
- Instance-level case studies showing the conflict-check and question-answer process, including both correctly and incorrectly resolved conflicts.
- Visualization of learned references: for a given color word, showing which feature dimensions are assigned high vs. low coefficients of variation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The paper ignores more recent continual cross-modal retrieval or online learning works"** — The paper does cite methods up to 2025 (Shubham et al., 2025; Duan et al., 2025). While the online baselines are limited, I cannot verify what additional methods exist. Removed as unverifiable.

- **Harsh Critic: "This complexity is not motivated by formal analysis or empirical necessity; it's unclear why simple learned embeddings plus a retrieval mechanism wouldn't suffice"** — This is a strawman. The paper's goal is to build a brain-inspired architecture; comparing it to an entirely different approach (learned embeddings + retrieval) is scope creep. The relevant question is whether the proposed architecture works as claimed, not whether a simpler alternative might also work.

- **Harsh Critic: "No experiment shows that the method scales beyond a few dozen classes"** — Already captured under the major weakness about dataset scale. The phrasing about "does not exist" is removed per hard rules.

- **Strength Finder: "Robust conflict detection under noise"** — This contradicts the verified weakness that conflict detection is not quantitatively evaluated. The anecdotal 10%-noise claim does not constitute robust evidence. Removed as conflicting with a verified weakness.

- **Strength Finder: "Seamless modality extension with frequency-based routing" (the AEN comparison advantage)** — The paper acknowledges it counts AEN's modality-confused outputs as correct, which is a generous evaluation that inflates AEN's numbers. While the routing idea is valid, the strength description oversells the comparison. Kept the routing strength but removed the inflated comparison framing.

## Novel Insights

The paper's most genuinely novel observation is that the coefficient of variation of descending signals in a bidirectional network can serve as an unsupervised signal for reference extraction — determining which sensory feature dimensions a word actually refers to, without explicit annotation. The idea that variance stabilization across learning trials can disambiguate attribute-level references (e.g., color vs. shape) from object-level references is elegant and, to my knowledge, not previously explored in multimodal learning. If validated at scale, this could inform both biologically plausible learning models and practical multimodal systems.

## Suggestions

- **Add ablation experiments as the highest priority**: Disable the reference extraction algorithm, the conflict detection, the lateral connections, and the human-in-the-loop mechanism one at a time. This would directly test whether each component contributes to performance. Without this, the paper's claims rest on correlation, not causation.

- **Replace the simulated HITL with at minimum a controlled corruption study**: Vary the percentage of incorrect feedback (0%, 25%, 50%, 100%) and measure how OML's performance degrades. This would provide a meaningful quantitative evaluation of the interactive learning loop without requiring human subjects.

- **Define the accuracy metric explicitly and report variance**: State whether accuracy is top-1 retrieval recall, classification accuracy, or another metric, and provide standard deviations across multiple runs.

- **Discuss the close-environment performance gap**: Acknowledge that OML underperforms offline methods when forgetting is not a factor, and explain why (e.g., online single-pass learning vs. multi-epoch optimization).

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | Comparison to OML |
|--------|-----------|----------|-------------------|
| 6Kfbi3ngT1 (COMM) | 2.67 | Withdrawn/Reject | OML has more novel ideas (reference extraction, HITL) and clearer architecture description. OML is stronger. |
| GL4jwXuR65 (Hippo-1) | 2.67 | Reject | Both are brain-inspired architectures. Hippo-1 had unclear descriptions and only MLP baselines. OML's architecture is better described but shares the weak-experiment problem. OML is slightly stronger. |
| mDuton6Tg7 | 3.00 | Withdrawn/Reject | Both address continual multimodal learning. That paper had insufficient baselines and marginal improvements. OML has more novelty but comparably weak experiments. OML is comparable. |
| eCrvaO0WVF (DAGR) | 4.50 | Withdrawn/Reject | Similar topic (MMCL). Had ablation studies and MTIL benchmark but missing SOTA baselines. OML has no ablations and much smaller datasets. OML is weaker. |
| Gq7mjFEoDm (HINT) | 6.00 | Accept (Poster) | Cross-modal retrieval. Comprehensive experiments, strong baselines, clear novelty. OML is substantially weaker in experimental validation. |
| rMHZfCznhZ (RLAP-CLIP) | 6.00 | Accept (Poster) | Continual multimodal learning. 8 datasets, thorough ablations, strong baselines. OML is substantially weaker. |

OML presents genuinely novel and interesting ideas — the reference extraction algorithm and the architecture with bidirectional pathways for conflict detection are creative contributions. However, the experimental validation is substantially below the standard of accepted papers in this area: no ablation studies, a simulated rather than evaluated human-in-the-loop mechanism, tiny datasets with handcrafted features, and no quantitative conflict detection evaluation. These are not fatal flaws — the ideas are sound — but they prevent the paper from rising to acceptance level. The paper falls between the 3.00 and 4.50 anchors: more novel than the former but with weaker experiments than the latter.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>