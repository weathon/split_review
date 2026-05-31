## Summary

This paper proposes OML, a biologically inspired hierarchical neural network for online multimodal learning with three claimed capabilities: (1) continuous learning without catastrophic forgetting, (2) precise reference extraction (identifying which feature dimensions a word refers to), and (3) conflict detection with human-in-the-loop interaction. The architecture uses feature neurons, unimodal association neurons, and multimodal association neurons with ascending, descending, and lateral pathways. Experiments on small multimodal datasets (Fruits, HomeF and augmented variants) show OML maintains stable accuracy in open environments while offline methods forget.

## Strengths

- **Demonstrated resistance to catastrophic forgetting**: Table 1 shows OML maintains nearly stable accuracy across close and open environments (e.g., 89.8% V→A on Fruits open vs. 89.2% close), while all offline methods (DAE, DBM, DJSRH, NRCH, FUME) drop significantly in open environments — e.g., DJSRH drops from 92.1% to 83.1% on Fruits V→A. This directly validates the continual learning claim.

- **Novel reference extraction mechanism**: Section 3.4 introduces a coefficient-of-variation-based algorithm that autonomously identifies which feature dimensions (e.g., color vs. shape) a word refers to during online learning. Table 2 shows OML achieves 87.3% on E-Fruits close V→A vs. 82.9% for the best online baseline AEN, and the paper transparently notes that it counts full-feature retrieval as correct for baselines (a systematic leniency toward baselines), making OML's advantage credible.

- **Modal extension capability demonstrated**: Table 3 shows OML outperforms AEN on three-modality (VAT) tasks across all six retrieval directions (e.g., 92.1% vs. 89.2% on VAT open T→V). The frequency-based signal routing mechanism explained in Section 3.3 enables OML to direct queries to the correct modality channel, which AEN cannot do.

## Weaknesses

### Fatal

None.

### Major

- **The human-in-the-loop component is not evaluated**: Despite the paper's title and prominently claimed second attribute ("It can detect conflict…ask the user appropriate questions and conduct learning based on user's answer"), the human interaction is never tested. The experiments default unanswered questions to "yes" (line 240: *"if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive"*). The claim that *"OML is able to detect all conflicts"* (Section 4.1(3)) is stated without any supporting numbers — no detection rate, false-alarm rate, or analysis of how different user responses affect learning outcomes. The human-in-the-loop framing is effectively an untested feature.

- **No ablation studies**: The architecture is elaborate — frequency coding with cosine activation (Eq. 1), Gaussian signal variables for descending pathways (Eqs. 2, 4), lateral connections based on weight similarity, Fourier transform at the MAN level (Eq. 6), the coefficient-of-variation reference extraction (Eq. 7), and four-case learning rules with threshold parameters θ, ϑ, r. None of these components are ablated. It is impossible to determine which mechanisms are necessary for the reported performance. This is a significant gap given the architecture's complexity.

- **Dataset statistics are absent**: The paper specifies datasets only by name and references (Xing et al., 2019; Lai et al., 2011). No information is provided about number of classes, samples per class, image resolution, or train/test splits. Without this, it is impossible to gauge task difficulty or assess whether the reported accuracies (82–92%) reflect meaningful learning or ceiling effects on small data.

### Minor

- **Retrieval/decoding procedure is underspecified**: The paper reports retrieval accuracy (V→A, A→V) as the primary evaluation metric but never defines how output is selected from the network — e.g., when an image is used to recall a word, how is the winning auditory UAN chosen? What is the selection criterion (highest activation, winner-take-all, threshold-based)? This gap undermines reproducibility.

- **No statistical variance or significance reporting**: Results are reported as single-point accuracies without error bars, standard deviations, or significance tests across multiple runs. For an online learning system where the order of neuron creation can affect outcomes, variance across runs should be reported.

- **Gaussian signal variable parameter initialization for FNs and UANs not specified**: The descending activation functions (Eqs. 2, 4) use Gaussian distributions with parameters (μ, σ), but the paper only shows how μ and σ are updated for word neurons (Eq. 8). How these parameters are initialized and updated for feature neurons and non-word UANs is not explained.

### Trivial

None.

## Nice-to-Haves

- Evaluate the reference extraction directly by measuring precision/recall per modality (e.g., whether color-word queries retrieve only color features).
- Report learning curves or neuron growth statistics over the course of online learning.
- Conduct a sensitivity analysis on the key thresholds (θ, ϑ, r) and the sample count needed for reference extraction.

## Removed Points

- **"Method is not sufficiently specified to be reproducible" (regarding growth rules)**: The paper does specify conditions for neuron creation via the four-case algorithm in Section 3.5, with the recognition criterion (d(x, wⱼ) ≤ θ) given in Eq. (1). The critic's framing that "no threshold is given" misreads the paper.
- **"Comparisons to offline methods are not meaningful"**: Offline methods serve as a catastrophic forgetting baseline, which is standard practice. The paper also includes online baselines (ART, AEN) and outperforms them.
- **"Leniency favoring baselines in Table 2"**: The paper transparently discloses this leniency. This strengthens the paper's case — OML outperforms baselines despite the advantage given to baselines.
- **"Fourier transform lacks purpose"**: The paper explains at line 119 that the Fourier transform extracts amplitude and frequency for signal routing to correct descending pathways.
- **Formatting nitpicks, missing appendix content, speculative claims about what the method might not handle**: Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviewers' critiques converge around the gap between the ambitious framing (human-in-the-loop interaction as a core contribution) and the evaluation (which simply defaults unanswered questions to "yes"), but this is a gap the paper itself creates rather than a novel observation.

## Suggestions

1. **Evaluate the human-in-the-loop**: Report conflict detection rates and false-alarm rates on mismatched data (the paper claims "detects all conflicts" but provides no numbers). Run experiments with simulated user responses (both correct and incorrect) to measure downstream impact on learning.
2. **Add ablation studies**: Remove the Fourier transform, the frequency coding, the lateral connections, and the descending signal variables one at a time to show which components actually contribute to performance.
3. **Report dataset statistics**: Provide number of classes, samples per class, train/test splits, and image resolution for all datasets used.
4. **Add multiple-run statistics**: Report means and standard deviations across at least 3–5 runs with different random seeds or data orders.
5. **Clarify retrieval decoding**: State explicitly how the winning neuron is selected for retrieval tasks (V→A, A→V, etc.).
6. **Explain parameter initialization**: Describe how μ and σ are initialized for descending signal variables of FNs and UANs, and whether Eq. (8) applies to all neuron types.

---

## Calibration Report

**Round 1 (Bracketing)** — Query: "online multimodal learning continual learning catastrophic forgetting" on three bands:

| Band | Avg Scores | Representative Anchors |
|------|-----------|----------------------|
| Low (< 3.5) | 2.00–3.00 | "Projected Subnetworks Scale Adaptation" (2.00), "LVLM-CL" (2.50), "Online Weight Approximation" (3.00) |
| Middle (3.5–7.5) | 3.80–4.50 | "Beyond Unimodal Learning" (4.33), "Relaxing Representation Alignment" (4.50), "CLIP model is an Efficient Online Continual Learner" (3.80) |
| High (> 7.5) | 8.00 | "Test-time Adaptation against Multi-modal Reliability Bias" (8.00) |

**Initial bracket**: The paper is clearly above the low band (2–3) papers, which have fundamental structural flaws. It is below the high band (8.0) papers, which have rigorous evaluation and clearer contributions. **Initial bracket: 3.5–5.5**.

**Round 2 (Narrowing)** — Querying for anchors inside the bracket:

| Anchor | Score | How this paper compares |
|--------|-------|------------------------|
| "Beyond Unimodal Learning" (Pa6SiS66p0) | 4.33 | Similar — both tackle multimodal continual learning with weak evaluation. OML has a more original architecture but weaker baselines |
| "Relaxing Representation Alignment" (CagdoUkvvl) | 4.50 | Similar — both have evaluation gaps. OML has stronger novelty, weaker evaluation |
| "CLIP model is an Efficient Online Continual Learner" (G9Ea7mlqGO) | 3.80 | OML is stronger — more original architecture, clearer problem framing |
| "Is multitask learning all you need" (Pin2kdWloe) | 5.75 | Stronger than OML — has theoretical analysis and more comprehensive experiments |
| "Comprehensive Online Training...Spiking Neural Networks" (JAnyCnK5In) | 4.75 | Slightly stronger than OML — more thorough evaluation despite different subfield |

**Final score determination**: The paper sits at the lower end of the middle band. Its genuinely novel architecture and clean demonstration of catastrophic forgetting resistance are notable strengths. However, the combination of three major weaknesses (unevaluated human-in-the-loop, no ablations, no dataset statistics) places it below the more thoroughly evaluated papers in this band. The nearest comparable papers are "Relaxing Representation Alignment" (4.50) and "Beyond Unimodal Learning" (4.33). OML's core contribution is more novel than either, but its evaluation is weaker. I score it at **4.5**, acknowledging the originality but penalizing the evaluation gaps.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>