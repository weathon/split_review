# DeFine: Enhancing LLM Decision-Making with Factor Profiles and Analogical Reasoning

- Decision: Reject
- Scores: 5, 3, 6, 6, 6

## Abstract
LLMs are ideal for decision-making due to their ability to reason over long contexts and identify critical factors. However, challenges arise when processing transcripts of spoken speech describing complex scenarios. These transcripts often contain ungrammatical or incomplete sentences, repetitions, hedging, and vagueness. For example, during a company's earnings call, an executive might project a positive revenue outlook to reassure investors, despite significant uncertainty regarding future earnings. It is crucial for LLMs to incorporate this uncertainty systematically when making decisions. In this paper, we introduce \textsc{DeFine}, a new framework that constructs probabilistic factor profiles from complex scenarios. \textsc{DeFine} then integrates these profiles with analogical reasoning, leveraging insights from similar past experiences to guide LLMs in making critical decisions in novel situations. Our framework separates the tasks of quantifying uncertainty in complex scenarios and incorporating it into LLM decision-making. This approach is particularly useful in fields such as medical consultations, negotiations, and political debates, where making decisions under uncertainty is vital.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper incorporates factor profiles and analogical reasoning with LLMs to perform decision making in financial scenarios. Experiments are conducted to demonstrate the effectiveness of the proposal in classification like decision making.

### Strengths
• Proposed factor profile as the basic construct to perform decision-making instead of full text. 
•  Prescribed a way to incorporate LLM outputs into Bradley-Terry models for estimating relative strengths of items and for bayes reasoning and analogical reasoning.

### Weaknesses
• The specific factor profile might limit the generalizability of the based LLMs. How to define factor profiles might become a human labor heavy task like the old days' expert systems. 
• The way on how to incorporate LLM output to Bradley-Terry models, bayes reasoning and analogical reasoning is tailored to specific a small number of decision outputs like exemplified decision making. It is not clear how this framework can be applied to open set decision making restricting the original power of LLMs.

### Questions
1. In the abstract, the spoken speech aspect is mentioned as the a key challenge. However, in the main content the spoken aspect of the transcripts are not being given additional attention again and address the spoken aspect explicitly. If there is little special regarding the spoken aspect, it should be fine to not say so in the abstract.
2. Any criteria to select the factors? Why 15 factors are chosen for the financial sector? For other applications, what should be operable rules to identify the right set of factors? What exactly is the "iterative process of querying the LLM for key variables crucial in forecasting stock movements"? How can it be generalized to other domains? 
3. What is the truth power and the insight of the proposal? Is it just about the similarity measure capability of  open set of texts and relevancy prefix-postfix conditional generation capability in LLMs  that replace the original hand-crafted similarity and relevancy in Bradley-Terry models and analogical reasoning?  Please discuss more?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a framework for making stock predictions based on corporate earnings call transcripts called DeFine. It uses an approach that mixes LLM + bayesian decision making: it extracts domain-specific features (factor profiles e.g. "Regulatory changes" or "Political events" that may affect the future stock price) along with the probabilities of a given outcome for each feature using an LLM. The features are suggested by the LLM and filtered by the researchers. It then trains a model that, through paired comparisons, identifies the importance of each feature, to finally create a prediction model. The paper also introduces a dataset of corporate earning calls transcripts that may be useful for future research.

### Strengths
The paper introduces a new dataset for predicting whether to buy a stock given a corporate earnings call, carefully splitting by date, which may be useful for future research.

Its method is also a good example of how to combine LLM +

### Weaknesses
- The framing of the paper could be revised and rescoped: it is presented as a general analogical decision making framework, but in its current form it is only tested for stock prediction, and the feature selection seem specific to the domain. At times, I felt like this work would be better suited for a financial-specific venue. If the paper is reframed to be solely focused on the financial domain, it would be interesting to ground the feature selection on that field's literature.

- **Some claims about LLMs should be softened and/or corrected.** "LLMs are ideal for decision-making due to their ability to reason over long contexts and identify critical factors" is not a statement that should be made lightly, as research in planning with LLMs is still nascent and often requiring to offset the actual planning to more reliable components (e.g. a solver, as in TravelPlanner (Xie et al., 2024); or a domain-specific solver as in AlphaGeometry (Trinh et al., 2024)). There has been extensive research on LLMs reasoning abilities or lack of thereof, e.g. about their lack of generalization to unseen (Dziri et al., 2023). "LLMs are designed to provide reasoning traces for LLM decisions; however, their explanations remain ambiguous": this leaves out the key detail that these explanations are not causal and are often inconsistent with the final decisions or classifications (e.g. Wang et al. 2023). This may affect seriously the reliability of the approach.

- There is some mention about the weaknesses of other methods during the intro ("The latter often require extensive sampling during inference, which tends to increase inference costs and potentially leads to latency issues.") but never directly compared for cost-effectiveness.

- Presentation could be improved to make the methods explanation more focused and clearly define what is the final definition of DeFine. Background on Bayesian Decision Making can be left as a paragraph, and tone could sometimes be adjusted to be a better fit for scientific claims (e.g. "a methodology that optimally integrates textual reasoning with quantitative analysis"). Please consider removing a footnote linking to the Wikipedia page for the definition of “earnings call”.

- Results presentation could sometimes be improved to be able to grasp takeaways, e.g. Figure 2's confusion matrices. Could you have a metric to synthesize these takeaways and move the full confusion matrix to the appendix?

- The variances for Tables 5 and 6 are concerningly low: if the influential factors have a similar salience (all around 0.03), it would defeat the main goal of Section 6.2 of automatically detecting the influential factors and outcomes.

- The cost estimation is not effective as a metric of cost reduction. Having just the difference between the two numbers is not enough. If one of the main advantages of this method is its cost reduction, then this aspect should be clearly quantified.

- The paper should be rescoped to not be presented as a general analogical reasoning frameworks given the uncertainties of adapting to a new domain. This single domain analysis is not properly advertised, as for example it's not possible to know this from the abstract, and make only an educated guess from the intro. There are missed opportunities to better highlight your work, e.g. make concrete statements on the benefits on DeFine in the intro.

- There has been no revision of the paper. It would have been important to see a first stab at this radical change in framing of LLMs' planning abilities. Besides acknowledging that LLMs have limited planning abilities, discussing how this may impact the method's reliability, as it's advertised specifically for high-stakes domains. There could be hallucination issues when summarizing the conversations that would affect the whole method's validity.

### Questions
- In Table 5 and 6, what was the variance in the detected salience? I see all outcomes shown being at around 0.03, but I understand that there may be a sharp decline that might not be shown.
- You mention when discussing Table 3 that “DEFINE performs best at ‘Strong Buy’ recommendations and faces challenges with ‘Strong Sell’ categories. This may be due to its reliance on earnings call transcripts". Isn't this true of all/most methods compared?
- How would you concretely adapt this to other domains? What adaptations would you need to make and what assumptions or prerequisites would this new application need to have?

### Soundness
2

### Presentation
2

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
This paper introduces DEFINE, a framework for enhancing LLM decision-making capabilities in complex scenarios, particularly focused on financial analysis of earnings call transcripts. The key contributions include:
1.A novel framework that constructs probabilistic factor profiles from complex scenarios and integrates them with analogical reasoning
2.A method for quantifying uncertainty in earnings call transcripts using key factors across macroeconomic, company-specific, and historical financial metrics
3.Implementation of the Bradley-Terry model to identify dominant factors and evaluate their collective impact on decision-making
4.Empirical validation showing improved performance over baseline methods in stock movement prediction tasks

### Strengths
1. this paper proposes a way to Successfully combines probabilistic factor profiles with analogical reasoning in a novel way and applied it in real world financial decision-making application.
2.The proposed method are evaluated in detailed ablation studies and verify the effectiveness.

### Weaknesses
1.The evaluation mainly focus on the financial domain and more cross-domain would strengthen the paper’s proposed method and claims.
2.Better and clear writing on some sections such as the Bradley-Terry Model.
3.The 15 factors seems to be quite domain dependent and reply on human experts to select them. How robust does the proposed method against the forecasting factors.
4.In section 2.2, where is w_{xy} and w_{yx} defined? It’s not clear why use EM here, it would be better to add the EM details in the appendix.
5.The analogous reasoning method extract some similar history as context which is similar to RAG, can we add a RAG baseline for comparison?
6.Is there any ablation result without analogical reasoning?

### Questions
1.The 15 factors seems to be quite domain dependent and reply on human experts to select them. How robust does the proposed method against the forecasting factors.
2.In section 2.2, where is w_{xy} and w_{yx} defined? It’s not clear why use EM here, it would be better to add the EM details in the appendix.
3.The analogous reasoning method extract some similar history as context which is similar to RAG, can we add a RAG baseline for comparison?
4.Is there any ablation result without analogical reasoning?

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
3

### Summary
This paper presents a novel approach to financial decision-making using LLMs. The authors propose using LLMs to generate factor summaries and predict outcome probabilities from earnings call transcripts. They also develop a method to find analogous examples from their training data to support the LLM during inference. Authors compare with 3 in-house baselines and 1 additional paper, DeLLMa. They show better performance, then perform ablations and report some insights.

### Strengths
I think there is value in what the authors did and I like the probabilistic grounding. The setup is rather interesting and I like the more targeted selection of in-context examples. Providing LLMs with better ways to do reasoning is a fundamental task.

I appreciate the structured approach here: authors first use an LLM to extract factors/categories from transcript calls and then they associate outcomes to those.

### Weaknesses
Since I'm not a finance expert, I kind of can't fully assess how applicable this approach is in practice. One of my issues is about the core contribution: are the authors essentially proposing an improved method for selecting in-context examples for the language model - “better way” that is, in this case, specific to their finance domain? If so, this, to me, feels very specific and slightly incremental.

While the setup is interesting, I see several limitations in the experimental evaluation:

* With a test set of 500 examples, I'd really like to see standard deviations to understand how reliable the results are, especially for the ablation studies.

* The baseline selection isn't well justified - for instance, is there a baseline that uses the DeFine model without the analogical reasoning component? or with a similarity search of similar transcripts/related factors instead of the analogical reasoning part? I would appreciate if the authors could defend their baselines.

* How does DeLLMa work? why is this a “strong baseline”? I would at least need to see a summary in the paper since this is the only baseline coming from an external work.

* The experimental details are insufficient for reproducibility. The authors do share prompts, but I am not sure which were the temperature, and even if more experiments had been run to account for noise - I understand the authors can probably add this to the camera ready, but still. Which prompts are the ones used for the baselines? the fact that from Figure 5 onwards there is not a backref to the text makes this harder to understand (also, names in the appendix are different from what I see in the paper?)

Minor notes:
* When discussing analogical reasoning, the authors only cite work from 2022 onwards, ignoring fundamental AI literature (e.g., Minsky's 1991 paper comes to mind - which I understand might be out of scope here, but the point still stands). While this might not be their focus, it overlooks important historical context (again, I know this is not the focus of the paper).

* I am putting this into the minor notes since it could be a “me” issue, but to me this paper was a bit too dense to read. Information density is very high, and the paper would benefit from more experiments (e.g., Outcomes are introduced in 2.1 and then defined only later). I had to go up and down the paper a couple of times to recover information. Sections 3 and 4 are very short and would benefit from some restructuring. They can probably be both put under the same main section.

* Not a finance expert, but how can I interpret that F1 score? is it good? Isn’t one of the issues with market prediction the fact that it’s hard to use history to predict the future? Also, I am not sure if I missed that here, but how would a random/simpler baseline perform here?

### Questions
//

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel framework,DEFINE, combining Probabilistic Factor Profile and Analogical reasoning in LLMs to support investment decisions. By using LLMs to extract factor profiles in transcripts, the model captures key information and their outputs in relevant domains. These factor profiles are utilized as analogous examples when the model is tested in unseen scenarios. By providing investment decisions like buying or selling stocks, the authors found that the model outperformed traditional models like DeLLMA and CoT-prompted LLMs. The downstream evaluation also shows that the model performs well in cross-sector domains with the application of analogical reasoning. The authors also investigate the most influential factors in the Consumer Defensive and technology domain, revealing the key information that supports the model's investment decisions. This study sheds light on the application in financial and commercial situations.

### Strengths
- The authors propose a framework, combining Probabilistic Factor Profiles with Analogical reasoning,  endowing the model with a strong generalizability in unseen scenarios and even cross-domain sectors.

- The authors compared five models (including DEFINE) with their performance in making 'correct' investment decisions, which their model outperforms other models in the accuracy metrics. Downstream evaluations are also applied in cross-domain sectors, demonstrating superior performance than random chance level, which makes the result more robust and generalizable.

- The authors also investigate the mechanisms and details of how this model works. By using the Bradley-Terry model, the authors figure out the most important factors from the profiles. The authors also explore the number of optimal analogous examples to provide in the test phase. Finally, the authors also find out the associations between the outcomes in the profile and investment decisions. Overall, the mechanistic analysis shows a step-by-step flow of how the model works.

- The paper's writing and visualization is satisfying.

### Weaknesses
 - One important contribution of the paper is the model adopts a framework with Probabilistic Factor Profiles with Analogical Reasoning. However, in the model comparison, three baseline LLMs are prompted with CoT with different instructions. If I do not understand incorrectly, these models do not contain any training or in-context learning to do the task. While factor profiles may be a good way to do so, I am wondering how well the LLM with purely CoT, with some examples in the context (just like transcripts and their optimal decisions) will perform. This aims to figure out the role of Analogical reasoning in the DEFINE model, which is tested in a more general sense. It is possible that LLM can do analogical reasoning themselves, without showing them explicitly. 

- Currently, the model uses analogous examples based on KL divergence between the current scenario and stored profiles. This is a good intuition to refer but it could strengthen the robustness if more ways are into consideration and compared. For example, there can be another LLM to 'help'  to pick up five examples from the profiles that it thinks referable. Or train a model based on the downstream accuracy and then test the whole pipeline on OOD datasets. 

The authors do not need to do all the proposed analysis but it would be better to clarify the exact role of the two key components in the new model.

### Questions
- One observation for this paper is though the model outperforms other model candidates, the increasing part mainly emerges in the action 'strong buy' for 'sell' actions, the model still fails to figure them out. What could be possible reasons for this phenomenon? Training Data distribution? Or model pipeline?

- Another similar question is why some domains are better in cross-domain but a few of them are not.

These questions are just proposed for further public discussion and do not necessarily mean any supplementary analysis.

### Soundness
3

### Presentation
4

### Contribution
3
