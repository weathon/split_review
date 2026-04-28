# Metric-Driven Attributions for Vision Transformers

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
Attribution algorithms explain computer vision models by attributing the model response to pixels within the input. Existing attribution methods generate explanations by combining transformations of internal model representations such as class activation maps, gradients, attention, or relevance scores. The effectiveness of an attribution map is measured using attribution quality metrics. This leads us to pose the following question: if attribution methods are assessed using attribution quality metrics, why are the metrics not used to generate the attributions? In response to this question, we propose a Metric-Driven Attribution for explaining Vision Transformers (ViT) called MDA. Guided by attribution quality metrics, the method creates attribution maps by performing patch order and patch magnitude optimization across all patch tokens. The first step orders the patches in terms of importance and the second step assigns the magnitude to each patch while preserving the patch order. Moreover, MDA can provide a smooth trade-off between sparse and dense attributions by modifying the optimization objective. Experimental evaluation demonstrates the proposed MDA method outperforms $7$ existing ViT attribution methods by an average of $12$% across $12$ attribution metrics on the ImageNet dataset for the ViT-base $16 \times 16$, ViT-tiny $16 \times 16$, and ViT-base $32 \times 32$ models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the attribution-based ViT explanation methods. The authors propose using attribution
quality metrics to generate the attributions as explanation results. The designed method, Metric-Driven
Attribution (MDA), consists of 2 steps: The first step orders the patches in terms of importance and the
second step assigns the magnitude to each patch while preserving the patch order, which can generate
smooth results. Experiments on ImageNet indicate the superiority of MDA.

### Strengths
1. The research question "why are the metrics not used to generate the attributions?" is interesting.
2. The two-step method can reduce the runtime from O(M^4) to O(M^3).

### Weaknesses
1. Motivation.

The reviewer's main concern is the motivation of this work. The proposed method MDA is exclusive to
perturbation-based evaluation metrics, such as Ins, Del, Ins-Del, etc. However, perturbation-based
evaluation only represents a specific aspect of desirable properties of explanation results, especially
considering that there are no ground truths for explanation (otherwise, we can adopt ground truths as a
method to generate explanation results). Therefore, the contribution of this work seems insignificant and
even questionable, as the proposed MDA ignores other evaluation metrics, such as localization ability [1],
faithfulness [2, 3], visual quality [1], sanity check [4], etc. The exclusive focus on perturbation metrics, which are inherently linked to the model's predictive behavior rather than the explanation's quality, raises concerns about the method's general applicability and interpretative value. The authors should clarify why optimizing for these metrics alone is sufficient for generating meaningful explanations.

[1] transformer interpretability beyond attention visualization. CVPR 2021.

[2] Rethinking Attention-Model Explainability through Faithfulness Violation Test. ICML 2022.

[3] on the faithfulness of vision transformer explanations. CVPR 2024.

[4] Sanity checks for saliency maps. NIPS 2018.

2. Computational complexity.

Although MDA reduces the search space from O(M^4) to O(M^3), it may still be slower than other
explanation methods, especially those not based on attributions. A detailed discussion about the
computational/time complexity compared to more methods would strengthen the paper. The authors should provide a more thorough analysis, including a comparison with methods that do not rely on attribution maps, such as gradient-based or attention-based techniques. Furthermore, a practical evaluation of the actual runtime on different hardware configurations would be beneficial.

3. Comparison to methods based on Shapley Value.

The idea is similar to Shapley Value [5, 6]. Could the author discuss the advantages and unique
contributions of MDA in terms of eﬀectiveness and complexity?

[5] Shap-CAM: Visual Explanations for Convolutional Neural Networks based on Shapley Value. ECCV 2022.

[6] A Unified Approach to Interpreting Model Predictions. NIPS 2017.

### Questions
As shown in Tables 1 and 2, the proposed MDA method exhibits performance degradation on Del ("Metric
From Petsiuk et al. (2018)"). Is there any analysis of this phenomenon? Is this related to how the patch
order is determined in step 1?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper argues that attribution quality metrics should be used to also generate the attributions and proposes Metric-Driven Attribution (MDA) for explaining Vision Transformers. Based on the metric, it creates attribution maps by performing patch order-magnitude optimization across the tokens. Patches are ordered according to their importance and then assigned magnitudes. MDA is claimed to provide a smooth trade-off between sparse and dense attributions by modifying the optimization objective.


Post discussion final comments:
The authors have addressed my concern regarding optimizing and evaluating the same metric. The additional experiments are convincing. While I still believe that some applications can benefit from more reliable attributions even if they are slow, I also support arguments of reviewer DmfJ and reviewer 7fM8 that this method will not easily scale to very large architectures.

In my opinion, this paper would be of interest to the research community but the rating still stands at 6. Hence, I am maintaing my score.

### Strengths
The paper gives a sound motivation for its contribution and the proposed approach makes intuitive sense.  

The paper is well written and easy to follow. 

The proposed method can control the density of attributions. 

Better quantitative results are achieved and the qualitative results also look impressive.

### Weaknesses
I think not optimizing the attribution maps w.r.t. the metric (that measures the attribution quality) is intentional rather than a neglect in the current literature because there is an inherent risk of biasing the results if we use the metric itself for computing the attribution maps. Provided the metric is perfect, this is a reasonable idea. However, metrics for evaluating attribution methods are still an active research topic. I would have to wait and hear the opinion of the other reviewers on this matter. 

The proposed method is computationally very expensive as the insertion and deletion processes are both iterative leading to O(M^4) complexity. The proposed method reduces the search space from O(M^4) to O(M^2) but that is still significant given 14x14 patches = 196. Moreover, the search space reduction relies on using another existing attribution method, making the solution less than elegant. 

Real time performance is an important criterion for attribution methods as one may require this information for every decision made by the model. Using insertion-deletion game for evaluating attribution methods, on the other hand, is an offline process so it makes more sense to use it for that purpose. 

During insertion (page 4), due you use the strongest response with respect to the ground truth? Maybe give a precise definition of model response to avoid confusion. 

Typos : 
“may violated” -> may be violated 
“memoization”  -> memorization

### Questions
Please see the Weaknesses section and write your response to the queries I have raised.

### Soundness
3

### Presentation
4

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
The paper is interested in a new attribution method, specifically designed for Vision Transformers to maximize the insertion and deletion metrics used for evaluating attribution methods in the literature. The method, called Metric-Driven Attribution (MDA), is separated in two stages. The first stage finds the best order of importance among all the patches, by gradually inserting patches and evaluating each time the model response. The second stage then assigns an attribution magnitude to all patch that will preserve the order found in the first stage. An additional hyperparameter is finally introduced in the attribution magnitudes, to govern the sparsity of the magnitudes. The model is then compared against different attribution methods applied to ViT models, measured using the same insertion and deletion metrics.

### Strengths
- **Originality**: The underlying idea of the paper of proposing method that measures attribution score with insertion and deletion is sounded and novel. 
- **Clarity**: The organization of the paper and description of the method are clear. The paper also includes multiple well-made figure that helps understand the overall method.
- **Significance**: The method provides both qualitatively and quantitatively good attribution maps. Attribution maps are usually the type of explanation methods that aligns the most with human preference in terms of explanation. The modular design of the method is also flexible to be further improved.

### Weaknesses
 - **Significance**: The major downside of the method is the runtime, as discussed in section 3.4. The runtime depends on both the granularity of the patch decomposition and the complexity of the model to analyze, in a multiplicative way since the method requires multiple forward pass to the model, from $\mathcal{O}(M^3)$ to $\mathcal{O}(M^4)$ depending on if the search space is pruned, where $M^2$ is the total number of patch. This can make the computation of the explanation for even a single image very expensive, but it is not compared with the other methods in the experiments. Furthermore, the method is currently limited to ViT models.
- **Quality**: The metrics considered for quantitative evaluation are only the ones optimized for (insertion/deletion AUC scores). It would be also informative to include a comparison with other types of metrics based on having ground-truths, such as evaluating for the segmentation task using ImageNet-Segmentation, as done in the evaluation of other methods (in Bi-Attn or T-Attr methods for instance). Specifically, the exclusive focus on insertion and deletion metrics raises concerns about the method's generalizability and its ability to capture other relevant aspects of attribution quality, such as localization accuracy or faithfulness to the model's decision-making process. The absence of a comparison with metrics that evaluate spatial accuracy, like pixel-level segmentation overlap, makes it difficult to assess the practical utility of the method beyond the specific optimization target.
- **Clarity**: The description of the metrics in section 2.1 is not really clear, and it is an important part to understand the method and the paper. Equation 2 does not correspond to the area under the MR curve, directly summing all $MR_k$ would not give the AUC. Furthermore, line 97 it is said "MR curve is formed on the range $[0,1]$", but it is not clear what variable is ranging in $[0,1]$ here. The explanation of how the $MR$ curves are constructed is vague, and it is unclear how the $MR_k$ values are obtained. The paper should clarify whether the $MR_k$ values represent the model's softmax output for the correct class or some other type of score, and it should be made explicit how the patches are inserted or deleted from the input image.

### Questions
- Could you provide a running time comparison with the other methods ? I noticed the mean running time per image was reported for MDA, but I would be interested in a comparison.  
- Could this approach be applied to other types of models (CNNs for instance) by patching the inputs similarly to ViTs ? The only part specific to ViT seems to be the separation into patches of the input images.  
- I'm not sure to understand why the ordering of the patches is found using two separate processes, since the "deletion-based patch ordering" is actually found by insertion of patches. From what I understood, the only differences between the two are: i) the starting image is first a blurred and then a black image, and ii) the ordering is first found from most to least important, and then from least to most important. I doubt the overall ordering found by the two processes are different between them. Could you expand more on why these two processes ? Furthermore, why start from a blurred image for insertion and from a black image for deletion ?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors are dealing with Explainable AI subject dedicated to vision transformers. Their idea is to optimize the order of patches based on the insertion-deletion tests. This is done firstly by convert a blurry image into a sharp one and at each time-step to find the most prominent patch (until a given limit). Then, the order of the rest of patches is found by imitating the deletion process. Lastly, a process to set a magnitude per each is described.

### Strengths
1) The idea of optimizing based on the examining metric is interesting, and sounds novel to me.
2) The non-technical parts are fluent and well written.
3) considering time complexity is important when applying XAI in online real-time applications. I think it is important to pay attention to this when developing a method (even for explainability which consider mostly as offline)

### Weaknesses
1) I find it problematic that the approach uses the same metric for derivation and experimental evaluation. To show agnosticity for the evaluation metric, it is much needed to evaluate in a clean setting when the metric is not involved in the derivation process (or actually optimized by it). Two additional fair potential metrics for evaluation in addition to the one presented in the paper could be: segmentation test and perturbation test. (elaborated on the T-Attr paper by Chefer et al.)
2) The technical parts are hard to follow, and sometimes indigestible. 1) in line 123 the notations $MR^{ins}$, $MR^{del}$ were used before definition. I would recommend define them first before using them. Moreover, in equation (3) you defined "$\|\cdot\|$ is the sum of all selected values" (line 129) - where it appears twice in the equation and in general overlaps with the norm symbol. I would recommend not shortening it and write it explicitly: $\Sigma_{i=1}^{M}\|A_i\|$ where $M$ is total number of attributions.
3) Some evaluations are missing: a) to better understand its effect on attribution sparsity or metric scores, ablating $\kappa$ would have been complete the ablation nicely. In a reasonable scale - something like 0 to 20-25 percentage. b) time efficiency comparison is missing and might shed light on the speed-up claims in section 3.4. (did not find also in the Supp.). A complete test comparison should include the timing of several other prominent approaches, however, I am aware that it might be difficult in the rebuttal frame-time. Thus, to have a better sense of timing, it would be nice to measure the time required to obtain explainability using your method for a single image (better to report it with std of several runs).

### Questions
1) As I understand it, you are selecting an equal number of elements at each time-step ($\frac{D^2}{N}$). Could you provide an intuition why?

2) How would you suggest tuning the $γ$ parameter for an unknown image?

3) Explainability could be beneficial in debugging misclassified images. It would be nice if you provide examples of misclassified cases and demonstrate how MDA addresses them.

Overall, I find similarities between your approach and general spectral analysis. When moving from a blurry to a sharp image, selecting the subset of pixels that most impact classification at each time-step is somewhat corelated with examining the image’s spectrum. I believe this is good direction for further research that has potential.

I still decided to give this paper a minor negative review due to two main concerns: (1) The method should be evaluated with metrics other than ins-del to ensure a fair comparison, and (2) a comparison of time efficiency is necessary, especially given its detailed discussion in the paper.

That being said, I think the idea presented in the paper is strong, and I would be willing to upgrade my rating if my concerns will addressed.

### Soundness
4

### Presentation
2

### Contribution
3
