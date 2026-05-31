## Human Reviewer 1

### Summary
This paper reformulates the classical lead–lag detection problem in financial markets as a temporal link prediction task on dynamic graphs. By representing assets as nodes and directional edges as lead–lag interactions, the authors aim to capture time-evolving interdependencies beyond traditional pairwise statistical methods such as Granger causality. The study builds a benchmark dataset of 37 entities (29 stocks and 8 commodities) covering five years of daily data enriched with financial indicators and sentiment features. It evaluates eight models — from LSTM baselines to several Temporal GNN (TGNN) architectures (JODIE, DySAT, TGAT, TGN, APAN, GraphMixer, and GraphMixer-TNF). Experiments compare performance across two settings: (1) both positive and negative lead–lag relationships, and (2) positive-only (bullish) relationships. The results show that GraphMixer, a simple MLP-based architecture, consistently outperforms more complex TGNNs, suggesting that model simplicity can suffice for this task.

### Strengths
1. Novel framing: The paper provides a fresh machine-learning-based formulation of lead–lag detection as temporal graph learning, moving beyond static or pairwise correlation-based approaches. This reconceptualization opens opportunities for applying TGNNs to dynamic financial dependencies.

2. Comparison fairness: The authors implement a fair experimental setting, using consistent frameworks (TGL) across models and appropriate evaluation metrics (AAUC, MRR, Recall@k), mitigating class imbalance concerns.

3. Empirical comprehensiveness: Comparative analyses across multiple architectures and ablation studies (feature type variations, statistical tests) provide a broad experimental overview.

### Weaknesses
1. Temporal heterogeneity and regime shifts overlooked: The dataset includes the COVID-19 crisis, during which the paper itself notes a “spike” in link formation density. Yet, the model evaluation does not examine robustness across different market regimes or stress periods. Without regime-based or rolling-window validation, it is unclear whether the model truly generalizes beyond specific volatility clusters.

2. Static features dominate performance: In the ablation study (Table 3), models using only static description embeddings achieve comparable or even better results than those incorporating temporal features such as price and sentiment. This implies that temporal dynamics — the central motivation of the paper — are not the main performance drivers. The dataset may therefore encode static inter-asset similarity rather than dynamic lead–lag propagation.

3. Lack of economic interpretability and validation: Despite references to “investment insights,” the study does not include trading simulations or backtesting to establish economic significance. Nor does it benchmark against traditional econometric baselines like Granger causality, VAR models, or rolling correlation networks, leaving its claims of superiority over “statistical methods” empirically unverified.

### Questions
1. Why do you think the model achieves nearly top-level performance even when using only static description embeddings?

2. Does the fact that a simple model like GraphMixer performs so well indicate that the temporal structure is not being properly captured — or perhaps that it is not as important as expected?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper investigates the problem of detecting lead–lag relationships among financial assets — that is, identifying which assets tend to move ahead of others in time. The authors argue that such temporal dependencies can be naturally represented as dynamic graphs, where nodes correspond to assets and edges indicate evolving lead–lag effects. To this end, they formulate the problem as a temporal link prediction task and evaluate several deep learning models.

A custom dataset of 37 financial assets over 1,257 time steps is constructed, incorporating price, technical indicators, and sentiment features. Experiments are conducted under two settings — one considering both positive and negative lead–lag relationships, and another focusing on positive (bullish) ones only. Results show that GraphMixer achieves the best overall performance across several ranking-based metrics (AP, AAUC, MRR, R@k), suggesting that temporal graph learning can effectively capture complex dependencies between asset movements. An ablation study and statistical significance analysis (via Friedman and Conover tests) are provided to support the empirical findings.

### Strengths
The paper is generally well written and easy to follow. The overall structure is clear. The proposed framework for modeling lead–lag relationships through temporal link prediction on dynamic graphs is conceptually intuitive and technically straightforward to understand. The authors also make an effort to compare a range of baseline models, from simple sequence models (e.g., LSTM) to state-of-the-art temporal GNNs, which helps situate their approach within the broader literature.

### Weaknesses
1) The motivation of the current paper is not sufficiently solid. Lead–lag analysis has a well-established foundation in financial econometrics, and the paper fails to clearly articulate the specific limitations of traditional approaches—such as Granger causality, transfer entropy, or temporal causal graphs—in modeling dynamic dependencies. Moreover, it does not demonstrate any distinctive advantage of TGNNs in capturing causal directionality or improving predictive interpretability. Although the proposed models show some empirical performance gains, the work lacks a theoretically novel problem formulation, making its motivation appear overly generic.

2) From a methodological perspective, the proposed approach lacks theoretical justification, particularly given that financial markets are high-dimensional stochastic systems with strong non-stationarity, heavy-tailed noise, and structural regime shifts. The paper does not provide any analysis—either theoretical or empirical—regarding the reliability and robustness of using temporal graph neural networks (TGNNs) for modeling such inherently unstable dynamics. While the model achieves performance improvements on the constructed dataset, it remains unclear why the architecture should generalize beyond this specific sample or how it avoids overfitting to transient correlations. In the absence of a theoretical grounding (e.g., under what assumptions the TGNN can approximate Granger causality or causal directionality), the results risk being purely correlational and non-informative from an economic standpoint.

3) A major limitation of this paper lies in the scale and representativeness of the dataset. The dynamic lead–lag graph includes only 37 nodes (assets) and 1257 time steps, which is extremely small compared to real-world financial markets that typically involve hundreds or thousands of correlated instruments. Such a limited sample size effectively makes this a proof-of-concept experiment, rather than a validation of the method’s robustness or generalizability. Given the stochastic and non-stationary nature of financial systems, conclusions drawn from such a small and domain-specific subset (mostly renewable energy and EV-related stocks) cannot be confidently generalized to broader market settings. The paper should either (i) justify why this small-scale dataset is sufficient to demonstrate the claimed methodological advantages, or (ii) extend the evaluation to a larger, more diverse asset universe to substantiate its claims.

4) Another important omission concerns the model architecture specifications.
For all temporal GNN baselines (GraphMixer, TGN, DySAT, TGAT, JODIE, and APAN), the paper does not report fundamental architectural details such as hidden dimensionality, number of layers, activation functions, dropout rates, or message-passing depth.
These parameters critically influence both model capacity and generalization, and without them, it is impossible to assess whether the reported performance differences arise from methodological advantages or from arbitrary architectural tuning.

5) The paper tends to overclaim its novelty.
Essentially, it models lead–lag relationships in financial event sequences from a purely data-driven perspective, yet such relationships have been extensively studied in financial econometrics.
Many assets (e.g., derivatives such as futures and options) are structurally designed to exhibit lead–lag behavior with respect to their underlying assets.
Therefore, the problem setting itself is not new. If the contribution is mainly algorithmic, the paper should clearly position itself as a temporal graph learning approach for financial data.
Conversely, if it aims to make a domain contribution, it should provide a stronger economic rationale for why existing causal or econometric tools (e.g., Granger causality, transfer entropy, or high-frequency microstructure analysis) are insufficient.
Without such grounding, the paper reads as a technical application rather than a conceptually motivated advancement, and the claimed practical significance feels overstated.

### Questions
1) Could the authors explicitly articulate what concrete limitations of traditional econometric or causal methods (e.g., Granger causality, transfer entropy, temporal causal graphs) their TGNN approach overcomes? What aspect of “dynamic dependency modeling” cannot be addressed by these existing frameworks?

2) Under what theoretical assumptions can TGNNs be expected to capture causal directionality or Granger-like dependencies?
Have the authors considered any formal connection between message-passing dynamics and causal inference principles in stochastic systems?

3) Since the dataset contains only 37 assets and 1257 time steps, what justifies the claim that the approach generalizes to broader market settings?
Can the authors comment on how the model’s complexity scales with larger, more realistic asset universes?

4) The dataset appears to be dominated by renewable energy and EV-related stocks.
How might this domain bias affect the interpretability of the learned lead–lag relationships?
Are the results robust across other industry sectors or asset classes?

5) Beyond numerical performance gains, what do the discovered lead–lag relationships imply from an economic or behavioral perspective?
Can the authors show any concrete examples (e.g., lead–lag between futures and underlying equities) that correspond to known market mechanisms?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper focuses on the importance of the lead-lag relationship in financial markets, which is proposed to be expressed in a temporal graph structure, with the detection of their effects as a temporal link prediction task. Based on this reformulation, the authors introduce a new benchmark for the performance comparison of SOTA temporal GNNs on modeling lead-lag interactions that can be both positive and negative. Experiments are evaluated on a custom dataset built upon financial assets based on temporal, structural, and sentiment features.

### Strengths
The main strengths of this work are summarized as follows:
1. The problem of inter-stock interactions (often expressed as a lead-lag effect) forms indeed an interesting modeling aspect in applications on financial markets; therefore, experimental comparisons on predicting the strength of lead-lag interactions can be useful (Significance).
2. Stock price prediction depends on external information; therefore, evaluating on a dataset built on interactions and sentiment features beyond pure price movements highlights the need for adding external knowledge in this domain (Quality).
3. The benchmark is easy to follow, and results include statistical significance tests (Clarity).

### Weaknesses
The weak aspects of the paper are the following:
- *(W1)* The authors disregard mentioning related works on hypergraphs for stock prediction tasks [3], some of which explicitely consider lead-lag relationships [1,4,5]. The related work should be enhanced such that the most recent works leveraging GNNs and graph interaction for stock data is presented. Additional recent models in stock prediction could be mentioned [2]. 
- *(W2)* It is unclear why predicting lead-lag interactions alone is so crucial, while in the relevant literature the end task is most of the time stock price prediction. The authors should justify their choice or experimentally showcase how the prediction of interaction can improve forecasting performance.
- *(W3)* For people aware of financial markets, it is common knowledge that stocks belonging in the same sector interact positively (and based on their size can lead smaller stocks), while stocks in competing sectors interact negatively. It is unclear how the proposed custom-made dataset captures complex interaction patterns, which is crucial since the final task is indeed predicting the interactions. The authors should mention also why existing datasets (e.g., those used in related works) are not sufficient for lead-lag modeling.
- *(W4)* Based on W3, to showcase how “easy” the constructed dataset is for lead-lag identification, including if temporal graphs are better than static, simpler models that build on correlations should be considered, e.g., graph-based baselines on similarity/causality measures (pairwise Granger-causality). Different experimental setups are crucial to prove the necessity of predicting dynamic interactions and could potentially be combined with an end task (e.g., forecasting).
- *(W5)* Including some visualizations on the predicted lead-lag correlations and how this is indeed connected to true effects during specific periods based on temporal patterns, could be a complementary way to prove the necessity of temporal graphs in the field. In the current form of the paper it is unlear how predicting the power of an interaction can be used in practice for solving tasks in financial markets. 
- *(W6)* The paper proposes a benchmark, yet fails to position itself against other benchmarks in the field (if existent) and why those are not enough for tasks in financial markets. The methododological novelty is limited since the authors do not propose a method but rather a whole family of methods that should be assessed, while the construction of the dataset seems a bit heuristic (not justified as an extension of prior works).

[1] HUYNH, Thanh Trung, et al. Efficient integration of multi-order dynamics and internal dynamics in stock movement prediction. In: Proceedings of the Sixteenth ACM International Conference on Web Search and Data Mining. 2023. p. 850-858.

[2] FAN, Jinyong; SHEN, Yanyan. StockMixer: A simple yet strong MLP-based architecture for stock price forecasting. In: Proceedings of the AAAI conference on artificial intelligence. 2024. p. 8389-8397.

[3] LIAO, Sihao, et al. Stock trend prediction based on dynamic hypergraph spatio-temporal network. Applied Soft Computing, 2024, 154: 111329.

[4] LI, Yongli, et al. Dynamic patterns of daily lead-lag networks in stock markets. Quantitative Finance, 2021, 21.12: 2055-2068.

### Questions
- *(Q1)* Based on (W1) and (W2), the authors should clarify the importance of a lead-lag detection benchmark for tasks involving financial market data, while properly positioning them against any work on machine learning (graph-based) methods in the field.
- *(Q2)* Based on (W3) and (W6), the authors should showcase why in practice existent datasets/benchmarks are insufficient and how the proposed dataset/benchmark can be leveraged for new studies in the field.
- *(Q3)* It is unclear whether the detection of lead-lag relationships is easy based on the extracted relationships and the link prediction task, and how temporal learning can be informative for stock markets, as expressed in (W4) and (W5).

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper presents a novel framework for detecting financial lead-lag relationships. Its core contribution is to reframe this classic statistical problem as a temporal link prediction task on a dynamic graph. By doing so, it moves the analysis from isolated, pairwise comparisons to a holistic, network-level problem, allowing the application of modern Temporal Graph Neural Networks (TGNNs). The authors provide a new benchmark dataset and a rigorous comparison of seven TGNNs, ultimately finding that a simple, MLP-based model (GraphMixer) outperforms more complex architectures.

### Strengths
- Transforming lead–lag detection into temporal graph link prediction is a generalizable framing that moves the topic from econometrics to machine learning.
- The dataset construction process (returns, indicators, LLM embeddings, sentiment) is described in fair detail, which encourages reproducibility.
- The use of Friedman and Conover's post-hoc tests (Figure 2) elevates the results from a simple "league table" to a statistically validated conclusion.

### Weaknesses
- The entire framework rests on two "magic numbers," $\tau=1$ day and $\epsilon=5\%$, which are never justified through a sensitivity analysis. The finding that GM is the best model is contingent on this specific, restrictive definition of a "lead-lag," and the results may not generalize to different time lags or thresholds.
- The paper claims to model both short-term "relationships" and long-term "effects" but then uses a fixed $\tau=1$ day lag for all graph construction. By definition, this architecture cannot capture longer-term (e.g., weekly or monthly) effects, making its initial framing misleading.
- The graph contains only 37 nodes, which is a very small network. The performance and ranking of these models could change dramatically on a larger, more realistic graph, where neighborhood aggregation and scalability become non-trivial problems.
- The introduction spends too much space on dataset and experimental description instead of building conceptual motivation or framing research gaps.
- Some strong, absolute claims are immediately contradicted by the authors themselves in the very next sentences, where they refine the claim to "existing studies rarely leverage graph-based representations, and when they do, they typically consider static rather than dynamic structures".

### Questions
Please see weakness above.

### Soundness
2

### Presentation
1

### Contribution
3

### Rating
2

### Confidence
4

---

## Human Reviewer 5

### Summary
This paper addresses the widely studied lead–lag relationships in financial markets by framing the problem as a temporal link-prediction task and applying Temporal Graph Neural Networks (TGNNs). The authors construct a real-world benchmark of 37 assets spanning roughly five years of daily observations, generate training/test labels under two schemes (considering both up/down moves and positive-only moves), and adapt multiple models (sequence baselines like LSTM and several TGNN variants). Models are evaluated with binary classification and ranking metrics including AP, AAUC, MRR, Recall@k. Results show that TGNN approaches, in particular GraphMixer, achieve the most accurate and stable performance across most metrics, significantly outperforming the LSTM baseline.

### Strengths
- The paper addresses a common and highly significant problem in the financial domain of the discovery and detection of lead–lag relationships, aiming to fill the gap left by existing deep learning methods in tackling this issue.
- The proposed method demonstrates strong originality, and the experimental section effectively explores how different types of relationships and link attributes impact the model’s performance across various metrics.

### Weaknesses
- In the domain of financial time series, relationships between entities are highly transient, and at the daily frequency it is difficult to assert the existence of persistent multi-day lead–lag effects. In this paper, however, any short-term co-movement observed on a single day is labeled as a positive sample, which introduces substantial noise into the dataset. As the authors themselves note, their model attempts to capture “lead–lag relationships” rather than statistically validated “lead–lag effects,” meaning that many detected links may lack statistical or economic significance.
- The paper fixes the parameters at $\tau=1,\epsilon=5\%$​, a single arbitrary configuration that undermines the robustness of its findings. Furthermore, the construction of lead–lag links through a link-prediction task in a TGNN framework remains a complete black box. It is unclear why the authors did not cross-validate these learned relations against established econometric or sequence-comparison methods such as Granger causality tests, correlation analysis, or Dynamic Time Warping (DTW). Solely relying on ablation studies provides limited evidence for the real-world validity and consistency of the captured relationships.
- Lacks intuitive visualization or clear qualitative illustrations of the constructed lead–lag links. Without graphical representations such as temporal evolution graphs, network snapshots, or case studies makes it hard to assess whether the model captures economically meaningful dependencies or merely statistical artifacts.
- The work entirely omits any practical evaluation in real financial markets, such as price forecasting or portfolio backtesting across multiple assets. Without testing how the detected lead–lag relationships translate into predictive or trading performance, it is impossible to judge their actual utility or robustness under realistic market conditions.
- The choice of using 384-dimensional asset description embeddings as base inputs is questionable. As a static vector, it is unclear how this representation can capture time-varying lead–lag dynamics rather than merely encode long-horizon, cross-sectional priors. Moreover, such high-dimensional embeddings can easily dominate or distort lower-dimensional financial time-series signals, leading to representational imbalance; for sequential and graph-based models (e.g., LSTM, TGNN), this may hinder effective learning of temporal dependencies. Finally, the main text provides limited architectural details (with some hyperparameters deferred to the appendix), leaving a full layer-by-layer specification and dimensionalities insufficiently documented.
- The dataset contains only 37 assets sampled at daily frequency, which severely limits the generalizability of the results. This small-scale setting cannot represent broader markets with diverse sectors or liquidity levels, and it is inadequate for evaluating models on higher-frequency data where lead–lag effects are more likely to persist or recur.

### Questions
- How do the authors justify treating any single-day co-movement as a valid lead–lag instance rather than transient noise? Have they evaluated the model’s robustness under stricter labeling criteria, such as requiring multi-day persistence or repeated occurrences within a time window?
- Why did the authors not benchmark their detected lead–lag links against classical econometric or statistical approaches to validate that the TGNN-derived relations correspond to statistically meaningful effects?
- How does authors ensure that the predicted “lead–lag links” reflect genuine economic dependencies rather than spurious statistical correlations? Is there any interpretability mechanism (e.g., attention visualization or feature attribution) that can help explain what drives a predicted link?
- Since the paper motivates the study with potential trading and portfolio applications, why was no backtesting or forecasting evaluation performed? How do the authors envision using the detected lead–lag patterns in practical decision-making？
- Given the Efficient Market Hypothesis suggests that stock prices already fully reflect all available information, can the authors provide any theoretical justification showing that their method could achieve greater stability or consistency compared to traditional statistical or price-sequence-based approaches?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4
