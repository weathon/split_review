# Scaling Laws for Multilingual Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
We propose a novel scaling law for general-purpose decoder-only language models (LMs) trained on multilingual data, tackling the problem of balancing languages during multilingual pretraining. A primary challenge in studying multilingual scaling is the difficulty of analyzing individual language performance due to cross-lingual transfer. To address this, we shift the focus from individual languages to language families. We introduce and validate a hypothesis that the test cross-entropy loss for each language family is determined solely by its own sampling ratio, independent of other languages in the mixture. This insight simplifies the complexity of multilingual scaling and make the analysis scalable to an arbitrary number of languages. Building on this hypothesis, we derive a power-law relationship that links performance with dataset size, model size and sampling ratios. This relationship enables us to predict performance across various combinations of the above three quantities, and derive the \textit{optimal sampling ratios} at different model scales. To demonstrate the effectiveness and accuracy of our proposed scaling law, we perform a large-scale empirical study, training more than 100 models on 23 languages spanning 5 language families. Our experiments show that the optimal sampling ratios derived from small models (85M parameters) generalize effectively to models that are several orders of magnitude larger (1.2B parameters), offering a resource-efficient approach for multilingual LM training at scale. \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper looks at the oft-neglected area of multilingual language model and in particular, scaling laws. They note that most prior work in scaling laws is focused on monolingual models or translation models (as opposed to broader generation models). The authors train more than 100 models varying in size from 85 million parameters to 1.2 billion (not counting embeddings) for 5 language families. Overall, they claim their sampling strategy is better at getting overall better multilingual loss.

### Strengths
An overlooked area in the field. Multilingual Language models are very important.

Lots of experiments.

### Weaknesses
A bit dense (especially some captions of figures and tables that took me a while to figure out.

For instance my thoughts about "Figure 1 Model size N figure is a bit confusing to me. What is N? 0,2,4,8 of what? Oh, 8 is 85Million parameters. It could be a bit clearer in the caption."

Figure 5 left and middle … a bit hard to know. Y-axis is loss (for a sampling ratio?) X-axis is sampling ratio? Colored lines are model sizes. Data size is just difference between left and middle graph? The caption should really be more explicit. Also, what am I supposed to take away from this?

I’d argue that MT is a type of generation and cache your claims in the intro a bit more.

Thanks for running the experiments in Figure 2. However, I think there are significant confounding factors in this analysis. First, Romance and Germanic languages are relatively closely related. Second, using group 1 and group 2 languages with Indic languages (which I assume to mean different scripts) adds another variable that makes it difficult to disentangle the interaction therein.

### Questions
Does better loss generalize to better downstream performance on other tasks? I would assume so I was just curious if you had tried anything?

Figure 1 appears to show that all models get better with more data, larger model size, and sampling ratio of 1. Why use a uniform sampling rate of 0.2 and not just 1.0? I assume that 1.0 implies 0.0 of others meaning 0.2 means equal sampling of all. If so, do you use all the data completely? And does this outperform other baselines? My guess is that this is shown somewhere in tables 3-6 but it is unclear to me.

What happens if you randomly group languages (not by family) and apply your scaling laws? Do the same conclusions hold? I'm trying to get at your claims that language family matter more - but I don't think you test languages apart from their language family ever.

I’d argue that MT is a type of generation and cache your claims in the intro a bit more.

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
This paper introduces a method to calculate the multilingual scaling law and estimate the optimal sampling ratio for each language during multilingual pre-training. Experimental results on models with 85M and 1.2B parameters show that the optimal sampling ratios estimated are better than the three naive baselines.

### Strengths
- The scaling law proposed is more fit for multilingual pre-training by considering cross-lingual transfer.
- There is an interesting finding that $\gamma_{i}(N, D)$ is independence from N and D.
- The optimal sampling ratios inferred can bring marginal improvement (< 0.1) than the three naive baselines.

### Weaknesses
 - **Missing important baselines**: The three baselines in this paper are naive. More baseline methods like the Equation (7) in Fernandes et al., 2023 are not incorporated.

- **More experiments needed**: The minimal cross-group transfer hypothesis (hypothesis 1) is hard to quantify and meet. It is still far from the real phenomenon. To support hypothesis 1, experiments are only conducted on (Romance, Indic) and (Sino-Tibetan, Slavic) language family pairs with varying three sampling ratios in {0.2, 0.4, 0.6}. How about the sampling ratio for other language family pairs varies? (For example, the results for more similar language families like Germanic and Romance or Romance and Slavic)

- **Overstatements**: 
  1. The first sentence in the abstract "We propose a novel scaling law for general-purpose decoder-only language models(LMs) trained on multilingual data, **addressing the problem** of balancing languages during multilingual pretraining." Actually, the problem is simplified into 5 language families and cases of low-resource languages are reduced in this paper (Line 190-191).

  2. The lines in Figure 4 are nearly parallel, and it is better to report the slope rate for each line.

- **Typos**:
  1. The x-y axis for Figure 4: $L(p)-p$ --> $log(L(p))-log(p)$
  2. Line 452: $q_j$ --> $q_i$
  3. Line 515: asses --> assess

### Questions
a. (Hypothesis 1) How about the sampling ratio for other language family pairs varies? For example, the results for more similar language families like Germanic and Romance or Romance and Slavic.

b. As shown in Table 5, it can be found that the probabilities of Romance, Germanic, and Sino-Tibetan differ between models with 85M or 1.2B parameters. How to interpret this phenomenon?

c. (Line 531, 100 models) Does it refer to the number of models investigated?

### Soundness
2

### Presentation
3

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
The paper studies a scaling law for general-purpose decoder-only multilingual Language Models to reduce the need for resource-intensive data mixture selection in large-scale training. This paper focuses on balancing language families rather than individual languages during pretraining. The authors hypothesize that pretraining can leverage language family groupings to simplify the complexity of multilingual learning. From this hypothesis, they derive a power-law relationship that links dataset size, model size, and language sampling ratios, helping to optimize training across multiple scales (85M, 397M, 810M, and 1.2B parameters) on each of the 5 language families.

### Strengths
S1. The proposed scaling law could simplify the complexity of cross-lingual interactions during training, offering a meaningful extension of existing work that focuses primarily on monolingual or bilingual models. This decoupling from individual languages could also reduce the computational burden.

S2. The paper also proposed an optimal sampling ratio as a practical data-mixing strategy, which could be applicable for real-world multilingual model training.

S3. The paper is clear in its presentation, with a well-structured flow of ideas that makes it easy to follow. The authors provide clear and well-presented tables, figures, and mathematical formulas, which support the text and make complex concepts more digestible.

### Weaknesses
W1. The primary issue with the paper is its focus on the generality of the proposed scaling law without applying it to specific downstream tasks (beyond machine translation as it is claimed). Testing it on downstream tasks like summarization or question answering, on metrics that are widely used to assess the performance of each downstream task, would have strengthened the claim that this scaling law is for a general-purpose decoder multilingual language model. It also provides more solid evidence of its applicability across different use cases to interested readers.

W2. The improvement in normalized loss from the optimal sampling ratio appears minimal. For example, in Table 4 for the 85M model, the difference between the uniform sampling ratio ($5.912$) and the proposed sampling ratio ($5.895$) is just $0.017$, raising questions about the significance of this gain. It is unclear to me how beneficial such a small reduction in loss is, especially given the additional complexity introduced by the data-mixing strategy. Again, going back to W1, if these minor improvements do not translate into meaningful performance gains on downstream tasks, the value of this approach is not that convincing. The paper should showcase the practical advantages of achieving these marginal gains in normalized loss.

Additionally, in Table 6 for the 1.2B model, the total normalized loss for uniform sampling seems inconsistent: summing the individual values ($1.142 + 1.180 + 1.273 + 1.142 + 1.134$) results in $5.871$, which differs from the reported value of $5.946$. If the former is true, this could imply that the proposed sampling ratio doesn't generalize as well for larger models (1.2B), which is the main purpose of this proposed sampling ratio. Clarifying this would help substantiate whether the benefits of the proposed ratio are meaningful across different model sizes.

W3. While the paper provides some empirical evidence supporting Hypothesis 1, this evidence is limited to specific language families (Indic-Romance and Slavic-Sino-Tibetan, with Sino-Tibetan only represented by Chinese). This is a substantial claim and is referenced throughout the paper. However, there are numerous studies, particularly in monolingual settings, showing cross-lingual transfer outside of phylogenetically related language families [1]. For example, English (Germanic) or other high-resource languages are widely used for cross-lingual transfer in various multilingual setups [1, 2]. Language similarity can also be measured in multiple ways, such as typological or geographical distance, and not solely by language families [3]. It would be valuable to investigate whether the proposed hypothesis holds between languages like English and Romance languages, where there is known cross-lingual transfer despite family differences.

### Questions
In addition to the points raised in the weaknesses, I do have additional questions:

- Could you provide more details by comparing your proposed scaling law with previous work in multilingual models? For example, can you fit previous works on scaling laws into your framework and compare their performance? This would give readers better clarity on the benefits and advantages of using the proposed approach.
- Have you tested your scaling law on out-of-distribution data as in data outside the CommonCrawl dataset? Since your test set is taken from the same dataset, I wonder if the scaling law would generalize well to datasets that are not part of CommonCrawl, especially as you included dataset size as part of the proposed scaling law. Exploring the model’s generalization ability on such data could provide additional insight.
- How well does the scaling law apply to low-resource language families like Niger-Congo? Also, could the current results on each language family have been skewed by the higher-resource languages such as English, Spanish, Russian, Hindi, and Chinese within their respective families? In other words, would the proposed strategy also benefit less-represented languages, such as Catalan and Kannada, which have fewer tokens?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a scaling law for multilingual LLMs. It also argues for a hypothesis that the cross entropy loss for each language family in the LLM is determined only by the sampling ratio of the family. Experiments are performed on 23 languages (from 5 families) and model sizes range from 95M parameters to 1.2B parameters.

### Strengths
1. Scaling laws are important objects of study; better understanding can help us inform modeling/training decisions. The paper examines scaling law in the context of multilingual LLM, which I believe is new. There are scaling laws on monolingual LLM and machine translation models, but this setup deserves its own study. 

2. One practical result is the prediction of good language sampling ratios. This is an important design decision.

### Weaknesses
1. While the results are interesting, I believe the claims are too strong. It would be better to tone down. Here are some examples of strong claims: 
- page 1: "Our contributions are grounded ... making our analysis scalable to an arbitrary number of languages." - The experiments are performed on 23 languages. There are 6000+ languages in the world. 
- page 7: Half a page is dedicated to explaining how the work is better than previous work (i.e. generalized framework, multilingual scalability, incorporation of dataset size, simpler...) I think it suffices to keep it simple and say that your work looks at a different problem; I do not see a need to argue so much. Further, it is somewhat strange to argue that your equation is simpler than previous work -- if we view scaling law as a phenomenon to be discovered, then faithfulness is probably more important than simplicity perhaps?

2. I question whether the proposed argument about language families as the main factor. It is true that there is probably more crosslingual transfer within a language family and less across families, but this is a very simplified view of language. Specifically: 
- Language families are genetic relationships, but in practice there are significant areal effects (c.f. https://aclanthology.org/N09-1067/ ). There are also other kinds of sharing, for example Japanese is an isolate but there are many Kanji characters borrowed from Chinese. 
- The experiments are actually not very diverse in terms of language families: Of the 23 languages (5 families) used, 22 languages (4 "families") are actually from the Indo-European "family". Germanic, Romance, Slavic, Indic are considered different branches of the Indo-European "family". So only 1 language (Chinese) is truly from a different family in the linguistic sense.
- One complication is script, which is not discussed in the paper. Different scripts will lead to very different tokenization results, which likely impacts LLM training. In the languages considered, most use the Latin script and the Russian branch uses both Cyrillic and Latin, I assume.

### Questions
1. This is not necessary a weakness, but I wonder if we should view the models to be on the small side compared to contemporaneous work. For example, training data is up to 50B tokens and model size is 398M parameters to 1.2B parameters. I think there is value in the experiments in any case, but can you comment a bit on the scale of some of the large multilingual LLMs in the literature? For example, EuroLLM-1.7B is trained on 4 trillion tokens. 

2. The citations are generally adequate. Here are a two more suggested papers to add - they discuss scaling laws for bilingual machine translation. 
https://aclanthology.org/2021.emnlp-main.478/
https://arxiv.org/abs/2109.07740

3. Regarding sampling strategy, the general rule-of-thumb I think is to up-weight lower-resourced languages. At the same time, some anecdotes seem to suggest it is better to make English data the largest (e.g. 50%) due to its potential to help LLM in reasoning and other tasks. Can you comment about the chosen sampling strategy in your experiments in the context of these guidelines? How similar or different is it? Or does it depend on the group of languages?

### Soundness
1

### Presentation
3

### Contribution
2
