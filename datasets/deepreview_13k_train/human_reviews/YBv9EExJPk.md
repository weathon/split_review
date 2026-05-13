# Multiple Descents in Unsupervised Auto-Encoders: The Role of Noise, Domain Shift and Anomalies

- Decision: Reject
- Scores: 5, 5, 5, 3, 3

## Abstract
The phenomenon of \textit{double descent} has recently gained attention in supervised learning. It challenges the conventional wisdom of the bias-variance trade-off by showcasing a surprising behavior. As the complexity of the model increases, the test error initially decreases until reaching a certain point where the model starts to overfit the train set, causing the test error to rise. However, deviating from classical theory, the error exhibits another decline when exceeding a certain degree of over-parameterization. We study the presence of double descent in unsupervised learning, an area that has received little attention and is not yet fully understood. We conduct extensive experiments using under-complete auto-encoders (AEs) for various applications, such as dealing with noisy data, domain shifts, and anomalies. We use synthetic and real data and identify model-wise, epoch-wise, and sample-wise double descent for all the aforementioned applications. Finally, we assessed the usability of the AEs for detecting anomalies and mitigating the domain shift between datasets. Our findings indicate that over-parameterized models can improve performance not only in terms of reconstruction, but also in enhancing capabilities for the downstream task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates the double descent phenomenon in the unsupervised setting. The experiments on synthetic datasets explore the relation between double descent and four variables: sample noise, feature noise, domain shift, and anomalies. Moreover, some observations remain for real-world datasets.

### Strengths
The paper investigates double descent in the unsupervised setting, which did not receive attention as much as supervised learning or self-supervised learning.

The paper has the following contributions:
1. The paper shows how the four different variables (sample noise, feature noise, domain shift, and anomalies) affect the double descent.
2. The paper connects observations of the synthetic and real-world datasets.
3. It is interesting to see that although there are four different variables, many of them share the same intuition (the magnitude or portion of the noise controls the vertical height and the horizontal position).

### Weaknesses
The paper is not smooth to read. Some details are not mentioned or explained. For example, providing some details regarding the under-complete AEs could help the readers understand why the experiments should be based on under-complete AEs. Besides, the experiment sections contain many figures and they could be rearranged for a smoother reading experience.

As for the experiment section specifically:
1. How is Fig.2 different from the traditional figure of test loss against the number of parameters? They seem to convey the same information. Does it mean the relation between the two in unsupervised learning is the same as supervised learning?
2. Some curves are missing. For example, in Fig.3a various levels of sample noises are shown, but many of them are missing in Fig.3b. Could you provide all the curves?
3. I recommend the authors put a paragraph or a table to summarize the relation between the double descent and the four variables as they share very similar behavior and intuition. It will be easier for the reader to access the experiment outcome.
4. For the paper to be more informative, the author could compare the double descent behaviors in unsupervised learning against the supervised learning regime. Could you conclude if there is any different behavior in the unsupervised setting than the ones observed in the other settings?

### Questions
Please refer to the weakness section for the questions.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the double descent phenomenon in relation to three key training parameters, training epochs, model size, and data sample size, within an unsupervised learning framework. To illustrate the phenomenon, consider training epochs: initially, test error decreases as the number of training epochs increases. However, after reaching a certain threshold, test error begins to increase. After a period of error rising, the test error decreases again, known as, double descent. Additionally, the authors conduct experiments using synthetic data and small-scope models to empirically examine the impact of customized noise, domain shifts, and anomalies on double descent behavior. Finally, the study assesses how model size influences domain adaptation and anomaly detection performance.

### Strengths
1. This work provides empirical evidence that the double descent phenomenon exists in various training parameters under unsupervised learning settings, and the non-linear relationship observed between test error and training parameters may be of interest.
2. Unlike previous studies, to verify the influential factor model size, this work proposes utilizing specific layers in different dimensions to simulate the changing of model size. This modification is well-suited for experiments with small-scope neural networks by avoiding introducing extra variables.

### Weaknesses
$	extbf{Weakness in method motivation and novelty}$

1. This work needs more motivation to study the phenomenon of double descent. Particularly, this work does not provide possible theoretical improvement or help better understand the unsupervised learning problems. Additionally, the patterns identified lack a compelling connection to practical real-world (deep) model training. To summarize, this paper does not show enough evidence that the revealed pattern can improve existing optimization problems theoretically or practically.


2. While the study emphasizes that its unsupervised learning focus is distinct from prior work, the observed double descent patterns align with those documented in supervised learning. This difference in setup, while noted, does not seem to substantively alter the properties of the optimization process.

3. The empirical verification of double descent with respect to model size (via specific layer dimensions), sample size, and training epochs lacks novelty.


$	extbf{Weakness in evaluation}$

A substantial portion of the paper, particularly Section 4, examines double descent behavior under conditions of customized noise, domain shift, and anomalies in the training data. However, these customized conditions appear to have been selected without a clear rationale, and the resulting findings are unsurprising.

### Questions
1. Could you elaborate on the fundamental differences between supervised and unsupervised learning that warrant separate investigations into the double descent phenomenon in each scenario?

2. What insights or practical applications do you anticipate arising from studying double descent under different data conditions, such as Gaussian noise and domain shift?

3. Section 5 is somewhat unclear. The conclusion drawn here—that over-parameterized models improve training performance under varying conditions—seems straightforward. Additionally, how does this finding relate to the double descent phenomenon?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the phenomenon of multiple descent in unsupervised learning paradigms, specifically using under-complete auto-encoders (AEs). Contrary to prior studies that suggest double descent does not occur in unsupervised learning, this work empirically demonstrates the presence of multiple descent under conditions of low SNR, significant anomalies, and domain shifts. Additionally, it identifies scenarios where multiple descent affect test loss, providing new insights to model selection and training with over-parameterized networks.

### Strengths
* This paper addresses an important and timely topic in understanding the generalization behavior of over-parameterized models.
The paper is well-written and easy to follow. It is interesting to see that under low SNR, over-parameterized models’ ability to fit (or memorize) noise can actually improve generalization when encountering domain shifts.
* The experiments are thorough, and the analysis of results provides insightful observations.

### Weaknesses
-  While the paper highlights the roles of noise, domain shift, and anomalies in multiple descent, providing further theoretical insights into the underlying mechanisms could enrich the understanding of why this phenomenon occurs.
- Defining critical regions for multiple descent more explicitly, possibly through some kind of scaling law like function characterizations, could make the findings more actionable and help readers choose appropriate model complexity and stopping condition in practical settings.

### Questions
- In practice, noise is not always Gaussian. How would different noise distributions impact the behavior of multiple descent?
- Could the paper provide theoretical insights or hypotheses on why multiple descent occurs under conditions of low SNR, domain shift, and anomalies, and how critical regions might be characterized more systematically?
- Are there practical ways to predict the occurrence of multiple descent based on data characteristics or noise conditions, making it more applicable for real-world scenarios? 
- Given that SNR is challenging to compute from data without specific model assumptions about signal and noise, what are some methods or approximations to determine SNR in real-world data?
- For the KNN-DAT experiment (Fig 12), what would be the relationship of test loss curve with different levels of source-target distribution shift? (e.g. measured by distribution distance such as KL divergence or Wasserstein distance) Does the relationship confirm with the simulated experiment?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper experimentally discovers the double descents (multiple descents) phenomenon in autoencoder models and explains this phenomenon to sample noise, feature noise, domain shift, and outliers. The double descent phenomenon represents a specific pattern in the generalization performance of a model based on its size. Notably, this phenomenon has provided significant motivation for studying the generalization performance of overparameterized models.

### Strengths
This study also provides empirical examples related to the generalization performance of overparameterized models in unsupervised learning. These findings will encourage further research on model complexity in unsupervised learning.

### Weaknesses
Although the paper claims to present extensive simulation results demonstrating the double descent phenomenon in unsupervised learning, the experiments primarily seem to involve regression tasks. This interpretation arises because the study examines the performance changes in autoencoders by adding noise to data or features, which can essentially be understood as fitting an arbitrary target variable, similar to a regression model. In this sense, the results could be viewed within the same context as previous findings observed in supervised learning.

Moreover, discovering multiple descent patterns may not offer a new perspective based solely on the current simulation results. Additional discussion and analysis would likely be necessary to substantiate this claim.

Before discussing the double descent phenomenon in unsupervised learning, it is essential first to define the performance metric in the context of unsupervised learning. If unsupervised learning is limited to distribution learning, I suggest defining the performance metric based on the distance to the target distribution and examining how performance varies with model size. Suitable models for unsupervised learning would include those capable of distribution learning, such as VAE, GAN, or diffusion models. Alternatively, a simpler experimental approach could involve using a clustering task.

### Questions
Is it possible to define the double descent phenomenon for unsupervised learning models other than autoencoders?

How can the use of test loss to define predictive performance in unsupervised learning be justified? From the perspective of distribution learning, shouldn't distributional similarity serve as the performance metric?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors study the phenomenon of double descent appearing in over-parametrized machine learning models. Where recent findings focused on supervised learning problems, here the authors focus on unsupervised learning specifically studying autoencoders. Considering the evolution of training loss with respect to different data modifications (sample noise, feature noise, domain shift, and anomalies), they find multiple descent phenomena appearing under different settings, yielding insights into the behaviour of learning of autoencoders studying both synthetic and real data.

### Strengths
- The presented paper shows some rigorous analysis of the double descent phenomenon under different settings
- The paper is well written and easy to follow.

### Weaknesses
 - The takeaway of this paper is not exactly clear. What can we do with these insights on Autoencoders, also given that the CNN AE -- probably the more relevant model in nowadays application -- presented in the appendix does not show the typical double descent with progressing training? The discovered connection between model size and performance does not seem so surprising to me. An extensive discussion and recent application of AE s would strongly benefit the paper. As a constructive suggestion, the authors could look into Sparse Autoencoders, which recently are in heavy use in XAI [1] and even have been adapted by Google in their Gemini project [2], and insights into their training dynamics would be of great use. Note that a smaller scale example on a standard vision benchmark could suffice here.
- The paper lacks a more theoretical discussion of *why* what we see is happening. The recent works shedding light onto this and showing that double descent is not in conflict with classical statistical learning theory could serve as a starting point [3,4] and should also be appropriately addressed in intro and related work.

### Questions
see weaknesses

### Soundness
4

### Presentation
3

### Contribution
3
