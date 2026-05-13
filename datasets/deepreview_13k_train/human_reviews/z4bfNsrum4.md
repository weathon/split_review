# Decoding Generalization from Memorization in Deep Neural Networks

- Decision: Reject
- Scores: 1, 3, 6, 3, 6

## Abstract
Overparameterized Deep Neural Networks that generalize well have been key to the dramatic success of Deep Learning in recent years. The reasons for their remarkable ability to generalize are not well understood yet. It has also been known that deep networks possess the ability to memorize training data, as evidenced by perfect or high training accuracies on models trained with corrupted data that have class labels shuffled to varying degrees. Concomitantly, such models are known to generalize poorly, i.e. they suffer from poor test accuracies, due to which it is thought that the act of memorizing substantially degrades the ability to generalize. It has, however, been unclear why the poor generalization that accompanies such memorization, comes about. One possibility is that in the process of training with corrupted data, the layers of the network irretrievably re-organize their representations in a manner that makes generalization difficult. The other possibility is that the network retains significant ability to generalize, but the trained network somehow “chooses” to readout in a manner that is detrimental to generalization. Here, we provide evidence for the latter possibility by demonstrating, empirically, that such models possess information in their representations for substantially improved generalization, even in the face of memorization. Furthermore, such generalization abilities can be easily decoded from the internals of the trained model, and we build a technique to do so from the outputs of specific layers of the network. We demonstrate results on multiple models trained with a number of standard datasets.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper investigates the generalization and memorization phenomena in training overparameterized models with the presence of label noise.  The authors propose MASC, which matches the sample representation angle with each class's representation primary subspace to determine the sample's possible true class. And they state the method can decouple generalization from overfitted network learned from noisy labels.

### Strengths
Very comprehensive experiments.

### Weaknesses
1. Lack of literature: First, the paper lacks related works that don't provide pictures of previous work, the discussion of previous work only appears in the first paragraph of the introduction and most papers are focused on experiments. While there are many theoretical papers trying to understand the problem[1][2].
2. Novelty: The entire Sec.3 tries to convey the idea: that the top component of the corrupted model still contains the class information to some degree. That is not a surprise since [1][2] both indicate that the model first learns the primary eigenspace that contains the correct label information and only learns and memorizes the label noise slowly in the later stage. The proposed method, which tries to cut off the representation space and only keep the main component using PCA, is not that novel because it is also the top eigenspace. Although learning the label noise reduces the energy of the clean label subspace that was learned at the beginning of training, it is not a surprise that the top eigenspace still contains meaningful information.
3. Novelty: Sec.4 tries to convey the idea: that the MASC built on a corrupted model using the correct label is a good classifier to reflect the true class distribution. However, the MASC is just a clustering algorithm, where we use the PCA to get a class vector and then use angle (cosine similarity) to cluster the example. It even somehow works with the original picture. Since the model already established some representation while learning the clean space, it is expected that it can perform well.

4. Writing: The paper is hard to read and follow due to its dense language, complex sentence structures, and grammar errors.  For example, ln 76-96 has multiple dense complex sentences and creates a hinge for readers to understand the main contribution. Ln 304-318 are also hard to follow.  The Methodology part only verbally describes the algorithm as well as the terminology part, it took me much longer time to understand the algorithm. For grammar errors, ln 305 we wanted to -> want, etc. Also, the table elements are not well separated in Table 1, Fig 1,2,3 exceeds the page margin.

### Questions
See weakness.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to investigate the sometimes confusing relationship between neural network generalization and memorization. To this end, the authors propose a method of analysis they call Minimum  Angle Subspace Classifier (MASC) which is a kind of combination between nearest neighbour classifier and a dimensional reduction method: it's a sort-of nearest subspace classifier with distance defined via the angle. Using MASC as their probe they find that the internal representations of the neural networks are able to generalize significantly better than the neural networks themselves.

### Strengths
- Understanding the relationship between generalization and memorization is an important and worthy area of study. 
- Good empirical breadth, with the analysis being applied across 5 standard datasets and three different architectures.
- The authors seem reasonably well versed in at least some of the vast literature on the topic of memorization and generalization.

### Weaknesses
 - I believe there is a methodological issue with the MASC based analysis. The original neural networks are trained to either 500 epochs or 99% - 100% percent accuracy on the training set. This means that the models are likely to be overfit on the training data, especially when training with corrupted data. This may well be the intention of the authors, but it has implications for their conclusions. In their analysis, the authors take a representation drawn from different layers in the architecture and build an alternate classifier on that representation. If the classifier is sufficiently regularized (which their MASC appears to be in at least some cases) and the representation still possesses sufficient variability across the input examples (i.e. the input data points are not collapsed on one-another), then it's not surprising that the MASC classifier is able to exceed the unregularized and overfit neural network classifier. 

- There is insufficient analysis of the properties of the MASC as an experimental probe. The degree to which the MASC is regularized is a very important property for the interpretation of the results. This aspect of the MASC is only sparingly discussed mainly in the appendix and it's unclear how this property globally impacts the conclusions of the paper. 

- There is a largely undiscussed lack of consistency across empirical results. The authors present a healthy breadth of experiments but across the main findings presented in Figs, 1, 2 and 3, the authors mainly focus on the MLP experiments and to some extent the CNN results. They largely neglect to incorporate the AlexNet results into their narrative. This is understandable, because these are often inconsistent with the pattern of results across the other datasets and architectures, but it leaves the reader questioning the generality of the stated findings.

- A very important baseline or control is missing. The MASC needs to be applied to a randomly initialized model (for each architecture). My interpretation of section 4 is that the authors are claiming that the generalization observed using their MASC (on the true uncorrupted training data) compared to the original neural network prediction is revealing hidden but learned generalization ability of the internal representation of the neural network. But this isn't necessarily so. The MASC classifier on a random projection of the input could potentially do just as well. Indeed it seems that as the level of corruption increases,  the dimensionality of the embedding is the most important determiner of MASC performance. This would likely also be predicted for a random embedding with a sufficiently regularized classifier. 

- The paper occasionally slides into nearly nonsensical rhetoric. For example: in line 76 the authors write: "We ask, why it is that in models trained with shuffled labels do we have poor generalization accompanying perfect / high training accuracy." The obvious answer is: "because there is little or no common structure between the training set and the test set on which generalization is evaluated. Most of the paper is more lucid than this would imply, but statements like this weakens the overall strength of the message of the paper.

Clarity: The paper is readable though its clarity would benefit significantly from more formal, mathematical definitions and descriptions of the different empirical probes that are used. It took me a while to decipher what the training set was for the "MASC Accuracy on Corrupted Training".

### Questions
I would like the authors to respond to points I listed under weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors probe the representations of DNNs trained with noised labels.

To test the hypothesis that intermediate representations "generalize" even if the output layer doesn't, the authors identify class-conditional subspaces in the hidden representations of each layer via PCA. They then show that these subspaces can be used to classify test points by simply choosing the subspace onto whose projection the angular distance to the point is minimal. They then show that such a classifier often has better test performance on models trained with noised labels, confirming the hypothesis.  

These subspaces are themselves constructed out of noised labels, but the authors also test the case where they are not, also finding consistent better test performance.

The authors present these findings as additional evidence of the complex interplays between generalization and memorization.

### Strengths
The paper investigates important questions in a novel way. It is well written and the claims are mostly backed by evidence.

### Weaknesses
The paper's main weakness is a fairly important lack of situating itself with respect to prior work. A number of papers have probed intermediate layers and latent representations of DNNs [e.g. 2,3], in an attempt to understand this very memorization-vs-generalization debate. It does feel to me that many of the claims made in this paper are obvious in light of this literature. While the specific empirical investigation done here is novel to me, the conclusions drawn by the authors are not.   It is hard to resist thinking that most readers familiar with the literature could have easily predicted the outcomes of these experiments. While validating known hypotheses is fundamental to science, it does feel like the contribution here is limited to that.

The paper's other main weakness is it's lack of scale (and proper analysis of scale), and the oddly poor performance of some models. I know this is an easy criticism to throw, but the largest model shown in the paper has 40M parameters and something like 18% test accuracy on an unperturbed training set. In contrast, a ResNet-152 from 2015 (He et al.) has a similary number of parameters and ~80% accuracy on the full ImageNet dataset, and an 11M parameter DenseNet (Abai et al) gets 60% accuracy on TinyImageNet.

> As a result, memorization is generally considered antithetical to generalization  

I see this written a lot, but this is a demonstrably false narrative. I think it's been the pretty clear narrative even since the 2016/17 works of Zhang et al & Arpit et al (in their _Main Contributions_ section, they write: _"DNNs learn simple patterns first, before memorizing, [..] in other words, DNN optimization is content-aware, taking advantage of patterns shared by multiple training examples"_) that generalization and memorization are **not at odds**; i.e. deep models do both but we don't understand how much of which and to what degree they contribute to test performance. It's also been fairly clear since ~2017, including the work of Arpit et al, that DNNs learn in some kind of hierarchical order (or frequency-based, DNNs learn lower frequencies first [1]), even in the presence of label noise. The latter already suggests that intermediate representations should be amenable to have _general_ information extracted from them, even if the last classifying later "overfits".

### Questions
I can't think of prior work having done this exact experiment, but it is very much in line with all that I know from the whole memorization vs generalization literature; and in that sense I come out of having read the paper with the feeling of not having learned anything. What is the one thing the authors think we can learn from this paper that's not in existing papers?

Coming back to scale, the effect is pretty minimal on AlexNet+TinyImagenet. Since this is the most "large-scale representative" of the tasks, it definitely begs the question of what actually happens at scale. Without training on all of ImageNet with a modern model, I wonder if something could be learned by repeating the experiment with e.g. 2x and 0.5x the number of parameters.

Section 5 constructs subspaces based on noisy labels for models without noisy labels (so presumably "no memorization"), and shows that this can be used with MACS to correctly retrieve the noised labels in some layer in most cases. I really fail to see how this "this supports the idea that memorization can not only coexist with generalization, but that in some cases memorization can be accompanied by superior generalization." I suspect this just shows that the subspace is expressive enough to separate somewhat arbitrary points, which I suspect can be explained by the occasionally high number of principal components. Conversely this may say nothing about generalization, since the underlying space is presumably a generalizing one, it just says that the overarching space of the subspace is also expressive enough to separate arbitrary points. We know this is the case from a long history of probing overparameterized deep neural networks. I would like the authors to expand on Section 5 and explain why they think it shows what they claim it shows.

Some suggested improvements:
- Table 1: use space between groups of 3 digits for large numbers
- Adam is a method with a paper that should be cited
- Figure 1: increase label size, and generally reconsider the zoom level of the plot, details are hard to see. Another tip is to hide the shared axes' labels to create more space for the figure (IIRC using pyplot just using `sharey=True` should accomplish this)
- Figure 2 should also have lines for the "Minimum Angle Subspace Classifier (MASC) Accuracy on Corrupted Training" lines of Figure 1, otherwise I don't see how to compare the two properly (and support the claim that "accuracies on the true training labels, as well as the test set are dramatically better here than with the experiments where subspaces were determined for the corrupted training data")
- The abstract is very long and I recommend being much much more concise. Again, what is the one thing the authors think we can learn from this paper that's not in existing papers?

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
3

### Summary
First, the paper presents experiments where the model attains high training accuracy but low test accuracy, the classical overfitting story. Then, they show that by using the intermediate activation of the neural network, they can get reasonable generalization performance beyond the naive test accuracy. The higher-level claim is that the generalization ability is not lost during the overfitting process, that ability can be "decoded" via techniques like MASC.

### Strengths
The idea that overfitting happens in the later layer of the network, though not new, is interesting in itself. The authors present a concrete technique how to extract the generalization performance from those activations.

### Weaknesses
First of all, the technique discussed in the paper is not a practical one -- they are not intended for people to use in practice to replace more careful network architecture design, hyperparameter tuning, data curation, etc.

So the paper has to be viewed from a scientific perspective.
- Novelty: the idea of using unsupervised technique on activation to get good generalization performance is not new. It roots in the rich literature of representation learning, which are not adequately discussed in the paper. Specifically, techniques like clustering or dimensionality reduction on intermediate activations have been explored for various tasks, and the paper doesn't sufficiently differentiate its approach from these existing methods. The lack of a clear comparison makes it difficult to assess the true novelty of the proposed method.
- Scientific rigor: The phenomenon isn't as robust as the experiment suggests, there are several places in Figure 1 and 2 where the MASC accuracy is not higher than test accuracy.  Especially on ImageNet. This raises concerns about the consistency and reliability of the observed effect. The paper should provide a more thorough analysis of the cases where MASC fails to outperform the standard test accuracy, including potential reasons for these failures.
- Experiment setting: It's sometime a bad criticism to say that the authors didn't run large-scale experiments. But in this case, they propose a phenomenon that's intended to hold a cross a wide range of scales, but the largest neural network they implementated is AlexNet. Even under academic budget, the author would need to show results on ResNet (from 2015). Let alone more recent models like MobileNet and ViT to be convincing. The limited scale of the experiments makes it difficult to generalize the findings to more complex and widely used architectures. The paper needs to demonstrate that the observed phenomenon is not an artifact of the specific models and datasets used.

### Questions
Given that no mild-scale experiment were presented, how does the phenomenon generalize to large scale neural networks? With ResNet50 and careful training, we can get high accuracy on CIFAR100 and ImageNet.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provide a deeper dive into the representation learning under generalization (learning with clean labels) or memorization (fitting to corrupted labels) for image classification models. The results show that even when heavily memorizing randomly corrupted labels, the intermediate layer representations could still provide non-trivial classification capabilities when probed with a simple classifier without using any extra label information. Furthermore, if the correct labels are provided post-hoc to build such probe, non-trivial accuracy can be obtained even when the original model was trained with completely random labels. This shows that even when fitting to completely random labels, the models are still learning useful visual representations for the input image, instead of arbitrarily wiring the network to build a lookup table for memorizing the random labels. This paper further show that a similar method can be used to build a "probe" with high accuracy for random labels when the original model was trained with correct labels.

### Strengths
This paper studies the interesting problem of representation building when the neural network memorizes corrupted training labels. Especially when learning under completely random noises, it was unclear if the neural networks simply ignore the underlying visual patterns and build an arbitrary lookup table for those random labels, or do they still learn useful visual representations. The experiments to study this question is clearly formulated. The conclusions are supported with experiments on multiple datasets and model architectures.

### Weaknesses
1. The presentation of the paper could be improved, especially the experiment results and figures. It is a bit difficult to digest or find the most relevant information from their figures. For example, Figure 1, 2, 3 each occupies a full page, and each contains 30 sub-panels. Even if the authors would like to include all the results in the main paper, I would still recommend choosing a subset of panels that can clearly support the conclusions and highlight them (e.g. making them bigger and putting them in a separate figure), or even consider alternative visualization to present a summary of the information contained in each of the 30 panels.

2. While the message in this paper is clear, it seems a bit specialized to the specifically chosen Minimum Angle Subspace Classifier (MASC). It is a bit unclear if it is the robustness of this classifier that enabled such phenomenon or does it hold for other simple classifiers as well. I think it is still interesting if it only holds for MASC, but including studies with other simple classifiers would make the results more comprehensive.

3. It looks like the conclusion in this paper is biasing towards that the models learn similar representation in both memorization and generalization model, because the learned representation can be turned to do memorization or generalization when the corrupted or true labels are revealed after the representation learning. If this is indeed the message, it would be great if the paper could have some way to measure the representation similarity, which would not only further confirm the message, but might also be able to allow us to do comparative studies such as, do Convolutional Nets have a stronger bias towards learning similar representations than MLPs?

4. (Minor) The MASC algorithm needs to use labels. I believe it is using the same labels as model training (e.g. corrupted labels in most cases) based on the comparison results in Section 4. It would be better if the paper could clearly clarify this in the methodology presentation (e.g. Section 2).

### Questions
See "Weakness" above.

### Soundness
3

### Presentation
2

### Contribution
3
