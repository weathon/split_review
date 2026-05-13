# Next state prediction gives rise to entangled, yet compositional representations of objects

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
Compositional representations are thought to enable humans to generalize across combinatorially vast state spaces. Models with learnable object slots, which encode information about objects in separate latent codes, have shown promise for this type of generalization but rely on strong architectural priors. Models with distributed representations, on the other hand, use overlapping, potentially entangled neural codes, and their ability to support compositional generalization remains underexplored. In this paper we examine whether distributed models can develop linearly separable representations of objects, like slotted models, through unsupervised training on videos of object interactions. We show that, surprisingly, models with distributed representations often match or outperform models with object slots in downstream prediction tasks. Furthermore, we find that linearly separable object representations can emerge without object-centric priors, with auxiliary objectives like next-state prediction playing a key role. Finally, we observe that distributed models' object representations are never fully disentangled, even if they are linearly separable: Multiple objects can be encoded through partially overlapping neural populations while still being highly separable with a linear classifier. We hypothesize that maintaining partially shared codes enables distributed models to better compress object dynamics, potentially enhancing generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies object disentanglement in the representation of visual scenes. Specifically, object-centric representations enforce an inductive bias for disentangling representation of different objects.  The claims that (1) distributed representations (not object disentangled) may outperform object-centric  ones in down-stream tasks; (2) Limited object disentanglement (linear separability)  may arise even without forcing it through the architecture.

The paper compares the representations learning in structured and non-structured representations and analyzes their linear separability.

### Strengths
-- Studying inductive biases for neural architecture is interesting. 
Its great to see a paper that is about more than just improving a few points on a known task. 

-- Interesting experiments.

### Weaknesses
W1. There is a lot of work on compositional representations in machine vision. 
From early papers focused on compositionality of attributes 
 [Yuval Atzmon et al 2016, Justin Jhonson 2017]. 

W2. The main higlighted claim is that, ith sufficient data, models can learn representation that disentangle objects. 
I am missing an argument that explains why that is surprising or unsexepected. Does theory sugests otherwise? 
In attribute compositionality, it was argued that discriminative models entangle peoperties that are correlated intheir trainin data, 
and cannot generalize to new combinations. But here, objects are not entangked dugin training. So why would disentaglement be a problem? 

W3. The paper measures linear separability. This is a different concept that compositionality, and the paper should make the distinction super clear and explicit, already in the title.  In the ML literature, compositionality usually means that one can represent new things using combination of concepts. 

W4. In high enough dimensions, it is easy to get linear separability, depending on the number of classes.

### Questions
Q1. What specific properties of the architecture or training procedure lead to linear separability effect?

Q2: How general are the results in the paper? Would they generalize to other object-centric approaches beside CWM / CSWM?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work performs a study comparing the learned representation spaces of unsupervised object-centric slot-based models and their unstructured counterparts trained on various datasets of dynamically interacting objects. The study focuses on the disentanglement of these representations in terms of objects and their capacity to capture underlying transformations that act on objects, regardless of their identity. The experiments include models trained on both reconstruction-based and contrastive objectives and test the learned representation’s efficacy in image reconstruction as well as multi-step dynamics prediction. Object separability is measured using a novel metric based on the ability of a linear classifier to recognize which object changed between two consecutive frame representations. Based on their experiments and analysis, the authors suggest that explicit object-level factorization is not necessary for learning these tasks and achieving compositional generalization, more so when the training objective includes next-state prediction. This is explained by the fact that the learned representations, although not object-centric, converge to being partially disentangled in terms of objects (as quantified by the object separability metric) while maintaining a level of entanglement that facilitates sharing of information about transformations that act on objects.

### Strengths
Summarized points:
- Well written paper
- Perform an interesting and seemingly novel study
- Revisits and challenges an important basic assumption that incorporating explicit object-centric structure in representation-learning models is beneficial/necessary for representing object-centric scenes/dynamics

### Weaknesses
Summarized points:
- Some conclusions are not convincingly backed-up by experiments
- There is room for more systematic fine-grained evaluation of performance with respect to different types of compositional generalization
- The implications of this study to downstream task performance, a major use-case/motivation for unsupervised representation-learning, are not assessed in experiments and mostly not discussed

**Related Work**

The overview of object-centric representations is focused entirely on slot-based models. Although these might be the most dominant in the literature, I believe this section can benefit from including additional types such as patch-based (e.g. [SPACE](https://arxiv.org/abs/2001.02407), [MarioNette](https://arxiv.org/abs/2104.14553)) and keypoint-based (e.g. [Jakab et al.](https://arxiv.org/abs/1806.07823), [DLP](https://arxiv.org/abs/2205.15821)).

**Experiments - Model Forward Prediction Ability**

*Prediction Accuracy*: The evaluation metric described in the second paragraph of the Experiment Section is not clear to me. What does it mean for the prediction to be “closest to the last frame”, closest compared to what?

In the case of the object-centric dynamics model, how do you compute the distance between two latent representations that are not from the same trajectory (e.g. contrastive examples or encoded ground-truth future states)? The latents are sets of vectors and thus lack ordering such that a simple L2 loss would not necessarily compute distances between aligned slots.

I find it surprising that CWM outperforms CSWM in object dynamics prediction. The original CSWM paper seems to have results on the cubes dataset that contradict your results (see Table 1 -> 3D Blocks -> 10 Steps -> CSWM vs. -factored states). Do you have an explanation for this discrepancy? Is there an essential difference in the setting or metrics they used compared to yours? 

Another question that arises here is why did you choose to compare the prediction abilities in latent space? The latent spaces are not as comparable as reconstructions of images in my opinion since they possess different structure. I suggest training a “stop-gradient decoder” on reconstructing the contrastive latents so you can obtain image reconstructions without affecting the contrastive model’s optimization process. You can then use perceptual metrics to quantify prediction performance (e.g. LPIPS, which you used in the autoencoder study).

Why do the authors not study object dynamics prediction with the autoencoder models in addition to the contrastive models in section 4.1? This study could potentially strengthen your conclusions. In any case, I believe it should be part of your experiments.

**Experiments - Reconstruction Quality**

Figure 5 presents similarity metrics using LPIPS. For better qualitative assessment I would suggest adding additional metrics such as pixelwise MSE, SSIM, FID.

“the auto-encoder performs better than the sequential auto-encoder on the test set, despite attaining substantially lower object separability scores” - Is it possible that this is due to the fact that the auto-encoder was trained on that task precisely while the sequential auto-encoder was trained on next-frame prediction? The distribution of latent representations produced by the latent dynamics model is most likely different from latent representations directly encoded from images.

**Experiments - Compositional Generalization**

Can the authors clarify why high accuracy in the dynamics prediction tasks suggests compositional generalization capabilities? Is there a systematic separation between the train and test data in terms of compositions of objects and/or their properties such that performing well on the test data would necessarily require compositional generalization?
Put more simply: can you say for certain or with high probability that the test data does in fact contain novel constellations and combinations of objects?
If so, I request that the authors add details about the train-test split with respect to the relevant factors of variation in each dataset. 

The above questions are also relevant to the reconstruction experiments.

**Discussion**

As I see it, the two major claims about non-object-centric unsupervised representation learning models are:
- They can learn representations with some form of disentanglement between objects (as quantified by the proposed separability score)
- The learned representation space captures some notion of underlying transformations that act on objects, regardless of their identity

I believe the results that show that the object-separability score does not translate to improved task performance when comparing the static autoencoder with the dynamic one is indicative of a broader question that should be asked, discussed and maybe answered in the context of this work: *What are the implications of the two major findings in the paper?*

*I find this question not sufficiently answered*. I suggest looking into two main aspects:

1. *Downstream Task Performance*: Questions that should be answered in my opinion:
- Are the two qualities of the learned representation indicative of downstream task performance?
- Are they efficiently leverageable by downstream models?

I would argue that in this study, downstream task performance was not assessed. Both dynamics prediction and image reconstruction are exactly what the respective models were trained on.
Downstream tasks in the actionable environments could be sequential decision-making while on the uncontrollable dynamics, one could infer underlying properties of the scene or trajectory such as the number of objects that remain in the scene by the end of the trajectory in the MOVi-A dataset.

2. *Compositional Generalization*: the models’ ability to generalize its representations to scenes with novel compositions of objects as well as novel compositions of objects and the transformations that are applied to them.

Here I argue that this type of generalization was not systematically assessed.

In order to do so, I suggest first defining the factors of variation of interest.
Some examples:
- Number of objects in the scene
- Combinations of individual object static properties such as color, shape, size, mass, friction (most relevant to the MOVi-A dataset)
- Dynamic transformations in static object properties (most relevant to Multi-dSprites)

Based on these factors one should create a train-test split such that performance of the same task on the test data would be indicative of the model’s representation’s capacity to facilitate compositional generalization of that type.
Examples of train-test splits:
- Train includes up to x objects -> Test includes between x and x+y objects
- Train includes only red cylinders and blue cubes -> Test includes blue cylinders and red cubes
- Train includes sequences where all but circular objects dynamically change scale -> Test includes sequences where circular objects do change scale

### Questions
For major questions and requests, see weaknesses.

Additional minor questions/requests:
- What are the actions that can be taken in the cubes and Multi-dSprites environments?
- Figure 6A: could the authors add labels of the objects/actions to the similarity matrices? It would be easier to interpret them knowing this information.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the quality and content of the latent representation of different models trained using unsupervised learning on dynamic scenes composed of multiple objects. The authors compare slot-based models against distributed models and investigate their ability to encode object identity and object dynamics (movement in the scene). They find that distributed models have a better ability to encode identity *and* movement than slot-based models.
They also show that the models trained with more specific losses, such as contrastive loss and next-state prediction, help to improve the quality of these representations through linear readout.

### Strengths
- The paper is overall clearly written and well presented. 

- The question tackled by the authors is very interesting and has not been extensively investigated in the past. 

- The method proposed to investigate the content of the latent representation by systematically controlling which object moves from one frame to the other and the nature of the movement is a very elegant way to test the information encoded in the latent representation. 

- The authors propose various ways to evaluate the content of the representations with different metrics, simple yet elegant and informative.

- The number of datasets and their variety in content and difficulty solidifies the authors' conclusions.

### Weaknesses
The results part should be improved. Each experiment compares only two models (either in terms of objective or model type -- slot-based vs. distributed), but we miss a big picture comparing the baseline (the CSWM) with all the models with their characteristics (contrastive, next-state prediction, ...). 
It would be easier to read and draw conclusions if all the models appeared on all the bar charts, clearly highlighting the benefit of each objective depending on the task, assuming that all the models are comparable in terms of number of parameters and architectural design. 
Maybe this could be done for one of the datasets, and the other results can appear in the appendix. 
It would also be informative to add in the Appendix the complete architecture of all the models, along with their number of parameters. 
I will be willing to increase my rating if this part is improved with a figure showcasing the totality of the results, for all models on all metrics, backing the claims of the authors.

### Questions
- For the dynamic loss (L_{AE-dynamic}), have the authors tried each term separately in addition to both combined? Does it change the conclusions for dynamic AE models?

- Instead of plotting the different metrics with respect to the number of training data, it would be interesting to do the same for various sizes of latent representation. Augmenting the capacity of this latent space will affect the information contained, making it more or less distributed -- and potentially showing different scores on the metrics. Have the authors tried this?

- Even though Fig. 6 seems to show that object identity is encoded in distributed models, is it possible to perform a linear to decode only object identity for the first or last frame of the videos? Slot models should be able to decode all the objects, but maybe the distributed models will only be able to decode the ones that are moving?

- In Fig. 2, the accuracy of both models increases with more data, but the gap seems to decrease. Is there a point with even more data where the CSWM is as good as the CWM?


- Fig. 7, why choose the CSWM as the baseline for the RSA if it's not the best model? It would be interesting to perform this analysis on all the models with respect to the CWM which seems to perform best on all the metrics, to see which component plays the biggest role in explaining the quality of the representations.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper explores how distributed representation models can develop compositional, linearly separable object representations without object-centric architectures/inductive biases. Through next-state prediction, the authors claim that these models match or exceed the performance of slot-based models in predicting object dynamics, even without dedicated object slots. The study finds that partially overlapping neural codes in distributed models enable effective generalization and object separability, making them a viable alternative for tasks involving dynamic object interactions.

### Strengths
The paper’s strengths lie in its idea of challenging the necessity of object slots, trying to show distributed models can effectively generalize with next-state prediction alone. It provides robust evidence across diverse datasets and offers new insights into how partial neural overlap supports transformation generalization, broadening representation learning approaches.

### Weaknesses
The paper exhibits several weaknesses in supporting its claims:

1. The claims about distributed models achieving compositional representations are not robustly supported by the experiments. The CSWM baseline, a model specifically optimized for the datasets used in their studies, underperforms on the new datasets used in this paper. This performance drop is predictable and weakens the validity of the comparisons. The core issue is that CSWM's architecture, which uses convolutional channels as 'slots', is fundamentally different from true slot-based models and not designed for generalization to diverse datasets. The contrastive loss used in CSWM is indeed a key contribution of that paper, but the ad-hoc slot implementation makes it a weak baseline for the claims made here about compositional representation learning.

2.  The study relies on Slot Attention, which is designed for static images, as a baseline in dynamic scenes. For a fair comparison in dynamic settings, it should have considered more relevant recent work, such as Parallelized Spatiotemporal Binding, which better aligns with the dynamical nature of the datasets. Slot Attention's primary focus is on disentangling static object representations, not on predicting object dynamics, making it an unsuitable benchmark for evaluating the dynamic prediction capabilities of the proposed model. The fact that it underperforms is not surprising given its design.

3. The claim that next-token or next-state prediction without specifically designed inductive biases can lead to a (somewhat) disentangled representation is not new. This phenomenon has been observed and documented in previous works, making the findings here less innovative. While the paper demonstrates this in an object-centric context, the core idea of using future prediction for representation learning is well-established. The novelty is therefore limited to the specific application rather than a fundamental breakthrough in representation learning.

### Questions
In Eq.6 , the t should be replaced by t+1?

### Soundness
1

### Presentation
3

### Contribution
2
