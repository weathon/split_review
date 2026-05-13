# AutoScale: Automatic Prediction of Compute-optimal Data Compositions for Training LLMs

- Decision: Reject
- Scores: 6, 8, 3, 5

## Abstract
Domain reweighting is an emerging research area aimed at adjusting the relative weights of different data sources to improve the effectiveness and efficiency of language model pre-training. This paper demonstrates that the optimal composition of training data from different domains is scale-dependent, challenging the existing practice of determining optimal mixtures through small-scale experiments and directly applying them at larger scales. We derive an analytical model for the dependence of optimal weights on data scale and introduce \textsf{AutoScale}, a novel, practical approach for optimizing data compositions at potentially large training data scales. \textsf{AutoScale} first uses a principled optimization framework to find optimal compositions at smaller, feasible scales, then predicts optimal compositions at larger scales using our derived model. Our evaluation on GPT-2 Large and BERT pre-training demonstrates \textsf{AutoScale}'s effectiveness in improving training convergence and downstream performance. Particularly, for GPT-2 Large on RedPajama, \textsf{AutoScale} decreases validation perplexity 28\% faster than baselines, with up to 38\% speed-up over unweighted training, achieving the best performance across downstream tasks. This work provides insights into the varying benefits of data sources across training scales for language models, contributing to the burgeoning research on scale-dependent data curation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors address an interesting topic in this paper: a method for automatically optimizing the mixture proportions of pretraining data domains when training language models. 
They begin by formulating the optimal mixing problem as a bi-level optimization and then propose the Direct Data Optimization (DDO) algorithm to formalize the relationship between optimal data compositions and training data scales. Using DDO, they conduct empirical studies to optimize domain weights at various training data scales, demonstrating that the optimal data composition varies with the scale of the training data. Finally, they introduce AutoScale, which automatically predicts optimal training data compositions at larger scales based on compositions optimized at smaller scales. 
Additionally, their evaluation of AutoScale on both decoder-only and encoder-only models demonstrates its ability to achieve computational savings.

### Strengths
1. AutoScale presents an interesting idea that distinguishes it from previous work, demonstrating that the optimal weights are only effective at the scale they were optimized for and become suboptimal when applied to other scales. It offers a practical method for automatically and efficiently determining domain weights when train large language models. 
2. The experiments are conducted on both encoder-only and decoder-only models and shows good results on decoder-only model. 
3. The work is supported by both empirical experiments and mathematical formulations. Additionally, the diagram in the paper is well-designed and effectively conveys the underlying concepts.

### Weaknesses
1. The experimental setup is not entirely convincing:

* The models used (a 774M decoder-only model and a 110M encoder-only model) are relatively small compared to today’s large language models, making it difficult to gauge performance at a larger scale. The limited model sizes raise concerns about the generalizability of the findings to the scale of models typically used in current research and applications. Specifically, the observed optimal data compositions might not hold for models with billions or trillions of parameters, which are more common in state-of-the-art language modeling.
* The data size is limited to 3B, 5B, and 10B tokens, with results in Table 1 only reflecting the 3B set. This restricted data scale makes it challenging to assess the effectiveness of the proposed method on larger datasets. The optimal mixing proportions could vary significantly with increased data volume, and the current experiments do not fully explore this aspect. Furthermore, the lack of results for the 5B and 10B token datasets in Table 1 makes it difficult to understand the performance trends as the training data size increases.
* Figure 3(b) lacks explanation, and the cola baseline and DDO performance seems unusually low, falling below random guessing (0.5). Also, stsb baseline seems low too. The performance of the baselines on the CoLA and STSB tasks is concerningly low, suggesting potential issues with the experimental setup or evaluation metrics. The fact that the CoLA performance is below random guessing indicates a fundamental problem that needs to be addressed. The low baseline performance on STSB also raises questions about the validity of the comparison between the proposed method and the baseline.

2. The evaluation of downstream tasks could be expanded. It would be helpful to see the models' performance on more complex tasks, such as mathematical problem-solving. The current evaluation focuses on standard GLUE tasks, which may not fully capture the capabilities of the models trained with the proposed method. Evaluating on more challenging and diverse tasks, such as mathematical reasoning or complex question answering, would provide a more comprehensive assessment of the model's performance and generalizability.

### Questions
1. If I understand correctly, for the downstream tasks, the evaluation metric used is perplexity. Why is perplexity chosen as the metric instead of one that is specific to the dataset or task itself?
2. Is there any potential explanation for why AutoScale doesn't perform as well on encoder-only models compared to decoder-only models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of predicting optimal data mix for a given compute budget (i.e., fixed total token count and model size). A key challenge here is that the optimal domain weighting may change at different scale, hence it is inaccurate to use smaller models to predict large model performance, while solving the optimization problem at the large model scale directly is computationally infeasible (requires multiple retraining).

The paper proposes a method that work on one domain at a time by fixing the rest of the data constant (hence the loss is constant for other domains too), and estimated a scaling law per domain. The power law parameters $\gamma_i$ and $l_i$ can be easily estimated, which approximate a regular data scaling function where $l_i$ is the irreducible loss of that domain. 

After the power law of each domain is found, the final objective is to mix the data so that the loss is minimize while keeping sum of the tokens reaches the budget, which becomes a convex function that can be solved efficiently. This gives the DDO method. The different $\gamma_i$ explains why there is a differet mix at different stage.

A method "AutoScale" is further proposed to obtain the data weight of a larger token budget, by iteratively mxing two data weights at different scale to create the weights of the next one. 

The proposed approach is tested on models like GPT-2 (autoregressive) and BERT (bidirectional), showing improved convergence rates and downstream task performance. Empricially, the results show AutoScale’s ability to shift data weights, favoring diverse data sources like CommonCrawl at larger scales while reducing reliance on traditionally high-quality, standard-format data such as Wikipedia. These findings match the empricial findings of the data weights used for prior succesful models such as Llama.

### Strengths
- This paper analyzes an important problem, data weighting of LLM training, which can improve the training efficiency with reasonable cost. It also presents an actionable algorithm for LLM training.
- The proposed method assumes a power law formulation which makes the data weighting problem practically solvable. It is important to point out that data weights is scale dependent.
- The empirical results and findings on the corpus weighting align with common belief of the community, such that further up-weighting high quality source is less effective, and books and web documents continue to be important at larger scale. This shows that the proposed method has strong explanatory ability.
- The experiment is quite thorough, considering the cost for training models is quite high even at small scales.

### Weaknesses
In general, the writing is difficult to parse. It is frequently frustratingly vague, including in the Abstract, where the actual method is alluded to but not elucidated. In the actual methods section, important questions about the method are unanswered, leaving the method underspecified. The learning rate schedule (linear? presumably linear decay?) is not explicitly stated for the tuning runs, nor is it clarified if it is the same as for the final run. Whether the decay timing is adjusted to the compute budget is also not mentioned. The value of the final validation loss hinges critically on these details - yet they go unmentioned. There is no addressing of the profound difficulties this method (and others like it) can be expected to have around epochs for individual datasets. A more thorough analysis would identify and investigate this issue with experiments demonstrating specific datasets being sampled for > 1 epoch, and the subsequent breakdown of the "scaling law" prediction. Evaluation is purely comparative to other methods, and does not assess to what extent the predicted 'optimal' values might differ from more expensively traditionally-derived 'optimal' values. No discussion of the relative cost of the method (with its 'linearly scaling' cost in the number of datasets) is mentioned, though it is clear it would become prohibitively expensive for dataset mixtures with more than a handful of individual datasets. The method proposed is prohibitively expensive at large model sizes, and seems unlikely to scale to larger compute budgets even at small dataset sizes due to the issue of datasets passing through multiple epochs, which is unaddressed in this work. This limitation goes unmentioned.

Fig 1: [a] suggests that you've tuned 6 models between 30M and 1.2 B tokens, yet [c] shows only three models being used to fit the predictor model. Why is that? where are the other data points? And are *all* of the linear fits R2=0.998? Is that the average R2? Also, [d] shows the predictions of the model extrapolated past 1.2 B to 307 B? Why are you not showing the training data points (between 30M and 1.2 B) as well? And isn't the largest model you look at trained to 10B? why show this extrapolation to so far beyond where you explore? This seems misleading. The x-axis should say (log scale) as well. In [b] the color used for the 1.2B model is the color used for the 0.6B model in [a]. And there is a typo in the title ('scale - depedent' -> "dependent"). In [e] the 38% improvement looks to be overstated due to the noise of those evaluation curves, you could just as easily pick out the peak in Autoscale curve at step 86k and the point in the Uniform curve at step 100k to get a smaller improvment result with the same underlying data. 

Table 1: boolq has the Autoscale value bolded as 'best' but the Data Mixing Laws value is greater. Also, consider place your method on the bottom row separated by a thin line.

Fig2: What is being depicted here? Is this showing power laws being fit to 3 empirical datapoints? Is the first column of points supposed to be at 0? It looks like the points are at [0.2, 1, 3] on the x-axis?


Nits:

Throughout: "AutoScale" is consistently the wrong font size. Please fix. Similarly, in section 5.2 the font size of the methods needs to be fixed. And in line 418 'from' is included in the method font instead of the default font.
181: work contribute -> contributes
379: N^(1)* is missing the N in summation
465: much lowered -> much lower
155 'a consistent shift can be observed', please be more specific, what is shifting, how is it consistent?

### Questions
- I am a bit unclear about your definition of "equivalent data size" at L243, what's the equivalence about (i.e., which size and which size)? Note that I understand the meaning of $N_I^0$, just wondering the terminology here.
- Maybe I missed something, but how do one control the budget for the next $N^(3)$? It seems the amount of tokens is defined by the initial weights of  $N^(1)$ and $N^(2)$. Or in other words, say I need to find a optimal weight for a total token of 300B, how should I start with $N^(1)$ and $N^(2)$?
- Adding to the prior question, if the optimal ratio of each domain follows a exponential function, after taking a few data points using AutoScale, can we simply fit the exponential function instead of using the AutoScale iterative method? You seem to be using that in Figure 1 (d). If y es, this simply answer my question above.
- While the problem of different data scale is resolved with a scaling law solution, can we also use a similar approach on model scale? Even though the cost of using a small amount of data for a larger model should be within a low percentage of the total training cost, setting up the experiment for the larger scale is non-trivial. It'd be nice to have a function that can predict the loss across model scales.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This work presents a method to estimate optimal data domain weights at large training-data scales by extrapolating via exponential functions fit to smaller-scale training runs. The proposed method is evaluated on GRT-2 Large + RedPajama and BERT pretraining, and compared to extant method baselines.

### Strengths
The general problem the authors attempt to address is important, and the assessment that present methods are limited and that performance headroom is available is well-framed. The code is open-sourced. The evaluations presented are limited, but positive.

### Weaknesses
I would like to list the following weakness fully ensuring the authors that I am not unreasonable and am completely open to increasing my score if these are addressed/answered satisfactorily.
* The work proposes using a different approach to finding optimal data weights for a given pre-training compute budget. This is well explained via results but does in fact require training the original size model. Given that we obtain suboptimal performance via the conventional way( smaller model, fewer data), an analysis showing how much performance could be gained by spending the compute and training these (equal parameter) networks would be useful. A comparison against simply training a model of the same size using the same total compute budget but with a uniform data distribution would help quantify the advantage of the proposed method.
* For Takeaway 1, Fig 1(b) only has 2 data points. Additional points would help make the case stronger. It’s a tough sell to make such a bold statement with two data points. But I’m hoping I am wrong :)
* Maybe I missed this, but the repeated claims that Wikipedia should be sampled less at a higher scale is a result of the OLS fit. But no experiment actually confirmed this fact in the paper, right ? Since the max scale was 1.2B ? Please correct me if I’m wrong.

General Comments/Typos:
* [Section2] :  “this work contribute”  -> “this work contributes”
* [Section 3.1] : wi = Ni/N => wi = Si/N ?
* [Algorithm 1] : Train the model on data S = ({S1 . . . Sm} \ Si) => S = ({S1 . . . Sm} \ Sj) ? 
* Some of the font sizes are very distracting to read.

### Questions
Fig 1: [a] suggests that you've tuned 6 models between 30M and 1.2 B tokens, yet [c] shows only three models being used to fit the predictor model. Why is that? where are the other data points? And are *all* of the linear fits R2=0.998? Is that the average R2? Also, [d] shows the predictions of the model extrapolated past 1.2 B to 307 B? Why are you not showing the training data points (between 30M and 1.2 B) as well? And isn't the largest model you look at trained to 10B? why show this extrapolation to so far beyond where you explore? This seems misleading. The x-axis should say (log scale) as well. In [b] the color used for the 1.2B model is the color used for the 0.6B model in [a]. And there is a typo in the title ('scale - depedent' -> "dependent"). In [e] the 38% improvement looks to be overstated due to the noise of those evaluation curves, you could just as easily pick out the peak in Autoscale curve at step 86k and the point in the Uniform curve at step 100k to get a smaller improvment result with the same underlying data. 

Table 1: boolq has the Autoscale value bolded as 'best' but the Data Mixing Laws value is greater. Also, consider place your method on the bottom row separated by a thin line.

Fig2: What is being depicted here? Is this showing power laws being fit to 3 empirical datapoints? Is the first column of points supposed to be at 0? It looks like the points are at [0.2, 1, 3] on the x-axis? 


Nits:

Throughout: "AutoScale" is consistently the wrong font size. Please fix. Similarly, in section 5.2 the font size of the methods needs to be fixed. And in line 418 'from' is included in the method font instead of the default font.
181: work contribute -> contributes
379: N^(1)* is missing the N in summation
465: much lowered -> much lower
155 'a consistent shift can be observed', please be more specific, what is shifting, how is it consistent?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes a method called “AutoScale” that helps predict the optimal composition of pre-training data for LLMs. It challenges the conventional notion of determining this via small scale experiments and simply applying them to a large scale where two axes change (data scale, parameter count). The experiments show a very promising line of research and it was a pleasure to read. 

I couldn’t check the math as well as I would have liked to.

### Strengths
* Very strong work in terms of the hypothesis and experimental setup albeit at smaller scales. The promise of finding optimal weights for training large networks without having to guesstimate it is a very attractive proposition. 
* The plots are really well done. They drive the main idea of the paper very well(especially Fig 1 (a, e) )

### Weaknesses
I would like to list the following weakness fully ensuring the authors that I am not unreasonable and am completely open to increasing my score if these are addressed/answered satisfactorily.
* The work proposes using a different approach to finding optimal data weights for a given pre-training compute budget. This is well explained via results but does in fact require training the original size model. Given that we obtain suboptimal performance via the conventional way( smaller model, fewer data), an analysis showing how much performance could be gained by spending the compute and training these (equal parameter) networks would be useful. 
* For Takeaway 1, Fig 1(b) only has 2 data points. Additional points would help make the case stronger. It’s a tough sell to make such a bold statement with two data points. But I’m hoping I am wrong :) 
* Maybe I missed this, but the repeated claims that Wikipedia should be sampled less at a higher scale is a result of the OLS fit. But no experiment actually confirmed this fact in the paper, right ? Since the max scale was 1.2B ? Please correct me if I’m wrong.

General Comments/Typos:
* [Section2] :  “this work contribute”  -> “this work contributes”
* [Section 3.1] : wi = Ni/N => wi = Si/N ?
* [Algorithm 1] : Train the model on data S = ({S1 . . . Sm} \ Si) => S = ({S1 . . . Sm} \ Sj) ? 
* Some of the font sizes are very distracting to read.

### Questions
* Even at a smaller scale, I see opportunities of clear promise where we could have had more points between 0.3B and 1.2B and show some trend. Any specific reason this was not done/ increased to more than 1.2B ? With scale, a lot of problems disappear that are apparent at lower scales.

### Soundness
3

### Presentation
3

### Contribution
3
