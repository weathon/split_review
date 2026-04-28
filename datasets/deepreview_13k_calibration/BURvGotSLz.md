# Is Training Necessary for Representation Learning

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
The field of neural network-based encoders is currently experiencing rapid growth. However, in the pursuit of higher performance, models are becoming increasingly complex and specialized for specific datasets and tasks, resulting in a loss of generality.
In response to this trend, we explore the finite element method (FEM) as a general solution for feature extraction and introduce LagrangeEmbedding, an untrainable encoder with a universal architecture across various types of raw data and recognition tasks. Our experimental results demonstrate its successful application and good performance in diverse domains, including data fitting, computer vision, and natural language processing.
LagrangeEmbedding is explainable, it adheres to the error-bound formula in FEM, which governs the relationship between mean absolute error (MAE) and the number of model parameters. 
As the encoder has no trainable parameters, neural networks utilizing it only need to train a linear layer. This reduces gradient computation and significantly accelerates training convergence.
Our research promises to advance machine learning by opening up new avenues for unsupervised representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the author proposed a feature extraction method termed LagrangeEmbedding, which can extract features from simple image and text datasets. LagrangeEmbedding fits a function with many piecewise linears. The proposed method is validated with regressor and classification tasks.

Overall, the ideal is novel, which can inspire further development of unsupervised representation learning. However, the related works that are closely related to the thinking of LagrangeEmbedding should be given. The proposed method seems to only work on simple datasets. What's more, the performance comparison is not provided.

### Strengths
1. The idea is novel. It provides a novel perspective for unsupervised representation learning.
2. Some detailed examples and analyses are provided.

### Weaknesses
1. The proposed method seems to only work on some toy tasks. 
2. The related work sections or some closely related works are not provided.
3. The proposed method is only validated on simple image and text datasets. The comparison results with SOTA methods are not given. Even the proposed method achieves lower accuracy than SOTA methods. The comparison experiment with SOTA methods can assist the reader in finding the gap between the proposed and SOTA methods.
4. The proposed method only runs in a non-parallel manner, as mentioned in the future directions section.

### Questions
1. It seems that the proposed method can only extract low-level features, unlike the deep learning-based methods. The extracted features seem only suitable for toy tasks. Does the proposed method can extract non-low-level features? 
The author is suggested to add some analysis and discussion.
2. How can we extend the proposed method for complex tasks in actual situations? The author is suggested to add some discussion.
3. I have not seen the author mention some closely related works. Is the proposed method totally original? If not, please provide the detailed related works and the difference between the proposed method and the related works.
4. In section 2.1,  the definition of m in x^{(m)} is not given. What's the difference bettween the x^{(N-1)} and  x^{(m)} ?

Other suggestions:
a） In Eqn(2), the ‘i’ is suggested to be replaced with 'n';
b） ”given function F (x) to be fitted”  ->``given function F (x) to be fitted”
c） The definition of SVR is not given.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a training-free approach for generating a feature vector, where each coordinate value corresponds to the output of a Lagrange basis function. The proposed method enjoys theoretical guarantees on its approximation error as a function of the number of parameters. The effectiveness of the resulting embedding is evaluated on fitting data drawn from known distributions, as well as classification/super-resolution on the MNIST dataset, and classification on AG News dataset.

### Strengths
- The method does not require training/backpropagation to generate input embeddings.
- The method is evaluated across multiple tasks from traditional data fitting, to computer vision and NLP tasks.
- The method enjoys theoretical bounds on the approximation error given the number of model parameters.
- Limitations are discussed

### Weaknesses
 - The paper over-promises and under-delivers. Among other broad claims - e.g. first paragraph of the conclusion, ``unparalleled level of explainability” - the title itself “Is training necessary for representation learning” suggests that the proposed method can be comparable to training-based approaches such as neural networks. Yet, there exists few, if any, quantitative comparisons between the proposed method and neural network approaches, especially for the (toy) computer vision and NLP experiments.
- In fact, the basic 2-layer convolutional network, for instance taken from the PyTorch tutorial page (https://github.com/pytorch/examples/tree/main/mnist), already achieves 98% accuracy on MNIST in the first epoch (outperforming the proposed approach), which completes in under a minute on a CPU and presumably orders of magnitude faster on GPU. The lack of direct comparison against such a baseline makes it difficult to assess the true value of the proposed method.
- Sec 3.1.2 compares against neural networks when fitting distributions drawn from 2-dimensional distributions, but it is not stated what network parameters nor training parameters are used other than the fact that it is a MLP. This lack of detail makes it difficult to reproduce the results or understand the comparison.
- It seems that in Table 1, Random Forest is already highly effective at achieving almost perfect R^2 scores, and performance on most of the distributions considered appears to have already saturated. This raises questions about the significance of the proposed method in these specific data fitting tasks.
- How did the projection layer in Sec 3.2.1 arise? There is no explanation for why this specific projection equation was introduced, and while it claims to contain “no trainable model parameters”, it appears to require careful hand-crafting as well. The lack of justification for this specific projection is a weakness.
- Speed is touted as an advantage of the method, but there exists no wall-clock timing comparisons for computing the proposed embedding. The absence of these timing comparisons makes it difficult to evaluate this claim.

Minor comments
- Eqn (2) $y^{(j)}$ should be $y^{(i)}$ instead
- In Sec 3.3, does “the neural network” refer to the proposed method (i.e. typo)? If not, are there quantitative results and comparisons for the proposed method? 
- Also in Appendix D.2., I assume “Remarkably, after just 4 epochs of training, the neural network outputs close approximate the target values” is also a typo?

### Questions
- Sec 3.3 - can you elaborate on how the pre-processing layer is implemented?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents LagrangeEmbedding, a method for obtaining a data representation based on a first-order Lagrange basis. The authors present an algorithm for generating a mesh on the input space and show how to form the Lagrange basis in an efficient way using parallelization. The effectiveness of the method was demonstrated on several datasets, mostly in low-dimensional settings.

### Strengths
* A novel method for obtaining representations in an unsupervised that doesn't require any learning.
* The paper is written well and clearly. The visual illustrations are good and help to convey the main points in the paper.
* The method is grounded by theoretical justifications, such as the universal approximation, which adds a nice flavor to the paper.
* Code was provided and the results seems to be reproducible.

### Weaknesses
 * The main limitation of the proposed approach, in my opinion, is that it misses the goal of the paper (or at least the one that was presented). I acknowledge that in some cases, mainly in low-dimensional settings or on simple datasets (e.g., MNIST) it works fine. However, the main goal of learning transferrable representations is from big, complex, and high-dimensional datasets. Currently, this approach doesn't fit these types of data, and I am skeptical if it will ever will as FEM is not a new idea. Hence, at least currently, I do not think this paper can make an impact as the authors imply in the paper. Nevertheless, I do appreciate novel and non-standard directions, even if they are not mature yet, and I give the paper credit for that.  
* Another possible limitation relates to the fact that the method doesn't have any learnable parameters. Often there is a domain shift between the dataset for learning representations and the dataset of interest, or between the training set and test set. Standard NN-based approaches can work well in such cases (depending on the magnitude of the shift) or can be adjusted to these shifts by fine-tuning the feature extractor, for example. Yet, as the proposed method heavily relied on the algorithm for obtaining a multiscale mesh based on the training set, it is not clear how it will work in such cases.  
* I expected to see a broader reference to kernel methods, but the paper seems to miss this related research direction entirely. Kernels also form a basis function and are also universal approximators, and perhaps there is some connection to the Lagrange basis function. More importantly, I find two studies particularly relevant (to address and compare to). First, the line of research on infinite-width NNs [1, 2] which also hinges on inner products in the input space. Second, the method presented in [3] also suggests to use simplices for approximating the full data kernel. When does the proposed approach preferred over these modeling choices? 
* Regarding the experiments, it is not clear what is the test performance of the proposed approach on MNIST. If it is 97.25% as implied in the text, how is that equivalent to 6-layer CNN when even a standard LeNet reaches ~99.3% accuracy?  
* In my opinion, some information is missing. Specifically,
  * A reference (or a proof) for the two properties of the Lagrange basis function in Section 2.
  * Intuition on the dimensionality reduction technique in section 3.2.1.
  * Why is the following true $(n_t/d!)^{1/d} = \mathcal{O}(h^{-1})$?

### Questions
* At the beginning of Section 2.1, what is $m$, did you mean $N-1$?
* Perhaps I didn't understand something, but to me the definition of the Lagrange function $\mathcal{L}_i$ seems to be the indicator function and not a linear function picking at $p^{(i)}$.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good
