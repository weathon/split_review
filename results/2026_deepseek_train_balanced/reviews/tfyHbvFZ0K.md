## Summary

This paper challenges a foundational assumption of the Knowledge Neuron (KN) thesis—the Knowledge Localization (KL) assumption, which holds that a fact can be localized to a few MLP neurons. Through consistency analysis across 3 PLMs (GPT-2, LLaMA2-7b, LLaMA3-8b) and 3 localization methods, the authors show that most facts (77% in LLaMA3-8b) violate this assumption. They propose an alternative Query Localization (QL) assumption with two hypotheses: (1) KNs are query-specific rather than fact-specific (Query-KN Mapping), and (2) the attention module dynamically selects which KNs to use for answering (Dynamic KN Selection). A Consistency-Aware modification method is introduced as a practical application. The paper is primarily an empirical analysis of the KN thesis's limitations, with a secondary applied contribution.

## Strengths

- **Multi-method, multi-model evidence for the failure of the KL assumption (Table 1-1):** The paper uses 3 different knowledge localization methods (Dai et al. 2022, Enguehard et al. 2023, Chen et al. 2024) across 3 PLMs and reports the intersection of facts classified as K_II by *all three* methods simultaneously (the ∩:II column). For LLaMA3-8b under the static threshold, this yields 77%—ruling out method-specific artifacts. All three methods independently show a large majority of facts violate the KL assumption, not just one.

- **Causal evidence for Query-KN Mapping via direct activation manipulation (Figure 2-1):** Rather than merely observing correlations or modifying weights (which confounds multiple effects), the paper directly manipulates KN *activation values* (suppress/enhance) and measures changes in answer probability. For K_II facts, editing the query's own KNs produces large ΔProb, while editing neighbor KNs (especially Intersection) has much smaller effects. A control comparison with K_I facts shows the expected pattern (smaller gap), ruling out trivial explanations.

- **Causal demonstration that attention influences KN selection (Figures 2-2, 2-3):** The paper introduces Knowledge Synapses (KSs)—high-attention column vectors—and directly manipulates their attention scores. Manipulating query-related KSs changes both KN activation values and answer probabilities, while manipulating irrelevant KSs has significantly smaller effects. The heatmap visualization (Figure 2-3) further shows that suppressing KSs visually reduces KN activations. This goes beyond prior KN thesis work that focused almost exclusively on MLP modules.

## Weaknesses

### Major

1. **No comparison against established model editing methods in the literature.** The Consistency-Aware method is compared only against two KN selection strategies internal to the paper's pipeline: 𝒩ᵢ (local set, the standard KN-based selection) and 𝒩_g (global set, a naive baseline). The paper claims "outperforms two baselines by an average of 8% and 9% respectively" (contributions bullet), but ROME (Meng et al., 2022), MEMIT (Meng et al., 2023), and the standard KN editing pipeline from prior work are never evaluated. Without these comparisons, the practical significance of the proposed method relative to the state of the art is unclear. The paper's primary contribution is analytical rather than applied, but the contribution bullet explicitly claims practical improvement, making this gap consequential.

2. **Key hyperparameters and threshold values are unreported, harming reproducibility.** The static threshold value for K_I/K_II classification is never specified—the violin plot caption says "We select a threshold of 0.3 as an example" (line 276) but does not confirm this is the value used in the actual experiments. The CAS metric's hyperparameters β₁ and β₂ (Equation 7) are introduced but their values are not reported. The KS scaling factor α (Equation 5) and the update operation's λ₁/λ₂ (Equation 2) are also unspecified. The "thresholding techniques" for CAS selection (line 815) are mentioned but not detailed. This makes the entire evaluation pipeline irreproducible from the paper alone.

3. **No variance or uncertainty reporting for main experimental results (Tables 1-2, 2-3).** All metrics (Rel, Gen, Loc, Avg, ΔPPL) are reported as single point estimates with no standard deviations, confidence intervals, or indication of whether results are from a single run or averaged over multiple runs. Given that the differences between methods are often modest (e.g., Avg of 0.43 vs. 0.51 in the Erasure setting on LLaMA3-8b), it is impossible to assess whether these improvements are statistically reliable.

### Minor

1. **The Welch's t-test on threshold-split groups is uninformative.** The paper classifies facts as K_I/K_II via a threshold on CS₂, then runs a Welch's t-test comparing the CS values of the two groups (reporting p < 1e-6). This is essentially tautological: any threshold-based split on a continuous variable will almost always produce a significant t-test on that same variable, regardless of whether the underlying grouping is meaningful. The paper's real evidence for K_II's prevalence comes from the raw distributions (violin plots showing most facts have low CS₂) and the modification-based evidence (Table 1-2), not this test. The t-test framing should be either removed or explicitly acknowledged as a sanity check, not as independent evidence.

2. **No ablation or sensitivity analysis of the CAS hyperparameters.** The CAS metric (Equation 7) trades off mean activation (μ) and consistency (σ) via β₁ and β₂. Without any ablation study, it is unclear how sensitive results are to these choices—whether the method works for a range of values or is tuned precisely to produce the reported numbers.

3. **Characterization of prior work overstates the novelty of the critique.** The paper states that "previous research and the KL assumption essentially assume that all factual knowledge belongs to K_I" (line 22) and that prior work observed KN thesis problems "without deeply analyzing their causes" (line 840). Prior work (e.g., Niu et al., 2024; Hase et al., 2023) has raised related concerns about the oversimplification of the KN thesis. The paper's QL assumption is a genuine extension, but the framing somewhat downplays existing critiques.

### Trivial

- The paper uses "0.3" as an example threshold in the violin plot caption, but the actual static threshold used for all quantitative experiments is never stated explicitly.

## Nice-to-Haves

- An analysis of what kinds of facts/relations tend to be K_II (the violin plots hint at variation by relation but this is not explored) would strengthen the scientific contribution.
- Comparison to established editing methods (ROME, MEMIT) would clarify the practical value of the Consistency-Aware approach.
- Ablation studies on β₁, β₂ for the CAS metric.

## Removed Points

These points from the input reviews were checked against the paper and removed or demoted:

- **"Dynamic KN Selection evidence is correlational" (Harsh Critic):** REMOVED. The paper directly manipulates KS attention scores (suppress/enhance) while using irrelevant-KS controls, which is a causal intervention design, not a correlational one. The claim is factually wrong about the paper's methodology.
- **"Circular classification is a fatal/structural flaw" (Harsh Critic):** DEMOTED to Minor. The classification is explicitly definitional: facts below a CS₂ threshold are called K_II. The main evidence comes from the raw CS₂ distributions and independent modification experiments (Table 1-2), not the t-test. The t-test criticism is valid but does not invalidate the paper's core claims.
- **"Straw man about prior work" framed as a critical issue:** DEMOTED to Minor (point 3 under Minor). The characterization of prior work is somewhat simplified but not a straw man; prior KN thesis work does broadly assume localization applies to facts.
- **Generic/superficial strengths from Strength Finder (e.g., "addressed an important problem"):** REMOVED. Not specific enough to the paper's concrete contributions.
- **"Larger PLMs have more K_II because more parameters mechanically lower Jaccard metric" (Harsh Critic):** REMOVED. The paper acknowledges this possibility ("larger models, with more parameters, are more likely to store a single fact across multiple neurons" - line 285). The core claim about K_II prevalence is already supported within each model size independently.
- **"The two baselines are not independent baselines" framed as completely invalid:** KEPT but as a Major weakness (point 1). The paper *does* reference the standard KN approach, but should compare to established editing methods for the practical claim.

## Novel Insights

The most penetrating observation from the review process is the asymmetry between the paper's two contributions. The analytical contribution (identifying query-dependent KN localization and the attention module's role) is well-supported by multi-method, multi-model evidence and causal manipulation experiments—this part of the paper is strong. However, the applied contribution (the Consistency-Aware method) is evaluated only against internal ablations with missing hyperparameter specifications and no variance reporting, which means its practical significance is unsubstantiated relative to existing methods. This creates a disconnect: the paper can convincingly claim the QL assumption is more realistic than the KL assumption, but cannot convincingly claim its proposed method is a practical improvement over the state of the art. The paper would be stronger if it either (a) added external baselines and hyperparameter specifications to close this gap, or (b) reframed the Consistency-Aware method strictly as a proof-of-concept validation of the QL assumption rather than a competitive editing method.

## Suggestions

1. Report the actual static threshold value used for K_I/K_II classification, and all hyperparameter values (β₁, β₂, α, λ₁, λ₂, CAS thresholding method).
2. Add comparisons to at least one established model editing method (ROME or MEMIT) to contextualize the practical claims.
3. Remove or explicitly qualify the Welch's t-test as a sanity check rather than primary evidence. Shift emphasis to the raw CS₂ distributions and modification-based evidence.
4. Report standard deviations or confidence intervals for all main results in Tables 1-2 and 2-3, and state how many independent runs were performed.
5. Add an ablation study varying β₁ and β₂ to demonstrate robustness of the CAS metric.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>