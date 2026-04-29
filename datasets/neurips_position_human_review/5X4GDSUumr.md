# There are no Champions in Long-Term Time Series Forecasting

- Decision: Reject
- Scores: 7, 4, 10

## Abstract
Recent advances in long-term time series forecasting have introduced numerous complex prediction models that consistently outperform previously published architectures.
However, this rapid progression raises concerns regarding inconsistent benchmarking and reporting practices, which may undermine the reliability of these comparisons.
Our position emphasizes the need to shift focus away from pursuing ever-more complex models and towards enhancing benchmarking practices through rigorous and standardized evaluation methods.
To support our claim, we first perform a broad, thorough, and reproducible evaluation of the top-performing models on the most popular benchmark by evaluating five models over 14 datasets encompassing 3,500+ trained networks for the hyperparameter (HP) searches.
Then, through a comprehensive analysis, we find that slight changes to experimental setups or current evaluation metrics drastically shift the common belief that newly published results are advancing the state of the art.
Our findings suggest the need for rigorous and standardized evaluation methods that enable more substantiated claims, including reproducible HP setups and statistical testing.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
The paper shows the important fact that any time series forecasting method on current time series benchmarks, as long as we artifitially choose some 'good' metric and story-telling method, can be tagged as 'champion' compared to baselines; also, current 'model selection' methods are unreliable. Thus, authors argue future benchmarks to improve benchmarks through different approaches; future papers to avoid  wrong claims; and our community to revise model-selection guidelines.

### Strengths
This paper is well-proven with thorough experiments. For example, the authors show possible 'champion cooking-up story-telling method' in these aspects,
(1) plot drawing
(2) Friedman-test-same model achieve questionable champion on MAE
(3) Limited gains of model complexity
(4) Hyper Parmeter sensitivity
(5) Metric sensitivity.

For model selection methods, authors show that:
(1) Model rankings are highly sensitive to dataset and horizon selection through 5000 repeated experiements.
(2) Current model selection methods need improvement.

Overall, this paper has conducted very thorough and solid experiments from various aspects, supporting its claims quite well.

### Weaknesses
The authors have discussed very thoroughly how fragile current benchmarks are with respect to hyperparameters and evaluation pipelins, which is good. However, current benchmarks are lacking in quite many domains. For example, (1) traditional methods may outperform current 'sota' DL-based methods, implying DL methods are only learning trival things; (2) lack of related contexts (e.g. perhaps news for finance, perhaps geometry information for weather forecasting).

### Questions
The authors have proposed the lack of current TSF benchmarks. I am perhaps more aggressive than the authors. I am in the TSF community, but I wonder: whether general-purpose TSF makes sense?

Let me give an example. The best weather forecasting AI method is probably using some 3D-ViT based methods with multimodality inputs. The best financial AI method is perhaps some ensemble of Features+Trees, some end2end methods. If there does not exist such 'general' TSF model surpassing these domain-specific sotas, is so-called 'general' TSF model worth studying? If we view weather as time series, if we view finance as time series, if we view NLP as time series, does it mean that we can find some TSF-based methods that can surpass GPT/Gemini/etc. on NLP, surpass best QT firms on Finance, and surpass the best methods for weather forecasting?

### Presentation
4

---

## Human Reviewer 2

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
This paper advocates the position that there is no absolute best model in time series forecasting domain at the moment and the performance of the model varies across dataset and often differs based on what evaluation metric to use to measure performance. The authors recommends that, instead of developing more and more complex time series forecasting model, the researchers should focus on improving benchmarking standards with more rigorous evaluation metrics, statistical testing or comprehensive experimental design.

### Strengths
1. The paper present a clear, concise and well articulated position. The position is timely and would spark discussions in the domain of time series forecasting.
2. The authors emphasis on the need of better benchmarking through more diverse and relevant real-world time series forecasting datasets, just like ImageNet in Image Classification domain, is convincing.
3. The focus on more statistical testing to find out best performing model is an important recommendation for time series forecasting domain.
4. The authors experimentally proven that more complex model does not necessarily outperform simpler models in many challenging use cases.
5. The authors provide a detailed experimental analysis to show how sensitive the state of the art models are across the dataset and why the future studies need more focus on robust hyper-parameter tuning and re-producible experiments in the time series forecasting domain.

### Weaknesses
1. This paper started the initial discussion with a strong and bold position. However, the arguments and recommendations made by the authors did not comprehensively and completely develop throughout the paper. 
2. Even though the authors highlight the loopholes or issues with existing evaluation metrics widely used in the time series forecasting community, they did not strongly recommend why this metric fails technically and what should be the exact technical way of using such metrics in future time series forecasting research. 
3. The authors spot on the need for more representative time series forecasting datasets, but they don't really guide the researchers on how to build those more robust datasets, what to avoid when developing those datasets, what to include, etc. 
4. The authors tell us in the beginning that we should divert our focus on building more complex models because even simpler architectures like DLinear do pretty well across benchmarks, but it is not clear why more complex architectures are not able to do better (what is wrong fundamentally) and what we should keep in mind when designing next models.
Overall, the paper lacks depth in discussion and analysis.

### Questions
1. The foundation models research in the "Alternative Views" section was interesting to me at the start, but why did it end in a surface-level analysis without any detailed explanation and sufficient relevant evidence from the literature?
2. It is not clear to me if the authors at the end recommends the researchers to come up with more generalized time series foundation models which can outperforms with a significant margin. Or do the authors believe that it is simply not possible to design such methods in the near future because of the inherent diversity of the datasets coming from diverse domains?
3. After reading this paper, it is clear that the time series forecasting models are more or less indistinguishable in each and every dataset. But if that is true, then what should the future researchers do? 
4. I did not find multiple strong and convincing pieces of evidence in the literature to employ the mentioned statistical tests to determine model superiority. I believe we need a more comprehensive and technical explanation to determine why the existing popular metrics are failing to identify the best model in a more robust manner. What's your take on this?

### Presentation
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper offers a constructive evaluation of Long-Term Series Forecasting by conducting evaluations across 5 models from 14 different data sets. They found that although there are claims of continuous improvement, these claims rely on specific circumstances, and that no one model consistently outperforms the others. They offer recommendations of standardizing evaluations, increasing benchmarking robustness, and examining the impact of underlying data quality on model performance.

### Strengths
The strengths of this paper include strong arguments for its position and a large amount of testing to provide support for its position. The paper is timely and organized clearly.

### Weaknesses
NA this paper was comprehensive and rigorous.

### Questions
This paper covered many subject areas for application. Are there certain areas that would benefit more or are more immediately in need of more rigorous benchmarking and evaluations from the research?

### Presentation
3
