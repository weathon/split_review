# Large Language Model Routing with Benchmark Datasets

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
There is a rapidly growing number of open-source Large Language Models (LLMs) and benchmark datasets to compare them. 
While some models dominate these benchmarks, no single model typically achieves the best accuracy in all tasks and use cases.
In this work, we address the challenge of selecting the best LLM out of a collection of models for new tasks.
We propose a new formulation for the problem, in which benchmark datasets are repurposed to learn a ``router'' model for this LLM selection, and we show that this problem can be reduced to a collection of binary classification tasks. We demonstrate the utility and limitations of learning model routers from various benchmark datasets, where we consistently improve performance upon using any single model for all tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper concentrates on the objective of selecting Large Language Model (LLM) from a diverse collection of models for novel tasks. The authors formulate this objective into a series of binary classification problems. The method learns correctness predictors and also defines several scoring metrics to select an LLM given a new task.

### Strengths
Strengths:
1. Formulation: The paper formulates the LLM routing process as a collection of binary classification tasks.
2. Better Performance: The proposed method achieves better results than a strong single model.

### Weaknesses
Weaknesses:
1. Comparison with Existing Methods: The concept of routing is a prevalent strategy in conventional Mixture-of-Experts (MoE) solutions. More comprehensive discussion and  experimental comparisons are encouraged. Specifically, the paper lacks a detailed analysis of how its approach differs from MoE in terms of both methodology and performance. The current discussion does not sufficiently address the nuances of MoE architectures, such as different gating mechanisms and their impact on model selection. A more thorough comparison, including a discussion of the computational overhead and performance trade-offs, is needed.
2. The notation needs more clarification. The definition of $g_m(x)$ is unclear, particularly its relationship to the gold label $y$. The paper should explicitly define the input and output spaces of $g_m(x)$ and clarify how it is trained to predict correctness. The notation in Eq.1 is also confusing, as it appears that $g_m$ is both an independent and dependent variable. This needs to be clarified with a more precise definition of the loss function and its relation to the parameters of $g_m$.
3. Results of "S3 true p" need further practical analysis. These results are only achieved when the model has access to the true accuracy of correctness predictors. The paper should discuss the practical limitations of this assumption and explore scenarios where the true accuracy is not available. The analysis should also include a discussion of the sensitivity of the method to inaccuracies in the correctness predictors and how these inaccuracies might affect the overall performance of the model selection process.

### Questions
1. $g_m(x)$ is defined to evaluate the correctness of model $m$ on an input $x$ and gold label $y$. The lack of$y$ in $g_m(x)$ causes confusion.
2. Eq.1 is a little bit confusing. It estimates the loss of $g_m(x)$ and $y(x,m)$ given $g_m$. $g_m$ seems to be both independent variable and dependent variable. 
3. The problem of OOD in Eq.3 lacks necessary discussion. Eq.3 does not contain notation of $P(y|x)$, it estimates $g_m$. Although the target of $g_m$ is to estimate the correctness of model $m$ that can be potential affected by OOD, there still lacks necessary clarification about what $P(y|x)$ represents in Eq.3.
4. The relation of solution of Eq.4 and OOD is not clear.  
5. There is only one optimization problem, that is Eq.1, to find the best predictor function.  Given the learned $g_m$, the rest of the method is to use $g_m$ to choose the language model. How to design a better predictor also needs more discussion. 
6. This approach takes a lot of efforts on choosing LLMs based on a prediction function. For example, Eq.3 chooses a language model directly based on the prediction of $g_m$. Eq.4 introduces the threshold and can get better generalization results. These tricks are valuable, but some of them are popular in traditional classification methods.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The main contribution of this paper is the proposal of a new problem formulation, which involves using benchmark datasets to learn a "router" model for selecting the best LLM. The authors demonstrate that this problem can be simplified into a series of binary classification tasks, and through experiments, they showcase the practicality and limitations of learning model routers from various benchmark datasets.

### Strengths
This paper showcases the potential of utilizing benchmarks for routing LLMs and explores three model scores in the context of out-of-distribution (OOD) generalization when assigning LLMs to new tasks. It also outlines potential future directions aimed at enhancing the quality and effectiveness of LLM routers.

* * The author propose three scores for selecting LLMs for a new task. Especially, the third score accounts for the OOD data because a new task is more likely to be different from datasets in benchmarks.

* * The routers only depend on the input x, which is different from prior works. It is more efficient if a router don't
need to obtain generations with LLM.

* * The author conducts a robust experiment and provides compelling evidence to demonstrate how an imperfect
correctness predictor can enhance the performance of LLMs.

### Weaknesses
 * * I'm somewhat confused about whether it's crucial to use "imperfect" one if we have a "perfect" correctness predictor. In other words, why do we opt for an imperfect correctness predictor, such as a non-parametric classifier, instead of a parametric one? It's not clear why the choice of a non-parametric classifier is preferred, especially given that parametric models may offer better generalization capabilities if trained correctly, potentially leading to a more robust correctness predictor. The paper should provide a more detailed justification for this design choice, including a discussion of the potential trade-offs between non-parametric and parametric approaches in this specific context.

* * From my perspective, this work bears similarities to the Mixture of Experts (MoE) model, where experts in MoE are replaced with LLMs. So, what is the distinguishes between this work and MoE, where LLMs serve as experts? Would the non-parametric method remain efficient if we use it for the traditional MoE? The paper should clarify how the proposed method differs from MoE, particularly in the context of selecting a single model for a task versus routing individual inputs to different experts. Furthermore, the efficiency of the non-parametric approach in a traditional MoE setting, where multiple experts might be selected, should be discussed, including potential computational overheads.

* * This paper doesn't seem to clarify the difference between this method and certain fine-tuning techniques, nor does it address whether the proposed method outperforms the current fine-tuning methods. If we fine-tune the selected LLM, would it certainly perform better than an LLM that hasn't been selected? Or should we use the selected LLM directly after the router has chosen it? It's crucial to address how the proposed method compares to fine-tuning, especially since fine-tuning is a common practice for adapting LLMs to new tasks. The paper should discuss the trade-offs between routing and fine-tuning, including scenarios where one approach might be preferred over the other. Moreover, it should clarify whether the selected LLM is intended to be used directly or as a starting point for further fine-tuning.

* * The results from the candidate LLMs (Table 5) clearly indicate that larger models outperform their smaller counterparts. This might suggest that the optimal strategy is simply to choose the largest model available. However, I believe this perspective may not be entirely accurate. Therefore, I propose showing more detail to challenge and potentially debunk this assumption. The paper should include a more granular analysis of model performance across different tasks, rather than just presenting average performance. This would help to identify specific scenarios where smaller models might outperform larger ones, thus demonstrating the value of the proposed routing approach.

### Questions
See **weakness**

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims at selecting the best LLM for a unseen task for practical usage. By formaluating the selection of LLM as the binary classification tasks, authors ropose three scores for selecting LLMs for a new task using these correctness predictors. The results on 29 datasets from HELM demonstrate the effectiveness of proposed methods.

### Strengths
The writing of this paper is commendable as it is well-structured and easily comprehensible. The paper addresses a significant problem: how to select the best model from a multitude of language models for a new task. The authors provide comprehensive experimental evidence of the effectiveness of their approach, particularly on the HELM benchmark.

### Weaknesses
I have some concerns that I would like to address in my review of this paper. Firstly, I believe that the application scope of this work may be somewhat limited. The main approach relies heavily on the Large Language Model (LLM) learning from past similar tasks and using that knowledge to measure performance on new tasks. However, I would like to highlight that acquiring the necessary "knowledge" for a slightly larger LLM can be a costly process, requiring evaluation on a large number of benchmarks. Specifically, the method's reliance on extensive pre-existing benchmark evaluations might not be practical in scenarios where such data is not readily available or when dealing with highly specialized tasks that are not covered by standard benchmarks. Additionally, when dealing with a new dataset, an alternative approach could involve evaluating a selection of promising models on a smaller amount of data to identify the best-performing model. This evaluation process can be time-efficient. Thus, the efficiency of different models could also be included

Another concern I have is related to the adequacy of the baseline comparisons. It seems that a simple baseline approach could involve evaluating all relevant LLMs ( < 100) on a very small dataset and selecting the best-performing model.

### Questions
Please see weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper poses the question whether based on existing benchmark performance, one can select the best LLM given a task associated with a dataset. The authors propose to consider the task all in terms of accuracy and train a binary classifier to estimate the task performance for each LLM. More precisely, in this work, the authors study three estimators. 

Empirically, the authors show that the proposed method outperforms best model in average (BMA) as well as an per instance perplexity based baseline. Training an estimator has O.O.D concerns, particularly the objective is to test on a different tasks; the authors have carefully examined and discussed this issue.

### Strengths
The paper is quite easy to follow, even though it presents some non trivial technical details (e.g. Lemma 4.1), thanks to the well organized presentations. 

The paper has shown strong empirical results: not only it outperforms the natural baseline BMA, the best model also outperforms an instance based approach based on perplexity. The approach is shown to achieve near 90% of Oracle accuracy (Table 1). 

The authors have investigated and discussed the prominent O.O.D issues thoroughly in the paper. In Table 1, it shows the oracle accuracy showing the gap. In the paragraphs reducing the OOD gap as well as the discussion, the authors discuss how the phenomenon shows as well how much data might be need to mitigate the issues.

### Weaknesses
The paper seems self contained however:
- it only compares with relatively straightforward instance based approach while in related routing LLM sections, it does mention more approaches but not compare with them.
- The O.O.D problem is well investigated and discussed, however, the authors don't compare with other ways of estimating the accuracy. One popular approach is like G-eval which might overcome the O.O.D issues in some extent.
- There is no clear conclusion that can be drawn from the paper that in practice, what score to use (and with O.O.D score, whether one should use a score). For example, the NN experiments show that S1 performs the best while in Table 1, S3 performs the best. Note that due to the fact that we work on dataset, there is only 28 datapoints. This is not to blame the authors but with this data size and different results, it seems impossible to draw conclusions.

### Questions
For S3, the authors say that "we assign a task descriptor u(d)", what is this u(d) please? I found this a bit confusing since Appendix A further sues u(d) as dataset distance.

By using S3, how many tasks end up using BMA please? Can you comment on the difference between Table 1 and Table 3?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
