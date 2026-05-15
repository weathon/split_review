Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper proposes DROSIA, a time series forecasting method that decouples sequential information from individual patch representations. Instead of using self-attention (which mixes all points' information into each point's representation), DROSIA concatenates all patch embeddings, compresses them to a single global vector via an MLP, and concatenates this sequential representation back to each individual patch embedding, followed by LayerNorm and an FFN. This achieves O(CL+CH) complexity — linear in input length L, channels C, and horizon H. Experiments on 8 multivariate long-term forecasting benchmarks show DROSIA achieving competitive or best results against iTransformer, PatchTST, FEDformer, TimesNet, TiDE, DLinear, and FreTS, with extensive ablations validating the decoupled design.

## Strengths

- **Competitive performance with linear complexity on standard benchmarks**: Table 1 shows DROSIA achieves best or second-best MSE on 7 of 8 datasets compared against 7 strong baselines spanning Transformer, CNN, and MLP families. Table 3's complexity analysis shows DROSIA is O(CL+CH) — uniquely linear in input length, channels, and horizon among the compared methods — directly supporting the paper's core efficiency claim.

- **Controlled experiment showing channel-independent modeling can surpass channel-dependent models with sufficient temporal context**: Table 2 provides a clean comparison on ECL (321 channels) and Traffic (862 channels) with varying input lengths L∈{96,192,336,512}. When L≥192, DROSIA (which uses no inter-channel information) consistently outperforms iTransformer (which uses cross-channel attention) across all four horizons. This is a well-designed experiment that makes a non-obvious empirical point.

- **Thorough ablation suite validating the decoupled design**: Table 4 shows the P+S (patch + sequential) configuration significantly outperforms both P-only and S-only variants (e.g., Traffic H=96: 0.376 vs 0.443 vs 0.450). Table 5 tests five different extraction methods (MLP, Self-Attention, CNN, RNN, Max Pooling) and shows all work comparably on small-variate datasets, demonstrating DROSIA is robust to the choice of extractor. Figure 3 provides sensitivity analysis across patch size, dimension ratio, model dimension, and number of layers on four datasets of varying scale.

- **Consistent improvement with longer input sequences**: Figure 4 shows DROSIA's performance monotonically improves as input length increases on ETTm1, ECL, and Traffic, eventually surpassing both channel-independent (PatchTST, DLinear) and channel-dependent (iTransformer, TimesNet) baselines — supporting the claim of strong sequence modeling capability.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparisons to other linear-complexity sequence models**: The paper claims "state-of-the-art performance with linear complexity" but does not compare against other recent models that also achieve linear or sub-quadratic complexity — such as Mamba (state-space model), TSMixer, ModernTCN, or linear-attention Transformer variants (e.g., Performer). These are relevant baselines for substantiating the SOTA claim, especially since DROSIA's linear complexity is a highlighted advantage. While the chosen baselines (iTransformer, PatchTST, etc.) are strong and widely used, omitting these models means the SOTA claim is only validated within a restricted comparison set. This does not invalidate the paper's contribution (which is about the decoupling mechanism itself, not pure efficiency), but the SOTA claim should be qualified.

- **The MLP-based information extractor is underspecified for full reproducibility**: The paper describes the information extraction as "We employ a simple and efficient MLP" but omits: number of layers, hidden dimensions beyond what can be inferred from the 1:1 ratio, activation functions, dropout rates, and whether the MLP is shared across encoder layers or unique per layer. The FFN in Equation (7) is similarly unspecified. Given that the MLP is central to how sequential information is extracted from the concatenated patches, these details are needed for exact reproduction. The paper does specify model dimensions (d=256 or 512) and the 1:1 ratio (sequential info dimension = d/2), which provides partial constraints, but the full architecture is not pinned down.

### Minor

- **Novelty is modest**: The core operation — concatenating all patch embeddings → MLP compression to a global vector → concatenating back to each patch → LayerNorm → FFN — is a straightforward architectural choice. The paper acknowledges it "resembles residual connection" (line 71). The decoupling claim is meaningful (preserving original patch embeddings alongside sequential info is different from self-attention's weighted mixing), but the design's position relative to existing global-context approaches (Set Transformers, Perceiver, learnable global tokens) is not discussed. The sociological framing ("transverse interaction," "generalized other") adds no technical clarity and could be removed.

- **Table 4's ablation description is confusing**: The text describes comparing "P+S", "P", "S" for "both models" (DROSIA and PatchTST) but the description is ambiguous about how to read the results across the two architectures. It states "The 'P+S' configuration of PatchTST means the patch representations and sequential information extracted via Self-Attention are concatenated" — but since PatchTST's encoder is inherently self-attention, it's unclear what architectural change "P+S" entails for PatchTST vs. using a DROSIA-style encoder. The table only shows data for two datasets (ECL, Traffic) without clarifying which rows correspond to which model. This weakens the ablation's interpretability.

- **Figure 4 shows only H=96 without error bars**: The influence of input length is only plotted for a single horizon (H=96). The paper reports standard deviations elsewhere (e.g., "three trials" for Table 2) but Figure 4 shows no uncertainty estimates. The trend may not generalize to longer horizons.

- **The concatenation of all patch embeddings produces a very large MLP input**: For typical settings (L=512, stride=8 → 64 patches, d=512), the concatenated vector is 64×512=32,768 dimensions. The MLP first layer's weight matrix is therefore (32,768 × d/2) = ~8M parameters for a single projection. While this is still linear in L, the practical parameter cost is non-trivial and is not discussed as a trade-off.

### Trivial
- The sociological motivation (Section 1, "transverse interaction," "generalized other") is an unusual framing that does not aid technical understanding and could be removed without loss.
- The paper states "Our code will be made open-source in the subsequent version" — providing a preliminary code release or pseudo-code would improve reproducibility given the underspecified MLP details.

## Nice-to-Haves
- An ablation replacing DROSIA's concatenation+MLP with simpler global average pooling over patches + addition to each patch, to isolate whether the parameterized MLP compression is necessary or a trivial pooling suffices.
- Visualization or interpretation of the learned sequential information vector (e.g., does it capture global trend, periodicity, or something else?) to strengthen the decoupling narrative.
- A discussion of how the method relates to other global-context architectures (Set Transformers, Perceiver, etc.) to better contextualize novelty.

## Removed Points

These points were flagged for removal from the main review; they are listed here for completeness but should be treated with caution.

- **Criticism that DROSIA's decoupling claim "applies equally" to existing methods**: The critic claimed DROSIA "also injects global sequential info into each patch" just like self-attention. This misreads the paper: DROSIA preserves the original patch embedding intact and adds sequential info as an *additional* representation, whereas self-attention overwrites each point's representation via weighted averaging. The paper's claim of decoupling (keeping individual and sequential info separate) is technically correct.

- **Criticism about missing appendix/proofs**: The paper's appendix content is stripped by the parser; it likely exists in the original submission.

- **Pure formatting/style nitpicks**: Not present in the source material; parser artifacts are not author errors.

- **Strawman claim that the paper provides "no theoretical or empirical argument" for the design**: The paper provides empirical validation via Tables 4 and 5 (ablation of decoupled representations, comparison of five extraction methods), which directly test the design decisions.

- **Criticism that "The decoupling claim ... applies equally to DROSIA"**: As noted above, this misunderstands the paper's contribution.

- **Strength from Strength Finder about "flexible information extraction module" being a core strength**: While valid, this is more of a supporting point than a core strength. Moved here to avoid over-weighting.

## Novel Insights

The reviews converge on an interesting tension: DROSIA is a simple method that works well, but its very simplicity makes the novelty somewhat thin. The most striking empirical finding — that channel-independent DROSIA can surpass channel-dependent iTransformer on large-variate datasets when given enough temporal context (Table 2) — is actually the paper's strongest contribution, perhaps stronger than the specific architectural design itself. This finding challenges the recent trend toward cross-channel modeling (iTransformer, TimeXer) and suggests that temporal depth can compensate for the absence of inter-channel information, at least on these benchmarks. The reviews did not fully articulate this: the decoupling mechanism may matter less than the demonstration that strong intra-channel modeling can dominate cross-channel approaches when the input sequence is sufficiently long. This is a genuine insight worth emphasizing beyond the paper's own framing.

## Suggestions

1. **Add comparisons to at least one state-space model (e.g., Mamba) and one linear-attention Transformer** to substantiate the linear-complexity SOTA claim. If these baselines are unavailable due to computational constraints, clearly qualify the SOTA claim (e.g., "state-of-the-art among compared Transformer/MLP/CNN-based forecasters").

2. **Fully specify the MLP architecture** used for information extraction: number of layers, hidden dimensions, activation function, dropout, and whether parameters are shared across encoder layers. If space is constrained, provide a pseudo-code algorithm or release preliminary code.

3. **Clarify Table 4's presentation**: Show results for both DROSIA and PatchTST across P+S, P, S configurations in a clearer layout, or explain the experimental design more precisely in the caption. Report results consistently for all 8 datasets, not just 2.

4. **Add error bars to Figure 4** and show results for at least one additional horizon (e.g., H=336 or H=720) to improve generalizability of the input-length analysis.

5. **Tone down the "state-of-the-art" claim** to match the comparison set (e.g., "competitive or superior performance against strong Transformer, CNN, and MLP baselines with linear complexity") or expand the baselines to justify the broader claim.

## Score and Decision

**Originality**: The decoupled representation idea is simple but underexplored in time series forecasting — moderate originality.

**Importance of research question**: Efficient long-sequence modeling for time series is a practically important problem.

**Claims support**: The core claims (competitive accuracy with linear complexity) are well-supported by the experiments. The SOTA claim is somewhat overstated given the restricted baseline set.

**Soundness of experiments**: Experiments are extensive (8 datasets, 7 baselines, 4 horizons, multiple ablations). The controlled experiment in Table 2 is a highlight. Minor presentation issues (Table 4 clarity, Figure 4 error bars) do not undermine the overall soundness.

**Clarity of writing**: Generally clear, though the sociological framing in Section 1 is distracting and some methodological details are underspecified.

**Value to the community**: The paper demonstrates a useful alternative to self-attention for time series encoding and provides compelling evidence for the power of intra-channel modeling with sufficient temporal context. The simplicity of the method is a practical advantage.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>