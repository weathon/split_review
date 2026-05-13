# Scaling Law with Learning Rate Annealing

- Decision: Reject
- Scores: 6, 5, 8, 8

## Abstract
We find that the cross-entropy loss curves of neural language models empirically adhere to a scaling law with learning rate (LR) annealing over training steps:
$$L(s) = L_0 + A\cdot S_1^{-\alpha} - C\cdot S_2,$$
where $L(s)$ is the validation loss at step $s$, $S_1$ is the area under the LR curve, $S_2$ is the LR annealing area, and $L_0$, $A$, $C$, $\alpha$ are constant parameters.
This formulation takes into account two factors: (1) power-law scaling over data size, and (2) the additional loss reduction during LR annealing. 
Therefore, this formulation can describe the full loss curve at each step, rather than the single loss point at the end of training.
Applying the scaling law with LR annealing and fitting only one or two training curves, we can accurately predict the loss at any given step across any learning rate scheduler (LRS).
This approach significantly reduces computational cost in formulating scaling laws while providing more accuracy and expressiveness for training dynamics.
Extensive experiments demonstrate that our findings hold across a range of hyper-parameters and model architectures, and our equation can extend to scaling effect of model sizes.
Moreover, our formulation provides accurate theoretical verification and explanation for empirical results observed in numerous previous studies, particularly those focusing on LR schedule and annealing.
We believe that this work is promising to enhance the understanding of LLM training dynamics while greatly democratizing scaling laws, and it can guide researchers in refining training strategies (e.g. critical LRS) for further LLMs~\footnote{We welcome any feedback, comment, and discussion at \href{https://www.alphaxiv.org/abs/2408.11029}{AlphaXiv} or \href{https://huggingface.co/papers/2408.11029}{HuggingFace}, where we also provide our implementation codes.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a scaling law that predicts the full loss curve of LLM pretraining: $L(s) = L_0 + A \cdot S_1^{-\alpha} - C \cdot S_2$. Extensive experiments demonstrate the law's effectiveness across many LLM pretraining settings. It can also be used to guide practitioners in choosing hyperparameters when setting the LR schedules.

### Strengths
1. Deriving a more accurate scaling law for LLM pretraining is an important topic. This paper presents a novel scaling law for loss curve prediction.
2. The proposed scaling law is validated in many LLM pretraining settings.
3. The proposed scaling law can be applied to guide practitioners in choosing hyperparameters when setting the LR schedules.

### Weaknesses
1. It is not very clear what kind of LR schedules this scaling law is applicable to and how large errors we will get for different schedules. I understand the authors' point that the law can be applied to various practical learning rate schedules. Still, it is easy to find or imagine many failure cases.
    * If we use an extremely large learning rate (say, 100) once in a while, the pretraining loss will go up to the level of random guessing repeatedly. Near the end of training, we turn to use very small learning rates. The proposed scaling law in the paper would suggest that doing this will lead to a much smaller loss than training without the extremely large learning rates, but it is hard to believe it to be true in practice. 
    * This law is invariant to padding zero learning rates at the end. For a training run with some learning rate schedule, adding more steps with zero learning rate should not change the final training loss. However, if we pad zeros at the end of the learning rate, the scaling law will predict a much smaller loss as $S_2$ will gradually increase to its maximum possible value $\eta_0$. There is a related discussion on this in Appendix H.3, and the authors proposed to add a multiplicative factor at some places of the formula. But this does not really lead to a different loss formula because the factor $\approx 1$ after fitting real data (i.e., $\epsilon \approx 0, \eta_i^\epsilon \approx 1$).
    * For the learning rate schedules in Figures 3(c) and 3(d), the scaling law's predictions deviate from the actual values by quite a lot. The predicted curves do not always follow the same trend as the actual curves, which is a concern because it could lead to incorrect conclusions about which schedules are better.
    * If at each step, I randomly choose the current learning rate from a uniform distribution (e.g., U[0, 1e-4]), will the scaling law still work?
2. While the title of Section 3 is called “Theory,” there is no real theoretical analysis in the paper to justify the proposed scaling law. The power law form for $S_1$ is obtained through speculation. The momentum form of $S_2$ is obtained from the observation of delay phenomenon, but it doesn't exclude the possibility that other forms could be better, e.g., sliding window average, or the same momentum form but the momentum coefficient $\lambda$ depends on learning rates. I acknowledge that proving any theorem about the loss curve in deep learning is hard, but I would like to see more evidence that every component of the scaling law is important (and perhaps irreplaceable). Doing some ablation studies could also be informative.

### Questions
It is an interesting paper overall, but I would like to see the authors' response to the two weaknesses I listed above.

=============

Post-rebuttal update:

I'm satisfied with the authors' response and would like to thank them for the additional experiments and clarification.

Assuming that the authors will further clarify to what schedules their scaling laws are applicable, I'm willing to raise my score to 7.
* Finding a good scaling law to capture LR schedules is challenging, and I don't think we should reject a paper because it has some failure cases. But the paper has to make enough efforts to search for failure cases and report them clearly for future exploration.
* I would encourage the authors to think more deeply about the precise definitions of "common" and "corner" cases. What properties are shared by widely adopted schedules that make the proposed scaling law work in practice?

As only 6 and 8 options are available, I have to keep my score 6 in the system.

### Soundness
3

### Presentation
2

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
This paper proposes a novel scaling law for training loss of language models when annealing learning rates. The new formulation
accounts for two main effects: (1) power-law scaling over data size, and (2) the additional loss reduction during LR annealing.  Applying the scaling law with LR annealing and fitting only one or two training curves, the authors show that their scaling law can accurately
predict the loss at any given step under any learning rate scheduler, under certain restrictions. The authors provide extenisive experimental verification for their scaling law for a range of hyper-parameters and model architectures, which can even be extended to scaling effect of model sizes.

### Strengths
This paper is well-written and easy to understand. The topics studied in this paper,  scaling law for training loss when annealing learning rates, is very related to the topic of ICLR conference and is of great significance, both theoreitcally and empirically.  The specific scaling law (Equation (1)) seems novel to me. The authors also provide extensive experimental justification for the accuracy of the scaling law, e.g. for cosine or WSD schedules. Overall I feel like this scaling law is quite non-trivial and will shed some light on studying the optimal learning rate schedule in pretraining, at least under certain conditions.

### Weaknesses
It is not completely clear under what assumptions the scaling law holds. Without necessary restrictions or premises, the scaling law seems problematic for the following obvious reasons.

1. Adding more steps with zero learning rate always reduces the predicted final loss. Any reasonable scaling law should be invariant to such operations like adding steps with zero learning rate which does not change the parameters at all.
2. Multiplying the entire schedule elementwise by a positive constant larger than 1 always decreases the predicted loss. This suggests that the scaling law must break when we use a sufficiently large peak learning rate. This is a very important limitation and I could not find related discussion on this.
3. Combing 1 and 2, if I solve for optimal LR schedule, what I get is at the first step I use an infinitely large LR, then I use 0 LR for many steps. This will give me a negative loss.


Besides the above main concern, I would like to see real applications of the scaling law, e.g., how we can make training or LR tuning more efficient by using this scaling law. I also would like to see more theoretical justifications for the scaling law.

### Questions
See weakness

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
4

### Summary
The paper proposes a new scaling law which captures the complete loss curve of a training run, instead of only fitting the final loss as done by traditional scaling laws. It shows that just using a constant and cosine schedule curve, it can predict the loss of any other lr schedule, including re-warmup periods.

### Strengths
The paper proposes a new scaling law for modeling the complete training loss curve for any schedule. It shows impressive results on predicting the loss curves of various lr schedules such as WSD, re-warmup, by training only on a single constant and cosine schedule trajectory. It shows results across various architectures such as MOEs as well as various model scales.

### Weaknesses
Some points in section 4.4 and 6 seem irrelevant. In section 4.4, the first point, about loss decreasing suddenly at lr annealing, the given equation has an inherent term S2 modeling the same. It feels a bit redundant to state this point, and this definitely cannot be stated as 'the reason behind why loss drops suddenly'. Similarly, in section 6, the exploration of the question 'why is there a momentum in loss while lr annealing' seems insufficient. The discussion lacks a mechanistic explanation of why the loss continues to decrease even after the learning rate has been reduced, which is a critical aspect of understanding the dynamics of the proposed scaling law. Specifically, the paper does not delve into the interplay between the learning rate, the optimization landscape, and the accumulated gradients, which could provide a more rigorous explanation for the observed momentum in loss.

### Questions
1. Is it possible for given values of lambda and other parameters, to predict the optimal learning rate schedule for a given training duration?

2. It would be really interesting to study the tradeoff in MOEs for the number of experts with different training durations - should the number of experts be increased for longer training durations?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper gives an analytical expression for the loss a a function of the learning rate schedule (after fixing “training and validation dataset, the same model size, the same training hyper-parameters such as warmup steps, max learning rate ηmax and batch size”). Their common expression accounts for both the benefit in loss due to more training duration as well the benefit due to learning rate annealing.

### Strengths
Learning rate scheduling is an important problem in the training of LLMs, which had not yet been addressed in general (i.e. given a schedule predict the final loss), this paper addresses that problem. While I do not believe the results in the paper are perfect, they are an important first step in addressing this problem. As an example of their predictive power they are able to approximately predict the behavior of loss even when it is non-montonic (Fig 3d).

### Weaknesses
Weakness:
1. The results in the paper would have been much easier to interpret had there been a comparison to simple baselines. For example, how good is the fit which averages the loss curves of all the schedules tried?  (for a fixed eta_max, batch size etc.)
2. One of the main application the results is comparing different schedule. In Section 4.3 “Determining optimal annealing ratio of wsd scheduler” the authors claim to explain the commonly observed durations of annealing in WSD (10-20%). It would have been more convincing if the authors had validated their curves empirically. For example in the predicted curves 
   
   a. The difference between cosine and WSD (with optimal hyperparams is around .05)
   
   b. The optimal anneleaning fraction decreases with more training. 
   
    Are these two observations matched in practice? As an evidence against a., in Hägele 2024 they observe that after decaying cosine to 0 they can match the performance of WSD.

### Questions
Some questions are present in the previous section of the review.

“The results show an almost perfect fit, achieving a coefficient of determination (R2) greater than 0.999.” Is this correlation for a single fit (i.e. “Given the same training and validation dataset, the same model size, the same training hyper-parameters such as warmup steps, max learning rate ηmax and batch size) or across multiple model fits? Because fitting across multiple models would not be statistically sound, if that is the case the authors should instead report the average of R^2 across different models.

### Soundness
2

### Presentation
3

### Contribution
3
