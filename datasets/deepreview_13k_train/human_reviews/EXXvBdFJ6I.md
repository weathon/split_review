# On the Inflation of KNN-Shapley Value

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Shapley value-based data valuation methods, originating from cooperative game theory, quantify the usefulness of each individual sample by considering its contribution to all possible training subsets. Despite their extensive applications, these methods encounter the challenge of value inflation—while samples with negative Shapley values are detrimental, some with positive values can also be harmful. This challenge prompts two fundamental questions: the suitability of zero as a threshold for distinguishing detrimental from beneficial samples and the determination of an appropriate threshold. To address these questions, we focus on KNN-Shapley and propose Calibrated KNN-Shapley (CKNN-Shapley), which calibrates zero as the threshold to distinguish detrimental samples from beneficial ones by mitigating the negative effects of small-sized training subsets. Through extensive experiments, we demonstrate the effectiveness of CKNN-Shapley in alleviating data valuation inflation, detecting detrimental samples, and assessing data quality. We also extend our approach beyond conventional classification settings, applying it to diverse and practical scenarios such as learning with mislabeled data, online learning with stream data, and active learning for label annotation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
There have been recent work focussed on providing tools to explore, quantify and curate data sets used for training learning algorithms. Several of the of widely used existing algorithms are based on the calculation of Shapley values from cooperative game theory.
The main difficulty for calculating Shapley values comes with the fact that it involves calculation involving training models with 2ˆN combinations of the training data which makes it intractable in real-life applications. In order to overcome this difficulty, a more practical variation have been proposed (2019,2021)  KNN -Shapley that enables the calculation of shapley values with a O(NlogN) complexity. The new calculation takes advantage of the nature and simplicity of the lazy NN algorithm as a surrogate substitution for more complex learning algorithms. 

The KNN algorithm can be greatly affected from the issue of inflation, which calls for a  proposed variation  by the authors call calibrated KNN-Shapley or CKNN-Shapley that the authors show that deals efficiently with the aforementioned inflation problem.

### Strengths
1) The paper is very well written,very well explained and self-contained. I was not familiar with the KNN shapley technique and was able to catch up quickly by reading the paper and looking at the provided references. The plots are very helpful as well.

2) The solution is proposed is very simple and arguable incremental but I think the impact of the small change makes the KNN-Shapley algorithm significantly better when using it in real-life applications. This is one of these cases where Ocham's razor's apply.  The fact that the change makes the KNN-based calculation faster is a plus as well.
 
3) Extensive experimental results in differensettings are helpful to see the potential of the proposed approach.

### Weaknesses
1) Since KNN is not an state-of-the-art algorithm in the modern practitioner toolbelt, my understanding of how this is used in real life would be that you would use CKNN-Shapley to clean the data and improve your training set quality and then go from there and use a more high performing algorithm e.g. GBM, XGboost, SVM etc. Is this the case? if it so can you add experiments where this two step is applied and see how this can improve the performance of these widely used algorithms?

2) Based on the provided experimental results The CKNN-Shapley  performance is better on almost all of the datasets where it was compared to other methods. It would be great to add p values that statistically shoe the significance. 

3) Minor: indentation is weird in some places e.g line 154. seems like the long Figure 1 caption gets "merged"with the main text.

### Questions
See 1) in weaknesses

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
4

### Summary
The paper aims to address the issue of value inflation in Shapley value-based data valuation methods. The proposed Calibrated KNN-Shapley (CKNN-Shapley) is to recalibrate the threshold to distinguish detrimental from beneficial samples, aiming to correct inflation that misidentifies some harmful samples as beneficial. CKNN-Shapley implements constraints on training subset sizes to mitigate inflation effects, which arise from the improper selection of small-sized subsets in the original KNN-Shapley approach. Through experiments, CKNN-Shapley demonstrates improved performance in classification and robustly adapts to applications like mislabeled data handling, online learning, and active learning.

### Strengths
(1) The paper introduces Calibrated KNN-Shapley (CKNN-Shapley) as a novel solution to address value inflation in data valuation using KNN-Shapley. This approach is significant as it recalibrates the threshold, effectively distinguishing between beneficial and detrimental samples, which is critical for robust data valuation.
(2) The paper conducts extensive experiments across various benchmark datasets, demonstrating CKNN-Shapley’s ability to outperform traditional KNN-Shapley and its variants. By testing on both image and text data, the paper validates CKNN-Shapley's broad applicability.
(3) CKNN-Shapley offers computational efficiency by directly assigning zero to certain sample subsets, reducing the recursive calculations required by the original KNN-Shapley. This efficiency makes it feasible for larger datasets, addressing a significant limitation of Shapley value-based methods in general.
(4) The paper’s calibration method and constraints on subset sizes provide a theoretical foundation that enhances the interpretability of data valuations. By setting a meaningful zero threshold and ensuring subsets closely resemble the original dataset, CKNN-Shapley offers more reliable and interpretable sample valuations.

### Weaknesses
 (1) Despite improvements over traditional Shapley calculations, CKNN-Shapley still incurs notable computational costs, particularly on large datasets or complex deep learning tasks. While more efficient than the original KNN-Shapley, the method may not yet be scalable for very large or high-dimensional datasets without further optimization. The paper lacks a detailed analysis of the computational complexity of CKNN-Shapley, especially in relation to the size of the dataset (n) and the number of neighbors (k). A more rigorous analysis, including empirical scaling behavior, is needed to fully understand its limitations.
(2) CKNN-Shapley, like KNN-Shapley, relies on K-Nearest Neighbors as a surrogate model, which may limit its applicability to contexts where KNN is less effective. This
assumption may restrict CKNN-Shapley’s performance in tasks with more complex decision boundaries, where a KNN-based approach may not be ideal. The paper does not explore the sensitivity of CKNN-Shapley to the choice of k in KNN, which can significantly impact performance, especially in high-dimensional spaces. Furthermore, the paper does not discuss the potential impact of using different distance metrics within the KNN algorithm, which could be crucial in various data modalities.
(3) The paper does not extensively explore or benchmark CKNN-Shapley against other semi-value methods or recent alternatives in data valuation, like Banzhaf values or other cooperative game-theoretic approaches. This lack of comparison limits understanding of CKNN-Shapley’s relative effectiveness and could benefit from further analysis of its competitive positioning. The paper should include a more comprehensive comparison with other data valuation methods, including those that do not rely on Shapley values, to provide a clearer picture of its strengths and weaknesses. This is important to understand the specific scenarios where CKNN-Shapley offers a significant advantage.
(4) While CKNN-Shapley is tested on simulated scenarios like mislabeled data and online learning, the paper lacks a real-world deployment case study to validate its robustness. Moreover, CKNN-Shapley’s sensitivity to hyperparameters in dynamic environments, such as varying batch sizes in streaming data, remains under-explored. The paper needs to provide more details on how CKNN-Shapley performs under different levels of noise and data drift, which are common in real-world scenarios. It should also discuss the practical challenges of implementing CKNN-Shapley in real-time systems and provide guidelines for parameter tuning in such environments.

### Questions
This paper proposed Calibrated KNN-Shapley (CKNN-Shapley), a semi-value method that calibrates zero as the threshold to distinguish detrimental samples from beneficial ones by mitigating the negative effects of small training subsets, addressing the value inflation issue observed in KNN-Shapley. The novelty is weak as it’s an improved version of KNN-Shapley. The detailed questions are listed below:
-
Could you provide more detailed guidelines or heuristics for selecting the subset size parameter T across different datasets? Specifically, how sensitive is CKNN-Shapley to T, and what considerations should practitioners have in choosing an appropriate threshold?
-
While CKNN-Shapley offers improvements in computational efficiency over traditional KNN-Shapley, what optimizations could make CKNN-Shapley scalable for very large or high-dimensional datasets? Could further modifications make CKNN-Shapley feasible for real-time data valuation in dynamic environments?
-
Since CKNN-Shapley relies on the KNN classifier as a surrogate model, how would CKNN-Shapley perform in contexts with complex decision boundaries or on tasks where KNN is not ideal? Is there a potential to generalize this approach beyond KNN, or could the calibrated approach be adapted for other surrogate models in Shapley-based data valuation?
-
Did you consider benchmarking CKNN-Shapley against other semi-value or cooperative game-theoretic approaches, such as Banzhaf values or alternatives in data valuation? If so, how does CKNN-Shapley perform relative to these methods, and in what contexts is it most advantageous?
-
Given the paper’s focus on simulated scenarios (e.g., mislabeled data, online learning, active learning), how would CKNN-Shapley perform in real-world applications where data is inherently noisy and highly variable? Are there specific real-world use cases (e.g., medical, financial data) where CKNN-Shapley has been tested, or do you have any recommendations for its deployment in production settings?
-
In your online learning and active learning experiments, how sensitive is CKNN-Shapley to hyperparameters like batch size and sample removal thresholds? How would you recommend setting these parameters for optimal performance in dynamic environments with streaming data?
-
CKNN-Shapley addresses value inflation effectively, yet inflation issues still exist to some extent. Are there additional strategies or constraints you would suggest for further reducing value inflation, particularly for beneficial samples that might still be overvalued?
-
In your experiments, how do you characterize the types of samples that CKNN-Shapley misidentifies, and are there common patterns or features among them? Could further insights into these misidentified samples help refine CKNN-Shapley or improve its robustness?
-
What are the significant contributions and connections of compared with existing studies for KNN-Shapley such as Threshold KNN-Shapley (Wang et al. 2023), KNN-Shapley (Wang and Jia 2023)?
-
More theoretical benefits and pitfalls need to be discussed in Section 3. How does CKNN-Shapley method work needs to be comprehensively elaborated in this section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers of the promblem of data evalution methods. Specifically, for a Shapely-value based method (kNN Shapley Value), the paper finds that it has some positive value miscalculated for some harmful datasets, thus resulting misunderstanding for some data points. The paper proposes to limit the calculation of kNN Shapley values only on data set whose size is above a specific value.

### Strengths
- The paper considers a problem setting (data evaluation) and a representative method (kNN Shapley value) that has high pratical importance.
- The paper is well motivated and the proposed approache is simple and effective.
- The paper also discusses the application of the proposed method in various applications.

### Weaknesses
 - The motivation seems only exist for the kNN based Shapley value, not other approaches of Shapley value. The sentence in abstract and introduction seems exaggerated that the problem exists for all Shapley value methods.
- The link between the motivation and the proposed method is vague. Specifically, does using the proposed $T$ value is designed to only solve the misclassified values? Is there probability that there are still misclassified values exist even using the probposed $T$? This also relates to the important problem of how to systematically assign the $T$ value, which is not theretically explored in the paper but just noted "the choice of T is contingent upon the dataset characteristics".
- What exactly does "semi-value" mean in the paper? It appears three times but does not a clear definition.

### Questions
- What exactly does "semi-value" mean in the paper? It appears three times but does not a clear definition.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Note added on December 4: I appreciate the authors' additional comments dated November 25 and 26. These confirm my overall evaluation and score of 6. I would emphasize that the central idea is the heuristic to use only the 2K nearest neighbors, and the simplicity of this idea should not be obscured. I appreciate the informal argument why inflation exists when too many neighbors are used.

The updated Table 7 shows that, sadly but not surprisingly, there is no free lunch, i.e., no clearly better test accuracy across the board. The main conclusion from this table is that it is harmful to remove samples based on the TKNN method. The benefits of other methods are unclear. The test sets used are just too small, as is the number and variety of datasets.

============

Shapley values can be used to measure the contribution of each point in a training set towards making a trained classifier more accurate. Ruoxi Jia et al. previously published an efficient method to calculate these Shapley values using k-nearest neighbor (kNN) classification. This paper shows empirically that those Shapley values tend to be too optimistic, and many data points with positive such values are actually harmful if used in training. The paper then proposes a heuristic improved version of kNN Shapley values, namely to use only the 2K nearest neighbors for each target point. Experimental results show that these new Shapley values lead to improved accuracy for trained classifiers.

### Strengths
The evidence for the phenomenon of inflation is believable. The experimental improvements in accuracy are large enough to be likely valid despite concerns about experimental methodology (test sets too small, not independent, no measure of statistical significance). The new heuristic kNN Shapley values can therefore be valuable in real-world applications.

### Weaknesses
The CKNN variation suggested for Shapley values is heuristic, with little evidence for any type of optimality. The paper should explain the motivation for introducing the hyperparameter T with more clarity and persuasiveness. 

The paper should explain better that because T = N-2K is used, in fact the method picks only the 2K nearest points. This is intuitively a good idea, but its ramifications must be explained.

It is not clear which experiments used an independent test set. The paper should report the statistical significance of differences in accuracy, using McNemar tests or something similar. Many differences may be not significant, because the test set is too small. 

Accuracy achieved with the CKNN method is highly sensitive to hyperparameters K and T. This makes the method less useful in practice.

012: Inflation is shown only for KNN-Shapley values, not for non-KNN values. So this sentence in the abstract is too strong.

019: It is misleading to mention small-sized training subsets, because with T = N-2K, in fact the training subset that is used for each target point is very small, of size 2K only. The benefit is that for each target point, this small subset is focused.

046: The reference (Jia et al., 2019b) to "Towards Efficient Data Valuation Based on the Shapley Value" is not correct, because KNN-Shapley does not appear in this paper. The reference to "Scalability vs. utility: Do we have to sacrifice one for the other in data importance quantification?" (CVPR, 2021) is also inappropriate, because the method is due to page 9 of "Efficient task-specific data valuation for nearest neighbor algorithms" (VLDB, 2019) .

Also, the formatting of the bibliography must be fixed, so that labels such as " (Jia et al., 2019b)" are visible in the PDF.

134: Figure 1 would be more clear using the same binning for the red and blue plots. The redline shows accuracy with a single bin removed. It would be more intuitive to remove this bin and also all bins to its left.

Maybe more important: The red line measures accuracy. This should be measured on an independent test set. The points that are removed are those that have a negative or small Shapley value as measured on the training set. It is not surprising that removing these points increases accuracy on the training set, because they have been identified as detrimental on precisely this set. The more interesting question is whether they are also detrimental on a separate i.i.d. test set.

153: The green region contains about half the entire dataset. Discuss why half of all points are harmful. It is not surprising if a few points are harmful, for example because their training labels are wrong. But it is surprising that so many points are. Is this true only because "harmful" is relative to the training set itself? Many fewer points may be harmful when the test set is independent.

174: It is not obvious that the first term is impactful, because it is small, since its denominator is N, which is much larger than K. Here is an alternative intuition: The reason to ignore the early terms is that their points are the most distant from the test point, so they are the most irrelevant to it. Even if they have the same label, that is accidental, so whether their labels are the same merely introduces noise. Moreover, the second and later terms include the denominator K << N, so they are much more heavily weighted than the first term.

197: Define "semi-value."

231: In Table 2, why are so many accuracies multiples of 0.01 or of 0.005? Because test sets contain only 100 or 200 data points? If this is true, then differences in accuracy are not statistically significant.

273: Why remove a fixed % of training points, when the advantage of CKNN is supposedly that the threshold zero tells us approximately how many points to remove?

Clarify the meaning of "KNN’s performance trained on the training set excluding samples". A fixed separate i.i.d. test set should be used. If accuracy is also measured on the training set excluding samples, this is not meaningful.

298: In Figure 3B, results for K < 5 must be included, since K=5 is best for the Wind dataset. The numerical values for Wind in Table 2 (0.8950 and 0.9100) are different from those in Figure 3B; why? 

In Figure 3C, T varies in the range 1950 to 1990. Why this range? Why is it so narrow? Explain how it is consistent with the recommendation T = N - 2K on line 377. 

More broadly, Figures 3B and 3C show that accuracy is highly sensitive to the choice of K and T. Why? Because training and test set sizes are small.

317: One goal of the CKNN method is for the empirically best threshold to be closer to zero. But why is this an important goal? Instead of the hyperparameter, we could use a validation set to determine the value of a non-zero threshold for standard kNN Shapley values, such as 0.8e-4 in Figure 1.

Note: I have not evaluated Section 5 carefully.

651: Typo.

728: Error in table title.

757: Table 7 is important and should be in the main paper, because this is how CKNN-Shapley might be used in practice. The same criticisms as above apply: test sets should be bigger and statistical significance should be reported.

### Questions
012: Inflation is shown only for KNN-Shapley values, not for non-KNN values. So this sentence in the abstract is too strong.

019: It is misleading to mention small-sized training subsets, because with T = N-2K, in fact the training subset that is used for each target point is very small, of size 2K only. The benefit is that for each target point, this small subset is focused.

046: The reference (Jia et al., 2019b) to "Towards Efficient Data Valuation Based on the Shapley Value" is not correct, because KNN-Shapley does not appear in this paper. The reference to "Scalability vs. utility: Do we have to sacrifice one for the other in data importance quantification?" (CVPR, 2021) is also inappropriate, because the method is due to page 9 of "Efficient task-specific data valuation for nearest neighbor algorithms" (VLDB, 2019) .

Also, the formatting of the bibliography must be fixed, so that labels such as " (Jia et al., 2019b)" are visible in the PDF.

134: Figure 1 would be more clear using the same binning for the red and blue plots. The redline shows accuracy with a single bin removed. It would be more intuitive to remove this bin and also all bins to its left.

Maybe more important: The red line measures accuracy. This should be measured on an independent test set. The points that are removed are those that have a negative or small Shapley value as measured on the training set. It is not surprising that removing these points increases accuracy on the training set, because they have been identified as detrimental on precisely this set. The more interesting question is whether they are also detrimental on a separate i.i.d. test set.

153: The green region contains about half the entire dataset. Discuss why half of all points are harmful. It is not surprising if a few points are harmful, for example because their training labels are wrong. But it is surprising that so many points are. Is this true only because "harmful" is relative to the training set itself? Many fewer points may be harmful when the test set is independent.

174: It is not obvious that the first term is impactful, because it is small, since its denominator is N, which is much larger than K. Here is an alternative intuition: The reason to ignore the early terms is that their points are the most distant from the test point, so they are the most irrelevant to it. Even if they have the same label, that is accidental, so whether their labels are the same merely introduces noise. Moreover, the second and later terms include the denominator K << N, so they are much more heavily weighted than the first term.

197: Define "semi-value."

231: In Table 2, why are so many accuracies multiples of 0.01 or of 0.005? Because test sets contain only 100 or 200 data points? If this is true, then differences in accuracy are not statistically significant.

273: Why remove a fixed % of training points, when the advantage of CKNN is supposedly that the threshold zero tells us approximately how many points to remove?

Clarify the meaning of "KNN’s performance trained on the training set excluding samples". A fixed separate i.i.d. test set should be used. If accuracy is also measured on the training set excluding samples, this is not meaningful.

298: In Figure 3B, results for K < 5 must be included, since K=5 is best for the Wind dataset. The numerical values for Wind in Table 2 (0.8950 and 0.9100) are different from those in Figure 3B; why? 

In Figure 3C, T varies in the range 1950 to 1990. Why this range? Why is it so narrow? Explain how it is consistent with the recommendation T = N - 2K on line 377. 

More broadly, Figures 3B and 3C show that accuracy is highly sensitive to the choice of K and T. Why? Because training and test set sizes are small.

317: One goal of the CKNN method is for the empirically best threshold to be closer to zero. But why is this an important goal? Instead of the hyperparameter, we could use a validation set to determine the value of a non-zero threshold for standard kNN Shapley values, such as 0.8e-4 in Figure 1.

Note: I have not evaluated Section 5 carefully.

651: Typo.

728: Error in table title.

757: Table 7 is important and should be in the main paper, because this is how CKNN-Shapley might be used in practice. The same criticisms as above apply: test sets should be bigger and statistical significance should be reported.

### Soundness
3

### Presentation
2

### Contribution
3
