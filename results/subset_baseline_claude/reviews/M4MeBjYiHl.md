## Summary

The paper proposes a volatility-adaptive multimodal DRL framework for stock trading that combines pre-trained LLMs (BERT/GPT-2), a Transformer-based feature extractor, and Soft Actor-Critic (SAC). The key technical novelties include a reprogramming layer to align price time-series with LLM semantic space, cross-attention fusion of news and price embeddings, multi-scale temporal feature extraction, and critic gradient feedback to the feature encoder for end-to-end optimization. Experiments on 10 NASDAQ-100 stocks over 2021–2022 show positive cumulative returns in a bear market where baselines fail, with ablations attributing gains to each module.

---

## Strengths

- **Comprehensive baseline comparison:** The multi-stock trading evaluation includes 9 baselines ranging from classic DRL (A2C, PPO, SAC, TD3, DDPG) to Transformer-based methods (TACR, StockFormer) and an ensemble strategy, providing a meaningful performance landscape.
- **End-to-end training signal:** Propagating critic gradients back to the Transformer feature extractor is a principled design choice that unifies feature representation learning with policy optimization, and the ablation confirms this matters (12.8% SR gain).
- **Ablation breadth:** The study systematically isolates news, price, and correlation modules, plus the fusion mechanism, giving a reasonable account of each component's contribution.
- **Practical multimodal alignment:** The use of a reprogramming layer inspired by Time-LLM to bridge price patches and LLM semantic space, followed by bidirectional cross-attention fusion, is a coherent design for aligning heterogeneous data sources.

---

## Weaknesses

### Fatal
None that fully invalidate the paper, but the issues below significantly limit the strength of the empirical claims.

### Major

1. **Numerical inconsistency between Table 1 and Table 3:** In Table 1, the full Ours(BERT) model achieves a Sharpe Ratio of 0.544; in Table 3 (ablation), the same complete model (all four modules active) reports SR = 0.608. These two numbers must be identical—they are never explained or reconciled. This raises serious questions about experimental reliability or identical experimental protocols.

2. **Misleading volatility claim vs. reported numbers:** The paper's core selling point is "volatility adaptability," yet Table 1 shows Buy-and-Hold has the *best* Annualized Volatility (AV = 0.320, bolded), while Ours(BERT) has AV = 0.440 and Ours(GPT-2) = 0.408—higher than eight of the nine other methods. The narrative ("our framework's ability to balance fluctuation control") directly contradicts the table. Claiming superiority in volatility control while reporting the highest AV is an unsupported assertion.

3. **Extremely limited evaluation scope:** The empirical conclusions rest on 10 stocks (selected for news coverage), a single 12-month test window (Dec 2021 – Dec 2022), which is exclusively a bear market (NASDAQ -31.5%). Positive returns during a broad downturn could arise from trivially learning to reduce equity exposure rather than from multimodal intelligence. There is no validation across bull markets, sideways markets, or different time periods, making generalizability unsubstantiated.

4. **Reprogramming layer equations are inconsistent with stated intent:** The paper states the reprogramming layer uses a vocabulary token embedding matrix E ∈ ℝ^{V×D} with text prototypes as K and V (to map price into LLM semantic space). However, Equations (2)–(4) define Q, K, and V all as projections of X_price, i.e., pure self-attention with no text prototype involvement. This is the opposite of how reprogramming layers function in Time-LLM. The stated motivation and the written equations are in conflict.

### Minor

- **No transaction cost modeling:** The trading simulation does not appear to account for bid-ask spreads, brokerage fees, or slippage. In a multi-stock setting, trading frictions can substantially alter realized Sharpe and CR, particularly for strategies that trade frequently.
- **Single-stock prediction baselines are weak:** The prediction comparison uses only Autoformer, raw GPT-2, and raw BERT. Contemporary time-series forecasting baselines (e.g., PatchTST, TimesNet, iTransformer) are absent, making it hard to situate prediction performance in the current literature.
- **Frozen vs. fine-tuned LLM undefined:** The paper does not clearly state whether the LLM backbone weights are frozen or updated during training, which affects computational budget, risk of overfitting, and reproducibility.

### Trivial
- The ablation table (Table 3) renders all cells as ✓ in the parsed text, obscuring which modules are removed per row. (Attributed to parser artifact.)

---

## Nice-to-Haves

- Evaluate on multiple distinct market regimes (bull, bear, sideways) and report statistical significance with confidence intervals across regime types.
- Clarify and correct the reprogramming equations to accurately reflect whether K and V come from text prototypes or price embeddings.
- Add a realistic transaction cost model (e.g., 0.1% per trade) to Table 1.
- Include a "cash-only" or "0% equity" baseline to verify that positive returns are not driven by learning to hold cash during a broad downturn.

---

## Novel Insights

The paper's most interesting technical choice is the critic-gradient feedback loop from SAC to the Transformer feature extractor, treating the feature encoder as trainable under the RL objective rather than as a frozen upstream module. This creates a tighter coupling between state representation and value estimation and is supported by the ablation. The practical problem formulation—bridging LLM semantic space and price dynamics for DRL-based trading—is timely, though the specific execution of the reprogramming layer is inconsistent with its stated design.

---

## Suggestions

- **Resolve the SR discrepancy** between Tables 1 and 3: re-run under identical conditions and report a single coherent number with seeds.
- **Correct or clarify Equations (2)–(4)**: if text prototypes serve as K and V in the reprogramming layer, the equations should reflect this (Q = X_price · W^Q, K = E · W^K, V = E · W^V).
- **Extend the test period** to at least 3–5 years covering multiple market regimes, and report metrics per regime.
- **Drop or soften the volatility-control narrative** unless AV can be shown lower than baselines, or reframe the claim around risk-adjusted returns (SR and MDD) where the results are more defensible.
- **Add a degenerate "go to cash" baseline** to demonstrate the positive return is not explainable by simply avoiding the 2022 bear market.

---

## Score and Decision

The paper addresses a genuinely relevant and active research problem, and the end-to-end gradient feedback design is a worthwhile contribution. However, the inconsistency between Table 1 and Table 3 Sharpe Ratios raises reproducibility concerns; the core claim of volatility adaptability is contradicted by the AV column of Table 1; and the evaluation is restricted to a single bear-market year on 10 cherry-picked stocks. The reprogramming layer equations conflict with their stated purpose. These are not minor rough edges—they undermine confidence in both the experimental results and the methodological description.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>