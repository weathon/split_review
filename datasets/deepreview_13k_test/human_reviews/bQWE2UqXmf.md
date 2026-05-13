# Raidar: geneRative AI Detection viA Rewriting

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
We find that large language models (LLMs) are more likely to modify human-written text than AI-generated text when tasked with rewriting. This tendency arises because LLMs often perceive AI-generated text as high-quality, leading to fewer modifications. We introduce a method to detect AI-generated content by prompting LLMs to rewrite text and calculating the editing distance of the output. We dubbed our gene\textbf{R}ative \textbf{AI} \textbf{D}etection vi\textbf{A} \textbf{R}ewriting method \textbf{\raidar}.  \raidar  significantly improves the F1 detection scores of existing AI content detection models -- both academic and commercial -- across various domains, including News, creative writing, student essays, code, Yelp reviews, and arXiv papers, with gains of up to 29 points. Operating solely on word symbols without high-dimensional features, our method is compatible with black box LLMs, and is inherently robust on new content. Our results illustrate the unique imprint of machine-generated text through the lens of the machines themselves.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses the problem of detecting AI-generated text. It makes a hypothesis that LLMs, when asked to rewrite, are more likely to modify human-generated text than AI-generated text. The hypothesis is based on the observation that AI-generated text is generally of higher quality than the average human-generated text and therefore needs fewer modifications. The work proposes a method for detecting AI-generated text based on the above hypothesis. The proposed method essentially involves asking LLM to rewrite the text and computing the edit distance between the input and the rewritten text. In this context the work introduces the notions of invariance, equivariance and uncertainty. Invariance is measured as the modification distance between the input and the LLM-rewritten input. Equivariance is measured as the modification distance between the rewritten text and the text obtained by transforming the input, rewriting and finally undoing the transformation. Uncertainty is measured as the average modification distance between different rewritings of the input by the same LLM with the same prompt. 

The work reports results from an experimental study of the proposed approach on several datasets and compares with several baselines. Invariance based scoring gives significantly better results than the baselines while equivariance and uncertainty based scoring also do well. The work also reports results from a study on robustness, source of generated data, different LLMs for rewriting, and impact of prompts used for rewriting, and the length of the input text.

### Strengths
1. Simple method for detecting AI-generated text that essentially consists of asking LM to rewrite the input and then computing edit-distance between the input and the rewritten text. Computationally simple.

2. Significant improvement in detection effectiveness over the baselines.

3. Interesting study on robustness, source of generated data, different LLMs for rewriting, impact of prompts used for rewriting, and the length of the input text.

### Weaknesses
1. Proposed method is critically dependent on LLM. Any change to LLM due to continual fine-tuning with new data might have unknown consequences for the detection method. The method might not be robust to LLM fine-tuning.

2. Though the proposed method is simple and computationally low cost, there is a cost associated with every call to the detection algorithm because of the calls made to LLM for rewriting. This might not be acceptable in some scenarios it is cheaper and desirable to have a model decoupled for LLM after training.

### Questions
1. In Table 1 you write "The results are in domain testing, where the model has been trained on the same domain." but you also use the term "in distribution" Are these equivalent terms?  I assume you consider each of the datasets as a different domain (e.g. news domain vs creating writing).  What is the difference between in-distribution and in-domain?

2. In Table 2, what is the domain for training and what is the domain for testing?

3. Would the effectiveness of detection improve further if multiple LLMs are asked to rewrite the input text and invariance scores for each LLM are used as features for training the logistic regression classifier? Also, would edit distance between the rewritten texts from different LLMs be useful as additional features for such a classifier?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to use rewriting as a task to detect whether a text is generated or not. They show that LLMs rewrite the text less when given a LLM-written text as opposed to a human-written text. The paper introduces a method that is based on prompting LLMs to rewrite text and calculating the editing distance of the output. This approach significantly improves the detection of LLM-written texts across domains.

### Strengths
* The paper tackles on a task that is very important to help mitigate the misuse of LLMs.

* The method proposed is simple yet effective. It is also very intuitive since it is actually also human nature to prefer (=critic less) your own writing than others.

* The paper is very well written.

### Weaknesses
* It would be nice to actually check the quality of human/LM written ext., i.e. which between the human and LM text do another set of humans prefer? It could be that the LM-written text is actually better quality (and thus requires fewer rewrites).

* It would be nice to include a discussion on how this method fares when the LLM is instruction-tuned to do rewrites the way humans do rewrites. Given that text rewriting is a widely used use case for LLMs, it would not be a surprise if these models are instruction-tuned on a task mixture that includes text rewriting.

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper provides a new approach for detecting LLM-generated text, based on the insight that LLMs will make minimal edits when asked to rewrite their own generations. The paper proposes three related detection models called Invariance, Equivariance, and Uncertainty and shows that they outperform state-of-the-art detectors such as Ghostbuster, DetectGPT, and GPTZero on a variety of paragraph-level detection tasks. The paper also introduces three new domains of generated code, Yelp reviews, and arXiv abstracts, finding that the model again outperforms existing baselines. While the paper has some missing details and would benefit from additional rounds of proofreading, the core idea and results lead me to recommend acceptance.

### Strengths
- The core idea in this work, that LLMs are less likely to make extensive edits to LLM-written text than human-text, is an intuitive and seemingly very reasonable approach.
- The paper obtains impressive performance compared to state-of-the-art models (Ghostbuster and GPTZero). In particular, the model seems to work especially well on short documents, which is a known failure mode for existing approaches
- The paper introduces three new detection datasets (Yelp reviews, code, arXiv abstracts) and evaluates on them in addition to an existing

### Weaknesses
1. The paper is missing some important details. For example, the paper does not provide a complete explanation of how the human reviews from the Yelp dataset were selected, nor does it provide a full explanation of how GPT 3.5 was prompted to generate data in the code/Yelp/arXiv domains. The paper also does not describe which scoring model was used for the DetectGPT results. 
2. I believe the results on OOD generalization are slightly misleading. Because DetectGPT and GPTZero should produce the same scores in-domain and out-of-domain, GPTZero actually has the highest score for the OOD creative writing task
3. Table 4 (robustness across generation models) is difficult to interpret without results from the baselines. Although the model seems to generalize well to generators it was not originally trained on (ada and davinci), these are also weaker models which (as stated in the table caption) results in an easier detection problem. Additionally, generalization results in the paper would benefit from the inclusion of models which are not from OpenAI, since these are likely more similar to one another than models like Claude, LLaMA, etc. 

MISCELLANEOUS SUGGESTIONS
- A small suggestion on related work: the introduction starts that token log probabilities are not available in black-box models such as GPT-3.5 and GPT-4, which is true. I think the paper would benefit from distinguishing “scoring models” from “target models” when discussing how this affects related work. DetectGPT is designed to only work when the scoring and target model are the same (cf. Figure 6 in their paper), although Ghostbuster operates under the assumption that the scoring and target model are different (but still requires access to generated documents from the target model). 
- Minor: Figure 6 text is too small to read and would benefit from error bars
- The paper has a large number of typos and grammatical errors. Although this does not affect my review score, the paper would benefit from an additional round of proofreading.

### Questions
1. Are all detection tasks in this paper at the paragraph level? How does the median length of documents vary across tasks? Did you try the method for any longer documents?
2. Did you experiment with combining the invariance, equivariance, and uncertainty features?
3. How was the impact of context length experiment run? In Figure 5, how many examples were included for each point on the plot?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses work on detected AI-generated text using rewriting. The authors formalize their hypothesis which “a generated text from an auto-regressive generative models retains a consistent structure, which another such model will likely to also have a low loss and treat it as high quality”. The proposed method captilizes of this hypothesis through quantifying rewrites in the form of edit distance scoring which the author/s use to train classifiers for the detection phase. The author/s also propose several variations of symbolic modifications including invariance, equivariance, and uncertainty. The author/s select previous well-known detector systems including GPTZero, Ghostbuster, and DetectGPT for the comparison of detection performances on 6 datasets. The author/s report favorable results of the proposed method in in Tables 1 and 2. Other experiments done include robustness in an adversarial setup using paraphrasing, effects of content length, quality of generated data, and type of detection model but these parts seem condensed and not thoroughly discussed.

### Strengths
The paper discusses work on an interesting framing of detecting text generated by large language models by gauging how much rewrites (edit distance) it gives to a piece of text with the hypothesis that it considers machine-generated texts, regardless of specific models, as high quality ones compared to human-generated texts. The simplicity of the method is what I appreciate the most with the paper. I also appreciate that the author/s are able to construct a good research plan for the methodology of the study and the formalization of the task. There are some revisions suggested below to improve the structure and organization of the paper, particularly the uniformity and presentation of results.

### Weaknesses
The paper starts well with the introduction, statement of motivation, discussion of hypothesis, and proposed method but went downhill with the presentation of results.

First, in the discussion of datasets and model baseline used, the definition and characteristics should definitely be expanded by including the size of the dataset plus other unique characteristics of the data that’s worth mentioning as well as the quantified performance of the baseline models just to give an idea to the readers of their relevance and why they are being used/compared in the study. 

Second, the discussion on Section 4 seems to be too condensed and there are sudden insertions of models for comparison. Claude was tested but was not mentioned in the baseline models. Why is that and why is Claude a viable candidate for comparison? 

Third, there is no concrete / definitive discussion for the results presented in Table 1 and 2 and these are the bread and butter of the study. The table captions and Section 4.3 simply state the observed increments against the previous systems and nothing more. I would have appreciated it if there are more discussions on particular weaknesses in the texts by previous works which the current work addresses, and give some examples of this. Why are proposed methods get big performance jumps, say in the code dataset and Arxiv dataset, compared to natural language datasets? In the robustness experiments, why are the previous detector models left out? It is important to still consider them in the mix for better comparison of true performance. These discussions should be in order.

The statement “text from the Ada model is most easily detected, possibly due to its discernibly lower quality compared to human-written content” is speculation. Some form of quantitative proof is required for this.

In terms of strengthening the paper, I strongly suggest the author/s to also experiment with second-language or non-native speaker writing corpora such as TOEFL or ESL essay corpus to gauge if the proposed method also exhibits that particular limitation of confusing AI-generated texts with non-native speaker-written texts. This has been a known limitation across all detectors of machine-generated texts. Refer to the existing works (https://arxiv.org/abs/2304.02819) and databases online (https://www.clarin.eu/resource-families/L2-corpora, https://uclouvain.be/en/research-institutes/ilc/cecl/learner-corpora-around-the-world.html) for the data to be experimented with. Regardless of the result, this would be a great addition and insight to the paper.

Lastly, the paper is littered with inconsistencies and wrong format for in-text citations which makes it very confusing to read. For example, it’s better to read referenced text as “Ghostbuster (Verma et al., 2023) instead of Ghostbuster Verman et al (2023)”. It seems like the Verma is included in the name of the model but it’s not. There are also cases where the model is “GPT-3.5-Trubo” and then becomes “GPT-3.5-turbo”. Diagrams in Figure 6 should conform to uniform range of [0.0,1.0] in the y axis.

I still see the importance and contribution of the study but major revision is required for the paper in order for readers to fully comprehend and appreciate the work.

### Questions
1. How large is the feature set or dimension then for training the classifiers? Did the author/s conduct and hyperparameter optimization with the classifiers?

2. How is the setup for comparison done for preliminary experiments shown in Table 1 and 2? What classifier was used for these experiments? There were two algorithms mentioned (LR and XGBoost) but it was never specified in the tables. The same way goes for Tables 4 and 5. I’m confused as a reader as to which classifier was used for the presentation of results. Revising this part and enriching the details should be in order.

3. Is the number of changes (deletions, insertions) done by the selective generative models between humans and machine-generated texts statistically significant? The visualization in Figure is nice but this would have been an additional supporting preliminary information to add to the hypothesis.

4. There are six datasets chosen for experimentations but why are only subsets or some of it are used for results presented in Table 3, 4, and 5?

5. The statement in Section 4.4 goes “In Table 5, while all models achieve significant detection performance”. So a statistical test was conducted? Can you give the details for this? Otherwise, I suggest using the word substantial instead.

6. Why is only the Yelp data used for special test cases such as effect of content length? Why not the other datasets as well? This seems very selective without reason.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
