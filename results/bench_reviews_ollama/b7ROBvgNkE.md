Now I have a thorough understanding of the paper. Let me now synthesize the final review, carefully verifying each claim from the harsh reviewer against the actual paper text.

**Examining the harsh reviewer's critical issues:**

1. **Inference procedure**: The paper's prediction mechanism is $g(\sum_k t_{i,k} \mathbf{p}_k)$ (Eq. 11, line 154), which uses the transport matrix T. The paper never explicitly discusses how inference (test time) works. The transport matrix depends on the mini-batch composition. This is a valid concern — not a fatal one necessarily, but a genuine gap in the method description.

2. **"Applicable to any deep recommendation model"**: The paper uses this language in the abstract, introduction, and conclusion. Experiments only use MLP. However, the paper's Section 5.1 states "Since all methods are model-agnostic, we implement them on the MLP" — so this is a deliberate choice since the methods being compared are model-agnostic. The claim of universal applicability is based on the method design (it regularizes training but doesn't modify the backbone architecture), but it's unverified by experiments.

3. **No variance/confidence intervals**: True — no standard deviations or significance tests are reported. This is standard to request.

4. **"Instance representation confusion" unsubstantiated**: The paper relies on Fig. 1(b) t-SNE visualization. No quantitative measure is provided. This is a valid concern.

5. **Data split 6:2:2.5**: This does sum to 10.5, which is odd. But this is a minor/typo concern.

6. **Near-Gaussian claim**: The preprocessing section (line 88) does claim sampling L distributions "transforms the original one-dimensional multimodal distributions into D*L one-dimensional near-Gaussian distributions w of length n." This is indeed a confusing/unjustified claim — sampling from a multimodal distribution gives you samples from that multimodal distribution, not near-Gaussian distributions. This appears to be a conceptual error or very poorly described.

7. **Prototype drift with W_p**: Valid concern. When W_p is learned freely, the projected prototypes P can drift away from the HVQ-VAE codebook, diluting the "credibility" claim. However, there's a partial counterargument: the assign loss and compact loss still anchor instances to the projected prototypes, and the task loss ensures the prototypes remain predictive.

8. **S_k+ thresholding**: Line 142 — the threshold is based on average transport values. This is somewhat ad hoc but is a design choice, not necessarily wrong.

9. **Missing SWAT comparison**: SWAT is discussed in related work but not compared in experiments. Valid but not a fatal concern.

10. **KMeans ablation fairness**: The KMeans in Table 3 could be unfair if it doesn't get the same W_p projection. The paper doesn't specify this detail.

Let me now write the consolidated review.</think>Now I have read the full paper. Let me synthesize the final review by carefully verifying each reviewer claim.

## Summary

ProWTP is a two-stage method for video watch-time prediction that (1) generates credible prototypes from watch-ratio label distributions using a Hierarchical VQ-VAE (HVQ-VAE), and (2) aligns instance representations with these prototypes via Semi-relaxed Unbalanced Optimal Transport (SUOT), supplemented by assignment and compactness losses. The key insight is that watch-ratio distributions within video duration buckets are multimodal, and prototypes derived from these label distributions — rather than from model representations — provide better calibration references for the recommendation model.

## Strengths

- **Label-derived prototypes outperform representation-derived ones.** Table 3 shows that HVQ-VAE prototypes consistently outperform KMeans (which clusters instance representations) and random initialization on both datasets and all metrics, supporting the core claim that prototypes grounded in label distributions are more credible calibration references than those derived from noisy model representations.

- **SUOT formulation is well-motivated and empirically validated for the mini-batch setting.** Standard OT enforces strict marginal constraints on prototypes, which is unreasonable when not all prototypes have corresponding instances in a mini-batch. Table 4 confirms that SUOT outperforms both standard OT and UOT on both datasets, validating the semi-relaxation design.

- **Comprehensive ablation studies validate component contributions.** Table 2 systematically removes HVQ-VAE, assign loss, compact loss, and SUOT, showing consistent degradation. Tables 3–4 separately validate prototype generation and alignment strategy choices. Figure 3 examines prototype count sensitivity.

- **The observation that watch-ratio distributions within duration buckets are multimodal (Fig. 1a) is a novel and empirically grounded insight** for the WTP literature that directly motivates the discrete prototype approach.

## Weaknesses

### Fatal
None.

### Major

- **The inference procedure is unspecified.** The task loss (Eq. 11, line 154) defines prediction as $g(\sum_k t_{i,k} \mathbf{p}_k)$, where the transport matrix **T** depends on the mini-batch composition. At inference time, how is the transport plan obtained? If OT is recomputed per test batch, a single sample's prediction would depend on whatever else happens to be in its batch, which is a substantial pragmatic and theoretical concern. If OT is bypassed at inference and $f(x)$ is fed directly to $g$, the training-inference mismatch and its implications must be analyzed. The paper does not address this, leaving a gap in the method's specification that is central to deployability. (Lines 154–157 define training prediction only; no inference procedure is described anywhere in the paper.)

- **The "near-Gaussian" claim in the pre-processing step is unjustified and conceptually suspect.** Line 88 states: "we first sample $L$ one-dimensional distributions $\mathbf{w}=(y_1,...,y_n)$ from each multimodal distribution. Using this sampling strategy, we transform the original one-dimensional multimodal distributions into $D*L$ one-dimensional near-Gaussian distributions $\mathbf{w}$ of length $n$." Sampling from a multimodal distribution yields samples *from that multimodal distribution*, not "near-Gaussian distributions" — unless by "sample L distributions" the authors mean something fundamentally different from what is written. This is either a conceptual error or severely underspecified, and it affects the validity of the HVQ-VAE input pipeline.

- **The core motivation — "instance representation confusion" — is not quantitatively established or validated.** The paper's primary motivation (lines 15, 119) is that models suffer from instance representation confusion, supported only by a qualitative t-SNE visualization in Fig. 1(b). There is no quantitative measure (e.g., cluster purity, silhouette score) before and after applying ProWTP to demonstrate that the diagnosed problem exists and that the method actually resolves it. Without this, the causal story from problem → solution is incomplete.

### Minor

- **The "applicable to any deep recommendation model" claim is overclaimed relative to evidence.** All experiments use only MLP as the backbone (line 168: "Since all methods are model-agnostic, we implement them on the MLP"). While the method's design is architecturally agnostic (it regularizes training without modifying the backbone), this claim is not experimentally validated on structurally different backbones (e.g., transformer-based or feature-interaction models). The claim in the abstract, introduction, and conclusion should be softened to match the evidence.

- **Prototype drift under learnable $\mathbf{W}_p$ is not analyzed.** The prototypes $\mathcal{P}$ from HVQ-VAE are projected through a learnable linear transformation $\mathbf{W}_p$ before alignment (line 121). Once $\mathbf{W}_p$ is freely optimized during stage 2, the projected prototypes can drift away from the original HVQ-VAE codebook, potentially diluting the "credibility" inherited from label distributions. The paper does not discuss or analyze this.

- **No variance or significance tests are reported.** Tables 1–4 report single numbers without standard deviations across runs, making it impossible to assess whether the improvements (some modest, e.g., ~0.001–0.01 on MAE) are statistically meaningful.

- **The data split ratio of 6:2:2.5 sums to 10.5** (line 166), which is internally inconsistent. This is likely a typo but should be clarified.

### Trivial
- The $S_k^+$ thresholding mechanism (line 142), which defines instances associated with a prototype via average transport value, is somewhat ad hoc, but this is a minor design choice rather than a fundamental issue.

## Nice-to-Haves

- Experiments on at least one non-MLP backbone (e.g., DeepFM, DCN) would substantiate the universality claim.
- Comparison with SWAT, which is cited in related work, would strengthen the empirical contribution.
- A visualization of the representation space *after* ProWTP training (corresponding to the "before" in Fig. 1b), ideally with quantitative cluster metrics, would directly validate the claimed mechanism of reducing representation confusion.
- Analysis of prototype alignment before and after $\mathbf{W}_p$ training to assess whether "credibility" from label distributions is preserved.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The Wechat dataset has no citation, size statistics, or access information, making reproducibility unlikely"** — The Wechat dataset is described as "public" (line 166) and cited as "collected from Wechat App" with a reference to (Gao et al., 2022) for Kuairand. While the Wechat citation is less detailed, this is a reproducibility nitpick about dataset availability — the paper cites it as public, which should be taken at face value per our rules.

- **"Missing comparison with SWAT" as a fatal/major weakness** — SWAT is mentioned in related work but is a different paradigm. The baseline comparison covers the established model-agnostic WTP methods. This is a nice-to-have suggestion, not a major weakness.

- **"The Kmeans ablation may be unfair if not given the same W_p projection"** — This is speculative; the paper doesn't specify either way, and KMeans prototypes could plausibly also be projected. This is a minor ambiguity rather than a demonstrated unfairness.

- **"The claim to be 'the first' to investigate multimodal distribution properties" without acknowledging prior bucketing work** — The paper's "first" claim is about explicitly modeling multimodal watch-ratio distributions via VQ-VAE, which is distinct from duration bucketing in D2Q/SWAT. This is a reasonable novelty claim; whether prior work "implicitly" captures this is a judgment call, not a factual error.

- **Formatting/typo criticisms** — The 6:2:2.5 data split ratio sums to 10.5, which is a genuine ambiguity/typo (kept above as minor). Other formatting complaints from the harsh reviewer about parser artifacts are removed per rules.

- **"The 'Since all methods are model-agnostic' statement in Section 5.1 is unfair comparison"** — The reviewer noted this, but this design choice ensures fair comparison by using the same backbone for all methods, which actually favors the baselines equally. This is not an unfairness issue.

## Novel Insights

The paper's most interesting tension is between "credible prototypes" and the learnable $\mathbf{W}_p$ projection. The entire premise is that prototypes derived from label distributions are more trustworthy than those from model representations — yet the linear transformation $\mathbf{W}_p$ can freely reshape these prototypes during training, potentially severing the connection to the original label distribution structure. The paper does not analyze whether the learned $\mathbf{W}_p$ preserves the semantic properties of the HVQ-VAE codebook, creating an internal inconsistency in the method's narrative: the very "credibility" that motivates the approach could be eroded by the optimization it enables.

## Suggestions

- Explicitly describe the inference pipeline: state whether SUOT is recomputed at test time, and if so, how batch composition effects are handled; if not, analyze the train-test mismatch.
- Add quantitative measures of representation confusion before/after ProWTP (e.g., silhouette score, within-cluster variance) to close the evidentiary gap around the method's core motivation.
- Clarify or correct the "near-Gaussian distributions" claim in the pre-processing step (line 88) — either explain what is meant or remove the claim.

## Evaluation

**Originality:** The idea of deriving calibration prototypes from label distributions rather than model representations, combined with SUOT alignment, is a creative and relatively novel framing for WTP. The multimodal watch-ratio observation is a genuine empirical contribution. However, the unexplained "near-Gaussian" claim and the unvalidated universality claim temper the originality.

**Importance of research question:** Video watch-time prediction is an important practical problem in industrial recommendation systems.

**Claims well supported:** The inference procedure gap and the unvalidated "representation confusion" diagnosis weaken the support for core claims. The ablation evidence for individual components (Tables 2–4) is solid and well-structured.

**Soundness of experiments:** Experiments cover two industrial datasets with appropriate metrics, but lack significance testing and are limited to a single backbone architecture. The data split ratio inconsistency (6:2:2.5 = 10.5) is a minor blemish.

**Clarity of writing:** The paper is generally readable but the pre-processing description (Section 4.2) is confusing, and the inference procedure is entirely omitted.

**Value to the community:** The label-derived prototype idea and SUOT alignment are conceptually valuable contributions that could inspire follow-up work, but the method description needs significant clarification.

## Score and Decision

The paper makes a creative contribution with a well-designed ablation structure, but has two major weaknesses: (1) the inference procedure is unspecified — a central aspect of method completeness — and (2) the "near-Gaussian" preprocessing claim is unjustified and potentially a conceptual error. The overclaimed universality and unvalidated core motivation further weaken it. These are addressable in revision but serious enough to prevent acceptance in current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>