Now I have enough calibration data. Let me write the final consolidated review.

**Round 1 Bracket:** Based on the calibration search, I initially placed the paper between 3.0 and 5.0. The closest topical anchor is "Input Dimension Expandable Network" (avg 2.50) which shares the same hierarchical modular architecture for online learning, small-scale datasets, and similar issues (no ablation, unclear learning rule). This paper is somewhat stronger than IDEN (more comprehensive experiments, clearer process, reference extraction contribution) but weaker than "Dynamic Alignment for Multimodal Continual Learning" (avg 4.50) which had proper ablation studies and rigorous evaluation.

**Round 2 Narrowing:** After reading additional anchors, I compared against "Architect Thyself" (avg 3.50, scores 4,6,2,2) — this paper has less grandiosity but more grounded contributions. The paper is better than IDEN (2.50) and "Mind the Interference" (2.67) but worse than papers with proper ablation studies and statistical rigor. The paper sits at approximately 3.5 on the scale.

---

## Summary

This paper proposes OML, a brain-inspired hierarchical neural network for online multimodal learning with three key capabilities: continuous learning without catastrophic forgetting, reference extraction (identifying which visual features a word refers to), and conflict detection with human-in-the-loop interaction. The network uses a modular architecture with ascending/descending/lateral pathways across feature, unimodal association, and multimodal association layers. Evaluated on small-scale fruit/object image-audio datasets, OML outperforms online baselines (ART, AEN) and maintains stable accuracy in open-environment settings where offline methods suffer catastrophic forgetting.

## Strengths

- **Reference extraction algorithm for precise feature attribution (Section 3.4, Eq. 7):** The paper designs a mechanism using the coefficient of variation of visual signals over time to determine which feature dimensions (e.g., color vs. shape) a word refers to. This is a genuine and novel contribution over prior online methods (ART, AEN) that treat all words uniformly. The evidence is in Table 2, where OML achieves the highest accuracy on E-Fruits and E-HomeF datasets (e.g., 87.3% on E-Fruits close V→A) while offline methods drop significantly (marked by ↓) because they cannot distinguish name words from attribute words.

- **Online learning without catastrophic forgetting is demonstrated:** The open environment experiments (Tables 1, 2, 3) show that OML maintains stable accuracy when new classes are introduced sequentially, while offline methods (DAE, DBM, DJSRH, NRCH, FUME) suffer large drops. For Fruits open environment, OML achieves 89.8% (V→A) and 89.0% (A→V), whereas the best offline method drops to 86.5% and 84.4%, respectively. The comparison with online methods (ART, AEN) is also favorable, showing 3–5 point improvements.

- **Modal extension capability is validated:** The paper extends the trained visual-auditory network to include a taste modality (Table 3, VAT dataset) and outperforms the only prior method handling this setting (AEN) on all six cross-modal retrieval tasks. The frequency-based routing via λ parameters provides a principled mechanism for directing signals to the correct modality, which AEN cannot do.

- **Clear architectural specification with explicit pathways:** The hierarchical network with ascending, descending, and lateral pathways is concretely defined (Sections 3.1–3.3, Eqs. 1–6), and the four learning scenarios in Section 3.5 provide a walkable description of how the network handles different input recognition states.

## Weaknesses

### Major

1. **The human-in-the-loop capability is not validated.** The paper's title and abstract prominently feature human-in-the-loop interaction, yet the experiments provide no evidence that this interaction works. The paper states (line 244): *"if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive."* This means the interaction is bypassed entirely. The claim that "OML is able to detect all conflicts and raise appropriate questions" (Section 4.1, third bullet) is stated without any quantitative results — no detection rate, false positive rate, or accuracy of the questions asked. Neither negative user responses nor a user study are simulated. The central claimed capability is unsupported by evidence.

2. **No ablation studies.** The method has many complex components: frequency-coded activation (Eq. 1), Fourier transforms on MAN outputs (Eq. 6), Gaussian probability density thresholds (Eqs. 2, 4), lateral connections (Section 3.1), and reference extraction via coefficient of variation (Section 3.4). None of these are ablated. It is impossible to determine whether the results come from the core architecture or from a particular design choice. The Fourier transform in particular is unmotivated — the paper does not explain why frequency-domain representation helps, nor does it compare with simpler alternatives (e.g., concatenation or addition).

3. **No error bars or statistical significance.** All tables report single accuracy values. Given the small datasets (the open environment divides data into four equal parts, implying very few samples per part), the results could easily be non-significant. This is a basic methodological requirement that is absent.

4. **The learning mechanism for existing feature neurons is underspecified.** The paper describes how new FNs are created (weights set to input features) in Section 3.5, but never explains what happens when a later input falls within the threshold θ of an existing FN. Does the FN's weight vector get updated? Is there any prototype refinement, Hebbian update, or adaptation mechanism? The paper is silent on this. Only the μ and σ of the word UAN are updated (Eq. 8). As described, existing FNs are static templates — the method is effectively a growing nearest-neighbor classifier with a fixed threshold, wrapped in a complex notation. This is a reproducibility issue: the paper should clarify whether FNs are ever updated beyond initialization.

### Minor

1. **Baseline input features are not specified.** The paper describes the features used by OML (Fourier descriptors for shape, mean color, MFCCs for audio, Section 4, paragraph 2) but does not clarify what input features the baselines (DAE, DBM, DJSRH, NRCH, FUME) received. If baselines were given different features, the comparison is unfair. This should be clarified.

2. **Conflict detection quantitative results are missing.** The paper mentions that with 10% mismatched pairs, "OML is able to detect all conflicts and raise appropriate questions" (Section 4.1, third bullet), but provides no quantitative evidence — no detection rate, no false positive rate, no comparison with any baseline. This is insufficient to support the claim.

3. **Dataset statistics are underspecified.** The paper does not report the number of classes, samples per class, number of color words, or detailed construction of the open environment partitions. The experimental setup lacks sufficient detail for reproducibility.

### Trivial

- The notation is occasionally heavy and internally inconsistent (e.g., using `r` to denote both the coefficient-of-variation vector and the threshold against which it is compared in Eq. 7).
- Multiple figure captions repeat the same text multiple times (parser artifacts, but the original likely has this issue).

## Nice-to-Haves

- Adding a simple prototype update rule for existing FNs (e.g., moving the weight vector toward the current input when the distance is below θ) would make the learning mechanism more complete and better justify the "learning" framing.
- Simulating both positive and negative user responses in the conflict detection experiment would strengthen the human-in-the-loop claim considerably.
- An ablation study removing the Fourier transform and replacing it with a simple sum or concatenation would clarify whether the frequency-domain machinery is actually necessary.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Critic's claim that "open environment comparison evaluating offline methods...is not a meaningful comparison" (Critic Claim 3, sub-point 2):** The paper compares offline methods on sequential data to demonstrate catastrophic forgetting — this is a standard experimental design in continual learning. The paper also compares with online methods (ART, AEN). This criticism is incorrect and removed.

- **Critic's claim that "the appropriate baseline for open environment would be continual learning methods adapted to multimodal data" (Critic Claim 3, sub-point 3):** The paper already compares with ART and AEN, which are online/continual learning methods. This criticism is incorrect and removed.

- **Strength Finder's claim about "Conflict detection and human-in-the-loop interaction" being validated:** The strength finder states this is "validated by the experiment in Section 4.1 (third bullet)" but the experiment only asserts the capability without providing quantitative evidence. This claimed strength is not supported by the paper's evidence and is removed from the strengths list.

- **Strength Finder's claim about "Detailed biologically-inspired architecture with explicit pathways":** This is a description of the design, not a validated strength. Generic design description without evidence that the biological inspiration leads to measurable improvements is not a strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the disconnect between the paper's ambitious claims (human-in-the-loop interaction, brain-inspired learning) and the actual evidence provided (a growing nearest-neighbor network tested on small datasets with no interaction validation). The reference extraction mechanism is the most interesting technical contribution, but it is not ablated or analyzed in isolation.

## Suggestions

1. **Conduct ablation studies** isolating the reference extraction, Fourier transform, frequency encoding, and lateral connections to determine which components drive performance.
2. **Validate the human-in-the-loop interaction** by simulating both positive and negative user responses, measuring conflict detection rate, false positive rate, and the accuracy of the resulting updates.
3. **Report error bars or confidence intervals** over multiple runs or random splits.
4. **Clarify what input features baselines received** and whether the comparison is fair.
5. **Specify whether existing FNs are updated** when similar inputs arrive, or clarify that the method uses fixed prototypes.
6. **Provide dataset statistics** (number of classes, samples per class, construction of open environment partitions).
7. **Add a discussion of limitations**, particularly the reliance on hand-crafted features, the scalability of the threshold-based approach, and the scope of the human-in-the-loop claim.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>