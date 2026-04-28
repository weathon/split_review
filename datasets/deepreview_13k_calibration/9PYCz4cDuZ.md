# Theoretical Aspects of Bias and Diversity in Minimum Bayes Risk Decoding

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
Text generation commonly relies on greedy and beam decoding that limit the search space and degrade output quality. Minimum Bayes Risk (MBR) decoding can mitigate this problem by utilizing automatic evaluation metrics and model-generated pseudo-references. Previous studies have conducted empirical analyses to reveal the improvement by MBR decoding, and reported various observations. However, despite these observations, the theoretical relationship between them remains uncertain. To address this, we present a novel theoretical interpretation of MBR decoding from the perspective of bias-diversity decomposition. We decompose errors in the estimated quality of generated hypotheses in MBR decoding into two key factors: *bias*, which reflects the closeness between utility functions and human evaluations, and *diversity*, which represents the variation in the estimated quality of utility functions. Our theoretical analysis reveals the difficulty in simultaneously improving both bias and diversity, and highlights the effectiveness of increasing diversity to enhance MBR decoding performance. This analysis verifies the alignment between our theoretical insights and the empirical results reported in previous work. Furthermore, to support our theoretical findings, we propose a new metric, pseudo-bias, which approximates the bias term using gold references. We also introduce a new MBR approach, Metric-augmented MBR (MAMBR), which increases diversity by adjusting the behavior of utility functions without altering the pseudo-references. Experimental results across multiple NLP tasks show that the decomposed terms in the bias-diversity decomposition correlate well with performance, and that MAMBR improves text generation quality by modifying utility function behavior. Our code will be available at https://github.com/[Anonymized].

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work aims at analyzing the characteristics of Minimum Bayes Risk (MBR) decoding through a bias-diversity/variance decomposition. On various tasks (e.g., MT, summarization, image captioning) and with a collection of sampling methods for generating pseudo-references, the authors show correlations between the bias, diversity, and overall MSE measures in MBR and the task performance. The authors argue for the importance of the diversity/variance measure in particular and propose a MAMBR approach that uses multiple loss functions to enhance MBR decoding.

### Strengths
This paper tackles an interesting problem of analyzing and enhancing MBR decoding. The experiments were conducted with multiple models, sampling methods, and tasks, ranging from pure text to multimodal scenarios. The writing is overall clear.

### Weaknesses
(1) Eq. (8) has counterintuitive namings. The L.H.S. of the equation corresponds more to the usual "bias" term and the current bias term on the R.H.S. corresponds more to the usual "MSE" term. Using the regular terminology, isn't the equation just MSE = bias^2 + variance?

(2) The work motivates with human-estimated quality (f hat) throughout the work, but uses a pseudo-bias that measures the metric/loss to gold references. The correlation between the pseudo-bias and actual human-estimated quality is not discussed.

(3) Meaningfulness of Figure 1. Since the pseudo-biases are direct functions of the gold references, the correlation between them and the task performance (also based on gold references) is less interesting. The diversity/variance measure can be interesting, but the correlation is also weaker. Also, for all of the reported correlation numbers, there are no associating p-values. 

(4) Effectiveness of MAMBR. The proposed MAMBR simply uses multiple rather than one metric/loss in the MBR calculation. The results in Table 1, 2 and 3 consistently show no or extremely small improvement of MAMBR over regular MBR decoding.

### Questions
N/A

### Soundness
2

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
### tldr;

This paper provides valuable theoretical insights through its new framework decomposing bias and diversity in MBR decoding's quality estimation errors. The theoretical contribution is significant and well-presented. However, the empirical section needs improvement. The experimental results are unclear and would benefit from better explanation and presentation. I would appreciate if the authors could address the specific concerns raised in the Weakness section.

### Summary 

- This paper presents a bias-diversity decomposition of the quality estimation error in Minimum Bayes Risk decoding
- The quality estimation error measures the discrepancy between the estimated quality using MBR decoding and the human judgement.
- Based on this decomposition the authors provide a novel theoretical interpretation of MBR decoding. -
	- The bias term captures the closeness between utility function and human evaluations i.e. the closeness between the human estimated quality and the quality estimated with a utility function.
	- The diversity term captures the variation in the estimated quality across different utility functions. Surprisingly this has a negative sign, suggesting that more diverse generations lead to lower error.
- Background in MBR:
  In MBR decoding the goal is not to find the most probable generation as is the case in typical beam-search decoding but rather find a generation that minimizes the expected risk for a given loss function and true posterior distribution
	- In practice, instead of expected risk, expected utility is computed by taking 1-risk. The expected utility is computed by comparing a generation to all other generation samples. Intuitively, MBR decoding ends up doing consensus decoding, i.e. picking generations which on average are most similar to other generations.
	  
- The authors propose a new metric, pseudo-bias to approximate the bias term using gold-references since human judgements are expensive to obtain.
- The authors also propose a new MBR decoding approach called Metric-augmented MBR which increases diversity by adjusting the behavior of utility functions without altering the pseudo-references.
- In Section 3.3 the authors provide an interpretation of this theoretical decomposition and its relation to prior studies.

### Strengths
### Strengths
- The interpretation provided in section 3.3 is particularly nice as it provides additional evidence from prior work. I also like the explicit calling out of "Unexplored Aspect" which is lated discussed in section 4.2 and 5.4.
- I admire the scholastic writing rigor of the paper. The authors have generally cited prior work well going back decades, a practice which is commonly missing in recent ML literature. However, some more details on Minimum Bayes Risk Decoding could further strengthen the paper and make it self-contained.
- The results of experiment in Section 5.4 for adjusting the diversity term by varying model parameters and pseudo-references respectively are convincing

### Weaknesses
### Weakness
- Section 5.2:
	- Based on the theoretical decomposition a reader might expect the overall MSE to have highest correlation with performance; followed by overall bias and overall diversity. It is not clear as to why the one best bias or one best MSE correlates more strongly with performance than overall MSE. This does not provide a strong evidence for the theoretical decomposition presented. The authors should clarify why the correlation with one-best metrics is more indicative of the theoretical decomposition than the overall metrics, given that the decomposition is defined over the entire set of generated samples. The current analysis seems to prioritize the final selection over the entire process, which is not fully justified by the presented theory.
- I found Figure 2 to be confusing. For e.g. consider this sentence "The results show that while ancestral sampling exhibits the highest bias, except in the case of the SAMSum dataset, it sometimes outperforms other sampling methods owing to its greater diversity." This statement is clearly false based on the plots.  For many plots bias and diversity move in the same direction as is predicted by the theoretical relationship but for many plots they move in opposite directions. For e.g. consider the plot for MSCOCO dataset. The overall bias and the one best bias go down while the overall diversity increases. The interpretation of Figure 2 needs to be revised to accurately reflect the observed trends. The current description does not align with the visual data, and the authors should provide a more nuanced explanation of the interplay between bias and diversity across different datasets and sampling methods. The claim that ancestral sampling's performance is due to its diversity is not consistently supported by the data presented.
- Going beyond the math, at an intuitive level, it is difficult to interpret the diversity term. From my understanding, MBR decoding tries to select generations which on average are similar to most other generations. However, the diversity terms suggests that having diverse generations actually leads to better estimation of quality error and thereby better performance. Though MBR is trying to do something exactly opposite to this. It is difficult to reconcile this tension and some more discussion in building the intuition around this is lacking in the paper. The paper needs a more thorough discussion on the counter-intuitive nature of the diversity term. The current explanation does not fully address the apparent contradiction between MBR's goal of selecting consensus generations and the finding that diverse generations improve quality estimation. A more detailed analysis of how diversity contributes to better error estimation, despite MBR's inherent tendency towards consensus, is needed.

### Questions
Please refer to the concerns raised above.

### Soundness
2

### Presentation
3

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
This paper introduces a bias-diversity decomposition for Minimum Bayes Risk Decoding. The bias reflects the distance between the utility functions and human evaluations, while diversity represents the variation. The analysis and experiments show that a lower bias and a higher diversity will lead to better model performance. It also proposes a Metric-augmented MBR, which use multiple utility functions with various parameters to enhance diversity.

### Strengths
1. It provides a bias-diversity view of MBR, which highlights the importance of several factors in MBR, such as the quality of utility functions / pseudo reference.  
2. The analysis is verified by the correlation between the bias / diversify of MBR with the model performance. It further investigates the influence of different sampling methods and the size of pseudo preferences.

### Weaknesses
1. The main weakness is the novelty and the contribution is limited. Although it proposes a bias-diversity decomposition of MBR, such decomposition is straightforward. The observations listed in Section 3.3 have mostly been covered in other literature, resulting in limited new insights.  
2. The Performance of MAMBR with ancestral sampling/epsilon sampling/beam decoding is not significantly better than the baseline model, which weakens the paper's claim.

### Questions
For all three tasks, the utility function and the evaluation metric are the same. What will Figure 1 be if the utility function is different from the evaluation metric?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper offers a theoretical perspective on MBR decoding by decomposing the discrepancy between automatic MBR scores with the human evaluations using a bias-diversity decomposition. Their analysis suggest that one may want systems that minimize bias but also the diversity should be increased, which aligns with previous paper’s empirical results. They then analyse performance of MBR decoding in several scenarios and show that the analysis holds, where models with higher diversity and lower bias have better correlations. They then introduce MAMBR, which aims to maximise diversity by modifying the behavior of the utility functions. Results show marginal gains in performance across different tasks, while using a similar number of sampled pseudo-references.

### Strengths
- The paper decomposes the MBR decoding into cleaner interpretations of bias and diversity, which can shed light on the MBR expression.  The resulting expression appears fairly elegant, especially if it explains existing empirical observations, which the paper linked to, where increasing diversity was shown to be helpful. 

- Their results show that increasing the diversity through MAMBR can result in better performance across 3 different tasks and various numbers of models without the need for any further references.

### Weaknesses
 - As I understand it, the approach uses pseudo-references, which are then used to approximate the human evaluation scores (by averaging over different references), which may impact the results. The generated hypothesis and the references appear to be generated from the same model just using different sampling strategies, which may result on a lot of similarity between the two systems and underestimate the bias for different approaches in Figure 2 than if independent human evlauation scores were used to assess the bias. Specifically, the use of model-generated pseudo-references, while common in MBR, introduces a potential circularity. Since the same model generates both the hypothesis and the references, the bias calculation might be skewed, as the model's inherent biases are present in both. This could lead to an underestimation of the true bias, especially when comparing different MBR decoding strategies, as the pseudo-references might not accurately represent the diversity of human-generated references.

- The results in Table 1, 2 and 3 seem quite marginal, and there hasn’t been any quantification of the significance of the results. The lack of statistical significance testing makes it difficult to ascertain whether the observed improvements are genuine or simply due to random variation. The effect sizes appear small, and without p-values or confidence intervals, it's hard to determine the practical relevance of the proposed MAMBR method. For example, a difference of 0.1 in BERTScore might not be meaningful in practice, and it's crucial to provide evidence that these differences are not just noise.



### Questions
- I personally found parts of the experimental section a bit confusing. Though the theoretical aspect was mostly quite clear and made sense, from section 5 onwards, I found the results a bit less clear, possibly due to my having less familiarity with previous works. I wasn’t clear on what was used as the references, the hypothesis and how performance was measured. As I understand it, the same models generated both the hypothesis and the references which are used in MBR decoding (just with different sampling approaches). Is this correct? Also are there are ground-truth human evaluation scores available, which performance is measured against, or are all results pseudo results using equation 10?

- In MAMBR you stated that “we train evaluation metrics with different initial random seeds to generate Θ as a set of diverse model parameters” but the evaluation metrics used appear to be external packages (e.g. COMET, BERTScore) that were leveraged. How exactly did you then implement MAMBR?

- In line 93 you say “Here, instead of using …” Is the here intentional, and describing the previous equation, or just introducing the new approach of using manual selection of the best hypothesis (equation 3). There are a few more instances of this in the earlier sections

### Soundness
3

### Presentation
2

### Contribution
3
