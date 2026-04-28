# Straight to Zero: Why Linearly Decaying the Learning Rate to Zero Works Best for LLMs

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 5, 8

## Abstract
LLMs are commonly trained with a learning rate (LR) warmup, followed by cosine decay to 10% of the maximum (10x decay). In a large-scale empirical study, we show that under an optimal max LR, a simple linear decay-to-zero (D2Z) schedule consistently outperforms other schedules when training at compute-optimal dataset sizes. Benefits increase further with more training tokens; e.g., a 617M-parameter model trained for 80 tokens-per-parameter (TPP) using D2Z achieves lower loss than when trained for 200 TPP using 10x decay, corresponding to an astonishing 60% FLOPs savings. This implies models like Llama2-7B, trained for 286 TPP with 10x decay, were severely under-decayed. We demonstrate the benefits of D2Z across a range of model sizes, batch sizes, and other training configurations. We explain the success of linear D2Z via a novel interpretation of AdamW as a convex combination of weight updates, with coefficients governed by the LR schedule. This interpretation demonstrates how linear D2Z balances the demands of early training (moving away quickly from initial conditions) and late training (smoothing over more updates to mitigate gradient noise).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyses the role the learning rate scheduler for LLM pre-training. The authors mainly focus on two questions:
- can we replace the widely used cosine learning rate scheduler by a simpler linear decay?
- can we do better than the commonly used rule to take the final lr as 1/10 of the peak lr?
The authors answer positively those two questions, demonstrating that a linear lr decaying to 0 works best for small models (most experiments are on 600m models, a few on 1.7B models) on the slimpajama dataset.
The authors conduct many ablations on the subject, including training length, sensitivity to peak lr, and role of weight decay.
The authors also propose a theoretical framework to try to understand this, based on unrolling EMAs with varying step-sizes.

### Strengths
- this paper studies a very important problem, that of the training dynamics of LLMs
- it is well-written and easy to read
- it makes a compelling story
- the paper convincingly demonstrates the importance of completely annealing the learning rate for small models on one dataset

### Weaknesses
 - The main weakness of this work is the small scale of the experiments. For instance, the base learning rates for the small-scale models used in this paper are very high (cf table 2 and fig.10, best lr is around 3e-3), so decaying it to 10x still yields a high LR at the end of training. For bigger models, the base lr is much lower (typically 3e-4 or 1e-4 for 7B models, even lower for larger models). Therefore, the final lr when using the 10x technique is low in this case. Hence, it is very likely that the impact of d2z would be far less in these cases (for instance, in Fig. 10, there is barely any difference between d2z and 10x for these learning rates).
In order to address this concern properly, this paper needs to show that the benefits of d2z do not completely vanish at large scales. A similar base lr sweep to that conducted for the 600M models for the 1.7B model would benefit the paper greatly.


- The methods section seems very vague:
    - There are no formal statement, everything is hand-wavy
    - The main problem with the discussion regarding the EMAs, and summarizing everything with the variables $c_{t, i}$, is that it makes it seem that the variables $x_t$ in the parameter’s update EMA (eq.3) are external variables to the problem, while clearly they depend on the parameters $y_t$ themselves. This makes all the discussion in section 3 flawed.

- The impact of the dataset is another thing that is not discussed, while it will change the learning curves. This warrants at least a discussion, clarifying that the phenomenon observed here might not happen for datasets of different sources/quality.

### Questions
- what base lr is used to train the 1.7B models?
- It is doubtful that d2z is optimal: with d2z, the last iterations have an almost zero learning rate, yielding no progress and effectively wasting these last steps. This effect is worsened for the cosine schedule, which spends more time at low lr's. Having a non-zero value for the last lr would be better: how about a decay to, e.g., 100x? I understand that this leads to another hyperparameter to tune, which is cumbersome, but this could also be discussed.

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
This manuscript empirically demonstrates that, with a fixed maximum learning rate, a simple linear decay-to-zero (D2Z) schedule often outperforms the widely-used cosine decay to 10% of the maximum, as well as other popular learning-rate schedules. It also shows that linear D2Z is robust to variations in maximum learning rate, weight decay, dataset size, and batch size.

### Strengths
The manuscript presents extensive experiments that validate the effectiveness of D2Z for training GPT-like models with 111M, 617M, and 1.7B parameters. It effectively illustrates D2Z's robustness across different maximum learning rates, weight decay values, dataset sizes, and batch sizes.

### Weaknesses
 - Linear D2Z appears to function more as an engineering trick than a comprehensive algorithm. While it demonstrates empirical effectiveness, the theoretical justification is somewhat unconvincing. The authors attempt to explain its success through theoretical convergence analysis (Eq. (1)) and update rules involving weight decay (Eq. (3), Eq. (4)), but a unified framework to interpret the results clearly is lacking. It seems the authors selectively apply certain perspectives to support their experimental findings. Furthermore, the convergence bound in Eq. (1) applies only to convex optimization problems with SGD, which are significantly different from the training of large language models (LLMs) using Adam. In summary, a more rigorous mathematical framework that connects the empirical results to theoretical principles is needed.

- Although the manuscript presents simple scaling law experiments in Appendix B.10, the experimental details are unclear. The authors are encouraged to provide more comprehensive information on scaling law experiments for D2Z to demonstrate its applicability to larger models.

- D2Z requires prior knowledge of the total number of iterations, which is not ideal for continuous pretraining scenarios. In contrast, WSD and cyclic schedules  are  more effective for continuous pretraining.

### Questions
Subsection 3.3 has a weak connection to the overall manuscript.  Can you further clarify its relevance to the main findings about D2Z.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The submission studies learning rate scheduling for LLM pre-training, in particular, the paper notices that, in high TPP setting, i.e. when the model is trained much longer than what scaling laws recommend, a linear decay to zero (D2Z) scheduling gives optimal performance and converges faster than the commonly used cosine decay to 0.1 max_lr. To be more specific, the method utilizes a recently proposed interpretation AdamW, which suggests that the model weights at a certain time step is an exponential moving average of past updates, with the smoothing factor determined by learning_rate * weight_decay_coefficient. Based on this observation, the authors suggest that linear decaying to zero allows for more updates to be averaged, therefore reducing the variance, which is a crucial component in the later phase of the optimization (which is the pattern for high TPP setting). 

The paper then empirically verifies the claims on an **extensive** set of experiment settings, all confirming the benefit of linear D2Z: Including better validation loss in high TPP setting, less sensitivity to the choice of batch size, learning rate setting. Additional experiment results are also presented in the appendix.

Overall, I find the paper well written, the presentation is very clear, and the empirical evidence convincing.

### Strengths
- The paper studies an important problem: How to schedule the learning rate, a critical but under-studied issue, until recently by Defazio et al. (2023). 

- The paper also studies the role of weight decay (as well as its interaction with learning rate and learning rate scheduling), which is also under studied, until recently by Andriushchenko et al. (2023) and  Wang & Aitchison, (2024)

- The argument, despite not being supported by strict proof, is built upon classic optimization theory (bias-variance decomposition) and simple linear algebra (EMA perspective of AdamW), so I find the claims fairly rigorous.

- The authors explore a wide range of confounding factors that could affect the conclusion on "best learning rate schedule", such as peak learning rate, batch size, weight decay, training length, and observe similar pattern across all settings, therefore I find the conclusion very solid and would consider starting using linear D2Z in my own LLM experiments.

### Weaknesses
 - I think there is room for improvement in the writing: Section 3.1 and 3.2: The paper's main argument is about the optimality of linear D2Z, but these two sections do not talk about, e.g. why cosine decay is suboptimal (which was only briefly mentioned in the caption of FIg.2) or why decay to zero is better than decay to 0.1 max_lr. Although I do understand the connection between the suboptimality of other scheduling and the reducing variance perspective, more explicit arguments can be made to improve the readability.

- The cyclic learning rate scheduling (or is it just cosine learning rate decay?) is used in experiments as a baseline but not explained or discussed in, e.g. Figure. 2.

- It would be nice if more details about the computational resources, model configuration (e.g. number of self attention layer, head, hidden dimension size) can be revealed.

- It would be nice if the experiment code can be released.

### Questions
- I really like the author's argument on why, given a fixed value of eta * lambda, modifying eta does not have the same effect as modifying lambda, since having a lambda too large would affect the bias reduction. I wonder if the authors have considered mitigating this issue by modifying the weight initialization scale: The EMA perspective suggests that the weight will end up having a magnitude ~ 1 / lambda, and if lambda is large, the relative difference (bias) between the final weights and initialization of fixed magnitude will indeed be very small, however, one can consider additionally scale the initialization by 1 / lambda, such that the bias could potentially be reduced at larger lambda. Such a strategy is also suggested by Wang & Aitchison, (2024) in Appendix A, Eq. 21 (but under fully scale invariant network assumption).

- I wonder what does the author think of the reason behind Finding 4, i.e. weight decay is beneficial only used together with certain learning rate scheduling. Such behavior is also observed when training ResNet on CIFAR-10, Loshchilov & Hutter, 2017 noticed that weight decay can improve test accuracy only combined with learning rate scheduling.

- Notice that the dataset scaling rule Wang & Aitchison (2024), also implied that the learning rate should increase as batch size increase, in particular, the authors suggest that the key hyperparameter is M * eta * lambda, where M = number_of_training_point / batch_size, therefore as batch_size increase, eta * lambda should also increase. But Wang & Aitchison (2024) mainly considered high-epoch settings with the dataset being repeated multiple times (e.g. standard CIFAR-10 training pipeline) so their claims may not be transferrable to LLM pre-training where the same training data point almost never show up twice.

- In a very extreme and unrealistic setting, where we can afford full batch training, in which case I wonder if weight decay can be entirely removed since there will be no gradient noise at all?

- I believe such interpretation can also be applied to nonadaptive optimizers, e.g. standard SGD or Sign-GD with momentum, would the authors think the claims still hold true?

- (Minor) Why is the batch size chosen as multiples of 63? This seems to be a weird number.

### Soundness
3

### Presentation
4

### Contribution
3
