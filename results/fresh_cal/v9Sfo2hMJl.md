Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes UniTS, a hybrid time series forecasting framework that combines a global feature extractor (a linear/MLP module with optional Transformer components) with a local feature extractor (multi-scale 1D CNNs), along with instance normalization and patching. Beyond the architecture, the paper makes an empirical contribution by systematically evaluating how the lookback window length affects model comparisons (running experiments under both fixed and finetuned lookback settings) and by conducting component-level ablations that isolate the contribution of attention, instance normalization, position encoding, and layer normalization in time series forecasting.

## Strengths

1. **Clean, component-level ablation of Transformer modules (Table 2, Section 4.4).** The paper directly adds attention, position encoding, and layer normalization to a linear baseline one at a time, measuring the performance impact on three datasets. The finding that adding attention layers consistently *degrades* performance while instance normalization is critical provides concrete, controlled evidence on a question that prior work (e.g., Li et al., 2023) addressed only indirectly by comparing whole architectures. This goes beyond claiming "Transformers don't help" to showing *which* components help and which hurt.

2. **Standardized evaluation with both fixed and finetuned lookback lengths (Section 4.1, Figure 2).** The paper identifies the inconsistent use of lookback windows across prior work as a source of unfair comparisons and runs experiments under both conventions. This methodological contribution is practically valuable — it reveals how the lookback length interacts with model rankings, a confound that is often ignored in the literature.

3. **Quantified ablation of the hybrid design (Section 4.5, Table 2).** The paper reports concrete numbers: removing the local feature extractor increases MSE by 2.19% and removing the global feature extractor increases MSE by 28.04%. Even though the LFE's contribution is modest, the comparison provides a clear picture of how much each module contributes, which is useful for practitioners.

4. **Broad baseline coverage.** The paper compares against 13 baselines spanning linear models (DLinear, RLinear/MLP), Transformers (PatchTST, FEDformer, Autoformer, SpaceTimeFormer), CNNs (MICN, TimesNet), RNNs (LSTNet), and MLP-based forecasting models (TiDE, N-BEATS, N-HiTS), providing a comprehensive view of relative performance.

## Weaknesses

### Fatal

None.

### Major

1. **The hybrid modeling contribution is weaker than the paper's framing suggests.** The ablation (Section 4.5, line 154) shows that removing the Local Feature Extractor (CNN branch) increases MSE by only **2.19%**, while removing the Global Feature Extractor (linear branch) increases MSE by **28.04%**. This means the model is overwhelmingly a global linear model (with instance normalization) receiving a tiny boost from the CNN adjunct. The paper's title, abstract, and contribution list emphasize "hybrid modeling" as the core innovation, but the evidence shows the hybrid design is not the primary driver of performance — the global linear mapping is. A 2.19% improvement is positive but does not warrant billing hybrid modeling as the central contribution. The paper would be better served by reframing its contributions around the standardization of lookback evaluation and component ablation.

### Minor

2. **The "rethinking" analysis in Section 4.4 partially replicates known findings.** The paper itself acknowledges (line 135) that Li et al. (2023) already demonstrated that the performance of PatchTST over DLinear is primarily attributable to instance normalization, not Transformer-specific mechanisms. The paper's own ablation (testing attention, PE, LN incrementally) is a more direct verification, but the core finding — that attention is not essential and IN is crucial — was already established. The framing as "rethinking" overstates the novelty of this particular result.

3. **Ambiguity in the SOTA evaluation protocol for setting (i).** The paper specifies (line 103) that for setting (i), "baseline results are collected by running experiments with six different lookback window lengths... The best results among these configurations are chosen as the performance metric." It then states (line 117) that results are for "all selected models with a finetuned lookback length." It does not explicitly state whether UniTS itself used the same best-of-six procedure or a different finetuning approach. While it is reasonable to assume UniTS underwent comparable tuning, the protocol should be stated symmetrically and unambiguously for all models including the proposed one. This is a clarity issue rather than a fatal flaw, as any asymmetry would likely favor baselines (which get to pick their best lookback), not UniTS.

4. **No statistical significance reported.** The paper reports single-run results without multiple seeds or confidence intervals. For a SOTA claim across 8 datasets and 13 baselines, the lack of any variance estimate makes it difficult to assess whether the reported improvements are statistically reliable. This is a standard expectation for empirical claims of this scale.

5. **The GFE architecture description is underspecified (Section 3.2.2).** The text describes a range of architectures from "a simple variant of the direct multi-step forecasting model" to "stacking multiple linear layers" to optionally adding "attention, position encoding, and layernorm mechanisms" to create "a comprehensive transformer layer." The reader cannot determine which specific configuration was used in the final UniTS model whose results appear in Table 1. The ablation in Table 2 clarifies some variants, but the default GFE used for the main SOTA results is never pinned down.

### Trivial

6. **ETTh1/ETTh2 mismatch.** Figure 2's caption (line 110) states the results are on ETTh1, while the text (line 128) says the figure illustrates results on ETTh2. The authors should verify which dataset was used.

## Nice-to-Haves

- **Test the hybrid model against its individual components as a function of lookback length.** The paper motivates hybrid modeling by claiming CNNs excel at short lookbacks while global models excel at long lookbacks, but never directly tests whether the hybrid model outperforms both pure alternatives across the lookback spectrum. An experiment varying lookback length and comparing UniTS, a GFE-only variant, and an LFE-only variant would directly validate the motivation.
- **The hyperparameter search experiment (Table 3)** is generic (Bayesian search not reaching grid-search optimum is a well-known phenomenon) and does not connect to any time-series-specific property. Consider replacing this with a more targeted analysis of how lookback length specifically interacts with model performance across architectures.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Table images are illegible / results cannot be evaluated"** — The embedded images are a PDF-extraction artifact; the original submission contains proper tables. This is a parser issue, not an author error.
- **"The paper does not test whether hybrid modeling closes the gap across lookback lengths"** — Scope creep. The paper's hybrid model evaluation is done at the aggregate level, and testing at every lookback length is a nice-to-have, not a required experiment.
- **"Hyperparameter search is generic and not connected to time series"** — Overstated. The experiment does demonstrate the practical point that hyperparameter choice matters for forecasting models, which is relevant even if not uniquely tied to time series properties.
- **Speculative claims about evaluation unfairness** — The protocol description, while ambiguous, describes baseline results being obtained under the same best-of-six procedure implied for all models. The concern that something is "biased against baselines" is not supported by the text.
- **Missing related work** — I cannot independently verify the existence or absence of relevant work.

## Novel Insights

The most interesting observation that emerges across the reviews is that the paper's own evidence undermines its headline claim: the hybrid model is, in practice, a well-tuned global linear model with a 2%-level CNN refinement. This creates a productive tension — the paper's *method* is less novel than claimed, but its *empirical findings* (that lookback standardization substantially changes model rankings, that attention is actively harmful, that IN is the real driver) are arguably more valuable. The disconnect between the paper's framing and its actual evidence is itself an insight worth noting: the community may be overvaluing architectural hybridity when the real gains come from evaluation standardization and careful hyperparameter selection.

## Suggestions

1. **Reframe the paper.** Move the emphasis from "hybrid modeling" as the core contribution to "systematic re-evaluation of temporal modeling assumptions with a proposed strong baseline." The standardized lookback evaluation and component ablation are the paper's strongest points.
2. **Clarify the evaluation protocol.** Explicitly state in Section 4.1 that UniTS also used the best-of-six lookback procedure, or if it used a different protocol, specify exactly what was done.
3. **Pin down the GFE architecture.** State clearly which GFE variant (single linear layer per patch, stacked linear layers, or one with attention/PE/LN) was used for the main SOTA results in Table 1.
4. **Add statistical significance.** Run at least 3 seeds for the main results (Table 1) and report mean ± std.
5. **Fix the ETTh1/ETTh2 mismatch** in Figure 2 caption vs. text.

## Score and Decision

The paper makes useful empirical contributions — standardized lookback evaluation and clean component ablation — that are worth preserving. However, the core claimed innovation (hybrid modeling) is only weakly supported (2.19% gain from the CNN branch), and the "rethinking" findings partially replicate prior work. The paper's framing overstates its novelty relative to what the evidence supports. With a major reframing and improved clarity in evaluation protocols, this paper could be suitable for a venues that value careful empirical analysis. In its current form, the gap between the claims and the evidence is too large.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>