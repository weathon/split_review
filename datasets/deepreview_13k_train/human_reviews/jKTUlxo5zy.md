# Less is More: Fewer Interpretable Region via Submodular Subset Selection

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Image attribution algorithms aim to identify important regions that are highly relevant to model decisions. Although existing attribution solutions can effectively assign importance to target elements, they still face the following challenges: 1) existing attribution methods generate inaccurate small regions thus misleading the direction of correct attribution, and 2) the model cannot produce good attribution results for samples with wrong predictions. To address the above challenges, this paper re-models the above image attribution problem as a submodular subset selection problem, aiming to enhance model interpretability using fewer regions. To address the lack of attention to local regions, we construct a novel submodular function to discover more accurate small interpretation regions. To enhance the attribution effect for all samples, we also impose four different constraints on the selection of sub-regions, i.e., confidence, effectiveness, consistency, and collaboration scores, to assess the importance of various subsets. Moreover, our theoretical analysis substantiates that the proposed function is in fact submodular. Extensive experiments show that the proposed method outperforms SOTA methods on two face datasets (Celeb-A and VGG-Face2) and one fine-grained dataset (CUB-200-2011). For correctly predicted samples, the proposed method improves the Deletion and Insertion scores with an average of 4.9\% and 2.5\% gain relative to HSIC-Attribution. For incorrectly predicted samples, our method achieves gains of 81.0\% and 18.4\% compared to the HSIC-Attribution algorithm in the average highest confidence and Insertion score respectively. The code is released at https://github.com/RuoyuChen10/SMDL-Attribution.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper points out two main issues with current State-of-the-Art (SoTA) image attribution methods: they ignore the impact of local, fine-grained attribution regions which may lead to incorrect explanations, and they may struggle to map the region/cause of a prediction error to image samples. 

To address these problems, the authors propose a new method based on submodular functions that divides an image into smaller regions and then selects the most informative ones (subset selection) to explain the model's decision-making process. They also employ a regional search to expand on the search regions.
The paper also introduces a novel submodular function to provide clearer and more detailed explanations, especially for incorrect predictions based on four major clues - confidence, effectiveness, consistency and collaboration scores.

The effectiveness of this new method is supported by experiments on facial recognition and fine-grained image recognition datasets, where it is shown to perform better than the current SoTA methods.

### Strengths
1. The paper highlights the importance of fine-grained, local regions for image attribution alongside causation of erroneous predictions to image features.
2. The novel submodular function proposed in the paper has been demonstrated to outperform several State-of-the-Art (SoTA) approaches.
3. The paper also introduce several interpretability clues such as confidence $s_{conf}$, effectiveness $s_{eff.}$, consistency $s_{cons.}$ and collaboration $s_{colla.}$ to evaluate the significance of the selected subsets. These additions effectively demonstrate better interpretability and are well supported by theoretical and empirical results.

### Weaknesses
 1. The idea of decomposing an input image $\mathbf{I}$ into regions has been studied for several vision tasks like self-supervision (Noroozi et al., 2016 etc.), object detection (Redmon and Farhadi, 2018) etc. These should be cited and the differences should be called out. Specifically, the paper should address how the proposed region decomposition differs from standard patch-based approaches and methods that use superpixels or other segmentation techniques, and why the chosen approach is more suitable for the task of image attribution.
2. The use of saliency maps $A$ in sub-region division is unclear. The paper should highlight how saliency maps are used to evaluate patch importance. It is not clear how the saliency map is used to guide the selection of patches within each sub-region, and how this process ensures that semantically meaningful regions are grouped together. The paper should provide a more detailed explanation of the mechanism by which the saliency map influences the sub-region division.
3. Most of the scoring functions like  $s_{eff.}$, $s_{cons.}$ etc.  rely on cosine similarity or distance metrics which have been studied extensively in literature (Deng et al., 2018, Wang et al., 2018 etc.) but have not been cited in the paper. The paper should clarify how these distance metrics are adapted or modified for the specific task of image attribution, and what advantages they offer over other distance measures.
4. The paper lacks the explanation regarding how individual scores contribute to achieving their respective objectives. For example, $s_{colla.}$ employs a cosine distance metric between the semantic feature vector of the target class $f_s$ and features extracted from the residual regions of the original image when the selected subset of regions $S$ is removed. To the best of my knowledge, maximizing this metric ensures that the collective impact of the selected region is sufficient to generate explainable representations. However, the paper does not clearly articulate the specific role of each score in the overall objective function and how they interact to achieve the desired attribution.
5. The proposed greedy search algorithm (section 4.3) has been studied for subset selection tasks (Wei et al., 2015) and is therefore prior art. The paper should acknowledge this and clarify the novelty of the proposed approach in the context of existing greedy search algorithms.
6. The paper misses a critical reference in submodular optimization (Fujishige, 2005) and should include it in the related work. This omission undermines the paper's claim of novelty in submodular optimization.
7. The experiments should include ablations on $k$ which is the number of sub-regions selected from $V$. Without this, it is difficult to assess the sensitivity of the method to the number of selected regions and to understand the impact of this parameter on the quality of the attribution.

### Questions
Most of the suggestions have been explained in detail in the weakness section. Additionally, some additional suggestions are listed below:
1. Section 4.1 which highlights the Sub-Region Division should be presented as an algorithm for better clarity.
2. It would be great to label the Input Image as $\mathbf{I}$ and saliency / attribution map as $\mathbf{A}$ in figure 1 for better clarity.
3. It is unclear as to what $M$ signifies in the problem definition, which should be clarified in sections 3 and 4.2. 
4. Lemmas 1 and 2 alongside equations 10 and 11 are already discussed in the problem definition in section 3, thus should be removed with referencing.
5. Theorem 1 is prior art (Nemhauser et al., 1978) and should just be cited.
6. Although optional, it would be good to have a set of notations as this paper encapsulates multiple domains in Machine Learning.
7. Experiments in section 5 indicate that the proposed method demonstrates significant improvements over existing methods. This shows the generalizability of the approach irrespective of the underlying model, which I believe can be highlighted for better impact.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of this paper propose a novel explainability method that restates the image attribution problem as a submodular subset selection problem. They suggest they can achieve better interpretability results with local regions. Moreover, they aim to obtain higher scores of interpretability with fewer regions.

### Strengths
- It is impressive that their method achieves a 81.0% gain in the average highest confidence score for incorrectly predicted samples. 
- Treating the interpretable region identification problem as a submodular subset selection problem is a novel and interesting idea.
- Their method has the ability to find the reasons that causes the prediction error for incorrectly predicted images.
- Adding the ablation study at the end is a good idea.

### Weaknesses
Some suggestions for minor improvements:
- The phrase "... at the level of theoretical aspects."at the introduction sounds a bit too wordy. It can be expressed more concisely.
- This sentence in the introduction "Image attribution algorithm is a typical interpretable method, which produces saliency
maps that explain how important image regions are to model decisions." can be better phrased, in my opinion, as "... that explain which image regions are more important to model decisions."
- I don't think fine-grainedness (page 2) is an actual word. Fine-graininess may be an alternative but I am not sure.
- On page 2, the word "...datasets." at the end of the first sentence of the second paragraph needs to be omitted.
- Contrary to what has been said on the introductory sentence of the White-Box Attribution method paragraph, I don't think there is a THE image attribution algorithm. I advise the authors to state either the name of the specific algorithm they are mentioning or use the plural.

### Questions
- How do the image attribution algorithms relate to attention in neural networks in general?
- What is the meaning of fine-grained interpretation regions?
- What does the "validity" of a submodular function mean?
- Is there an explanation on why the blue curve on the left of Figure 1 dips to almost 0 around 0.8?
- You claim your method can find fewer regions that make the model predictions more confident but I am seeing more highlighted regions in your setting. Am I missing something or misreading the images? Can you elaborate more on what I should be seeing?
- How does your method compare to the SOTA HSIC-Attribution method in terms of algorithmic complexity and time?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article transforms the image attribution problem into a submodular subset selection problem and determines the importance of divided regions through a greedy search algorithm. The author designed the submodular function from four aspects, hoping to use fewer areas to obtain a higher interpretable area. The author verified the effectiveness of this method on two tasks: face recognition and fine-grained recognition. Experimental results show that this method can achieve better attribution effects and can better debug incorrectly predicted samples.

### Strengths
- This paper reformulates the attribution problem as a submodular subset selection problem that achieves higher interpretability with fewer fine-grained regions.

- The proposed method enables more accurate attribution and can help find the reasons for the model to produce incorrect prediction results.

- It is meaningful to verify this interpretable method on face recognition and fine-grained recognition tasks, because these tasks are closer to practical applications.

- The authors provide some theoretical guarantees.

### Weaknesses
 - In Algorithm 1, I didn't see the use of variable k. Should n of line 3 be k?

- In Table 1, why are some results of LIME and Kernel Shap not reported? Is it because these attribution algorithms have limitations on the CUB data set? Hope the author can explain it.

- It would be better if the authors could discuss the limitations of this method.

- Can the author further state whether the proposed method is white-box based or black-box based (assuming that the calculation of a priori saliency map is not considered)?

### Questions
Listed in the weakness of the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper applies the submodular subset selection theory to the image attribution method, and can effectively improve the attribution ability of the baseline saliency map. The authors verified the effectiveness of this method on the Celeb-A, VGGFace2 and CUB datasets. Experiments show that the method proposed in this article can obtain more effective explanations with fewer regions than the baseline method. In addition, this method has great advantages in searching for regions that lead to model prediction errors.

### Strengths
- It is very interesting and practical to use interpretability to find the reasons for model prediction errors, which is helpful for humans to discover model defects and assist in improvement.

- Different from perturbation-based and gradient-based methods, the author adopts a method based on searching image areas for image attribution and achieves better performance.

- The author conducted a detailed analysis and included more experimental results and visualization results in the appendix.

### Weaknesses
 - In Section 5.3, for the discover the causes of incorrect predictions, the author only verified it on ResNet and achieved good quantitative results. It would be more convincing if the author could try to add some backbone, such as VGGNet. Specifically, the current experiments lack a thorough evaluation of the method's robustness across different network architectures. The choice of ResNet might introduce biases, and it is crucial to demonstrate that the proposed approach is not limited to a specific architecture. Testing with VGGNet, which has a different structure and depth, would provide valuable insights into the method's generalizability. Furthermore, exploring other architectures like MobileNet or EfficientNet would further strengthen the claims of broad applicability.

- Why are the results of LIME and Kernel Shap under CUB data not reported in Table 1? The absence of these results raises concerns about the completeness of the evaluation. It is important to understand why these methods could not be applied to the CUB dataset. If there are technical limitations, they should be explicitly stated and justified. If these methods are applicable, the results should be included for a comprehensive comparison.

- In Table 2, the saliency map without a priori seems to be better than the method of adding a priori saliency map in terms of average highest confidence evaluation metric. Can the author add an ablation experiment to observe the impact of different partition sizes on the results without adding a priori saliency map, such as 8x8, 12x12, etc. The current results suggest that the a priori saliency map might not be beneficial, and it is important to investigate the impact of the patch size on the performance of the method without the a priori map. This ablation study would help determine the optimal patch size for the proposed approach and provide a more complete understanding of its behavior.

- In the introduction, “and a fine-grained dataset CUB-200-2011 (Welinder et al., 2010) datasets” -> “and a fine-grained dataset CUB-200-2011 (Welinder et al., 2010)”

- In Algorithm 1, the input k is not used, please check carefully.

### Questions
See weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
