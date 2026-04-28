# A Curriculum View of Robust Loss Functions

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Robust loss functions are designed to combat the adverse impacts of label noise, whose robustness is typically supported by theoretical bounds agnostic to the training dynamics. However, these bounds may fail to characterize the empirical performance as it remains unclear why robust loss functions can underfit. We show that most loss functions can be rewritten into a form with the same class-score margin and different sample-weighting functions. The resulting curriculum view provides a straightforward analysis of the training dynamics, which helps attribute underfitting to diminished average sample weights and noise robustness to larger weights for clean samples. We show that simple fixes to the curriculums can make underfitting robust loss functions competitive with the state-of-the-art, and training schedules can substantially affect the noise robustness even with robust loss functions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors examine the challenges of underfitting and the factors influencing the robustness of loss functions in the context of training with noisy labels. They approach these questions by analyzing robust loss functions through a lens that emphasizes the importance of sample-weighting strategies and an optional implicit regularizer. To address underfitting, they suggest modifying these sample-weighting approaches. Additionally, they present evidence that refining the schedule of learning rate adjustments can enhance the robustness of the loss functions.

### Strengths
* This work connects several popular robust loss designs to a sample-weighting curriculum.

* Empirically, the authors explain the two open questions in the literature of learning with noisy labels. The introduce of a marginal effective learning rate looks interesting and helps with explaining the underfitting issue. And the shifting of soft-margin mitigates the underfitting, especially when the number of classes is large.

### Weaknesses
 * The presentation of experiments could be further improved, i.e., what is $\tau$ in Figure 4.

* The proposed strategy for shifting and rescaling appears to hold potential; however, its design is somewhat heuristic and depends heavily on a crucial hyper-parameter. This may hinder the efficient usage of the proposed method in practice.

* In Table 3, why MAE has such pretty bad performances under CIFAR-100?

* Maybe I missed some important details, I was wondering how authors pick  $\tau$ for reporting experiment results in Table 5, 6.

### Questions
My main concerns are from the empirical sections:

* what is $\tau$ in Figure 4?

* In Table 3, why MAE has such pretty bad performances under CIFAR-100?

* Maybe I missed some important details, I was wondering how authors pick  $\tau$ for reporting experiment results in Table 5, 6.

### Soundness
3 good

### Presentation
3 good

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
The goal of the paper is to study the behaviour of robust loss functions during training from a sample reweighting perspective. To do this, the authors propose to rewrite each loss on a common form that has the same gradients as the original loss. This common form is of a gradient weight $w$ times a margin difference $\Delta$ (they also consider a more general form taking regularization into account). The authors then study these two quantities for different loss functions during training for clean and noisy labelled examples separately. For example, i) they find that gradient weights are higher for clean samples for the losses that generalize the best, ii) Mean Absolute Error (MAE) first learns easy examples which causes lower $\Delta$ of noisy examples (“sample sifting”), iii) label smoothing increases convergence and separations in $\Delta$. Finally, the authors study the underfitting issues of MAE via $w$ and $\Delta$ and proposes an effective fix.

Therefore, the contributions of the paper are to rewrite the losses on a common form, their observations, as well as the modification of MAE.

### Strengths
I find the paper has a well-organized structure which makes the high-level ideas easy to follow. I did not notice any technical issues in the paper. Furthermore, I like that mean and standard deviation were reported in Table 6, to show have some indication of variance between runs. The results are reproducible as the training setup (architecture, learning rate, weight decay, etc) are clearly stated including what hyperparameters were used and how they were selected. As far as I know, there is theoretical novelty in rewriting of the losses into a common form, and algorithmically in the proposed change to MAE.

### Weaknesses
I immensely value research papers improving our understanding and not just present a new method, which I believe is the goal of this paper. Having said that, I believe the significance of this work could be improved considerably by making the explanations, findings, and conclusions **clearer**:
* What is the motivation for rewriting the losses in this particular way? What novel perspective does this form give over something more intuitive like the $p_y$ and the gradient magnitude of the loss wrt to the logits? For example, in Figure 1, couldn’t one see the same thing with an x-axis with $p_y$ instead of $\Delta$, and the y-axis being the gradient magnitude wrt the logits for the MAE green curve instead of $w$?
* How isn’t it trivial that different loss functions have different gradient weights, and therefore different sample weights? If all loss functions penalized the same, there would be no reason to have different ones?
* A single sentence motivating the inequality in Equation 5 would make it clearer.
* The clarity of several equations could be improved:
  * The equation between Equations 2 and 3 is crucial and could be made much clearer: i) a single sentence discussion or motivation for using stop gradient, ii) what $\Delta_y$ is, iii) why two additional minus signs are added in the middle equation, iv) and as $w$ is a key component of the paper, I believe it deserves a proper definition.
  * The equation at the end of page 3: i) why are stop gradients used in that derivation? ii) why is a factor of k and 1/k introduced?
* It was unclear to me, why the more general form that accounts for regularization was introduced, when its properties like $R(s)$ never were studied.

**Experimental Rigor.**

Reporting mean and standard deviation would improve the conclusiveness of the observations in the tables. Furthermore, the network predictions from several runs could be used to have more reliable histogram estimates (more data).

**Novelty and Significance.**
* What novelty and significance does this work add over that of Wang et al. [1]?
  * What are the benefits of viewing the losses in terms of the gradient of $\Delta$ rather than the more natural gradient magnitude wrt to the logits?
  * The following finding is not novel: “Zhang & Sabuncu (2018) attribute underfitting of MAE to the lack of the 1/py term in sample gradients, which “treats every sample equally” and thus hampers learning. In contrast, we show that MAE emphasizes samples with moderate ∆(s, y).” That MAE does not treat samples equally and instead focus on examples with moderate loss/$\Delta$, is not novel in this work. This is one of the main findings of Wang et al., which is clearly shown in their Figure 1 (or 2 depending on version of the paper), where examples with low and high $p_y$ have small gradients.
  * I believe the following quote is misrepresenting the related work: “.. attribute underfitting to their low variance, making clean and noise samples less distinguishable. But as shown in Table 4 MAE can underfit data with clean labels.”. Wang et al. did not mention that the variance was low between clean and noisy samples, but rather the more general “informative” and “uninformative” examples. Furthermore, the finding that MAE underfits clean examples is not novel, and even Wang et al. clearly shows this in their Table 1.
  * Finally, Wang et al. already proposed a fix for MAE. Therefore, the novelty and significance of the proposed fix in this paper is unclear. A proper comparison (theoretically and experimentally) with other fixes for MAE is required.
* What’s the significance of the proposed way of rewriting the loss functions? If one instead does similar studies in terms of loss values (e.g., Figure 3 in [1], and Figure 2 in [2]) or gradients (e.g., Theorem 1 in [3]), it seems many of the findings in the paper are already well-known. For example, that the gradients of clean examples dominates the early learning phase and then the gradients for noisy labelled examples take over, resulting in overfitting [3]. Another example, that regularization methods If there are any novel and significant findings, I believe the authors should much more clearly state, relate, and discuss the significance of them compared to related work. That MAE focuses on moderate loss examples, as shown by Wang et al. (2019a).


**Missing related work.**

The list of robust loss functions is comprehensive, but missing some relevant ones based on information theory: i) f-divergences [5], ii) Bregman divergences [6], and iii) Jensen-Shannon divergences [7].

### Questions
Why would one use your rewriting of the loss function to study the training dynamics of robust loss functions over say the gradient perspective in Wang et al. or that in the GCE paper? What novel findings do you, and can you, make only because of this framework?

Most experiments, and the only proposed fix based on the analysis, are related to MAE. As Wang et al. has studied and proposed a fix for MAE, could you clarify what novelty you bring to the understanding of MAE, and why it is significant?

Why would one use your fix for MAE over the fix proposed by Wang et al.?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates robust loss functions used in learning with noisy labels. This paper unifies a broad array of loss functions into a novel standard form, which consists of a primary loss function inducing a sample-weighting curriculum and an optional implicit regularizer. The resulting curriculum view leads to a straightforward analysis of the training dynamics, which may help demystify how loss functions and regularizers affect learning and noise robustness. This paper shows that robust loss functions implicitly sift and neglect corrupted samples, and analyze the roles of regularizers with different loss functions. Finally, this paper proposes effective fixes to address the underfitting issue of robust loss functions.

### Strengths
- A novel curriculum perspective of robust loss functions is proposed, which consists of a primary loss function inducing a sample-weighting curriculum and an optional implicit regularizer.
- A sufficient number of robust loss functions are reviewed.
- The proposed simple fix seems to work well.

### Weaknesses
 - Although a novel perspective that includes many loss functions is proposed, this perspective is unable to guide us to obtain any better robust loss functions, except for the simple fix to alleviate the underfitting issue.
- To me, the fix derived from the curriculum view is the central part of this paper. However, this paper did not provide extensive experiments to empirically validate this method. Is this method versatile enough? Can any robust loss functions (excluding MAE) be equipped with this method? Can this method work well on a variety of large-scale datasets? Without clearly and extensively demonstrating the effectiveness, the key contribution this paper seems limited.

### Questions
- Is the proposed fix versatile enough? 
- Can any robust loss functions (excluding MAE) be equipped with this method? 
- Can this method work well on a variety of large-scale datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new perspective for robust losses when learning with noisy labels. The authors show that most robust loss functions differ only in the sample-weighting curriculums they implicitly define with an optional implicit regularizer. This fills in the explanation of the dynamic performance of robust losses in training. Then the authors show the effects of loss functions and regularizers on learning through empirical studies, respectively.

### Strengths
- The motivation for understanding empirical phenomenons of robust losses against label noise is interesting. The common features different losses shown make the understanding significant. Good motivation, especially since the data are becoming larger and learning with noisy labels is becoming a pressing challenge.

- The empicial results echo the theoretical study. This paper conducts extensive experiments and comprehensive studies to evaluate the losses and regularizers, which helps give suggestions for using them.

- Experiments are well designed. The theoretical statements in this paper seem correct. I think this work is valuable.

### Weaknesses
 - The robust losses involves the curriculum view, i.e., a sample-weighting perspective, the paper should include more discussion and empirical comparisons with curriculum and reweighting noisy-label learning methods.

- Eq.3 appears to rely on a number of assumptions, which should be clarified in the formulation of these assumptions.

- As one of the main formulas of the paper, it is not quite clear how Eq.4 was obtained. More details should be provided.

### Questions
The results and findings in this paper are insightful and would be useful for future research. The paper is also well-written with solid theoretical exposition and strong results. Overall, this is a good paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
