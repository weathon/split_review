# On Linear Representations and Pretraining Data Frequency in Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Pretraining data has a direct impact on the behaviors and quality of language models (LMs), but we only understand the most basic principles of this relationship. While most work focuses on pretraining data's effect on downstream task behavior, we investigate its relationship to LM representations. Previous work has discovered that, in language models, some concepts are encoded as ``linear representations'', but what factors cause these representations to form (or not)? We study the connection between differences in pretraining data frequency and differences in trained models' linear representations of factual recall relations. We find evidence that the two are linked, with the formation of linear representations strongly connected to pretraining term frequencies. First, we establish that the presence of linear representations for subject-relation-object (s-r-o) fact triplets is highly correlated with both subject-object co-occurrence frequency and in-context learning accuracy. This is the case across all phases of pretraining, i.e., it is not affected by the model's underlying capability. In OLMo 7B and GPT-J (6B), we discover that a linear representation consistently (but not exclusively) forms when the subjects and objects within a relation co-occur at least 1-2k times, regardless of when these occurrences happen during pretraining. In the OLMo 1B model, consistent linearity only occurs after 4.4k occurrences, suggesting a connection to scale. Finally, we train a regression model on measurements of linear representation quality that can predict how often a term was seen in pretraining. We show such model achieves low error even for a different model and pretraining dataset, providing a new unsupervised method for exploring possible data sources of closed-source models. We conclude that the presence or absence of linear representations in LMs contains signal about their pretraining corpora that may provide new avenues for controlling and improving model behavior. We release our code to support future work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors investigate the correlation between linear representations and pre-training data frequency in language models. The work is conducted on recent findings that the linearity of different types of relations varies significantly depending on the specific relationship. Existing work does show that language model exhibit such linear structures, but do not reveal the underlying reason why some relations exhibit such structure while other do not. The main contribution of this work is to empirically draw the correlation between such linear structure and data frequency. It shows that that linear representations for factual recall relations are related to mention frequency and the model size. In addition, more detailed results show that linear representations form at predictable frequency thresholds during training, which allows the prediction of term frequencies in the training data. Finally, the authors release a tool for searching through tokenized text for understanding training data characteristics.

Overall, the findings are insightful for understanding linear representation structures in language models. This empirical study complements existing theoretical evidence on the same subject. It provides a perspective to the problem, which can be among many other factors in driving the formation of linear structures. On the utility side, the findings can be used for understanding training data, which are typically not published for current LLMs.

### Strengths
A perspective for understanding the reason that some features from LLMs demonstrate linear structures while others do not.

A tool for search through tokenized text to support the understanding of training data.

### Weaknesses
It provides one perspective to the problem empirically, with a specific set of metrics. While giving useful information, the depth of understanding and the utility domain is constrained mostly to the correlation between term frequency, the model size and the linear structure.

### Questions
Could there be some theoretical discussion on the training dynamics and the frequency thresholds?

One related work is 

Guangsheng Bao, Zhiyang Teng, and Yue Zhang. 2023. Token-Level Fitting Issues of Seq2seq Models. In Proceedings of the 8th Workshop on Representation Learning for NLP (RepL4NLP) at ACL 2023. Toronto, Canada from July 9th to July 14th, 2023.

which also discusses the correlation between term frequencies and model accuracy.

### Soundness
3

### Presentation
4

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
This paper explores the question of why linear structures form in LLMs by investigating the connection between training data frequency and the formation of linear representation, focusing specifically on factual recall relations. The study reveals that (1) the formation of linear representations is strongly correlated with subject-object co-occurrence frequency, and (2) the presence of linear representations can help predict relation frequency. Experiments are conducted using OLMo-1B, oLMo-7B, and GPT-J to validate these findings.

### Strengths
- Exploring the origin of linear representation is an important question in LM interpretability. This work identifies a correlation between linear representations of factual recall relations and the subj-obj co-occurrence frequency in pretraining.
- This paper investigates the relationship between few-shot accuracy and the existence of a linear representation.
- Using the existence of linear representations to predict the frequency of terms in the pretraining corpus is interesting.

### Weaknesses
 - The scope of the work is somewhat limited, as only 25 factual relations are investigated. It is unclear whether the identified correlation is also valid for other relation types. Expanding the analysis to include more factual relations and other types of relations could further enhance the robustness of the findings and potentially offer additional insights.
- The linear representation seems to be affected by the context in LREs (e.g., four "X plays the Y" examples before the fifth one. Are the findings universally applicable to LLM generation without involving ICL formats?

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This research paper explores how the frequency of certain words appearing together in the data used to train a language model (LM) affects the LM's ability to learn simple, linear rules for representing facts. The authors found that the more often two words related to a fact appear together in the training data, the more likely the LM is to learn a simple rule to represent that fact. This discovery helps to understand how LMs learn factual information and could be used to figure out what kind of data was used to train secret LMs. The authors also created a tool to help others count how often words appear together in large datasets

### Strengths
The study finds a strong correlation  between the average co-occurrence frequency of subjects and objects within a relation and the quality of linear representations (LREs) formed for that relation. This correlation surpasses the individual correlations with subject frequencies or object frequencies, highlighting the significance of subject-object co-occurrence.

The study focuses uses Linear Relational Embeddings (LREs), which effectively approximate the computations performed by an LLM to predict objects in factual subject-relation-object triplets. This paper builds upon this research by examining how the frequency of subject-object co-occurrences in pretraining data directly impacts the emergence and quality of these LREs

The paper introduces a promising technique for analyzing the pretraining data of closed-source models by leveraging the connection between linearity and frequency.

### Weaknesses
The paper presents valuable findings, however they should provide some discussion along the following directions:

(a) The paper primarily focuses on Linear Relational Embeddings (LREs) as a representative class of linear representations in LLMs. However, LLMs might employ various other forms of linear or non-linear structures to encode information. This focus on LREs could limit the generalizability of the findings to other types of representations. Is there any strong hypothesis to strict to LREs? It would be beneficial to explore the limitations of LREs in capturing more complex relationships that might be encoded through non-linear transformations or other architectural features of LLMs, such as attention mechanisms.

(b) While the study demonstrates that LRE features can be used to predict the frequencies of individual terms with reasonable accuracy, predicting the frequency of subject-object co-occurrences is challenging. The regression models achieve only marginal improvements over baseline performance in this task.  Integrating additional features might be helpful here. The paper should discuss why predicting co-occurrence is substantially harder, and consider if the model is simply learning to predict the mean co-occurrence frequency, rather than capturing the nuances of individual subject-object pairs. Exploring features beyond simple frequency counts, such as pointwise mutual information or other measures of association, could potentially improve the prediction of co-occurrence frequencies.

(c) The study analyzes a set of 25 factual relations from the Relations dataset. However, LLMs are trained on vast and diverse data, encompassing a much wider range of relations and concepts. Expanding the scope of analysis to encompass a broader range of relations would provide a more comprehensive understanding of the role of frequency in shaping LLM representations. The current selection of relations might not be representative of the full spectrum of relations learned by LLMs. It would be valuable to include a discussion on how the findings might generalize to other types of relations, such as those involving abstract concepts or complex events.

(d)  The paper focuses primarily on the frequency of terms in the pretraining data. However, other factors, such as the context in which terms appear, the syntactic structure of sentences, or the semantic relationships between words, could also influence the formation of linear representations. For example, LLMs are proven to not do well is facts  are stored in templates , as it tend to remember the template and not the facts. The proposed approach may not be applicable in those scenarios. The paper should acknowledge that the observed correlation between co-occurrence frequency and LRE quality might be confounded by these other factors. A more thorough analysis should consider the potential influence of these variables and discuss how they might interact with frequency to shape the learned representations.

### Questions
Refer the previous section.

It would be good if authors can dedicate a section to discuss the potential impact of confounding factors, such as context, syntax, and semantics. Explain why controlling for these factors is challenging in the current study but emphasize the importance of future work to disentangle their effects from the influence of frequency.

### Soundness
3

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
4

### Summary
This paper finds that the formation of linear representations for factual recall relations in LMs is highly correlated with the frequency of subject-object cooccurrence in the pretraining data. The formation of linear representation can happen at any stage of pretraining as long as the subj-obj cooccurrence exceeds some threshold, i.e., a linear representation can form consistently when the subjects and objects co-occur at least 1-2k times even at early stages of pretraining. The results also indicate that the frequency threshold is related to the model size, and larger models tend to require smaller thresholds. Using the metrics that evaluate the quality of linear representations, the authors can predict the approximate frequencies of individual terms as well as the co-occurrence of terms in the pretraining corpus better than using the LMs' uncertainty alone.

### Strengths
This paper draws an interesting connection between pretraining term frequency to the formation of linear representation of factual recall relations. The fact that the formation of linear representations could happen at any pretraining stage is particularly intriguing. The experiments and results are easy to understand and the discussion of related work is comprehensive.

### Weaknesses
- Being able to predict the frequencies of individual terms as well as the co-occurrence seems to be a direct implication of high correlation and therefore does not sound like a major standalone contribution. Also, "Importantly, this regression model generalizes beyond the specific LM it was trained on without additional supervision.": the prediction results seem to be very noisy and not much better than the mean frequency baseline.
- Some claims are not properly justified:
  - Line 75: "This frequency threshold decreases with model size": This is only tested two model sizes (OLMo-7B and OLMo-7B), and the fact that GPT-J (6B) has as smaller threshold than OLMo-7B is an counterexample for this. Would be good just to be consistent with the rest of discussion to claim there is a connection to scale.
  - Line 93-94: "Linear representations form at predictable frequency thresholds during training, regardless of when this frequency threshold is met for the nouns in the relation." The term "predictable" can be understood as there is a strong correlation between the linear representation quality and the co-occurrence frequency. However, the fact that this threshold is predictable regardless of when this frequency threshold is met is not well supported by results. It is necessary to show that the threshold (mean causality >.9) is consistent across different checkpoints.
    - Line 319-320: "Regardless of pretraining step, models that surpass this threshold have very high causality scores." It would be nice if you could arrange results into different scatter plots for each pretraining stage and compare them, say by fitting a linear model and comparing their slopes and biases.
  - Line 100: The efficiency of the proposed searching tool is not well discussed. It is unclear how this tool compares to existing methods like WIMBD, and the paper does not provide sufficient details about its implementation or performance characteristics to justify claims of efficiency.
  - Line 455: "Some relations, like star-constellation perform very poorly, possibly due to low frequency" Why low frequency is the cause?
  - Line 471: "Second, evaluating on the LRE features of a heldout model (scaled by the ratio of total tokens trained between the two models) maintains around the same accuracy," How do the results support "around the same accuracy"? If it is comparing Train OLMo and Train GPT-J in Table 1, the drop of accuracy is larger than the performance gap between LRE features and mean baseline. I am not sure if this entails "around the same accuracy". The claim of maintained accuracy is not supported by the provided data, as the performance drop is substantial and not within a reasonable margin of error.
  - Line 483: "In general, the regression transfers well, without performance deteriorating much (about 5%), suggesting LREs are encoding information in a consistent way across models." What results support this? Table 2 only shows a few examples which is insufficient for supporting the claim. Are there aggregated numbers of all pairs? How many of them have errors less than 5%?
- Some important details are missing from the experiments
  - The results in Figure 3 and Table 1 do not match: 1) why is the mean freq. baseline performance different? 2) why do LRE features (Table 1: 0.76) seem to perform better than LRE + LM (Figure 3: ~0.67) for OLMo, if Figure 3 shows the results for OLMo. The author should explain how are the numbers related to each other.
  - Table 2: 1) "Predictions are better for relations that are closer to those found in fitting the relation (country-related relations)" What does closer mean here? How did you measure this? 2) "Some relations, like star-constellation perform very poorly, possibly due to low frequency"
- Some figures and tables need to be more carefully explained:
  - The two left plots in Figure 2 need more explanations or presented in a better way. Specifically, why are some points darker than the others? What do the lines (light grey and dark grey lines) mean? Also, why do all dots for GPT-J have the same shape while the dots for the 2 left plots do not? What do different shapes mean (should be either explained in the caption or represented in the legend)?
  - Table 1: "Train OLMo" and "Train GPT-J" are hardly self-explanatory, the authors should consider better ways to explain the settings.


### Questions
1. The experiments follow previous work and only analyze 25 relations. What are the reasons for not including other relations?
2. Section 4.3 is interesting to some degree but I am not sure about the implication of the results. Looks like it is just a description of what is observed. What is the research question you want to answer here?
3. Typos:
   1. Line 455 the regression model can "be" sensitive to ...
   2. Line 416: the paragraph does not end properly.

### Soundness
3

### Presentation
3

### Contribution
2
