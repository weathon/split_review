Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper presents an unsupervised pipeline for learning dynamic functional connectomes from brain-wide calcium imaging in *C. elegans*. The key idea is to compute time-varying pairwise "differential affinities" between neurons, organize them into a 3-way tensor (time × worms × affinities), apply non-negative tensor factorization (NTF) to discover components that capture repeated affinity patterns across animals and time intervals, and then run a nested weighted stochastic block model (NWSBM) on the resulting affinity factors to infer communities. The pipeline makes a novel biological prediction (AWB neuron involvement in salt sensing) that the authors validate with a causal silencing experiment.

## Strengths

- **Novel tensor formulation that captures dynamic interactions via affinities rather than raw neural traces.** The paper constructs a 3-way tensor with dimensions `time × worms × pairwise affinities` instead of the more standard `worms × neurons × time`. This design allows non-linear affinity computations to be performed *before* tensorization (Sections 2.1–2.2), and the resulting temporal factor in each component naturally highlights experimental epochs when a given affinity pattern is active (Fig. 3a,c). This is a genuine departure from prior work that largely uses static correlations or multi-linear decompositions of raw traces.

- **Experimental validation with a causal manipulation of a novel predicted neuron.** The algorithm predicted that neuron AWB—canonically an aversive olfactory neuron—participates in salt sensation. Silencing AWB with histamine significantly increased salt avoidance (p = 5.7e-11, +25% effect), a non-obvious result that contradicts prior assumptions (Section 4). This provides direct causal evidence that the method can recover functionally relevant predictions, not just correlational patterns.

- **Community detection choice is quantitatively grounded.** On the LFR weighted benchmark (9 network types), NWSBM achieves the highest mean NMI in 6 out of 9 cases, outperforming Louvain, Combo, AS, NNSED, and GNNS100 (Table 1). This supports the choice of NWSBM for extracting communities from the affinity factors.

- **Interpretable components that map to experimental conditions.** The temporal and worm factors from tensor components align with stimulus intervals (e.g., NaCl application in Fig. 3a,b, pentanedione in Fig. 3c,d), and the community structure can be traced back to individual neural traces (Fig. 4). This interpretability is a concrete practical advantage.

## Weaknesses

### Fatal
None.

### Major

- **The validation experiment does not test the dynamic community structure—the paper's core contribution.** The paper claims to "reveal which communities form among neurons at different times" and to validate its ability to "robustly predict causal interactions between neurons." However, the experiment simply confirms that one neuron (AWB) plays a role in salt sensing—a finding that could have been obtained by simpler correlation-based methods. The predicted *community organization* (which neurons cluster together, how groups change over time) is never directly validated. The link between the *specific inferred network structure* and behavior is not established. This is a structural gap between the claimed contribution and the evidence provided.

- **The differential affinity computation is critically underspecified.** Section 2.1 describes the measure only in prose: "compare two neurons' derivatives during intervals in which both had a constant sign." No formal equation is provided. Missing details include: how derivatives are estimated from noisy calcium traces (finite differences? smoothing? kernel?), how monotonic intervals are identified, what window size is used, what similarity metric is applied to the derivatives (correlation? Euclidean distance? something else?), and how the result is normalized to produce bounded, non-negative affinities. Without these details the method is not reproducible. The paper also acknowledges that coinciding monotonic changes could arise from "a common phenomenon" (line 38) rather than interaction, but provides no analysis of how frequently this produces spurious affinities.

- **Tensor alignment across worms with different stimulus sequences is unaddressed.** The paper states that worms were exposed to stimuli in "3 possible sequences" (line 119). The tensor has a shared time axis across worms, but the paper never explains how time is aligned when different worms received stimuli in different orders. Line 81 states "the application of these stimuli is important, since it provides correspondence between the time axes," but the mechanism for achieving this correspondence is not described. If alignment is by absolute recording time, the same tensor index corresponds to different stimuli across worms. If alignment is by stimulus onset, the handling of variable sequence orders and durations is unspecified. This is a fundamental issue: the temporal factor that identifies "when" a pattern is active is uninterpretable without a clear alignment procedure.

- **The number of tensor components R for the real data is not specified or justified.** Section 2.2 says "let $R$ be the number of components chosen" but never states what value of $R$ was used for the *C. elegans* data or how it was selected. This is a critical hyperparameter that determines the granularity of the decomposition. No selection criterion (explained variance elbow, stability analysis, cross-validation) is provided, and no sensitivity analysis is shown. This makes the results arbitrary and unreproducible.

### Minor

- **The benchmark NMI scores are low in absolute terms.** NWSBM achieves only 0.28–0.65 on most benchmarks, and on Net 8 three other methods obtain perfect scores (1.0) while NWSBM gets 0.51. While NWSBM leads in 6/9 cases, the low absolute scores suggest either the benchmarks are very challenging or the methods struggle with these weighted networks. No statistical significance is reported (e.g., confidence intervals across the 10 instances).

- **The decision to vectorize affinity matrices (removing symmetry) discards structural information** and inflates the effective data dimension. This design choice is mentioned in passing (line 53) but its implications are not discussed.

- **The qualitative examples in Fig. 3 are illustrative but not statistically evaluated** (e.g., significance of component loadings, reproducibility across random seeds of the NTF decomposition, or stability of community assignments).

### Trivial
- Several figure captions describe panels but standalone readability could be improved.
- The claim of "non-linear similarities" (line 34) overstates what is essentially a derivative-based comparison; the non-linearity comes from the separation of affinity computation from tensorization, not from the affinity measure itself.

## Nice-to-Haves
- Baseline comparison on real data against simpler alternatives (e.g., sliding-window Pearson correlation + Louvain, or NMF on neuron×time matrix + clustering).
- Ablation replacing differential affinity with standard correlation (global or windowed) to test whether the specific measure adds value.
- Additional validation experiments testing more predictions from the same community (beyond just AWB).
- Comparison of inferred communities against known anatomical connectomes (chemical synapses, gap junctions) to assess biological plausibility.
- Systematic selection procedure for $R$ with robustness analysis.

## Removed Points

- **"Compared methods (Combo, AS, NNSED, GNNS100) are nonstandard and may be improperly configured"**: These are known methods in the community detection literature; the paper refers to them without full description which is standard for benchmark tables. Removed as this criticism reflects reviewer unfamiliarity rather than an author error.
- **"Lack of details on LFR parameter settings"**: The paper references "A1 for details" (line 143), indicating these are in the appendix, which the parser stripped from this version. Removed per the rule that missing appendix content is a parser artifact.
- **Several formatting/style nitpicks** from the Section-by-Section Notes (e.g., "vague about prior work," "claim that NWSBM yields 'a clear view' is subjective"): removed as generic or stylistic critiques that do not affect the paper's validity.
- **"Not directly compared to sliding-window correlation or fMRI methods"**: The paper explicitly scopes itself to *C. elegans* neural data; demanding comparison to fMRI methods is scope creep.
- **"Post-hoc speculation" about the direction of the behavioral effect**: The paper appropriately interprets the surprising result (increased avoidance when silencing an aversive neuron) as suggesting oppositional interactions. This is standard scientific interpretation, not speculation.

## Novel Insights

The most interesting observation that emerges from synthesizing the reviews is the tension between the paper's ambition and its validation strategy. The paper introduces a genuinely novel representational approach—operating on pairwise affinities via tensor factorization rather than raw traces—which is a conceptually clean way to handle time-varying functional interactions. Yet the validation tests only the weakest link in the chain (a single neuron prediction), leaving the central claim about *dynamic community organization* entirely unsupported. This is not a fatal flaw but a striking asymmetry: the pipeline generates rich, multi-level structure (affinity patterns × time intervals × worm loadings × community partitions), but the experiment only confirms that one node in one community participates in the expected sensory modality. A more compelling validation would test whether the inferred communities are stable across random restarts, whether they overlap meaningfully with known anatomical circuits, or whether silencing multiple members of the same predicted community produces concordant behavioral effects.

## Suggestions

1. **Formalize the affinity computation completely.** Provide explicit equations for derivative estimation, monotonic interval detection, the similarity metric applied within intervals, and the normalization to bounded non-negative values.
2. **Describe and justify the temporal alignment procedure.** Explain how the 3 different stimulus sequences are handled—whether worms are aligned by stimulus onset, by absolute time, or by some other scheme—and discuss the limitations of the chosen approach.
3. **Specify $R$ and provide a selection rationale.** State the value used, describe the selection method (e.g., reconstruction error elbow, stability), and show sensitivity to this choice.
4. **Validate the community structure directly.** At minimum, show that community assignments are stable across random seeds and subsamples of worms, and compare the inferred communities to known anatomical connectomes (chemical and electrical) to assess whether they capture biologically plausible groupings.
5. **Temper the claims in the abstract.** The current wording ("experimentally validated, confirming that our method is able to robustly predict causal interactions between neurons to generate behavior") overstates what the single validation experiment demonstrates.

## Score and Decision

The paper introduces a novel and well-motivated pipeline for learning dynamic functional connectomes, and the experimental validation of a surprising biological prediction (AWB involvement in salt sensing) is a genuine strength. However, the method is critically underspecified in several respects—the affinity computation lacks a formal definition, the tensor alignment across worms with different stimulus sequences is not explained, and the key hyperparameter $R$ is not justified or even stated. Moreover, the validation experiment tests only a single-neuron prediction, leaving the paper's core claim about *dynamic community organization* unvalidated. These issues are addressable with substantial revision, but in its current form the paper does not meet the bar for acceptance.

**Overall assessment**: The core idea is promising and the biological finding is interesting, but the methodological gaps and the mismatch between claims and evidence are too significant to overlook.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>