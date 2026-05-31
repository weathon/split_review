## Human Reviewer 1

### Summary
This paper proposes a volatility-adaptive multimodal DRL framework for stock trading that integrates LLMs, Transformers, and the SAC algorithm. By fusing textual financial news with price dynamics through attention-based reprogramming and cross-modal fusion, the model captures sentiment–price interactions and adapts to market volatility. Experiments on NASDAQ-100 data demonstrate superior performance over existing methods.

### Strengths
The paper explores the integration of textual financial news and quantitative price data within a multimodal framework. By leveraging a pre-trained LLM for news encoding and Transformer-based modules for price representation, it provides a reasonable step toward combining sentiment and numerical information for trading decision-making.

### Weaknesses
1. Many notations are not clearly defined. For instance, some symbols that represent vector data should be written in boldface using `\mathbf{}`. For example, in the expression
   $P = \\{ p^{\text{open}}, p^{\text{close}}, ..., p^{\text{volume}}\\}$,
   the terms such as $\mathbf{p}^{\text{open}}$ should be in bold to indicate vector representations.
2. The model assumes a perfectly aligned one-to-one correspondence between daily news and price data, based on a curated open-source dataset. However, in real-world markets, news arrivals are irregular. Some days contain multiple news items, while others have none. The current framework does not explicitly handle such temporal misalignment or modality sparsity, which may limit its applicability to more realistic, unbalanced data distributions.

3. The prompt design includes two key parameters, sequence length (seq len) and prediction length (pred len). However, the paper lacks a sensitivity analysis to examine how model performance varies under different context window sizes or forecasting horizons, even though these parameters directly affect the model’s temporal reasoning capacity and generalization ability.

### Questions
1. In Figure 4, many methods show a noticeable jump in CW around 2022-10. What caused this sudden change?

2. How does the method realize the stated volatility-adaptive capability? There seems to be no explicit risk control, and in Appendix E Algorithm 1, market volatility is included as an input but not utilized in the whole algorihtm.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper introduces a multimodal DRL framework involving LLMs, Transformer and SAC for stock trading. Experiments on NASDAQ-100 shows its SOTA performance.

### Strengths
1. This paper introduces the attention-based reprogramming layer to project time-series data into an LLM's semantic space, bridging structured and unstructured modalities.
2. The proposed framework somehow address volatility resilience, which is a critical limitation in real-world DRL trading.

### Weaknesses
1. In general, the novelty of this work is not enough for top conferences such as ICLR, it is a combination of LLMs, transformer and RL with limited contribution from the algorithm perspectives.
2. Experiments on NASDAQ-100 stocks is not enough, I recommend the authors to conduct experiments on more diversified and large-scale datasets to further evaluation the performance.
3. The proposed framework is quite complex, which raises my concern on the latency of real-world settings. More discussion on this is required.
4. As the motivation of this work is performance under extreme market conditions, more ablation study with quantified results on volatility-specific effects will help.

### Questions
1. For data alignment, how are timestamps between news articles and stock prices synchronized to avoid look-ahead bias?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces a multimodal deep reinforcement learning system that integrates large language models, Transformers, and the Soft Actor-Critic algorithm to improve trading robustness under market volatility. The model first extracts sentiment and event representations from financial news using a pre-trained LLM (BERT or GPT-2), then aligns price data to this semantic space through a reprogramming layer, and finally fuses both modalities using cross-attention. A Transformer encoder captures multi-scale temporal dynamics and inter-stock correlations, and SAC’s critic gradient feedback jointly optimizes feature learning and trading policy.

### Strengths
1. LLM-driven semantic alignment of news and prices.
The reprogramming layer projects numerical price data into the LLM semantic space using multi-head attention, enabling consistent multimodal fusion. This design avoids retraining large language models while ensuring semantic compatibility. The combination of prompt engineering for financial contexts and dynamic feature extraction demonstrates careful adaptation of general LLMs to finance-specific tasks.

2. Contextualized volatility awareness and interpretability.
The model’s design explicitly addresses volatility through multi-scale fusion (Eq. 7–8) and sentiment integration, helping explain its superior performance during unstable periods such as the 2021–2022 NASDAQ downturn (Fig. 4).

### Weaknesses
1. Insufficient ablation and parameter sensitivity analysis.
Although ablations are mentioned (Abstract; Sec. 3.4), details are sparse. It remains unclear how much each module—LLM feature extraction, reprogramming layer, or multi-scale fusion—contributes independently to the final gains. The effect of hyperparameters such as attention head count, SAC learning rate, or prompt length is not examined, limiting interpretability of results.

2. Inadequate computational efficiency discussion.
While hardware configuration is reported (Sec. 3.2), there is no runtime, memory, or inference-latency comparison. Training involves LLM encoding and multi-head attention fusion (Sec. 2.1–2.3), which are computationally heavy. Without quantitative cost analysis, practical deployability in real-time trading remains uncertain.

3. Restricted dataset scope and generalization evidence.
Experiments are limited to ten NASDAQ-100 components and five stocks for prediction (Sec. 3.1–3.5). The paper does not test across other markets or periods beyond 2019–2022, leaving the model’s adaptability to different economic regimes unproven. The reliance on English-language news may also bias performance toward U.S. markets.

4. Limited theoretical grounding of critic-Transformer gradient feedback.
The mechanism where SAC critic gradients enhance Transformer feature learning (Sec. 2.4) is described conceptually but lacks a mathematical formulation or ablation isolating its contribution. No explicit derivation links Eq. 9 to gradient propagation into the encoder. This omission reduces the clarity of how end-to-end optimization improves stability or volatility adaptation.

### Questions
1. What is the computational cost relative to baseline DRL methods?
Can the authors report average training time per epoch, GPU memory usage, and inference latency for real-time trading? Such data would clarify whether the proposed framework is feasible in practical financial environments.

2. Could broader datasets or markets be included to test generalization?
Would expanding experiments to other stock indices (e.g., S&P 500, Hong Kong HSI) or different time spans strengthen evidence that the model generalizes across regimes and news distributions? 

3. How exactly are SAC critic gradients propagated into the Transformer?
Could the authors provide explicit mathematical expressions or algorithmic pseudocode detailing the gradient flow from the critic network into Transformer layers?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes a volatility-adaptive, multimodal DRL framework to improve stock trading performance during turbulent markets, where traditional models often fail by ignoring news, failing to capture multi-scale trends, and lacking resilience. The framework integrates LLMs, Transformers, and the Soft Actor-Critic (SAC) algorithm:

1. The Multimodal LLM module extracts news sentiment and uses a multi-head attention reprogramming layer to align structured price data into the LLM’s semantic space. Price and news embeddings are then fused via cross-attention.
2. A Transformer is used to model multi-scale temporal patterns and inter-stock correlations, generating a unified state.
3. The SAC agent uses this state for decisions, with gradient feedback propagating back to the Transformer, ensuring end-to-end optimization that enhances the agent's volatility sensitivity.

Experiments on NASDAQ-100 stocks demonstrated that the framework outperformed baselines, yielding positive returns and high Sharpe Ratios during a turbulent test period.

### Strengths
[S1] Cross-Modality: The paper introduces a cross-attention mechanism that fuses and aligns news and price embeddings to capture how news sentiment relates to price features, rather than simple concatenation.

[S2] Volatility resilience: The combination of multi-scale price modeling and news context allows the agent to adapt to different market volatility regimes.

### Weaknesses
[W1] Limited stock set size: The model was evaluated using only ten stocks with sufficient news coverage drawn from the NASDAQ-100. This pre-filtered selection might not capture the full complexity of broader markets. The reported performance may not generalize well across diverse asset sets.

[W2] Insufficient comparison with news-driven models: The experimental evaluation would benefit from stronger comparisons with models that also leverage financial news. In Table 1, all baselines are traditional DRL or time-series methods that do not incorporate textual data, making it difficult to isolate the value of the proposed multimodal design. Similarly, Table 2 should include Time-LLM (Jin et al., 2023) or other news-driven approaches to better demonstrate how the proposed reprogramming layer differs from existing methods in stock price prediction.

[W3] Short testing period: Backtesting was conducted in a single year (December 2021 to December 2022). A one-year window offers a partial view of how the framework performs under different market regimes. To demonstrate the model’s long-term robustness, testing across different cycles (bull, bear, and sideways markets) would be essential.

[W4] Lack of transparency in strategy design and trading costs: The paper provides limited insight into the practical details of the trading strategy. It’s unclear how model outputs translate into actual portfolio allocations. Moreover, the study does not mention transaction costs, which are critical in the profitability of any trading system. 

[W5] News data source and validation: The paper relies on a Hugging Face dataset, but the source is not a verified commercial feed. The paper should identify the underlying news sources contributing to the dataset and explain how the data was collected and verified. This transparency would enable readers to assess the reliability of the textual inputs that drive the model’s decisions.

### Questions
[Q1] Novelty of the reprogramming layer: What is the difference and the novelty of your model compared to Time-LLM in the reprogramming layer in Table 2?

[Q2] Investment strategy details: The paper does not provide sufficient detail on how trading actions are translated into portfolio allocations. It remains unclear whether the portfolio weights are distributed. 

[Q3] Generalizability across market depth: How does performance hold up when applied to broader stock sets without sufficient news coverage? Many assets have sparse news coverage, which could disrupt the multimodal alignment process. The authors should clarify how the model handles such data gaps.

[Q4] Transaction cost impact on realized returns: Since real-world trading always incurs transaction costs, it would be useful to know whether transaction fees or slippage were included in the performance results reported in Table 1.

[Q5] Model complexity: The complexity of the multi-module architecture (LLM, Reprogramming, Transformer, DRL) makes the model harder to interpret, and the time complexity of the overall framework is not mentioned in the paper.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4