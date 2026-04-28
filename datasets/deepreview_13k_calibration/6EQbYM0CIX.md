# Conditional Generative Modeling for High-dimensional Marked Temporal Point Processes

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Point processes offer a versatile framework for sequential event modeling. 
However, the computational challenges and constrained representational power of the existing point process models have impeded their potential for wider applications.
This limitation becomes especially pronounced when dealing with event data that is associated with multi-dimensional or high-dimensional marks such as texts or images.
To address this challenge, this study proposes a novel event-generation framework for modeling point processes with high-dimensional marks. 
We aim to capture the distribution of events without explicitly specifying the conditional intensity or probability density function. Instead, we use a conditional generator that takes the history of events as input and generates the high-quality subsequent event that is likely to occur given the prior observations.
The proposed framework offers a host of benefits, including considerable representational power to capture intricate dynamics in multi- or even high-dimensional event space, as well as exceptional efficiency in learning the model and generating samples. 
Our numerical results demonstrate superior performance compared to other state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The proposed method is a generative model that outputs the time and the mark of the point process with a generator network, that is, maps noise to data. The learning is then performed using kernel density estimation or variation approximation. The method shows promising results on synthetic and real-world data.

### Strengths
The paper proposes a new conditional network to generate samples of a marked TPP directly. This is a nice alternative to the usual approaches of generating either time or mark first and conditioning the generation of the other. The generation is performed through a network that takes in the history embedding and a random noise vector that acts a source of noise similar to a generator in GANs. The training is not done in an adversarial way but rather using either kernel density estimation or variational inference. According to the empirical results this works surprisingly well on some synthetic data and a real-world scenario of earthquake prediction.

### Weaknesses
The model estimation seems like the most important contribution of the paper, although both rely on already known techniques. Equation 6 seems to include samples, something that is stated as a drawback for some of the competing methods. What is the computation cost of Algorithm 2, and compared to other methods?

In Appendix C it is stated that the second term of the ELBO is minimizing the NLL $p(x | z, h)$ which is the cross entropy between the observed and reconstructed event. But in this case, $x$ is both the mark and the time so I am not sure how this works out. The specific losses and their weights are not clearly defined, making it difficult to understand how the joint density is evaluated. It's unclear how the reconstruction loss is calculated when $x$ includes both time and mark, and how the different components are weighted.

In 3.1 it says that only the conditional intensity can be computed in the baselines and the density has to be computed with numerical approximation. 1) How can your method compute the density in closed-form? 2) At least for fully NN model it is possible to compute the intensity and cumulative intensity in closed-form which will give you density. The claim that only the conditional intensity can be computed for baselines is not accurate, as fully neural network models can provide closed-form intensity and cumulative intensity, allowing for density calculation.

As there is so much focus on thinning there seems to be a lack of baselines that do not require it, for example, having parametric density functions or (continuous) normalizing flows would allow immediate sampling. Using inverse CDF parameterization as well as diffusion models also allow direct sampling. The expressiveness of these models is still probably good enough for the tasks considered in the paper. The lack of comparison to methods that allow for direct sampling, such as normalizing flows or diffusion models, is a significant oversight. These methods offer direct sampling capabilities and should be considered as baselines.

I am surprised with the results on synthetic data since at least fully NN model should be able to capture such simple intensity. Perhaps the model was not tuned correctly.

Section 3.2 setup is not really realistic. This is not a TPP problem but rather an image generation problem. Just because some methods cannot capture the complicated distribution *within* each mark does not mean that they cannot capture relations *between* marks -- what should have been tested. That is, the *temporal* point process here is easy and the conditional generation of marks is hard. I don't see why RMTPP augmented with a strong image generator could not beat proposed method. A more meaningful comparison would be some kind of dataset where each pixel in an image arrives at some time and they have some sort of interaction between each other, which is non-trivial. The high-dimensional mark experiments are essentially image generation tasks, not true temporal point process problems. The interactions between marks are simplistic, and the challenge lies primarily in generating high-fidelity images, not in modeling complex temporal dependencies between different types of marks. A more realistic setup would involve complex interactions between different types of marks, rather than just generating images conditionally.

The drawback of 3.2 is shown on in 3.3 since we have much simpler and lower dimensional real-world data.

The main issues are 1) the question of which part of the paper helps in getting the good results the most, is it avoiding learning using likelihood or the architecture? 2) Why some baselines are not performing so well on synthetic data and why stronger baselines are not used in 3.2? 3) Missing demonstration of generating proper high-dimensional marked point processes.

Minor:

- (Graves & Graves, 2012) citation is wrong, both the reference and the formatting of the reference "we opt for long short-term memory (LSTM) (Graves & Graves, 2012)".

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a model-agnostic generative framework to model event sequences with high-dimensional marks, a setting generally overlooked by prior works. Instead of directly defining a parametric form of the conditional intensity function (or conditional density function), they propose to estimate the distribution of events using samples generated from a conditional generator. The framework being introduced can be trained through different learning algorithms, and enjoys better computational efficiency compared to approaches relying on the thinning algorithm to simulate new events.

### Strengths
1) The proposed framework scales well to a setting with high-dimensional marks, an interesting research direction that has currently received little attention from the neural TPP community. 
2) The framework being model-agnostic, it could be easily extended to other classes of models and learning algorithms than the ones presented in the paper. 
3) The methodology proposed by the authors is presented clearly, which makes the paper intelligible and easy to follow.

### Weaknesses
1) In Section 2.2, you state "the proposed model enjoys considerable representational power, as it does not impose any restrictions on the parametric form of the conditional intensity $\lambda$ or PDF $f$.". Several neural TPP models, such as FullyNN [], also do not impose any restrictions on the parametric form of the conditional intensity function. In what sense does your approach enjoy additional expressiveness compared to these models? Specifically, while the claim of not imposing restrictions is true, many neural network models achieve this by using flexible function approximators. The paper needs to clarify what specific aspect of their approach provides additional expressiveness beyond the flexibility offered by neural networks in general. For example, does the model architecture or training procedure enable it to capture more complex dependencies or distributions compared to existing neural TPP models?

2) In section 2.3 regarding equation (5), you say "It is worth noting that this learning objective circumvents the need to compute the integral in the second term of (3)...". However, the negative log-likelihood expressed in terms of the events PDF still involves the conditional CDF evaluated at the observation window, which appears to have been omitted in this case. The paper needs to explicitly address how the conditional CDF is handled or approximated, as it is a crucial component of the likelihood function. The current explanation is insufficient and raises concerns about the correctness of the derived learning objective.

3) For semi-synthetic and real world data, why don't you provide evaluation metrics to assess the performance of the different baselines as you did with the simulated datasets? Visualizations on hand-picked sequences are not enough to get a clear overview of the baselines performance. The lack of quantitative evaluation makes it difficult to objectively compare the proposed method with the baselines. The paper should include metrics relevant to the specific data types used (e.g., image similarity metrics for image data, text similarity metrics for text data) to provide a more rigorous comparison.

4) From the training details provided in the Appendix, I understand that you fixed the hyper-parameters of the different models. Did you experiment with other hyper-parameters configurations as well? The paper should clarify whether a hyperparameter search was performed for the baselines and the proposed method. If not, the results might be biased due to suboptimal hyperparameter settings. It is important to ensure a fair comparison by optimizing hyperparameters for all models.

5) On Figure 6, you only show the results for the proposed CEG method, what about the other baselines (e.g. DNSK)? The paper should include results for the baseline methods in Figure 6 to allow for a direct visual comparison. Without this, it is impossible to assess the relative performance of the proposed method.

### Questions
See the 'Weaknesses' section.

### Soundness
2 fair

### Presentation
3 good

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
The paper proposes a new method to generate event sequences with high dimensional marks such as text and images. The method combines MTPP models with conditional density generator which directly models the generator function condition on history and a random vector from Normal distribution. This makes the approach more efficient (in terms of sample generation and prediction), and more expressive (by avoiding explicitly confining the conditional intensity function to a specific form).

### Strengths
Originality: The idea of making the mark to not restricted to discrete or continuous is somewhat novel. Some works have been done in spatio-temporal point process (i.e. Chan et al. NEURAL SPATIO-TEMPORAL POINT PROCESSES). It is interesting to see in high dimensional mark as text and image which are modern applications(i.e. Vision and NLP).  One paper in the domain is (Mehrasa A Variational Auto-Encoder Model for Stochastic Point Processes).  As far as I know,  this is the first work to do it with “GAN-type” generative models. 

Quality: the overall okay. The authors attempt to include a comprehensive experiments from full synthetic, semi-synthetic and real applcaitions to support the main claim of the proposed model. 

Clarity: Overall the presentation is fine. I understand the flow of the paper fairly well, from motivation, proposal of model, model itself, and experiments. I have questions about some details such as the comments from weakness. 

significance. This can be an interesting idea – combined TPP with generated models, and benefit the TPP community.

### Weaknesses
Quality:
Methodology: the paper proposes a conditional generator for tpp with high dimension marks. Combining 1dimensional timestamp and high dimensional marks and learn to estimate the density (whether implicitly or explicitly) seems to be a little problematic. Error in estimating of timestamp will likely to be engulfed by error in estimating high dimension marks. (a similar example in causal inference for estimating outcome given (potentitally) high dimension covariates X and 1 D binary treatment {0,1}, i,e, g(y;X,T). ) Specifically, the optimization process might prioritize minimizing the error in the high-dimensional mark space, potentially at the expense of accurate timestamp prediction. This imbalance could lead to a model that generates realistic marks but fails to capture the temporal dynamics of the event sequence accurately. A clear strategy or mechanism to balance these two aspects during training is not adequately presented in the current manuscript.

Data and Analysis & Experimental Design: the author(s) should focus on experiments on high dimensional marks. 
1.Experiments on synthetic data with 1D and 3D does not support the main claim. However it can be added to Appendix instead of main text. 1.Could the author generate tpp with high dimensional marks? (reasonably high like 50?) The current experiments with T-MNIST and T-CIFAR, while involving high-dimensional data, do not explicitly demonstrate the model's ability to handle marks of dimensionality in the range of 50-100. This range is crucial as it represents a middle ground between low-dimensional examples and extremely high-dimensional cases like images.

2. For semi synthetic data, maybe the author(s) should try to find some quantitative metrics. I can “see” the performance of CEG is good on T-MNIST but   I cannot evaluate how good the generated series on T-CIFAR, even though it is better than DNSK. The lack of quantitative metrics makes it difficult to objectively assess the performance on T-CIFAR. While visual inspection is helpful, it is subjective and does not provide a rigorous comparison.
3. Real data: a. Northern California earthquake catalog. It seems to it is spatiotemporal point process. Thus mark is 2-dimensional. B. Atlanta crime reports with textual description is an interesting application. Even so the mark is processed to be in 10 dimensional. These datasets do not fully validate the proposed method's effectiveness for high-dimensional marks. The earthquake data is essentially a spatio-temporal point process, and the crime reports, while interesting, use a reduced 10-dimensional representation of the text data.
4. There is no evaluation of time in the above experiments. The absence of any temporal evaluation metrics in the experiments is a significant omission. It is crucial to assess how well the model predicts the timing of events, not just the associated marks.

Clarity: The key of the proposed model is equation (5). However, to estimate the density conditional PDF in 5, it is unclear whether (6) or (7) are used in the experiment. Also in the experiment section only the density estimation of t without mark is shown. This is very limiting and does not support the proposed model. The lack of clarity regarding which equation is used in each experiment makes it difficult to replicate the results and understand the specific implementation details. Furthermore, demonstrating density estimation of only the timestamp without considering the mark does not provide sufficient evidence for the model's ability to handle high-dimensional marked temporal point processes.

### Questions
1.	See comments in Weakness.
2.	Datasets to validate. Could the authors find a dataset of sequences of video frames and perform experiments on such datasets so that the generated dynamics can be reflected? 
3.	Baselines and ablation. Has the authors done experiments on removing timestamps so that x is just the mark from f(x|Ht(x)) in equation 5?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
