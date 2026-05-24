## Summary

This paper argues that time series forecasting has plateaued because standard models ignore external influences ("self-stimulation"). The authors provide a control-theoretic analysis proving that ignoring influences imposes an irreducible error bound, introduce a new paradigm (IATSF) that explicitly models textual influences, present a leak-free benchmark with temporally-synced text across three dataset categories, and develop FIATS, a lightweight model with channel-aware cross-attention mechanisms (CASM/CAPS) that operationalizes the paradigm. Experiments show FIATS substantially outperforming self-stimulated baselines—including billion-parameter foundation models—on synthetic, physics, traffic, and market datasets.

## Strengths

- **Strong theoretical framing with empirical validation**: Proposition 2.1 and 3.1 provide a clean control-theoretic formalization of why ignoring influences creates an irreducible error floor, and Proposition 3.1 shows that incorporating any measurable influence reduces it. The FM Toy experiment directly validates this: FIATS achieves near-zero MSE (0.003) while all self-stimulated baselines—including large pretrained models—fail, demonstrating the theory in a controlled setting.

- **Well-constructed, purpose-built benchmark**: The IATSF benchmark is carefully designed to be leak-free, temporally synchronized, and to use independently evolving influences (weather forecasts, developer logs). The inclusion of three distinct categories—toy systems, complex real-world systems, and human-driven business systems—provides a meaningful testbed spanning different influence types and difficulty levels.

- **Consistent and substantial empirical gains**: FIATS achieves a 36% average MSE reduction on Atmospheric Physics and 44.3% on NYC Traffic Speed compared to the best self-stimulated baseline (PatchTST), gains that persist across all prediction lengths. This holds even against billion-parameter foundation models (Chronos-L, MOIRAI-L), making a compelling case that influence information, not model scale, drives the improvement.

- **Interpretable architecture with meaningful ablations**: The CASM attention maps (Figs. 3, 5) reveal that the model learns channel-specific sensitivity to different influence sentences. The "Zero News" ablation collapses performance to self-stimulated levels, confirming influences drive the gains, and "Zero Desc." degradation confirms channel descriptions matter. The embedding model robustness check (OpenAI vs. MiniLLM vs. mpnet) is a positive sign of architectural stability.

- **Lightweight, LLM-free design isolates the contribution**: Unlike prior text-informed forecasters that rely on large language models, FIATS uses standard text embeddings and a modest architecture, making it clear that gains come from influence modeling rather than from scaling up model capacity.

## Weaknesses

### Fatal

None.

### Major

- **No simple influence-aware baselines isolate the architecture from the information**: The paper ablates *Zero News* (showing influences matter) and *Zero Desc.* (showing channel descriptions matter), but never tests whether a trivial baseline—e.g., concatenating text embeddings with time-series patches and feeding the result to a standard PatchTST or DLinear encoder-decoder—could achieve comparable gains from the same influence information. TimeLLM is the only multimodal comparator, and it is an LLM-based reprogramming approach, not a simple integration. Without such a baseline, the claim that FIATS's *principled CASM/CAPS architecture* is necessary for the gains (rather than merely having access to influence text in *any* form) remains unsubstantiated. This is a structural evidential gap that cuts across all experimental sections.

- **No statistical variation reported**: Every table and figure reports a single MSE value with no error bars, standard deviations, confidence intervals, or mention of multiple seeds. On the Electricity Utility dataset, differences between methods are often in the third decimal place (e.g., FIATS 0.124 vs. TimeLLM 0.131 at pred. len 96), where it is impossible to judge whether the ordering is meaningful without variance estimates. Even the larger gaps (e.g., Atmospheric Physics) would benefit from uncertainty quantification to support the strong conclusions drawn. This is a basic methodological requirement in empirical ML.

### Minor

- **Insufficient comparison with existing text-informed forecasting methods**: The paper cites several recent text-informed forecasting works (Aksu et al., 2024; Williams et al., 2025; Wang et al., 2024a; Liu et al., 2024a) but only includes TimeLLM as a multimodal baseline. The argument that existing multimodal datasets are unsuitable for influence-aware evaluation is reasonable, but the paper should explain why those methods cannot be adapted to the IATSF benchmark, or at minimum discuss their relationship more concretely.

- **Claims of lightweight/efficient design are unsubstantiated**: The paper brands FIATS as "lightweight" and "LLM-free" but provides no parameter counts, runtime measurements, or memory comparisons against baselines. Without this data, the efficiency claim is purely rhetorical.

- **FIITS is undefined in the main text**: FIITS appears prominently in Table 1 (and often places second) but is never explained. Its values closely match the "Zero News" ablation, suggesting it is FIATS without influence, but the reader should not have to guess.

- **Theoretical contribution is somewhat oversold**: Proposition 2.1 formalizes the well-known fact that omitting an influential variable induces irreducible error; the control-theoretic framing adds structure but the "missing foundation" rhetoric ("breaking a barrier," "primary path forward") overstates the novelty of the theoretical insight. Similarly, the full-observability assumption ($X = Z$) is acknowledged but its implications for the bound's real-world applicability are not revisited, weakening the link between theory and the practical architecture.

- **Hyperparameter and training details absent**: No information is provided about optimizers, learning rates, schedules, batch sizes, or early stopping criteria. These are standard for reproducibility even if code is available.

### Trivial

- The paper repeatedly uses phrases like "breaking the barrier" and "primary path forward," which come across as overclaiming and distract from the otherwise solid contributions.

## Nice-to-Haves

- **Computational cost comparison**: Reporting wall-clock time, parameter counts, or memory usage for FIATS vs. baselines would substantiate the lightweight claim and aid practitioners.
- **Discussion of when channel descriptions are unavailable**: The model requires natural-language channel descriptions; acknowledging this constraint and discussing fallback strategies (e.g., learned channel embeddings) would strengthen the limitations section.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Benchmark documentation deferred to appendix (from harsh critic)**: The harsh critic noted that weather forecast text generation details and leak-free verification are relegated to Appendices N and O, which the reviewer could not see. Per review guidelines, missing appendix content is a parser artifact (the original submission includes those appendices) and cannot be held against the paper.

- **Harsh critic's claim that Proposition 2.1 is just a restatement of omitted-variable bias**: While the core insight is indeed well-known, the control-theoretic formalization and the specific bound derivation in a forecasting context constitute a genuine (if modest) contribution. This is retained as Minor under "theoretical contribution oversold" rather than removed entirely.

- **Harsh critic's request for more multimodal baselines beyond those cited**: The paper already includes TimeLLM as a multimodal baseline. Demanding adaptation of every cited text-informed method to the new benchmark is scope creep. Retained only as a Minor observation that more discussion would help.

- **Strength Finder's claim that the paper "rigorously" proves a "fundamental" barrier**: The theory is well-structured but not groundbreaking; the word "rigorous" is appropriate but "fundamental" overstates the novelty. This strength is retained with moderated language.

- **Strength Finder's framing of gains as "decisively validating" the paradigm**: The gains are real and impressive, but the missing error bars and simple baselines prevent "decisive" validation. The strength is retained but the language is tempered.

## Novel Insights

The paper's most genuinely novel observation is the explicit mapping between linear control systems and cross-attention mechanisms: channel-specific sensitivity to influences ($\frac{d x_f^i}{d U_f^j} = c^i B^j$) maps naturally to queries-as-channel-descriptors and keys-as-influence-filters. This connection—while the paper only sketches it for the linear case—is an elegant bridge between classical systems theory and modern transformer architectures that could inspire further work beyond time series forecasting. The CASM block's residual stacking with self-attention also provides a template for how to incorporate structured domain knowledge (sensitivity matrices) into learned attention patterns without sacrificing the flexibility of deep networks.

## Suggestions

- Add at least one simple influence-aware baseline: concatenate text embeddings to time-series patches and feed to PatchTST or DLinear. This would cleanly separate the value of *having* influence information from the value of the *specific architecture* used to integrate it.
- Run each model with ≥3 random seeds and report mean ± std in tables, or at minimum note that results are stable across runs. This is standard practice and would immediately strengthen all quantitative claims.
- Define FIITS explicitly in the main text.
- Include parameter counts and a brief runtime comparison to substantiate the "lightweight" claim.
- Tone down the "breaking the barrier" rhetoric in the abstract and introduction to better match the actual contribution level.

## Score and Decision

**Bracket (Round 1)**: The paper sits between 4.5–7.0. Weak anchors (LST-Bench at 2.50, BenchStock at 2.60, TimeRAG at 3.00) are clearly below this paper. Middle anchors (CiK at 5.00, TGForecaster at 5.00, GIFT-Eval at 5.25) provide the closest comparison—FIATS has substantially stronger theory, a more carefully constructed benchmark, and more compelling results than these related works. Strong anchors (FITS at 8.00, TimeMixer++ at 8.00, ModernTCN at 8.00) are clearly above this paper in execution polish and experimental rigor.

**Narrowing (Round 2)**: Compared to Time-LLM (7.00, Accept) and DAM (7.00, Accept), FIATS has stronger theoretical grounding and a more purposefully designed benchmark, but weaker experimental rigor (no error bars, no simple baselines). These experimental gaps prevent the paper from reaching the 7.0 tier. Compared to TGForecaster (5.00, Reject)—a closely related prior work on the same core idea—FIATS adds substantial value through control-theoretic formalization, leak-free benchmark design, and more sophisticated architecture. The paper clearly exceeds the 5.0 tier.

**Anchor comparison summary**:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| LST-Bench (2wwPG1wpsu) | 2.50 | 1 | FIATS much stronger |
| BenchStock (bsXxNkhvm6) | 2.60 | 1 | FIATS much stronger |
| TimeRAG (GvzL4LuycW) | 3.00 | 1 | FIATS much stronger |
| CiK (4F1a8nNFGK) | 5.00 | 1 | FIATS stronger (better theory, more rigorous benchmark) |
| TGForecaster (mfc6FKgtQA) | 5.00 | 1 | FIATS clearly stronger (theory, architecture, experiments) |
| GIFT-Eval (9EBSEkFSje) | 5.25 | 1 | Different focus; FIATS more novel |
| Dual-Forecaster (QE1ClsZjOQ) | 4.50 | 1 | FIATS stronger |
| Hybrid Modeling (v9Sfo2hMJl) | 5.67 | 2 | FIATS comparable; more novel direction |
| Simple Baseline (oANkBaVci5) | 6.75 | 2 | Different focus; FIATS comparable in contribution |
| Time-LLM (Unb5CVPtae) | 7.00 | 2 | FIATS has better theory but weaker experimental rigor |
| DAM (4NhMhElWqP) | 7.00 | 2 | Comparable ambition; DAM slightly more polished experiments |
| Time-MoE (e1wDDFmlVu) | 7.33 | 2 | Different focus; FIATS below |
| FITS (bWcnvZ3qMb) | 8.00 | 1 | FIATS clearly below in execution polish |
| TimeMixer++ (1CLzLXSFNn) | 8.00 | 1 | FIATS clearly below |

The paper makes genuine and well-motivated contributions (theory, benchmark, model) with strong empirical results, but two major experimental gaps—absence of simple influence-aware baselines and lack of statistical variance reporting—prevent the evidence from being fully conclusive. The paper lands at **6.0**: clearly above the reject-tier papers on this topic, but below the accept-tier papers that demonstrate more rigorous evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>