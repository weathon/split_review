# Training-Like Data Reconstruction

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 3, 1

## Abstract
Machine Learning models are often trained on proprietary and private data that cannot be shared, though the trained models themselves are distributed openly assuming that sharing model weights is privacy preserving, as training data is not expected to be inferred from the model weights. In this paper, we present Training-Like Data Reconstruction (TLDR), a network inversion-based approach to reconstruct training-like data from trained models. To begin with, we introduce a comprehensive network inversion technique that learns the input space corresponding to different classes in the classifier using a single conditioned generator. While inversion may typically return random and arbitrary input images for a given output label, we modify the inversion process to incentivize the generator to reconstruct training-like data by exploiting key properties of the classifier with respect to the training data. Specifically, the classifier is expected to be relatively more confident and robust in classifying training samples, and the gradient of the classifiers output with respect to the classifier’s weights is also expected to be lower for training data than for random inverted samples. Using these insights, along with some prior knowledge about the images, we guide the generator to produce data closely resembling the original training data. To validate our approach, we conduct empirical evaluations on multiple standard vision classification datasets, demonstrating that leveraging these robustness and gradient properties enables the reconstruction of data semantically similar to the original training data, thereby highlighting the potential privacy risks involved in sharing machine learning models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new method for reconstructing data that resembles the training dataset of an ML model. The method is based on two steps: inversion, where one learns the space corresponding to different classes, and reconstruction.

### Strengths
- The related work presents an interesting connection between reconstruction attacks and works from the '90s.
- The method is fairly presented.

### Weaknesses
 - The paper defines no metrics to evaluate the effectiveness of the method. The only results that are shown are reconstructed images.
- No empirical comparison is provided against state of the art methods (or any methods, for that matter). Unfortunately, this makes it impossible to judge how better the method is with respect to prior work.
- It is unclear what the main goal of the reconstruction attack is. In the literature, there are two: 1) reconstructing one (or more) images that look as close as possible to the original image (e.g., see Balle et al. 2022 as referenced by the authors), and 2) reconstructing images that resembles data from a certain label (e.g., (Fredrikson et al., 2015)). Based on the results (Fig 3-4), it seems to me that the proposed attack is trying to do the former but is achieving the latter.

(Fredrikson et al., 2015) "Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures". You may want to include this reference, which predates (Yang et al., 2019) in terms of model inversion attacks.

### Questions
>While these attacks have been demonstrated in controlled settings, where models are typically over-parameterized or overly simplistic, the risks associated with sharing models trained on large, complex and multi-class datasets are yet been fully explored.

Some of the related work you mentioned did actually consider some of these factors. You may want to be more precise here.

>For under-parameterized models, where there is no possibility of memorization

This is an overstatement.

### Soundness
1

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
The paper introduces a network inversion approach to reconstruct training-like data from trained models. The paper modifies the inversion process to incentivize the generator to reconstruct training like data by exploiting several key properties of the classifier with respect to the training data. For example, the classifier is expected to be relatively more confident and robust in classifying training samples, the gradient of the classifier output with respect to the classifier's weight is also expected to lower for the training  data than for the random inverted image.

### Strengths
The method extends inversion techniques from simpler architectures to CNNs, demonstrating its potential with complex datasets and classifiers.

The incorporates a few types of losses including Cross-entropy, KL divergence, cosine similarity, and feature orthogonality losses that may be useful to reconstruct training like data.

Demonstrates the model's effectiveness across multiple datasets, highlighting privacy risks in different scenarios.

### Weaknesses
The paper assumes because training data possess these properties, we can use these properties to reconstruct the training data, which may not be theoretically right. For example, A => B does not mean B>A. 

The paper also do not have any formal metrics on how successful the reconstruction attack is. Specifically, the paper lacks quantitative metrics to assess the fidelity of the reconstructed images compared to the original training data. Without metrics like pixel-wise accuracy, structural similarity index (SSIM), or perceptual metrics, it's difficult to objectively evaluate the success of the reconstruction.

The paper also do not provide clear details about the experimental setup like details about the models, dropout rates and so on, and do not discuss details about how successful the attack can be for different types of models and architecture. For example, the paper does not specify the exact CNN architectures used (number of layers, filter sizes, etc.), the optimization algorithms, learning rates, batch sizes, or dropout rates, making it difficult to reproduce the results or assess the generality of the approach. Furthermore, the paper does not discuss how the attack performs on different model architectures, such as ResNets or Transformers, which could reveal the robustness of the proposed method.

The paper may benefit more from detailed discussion about which loss is more important to the reconstruction attack. The paper uses a combination of losses, but does not provide a clear analysis of the contribution of each loss term to the final reconstruction quality. It is unclear if all losses are equally important or if some are more critical than others.

### Questions
Under what conditions which the attacks more successful versus not?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors present a technique called Training-Like Data Reconstruction (TLDR) which can essentially create samples which are similar to the data which a neural network based classifier was trained on. Their technique is based on learning a generative model which can take in label encodings and produce outputs in the image space by using up-convolutions. The signal for training the generator comes from the classifier itself. Essentially, the authors come up with a loss function which encourages the generator to produce samples which the pre-trained classifier will classify into the same class as that of the conditional label provided to the generator. The loss function is made up of several regularizations and terms which encourage the generator to produce images which look similar to the training data. Evaluation is done on CNN based classifiers and 4 datasets including Cifar-10 abd MNIST.

### Strengths
The main aim of the paper is quite clear to understand. The authors lay out the techniques they use to design their inversion network and explain the three desired properties they would want their generative model to have quite well. If their generative model is able to produce high confidence samples which have some room for perturbation (i.e some perturbation in the input space do not produce wildly different output distributions by the classifier) and have low gradient norm, then their model has a better likelihood of producing realistic samples.  I also liked their use of vector and matrix conditioning techniques which I believe are useful for generating controlled samples from generative models. The authors also provided a very comprehensive literature review in the space of model inversion based attacks which is well appreciated.

### Weaknesses
The paper suffers from several weaknesses which I believe can be addressed.

Firstly, the experimental evaluation is very limited. The authors only perform evaluation on MNIST, FMNIST, SVHN and CIFAR-10. These are very simple datasets and we do not know if this technique will be applicable to more complex datasets such as Imagenet or Ms-COCO where finegrained details need to be captured. Furthermore, the evaluation lacks a quantitative comparison between the reconstructed images and the original training data. The authors only presented visual samples, which are insufficient to assess the quality of the reconstruction. A more rigorous evaluation would include metrics such as SSIM, PSNR, or FID to provide a quantitative measure of similarity. Also, evaluation was only done on CNN based classifiers and it would be interesting to know if this technique can perform well on more modern architectures like ViTs, which have different inductive biases and may pose unique challenges for the proposed inversion technique.

Another concern I have about the paper is the complexity of the TLDR scheme. In total, there are 9 types of loss functions including KL divergence, Cross entropy, variational losses, feature orthogonality, cosine similarity etc. There is no clear understanding of the impact of each type of loss function and whether they are all necessary. The paper lacks a detailed ablation study to justify the inclusion of each loss term and to understand their individual contributions to the final reconstruction quality. Without such an analysis, it is difficult to assess the necessity of each component and whether a simpler approach could achieve comparable results. The interplay between these losses and their effect on the generator's learning dynamics is also not well understood.

Finally, I am concerned about the quality of the reconstructions themselves. CIFAR-10 is the most complex dataset they perform their evaluation on and many of the samples are hard to parse. The inversion scheme does not capture color / contrast very well and my understanding is that this inversion is only done to get a feel for what the training data was and not to be able to steal confidential training data and reuse it. The lack of high-fidelity reconstructions raises questions about the practical utility of the proposed method. If the reconstructed samples are not sufficiently representative of the original training data, the method's ability to reveal meaningful information about the training set is limited.

### Questions
What exactly is the input to the generator? You discuss four approaches - label, vector, intermediate matrix and vector-matrix conditioning.
Additionally, if you only use vector conditioning, do you simply sample from a Gaussian, softmax it, and then feed this to the Generator?
Also, in Figure 1, the input to the generator seems to be a latent + conditioning vector. What is the source of the latent vector?

What exactly is the cosine similarity between? It says on Line 319 that "cosine similarity between features of generated images i and j". Where are two images coming from?

Typos and grammatical errors

Line 219 has a typo ' a diverse data distributions'

Line 234 - 'we given its simplicity'

Line 255 - for a encoding the label

Line 240 - learnt off of the labels each representative of the separate classes

Other 

Is the claim on Line 256 an observation you made during your research or a previously known fact from the literature? If so, please cite the relevant literature.

Do you think you could use a more powerful generative model i.e diffusion model?

### Soundness
2

### Presentation
2

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
This work introduces a novel approach to reconstruction of training data from ML models using an inversion-based attack. The attack is evaluated on a number of CV benchmark datasets.

### Strengths
The paper is well-motivated, the presentation is mostly on the positive side and mostly well-written.

### Weaknesses
The biggest scientific weakness of this work is its impact. We have previously seen dozens of papers on model inversion and data reconstruction using various techniques ranging from inversion networks (e.g. [1, 2]) to gradient reconstruction ([3,4]). Note that these cover collaborative learning in most cases, as authors have already linked the relevant centralised settings in their related work. There is hardly anything new about the approach proposed here or the results obtained in this work. The datasets used here are the basic toy datasets that have previously been inverted multiple times using the techniques I linked above across a very large number of training settings and model architectures (mostly beyond the basic CNN architectures). While novelty is not the only factor that we are looking for when assessing submissions, I can hardly see any additional insights, unexplored work directions or interesting findings either. Almost everything in this work has previously been studied (e.g. the attack method, the use of priors, combination of multiple reconstruction factors etc.) in great detail and I do not see how the community benefits from this work.

In terms of more addressable concerns I have: the paper is not well-presented given the tight space constraints. With only 9-10 pages, authors should really concentrate on new methods, novel results and discussion. Currently, the introduction (which is in my view really inflated for no particular reason) takes 2 pages. This is not to mention the 2 pages of basic ML vocabulary, where each term has its own paragraph with margins (e.g. you do not need to explain what a cross-entropy loss is at ICLR). This adds up to about 4-5 pages of superfluous content. And given my criticism of the novelty and the impact of the work and its findings, this is exactly where this extra space should have gone - to explore the method in more detail, show novel insights etc. There are also 2 diagrams which I find to be relatively similar and they take about a page as well without adding much to the content (i.e. one would suffice, two are too much). 

While this may not be the comment the authors expected to hear, I would encourage them to concentrate on a) extracting as many novel scientific insights from their method as possible and b) restructuring the work so these results are clear to the reader. This would make the paper useful for the community and acceptable for publication.

### Questions
None.

### Soundness
3

### Presentation
2

### Contribution
1
