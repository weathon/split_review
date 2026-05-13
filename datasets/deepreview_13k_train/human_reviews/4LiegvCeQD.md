# IEL: Intra-Model Ensemble Learning For Single Sample Test-Time Adaptation

- Decision: Reject
- Scores: 1, 3, 3, 3

## Abstract
Test-Time Adaptation (TTA) problems involve adapting pre-trained models to new data distributions in testing time, with access to only model weights and a stream of unlabeled data. In this work, we present IEL, a method for adapting sets of independently pre-trained classifiers to distribution shifted data one sample at a time without labels. We minimize the cross-entropy between the classifier output that has the highest predicted probability for the majority voted class (a high confidence softmax) and all other models in a set of classifiers. The majority voted model that all others learn from may change from sample to sample, allowing the group to collectively learn from each other. Our method uniquely optimizes all trainable parameters in each model and needs only a single sample for adaptation. Using sets of independently pre-trained base classifiers with distinct architectures, we show that our approach can reduce generalization error for image classification tasks on corrupted CIFAR-10, CIFAR-100, and ImageNet while also minimizing the entropy of model outputs.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper introduces an intra-model ensemble learning method for single sample test-time adaption. It minimizes the cross-entropy losses between the output with the highest confidence score and all other classifier's outputs. It optimizes all trainable parameters (except for BN layers) and requires only a single sample for TTA. It achieves improved performance on corrupted datasets including CIFAR10-C, CIFAR100-C and ImageNet-C.

### Strengths
- The paper addresses a challenging TTA settings where only a single, unlabeled sample is given for adaptation during test time.
- The paper adopts an interesting approach of ensemble learning to dynamically optimize a group of learners (pre-trained models), showing improved TTA performance.

### Weaknesses
 - The proposed algorithm offers no substantial improvement over existing ensemble learning methods. It simply combines 1) selecting the most confident prediction and 2) cross-entropy minimization of ensemble models. Technical contributions to both ensemble learning and single-sample TTA remain limited.
- The paper lacks sufficient experimentation to demonstrate the proposed method’s effectiveness. It only compares results across different backbone architectures, without considering other baseline methods suitable for single-sample TTA, such as NOTE [1] and REALM [2]. Additionally, it does not explore alternative TTA settings, such as continual TTA, where incoming domains continuously change.
- The experiment section (Sec. 4) requires more careful writing and clarification. For instance, it should include a clear definition and detailed description of the tuning set samples, as well as more comprehensive experiments, including ablation studies, to examine the correlation between the number of ensemble models and TTA performance.
- In Section 4.1, the authors state that no catastrophic forgetting was observed on the ImageNet-C dataset. However, this is unlikely to be accurate since only 7,000 samples per corruption type from ImageNet-C were used for evaluation. More rigorous experiments and substantiated claims are needed.
- As noted in the limitations, the proposed method requires significant computational resources to utilize multiple pre-trained networks. However, the paper does not provide any empirical analysis or comparison of computational cost or adaptation latency.

### Questions
Please refer to the weaknesses part.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a test-time adaptation (TTA) technique based on model ensembling. A set of models is simultaneously trained, and for each sample, the model with highest confidence is used as a teacher for all student models. Updates happen via standard cross-entropy. The authors show improvements over a non-adapted baseline model across CIFAR10/100-C and ImageNet-C.

### Strengths
The technique is simple and elegant. It generalises the typically used concept of a student/teacher setup which typically uses a single model, and is straightforward to scale in practice (by increasing the size of the ensemble).

### Weaknesses
The presentation and investigation done in the paper is well below the bar for ICLR. There are no baselines, and the results are not well presented and contextualised. The introduction to the paper is lengthy, and should be made more crisp. The contribution statement is not accurate and needs to be adapted to what is actually shown in the paper. A lot of important controls and analysis experiments are missing to back up the claims. While I think that the general idea has potential, it needs a much better investigation to be considered for acceptance. A list of actionable points is given below.

For full transparency, while I would be happy to increase the score if my points are addressed, I doubt this is doable within the rebuttal period. Depending on the other reviews, I would already suggest that the authors consider a full revision of the paper and submission of their paper to the next conference. That being said, I think this could become a very nice paper if more work is spent on the experiments, and I would be happy to iterated with the authors during the discussion period.

**Major**

**W1** There is a very lengthy introduction. The method section only starts on page 5. Before, a fair amount of related work is cited (great), but without considering any of that later as methods for comparisons.

**W2** A naiive baseline is omitted: What happens if a state-of-the-art adaptation technique like EATA, or even older/simpler techniques like TENT are used, but adapting $n$ models in parallel, and then ensembling of the outputs?

**W3** Section 3 needs a rewrite and improvements to clarity. For example, basic metrics like the cross-entropy loss are abbreviated with an extra symbol $\delta$, it would be better to clearly define the loss formulation used instead.

**W4** The contributions reference “continual learning” (l. 130, l. 134), but there is no experiment backing this up. The reference should be removed.

**W5** Claim 3 in the contributions (ll. 135-136) states that TTA requires a full batch. This is misleading or even wrong. There are certainly techniques that measure improvements when only a single sample is available (= model is adapted on that sample, and performance is measured) before the domain changes (e.g. Batch norm adaptation, or MEMO). However, in the setting considered here, model updates still accumulate on the same domain. In that setting, any TTA technique, like TENT, can be made suitable for the discussed setting by only updating every N steps (where N is the batch size), collecting the samples in the meantime.

**W6** Claim 4 in the contributions is not at all corroborated by results in the paper and should be dropped.

**W7** The paper needs to add recent methods to compare to. The current tables provide a lot of irrelevant details, and should be compressed. Instead of listing all different domains, it would be better to run a sufficient number of baseline models on the considered datasets to contrast the results. When doing so, it could be interesting to investigate whether the ensembling mechanism proposed is *orthogonal* to other adaptation methods: E.g., if we consider the EATA loss function for ensembling, does this improve over EATA?

**W8** Analysis should be added: What happens if the number of models in the ensemble varies? How robust is this technique to common problem in cross-entropy based adaptation (model collapse) when training over long time intervals?

**W9** In case the authors decide to keep the continual learning claim: How does the model perform in the continual adaptation settings used in CoTTA or EATA, and how does the model perform on long-term adaptation on CCC (Press et al., 2023)?

**Minor**

- Related work in l. 178: Batch norm adaptation (Schneider et al., 2020) re-estimates batch norm statistics, and this was shown to also work on single samples. Test time training (Sun et al., 2019) also considers single samples. TENT, in contrast, *additionally* performs entropy minimisation akin to the cross-entropy loss discussed in the study.
- Figure 1 misses a legend. The color code could be adapted, and e.g. corruptions of the same type could get the same color with different marker colours. That would make the plot more interpretable than the current 15 random colours.

### Questions
Please see the weaknesses above that are directly actionable. No further Qs.

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The submission describes a method for adapting an ensemble of classifiers to a new data distribution using only unlabeled data. Specifically, the classifiers are trained sequentially soft pseudo-labels, which are the output of the model that has the highest predicted probability for the majority class across classifiers. Experiments are performed on standard datasets (CIFAR10, CIFAR100, ImageNet) with synthetic distribution shifts for an ensemble consisting of 5 pre-trained image classification models.

### Strengths
Strengths:
* the studied problem is realistic and relevant
* the propose method makes sense and is simple enough for practical use
* experiments show improved accuracy by the proposed test-time-adaptation

### Weaknesses
Unfortunately, the submission has a number of weaknesses.

* incomplete method

The method works iteratively but the submission does not provide a termination condition. This is a not minor issue, as the manuscript makes it sound: without a termination condition, the method cannot be run in practice, and because no labeled data is available at test time, standard techniques, such as checking for a drop of validation accuracy, cannot be applied, either.

* lack of clarity in contribution and scientific comparison to prior work

The submission almost exclusively showcases the proposed method itself, but it does not put the method into context and competition with prior or alternative techniques. This leaves the novelty and relevance of the contribution unclear. Specifically, for a publication at a scientific venue, I expect that the novel aspect of the proposed method is clearly described, contrasting it to ideas and techniques that already existed in previous works. The manuscript does not do a good enough job doing so. As related work it concentrates almost exclusively on recent papers from the application domain of test-time adaptation with deep networks. However, ensemble methods have been studied extensively in machine learning, e.g. [Alaydin, "Introduction to Machine Learning", 2014; Chapter 17], and self-training methods for learning from unlabeled data also have a long history, going back at least to [Fralick, "Learning to Recognize Patterns without a Teacher", 1965], and having emerged many times afters, e.g. in the context of semi-supervised  learning (e.g. Chapelle "Semi-Supervised Learning", 2006) and also test-time adaptation, e.g. [Royer et al, "Classifier adaptation at prediction time", 2015] . Even for adapting ensemble methods self-training was proposed before, e.g. [Ghosh et al, "Self Training with Ensemble of Teacher Models", 2021]. In light of extensive prior work, the manuscript should make clear what the technical novelty of the proposed method is.

* lack of baselines in experiments

The experiments evaluation presents results for the proposed method, but it does not contrast them against prior works. Consequently, the reader only learns that using proposed method often (but not always) works better than not doing test-time adaptation, but if the method is better than already existing methods for test-time-adaptation. It would also be important to see at least a comparison to obvious baselines, such simply self-training each network individually. For the specific choices made, e.g. using the majority vote prediction as target label but the softmax scores of the most confidence classifier, an ablation study would be needed if this is actually useful, or if maybe using hard labels or the ensemble average confidence would work equally well (or better).

* unsubstantiated claims

The manuscript contains factual claims, e.g. about design choices that are not self-evident but also not  substantiated with evidence. Some of these appear misleading and/or are not credible, see "Questions". The counterexample on page 4 seems to be a misunderstanding of prior work. Claims in the literature are not that diversity is *necessary* for a good ensemble. Indeed, as the submission states, an ensemble consisting of many copies of a perfect classifier are still perfect. But rather, diversity of prediction *mistakes* between models in an ensemble can provably beneficial accuracy. Without any errors, that notion is not defined. But if mistakes do occur, the variance of predictions is decreased if errors are negative correlated (e.g. (17.5) in [Alpaydin, 2014]).

* shortcomings in the experimental protocol

Several aspects about the experimental evaluation are unclear or misleading (see questions below).
- The reported accuracy value in Tables 1-3 are "highest accuracy improvements" over all epochs.
That means they are not unbiased estimates, but potentially overconfident.
- The description of ensemble elements is not clear from the text, it currently seems only provided in the Table headers.
- The specified regularization constant $\alpha=10e^{-11}$ (which should probably be $\alpha=10^{-11}$) is so small that no regularizing effect is mathematically possible even after hundreds of thousands of steps. I would expect $\alpha=0$ to work equally well.
- The exact variant of "ImageNet" dataset used is not clear. Best provide a source how the data was obtained and prepared.
- The results table lists differences in accuracy, but not absolute accuracy numbers, which would be useful to judge e.g. if the base classifiers are suitable for the task.
- It is not specified how the method's hyper-parameters were selected.
- Given the mixed positive and negative results, a test of significance should be performed if the reported results are not equally well explained by random chance (e.g. Wilcoxon signed rank).

Further comments:
- I found the analogies with human learning or research (for example the top of page 3) rather superficial, and I would recommend to remove those.
- The reference section should be corrected. Many papers are listed as arXiv or without publication venue, which actually have been published, e.g. [Arazo et al, IJCNN 2020], [Bucila etal, KDD 2006], ...

### Questions
* What are the key technical differences of the proposed method to simply applying gradient-based self-training to an ensemble classifier, one sample at a time? 

* What are the key technical differences to prior work on ensemble self-training, such at [Ghosh, 2021]?

* Please clarify these claims: 1) page 3: "we minimize the diversity of the ensemble [...] in a way that facilitates generalization of the source training domain to the new testing domain." What does "facilitates generalization" mean here? Just higher test accuracy? In what way is lower *diversity* of the ensemble an important factor for that? 2) In the conclusion: "member models are optimized and improved like in knowledge distillation and create an upward spiral effect". What do you mean by upward spiral effect? E.g. from Figure 3 it appears that model accuracy goes up and down over epochs. 

* How were the method's hyperparameters chosen, given that standard model selection is not possible in the test-time adaptation setting?

* Which variant/subset of ImageNet was used? Is the "test" data the actual "test" set or the "validation" part?

* The manuscript emphasizes a batchsize of 1, but multiple *epochs* are run on the adaptation data. Does this mean that your method must buffer all test data, or at least see it repeatedly, such that statistics can be collected? Wouldn't batch-based TTA techniques be also applicable then?

### Soundness
2

### Presentation
2

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
This work introduces a new method for Test-Time Adaptation (TTA), Intra-model Ensemble Learning (IEL), that optimizes multiple models for ensembled inference. In the IEL framework, the output of the model with the highest probability for the class that received the most votes is set as the pseudo-label, and all other models are optimized to output this pseudo-label via minimizing the cross-entropy. This process minimizes the diversity within the ensemble and aligns the outputs of the models to ensure mutual agreement. Experimental results show the effectiveness of the proposed framework.

### Strengths
1. This paper is well written and easy to follow along with their reasoning.
2. The idea of utilizing ensemble methods for TTA is simple, intuitive and easy to adapt.
3. Experiments were conducted on a single-sample setting, which is one of the challenging tasks in TTA.

### Weaknesses
1. There is insufficient justification for minimizing the ensemble diversity. Personally, I believe that as diversity increases, performance can be improved in general including TTA since the information is also increases. For example, in [1] which is also referenced in this manuscript, it was shown that increasing diversity can lead to a lower loss. Additionally, the counterexample of ensemble of models with 100% performance (Lines 161–166) is unrealistic and therefore inappropriate for supporting the claim. If there is a large distribution shift and the source-trained models perform poorly on target dataset, reducing diversity may actually have an adverse effect. In conclusion, it remains unclear how reducing ensemble diversity benefits TTA.

2. Due to multiple assumptions, the scope of application of this research is limited. The authors assume there are multiple source-trained models (Lines 230–232), but it is questionable whether this assumption is easily met in practice. Furthermore, the assumption of stationary distribution shifts (Line 265-266) raises concerns about whether IEL would be effective in other TTA scenarios such as online imbalanced label distribution shifts or mixed distribution shifts [2]. The lack of discussion regarding the computational overhead of maintaining and optimizing multiple models further limits the practical applicability of this approach.

3. The experiments conducted do not sufficiently demonstrate the effectiveness of IEL. For example, the authors should include 1) performance comparisons with various previous works on TTA, 2) ablation study on the number of ensemble models, and 3) comparisons of computational costs associated with using multiple models. As mentioned earlier, including experiments across diverse TTA scenarios would also provide a more comprehensive understanding of IEL’s effectiveness.

### Questions
1. Is there any theoretical or empirical evidence that a minimizing the diversity of the ensemble is beneficial for TTA? 

2. In Figure 2, it shows that predictions with lower IEL loss have lower entropy. However, previous study [3], also cited in the paper (Lines 101–105, 173–176), claimed that reducing entropy of output during training can be problematic for TTA. This raises doubts about whether lower IEL loss actually leads to higher TTA performance, and I am curious whether there is any evidence to verify the relationship between IEL and TTA performance. 

3. Are there any experimental results that address the weaknesses mentioned (e.g., comparisons with previous studies, ablation study on the number of models, computational cost comparisons, and performance comparisons across various TTA scenarios)? 

4. If there are multiple source-trained models, what advantages does IEL offer over an approach that applies conventional TTA methods to each model individually and then performs an ensemble?

[3] Entropy is not enough for test-time adaptation: From the perspective of disentangled factors

### Soundness
1

### Presentation
2

### Contribution
2
