# Beyond Standardization – Putting the Normality in Normalization

- Decision: Reject
- Scores: 8, 8, 6, 5, 3

## Abstract
The normal distribution plays a central role in information theory – it is at the same time the best-case signal and worst-case noise distribution, has the greatest representational capacity of any distribution, and offers an equivalence between uncorrelatedness and independence for joint distributions. Accounting for the mean and variance of activations throughout the layers of deep neural networks has had a significant effect on facilitating their effective training, but seldom has a prescription for precisely what distribution these activations should take, and how this might be achieved, been offered. Motivated by the information-theoretic properties of the normal distribution, we address this question and concurrently present normality normalization: a novel normalization layer which encourages normality in the feature representations of neural networks using the power transform and employs additive Gaussian noise during training. Our experiments comprehensively demonstrate the effectiveness of normality normalization, in regards to its generalization performance on an array of widely used model and dataset combinations, its strong performance across various common factors of variation such as model width, depth, and training minibatch size, its suitability for usage wherever existing normalization layers are conventionally used, and as a means to improving model robustness to random perturbations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel normalization layer, "normality normalization", which aims to achieve almost-Gaussian pre-activations, which goes one step further than any previous normalization layer in ensuring Gaussianity of pre-activations.  They motivate this by citing the intension behind design of previous normalization techniques, information-theoretic arguments that Gaussian distribution has the highest capacity, is more noise-robust, and it simplifies dependencies to correlations, and cite parts of literature that assume or approximate Gaussianity as a desirable property.  

The key technical idea is to use Yeo-Johnson power transform, which aims to make the distribution symmetric and make the tails more like a Gaussian distribution's tails, via a parameter $\lambda$. The best parameter $\hat \lambda$  can be tuned via a maximum likelihood estimation (MLE) loss that captures the normality of the values, given the mean and std of the transformed values. However, because there is no closed form solution for this, this would require an iterative approach. The authors argue that a second-order approximation of this MLE  is sufficient for sufficiently accurate estimate of $\hat\lambda,$ which allows them to compute it via a single Newton iteration.  

They show that empirically, this novel normalization leads to higher validation accuracies across the board, for Layer, Instance, and Batch Normalization,  in ResNet, and ViT architectures. They further show that this improved accuracies hold accross various depths, widths, suggesting that it is not an ad hoc or highly sensitive behavior, but rather a robust improvement across the board.

### Strengths
I very much like overall message and contribution of this paper. First, authors present a a very well motivated argument for why Gaussianity is a good objective in neural networks. This is substantiated by several information-theoretic arguments, as well as the recognition that achieving Gaussianity has been the motivation behind other important modules, such as batch normalizatioin. After recognizing Gaussianity as a key objective in neural architecture design, they set out to solve it in a more principled manner. Furthermore, while the straightforward iterative solution to the power transformation might be too costly, they find that a quadratic approximation is good enough approximation, which can be solved in a single step, adding further novelty and value to their contribution. Finally, the empirical results make a very solid case for the empirical value of this new type of normalization layer.

### Weaknesses
Perhaps the main weakness that I currently perceive is how solid is the empirical case that the paper currently presents. Let me try to break this down:
- Given that noise factor $\xi$ is a hyper parameter, it would be nice to have a plot that shows the accuracy for various values of it. This would be quite important to assess the empirical vaulue of the results. Is a wide range of values for $\xi$ good enough? Or it requires a rather careful tweaking, which is problem/model-dependent? If it is the latter, it might also warrant doing a nested cross validation, (a separate validation and test set, to pick the best value of $\xi$)
- Perhaps the authors can report the percentage increase of time for training networks with BNN or LNN compared to those with BN/LN, so that readers have a better idea of what type of time-accuracy trade off their method offers? While the authors argue that the complexity of this new layer is $O(D)$, the hidden constants here might be important and not negligible. For example, compared to a classical BN or LN layer, there might be 5x or 10x more computations, which is good to report.
- I think adding a few or at least one comparable method to the empirical results is certainly helpful to readers.  While I recognize that there might not be a comparable method in the sense that they don't modify normalization layers, is it possible to compare to methods that involve injecting noise for stability or improving accuracy?
- On a related note, someone might argue that empirical value from the method is solely due to the noise injection, and not the particular power transform method. Thus, perhaps a few more empirical tests (adding noise to classic BN or LN, or an existing method that does that), would help the reader to assess the value of this work a lot!

While I think the writing of the paper is reasonably good, there are a few things that can be improved.
- Earlier in the text, namely in section 2 and introducing $\mathbf{h} = (h_i)_{i=1}^N$,  it was not clear to me what does $N$ represent. While it became clear later that this could be either the batch-wise dimension or across the feature dimension or channels, it wasn't mentioned earlier in the text. This also made it confusing of what type of normality the authors are proposing (across batch or features). Perhaps some clarifying sentences could help the readers and avoid their confusing!
- Authors use "standardization" to refer to the mean-reduction/std-division step (for example in Algorithm 1). I think this terminology is rather confusing, because standardization typically refers to this when it is done as a pre-processing step (just one before training), and not when it is part of the model and applied during training. In general, please try to avoid terminology that conflicts with existing ones.
- While technically speaking, there is nothing wrong with the title, IMHO, the current title lacking a bit awkwardly worded, which might give the wrong first impression to some readers (or cause them to not read it at all). If I may make a suggestion, a simple and descriptive title might do the paper more justice and avoid bad first impressions.

### Questions
- I understand the idea behind introduction of $s$ in the Gaussian noise is to make the scale of noise comparable to scale of the pre-activations. But if that's the goal, why not use a multiplicative noise that automatically achieves it? 
- Just out of curiosity, Suppose we we have matrix $X$ which is $n\times d$ where $d$ is feature dimension and $n$ is batch size. Now, suppose we do BNN across the batch and achieve semi-Gaussian pre-activations. What happens to the distribution of pre-activations across the feature dimension? In other words, I wonder what are the effeects of normality normalization on the dimension that it is not explicitly normalizing.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The main contribution is a novel parametric layer for deep nets that improves the accuracy of image classification across models and datasets. The layer design is inspired by traditional normalization layer. Recent papers show that normalization layers (such as batch and layer normalization) make intermediate data distribution Gaussian across the layers at initialization. To go beyond initialization, this paper proposes to maintains the gaussian property during and after training using power transform (Yan&Johnson). In my opinion, the paper provides a value insights on deep learning training in addition to empirical improvements.

### Strengths
The main strength of the paper is its significant improvement in accuracy for image classification across various datasets. This improvement relies on a specific parametric layer that can be integrated into different neural architectures. In addition to this empirical contribution, the paper provides valuable insight into the mechanisms of normalization layers in deep learning, suggesting that making intermediate representations Gaussian enhances training.

### Weaknesses
The weakness is  **presentation and motivation**.  
- There are several methods beyond power transforms for converting data distributions to Gaussian, including quantile transformation. I implemented quantile transformation myself, which requires no parameters like $\lambda$. However, after normalization, I observed that training became significantly slower and did not yield better generalization accuracy. Given the claim that Gaussian features improve performance, it's essential to verify if other Gaussian transformations, such as quantile transformation, also enhance performance. Since the implementation is easy, I recommend authors to conduct initial experiments on small datasets. Specifically, it would be valuable to see a comparison of training stability and final performance when using quantile normalization versus the proposed power transform. The lack of this comparison makes it difficult to isolate the specific benefits of the power transform over other Gaussianization techniques.
- In my opinion, the writing could be significantly improved. I found it challenging to connect the various concepts, such as the "best-signal" case, the mutual information framework, and noise robustness, to the proposed method. The current narrative feels disjointed, making it hard to understand the underlying motivation for the specific design choices. The connection between the theoretical framework and the practical implementation needs to be more clearly articulated.
- The introduction and abstract begin by explaining the ubiquity of the Gaussian distribution, attempting to **justify** why the proposed method performs well in practice. However, the concepts of the best-signal case or worst-case noise distribution for Gaussian do not clearly connect to the proposed normalization method. The justification feels somewhat superficial and lacks a clear mechanistic link to the proposed approach. It's not clear how these theoretical concepts directly translate into the observed empirical improvements.
- The contribution could be more effectively **connected to related literature**. For instance, some cited papers demonstrate that normalization layers make intermediate data representations increasingly Gaussian at initialization. Building on these findings, the designed layers could be motivated by preserving this Gaussian property throughout training. The paper should explicitly discuss how the proposed method builds upon and extends these existing findings, rather than presenting it as a completely separate idea. A more thorough literature review is needed to contextualize the contribution.
- While the paper focuses on the distribution of individual coordinates, it is important to study how proposed method impact the **joint distribution** of data (across multiple features). Remarkably, references in *Neural Networks as Gaussian Processes* study the joint distribution of data not only a single feature, hence it is important to investigate the joint data distribution. The paper needs to address how the proposed method affects the correlations between different features and whether it leads to more independent representations. This is a crucial aspect that is currently missing from the analysis.

### Questions
- In Figure 5, are the weights random or they are optimized? I am wonderding how the distributions look like after linear layers (not after normalization) when the weights are random. Notably, the data distribution can be gaussian after linear layers or activations while pre-activations are not gaussian. 
-  Does power normalization enhance training convergence as well? The current results only demonstrate improvements in generalization, but I’m very interested in observing how both training and test accuracy evolve during training.
-  How crucial is it to optimize $\lambda$? 
-  As noted, there are several transformations that convert data distributions to Gaussian. Why did you choose power transformation specifically?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose "normality normalization," a new layer that promotes normal distribution properties in neural network features by using a power transform and Gaussian noise. They back their method with experiments showing improved generalization and robustness compared to traditional normalization techniques. This approach performs well across various model architectures and increases resilience to random perturbations, offering a potentially valuable alternative for stabilizing deep network training.

### Strengths
* $\textbf{Theoretical Foundation}$: The use of information theory to support Normality Normalization is robust and well-articulated, highlighting benefits for maximizing representation capacity and robustness.

* $\textbf{Effective Generalization Result}$: Experimental results across multiple architectures and datasets demonstrate consistent improvements in model generalization.

* $\textbf{Comprehensive Analysis}$: The paper provides a detailed explanation of the power transform method, parameter estimation, and noise robustness, making the approach well-documented and technically thorough.

### Weaknesses
 * $\textbf{Limited Baseline Comparisons}$: Comparisons focus on BatchNorm and LayerNorm but do not include other normalization methods like GroupNorm or adaptive techniques, which weakens the generalizability of claims.


* $\textbf{Lack of Practical Efficiency Metrics}$: The paper does not address the computational cost, making it hard to evaluate whether benefits outweigh added complexity in real-world applications.

### Questions
Can the approach generalize to other tasks, such as unsupervised learning, where feature distribution is critical?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce normality normalization, a variant of batch normalization. Instead of just normalizing the first two moments, the authors normalize the distribution to be approximately normal. The normality normalization relies on the so-called power transformation, which can be approximated with an iterative method. The authors demonstrate consistent gains for many small-scale computer vision datasets and models when using normality normalization instead of batch/layer-norm. They also provide a whole section dedicated to motivation and the relationship to information theory.

### Strengths
- Normalization is common and impactful.
- They authors consider multiple models, datasets and normalization baselines and show consistent improvements.

### Weaknesses
 - The experimental parts are relatively small-scale. Would be interesting to train e.g. a small GPT-2 style model.
- Most people might find section 5 (motivation), to not be very relevant. The good empirical results is all the motivation was is needed. :)
- The motivation behind the hyperparameter selection is not clear.
- The baseline accuracy (71.6%) is still suspiciously low (typically, ResNet50 has an accuracy > 75%).

### Questions
- How was the hyperparameters selected for the experiments?
- Are you able to run a more large scale experiment?


# Update

I've reviewed the comments from the other reviewers. I note one mentioning that `The baseline accuracy (71.6%) is still suspiciously low (typically, ResNet50 has an accuracy > 75%).`. I am inclined to agree with this reviewer. I didn't catch this issue when reading the paper myself, but applaud the reviewer for his/her diligence. In light of this issue, I've decreased the score to a 5.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new type of normalization layer for neural networks, to encourage the pre-activation distributions to be Gaussian. This is motivated by several information-theory arguments such as increasing robustness to noise. The layer is composed of standard normalization, a power transform (in which a single power parameter is determined by approximately maximizing the Gaussian likelihood), centralization, and the addition of Gaussian noise. The benefits of these layers are examined empirically.

### Strengths
1. The idea is interesting, original, novel, and with a reasonable motivation. 

2. The proposed layer does seem to improve generalization performance in all cases it was tested on, compared to the existing normalization layers (batch-norm, layer-norm, group-norm, and instance-norm). 

3. The experiments convincingly demonstrate the improvements in normality and noise robustness after using the new normalization layer. 

4. The effect of various quantities, such as width, depth, and minibatch size is examined.

5. The presentation is clear and informative.

### Weaknesses
1. The main issue of this paper is the scale of the experiments. For this type of paper, the bare minimum is an Imagenet experiment and possibly also some Language model fine-tuning. However, this paper stops at the scale of tiny Imagenet and CIFAR. This is crucial since many methods work well on such small datasets but not in Imagenet (for example, weight normalization). The lack of a full ImageNet experiment is a significant concern, as it is unclear if the observed improvements would generalize to larger, more complex datasets and tasks. The experiments on ImageNet100, while larger than CIFAR, do not fully address this concern due to the reduced number of classes and samples compared to the full ImageNet dataset. Furthermore, the absence of any language model fine-tuning experiments limits the assessment of the proposed method's applicability to other domains.

2. Even the existing results are compared to suspiciously low accuracy baselines. For example, ResNet18 in CIFAR10 with standard BN achieves 88.89% test accuracy, while the first GitHub repo I found on Google search achieves 93.02 accuracy (https://github.com/kuangliu/pytorch-cifar), which is better than the 90.41% accuracy reported using the proposed BNN method. This is important, since in many cases using better baselines can cause the improvement to narrow or even disappear. Ideally, for each model and dataset, we need a baseline near the current state-of-the-art and show the new method improves. The most convincing thing would be to show the state-of-the-art is improved for a dataset (using the best model), but I acknowledge this may require too large resources. The low baseline accuracies raise concerns that the observed improvements may not be as significant when compared to more optimized implementations of existing normalization techniques. The use of data augmentations, which are standard practice in achieving state-of-the-art results, is not consistently reported, making it difficult to assess the true impact of the proposed method.

3. Missing ablation studies: how much each part of the proposed layer is contributing to the improvement? e.g. is the power transform more important than the added noise? How sensitive are we to the $\xi$  parameter? This is important, since if most of the benefits come from the added Gaussian noise, this takes away some of the novelty of the method, as this is somewhat similar to Gaussian dropout, which has already been suggested before (“Fast Droput Training” ICML 2013, “Variational Dropout and the Local Reparameterization Trick” NeurIPS 2015). The lack of ablation studies makes it difficult to understand the individual contributions of each component of the proposed normalization layer. Specifically, it is unclear whether the power transform or the added noise is the primary driver of the observed improvements. Furthermore, the sensitivity of the method to the $\xi$ parameter is not thoroughly explored, which is important for practical implementation and parameter tuning. Without these studies, it is difficult to ascertain the novelty of the method, especially given its resemblance to Gaussian dropout.

Minor points:

line 150: “No additional parameters” title is misleading, even though the paragraph says no additional learnable parameters since the $\xi$  is a free parameter (but not a learned parameter)

Table 2: some are the test accuracy results are extremely low (e.g. 66.56% on CIFAR10), probably because ViTs don't work well in small datasets. If we must test layer norm on small datasets, then I would use an architecture with more reasonable performance, such as Convnext. 

Motivation section: it is a bit strange that this section appears toward the end. It's more common to write this at the beginning.

line 499: I'm not sure what the line “Seldom has the question of precisely what distribution a deep learning model should use to effectively encode its representations” means. I think this has been investigated in many different contexts, for example, the information bottleneck papers and the quantization literature (where some distributions are easier to quantize than others).

### Questions
See weakness section.

### Soundness
2

### Presentation
3

### Contribution
2
