# Towards Efficient and Accurate Identification of Memorization in Deep Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6

## Abstract
\textit{Memorization} is the ability of deep models to learn verbatim arbitrary inputs from the training data. One of the most popular means of calculating memorization scores (i.e., the probability that a point is memorized) is via the pseudo Leave-One-Out (pLOO) method proposed by~\citet{feldman2020longtail}. However, this technique suffers from two shortcomings: it is computationally prohibitive (as it requires training thousands of models) and it produces inaccurate scores. The goal of this work is to overcome both these limitations simultaneously. To do so, we take the following approach: \textbf{First}, we demonstrate that the major source of pLOO's computation bottleneck is its execution on the entire dataset, not just the memorized points. We find running pLOO on all the points is unnecessary since most of them are not even memorized. \textbf{Second}, we develop a simple proxy to identify the memorized points without having to run pLOO in the first place. To do so, we study the model training cycle and find that memorized points are learned towards the last iterations. We build a simple proxy based on this observation and find that our proxy: \textit{a)} is strongly correlated with the actual memorization scores (Pearson score $<-0.95$) across all our models and datasets and \textit{b)} requires only a single model (instead of the thousands needed by pLOO). However, our proxy does not provide the exact memorization scores. \textbf{Third}, to calculate these, we incorporate our proxy into the pLOO method, resulting in pLOO\textsubscript{\textit{improved}}. In doing so, we show that our pLOO\textsubscript{\textit{improved}} reduces both computational overhead (by over 90\%) and the error in the approximated memorization scores (by over 65\%). Therefore, our work makes it possible to study memorization in large datasets and real-world models while requiring only a fraction of the computational resources.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses computational and accuracy limitations in measuring memorization through the "pseudo-leave-one-out" (pLOO) (Feldman & Zhang, 2020). The key idea is to leverage an insight that data points that are memorized tend to be misclassified in early training stages and only correctly classified in later stages. Based on this observation, the authors propose a proxy metric termed Accuracy per Batch (ApB) to identify candidate memorized training points. (This could also be used as a heuristic to detect memorized points.) Using these proxy scores, they develop a more efficient sampling strategy for pLOO, achieving a 90% reduction in computational cost and a 65% reduction in error.

### Strengths
- The paper is well-written, has clear motivation, and presents valuable contributions to the ICLR community.
- The insights are novel and can be practically significant, with the proposed ApB metric demonstrating improved efficiency and accuracy compared to pLOO.

### Weaknesses
 - Several writings in the paper lack technical justification. For example, the intuition presented in Section 2 lacks technical rigor. While the authors demonstrate convincing empirical results on image classification tasks to support their claims, its applicability or generability to other domains remains uncertain. It would be useful to extend the analysis (e.g., memorized data points have a high loss at the early stage of training and a low loss at the later stage) on simpler models such as linear regression to gain technical insights. Although I believe that extensive theoretical analysis is not required to meet the bar for ICLR presentation, this is certainly one weakness of the paper.
- The authors’ claim that the memorized points constitute a small fraction of training data seems to be overly specific to certain datasets and architectures. In extreme cases, such as when all labels are randomized (e.g., [1]), the model must memorize all points to obtain 100% training accuracy. I believe that the authors’ claim can be generally true for academic datasets with no label noise but might not hold in more practical (or broader) settings.
- The limitations of the proposed approach are not sufficiently discussed. While pLOO offers general applicability across various settings (e.g., we can train the models on various subsets of the dataset), including more non-typical settings like continual learning scenarios, it's unclear how ApB can be extended to non-standard settings. For example, ApB will assign a high memorization probability to all data points that appeared in the last task.
- Another concern is that the authors treat noisy LOO estimates as ground truth. LOO has known reliability issues in machine learning [2], which may affect the conclusion and results of the paper. The pLOO provides guarantees based on the number of models trained (in the infinite limit), suggesting that a more appropriate baseline would be pLOO with an increased number of retraining rather than relying on potentially unreliable baseline measures. In addition, ApB does not offer such a guarantee since it produces a bias in the data selection process, which can be another limitation.
- The experimental setup lacks sufficient detail for reproducibility (e.g., learning rate and batch size used).

### Questions
(I’ve included additional suggestions as well as the questions.)
- I feel like several claims in the paper are overstated. For example, line 58's claim about requiring "hundreds of thousands of models, computationally intractable" contradicts existing literature showing this has been done on CIFAR-10 (e.g., [3]). (It is technically not intractable.) Similarly, line 230's comment about pLOO's inapplicability to production models raises questions about the method's broader applicability for obtaining memorization scores.
- The examples in lines 157-161 appear redundant and could be omitted.
- Could the authors provide a precise definition of ApB in Section 4.3?
- Do the authors think the insights presented in this paper hold for other settings (e.g., regression or language models)?
- (Minor) There are several instances of incorrect usage of \citet and \citep.
- (Minor) The phrase "in short" is repeated in line 113.
- (Minor) Line 241 should say "a small fraction of the dataset" rather than just "a fraction."
- (Minor) Section(5) contains formatting issues at line 377.

[1] What Do Neural Networks Learn When Trained With Random Labels? [2] A Bayesian Approach To Analysing Training Data Attribution In Deep Learning [3] Datamodels: Predicting Predictions from Training Data

### Soundness
2

### Presentation
2

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
To mitigate the computation cost of identifying memorized points in deep neural networks, this paper proposes a heuristic meric, ApB, to efficiently identify memorized points and accurately calculate the memorization scores. With incorporating pLOO method by running pLOO only on the points filtered by ApB, empirical experiments show that the proposed method, compared with pLOO, can reduce the computational cost by over 90%  and improve accuracy by over 65%.

### Strengths
1.	The presentation is easy to follow and understand.

2.	The paper propose to reduce computing cost of identifying memorized points by only evaluating a fraction of samples, filtered by ApB, which is straightforward, efficient and effective.

### Weaknesses
1.	In this paper, the motivation of studying identifying memorized points and related works are not well presented, making it difficult to understand the position of the paper in the literature and the impact of the paper. Some more details are needed, like why identification of memorization is important and some more works related to identifying memorization.
2.	The main hypothesis studied in this paper, “Generalized points are learned faster than memorized ones during training”, was extensively studied and verified in the literature, like [1][2]. The only contribution of this paper is introducing a heuristic metric ApB to filter some points to identify memorized points.

3.	The definition of the metric ApB is not clear. It’s better to define it mathematically.  To my understanding, after every epoch, it does inference for every examples in the training dataset, then calculate the ration of being correct for each samples over all the epochs. Please help confirm if my understanding is correct?
4.	In section 4.1, what method is utilized to obtain memorization scores? LOO? pLOO? And in section 4.2, how the labels are obtained, for generalized points and memorized points?
5.	In figure 1, that “CIFAR-10 has consistently fewer memorized points across all models compared to CIFAR-100” may be because each class in CIFAR10 has more samples(5k) than CIFAR100(500), since it’s known that classes with fewer samples will lead to more memorized points, such as the example in line 193.
6.	Almost all the figures are overwide and need to be re-organized. Moreover, please refer to template instructions to use \citet and \citep appropriately.

### Questions
1.	The definition of the metric ApB is not clear. It’s better to define it mathematically.  To my understanding, after every epoch, it does inference for every examples in the training dataset, then calculate the ration of being correct for each samples over all the epochs. Please help confirm if my understanding is correct?
2.	In section 4.1, what method is utilized to obtain memorization scores? LOO? pLOO? And in section 4.2, how the labels are obtained, for generalized points and memorized points?
3.	In figure 1, that “CIFAR-10 has consistently fewer memorized points across all models compared to CIFAR-100” may be because each class in CIFAR10 has more samples(5k) than CIFAR100(500), since it’s known that classes with fewer samples will lead to more memorized points, such as the example in line 193.
4.	Almost all the figures are overwide and need to be re-organized. Moreover, please refer to template instructions to use \citet and \citep appropriately.

### Soundness
3

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
This paper studies the memorization ability of neural networks by proposing an efficient approximate method to identify memorized points and consequently calculate the memory score. The development is based on the observation that memorized points are learned towards the end of the training cycle. Imperical results indicate that the proposed method can accurately predict the memorization scores by reducing the computational overhead by over 90%.

### Strengths
The paper focus on a sub-problem in the pLOO paper, which is to define efficient method to estimate the memorization ability of neural networks. The paper is in general written clearly. The problem of estimating the memorization ability of neural network is important to understand some properties of neural networks. The proposed method is intuitive and efficient.

### Weaknesses
I feel the paper in general is not complete. The current version explains the problem and proposes an efficient solution based on an intuition of the training dynamic of neural networks. Although the explanation is clear, most of the definitions and problem settings have been proposed by previous works. I think there are more work to be done to make the paper more complete. For example, more experiments need to be conducted to verify the effectiveness and usefulness of the proposed method. The authors should at least follow the experimental setting in the pLOO paper to make the experimental part richer and more extensive. The current experiments are too simple to drawn conclusions from.

Furthermore, if possible, a theoretical explanation on the proposed method would make the paper more solid.

### Questions
Please refer to the weaknesses part.

### Soundness
2

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
5

### Summary
This paper seeks to understand and detect memorization of deep neural networks. The authors wish to improve upon prior work, that was computationally too expensive to scale to large-scale datasets and models. The key observation is that outliers are most likely to be memorized, as they are not a part of the generalizable portions of the dataset (that is characterized by many similar samples). Further, the outliers that are likely to be memorized are learned late in the training process. Using this idea they are able to detect which samples are most likely to be memorized, thereby reducing the number of samples that need be carefully analyzed for memorization (reducing computational cost). They also show improved results relative to pLOO, which needs to make approximations for computational efficiency, which here are shown to possibly introduce high errors. So the proposed approach is deemed by the authors both computationally faster and also more accurate in detecting memorized training samples.

### Strengths
The ideas in this paper are sound, and the experimental results are convincing.

### Weaknesses
The ideas in this paper are sound, and the experimental results are convincing.

The main criticisms are on the writing. Generally the paper is written well, but there are places where much improvement is needed. See below for details.

1. Please define what a "shard" is. The reviewer understands what is meant, but it would be good to define this term, so there is no ambiguity.

2. More important:

- On p. 3, it is written "In short, our method is not only faster than pLOO, but also
more accurate as well. In short, our method is both significantly faster and more accurate than
pLOO, the most popular method for finding memorized points in current literature.
In short, our work makes the following contributions:"
This is three consecutive sentences that begin "In short," which is very poor. And worse, the first and second sentences are essentially duplications.

- On p. 4, "In other words, we train 2000 instances of each of the models (i.e., 1000 models where xi is present
and 1000 models where xi absent from the training data ). 100% models output the ground-truth
label for xi (i.e., all 1000 instances classified the point correctly). However, once xi is removed
from the training data, 25% of the models assign xi the ground-truth label (i.e., 250 out of the 1000
instances classified the point correctly). The resulting memorization score is 100%−25% = 75%."
There is a lot of detail here for a fairly simple concept. Also, I assume you do not always train 2000 instances, but this is an example. I guess better would be, "In other words, *if* we train 2000 instances ..." This is just an example. The writing generally can be made a bit more serious technically.

- Which brings me to the issue of cats. There seem to be a fixation with cats. At the bottom of p. 3 and top of p. 4 there are discussions of cats and outliers. Then again at the middle of p. 4. Cats are also mentioned in the Introduction. This is a minor point, but it distracts the reader, because the discussion becomes somewhat casual, and kinda assumes the reader knows something about the "history" of cats in ML. I suggest trying to use less casual writing.

- At the beginning of Sec. 4.3 you state you have "validated" your hypothesis. I think this is a strong statement. I think you have found *evidence* for your hypothesis, but I am not sure you have validated it.

- In the middle of p. 9 you begin a paragraph "In this work, ..." and then at the beginning of the Conclusions you also begin as "In this work, ...." This is small, but it is indicative of a need to improve the writing in small ways throughout the paper.

### Questions
1. Please define what a "shard" is. The reviewer understands what is meant, but it would be good to define this term, so there is no ambiguity.

2. More important:

- On p. 3, it is written "In short, our method is not only faster than pLOO, but also
more accurate as well. In short, our method is both significantly faster and more accurate than
pLOO, the most popular method for finding memorized points in current literature.
In short, our work makes the following contributions:"
This is three consecutive sentences that begin "In short," which is very poor. And worse, the first and second sentences are essentially duplications.

- On p. 4, "In other words, we train 2000 instances of each of the models (i.e., 1000 models where xi is present
and 1000 models where xi absent from the training data ). 100% models output the ground-truth
label for xi (i.e., all 1000 instances classified the point correctly). However, once xi is removed
from the training data, 25% of the models assign xi the ground-truth label (i.e., 250 out of the 1000
instances classified the point correctly). The resulting memorization score is 100%−25% = 75%."
There is a lot of detail here for a fairly simple concept. Also, I assume you do not always train 2000 instances, but this is an example. I guess better would be, "In other words, *if* we train 2000 instances ..." This is just an example. The writing generally can be made a bit more serious technically.

- Which brings me to the issue of cats. There seem to be a fixation with cats. At the bottom of p. 3 and top of p. 4 there are discussions of cats and outliers. Then again at the middle of p. 4. Cats are also mentioned in the Introduction. This is a minor point, but it distracts the reader, because the discussion becomes somewhat casual, and kinda assumes the reader knows something about the "history" of cats in ML. I suggest trying to use less casual writing.

- At the beginning of Sec. 4.3 you state you have "validated" your hypothesis. I think this is a strong statement. I think you have found *evidence* for your hypothesis, but I am not sure you have validated it.

- In the middle of p. 9 you begin a paragraph "In this work, ..." and then at the beginning of the Conclusions you also begin as "In this work, ...." This is small, but it is indicative of a need to improve the writing in small ways throughout the paper.

### Soundness
3

### Presentation
2

### Contribution
3
