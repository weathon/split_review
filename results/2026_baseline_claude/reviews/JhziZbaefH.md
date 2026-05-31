## Summary

The paper proposes OML, a brain-inspired hierarchical and modular neural network for **online multimodal learning (OML)** that continuously acquires new multimodal concepts and associations without catastrophic forgetting. The architecture features ascending, descending, and lateral pathways across feature neurons (FN), unimodal association neurons (UAN), and multimodal association neurons (MAN), along with a reference extraction algorithm that identifies which feature dimensions a word genuinely refers to (e.g., color words refer to color features only), and a human-in-the-loop conflict resolution mechanism that generates clarifying questions when newly taught associations contradict prior knowledge.

---

## Strengths

- **Novel problem formulation.** The paper explicitly combines three capabilities—continual multimodal learning, precise feature-level reference attribution, and interactive conflict resolution—into a unified system. The reference extraction algorithm that computes the coefficient of variation per feature dimension to determine what a word "means" (Section 3.4) is a genuinely novel and well-motivated mechanism that other baselines lack.

- **Frequency-based cross-channel routing.** Using the Fourier transform at the MAN level to encode signals with amplitude and frequency pairs, and then routing descending signals via frequency matching (the λ parameter), is a creative and practical mechanism for ensuring a word like "tián" (sweet) retrieves from the taste channel and "hóng sè" (red) retrieves from the visual channel. Table 3 validates that this distinction cannot be made by AEN.

- **Systematic experimental design.** The paper compares against five offline and two online baselines across four dataset variants (Fruits, HomeF, E-Fruits, E-HomeF, VAT, VAT-HomeF) in both closed and open environments. The open environment (sequential disjoint class splits) directly operationalizes catastrophic forgetting, and OML's results are stable while offline baselines drop markedly (Table 2, E-Fruits V→A: DJSRH 78.4 vs. OML 87.3).

- **Principled incremental architecture.** Growing the network by adding new neurons and pathways only when encountering genuinely novel concepts avoids modifying previously learned representations, providing a structural (rather than regularization-based) guarantee against forgetting—a strength over replay or distillation approaches for this task.

---

## Weaknesses

### Fatal
None. The core claims are internally consistent and supported by the experimental results provided.

### Major

1. **Evaluation metric is never defined.** Tables 1–3 report a quantity labeled "accuracy," but cross-modal retrieval tasks (V→A, A→V, T→V, etc.) are conventionally evaluated with mean average precision (mAP) or recall@k, not accuracy. The paper neither defines what "accuracy" means (e.g., top-1 recall? fraction of correctly recalled class labels?) nor provides the formula. Without this, the numerical results cannot be properly interpreted or reproduced.

2. **The human-in-the-loop component is not actually evaluated.** Section 3.5 describes the conflict-detection and question-generation mechanism as a core contribution, and the introduction frames human interaction as central. Yet the experiment section states: *"if the question posed to the user by OML remains unanswered for a certain period of time, we set the answer to be positive."* This means every conflict is resolved by an automatic positive response. There is no measurement of conflict detection precision/recall, no evaluation of what happens with incorrect user answers, and no assessment of how frequently questions are triggered. The human-in-the-loop component, as presented, is not empirically validated at all.

3. **Dataset scale is too small to support general claims.** The Fruits dataset contains uttered Chinese names of common fruits, a very restricted category and class count. The number of samples, classes, and training/test split sizes are not reported anywhere in the paper. ICLR-level claims about "online multimodal learning throughout a lifetime" are difficult to sustain on tiny fruit datasets with hand-crafted backbone features.

### Minor

1. **No ablation studies.** The paper has several design choices (lateral connections, reference extraction threshold r=0.5, frequency-based routing, the specific conflict-checking logic in Cases 1–4). None of these are individually ablated, making it impossible to judge their relative contribution.

2. **Hand-crafted, non-deep features.** The visual backbone uses SAM + Fourier boundary descriptors (shape) + mean color inside boundary; the auditory backbone uses MFCC with short-time energy/zero-crossing for syllable segmentation. These are classical signal-processing features. While valid for the chosen datasets, this limits the generalizability of the approach to richer domains and distances it from modern representation learning.

3. **Computational complexity not analyzed.** As the network grows (new neurons, connections), the paper does not discuss how retrieval time, memory, or learning time scale with the number of concepts. This is particularly relevant for the open environment with sequential class splits.

### Trivial

- "OLM" appears in one sentence (Section 4) where "OML" is clearly intended—a minor inconsistency.

---

## Nice-to-Haves

- A measurement of conflict-detection accuracy (precision/recall for true conflicts vs. false alarms) on a labeled subset where ground-truth conflicts are known.
- An experiment with at least one standard large-scale multimodal benchmark (even in a reduced online-learning setup) to show the approach's applicability beyond small fruit/home-object datasets.
- Sensitivity analysis of the reference-extraction threshold r and the density threshold ϑ.
- A table showing how network size (number of neurons) grows over sequential learning, confirming the network remains tractable.

---

## Novel Insights

The reference extraction mechanism (Section 3.4) offers a genuinely novel insight: rather than treating a word's multimodal association as uniform across all feature dimensions, one can exploit the **stability of feature statistics across training examples** to identify which dimensions a word actually refers to. Using the coefficient of variation (σ/μ) as a proxy for semantic relevance—small variation implies the feature is semantically anchored to that word—is an elegant and biologically plausible idea that could inspire more principled grounding mechanisms in larger language-vision systems. The Fourier-frequency routing scheme for directing descending signals to the correct modality is also independently interesting as a lightweight mechanism for disambiguating cross-modal associations without learned attention.

---

## Suggestions

- Define the evaluation metric precisely (formula, what counts as a correct answer) and report standard retrieval metrics (mAP or recall@k) alongside accuracy.
- Design a controlled human-in-the-loop evaluation: inject a known percentage of deliberate label errors and measure (a) what fraction OML correctly flags, (b) what fraction are false positives, and (c) the effect of wrong user answers on downstream accuracy.
- Report dataset statistics (number of classes, samples per class, train/test split) and consider extending experiments to larger-scale visual-language benchmarks even with a simplified setup.
- Provide at least an ablation removing reference extraction (r=∞) and lateral connections to quantify each component's contribution.

---

## Score and Decision

The paper addresses an underexplored and genuinely important problem, and the proposed architecture is creative and coherent. However, two major weaknesses significantly reduce confidence in the results: the evaluation metric is undefined, making the reported numbers uninterpretable, and the central human-in-the-loop claim is not experimentally evaluated at all (collapsed to automatic positive responses). Combined with the small dataset scale and absence of ablations, the paper falls short of the rigor expected at ICLR.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>