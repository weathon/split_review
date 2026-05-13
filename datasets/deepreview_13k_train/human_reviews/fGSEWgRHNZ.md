# Adaptively Private Next-Token Prediction of Large Language Models

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
As Large Language Models (LLMs) proliferate, developing privacy safeguards for these models is crucial. One popular safeguard involves training LLMs in a differentially private manner. However, such solutions are shown to be computationally expensive and detrimental to the utility of these models. Since LLMs are deployed on the cloud and thus only accessible via an API, a Machine Learning as a Service (MLaaS) provider can protect its downstream data by privatizing the predictions during the decoding process. However, the practicality of such solutions still largely lags behind DP training methods. One recent promising approach, Private Mixing of Ensemble Distributions (PMixED) \cite{flemings2024differentially}, avoids additive noise by sampling from the output distributions of private LLMs mixed with the output distribution of a public model. Yet, PMixED must satisfy a fixed privacy level for a given number of queries, which is difficult for an analyst to estimate before inference and, hence, does not scale. To this end, we relax the requirements to a more practical setting by introducing Adaptive PMixED (\texttt{AdaPMixED}), a private decoding framework based on PMixED that is adaptive to the private and public output distributions evaluated on a given input query. In this setting, we introduce a noisy screening mechanism that filters out queries with potentially expensive privacy loss, and a data-dependent analysis that exploits the divergence of the private and public output distributions in its privacy loss calculation. Our experimental evaluations demonstrate that our mechanism and analysis \textit{can reduce the privacy loss by $16\times$} while preserving the utility over the original PMixED. Furthermore, performing 100K predictions with \texttt{AdaPMixED} still achieves strong utility and a reasonable data-dependent privacy loss of $\epsilon=5.25$.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To address the limitations of differentially private (DP) training for LLMs, Adaptive PMixED (APMixED) is introduced as a private decoding framework that adapts to the divergence between private and public model outputs. It includes mechanisms to screen high-risk queries and calculate data-dependent privacy loss, achieving practical scalability and strong utility. Experimental results show that APMixED enables up to 100K predictions with reasonable privacy loss, outperforming traditional methods.

### Strengths
Reasonably Novel idea, that reintroduces work from PATE which was largely overlooked. Well structured and the problem is well introduced. See Questions.

### Weaknesses
I think that the general framing of the paper is good, but more work can be done to clarify the specific contributions and algorithms of the paper. For example, I was a bit confused by what the noisy screening method concretely is. Why is it not sparse vector, or confident-GNmax for PATE? Perhaps I missed something but it feels the algorithm could be more clearly specified.  See Questions.

I think this is more up to date with regards to tight bounds for DPSGD : https://www.usenix.org/system/files/usenixsecurity23-nasr.pdf 
“We design an improved auditing scheme that yields tight privacy estimates for natural (not adversarially crafted) datasets—if the adversary can see all model updates during training”

Can you compare for something - create private labels using this method, then train non-privately on those private labels? In order to produce a model that you can ask infinite # of queries. This is what PATE (https://arxiv.org/abs/1802.08908) does, and how it differs from CaPC  (https://arxiv.org/abs/2102.05188).

For the empirical work, why can’t you fix epsilon? Having variable number of queries answered, privacy loss, and PPL changing makes it hard to compare. In PATE methods they tend to compare apples-to-apples, (specifically  epsilon versus label-count versus label accuracy);  like this one : https://arxiv.org/pdf/2202.10517, which isn't relevant in the specific algorithm, but rather in the presentation of epsilon versus label-count versus label accuracy. 

Did you try varying `N` partitions? In PATE this ends up being quite important.

Do you have an assessment of how different the finetuning datasets are from the original model? The degree of dataset-similarity here matters a lot for the performance of DP finetuning algos, though in your defense you are comparing against other methods. Still it would be good to quantify this a bit better.

### Questions
* I think this is more up to date with regards to tight bounds for DPSGD : https://www.usenix.org/system/files/usenixsecurity23-nasr.pdf 
“We design an improved auditing scheme that yields tight privacy estimates for natural (not adversarially crafted) datasets—if the adversary can see all model updates during training”
* Can you compare for something - create private labels using this method, then train non-privately on those private labels? In order to produce a model that you can ask infinite # of queries. This is what PATE (https://arxiv.org/abs/1802.08908) does, and how it differs from CaPC  (https://arxiv.org/abs/2102.05188).

* For the empirical work, why can’t you fix epsilon? Having variable number of queries answered, privacy loss, and PPL changing makes it hard to compare. In PATE methods they tend to compare apples-to-apples, (specifically  epsilon versus label-count versus label accuracy);  like this one : https://arxiv.org/pdf/2202.10517, which isn't relevant in the specific algorithm, but rather in the presentation of epsilon versus label-count versus label accuracy. 

* Did you try varying `N` partitions? In PATE this ends up being quite important.

* Do you have an assessment of how different the finetuning datasets are from the original model? The degree of dataset-similarity here matters a lot for the performance of DP finetuning algos, though in your defense you are comparing against other methods. Still it would be good to quantify this a bit better.


Overall, it seems like a good paper, but I’d like to see the algorithmic contributions to be a bit more explicitly stated in the context of existing work, and I’d like the empirical experiments to be more clearly showing their contribution.

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
This paper introduces AdaPMixED, an algorithm for differentially private (DP) next-token prediction that builds on PMixED which was introduced previously. AdaPMixED improves the practicability of PMixED, where knowing the number of queries beforehand is less likely, by dynamically adapting the privacy level based on the divergence between public and private model outputs. Specifically, AdaPMixED introduces a noisy screening mechanism to filter out queries that might incur high privacy loss, and it performs a data-dependent privacy analysis to assess and adjust privacy loss per query. Experimental results show that AdaPMixED significantly reduces privacy loss compared to PMixED while retaining strong model utility, especially in high-query scenarios.

### Strengths
- The paper is well-written and the evaluation includes comparing AdaPMixED with other DP methods across different datasets. The results demonstrated large privacy gains while maintaining utility, especially in high-query situations.
- The proposed method is clearly explained and simple to implement, making the previous approach PMixED more practical.

### Weaknesses
 - The novelty is somewhat limited where it seems like only the noise screen filtering mechanism is original. The data dependent privacy analysis is an application of an existing approach to PMixED. Though the authors emphasized the importance of noise screen filtering, from the results in Table 2, majority of the privacy loss gain comes from data dependent privacy analysis.
- The model used in experiments (GPT2) seems a bit outdated, it is unclear how the privacy and utility trade-off really look like for the more recent LLMs.
- Experiment details can be explained more, e.g. how is the dataset partitioned and what is used as the public model. I understand that the setup is rather similar to the prior work PMixED but the paper should be self-contained without needing to check another paper for the setup. Some minor detailed results are missing in table 1, e.g. PMixED results are not shown for PubMed and Air Dialogue.

### Questions
- Is the public model the original pretrained GPT2? How do you make sure that the public model training data does not intersect with the 4 datasets in the experiment? E.g. wikipedia seems to be a rather common pretraining dataset for most public models.
- For the ablation study in Section 5, which dataset is it performed on? How does the optimal hyperparameters change with the underlying dataset?

### Soundness
2

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
The authors explore the challenges of privacy preservation in large language models (LLMs), which are typically deployed via APIs by machine learning as a service (MLaaS) providers. Traditional privacy-preserving methods, such as Differential Privacy (DP) using DP-SGD, often incur significant computational costs, and the increased noise due to privacy preservation can negatively impact the model's utility. The Private Ensemble Distribution Hybrid (PMixED) approach improves utility by mixing the output distributions of private and public models without adding noise, but it suffers from inflexible privacy constraints and does not scale well as the number of queries increases. To overcome these limitations, the authors introduce Adaptive PMixED (AdaPMixED), which dynamically optimizes the trade-off between privacy and utility based on the difference between the private and public output distributions of each query. This approach includes a novel noise filtering mechanism that filters out high-risk queries, as well as data-based privacy loss analysis, allowing for more efficient use of privacy budgets. Experiments show that AdaPMixED significantly reduces privacy loss (up to 16x compared to PMixED) while maintaining or enhancing model utility across a variety of datasets.

### Strengths
The author introduced several important advantages of AdaPMixED in the field of privacy protection LLM. First, AdaPMixED is highly scalable and capable of handling up to 100,000 queries with little impact on privacy and utility, which is a significant improvement over both PMixED and traditional DP methods. This makes it ideal for practical applications where MLaaS is widely used. Furthermore, this method significantly reduces privacy loss by dynamically adjusting privacy parameters based on real-time output distribution analysis. This not only saves the privacy budget but also ensures that the model’s usefulness is preserved, as evidenced by lower perplexity scores in the next token prediction task compared to other methods.

### Weaknesses
In my opinion, a key weakness of the AdaPMixED framework is its handling of situations where there are large divergences between private and public model outputs. In this case, the system defaults to using the output of the public model to reduce privacy risks. However, this situation illustrates that the output of private models is very important and should not be ignored. For example, the private model may provide personalized output that the public model alone cannot provide.

Furthermore, the authors primarily considered real-world usage, but the complexity of AdaPMixED may hinder its practical deployment, especially in MLaaS environments where throughput and latency are critical. The multiple decision-making layers involved in AdaPMixED, from divergent evaluation to dynamic output adjustment, can significantly increase the computational overhead. This complexity can reduce the efficiency of the system, especially under high load conditions typical in MLaaS environments. The authors could add some experiments on the trade-offs between throughput and privacy utility advantages provided by AdaPMixED.

### Questions
Refers to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on privacy-preserving LLMs, where the end goal is to allow untrusted parties to interact with an LLM that has been fine-tuned on a private dataset, while protecting the private dataset with differential privacy (DP). DP next-token prediction is one way of achieving this goal, which has been overlooked compared to alternatives such as DP training and fine-tuning, but is becoming increasingly relevant as most LLMs are accessed through APIs.

The paper builds on PMixED, a preexisting DP next-token prediction algorithm that mixes private next-token distributions with a public distribution, to introduce AdaPMixED. AdaPMixED uses a data-dependent privacy loss, which allows an analyst to adaptively check the privacy loss consumed so far, unlike PMixED where the privacy loss and the total number of tokens have to be fixed upfront. AdaPMixED also introduces a noisy screening mechanism, which saves privacy by routing certain queries to a public model when the private model will not help. 

AdaPMixED is evaluated on four datasets (adding two datasets not evaluated by PMixED) with pretrained GPT-2 models. It achieves lower perplexity than other baselines (PMixED, DP-SGD, public model) for a significantly lower (but data-dependent!) privacy loss. This allows AdaPMixED to answer massively more queries than PMixED, which is critical to make DP next-token prediction scale and provide a credible alternative to DP training.

### Strengths
Main strengths:
- The privacy-utility improvements of AdaPMixED can be particularly significant, because they show that next-token prediction can be practical, compared to well-studied alternatives like DP-SGD. I was personally not aware of the PMixED line of work, and I used to consider that next-token was a dead-end in terms of DP, since privacy loss accumulates with the number of queries. It turns out that mixing public predictions with private predictions, along with a careful privacy analysis, allows such DP APIs to support pretty credible workloads (100K queries for single-digit data-dependent epsilon, whereas previous work only evaluated up to 1K queries). This is a welcome development, and I appreciate the authors' work in this important direction.
- Supporting adaptive workloads is critical, and often overlooked in the DP literature (as the authors note when referring to Dwork & Feldman). The key idea to remove the non-adaptivity limitation from PMixED is to use a data-dependent privacy loss.
- The utility results are novel and useful (Thm 4.3). 

Other strengths:
- The noise-screening mechanism is original and not present in PMixED. I am hesitant to consider this technique (and Thm 4.1) as a particularly significant new result, even though the paper claims this is one of its three contributions. The adaptation seems pretty straightforward: it does not involve data-dependent loss, only some post-processing, a sensitivity calculation and a Gaussian mechanism. It can still be nice technique if it comes with experimental gains. 
- The privacy loss breakdown in Tab 2b was useful.

Thank you for this paper, I learned a lot about private next-token prediction!

### Weaknesses
Data-dependent loss
- The data-dependent loss is a major flaw of this paper in my opinion, and the reason for my overall "reject" score. I am willing to change my score if I can be convinced that the current results are fair (maybe I misunderstood something), or with new results that incorporate a sanitized version of the data-dependent loss.
- My problem with data-dependent loss is that it can leak privacy, since it depends on the data (more specifically, it depends on the whole database passed to the DP mechanism). This does not satisfy the standard DP definition, and therefore one should not treat data-dependent epsilons and data-independent epsilons the same way. Yet, this is exactly what Table 1 is doing, by listing the "privacy loss epsilon" for DP-SGD and PMixED (meaning data-independent, with strong guarantees) and AdaPMixED (meaning data-dependent, with weak semantics) in the same table. This is simply not an apples-to-apples comparison, and any claim using this table to argue that AdaPMixED outperforms the data-independent baselines is misleading.
- The paper does acknowledge the privacy risks of data-dependent loss. But at the very least the epsilon values should then come with a clear disclaimer in the Table and summary of the results in the conclusion, or even a different notation such as $\epsilon_{data-dependent}$. This is not the case in the paper.
- The paper mentions that "one can sanitize the privacy loss via smooth sensitivity analysis, similar to Papernot et al. (2018), if the privacy loss needs to be released." This is such a crucial point. I don't think the paper can possibly afford to put this off to future work. The key results in the evaluation do release privacy loss, and without this there is no apples-to-apples comparison with data-independent baselines.


Noisy screening:
- The tradeoff evaluated in 5.3 seems pretty small. I agree that saving privacy loss is valuable, and barely changes perplexity, but the savings don't seem to be very significant. Also, I am worried that the results are falling within the uncertainty due to experimental randomness (e.g., Section 5.3 analyzes a 0.08 or 0.33 PPL decrease, but Table 1 has confidence intervals of at least 4 PPL). I think that more experiments are needed to evaluate a proper tradeoff curve with x=privacy loss and y=perplexity as the noisy screening changes, with the average of multiple runs.
- Fig 2e) attempts to do that, but it is hard to interpret since it involves 4 parameters, the values barely change, and there is no clear trend.
- Overall, it seems that noisy screening has a pretty limited impact (or at least the evaluation doesn't show clear and significant trends). This makes me doubt the importance of what is supposed to be a major contribution of the paper.

Other weaknesses and minor comments:
- The Fig 2 axis are a bit misleading, the scale should probably be fixed across all 6 experiments, if we want to compare the relative importance of different methods.
- Alg. 1 is hard to parse, having some comments or headings (e.g., "Noisy screening") would be helpful.
- PMixED has been published, you could use this reference instead of the arXiv preprint: https://aclanthology.org/2024.naacl-long.247.pdf
 - While 100K queries (where one query is one next-token prediction) is a massive improvement over previous next-token prediction work, this is only practical for a limited class of workloads. For instance, that would represent around 10 short answers (100 to 1000 tokens) per day for a few weeks on a corporate or medical dataset. Once the budget is exhausted, it's time to fine-tune the private LLMs on fresh data, which might be pretty scarce if it's only been a few weeks since the previous round of fine-tuning. This is not a limitation of the paper,  given the improvements over prior work, but it could still be interesting to discuss such practical implications.

### Questions
- Is there any reason why you did not analyze a sanitized version of the data-dependent privacy loss, e.g., with smooth sensitivity? I understand that there might be technical difficulties, or that smooth sensitivity could erase the gains from the data-dependent analysis. But this is a vital point in my opinion, without which it is simply not possible to compare with data-independent baselines.
- Have you considered using privacy odometers? They seem well-suited for your motivation, allowing an analyst to stop a computation adaptively and measure their privacy loss. Maybe all you need is an odometer with PMixED? If not, it could be helpful to justify why data-dependent loss is the only way forward for adaptivity.
- The noisy screening mechanism might be a good fit for the sparse vector technique, depending on how often we expect queries to skip the private ensemble.

### Soundness
2

### Presentation
4

### Contribution
3
