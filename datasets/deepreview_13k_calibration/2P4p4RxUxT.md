# Conformal confidence sets for biomedical image segmentation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 3, 8

## Abstract
We develop confidence sets which provide spatial uncertainty guarantees for the output of a black-box machine learning model designed for image segmentation. To do so we adapt conformal inference to the imaging setting, obtaining thresholds on a calibration dataset based on the distribution of the maximum of the transformed logit scores within and outside of the ground truth masks. We prove that these confidence sets, when applied to new predictions of the model, are guaranteed to contain the true unknown segmented mask with desired probability. We show that learning appropriate score transformations on a learning dataset before performing calibration is crucial for optimizing performance. We illustrate and validate our approach on a polpys tumor dataset. To do so we obtain the logit scores from a deep neural network trained for polpys segmentation and show that using distance transformed scores to obtain outer confidence sets and the original scores for inner confidence sets enables tight bounds on tumor location whilst controlling the false coverage rate.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Authors develop confidence sets providing spatial uncertainty guarantees for outputs of a black-box machine learning model designed for image segmentation. Specifically, this paper adapts conformal inference to the imaging setting, obtaining thresholds on a calibration dataset based on the distribution of the maximum of the transformed logit scores within and outside of the ground truth masks. Qualitative evaluations are implemented on a polyp tumor dataset to demonstrate the effectiveness of this approach.

### Strengths
1.  The topic of this work is quite interesting. By proposing the concept of conformal confidence sets, this work could provide spatial uncertainty guarantees for the outputs of image segmentation models.
2.  Theoretical proofs are well formulated to serve as a strong proof for this paper.

### Weaknesses
1.  A very obvious typos “polpys” exist many times, even in the abstract. That should be “polyps”.
2.  It will be more convincing if authors could provide quantitative results for the segmentation performance of polyp segmentation. The evaluation metrics include Dice, Precision, Recall, etc. For comparable baseline models, authors could choose PraNet, SANet, etc. The lack of these standard metrics makes it difficult to assess the practical utility of the proposed method in comparison to existing segmentation techniques. Without these metrics, it's unclear how the uncertainty quantification relates to the actual segmentation quality.
3.  Since the concept of conformal confidence sets can be generalized to other medical image segmentation tasks, maybe more public datasets are applicable to this work, such as vertebrae or tooth segmentation. The current evaluation is limited to a single polyp dataset, which restricts the generalizability of the findings. Exploring diverse datasets would demonstrate the robustness of the method across different anatomical structures and imaging modalities.
4.  Some technical terms need to be further explained for a better understanding, such as FWER/FDR/FDP in the introduction part. The current explanation is insufficient for readers unfamiliar with these statistical concepts. A more detailed explanation of these terms, along with their relevance to the proposed method, is necessary for clarity.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors formally present an approach that aims at inferring uncertainty margins to segmentations. They propose either take the logit score of a CNN and to threshold it to obtain this margin, or to threshold at a certain distance to the predicted segmentation. Threshold and type of margin (logit score / distance) is to be identified experimentally for a given dataset. Experiments on one public dataset  are shown (containing still images from minmally invasive surgery).

### Strengths
* The authors present the problem in a formal manner, relating it to existing work.  
* The overall problem addressed is relevant.

### Weaknesses
 * The motivation for the scores functions (logit, distance, ...) is weak. The necessity to choose the type and to even mix them gives the overall approach a bit of a heuristic touch. (While I do understand that you would consider your contribution here to be in the formal derivation of underlying theory, i.e., very much the opposite of a heuristic.)
* The experiments only provide insights into one very narrow application. they are merely fulfilling the purpose of an illustation of the problem, but not a validation.

### Questions
* You are testing on public data. Has your pretrained polyp segmentation algorithm been trained on the same public data? 
* Are there any susequent video frames in the dataset, or images of the same polyp / patient? If there are, did you stratify your training / testing set accordingly?  
* Please remove the reference to tumors throughout the paper. Polyps may be precursors to tumors, but they aren't any. 
* You are using a dataset from different centers, there may be systematic differences in how the polyp areas are annotated - some annotators being more inclusive with respect to surrounding tissue, others being less. How does this variability impact on your measure? 
*  I might have missed it but what is the accuracy of your underlying segmentation algorithm? I would be under the impression that it is a well performing algorithm on a rather easy segmentation task? How does your approach relate to extrema in algorithmic performance, i.e., perfect segmentations or complete misses? 
* You are stating "In order to make efficient use of the data available, the learning dataset can in fact contain some or all of the data used to train the image segmentor." Your training data may be fairly overfittet impacting on your logit score and, hence, your choice of margin (logit/distance, thresholds). Wouldn't it be a safer approach to generate cross-validated logit functions and use them in the comparison?
* I understand that the primary contribution of this study is the theory offered. Still, you are stressing that your algorithm is a very lightweight addition to any pretrained segmentation algorithm. And there are a lot of standard computer vision / biomedical image data sets for segmentation available, as well as pretrained algorithms. Would you be able to generate segmentations maps for predefined certainty levels, and compare these levels with the testing performances across a larger set of applications? It would be quite convincing, if e.g., your 90% certainty map of the outer margin would indeed include 90% pixels of a test set or lead to a sufficiently large overlap (that has previously been defined) in 90% of all test cases.

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
4

### Summary
The paper proposes a conformal prediction based method to quantify the uncertainty for medical image segmentation. The proposed method is particularly designed for pre-trained segmentation models which notoriously make overconfident and wrong predictions. The proposed method learns thresholds using the maximum logit scores from a calibration set for the inside and outside of the ground truth masks and apply them on the logit scores of the test image to return conformalized segmentation prediction which guarantees to include the ground truth segmentation. The paper shows that naively learning the outside thresholds on max logits is not optimal and propose to transform the scores using a distance to make sure that far away pixels have lower scores. The method is validated on a single dataset for polyp segmentation and the results show that the proposed method produces conformal sets with narrower boundaries compared to using scores which are not transformed.

### Strengths
- The idea of using transformed max logit scores is simple but quite effective strategy to produces conformal segmentation sets.
- The presented experiments show the effectiveness of the method compared to using non-transformed logits.

### Weaknesses
1- Although I found the proposed idea of transforming max logit scores interesting, I don't think that the paper presents enough contribution to be presented in ICLR. The idea of applying conformal prediction to max logits for inside and outside of the boundaries is a direct extension of initial conformal prediction methods developed for segmentation, and applying transformations based on distance is an intuitive choice to refine predicted boundaries.

2- The paper does not present any comparisons with the existing conformal prediction works for image segmentation.

[1] Mossina et al. Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty, CVPR Workshops, 2024,

3- The method is evaluated on only a single dataset. Multiple datasets should be included to make sure that the performance generalizes across datasets.

4- In many segmentation tasks, we are interested in segmenting multiple structures. The paper only focuses on binary segmentation. I think the method should be validated on multi-class setting to make sure that it is also applicable in that setting.

5- The explanation of how the method is applied at test time could also be clearer. As I understand it, during testing, the method applies the inner threshold on max logits to find inner boundaries, then applies a distance transformation based on each pixel’s distance from these inner boundaries, and finally applies an outer boundary threshold. However, the exact steps of the algorithm during test time need more clarification.

6- In conventional uncertainty quantification algorithms for segmentation such as [2, 3] the uncertainty is quantified by the variance of the segmentation samples generated from the posterior distribution. How can the quantification be done in this case? Is it the margin between the inner and outer boundaries? Is the uncertainty quantified by the algorithm correlates with the uncertainty in the input image? For example, does the method output larger margins when there is greater disagreement between the segmentations of different experts?  

[2] Kohl et al. A Probabilistic U-Net for Segmentation of Ambiguous Images
[3] Erdil et al. MCMC Shape Sampling for Image Segmentation with Nonparametric Shape Priors

7- The margin between the inner and outer boundaries appears quite large and there can be many unplausible segmentations within this area. For practical applications, an uncertainty quantification method should ideally produce a set of plausible segmentation samples within this margin, rather than simply indicating a large margin that may or may not include the ground truth segmentation. How could one obtain a plausible segmentation sample from this margin?

### Questions
- How does the results generalize to other datasets and segmentation of multiple structures?
- How does the uncertainty quantified by the proposed method relates with the real uncertainty (assuming it can be measured by the disagreement between multiple experts)?
- How one can use the proposed method in a practical application? Can we get samples of plausible segmentations within the margin outputted by the algorithm?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a conformal prediction method that computes confidence sets with spatial uncertainty guarantees in image segmentation from any machine learning model. They illustrate the usefulness of the proposed method on medical images.

### Strengths
The paper is well-written and clear, although it took a second read-through to fully understand. The proposed method seems to work very well, and the presented experiments are convincing.

### Weaknesses
I am missing more quantitative results. For instance, aggregated coverage scores (e.g., mean; or other metrics, e.g., evaluate Equations 1 and 2) for the different versions on more than one dataset. This comparison should then also include some existing methods, to illustrate the relative strengths of different methods.

As just mentioned, for the results to be more convincing, I would also like to see examples on more than just one dataset.

Also, there must be other score transformation functions that could also be evaluated. Testing a couple more could strengthen the results and make it more convincing.

- Theorem 2.8: The H should have a subscript \rho, with the distance metric.
- Line 269: Says "poplys".
- Figure 2: Label the rows of the image grid.
- Line 364: Missing start of the sentence, or just that the first letter should be capital?
- Figure 5: It still says "Original scores".

### Questions
- Couldn't a related/similar smooth distance be defined using kernels?
- What is called "original scores", is this when you use the identity score transformation?
- What are the dashed lines in Figures 4 and 5?

Major comments:
- Add labels and/or legends to the rows and columns of the figures.

Minor comments:
- The word "polyp" is misspelled in different ways in almost every instance. Do check this.
- It says "... the set a side [num] images ...", or something similar, a few times. Check the grammar there.

### Soundness
4

### Presentation
3

### Contribution
3
