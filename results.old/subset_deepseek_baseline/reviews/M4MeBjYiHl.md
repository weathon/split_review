## Summary

This paper proposes a multimodal deep reinforcement learning framework for stock trading that integrates pre-trained LLMs (BERT/GPT-2), Transformers, and the Soft Actor-Critic algorithm. The framework uses an LLM-driven module with a reprogramming layer to align price and news modalities, a Transformer feature extractor to capture multi-scale temporal dynamics and inter-stock correlations, and critic gradient feedback to the Transformer for end-to-end optimization. Experiments on 10 NASDAQ-100 stocks show the method outperforms several DRL baselines in multi-stock trading and surpasses time-series and LLM-only models in single-stock prediction.

## Strengths

- The problem of integrating textual news with price data in a DRL setting is relevant and timely. The paper addresses an important gap in existing DRL trading methods that neglect unstructured financial information.
- The proposed architecture is technically multifaceted, combining reprogramming-based cross-modal alignment, multi-scale Transformer features, and gradient feedback from SAC to the feature extractor—an interesting integration.
- The experimental evaluation includes a reasonable set of baselines across both trading and prediction tasks, and the ablation study (though presented with formatting issues) attempts to isolate component contributions.

## Weaknesses

### Fatal
None.

### Major

1. **No transaction costs in trading experiments.** The paper reports cumulative returns and Sharpe ratios without any mention of transaction costs, slippage, or market impact. In any realistic stock trading simulation, transaction costs significantly reduce net returns and alter the relative ordering of strategies. This omission makes the claimed superiority over baselines unverifiable for practical deployment and undermines the paper’s central claim of effectiveness in “real-world volatile markets.”

2. **Ambiguity and likely flaw in prediction evaluation scaling.** The paper states that all numerical features were normalized to [0,1] using min-max scaling, but the MSE/MAE values reported in Table 2 (e.g., AMD MSE = 9.66 for Autoformer) far exceed 1, which is impossible if the data were truly normalized. This suggests either the normalization was not applied in the prediction task or the description is inaccurate. Inconsistent scaling across stocks makes the reported errors incomparable and the claimed prediction improvements unreliable.

3. **Insufficient explanation of the end-to-end gradient-feedback mechanism.** The paper claims that critic gradients propagate back to the Transformer to jointly optimize feature learning and policy, but it does not specify how this is implemented—e.g., whether the LLM backbone is frozen, how the Transformer loss is defined, whether the gradient flow bypasses the supervised LLM training, or how the critic gradient is combined with any auxiliary prediction loss. Without these details, the claimed end-to-end optimization cannot be assessed or reproduced.

4. **Garbled and uninterpretable ablation results.** Table 3 shows all rows with identical checkmarks, making it impossible to determine which module combinations produced the reported CR/SR values. The textual description partially offsets this (mentioning a “best sub-module combination” with news+price, and a baseline with price+correlation), but the table itself is broken and the mapping between rows and configurations is lost. This prevents verification of a core contribution.

5. **Limited scope and lack of broader evaluation.** The experiments only cover 10 stocks from NASDAQ-100, a single bear-market period (Dec 2021–Dec 2022), and one prediction horizon. No out-of-sample testing across different market regimes, no sensitivity analysis, and no comparison with more recent multimodal finance methods (e.g., FinGPT with DRL, or cross-modal transformers for stock prediction). The claims would need substantially more evidence to support generalizability.

### Minor

- The paper does not report the computational cost or inference latency, which matters for trading applications.  
- Several technical details are under-specified: the “hold” feature in the state space, the exact structure of the Transformer decoder in the predictive module, and the reward function in the trading environment.  
- The baselines used for single-stock prediction (Autoformer, GPT-2, BERT) are not the most competitive for this specific multimodal forecasting task; a comparison with methods like FinBERT+LSTM or Informer would be more informative.

### Trivial

- The structure of Section 2 could be streamlined; the dual use of the term “Multimodal LLM” for both the observation extraction module and the final reasoning LLM is slightly confusing.

## Nice-to-Haves

- Include transaction costs (e.g., 0.1% per trade) and show sensitivity to different cost levels.  
- Provide a clear pseudo-code or algorithmic description of the joint gradient-feedback training loop.  
- Test on additional time periods including bull markets and high-volatility events beyond COVID-19.  
- Compare with other multimodal DRL approaches (e.g., FinBERT sentiment features + PPO) to isolate the benefit of the reprogramming and cross-attention components.

## Novel Insights

None beyond the paper’s own contributions—the integration of reprogramming-based price-news alignment with Transformer multi-scale features and SAC critic feedback is the main novelty. The paper does not yield a surprising or unexpected empirical finding that transcends its specific architecture.

## Suggestions

- Add a thorough discussion and ablation of transaction costs. Even if the authors choose to ignore them, state this clearly and argue why the comparative conclusions still hold.  
- Normalize the prediction MSE/MAE by the range or mean of the target for each stock to enable fair cross-stock comparison, or report percentage errors (e.g., MAPE).  
- Provide a full, readable ablation table (e.g., with ×/✓ symbols and clear row labels) and include CR, SR, AV, MDD for each configuration.  
- Detail the gradient-feedback training step: which layers receive critic gradients, what loss weights are used, whether the LLM is frozen or fine-tuned.  
- Consider adding statistical significance tests for the trading results (though the paper mentions tests for random-strategy comparison in the appendix, which is not viewable).

## Score and Decision

**Score:** 4.0 – The paper addresses an interesting problem and proposes a technically reasonable architecture, but several major flaws (no transaction costs, prediction scaling inconsistency, unclear end-to-end training, broken ablation table) undermine the trustworthiness of the experimental claims. The contributions are not sufficiently validated in the present form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>