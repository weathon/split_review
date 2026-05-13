# Deep Unlearning: Fast and Efficient Training-free Approach to Controlled Forgetting

- Decision: Reject
- Scores: 8, 3, 5, 5

## Abstract
Machine {\em unlearning} has emerged as a prominent and challenging area of interest, driven in large part by the rising regulatory demands for industries to delete user data upon request and the heightened awareness of privacy. Existing approaches either retrain models from scratch or use several finetuning steps for every deletion request, often constrained by computational resource limitations and restricted access to the original training data. In this work, we introduce a novel class unlearning algorithm designed to strategically eliminate an entire class or a group of classes from the learned model. To that end, our algorithm first estimates the Retain Space and the Forget Space, representing the feature or activation spaces for samples from classes to be retained and unlearned, respectively. To obtain these spaces, we propose a novel singular value decomposition-based technique that requires layer wise collection of network activations from a few forward passes through the network. We then compute the shared information between these spaces and remove it from the forget space to isolate class-discriminatory feature space for unlearning. Finally, we project the model weights in the orthogonal direction of the class-discriminatory space to obtain the unlearned model. We demonstrate our algorithm’s efficacy on ImageNet using a Vision Transformer with only $\sim 1.5$% drop in retain accuracy compared to the original model, while maintaining under $1$% accuracy on the unlearned class samples. Further our comprehensive analysis on a variety of image classification datasets and network architectures shows up to $4.07$% better retain accuracy with similar unlearning (forgetting) on the forget class samples while being $6.5\times$ faster as compared to a strong baseline we propose. Additionally, we investigate the impact of unlearning on network decision boundaries and conduct saliency-based analysis to illustrate that the post-unlearning model struggles to identify class-discriminatory features from the forgotten classes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this research endeavor, a novel class unlearning algorithm is introduced, meticulously designed to eliminate an entire class or a group of classes from the acquired model. The algorithm, developed within this study, initiates by estimating two essential spaces: the Retain Space and the Forget Space. These spaces represent the feature or activation spaces corresponding to the samples from classes that need to be retained and unlearned, respectively. The method proposed for obtaining these spaces leverages a unique singular value decomposition-based technique, mandating the collection of network activations at different layers via several forward passes through the network. Subsequently, the shared information between these spaces is computed and selectively removed from the Forget Space, thus isolating the class-discriminatory feature space for the unlearning process. Ultimately, the model weights are projected in the orthogonal direction of the class-discriminatory space, resulting in the derivation of the unlearned model.

### Strengths
1. The method is very simple and elegant.
2. Provides a strong baseline stable-ascent and also the proposed method beats the stable ascent.
3. Results are more satisfactory than current SoTA methods.

### Weaknesses
1. Requires a few training samples for unlearning. There are methods for zero-shot unlearning.

### Questions
1. There is a more fundamental question about the class unlearning setup. The whole point of unlearning is to replicate a completely retrained model in parameter space or in output space  Now for the preliminary section 3 it is mentioned that for an unlearned model the output label of a datapoint belonging to an unlearned class, is not a true label in this case the unlearned class i.e. y_i != f(x_i,\theta_f). Why is this the case? Is it not that the unlearned model output should be exact/almost the same as the retrained model? If the retrained model gives output as the true label on very few samples why unlearned model can’t give output the same? In other terms,. if the retrained model gives accuracy let's say 3% on the test forget set and the unlearning model also gives similar accuracy on the forget set. The unlearning method is valid. So, I think the y_i != f(x_i,\theta_f) can be formulated in better probabilistic terms so that it matches the retrained model. The implicit assumption is that for a retrained model the accuracy on the forget set if 0 is not correct. We can set adversarial examples such that the retrained model gives an accuracy of 100% on the forget set.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a method for unlearning an entire class or a group of classes from a learned model. They estimate internal activations corresponding to all the layer, for the forget and retain set and then compute a forget and retain space. Then they intersect the two spaces and removes it from the forget space, and final project the weights onto the orthogonal space corresponding to this space. They show that such a method is efficient and performs better than the contemporary methods.

### Strengths
1. The paper address the problem of machine unlearning which is an important problem given the recent explosion in large scale models.
2. The proposed method is easy to use, as it applied layer wise, and only requires layer wise SVD computation.
3. Stable Ascent as a heurestic based method for unlearning is interesting in the case of linear models, however, in this case it is for non-linear models.
4. The paper provides empirical results for different datasets and models.

### Weaknesses
1. The paper is lacking a clear and precise definition of unlearning. Its is important to show the definition of unlearning that you want to achieve through your algorithm.
2. The proposed algorithm is an empirical algorithm without any theoretical guarantees. It is important for unlearning papers to provide unlearning guarantees against an adversary.
3. The approach is very similar to this method (http://proceedings.mlr.press/v130/izzo21a/izzo21a.pdf) applied on each layer, which is not cited.
4. A simple baseline is just applying all the unlearning algorithm mentioned in the paper to the last layer vs the entire model. This comparison is missing.
5. All the unlearning verification are only show wrt accuracy of the model or the confusion matrix, however, the information is usually contained in the weights of the model, hence other metrics like membership attack or re-train time after forgetting show be considered.
6. The authors should also consider applying this method a linear perturbation of the network, as in those settings you will be able to get theoretical guarantees in regards to the proposed method, and also get better results.
7. Since the method is applied on each layer, the authors should provide a plot of how different different weights of the model move, for instance plot the relative weight change after unlearning to see which layers are affected the most after unlearning.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

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
This paper proposes a novel method for class unlearning inspired by work in continual learning that uses Singular Value Decomposition as a means for separating ‘spaces’ containing knowledge of different tasks. In this work, aninstantiation of SVD is used to separate out the ‘forget space’ (the ‘space’ in which the activations of samples belonging to the forget set lie) from the ‘retain space’ (analogously, for retain samples). These spaces are obtained by running SVD on activations (retain or forget) from all layers of the network. The authors show that a small subset of the retain and forget sets suffices for obtaining these activations. Once the forget space is identified, the model weights are updated by a projection to a space that removes forget set information.
The authors also use a baseline that they refer to as Stable Ascent (which was proposed in recent work). Interestingly, they show that both this baseline and their proposed method surpass the previous state-of-the-art in the context of class unlearning on some benchmarks, with their proposed method making further progress over Stable Ascent. They investigate empirically different scenarios (different datasets and architectures, removal of one or more classes either in one-go or sequentially) and report both quantitative results (accuracies) and qualitative ones (gradcam heatmaps to visualize feature saliency).

### Strengths
- The paper studies the important problem of unlearning that is attracting increasing attention recently
- The proposed method is well-motivated and an interesting idea
- For the most part, the paper is well written (see below for some exceptions)
- Indeed the Transformer results are the first to my knowledge application of unlearning methods in larger-scale models that are closer to the state-of-the-art, which is really interesting.
- interesting qualitative analysis of saliency.

### Weaknesses
 - Motivation: the way that the problem of unlearning is motivated in this paper (data deletion; user privacy) seems at odds with the problem of unlearning classes (as it would correspond to unlearning individual data points that don’t necessarily belong to the same ‘class’, depending on the definition of class). What are application scenarios for class unlearning? While the authors have motivated the problem of unlearning well, motivation of missing for class unlearning in particular.
- the authors claim that Stable Ascent is one of the contributions of the paper but this baseline has already been proposed in previous work that the authors did not cite ([A] – see References below, where it is referred to as NegGrad+ and the authors of that work also find that it is a strong baseline, surpassing previous SOTA in several scenarios)
- recent unlearning methods are missing from the Related Work section, e.g. [A, B, C, D] (see References below), and it would also significantly strengthen the paper to empirically compare against them too.  
- ablations are missing. For example, how large is the contribution of the proposed scaling? It would be good to investigate a version of the proposed method without this. Further, how important is it to use activations from all layers for SVD versus just the top layer(s)?
- also, it would be good to motivate the scaling a bit more. Is such a scaling used in the continual learning literature / related methods? If not, what is different about this application that necessitates it?
- the evaluation is lacking. While several evaluation metrics are used for unlearning, the authors rely primarily on accuracy metrics. A particularly important class of evaluation techniques that is missing is membership inference attacks (see e.g. the papers by Golatkar et al, which are cited in this work, and also see [A] from the references below)
- In fact, the evaluation metrics seem to be at odds with the goal of class unlearning that the authors state in the Introduction, namely that “the unlearning algorithm should produce parameters that are equivalent to those of a model trained without the target class”. Despite this definition, the authors don’t look at proximity in weight space or related metrics and instead rely primarily on accuracy.
- In section 3, the description of the problem of class unlearning isn’t precise enough. It’s defined as producing a set of unlearned parameters such that two conditions (test retain examples are correctly classified and test forget examples incorrectly classified) are satisfied for ‘many samples’. But how many samples? Usually, the accuracy on each of those two sets is desired to be just as high/low as it would be for retrain-from-scratch. Is there a reason that this is not the definition used? Also, how come this definition refers only to test examples? Usually it is also desired to have similar conditions hold for the training set (retain and forget partitions).
- clarity: the algorithm is presented in terms of linear and convolutional layers. But in their experiments, the authors also use Transformers. It’s not directly obvious how the proposed method is used for attention layers.
- clarity: “for both linear and convolutional layers, where l is a layer and i is retain sample ” – i was not mentioned in that context. 

Minor issues and typos
==================
- ‘produce parameters that are equivalent to those of a model trained without the forget set’ – not clear what the word ‘equivalent’ means here.
- ‘Generalization on retain samples’ – this is a little confusing as the retain set is part of the training set, so generalization isn’t an appropriate term (as it refers to held-out samples). ‘accuracy’ or ‘performance’ are more appropriate.
- ‘we asks the question’ → ‘we ask the question’
- ‘this section focus’ →‘this section focuses’
- ‘sorted in by the amount →‘sorted by the amount’ 
- ‘the samples form class to be retained’ →‘the samples from the class’
- In several places, some articles are missing, and there are more typos than these mentioned here. 
Please proofread the paper and check for grammatical errors.

### Questions
- What is it about this method that makes it specific to class unlearning? Could one use this method to unlearn a random subset of the training dataset? If not then why not?
- in figure 4, I was surprised that the method of Tarun et al. is more efficient than the proposed method, since Tarun et al uses SGD (in several phases too) while the proposed method only requires forward passes of a few samples (and no backward passes). Why is that?
- in figure 5b, why are the confidence intervals so large? Can we draw any meaningful conclusions from this figure?
- why is the reference point / oracle of Retraining not included in all tables? Is this because it is too computationally expensive to compute this for some models / datasets? Without that reference point, it is not possible to know what the target accuracy/error is for the forget set (because the goal is usually defined as matching / being as close as possible to the accuracy/error of Retrain on the forget set). Could you explain how the results are interpreted given the absence of that reference point?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the question of whether we can unlearn one or more classes from a well-trained model if only a few samples are accessible from the training data of a large dataset. To address this question, the authors propose a novel singular value decomposition-based class unlearning method. This work first estimates the retain space and forget space of the model layer by layer based on the singular value decomposition technique, and then removes the shared information between spaces from the forget space to isolate the class-discriminatory feature space for unlearning, and finally, projects the model weights in the orthogonal direction of the class-discriminatory space to obtain the unlearned model. The authors demonstrate the effectiveness of the method on CIFAR-10, CIFAR-100, and ImageNet datasets as well as VGG11, ResNet18, and ViT models. They also display the applicability of their method in two practical scenarios of multi-class unlearning.

### Strengths
**Originality:** As far as I know, this paper is the first to propose the method of decomposing feature space through SVD to solve class unlearning, so this work is novel.

**Quality:** The approach seems reasonable. By decomposing the feature space of each layer of the well-trained model, the features of the unlearn class are eliminated while reducing the impact on the features of the retained classes. The experimental evaluations in the paper also provide evidence to support the claims made in the paper. In particular, there are verifications on the large datasets ImageNet and ViT. However, the method also has some unclear aspects that I mentioned below.

**Clarity:** The paper is generally well-written. However, there is room for improvement as I mention below.

### Weaknesses
 **Methodology:**
1. The authors only describe the representations collection of linear and convolutional layers, but how to deal with the transformer layer, BatchNorm, etc.? It's unclear how the method handles the specific weight matrices within a transformer's attention mechanism (Key, Query, Value, Output projections) and whether the same SVD-based approach is directly applicable. Additionally, the role of batch normalization layers in feature space manipulation is not discussed, leaving a gap in the completeness of the methodology.
2. The authors perform SVD operation based on the representations matrix of $X_r$ and $X_f$. Do the sample size and sampling strategy of $X_r$ and $X_f$ affect the results of the algorithm? The paper lacks a sensitivity analysis on how the size and composition of these sample sets impact the quality of the estimated retain and forget spaces. It's crucial to understand if a small or biased sample set could lead to inaccurate space decomposition and thus, poor unlearning performance.
3. Why did the authors consider designing importance-base space scaling? Won't this cause the deformation of the forget space and retain space? The rationale behind scaling the forget and retain spaces based on importance is not fully justified. While the goal is to emphasize the discriminatory space, it's unclear if this scaling introduces unintended distortions in the feature space, potentially affecting the representation of both retained and forgotten classes.
4. The choice of best $\alpha$ in Eq.(1) seems to be a trick as different datasets give different $\alpha$ sets. Is there a more reasonable way to choose, like learnable $\alpha$? The method's reliance on a manually tuned $\alpha$ parameter raises concerns about its generalizability and robustness. The lack of a principled approach to selecting this parameter, such as a learnable scheme, makes the method less appealing and potentially prone to overfitting to specific datasets.


**Experiments:**
1. The authors mention that the experimental results come from 10 different target unlearning classes, and CIFAR-100 is evaluated for every 10th. Does it mean that the [10, 20, …, 100]-th class was used as an unlearning class to conduct the experiment? It's unclear if the selection of unlearning classes in CIFAR-100 is representative of the dataset's overall class distribution. Evaluating only every 10th class might not provide a comprehensive picture of the method's performance across all classes.
2. Does the "Original" represent the well-train model? Are the results reported on all retain and forget classes? It's not clear if the reported accuracy for the original model is an overall accuracy or if the accuracy of the retain and forget classes are reported separately. This distinction is important for evaluating the efficacy of the unlearning method.
3. How is the classification head designed? For example, for CIFAR-100, the classification head of the well-train model outputs a 100-dimensional vector. What about the unlearning model? The paper does not specify if the classification head is modified during the unlearning process. If the classification head is not modified, it is unclear how the model is evaluated after unlearning.
4. In Figure 4, the proposed method does not have an advantage in efficiency compared to the Tarun et al. (2023)? Could the authors provide further analysis? The efficiency comparison with Tarun et al. (2023) is not convincing. The paper should provide a more detailed analysis of the computational cost and runtime of the proposed method compared to the baseline.
5. While I think the multi-class forgetting experiment is interesting, what the authors provide is not sufficient. First, simply conducting experiments on CIFAR10 is not convincing. Second, the effects of baselines were not compared. Third, the result analysis is insufficient. For example, why is the original model of resnet18 better in Figure 5a, but not as good as the unlearning model in Figure 5b?

### Questions
1. See weakness for details on methodological and experimental issues.
2. The authors only mention three related works of literature on class unlearning. I am wondering about the importance and practicality of this problem.
3. This paper only evaluates the effectiveness of the method based on the classification accuracy of forgetting and retaining classes. Have the authors considered verification metrics with more theoretical guarantees? If the forgetting class is known, the output probability of the forgetting class can be forced to 0 without changing the model parameters to ensure the effect of forgetting and retaining classes, but this approach is obviously contrary to the motivation of unlearning.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
