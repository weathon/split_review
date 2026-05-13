# DAME: A Distillation Based Approach For Model-agnostic Local Explainability

- Decision: Reject
- Scores: 6, 8, 6, 5

## Abstract
The frameworks for explaining the functional space learned by deep neural networks, also known as eXplainable AI (XAI) models, are majorly based on the notion of the locality. Most of the approaches for local model-agnostic explainability employ linear models. Driven by the fact that a linear model is inherently interpretable (linear coefficients being the explanation), they are used to approximate the non-linear function locally. In this paper, we argue that local linear approximation is inapt as the black boxes under investigation are often highly non linear. We present a novel perturbation-based approach for local explainability, called the Distillation Approach for Model-agnostic Explainability (DAME). It separates out the two tasks- local approximation and generating explanation, and successfully attempts generating explanations by operating on high dimensional input space. The DAME framework is a learnable, saliency-based explainability model, which is post-hoc, model-agnostic, and requires only query access to the black box. Extensive evaluations including quantitative, qualitative and subjective measures, presented on diverse object and sound classification tasks, demonstrate that the DAME approach provides improved explanation compared to other XAI methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes Distillation Approach for Model-agnostic Explainability (DAME), an approach which fits a non-linear model is fit in the vicinity of an input sample to to explained. The model is fit to obtain a saliency map explanation based on a teacher-student distillation approach which uses a combination of 3 loss functions. The proposed method is comprehensively evaluated on image and audio datasets using a number of evaluation techniques and shows improvement over existing local explainability methods.

### Strengths
Overall when the decision boundary is wiggly and inputs are high dimentsional, sparse linear models may not mimic the source model's behaviour around a sample and it makes sense to use a non-linear approach which might provide a better approximation. The approach proposed to generate the local saliency explanation is novel. The evaluation is quite comprehensive including fidelity-based, subjective and qualitative evaluations and comparison with 9 XAI methods.

### Weaknesses
Based on the 3 loss functions that need to be handled, it seems likely that the method may not work out of the box (like LIME) and users will probably need to customize/tune hyper-parameters etc. to get the explanations right.

### Questions
- How is local vicinity and distance between the given sample and perturbations defined in DAME - is this same as LIME?
- In case of DAME, can the authors comment on local invariance of explanations (do similar inputs yield similar explanations)?
- Would DAME be impacted by correlated featured?
- Instead of using a masking approach to generate perturbations (e.g. LIME), if we have a realistic distribution of perturbed images (e.g. MeLIME), can the DAME pipeline still be used?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a framework for generating a learnable saliency-based explanations model, which is model-agnostic and requires only black box query access to the model. The framework consists of two models: a mask-generation module that generates the saliency maps and a student network to distill the black-box model's predictions by approximating the black-box model's local behavior near the input sample. The parameters of these two networks are learned by generating perturbations in the neighborhood of a given sample.

### Strengths
- The paper addresses an important question on generating saliency map-based explanations with only black-box
access to a model.
- Besides traditional tasks from Computer Vision, the paper also reports results on audio processing tasks.
-  The paper is well-written and easy to follow.

### Weaknesses
One of the critical issues with the paper is how they evaluate & the choice of baselines. Even though they consider a
diverse set of tasks, the authors must add additional experiments to strengthen the paper.

It is hard to see whether the proposed framework offers a clear advantage over the baselines (as explanations are typically subjective).

It would also be essential to understand how architectural changes affect the results.

- Does the architecture of the map generation & student network affect the performance? Does it need to be shallow
or deeper? What are the design considerations for these networks?
- How does the proposed method compare to, say, just distilling a smaller model from the black-box model & then
using the distilled network to generate saliency maps (and use these as explanations for the black-box model?)? This should be a baseline.
- What's the need for a map-generation network in the framework? Can't we distill the black-box model through a
student network exposed to the perturbations?
- The authors should add the above two setups as baselines.

### Questions
The proposed framework incurs an additional computation cost but performs worse than a simpler technique like RISE, and the improvement seems marginal.

How important are the perturbations? The mask-generation network seems to be trainable without the perturbations of inputs. It would be better to investigate the impact of the number of perturbations on explanation performance to evaluate the effectiveness of the perturbations.

I also encourage the authors to consider benchmarks like CUB & AwA2 (and other benchmarks where concepts are annotated), which contain annotations of salient parts of the image; this helps them compare against some gold standards

Refer to Weaknesses for additional questions.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a model-agnostic, gradient-free, saliency-based method to understand local behavior of black-box models. They establish the shortcomings of previous works like LIME that use a locally linear model to approximate the behavior of a neural network in a given sample’s neighborhood. They use ideas from the MLX (Machine Learning from Explanations) area and propose to address this via distilling the black-box model into a smaller student model only in the sample’s neighborhood. Concretely, they generate perturbations of a sample and then learn saliency masks (explanations) such that a perturbed sample masked by the saliency when passed through the student model has the same target class softmax score as the teacher. These two models, the one that learns the masks and the student that distills the black-box in a sample’s neighborhood, are chained and trained together using a distillation+explanation loss (with 2 more loss terms to avoid identity learning and preserve class distributions between student and teacher). They share results of their approach on 2 vision datasets and 2 audio datasets.

### Strengths
1.	This method works in input space and not in the binary mask space like LIME does
2.	The paper establishes the shortcoming of locally linear approximations with a small toy experiment.
3.	They share results from many varied experiments with both quantitative metrics and qualitative samples. To quantify the quality of their explanations, they compute IoU with human annotations for samples that are classified correctly by the model – since that is the class that human annotations would be explaining.
4.	It is an intuitive approach. The paper is well written and easy to follow
5.	They compare with LIME, RISE, GRADCam and other gradient based methods from Integrated Gradients family.
6.	The appendix is very thorough and quite informative

### Weaknesses
1.	The biggest bottleneck to using this approach would be having to train a whole new model to understand the behavior of the model for one single input sample.
2.	Results from RISE are often quite competitive in tables 1 and 2. Smooth Grad is also quite competitive.
3.	This approach is akin to a gradient-based approach in the guise of gradient-free. If one was to distill the whole black-box into another model (not just in the sample’s neighborhood) and then apply any gradient-based method, I believe that that would be much simpler since one won’t have to train a smaller model to get an explanation for each sample and I believe it would perform competitively seeing the numbers in tables 1 and 2. So, I have doubts about why the authors have taken this round-about route. It is at least worth it to compare this with works that use distillation to understand models.
4.	I might have missed something here but the audio experiment results don’t seem too convincing:
a.	In task 2, padding noise on two sides is an easy noise pattern to learn/catch. 
b.	In task 3, cough data says that it was manually annotated. Are there going to be any plans to release this to enable discussion/reproducibility?
5.	Some language in the paper such as “mildly vs strongly non-linear” is non-standard. This is a small nitpick.

### Questions
1.	Have the authors considered using this method on well-known spurious feature detection image datasets like Decoy-MNIST and ISIC?
2.	If one was to distill the whole black-box into another model (not just in the sample’s neighborhood) and then apply any gradient-based method, I believe that that would be much simpler since one won’t have to train a smaller model to get an explanation for each sample and I believe it would perform competitively seeing the numbers in tables 1 and 2. So, I have doubts about why the authors have taken this round-about route. It is at least worth it to compare this with works that use distillation to understand models. I would like to get the authors thoughts on these points.
3.	Can the authors clarify if I have incorrectly interpreted the audio experiments setup or results? Are there going to be any plans to release manually annotated cough data to enable discussion/reproducibility?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Explaining a deep neural network decision on a data point by using linear models as approximators in the locality of the data point has become a common practice. This paper argues that local linear approximation is inapt as the black boxes under investigation are often highly nonlinear. They propose a novel local attribution methods Distillation Approach for Model-agnostic Explainability (DAME) which does not use a linear model as local approximator. The method consist of training a student network to copy the prediction of the original DNN on the perturbated version of the data point along with a Mask-generator network that masks those perturbated samples. After training, this Mask-generator will be used to generate an explanation for the original DNN. DAME is evaluated on computer vision datasets using (a) IoU between the explanation and human annotation, (b) human subjective rating of the quality of the explanation, and (c) the drop in accuracy of the original DNN when the important pixels are removed. They also evaluate it using an audio dataset and a medical dataset, on which both use an IoU metric.

### Strengths
- The paper is clear and the work is well contextualized regarding prior works (although it could refer to more recent perturbation-based attribution methods).
- Using distillation methods for explaining a model is an interesting idea

### Weaknesses
 - The paper is clear and the work is well contextualized regarding prior works (although it could refer to more recent perturbation-based attribution methods).
- Using distillation methods for explaining a model is an interesting idea

 - The main weakness of this paper is in the evaluation. 
	- It is because we do not know the reasoning behind DNN decisions --i.e. we do not what a good explanation of its decision is-- that we carefully develop methods for that purpose. In that sense, a subjective human evaluation of the quality of the explanation (b) is not actually informative of the quality of the explanation
	- The decisions of a DNN do not necessarily rely on the same features humans rely on (the opposite has previously been shown [1-2]). Hence an explanation that accurately depicts that the DNN does not use human-like features will be wrongly penalized by IoU metrics (a)
	- On the other hand, a standard way to evaluate attribution methods is using fidelity measure, Deletion and Insertion --introduced in RISE-- being the most widely used ones, which the paper does to compare DAME with RISE and LIME (it is not exactly clear if pixels are progressively removed as in Deletion or if all important pixels are removed at once). If Deletion is indeed used, the results of the 2 baseline are slightly surprising as RISE has been shown consistently to be better than LIME in previous work [3-4], which is not the case here.
- Also, the motivation of the paper comes from the claim that linear models are inapt to accurately approximate non-linear models locally. An instantiation of the proposed framework with linear models is missing to make the claim more concrete.

### Questions
- I was wondering if the authors have thought about running standard attribution methods on the original and student models as a sanity check that they do seem to have similar decisions for similar reasons?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
