# TabM: Advancing tabular deep learning with parameter-efficient ensembling

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Deep learning architectures for supervised learning on tabular data range from simple multilayer perceptrons (MLP) to sophisticated Transformers and retrieval-augmented methods.
This study highlights a major, yet so far overlooked opportunity for substantially improving tabular MLPs: namely, parameter-efficient ensembling
--- a paradigm for implementing an ensemble of models as one model producing multiple predictions.
We start by developing \model\ --- a simple model based on MLP and our variations of BatchEnsemble (an existing technique).
Then, we perform a large-scale evaluation of tabular DL architectures on public benchmarks in terms of both task performance and efficiency, which renders the landscape of tabular DL in a new light.
Generally, we show that MLPs, including \model, form a line of stronger and more practical models compared to attention- and retrieval-based architectures.
In particular, we find that \model\ demonstrates the best performance among tabular DL models.
Lastly, we conduct an empirical analysis on the ensemble-like nature of \model.
For example, we observe that the multiple predictions of \model\ are weak individually, but powerful collectively.
Overall, our work brings an impactful technique to tabular DL, analyses its behaviour, and advances the performance-efficiency \mbox{trade-off} with \model\ --- a simple and powerful baseline for researchers and practitioners.
The code is available at: \url{\repository}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose TabM, a variation of an MLP with $k$ heads that uses a shared backbone, and only certain aspects of the architecture in the beginning  and in the end are specialized. The heads are trained independently. The work is compared with prior DL methods (plain and attention architectures), retrieval-based methods, and tree-based methods on a diverse collection of classification and regression tasks. Based on the results, the proposed method manages to outperform all baselines with tuned hyperparameters.

### Strengths
- The proposed method achieves better performance compared to the other methods with tuned hyperparameters. 
- The set of considered baselines is extensive.
- Extensive results on classification/regression datasets. Additionally, results are provided on well-known benchmarks in the domain.
- The authors provide extensive ablations of the different components of the method. The authors additionally provide a time comparison of the different methods.

### Weaknesses
- The work is difficult to read, the captions of Figure 2 and Figure 3 are long and blend with the core manuscript text, making it hard to keep track of the manuscript flow.

### Questions
- Table 2, for the MLP (Maps Routing dataset) the time unit is missing. I am guessing it is 10 minutes.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper come up with an efficient ensembling method for tabular deep learning — which integrate BatchEnsemble with multilayer perceptron. This method exhibits great improvements in their benchmark.

### Strengths
- [Major] This method is simple yet effective.
- [Major] The paper is easy to read.

### Weaknesses
- [Medium] The proposed method is not much novel. Note that this concern is not the main reason that I chose to reject this paper. If other concerns listed can be addressed (e.g., more technical contributions, comprehensive empirical study for depper understandings), I think this paper is still very useful.
- [Major] More experiments are needed to fully understand the behavior of TabM. In the abstract, the authors mentioned “we show that parameter-efficient ensembling is not an arbitrary trick, but rather a highly effective way to reduce overfitting and improve optimization dynamics of tabular MLPs.” However, in the paper, there is no discussion why TabM helps with reducing overfitting and optimization dynamics. Of course the experiments proves this, but it seems like a general benefits of ensemble models. At least, some explanation supported by experiments is needed to fully understand this method — especially this method is already very simple and not much novel, understanding this better is important to have sufficient technical contribution.
- [Major] Baselines missing. This method is an ensemble method. At least we could compare it to other naive ensemble method. For instance, how much speed up it provides compared to normal ensemble; how robust it compared to normal ensemble; etc.
- [Major] Datasets missing. Yes this paper test on many datasets — but the more important thing is the diversity. For instance, how about high-dimensional datasets and large datasets (I know it is on Table 2, but only evaluated on two datasets and three baselines, moreover, only TabMmini has been evaluated). I suggest the authors to use TabZilla hard benchmark, and then evaluate the method’s capability under different circumstances. These kind of experiments can make the findings more interesting.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes TabM, a deep learning model for tabular data based on MLP enhanced with BatchEnsemble, along with custom modifications designed to improve the model's efficiency and performance. The authors position TabM as an efficient alternative to more complex architectures like Transformer-based models, claiming it achieves superior performance without their added computational cost. The paper also provides a detailed analysis, suggesting that parameter-efficient ensembling can effectively address overfitting and improve optimization dynamics in tabular MLPs.

### Strengths
1. The paper is well-structured and clearly written, making the methods, results, and analysis easy to understand.
2. TabM demonstrates competitive performance, positioning it as an efficient alternative for tabular data modeling.
3. By introducing BatchEnsemble techniques into tabular data modeling, the authors have adapted and enhanced a previously underutilized approach in this domain.
4. The paper provides a thorough analysis of each component's impact on model performance, contributing valuable insights.

### Weaknesses
1. Although the authors mention similar methods, a more detailed comparison with other related approaches for tabular data, such as Trompt, would be helpful. Despite structural differences, both methods share commonalities in prediction, such as averaging multiple head (cycle) outputs and summing losses across heads (cycles). 
2. Comparisons with standard ensemble methods are insufficient. Incorporating results from methods like model soup could help position TabM's performance.
3. Dataset scope is somewhat limited, particularly for classification tasks. For a more comprehensive evaluation, the authors might consider incorporating the datasets from Tabzilla, which could provide richer classification benchmarks and enable a more detailed analysis, such as comparing performance across binary, multiclass, and regression tasks or evaluating model performance on datasets of varying sizes.

[1] Kuan-Yu Chen, Ping-Han Chiang, Hsin-Rung Chou, Ting-Wei Chen, Tien-Hao Chang: Trompt: Towards a Better Deep Neural Network for Tabular Data. In ICML

[2] Duncan C. McElfresh, Sujay Khandagale, Jonathan Valverde, Vishak Prasad C., Ganesh Ramakrishnan, Micah Goldblum, Colin White: When Do Neural Nets Outperform Boosted Trees on Tabular Data? In NeurIPS

### Questions
1. In Table 2 (p.10), the last column of the MLP row lists "10." Could the authors confirm if it is measured in minutes, as there’s no unit mentioned?
2. In line 1027, the authors state, *For numerical features, by default, we used a slightly modified version of the quantile normalization from the Scikit-learn package, with rare exceptions when it turned out to be detrimental.* Could the authors clarify how they define “detrimental” in this context and provide further explanation?
3. Could the authors provide more detailed diversity metrics for the predictions of the 32 base models?
4. Line 431 notes, *Interestingly, the best prediction head of TabM performs no better than the plain MLP.* Would an ensemble of 32 independently and undertrained MLPs yield similarly strong performance?
5. The ranking method used is unconventional. Is this ranking method novel to this paper? Could the authors also provide results for a more traditional average rank metric to facilitate comparison, as it would be interesting to see how these two measures differ?
6. One advantage of using deep learning for tabular data is the ability to generate embeddings that are useful for downstream tasks and multimodal learning. How does TabM determine the representation of each sample? Is it based on concatenation, averaging across base models, or some other method? Additionally, could the authors provide a comparison of TabM’s embeddings with those from other deep learning approaches on specific tasks to showcase their effectiveness?

---
Lastly, if the authors can address the concerns noted in the weaknesses and questions, I will consider raising my score accordingly.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper applies the BatchEnsemble technique to MLPs for tabular data, and investigates several modifications. The results show an improvement over MLPs and several deep baseline models and GBRT on a broach benchmark of 50 datasets from the literature. The experiments show that in the first adapter layer in particular is extremely critical, and results in the majority of gains.

### Strengths
The paper discusses the adoption of the BatchNorm architecture for the tabular setting, and describes several interesting ablations.
The empirical evaluation is broad and in-depth and well presented.
The empirical results are quite strong against a broad variety of baselines.
The paper is well written.

### Weaknesses
- The technical novelty of the paper is somewhat small; however, this is made up for by the in-depth analysis with somewhat surprising results and the good performance of the proposed model.
- The paper doesn't describe the relationship to dropout, even though dropout was original describes as an efficient ensemble approach. Given the simple nature of TabM_mini, there seem to be some obvious parallels between drop-out and TabM_mini that I think are worth discussing. In particular, TabM_mini actually contains a dropout layer, and it would be interesting to evaluate how the two forms of ensembling complement each other.
- The comparison doesn't include TabPFN, an extremely strong baseline. McElfresh showed that even subsampling data to at most 3000 datapoints, TabPFN outperforms most other models.
- Given the focus on improving MLP performance, a comparison with regularization cocktails and "Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data" might be relevant but not essential.
- Given the somewhat surprising result about the importance of the initial adapter, it would be great to have more ablations on the different components. In particular, it's unclear in how far the initial adapter and last layer are coupled. How does the performance change if the best performing last layer is used for all the initial adapters? I.e. are the initial layer and last layer co-adapted or do they work independently? 

## Minor comments
Figure 2 cuts off points at 8%. It seems there's a lot of points on exactly that line, which seems a bit suspicious. Are these all the outliers that are clipped to the limits of the figure? It would be great to indicate outliers in the plot.

Table 2 is far below the mention and maybe should be moved up.

Table 2, MLP on the Maps dataset is missing units in duration.

The title of section 5.3 should read "How does the performance of TabM depend on k?"

Line 257: "requires a special care" should be "requires special care"

Line 160: multiplication with 100% is not mathematically meaningful.

### Questions
- Are number of layers for MLP and TabM tuned as hyper-parameters? What are typical values for each?

- Why is k not included in the hyper-parameter search for TabM?

- How do you ensure diversity for the MLPs in the ensemble in Figure 6?

- How do you initialize the last layers in TabM to ensure diversity?

- Is it possible that TabM_mini outperforms the real ensemble because of more diversity in the initialization?

- Is it correct that when doing the full ensemble, adding an adapter into each model would lead to an equivalent ensemble? I was wondering why this ablation was not performed, but I assume random initialization of weights for each member of the ensemble makes the adapters irrelevant.

### Soundness
3

### Presentation
3

### Contribution
3
