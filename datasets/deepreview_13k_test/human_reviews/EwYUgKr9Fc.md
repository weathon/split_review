# Semantic Membership Inference Attack against Large Language Models

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Membership Inference Attacks (MIAs) determine whether a specific data point was included in the training set of a target model. In this paper, we introduce the Semantic Membership Inference Attack (SMIA), a novel approach that enhances MIA performance by leveraging the semantic content of inputs and their perturbations. SMIA trains a neural network to analyze the target model’s behavior on perturbed inputs, effectively capturing variations in output probability distributions between members and non-members. We conduct comprehensive evaluations on the Pythia and GPT-Neo model families using the Wikipedia dataset. Our results show that SMIA significantly outperforms existing MIAs; for instance, SMIA achieves an AUC-ROC of 67.39\% on Pythia-12B, compared to 58.90\% by the second-best attack.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the problem of membership inference in large language models by proposing "semantic MIAs". The key idea is to use various perturbations to the input text, then analyze the behavior of a model on these points, train an auxiliary model on these behaviors, and finally use that model to predict membership. The authors show that SMIAs outperform prior MIAs on different benchmarks.

### Strengths
1. The paper does a good job at explaining their methodology, which considers the fact that learning a classifier on top of LLM behaviors can allow learning membership signals well.
2. The work demonstrates strong gains over past MIAs across multiple benchmark datasets.

### Weaknesses
There are various works at this point in literature which have argued that "WC" based assessment of MIAs when data is split across a cut-off date, is not sound. This work bases many of their gains on that setting.

[1] Do Membership Inference Attacks Work on Large Language Models? https://arxiv.org/abs/2402.07841.   
[2] LLM Dataset Inference: Did you train on my dataset? https://arxiv.org/abs/2406.06443.   
[3] Blind Baselines Beat Membership Inference Attacks for Foundation Models. https://arxiv.org/abs/2406.16201.    

Key weaknesses:
1. The method should be tested across all 20 train-test splits of Pile. Paper [2] on LLM Dataset Inference particularly shows how most MIAs perform well only on a few datasets
2. The blind baseline of n-gram is not considered in this work (paper [3]). This is an important comparison to understand if the gains in this work are meaningful.
3. Given that the goal of MI in LLMs is hard, I would love to see experiments on dataset inference.
4. The idea of learning an auxiliary classifier on top of the membership signal from neighbours seems to have been explored in [2]

### Questions
- How does the member data of the embedding model impact the performance of the SMIA

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
This paper introduces SMIA (Semantic Membership Inference Attack), an innovative approach to membership inference attacks against LLMs that leverages semantic analysis. The key insight is that LLMs exhibit distinct behavioral patterns when processing semantically similar variants of their training data versus unseen data. SMIA capitalizes on this by generating semantic neighbours for input texts, analyzing how the target model responds to these variations, and training a neural network to detect membership based on these response patterns. The authors evaluate SMIA extensively on the Pythia and GPT-Neo model families using Wikipedia and MIMIR datasets, demonstrating significant improvements over existing approaches - notably achieving an AUC-ROC of 67.39% on Pythia-12B compared to previous best of 58.90%.

### Strengths
The authors present a well-designed pipeline that combines neighbour generation using masked language models, semantic embedding analysis via the Cohere model, and neural network classification. This comprehensive approach allows SMIA to detect both exact matches and semantically similar content, representing a significant advancement over existing methods.
The experimental evaluation is particularly thorough, examining performance across different model sizes, architectures, and datasets. The authors carefully consider the impact of dataset distribution by using two different non-member datasets - one from the same distribution (Wikipedia Test) and another from a different time period (Wikipedia Cutoff). This reveals important insights about how data distribution affects attack performance. Additionally, the analysis of modified text scenarios (through word additions, deletions, and duplications) provides practical insights into the method's

### Weaknesses
1. The choice of key hyperparameters, particularly the use of 25 neighbours, lacks thorough clarification. While Table 7 shows performance improvements with increasing neighbour count, there's no clear analysis of the trade-off between computational cost and performance gain. The paper should examine the diminishing returns beyond 25 neighbours and justify why this specific number optimally balances effectiveness and efficiency.
2. A concerning weakness emerges in the method's inconsistent performance across different types of text modifications. As shown in Table 3, while SMIA achieves an AUC-ROC of 62.47% for word deletions on Pythia-12B (WT dataset), it drops to 55.13% and 54.19% for word duplications and additions respectively. This significant performance gap suggests an inherent bias in the method's ability to handle different types of text alterations. The authors don't adequately explain this asymmetry or propose potential solutions.
3. Aminor problem is the heavy reliance on the Cohere Embedding model, a third-party service, introduces both a potential point of failure and a privacy concern - users must share their data with an external service to generate embeddings. The authors don't explore alternative embedding approaches or analyze how the choice of embedding model impacts performance. Furthermore, the paper lacks a comprehensive analysis of the cost implications of using such commercial services at scale.
4. The method shows notably better performance with word deletions compared to additions or duplications, as evidenced in Table 3. For instance, with Pythia-12B on the Wikipedia Test dataset, SMIA achieves an AUC-ROC of 62.47% for word deletions but only 54.19% for additions. This behavioral asymmetry suggests fundamental limitations in how SMIA handles different types of semantic modifications, yet the paper offers limited analysis of why this occurs or how it might be addressed. This becomes particularly relevant when considering real-world scenarios where adversaries might deliberately modify texts in ways that exploit these weaknesses.
5. While authors demonstrate the attack's effectiveness, they provide minimal insight into how model owners might protect against such attacks. This omission is particularly notable given the paper's focus on privacy implications and its potential impact on real-world applications of LLMs. A more comprehensive treatment of potential countermeasures would significantly enhance the paper's practical value and provide important context for the security community.

### Questions
1. The scalability of SMIA deserves further exploration - how would the method perform with larger training datasets and more complex model architectures? The current evaluation uses 6,000 members and non-members each, which may not fully reflect real-world scenarios.
2. The choice of neural network architecture for the SMIA model itself appears somewhat arbitrary. Have the authors explored alternative architectures that might improve performance or efficiency? Additionally, how sensitive is the method to the quality and dimensionality of the semantic embeddings?
3.  How might defenders mitigate against SMIA?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces the Semantic Membership Inference Attack (SMIA), a novel approach that conducts Membership Inference Attacks by leveraging the semantic content of inputs and their perturbations. SMIA trains a model to detect variations in model behavior between member data members and non-members by analyzing how output probability distributions change with input perturbations. Evaluated on two models and two datasets, SMIA outperforms existing MIA techniques, achieving higher AUC and TPR when FPR is low in detecting membership.

### Strengths
1. The proposed method in this paper shows a very good novelty.

2. The proposed method has a good performance considering both AUC and TPR when FPR is low.

3. The proposed method successfully identifies membership even when data undergoes slight modifications due to its design motivation.

### Weaknesses
1.  Though the authors claim the proposed method is designed for grey-box models, there are no direct experiments about the real grey-box models. 

2. The experiments are not very comprehensive on the ablation part. For example, the authors might provide results if changing the embedding model or changing the classification models. 

3. There is no intuitive explanation of the proposed methods like what is the difference between the trends of loss from members and trends of loss from non-members.

### Questions
1. Could the authors provide some examples of grey-box models?

2. How will the performance of SMIA change if changing the embedding model or classification models?

3. What is the general behavior of loss from members? For example, will the loss from members change less than non-members considering neighbours?

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
3

### Summary
This paper proposes a new membership inference attack (MIA) for LLMs, called SMIA, with the goal to measure memorization. SMIA's intuition is that semantically similar “neighbors” of a sample contain membership signal. In the threat model, the adversary can query the target LLM to obtain losses/log probs, and has access to a set of known training members and non-members.

Concretely, given a target sample, the attack works as follows:

1. Generate "neighbors" of the target via repeated random masking and infilling (via T5 3B).
2. Calculate semantic embeddings of the target sample and all neighbors (via Cohere Embedding v3).
3. For every neighbor, calculate the difference to the target sample in terms of i) loss and ii) semantic embedding (full direction). Use the resulting 1 + 1024 values as the input to a moderately-sized MLP classifier that predicts a membership score.
4. Return "member" if the average membership score over all neighbors is larger than some threshold.

The paper evaluates SMIA for Pythia and GPT-NEO models on Wikipedia and MIMIR data. All results are reported in terms of AU-ROC; a few results also in terms of TPR @ FPR. For Wikipedia, the evaluation dataset uses Wikipedia text in the Pile training split as members, and one of two types of non-members: *WT* uses Wikipedia text from the Pile test split (before March 2020); *WC* uses Wikipedia pages published after August 2023 (not in the Pile training split). For MIMIR, the evaluation uses the highest n-gram overlap subsplit with various splits.

### Strengths
The paper introduces SMIA and its intuition very thoroughly. Even though there is no code, the attack's description should be sufficient to reimplement SMIA and reproduce most reported results. I also find it very interesting that directions in embedding space seem to carry non-trivial membership signal and think that the idea of considering not only exact verbatim samples for MI in LLMs is important. Lastly, although MI for LLMs remains a hard task, this paper manages to achieve small but consistent improvements over most existing methods in some settings.

### Weaknesses
**Evaluation datasets measure distribution shift, not MI**: Some evaluation datasets in this paper might be deeply flawed, in that they do not measure MI performance but just distribution shifts. For Wikipedia data, SMIA only yields a big improvement on the WC split, which uses temporally shifted Wikipedia articles as non-members. However, [Das et al., 2024](https://arxiv.org/abs/2406.16201) show that simple "blind" baselines that classify membership just based on the data (without any signal from the target model) already achieve very high MIA success.
Hence, SMIA could potentially just be a good distribution shift detector and the evaluation misleading. This is particularly concerning since the membership classifier is a NN, which might be particularly prone to overfitting on spurious correlations in the evaluation data. One way to alleviate this concern could be a blind baseline that uses inputs independent of the target model (e.g., random or constant loss).
For MIMIR, this is less of a concern. However, there SMIA only achieves significantly better MIA success for GitHub data and Wikipedia data for one model; existing attacks perform similarly or better on all other subsplits (in terms of TPR @ 2% FPR).

**AU-ROC alone is insufficient to evaluate MIAs**: It has long been known that only reporting AU-ROC in the evaluation of MIAs is deeply flawed and misleading [(Carlini et al., 2021)](https://arxiv.org/abs/2112.03570). Yet, this paper uses only AU-ROC as its main metric, and only reports TPR@low FPR values for a very limited subset of results in App. C.1. In particular, the effects of deduplication (Table 6), varying number of neighbors (Table 7), and slight modifications (Table 3) are only reported in terms of AU-ROC, and can hence not be judged soundly. The paper should report TPR @ low FPR (e.g., 2% or 1%) together with full ROC curves as the main metric, and defer AU-ROC metrics to the appendix (or omit them entirely).
NB: Consequently, while I looked at all tables in the main matter, I can only judge SMIA's performance by the values on Tables 4 and 5 (App. C.1).

**Complex approach without ablation**: SMIA is a complex approach that relies on many moving parts; yet, there is very little investigation about why every part is necessary. Hence, this paper requires a more thorough ablation study (e.g., what if the classifier only acts on losses/embedding directions, or what if the NN is replaced by a linear classifier?).

**Other minor points/feedback**:
1. SMIA requires a known member and non-member subset from the training data distribution. This is a non-trivial assumption that requires some discussion.
2. The lowest reported FPR threshold is 2%. This is still relatively high; it would be interesting to also report the attack's performance at lower FPRs such as 1% and 0.1% if feasible.
3. I found two things in Figure 2 slightly confusing: i) the axis label, and ii) that all neighbors are larger on one axis; I understood that the similarity is somewhat independent of the parameter space? Also, e.g., $x_1^m$ seems to be further from $x^m$ than $x^n$. Right now, I think the figure does not carry much information and could be confusing, hence it might be dropped. Finally, there is a typo in the caption (`taregt`).
4. Sec. 5.1 mostly repeats the results displayed in Table 1. I think the space could be used better by dropping this repetition and instead show some of the interesting studies currently in App. C.

### Questions
1. L218: Does the replacement actually happen in terms of words, or should it be tokens?
2. For the neighbor generation, are the resulting neighbors all unique, or could it be that some neighbours are duplicates/equal to the original sample?
3. Were T5 or the Cohere Embedding V3 model trained on some of the evaluation datasets? In particular, could it be that one of those models was only trained on the members for WC but not the non-members?
4. L382--384: Why are the MIMIR splits constrained to only 1000 samples, especially before splitting?
5. L391: The intuition about "Why SMIA Outperforms Other MIAs" mentions that using a neural network is one of the key success factors. However, I think simply using a neural network does not imply a stronger attack; could the authors elaborate this a bit more?

### Soundness
2

### Presentation
3

### Contribution
2
