# One-Hot Encoding Strikes Back: Fully Orthogonal Coordinate-Aligned Class Representations

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Representation learning via embeddings has become a central component in many machine learning tasks.  This featurization process has gotten gradually less interpretable from each coordinating having a specific meaning (e.g., one-hot encodings) to learned distributed representations where meaning is entangled across all coordinates.  In this paper, we provide a new mechanism that converts state-of-the-art embedded representations and carefully augments them to allocate some of the coordinates for specific meaning.  We focus on applications in multi-class image processing applications, where our method Iterative Class Rectification (ICR) makes the representation of each class completely orthogonal, and then changes the basis to be on coordinate axes.  This allows these representations to regain their long-lost interpretability, and demonstrating that classification accuracy is about the same or in some cases slightly improved.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
While representations in deep learning have become more expressive over time, their interpretability has deteriorated over time as well. This paper advocates to recover the interpretability of the features produced by a deep learning model, by building on top of previous works that encourage sparse and compact representations, and proposing two post-hoc methods that further orthogonalizes these representations. Empirical results show that representations obtained with the proposed methods are indeed orthogonal and axis-aligned, while retaining the classification performance.

### Strengths
- The motivation of the work is really well-driven in the introduction section, and it is really appealing.
- Theoretical guarantees for both proposed algorithms are provided.
- Empirical results show the effectiveness of the proposed approaches, as well as the problems of previous approaches.
- I can easily see this work being leveraged by practitioners to improve the interpretability of their features.

### Weaknesses
 - W1. The introduction of the proposed methods is rather convoluted, short, and unclear. Besides, it relies too much on the reader having previous knowledge of how ISR works. The authors should work on providing more context and explanations to the reader. This is the biggest concern I have with the current state of the manuscript.
- W2. Citations should be fixed, as well as references in the bibliography (e.g., some of them have no venues).
- W3. The explanation of why we cannot simply run Gram-Schmidt (GS) is unclear to me and, in any case, traditional orthogonalization methods (GS, Householder transformations, etc.) should be added as baselines in the experimental section.
- W4. I find the back-and-forth between using OPL vs. CIDER in sections 3.2 and 3.3 a bit too confusing
- W5. The presentation of the results needs a bit more polishing. For example, no statistical results (e.g. standard deviations) are presented, and there is no point in having 3 decimals in Table 4 as the least accuracy is $100/10.000 = 0.01$.

### Questions
- Q1. What does it mean that DCR uses a "discontinuous operation"? Discontinuous wrt what exactly?
- Q2. Why is it sensible to normalize the class means? That is, why is it a good idea to completely disregard the magnitude of the class means (since $\arg\min_j D(x, v_j) \neq \arg\min_j D(x, v_j / ||v_j||)$ in general).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript presents a mechanism that takes state-of-the-art learned representations and modifies them to assign specific meanings to some of the coordinates. The method makes the representation of each class orthogonal to the others, and then changes the basis to be on coordinate axes. This adjustment aims to improve the interpretability of the representations.

### Strengths
- The paper delves into an interesting research direction to  leverage pre-trained encoders 
- The authors provide theoretical proofs that underpin the orthogonalization achieved by the proposed methods, granted certain assumptions are met

### Weaknesses
### Major weaknesses:

- The experiments, conducted only on a Resnet-9 and limited to CIFAR10 and CIFAR100 datasets, lack the breadth needed to prove the generality of the method.
 
- The assumption that class means should be entirely orthogonal raises questions. While it makes sense for entirely independent classes, it doesn't account for cases where classes share features or have relationships. The logic behind making every pair of classes orthogonal, especially when some classes naturally have similarities (e.g., apple and orange), remains unclear. This orthogonality constraint may discard potentially useful information encoded in the relationships between classes, hindering the learning of a meaningful metric space.

- Despite emphasizing the method's potential for enhanced embedding interpretability, by orthogonalizing them, the paper does not provide empirical evidence that assesses this claim of improved interpretability.

### Weaknesses:
- The method primary objective and results appear straightforward, yet the paper presents the method in a very convoluted manner.

- While the paper suggests possible advantages in downstream tasks by 'ignoring' particular classes or concept, there are not any experiment supporting this claim.

### Minor: 
- The paper does not discuss the relationship with prototypical networks, leaving a potentially relevant connection unaddressed.

- The paper claims that "if the representations are successful, then for direct tasks only a simple classifier is required afterwards,", however, it is arguable if a linear layer is always enough after a learned representation 
- Typo: Roccio algorithm

### Questions
- Why is it necessary for classes to be orthogonal before projecting them into the new basis? Wouldn't it be possible to simply compute the coefficients and execute a change of basis, e.g., using a least squares approach? The rationale behind the choice to orthogonalize vectors first and then execute a change of basis using an orthogonal matrix remains ambiguous. Why not directly learn a non-orthogonal matrix for this transformation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a post-processing step to the training phase of a learned embedding in the context of  multi-class image classification. The main objective of the step is to obtain orthogonal class means while preserving linearly separable classes at the last layer of the network.
Two algorithms are proposed : Iterative Class Rectification and Discontinuous Class Rectification. Theoretical guarantees of the convergence of both methods are given and numerous experiments are carried out to demonstrate the orthogonality obtained and the preservation of performance in a classification context.

### Strengths
- The proposed method is simple, its internal objectives are well described, and the theoretical part seems sound. 
- Numerous experiments are carried out

### Weaknesses
 - The orthogonality objective of the method (although achieved) is not linked to a specific performance improvement in the experimental context,  which makes  its claim somewhat arbitrary. For example, the use of the post-processing step for Out-of-Distribution detection leads to a performance degradation.

- In general, the choice of a smaller ResNet architecture (ResNet-9) does not allow to obtain experimental results equivalent to those provided by the mentioned methods for baseline comparison, although complete results and numerous details are provided.

- The method does not seem to perform consistently depending on the evaluation criteria for image classification. This affects the evaluation of the performance in the case of classification.  Since classification performance does not seem to be the main objective of the post-processing steps : other experiments could have been tried, such as robustness to label noise or robustness to adversarial attacks, as for example in the OPL method paper.

- From a broader point of view, it seems that the goal of orthogonalising the latent space has something in common with  the orthogonal classifier setting, which could provide further experiments and theoretical approaches (See for examples « Controling directions orthogonal to a classifier », ICLR’22).

- As ICR is an extension of ISR (Aboagaye et al.),  the scope of the contribution is limited, despite the scaling capacity of the proposed algorithms.

### Questions
-What query related experiments in the SOTA could be used to evaluate the validity of the method ?

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
This paper proposes two techniques ICR and DCR for transforming existing class embeddings to be orthogonal and axis aligned for interpretability and better performance.

The brevity of the review doesn't stand for the quality of the review or of the paper, it is solely because of the prime questions I have about the paper.

### Strengths
The motivation for the problem setup (within in its assumptions) makes sense for the modern-day end-to-end learned representations.

The math behind the formulations and algorithms checks out and gives us a projection matrix that helps in improving the interpretability and accuracy in certain multi-class settings.

The applications to OOD also make quite a bit of sense.

### Weaknesses
I found the paper's fundamental question confusing. If I understand correctly, authors want to take the "spherical" learned embeddings of the images from the penultimate layer -- which often are not disentangled. Then the authors want to compute the class prototype by the class mean which will not be orthogonal to other classes (by design). The goal is to transform these to be orthogonal using techniques like OPL and CIDER and then make them axis-aligned and binary through ICR and DCR. Please correct me if I am wrong in this.

Now the questions are

1) I do not see why we need orthogonal class representations -- because semantically I would like to have a substantial weight in the tail of similar but not the same classes. For instance, if we have an image of an orange, it is desirable to have some non-zero activation for the "apple" class prototype due to their semantic similarity. Enforcing orthogonality seems to discard this potentially valuable information. In case I do not want the semantic similarity between class prototypes to be smooth, one can normalize with the appropriate temperature.

2) The second question is more about why we even need these transformations. If you learn a one-vs-all multi-class classifier for all these data points and classes you will end up generating a "one-hot" vector of dimensionality = number of classes. This is the regular linear classifier with softmax after all the multi-class image classification networks we learn today. The classifier itself is the projection to ensure you obtain an orthogonal axis-aligned vector for each datapoint and in turn each class. Leaving it at softmax and not thresholing gives your semantically meaningful embeddings that can further be used for class embeddings. A standard linear layer on top of the penultimate layer, followed by a softmax activation, effectively achieves this. The resulting probabilities can be interpreted as a measure of class membership, and the weights of the linear layer can be seen as class prototypes. Why is the proposed method superior to this standard approach?

It would be great if these questions could be resolved and the paper heavily leans on OPL and CIDER at times and would be good to have a short background section on the math behind them.

I also point the authors to error-correcting output code line of work [1] and probably a concise survey [2] spanning interpretable and learned ECOCs. They aim at learning sub-linear cost class representations in binary space (not necessarily orthogonal, but can be made and also made interpretable in attribute space). This helps result in axis-aligned attribute interpretable binary codes for classes. This also deals with some notions of OOD detection.

### Questions
see above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
