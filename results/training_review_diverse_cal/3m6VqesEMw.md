I have all the paper content I need from the initial read. Let me now produce the final consolidated review.

---

## Summary

This paper proposes T³-S2S, a training-free triplet of modules — prompt balance, characteristics prominence, and dense tuning — that operate on cross-attention layers to improve multi-instance sketch-to-scene generation with frozen SDXL + ControlNet. The key motivations are two diagnosed failure modes: imbalanced prompt energy (rare-instance tokens have lower L2 norms in text embeddings) and value matrix homogeneity (small numerical differences between tokens in V matrices lead to instance coupling). The prompt balance module rescales instance keyword embeddings; characteristics prominence uses TopK indices from value matrices to amplify feature-map regions via spatial masks; dense tuning (adapted from Dense Diffusion) refines attention maps. Qualitative results show improvements on small/overlapping instances, but the quantitative evaluation is limited to 20 self-built scenes with small CLIP-Score margins and no statistical testing.

## Strengths

- **Identification of prompt energy imbalance as a concrete, measurable failure cause.** Section 3.2 quantifies that multi-instance prompt embeddings yield lower L2 norms for keywords like "houses" compared to single-word embeddings, and shows that cosine similarity analysis reveals diminished emphasis on rare instances. This goes beyond prior work that only examined attention maps and provides a clear diagnostic that motivates the prompt balance module.

- **Training-free approach with practical modular design.** All three modules (prompt balance, characteristics prominence, dense tuning) operate on frozen pretrained models without fine-tuning or additional data collection. The ablation in Figure 7 qualitatively isolates each module's effect: dense tuning reduces instance overlap, prompt balance recovers small objects, characteristics prominence sharpens features. This modular design means practitioners can deploy subsets of the method.

- **Directly addresses the under-explored role of value matrices in cross-attention.** Section 3.3 visualizes value-feature pairs and demonstrates that amplifying TopK values in V matrices can recover missing instances (Figure 4), introducing the concept of value homogeneity as a distinct failure mode separable from attention-map issues. The characteristics prominence module then operationalizes this insight by amplifying feature-map channels at TopK-corresponding spatial regions.

## Weaknesses

### Fatal
None.

### Major

- **The derivation of per-instance sketch masks $\mathbf{u}_m^i$ is never explained, making the core novel module (characteristics prominence) underspecified.** In Section 4.3, Eq. 5 sums "the sketch $\mathbf{u}_m^i \in \mathbb{R}^{b_m}$ of the instance at the current scale" to create enhancement masks $\mathbf{h}_m^j$. The input to the system is a single sketch image $\mathbf{C}_s \in \mathbb{R}^{h \times w}$, not a set of instance-level spatial maps. The paper never clarifies how $\mathbf{u}_m^i$ is obtained — whether it is the input sketch resampled at the current spatial resolution, a region extracted via attention maps, or something else. The $i$ superscript implies distinct sketches per instance, but no mechanism for instance-level decomposition of the input sketch is described. Without this, the characteristics prominence module (one of two novel contributions) is unreproducible and its empirical behavior uninterpretable. This is not a trivial omission; it is the central technical operation of the module.

- **Evaluation is too limited to support the claimed quantitative improvements.** The entire quantitative benchmark is 20 self-built sketch scenes (Section 5.1). No confidence intervals, bootstrapped statistics, or significance tests are reported. The user study is described only as "a 1-5 rating scale" with no information on number of participants, inter-rater reliability, or protocol — details may exist in the stripped appendix, but the main paper's reporting is insufficient. Baseline comparisons are restricted to ControlNet, T2I-Adapter, and Dense Diffusion; several training-free multi-instance methods that directly address the same "missing instance" problem (e.g., Attend-and-Excite, BoxDiff) are mentioned in passing (line 250) but not quantitatively compared with the full method. Given the small scale and lack of statistical rigor, the quantitative evidence does not convincingly show that T³-S2S outperforms baselines or that each module contributes significant value.

### Minor

- **The connection between the observed value homogeneity and the proposed characteristics prominence remedy is indirect.** The paper shows that value matrices have small numerical differences across tokens for small-area instances (homogeneity), and that naively amplifying TopK values recovers instances but introduces noise. The characteristics prominence module instead amplifies feature maps at TopK-index-corresponding spatial regions using sketch masks — but this does not directly address the homogeneity in the value matrices themselves. The diagnostic (homogeneity in V) and the remedy (amplifying F at selected spatial locations) operate at different points in the pipeline, and the paper does not demonstrate a causal link (e.g., by showing that the module measurably reduces homogeneity in the output).

- **Hyperparameter selection rests on a single qualitative example.** Figure 8 shows the effect of varying $K$ and $\beta$ for one sample only, with no quantitative sweep across multiple prompts. While $K=2, \beta=1$ is a plausible default, there is no evidence that these values generalize.

- **Prompt balance module's handling of compositional prompts is not analyzed.** Replacing keyword embeddings with single-word embeddings (e.g., "stone bridge" → "stone" and "bridge") could break adjective-noun or compound-noun relationships. The paper uses SpaCy for keyword detection but does not discuss failure cases or analyze how this interacts with prompt compositionality.

- **The dense tuning module is delegated almost entirely to an external reference.** The paper states "Specific implementation refers to Dense Diffusion (Kim et al., 2023)" without summarizing how the module operates in this context. While this is acceptable for a well-known technique, a brief self-contained summary would improve readability.

### Trivial

- The paper uses the notation $\mathrm{T^{3}}$ in the title and $\mathbf{T}^{3}$ in the body, with inconsistent superscript formatting.

## Nice-to-Haves

- A controlled causal experiment (e.g., artificially balancing prompt energy and showing improvement in isolation) would strengthen the claim that energy imbalance *causes* missing instances, rather than merely correlating with them.
- A detection-based metric (e.g., using an off-the-shelf object detector to count whether each prompted instance appears in the generated image) would more directly test the central claim about preventing missing instances than CLIP-Score on cropped regions.
- A limitations section discussing failure cases (highly overlapping sketch regions, very large numbers of instances, non-noun keywords) would improve completeness.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- *Missing comparison with Attend-and-Excite and BoxDiff* — The sentence at line 250 (truncated by parser) explicitly mentions comparing with Attend-and-Excite in the appendix. Since the appendix is stripped, this criticism cannot be verified from the visible text and relates to appendix content, per instructions.
- *User study details not in main text* — Details may exist in the stripped appendix (Section C and E are referenced). The criticism about insufficient reporting in the *main paper* is retained in weakened form under Major, but the strong claim that details are entirely absent is removed.
- *Figures not present / parser stripping* — This is a known parser artifact, not a paper flaw.
- *Claims about poor sketch-to-image methods in general* — These are framing, not methodological weaknesses.
- *Reproducibility concerns about undisclosed large artifacts* — The paper specifies all key hyperparameters (K, β, scheduler, steps, guidance scale, resolution, GPU) in Section 5.1.

## Novel Insights

The reviews collectively surface an interesting tension that the paper itself does not fully confront: the characteristics prominence module uses TopK indices from the value matrices to decide *which* instance tokens to amplify, and then applies amplification via spatial sketch masks — but if those sketch masks are not per-instance (i.e., if $\mathbf{u}_m^i$ is just the input sketch resampled), then the module amounts to "amplify spatial regions where any instance token appears." This would mean the module cannot distinguish between overlapping instances at the same spatial location, which is precisely the coupling problem it aims to solve. The key question — whether the module genuinely achieves instance-level differentiation or just broadly boosts attention to all sketched regions — depends entirely on the unclarified definition of $\mathbf{u}_m^i$. Neither reviewer nor the paper's own analysis resolves this, and it represents the single most important clarification the authors would need to provide.

## Suggestions

1. **Clarify $\mathbf{u}_m^i$ explicitly.** Define how per-instance spatial masks are derived from the single input sketch. If they are attention-map-based (from Dense Diffusion's approach), state this and provide the formula. If they are the input sketch downsampled per scale, state this and explain how the "per-instance" superscript is justified. Revise the notation if needed to avoid implying instance-level decomposition that does not exist.

2. **Expand and strengthen the quantitative evaluation.** Report results on standard multi-instance benchmarks adapted for sketch input. Provide confidence intervals or bootstrapped statistics. Include per-instance recall metrics (e.g., object-detection-based presence/absence). Compare against Attend-and-Excite and BoxDiff quantitatively. Report user study details (participant count, instructions, inter-rater agreement) either in main text or a properly referenced appendix section available for review.

3. **Provide a quantitative hyperparameter sensitivity analysis** across multiple prompts and instances, not a single qualitative example. Show how K and β affect instance recall and visual quality metrics systematically.

4. **Add a controlled experiment for the causal claim.** Artificially balance prompt energy in isolation (without other modules) and measure whether missing instances are recovered, to confirm that the energy imbalance is causal rather than correlational.

5. **Discuss failure modes.** Address when the prompt balance module might harm generation (compositional prompts, large instance counts) and when characteristics prominence might fail (highly overlapping sketch regions).

## Score and Decision

The paper identifies genuinely interesting and under-explored failure modes in cross-attention (energy imbalance, value homogeneity) and proposes a practical, training-free triplet of modules with plausible qualitative benefits. However, the core novel module (characteristics prominence) is underspecified to the point of unreproducibility — the origin of per-instance sketch masks $\mathbf{u}_m^i$ is never explained. The quantitative evaluation is also too weak to support the claimed improvements: 20 scenes, no statistical testing, tiny CLIP-Score margins, limited baselines. These are structural issues that prevent acceptance in the current form. The paper could be viable after major revisions that resolve the $\mathbf{u}_m^i$ ambiguity and substantially strengthen the evaluation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>