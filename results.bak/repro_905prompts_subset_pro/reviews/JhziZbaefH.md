## Summary

This paper proposes OML, a brain-inspired neural network for online multimodal learning. The architecture uses a hierarchical, modular design with feature neurons, unimodal association neurons, and multimodal association neurons connected by ascending, descending, and lateral pathways. Key claimed innovations include (1) a frequency-based signal routing mechanism that enables cross-modal recall and modality disambiguation, (2) an autonomous reference extraction algorithm that learns which feature dimensions a word refers to, and (3) a conflict detection and human-in-the-loop (HITL) mechanism that asks users questions when input conflicts with stored knowledge. Experiments on small-scale fruit/object datasets with vision, audio, and taste modalities show OML outperforms online baselines and largely avoids catastrophic forgetting.

## Strengths

- **Novel hierarchical architecture with bidirectional pathways**: The design of specialized neuron types (feature, unimodal association, multimodal association) with ascending, descending, and lateral connections is genuinely creative for the online multimodal learning setting. The frequency-tagged signal routing (Section 3.3) provides a principled way to ensure cross-modal recall activates the correct target modality, which is absent in prior online methods like AEN and ART.

- **Effective reference extraction mechanism**: The algorithm that tracks variance shrinkage across feature dimensions and uses the coefficient of variation to determine which features a word refers to (Section 3.4, Eq. 7) is a well-motivated idea. Table 2 demonstrates that OML maintains performance when color-referring words are introduced (87.8% V→A open, 86.2% A→V open on E-Fruits), while offline methods suffer drops of 6–13 points. The paper is transparent that baseline scoring is lenient (returning the full object counts as correct for baselines), making OML's advantage a conservative estimate.

- **Strong continuous learning results**: In open-environment settings (Tables 1–3), OML's accuracy remains stable or improves while offline methods degrade sharply. For example, on Fruits (open), OML achieves 89.8% V→A and 89.0% A→V, while the best offline method (NRCH) drops to 86.5% and 84.4%. On the modality extension task (Table 3), OML consistently beats AEN across all six cross-modal retrieval directions.

- **The conflict detection and learning procedure is described in substantial detail**: Section 3.5 methodically enumerates four activation scenarios and specifies conflict conditions, question templates, and update rules for each. This algorithmic specificity is a genuine contribution over prior online multimodal methods.

## Weaknesses

### Fatal

None.

### Major

- **The human-in-the-loop claim is experimentally unvalidated**: The paper's Section 1 explicitly lists HITL conflict resolution as one of two defining additional attributes of the method. Yet the experimental validation consists of a single sentence: "when we randomly add 10% of word-image or word-taste data pairs with incorrect matches, OML is able to detect all conflicts and raise appropriate questions" (end of Section 4). There are no metrics for conflict detection precision/recall, no measurement of question quality or quantity, no comparison of learning outcomes with vs. without user feedback, and no false-positive analysis. Given that HITL is half of the paper's claimed contribution, this evidential gap is substantial.

- **The signal-routing mathematics are imprecisely specified**: Eq. (1) defines the FN output as a double sum over dimensions and time steps (`Σ_{i=1}^n Σ_{t=1}^T`), which reads as a scalar. Eq. (3) sums these into `z^β`, and Eq. (6) applies a Fourier transform `F(z^β)` to what is, as written, also a scalar. The intended interpretation (a time-domain signal vector whose frequency components are extracted by the Fourier transform) is recoverable from context, but the notation is inconsistent — sometimes bold vectors, sometimes scalars, with no explicit signal dimensionality. Since frequency-based routing is the core mechanism enabling cross-modal recall and modality disambiguation, this imprecision undermines reproducibility and clarity for a central component.

### Minor

- **No ablation studies**: The contributions of lateral connections, reference extraction, conflict checking, and frequency-based routing are never isolated. Without ablations, it is unclear which components are actually responsible for the observed gains over AEN and ART.

- **Lateral connection mechanism is underspecified**: The paper states that "activated FNs activate their similar FNs via the lateral pathways, which improves the generalization ability" but never specifies what "activate" means concretely — is it activation propagation, weight sharing, or something else? The connection criterion is given (`d(w_i, w_j) ≤ 2θ`), but the operational semantics during learning are absent.

- **Limited evidence for reference extraction claims**: While Table 2 results are positive, the evaluation relies on end-to-end retrieval accuracy with lenient scoring for baselines. A direct diagnostic experiment — e.g., probing whether a color-word neuron's descending signal selectively activates color but not shape feature neurons — would provide stronger evidence that the reference extraction mechanism actually disentangles referring behavior as claimed.

- **Hyperparameter choices stated without sensitivity analysis**: Parameters θ (quarter of weight norm), ϑ = 0.8, r = 0.5 are given without justification or analysis of how sensitive results are to these choices.

### Trivial

- The default answer for unanswered user queries is set to "positive" (end of Section 4, before 4.1), which introduces a learning bias that is not discussed.

- No explicit forgetting metric is reported; the catastrophic forgetting claim relies on comparing open-environment accuracy against closed-environment accuracy, which is indirect.

- Computational cost, memory growth, and scalability to larger vocabularies are not discussed.

## Nice-to-Haves

- A focused HITL evaluation with metrics for conflict detection quality, question counts, and learning accuracy with/without feedback would substantially strengthen the paper.

- A diagnostic experiment directly measuring reference extraction (probing descending pathway selectivity) would provide stronger evidence for this component.

- Clarifying the signal routing mathematics with explicit vector dimensions and a running example of how the Fourier transform yields a routing decision.

- Ablation studies isolating the contribution of each architectural component.

- Discussion of limitations, computational cost, and scalability.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The Fourier transform of a scalar is not meaningful" (harsh critic, framed as fatal)**: Removed as a fatal claim. The intended meaning is recoverable — `y^{α_k}` is intended as a time-domain signal vector, not a scalar. The notation is sloppy but the concept is not broken. Retained as a major presentation/clarity weakness instead.

- **"The experimental design obscures the contribution of reference extraction" (harsh critic)**: Removed as a critique of the evaluation design. The paper is transparent that baseline scoring is lenient (returning full objects counts as correct), which is a conservative choice that favors baselines, not OML. This does not obscure OML's contribution — if anything, it makes OML's advantage harder to demonstrate.

- **"What 'activated by the auditory channel' means when signals are frequency-encoded remains unclear" (harsh critic)**: Removed. Section 3.5 explicitly defines sets like `^A N^b` (visual FNs activated by the auditory channel) and uses them in concrete intersection checks. The mechanism is specified.

- **"The offline baselines (DAE, DBM, etc.) are not appropriate comparators" (harsh critic)**: Removed. The paper explicitly distinguishes offline from online methods and uses offline methods primarily to demonstrate catastrophic forgetting in the open environment, which is an appropriate use. The meaningful comparison is indeed with ART and AEN, which the paper provides.

- **"Brain-inspired label used without connecting to specific neurobiological evidence" (harsh critic)**: Removed. This is a stylistic framing choice, not a scientific weakness. The paper cites Kudithipudi et al. (2022) for biological motivation and the architecture is described in computational terms.

- **Strength Finder: "Conflict detection… is experimentally validated by the ability to detect all conflicts when incorrect multimodal pairs are injected"**: Removed as a standalone strength. This is the same one-sentence claim noted as a major weakness above; calling it "experimentally validated" overstates the evidence.

- **Strength Finder: "The paper addressed an important problem" / generic strengths**: Removed as superficial. These lack concrete evidence anchoring.

## Novel Insights

The paper's use of frequency-tagged signals for modality disambiguation in an online growing network is a genuinely creative idea not seen in prior online multimodal methods. Instead of requiring separate output heads or explicit modality labels, the λ parameters on feature dimensions create an implicit routing mechanism where the Fourier transform at the multimodal association layer naturally separates signals by their source modality and feature type. Combined with the variance-tracking reference extraction, this provides an elegant, unified mechanism for both "what does this word refer to?" (reference extraction) and "which modality should be activated?" (routing). While the mathematical presentation needs improvement, the conceptual synthesis of these ideas within a single online learning architecture is novel.

## Suggestions

- Prioritize adding a proper HITL evaluation (even if simulated) before strengthening other aspects. Without this, one of the paper's two core claims remains unsubstantiated.
- Rewrite the signal equations with explicit vector/matrix dimensions so that the Fourier transform operation is clearly defined. A running example with concrete numbers would help enormously.
- Add at minimum an ablation removing the conflict detection mechanism to show its impact on learning outcomes.
- Consider replacing the single-sentence "10% incorrect matches" claim with a proper table reporting conflict detection precision, recall, and learning accuracy with user corrections vs. without.

---

**Calibration summary across all rounds:**

*Round 1 anchors (bracketing):*
- WM5G2NWSYC (2.00): Projected Subnetworks — substantially weaker paper with thin contributions. OML is clearly stronger.
- gNoqEdT2wO (2.33): Multimodal Class-Incremental benchmark — weaker contribution, simpler method. OML is stronger.
- Pa6SiS66p0 (4.33): Beyond Unimodal Learning — interesting problem but weak baselines. OML has more novel architecture but similar evaluation gaps. OML is comparable to slightly stronger.
- UhKkWHkvfg (5.00): MDAA for MM-CTTA — similar methodological confusion, less clear contributions. OML has more novelty.
- TPZRq4FALB (8.00): READ — far stronger in rigor, experimental depth, and clarity. OML is clearly below this.

*Round 1 bracket: 4.5–6.5*

*Round 2 anchors (narrowing):*
- cHyQT6Y1jY (5.75): Cognitive Dissonance in LLMs — similar profile of interesting cognitive-inspired ideas with execution gaps. OML has more novel architecture, comparable rigor issues. OML is slightly below due to HITL overclaim.
- sb7qHFYwBc (6.50): C-CLIP — stronger execution, clearer contributions, solid experiments. OML is below this.
- OCpxDSn0G4 (6.00): Meta-Continual NF — less novel but better executed. OML is below this.

*Final score:* 5.5 — the paper presents genuinely novel architectural ideas but has a significant gap between its HITL claims and experimental evidence, with notation issues that undermine clarity of the core mechanism.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>