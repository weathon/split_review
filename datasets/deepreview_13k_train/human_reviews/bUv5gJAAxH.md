# Relating Implicit Bias and Adversarial Attacks through Intrinsic Dimension

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Despite their impressive performance in classification, neural networks are known to be vulnerable to adversarial attacks. These attacks are small perturbations of the input data designed to fool the model. Naturally, a question arises regarding the potential connection between the architecture, settings, or properties of the model and the nature of the attack. In this work, we aim to shed light on this problem by focusing on the implicit bias of the neural network, which refers to its inherent inclination to favor specific patterns or outcomes. Specifically, we investigate one aspect of the implicit bias, which involves the essential Fourier frequencies required for accurate image classification. We conduct tests to assess the statistical relationship between these frequencies and those necessary for a successful attack. To delve into this relationship, we propose a new method that can uncover non-linear correlations between sets of coordinates, which, in our case, are the aforementioned frequencies. By exploiting the entanglement between intrinsic dimension and correlation, we provide empirical evidence that the network bias in Fourier space and the target frequencies of adversarial attacks are closely tied.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an empirical investigation of the correlation between the 
essential input frequencies required for accuracy of neural network image classifiers, and the frequencies targeted by adversarial attacks. They follow a recent approach by Karantzas et al. in which a Fourier mask is computed for a given input image, and then compared (in the Fourier space) with a mask similarly computed for a successful attack of the image. The authors seek to test their assertion that the network spectral bias determines the nature of successful attacks. Following Karantzas et al., the modulatory masks are computed by applying a Fast Fourier Transform, and then masking with a matrix of traininable parameters between 0 and 1. The result is converted back into an image by taking the real part of the inverse FFT, and then fed to the pretrained classifier to obtain a prediction that is used to train the mask parameters. 

The authors assess the relationships between original images and their successfully attacked counterparts through a test based on intrinsic dimensionality on a vector formed by flattening and concatenating the two masks. They reason that correlation between the two would be revealed by a strong drop in ID, as compared with that of vector in which the coordinates derived from one of the masks. Z-scores are used to test the hypothesis that the drop in ID is significant. The authors then present empirical evidence for their claims based on this test.

### Strengths
S1) The authors' observation that ID collapses when two sets of variables are highly correlated is an interesting. The contrast in ID between the cases of shuffled vs unshuffled variables is a compelling argument for the existence or lack of a correlation effect. 

S2) For the image datasets and learning models considered in the empirical evaluation, the authors have made a good case for regarding the susceptibility of adversarial attack as being revealed by frequency components. The authors further exploit the idea of shuffling to demonstrate the existence of class-specific information in the masks.

S3) The paper presentation is of a high standard: well-organized, well-written, and clear.

### Weaknesses
W1) Among the technical contributions of the paper, the only novel idea is that of testing correlation using intrinsic dimensionality and variable shuffling. In other respects, the authors draw upon the Fourier mask framework of Karantzas et al. for analyzing the robustness of ANNs. 

W2) The authors have not accounted for the potential for bias in their Z-score test. The variance of the ID (and therefore the significance of the Z-score) itself strongly depends on the dimensionality within which it is assessed. Setting a threshold for hypothesis testing that is uniform across all dimensions may not be appropriate here. Estimation of ID also has its own biases that may confound hypothesis testing of this type. Accounting for (and if necessary, adjusting for) dimensional bias would greatly improve both the importance and novelty of the results.

### Questions
Please address the point raised as W2.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The primary objective of the paper is to find a correlation between the frequencies that a hypothesis is attending to correctly classify an image with the frequencies that adversarial attacks take advantage of. The proposal is that if such a correlation exists, then "the network spectral bias determines the nature of the adversarial attacks in the Fourier space".

To this end, the paper first provides a light review of the concept of "implicit bias" and its relationship with Fourier transform of images. The paper then follows to describe the issue of adversarial attacks and the concept of intrinsic dimension of a data set. Next, the methodology of the proposal is described in which a method of Karantzas et al. is used to obtain the aforementioned frequencies. The paper then describes a method for determining the existence of correlation between two sets of data based on the difference between the intrinsic dimension of the concatenation of the two sets with the intrinsic dimension of the concatenation of one of the sets with a random shuffling of the other set. The argument is supported by providing an example of a 2D spiral.

Finally, the paper reports the results of performing the proposed method on CIFAR and ImageNet data sets. The results suggest that the intrinsic dimension of concatenated natural and adversarial frequencies is on average increased by 4 or 5 almost surely when one the natural or adversarial samples is randomized.

### Strengths
### Originality:
The paper is original in its use of topological information to determine correlation between two sets of data.

### Quality:
The paper is well-written for the most parts.

### Clarity:
The language is simple and the paper refrains from using complicated mathematical concepts.

### Significance:
The paper proposes a method for solving the problem of efficient determination of correlation between subsets of $\mathbb{R}^n$ for $n >> 1$. This is a very well-known problem and is a subject of active research.

### Weaknesses
### Minor:
- The use of the Z-test is questionable in this context. While convenient, its applicability relies on the assumption of a known population standard deviation and a normal distribution. Given that the intrinsic dimension is inherently non-negative, a normal distribution is unlikely. The paper should at least acknowledge the limitations of using a Z-test and consider alternatives like a t-test. Furthermore, exploring non-parametric tests or distributions like Poisson/Gamma might be more appropriate for modeling the intrinsic dimension. Even though the issue of the distribution does not appear to be detrimental to the results of the paper, the issues of Z-test should be clearly stated in the paper.

- The experimental setup uses $\epsilon = 0.01$ for $\ell_\infty$ attacks on CIFAR, which deviates from the conventional value of $\frac{8}{255} \approx 0.03$ (refer to https://robustbench.github.io/). This discrepancy should be justified or addressed.

### Major:
- The core proposal lacks rigorous theoretical grounding. The introduced concepts, especially the correlation test, are not formally defined. This makes it challenging to assess the validity and reproducibility of the proposed method. For instance, the paper introduces the concept of "implicit bias" without providing a clear explanation of what it entails or how it relates to the Fourier transform of images. The paper only describes these relations as some "deep connection" without providing any further explanation.

- The literature review inadequately addresses the concept of "implicit bias" and its connection to the Fourier domain. This omission hinders a comprehensive understanding of the paper's theoretical underpinnings. The paper simply assumes that the reader has the required background knowledge.

### Questions
- Please elaborate on the significance of the proposal from the perspective of robustness in machine learning. Specifically, I don't see the significance of providing "empirical evidence that the network bias in Fourier space and the target frequencies of adversarial attacks are closely tied". The literature on this issue is pretty big as evident from a simple search in Google Scholar.

- I don't find the verbal description of the proposed correlation test convincing at all. Even if the concept is sound, no formal statement or expression of the method is present. I cannot see how it is possible to verify the arguments made in the paper in its current form.

### Soundness
1 poor

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The goal of this paper is to explore the connections between implicit bias and the adversarial vulnerability of deep neural networks.

### Strengths
The research topic in this paper is essential for the ML community.

### Weaknesses
The contributions are somewhat limited. In this paper, the authors do not provide sufficient evidence to support their arguments for the strong correlations between implicit bias and adversarial attacks. From Tab.2, the cosine similarity is not sharp, suggesting a weak linear correlation. The authors should present many more results beyond simple cosine similarity to clarify the relationship. For instance, exploring non-linear correlation metrics or conducting adversarial attacks with varying perturbation budgets and observing the impact on the proposed correlation metrics would provide a more comprehensive understanding. Moreover, the important thing is that the authors need to give a clear presentation about why we need to relate the implicit bias and adversarial attack together. What are the practical implications of understanding this relationship? How does it improve our understanding or ability to defend against adversarial attacks?

Then, the proposed method is limited and incompleted in Sec.3.2, which is challenging to apply to practical applications. Specifically, the reliance on knowing the "adversarial class" is problematic. How do we know the adversarial class? Since we usually adopt an untargeted adversarial attack, how do we compute Eq.(1) for adversarial examples? Also, the obtained frequency masks should be explained further. Compared to the model trained with original features, what is the performance if we only consider the mask features of images to train a model? Does training solely on these masked features retain comparable accuracy, suggesting that these features are indeed crucial for classification? Providing quantitative results on the performance of a model trained only on the masked features would strengthen the argument.

Finally, this paper does not propose new methods or strategies on top of their findings. What can we do next after finding the correlations? The paper would be significantly stronger if it offered some concrete directions for future work, such as potential adversarial defense mechanisms based on the identified correlations or novel training strategies that mitigate the impact of implicit bias.

### Questions
Please address all my concerns in the Weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The focus in this paper is on minimum one-norm frequency masks of images with respect to a given neural network classifier.  They are such that if the fast Fourier transform of an image is multiplied pixel-wise by the mask and then the inverse of the fast Fourier transform is applied, the resulting image is assigned the same class by the network as the original image.  The authors propose a technique based on the notion of intrinsic dimension to measure possibly non-linear correlation, and apply it to assess correlation between the frequency masks of images and their adversarial perturbations.  The main result is that some correlation is shown in this way for CIFAR-10 and Imagenette datasets.

### Strengths
The figures in the paper help with understanding.

The authors indicate interesting directions for future work in the last section.

### Weaknesses
The reported decreases in the estimates of intrinsic dimension compared with the randomly shuffled data are relatively small.

One would expect some correlation between the frequency masks of the images and their adversarial perturbations simply because the adversarial noise is small.  I am not sure what beyond that I can conclude from the main result in the paper.

The proposed technique for assessing possibly non-linear correlation makes sense, however this paper shows that it is currently not practical for high-dimensional data, e.g. already for the Imagenette dataset there are computational and reliability issues.

The lack of space between paragraphs makes the paper harder to read, and is contrary to the formatting instructions in the LaTeX template for the conference.

### Questions
What classes do the adversarial attacks used in the paper target, this does not seem to be stated anywhere in the paper?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
