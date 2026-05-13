# Beyond the training set: an intuitive method for detecting distribution shift in model-based optimization

- Decision: Reject
- Scores: 6, 5, 6, 3, 6

## Abstract
Model-based optimization (MBO) is increasingly applied to design problems in science and engineering. A common scenario involves using a fixed training set to train models, with the goal of designing new samples that outperform those present in the training data. A major challenge in this setting is distribution shift, where the distributions of training and designed samples are different. While some shift is expected, as the goal is to create better designs, this change can negatively affect model accuracy and subsequently, design quality. Despite the widespread nature of this problem, addressing it demands deep domain knowledge and artful application. To tackle this issue, we propose a straightforward method for design practitioners that detects distribution shifts. This method trains a binary classifier using knowledge of the unlabeled design distribution to separate the training data from the design data. The classifier’s logit scores are then used as a proxy measure of distribution shift. We validate our method in a real-world application by running offline MBO and evaluate the effect of distribution shift on design quality. We find that the intensity of the shift in the design distribution varies based on the number of steps taken by the optimization algorithm, and our simple approach can identify these shifts. This enables users to constrain their search to regions where the model's predictions are reliable, thereby increasing the quality of designs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a method for detecting out-of-distribution samples drawn in model-based optimization ML-guided design. The main idea is that black-box MBO may when optimizing some target function result in designing (drawing from the input space) a sample that is OOD w.r.t the available training data. At the same time, these OOD samples are those for which the performance of the target function predictor is less reliable and therefore undesirable as design choices. Shift between training and design distributions are measured via a shift detection model that classifies samples coming from each distribution. The OOD detection is then used to limit the search space in the design process to those with low “OOD scores,” i.e. close to the distribution of the desired data.

### Strengths
Addresses an important problem in ML-guided design where under-represented regions of the input space are exploited by the surrogate prediction model.  

By using a distribution classifier, avoids estimating the distribution of the respective data sub-spaces directly. This is especially important to allow for high-dimensional data and avoids setting limiting assumptions on their distribution.   

Synthetic and real experiments show the design shift problem and well motivate the use of OOD detection in MBO design pipelines

### Weaknesses
This approach overly constricts the search space of allowable design samples. The OOD scores rely on a classifier that considers only the data, and therefore is only effective to combat covariate shift. This means that design samples will be forced to be similar to training samples, even if distant samples in the input space could still have correct surrogate model predictions. The method's reliance on a binary classifier to distinguish between training and design distributions, while computationally efficient, may oversimplify the nuances of complex, high-dimensional data spaces. By collapsing the distribution shift into a single scalar score, the approach may discard valuable information about the specific nature of the shift, potentially leading to suboptimal design choices. Furthermore, the method does not explicitly account for the uncertainty in the OOD score itself, which could be significant, especially when the classifier is trained on limited data or when the shift is subtle. This lack of uncertainty quantification could lead to overconfident filtering of potentially useful design samples.

### Questions
Q1] The statement that distribution shifts in supervised regression “typically takes the form of covariate shift” is not well supported. Assuming covariate shifts is ones of the most restrictive assumptions on shift since the model predictions p(y|x) is unchanged between training and test/design distribution. Can you expand on this argument for focusing on this type of error?

Q2] Several approaches to refining the search space in ML-guided design are discussed in Section 3 (first paragraph). Why were these not used as baseline comparisons in the experiments?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an innovative solution to tackle the prevalent issue of distribution shift in model-based optimization (MBO) during design problems. Through the training of a binary classifier, the proposed method aims to differentiate between training and design data distributions, using classifier's logit scores as a distribution shift metric. The authors have also showcased the efficacy of their method in real-world scenarios.

### Strengths
The topic is extremely relevant in today's design scenarios where ML is frequently employed. Addressing the distribution shift problem is vital for the efficacy and reliability of models.

The paper's strength lies in its rigorous testing and validation. The authors did not stop at theoretical validation but extended their methodology to real-world applications, especially the experiment involving Adeno-Associated Virus (AAV) capsid sequences.

The straightforward nature of the proposed solution, its ability to be integrated with existing design methods, and its applicability across different black-box models make it versatile and broadly applicable.

The authors provided a clear understanding of the challenges tied to distribution shifts, especially feedback covariate shift, and visualized the problem effectively with Figure 1.

### Weaknesses
While the simplicity of the method is a strength, there are concerns about its robustness when exposed to diverse and complex real-world scenarios. The ability to detect distribution shifts in more intricate and nuanced cases would be important. Specifically, it's unclear how the binary classifier would perform with highly multimodal distributions or when the shift is not a simple, monotonic change. The paper would have benefitted from a clearer comparative analysis of the proposed method against the existing methods to handle distribution shift. Such a comparison can elucidate the advantages of their approach over others. It is not sufficient to simply state that the method is broadly applicable; concrete comparisons are needed to show its superiority or equivalence to existing methods. 

While the paper provides qualitative insights and findings from experiments, more quantitative metrics that measure the efficacy, false positives, and false negatives of the method would give a clearer picture. The current evaluation relies heavily on a regret metric, which is not a standard way to evaluate distribution shift detection. It's not clear if the approach would be as effective across diverse domains outside of the ones presented in the paper. The experiments are limited to protein sequence design and structure prediction, and it is not clear how well the method would generalize to other areas where the nature of the data and the shift might be very different.

### Questions
Include a detailed comparison section with existing methods to highlight the novelty and advantages of the proposed technique.
Offer more depth on the architecture and functioning of the binary classifier.
Provide additional quantitative metrics for method evaluation.
Explore the methodology's application in a wider array of domains and provide insights or findings from such applications.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this study a new technique is proposed to filter out designed samples by offline MBO for which the surrogate model does not provide reliable predictions. In practical settings, this allows for prioritizing improved samples that have reliable predictions by the surrogate model and stay close to the initial set used for training. This is done by training a classifier to distinguish between the training and the designed samples. For each design sample, the logit score of the classifier determines its extent of deviation from the training distribution.

### Strengths
Generation of experimental data for the problem of AAV design to evaluate the performance of their technique

### Weaknesses
See Questions

1) It is not clear how the threshold on the OOD scores should be determined? Is there a systematic way to do this?
2) The binary classifier is trained to assign designed samples a different label from the training samples even if the designed samples are similar to the training samples. What are the downsides of this?
3) It is not discussed when the proposed technique could fail.
4) Minor: Change Figure 4 to Figure 3 in the text

### Questions
1)	It is not clear how the threshold on the OOD scores should be determined? Is there a systematic way to do this?
2)	The binary classifier is trained to assign designed samples a different label from the training samples even if the designed samples are similar to the training samples. What are the downsides of this?
3)	It is not discussed when the proposed technique could fail.
4)	Minor: Change Figure 4 to Figure 3 in the text

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Model-based optimization can be tricky in practice because, by definition, the goal is to move away from the training data to not parts of the search space. This means that models may extrapolate unpredictably. There are a variety of methods for reasoning about models' reliability in certain regions. The authors propose a simple approach: train a model that detects whether a point in the search space is similar to the training data. This can be done using a binary classifier. The outputs of this classifier can be combined with the output of the predictive model to form an acquisition function that penalizes reckless exploration.

### Strengths
The paper addresses a key challenge in model-based optimization: knowing when to trust the model's enthusiasm for certain new designs vs. where in the search space to not trust the model.

The paper presents a section of experiments based on real-world wet-lab experiments.

### Weaknesses
The paper proposes a method (sec 2.4) for improving MBO using a surrogate OOD classifier model to penalize exploring regions of the search space where the model is likely to extrapolate poorly, since the regions are out of the distribution that the model was trained on. However, there are *no* experiments that directly test the impact of this approach. The fidelity between OOD metrics and model errors are presented, but no results demonstrate that incorporating the OOD classifier in the MBO search procedure improves the quality of proposed designs. As far as I understand, the analysis on the AAV data in section 4.3 does not actually incorporate the OOD classifier to change the library of selected AAV sequences. Instead, a library was generated without the paper's proposed MBO approach, and then some analysis was done retrospectively to argue that perhaps using the OOD classifier would have been helpful. Given that the paper provides a concrete proposal for an MBO algorithm, there needs to be a head-to-head comparison between this approach and a baseline approach. This could be done easily, for example, on the synthetic 2D data of Sec 4.1.

OOD detection seems like an unreliable way to reason about where the model will reliably be able to extrapolate, since it only looks at the P(x) distribution of training data, not the distribution P(y|x) or labels or anything about the particular inductive biases and invariances of the model being used to make predictions. In particular, many modern predictive models use some sort of pretraining on natural protein sequences. How does this impact your assumptions?

### Questions
I find the overall flow of the proposed algorithm a bit confusing. If I understand correctly, the approach is this: fit a predictive model, run some sort of search algorithm to find points with high predictive model score, train an OOD classifier where the positive examples are the points from the previous step and the negative examples are the training data used to train the predictive model, re-run the search algorithm using a modified objective that combines the scores of the OOD model with the original model. Is this correct?

As far as I can tell, the data used for fig 3 came from a single round of MBO; only one additional wet-lab experiment was run, and it was run on sequences from the entire trajectory of the Adalead optimizer used for finding sequences with high model score. I understand that wet-lab experiments are expensive, and that multiple rounds of experiments would be infeasible. However, I don't understand the point of focusing on the 15 steps of the Adalead algorithm. This method should be treated as a black-box search algorithm used for finding high-scoring sequences. Why was experimental capacity spent on sequences from the early iterations of Adalead?

I don't understand this:
'' In contrast, the Deep Ensemble scores cannot effectively serve as a quantitative predictor of shift intensity.' Why not?

Section 4.2 is extremely terse. What is the key take-away point from it that suggests it should appear in the paper?

There need to be far more details about the AAV setup. Is the data public? Will it be released with the paper? How big is it? How long is the sub-sequence of the protein that was mutated? 

Perhaps I'm misunderstanding things. Can you please address the 'weaknesses' above?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses a common issue in design problems. Given a expensive-to-evaluate function $f(x)$ and an initial set of training points, the goal is to find points $x$ where $f(x)$ is maximised. In model-based optimization (MBO) approaches, the idea is to iteratively train a surrogate model to approximate $f(x)$ using the existing data and use it to generate new data. However, the common issue here is that the initial points may not be sampled i.i.d. from the input space, leading to a distribution shift problem.

The paper addresses the issue by training a binary classifier, which they call it Out-Of-Distribution (OOD) classifier, to predict whether the input comes from the training data or from the design data, and uses the classifier's logit to derive a notion called OOD score that can be used to weight the input towards the distribution of the design data. Using the OOD scores, they show how the distribution shift problem can be largely mitigated.

Experiments were conducted in a 2D toy model, a simulated protein structure design, and the design of AAV capsid protein.

### Strengths
The paper is well-written. It's idea is clear and easy to understand. Experiments are reasonable and convincing for the design problems addressed in the paper.

### Weaknesses
Forgive me for being straight to the point but I think the main contribution of the paper, the OOD classifier and its OOD score, is very well-known in the ML literature, under the name of propensity score (e.g. [1], [2]):

[1] Agarwal et al. Linear-Time Estimators for Propensity Scores. In AISTATS, 2011.
[2] P. Rosenbaum and D. Rubin. The central role of propensity score in observational studies for causal effects. Biometrica, 70:41–55, 1983.

It is the same idea: train a binary classifier using sampled points from two separate distributions $p$ and $q$ as negative and positive examples, then to make any point $x$ coming from distribution $p$ look like it comes from $q$, we assign a weight equal to the Radon-Nikodym derivative (RND) $\frac{dq}{dp}(x)$ (see section 3 of [1]) to $x$. The RND is estimated by a function of the prediction scores of the classifier, named as the propensity score, which matches with the OOD score of the paper.

If we take OOD classifier/score out of consideration then unfortunately the remaining contributions are not sufficient for me to recommend acceptance.

### Questions
I do not have any specific question. The paper should have been otherwise a good paper had the propensity score not been invented before.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
