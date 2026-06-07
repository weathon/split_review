Now I have sufficient calibration data. Let me compose the final review.

**Calibration Summary:**

Round 1 bracketing: The paper clearly outperforms the <3.5 band (papers scoring 2.0-3.0, rejected for fundamental flaws) but is well below the >7.5 band (papers scoring 8.0, unanimously accepted). The plausible range is 3.5-7.0.

Round 2 narrowing:
- PROOF (5.67, reject): First VLM for CIL, rigorous evaluation on 9 datasets with ablations, rejected due to inference mismatch. OML is more novel architecturally but much less rigorously evaluated.
- DMI (5.50, reject): Theoretical + empirical contribution, rejected due to unclear architecture and confusing claims. OML has clearer architecture but weaker experiments.
- MDAA (5.00, reject): Multi-modal continual TTA with proper experiments, rejected for limited novelty. OML has more novelty but weaker evaluation.
- OPWA (4.75, reject): Online prototype aggregation, proper but limited experiments. OML has more novelty but significantly less rigorous evaluation.

Final score: **4.5**. The paper's architecture is genuinely novel and the online learning results are consistent across settings. However, the evaluation has serious gaps (no variance, no ablations, no dataset statistics) and the headline human-in-the-loop contribution is essentially untested. This places it between OPWA (4.75, rejected for evaluation gaps) and the stronger 5+ papers that have both novelty and rigorous evaluation.

---

## Summary

This paper proposes OML, a hierarchical modular neural architecture for online multimodal learning that incorporates (a) ascending/descending/lateral signal pathways for continual learning, (b) a coefficient-of-variation-based reference extraction algorithm that identifies which features a word refers to, and (c) a conflict-detection mechanism for human-in-the-loop interaction. The architecture is tested on four small-scale datasets under both close (i.i.d.) and open (sequential class splits) environments.

## Strengths

- **Novel architecture for an underexplored problem.** The combination of frequency-tagged feature neurons, Fourier-based signal routing at the multimodal association layer, and separate order-dependent/order-independent activation modes for auditory vs. visual channels is genuinely novel. Prior online multimodal methods (Xing et al., ART, AEN) do not have this hierarchical pathway structure. The explicit separation of OIAM and ODAM modalities (Section 3.2) is well-motivated by the different nature of visual and auditory concepts.

- **Consistent empirical advantage across all open-environment conditions.** In every open-environment condition in Tables 1-3 (16 task-environment combinations total), OML achieves the highest accuracy among all methods. For example, Fruits Open V→A: OML 89.8% vs. next-best AEN 86.2%; E-Fruits Open V→A: OML 87.8% vs. next-best AEN 84.1%; VAT Open T→A: OML 93.9% vs. AEN 89.0%. Offline methods drop significantly (marked with ↓) due to catastrophic forgetting, confirming that OML's growing architecture effectively mitigates this problem.

- **Reference extraction algorithm with concrete empirical validation.** The coefficient-of-variation method (Section 3.4) for identifying which features a word refers to is clearly described and directly tested in the E-Fruits/E-HomeF experiments (Table 2). The paper transparently notes that baselines ART and AEN cannot distinguish name words from color words and are scored generously (returning all features counts as correct), yet OML still outperforms under this favorable-to-baseline regime.

## Weaknesses

### Major

1. **The headline human-in-the-loop contribution is essentially unevaluated.** The paper states (line 240) that unanswered questions are auto-answered positively — meaning the quantitative experiments bypass the interaction loop entirely. No experiments with actual human users or even a simulated user providing negative/noisy answers are conducted. The only quantitative claim about conflict detection (line 250) is a single unsupported sentence: "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions." No precision, recall, confusion matrix, or operating-point analysis is provided. Since conflict-driven interaction is listed as one of the two core attributes (line 37-38: "it can ask the user appropriate questions and conduct learning based on user's answer"), this gap undermines a central claimed contribution.

2. **No variance or statistical significance reported for any result.** Every accuracy in Tables 1-3 is a single point. There is no mention of the number of trials, random seeds, standard deviations, or confidence intervals. Given the small scale of the datasets and modest margins in some comparisons (e.g., Fruits Open V→A: 89.8 vs. 86.2), it is impossible to assess whether the reported differences are reliable or within run-to-run noise. This is a basic evidential gap that weakens every quantitative claim.

### Minor

3. **No ablation studies.** The architecture has many interacting components (FNs, UANs, MANs, lateral connections, Fourier transforms, frequency parameters λ, thresholds θ, ϑ, r, and the reference extraction algorithm). No experiment isolates which components drive performance. A minimal ablation would compare OML against a version without lateral connections or without reference extraction. Without this, attributing the performance to specific design choices is speculative.

4. **No dataset statistics reported.** The paper does not report the number of classes, samples per class, vocabulary size, or feature dimensionality for any dataset (Fruits, HomeF, E-Fruits, E-HomeF, VAT, VAT-HomeF). The figures only depict fruits and color words, suggesting very small scale, but the reader cannot verify this or assess scalability.

5. **No computational cost or scaling analysis.** The network grows by adding neurons and connections for each new concept. No runtime, memory, or scaling analysis is provided. It is unclear how the method would behave with a vocabulary of hundreds or thousands of words.

6. **No sensitivity analysis for the three manually-set thresholds.** θ is set to "a quarter of the 2-norm," ϑ = 0.8, r = 0.5 — all without any sensitivity study showing how results change with different values.

### Trivial

7. The conclusion (lines 254-255) is generic and does not acknowledge any limitations or discuss failure modes.

## Nice-to-Haves

- The paper could be strengthened by comparing against additional continual learning baselines (e.g., replay-based methods that are standard in the continual learning literature), though the current comparison against ART and AEN is reasonable for the paper's own subfield.
- The reference extraction method's vulnerability to correlated features (e.g., all "red" training objects also having similar shapes) could be explicitly discussed as a limitation, even if not empirically tested.

## Removed Points

- **"Activation function (Eq. 1) does not encode input information"**: This misunderstands the prototype-based design. The FN's weight w_j is the stored prototype; which FN fires (determined by the distance check d(x, w_j) ≤ θ) conveys which feature prototype was matched, and the frequency-tagged signal encodes the prototype for routing at the MAN level. Downstream UANs know which FNs they connect to via the binary matrix W^{α_k}. This is a standard prototype-neuron mechanism, not a flaw.

- **"Straw-man comparison with offline methods"**: The paper transparently reports drops with ↓ and explicitly states offline methods "are frozen after training." The meaningful comparison is OML vs. online methods (ART, AEN), where OML consistently wins. Including offline methods as a lower-bound demonstration of catastrophic forgetting is informative, not deceptive.

- **"Baseline scoring favoritism in Tables 2-3"**: The paper explicitly discloses the generous scoring for baselines (lines 248-250: "we count this as a correct result for them"). Being transparent about a favorable-to-baselines protocol while still outperforming them is not a weakness.

- **"Feature extraction uses hand-crafted features, weakening the 'neural network' claim"**: SAM (a neural network) extracts object boundaries. Fourier descriptors and MFCCs are standard signal-processing features used throughout the literature. This is a nitpick about presentation, not a substantive weakness.

- **"Correlated-features vulnerability in reference extraction"**: Plausible as a theoretical concern but speculative — no evidence that this causes problems in practice. Not a verified weakness of the submitted work.

- **"Brain-inspired framing is decorative"**: Subjective framing critique with no specific technical claim to verify against the paper.

- **"Missing continual learning baselines (EWC, SI, etc.)"**: The paper uses methods from its own literature (Xing et al., ART, AEN). Demanding baselines from a different subfield (deep-learning continual learning) is scope creep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate the human-in-the-loop claim.** The most impactful improvement would be running experiments with a simulated user that provides both positive and negative answers with varying probabilities, and reporting conflict detection accuracy (precision, recall, F1). Even a simple ablation showing the effect of different answer patterns on downstream accuracy would substantially strengthen the paper.
2. **Report variance.** Run each experiment at least 5 times with different random seeds and report means ± std.
3. **Add ablation studies.** At minimum: (a) remove lateral connections, (b) replace reference extraction with a baseline version that treats all words identically, (c) vary the distance threshold θ.
4. **Report dataset statistics** (class counts, samples per class, vocabulary size, feature dimensions) and include a discussion of scalability.

## Score and Decision

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison to OML |
|------|-----------|-------|-------------------|
| gNoqEdT2wO.md (MCIL benchmark) | 2.33 | R1 bracketing | Weaker: benchmark paper with no new method; OML has novel architecture |
| WM5G2NWSYC.md (Projected Subnetworks) | 2.00 | R1 bracketing | Weaker: unclear contribution; OML has clearer architecture and results |
| JIlIYIHMuv.md (LVLM-CL) | 2.50 | R1 bracketing | Weaker: straightforward application of existing methods; OML is more novel |
| HCCkCjClO0.md (Online Weight Approximation) | 3.00 | R1 bracketing | Weaker: incremental method; OML has more architectural novelty |
| jUCtGezFwH.md (OPWA) | 4.75 | R1 middle, R2 narrowing | Stronger evaluation (proper baselines, clearer reporting) but less novelty; OML is comparable in quality but less rigorous |
| eXrUdcxfCw.md (EMA Prototypes) | 4.80 | R1 middle | Similar: prototype-based method with modest novelty but proper evaluation; OML is more novel but less rigorous |
| G9Ea7mlqGO.md (CLIP online continual) | 3.80 | R1 middle | Weaker evaluation than both; OML has more novel architecture |
| UhKkWHkvfg.md (MDAA) | 5.00 | R1 middle, R2 narrowing | Stronger: proper multi-modal benchmarks and ablations; OML has more novel architecture but significantly weaker evaluation |
| KbetDM33YG.md (Online GNN Evaluation) | 8.00 | R1 high | Much stronger: clear problem, rigorous evaluation, accepted — OML is not at this level |
| GRMfXcAAFh.md (Oscillatory SSM) | 8.00 | R1 high | Much stronger: theoretical analysis + strong experiments; OML is far from this level |
| k9NYnsC4Mq.md (PROOF) | 5.67 | R2 narrowing | Stronger: 9 benchmark datasets, detailed ablations, SOTA comparisons; OML has more unique architecture but substantially weaker evaluation |
| BZWssJoYEv.md (DMI) | 5.50 | R2 narrowing | Comparable novelty but more theoretical grounding and proper evaluation; OML has clearer architecture but weaker experiments |
| Pa6SiS66p0.md (Beyond Unimodal) | 4.33 | R2 narrowing | Similar: multimodal continual learning exploration, comparable evaluation depth |
| vSOTacnSNf.md (Multimodal Meta-learning) | 4.33 | R2 narrowing | Similar: novel method with limited evaluation |

**My rationale:** The paper sits below the 5+ papers (PROOF, DMI, MDAA) which all have proper evaluation protocols (multiple runs, ablations, standard benchmarks). It sits above the 2-3 range papers which have fundamental flaws or very weak novelty. OML's architecture is genuinely novel — the hierarchical pathway design, frequency routing, and reference extraction are clearly original — but the evaluation has critical gaps: no variance, no ablations, no dataset statistics, and most importantly, the headline human-in-the-loop contribution is essentially unevaluated. The decision is Reject with encouragement to address the evaluation gaps in a revision.