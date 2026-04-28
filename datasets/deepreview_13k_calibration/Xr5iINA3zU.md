# Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 3, 6

## Abstract
The increasing presence of AI-generated content on the internet raises a critical question: What happens when generative machine learning models are pretrained on web-scale datasets containing data created by earlier models?
Some authors prophesy \textit{model collapse} under a `{\it replace}' scenario: a sequence of models, the first trained with real data and each later one trained {\it only on} synthetic data from its preceding model. In this scenario, models successively degrade. Others see collapse as easily avoidable; in an `{\it accumulate}' scenario, a sequence of models is trained, but each training uses all real and synthetic data generated so far. In this work, we deepen and extend the study of these contrasting scenarios.
First, collapse versus avoidance of collapse is studied
by comparing the replace and accumulate scenarios 
on each of three prominent generative modeling settings; 
we find the same contrast emerges in all three settings. Second, we study a compromise scenario; the available data remains the same as in the {\it accumulate} scenario -- but unlike {\it accumulate} and like {\it replace}, each model is trained using a fixed compute budget; we demonstrate that model test loss on real data is larger than in the {\it accumulate} scenario, but apparently plateaus, unlike the divergence seen with {\it replace} .
Third, we study the relative importance of cardinality and 
proportion of real data for avoiding model collapse.
Surprisingly, we find a non-trivial interaction between real and synthetic data, where the value of synthetic data for reducing test loss depends on the absolute quantity of real data.
Our insights are particularly important when forecasting whether future frontier generative models will collapse or thrive, and our results open avenues for empirically and mathematically studying the context-dependent value of synthetic data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Update: I appreciate the authors efforts to address my concerns, and thus would like to raise my score. Ideally, I would change it to a 7 b/c I feel it does deserve acceptance but not spotlight/oral. 

This paper studies how training on synthetically generated data in the model-data feedback loop. In particular the authors claim to focus on a more nuanced setting than previous papers on the topic by considering settings where (i) parts of the real-data and synthetic data are used together (instead of discarding the real-data entirely in favor of synthetic), (ii) only a fixed budget is available for updating the model, and (iii) consider how important the proportion vs. cardinality is when updating the model. The authors demonstrate that keeping some of the real data can help prevent collapse, that the right amount of synthetic + real data can improve performance, and in some cases, no amount of synthetic data is outperform real data. The authors provide some proofs to demonstrate their claims too.

### Strengths
- *Important Problem Setting.* The problem of model collapse is a pressing problem and I found the authors investigation into the more nuanced issues of the model-data feedback loop compelling: that likely parts of synthetic and real data will be aggreagated, the budget assumptions etc. 

- *Thorough Experiments.* The authors conduct well-designed experiments on a variety of models and settings, including Gaussian models, kernel density estimators, linear regression and language models on a variety of datasets. While some of these models and datasets are fairly simple, they nonetheless help suport the author's claims. 

- *Theoretical Insights.*  In addition to the empirical insights, the authors are able to proud some theoretical guarantees. This helps complement the empirical results with simpler models.

### Weaknesses
 - * Novelty.* The novelty of this work is fairly limited since it builds quite a bit on existing work. It starts by addressing some of the claims from Gertgrasser et al, and then uses the model/settings in Shumailov et al. The settings the authors tried out (not replacing data en-masse. etc) are important but do seem a bit incremental conceptually.

- *More Real-settings.* The authors motivate their work a fair bit from the perspective of language models. I would like to have seen more experiments on this setting under a couple of different model strengths and synthetic data quality.

### Questions
- Can the authors please clarify their novelty a bit more?
- Can the authors please discuss how they expect their results to hold when training significantly larger models, or changing the quality of the synthetic data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
this work study the model collapse with the sythetic data.

### Strengths
1. The research topic is very interested. It tries to study the model collapse issue when the world have more and more sythetic data due to generative model.

2. The paper contain a lot of experiemts to valdiate their claim.

3. The finding in this work is interesting. they find a non-trivial interaction between real and synthetic data, where the value of synthetic
data for reducing model test loss depends on the absolute quantity of real data.

### Weaknesses
1. the paper starts with MULTIVARIATE GAUSSIAN MODELING, can the findings still hold for other model, like VAE, diffusion model, or Transformer. Somehow,  I feel the paper make too strong claim since there are many generative model.

2. the reprodubility is unclear at this time.

3. the math proof in Appendix is mainly for Guassina model, it is unclear how it can generalize to more generative models.

### Questions
1. the paper starts with MULTIVARIATE GAUSSIAN MODELING, can the findings still hold for other model, like VAE, diffusion model, or Transformer. Somehow,  I feel the paper make too strong claim since there are many generative model.

2. the reprodubility is unclear at this time.

3. the math proof in Appendix is mainly for Guassina model, it is unclear how it can generalize to more generative models.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the impact of iteratively training a generative model on a combination of real and synthetic data generated from a previously trained model. This is an important area of research to explore and understand, as exclusively training models on synthetic data will eventually fail, as highlighted by prior work. 
The authors conduct experiments to validate previous findings, offering new evidence to clarify cases in which model collapse can be avoided. They also explore additional experimental settings in which they control for the ratio of synthetic/real data and the absolute quantity of real data to gain further insight into the limits of training with synthetic data.

### Strengths
1. Motivation. The research question is clearly defined and contextually relevant. Exploring the impact of training with synthetically generated data is important for advancing the field of machine learning.

2. Experiment section. The experiments are thorough, relevant, and insightful. The authors verify that the hypotheses they are testing hold across a wide range of models and data generation processes. They present interesting experiments that control for different parameters, offering clear insights into the scope of the problem. The authors clearly list the questions they aim to answer and provide solid experiments to support their conclusions, along with clear and detailed explanations of their experimental setup.

3. Writing and structure. The paper is well written and follows a logical and clear structure.

### Weaknesses
1. Contribution. The majority of the experimental section (4/9 pages) validates the findings of previous work (Gerstgrasser et al., 2024). The experiments verify that retraining with a mix of synthetic and real data can avoid model collapse in three additional settings. Although it is valuable to reproduce and verify previous findings, this should not constitute the main contribution of a novel work. Emphasizing and clarifying the unique contributions and findings of this paper would strengthen its impact. The core issue is that the paper does not sufficiently justify why these specific settings are noteworthy. The existing literature already contains extensive experiments on model collapse, and the paper fails to articulate why these particular settings are crucial to explore. The paper needs to establish a strong rationale for why the chosen settings are significant, either due to limitations in existing work, specific properties that would challenge previous findings, or practical relevance. Without a clear justification, the experiments appear to be incremental rather than groundbreaking.

2. Presentation. Overall, the presentation of the work could be improved in several ways. First, a clearer discussion of related work to better position this paper's contributions is needed. In the introduction, various papers on model collapse are listed with the comment that they have differing methodologies and conclusions. What are the differing methodologies and conclusions? A brief summary of these differences and a clearer statement of this work's position relative to others is required. This should be easy to achieve as the paper is one page short of the limit, so I am not sure what justifies the almost nonexistent discussion of the listed previous work. Second, the presentation of figures could be improved (e.g., readability of axis labels, font size, relative scaling of the plots). Some figures use notation like 1.2×10^0 instead of simply 1.2, and there is a lot of wasted empty space in the figures. Lastly, there are several errors in the references, as several published works are cited as arXiv references. This gives the impression of an unpolished work.

Minor

1. Some of the writing is needlessly sensationalized. For example, describing "that model collapse is caused by deleting past data en masse and avoided by instead accumulating real and synthetic data" as a "provocative pair of claims" feels excessive. It’s clear that using real data works and that purely generated data does not, so it is not surprising that a middle ground exists. Especially since this finding was already made by previous work. 

2. The use of tweets and LinkedIn posts as references gives the paper an unserious tone, though this may be a matter of personal preference.

### Questions
1. This paper presents iterative settings in which performance either suffers from model collapse (replace) or avoids it (accumulate and accumulate+subsample). Have the authors explored ways to identify the breaking point between these two modes? For example, would the results hold if, instead of adding $n$ samples at each iteration, we add an increasing amount of synthetic data (say, $2n$ each time)?

2. Another question is about the relative quality of the synthetic data. Presumably, there is a connection between how well the model learns the task and whether its generated data can effectively train a second iteration. Do the authors have comments on this?


3. Regarding the observations in the blob experiment, the authors note a tendency: "Interestingly, for specific pairs of datasets and numbers of samples per iteration, training on real data while accumulating synthetic data can yield lower loss on real test data than training on real data alone." For these specific settings where the true distribution is known (I believe that it is the case?), it would be valuable to report the NLL value of the true distribution as a reference point.

4. Have the authors considered extending the result from Theorem 1 to the accumulate-subsample setup? Or relating this result to their experimental results? This could strengthen the contribution of this work.

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the risks of training generative models on datasets increasingly dominated by AI-generated (synthetic) data, studying "model collapse"—where model performance deteriorates as synthetic data accumulates. Through theoretical and empirical analyses, the authors explore when and how this collapse can be mitigated. They test three data-handling approaches (replace, accumulate, and accumulate-subsample) across various generative model settings. Findings suggest that model collapse is avoidable if synthetic data is accumulated alongside real data, and highlight how different ratios of real to synthetic data influence model performance.

### Strengths
1. The studied problem of model collapse under increasing AI-generatd data is prompt and interesting.

2. The theories and empirical studies round up the good work.

3. This paper offers actionable guidance on how to balance real and synthetic data in training.

### Weaknesses
1. Some of the theoretical proofs hinge on idealized assumptions (e.g., independence and Gaussian distribution in certain proofs). These may not fully apply in practical, real-world datasets. Specifically, the assumption of independent data points is a strong one, as real-world data often exhibits complex dependencies. The use of Gaussian distributions, while mathematically tractable, may not accurately represent the underlying distributions of many real-world datasets, particularly in areas like natural language or image processing where distributions are often highly non-Gaussian and multimodal. This discrepancy could limit the applicability of the theoretical results.

2. The "accumulate-subsample" paradigm offers a practical perspective on fixed compute budgets but is tested under simplified conditions. Additional real-world constraints (e.g., dynamic memory handling) are not considered in depth. For instance, the paper does not address how the subsampling strategy interacts with the learning dynamics, such as whether certain data points are consistently under or over-represented during training. Furthermore, the computational overhead of the subsampling process itself, which could be significant for large datasets, is not discussed. The paper also does not consider the potential for bias introduced by the subsampling method.

3. While language models are likely the most relevant generative model for readers, the theoretical analysis does not extend to this model type and is instead focused on Gaussian and kernel density estimation models. Additionally, the size of the language model used in this study is quite small. While contemporary models like Llama range from 7B to 70B parameters, the paper’s experiments are limited to Gemma2 with only 2B parameters. This raises concerns about the generalizability of the empirical findings to larger, more complex models. The limited size of the language model may not fully capture the nuances of model collapse in more realistic settings.

### Questions
1. The study's empirical analysis is limited to a 2B parameter language model. Given the prevalence of larger models like Llama 3 and Mistral, do the authors plan to extend their experiments to these more widely used models to assess the generalizability of their findings?

2. This work primarily explores synthetic data quantity, but the quality of synthetic data is also a significant factor. Would lower-quality synthetic data exacerbate collapse, and could filtering or curating synthetic data mitigate this effect?

### Soundness
2

### Presentation
3

### Contribution
3
