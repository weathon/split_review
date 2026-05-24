Now I have a thorough understanding of the paper and anchors. Let me compile the final review.

---

## Summary

This paper proposes OML, a brain-inspired hierarchical neural network for online multimodal learning that can continuously learn new multimodal concepts without catastrophic forgetting, detect conflicts between current input and prior knowledge, query a human user, and extract precise feature-level referents of words (e.g., learning that "red" refers to color, not shape). The architecture uses custom neuron models with ascending/descending/lateral pathways, a reference extraction algorithm based on coefficient of variation, and a four-case conflict-check-and-ask learning procedure. Experiments on small fruit/object datasets with hand-crafted features show OML retains high cross-modal retrieval accuracy in open (sequential) environments while offline baselines degrade, and OML outperforms the online baseline AEN on modal extension tasks.

## Strengths

- **Online continual learning without catastrophic forgetting.** In open-environment evaluations (Tables 1–2), OML maintains stable accuracy (e.g., Fruits Open V→A 89.8, HomeF Open A→V 83.6) while offline methods suffer sharp drops (DBM falls from 70.5 to 54.3 on Fruits V→A). This directly validates the claim of online multimodal learning without forgetting.

- **Novel reference extraction mechanism for attribute grounding.** The algorithm in Section 3.4 uses coefficient of variation to identify which feature dimensions a word refers to. On the enhanced datasets E-Fruits and E-HomeF, where color-referring words are added, OML maintains near-baseline accuracy while offline methods drop by 5–15 points (Table 2), suggesting the architecture learns to distinguish name words from attribute words.

- **Effective cross-modal recall across all modality pairs.** The bidirectional ascending/descending pathway design consistently produces strong performance on both V→A and A→V tasks across all datasets (e.g., Fruits Close V→A 89.2, A→V 88.7; HomeF Open V→A 85.5, A→V 83.6), and on all six cross-modal directions in the taste-extension experiment (Table 3).

- **Seamless extension to a new modality.** Table 3 demonstrates that when a taste channel is added to a previously trained visual-auditory network, OML outperforms AEN on all retrieval directions (e.g., VAT Open T→V 92.1 vs. 89.2) by using frequency-tagged signals to route descending activations to the correct modality channel.

## Weaknesses

### Fatal

None.

### Major

- **The conflict detection and human-in-the-loop mechanism — the paper's most distinctive claimed contribution — is not quantitatively evaluated.** The paper states as a core attribute that OML "(2) It can detect conflict between the current input and the learned ones. If a conflict occurs, it can ask the user appropriate questions and conduct learning based on user's answer" (Section 1). Yet the experimental evidence consists of a single qualitative sentence in Section 4.1: "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions." No detection rate, false positive/negative analysis, comparison to a "no conflict-check" ablation, or demonstration that user feedback actually improves learning outcomes is provided. Furthermore, the interaction loop is effectively disabled throughout the experiments: "if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive" (Section 4). This means the paper's headline human-in-the-loop capability — including the engaging motivating example in Figure 1 — goes essentially unevaluated. This substantially weakens the paper's central contribution claim.

### Minor

- **No ablation studies.** OML bundles together the hierarchical architecture, cosine-frequency signaling, lateral connections, reference extraction, and conflict-questioning logic. Without ablations, it is impossible to determine which components are responsible for the observed gains. For example, the improvement on E-Fruits (Table 2) is attributed to reference extraction, but could arise from other architectural factors.

- **Accuracy metric is not precisely defined.** The paper reports "accuracy" in all tables without specifying whether it is top-1 retrieval accuracy, how ties are handled, or over what test split. Section 4 states "we use one channel input to get outputs from other channels on the testing dataset" but the exact retrieval evaluation protocol is underspecified.

- **Limited scale and feature representation.** Experiments use small datasets (Fruits, HomeF) with hand-engineered features (Fourier descriptors, mean color, MFCCs). The paper does not discuss how the approach would scale to natural feature representations or larger datasets, nor does it analyze sensitivity to feature extraction quality.

- **No error bars or significance tests.** Tables 1–3 report single-point accuracy values without any indication of variance across runs or statistical significance, making it difficult to assess whether the often-modest margins (e.g., OML 89.8 vs. AEN 86.2 on Fruits Open V→A) are reliable.

### Trivial

- The method description, while mathematically specified, is dense and would benefit from a more streamlined presentation clarifying the functional role of design choices (cosine-weighted sums, Fourier transforms) beyond the appeal to brain inspiration.

## Nice-to-Haves

- A controlled test for reference extraction where the model is taught words referring to known feature subsets (e.g., only color, only shape) with ground-truth annotation of which dimensions should be identified, and reporting precision/recall of the extraction.
- A simulated noisy-teaching experiment with quantitative conflict-detection metrics (precision, recall) and a demonstration that learning with user feedback produces better final representations than learning without it.
- Comparison with offline methods trained on all data at once in the close environment to contextualize OML's slight underperformance against offline baselines there (Table 1, Close: NRCH and FUME outperform OML).
- Explicit discussion of limitations: dataset scale, engineered features, the "default yes" assumption for unanswered questions.

## Removed Points

These points from the input reviews were considered but not retained in the final review:

- **"Offline methods comparison is misleading/unfair."** The open-environment setup is a standard continual learning evaluation — showing that offline methods suffer catastrophic forgetting under sequential training is the intended demonstration, not a fairness issue. The paper does not claim offline methods are designed for this setting.

- **"Lateral connections are barely used / never tested."** Lateral connections are explicitly used in the conflict-detection logic of Section 3.5 (cases 1 and 2), where the intersection with laterally-connected neuron sets determines whether a conflict is raised. The claim that they are "barely used" is factually incorrect.

- **"ODAM channel asymmetry not made concrete."** Section 3.4 describes how μ and σ are accumulated and how the reference extraction function re(μ,σ) operates (Eq. 7). While the distinction between online inference and batch statistics could be clearer, the mechanism is specified.

- **"Method description hinders reproducibility."** The equations (1–8) are mathematically specified with concrete parameters. An independent researcher could implement from these specifications. This is a presentation/clarity issue, not a reproducibility blocker.

- **"Ascending/descending/lateral pathway functional role not justified."** The paper describes what each pathway does: ascending pathways carry feature signals upward, descending pathways carry activation from MANs back to FNs to enable cross-modal recall, and lateral pathways connect similar FNs to improve generalization. These functional roles are clearly stated.

- **Any concern about the existence or availability of cited models, benchmarks, or datasets.** All cited references are assumed to exist and be available.

## Novel Insights

Beyond the paper's own contributions, the review process highlights an important gap in how interactive learning systems are evaluated. The paper designs a genuinely interesting conflict-detection-and-questioning protocol (the four cases in Section 3.5, with context-aware questions like "I think you call it X before, now you also call it Y?") but falls into a common trap: the experiments evaluate only retrieval accuracy rather than the interaction mechanism itself. This suggests a broader need in the field for standardized evaluation protocols for human-in-the-loop learning systems — metrics like conflict detection precision/recall, question appropriateness, and learning improvement from feedback — that go beyond end-task accuracy.

## Suggestions

- Add a focused experiment that quantitatively evaluates conflict detection: inject a known percentage of mismatched pairs, report detection precision and recall, and show that learning *with* simulated user feedback produces better representations than learning *without* it.
- Conduct ablation experiments that remove individual components (reference extraction, lateral connections, conflict checking) to isolate their contributions.
- Define the retrieval accuracy metric precisely (top-1, top-k, or MAP) and report results with error bars across multiple random seeds.
- Clarify in the experiments section how offline baselines were trained in the open environment (e.g., were they fine-tuned sequentially or retrained from scratch on each new partition?).

---

**Calibration summary:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| SI6zocV2SS | 1.50 | 1 | Weaker than OML — simple neuron-freezing with Hebbian learning, much less novelty |
| WM5G2NWSYC | 2.00 | 1 | Weaker — projected subnetworks for meta-learning, limited evaluation |
| gNoqEdT2wO | 2.33 | 1 | Weaker — a benchmark proposal without novel method |
| HCCkCjClO0 | 3.00 | 1 | Weaker — online weight approximation, limited novelty |
| Pa6SiS66p0 | 4.33 | 1 | Stronger evaluation design (benchmark + analysis) but simpler method; OML has more novelty but weaker evaluation |
| 0CtIt485ew | 4.00 | 1,2 | Comparable — brain-inspired continual learning, better evaluation (standard benchmarks, ablation) but limited biological connection; OML has more novel problem framing but weaker evaluation of its key claims |
| jYyste2HLP | 4.33 | 1,2 | Slightly stronger — bio-inspired model with more comprehensive experiments (public + proprietary dataset, real robot); OML has similar novelty but weaker evaluation |
| JAnyCnK5In | 4.75 | 1 | Stronger — SNN online training with more rigorous experiments |
| IhOeYKqnfp | 4.25 | 2 | Comparable in spirit (novel neuron model for continual learning) but better ablation and standard benchmarks; OML has broader scope but weaker validation |
| 3YQYo1O01W | 3.67 | 2 | Most comparable — interesting problem (vision-knowledge conflicts) with weak evaluation of core claims; OML is similar in the gap between claimed contribution and empirical support |

**Round-1 bracket:** 3.0–5.0. Round 2 narrowed this to 3.5–4.0. OML's core weakness — the unevaluated conflict-detection/human-in-the-loop claim — places it below the better-evaluated anchors at ~4.0+ (Artsy, FlyOrien, CMN) and closer to ConflictVis (3.67), which shares the pattern of an interesting problem formulation with insufficient empirical validation of its central claims. I assign **3.5**.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>