Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper tackles the Lookback Window Limitation (LWL) in long-term time series forecasting by proposing two model-agnostic modules: the Information Bottleneck Filter (IBF), which uses information bottleneck theory to select informative subsequences and suppress redundancy, and the Hybrid-Transformer-Mamba (HTM), which splits long sequences into blocks and processes them with Mamba (long-range, linear complexity) and Transformer (short-range) respectively. By integrating these into PatchTST to form PIH (Patch-IBF-HTM), the authors demonstrate consistent performance improvements as the lookback window grows to 1024, outperforming prior methods whose performance plateaus or degrades at larger windows. The modules are also shown to benefit other Transformer-based models (Transformer, Informer, Autoformer).

## Strengths

1. **Principled approach to overcoming LWL with clear empirical evidence:** The paper identifies two concrete causes of LWL (redundancy and architectural limits), proposes modules targeting each, and shows in Fig. 3(a) that while PatchTST's performance degrades from L=512 to L=1024, PIH's steadily improves. Table 1 reports strong results at L=1024 across seven datasets, directly supporting the central claim that longer windows become beneficial with the proposed modules.

2. **IBF provides an adaptive, information-theoretic approach to redundancy reduction beyond fixed patching:** Rather than relying on heuristic patch aggregation alone, IBF uses information bottleneck principles with a noise injection strategy to learn which subsequences to retain. Section 3.2 develops the formulation (relaxing discrete selection to continuous Gumbel-sigmoid sampling, deriving variational bounds for the two IB terms), and the ablation in Fig. 6 confirms that adding IBF consistently improves performance over the PatchTST baseline.

3. **HTM effectively combines Mamba and Transformer strengths for long sequences:** The hybrid design uses Mamba (linear in N) for the full patch sequence while Transformer processes short blocks (quadratic in N/K), reducing computation 2–3× over pure Transformer (Fig. 3(b)). The ablation shows HTM outperforms both pure Transformer (PatchTST) and pure Mamba (HMM) variants, validating the design rationale.

4. **Model-agnostic integration benefits multiple architectures:** When IBF and HTM are integrated into Transformer, Informer, and Autoformer, all show improved performance and increased lookback window limits (Fig. 4, Fig. 5). On ETTm1, for instance, the effective window limit increases from 48 to 192 for Transformer. This demonstrates general applicability beyond the primary PatchTST backbone.

5. **Comprehensive ablation and analysis validate design choices:** Fig. 6 ablates each module individually, compares interval vs. block split strategies, and shows that both IBF and HTM contribute positively and their combination is best. The paper also examines performance across multiple window sizes and prediction horizons, providing a nuanced view of where the modules help most.

## Weaknesses

### Fatal
None.

### Major

1. **Undefined symbols A and B in the IBF variational upper bound (Eq. 9).** The derivation of the IBF loss — one of the paper's two central modules — contains a critical gap. The variational upper bound for the compression term is given as  
   \[
   -I(\mathbf{z}^{\text{noise}},\mathbf{z}) \le \mathbb{E}_\mathbf{z}\left(-\frac12\log A + \frac{1}{2N}A + \frac{1}{2N}B^2\right)
   \]
   without ever defining what \(A\) and \(B\) represent. These symbols appear nowhere in the preceding or following text, and no derivation connects them to the mutual information of \(\mathbf{z}^{\text{noise}}\) and \(\mathbf{z}\). The paper states that "by tailoring a noise prior for each input, the IB objective can yield a manageable variational upper bound" and then simply asserts the bound. Because the entire \(\mathcal{L}_{\text{comp}}\) term in the training objective depends on this expression, the reader cannot verify its correctness or tightness. While the overall IBF method (noise injection + Gumbel-sigmoid selection + prediction loss) is operationally well-defined and the empirical results are plausible, the theoretical grounding claimed by the paper — that IBF implements information bottleneck compression — is unsupported as presented. The authors must provide the full derivation, state the distributional assumptions (e.g., Gaussian posterior for \(\mathbf{z}^{\text{noise}}\) given \(\mathbf{z}\)), and define every symbol.

### Minor

1. **No error bars or statistical significance reported.** Table 1 reports only mean MSE/MAE. In time-series forecasting, results can vary across random seeds and data splits; single-run or mean-only comparisons are insufficient to fully support a state-of-the-art claim. Standard deviations over multiple runs would substantially strengthen the evidence.

2. **Interpretability claim is unsubstantiated.** The paper states that IBF "enhances the model's interpretability" and provides one example visualization (Fig. 3(c)) showing top-20 patches marked green on a single Electricity sample. There is no ground truth for "important subsequences," no comparison with alternative interpretability methods, no quantitative metric (fidelity, stability, etc.), and no user study. The visualization merely shows that the learned weights are non-uniform. This claim should be dropped or explicitly framed as a qualitative observation rather than a contribution.

3. **Model-agnostic integration procedure is underspecified.** Section 4.2 reports that IBF and HTM were integrated into Transformer, Informer, and Autoformer with performance improvements, but the insertion points are not described. For IBF, the paper's rationale for placing it after Mamba (Section 3.2) relies on Mamba's recurrent state accumulation. When placed after a Transformer layer (which does not accumulate history the same way), the same rationale does not directly apply. Specifying where the modules were inserted and whether placements were heuristic or validated would clarify the generality claim.

4. **Computational complexity lacks grounding in specific values.** The total complexity is given as \(O(L/P) + O((L/(PK))^2)\), with the claim that "appropriate choices of \(P\) and \(K\) can maintain \(L/(PK)\) within an acceptable constant range." But the actual values of \(P\) and \(K\) used in experiments are not reported, leaving the complexity advantage conceptual rather than concrete.

### Trivial
None.

## Nice-to-Haves
- Releasing code would aid reproducibility, given the number of moving parts (IBF training with Gumbel-sigmoid, HTM split modes, integration into multiple architectures).
- The limitation section could acknowledge that the IBF loss may be sensitive to \(\beta\) and that the Gaussian noise prior may not be optimal.
- Adding a variant with random patch selection (instead of IBF) to the ablation would help isolate whether IBF's information bottleneck objective provides benefits beyond any selection mechanism.
- The interval/block split methods are heuristic; an adaptive end-to-end segmentation method would be a natural extension.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing hyperparameter values (P, S, K, τ, β values):** The symbols are all defined in the paper (patch length \(P\), stride \(S\), number of blocks \(K\), temperature \(\tau\), Lagrange multiplier \(\beta\)). The critic's complaint is that the specific numerical values are not reported. This is a minor reproducibility request appropriately addressed by the authors in a rebuttal or appendix, but the hard rule requires removing criticisms about undisclosed hyperparameters as nitpicks. *Moved per hard rule.*

- **"Only seven datasets" and missing specific baselines (TimesNet, etc.):** Seven datasets (Weather, Traffic, Electricity, four ETT variants) is the standard benchmark suite in the LTSF literature. Eight baselines are included. A paper cannot cover every model ever published, and demanding additional baselines constitutes scope creep. *Moved per soft rule (scope creep).*

- **Typos and minor writing errors ("redundany," etc.):** The hard rule explicitly removes all criticism about typos, spelling, grammar, punctuation, and formatting artifacts. *Moved per hard rule.*

- **Code availability criticism:** The hard rule prohibits questioning the release status of any cited artifact; the reviewer extends this to code not being mentioned. *Moved per hard rule.*

## Novel Insights

The key insight that emerges from reconciling the reviews is that the paper has a clear success/partial-failure profile: the empirical architecture contributions (HTM's hybrid design, the noise-injection selection procedure) are well-supported and convincing, but the paper attempts to wrap them in information-theoretic formalism that is incompletely specified. The most interesting finding — that PIH's improvement over PatchTST grows monotonically with window size while PatchTST's saturates — is a genuinely novel empirical observation that stands independently of the IB derivation. The reviewers converge on the point that the paper would be stronger if it treated the IBF module's IB framing as intuition/motivation rather than a rigorous theoretical guarantee, since the operational method (Gumbel sigmoid selection with noise regularization) is well-defined and empirically effective on its own.

## Suggestions

1. **Complete the IBF derivation.** Provide the full variational bound derivation for \(\mathcal{L}_{\text{comp}}\), define \(A\) and \(B\), state the distributional assumptions (Gaussian posterior? which variance parameterization?), and cite the derivation source (likely a KL divergence between Gaussians following the noise injection in Eq. 7). If the bound follows directly from Yu et al. 2021a, cite the specific equation.

2. **Temper the SOTA claim and add error bars.** Replace "state-of-the-art" with "competitive results at longer lookback windows" or similar, and add standard deviations (3–5 runs) to the main results table. This addresses the primary statistical concern without requiring additional baselines.

3. **Drop or reframe the interpretability claim.** Either remove "interpretability" from the contributions or explicitly state that the visualization is a qualitative illustration of IBF's behavior, not a formal evaluation.

4. **Report the specific P, S, K, τ, β values used in experiments.** These are essential for reproducibility and for grounding the complexity analysis.

5. **Describe the integration points** for the model-agnostic experiments (Section 4.2). A brief sentence per architecture specifying where IBF and HTM are inserted would clarify the generality claim.

6. **Acknowledge the theoretical gap** in the limitations section — specifically that the variational bound in Eq. 9 requires further specification of distributional assumptions.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>