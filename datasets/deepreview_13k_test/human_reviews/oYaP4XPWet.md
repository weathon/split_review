# Training and Evaluating Causal Forecasting Models for Time-Series

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Deep learning time-series models are often used to make forecasts that inform downstream decisions.
Since these decisions can differ from those in the training set, there is an implicit requirement that time-series models will generalize outside of their training distribution.
Despite this core requirement, time-series models are typically trained and evaluated on in-distribution predictive tasks.
We extend the orthogonal statistical learning framework to train causal time-series models that generalize better when forecasting the effect of actions outside of their training distribution. To evaluate these models, we leverage Regression Discontinuity Designs popular in economics to construct a test set of causal treatment effects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper concentrates on using orthogonal learning for causal inference and forecasting, for the case of time-series. The paper is well written overall, combining theoretical results (mostly relying on the work of others, e.g., as in the proofs) and empirical investigations. It provides a set of interesting results related to both learning and evaluating forecasting approaches in a causal framework. I find that the paper makes some novel and potentially valuable contribution.

### Strengths
It is great to see that the authors focus on both theoretical results and using empirical investigations (for 2 different cases) to explore their approach. It is mostly an extension to existing ideas and methods (e.g., orthogonal learning, for time-series), but still in a way that makes it very valuable since time series learning and forecasting is a very broad field for which any improvement can make a high impact.

### Weaknesses
Even though the paper is well written, it is also very compact overall, and difficult to read at stages. Already the motivations could be better developed, as well as the justification for orthogonal learning. Personally, I felt quite frustrated with the readability of the paper. Besides quite a number of points that could be improved in terms of presentation (citation style for references and equations), the flow of the paper is difficult to follow at stages. This is possibly due to page limitations, but still, the authors could have chosen to lighten the introductory parts, in order to leave more room for the novel developments in the paper. Also in terms of the presentation, some of the methodological parts are written as if we only consider a specific application (e.g., mentioning daily prices as treatment at the top of page 5). However, different applications are presented in the empirical investigation part. Maybe there could be some additional effort made with the writing, to make the paper easier to read and to better separate purely methodological considerations and developments from application-specific considerations.

### Questions
My suggestions would include:
- improving the presentation (especially citations to references and equations)
- improving the way the methodology is presented, so that it does not need to rely on discussing a specific application
- be clear about why we care about improving RDD RMSE - especially here, the TST baseline in table 1 (which does not rely on any causal inference approach) seems to be as competitive as the bespoke causal approaches...

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an alternative loss function for training causal deep learning models to estimate conditional average treatment effects (CATE) over time - through the use of orthogonal learning to directly learn the CATE from data under unconfoundedness assumptions. Losses are applied over a customised TFT architecture for time series predictions, and they demonstrate improvements using Regression Discontinuity Design (RDD) experiments.

### Strengths
While many architectures have been proposed for time series forecasting in general, causal temporal models have been relatively understudied by comparison. The paper is also well motivated and clearly presented — with the use of orthogonal learning being an interesting approach, and use of the TFT being sensible to incorporate a wider range of inputs. The outline of the RDD evaluation approach is also useful, providing a way to evaluate causal temporal models on live observational data.

### Weaknesses
However, the performance improvements do appear slim, with the causal TFT underperforming the causal transformer on both on all in distribution time-steps and 2/5 of the RDD forecast horizons. Where improvements exist, it is also not immediately clear if they are attributable to the improved loss function or the use of the TFT — with the novelty of the former far out-weighing the latter.

### Questions
1. How does the causal TFT compare to other models under the original simulation framework used to evaluate Melnychuk 2020, Bica 2020 and Lim 2018?  While more simplistic, it makes it easier to control the degree of bias present in policies, which could widen performance gaps (vs the slim margins seen in the RDD experiments).
2.  Where improvements are seen (i.e. shorter time steps in RDD expts), are these attributable to the use of TFT or new loss function proposed?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper highlights the need for time series models to showcase generalization to out-of-distribution data, where the relationship between treatment and outcome differs from the training data. To this end, the authors propose extending the orthogonal statistical learning framework to train causal forecasting models that can capture changes in outcome based on changes in treatment outside of the training distribution. Due to a lack of out-of-distribution evaluation of existing time series models, the authors propose to evaluate out-of-distribution by creating a test set of causal treatment effects using Regression Discontinuity Designs (RDD).

### Strengths
1. This work has real-world applications and has the potential to improve decision-making processes that depend on forecasts from time series models.
2. The two extensions to adapt the orthogonal statistical learning framework to train causal models—defining daily treatment effects and extending the binary treatment effect data model to categorical and linear treatments—are mathematically justified.
3. Despite the complex approach and new terminologies introduced, the paper is well-structured and relatively easy to follow.

### Weaknesses
1. T_t for treatment at time t, and T_1, T_2 ​ for treatment types can be confusing.
2. The evaluation method using RDD is complex and may generate only a few test set examples.

### Questions
Why are more datasets not considered for evaluation?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors argue that current deep learning approaches to time series modeling are limited by not explicitly modeling causality. To remedy the situation, the authors propose a framework to convert neural network time series models into causal models by fitting a conditional average treatment effect (CATE) model on a temporally held-out dataset. The authors demonstrate how to use orthogonal learning to construct the CATE model and model high-dimensional treatment using 3 different encodings (one-hot, cumulative, and linear). To evaluate the models, the authors construct ground truth CATEs using regression discontinuity designs (RDDs), which use a temporal cutoff to create examples with and without a specified treatment. The authors then show that while non-causal models perform well in terms of RMSE and MAE in distribution, they perform poorly on recovering the CATEs constructed using RDD and domain knowledge. The authors then conclude that their causal models are superior in settings with clear causal relationships.

### Strengths
The authors pursue an interesting synthesis of methods from deep learning for time series and statistic tools for treatment effect prediction.  Certainly there are many cases in time series where there might be nuisance variables that lead to unexpected behavior out of distribution, and in cases where there is domain knowledge about these nuisance variables, this method might be helpful.

### Weaknesses
Overall I found the paper pretty challenging to parse, for example how exactly the models were constructed and evaluated. I am not a domain expert in casual methods, but I work in machine learning and time series modeling, and I don't think the material was so technical that its complexity was the source of the problem, so sections 2-4 might benefit from some reworking to make the key details more salient.

Beyond style, I take two of the central claims of the paper to be:

(1) Adding causal modeling to neural network time series models helps in practical out-of-distribution scenarios

(2) Estimating CATEs in a time-series setting is novel and necessitates methodological innovation

I don't have enough domain knowledge to fully assess (2), but I am currently unconvinced that the paper demonstrates (1). The evaluation of the model seems a little circular in that the examples are special designed using a similar procedure to the method being evaluated. Perhaps I'm misunderstanding, but I take the evaluation to be whether the causal predictions of the model match a linear RDD analysis. If this is a misunderstanding, a correction might be helpful. If I've understood correctly, when would we be better served by apply the methodology in the paper than just applying the linear RDD analysis directly? This evaluation also seems limited to cases where the causal structure of the problem is known and the changing covariate (e.g. price) is observed. How does this solve prediction in out-of-distribution settings? There is also no explicit evaluation on out-of-distribution data using the method, even though this was one of the stated motivations in the introduction.

For (2), the contribution appears to be mostly the encoding of the treatment and the treatment effect \theta(W_t), because the other tools seem to be borrowed directly from related work. There are some additional proof that those tools can be extended to this setting, but as far as I can tell, the crux of the method is combining a pre-trained time series backbone with existing statistical. Please correct me if this is a misunderstanding. Further from the evaluations that were presented in the results, the method's performance is nearly identical to the baseline for several of the encoding, in terms of the causal evaluation, and its general forecasting performance is worse. What is the practical take-away from this evaluation? What are the settings in which I would want to adopt this method as an alternative to simpler deep learning forecasting methods given that it performs worse in-distribution and there is no explicit out-of-distribution evaluation? In terms of predicting CATE, how can this be used beyond recapitulating the known effects of known treatments?

### Questions
I have outlined some potential confusions and questions in my "Weaknesses" section response.

### Soundness
3

### Presentation
2

### Contribution
2
