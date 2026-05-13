# Unified Uncertainty Estimation

- Decision: Reject
- Scores: 5, 3, 5, 8

## Abstract
In order to build robust, fair, and safe AI systems, we would like our classifiers to recognize and say “I don’t know” when facing test examples that do not belong to any of the in-domain classes observed during training. Perhaps surprisingly, the ubiquitous strategy to predict under uncertainty is the simplistic reject-or-classify rule: abstain from prediction if epistemic uncertainty is high, classify otherwise. We argue that this recipe has several problems: it does not allow different sources of uncertainty to communicate with each other, produces miscalibrated predictions, and it does not allow to correct for misspecifications in our uncertainty estimates. To address these issues, we introduce unified uncertainty calibration (U2C), a framework for the unified, non-linear calibration of aleatoric and epistemic uncertainties. Unified uncertainty calibration enables a clean analysis of uncertainty estimation via learning theory, and significantly outperforms reject-or-classify across a variety of standard benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new way of combining uncertainties. Given a calibrated network f_\tau and an epistemic uncertainty estimator u, instead of doing reject-or-classify, the paper suggests to do the following: (1) use a new validation set {x_i, y_i} and relabel 5% of its data---that has the worst uncertainty scores u(x_i)---with a new label c+1 to obtain {x_i, y_i'}; (2) train a calibration function \tau_u that serves as the logit for the class c+1 using cross entropy loss between (f_\tau(x_i), \tau_u(x_i)) and one-hot(y_i'). Empirically, with different ucertainty estimators u, the proposed approach was able to improve the performance of the model in a couple of settings.


---- After Rebuttal ------
While there are some merits in the proposed unifying framework for uncertainty estimation and the authors have tried to address some of my questions, I discussed with other reviewers and shared similar concerns as them, hence I am adjusting my score accordingly.

### Strengths
The paper is very well written, with a clear overview of the field and an explanation of why reject-or-classify is not ideal. The proposed approach is simple (in a good sense) and well-motivated. The simplicity makes it applicable to all classification settings. The experimental results show the efficacy of the methods in a variety of settings.

### Weaknesses
The paper doesn't have major weaknesses to me, though I do have a couple of questions for the authors to answer listed below.

- Does \tau^u need to be calibrated in some sense? For example, is it possible that adding \tau^u as the logits for class c+1 will mess up with the calibrated logits for the classes 1~c?
- The choice of u and f_\tau. Does the approach have some requirement on u? For example, given a very "u", the data chosen to be labeled as c+1 can be wildly wrong. Is there a way to choose u itself? If so, can it be integrated into this unified approach? 
- Should \tau^u(u(x)) in Eq.8 be \tau_u(x)? Or maybe the objective (7) should be changed to \tau_u(u(x_i^va))?

### Questions
- Does \tau^u need to be calibrated in some sense? For example, is it possible that adding \tau^u as the logits for class c+1 will mess up with the calibrated logits for the classes 1~c?
- The choice of u and f_\tau. Does the approach have some requirement on u? For example, given a very "u", the data chosen to be labeled as c+1 can be wildly wrong. Is there a way to choose u itself? If so, can it be integrated into this unified approach? 
- Should \tau^u(u(x)) in Eq.8 be \tau_u(x)? Or maybe the objective (7) should be changed to \tau_u(u(x_i^va))?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A method is proposed to produce scores over the classes in a multiclass classification problem, as well as a score indicating that the sample is out-of-distribution. These scores sum to one. It is claimed that they are well-calibrated in-sample and have good out-of-sample detection error. It is suggested that in-sample calibration quantifies aleatoric uncertainty, and out-of-sample detection quantifies epistemic uncertainty.

### Strengths
The problem of separating aleatoric and epistemic uncertainty is interesting. The proposed method attacks one aspect of the aleatoric-epistemic uncertainty problem by considering the calibration and out-of-sample detection problem in multiclass classification jointly.

### Weaknesses
A lot of the paper has a philosophical feeling to it, involving comments on etymology, sources of randomness, and vague correct-sounding statements that are presented without citation. Sometimes, these statements are patently incorrect. Examples follow:
- Eq. (2) is an incorrect definition of ECE. ECE does not have an inner expectation over p \sim [0,1]. It is also strange (although technically correct) to write the outer expectation over (x, y) \sim P -- the outer expectation is only over x \sim P_X. Please see one of the references you have cited for the right measure-theoretic definition.
- The first sentence of page 4 is, "In practice, a classifier models aleatoric uncertainty if it is well calibrated (Guo et al., 2017; Wang et al., 2021), namely it satisfies \pi_f (x) ≈ P(Y = y | X = x) for all examples (x, y)."
Neither of the papers claim that calibration models aleatoric uncertainty, or that the learnt \pi_f is close to the true regression function, so this is an unsubstantiated opinion of the authors. Also, it is impossible to learn the true regression function, and none of these methods do it (or claim to). 
- Section 3.1: "In machine learning research, aleatoric uncertainty arises due to irreducible sources of randomness in the process of labeling data." This is a strange statement that also falsely implies that all source of aleatoric uncertainty is annotator noise. 
- Section 3.2: "Epistemic uncertainty is an unsupervised quantity, and as such it is more challenging to estimate than its supervised counterpart, aleatoric uncertainty." (no citation is provided)

Some other writing issues: 
- The function u(x), central to the method of the paper, is mentioned inline as part of examples which were listed only for the sake of completeness (in the authors' words). 
- There are two lemmas but no theorem. 
- Changing notation: from \tau_u to \tau^u
- What is an example of a "non-linear" \tilde{\tau}_u in eq. (7)? This is so central to the method that it should be transparent at first reading. 

The theoretical results are not noteworthy, and are better presented as an illustrative synthetic example involving some computation. Lemma 5.1 is a decomposition of errors. Lemma 5.2 verifies that RC does not do well on the given example. 

I had some issues understanding the method, but I believe it essentially boils down to relabeling some percentage of the validation dataset as out-of-sample, then learning some model to predict those out-of-sample points. Then a softmax is applied in the end to make sure things sum to one. The method makes sense but I feel lacks the level of novelty expected from ICLR.

### Questions
- Eq. (4): Why is this a good way to separate aleatoric and epistemic uncertainty? Is there a specific paper that has justified the use of these? 
- What is the purpose of including etymological remarks when introducing aleatoric and epistemic uncertainty? 
- What is the "non-linear" \tilde{\tau}_u in eq. (7)?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of uncertainty calibration in neural network classifiers. Specifically, it looks at combining aleatoric uncertainty and epistemic uncertainty. Current methods use a simple "reject-or-classify" rule to abstain from prediction when epistemic uncertainty is high. However, this approach has issues - the two uncertainties don't communicate, predictions are miscalibrated, and epistemic estimates may be misspecified.
The proposed Unified Uncertainty Calibration (U2C) framework allows both kinds of uncertainties to communicate with each other, resulting in well-calibrated probabilistic predictions. The key ideas are: relabeling the 5% most uncertain validation data as OOD. Blend aleatoric and epistemic uncertainties into an extended (c+1 class) softmax vector. Learn a non-linear calibration function of the epistemic uncertainty by minimizing the cross-entropy on the relabeled validation set. This allows the two uncertainties to communicate and produce well-calibrated probabilistic predictions.

### Strengths
1.	The paper introduces a novel uncertainty calibration technique (U2C) that intelligently combines aleatoric and epistemic uncertainty to improve classifier robustness. Both theoretical and empirical results demonstrate the efficacy of the proposed approach.

2.	The theoretical analysis provides useful insights into the behavior of U2C compared to the commonly used reject-or-classify recipe. 

3.	The extensive experiments on ImageNet benchmarks demonstrate clear improvements from using U2C over reject-or-classify. The consistent gains across different network architectures, uncertainty estimators, and data distributions validate the efficacy of the proposed approach.

### Weaknesses
1. In section 5, the statement "In contrast, if P_in has a lot of mass in C but little in B, then RC outperforms U2C in terms of hard predictions" appears to be incorrect. Based on Figure 1 and lemma 5, it seems that if \$P_{in}\$ has more mass in C but little in B, then U2C should outperform RC. This discrepancy needs clarification.

2. The description of the proposed U2C framework is quite condensed. An algorithm, presented as pseudocode, would significantly improve clarity and facilitate a more thorough understanding of the implementation steps, including the relabeling process, blending of uncertainties, and the learning of the non-linear calibration function.

3. There are some notational inconsistencies that should be addressed. For example, \$\tau^u\$ in Eq. 8 does not coincide with \$\tau_u\$ used in the preceding text. Ensuring consistent notation throughout the paper is crucial for clarity.

4. The paper lacks a comprehensive comparison with prior works that also explore the unified modeling of aleatoric and epistemic uncertainty. For instance, the work by Malinin and Gales [1] utilizes a Dirichlet distribution to model both types of uncertainty uniformly. A detailed discussion contrasting U2C with such approaches, especially regarding the trade-offs between retraining requirements and computational overhead, would strengthen the paper's contribution.

5. The rationale for discarding 5% of the validation set data of IID and treating it as OOD data is not entirely convincing. While these data points may exhibit high epistemic uncertainty, they fundamentally remain IID. A more detailed justification for this approach, perhaps with a discussion on the characteristics that make these points "look most like OOD," would be beneficial.

### Questions
Please refer to weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a U2C framework to combine aleatoric and epistemic uncertainties in OOD classification problems. The benchmark method, reject-or-classify (RC), abstains from prediction if the epistemic uncertainty is high, and otherwise produces an in-domain prediction. The RC method follows a "hard" way to classify a sample into the out-domain class, while the proposed U2C method takes a softer approach by concatenating an epistemic uncertainty score to the logit vector of a pre-trained predictor, before passing the augmented vector to a softmax layer. The problem does not assume the accessibility of out-domain data, so the U2C method picks the most epistemically uncertain data from the training set and then replaces their original labels with a new out-domain label.

### Strengths
1. The idea is very natural and intuitive. The separation of epistemic uncertainty and aleatoric scores in the RC method inevitably induces various inconveniences, as discussed in the introduction, and the U2C framework is a natural attempt to construct "epistemic scores" that are comparable to aleatoric scores.

2. The U2C framework identifies a new problem formulation for uncertainty calibration, and I think one contribution of the work is to formulate this "calibration" task under the OOD setting. 

3. The algorithm benefits from a good epistemic uncertainty estimator and a high-performance calibrating algorithm, making it adaptive and flexible.

### Weaknesses
1. The U2C algorithm's reliance on treating the most epistemically uncertain samples in the training set as OOD samples raises concerns. This approach hinges on the assumption that OOD samples will exhibit comparable epistemic uncertainty to these extreme in-domain samples. However, this assumption may not hold universally. Consider a scenario where the epistemic uncertainty estimator fails to adequately capture the uncertainty associated with OOD samples. For instance, in a binary classification task of dogs versus cats, if a mouse image (OOD) is presented, the model might still produce a high confidence prediction, say (0.8, 0.2), misclassifying the mouse as a dog. In such cases, the epistemic uncertainty would be low despite the input being OOD, thus undermining the core premise of U2C. The performance of U2C is therefore intimately tied to the effectiveness of the chosen epistemic uncertainty estimator, and further investigation into the robustness of this relationship is needed.

2. The theoretical analysis, particularly Lemma 5.2, presents a somewhat simplified critique of the RC method. While it's true that the losses can theoretically approach infinity, practical implementations often employ truncation or capping mechanisms to prevent such extreme values. A more nuanced discussion acknowledging these practical considerations would strengthen the theoretical foundation and provide a more accurate comparison between RC and U2C.

Minor comments:

1. The statement "Roughly speaking, neural networks with small ece produce calibrated confidence scores, meaning XXX" is inaccurate. Formula (2), which defines ECE, represents a "marginal" or "global" measure of calibration. The XXX formula, on the other hand, describes an "individual" or "conditional" calibration criterion. A low ECE does not necessarily guarantee individual calibration. This distinction is crucial and should be clarified to avoid misleading interpretations.

2. Regarding the numerical experiments, it is unclear whether the models are pre-trained or trained from scratch. Providing details about the training procedure would enhance the reproducibility and clarity of the experimental setup.

### Questions
As above in the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
