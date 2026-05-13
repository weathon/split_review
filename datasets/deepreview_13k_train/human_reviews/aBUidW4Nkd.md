# Object-Centric Learning with Slot Mixture Module

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Object-centric architectures usually apply a differentiable module to the entire feature map to decompose it into sets of entity representations called slots. Some of these methods structurally resemble clustering algorithms, where the cluster's center in latent space serves as a slot representation. Slot Attention is an example of such a method, acting as a learnable analog of the soft k-means algorithm. Our work employs a learnable clustering method based on the Gaussian Mixture Model. Unlike other approaches, we represent slots not only as centers of clusters but also incorporate information about the distance between clusters and assigned vectors, leading to more expressive slot representations. Our experiments demonstrate that using this approach instead of Slot Attention improves performance in object-centric scenarios, achieving state-of-the-art results in the set property prediction task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a generalization of the Slot Attention approach by Locatello et al. 2020, replacing the k-means algorithm with a Gaussian Mixture Model to improve the expressiveness of the slot representations. In Slot Attention (SA), slot representations are cluster centers, which means that SA is limited by the information contained and represented in these cluster centers, whereas SMM represents slots not only as centers of clusters but also incorporate information about the distance between clusters and assigned vectors. Experiment results on standard benchmark datasets showed improved performance over SA.

### Strengths
The idea presented in this manuscript is quite sound and intuitive. Overall, the manuscript is well-written and easy to digest. Given the growing interest in Slot Attention, this paper comes timely. It proposes a new direction into how object-centric learning via slot attention could be approached without drastically departing from the main concept while achieving better performance.

### Weaknesses
1. There is a typo in Equation 7. The covariance matrix $\Sigma^{\*}$ should be computed based on the updated mean $\mu^{\*}$ and not the original $\mu_{k}$. This is important for the correct calculation of the Gaussian Mixture Model's parameters.

2. The qualitative results could be improved, in my opinion. The images depicted in Figure 2 are quite blurry, especially at the provided resolution of 96x96. This makes it quite difficult to assess whether SMM brings actually any substantial improvements over SA or not. Providing higher quality images, perhaps at 128x128 or 256x256 resolution, would significantly strengthen the manuscript and allow for a more thorough visual comparison.

3. In Figure 2, the images produced from SMM seem quite distorted, particularly for the ClevrTex dataset. These distortions seem more pronounced than those observed in SA reconstructions. Given the increased expressiveness of SMM, one might expect the reconstructions from the learned slots to be more naturally-looking and less prone to such artifacts. It is not entirely clear whether these distortions are primarily due to limitations of the considered Image GPT model or if they indicate that the learned slot representations are not capturing the underlying structure of the data as effectively as they could.

4. Comparing *quantitatively* the attention maps learned by SMM against those learned by SA would have been quite helpful. While Figure 4 provides some insight into the SMM attention maps, a direct side-by-side comparison with SA's attention maps, particularly for more complex image scenes, would allow for a more rigorous evaluation. I am under the impression that for more complex image scenes, the attention maps learned by SA would be more accurate than those learned by SMM due to potentially the high-variance involved in the SMM updates. A quantitative comparison, perhaps using a metric like Intersection over Union (IoU) or a similar measure of overlap between the attention maps and ground truth object masks, could shed more light on this aspect.

### Questions
My main concerns mainly pertain to the quality of the reconstructed images. Any improvements in that aspect would strengthen the manuscript.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an object-centric architecture that is able to decompose the scene into a set of slots, useful for several downstream tasks ranging from image reconstruction, object discovery and property prediction. While the traditional Slot Attention model generates the slots using a learnable k-means clustering, the proposed method clusters the pixels using a learnable version of the gaussian mixture modeling. Concretely, they are using an iterative approach to estimate not only the centroids of the clusters, but also the covariance associated with each component. The resulting model proves to be beneficial compared to the basic Slot Attention architecture, especially in more difficult scenarios such as low resolution or harder datasets.

### Strengths
- The idea of replacing the k-means algorithm with GMM in the slot attention architecture represent an interesting and novel idea. Given that k-means clustering is a particular case of GMM, the resulting method has potential to mimic, and go beyond the capabilities of the slot attention models.
- The method shows improvement on various tasks

### Weaknesses
 - Since k-means is a particular case of the GMM framework (with the GMM allowing for a learnable variance in clusters), a discussion regarding the advantages of going for the more general model should be included. What are some real world scenarios where a gaussian-based method perform better? Specifically, it would be beneficial to elaborate on the scenarios where the added complexity of modeling variance is crucial, and if these scenarios are actually present in the datasets used for evaluation. It is not clear if the datasets used are complex enough to justify the added complexity of the GMM.
- From the results in Appendix, Table 9 the SMM model seems to be more sensitive to then number of iterations compared to the traditional SA. Is this a consequence of the EM algorithm not converging or are there other optimisation issues that causes this phenomena? It is important to investigate if the increased sensitivity to the number of iterations is a consequence of the EM algorithm not converging properly, or if there are other optimization issues at play. This could potentially limit the applicability of the method in scenarios where computational resources are limited.
- As mentioning in Section 3, the SMM differs from SA in 3 aspects: the dot product is replaced by the Gaussian density function; both covariance and mean values are updated in the iterative process and the slot representation is a combination of mean and covariance. It would be insightful to see an ablation study showing the contribution of each one of the changes. Specifically, it would be beneficial to understand the individual impact of each of these changes, as it is not clear if all of them are equally important for the final performance of the model. This would allow for a more focused future research.

### Questions
Please see the Weaknesses section

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a modification of the popular Slot-Attention module in which the slots parameterize a gaussian mixture model, rather than a k-means model (which is how the original SA is typically conceptualized). This allows slots to model both the means and variances (diagonalized covariance) of a latent distribution leading to improved performance on various benchmarks, whilst also allowing "empty" slots to be identified and discarded based on their learned prior mixture weights. The results on various benchmarks are compelling, and the experiments are well-thought out - offering fair comparisons against a vanilla (with implicit gradients) SA baseline, and with some ablations.

### Strengths
The paper is very well-written and easy to follow. The methodology is motivated and presented clearly, and the experiments are thorough.

The idea itself is a fairly simple and elegant extension of SA which has not been explored in the community before. As comparisons with SA are made using implicit gradients (which are commonly used for improved training stability of such models now) on various benchmarks, there are good reasons to expect that the proposed SMM model may replace SA in most use-cases (i.e. it improves upon the _practical_ state of the art in a simple way). Given the considerable popularity of SA and its derivatives, this means the paper should have considerable impact in the Object-Centric Learning community.

The ablations compare SA and SMM against their barebones counter-parts (which are closed to traditional k-Means and GMMs), bolstering the suggestion that the learning of the variance is truly beneficial for learning superior slot representations. In addition to comparing on reconstruction and property identification datasets, they show that the quality of edited images (formed through the manipulation of slots) is superior in the SMM model also, lending further credence to the former claim.

### Weaknesses
Given the emphasis on the method as an improvement over SA across numerous datasets and kinds of OCL tasks, there are no significant weaknesses in the methodology or choice of experiments. That being said, it would have been interesting to see an analysis of the properties of the learned representations (disentanglement, interpolation/extrapolation over generative factors, etc.), but the paper already contains sufficient information to demonstrate the value of SMMs - most notably the Concept Sampling experiments which show steerability at the level of distinct generative factors.

One minor note is that whilst the authors do take care to fairly compare SA against SMMs, it is still possible that SA with $2D$ slots would have been a "fairer" baseline (though, as they rightly point out, this would have been a model with more learnable parameters), in that the capacity in the slots may have been the limiting factor (unlikely); though I suspect the GMMs would still have performed more strongly (as $D$ is not so much the bottleneck, as the form of the distribution the models can capture). It would also be interesting to see how the behaviour of the two models varied as slots became very small, or sparse regularization was applied to the slot representations. Specifically, an analysis of whether SMMs are more or less prone to assigning multiple slots to the same object, or splitting a single object across multiple slots, compared to SA would be valuable.

### Questions
Some minor questions which likely reflect ignorance on the part of the reviewer:
* _Redundant Slots_: Do the authors every observe multiple slots sharing the encoding the same object in a scene, or "competition" between the spatial attention over the CNN Feature maps work strongly enough to prevent this, even in SMMs?
* At the end of page one you write that "We believe... set prediction... requires distinguishing objects from each other"- this reads as if you are saying that set prediction is a better measure of OCL competency than object discovery - I am not sure I follow this argument if so, as it seems that entanglement of representations should be less of a hindrance to object discovery than the production of e.g. object-wise masks?
* At the start of section 3 you state that "GRU [...]. takes current and previous slot representations as input and hidden states" but in Algorithm 1 it seems that the GRU is fed only the means?
* It seems as if figure 1 (left) might differ from Algorithm 1 in a few ways (at least, it was sufficiently unclear that perhaps labelling edges would be worthwhile). Most notably, the L2 difference for computing the covariance matrix is taken after the GRU-mean update in the algorithm, but before in the figure. Additionally, I don't think the MLP / LayerNorm are represented in the figure.

Nitpicks:
* The penultimate sentence of the first paragraph in sec 2.1 is somewhat difficult to parse
* The second paragraph in sec 2.1 - "updating iteration as" needs changing
* In the first paragraph of sec 4.3 you describe the role of the 4th channel in the spatial broadcast decoder as being "for the weights of the mixture component" ; whilst this is correct in the context of the sentence, it is slightly confusing given that the slots are represented with mixture components $$\pi$ within the SMM itself. It might be clearer to talk about the weights of _masks_.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies object-centric learning based on the existing slot attention method. Particularly, it incorporates Gaussian mixture model (GMM) rather than the soft k-means clustering used in the original slot attention to learn better slot representations, achieving promising results on three tasks: image reconstruction, set prediction and object discovery.

### Strengths
1) The paper studies a very important problem of object-centric learning. 

2) The introduced GMM mechanism to learn distinguishable slot representations appears to be more effective than using a single mean vector to represent each slot.

### Weaknesses
1) The key contribution of this paper is the application of GMM mechanism for better slot representation learning, but the improvements are more about the performance in supervised tasks: image reconstruction and set prediction, instead of the more desirable unsupervised object segmentation. This makes the general contribution to be less appealing.

2) In page 2, the claimed Contributions (2) and (3) are not very meaningful, or at least both can be combined, because both sentences describe the experimental results.

3) In Equations (1)(2), it's suggested to use math symbols instead of English words. It’s also suggested to use bold symbols to represent vectors. 

4) In page 4, it is unclear how the function f_theta(x, u, diag) works. Obviously, the input has three elements instead of two as described in the text "R^{NxD} x R^{KxD} -> R^{NxK}". More details should be provided because this is the primary technique contribution of this paper.

5) In Section 4.3, for the experiments of object discovery, the dataset(ClevrTex) is a bit too simple and the evaluation metric ARI is actually not suitable as well because the scores can easily achieve perfect numbers. It is advised to evaluate on more complex (real-world) datasets and use additional metrics such as AP scores, as also pointed out in the paper "Promising or elusive? unsupervised object segmentation from real-world single images, NeurIPS 2022". 

6) In Section 5 “Related Works”, in the field of object-centric learning, recently, there are a number of works using pretrained feature representations to discovery objects, such as DINOSAUR (Bridging the Gap to Real-World Object-Centric Learning, ICLR 2023), Odin (Object discovery and representation networks, ECCV 2022), and CutLER (Cut and Learn for Unsupervised Object Detection and Instance Segmentation, CVPR 2023). They should be discussed appropriately. 

More other related works should be discussed as well, including (1) Invariant Slot Attention: Object Discovery with Slot-Centric Reference Frames, ICML 2023, (2) Spotlight Attention: Robust Object-Centric Learning With a Spatial Locality Prior, arxiv 2023.

To sum up, the paper can be further improved in the following aspects: 1) a better presentation about the technique parts, 2) more concrete experiments to demonstrate better performance in object discovery, 3) discussions about more related and recent works in the field of object-centric learning.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
