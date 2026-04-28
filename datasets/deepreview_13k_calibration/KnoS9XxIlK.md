# A Multi-Power Law for Loss Curve Prediction Across Learning Rate Schedules

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 5, 8, 6

## Abstract
Training large models is both resource-intensive and time-consuming, making it crucial to understand the quantitative relationship between model performance and hyperparameters. In this paper, we derive an empirical law that predicts pretraining loss for large language models for every intermediate training step across various learning rate schedules, including constant, cosine, and step decay schedules. Our proposed law takes a multi-power form, combining a power law based on the sum of learning rates and additional power laws to account for a loss reduction effect as learning rate decays. We validate this law extensively on Llama-2 models of varying sizes and demonstrate that, after fitting on a few learning rate schedules, it accurately predicts the loss curves for unseen schedules of different shapes and horizons. Moreover, by minimizing the predicted final pretraining loss across learning rate schedules, we are able to find a schedule that outperforms the widely-used cosine learning rate schedule. Interestingly, this automatically discovered schedule bears some resemblance to the recently proposed Warmup-Stable-Decay (WSD) schedule (hu et al, 2024) but achieves a slightly lower final loss. We believe these results could offer valuable insights for understanding the dynamics of pretraining and for designing learning rate schedules to improve efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper authors introduce an empirical power law that predicts the pretrianing loss for LLMs as a given training step. Method is tested across the set of learning rate schedules: constant, cosine and step decay. Using the proposed power law authors were able to find the schedule that outperforms widely used cosine learning rate schedule.

### Strengths
Improving the predictability of LLMs at different scales has been a very important task for many years. This paper attempts to make the projections very granular, in particular, authors propose an empirically tuned power law that allows to predict the training loss for a given model at every individual step across the set of learning rates. Within the range of tested LR schedules, authors also demonstrated that their method improves training loss compared to the popular cosine learning rate schedule.

### Weaknesses
I think this work has a lot of potential, but it is important to conduct additional testing and analysis of the proposed method:

1. Given that the training loss demonstrates an improvement for the provided method, it is important to understand how the gain in training loss quality effects validation loss. In case the proposed method has a lower generalization capacity, it might not be beneficial to train with it even provided the improvement in the training loss. 
2. Several prior works tried to control training dynamics and make LLMs more predictable with various levels of granularity. For example, MuP paper: https://arxiv.org/abs/2203.03466 that proposes a list of adjustments in the architecture to improve predictability of the LLMs at scale. It would be very interesting to understand the benefits of the proposed method in the scenario when combined with techniques like MuP. 
3. During optimization of LLMs it is usually very important to look at the batch size together with learning rate. Here is the paper that proposes how the critical batch size should be estimate assuming the perfectly tuned learning rate: https://arxiv.org/abs/1812.06162. I think it is important to understand the temperature of the training in the proposed method and how the benefits would be affected once the batch size is tuned. 
4. One other thing that I struggled with was understanding what is the actionable outcome from this work. If the authors propose a new learning rate schedule derived from the power law equations, it should be rigorously tested across a set of downstream tasks, or at least authors should demonstrate improvements in terms of the validation loss and not just the training loss.  
5. Finally, I would recommend authors testing their methodology against the existing scaling laws that allow us to understand benefits of this method when scaling the pretraining FLOP budget.

### Questions
It would be good to see the quality change on the validation or test set in addition to the training set.
If you have quality on the downstream tasks, that would be very important to look at as well for the proposed method. 
From these, I would also want to see how marginal the improvements are by looking at the stddev values for the validation loss due to the randomness.

### Soundness
2

### Presentation
3

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
This paper introduces a multi-power law for predicting loss curves in LLMs. The law is empirically derived, with all experiments conducted using Llama-2 models of various sizes (25M, 100M, 400M). The proposed law predicts training loss curves under decaying learning rates across different iterations. Building on Chinchilla's scaling law, it incorporates additional terms to account for the impact of learning rate decay, which Chinchilla’s law does not explicitly address. The authors fit the multi-power law to three loss curves under distinct learning rate schedules, demonstrating that it can predict loss curves for unseen schedules, validated using WSD. Additionally, they applied the law to optimize learning rate schedules, identifying one that resembles WSD but achieves faster convergence.

### Strengths
1. The proposed multi-power law shows potential for predicting loss curves for unseen learning rate schedules, though it has not been sufficiently validated.

2. The proposed law could be leveraged to optimize learning rate schedules, potentially accelerating LLM training.

3. The paper provides valuable insights into pretraining dynamics, offering guidance for designing learning rate schedules that can simplify the complex task of learning rate tuning.

### Weaknesses
1. The theoretical justification for the proposed multi-power law is limited. The formulation of the law in Equation 2 lacks rigorous derivation or justification, raising doubts about its generalizability to unseen learning schedules. Specifically, the paper does not provide a mechanistic explanation for why the additional terms in the multi-power law should take the specific form they do, or why they should be additive. The lack of a theoretical basis makes it difficult to assess the conditions under which the law might break down.

2. The paper does not clearly state the fundamental assumptions underlying the proposed law. It is unclear whether the additional terms in Chinchilla's law (the second and third terms in Equation 2) should be model-independent, batch-size-independent, or optimizer-independent. The paper appears to assume that the impact of learning rate schedules remains independent of these factors, a point with which the reviewer may disagree. For instance, the effect of learning rate decay might interact with the batch size, where smaller batch sizes could be more sensitive to changes in learning rate. This interaction is not addressed, limiting the applicability of the proposed law.

3. The experimental section does not explore other types of learning rate schedules, such as cyclic or increasing schedules, leaving it unconvincing that the proposed law applies universally to various schedulers. The validation is primarily limited to cosine and constant learning rate schedules, which are both monotonically decreasing. The lack of experiments with non-monotonic schedules, such as cyclical learning rates or schedules with a warm-up phase followed by decay, raises questions about the law's robustness and general applicability.

4. It remains unclear if the learning rate scheduler derived from the proposed law consistently outperforms baseline schedulers. While the paper demonstrates reduced training loss at specific iterations with the proposed scheduler, it does not clarify if this advantage holds at convergence. The paper only shows that the optimized schedule achieves lower loss at certain points during training, but it is not clear if this translates to a lower final loss or faster convergence to the same final loss. The lack of a clear convergence analysis makes it difficult to assess the practical utility of the optimized schedule.

5. The scope of application for the proposed law appears restrictive. The parameters of the law need to be fitted under the same task, model, batch size, and optimizer before yielding an improved learning rate schedule. It seems that the model, batch size, and optimizer must remain unchanged to apply the law effectively. This limitation significantly reduces the practical applicability of the law, as it requires retraining with different configurations to obtain new parameters.

6. There is a typo on line 491, and Figure 8 lacks clarity. The curves for the baseline methods are difficult to distinguish due to missing labels.

### Questions
1. How does the proposed law generalize to other model types, such as high-parameter models like Llama-7B? Currently, it has only been tested on models with 25M, 100M, or 400M parameters.

2. The paper claims that the proposed approach is effective for long-horizon predictions, but the validation is limited to training curves with cosine and constant learning rate schedulers. Could you add plots supporting this claim for additional learning rate schedulers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a multi-power law for loss curve prediction of large language models. By using power law to fit loss curve of different learning rate in each step, it can accurately predict the loss curves for unseen schedules of different shapes and horizons in different sizes of Llama-2 models. Moreover, by minimizing the predicted final loss across learning rate schedules, it is able to find a schedule that outperforms the widely-used cosine learning rate schedule.

### Strengths
1.	It achieves good loss curve prediction performance for 25M, 100M and 400M Llama-2 models and unseen learning rate schedules. 
2.	It can also help to find a better learning rate schedule than cosine learning schedule.

### Weaknesses
1.	It is empirical law which is not well-proofed as well as fully verified. It would be better to include more kinds of LLMs and larger model sizes since it can benefit more for large model training and new model structure exploration.
2.	It only considers the relationship between learning rate and the loss curve. However, many other hyper-parameters will also affect the loss curve, such as model size, batch size, initialization seeds, etc. It would be better to take a comprehensive view so that the prediction could be more practical.
3.	It is interesting that the multi-power law can also be used to tune optimal learning rate schedule for each case. It would be better to give more results on different kinds of models and larger model sizes.
4.	It seems the parameters A, B, C, \alpha, \beta, \gama,and L0 need to be tuned per model (or even per combination of other hyper-parameters). The tuning process needs to collect data from different learning rates. Each optimization takes over 5 × 10^4 steps. The tuning cost is a little high.

### Questions
Please address the questions in weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors formulate and fit an intricate multi-power law (MPL)
function to estimate a subset of learning rate schedules using only
very simple staged LR schedules, i.e., those with constant LR over
different sections of time, for its derivation. The main contribution
is the inclusion of learning rate decay in the formulation of the
scaling law using the empirically motivated MPL term. It is important
to note that the empirical law was fit with extremely few examples,
requiring only 9 training runs for strong fits on unseen data at test
time.

The method is used to propose an optimised WSD-like schedule with a
smoother transition between the constant ("stable") and decay phase.

### Strengths
The paper's findings and the design of the empirical law are extremely
exiting, even with limitations such as only being able to work with a
fixed maximum learning rate. Similarly, being able to extrapolate to
longer horizons is both important in practice but a testament to the
design of the MPL.

### Weaknesses
Despite highlighting the flexibitily of the method, it is only tested
on few unseen LR schedules.

It would be nice to quantify how well/badly extrapolation to other
model sizes works.



### Questions
### Please address

Page 1, line 052f:  
I do not understand: the statement is made here (and in section 5.1)
that only monotonously decreasing schedules ("we restrict our
attention to the class of LR schedules that decay the LR over time")
are used. However, in sections 2 and 3 and appendix C.1, you state
that warmup was included in every experiment and taken into
consideration in practice.

Page 10, line 516f:  
You state that the final learning rate for the "tuned" WSD schedule
was fixed to 1/10 of its peak. I don't think this makes for a fair
comparison, since your proposed optimized version decays to a far
lower final learning rate. This is consistent with results on learning
rate schedules in the LLM setting, which found that a decay to very
low learning rates (more specifically, zero) is best.

### Minor comments

Page 1, line 053:  
Should this be "$\eta_{t} >= \eta_{t + 1}$" instead of "$\eta_{t} >=
\eta_{t - 1}$"?

Page 3, line 123:  
I believe this should this be "as illustrated in Figure 2(b)", not "as
illustrated in Figure 1(b)".

Page 10, line 512f:  
"So the optimization of the WSD schedule is still disturbing."  
Please rephrase this sentence, it is unclear to me what you mean here.
Do you want to imply that optimizing the WSD schedule is difficult?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an empirical scaling law for loss prediction while considering learning rate schedules. The formula is in a multi-power form, which includes a power law that is applied on the sum of learning rates and another power law related to learning rate decay. The rationale behind the approximation has been explained. Loss curves with both predicted and actual values on 25M, 100M, and 400M parameter models have been obtained from experiments and shown in the paper. An approach for finding an optimal learning rate scheduled based on the empirical law is also presented.

### Strengths
- The inclusion of learning rate schedules in scaling law. 
- Experiments were conducted to study various aspects in this work.

### Weaknesses
 - The scaling law expression in (2) is quite complicated, making it difficult to understand the intuitive meaning behind the formula. 
- To apply the result, the initial learning rate still needs to be specified. 
- One way of using the result, as presented in the paper, is to find the optimal learning rate schedule. However, the usefulness of such optimization in practice is not very clear. From Figure 1, the loss difference between the different learning rate schedules seems to be quite small. Only the loss is shown throughout the paper, and no benchmark evaluation result is presented, so it is not clear whether such small changes in loss would actually cause a significant difference in the model accuracy or not. 
- The consideration of models with 25M, 100M, and 400M parameters, adhering to the Llama-2 architecture, may be due to limitations in the GPU resource, which is understandable. However, most practical LLMs have at least 1B parameters, so the current results are insufficient for showing that this scaling law actually works for models with practical sizes. 
- Some figures, such as Figure 2, are quite hard to read and understand, due to the many curves in the figure without a clear labeling of them.

### Questions
- Is it possible to analyze the sensitivity of different terms in the expression (2), and try to simplify the formula while still giving a similar prediction?
- Could you add benchmark evaluation results, to see whether the loss improvement with optimized learning schedule indeed improves the accuracy?
- For figures with two y axes in the same plot, such as Figure 2, could you put each of them into two separate plots with one y axis each, to improve the readability?

### Soundness
3

### Presentation
3

### Contribution
3
