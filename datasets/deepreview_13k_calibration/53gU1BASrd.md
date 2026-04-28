# Evaluating and Finetuning Models For Financial Time Series Forecasting

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Time series forecasting is a challenging task as it is subject to a lot of noise, and the predictions often depend on external events. Still, recent deep learning techniques advanced the state-of-the-art on certain datasets, while they keep failing on other noisy datasets. This paper studies the case of financial time series forecasting, a problem that exhibits both a high noise and many unknown dependencies. We will show that the current evaluation pipelines are imperfect and forget a trivial baseline that can beat most models. We propose a new evaluation pipeline that is better suited for our task, and we run this pipeline on recent models. This pipeline is based on the idea of deciding which assets to buy and sell rather than predicting exact prices. Next, as the small datasets used in current approaches limit the size of the models, we train a general model on a massive dataset (containing a hundred times more data points than existing datasets) and show this model can be finetuned to improve the performance on small datasets. All our code and models will be published to help the community bootstrap and evaluate their future models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose model construction pipeline to be used to benchmark methods for returns forecasting and portfolio construction in financial applications. The author also proposes a procedure to transfer pre-trained models onto smaller datasets and fine tuned for trading applications.

### Strengths
Given the diversity of time series datasets, having access to a high quality specialist dataset for finance can be useful. Knowledge of standardised approaches to evaluate and benchmark both forecasting and portfolio construction methods can be useful for practitioners.

### Weaknesses
While the paper does put together a sequence of standardised techniques (for evaluation and for transfer learning), it fails to 1) concretely demonstrate what novel methods have been proposed and 2) why existing methods are insufficient.

On the evaluation front, numerous papers have been proposed to evaluate machine learning-based trading strategies (see references for both forecasting and portfolio construction), including 1) which benchmarks a variety of techniques in a standardised fashion. All of which have not been referenced by authors.

Furthermore, in contrast to claims that standardised datasets are lacking -- numerous open-source financial datasets can be found, and a list has been supplied below. The authors themselves do not open source their dataset (citing legal reasons that prevent publication), which run slightly contrary to the goal of developing a common framework for benchmarking.

In addition, transfer learning in the financial domain is also not a novel idea, and comparisons to previous works are absolutely required.

### Questions
1. Why is evaluation only performed on one day or one week of data? Most finanical papers test strategies over multiple years.
2. Why is the proposed pipeline superior to existing methods for evaluating trading strategies?
3. Is MSE benchmarked with regards to price forecasts (as seen from LAST)? Would returns or price change forecasts (with naive benchmark being returns=0) be more suitable approach given the non-stationarity of price data?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors conduct a benchmarking study on deep learning applied to financial time series forecasting. 


The authors construct a dataset of financial time series, including the price and volume histories of various stocks, options, etc.
On this dataset, the authors pre-train several relevant deep learning (DL) approaches. These models are then fine-tuned to forecast the price and volume of stocks in the S&P500 and CAC40 indices. The authors demonstrate that a naïve baseline outperforms DL approaches on their selected tasks when evaluated using standard forecasting metrics. To address this, they propose an evaluating performance based on the returns and risks associated with using the DL approaches for portfolio management. They find that DL tends to perform better than the baseline under this evaluation.

### Strengths
- The experimental evaluation is thorough, although the authors are encouraged to more completely describe their methodology.
- The authors provide convincing empirical evidence that DL methods struggle to beat baseline methods.

### Weaknesses
 - Although the evaluation of Scinet and DA-RNN on finance data is novel as far as I am aware, the benchmarking of DL on financial data is not novel. For example, [1] evaluates Transformers on several indexes, and also considers the risk/return on trading strategies based on DL forecasts. As the authors point out, their benchmarking submission also does not include comparison to other families of time series forecasting methods.

- While the authors claim to collect a comprehensive dataset, no description is given other than the number of samples. This makes evaluation of the significance and quality of their dataset difficult. Furthermore, while a complete collection of financial price histories could be beneficial to the community, it is ultimately not difficult to assemble publicly available historical price data, making this contribution limited.


- I disagree with the author's characterization that the naïve or LAST baseline (predicting the last known point) has been ignored in forecasting of financial time series. See [2], where a widely used textbook states that the naïve approach works well in financial data. Furthermore, the authors should consider the existence of metrics such as the Mean Absolute Scaled Error (MASE), which compares forecast performance against the naïve one-step forecast model. The M3/M4 papers as cited in this submission also perform evaluation against the naïve baseline. While individual papers in the financial forecasting literature (such as [1]) do fail to make adequate comparison, I believe the authors claims that this is a systemic issue needs further support.


- The authors are encouraged to add more clarity in the writing of this submission. While the flow and core narrative of this submission is clear, it often does not contain enough detail for critical evaluation. Also, table 3 appears to exceed the allowable margins.

### Questions
- The submission would benefit from a brief survey of any existing approaches which evaluate forecasting models based on portfolio performance. Given that the expected return, risk and Sharpe ratio are widely used metrics, it would be beneficial to understand the novelty of the portfolio evaluation proposed in this submission.

- Any rebuttal to the above weaknesses would be appreciated.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article points out the existing imperfection of the evaluation pipeline used for financial time series forecasting. From this observation, the article explores the specific reason hidden in this phenomenon and put forward a brand-new evaluation pipeline based on portfolio construction, whose main idea lies at mapping the predictions of each model to an investment strategy. Based on this new evaluation pipeline, the authors' team test many baseline models' effect in financial time series forecasting task.
The contributions of this article contains:
1. This article introduce a new evaluation pipeline better suited for financial time series.
2. This article compare state-of-the-art deep learning methods for financial time series forecasting based on the brand-new evaluation pipeline.

### Strengths
1. originality: This article is innovative, figuring out the existing problem in evaluation pipeline of financial time series forecasting，and putting forward a brand-new angle to evaluate the effect.
2. quality: The logical chain of this article is relatively complete, from definition of financial time series forecasting problem, the methodology of experimenting, to the final result of their experiments and their conclusions.
3. clarity: The article is relatively clear，but the meaning of many variables involved in formulas are not mentioned, which confused me a lot.
4. significance: The contributions of this article are not significant. On the one hand, the evaluation pipeline put forward in this article only works for financial time series forecasting, which is not general. On the other hand, this article claim they are training a general model which could be used for many specific tasks, but they didn't list any experiment result about this "general model".

### Weaknesses
1. The meaning of many variables involved in formulas are not mentioned. For example, the $P_t$ put forward in section 3, which should be relevant with time step variant $t$, but the formula does not contain $t$. Furthermore, the definition of $R^i_j$ in section 4.4 lacks clarity regarding the index $j$, as the formula appears to be independent of it. The lack of clear definitions for these variables makes it difficult to understand the proposed methodology and assess its validity.
2. This passage is aimed to address the existing problem in the evaluation pipeline of financial time series forecasting, which means one of this passage's key point is putting forward the existing problem, but the problem is mentioned in a paragraph in section 6.1 " FORECASTING EVALUATION RESULTS". It's too "convert" to figure out, making it difficult for me to grasp the logical lines of the entire article. The core issue motivating the new pipeline should be presented much earlier and more explicitly to establish the context for the entire work. The current placement buries the motivation within the results section, which is confusing.
3. The author mentioned that one of the contribution of this article is "We train large models on a large dataset", and "We show that these models can be used to solve more specific tasks". But he did not list the experiment result of these "general models" trained by his team, and there was no experiment result that could prove their general models can be used to solve more specific tasks. The claim about general models lacks empirical support, and the absence of results for these models significantly weakens the contribution of the paper.

### Questions
1. About the definition of $R^i_j$ which is put forward in section 4.4，the formula to calculate $R^i_j$ seems irrelevant with $j$，what's the meaning of $j$ ？
2. About the definition of $P_t$ (the value of a portfolio at time t) which is put forward in section 3，the formula to calculate $P_t$ seems irrelevant with time step $t$，does the time step $t$ influence $x^i_k$，or $w_i$ ？
3. In the experiment, why not control the scale(the number of parameters) of baseline models？If the  scales of baseline models are not consistent，are the result convincing？

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed to evaluate the financial time series forecasting models by deciding which assets to buy and sell, i.e., form a portfolio, according to the prediction, rather than comparing the errors between predictions and ground-truths. The authors collected a dataset from S&P500 and CAC40, and evaluated several forecasting models (e.g., Scinet and DARNN) using the proposed evaluation pipeline.

### Strengths
* In general, the idea of indirect comparison, through the proxy of portfolio optimisation and backtesting, is an interesting alternative to the direct comparison, i.e., on prediction errors.

* The optimisation over Sharpe ratio is reasonable choice under the context.

* The authors found that "LAST", the very simple baseline of always predicting the next value as its current one, is surprisingly hard to beat, which was often ignored in previous works.

### Weaknesses
 * It remains unclear how the datasets were collected. The authors claimed that "we cleverly used web scrapping tools" and the data sources are unknown thus the quality of data might be questionable.

* The transaction cost is not discussed in this paper, so the metrics of portfolio may not be meaningful as the impact of transaction cost is significant, given the reasonably frequent rebalance.

### Questions
The objective function in (1) does not look like a trivial problem, esp. given the non-negative and sum-to-one constraints, what was the optimiser used in this paper? did it converge?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
