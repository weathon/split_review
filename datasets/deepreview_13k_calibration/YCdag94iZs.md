# MILCA: Multiple Instance Learning using Counting and Attention

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
In Multiple Instance Learning (MIL), a bag is comprised of instances and the label is prescribed to the whole bag, with no information on the labels of each instance.
The leading approaches for MIL are Embedded Space (ES) solutions, where the full bag is embedded into a vector space. 
While very complex models were constructed for MIL classification tasks, we show that often some features are associated with a class, and a simple counting/summing algorithm leads to similar or better accuracy than current solutions.  This can be improved in some cases by weighting these selected features using a fully connected network to predict the coefficient of each feature. 
However, a simple relative contribution of each feature, where the sum of the coefficients is normalized to 1,  fails to count the feature. Thus instead, we replace the softmax by a projection of the coefficients to [-1,1] or [0,1] but do not limit their sum. This allows the model to count features. 
The resulting algorithm - MILCA (Multiple Instance Learning using Counting and Attention) is applied to multiple previous and new real-world MIL tasks, as well as recovering the host disease history from sequenced T Cell Receptor Repertoires. In most cases,  MILCA is significantly better and way more efficient than currently used MIL algorithms, with a 3 \% higher accuracy than current SOTA on average. To summarize, in MIL classification tasks, where often the number of features is large compared to the number of bags, complex models are typically not better than a weighted sum of informative features.  
The code for MILCA is available at: github.com/submissionanonymous6/MILCA

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new multiple instance learning method using counting and attention, to address the shortcoming of existing methods which are unable to enumerate the features. In the proposed method, a simple strategy is designed to seek out the informative features, and then based on these selected features, it counts the average in each bag of instances associated with each class. Compared with existing works, the proposed method demonstrates superior performance on MIL datasets and new real-world MIL tasks.

### Strengths
Significance: This work proposes a new MIL method based on using counting and attention, to address the overfit problem of most existing methods. Experimental results also illustrate the proposed method can achieve better performance than SOTA. 

And the originality may be limited.

### Weaknesses
1.	The motivation for designing this method is not specific, and the method's novelty is also less pronounced. What’s improved for MIL by the proposed method (except the performance)? Why is the proposed method more effective than the existing methods? Lack of some theoretical analyses.  

2.	For some basic concepts, it seems that the author's understanding is not entirely accurate.  

3.	The writing is of a poor standard, making it difficult to understand the key of the proposed method. Furthermore, the structure is not professional.  

More detailed comments can be found in Questions.

### Questions
1.	See the first point in weaknesses.

2.	In the part of Introduction, authors present many fundamental concepts related to MIL, but there are a lack of depth analyses on the motivation behind proposing MILCA. Under limited spaces, it would be beneficial for the authors to devote more attention to these more important contents (which are most closely related to the proposed method), including some explanation of why to design this method, an analysis of the problems in most existing methods, and a discussion of how these problems are to be solved by the proposed method. It would be advisable for the authors to consider reorganizing the content to achieve this. 

3.	‘Such a classifier (MILCA) is better than SOTA…’, maybe it is not novelty. Experimental results are regarded as an illustration of validating the effectiveness of the proposed method with your novel design. Moreover, Why ‘MILCA has fewer or no learnable parameters…’? Here need more details to explain it. 

4.	For ‘counting’ in MIL problems, there are not related works in the recent years, why? Is it not suitable in real applications? For limitation, MILCA is a naïve Bayesian estimator, and it means that MILCA defaults on the independence among features, which may also go against with the real applications. How to consider this problem? Could you give some examples to illustrate the application problem of the proposed method. 

5.	In the training process, how to optimize the parameter $M$? It is recommended that the change figure of the optimised M value be provided.

6.	The proposed method gives three models: C1, C2 and C3. Why to design three models? The results indicate that the third model (C3) is better than others. It is recommended to analyse which problem each model is more suited to.

7.	In experiments, authors mentioned ‘the results are the average of 10-fold cross validation’. But, authors then mentioned ‘in each fold, the data are divided into three parts: training (64%), validation (16%) and testing (20%)’. It may be inferred that the authors lacked a clear understanding of the concept of k-fold cross-validation, which is very serious issue.

8.	Last but not least, the writing and structure of this manuscript require significant improvement, and the current version is very messy and unprofessional, which makes it difficult to understand the proposed method, especially not primary and secondary. For example, 
- The section on novelty should be incorporated with the introduction, and the latter should include further discussion of the motivation, such as an examination of the shortcomings of existing MIL methods and an analysis of how the proposed method addresses these issues. 
- The subsections 4.3, 4.4, 4.5 and 4.6 should be placed with the results together, included in the part of experiments and analyses (section 4).

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel approach to Multiple Instance Learning (MIL), where the goal is to classify a bag composed of instances, by incorporating counting and attention mechanisms. Instead of relying on a single aggregated bag embedding for classification, the method identifies representative features across the dataset and encodes each bag as a count of these features. The informative features are identified by using statistical methods like Mann Whitney test. The paper introduces four variants of the classification component, which have different number of learnable parameters. The proposed method is evaluated on several classical MIL datasets, as well as a simulated dataset and disease classification using T cells repertoires.

### Strengths
- While the concepts and issues presented in the paper have been previously discussed, the methods introduced offer a fresh perspective. The method proposes a seemingly novel approach for encoding bags as a count of dataset wide features. The main idea seems to be simple and have good performances on multiple benchmarks.
- The proposed approach seems to have better performance than the baseline on the disease classification using T cells repertoires benchmark.
- The paper introduces a new dataset, named Wiki dataset.

### Weaknesses
 **Limited technical novelty.**  As mentioned in the paper, the idea of counting in MIL is not novel and was already explored in other works. The model reuses a lot of existing modules such as Mann-Whitney test, thus novelty is also limited.

**Incomplete experiments.** The section 4.4 presents the compared methods, but the results of some methods are not shown in the experimental section. For example, the results of BDR and MI-SDB are not shown in Table 1. The results reported in MI-SDB outperform the proposed method. The Table 1 should compare with recent or state-of-the-art methods, otherwise the second novelty claim is not valid (L77). 

**Experimental validation.** The paper introduces four variants of the proposed model. However, there are significant performance differences between these models. For example, MILCA2 is much better on wiki dataset (Table 2) than MILCA3, but MILCA2 is much better on classical MIL datasets (Table 1) than MILCA3. The best variant seems to depend on the target dataset. It would be great to add a paragraph to discuss the difference of performances between the variants, and to explain how to choose the best variant. Classical MIL datasets tend to be smaller in size compared to contemporary MIL datasets, which typically feature more diverse and intricate characteristics. The scalability of this approach to larger and more complex datasets remains uncertain. The results for the simulated, wiki, and TCR datasets utilize different models compared to those evaluated on the classical MIL datasets, yet the rationale for this choice is unclear. To enhance the analysis, it is essential to expand the results for these datasets to incorporate additional MIL models.

**Paper clarity should be improved.** Overall, the paper presentation should be improved to be easier to read. The paper lacks a clear and intuitive structure. For example, the section 4 named "Methods and Model" contains subsections that are not about the proposed model. It contains two sub-sections about datasets, and one about the experimental setup. Something is missing at the beginning of the model section (section 4). I think a high level overview of the model, with its inputs and outputs, and the task solved. Some notations are not consistent. For example at line 130, the bag is named B, but in Figure it is named X.

**The term "tabular data" is confusing or incorrect.** The term "tabular data" may not be the right term as the goal is to create vectorial representations of the inputs. The term "tabular" refers to data that is displayed in columns or tables, which is different from what is done in the paper. Tabular data is not limited to numerical values and can contain strings. Removing the "tabular data" constraint will make the model more generic as it can be used on images.

### Questions
- Why some methods introduced in section 4.4 are not shown in Table 1 or 2?
- There is not enough information about the new dataset in the paper. It is important to explain how the dataset is built as it is one contribution. The current information in the paper or appendix is not enough to reproduce the dataset. 
- Table 2: It is confusing to see the number of learnable parameters for C1 is 0. If there is no learnable parameters, how is the decision made? 
- L139: It is not clear when the average or median is used. It would be great to explain how to choose between these two options.
- Why two standard deviation is shown instead of just 1 standard deviation in Table 1? 
- How would this model scale to larger and more complex datasets?

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
5

### Summary
This paper introduces a technique called MILCA, designed to perform counting and summing of features. In MILCA, feature weights are predicted using a fully connected network (FCN) where the softmax layer is replaced with a projection to produce coefficients within a specified range, either [-1, 1] or [0, 1]. Experiments on various multiple-instance learning (MIL) tasks demonstrate the effectiveness of MILCA.

### Strengths
+ The analogy of explaining three solution spaces—Instance Space (IS), Bag Space (BS), and Embedding Space (ES)—by likening a book to a bag and its chapters to instances is highly intuitive.  
+ The paper is well-written in a clear, straightforward style, making it easy to understand.  
+ Detailed experimental procedures are included, aiding replicability. Additionally, the source code is provided to facilitate reproduction.  
+ The proposed technique is both simpler and more efficient, demonstrating strong performance across several existing MIL benchmarks.

### Weaknesses
 - In my view, this paper lacks sufficient novelty. The counting-based approach appears to be a straightforward extension within the MIL space, and it does not introduce any new theoretical contributions either.
- The datasets used for evaluation are relatively simple. I recommend that the authors conduct experiments on more complex, high-dimensional datasets (such as video datasets) designed for MIL settings. Examples include UCF-Crime, ShanghaiTech, Avenue, and XD-Violence,  used in [1, 2, 3]. Additionally, it would be beneficial to compare the performance of the proposed technique with other models, such as those in [1, 4].
- The authors’ focus is primarily on bag label prediction; however, current trends in the MIL domain increasingly emphasize instance label prediction, which is crucial for applications like video anomaly detection [1, 2, 3]. I am curious whether the current approach could be extended to instance label prediction. If so, how does the proposed technique compare to state-of-the-art methods on more challenging datasets, such as those in the video domain?
- **Minor:** Some annotations are used without formal definitions. For example, $v_i$ appears undefined in the "Novelty" section of the Introduction, point 4, though its meaning can be inferred from the context. Providing formal definitions of symbols before or immediately after their introduction would enhance the paper’s readability.

### Questions
Please refer to Weaknesses Section

### Soundness
2

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
4

### Summary
This paper attempts to analyze the impact of certain intrinsic feature attributes on classification within several specific datasets. The author assumes that some feature attributes exhibit significant differences between positive and negative bags(instances), and thus employs t-tests to examine each feature. This approach seeks to determine which features are associated with positive bags(instances), forming a set called PF, while those associated with negative instances form a set called NF. After the feature selection phase is completed, three classification methods—C1, C2, and C3—are provided based on the selected PF and NF, further exploring the influence of these classifiers.

### Strengths
***Significance***: The authors propose applying feature selection in multi-instance learning. This idea may be meaningful in some specific scenarios, for example, when the data features themselves are well-normalized and highly indicative. 

***Originality***: Feature selection strategies have been widely applied in early simple datasets, which limits the degree of originality. 

***Clarity***: I appreciate that the authors have made their code publicly available, which contributes to higher clarity. 

***Quality***: However, during the review process, I found that there may exists some substantial error in the official implementation of the author's statistical process. This error may lead to an unsubstantiated PF/NF set in feature selection process, making it difficult to ensure the reliability and significance of the final conclusion.   For detail see Reliability in Weaknesses.

### Weaknesses
 ***Reliability***: The author assumes that some feature attributes exhibit significant differences between positive and negative bags(instances). To validate the thought, the author employs t-tests to examine each feature, to further determine which features are associated with positive bags(instances), forming a set called PF, while those associated with negative instances form a set called NF. After the feature selection phase is completed, three classification methods—C1, C2, and C3—are provided based on the selected PF and NF, further exploring the influence of these classifiers. Essentially, the selection of PF and NF forms the basis of the paper and experiment setups.

This process involves the following code provided by the authors:

1. `MILCA/utils_for_c_tests.py`, lines 42-49:
   ```python
   def Feature_props(datasetA, datasetB):
       N = len(datasetA[0][0])
       statistic = np.zeros((N, 3))
       for i in range(N):
           dist_i_A, dist_i_B = get_dist(datasetA, i), get_dist(datasetB, i)
           statistic[i, 0], statistic[i, 1] = stats.ttest_ind(dist_i_A, dist_i_B)
           statistic[i, 2] = np.mean(dist_i_A) - np.mean(dist_i_B)
       return statistic
   ```

2. `MILCA/utils_for_c_tests.py`, lines 19-27:
   ```python
   # This function gets a dataset and an index, and returns the distribution (list of means) of the index in the bags.
   def get_dist(dataset, index):
       dist = []
       for bag in dataset:
           feat_count = 0
           for instance in bag:
               feat_count += instance[index]
           dist.append(feat_count / len(bag))
       return dist
   ```
3. `MILCA/utils_for_c_tests.py`, lines 52-61:
   ```python
   def get_two_scores_count(bag, best_feat):
       inst_count, feat_count_p, feat_count_n = len(bag), 0, 0
       for instance in bag:
           for i in range(len(instance)):
               if i in best_feat.keys():
                   if best_feat[i] == 1:
                       feat_count_p += instance[i]
                   else:
                       feat_count_n += instance[i]
       return feat_count_p / inst_count, feat_count_n / inst_count
   ```

4. `MILCA/C1.py`, lines 15-45:
   ```python
   start_time = time.time()
   # Find significant features
   stat_train = Feature_props(g_train_pos, g_train_neg)
   condition = stat_train[:, 1] < p_cutoff # find significant features.
   top_k_index = {}
   for i in range(len(g_train_pos[0][0])):
       if condition[i]:
           top_k_index[i] = np.sign(stat_train[i, 1] - stat_train[i, 0])
   # Compute difference for significant features
   for i, bag in enumerate(train_samples):
       z_p_tr, z_n_tr = get_two_scores_count(bag, top_k_index)
       train_predicted_scores_pos[i] = z_p_tr
       train_predicted_scores_neg[i] = z_n_tr
   for i, bag in enumerate(test_samples):
       z_p_te, z_n_te = get_two_scores_count(bag, top_k_index)
       test_predicted_scores_pos[i] = z_p_te
       test_predicted_scores_neg[i] = z_n_te

   # in C1 you only use one dataset, so I use two flags to decide if I should use the positive or negative (I use the larger class) and set the other to 0
   beta1, beta2 = 1, 1
   beta2 = 0
   train_predicted_scores = beta1 * train_predicted_scores_pos + beta2 * train_predicted_scores_neg
   auc_train = roc_auc_score(train_labels, train_predicted_scores)
   print(auc_train)
   best_beta = 1
   if (auc_train < 0.5):
       beta1 = -beta1
       beta2 = -beta2

   test_predicted_scores = beta1 * test_predicted_scores_pos - beta2 * best_beta * test_predicted_scores_neg
   end_time = time.time()
   ```
In C1.py, the author computes the statistical results  from ***Feature_props*** and identifies significant features based on the p-values stored in ***stat_train[:, 1]***. According to the paper, the author's intention is to store in ***top_k_index*** which features belong to ***PF*** (associated with positive bags) and which features belong to ***NF*** (associated with negative bags). The positive or negative sign stored in ***top_k_index*** affects the subsequent ***z_p_tr*** and ***z_n_tr***, which corresponds to nearly all the classifier equations  in the paper.

When constructing the classifier C1 using PF, the authors state in the paper that they take the mean of all feature attributes in both positive and negative bags in the training set, and then perform statistical comparisons of feature attributes between the positive and negative groups using t-tests. Features with p-values below a certain threshold are selected as important features, as stated in line 136-140 of the original text:"Features with a p-value below a threshold, or simply the top M most significant features (p and M are optimized
per dataset on the training set) are selected (further denoted as SF). Each significant feature is associated with the class where its average (median) is highest (further defined as positive features PF and negative features NF)". In my opinion, the author made a factual error in the implementation of  ***top_k_index***. To further illustrate this error, I verified the official function example provided by Scipy. It confirms that stats.ttest_ind returns a structure Ttest_indResult(statistic, pvalue), where ***stat_train[:, 0]*** corresponds to the statistic and ***stat_train[:, 1]*** to the p-value. This is also verified by the author in MILCA/C1.py, line 18. On MILCA/C1.py, line 22, I assume the author's intention might have been ***top_k_index[i] = np.sign(stat_train[i, 2])***, to store whether each significant feature associates with ***PF*** or ***NF***. However, the actual implementation subtracts the p-value from the statistic, ***stat_train[i, 1] - stat_train[i, 0]***. This might be a mistake, as I do not understand the rationale of subtracting the statistic  from the  p-value, because they represent different concepts and scales, and such operation lacks statistical support.  This operation is the same in all the experiments of experiments C1, C2, and C3. When you select the feature attributes in a wrong way, the reliability of the subsequent conclusions cannot be verified. I would welcome the author to further clarify his/her thoughts on this point to provide more reliability. 

***Limitation***:The author's algorithm first requires the feature attributes to be highly indicative. In my opinion, MILCA may be useful only when each dimension of the feature attributes must be strictly preprocessed(Figure 1.A) to have clear statistical significance. In most current real-world scenarios, I cannot think of practical applications apart from simplest cases like the bag of words or other simple handcrafted benchmarks. In many real applications(i.e. cancer diagnosis,anomaly detection), the feature attributes may have the following characteristics:

L1.Inconsistent scale: This can lead to some attributes having intrinsically larger ranges of variation than others. For example in C2,  simply summing these attributes may result in significant biases.

L2.Attributes cannot independently indicate positive or negative correlations: Unless features are manually analyzed and highly processed, or in the case of simple data like bag-of-words models, it's hard to imagine some common scenarios where this is applicable.

L3.Correlation among attributes: Many tasks can only provide deep features, which do not have simple independent relationships. The evaluation of these feature attributes by the algorithm may be biased.

I'd welcome the authors to present their strategies for addressing these limitations above, because these limitations are pretty common in any real-world application.

***Contribution***: The contributions of the paper are actually based on the analysis of feature attributes. I believe this is not a new concept[1], and this approach is not highly relevant to multiple instance learning. Also, I would like the author to explicitly clarify the novelty and substantial  advancement when compared with the paper[2]. Currently for me it's hard to say that the author's research essentially advances the field of multiple-instance learning.

### Questions
No more questions here. More clarifies about Weaknesses are welcome.

### Soundness
1

### Presentation
2

### Contribution
1
