# Fully Hyperbolic Convolutional Neural Networks for Computer Vision

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Real-world visual data exhibit intrinsic hierarchical structures that can be represented effectively in hyperbolic spaces. Hyperbolic neural networks (HNNs) are a promising approach for learning feature representations in such spaces. However, current HNNs in computer vision rely on Euclidean backbones and only project features to the hyperbolic space in the task heads, limiting their ability to fully leverage the benefits of hyperbolic geometry. To address this, we present HCNN, a fully hyperbolic convolutional neural network (CNN) designed for computer vision tasks. Based on the Lorentz model, we generalize fundamental components of CNNs and propose novel formulations of the convolutional layer, batch normalization, and multinomial logistic regression. {Experiments on standard vision tasks demonstrate the promising performance of our HCNN framework in both hybrid and fully hyperbolic settings.} Overall, we believe our contributions provide a foundation for developing more powerful HNNs that can better represent complex structures found in image data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes layers for neural networks that operate with hyperbolic features, instead of the standard Euclidean vector features. The paper presents Convolution layers, Batch-normalization, activation function, skip connections and formula for hyperbolic decision boundaries and logits. The hyperbolic features are describe via a Lorentz model, which, compared to the Poincare model, had improved numerical stability and convenient closed form expressions for certain operations. The paper then experimentally validates the soundness of their approach in comparison to an Euclidean baseline (same architecture otherwise) and hybrid adaptions that combine Euclidean layers with hyperbolic layers. The results show a modest improvement in performance (though might not be significant), and increase robustness against adversarial attacks. With VAE experiments the authors show improved reconstruction metrics as well as a qualitatively nicer organization of the latent space.

### Strengths
* Although the first part of the methodology section makes too much use of references to the appendix, it is generally clearly written and accessible.
* The authors provide answers to a so-far unaddressed problem (will the use of hyperbolic representations be useful beyond just as an embedding space, but instead use throughout the network)
* The paper is self-contained and is accompanied with code

### Weaknesses
1. I find the evidence for the actual usefulness of hyperbolic representations not convincing, in contrast to what the authors present in the abstract and introduction by saying things like "demonstrate the superiority of our HCNN framework". This is not to downplay the results, I still think it is valuable that these original approaches are developed and explored, however, I think some conclusions could be nuanced and perhaps more precisely formulate. Which brings me to the next item
2. It is not always clear what the hypotheses are. It seems like it is "just interesting" to try and build a fully hyperbolic network, without clearly specifying why this would be useful. In particular, the experiments should be accompanied with clear hypotheses of what is expected (why would the Lorentz model be better than the Poincare model if both are isometric representations of the same thing? Why would one expect HE or H model be better compared to the other? Why would the H model be more robust to adversarial attacks?). It would help if the experiments are more clearly motivated, and explain to what questions these experiments provide answers
3. The results, in particular in Table 1, all look the same to me. Almost all results lie within each others uncertainty margins and hence drawing conclusions based on these results is dubious, especially if they as strongly state as on some instances in the paper.
4. It would be great if some very narrowly defined experiments could be defined to test for desirable properties of the network (if this is possible). Because, the performances are all so close to each other which I think has to do with the fact that almost any neural network can get great results if you engineer it well enough, even if the code contains bugs or design flaws! However, in order to define such experiments one first has to clearly specify what unique properties are obtained by the HCNNs, which I couldn't really get from the paper, nor did I find concrete research questions that are being addressed. 
5. In the Lorentz model section, Figure 4 is reference. It is not nice to refer to a figure which isn't even included in the document. Moreover, the proper way of refering to figures in order of appearance (e.g. first refer to figure 1, then 2 then 3 etc. Not starting with fig 4). I think if this figure is that important it should be included in the main body. Moreover, it would have been nice to include the appendix in the main pdf, not as a separate document.

### Questions
1. The contributions state "superior performance" without specifying relative to what? Regardless of the comparison, this statement should be nuanced given the discussion above.
2. Page 3, on the Lorentz model. What is "the upper sheet" and what is meant with a "two-sheeted hyperboloid"?
3. In Equation 1 it says $x_t > 0$. Is this because $x_t \geq \sqrt{-1/K}$, and if so, why not specify that instead?
4. Section 4.1 Formalization of the convolution layer... It says "an affine transformation between a linearized kernel and a ..." an affine transformation is a transformation of something, not between two things right? One could say the transformation of a vector is parametrized by a kernel (and a bias), or am I misunderstanding something here?
4. On the same note, equation 3: The definition of LFC seems essential to me, why is it hidden in the appendix and not the main body? This layer is the main work-horse of the neural network, I imagine.
5. Next, "the correct local connectivity is established", what does that mean?
6. Equation 5, why are there additional | | (vertical bars). I count three of them on each side. Two for the norm, which makes sense, but then another outside of it. Please remove it unless there is a particular reason for it.
7. Regarding the Multinomial Logistic Regression. Is this common? I thought that usually the outputs are parametrized as multi-class Bernoullis with probabilities obtained by soft-max, not channel-wise exponentials. I.e., typically one considers mutually exclusive classes, no? Does there exists a construction for hyperbolic soft-max?
8. In 4.4 you mention "... provides best empirical performance", that is nice. But what is theoretical lost with the approach of simply adding the spatial parts? Is this mathematically allowed? It feels like a hack that could theoretically break certain properties of the network (not sure about this though). I suppose since addition is not defined you need to define an alternative, and this one seems as good as anything, but until this point the motivation has been primarily the idea of parallel transport and Frechet mean type "additions".
9. In section 5.1 you write "replace only the resnet encoder blocks with the highest hyperbolicity", what is "hyperbolicity? What is $\delta_{rel}$, and why would different blocks have different hyperbolicity? Many details are missing here.
10. Also, when working with hybrid models, how does one convert a hyperbolic representation to an Euclidean one? 
11. Main result section: "This suggests that the Lorentz model is better suited for HNNs than the Poincaré model", was this expected, why or why not?
12. It says the Hybrid Poincaré model is inferior to the Euclidean case. But isn't this also the case for the Hybrid Loretnz model on Cifar-10, and for the other tasks the difference seems not significant. As stated in the limitations sections above, I think the results could be more critically assessed and conclusions should be nuanced at certain locations. I might of course be mistaken in my analyses, in which case it means the paper could improve still a bit in terms of presentation and discussion of the results :)
13. Regarding robustness experiments. Why is this a relevant experiment?
14. Just above the conclusion "As these structures cannot be found for the hybrid model, ... little impact ..." I do not understand this sentence, could this be clarified? Thank you!

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the  authors propose the first fully hyperbolic convolutional neural network encoder in computer vision. In particular, the authors introduce Lorentzian formulations of the 2D convolutional layer, batch normalization, and multinomial logistic regression for constructing the fully hyperbolic convolutional neural network. Extensive experiments show that the proposed method is better than existing hybrid hyperbolic convolutional neural network.

### Strengths
1. The paper introduced the Lorentzian formulations of the 2D convolutional layer, batch normalization, and multinomial logistic regression which are new in the literature of hyperbolic neural networks.

2. The authors conducted extensive experiments (image classification, image generation) to demonstrate the effectiveness of the proposed HCNN Lorentz.

### Weaknesses
1. Across all the experiments, the improvement of the proposed HCNN Lorentz/HECNN Lorentz over the standard Euclidean neural network is usually small (65.96 vs. 65.19 on Tiny-ImageNet), so it is not clear what is the practical advantage of the proposed method over standard Euclidean neural network. The reported improvements, while statistically significant, do not demonstrate a clear practical advantage in terms of raw performance gains. The magnitude of the improvement is not substantial enough to justify the increased complexity and computational cost of the hyperbolic approach, especially when considering the potential for optimization of standard Euclidean networks.

2. There is a lack of in-depth analysis of the experimental results. For example, the results show that HECNN is the best when the embedding dimension is low. However, the reason of such an improvement is not clear. Similarly for the image generation task. The paper does not provide sufficient analysis to explain why the hyperbolic models perform better under specific conditions. For instance, the claim that HECNN excels at lower embedding dimensions lacks a mechanistic explanation, and the image generation results are not thoroughly analyzed to understand the underlying factors contributing to the observed performance. The lack of ablation studies further hinders the understanding of the contribution of different components of the proposed method.

3. It is known that hyperbolic space is well suited for hierarchical dataset, however, none of the experiments clearly demonstrate this. The experiments do not explicitly leverage the hierarchical nature of the datasets. While the datasets may contain implicit hierarchies, the experiments do not provide a clear demonstration of how the hyperbolic space is advantageous for capturing and exploiting these hierarchical relationships. The paper would benefit from experiments that specifically target hierarchical data or explicitly measure the model's ability to capture hierarchical structures.

### Questions
1. The authors show that fully  hyperbolic neural networks is better than the hybrid version, however, would fully  hyperbolic neural networks incur more parameters than the hybrid version? Also, how about the time complexity comparison？

2. It is not clear what is the real difference made by Lorentzian convolutional layer compared with the standard convolutional layer, more analysis and visualizations are needed to understand the real benefits of the proposed approaches.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a fully hyperbolic convolutional network based on the Lorentz model of hyperbolic geometry. Lorentz formulations of Euclidean operations and extensions from the Poincare reformulations of operations such as MLR, FC, and Concat are presented. A series of networks are presented and evaluated in classification tasks, under adversarial attacks and reconstruction tasks. \

Contributions:
Fully Hyperbolic convolutional neural network outperforming Poincare alternatives. \
 
Reformulation of core operations of convolutional neural networks for the Lorentz model. \
 
Lorentz batch normalization is proposed based on centroid. \
 
Lorentz residual and activation functions are proposed based on space-time vector decomposition. \

### Strengths
Many of the reformulations are sensible and follow well-established reformulations of hyperbolic deep learning that are widely applicable in hyperbolic deep learning in Lorentz models. \
 
A fully Lorentz formulation of convolutional networks is missing in the hyperbolic deep learning field and is likely to be an essential component given the improved stability of such models of hyperbolic space. Hence, this work presents a good addition to the literature. \
 
Using Lorentzian centroid in the normalization is sensible and alleviates many of the computation restrictions of the frechet mean on the Poincare model. This normalization scheme seems reasonable and computationally efficient (more empirical studies to show performance would be a nice addition). \
 
The experimentation demonstrates good performance increases under fully Lorentz models, although this could be expanded. \
 
The work for the most part is well written and nicely organized. \

### Weaknesses
The claims of novelty regarding the first fully hyperbolic and first hybrid CNN for vision tasks do not hold true, you do not cite, nor address the work [1]. Additionally, you reference and discuss a survey of hyperbolic deep learning for vision which contains a significant number of hybrid architectures for vision [2].

The same issue holds true for batch-normalization regarding missing literature, where [1] also presented a method that does not rely on frechet mean, however, your method is the first to my knowledge to operate in the Lorentz model via such a method. 

The experimental ablations and sensitivity are extremely limited, for example, I would expect at the least to see experiments analyzing their performance with and with the batch norm, as there exist many works that suggest batch norm is not necessary [2]. In addition, further analysis into each component, and architectural setting would be a useful insight for those wanting to utilize this work, i.e. initialisations, and curvatures. Specifically, an ablation study isolating the impact of the Lorentz batch normalization, Lorentz residual connections, and activation functions would provide a clearer understanding of their individual contributions to the overall performance. It would also be valuable to see how performance varies with different curvature settings, as this is a crucial parameter in hyperbolic models.

No comparison is made to existing hyperbolic CNN operations i.e. Hyperbolic neural networks ++ [2], and Poincare Resnet [1]. Although not operating in the same hyperbolic model which is notably more unstable, a comparison would help demonstrate the benefits of your proposal. While acknowledging the instability of the Poincare model, a comparative analysis, even if limited, against these established methods would significantly strengthen the paper's contributions and provide a clearer picture of the advantages of the proposed Lorentz-based approach. This could involve evaluating performance on a common dataset or task, or at least a discussion of the expected differences in behavior and performance.

You mention that alternative residual connection methods perform worse, however no results are shown for this analysis, these missing experimentation (even if placed in the supplementary) would provide a more compelling analysis. In addition, a comparison to the Poincare midpoint [1] could be made given the Lorentz model is isometric to Poincare. Specifically, the paper should include a table or figure directly comparing the performance of the proposed Lorentz residual connection method against viable alternatives, including the Poincare midpoint method. This would provide empirical evidence to support the claim of superiority.

The choice of FID is a debated metric, it has been shown that this metric does not appropriately represent the quality of generations [3]. It would be nice to see a series of the generations to compare human perception of the generations. Furthermore, exploring alternative metrics such as Inception Score (IS) or Kernel Inception Distance (KID) could offer a more comprehensive evaluation of the generative model's performance.

You refer to the benefit of capturing hierarchies, yet your empirical studies do not support /compare the capturing of hierarchies of any kind to support this claim. The paper should include experiments or analyses that specifically investigate the model's ability to capture hierarchical relationships in the data. This could involve visualizing the learned representations at different layers, or comparing the model's performance on datasets with varying degrees of hierarchical structure.

### Questions
Do you observe any need for hyperbolic non-linear activation functions given that hyperbolic networks are inherently non-linear? Some works in Poincare ball suggest that it's not essential but marginally improves performance. \
 
You interchangeably reference Hybrid Lorentz as your own work and also reference (Nagano et al., 2019), can you define how yours differs? \
 
In the re-scaling procedure, you assume that the variance direction is along the geodesic intersecting the origin, however, this may not be the case, therefore is not an accurate formulation. Can you elaborate if I have mis-understood. \
 
Can you expand on the residual connection and activation section, currently it is unclear how the time and space components (dimensions of the point) can be added without the issues that arise in hyperbolic space? You suggest that the space component lies in Euclidean space, however simply decomposing the hyperbolic vector based of the first dimension to achieve this space and time component does not align to conventional works. I would be grateful if you could elaborate. \

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
