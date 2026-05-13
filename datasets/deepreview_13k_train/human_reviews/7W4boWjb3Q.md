# Partitioned-Learned Count-Min Sketch

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
We propose Partitioned Learned Count-Min Sketch (PL-CMS), a new approach to learning augmented frequent item identification in data streams. Our method builds on the learned Count-Min Sketch (LCMS) algorithm of Hsu et al. (ICLR 2019), which combines a standard Count-Min Sketch frequency estimation data structure with a learned model, by partitioning items in the input stream into two sets. Items with sufficiently high predicted frequencies have their frequencies tracked exactly, while the remaining items, with low predicted frequencies, are placed into the Count-Min Sketch data structure. 
 
Inspired by an approach of Vaidya et al. for learning augmented Bloom filters (ICLR 2021), our PL-CMS algorithm partitions items into different sets, based on multiple predicted frequency thresholds. Each set is handled by a separate Count-Min Sketch data structure. Unlike classic LCMS, this allows the algorithm to take advantage of the full prediction space of the learned model. We demonstrate that, given fixed partitioning thresholds, the parameters of our data structure can be efficiently optimized using a convex program. Empirically, we show that, on a variety of benchmarks, PL-CMS obtains a lower false positive rate for frequent item identification as compared to LCMS and standard Count-Min Sketch.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In their paper, the authors introduce a novel approach for efficient heavy hitter frequency estimation, referred to as PL-CMS, which leverages a learned Count Min Sketch (CMS) technique across multiple score partitions generated from a trained model. This method builds upon prior research, notably the 'Learned Count Min Sketch' (LCMS), which employs a single score threshold, as well as the work of Dai and Shrivastava (2020) and Vaidya et al. (2020), where multiple partitions are utilized for a learned Bloom filter.

The key advantage of PL-CMS is its ability to achieve lower false positive rates while adhering to specific space constraints. The authors demonstrate the effectiveness of their approach through experiments conducted on four real-world datasets.

### Strengths
1. PL-CMS performs better with lower False Positive Rates compared to LCMS and CMS.
2. The approach although derived and inspired from the existing works, fills are right gap in the literature of learned CMS structures.
3. The theoretical analysis provided an upper bound on False positive rate.

### Weaknesses
1. The solution is a simple extension of Dai and Shrivastava (2020) and Vaidya et.al. (2020) for LCMS. In my opinion it discounts the novelty. However it is not a strong criticism against the paper.
2. Fig 2 legends will help.
3. The choice of parameters are not well explained (page 7 para 4 and Section 4.5). How does that relate to Fig 2?
4. page 7 para 4- “We ignore the space of the learned model itself, which is lower order is our settings”. Please provide space taken by model and CMS tables together for each dataset to justify the statement.

### Questions
1. Comparison with other 2 methods of Zhang et. al. (2020): The paper hinted that their approach involves highly accurate learned model and hence omitted for comparison. Are there ways to compare them on equal grounds?
2. What is the model size for LCMS and PL-CMS for each datasets? Can we train them to achieve similar accuracy levels as in Zhang et. al. (2020)? What are the bottlenecks?
3. Is the code available for replication of plots/results?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the frequency estimation problem in the learning-based setting where we aim to improve the performance of algorithms with the help of machine learning prediction. In the previous work of (Hsu et al. 2019), the main idea is to use the machine learning method to participate items into two sets. Items with sufficiently high predicted frequencies have their frequencies tracked exactly, while the remaining items, with low predicted frequencies, are placed into the Count-Min Sketch data structure. In this work, the authors extend this idea and propose the partitioned learned count-min sketch(PL-CMS) where the algorithm partitions the items into multiple ranges based on the prediction. The paper studies how to set the threshold of each range to make the performance of the algorithm better formally (in this paper,  the estimation error metric is different where the authors aim to improve the false positive rate of identifying the heavy items). The experiments also show the advantages of the proposed algorithm.

### Strengths
1. The theoretical contribution of the paper is solid. The idea of extending the prediction to multiple ranges is natural. However, the analysis of how to set the thresholds of each range is not clear. The paper gives a formal analysis of this.

2. The presentation of the paper is clear and easy to follow.

### Weaknesses
1. The paper does not give a study of the cases when the machine learning prediction is noisy, which is one of the central parts of the previous works. In this work, we want to partition the items into multiple ranges, hence the requirement of the prediction precisions is even higher and the study of the algorithm using the noisy prediction is even more important. 
(one related model in [1] is rather than predict the range each item will be in, we instead assume the prediction can give an approximation of the frequency of each item. with an alpha additive error and beta multiplicative error)

2. The paper's analysis focuses on optimizing space allocation based on predicted item frequencies, but it lacks a rigorous investigation into how prediction errors directly impact the final false positive rate. While the algorithm might adapt to some degree, a formal analysis relating the magnitude of prediction error to the resulting estimation error is missing. For example, if the prediction model consistently overestimates the frequency of a subset of items, how does this affect the space allocation and the overall false positive rate, compared to a scenario where the prediction errors are more uniformly distributed?

### Questions
1. In this paper, the definition of the heavy items we are interested in is the i such that $f_i \ge n/k$. In a number of the works, the heavy hitter also be defined as $f_i \ge \sum_j f_j / k$, can the analysis in this work be extended to this model?

2. In the experiments, the authors study the performance of the algorithm using both the ideal prediction and the noisy prediction. The result shows that there are still some gaps in performance between the two cases. I think it would be an interesting part if the author could give an (brief) analysis of the precision of the current prediction.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how to partition the stream into multiple region and process each local region with a Count-Min Sketch. Heavy hitters and frequent items are important tasks in streaming setting and have many applications. The authors provide both theoretical analysis and experimental studies to showcase the proposed algorithm outperforms the baseline in many cases.

### Strengths
The main idea of this paper is sound and intuitive. In fact many other sketching algorithm (not learned) leverage the same idea. Some recent works in the space are AugmentedSketch, ElasticSketch, and Panakos.

The theory analysis is well written and friendly to readers. The analysis looks correct to me.

The parameter optimization method is interesting and may lead to broader impact.

### Weaknesses
The main idea of this paper is sound and intuitive. In fact many other sketching algorithm (not learned) leverage the same idea. Some recent works in the space are AugmentedSketch, ElasticSketch, and Panakos.

The theory analysis is well written and friendly to readers. The analysis looks correct to me.

The parameter optimization method is interesting and may lead to broader impact.


AOL dataset is subject to controversy. I would recommend the author to remove experimental results about AOL. (https://en.wikipedia.org/wiki/AOL_search_log_release)

Author may want to clarify the assumption on the stream and compare with some other popular summaries in the experiments to indicate the benefits of learning. If the stream is in insertion-only or in bounded-deletion model, then author should compare with the SpaceSaving algorithm. (see https://arxiv.org/pdf/2309.12623.pdf and https://arxiv.org/abs/1803.08777). If the stream is in turnstile model, then the author should include comparison with Count Sketch (Charikar, Moses, Kevin Chen, and Martin Farach-Colton. "Finding frequent items in data streams.").

I might have missed it. How is the score $l_i$ decided and is it learned in training? For instance, in Macbeth, the proposed algorithms use threshold 200|100, and 300|200|100.

### Questions
See weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to incorporate learned information to improve the performance for the count-min sketch (for the heavy-hitter analysis task in data streams). In particular, the algorithm receives a prediction of the frequency of input items, and it utilizes this info to build a separate data structure for items with similar (predicted) frequencies via a simple thresholding strategy. Indeed, if this partition of the data is good enough (which means items of similar frequency are put in the same parts), then it can achieve a better accuracy-space tradeoff compared with a generic count-min sketch. Similar ideas have been considered in recent papers such as Vaidya et al. (ICLR 2021) which studied bloom filters.

### Strengths
I think that the general idea of having separate count-min sketch for items of similar frequency is nice, and it is convincin that this could improve the performance (provided that the prediction is accurate). In addition, the experiment results seem to be promising. In particular, it looks like even with a relatively simple and weak prediction, the proposed algorithm can already achieve significant improvement over baselines on various data sets.

### Weaknesses
- The algorithm needs additional information than the estimated frequency of items, particularly the E_i F_i parameters are only artifacts of your algorithm instead of something natural to the heavy-hitter problem

- The robustness (i.e., what happens if the prediction is completely wrong) is not discussed/evaluated. Indeed, one major motivation for algorithms with predictions is to utilize ML predictions while still preserving the worst-case guarantee.

- It would also be better to have a measure of the prediction error, as well as relate the performance of your algorithm to that error measure to obtain a smooth tradeoff between robustness and consistency.

- I also see some technical issues, and please find the detailed comments in the "Questions" section.

- It seems your E_i and F_i are dependent on the thresholds t_i’s. However, it seems you need to estimate E_i and F_i, and then use them to find the t_i’s. This does not make sense to me.

- Page 4, “which region is falls in” -> “which region it falls in”

- Page 4, item 1 in Sec 2.2 has unpaired parenthesis

- Page 6, third paragraph. Can you give more intuition on why the theoretical upper bound does not work well? Is there any rationale for introducing a p in the exponent? This way of adding a new parameter seems quite random to me.

- In page 6 you mentioned that using larger number of score thresholds typically does not improve the performance — why is this? Also, this somewhat contradicts the claim in Section 5, where you mention that “determining the optimal number of partitions is a crucial next step that can significantly enhance its performance”.

- Page 7, why the space of the learned model is of the lower order so that it can be ignored?

- Only the arXiv version of Vaidya et al., ICLR 2021 paper is cited — consider citing the conference version. Please also check this for other references.

- Several references do not have their venues listed, for isntance Chabchoub et al., 2009 and Dolera et al., 2022.

### Questions
- It seems your E_i and F_i are dependent on the thresholds t_i’s. However, it seems you need to estimate E_i and F_i, and then use them to find the t_i’s. This does not make sense to me.

- Page 4, “which region is falls in” -> “which region it falls in”

- Page 4, item 1 in Sec 2.2 has unpaired parenthesis

- Page 6, third paragraph. Can you give more intuition on why the theoretical upper bound does not work well? Is there any rationale for introducing a p in the exponent? This way of adding a new parameter seems quite random to me.

- In page 6 you mentioned that using larger number of score thresholds typically does not improve the performance — why is this? Also, this somewhat contradicts the claim in Section 5, where you mention that “determining the optimal number of partitions is a crucial next step that can significantly enhance its performance”.

- Page 7, why the space of the learned model is of the lower order so that it can be ignored?

- Only the arXiv version of Vaidya et al., ICLR 2021 paper is cited — consider citing the conference version. Please also check this for other references.

- Several references do not have their venues listed, for isntance Chabchoub et al., 2009 and Dolera et al., 2022.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
