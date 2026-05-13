# Label-encoding Risk Minimization under Label Insufficient Scenarios

- Decision: Reject
- Scores: 3, 6, 6, 5, 5

## Abstract
The Empirical Risk Minimization (ERM) adopts the supervision information, $i.e.$, class labels, to guide the learning of labeled samples and achieves great success in many applications. However, many real-world applications usually face the label insufficient scenario, where there exist limited or even no labeled samples but abundant unlabeled samples. Under those scenarios, the ERM cannot be directly applied to tackle them. To alleviate this issue, we propose a Label-encoding Risk Minimization (LRM), which draws inspiration from the phenomenon of neural collapse. Specifically, the proposed LRM first estimates the label encodings through prediction means for unlabeled samples and then aligns them with their corresponding ground-truth label encodings. As a result, the LRM takes both the prediction discriminability and diversity into account and can be utilized as a plugin in existing models to address scenarios with insufficient labels. Theoretically, we analyze the relationship between the LRM and ERM. Empirically, we demonstrate the superiority of the LRM under several label insufficient scenarios, including semi-supervised learning, unsupervised domain adaptation, and semi-supervised heterogeneous domain adaptation. The code will be released soon.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates scenarios with limited label information, such as semi-supervised learning or unsupervised domain adaptation for multiclass problems.
It proposes a new way to incorporate the unlabeled data into the risk formulation, by estimating and optimizing the mean prediction for each  class. The method is motivated by NCC, and is demonstrated to be applicable to several base methods, task types, and datasets.

### Strengths
* The proposed modification gives substantial improvements in the experiments, and can be combined with several different base methods.
* The proposal can be applied in several related, but distinct, settings with limited label information.
* I think the single-sample DST+LRM results for Cifar10 (~68%) are quite impressive.

### Weaknesses
### Claims
The paper makes several claims that are wrong or (in my opinion) overstated:


> We prove that the underlying cause of NCC roots in the use of label encoding, i.e., one-hot label encoding, which
> leads to the collapse of the features through back-propagation.

I don't think this is true. On one hand, it requires the injectivity assumption made later in the paper. On the other, I believe that if you assume this, then there is no need for one-hot encodings, e.g., if you use squared error, and map each category to a distinct point in R^m, then optimizing the loss to zero requires the features to collapse for each category.

---

>  Since these label encodings serve as accurate supervision information

This doesn't seem to be true, at least not without additional qualifiers. From the appendix:

> Furthermore, we observe that $w_c^u$ and $s^u_c$ in Eq. (7) may be incorrect at the beginning of the training iteration. 
> To prevent them from fitting into certain categories too early leading to unstable learning, we perform an additional softmax
> transformation before calculating cross-entropy loss, which encourages them smoother. 
> The same strategy is also adopted in the following two tasks.

---

In the intro,
> One problem of EntMin is that the soft-labels assigned by the classifier could be mainly from dominant
> categories with large numbers of samples, resulting in a decrease in prediction diversity (Cui et al., 2020) that the samples are prone to be
> pushed towards the majority categories. One reason for that
> lies in the absence of more appropriate guidance information for unlabeled samples. So we want to
> ask “for unlabeled samples, is there more precise guidance information available?”

To me, this insinuates that the paper would look at imbalanced settings, as these seem to motivate this work here. In fact, though, this is deferred to future work:

> As a future direction, we intend to investigate the relationship between the LRM and ERM, in the context of
> class-imbalanced supervised learning.

---

Theorem 1:
> In addition, Theorem 1 is loss-agnostic and solely relies on the mapping property of f (·)

It is *not* loss agnostic. In fact, the theorem itself states that it assumes L(x,y) =  0 => x = y, which is not true, e.g., for max-margin losses.

> The linear classifier is an injective function, which thus satisfies Theorem 1.

A linear classifier need not be injective. In fact, if C < d, it *cannot* be injective.
Regarding softmax, if you use `f` as the softmax function, and `L` as cross-entropy, then I would no longer call `h` the "features" -- these are now the logits. And I don't think applying L2 normalization or ReLU nonlinearities to the logits is a common practice.

---

sec. 4.2
> These label encodings serve as reliable supervised information for learning from labeled samples.
> Moreover, note that the label encodings remain consistent for both labeled and unlabeled samples
> under label insufficient scenarios studied in this paper. Consequently, it is reasonable to apply
> label encodings to guide the learning process of unlabeled samples. 

that is an unsubstantiated claim (at this point in the paper at least)

> Specifically, we first calculate the weighted average of prediction probabilities for unlabeled samples in each category, i.e., prediction mean.

The way this is written is wrong, though the actual calculations presented in the paper seem to be sensible. You cannot average predictions for unlabeled samples *of a category*, precisely because the categories are unknown. So the averaging is actually over the predicted distribution of categories as provided by some classifier.

### Theorem 3:
Theorem 3 seems to be the wrong way around, in the sense that normally, you'd like the original loss/risk to be upper-bounded by your proposed surrogate, so that optimizing the latter gives some guarantees on the former.

On a positive note, though, Fig. 2 shows that in practice, the two values can be quite close, so this might be more a theoretical concern.

### Readability:
The paper would benefit from grammar improvements. Mostly, these do not impact readability too much. Below are two examples where I don't think the overall sentence structure works.  


page  2:
> As the ERM heavily relies on the guidance of the label information and fails to fully utilize the potential of unlabeled
samples, leading to suboptimal performance in label insufficient scenarios.

page 9: 
> Accordingly, under the setting where only labeled samples from both domains are
> available for training, which can be regarded as a class-balanced supervised learning task.

### questions:
 The label-encoding risk is a *global* quantity, in the sense that is needs to know all training points to be calculated, and does not decompose into a sum over individual points. How does that integrate into mini-batch training?

---

> [...] while in contrast, according to properties (4) and (5) in Theorem 2, LRM minimizes the label-encoding risk, which is verified in Appendix D.4.

I don't understand this argument. Doesn't the LRM minimize the Label-encoding risk by construction? What does this have to do with (4) and (5)?

### Questions
The label-encoding risk is a *global* quantity, in the sense that is needs to know all training points to be calculated, and does not decompose into a sum over individual points. How does that integrate into mini-batch training?

--- 

> [...] while in contrast, according to properties (4) and (5) in Theorem 2, LRM minimizes the label-encoding risk, which is verified in Appendix D.4.

I don't understand this argument. Doesn't the LRM minimize the Label-encoding risk by construction? What does this have to do with (4) and (5)?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Label-encoding Risk Minimization (LRM) for label-insufficient scenarios. The proposed LRM firstly estimates the label encodings through prediction means for unlabeled samples and then aligns them with their ground-truth label encodings. The authors theoretically analyze the relationship between LRM and ERM. The authors demonstrate the superiority of LRM under several label insufficient scenarios, including semi-supervised learning, unsupervised domain adaptation, and semi-supervised heterogeneous domain adaptation.

### Strengths
1.	The paper is well-written and easy to follow.
2.	The paper proves that the underlying cause of neural collapse (NCC) is the use of one-hot label encoding, and proposes label-encoding risk minimization, which minimizes the discrepancy between estimated label encodings of unlabeled samples and their corresponding label encodings. The proposed method is reasonable with a theoretical guarantee.
3.	The authors apply LRM on multiple label insufficient scenarios: semi-supervised learning, unsupervised domain adaptation and semi-supervised heterogeneous domain adaptation. The consistent performance gains validate the effectiveness and generality of LRM.

### Weaknesses
1.	The author primarily proves and experiments with methods in label insufficient scenarios. However, in real-world situations, many data exhibit a long-tail (class-imbalanced) distribution. Can this proposed method be applied to class-imbalanced supervised and semi-supervised scenarios?
2.	As shown in Table1, the authors combine LRM with two semi-supervised methods: FlexMatch and DST. Can the proposed method be combined with other SSL methods, such as MixMatch [1] and ReMixMatch [2]?
3.	As shown in Table2, the authors combine LRM with two UDA methods: CDAN and SDAT. Can the proposed method be combined with SOTA UDA methods [3]?

### Questions
See weakness for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, authors focus on extending the empirical risk minimization (ERM) of the supervised learning to the label insufficient scenarios with proposed label-encoding risk minimization (LRM), which draws inspiration from the phenomenon of neural class-mean collapse (NCC). The core idea of LRM comes from estimating the label encodings through prediction means for unlabeled samples and aligning them with their corresponding ground-truth label encodings.

### Strengths
Specifically, it is implemented by adding LRM term to objective function. Authors not only analyze the relationship between the LRM and ERM in theory, but also demonstrate the superiority of the LRM under several label insufficient scenarios including semi-supervised learning (SSL), unsupervised domain adaptation (UDA) and semi-supervised heterogeneous domain adaptation (SHDA). LRM also can be utilized as a plugin in existing models to cope with insufficient label scenarios. Moreover, parameter sensitivity and feature visualization also be analyzed with elaborate experiments. The paper is overall well written.
Although, the calculation of the prediction means of unlabeled samples is simple, the idea of treating prediction means as an estimation of label encoding is interesting. Experimental results are attractive on several label insufficient scenarios. Fundamental proofs of theorems and implementation details in supplementary material also help with paper understanding for readers.
I'm looking forward to open source codes.

### Weaknesses
However, there are some questions need to be clarified from authors.

1.	In this paper, the core assumption is that the label encodings should remain consistent for both labeled and unlabeled samples under label insufficient scenarios. How about the performance if this assumption does not hold ? In other words, if unlabeled samples have different classes or even class is unknown (All datasets of experiment have explicit classes in manuscript, such as CIFAR, Office and so on.) how we evaluate the LRM ?
2.	Although, authors perform two tasks on class-imbalanced setting in order to verify the effectiveness of the proposed LRM. This is no theoretical guarantee on class-imbalanced supervised learning. If it exceeds the scope of this work, do we need more experiments to support the conclusion ? Because, in the real world, class-imbalanced problem is pervasive.
3.	In Figure 2(a), please give the detailed explanation why the accuracy of ERM is fluctuant while that of ERM+LRM is not. It is hard to understand.

### Questions
1.	In this paper, the core assumption is that the label encodings should remain consistent for both labeled and unlabeled samples under label insufficient scenarios. How about the performance if this assumption does not hold ? In other words, if unlabeled samples have different classes or even class is unknown (All datasets of experiment have explicit classes in manuscript, such as CIFAR, Office and so on.) how we evaluate the LRM ?
2.	Although, authors perform two tasks on class-imbalanced setting in order to verify the effectiveness of the proposed LRM. This is no theoretical guarantee on class-imbalanced supervised learning. If it exceeds the scope of this work, do we need more experiments to support the conclusion ? Because, in the real world, class-imbalanced problem is pervasive.
3.	In Figure 2(a), please give the detailed explanation why the accuracy of ERM is fluctuant while that of ERM+LRM is not. It is hard to understand.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Empirical Risk Minimization (ERM) performs well with the sufficient labels, but suffers from neural collapse in situations with insufficient labels.  In this paper, authors prove that label encoding (one-hot encoding) is the cause of Neural Class-Mean Collapse (NCC), and propose Label-encoding Risk Minimization (LRM) to alleviate the NCC problem.

### Strengths
- The authors have demonstrated the cause of NCC through the use of label encoding and have further enhanced it to improve network performance. 
- The evidence supporting NCC and LRM is explicitly presented.
- Experimental results show that LRM achieves good performance in various tasks such as semi-supervised learning (SSL), unsupervised domain adaptation (UDA), and semi-supervised heterogeneous domain adaptation (SHDA).

### Weaknesses
 - Although authous conducted experiments on a variety of tasks, for each task they only ran experiments on specific datasets. For example, for UDA, they only ran experiments on Office-31 and did not evaluate on many other UDA datasets.

- Authours also do not have experimental results on large scale data. It is not confirmed that their algorithm is useful when training a model from scratch on large scale training data.

### Questions
- Can we say that domain adaptation is a situation where there are not enough labels? A typical domain adaptation is a setting where there are no target labels at all, and the amount of labels in the source data is irrelevant. What does it mean to have insufficient labels in this situation?

- Is there a reason why you didn't perform experiments on a large scale dataset such as ImageNet?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a Label-encoding Risk Minimization (LRM), which draws inspiration from the phenomenon of neural collapse. Specifically, the proposed LRM first estimates the label encodings through prediction means for unlabeled samples and then aligns them with their corresponding ground-truth label encodings. As a result, the LRM takes both the prediction discriminability and diversity into account and can be utilized as a plugin in existing models to address scenarios with insufficient labels. Theoretically, the authors analyze the relationship between the LRM and ERM.

### Strengths
- The authors propose a new method to extend the limitation of classical Empirical Risk Minimization (ERM) into the label insufficient scenario.
- The experiments have been conducted to illustrate the superiority of the proposed method.

### Weaknesses
 - The authors validate the performance of the proposed only on some small-scale datasets, such as CIFAR-10, CIFAR-100, an so on. The validation on larger-scale datasets are missing. 
- The qualitative analysis and visualization in experiments are missing.

### Questions
- The authors validate the performance of the proposed only on some small-scale datasets, such as CIFAR-10, CIFAR-100, an so on. The validation on larger-scale datasets are missing. 
- The qualitative analysis and visualization in experiments are missing.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
