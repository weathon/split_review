# Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 5, 5, 5

## Abstract
Recent works have showcased the ability of large-scale language models (LLMs) to embody diverse personas in their responses, exemplified by prompts like \textit{`You are Yoda. Explain the Theory of Relativity.'} While this ability allows personalization of LLMs and enables human behavior simulation, its effect on LLMs' capabilities remains unclear. To fill this gap, we present the first extensive study of the unintended side-effects of persona assignment on the ability of LLMs to perform \emph{basic reasoning} tasks. Our study covers 24 reasoning datasets (spanning mathematics, law, medicine, morals, and more), 4 LLMs (2 versions of \chatgpt{}, GPT-4-Turbo, and \llama{}-70b-chat), and 19 diverse personas (e.g., `an Asian person') spanning 5 socio-demographic groups: race, gender, religion, disability, and political affiliation.
Our experiments unveil that LLMs harbor deep rooted bias against various socio-demographics underneath a veneer of fairness. While they overtly reject stereotypes when explicitly asked (\textit{`Are Black people less skilled at mathematics?'}), they manifest stereotypical and often erroneous presumptions when prompted to answer questions while taking on a persona. These can be observed as abstentions in the model's response, e.g., \textit{`As a Black person, I am unable to answer this question as it requires math knowledge'}, and generally result in a substantial drop in performance on reasoning tasks. Our experiments with \chatgpt{} show that this bias is \textit{ubiquitous}---80\% of our personas demonstrate bias; it is \textit{significant}---certain datasets show relative drops in performance of 70\%+; and can be especially \textit{harmful for certain groups}---some personas suffer statistically significant drops on more than 80\% of the datasets. Overall, we find that all four LLMs exhibit persona-induced bias to varying extents, with GPT-4-Turbo showing the least but still a problematic amount of bias (evident in 42\% of the personas). Further analysis shows that these persona-induced errors can be hard-to-discern as they do not always manifest as explicit abstentions. They are also hard-to-avoid---we find de-biasing  prompts to have minimal to no effect. Our findings serve as a cautionary tale that the practice of assigning personas to LLMs---a trend on the rise---can surface their deep-rooted biases and have unforeseeable and detrimental side-effects.\footnote{\label{footnote:code}Code and model outputs will be made available at \href{https://allenai.io/persona-bias}{https://allenai.io/persona-bias}.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors study how specifying different personas (based on political ideology, religious beliefs, race, gender, etc) in the initial prompts for ChatGPT (gpt-3.5-turbo specifically) results in worse performance on a slew of reasoning task evaluations. It is noted the when specifically asked whether these personas would impact the ability to answer reasoning task questions the LLM responds that the type of persona will not matter. Unfortunately, as the authors discover, the bias is baked deep into the model, and that protections are merely superficial. The authors created a "human" and "average human" baseline persona to compare against.

The "physically disabled" persona does much worse on the evaluations reasoning tasks compared to the human persona. Of note, binary gender personas do not impact the reasoning capabilities.

### Strengths
The paper presents an interesting question and provides solid results. The paper is by-and-large well written. The paper provides enough detail such that the results can be reproduced and built upon. The paper does a good job citing the relevant literature,

### Weaknesses
From a writing standpoint, I wish the authors did not abbreviate "statistically significant", and given that they chose to do so they should be consistent with the abbreviation. The authors do not specify explicitly what the "human" and "average human" persona prompts are. I assume the term "human" was put in place of the {persona} holder showed in Table 1, but I wish that I hadn't needed to assume. I also wish they had provided results for these datasets when no persona was provided. I wish the authors had performed similar analysis on a different LLM; I am left unsure if this is an issue exclusively for gpt-3.5 or is it in all LLMs.

### Questions
- In section 5 the authors note "it relies on the task requiring a well-defined expertise that can be succinctly specified in the prompt".  Would it be possible in the prompt just to specify the LLM should as an "expert in the subject" or "domain expert". Why the need to explicitly state the LLM should adopt the persona of "chemist" or "lawyer".
- How does the LLM perform on these tasks when no persona is provided?
- In table 8 which of the persona prompts succeeded and which failed your test?
- Did you consider how intersectionality could alter the results (i.e. you are a Hispanic life-long Republican). Would be really interesting.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies how personas can affect reasoning capabilities of language models and biases that can arise as a result of this. Authors perform different empirical evaluations on various personas and datasets and showcase the existing disparities amongst different groups/personas. Authors also show that prompt based bias mitigation approaches have minimal effect in reducing biases studied in this work.

### Strengths
1. The paper is written clearly and is easy to follow.

2. The paper studies a timely and important issue.

3. Different datasets are studied in this work.

### Weaknesses
1. The experimental results are shallow and are not discussed in detail. The results only touch the surface area of what authors have observed. I would have loved to see more in depth discussion on what was the reason behind these observations.

2. Only a simple prompt base mitigation strategy was considered which was not that effective. It would have been good if authors have considered more sophisticated approaches to address this issue.

3. The studied personas were limited and authors did not consider intersectional biases.

4. Only gpt-3.5-turbo was used in this study. It would have been interesting to see how different models perform differently in terms of persona biases.

Overall, since the paper was mostly empirical, I would have loved to see more detailed studies and ablations with a larger pool of models and more in depth discussion on the findings and results to fully support the claims.

### Questions
I am still not 100% clear and convinced on why demographics, such as religious, should perform lower than each of the more fine-grained demographics, such as Atheist, Christian, and Jewish.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
LLMs can ascribe to a persona by being prompted to respond as a person with specific characteristics. This paper examines biases revealed by persona-assignment that may otherwise go undetected. The results show that being prompted to take on a particular persona reveals stereotypical responses compared to being prompted to comment on that persona directly. The paper mainly includes an experimental demonstration of this problem.

### Strengths
(1) The paper underlines a distinction between persona-assigned stereotype bias and more general word association bias. This is an important result in the discussion about bias in LLMs

(2) Section 4 of the analysis is quite interesting where the model abstains from responding for various reasons. Similarly Section 5 is interesting. Strengthening these two sections would be a possible path towards improvement.

### Weaknesses
(1) The related works section is underdeveloped. For instance, the work should be properly situated within the context of existing research on Algorithmic bias. But instead, the paper includes only minimal reference to "bias in models"

(2) The paper is not precise in its definition of bias. From the text, it seems like the paper is mainly interested in stereotypes found in word associations. Using 'bias' as a general all encompassing term weakens the overall point of the paper. It would be helpful to be more precise.

(3) Results overstated. The paper states "In summary, these results indicate that there is significant bias inherent in the LLM for nearly all personas, both at the group level (e.g., religion-based personas) as well as for individual personas." Figure 2 shows that for the "Race" categories, the accuracy ranges from ~60% to ~63% compared to ~65% for human persona. With the accuracy being so low across the board, this does not seem to be a "significant" bias. The two bars between man and woman are almost indistinguishable and also very close to human persona. The two groups with differences seem to be physically disable and religious where the accuracy is worse than a coin toss. The paper does not include discussion in the context of such low accuracy. This continues where throughout results section where the paper makes claims like "nearly all personas have large drops on some datasets" which is not a particularly well-supported or meaningful claim.

(4) Analysis is not statistically sound. For instance, Figure 3 "using a scatter plot with various personas on the x-axis. Each point now corresponds to a relative drop in accuracy on one dataset, compared to the Human baseline. The box represents the 25th -75th percentile...". The y-axis is "relative % change". The paper does not outline assumptions being made here about direct comparison between datasets. Further, the accuracy reported does not include error bars so how can you justify comparison in this way?

(5) Figure 8 switches from 'Accuracy' to error rate with no supported discussion. The plot is also scaled from 0.0 to 0.6 without explanation. The general discussion is overstated without appropriate experimental and analytical details to support.

### Questions
(1) This work could be viewed as simply a evidence against asking an LLM to take on a human persona. As in, it is not just that assigning personas can surface "deep-rooted biases" but possibly that the act of asking an LLM to take on a human persona is potentially flawed in some fundamental way. What do the authors mean by "deep-rooted biases" and "detrimental side-effects"? Can you be more specific in terms of the connecting the results in this paper to some larger take away?


(2) In table 2, the "Race" category contains race (caucasian), ethnicity (hispanic) and nationality (African). Can you explain this choice? Why "African" person instead of "African American" for instance? And given that you have the flexibility to do so, what is the reason for not including a non-binary gender option?

(3) Why is the y-axis in Figure 2 not standardized from 0.0 - 1.0 or 0.5 - 1.0? Is this test accuracy? If this is AUC, then the scale should be 0.5 - 1.0. Further, why is the best accuracy ~65% across the board? Might this limit the significance of the results?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper evaluates the effect of 16 different persona assignments on ChatGPT’s ability to perform basic reasoning tasks, which span 24 datasets. The authors find large drops in accuracy for certain personas (including physically disabled individuals and religious individuals). One of the main factors identified by the authors for this significant drop in performance was ChatGPT’s tendency to abstain from answering for those personas. The authors also tried a few prompt variants to de-bias the model.

### Strengths
Given the increasing number of works interested in using LLMs to simulate human behavior, this work studies an important facet of that application which is the potential bias that is introduced when prompting LLMs to exhibit certain personas. The authors also evaluated ChatGPT across a number of personas and reasoning tasks.

### Weaknesses
My primary concern is that this work only evaluates one model, i.e., ChatGPT, which makes it challenging to assess the generalizability of the findings regarding the bias of LLMs. For example, it seems intuitive based on anecdotal evidence that ChatGPT would be more likely to abstain from answering questions for certain personas, but that does not necessarily mean it should be penalized for that behavior. While the authors mentioned in a footnote that they also ran similar experiments on a Llama-2 model (could the authors clarify which model specifically?), it would be helpful to see the same evaluation conducted across a number of different LLMs.

A few comments about providing more experimental details and justification: (1) could the authors clarify how the “human” and “average human” baselines were implemented? (2) Could the authors explain why they chose to sample from ChatGPT with temperature 0? Relatedly, since it was mentioned that there was significant variation in the model’s performance across different runs, could the authors include error bars in the results analysis?

The approaches considered to de-bias LLMs seemed to be very handcrafted. Could the authors try a more systematic approach to exploring the prompt space or types of examples that could be provided to the LLMs to de-bias the model? It would be interesting to see de-biasing results across more LLMs.

### Questions
- Please clarify the questions raised in the weakness section above.
- It would be helpful for informing future work and for gaining a deeper understanding of the findings in this work to be able to understand *why* certain personas experience a larger performance drop. What are systematic approaches to getting at this question?
- I also wonder if these biases are more prevalent in objective questions (where there is a ground truth answer) as compared to subjective questions or tasks.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
