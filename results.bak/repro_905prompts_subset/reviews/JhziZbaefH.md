## Summary

This paper proposes OML, a brain-inspired hierarchical neural architecture for online multimodal learning. The network uses distinct neuron types (FNs, UANs, MANs) organized into ascending, descending, and lateral pathways to learn multimodal associations incrementally. It also features a reference extraction mechanism that uses coefficient-of-variation thresholds to identify which feature dimensions (e.g., color vs. shape) a word refers to, and a rule-based conflict detection system that can ask users questions when input mismatches occur. Experiments on Fruits, HomeF, and extended datasets show OML outperforming other online methods in open-environment settings across three evaluation scenarios.

---

## Strengths

- **Novel architecture with explicit design for online multimodal learning.** The hierarchical modular architecture with three neuron types (FN, UAN, MAN) and dedicated ascending/descending/lateral pathways is a well-specified and principled design for incremental multimodal binding. The distinction between OIAM (order-independent, visual) and ODAM (order-dependent, auditory) activation modes reflects genuine differences between modalities.

- **Reference extraction mechanism is clever and grounded.** The coefficient-of-variation approach (Section 3.4) provides a clear, interpretable way to identify which feature dimensions a word refers to. This goes beyond standard multimodal alignment by attempting to learn word-referent structure (e.g., "red" → color features only), which is a non-trivial and under-explored problem.

- **Strong empirical results on the core multimodal learning task.** In the open environment (Tables 1–3), OML consistently achieves the highest accuracy across both datasets and all recall directions. On HomeF Open A→V, OML (83.6) substantially outperforms the best offline method NRCH (76.9) and the best online method AEN (80.4), demonstrating genuine benefit for online learning without catastrophic forgetting.

- **Modality extension to a third (taste) channel.** Table 3 shows OML significantly outperforming AEN on all VAT and VAT-HomeF tasks, including directions like T→A and T→V. The frequency-parameter routing mechanism that lets OML distinguish whether "tián" refers to taste or vision is a concrete architectural innovation.

---

## Weaknesses

### Major

1. **The conflict detection claim is effectively untested.** The paper lists conflict detection with human-in-the-loop interaction as a headline contribution (attribute (2) in Section 1). Yet the only evidence provided is a single sentence in Section 4.1(3): *"when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions."* No experimental protocol, no metrics (TPR, FPR, precision, recall), no comparison against a variant without interaction, no analysis of which conflict types succeed or fail. For a claimed capability that distinguishes OML from prior online methods, this is a critical evidential gap.

2. **No statistical rigor on any experimental result.** All numbers in Tables 1–3 report single values without standard deviations, confidence intervals, or significance tests. The margins between OML and the next-best online method are often 1–3 percentage points (e.g., Fruits Open V→A: OML 89.8 vs. AEN 86.2; HomeF Open V→A: OML 85.5 vs. AEN 82.3). Without variance estimates, these differences cannot be trusted as reliable.

3. **No ablation studies.** None of the architectural components are ablated to measure their individual contributions: no removal of lateral connections, no removal of descending pathways, no removal of the Fourier routing (Eq. 6), no removal of the reference extraction module. The paper claims these components are essential (Section 3), but provides no evidence.

### Minor

4. **Method is a rule-based symbolic system, not a learned neural network.** The architecture uses hand-designed activation functions, deterministic connection-adding rules, and conditional if-then logic for learning (Section 3.5). No loss function, gradient signal, or optimization procedure is specified. New neurons are initialized based on recognition failures, not trained. This does not invalidate the contribution, but framing it as a "neural network" that "learns" is imprecise — it is closer to an ART-style adaptive resonance system with additional structure. A more accurate framing would help the reader evaluate what is being proposed.

5. **Reference extraction is validated only indirectly.** The claim that OML can identify which features a word refers to (e.g., color vs. shape) is supported solely through higher accuracy on E-Fruits and E-HomeF (Table 2) relative to baselines. No experiment directly verifies that the coefficient-of-variation thresholds pick out the correct feature dimensions (e.g., showing that for "red," σ is low for color dimensions and high for shape dimensions). An ablation removing the reference extraction component is also absent.

6. **Feature provision to baselines is unspecified.** The paper describes OML's features (SAM for vision, MFCCs for audio, provided features for taste) but does not clarify whether the same precomputed features were provided to all baseline methods. DAE and DBM typically learn end-to-end from raw data; feeding them precomputed features could alter their behavior. If they received different features, the comparison is not controlled.

7. **Offline methods are evaluated in a setting they are not designed for.** The open environment feeds four sequential data parts to offline methods. Their catastrophic forgetting is expected — these methods are designed for batch training on the full dataset. While this demonstrates that offline methods fail in incremental settings, it does not constitute a meaningful comparative evaluation. A proper continual learning baseline (e.g., fine-tuning with replay, EWC) would better establish the problem's difficulty.

### Trivial

8. The motivational "garnet" example from Figure 1 does not appear in the experiments (which use Chinese fruit and color names like "hóng sè").
9. The claim that OML learns "in a manner similar to humans" is asserted (abstract, conclusion) without any behavioral or cognitive evidence.

---

## Nice-to-Haves

- Add an experiment directly measuring conflict detection accuracy: introduce known-mismatched pairs at controlled rates and report precision/recall for question-asking, ideally compared against a variant with no interaction.
- Add an ablation removing the reference extraction component to isolate its contribution to Table 2 results.
- Visualize the coefficient-of-variation values across feature dimensions for specific learned words to directly verify the reference extraction mechanism.
- Report multiple runs (≥5) with mean ± std for all key results.

---

## Removed Points

The following points were flagged by the harsh critic but are removed or demoted from the main review:

- *Criticism about missing related work on continual learning (EWC, progressive networks, replay-based methods).* The paper's scope is specifically multimodal online learning with human interaction; it cites the relevant multimodal online learning literature (Xing et al., Tan et al., AEN). Requesting a survey of general CL methods is scope creep. → **Removed.**

- *Criticism about T parameter in Eq. (1) being "perplexing."* The paper explicitly states its value "does not affect the algorithm." This is noted by the authors; it is a design choice for encoding, not a flaw. → **Removed.**

- *Criticism about the Fourier transform being "artificial" or the temporal aspect being "artificial."* The Fourier transform is used for signal routing between channels (matching frequencies to pathways), which is a design decision explained in the paper. The temporal aspect is part of the signal formulation, not an empirical claim. → **Removed.**

- *"Reproducibility: the paper omits code release."* Code release is not a requirement for submission; this is a nice-to-have. → **Moved to minor/trivial framing or removed.**

- *"Human-likeness claim requires behavioral validation."* The paper's human-like framing is a common rhetorical device in brain-inspired AI papers; demanding behavioral studies is outside the paper's scope. The claim is noted as overblown but not a fatal weakness. → **Removed as a formal weakness, noted as trivial.**

- *Criticism about Gaussian threshold ϑ=0.8 initialization not specified.* The threshold is given as a fixed hyperparameter, which is standard. → **Removed.**

---

## Novel Insights

The harsh critic raises a point that, while over-stated, contains a genuine insight: the paper's architecture is fundamentally a *symbolic rule system with neural vocabulary* rather than a learning algorithm in the conventional sense. The authors might benefit from reframing OML as a "biologically-inspired cognitive architecture" rather than a "brain-inspired neural network," as this would better align reader expectations with what the method actually does (hand-coded update rules, no gradient-based optimization). The lack of a formal learning objective means the paper's central theoretical claim — that this architecture enables "learning" — cannot be evaluated against any standard notion of learnability or convergence. This is not a fatal flaw for an engineering contribution, but it is a genuine conceptual tension that the paper does not acknowledge.

---

## Suggestions

1. **Evaluate conflict detection quantitatively.** Design a controlled experiment with known proportions of mismatched pairs and report precision, recall, and F1 for question-asking. Compare against a variant without interaction to establish baseline performance.

2. **Add standard deviations.** Repeat all key experiments at least 5 times and report mean ± std. Without this, the reported margins cannot be interpreted.

3. **Add ablation studies.** Systematically remove: lateral connections, descending pathways, Fourier routing, and reference extraction. Show the contribution of each component.

4. **Directly validate reference extraction.** For learned color words, plot the coefficient of variation across color-feature vs. shape-feature dimensions to confirm the mechanism works as described.

5. **Reframe the method's terminology.** Call it a "cognitive architecture" or "neuro-symbolic system" rather than a neural network, since there is no learning signal, loss function, or optimization.

6. **Specify features provided to baselines.** Clarify whether DAE, DBM, etc. received the same SAM/MFCC features or raw data.

---

## Calibration

**Round 1 bracket:** [3.5, 5.0] — above the weak-anchor band (2.3–3.3: YrxhSkfHh0 at 3.33, gNoqEdT2wO at 2.33, a4O528mek9 at 3.00) but below strong papers (8.0 cluster). Comparable to middling rejected papers in the 4–5 range.

**Round 2 narrowing:** Compared against cHyQT6Y1jY (5.75, cognitive-dissonance aware CL in LLMs — also has conflict detection but with proper evaluation, proper learning framework), Pa6SiS66p0 (4.33, multimodal lifelong learning benchmark — limited baselines, single dataset), CagdoUkvvl (4.50, multimodal CL with dual-learner — has loss functions and ablations), YFdopzmpdr (5.20, stability-plasticity architecture — extensive experiments). The current paper has more architectural novelty than Pa6SiS66p0 and a more clearly defined architecture than all anchors, but the evaluation gaps (untested conflict detection, no variance, no ablations) are more severe than any anchor in this band. It is weaker than cHyQT6Y1jY and YFdopzmpdr, comparable to CagdoUkvvl but with weaker methodology, slightly below Pa6SiS66p0 in evaluation completeness.

**Final score:** 4.0 — the paper has genuine architectural novelty and reasonable baseline results, but the severe under-evaluation of its flagship capability (conflict detection) prevents a higher score.

**Anchors considered:**
- YrxhSkfHh0 (3.33, R1) — weaker paper; this paper is stronger
- gNoqEdT2wO (2.33, R1) — much weaker; this paper is stronger
- a4O528mek9 (3.00, R1) — weaker; this paper is stronger
- uffmkDtlR2 (2.60, R1) — weaker; this paper is stronger
- BZWssJoYEv (5.50, R1) — stronger overall evaluation; this paper is weaker
- 3YQYo1O01W (3.67, R1) — comparable; conflict detection study with limited evaluation
- Pe3AxLq6Wf (6.25, R1) — significantly stronger; proper learning framework
- cHyQT6Y1jY (5.75, R2) — stronger; evaluates conflict detection properly
- YFdopzmpdr (5.20, R2) — stronger; extensive experiments
- Pa6SiS66p0 (4.33, R2) — slightly stronger evaluation; less architectural novelty
- CagdoUkvvl (4.50, R2) — stronger methodology (loss functions, ablations)
- vSOTacnSNf (4.33, R3) — comparable; rejected
- XTwwtlEfTF (4.50, R3) — comparable; rejected

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>