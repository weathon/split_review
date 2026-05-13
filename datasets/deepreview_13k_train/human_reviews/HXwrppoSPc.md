# COMiX: Compositional explanations using prototypes

- Decision: Reject
- Scores: 3, 3, 6, 1

## Abstract
Aligning machine representations with human understanding is key to improving interpretability of machine learning (ML) models. 
When classifying a new image, humans often explain their decisions by decomposing the image into concepts and pointing to corresponding regions in familiar images.
Current ML explanation techniques typically either trace decision-making processes to reference prototypes, generate attribution maps highlighting feature importance, or incorporate intermediate bottlenecks designed to align with human-interpretable concepts.
The proposed method, named COMiX, classifies an image by decomposing it into regions based on learned concepts and tracing each region to corresponding ones in images from the training dataset, assuring that explanations fully represent the actual decision-making process. We dissect the test image into selected internal representations of a neural network to derive prototypical parts (primitives) and match them with the corresponding primitives derived from the training data. 
In a series of qualitative and quantitative experiments, we theoretically prove and demonstrate that our method, in contrast to \textit{post hoc} analysis, provides fidelity of explanations and shows that the efficiency is competitive with other inherently interpretable architectures. Notably, it shows substantial improvements in fidelity and sparsity metrics, including $48.82\%$ improvement in the C-insertion score on the ImageNet dataset over the best state-of-the-art baseline.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduced COMiX, an intrinsic explainable artificial intelligence (XAI) method designed to accurately identify prototypical regions within a test image and correlate them with corresponding regions in training images. This method is based on the feature encoder of the trained B-cos network and emphasizes the extraction of class-defining features that serve as prototypes, which are subsequently utilized for class predictions.

### Strengths
- S1: The proposed method is well-motivated, and the relationship between the prototypes and the class-defining features is clear. The requirements for intrinsic interpretability that the authors address are essential components of intrinsic XAI approaches.

### Weaknesses
 - W1: One of my primary concerns pertains to the insufficient details regarding the essential computations involved in the proposed method, which necessitate considerable computational resources. In particular, additional clarification is needed on the computation of mutual information maximization as described in Equation 8. Specifically, how are p(F_j) and p(l(F_j) = c) calculated? Does this process necessitate traversing every row of W_{1 \to L}(d, \theta)? This indeed involves significant computational effort, alongside other tasks requiring substantial computation, such as the generation of pseudolabels for each CDF. The lack of clarity on the precise steps for calculating these probabilities and the computational complexity associated with traversing the weight matrix remain a significant concern, hindering a full understanding of the method's feasibility.

- W2: A secondary concern is the absence of baseline comparisons within the experimental results. While the authors sought to relate their method to prototypical approaches, they did not include comparisons with other state-of-the-art prototype-based methods, such as PIP-Net [1] and ProtoConcept [2], which demonstrate superior performance in accuracy evaluations. Additionally, Table 3 would benefit from including more baseline comparisons, as suggested by references [2, 4]. The lack of direct comparison with established prototype-based methods makes it difficult to assess the relative strengths and weaknesses of the proposed approach. The claim of combining object-level attention and prototypes, as presented in Table 3, necessitates a more rigorous evaluation against similar methods.

- W3: In Table 2, the proposed method demonstrates inferior performance relative to the original B-cos in multiple cases, raising concerns about the suggested approach's efficacy. Additionally, it would be valuable to explore the performance of the end-to-end model by training the feature extractor of the B-cos. The performance degradation compared to the original B-cos model raises questions about the trade-offs introduced by the proposed method. Investigating the performance of an end-to-end trained model would provide a more comprehensive understanding of the method's potential.

- W4: The experiment regarding sparsity requires further validation. Most studies on prototypical learning have addressed the impact of increased sparsity by utilizing global and local explanations or by adjusting the number of prototypes employed [1, 2]. Although Figure 6 presents an ablation study on the size of K, it would be beneficial to enhance this section by incorporating additional baseline comparisons. The current sparsity analysis lacks sufficient context, particularly in relation to existing methods that explore sparsity through different mechanisms. The ablation study on K is a good start, but it needs to be complemented by comparisons with other approaches.

- W5: The experiment focusing on prototypical explanations was conducted solely in a qualitative way. For a quantitative approach, please refer to [2]. Additionally, refer to references [3] and [4] for insights into unsupervised concept discovery. The absence of quantitative evaluation for the prototypical explanations limits the ability to objectively assess the quality of the explanations. Relying solely on qualitative analysis makes it difficult to compare the proposed method with other approaches that use quantitative metrics.

### Questions
Most of my main concerns are listed in the Weakness section. Here, I listed additional questions.

- Q1: In Section 4.4, the authors acknowledged the trade-offs of using l_2 distances. Have the authors considered employing alternative similarity measures, such as cosine similarity? What prompted the decision not to utilize cosine similarity, especially given that the B-cos method inherently leverages this approach?

- Q2: It appears that the negative sign in the L2 distance equation (Eq. 10) may be a typo, as it relates to the process of extracting pseudolabels for each CDF based on the similarity. Is it a typo?

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
3

### Summary
In this paper, the authors proposed COMiX, a method for constructing an interpretable image classifier from a trained B-cos network. In particular, the method starts by training a base B-cos network, and finding M class-defining B-cos features for each class. For a given input image, COMiX first computes a transformation matrix corresponding to the composition of all the layers in the base B-cos network, and then selects a pseudo-label based on the closest training image in terms of the B-cos network's output. For each class-defining feature belonging to the pseudo-label class, the method computes a class prediction based on K nearest training images in terms of that feature's values, and the final prediction is made using majority voting. The authors compared their COMiX classifiers with competing methods (e.g., baseline convolutional networks, ProtoPNet models, B-cos networks) on a number of datasets, and found that their COMiX classifiers performed similarly (or better) to other methods in terms of accuracy and interpretability metrics.

### Strengths
- Originality: The paper proposed an elaborate scheme to turn a B-cos network into a model with a capability to perform case-based reasoning (using k-nearest neighbors).
- Quality: The proposed method did not significantly degrade the classification performance.
- Clarity: The introduction is well-written, and the paper is well-motivated.
- Significance: Interpretability is an important topic.

### Weaknesses
 - Originality: The proposed form of interpretability ("this part of the test image looks like that part of a training image") has been explored in prior work (e.g., ProtoPNet). There is no novelty here.
- Quality: The proposed method constructs a model that is not trainable end-to-end. Also, the proposed method is biased toward the pseudo-label predicted by the B-cos network, since the selection of class-defining features are based on the predicted pseudo-label. This introduces a potential circularity, where the interpretability is tied to the initial B-cos network's prediction, rather than providing an independent explanation. Furthermore, the method's reliance on a pseudo-label for feature selection means that if the initial prediction is incorrect, the subsequent interpretability analysis is likely to be flawed.
- Quality: The accuracy of COMiX is not particularly strong. The paper lacks a thorough comparison with other methods that also aim for interpretability, such as those that learn disentangled representations or use attention mechanisms. The absence of these comparisons makes it difficult to assess the true performance of COMiX relative to the state-of-the-art.
- Clarity: The section describing the algorithm of COMiX is difficult to follow. The presentation is not clear. The notations are confusing. In particular, how is the class-defining features selected using equations (7) and (8), and how is the mutual information computed (equation (8))? The paper does not provide sufficient detail on the practical implementation of these equations, making it hard to reproduce or fully understand the method. The lack of clarity in the feature selection process is a major concern.
- Significance: Given that there is little innovation in terms of interpretability and the accuracy results are mediocre, the proposed method cannot significantly advance the field of interpretable machine learning.

### Questions
How is the class-defining features selected using equations (7) and (8)?
How is the mutual information computed using equation (8)?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Being able to interpret deep neural networks' decisions is becoming increasingly important with the integration of AI into high-risk areas such as autonomous driving and medical diagnosis. Existing methods attempt to explain existing model post-hoc, but may not be faithful to the inner workings of the network. The authors present COMiX, a prototype based method for image classification that links the prediction logic to image parts in the training data. COMiX utilizes B-cos networks for transparency (due to its linearity) from the input pixels to the class defining features used for classification. COMiX then aligns the features from the test image to the features in the training images to perform a KNN-based prediction in order to establish a “this part looks like this one” example-based prediction. The authors measure their model’s ability on four desiderata: fidelity, sparsity, necessity, and sufficiency. They apply their method to several vision backbones and one several popular image datasets. In addition, they qualitatively show the effectiveness of their method for explaining its predictions.

### Strengths
- Qualitative results are strong and convincing
- Modeling / approach is simple
- Robust use in different models / architectures
- Robust ability across datasets
- Creative use with B-cos networks and label aggregation
- Sufficient set of quantitative evaluation metrics
- Hyperparameter analysis / ablation studies present
- Better sparsity than ViT baseline and best insertion scores w/ competitive deletion scores.

### Weaknesses
 - The interpretability framework novelty isn't significantly more compared to ProtoPNet (Seems like another ‘this looks like that’ explanation just reframed)
  - Much of the framework is similar to ProtoPNet with the exception of using pretrained features as concepts (as opposed to specialized vectors), a b-cos backbone, and KNN based prediction on feature similarity. 

- Presentation is unclear at times:
  - Motivation/need for sufficiency is unclear
  - Notation seems convoluted
    - Confused about $s_{L}(x;\theta)$ It seems that it should replace $W_{1->L}(x;\theta)$ in equation 4.
  - Not entirely clear on the attribution method. Is it which feature a pixel contributes most to?

### Questions
- Could you clear up my understanding of the attribution used to make the visualization?
- What is $s_L(x:\theta)$ exactly? Could you provide a better/clearer definition?
- I’m not entirely sure of the definition of necessity, and I’m unsure of the need for sufficiency. It seems redundant. Could the authors clarify necessity, and the need for sufficiency as a desiderata?
- What is the speed of this method compared to others, given it has to look through the entire training data?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes a model that aims to be locally interpretable by design, as it combines B-cos Networks, which provide faithful saliency maps, with prototype methods. During inference, a pseudo-label is computed, whose M learned class features, or class prototypes, are then compared to the test image. The resulting classification seems to be the majority vote of the classes to which the most similar prototype belongs.
As B-cos Networks can provide faithful localizations on training and test images, this enables a visualization of the matching pixels.
As the features are not restricted to patches, the method is considered as object-level attention with prototypes.

### Strengths
The paper explores the important field of building interpretable models.

The core idea of the paper is presented clearly, with good figures 1 and 5. 

Combining b-cos with prototypes is a novel combination. 

The method is evaluated on a sufficient number of datasets and across various architectures.

### Weaknesses
The paper is missing the discussion of several competitors, e.g.:ProtoPool, Pip-Net, Q-SENN (citations at the bottom);
All of these focus on sparsity and Q-SENN and ProtoPool additionally aim for object-level prototypes or features, not restricting the prototypes to patches.
They further achieve better results in e.g accuracy and sparsity, which leads to global interpretability.
Notably, ProtoPool also uses exact training images as prototype for matching.
Thus, the novelty of the proposed method is very limited, as it just combines two existing methods, prototypes and b-cos, even without proper citation and comparison to in multiple ways superior SOTA. Notably, SOTA methods are backbone independent, so presumably compatible with b-cos. 

The reported baselines are significantly too bad. Just training a vanilla resnet34 on CUB (on presumably the same data: 224x224, no crop) with hyperparameters optimized for a resnet50 on 448 gets 2.7 p.p. more accuracy. 
This more than doubles the gap, and questions the validity of other results too.

The writing, especially of the method, is not clear:
 Eq. 4-11 lack explanations.
The algorithm 1 is unclear and lacks explanations. 
Figure 2 is not clear. 
What is trained when and how many settings (encoder training, CDF computation, inference?) exist and are shown is not clear.
The indices in eq.2-3 are unclear.
What is M set to?
Table 4 is not clear. What is the probed model for the other methods, and why is b-cos not a baseline?

Using a parametrized metric (PQ) with just one competitor is not convincing, when the parameters are chosen.
Additionally, the sparsity seems just slightly above a black-box model.

The definition of sufficiency in l308 seems different to the initially stated goal.

The standard deviations of results, excluding table 2,  and number of seeds per result are missing.

"Previous work has also shown that B-cos transformers inherently learn human-interpretable
features."  (l.217) needs a citation if available. I am not aware of any work showing that.


ProtoPool: Rymarczyk, Dawid, et al. "Interpretable image classification with differentiable prototypes assignment." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022.
Pip-Net: Meike Nauta, Jörg Schlötterer, Maurice van Keulen, Christin Seifert (2023). “PIP-Net: Patch-Based Intuitive Prototypes for Interpretable Image Classification.” IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
Q-SENN: Norrenbrock, Thomas, Marco Rudolph, and Bodo Rosenhahn. "Q-senn: Quantized self-explaining neural networks." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 38. No. 19. 2024.

### Questions
Am I misunderstanding the method?

Why is an uninterpretable pseudo-label necessary?

Did I use a wrong configuration for my baseline?

### Soundness
1

### Presentation
2

### Contribution
1
