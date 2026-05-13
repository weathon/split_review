# AI2TALE: An Innovative Information Theory-based Approach for Learning to Localize Phishing Attacks

- Decision: Accept
- Scores: 8, 3, 8

## Abstract
Phishing attacks remain a significant challenge for detection, explanation, and defense, despite over a decade of research on both technical and non-technical solutions. AI-based phishing detection methods are among the most effective approaches for defeating phishing attacks, providing predictions on the vulnerability label (i.e., phishing or benign) of data. However, they often lack intrinsic explainability, failing to identify the specific information that triggers the classification. To this end, we propose an innovative deep learning-based approach for email (the most common phishing way) phishing attack localization. Our method aims to not only predict the vulnerability label of the email data but also provide the capability to automatically learn and figure out the most important and phishing-relevant information (i.e., sentences) in the phishing email data, offering useful and concise explanations for the identified vulnerability. 

The extensive experiments on seven diverse real-world email datasets demonstrate the capability and effectiveness of our method in selecting crucial information, enabling accurate detection and offering useful and concise explanations (via the most important and phishing-relevant information triggering the classification) for the vulnerability of phishing emails. Notably, our approach outperforms state-of-the-art baselines by 1.5% to 3.5% on average in Label-Accuracy and Cognitive-True-Positive metrics under a weakly supervised setting, where only vulnerability labels are used without requiring ground truth phishing information.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work addresses the problem of phishing attacks and introduces an information theory-based model called AI2TALE to detect them without requiring ground truth while also providing explainable results. The authors validate this model on seven diverse real-world email datasets, demonstrating that the AI2TALE model achieves state-of-the-art results. The model is also tested with human participants, who found it helpful for detecting phishing attacks.

### Strengths
Overall, this is a well-written and clearly explained work. The motivation and contributions are effectively communicated, as are the details of the algorithm, including the model architecture and data. According to the results presented in the tables, the AI2TALE model achieves state-of-the-art performance in detecting phishing attacks based on two measures—Label-Accuracy and Cognitive-True-Positive—which the authors believe are more appropriate for this task. The model also achieves state-of-the-art results with the well-known F1 score. The results are also validated by humans who found this model helpful. Another strength of this paper is that the results of this information-theory-based model are explainable, a claim that appears valid based on the presented figures. Finally, all code is reproducible and open-source.

### Weaknesses
I have included a few comments regarding the presentation and also have some feedback on the experimental section.
   
   A) Presentation Comments
   
   A1) In lines 058 to 060, where you mention that early-stage AI approaches are among the most effective solutions for preventing and reducing negative effects, this seems like a strong statement. It would be beneficial to include a citation to support this claim.
   
   A2) In line 152, you introduce the term "AI2TALE" for the first time as the name of your model. It would be helpful to clarify what this acronym stands for and briefly explain your rationale behind the name selection.
   
   A3) In line 330, you refer to your method as “Algorithm 1.” Since this is the only algorithm presented in your paper, it is unnecessary to number it as "1." Consider renaming it simply as “Algorithm” throughout the text.
   
   A4) In Section 4.1, “Studied Datasets” (lines 360-371), you list several datasets used in your research. Please add citations and links for each referenced dataset. Additionally, include citations and links in Section 6.2 of the appendices (lines 778-788).
   
   A5) In line 404, you mention that readers seeking more details can refer to the appendices. Please specify the exact section or appendix that contains the relevant information.

   A6) In Section 6.2 of the appendices (lines 789-799), this paragraph appears to be more relevant to the following section, 6.3, on data preprocessing and embeddings.

   A7) The link of your code, see line 897, should be in the main paper, such as in the introduction. 

A8) As mentioned in the author guidelines (see https://iclr.cc/Conferences/2025/AuthorGuide), you are encouraged to include a Reproducibility Statement at the end of the main text. This statement should detail the efforts made to ensure reproducibility and include any necessary information for those wishing to replicate your results.

   A9) You have referenced a good selection of papers with nice variation; however, I think a few relevant papers are missing. These include "Feature-based Learning for Diverse and Privacy-Preserving Counterfactual Explanations" by Vy Vo et al., "The Anatomy of Deception: Measuring Technical and Human Factors of a Large-Scale Phishing Campaign" by Anargyros Chrysanthou et al., "Towards Modeling Uncertainties of Self-Explaining Neural Networks via Conformal Prediction" by Wei Qian et al., and "DIB-X: Formulating Explainability Principles for a Self-Explainable Model Through Information Theoretic Learning" by Changkyu Choi et al. In the related work section of the appendices or the main paper, you could also include additional studies based on information theory that are not necessarily related to phishing attacks.
   
B) Experimental Section Comments
    
   B1) In Table 1 (line 424), you present the results for each model. Since you used multiple datasets, it would be helpful to show the results for each dataset separately.
    
   B2) In Table 2 (line 443), it would be nice to include the second and third sentence top sentences of the model highlighting them with different colors and briefly discussing them.
    
   B3) In the human evaluation section (line 493), please include any available statistics on the participants, such as their expertise, gender, education level, etc.

   B4) In Section 6.7 of the appendices (lines 899–960), Table 3 presents results that, in my opinion, are quite significant and provide further support for the strength of your model. It would be better to incorporate the results from Table 3 into Table 1 and remove the "average" section.

### Questions
1) In line 271, you mention that $p(\tilde{x_i}|X)$ is a Gaussian mixture distribution. Why did you choose this distribution? Did you evaluate the effect of this assumption on your results?
    
  2) In your algorithm (see line 333), you split an email into sentences based on periods or commas. Have you examined whether this sentence-splitting method impacts your results? There are alternative ways to split text, such as by a specified number of characters.
    
  3) Based on the main paper and appendices, it appears you developed a feed-forward neural network (see lines 879–881) for the selection model in your algorithm (see line 339). My understanding is that this neural network creates word embeddings based on the provided texts and then focuses on detecting phishing attacks. Why did you choose this model instead of a more advanced architecture, such as a transformer?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper builds a system that identifies both, whether an email text is a phishing attack and which top-1 sentence in the email has the highest contribution to the classification label. The method is based on information theory, which is used by the model to distribute importance weights to features. The paper claims that this is one of the first works in phishing localization and that XAI techniques have not been applied to phishing attacks in the literature. By comparing against 7 open source datasets and 5 popular baseline methods, the method shows an improvement of 1.5-3.5% over baselines.

### Strengths
It is good to focus on explainable approaches so we can understand what ML models do. The method uses information theory approaches, which is indeed an innovative angle.

### Weaknesses
Firstly, the claim that this is one of the only works for interpretable phishing localization might be inflated. There is plenty of work in the domain of phishing attack detection that builds ML models and applies XAI techniques to understand why something was labelled as a phishing attempt, see e.g., [1-2] as just two random examples. These techniques even go beyond text and also tag why images or URLs were considered phishing. Thus, the novelty of this approach is severely lacking. Please provide a more detailed comparison of the proposed approach to existing XAI techniques in phishing detection, highlighting specific differences in methodology or capabilities.

Second, one of the most popular explanation techniques for text, especially for deep nets is the attention mechanism. The proposed approach seems to somewhat achieve a similar goal by learning one model that both classifies text as phishing and also discovers features (sentences) that led to the classification decision. Yet, the paper makes no mention of this popular technique, nor do they compare with it in terms of fidelity, speed, correctness, etc. Thus, there is insufficient comparison with existing methods. The authors are advised to include a comparison with attention-based methods, evaluating aspects like fidelity, speed, and correctness. 

Third, the writing can substantially be improved. There are several typos that hinder comprehension. A non-exhaustive list: page 2, second last para -> which information causes. page 4, first sentence -> given an email. page 5, line 255 -> we encourage. 


[1] Chai, Yidong, et al. "An explainable multi-modal hierarchical attention model for developing phishing threat intelligence." IEEE Transactions on Dependable and Secure Computing 19.2 (2021): 790-803.
[2] Lin, Yun, et al. "Phishpedia: A hybrid deep learning based approach to visually identify phishing webpages." 30th USENIX Security Symposium (USENIX Security 21). 2021.

### Questions
Please see below some questions and comments to improve the manuscript:

- Overall, the terminology used in this paper, e.g., phishing attack localization and phishing vulnerability are atypical for the cybersecurity community. Page 1, para 2 states that AI has been used for malware vulnerability detection. Malware detection and vulnerable code detection are two entirely different sub-domains. Moreover, page 3 states that post-hoc explanations do not offer a comprehensive understanding of the model's internal architecture or workings. Overexaggerated claim. Model-based XAI techniques like integrated gradients do exactly that! Deep models are also called "self-explanatory" methods in the manuscript. Again, popular literature dictates that deep learning is inherently a black box and thus cannot be self-explanatory/interpretable. The authors are advised to revise the manuscript and avoid redefining terms that already exist in the domain.

- This work is not the first or the only work that labels an object as phishing and identifies which features led to the classification decisions. Could the authors present a comparative analysis against existing methods, e.g., [1-2], and justify why they were not mentioned in the manuscript? 

- Please add references for the datasets mentioned on page 7.

- Please include the definition of the evaluation metrics (especially cognitive true positive) in the main body text (Section 4.2). Without the definition, it is impossible to understand the results. 

- The significance of the results in table 1 are hard to interpret because the authors do not provide any information regarding the dataset, e.g., number of phishing emails, sentences per email etc. Moreover, the improvement in the results is marginal (1-3%). Does the proposed approach provide benefits beyond the results in Table 1?

- Please also report false positives and false negatives for each method in table 1. FPs are especially a big problem in cybersecurity tasks.

- Please provide more details regarding the human study. 25 participants don't seem statistically significant for 10 emails, each with 5 options, as estimated by Cochran's formula. Moreover, it is unclear what questions are asked or how they are phrased exactly. For instance, if the participants are always shown the top-1 sentence and not given an option of top-3 sentences, this can very likely be interpreted as a rhetorical question, which leads people to respond in the affirmative most of the time. The authors are advised to increase the sample size to a statistically significant level, provide the exact phrasing of questions asked, and include control questions or alternative options (like top-3 sentences) to reduce bias.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel approach to phishing attack localization using deep learning and information theory principles. The method aims to classify emails as phishing or benign and explain these classifications by identifying the most relevant information within the emails. In short, phishing attack localization aims to customize phishing attacks to align with a target region or group's specific cultural, linguistic, and contextual characteristics. The paper examines how localized phishing tactics, such as using native language, regional events, or imitating local institutions, enhance the effectiveness of phishing campaigns by increasing their credibility. The study compares localized versus generic phishing attacks and highlights key factors that improve success rates. It also discusses the growing role of AI in automating localization efforts, presenting a challenge for organizations to develop stronger, region-specific defense mechanisms to counter these advanced attacks. The authors have conducted extensive experiments on multiple datasets to demonstrate the efficacy of their approach. Overall, it’s an interesting paper with a sound contribution.

### Strengths
Strengths:
- Original Contribution: The proposed method (enhances explainability) is a significant improvement in phishing defense and a good use of AI.
- The use of information theory and the mutual information training principle to select relevant features is well-founded. The introduction of a selection network that utilizes latent variables to identify important sentences is also good.
- The authors provide thorough evaluations across seven diverse datasets. The comparative performance metrics (Label-Accuracy and Cognitive-True-Positive) are appropriate and lend credibility to their claims of improved performance over baseline models.
- The paper is well-organized, with clear sectioning and logical flow. The introduction succinctly frames the problem and the proposed solution, making it accessible even to readers less familiar with the technical intricacies.
- The use of human evaluations to assess the interpretability of the selected sentences enhances the practical relevance of the findings.

### Weaknesses
Weaknesses:
- It could be good to add a more elaborate discussion of the ethical implications of deploying this AI-based system in real-world applications, particularly concerning privacy concerns and the risk of misclassification.
- The authors acknowledge potential limitations regarding selecting non-relevant sentences. A more thorough discussion of these limitations and how they might affect real-world applications would be good. For example, the risk of misclassification and potential consequences of user confusion arising from irrelevant explanations.
- The paper mentions the introduction of hyperparameters in the mutual information maximization and data-distribution mechanisms. It would be good to elaborate on the model’s sensitivity to these hyperparameters and their impact on the performance. It would also be beneficial for the authors to discuss how the introduced hyperparameters are likely to generalize to different contexts and model types. Understanding whether these hyperparameters remain effective across various datasets or when applied to different phishing detection frameworks.
- The results section could benefit from more visualizations (figures or tables) to make the results more digestible and better illustrate the performance improvements.

### Questions
- The paper compares the proposed method with state-of-the-art AI-based approaches. Did you consider including a more elaborate discussion of how traditional (non-AI) phishing detection methods, such as URL filtering and white and blacklisting IPs, sandboxing, etc.,  can be complemented by or replace improvements offered by AI2TALE?
- Can you elaborate on what defense mechanisms organizations should prioritize to counter the increasingly sophisticated, region-specific threats posed by localizaion?

### Soundness
3

### Presentation
3

### Contribution
3
