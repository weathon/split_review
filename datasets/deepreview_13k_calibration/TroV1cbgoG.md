# The Role of Label Noise in the Feature Learning Process

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Deep learning with noisy labels presents significant challenges.
In this work, we theoretically characterize the role of label noise in training neural networks from a feature learning perspective.
Specifically, we consider a *signal-noise* data distribution, where each data point comprises a label-dependent signal and label-independent noise, and rigorously analyze the training dynamics of a two-layer convolutional neural network under this data setting, along with the presence of label noise.
Particularly, we identify two stages in which the dynamics exhibit distinct patterns.
In *Stage I*, the model perfectly fits all the clean samples (i.e., samples without label noise) while ignoring the noisy ones (i.e., samples with noisy labels).
In the first stage, the model learns the signal from the clean samples, which generalizes well on unseen data.
In *Stage II*, as the training loss converges, the gradient in the direction of noise surpasses that of the signal, leading to over-fitting on noisy samples.
Eventually, the model memorizes the noise present in the noisy samples, which degrades its generalization ability.
In contrast, when training without label noise, the dynamics do not exhibit this two-stage pattern.
Furthermore, our results provide theoretical supports for two widely used techniques for tackling label noise: early stopping and sample selection.
Experiments on both synthetic and real-world datasets confirm our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper analyses generalisation error of gradient descent with label noise in a binary classification problem setting where the input is split into two patches, with only the first patch being dependent on the class label and the second patch being random noise. The results mainly apply to the setting where the input norm in a noisy patch is much larger than the signal patch and where the number of training points is small relative to the dimension of an input patch. The model is a simple one hidden layer MLP, which is applied separately to both patches and added.


Under this setting the paper goes on to show that the first layer weights pick up the signal component of the data first during training even in the presence of label noise. The mislabelled datapoints are fit by the training algorithm in the second phase which corresponds to overfitting. This motivates the ideas of early stopping during training and outlier identification via large loss.

### Strengths
The paper provides reasonably well written theory and experiments to support a commonly used intuitive heuristic of early stopping and outlier identification. The paper is organised well and is mostly easy to follow.

### Weaknesses
I am not fully familiar with the papers (Cao et al. and Kou et al.) which is the setting this paper also operates in. The setting is extremely simplistic and the final conclusion is not surprising while it may still be technically challenging to prove. It is not clear the extra contribution over those papers is significant enough.

There are a few other technical issues which could be errors in the Theorems/proofs even if the overall message of the paper is correct.

The setting essentially corresponds to linearly separable data with label noise. (the hyper plane with a normal [\mu, \0]  separates the data perfectly). The model is more convoluted and assumes that you know the split of the data x into the noise component and the signal component. This seems very artificial and unrealistic.

From the way $\overline \rho$ and $\underline \rho$ are defined, they seem like symmetric objects with flipped signs. So lines 230 to 233 (and other places) confuse me by stating that $\overline \rho $ keeps increasing, but $\underline \rho$ is bounded below.

### Questions
Please justify this setting of linearly separable data with an unnecessarily complex model in a self contained manner. 

The argument effectively says that as the training progresses, $w_{j,r}$ only has positive components along the noise points $\xi_i$. Why is that?  i.e why is $\overline \rho$ eventually larger than $\underline \rho$?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work examines the learning dynamics of a 2-layer convolutional network with ReLU activations on a signal-noise data distribution from prior work, with the change that the training data sampled from this distribution has flipped labels with non-trivial probability. The main result is a characterization of the dynamics that shows that there are two stages: one in which the model first fits the "clean" data (no label noise) and then a second stage in which the model fits the noisy data.

### Strengths
**Significance:** Non-trivial amounts of label noise in training data is a common occurrence, and this work contributes to our theoretical understanding of how model training works on such data.

**Quality:** This is a mostly theoretical work that is conducted in a well-known setting; the theory seems sound and I did not see any glaring issues (although I did not carefully check details of the calculations in the appendix).

**Clarity:** The paper is overall well-written, and the core proof ideas receive sufficient exposition in the main body of the paper.

**Originality:** Although this work reuses the data model of earlier work [1, 2], it increases the allowable label noise probability of [2].

[1] Cao, Yuan et al. “Benign Overfitting in Two-layer Convolutional Neural Networks.” ArXiv abs/2202.06526 (2022).
[2] Kou, Yiwen et al. “Benign Overfitting in Two-layer ReLU Convolutional Neural Networks.” International Conference on Machine Learning (2023).

### Weaknesses
The main weakness I see with this work is its contribution relative to the previous work of Kou et al. (2023). In particular, I outline my concerns regarding the changes in the theory below (along with a few concerns regarding the experiments).

- **Differences in Setting:** The main differences between the setting in this paper and that of Kou et al. (2023) are that the label noise probabilities $\tau^+, \tau^-$ can be arbitrarily large up to the threshold of not completely destroying the signal ($1/2$), and that the SNR for the setting in this paper needs to be $n * SNR^2 = \Theta(1)$. I view the first change as the main contribution of the paper, however, 
I feel the second change needs further justification.   
The authors claim that this change corresponds to a milder constraint on $d$, but it is not clear to me that this is the case given it could just correspond to a higher signal setting. I agree this would follow if the lower bound on $d$ were only in terms of $|\mu|| \sigma_{\xi}^{-1}$, but the first part of the lower bound in Condition 4.1 does not make sense to me -- the definition of $T^*$ involves $d$ (and if we fix this, we run into the issue I mentioned). Overall, my concern here is that the higher label noise is being counterbalanced by higher signal. It would be very helpful if the authors included something like Tables 1 and 2 from Appendix A of Kou et al. (2023) to have a more granular comparison to the settings of prior work, and justify each change.

- **Differences in Proofs:** Once again, the key difference in the proofs in this paper versus Kou et al. (2023) is handling the different SNR constraint; it would be helpful to provide more exposition regarding the key technique in Kou et al. (2023) to make it clearer how the new proof differs. Also, the authors state that the "signal coefficients are on the same order as noise coefficients", which again goes back to my concern regarding the change to the SNR setting. This does not seem like an extension of the Kou et al. (2023) setting but rather a different setting where we have balanced greater signal strength with label noise.

- **Takeaways:** The main takeaway from the results in this paper is that, because of the two-stage dynamics, early stopping makes sense when training with significant label noise. This is a useful perspective, but it is hard to conclude from the theory itself because we are working in the asymptotic setting. Further experiments investigating early stopping and its relation to the two-stage dynamics would be useful.

- **Experiments:** Minor comments -- neither Figures 1 nor 2 are easy to read by themselves; it would be helpful to either break up the plots more (both figures plot several curves which leads to a lot of visual clutter, at least train/test should be broken up in Figure 2) or provide more textual exposition regarding what's being plotted so that the reader does not have to refer back to the definitions repeatedly. More importantly, I feel it would be useful to have more practical experiments focusing on the two-stage dynamics similar to the synthetic ones. Right now, Figure 2 relies on comparing the accuracies on the noisy/non-noisy samples for a single choice of label noise parameter; it would at the very least be useful to verify the phenomena for a wider range of label noise parameters since this should fall within the theory.

### Questions
- It appears that unlike in prior work, the signal patch here is always fixed to be $x^{(1)}$ -- is this correct? If so, why is this necessary?

### Soundness
3

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
4

### Summary
This paper proposes to theoretically analyze the learning behavior on data sets with label noise. Theoretical results on the case with label noise generally match existing empirical observations, and the authors have also conducted several experiments to verify their theoretical analysis.

### Strengths
- Theoretical results are generally sound and match empirical observations
- The paper is clearly written and easy to understand

### Weaknesses
The novelty seems limited: the analysis mostly follows the framework in (Kou et al. 2023) with modifications to settings with label noise

While the model setup in section 3 should generally follow (Kou et al. 2023), I am a bit curious on how this model can be realized, as it needs to distinguish signal and noise into different parts for activation in advance? I have checked (Kou et al. 2023) but did not find sufficient explanation, and the authors are encouraged to add some explanation for this point.

Also in section 3, the authors mentioned that their analysis is applicable to class-conditional noise. However, I cannot find how this type of noise leads to different learning behaviors, and most quantities related to noise rates $\tau_+, \tau_-$ are symmetric on them. Is this really the case? If so, the authors can clarify this point to avoid possible misunderstandings. 

Note that current analysis focuses on binary classification only, which can be a bit restricted as the noise patterns under binary classification are much simpler: the positive samples can only be mislabeled to negative label, while the negative samples can only be mislabeled to positive label. As such, some discussion on whether the analysis framework can be generalized to multi-class classification is certainly welcome here. 

In addition, I wonder if current analysis can be applied to sample-dependent noise as well, where we can assume the noisy label $\tilde{y}_i$ has some dependencies on the sample noise $\xi$. Some discussion on this direction is also welcome.

### Questions
- While the model setup in section 3 should generally follow (Kou et al. 2023), I am a bit curious on how this model can be realized, as it needs to distinguish signal and noise into different parts for activation in advance? I have checked (Kou et al. 2023) but did not find sufficient explanation, and the authors are encouraged to add some explanation for this point.
- Also in section 3, the authors mentioned that their analysis is applicable to class-conditional noise. However, I cannot find how this type of noise leads to different learning behaviors, and most quantities related to noise rates $\tau_+, \tau_-$ are symmetric on them. Is this really the case? If so, the authors can clarify this point to avoid possible misunderstandings. 
- Note that current analysis focuses on binary classification only, which can be a bit restricted as the noise patterns under binary classification are much simpler: the positive samples can only be mislabeled to negative label, while the negative samples can only be mislabeled to positive label. As such, some discussion on whether the analysis framework can be generalized to multi-class classification is certainly welcome here. 
- In addition, I wonder if current analysis can be applied to sample-dependent noise as well, where we can assume the noisy label $\tilde{y}_i$ has some dependencies on the sample noise $\xi$. Some discussion on this direction is also welcome.

### Soundness
3

### Presentation
3

### Contribution
2
