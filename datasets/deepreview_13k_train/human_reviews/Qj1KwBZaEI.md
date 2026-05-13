# Intrinsic Dimension Correlation: uncovering nonlinear connections in multimodal representations

- Decision: Accept
- Scores: 8, 5, 6, 8, 8

## Abstract
\freefootnote{\vspace{-0.3cm}\\ Correspondence to: \href{mailto:lorenzo.basile@phd.units.it}{lorenzo.basile@phd.units.it}. However, these correlations often exhibit a high-dimensional and strongly nonlinear nature, which makes them challenging to detect using standard methods. 
 This paper exploits the entanglement between intrinsic dimensionality and correlation to propose a metric that quantifies the (potentially nonlinear) correlation between high-dimensional manifolds. We first validate our method on synthetic data in controlled environments, showcasing its advantages and drawbacks compared to existing techniques. Subsequently, we extend our analysis to large-scale applications in neural network representations. Specifically, we focus on latent representations of multimodal data, uncovering clear correlations between paired visual and textual embeddings, whereas existing methods struggle significantly in detecting similarity. Our results indicate the presence of highly nonlinear correlation patterns between latent manifolds.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new metric, Intrinsic Dimension Correlation (IdCor), designed to detect nonlinear correlations between features describing data points, in particular the latent representations output by deep networks. IdCor leverages "intrinsic dimension" (Id) as a proxy for information and estimates correlation using a normalized mutual information approach. By quantifying correlation based on the minimal number of variables required to represent data, IdCor aims to provide insight into nonlinear dependencies that standard methods may not achieve. The authors test their method on a variety of synthetic datasets and deep neural networks, including multimodal models.

### Strengths
- IdCor introduces an interesting approach of measuring nonlinear correlations by combining the notions of mutual information and intrinsic dimensionality.

-  The paper conducts experiments using both synthetic and real-world datasets.

- The paper is well-written and organized.

- Interesting discussion on latent space alignment.

### Weaknesses
__Choice of Id estimator:__ Not enough reasons are given for the choice of using TwoNN. Given that this is the main point of the paper, benchmarking it against other more popular methods for Id estimation would be strongly advised, e.g., Levina & Bickel's. Moreover, through lines 179--185, the authors list several references that estimated the Id found in the representations output by deep networks. I believe it would be helpful to list which methods those authors used for computing Id and possibly using the same ones to compare against using TwoNN. It is not clear why TwoNN is preferred over other methods, especially given its known sensitivity to data density variations. A more thorough justification, including a comparison with other estimators like the MLE estimator by Levina and Bickel, is needed to establish the robustness of the proposed IdCor metric.

__Id assumptions:__ The proposed measure IdCor assumes that the intrinsic dimensionality is roughly constant throughout the data. That is unlikely to be true for most real-world data (in line with what the authors point out in lines 312--313). A simple example is one in which we have clustered data but different clusters might have different dimensionalities -- a reasonable assumption if one takes into account that a clustered representation might be clustered precisely due to the fact that different "concepts" may require different topologies. E.g., the dimensionality of the space of images of dogs is likely to much much higher than that of images of soccer balls due to the different symmetries and "directions" of variability (e.g. color) between the two objects encountered in natural scene data. Here are a couple of recent papers that directly consider this possibility and propose solutions for dealing with this dimensional heterogeneity:

[1] Allegra, M., Facco, E., Denti, F., Laio, A., & Mira, A. (2020). "Data segmentation based on the local intrinsic dimension". Scientific reports, 10(1), 16449.

[2] Dyballa, L., Zucker, S., (2023). “IAN: Iterated Adaptive Neighborhoods for manifold learning and dimensionality estimation”, Neural Computation, 35 (3): 453-524. 

The first one is in fact by the same group as that of the TwoNN method. So I would consider both including this limitation in Discussion section, and proposing a way to adapt the IdCor computation that would allow for multiple dimensionalities to be present within the same dataset. (E.g., considering each subset with homogeneous dimension at a time and later aggregating the results somehow seems like a reasonable candidate strategy.) The assumption of a global, uniform intrinsic dimension is a significant limitation that needs to be addressed, especially when dealing with complex, real-world datasets where different regions of the data manifold may exhibit varying dimensionalities. The authors should explore methods for local intrinsic dimension estimation and adapt IdCor to handle such cases.

__Synthetic results:__ I believe the authors jump prematurely into the deep net section without sufficiently exploring the synthetic data first (important, because it provides ground truth). For example: since the data is randomly sampled, how many times has this experiment been repeated. Then, values reported in Table 2 should show the mean and standard. dev. across multiple random seeds, not just one instance. (as far as I understand it, although multiple permutations were considered to compute the p-values, they all came from the same data set, correct?)  How many points are sampled? (Important when estimating dimensionality.) How robust are the results w.r.t. the average sampling density? How is the sampling done? Uniformly or drawn from a Gaussian distribution? (both should be tested) Why not show the results for several values of Id? I think the results with synthetic data can be made considerable more interesting but adding these. These modifications are easy to implement (see [2] for examples), and it would be a much stronger way of empirically testing the robustness of the proposed method. (I would also suggest to move these results into the Results section.) The lack of statistical rigor in the synthetic data experiments, such as reporting only single runs instead of means and standard deviations across multiple trials, significantly undermines the validity of the results. The authors should also investigate the sensitivity of IdCor to the number of sampled points and the sampling distribution.

__Figure 2:__ the points plotted should also be the mean across several different weight initializations of the MLP, with std. dev. shown as error bars.

__Figure 3:__ Authors show that the value of IdCor are high when the same dataset is compared across multiple representations output from networks. I believe it would be important to show that if the dataset is changed, then IdCor should go down considerable (this would work as a sanity check that the method is not simply giving a high correlation between any two high-dimensional datasets). The multimodal results in Table 3 do not help in showing this, since the values produced by IdCor are still the highest (or close to) every case. It is crucial to demonstrate that IdCor is sensitive to changes in the underlying data distribution and not just the representation. The authors should include experiments where IdCor is computed on representations of different datasets to show that the correlation decreases as the data becomes less related.

__Minor points:__

Line 239-240: It is confusing to call these datasets "2D", given that two of them are actually 1-D manifolds. What is common between them is that they are all embedded in 2D space;  this should be made more clear. Line 196: for the same reason, it is inadvisable to call the spiral shaped dataset simply a "2D dataset". It is a 1-D manifold embedded in 2-D ambient space. This is in fact what was shown in Fig. 1, bottom-right: the Id of the circle is correctly labeled as 1.

The paper could elaborate more on how IdCor’s detection of nonlinear correlations leads to interpretability benefits, providing examples of how this information could aid in model evaluation or adjustment. In other words, clarifying how quantifying similarity between different models (lines 36--37, 107)) can help interpreting them?

TwoNN should be defined either in the main text or the Appendix since it is the method underlying all Id computations used in IdCor.

Lines 163-164: PCA might not be correct even if the data lie in a hyperplane: for example, a circle (1-dimensional) would lie on a hyperplane yet would require 2 principal component coordinates to be embedded. Thus, PCA can find the minimum number of dimensions required to embed the data (dimension of the ambient space), but not necessarily their intrinsic dimension (in the topological sense).

The methods listed in lines 166--169 can be used for dimensionality reduction but not for dimensionality estimation. Unlike PCA, which produces a way to rank dimensions based on their explained variance, all of these require the user to pre-specify the desired dimension.

### Questions
- How does IdCor perform under different levels of added noise, especially when applied to real-world, noisy datasets?

- Why is Id+ not included in Table 2?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Intrinsic Dimension Correlation ($I_{d}$Cor), a novel similarity metric aimed at detecting correlations between high-dimensional data representations, particularly in nonlinear, multimodal contexts. Unlike traditional similarity metrics that rely on pairwise distances or explicit mappings, $I_{d}$Cor leverages intrinsic dimensionality (ID) as a proxy to assess correlation. It operates by measuring the reduction in combined intrinsic dimensionality when two datasets are concatenated, capturing their shared structural complexity. The paper applies $I_{d}$Cor to multimodal datasets, showing potential in revealing non-linear correlations between different modalities of data corresponding to the same source. $I_{d}$Cor demonstrates the ability to detect correlations that traditional metrics like CKA, CCA, and Distance Correlation (dCorr) might miss.

### Strengths
1. Innovative Use of Intrinsic Dimensionality for Correlation Measurement: Extending traditional distance correlation by looking at intrinsic dimension correlation is a novel perspective in representation similarity metrics. 
2. Focus on Multimodal and Nonlinear Correlation: $I_{d}$Cor is specifically designed to tackle non-linear correlations in multimodal data, an area where traditional similarity metrics often struggle. 
3. $I_{d}$Cor incorporates permutation testing to establish the statistical significance of its correlation scores. This approach adds robustness to the metric, allowing users to differentiate between meaningful correlations and spurious ones with a quantifiable p-value.

### Weaknesses
I believe the current version of the manuscript requires several improvements, but I’ve summarized my primary concerns below:

1. **Insufficient Evaluation:** $I_{d}$Cor’s evaluation lacks rigor in assessing fundamental metric properties. I would like to see a comprehensive study on the metric’s invariance properties (e.g., scaling, rotation, linear/non-linear transformations, translations, subset translations, etc.). Additionally, Ding et al. [1] proposed a comprehensive set of sensitivity and specificity tests for validating new similarity metrics. Performing these tests on $I_{d}$Cor would help establish its standing among existing metrics. Specifically, the sensitivity test, which evaluates the metric's response to linear combinations of original coordinates, is crucial for understanding how $I_d$Cor behaves with transformations that preserve information content. The absence of such analysis leaves a gap in understanding the metric's behavior under various data manipulations.


2. **Lack of Comparison to Recent, Relevant Metrics:**  $I_{d}$Cor is compared only to CCA and CKA, yet several newer similarity metrics have since emerged, such as Representation Topology Divergence (RTD) [2], Graph-Based Similarity (GBS)[3], and Inner Product Similarity[4]. You could even look at Deep CCA [5]. These metrics are known to capture complex structural and topological differences, often outperforming CKA and CCA. Benchmarking $I_{d}$Cor against these advanced metrics would clarify its effectiveness and limitations, especially in high-dimensional and multimodal contexts. For instance, RTD, which focuses on topological differences, could reveal whether $I_d$Cor is sensitive to changes in the global structure of the representation space, a critical aspect not fully addressed by local neighborhood analysis.

3. **Ambiguity in Purpose:** The paper’s positioning of $I_{d}$Cor as either a structural or functional similarity metric is unclear. It is referred to as a correlation metric, but intrinsic dimension calculation relies on distances between data points, suggesting a structural basis. However, the metric is evaluated on its ability to detect similarities between multimodal representations (which, according to Maiorca et al. [6], differ primarily by affine transformations), leaning toward functional similarity. The choice of benchmarking $I_{d}$Cor against structural similarity metrics like CKA (known to be limited to scaling and orthogonal invariances) instead of functional metrics contributes to this ambiguity. I recommend clarifying the intended classification in the paper. This lack of clarity makes it difficult to interpret the results and understand the specific scenarios where $I_d$Cor is most applicable.

4. **Limitations of TwoNN:** 
- $I_{d}$Cor ’s reliance on intrinsic dimension estimation through second-nearest neighbor (TwoNN) consistency severely limits its insight into global structural alignment. I find it hard to see how $I_{d}$Cor could accurately quantify correlation between two spaces as a global value when it relies only on 2-NN consistency to assess similarity. Many fundamental changes can be made to a representation space while maintaining 2-NN consistency. Since the metric is “automatically invariant to any transformation that preserves the local neighborhood structure of data points,” it would miss changes that impact global structure but not local neighborhoods. This narrow focus makes $I_{d}$Cor unreliable in scenarios requiring a functional or comprehensive structural alignment. The TwoNN estimator's sensitivity to local density variations also raises questions about its robustness in non-uniform data distributions.
- The paper evaluates $I_{d}$Cor on multimodal alignment with spaces that are already trained and tend to have good nearest neighbor consistency. I would like to see tests on spaces with high local but low global consistency to see if  $I_{d}$Cor can still perform well. This limitation raises the concern that  $I_{d}$Cor may be reporting high correlations due to a lack of sensitivity to broader transformations rather than genuinely revealing correlations among multimodal spaces. Additional experiments with controlled transformations (such as subset translations) are necessary to determine whether  $I_{d}$Cor’s high correlation scores reflect meaningful similarity or an inability to detect fundamental changes in the representation space.

### Questions
1. Have you run experiments where you examine more than two nearest neighbors of each point when computing intrinsic dimension?
2. What is the exact computational complexity of your proposed approach?
3. Why is only the p-value reported for coarse vs. random alignment? I would like to see the IdCor value as well.
4. Are the p-values consistently the lowest possible in all the multimodal heatmaps?
5. For the N24News dataset, do you treat the headline as the corresponding text component or the caption?

### Soundness
3

### Presentation
2

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
This paper propose a way to define a proxy metric for mutual information to measure the relationship between two high dimensional distribution. The idea is fairly simple. Given distribution X and Y, and joint distribution X \times Y, it uses manifold learning based dimension reduction algorithm to reduce the dimension of X, Y and X \times Y. Intuitively, if X \times Y can be reduced to the same dimension of X or Y, then X and Y must be highly related. Moreover, the relationship between X and Y can be nonlinear due to the nonlinear dimension reduction algorithm. 

They author shows clean and well illustrated toy example to illustrate how the metric identify the nonlinear relationship between data. And show the model can be applied to analyze the distance between two neural representations and multi-model neural representations.

### Strengths
1. Simple and well-motivated idea. I really like this idea! 
2. Writing is good and easy to read.
3. Potentially influential application for deep learning and many field like neural science (distance between artificial/biological neural representation).

### Weaknesses
1. I think you want to show the discriminative power of I_dCor. This is probably the most important weakness. i.e. show I_dCor is not just a high score in general. If it maps different neural representation trained on imagenet to be close, then it should also map neural representations pre-trained on different dataset to be far away. So it would nice if you can come up with a task or metric that measure the discriminative power of your method I_dCor compared to other method. For example, construct subset of Imagenet using class label, map through a pretrained encoder, and use I_dCor to measure distance between the subset. You can use the distance metric and maybe just nearest neighbor to classify the label of each subset. Then show the I_dCor is superior then other measure. This might not be the best idea, but I believe you guys can come up with something better.

2. The assumption might be too strong. Like the author mentions, this idea is depends on the manifold learning algorithm for non-linear dimension reduction. The manifold learning must be able to identify the manifold from a high dimensional ambient space. But personally I think it's fine if you show the method actually works well, but you need more analyze to define "work well" than what you currently have. For example, see 1.

3. The analysis in figure 3 could be less ambiguous. I think you want to say the different (neural) representation of ImageNet is consistently similar under I_dCor, i.e. the similarity score has small variance. But it has a much bigger variance under a different metric under other metrics. I think this could be better shown than using two tables. 

4. I'm not sure if figure 2 is that meaningful. Because these different metric are under different scale right? As the network becomes more nonlinear, other metric decrease, so is I_dCor. So I'm not sure what it really says.

### Questions
I don't have any questions.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce a novel metric for determining the correlation of high dimensional datasets. They propose to use normalized mutual information, whereby the mutual information, expressed in the form of entropies, is replaced with the intrinsic dimension, which they calculate using the Two-NN method. This metric is then tested on synthetic data against CCA and dCor, showing that IdCor can effectively find correlation in non-linear settings, and can do so better than dCor. The authors then go on to show this in the context of large vision models, showing the correlation between various large vision models, and then extend into a multi-modality setting, showing a correlation between vision models and LLMs on a multi-modality dataset.

### Strengths
From an originality/novelty perspective, the paper is quite novel in that this is a new use case for the relationship between intrinsic dimension and entropy, being substituted into a mutual information context.

The paper is quite clear, and it is very easy to see not only how various parts are put together, but the rationale between combining them as well. This is especially apparent in the beginning of Part 3: "Correlation through Intrinsic Dimension", where the authors give a very clear example why ID is needed, and the relationship betwen ID and NMI. 

The authors do a very good job anticipating many of the questions readers might have, and explaining abnormalities in the results. In the results, they address several oddities that appear, such as the apparent lack of comparative performance on SigLIP and CLIP for coarsely aligned imagenet.

On the topic of results, the results are very good, with IdCor demonstrating very good performance, and a clear picture is painted as to its ability to deal with nonlinearity when obtaining a correlation metric. 

The authors have a very substantial list of references, and are hitting many of the related and necessary works for understanding what the authors are trying to do. 

The combination of these come together to create a very high-quality paper. Moreover, I believe this could have a moderate to highly significant impact on the field, and I can see how this new metric can certainly help with discovering the underlying mechanics of deep neural networks.

### Weaknesses
While the work is generally very clear, there is one place where a slight modification would help significantly.

While the reasoning behind using IdCor and not Id by itself is made fairly clear, the inclusion of the intrinsic dimension itself in table 1 could cause some confusion in this matter. A quick explanation of why Id is not sufficient (I believe no more than a sentence or two would be needed) should be all that is needed to ensure that it is clear that IdCor gives a better estimate, and is more useful. Specifically, the authors should clarify that while the intrinsic dimension can indicate the complexity of a single dataset, it cannot be directly used to compare correlations between two datasets, as the intrinsic dimension of a merged dataset is influenced by both intra-dataset and inter-dataset correlations. This distinction is crucial for the reader to fully grasp the motivation behind IdCor.

Other than that, there are only a few very minor grammatical mistakes. The most pressing is Section I, last paragraph, bullet point 1,

### Questions
In table 3/Section 4.2.1 "Coarse Alignment", it is seen that IdCor is outperformed by other methods for CLIP and SigLIP. The authors do give an explanation as to why, stating that these two use a self-supervised loss, which have no explicit notion of class. This is a good explanation, but I think this should be discussed a little bit further. Is it that any model with no explicit notion of class/using a self-supervised loss will cause IdCor to be less performant (meaning this should be put as a limitation), or is this a fluke of these two specific examples, and on other methods with self-supervised loss, IdCor outperforms other metrics? Either a theoretical explanation of why this is the case, or a few more examples using self-supervised loss on coarsely aligned data could help greatly towards ensuring that future works do not encounter problems with IdCor by inadvertantly using it incorrectly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel metric for latent space analysis based on intrinsic dimension correlation. With respect to previous metrics, this paper proposes a method that takes care of data nonlinearities and computations efficiency, two crucial aspects of real-worls problems.

I would like to thank the authors for this interesting paper. Overall, I find the paper interesting and relevant to the scope of the conference.

### Strengths
1) The paper explores the latent space from an information-theoretic point of view, which is very valuable considering that nowadays lots of papers just do so from architectural and neural points of view.
2) The method proposed in the paper consider the nonlinearity of the data, representing a crucial advancement with respect to previous methods that mainly focus on linear structures.
3) Results of the method seem consistent across different types of representations, ranging from different models to multimodal.
4) The paper is readable and easily understandable.

### Weaknesses
1) Although the authors claim that the proposed method can be extended to more than two modalities, no mathematical formulation is presented for this in the method section. Indeed, equations (1,2,3) focus on X and Y, and I am curious if it is possible to extend this to three or more. Specifically, the current formulation relies on pairwise comparisons of intrinsic dimensionality. Extending this to multiple modalities would require a more complex framework, potentially involving higher-order tensors or a different approach to aggregating pairwise correlations. The lack of a concrete mathematical formulation makes it difficult to assess the feasibility and potential limitations of such an extension.
2) A graphical representation, which is lacking, of the differences between the various methods (like figure 1) may help the reader better understand that method and its advantages. It is not clear how the proposed method differs geometrically from existing correlation measures. A visual comparison, perhaps using synthetic data, could highlight the specific scenarios where the proposed method excels, especially in capturing nonlinear relationships. Without such a visualization, it is challenging to grasp the practical implications of the theoretical advancements.
3) The authors could maybe insert a downstream example in which their method makes the difference. This would make the paper more effective and also highlight the importance of the proposal to practical researchers. While the theoretical framework is interesting, it is crucial to demonstrate its practical utility. A downstream task, such as cross-modal retrieval or transfer learning, would provide concrete evidence of the method's effectiveness. Without such an example, the paper risks being perceived as primarily theoretical, with limited immediate applicability.

### Questions
1) Related to the weakness 1, I would like to know whether exists a formulation for more than two modalities.

### Soundness
4

### Presentation
4

### Contribution
3
