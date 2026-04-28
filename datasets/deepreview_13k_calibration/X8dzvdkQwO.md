# Fine-tuning can Help Detect Pretraining Data from Large Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
In the era of large language models (LLMs), detecting pretraining data has been increasingly important due to concerns about fair evaluation and ethical risks.
Current methods differentiate members and non-members by designing scoring functions, like Perplexity and \mink.
However, the diversity and complexity of training data magnifies the difficulty of distinguishing, leading to suboptimal performance in detecting pretraining data.
In this paper, we first explore the benefits of unseen data, which can be easily collected after the release of the LLM.
We find that the perplexities of LLMs perform differently for members and non-members, after fine-tuning with a small amount of previously unseen data.
In light of this, we introduce a novel and effective method termed \textit{Fine-tuned Score Deviation} (\textbf{FSD}), which improves the performance of current scoring functions for pretraining data detection. 
In particular, we propose to measure the deviation distance of current scores after fine-tuning on a small amount of unseen data within the same domain.  
In effect, using a few unseen data can largely decrease the scores of all non-members, leading to a larger deviation distance than members. Extensive experiments demonstrate the effectiveness of our method, significantly improving the AUC score on common benchmark datasets across various models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper addresses the problem of detecting prestrainign data from LLMs. They notice that when fine-tuning an LLM on a few non-members selected by a cut-off date, the perplexity on other non-members (also based on the same cut-off date) decrease. Based on this observation, the authors propose a new method (Fine-tuned Score Deviation; FSD) to improve prior membership inference attacks (MIA) by adjusting the scores based on this fine-tuning phenomenon. They conduct experiments on 4 cut-off based benchmarks: WikiMIA, BookMIA, ArXivTection and BookTection and show significant gains wrt the baselines. The specific questions they tackle are:

1. Can FSD improve the performance of current MIA methods?
2. How many samples does the method need for fine-tuning?
3. Does FSD work across different model sizes?
4. Does FSD work with members for fine-tuning, instead of non-members?
5. Does FSD work for any fine-tuning method?

### Strengths
1. The idea is simple and intriguing, enlarging the difference between members and non-members could boost any MIA method.
2. The idea works for any MIA method.

### Weaknesses
The evaluation has major flaw. It only uses benchmarks that separates members and non-members based on cut-off dates. As Duan et al., 2024, Das et al., 2024, and Maini et al., 2024 show, this is fundamentally wrong because it introduces a temporal shift that bias the benchmark. These works have consistently proved the need to avoid evaluating MIA based on cut-off dates. This paper acknowledges these works on lines 458-459 and questions whether the results of this ICLR submission are influenced by this temporal shift. However, instead of following the recommendations from these papers for a correct evaluation, they simply remove timestamps. This is not enough as Duan et al., (2024) shows. Duan et al., shows that the cut-offs introduces changes in the n-grams. An IID split have a higher n-gram overlap between members and non-members than the temporal split. Therefore, even when removing the timestamps in the plain texts, the n-gram distribution is different, making the evaluated method classify temporal data rather than membership. Moreover, the authors acknowledge this possibility in lines 535-537 but they do not follow the recommendations of the papers mentioned above, which are to evaluate on for example Pythia with data from the Pile. 

It is also concerning that the method's effectiveness is not demonstrated on a truly IID setup in the main paper. The core experiments rely on the flawed cut-off date methodology, which introduces a temporal bias. This makes it difficult to ascertain whether the observed improvements are due to the method's ability to detect membership or simply its sensitivity to temporal shifts in the data. The lack of IID experiments in the main paper undermines the validity of the claims, as the method might be exploiting temporal patterns rather than genuine membership signals. The results presented in Figure 4 might be explained by the temporal bias of the evaluation. Training more on new data might make the method identify better the n-gram distribution of the documents after the cut-off. This hypothesis can only be rejected by evaluating on an IID setup.

### Questions
* Please conduct your experiments on an IID setup (see the works of Duan et al., 2024, Das et al., 2024, and Maini et al., 2024 that you cite; eg: using Pythia use as members the training set and as non-members the dev and test sets) so that we can clearly see the effectiveness of your work.
* It is possible that the results of Figure 4 are explained by the temporal bias of the evaluation. Training more on new data might make the method identify better the n-gram distribution of the documents after the cut-off. We can reject this hypothesis by evaluating on an IID setup.

### Soundness
2

### Presentation
4

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
The paper proposes a new method for improving the accuracy of pretraining data detection in LLMs, called Fine-tuned Score Deviation. they shows that fine-tuning models on a small set of non-member data increases the deviation between score distributions of seen and unseen data. They validate this claim via experiments on WikiMIA, BookMIA, ArXivTection and BookTection datasets. FSD consistently improves the performance of existing detection methods based on scoring functions like perplexity and Min-k%.

### Strengths
Very interesting observation, and notable improvement in pretraining data detection accuracy. I think this paper has a clearly defined objective, and interesting empirical results.

The results are strong, showing substantial improvements in AUC and tpr at low fpr across the selected datasets and models. FSD helps improving existing score-based pretraining data detection methods.

### Weaknesses
1. Have you experimented on the MIMIR dataset? This dataset seems to be more challenging, and authors claim this is because seen and unseen examples are not from different temporal distributions. I am very interested to see how this method helps MIA on MIMIR dataset.

2. They have not explained or given intuition about why finetuning increases the gap between distributions.

3.  The method requires fine-tuning the LLM, which makes it more expensive compared to existing methods. If authors find some intuition about why finetuning has this impact, they may find less expensive methods.

### Questions
1. Do you have intuitions or theoretical understanding about why finetuning increases the gap between distributions?

2. What is the role of the finetuning technique you use? Is there a dependency on LORA?

3. How sensitive is FSD to using unseen data from a loosely related domain impact detection performance?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper tackles the issue of detecting pretraining data. It introduces a method where a pretrained model is fine-tuned with non-member data from the same domain. The goal is to increase the gap in scores like perplexity between member and non-member data, making it easier to spot training data.

### Strengths
* Clear introduction to the problem and motivation.
* The method is well explained and supported with intuitive examples, such as Figure 2.
* Comparisons with other relevant baselines, and showing significant improvement over them.
* Thorough experiments, including ablation studies that address additional research questions.
* Creative use of non-member data.

### Weaknesses
 * The paper assumes access to unseen data in the same domain but doesn’t define 'domain' clearly. Could the authors explain how they handle differences between domains, especially if vocabularies differ a lot, and how they decide what data counts as 'same domain'? For instance, if the pretraining data includes both scientific articles and general news, how would the method handle fine-tuning data that is only from one of these areas? The lack of clarity on domain boundaries makes the method's applicability less clear.
*  *"To the best of our knowledge, our method is the first to utilize some collected non-members in the task of pretraining data detection"* - There’s limited information on how to collect non-member data, which seems a key aspect of your method. The paper should elaborate on practical strategies for obtaining this data, considering the potential difficulty in identifying truly 'unseen' data, especially for models trained on vast internet datasets. The method's reliance on this potentially hard-to-obtain data is a significant limitation.
* The approach assumes access to both unseen data and model probabilities for each token, compared to other black-box assumption methods. While access to model probabilities might be reasonable for some open-source models, it's not a given for all models, especially those accessed via APIs. This limits the general applicability of the method, as many real-world scenarios involve using models where only the final output is available.

### Questions
* Could you explain more about the datasets, like how they’re labeled and how well they fit the models used? Is there a class imbalance in any of the datasets?
* Should fine-tuning happen for each example $x$ (or each group of examples $x_i$ within the same domain)? If so, that might be a big drawback.
* Fine-tuning can be delicate, and it’s easy to go past the optimal point. An experiment on how sensitive this method is to fine-tuning parameters (e.g., number of epochs, LoRA rank) would be useful.
* For a more diverse test set, what happens if we fine-tune once on a mix of domains?
* If non-member data in the specific domain is not available, is there any alternative in the general frame of this method?



**Minor suggestions:**
* If terms like "Data Contamination" or "Membership Inference Attack" are central, it might help to introduce them earlier (e.g., in the Introduction or Background). If not, why are they in the Related Work section?
* Adding an ethics statement could underscore the method's role in detecting sensitive information used in LLM training, addressing the ethical significance of such methodologies.
* Consider renaming either the “Method” section or subsection for clarity.
* Start a distinct “Results” section.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper found that fine-tuning significantly reduces the perplexity of non-member data, which inspired the author to propose a new data detection method, FSD. The method determines whether data was used in training by comparing its perplexity in the original model versus the fine-tuned model. Experimental results showed a significant improvement over baseline methods.

### Strengths
1. The improvement is very significant.
2. The experiments and analysis are solid.
3. The writing is good and easy to follow.

### Weaknesses
1. This method requires fine-tuning the models. However, many models do not support fine-tuning especially white-box models, making this approach impractical in reality.
2. Fine-tuning every model you want to detect would be very costly.
3. Meta-evaluation typically fine-tunes a model on the data that needs to be detected, in order to assess whether the detection method is effective. However, this method is similar to the meta-evaluation.
4. The in-distribution non-member data is not easy to be acquired for fine-tuning.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
