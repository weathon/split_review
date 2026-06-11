## Summary

This paper proposes OML, a brain-inspired neural architecture for online multimodal learning with human-in-the-loop interaction. The network uses a hierarchical structure with feature neurons, unimodal association neurons (UANs), and multimodal association neurons (MANs) connected via ascending, descending, and lateral pathways. Key claimed capabilities include continuous learning without catastrophic forgetting, autonomous reference extraction to identify which features a word refers to, conflict detection with user questioning, and modal extension. Experiments on small fruit-image/Chinese-word datasets compare OML against offline methods (DAE, DBM, DJSRH, NRCH, FUME) and online methods (ART, AEN).

## Strengths

- **Catastrophic forgetting resistance in open environments**: Table 1 shows OML is the only method whose accuracy does not degrade moving from close to open environments. On Fruits V→A: 89.2% (close) → 89.8% (open), while every offline method drops substantially (e.g., DAE: 67.0→52.3). OML achieves the highest accuracy in all four open-environment settings in Table 1, providing concrete evidence that its dynamic neuron/pathway addition mechanism mitigates catastrophic forgetting.

- **Reference extraction via coefficient-of-variation thresholding**: Section 3.4 introduces a principled algorithm that autonomously identifies which feature dimensions a word refers to (e.g., "red" → color, "apple" → shape+color) by computing the coefficient of variation across samples. Table 2 shows this yields measurable benefits: on E-Fruits Open V→A, OML achieves 87.8% vs. 84.1% for the next-best online method (AEN), while offline methods degrade significantly (marked ↓) due to catastrophic forgetting from learning new color words.

- **Conflict detection mechanism with formalized interaction protocol**: Section 3.5 defines four learning scenarios with specific question templates the network poses when conflicts arise (e.g., when visual and auditory channels disagree about an input pair). The paper reports that with 10% deliberately mismatched pairs, OML detects all conflicts and raises appropriate questions. No prior online multimodal method (ART, AEN) supports this capability.

- **Modal extension with frequency-tagged signal routing**: Table 3 shows OML outperforms AEN on all 12 comparisons (6 tasks × 2 datasets) for extending a trained network with a new taste modality. The λ frequency parameter in the MAN activation (Eq. 6) enables correct routing of descending signals to the appropriate modality channel.

## Weaknesses

### Fatal
None.

### Major

- **No statistical rigor on any experimental result**: Every number in Tables 1–3 is a single point estimate with no error bars, standard deviations, or mention of repeated trials. Without this, the reader cannot assess whether the claimed improvements over baselines (often a few percentage points, e.g., 87.8% vs. 84.1%) are meaningful or within noise range for this evaluation setup. This is a fundamental gap for any empirical paper.

- **Human-in-the-loop component is not actually evaluated**: The paper states "if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive" (line 240). This means the interaction loop was bypassed via auto-answer during experiments. There is no user study, no analysis of question quality, no measurement of how often questions are asked, no evaluation of behavior under negative answers, and no ablation showing the interaction component contributes anything. The reported conflict detection claim ("when we randomly add 10%... OML is able to detect all conflicts") is qualitative with no measurement methodology, trial count, or quantitative results. Given "Human-in-the-Loop" is in the paper's title, this is a severe evidential gap.

- **No ablation studies despite many interacting components**: The method includes frequency-encoded FN activation (Eq. 1), OIAM vs. ODAM UANs, Fourier transforms in MAN activation (Eq. 6), lateral connections between FNs, the reference extraction algorithm (Section 3.4), conflict detection, and the question-asking protocol. Not a single component is ablated, making it impossible to attribute any observed performance to any specific design choice or to validate that the complex machinery is necessary.

- **Dataset details are absent**: The paper never states the number of classes, number of samples per class, or total dataset size for any of the datasets (Fruits, HomeF, E-Fruits, E-HomeF, VAT, VAT-HomeF). Without these basic statistics, the scope and difficulty of the evaluation cannot be assessed. The evaluation is confined to small, non-standard collections of fruit images paired with uttered Chinese words, with no comparison on any standard multimodal benchmark (CUB, Flickr30K, etc.).

### Minor

- **Reference extraction algorithm not validated in isolation**: The mechanism in Section 3.4 is a core claimed contribution, but it is only tested indirectly through Table 2's end-to-end accuracy. No controlled experiment measures whether the algorithm correctly identifies referring dimensions as a function of the number of training examples, or how the threshold r affects precision/recall.

- **Network growth/scaling not analyzed**: Since OML dynamically creates new neurons and connections during learning, the paper should report how the network scales (neurons added, connections created) as a function of learned concepts. This is important for assessing practical applicability.

- **Potential issue with T parameter in Eq. (1)**: The paper states T "does not affect the algorithm" (line 71), but the activation output is y = Σ_i Σ_{t=1}^T w_{j,i} cos(λ_i · 2π · (t-1)/T). For integer-valued λ_i (natural numbers per the paper's usage) and T=150, the inner sum Σ_t cos(λ_i · 2π · (t-1)/T) equals 0 for any λ_i not divisible by T. This would make most feature dimensions contribute zero activation. The claim that T is irrelevant warrants clarification—either λ_i are not integers as stated, or the formulation differs from how it reads.

- **Limited baseline for modal extension and dated offline baselines**: Table 3 compares OML against only AEN. For Tables 1–2, DAE (2011) and DBM (2014) are very early architectures that have been superseded. While some newer offline methods are included (NRCH 2024, FUME 2025), the baseline set could be stronger.

- **Hand-crafted features limit generality**: The method uses Fourier descriptors for shape, mean color values, MFCCs for audio, and taste features. This is a deliberate choice consistent with prior work, but it leaves unclear how the method would perform with learned deep features on larger-scale problems.

### Trivial

- The claim "All the designs make our method do learning like the way humans do" (abstract) is stated without evidence and should be softened.
- "OLM" appears in place of "OML" on line 240 (likely a parser artifact).

## Nice-to-Haves

- Evaluation on at least one standard multimodal benchmark (e.g., CUB with attribute annotations) would substantially strengthen generalization claims.
- A small user study testing whether the system's questions are perceived as appropriate and whether interaction improves learning outcomes.
- Analysis of how the reference extraction threshold r affects precision/recall of identifying referring feature dimensions.
- Comparison against simple online continual learning baselines (EWC, SI, GEM) adapted for multimodal data.

## Removed Points

*These points were flagged to be removed; treat them with caution.*

- **Baseline comparison unfairness in precise referring**: The harsh critic claimed baselines are disadvantaged because they return all features when queried with a color word. In fact, the paper states "we count this as a correct result for them" (line 248), meaning baselines are scored *more leniently*. The asymmetry favors the baselines, not OML. Removed per rule: critiques of unfair comparison where asymmetry favors the baseline should be removed.

- **Offline methods "not designed for online learning"**: The critic argued the comparison is unfair because offline methods are frozen after training. The paper includes them specifically to demonstrate catastrophic forgetting, which is a valid and informative comparison. OML is explicitly compared against online methods (ART, AEN) for direct competitiveness.

- **Missing dataset release/availability**: Removed per hard rules—the paper cites prior work for datasets; questioning release status is prohibited.

- **Specific missing related works**: Removed per hard rules about not mentioning missing related works as external sources cannot confirm their existence.

- **Notation/style nitpicks** about symbol reuse: Removed as formatting/style complaints.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a perspective that meaningfully reframes or deepens the paper's claims beyond what the authors already state.

## Suggestions

1. **Add error bars or confidence intervals** (from ≥5 independent runs) to all main results in Tables 1–3.
2. **Evaluate the human-in-the-loop component properly**: conduct a small user study, or at minimum quantitatively evaluate conflict detection accuracy (true positives, false positives) across multiple controlled trials with different mismatch rates and answer types.
3. **Provide ablation studies** isolating at minimum: (a) the reference extraction algorithm, (b) the Fourier-based signal routing vs. simpler alternatives, (c) lateral connections, and (d) the conflict detection mechanism.
4. **Report basic dataset statistics**: class count, sample count per class/dataset, number of unique words.
5. **Clarify the mathematical behavior of Eq. (1)**: explain how the T parameter interacts with λ_i values and demonstrate that the activation function produces meaningful outputs for the chosen parameter settings.
6. **Report network growth statistics**: number of neurons and connections added over the learning process as a function of the number of learned concepts.

---

## Calibration Report

**Round 1 bracket:** 3.0 – 4.5 (determined by comparing against weak anchors scoring 2.0–2.5 and strong-scoring anchors at 5.25+, none of which fit the paper's profile).

**Round 2 anchors consulted (selected for topical relevance):**

| Anchor path | Avg Score | Round | Comparison |
|---|---|---|---|
| `gNoqEdT2wO` — Multimodal CIL benchmark | 2.33 | 1 | Weaker than our paper; minimal novelty, tiny contribution. Our paper at least proposes a novel method. |
| `0CtIt485ew` — Brain-inspired continual learning (Artsy) | 4.00 | 1 | Stronger than our paper; uses CIFAR100/TinyImageNet standard benchmarks, has clearer evaluation. Our paper uses tiny non-standard fruit datasets and has untested human-in-the-loop. |
| `sKPzAXoylB` — UPGD (Addressing Loss of Plasticity) | 5.25 | 1 | Much stronger; comprehensive experiments, ablation studies, statistical rigor. Our paper does not compare. |
| `Pa6SiS66p0` — Multimodal lifelong learning benchmark | 4.33 | 2 | Stronger; uses VGGSound benchmark dataset, clear problem framing. Our paper has weaker evaluation on all fronts. |
| `IhOeYKqnfp` — Continual Memory Neurons | 4.25 | 2 | Stronger; tests on MNIST, CIFAR10, ImageNet standard benchmarks. Our paper's fruit-only evaluation is less compelling. |
| `G9Ea7mlqGO` — CLIP online continual learner | 3.80 | 2 | Stronger; uses standard datasets (CUB200, StanfordCars, Aircraft), has gradient analysis. Our paper's evaluation is less rigorous. |
| `TJHB4ySVZM` — Data Extrapolation (text-to-image) | 3.40 | 3 | Comparable overall quality; both are weak reject. |
| `TBw53TdDgb` — SADE (OCR) | 3.50 | 3 | Comparable overall quality; both are weak reject. |

**Final score determination:** The paper is clearly weaker than the 4.0+ anchors (Artsy, CMN, Multimodal CL) which at minimum use standard benchmarks and have clearer evaluation protocols. It is slightly weaker than the 3.80 CLIP paper which has gradient analysis and standard datasets. It is comparable to papers in the 3.4–3.5 range. Score 3.5 reflects a paper with a genuinely novel architecture and interesting mechanisms but an evaluation that falls substantially short of what is needed to validate the ambitious claims, particularly the untested "human-in-the-loop" title component.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>