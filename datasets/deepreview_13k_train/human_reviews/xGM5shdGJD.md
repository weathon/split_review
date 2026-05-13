# A Hitchhiker's Guide to Scaling Law Estimation

- Decision: Reject
- Scores: 3, 8, 6, 3, 6

## Abstract
Scaling laws predict the loss of a target machine learning model by extrapolating from easier-to-train models with fewer parameters or smaller training sets. This provides an efficient way for practitioners and researchers alike to compare pretraining decisions involving optimizers, datasets, and model architectures. Despite the widespread use of scaling laws to model the dynamics of language model training, there has been little work on understanding how to best estimate and interpret them.
We collect (and release) a large-scale dataset containing losses and downstream evaluations for 485 previously published pretrained models. We use these to estimate more than 1000 scaling laws, then derive a set of best practices for estimating scaling laws in new model families.
We find that fitting scaling laws to intermediate checkpoints of training runs (and not just their final losses) substantially improves accuracy, and that---all else equal---estimates of performance are generally most accurate when derived from other models of similar sizes. However, because there is a significant degree of variability across model seeds, training multiple small models is sometimes more useful than training a single large one. Moreover, while different model families differ scaling behavior, they are often similar enough that a target model's behavior can be predicted from a single model with the same architecture, along with scaling parameter estimates derived from other model families.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on understanding good practices for fitting scaling laws for language models. The paper first collects and releases a large-scale dataset containing losses and downstream evaluations for published pretrained models. Then it uses this dataset to estimate scaling laws and understand the nuance in how to estimate the scaling law.

### Strengths
- The paper organizes and releases a dataset covering existing model’s losses and other information for the study of the scaling laws.
- The paper has taken a detailed approach to understand the relationship between different model families’ fitted scaling laws’ similarities, how to estimate the scaling law for a new model using limited amount of training runs.

### Weaknesses
The main weaknesses of this paper, from my point of view, are its practical usefulness and its presentation.

- **[Practical usefulness]** Scaling laws are most useful when the target model whose performance to be predicted require much larger compute than the set of smaller models (with varying tokens, parameters, compute) that can be feasibly explored. This paper performs eval only on the largest models within the model family. So it’s not clear to me how big are the set of the second largest models used for scaling law fitting. In contrast, for Llama 3’s scaling law experiments, their small-scale training runs have compute budget up to $10^{22}$ FLOPS but they use the fitted model to guide the allocation of parameter and token to train the 405B model under $3.8 \times 10^{25}$ FLOPS of compute budget.
    - Besides, although I find the problems explored by the authors on how to build on existing scaling laws and use only limited amount of new model runs to fit scaling laws to be interesting, I’m not sure whether such approaches would be seriously considered by practitioners who want to use scaling laws to train large models. As the authors have shown, over certain regimes, not doing the scaling law fitting by generating a lot of small scale model training runs could be less accurate. I would appreciate the authors’ comments on when they think the approaches explored in Section 5 and 6 would be practically useful.
- **[Presentation could be further improved]**
    - **[Notation]** I find some of the notation used in the paper can be changed to improve readability. For example, $\max_{\# \textrm{params}} (F)$ is used to represent the set of functions $f$ with maximum number of parameters. I find this notation to be a bit unintuitive. The same is true for $\max_{\#\text{toks}}(F, q)$.
        - In addition, on line 317, page 6, I think $\hat{L}(\cdot \mid F_{\textrm{train}})$ is meant to mean the **loss** of the largest-compute model, but the current notation defines this to be the **function** that uses the largest compute.
    - **[Figures]** In terms of figures, I think the table representation is a bit difficult to interpret, especially the color bar’s choice as well as the isoFLOP contours. Besides, Figure 6 and 7 in the Appendix have overlapping numbers, which make them difficult to read.
    - **[Codebase]** Because the authors mention the database is one of their contributions, the current codebase is a bit poorly documented, which makes me think they are unready to be used as a public benchmark for follow-up works.
    - **[Organization]** Some discussion of Figure 1 (on page 3) is later on discussed on page 9. I think this could potentially be reorganized to improve the flow of the paper.
- Minor:
    - I think it is incorrect to say the intercept $E$ in the scaling law is the “baseline”. Instead it’s actually the best loss this fitted model class can do given infinite compute and parameters.
    - There is a redundant “future work” on line 436.

### Questions
- In terms of the equation on line 164, the paper uses squared error as the loss. But Hoﬀmann, 2022 (Chinchilla) uses Huber loss to make the objective more robust to outliers. Can the authors explain why they don’t consider outlier-robust losses?
- The authors mention the intermediate losses could have spikes or increase, making them less useful as regression target. I wonder if the authors have considered applying outlier removal/smoothing of the losses before the scaling law fitting.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
This paper studies the estimation of scaling law of large language models. The authors build a dataset containing losses and evaluation of pretrained models, and run estimation of scaling laws on this dataset. The authors arrive at some interesting findings that covers different aspects of scaling law estimation, e.g. the reliability of extrapolation, the use of partially trained model, the difference choices of model sizes.

### Strengths
1. The authors build and release a dataset that is useful for the reproduction and further analysis of the results. 
2. The authors provide a systematic empirical study to the scaling laws. The empirical results in this paper lead to a vast number of implications on scaling law estimation. Some of them are novel to me.

### Weaknesses
I am not en expert in this field, and the paper looks overall good to me. My major concern is that readability can be improved. Many of the results and conclusions are not clearly explained, and require experiment results that are scattered across the paper and appendix, e.g., section 5.1. I would encourage the authors to reorganize the experiments and conclusions part of this paper. Specifically, the connection between the experimental setup, the observed results, and the conclusions drawn is often unclear. For instance, in section 5.1, it's difficult to immediately grasp how the specific choices of model sizes and training regimes directly lead to the stated conclusions about extrapolation reliability. The lack of clear signposting between different parts of the analysis makes it challenging to follow the overall narrative and appreciate the significance of each finding. The paper would benefit from a more structured presentation of the experimental results, with each experiment clearly motivated, described, and then linked to the corresponding conclusions.

### Questions
See weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work attempts to provide a set of guidelines for employing Neural Scaling Laws (NSL) with #of parameters (P) and #of data tokens (N) in training large language models (LLMs). Concretely, the authors perform downstream inference to compute the test loss for a wide range of LLMs, curating a new dataset which can be used for practitioners and theorists who are interested in scaling laws. The authors then define their target model as the largest possible model which has been trained and study the convergence of NSL predictions to the target performance. From analyzing their data, the authors subsequently give general best practices regarding several important topics related to LLM training, including how well can scaling laws be relied upon when fixing all other parameters aside from P and N, whether scaling laws can transfer between different architectures, how many models should one employ to obtain a reliable scaling law, how many training checkpoints should be used and more.

### Strengths
I believe the paper has several clear strengths:

1) The topic is very timely and relevant, there is indeed a large body of work dedicated to both empirical and theoretical studies of NSL, and often times reproducing results in this field is very difficult, therefore a contribution which also includes a large dataset is appreciated.
2) The paper is clear and well written, with minor phrasing mistakes.
3) This work collects and releases a very useful public dataset which allows one to analyze scaling laws from 485 pretrained models, and estimate more than 1000 scaling laws. This is a major community contribution which should not be overlooked and encouraged.
4) The authors provide useful best practices for estimating scaling laws in new model families, including some insights which may not be trivial, such as adding checkpoints in the middle of training can lead to a much better estimate of the final test loss scaling.

### Weaknesses
In spite of the strengths, the paper has several drawbacks:

**Main weakness:**

The main weakness of this paper, in my opinion, is in its lack of novelty. The main contribution of the paper in my eyes is the curation and publication of data, which is very useful indeed, but I cannot say that the insights gained by this paper are revolutionary or incredibly deep. 

**Minor weaknesses:**
1) The paper is entirely empirical, with no real attempt to understand why the rules of thumb given in the paper seem to be correct. This is understandable but unfortunate. 
2) The paper focuses only on language models, but scaling laws apply to other modalities and other model parameters. For instance scaling with compute-optimal scaling was not discussed aside from L514-L518.

### Questions
My comments/questions are:

1) L25: 'differ scaling behavior' - missing word
2) Figure 2 appears before Figure 1
3) L87-88: "A scaling law estimates the loss of a costly model by training cheaper ones (see Fig. 2) which share a pretraining procedure and differ by some hyperparameters" I'm not 
sure I agree with this definition, it might be the correct "empirical scaling law" definition but there are cases where the theory can be derived and there is no concept of really training smaller models, it's more along the lines of studying the behavior of the optimal solution for a model family under a change of dataset size, number of parameters, and compute.
4) L420 - "on all F provides on of the lowest ARE"
5) L526 - "checkpoitns"

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides a collections of training curves that can be used to investigate different scaling laws formulations. Specifically, the authors collected a large-scale dataset with information on losses and evaluations from 485 models to estimate over 1,000 scaling laws, exploring factors affecting accuracy in scaling law predictions, such as model size, training checkpoints, and family-specific characteristics.

The authors provide a metric named absolute relative error (ARE) to estimate the accuracy of the scaling law fitting, and based on this metric, the authors investigated various factors that may affect the accuracy of scaling law prediction. They have also provided analysis on some important research questions about scaling law.

### Strengths
1. A large collection of training curves have been collected. This dataset can be used in further studies of scaling law and also facilitate the study of LLM training dynamics.

2. Some important research questions about fitting scaling laws equations are proposed. Some of these questions are worth further investigating. Such as "if we can do 'transfer learning' with fitting scaling law equations for different experiment settings". Although I think there is some problems of their analysis process.

### Weaknesses
1. **The authors ignored an important factor for LLM training: learning rate schedule.**

In fact, the authors have pointed out that previous studies "is based on the assumption that changes in the learning rate schedule" "render losses from intermediate checkpoints uninformative". This rule is regarded to be true in almost all previous studies on scaling laws, including Kaplan et al., Hoffmann et al., and (Porian et al., 2024).

The authors cited two previous studies in line 392-395 to motivate their claim that intermediate checkpoints can be used in fitting scaling law equations. But I have to point out that these two previous studies they have cited do not provide any solid supports about using intermediate checkpoints in scaling law equation fitting. Specifically:

- (Hu et al., 2024) proposed the WSD learning rate scheduler, in which the validation loss decrease gently when the LR is constant and the validation loss decrease sharply as the LR anneals. The validation loss yield by the intermediate checkpoints in this learning rate scheduler do not fit the shape of the scaling law equation in eq.1 at all. In particular, eq.1 can not model the sharp drop of validation loss in the anneal stage. The validation losses obtained from these intermediate checkpoints **can not** be used to fit equations in forms of eq.1.

- (Porian et al., 2024)  found that careful learning rate decay is not essential for the validity of the scaling law. In their studies, they used the **final loss values** yield by the constant LR and cosine LR decay to fit the same form of scaling law equation and found little difference. They did not discussed to use the intermediate checkpoints to fit the scaling law equation.

2. **The definition of ARE is ill formed.**

The author define ARE as the mean prediction error on `max_{#toks}(F_{max}, 0.3)`. This definition implies that we can use eq.1 to predict losses of intermediate checkpoints, in particular the loss values of the last 30% of one intact training process, since the definition of `max_{#toks}(F,q)` "does not distinguish between partially trained models on one hand, and models trained to convergence on a subset of the largest training set used in a family on the other.".

This is simply *wrong*. For example, let's consider a WSD scheduler where the LR remains constant in the first 70% of training and starts to decay in the last 30% of training. The equation fitted using the loss values obtained from the first 70% of steps is not aware of how the LR is going to decay in the last 30% of training. Therefore, the prediction becomes a curve fitting game and provides absolutely no meaningful information.

All the following discussion and analysis of this paper is build upon the calculation of ARE. So if ARE is ill formed. I think we need to question the analysis results obtained based on ARE. It would be better to re-evaluate your key findings using alternative metrics.

### Questions
Does the collected dataset contain loss curves obtained from the WSD scheduler? or other learning scheduler?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper conducts extensive experiments to investigate scaling laws in large language models (LLMs). The topic is both relevant and insightful, providing valuable guidance for future experimental design in this area.

### Strengths
- The exploration of scaling laws is compelling and relevant, offering insights that can guide experimental decisions in LLM research.
- The paper clearly presents relationships between parameters across various scaling laws (e.g., as illustrated in Figure 3).
- It offers useful findings, such as the preference for extrapolation from a larger number of small, partially trained models rather than a smaller number of large models (as shown in Figure 1).
- Each section concludes with clear takeaways, helping readers understand the implications of each experimental finding.

### Weaknesses
 - W1: Figures, especially in the appendix (such as Figures 6 and 7), need improvement as some numbers overflow the plot areas.
- W2: Experiments on larger and more recent models, such as LLaMA 3 (70B or above), would strengthen the relevance and impact of the findings.

### Questions
- Q1: Could you specify the data collection process in more detail, such as the types of public datasets used and the methods for aggregating them as described in Section 3?
- Q2: Could you add a summarization table to capture the implications of the experiments, making it clearer how readers can apply the findings?

### Soundness
3

### Presentation
3

### Contribution
3
