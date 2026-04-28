# Just Select Twice: Leveraging Low Quality Data to Improve Data Selection

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 8, 3, 3

## Abstract
Data valuation is crucial for assessing the impact and quality of individual data points, enabling the ranking of data by importance for efficient data collection, storage, and training. Many data valuation methods are sensitive to outliers and require a certain level of noise to effectively distinguish low-quality data from high-quality data, making them particularly useful for data removal tasks. In particular, optimal transport-based methods exhibit notable performance in outlier detection but show only moderate effectiveness in high-quality data selection, due to their sensitivity to outliers and insensitivity to small variations. To mitigate the issue of insensitivity to high-quality data and facilitate effective data selection, in this paper, we propose a straightforward two-stage approach, JST, that initially does data valuation as usual, but then performs a second-round data selection where the identified low-quality data points are designated as the validation set to perform data valuation again. In this way, high-quality data become outliers with respect to the new validation set and can be naturally identified. We empirically evaluate an instantiation of our framework based on optimal transport method for data selection and data pruning on several standard datasets and our framework demonstrates superior performance compared to pure data valuation, especially under small noise conditions. Additionally, we show the general applicability of our framework to influence function based and reinforcement learning based data valuation methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a two-stage framework, JST, to assist existing data valuation methods in selecting high-quality data points. These data valuation methods are sensitive to outliers but fall short in recognizing in-distribution data points. This framework uses outliers as a validation set and again leverages the sensitivity of these methods to outliers to identify high-quality data points. The experiments show that JST significantly improves over baselines, verifying the effectiveness of the framework. However, it is not adaptable for marginal contribution-based data valuation methods due to a lack of the property of higher sensitivity to outliers.

### Strengths
1. The narrative of this paper is clear and easy to understand, and the illustrations are vivid and illustrative.

2. The framework is experimentally effective on tested tasks.

### Weaknesses
1. The lack of theoretical analysis makes the article seem incomplete.

2. The results of Figure 4 seem inconsistent with the analysis of Figure 1. Specifically, in round 1 of Figure 4, outliers appear mixed with in-distribution data points at low data values. This raises concerns about the effectiveness of using outliers as a validation set, as the NDRoutlier might be negatively impacted by the presence of in-distribution data points with low values. It is unclear how JST can effectively identify high-quality data points when the initial ranking is noisy.

3. Some experimental phenomena can be further explained. For example, the close proximity of the three curves in Figure 5 makes the claim of "much higher accuracy" seem overstated. The random selection baseline's strong performance also warrants further discussion, especially given its horizontal line behavior in Figure 3, which contrasts with its performance in Figure 5.

4. I recommend that the authors add experiments about time cost to demonstrate their applicability in reality. The addition of a second stage to the framework seems likely to more than double the computation time. The practical implications of this increased time cost should be evaluated, especially given the seemingly marginal improvements in Figure 5.

5. Some symbols are not clear and a bit confusing. The use of “-” in the subtitles on the left and right sides of the three figures in Figure 1, being very close to “Noise Level - Std. Dev” and “NDRoutlier-NDRin-distribution”, makes it difficult to understand the figure.

### Questions
The authors discovered a phenomenon that existing data valuation methods are not sensitive to in-distribution data points and used this property to design a two-stage framework. However, they did not explain this phenomenon mathematically.

In round 1 of Figure 4, I see that outliers are mixed with in-distribution data points at low data values. Wouldn’t this cause the NDRoutlier to be poor as well? How does JST work in this case?

In Figure 5, the three curves are very close. I think "our framework achieves much higher accuracy compared to the pure data valuation method" is overclaimed. Also, I hope the author can explain why random selection has such good results. In Figure 3, the curve of random is a horizontal line.


Adding a stage seems to more than double the time, but the improvement of the new framework in Figure 5 is not significant, which may not be a good thing in real applications. Therefore, the author can add experiments on time cost trade-offs to show that the improvement in performance is reasonable for the increase in time cost.

 “-” in the subtitles on the left and right sides of the three figures in Figure 1 is very close to “Noise Level - Std. Dev” and “NDRoutlier-NDRin-distribution”. This is a bit confusing for me to understand the whole figure.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose an interesting and novel way of computing data values, specifically aimed at ensuring high sensitivity to high-quality data and low-quality data (outliers), crucial for the data selection use case.

### Strengths
- The authors clearly state the problem, and Figure 1 helps show the noise sensitivity levels for the different methods.
- The suggested solution is novel and well-illustrated. 
- It was good to see authors assess JST with semi-value approaches like data Banzhaf and show where JST may not do so well.
- The figures (both in the results and methodology section) that the authors use are very descriptive, nicely drawn, and intuitive.
- The authors run experiments on various image datasets: MNIST, CIFAR, SVHN, and Food-101.

### Weaknesses
 **Questions and weaknesses**
- The authors could improve the figures and captioning, especially in the main text. The captions are not sufficiently descriptive. For example, in Figure 3, the authors don't clearly state the base data valuation method used.  In Figure 6, when using the random data valuation, it's unclear what the selection criteria for the images is. And what's the base data valuation method used?
- Could authors provide the rationale for selecting varied noise levels for different experiments (different base methods) on the same dataset? For example, why is noise level 10 in Figure 8 but 6/9 in Figure 7, and so on?
- I wonder if the initial utility function that uses the “general clean validation” set might in principle be “significantly” different from the one that uses the “low-quality-noisy validation” set. Consequently, I am curious if and by how much the value of a datum changes in the initial setup versus the second setup. If the value of datum A > the value of datum B in the initial setup is that still the case?
- What’s the stability of JST across runs?
- In case of issues like replication, wouldn’t that “poison” the level-two training/validation sets?
- Without “synthetic” noise injection, how well does JST work or compare to marginal-contribution methods on “natural” data with likely outliers, for example, low representation of samples from a given class, sensitive group, etc? 

**Miscellaneous and minor**
- Minor: The text font size on the figures could be made larger to improve readability.
- How well does the framework scale to tabular datasets?
- Are there differences in class balance when using JST versus the base/pure data valuation method? Is it likely to make things worse/better?
- Given the costly nature of level-one data valuation, how scalable is two-level data valuation (JST)?
- Given that JST doesn’t improve things in methods like Banzhaf values, where these methods have additional favorable characteristics like replication robustness and consistency across runs, what’s the incentive for one to use JST over them?

### Questions
Questions are contextually embedded in the weakness section. Authors should please address questions added in the sub-section "questions and weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies data valuation, specifically using data values to perform data selection. The authors proposed to exploit a property of optimal transport-based data valuation methods, namely their sensitivity to outliers (and insensitivity to inliers), and describe a two stage algorithm. The proposed algorithm first selects outliers, and then in the second stage use the selected outliers as validation dataset to again select outliers. Due to the statistical difference, the outliers selected in the second stage are high quality data points. Empirical results on image datasets are provided.

### Strengths
- The studied problem is relevant and important.
- The method is described clearly.
- Some empirical validation is provided.

### Weaknesses
 - There does not seem to be theoretical justification or characterization of the effectiveness of this method. In comparison, the optimal transport based method (Just et al., 2023) or the influence based method (Koh et al., 2017) both provide theoretical justifications.

- The empirical performance can be made more extensive. There are quite a few existing data valuation methods, such as those described in (Sim et al, 2022). While it is understood the proposed method is motivated by the property of optimal transport-based method, the authors indeed investigate other methods such as reinforcement learning based method (Yoon et al., 2020). Thus, it makes sense to compare with these existing methods.

- The key property of this method requires that low-quality and high-quality data to be "outliers" to each other. But in practice, this relationship is not so crisp. For a specific task, the characterization of ideal high-quality data is fairly narrow (i.e., there is only one kind of data which is high quality), while there are (possibly infinitely) many characterizations of low-quality data/outliers. While it is true that outliers (say outlier distribution A) would be statistically different from high quality data (outliers to high quality data), but another type of outlier (say outlier distribution B) would also be outlers to outlier distribution A, but this does not make it high quality. In other words, high quality is the outlier to outliers, but the reverse need not be true (an outlier to an outlier is a high quality data point).

### Questions
In abstract, 

`Many data valuation methods are sensitive to outliers and require a certain level of noise to effectively distinguish low-quality data from high-quality data,`

What is meant by "require a certain level of noise... "?


In Figure 1, how are the rates computed? and why do they show a higher sensitivity of data valuation methods to outliers?

Instead of ResNet-18 and ResNet-18 pretrained on Image1K, what do you propose as a principled and general way to perform feature extraction for a dataset to use your method?

What would be the empirical results if there are different types of outliers present? For instance two differnt types of noise.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to enhance data selection by performing a second round of data valuation. The first round of data valuation is done using a validation set. The proposed algorithm would identify $k$ points with the lowest valuation (i.e., performance on the validation set). The second round would value the remaining points based on how poorly they perform on this low value set. Points that perform poorly are high quality data.

### Strengths
It is important to study how data valuation can be better adapted to select high quality data (instead of only filtering out low quality data). The experiments consider various datasets and data valuation methods.

### Weaknesses
1. The clarity of the paper can be improved. The paper repeatedly use the word "outlier" but does not define or use the word precisely. How do we distinguish between outliers and in-distribution data? How do outliers differ from noisy data? Does the classification depend on the data valuation method? Without clear examples or definition, the significance of Figure 1 is unclear.  The definition of outlier seems to change in line 79 "allows high-quality data to be identified as outliers in the new context". The authors can provide a clear definition or example at the start of the paper and use it consistently.
2. The experiments only consider corrupted images. Would the JST algorithm perform well for other scenarios such as corrupted labels? For example, the first round of data valuation might select some data with wrong label A. In the second round, any data with different label (e.g., true label B and wrong label C) would have the same low score. The revision should. include more experiments to prove the method is useful for other data corruption.

Minor comments: Citations should be in the form of (author, year) instead of author (year).

### Questions
1. Explain how the normalised outlier detection and in-distribution data detection rate is computed in Fig 1. Is there some ground truth to classify whether data is an outlier or in-distribution? 
Ideally, how should Fig 1 look like for a good data valuation method? Is that achieved by your method?
2. What is a more precise definition for sensitivity to outliers and sensitivity to high quality data?
3. Would the JST algorithm work for tabular data and other form of errors such as corrupted labels?

### Soundness
2

### Presentation
2

### Contribution
2
