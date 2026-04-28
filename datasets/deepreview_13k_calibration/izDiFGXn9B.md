# Benchmarking a well-calibrated measure of weight similarity of deep neural network models

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Deep learning approaches have revolutionized artificial intelligence, but model opacity and fragility remain significant challenges. The reason for these challenges, we believe, is a knowledge gap at the heart of the field --- the lack of well-calibrated metrics quantifying the similarity of the internal representations of models obtained using different architectures, training strategies, different checkpoints, or under different random initializations.  While several metrics have been proposed, they are poorly calibrated and susceptible to manipulations and confounding factors, as well as being computationally intensive when probed with a large and diverse set of test samples. We report here an integration of chain normalization of weights and centered kernel alignment that, by focusing on weight similarity instead of activation similarity, overcomes most of the limitations of existing metrics. Our approach is sample-agnostic, symmetric in weight space, computationally efficient, and well-calibrated.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Examines the correlation between weight similarity measures [1] and the functional similarity of models, showing that in many cases such measures perform better than representation similarity. They improve on the set-up of [2] by using the fraction of agreed predictions instead of the (coarser) accuracy gap. The paper also examines ’intuitive’ calibration tests that compare models with random weights and trained models. The weight similarity metric, wCKA, is motivated by showing that it is invariant to intertwiner groups, groups that transform model weights such that the underlying network function is unchanged but the representations are different, a desirable property for a measure on model weights.

### Strengths
- If it holds up, the core result— that comparing just the weights of models often performs better on statistical testing for functional similarity than representation similarity— is both interesting and surprising. The method also is substantially more efficient, does not require data, and may be complementary to representation similarity methods. 
- The experiments are a decent start to begin to validate the above claims.
- The theoretical grounding is nice, and supports the experimental claims made in the paper. In particular, connecting chain normalization [1] (which seems to me to be an under-cited paper!), showing invariance to intertwiner groups [3], and using CKA [4].

### Weaknesses
 - The current experiments are not nearly sufficient to justify the usefulness of the metric. The models considered are far too small (all less than 2500 neurons) and trained on too toy of problems (MNIST). The scope and size of the model architecture and datasets examined (e.g., there are large fully connected models that achieve good enough performance on ImageNet or CIFAR-10 or text tasks) should be increased. 
- There is a large related literature on learning on learning on models (eg [5]) that the authors do not cite / are not aware of and should probably be used to contextualize (or strengthen) these results.

### Questions
- Why consider only extremely small architectures and very small datasets? The method seems very cheap to use.
- Why not extend to the same set of architectures considered in [1]?
- Could the authors better motivate the transfer experiments in Fig. 4? They seem prima-facie designed to adversely select against representation dissimilarity metrics?

### Soundness
2

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
4

### Summary
The paper presents a novel model similarity metric, weights centered kernel alignment (wCKA), which compares the weights of the models directly instead of the internal representations / activations like past works have done. The method is a combination of the weight normalization operator and CKA, both of which have been proposed by past works. The authors compare their proposed method with three popular model (dis)similarity metrics often used in the literature, namely Procrustes distance, CKA and deconfounded CKA. They use a benchmarking framework correlating the various model similarity measures with model functionality. They show through statistical testing that their method is better "calibrated" and better captures the functional similarities between different models than the considered benchmark methods.

### Strengths
- I do believe the problem being tackled is an important one and better model similarity measures would greatly benefit the field as a whole.
- The paper is generally well written and clear although some sections would require further clarifications (see the other sections of this review)
- The proposed method is interesting and takes a different approach to model comparison, namely comparing weights, than past methods which have focused on comparing representations. The method is theoretically sound as far as I can tell.
- I like the comparison / benchmarking framework proposed, which follows in the steps of Ding et al., 2021 relating model similarity to model functionality. Furthermore, using the agreed predictions between two models across standard test samples, OOD corruptions and adversarial samples is a notable improvement over simply utilizing the accuracy on a given task. This benchmarking framework, or a similar one, should be used in papers in this field.
- The benchmarked methods (Procrustes, CKA, dCKA) are relevant.
- I appreciate the fact that the authors have run statistical tests to support their conclusions.

### Weaknesses
While I do generally like the quality of the paper there are few important weaknesses that prevent me from giving a higher score. These weaknesses are presented below, in order of importance.

- **The scope of the method is inherently limited.** From my understanding, the proposed method relies on the models being MLPs, i.e. simple feedforward linear networks, and the experiments show this, all experiments being done with standard MLPs. Even in section 3.3 where a pre-trained conv net back-bone is used, it’s the MLP heads which are then fine-tuned that are compared (as far as I can tell, see questions). I consider this to be the main limitation of the work. The method being presented isn’t extended to any type of modern deep learning architectures, i.e. convolutional layers (although this might be possible as discussed in (Wang et al., 2022)), residual connections, attention mechanisms / transformers. Since model similarity measures are inherently practical tools, i.e. they are meant to be used in practice to evaluate and compare models, the fact that the proposed method doesn’t extend to *any* modern model architectures, which are used by practitioners and researchers alike, will significantly limit the impact of this work. The authors do acknowledge this weakness in the last paragraph of the discussion, which I appreciate, but it doesn’t do anything to actually remedy this weakness.
- **A more detailed discussion of the implications of switching from representation based model similarity metrics to a weights based similarity metrics is missing.** The switch from representation based model comparison to weights based model comparison is significant and hasn’t been properly discussed anywhere in the paper. For example, in Figure 1 the authors show that their method yields ~0 similarity between randomly initialized neural networks and use this as a justification to say that their method is “better calibrated”. However, this might simply be an artefact of their method being weights-based instead of representations-based. The Johnson-Lindenstrauss lemma, a classical result in data science, states that a set of high dimensional points can be embedded into a space of much lower dimension in such a way that distances between points are approximately preserved through random orthogonal projections. In a sense, multiplication by a randomly initialized weight matrix is a random projection, therefore I expect even randomly initialized neural network to have some similarity in their representations. Therefore the fact that the other, representation based, similarity measures don’t have a score of ~0 when comparing randomly initialized network isn’t necessarily a “bug” as the authors make it out to be.
- The scope of the empirical evaluations is limited. The paper presents a novel similarity metric but does little to justify the method's usefulness. In other words, what characteristic of neural networks can be observed using this method that couldn't be observed with past methods?
- The novelty and contribution of this work is somewhat limited since wCKA combines the normalization operator from (Wang et al., 2022) with CKA (Kornblith et al., 2019). A more detailed comparison with (Wang et al., 2022) would be appreciated, this is however relatively minimal.

### Questions
Here I list my questions as well as more minor weaknesses and comments which should be addressed in future iterations of this work but are unlikely to influence my score.

- In the abstract the authors write “… similarity of the internal representations of models…” while their method isn’t concerned with representations, I recommend writing "similarity of models" directly like is done in the text.
- First paragraph of the intro: “and, most recently, large language models.” LLMs are not a exactly a novel “model architecture”, I would remove it from the list.
- The introduction section is somewhat lengthy and convoluted. While I agree with the important “knowledge gap at the heart of the field” I don't think a single model similarity measure, no matter how advanced, is likely to fully bridge that gap.
- The methods section is somewhat lacking in terms of explanations and intuition.
    - The description of the Procrustes method, i.e. “minimizing the Frobenius norm of the difference between the two matrices”, isn’t quite accurate and could be more detailed while still remaining brief.
    - Eq. 2 is the empirical estimator of HSIC. This is a detail but is worth mentioning.
    - Section 2.2 where wCKA is introduced would benefit from a better description of the weight normalization operator (on which wCKA is based) and of the wCKA method itself. Right now the section is mostly comprised of equations with little or no explanations or intuition provided as to what the normalization or the method are doing.
- The authors use $xW$ to denote the multiplication of a linear layer’s weights with its inputs. This is a bit arbitrary but I believe the $Wx+b$ formulation is more popular and will be more familiar to readers so I would suggest using that formulation instead.
- Multiple references are not well cited, for example Klabunde et al., Landi et al. and Ferreira et al. are lacking the year of the publication.
- In section 2.4 the “S” used in the equation is not properly defined.
- While I generally like the benchmarking framework described in section 2.4, the proposed wCKA method does not require any data therefore none of the “clean test samples, OOD corruptions, and adversarial attacks” will affect wCKA. A proper discussion of this would benefit the paper.
- The concept of “calibration” is used throughout the paper, even in the title, but there is no clear definition of what a “well-calibrated” method signifies anywhere in the text. While I would agree that the concept of "calibration" is hard to define, it is still important to provide a definition of the term, even if it's just in the context of this specific work.
- Section 3.3 is misleading since it gives the impression that the proposed method can be applied to convolutional neural networks but from my understanding wCKA is only applied to the fine-tuned MLPs which are added on top of the pre-trained convolutional backbone (unless I misunderstood?). Either way this needs to be made clearer in the text.

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
3

### Summary
This paper proposes a new way of comparing neural networks. While the vast majority of such methods operate on the hidden activations of the two networks (working on the assumption that two models are similar if they represent the same data in a similar way), this work proposes a similarity function based on the network weights themselves, wCKA. By looking at the weights directly and performing several normalizations, wCKA attempts to overcome a number of issues that plague existing work such as a strong dependence of hyperparameter choices. At a high-level, the method consists of applying the well-known similarity method for activations, centered kernel alignment (CKA), to a normalized version of the network weights. The work then shows that wCKA is invariant to various similarities in architecture that do not result in functional differences in the network. Finally, the paper describes a range of small-scale experiments which suggest that wCKA is well-calibrated and can “see past” some differences in training and architecture to align with functional similarity.

### Strengths
**Clarity:** The paper is well-written and clear. It gives a good introduction to a major problem in the field of representation similarity: that the similarity of representations can depend heavily on training hyperparameters and other details and thus do not capture what researchers really want when comparing models. With the exception of a few points noted below, the background section is concise, getting the main ideas across without introducing unnecessary mathematics.

**Problem importance:** The reviewer believes that this is an important and fundamental problem that remains unsolved. While the reviewer does not agree with statements in the introduction and abstract that suggest that this is the major barrier needed to overcome network fragility, it is definitely a challenge that deserves deep thought from the field.

**Approach:** The approach of looking directly at the weights of a network is natural and it is surprising that more works have not yet explored it. By looking at the weights of a network one avoids the additional dependence on choice of activation data. As raw weights are challenging to interpret, the reviewer would have been interested in understanding what structural features of the weights are weighing most heavily in the similarity measurements (even at an informal level).

### Weaknesses
Overall, this reviewer thinks that this paper would benefit from more and wider experiments. The two major areas where things could be further fleshed out include:

**More realistic networks in experiments:** Unfortunately, where similarity functions are likely needed the most is in the setting of large, real-world models. For instance, LLMs, ResNet50 sized classifiers, object detectors, and various flavors of generative image models. While it makes sense to start studies from small MLPs, it would have been great to see a proof-of-concept that this works on large architectures trained on large and high-dimensional datasets. This is particularly important because, beyond compute considerations alone, some analytical methods tend to fail as models are scaled-up (potentially because of concentration of measure type phenomena). While there are many models and datasets that would work for this, something like a ResNet50 for vision models and Llama3-8B for language models would be reasonable targets. In terms of datasets, any vision dataset with larger ambient dimension (e.g., ImageNet) would be interesting to see. The current experiments are limited to small MLPs and do not demonstrate the applicability of wCKA to more complex and realistic scenarios, which is a significant limitation given the intended use case of such a similarity metric.

**More granular results:** The reviewer finished the work feeling that they still don’t have a sense of the quirks of the wCKA similarity function. All similarity functions are sensitive to some types of model differences over others. Sometimes this follows from basic properties of the comparison method. At other times, particularities only become apparent via fine-grained testing. For instance, heatmaps with individual comparisons of layers would have been useful to get a feel for wCKA. An interesting experiment (which has been applied before for representation similarity functions) is to look at similarity between different layers of a single model. It would be interesting to compare this to the equivalent CKA experiment. It would also have been useful to compare the same architecture trained on different datasets, does wCKA show these as different? Without these more granular results, it is difficult to understand the behavior of wCKA and its sensitivity to various architectural and training differences. The current experiments do not provide enough insight into the specific properties of the proposed similarity function.

**Limitations:** In line with the problem of getting to know wCKA better, it would be useful to describe its limitations. Either limitations that are intrinsic to its definition or empirically observed limitations. Examples include limitations to the types of layers to which wCKA can be applied and/or compared. I know some of this is directly inherited from CKA, but it would be good to state explicitly as some of this has different implications when weights are used. When we apply CKA to activations arising from the same subset of data, we can compare them even though the feature space dimensions may be different because the number of instances is the same. On the other hand, when one does this for weights, such a comparison is not possible I think? The paper should explicitly discuss the limitations of wCKA, including the types of layers it can be applied to and the challenges in comparing weights across different architectures or even within the same architecture but with different layer sizes.

### Questions
- Ultimately, we want similarity metrics to give us greater insight into our models. Has wCKA provided any insights not found with other comparison methods?
- Are there any limitation on the types of layers wCKA can be applied to?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the challenge of the lack of well-calibrated metrics for quantifying the similarity between neural networks. Instead of computing similarity between representations, the authors propose wCKA to measure the similarity between weights. wCKA is invariant to neuron permutation, independent of specific input samples, and computationally efficient. wCKA can provide well-calibrated similarity compared with representation similarities, such as CKA and dCKA, and aligns better with functional similarities across different architectures, training methods, and initializations.

### Strengths
The method is well-motivated and is interesting to the interpretable AI community. The proposed wCKA focuses on weight similarity, which is a novel approach, and unlike CKA and dCKA, its computation is independent of the number of samples.  wCKA is well-calibrated and correlates well with functional similarities.

### Weaknesses
My biggest concern is that the wCKA only applies to neural networks with specific architectures, such as fully connected neural networks, and it is not easy to be generalized for other architectures, such as transformer, which are the mainstream of deep learning.

The evaluation is limited. Although the paper shows promising results, most of the experiments are on MNIST. It would be interesting to see how wCKA performs on diverse real-world datasets, such as larger image datasets (ImageNet or CIFAR-100) and text datasets (GLUE benchmark).

### Questions
1. Can wCKA be applied easily to other architectures, such as transformer?

2. Can wCKA be applied to a specific layer, or must it be the whole network? Would applying a layer-wise wCKA affects the conclusion if possible?

3. If wCKA can only be applied to the whole network, which layer did you apply CKA/dCKA on in the benchmarking?

4. Although the computation is independent of the number of samples, it depends on the number of parameters. All models tested in the paper are small. Would wCKA be scalable to large architectures with billions of parameters? It would be great to have any theoretical or empirical analysis of wCKA's computational complexity as the number of parameters increases,

5. It would be great if the author could provide examples of real-world applications where wCKA is more favorable than existing methods due to its unique properties, such as sample-independence and computational efficiency.

### Soundness
2

### Presentation
3

### Contribution
2
