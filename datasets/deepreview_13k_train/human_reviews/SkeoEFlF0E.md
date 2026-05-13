# NEURAL ADDITIVE TENSOR DECOMPOSITION FOR SPARSE TENSORS

- Decision: Reject
- Scores: 8, 3, 5, 3

## Abstract
Canonical Polyadic Decomposition (CPD) is a fundamental technique for tensor analysis, discovering underlying multi-linear structures represented as rank-one tensors (components). The simplicity of the rank-one tensors facilitates the interpretation of hidden structures within tensors compared to other types of conventional tensor decomposition models. However, CPD has limitations in modeling nonlinear structures present in real-world tensors. Recent tensor decomposition models combined with neural networks have shown superior performance in tensor completion tasks compared to multi-linear tensor models. Nevertheless, one drawback of those nonlinear tensor models is the lack of interpretability since their black-box approaches entangle all interactions between latent components, unlike CPD, which handles the components individually as rank-one tensors.

To overcome this major limitation and bridge the gap between CPD and various state-of-the-art neural tensor models,
we propose Neural Additive Tensor Decomposition (NeAT) to accurately capture non-linear interactions in sparse tensors while respecting the separation of distinct components in a similar vein as CPD. The main idea is to neuralize each component to model non-linear interactions within each component separately. This not only captures non-linear interactions but also makes the decomposition results easy to interpret by being as close to the CPD model as possible. Extensive experiments with six large-scale real-world datasets demonstrate that \method{} is more accurate than the state-of-the-art neural tensor models and easy to interpret latent patterns.
In the link prediction task, 
NeAT outperforms CPD by 10\% and the second-best performing neural tensor model by 4\%, in terms of AUC score.
Finally, we demonstrate the interpretability of NeAT by visualizing and analyzing latent components from real data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article presents a new tensor decomposition method called Neural additive tensor decomposition (NEAT), which extends the standard CP Decomposition with non-linear functions. The method incorporates ideas from neural tensor models, and applies Multi-layer perceptrons (MLPs) to each rank-1 CP factors. The proposed method captures non-linear interactions and also helps in interpretability of results.  Numerical results are presented on different datasets to illustrate the performance of the proposed method in comparison to SoTA neural and other tensor decomposition methods.

### Strengths
Strengths:
1. The paper presents an interesting new tensor decomposition that captures non-linear interactions 
2. The decomposition appears to have an easily interpretable form, and this advantageous in many applications
3. The pair presents extensive numerical results, which show that the proposed outperforms other compared methods.

### Weaknesses
Weakness:
From a numerical computation perspective, 
1.  The computational cost of the method could be an issue for large tensors.
2. The decomposition is non-unique and the optimization problem looks difficult to solve for a good minima.

### Questions
The paper presents an interesting new tensor decomposition, which has several advantages and will likely be useful in a number of applications involving tensors. The paper is well written. Numerical experiments section is extensive and presents many different results illustrating the superior performance of the prosper method, and studies different aspects of the method. 

I have the following few minor questions:

1.  How is the optimization problem m in eq (8) computed? Is it just by ADAM or autograd?

2. Movielens seems to be a very easy datasets for neural methods. They all achieve very high accuracy. Is there a particular reason for this?

3. How is the downstream task performed (transductive and inductive) for CP and Tucker decompositions? These do not have parameters to train (and freeze). Are the factor matrices simply used as input features to the classifier?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a neural network model (NEAT) for sparse tensor decomposition. NEAT replaces the direct inner products of factors in CP decomposition with learnable MLPs. The authors showed NEAT outperformed CP and other neural network based tensor decomposition models in several real world tensor completion datasets and one downstream task. The authors showed the latern factors learned by NEAT can be used for interpretability.

### Strengths
The paper is clearly written and fairly easy to follow. The authors conduct thorough experiments to show the performance of the proposed model.

### Weaknesses
 * The contribution is somewhat limited. Rank-k CP decomposition is the sum of the outer products of k rank-1 factors. The proposed NEAT model uses learnable MLPs to replace the outer product. There have been many papers doing similar things, some of which are cited in this paper as well. It is unclear how the proposed NEAT model is different comparing with the existing neural network based models. From section 2, it seems the biggest advantage of NEAT is that there's no cross factor interaction, as NEAT is a direct extension of CP decomposition model.
* The analysis of the empirical evaluation is not strong enough to justify the contribution. The chosen datasets are not complicated enough to demonstrate that NEAT significantly outperforms baselines. The interpretability part is good to have but is not good enough to convince readers that the proposed model is outstanding on that part.

### Questions
* In section 2, the authors mentioned that "... neural network entangled associations of all components makes it difficult to identify the contribution, ...  the proposed method NEAT ... simplifying the discovery of non-linear latent patterns".  Could the authors please elaborate on this? Does it always hold that simple methods are better? What types of tensors would be better fit by complex models, and what types of tensors would be better fit by the proposed model or CP model?
* How many extra parameters are introduced by NEAT when comparing with CP when the factors CP rank are the same? Could it be the case that, for some sparse tensors, the total number of parameters of NEAT is more than the number of observed entries? In that case, how does NEAT do in terms of overfitting?
* Does the proposed model work for non-sparse tensors?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a neural tensor decomposition method called NEAT that captures nonlinear patterns in sparse tensors while maintaining interpretability. Aligned with classical CPD, NEAT decomposes a tensor into a sum of components, where each component is modeled by a separate MLP. This allows the expression of nonlinearities in an additive, separable way. NEAT is evaluated on link prediction for multiple real-world sparse tensors. NEAT also produces interpretable embeddings that allow the discovery of patterns in different components.

### Strengths
The proposed model shows a novel and reasonable way to combine the simple but interpretable CPD with the deep module. Besides state-of-the-art link prediction performance on multiple datasets, the design of the down-streaming task with finetuning is interesting. Also, the presentation is smooth and easy to follow.

### Weaknesses
 - Compared to prior deep tensor work, the main selling point of the work is the interpretability based on the component(rank)-wise modeling. The experiment part (section 4.4) also highlights it. However, as component-wise nonlinear MLPs are used, do the learned latent factors really reflect the useful pattern in data? In other words, is it possible that meaningful patterns will be encoded in component-wise MLP, otherwise the latent factor's component?  More discussion or numerical experiments to investigate the consistency are encouraged.

- As I recognize the importance of the interpretability of tensor factor, is the interpretability from component-independent formulation better or more helpful than such component-cross methods? For example, for Tucker decomposition, the learned Tucker core can also show interpretability to help people understand the inner pattern of data. Some claims on why component-wise interpretability is crucial should be highlighted. Otherwise, the novelty and contribution of the proposed work could be limited.   

- The experiment setting and analysis could be further enhanced. Some other non-linear tensor methods could be added as baselines, such as Gaussian-Process-based[1]. The downstream task setting by finetuning is interesting, but some discussion and analysis on why the proposed design could enhance the generalization performance are encouraged.

### Questions
See weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers a modified CP decomposition in which the multi-vector inner product defining each element is replaced by a sum of neural networks, whose input dimension is equal to the order of the tensor. The experiments focus on tensor completion for binary tensors, with a cross-entropy loss function. The experiments include comparison with alternate decompositions for accuracy on a few tensor completion test problems. Additionally performance and interpretability is considered for classification tasks.

### Strengths
+ The proposed model is relatively simple and makes sense, though theoretical/application grounding of the method is not quite clear.
 + The results demonstrate improvements in accuracy over a variety of baselines, which seem to be achieved with a more compact model (though model size is not explicitly evaluated).
 + The results include both performance evaluation and downstream tasks.
 + The paper is clear / reasonably well-written, in both presentation of the method and its evaluation.

### Weaknesses
 - Besides the definition of the new algorithm, the paper has practically no theoretical analysis, besides a simple cost quantification based on CP parameters.
 - In discussion of closely related works on tensor decompositions with factors replaced by neural nets, the following sentence is used as contrast "However, the way they used neural network entangled associations of all components makes it difficult to identify the contribution of entities." This seems overly broad, and should be justified by particular aspects of each of the related methods.
 - Comparison of different models in accuracy for relative to model size would be of interest.
 - The accuracy improvements compared to other models seem pretty minor.
 - I have some concerns regarding whether state-of-the-art methods are being used as baselines here, please see the questions.

### Questions
* Are the baselines implemented by the authors or are existing codes used? I would be concerned that Adam is not an efficient method (does not lead to the more accurate decomposition) for training some of the baselines.
 * Why is CPD not trained relative to cross-entropy? There are existing works for CP completion with generalized loss functions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
