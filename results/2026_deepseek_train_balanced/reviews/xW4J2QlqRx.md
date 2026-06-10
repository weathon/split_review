Now let me compose the final review.

## Summary

The paper introduces ContextFormer, a plug-and-play framework that augments existing pre-trained time series forecasting models (PatchTST, iTransformer) with multimodal contextual metadata (categorical, continuous, time-varying) via cross-attention-based fusion with a frozen base model and zero-initialized new components. The approach is motivated by theoretical analysis showing that adding context reduces forecast uncertainty (mutual information) and that, for a linear autoregressive model, context-aware regression is guaranteed to match the base model's error.

## Strengths

- **Well-motivated practical problem.** Integrating heterogeneous metadata (categorical, continuous, time-varying) into existing SOTA forecasters is a genuine gap. The paper correctly identifies that current foundation models ignore metadata entirely and that simple linear covariate regression (as in TiDE) may be insufficient for complex multimodal metadata. This framing is clear and practically relevant.

- **Plug-and-play fine-tuning with frozen base model is a clean design choice.** Freezing the pre-trained base model and adding zero-initialized lightweight components (Section 5.2) is architecturally distinct from prior context-aware models that require joint training from scratch. This enables any pre-trained forecaster to be augmented without altering its learned time-series representations. The zero-initialization strategy that preserves base-model performance at initialization is well-motivated by the AR residual-regression analysis (Section 4.2).

- **Consistent improvements across diverse domains and two base architectures.** The experimental results (Tables 1, 2) show that ContextFormer-enhanced models "consistently surpass their context-agnostic counterparts across all rows and evaluation metrics" and outperform context-aware baselines (TiDE, TimeXer) in the majority of experiments. The evaluation spans six real-world datasets (traffic, energy, environment, retail, finance) using two structurally distinct transformer-based architectures (PatchTST, iTransformer), demonstrating generalization across model families and application domains.

- **Structured heterogeneous metadata encoding.** The metadata embedding module (Section 5.1) uses separate encoders for categorical and continuous features before fusing them through a transformer network, which directly addresses the "diversity within datasets" challenge identified in the introduction.

## Weaknesses

### Fatal

None.

### Major

1. **Overclaimed "guarantee" does not hold for the deep learning setting.** The paper states in Section 5.2: *"The fine-tuned model is guaranteed to perform at least as well as the context-agnostic base model, provided the test distribution matches the training distribution."* This guarantee is proven only for the linear autoregressive case (Section 4.2, Eq. 112–127), where a convex least-squares problem has a closed-form solution. The actual ContextFormer uses cross-attention layers, transformer encoders, and non-convex optimization via gradient descent. Zero-initializing weights at the start of training does **not** guarantee that training will not increase the loss — overfitting to noisy metadata, optimization instability, or distribution shift can all push the model to a worse solution. The paper offers no analysis of when degradation might occur. The claim is stated without qualification, creating a misleading impression of theoretical rigor. This does not invalidate the empirical results, but the central advertised advantage of the fine-tuning strategy (bullet 1 vs. training from scratch) rests on this unsupported guarantee.

2. **No ablation study, missing critical baseline.** The paper never tests the most natural baseline: **concatenating metadata features directly as additional input channels** to PatchTST or iTransformer. Without this, it is impossible to tell whether the improvements come from the proposed cross-attention architecture or simply from the availability of metadata. Similarly, there are no ablations isolating:
   - The contribution of cross-attention vs. simpler fusion (concatenation, gating, MLP)
   - The contribution of temporal embeddings vs. metadata embeddings
   - Zero initialization vs. random initialization
   - Frozen vs. unfrozen base model
   
   A method paper whose central claim is that its specific architectural choices matter must demonstrate this through controlled ablation. The paper does not.

3. **Textual metadata capability is claimed but never evaluated.** The abstract states ContextFormer handles *"categorical, continuous, time-varying, and even textual information."* Figure 1 prominently features news articles and tweets. The contributions list includes textual metadata. Yet **none of the six experimental datasets involve text** — the metadata is categorical (e.g., wind direction, location) or continuous (e.g., oil price, search trends). There is no toy example, no case study, no experiment with actual text. This claimed capability is entirely unvalidated.

4. **Unsupported claim about foundation model outperformance.** The conclusion (Section 7) states ContextFormer *"consistently outperform[s] baseline models and even forecasting foundation models."* The paper mentions foundation models (Chronos, TimesFM, Lag-Llama, Time-LLM) in the related work but never benchmarks against any of them. The experimental comparisons are limited to PatchTST, iTransformer, TiDE, and TimeXer — none of which are foundation models. This claim is unsupported and should be removed.

### Minor

1. **Cross-attention mechanism is under-described.** The core architectural innovation is described in one sentence: *"The cross-attention layers are transformer blocks that use the hidden state representations of the historical time series, along with either the temporal or metadata embeddings, to extract relevant contextual information for forecasting."* It is unclear (a) at which layer(s) in the base model the hidden state is extracted, (b) whether the cross-attention output **replaces, is added to, or is concatenated** with the base model's representations and how it is fed back, (c) the number of cross-attention layers, heads, and key/query/value dimensions, and (d) whether the same mechanism applies to PatchTST (patch-based tokens) and iTransformer (inverted-dimension tokens) which have fundamentally different internal representations. Figure 5 shows the architecture schematically but the text lacks a concrete forward-pass description. While dimensional details may be in the appendix (Tables 8, 9), the integration mechanism itself needs to be stated explicitly in the main text.

2. **No error bars or statistical significance.** No standard deviations, confidence intervals, or multiple-seed results are reported anywhere. It is impossible to assess whether the reported improvements (including the headline "up to 30%") are consistent across runs or within the noise of training.

3. **Limited evaluation scope.** Only two forecast horizons (48, 96) with a fixed lookback (96) are tested. It is unclear whether results hold for shorter horizons or different lookback lengths. The synthetic experiment uses true ARMA generating coefficients as metadata (an oracle-level signal), which is an unrealistically favorable setting — this is a preliminary experiment but its relationship to real-world utility is unclear.

### Trivial

- None.

## Nice-to-Haves

- **Test on a text dataset.** If the paper claims textual capability, at minimum one experiment with actual text data (e.g., news headlines + stock prices, or social media sentiment) should be included.
- **Add the metadata-as-input-features baseline.** This is the simplest possible context-aware baseline and is essential for attributing improvements to the proposed architecture.
- **Benchmark against TFT (Lim et al., 2021),** which is a well-known model designed specifically for incorporating covariates and static metadata. It is mentioned in related work but never compared against.
- **Report results with confidence intervals or across multiple seeds** to establish statistical significance.

## Removed Points

The following points from the input reviews were removed after verification:

- *"The method is critically underspecified / not reproducible from the paper alone"* (stated as a structural flaw by the harsh critic) → Downgraded from Major to Minor. The main text gives a high-level description; dimensional details are referenced to the appendix (Tables 8, 9) which exists in the original submission. The integration mechanism itself still needs clearer specification.
- *"The AR argument proves a trivial point that does not need experimental validation"* → Removed. Demonstrating the theoretical motivation experimentally is standard practice and not a weakness.
- *"The mutual information argument does not specifically motivate cross-attention"* → Removed. The MI argument motivates context-awareness generally; the paper uses cross-attention as the specific implementation. Scope-mismatch criticisms of theoretical motivation sections are not substantive weaknesses.
- *"Challenge 1 (lack of multimodal foundation models) is not addressed since the metadata encoder is trained from scratch"* → Removed. The paper explicitly states that foundation models are unavailable and proposes training lightweight per-dataset encoders as a practical alternative. Criticizing the paper for not solving a problem it explicitly identifies as unsolved is scope creep.
- *"The temporal embedding adds parametric complexity with no analysis"* → Removed. This is speculative — the paper could not reasonably include analysis of every possible impact of every component.
- *"The related work section is an undifferentiated list"* → Removed. The related work is appropriately organized by categories and covers the relevant literature. This is a subjective stylistic preference.
- *"TiDE/TimeXer comparison may be apples-to-oranges"* → Weakened. The paper's table caption states ContextFormer outperforms these baselines in the "majority of experiments." While it would be good to clarify whether these baselines received the same metadata, this does not rise to a major weakness since the primary comparison (ContextFormer vs. the base model) is clean.
- *"The guarantee claim is structurally invalid / the paper should not be accepted as-is"* → Downgraded from "structurally fatal" to Major. The empirical results are independent of the guarantee claim; the paper could drop the guarantee language and the rest would still stand. The claim is overblown but not paper-invalidating.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the linear-AR theoretical guarantee and the deep learning implementation, and the lack of ablations, but these are standard verification findings rather than novel cross-reviewer synthesis.

## Suggestions

1. **Soften or remove the guarantee claim.** Replace "guaranteed" with an empirical statement ("in our experiments, we observed that ContextFormer never degraded performance...") or discuss conditions under which degradation could occur (e.g., noisy/irrelevant metadata, distribution shift).
2. **Add at minimum one ablation study** comparing ContextFormer's cross-attention fusion against simple metadata concatenation as additional input channels. This is the most critical missing experiment.
3. **Remove the textual metadata claim** from the abstract and contributions, or include an experiment with actual text data.
4. **Remove the foundation model outperformance claim** from the conclusion, or benchmark against at least one foundation model (Chronos, TimesFM).
5. **Clarify the cross-attention integration mechanism** in the main text: specify the hidden-state extraction point, how the attention output is merged with the base model's forward pass, and the architectural dimensions (layers, heads).

## Score and Decision

The paper addresses a practically important problem and the plug-and-play design with frozen base model is a sensible contribution. The empirical results show consistent improvements across multiple domains. However, the paper is held back by four major issues: (1) an overclaimed theoretical guarantee that does not actually hold for the deep learning method presented, (2) a complete absence of ablation studies that would attribute improvements to the architecture rather than metadata availability, (3) an untested claim about textual metadata that is central to the paper's framing, and (4) an unsupported conclusion about outperforming foundation models. These are not minor gaps — the evaluation does not convincingly distinguish the contribution of the proposed architecture from much simpler alternatives. The paper requires substantial revision before it meets the standards of a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>