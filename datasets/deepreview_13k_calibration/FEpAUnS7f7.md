# Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents

- Decision: Accept
- Avg Score: 4.80
- Scores: 6, 5, 5, 3, 5

## Abstract
This paper presents a novel application of large language models (LLMs) to enhance user comprehension of privacy policies through an interactive dialogue agent. We demonstrate that LLMs significantly outperform traditional models in tasks like Data Practice Identification, Choice Identification, Policy Summarization, and Privacy Question Answering, setting new benchmarks in privacy policy analysis. Building on these findings, we introduce an innovative LLM-based agent that functions as an expert system for processing website privacy policies, guiding users through complex legal language without requiring them to pose specific questions. A user study with 100 participants showed that users assisted by the agent had higher comprehension levels (mean score of 2.6 out of 3 vs. 1.8 in the control group), reduced cognitive load (task difficulty ratings of 3.2 out of 10 vs. 7.8), increased confidence in managing privacy, and completed tasks in less time (5.5 minutes vs. 15.8 minutes). This work highlights the potential of LLM-based agents to transform user interaction with privacy policies, leading to more informed consent and empowering users in the digital services landscape.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors assess the performance of OpenAI's GPT suite of LLMs on a set of text classification tasks using an existing privacy policy dataset. They compare the models' performance to baseline, non-LLM models from the dataset's creators. Additionally, they develop an LLM-powered agent to assist with reading and interpreting privacy policies, measuring its effect on comprehension and cognitive effort in a population of 100 users.

### Strengths
Originality: moderate. As the authors themselves note, there is substantial prior work on the problems with user comprehension of privacy policies and terms, and this paper is largely a straightforward application of a new model to an existing task. However, the agent the authors developed to assist users is a novel contribution, especially providing the ability to automatically surface opt-out mechanisms for users.

Quality: moderate. It might not be earth-shattering, but the execution nonetheless seems thorough.

Clarity: high. The presentation of the experiments and analyses performed is very clear.

Significance: moderate. The effects of the agent on user comprehension are notable, though practical impact feels limited given that it still takes nearly 6 minutes to read a privacy policy.

### Weaknesses
The authors state that "GPT-4o-mini, under zero-shot learning conditions without additional context, outperformed the baseline model on average" on the Data Practice Identification task. However, the model suffered from consistently poor recall, which the authors do not meaningfully address.

Statistical tests in section 6 not corrected for multiple comparisons.

As noted above, given that it takes nearly 6 minutes to read a privacy policy even with assistance, I feel skeptical that this approach would make a meaningful difference in the number of users that actually read privacy policies. Coupled with the models' poor recall and tendency to hallucinate, it seems likely that users would still miss the most important information in the privacy policy or even be presented with false information. It might be informative to conduct time-limited trials, where user comprehension is measured after e.g. a 30 second time limit. Another idea might be to measure the time it takes the user to be able to achieve an 80% score on a comprehension test (allowing multiple attempts).

The assessment of user comprehension is extremely coarse (three questions). A more fine-grained assessment might provide interesting insights for where further improvements (either to the agent or the UX) are most needed.

### Questions
Why was the user comprehension assessment only three questions? Do you think such a short assessment meaningfully measures user comprehension? How were the three questions chosen?

Did you track instances of hallucination in experimental group user sessions? How frequent and severe were they? How correlated was user trust with the accuracy of the information provided by the agent?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In the paper, the authors address a very specific issue of understanding the privacy policies of the users of various websites in a comprehensive manner from different aspects by LLM agents. It was built with an aim to help the general users of the websites about the privacy concerns and the policies of the personal or other data they share. The performance of the build LLM agent was evaluated on 100 people where half of them studied the policies by themselves and the rest used the LLM agent. The empirical results infer the users who used the LLM agent they got a better understanding of the websites user policies than the manually readers.

### Strengths
1.	The entire paper is well-written and presented the ideas in very clear way. 
2.	The authors explored a very specific and less explored use case of LLM agents in recent times.
3.	The empirical analysis is comprehensive and make sense of the idea the authors proposed.
4.	Multiple open-sourced and close-sourced LLMs were used and compared their performance. 
5.	The built agents archive comparable performance like benchmarks and sometimes outperforms the baselines.

### Weaknesses
1.	As a whole, this paper is more like a building a new tool for the various website users, than a theoretical or technical presentations of ideas and experimental analysis. However, before making it available for the public usage, it needs several things to be considered, e.g., misinformation, hallucination, privacy leakage of company policies. 
2.	It doesn’t include any novel technical or theoretical contributions in terms of the finding the research gaps of LLMs agents to be utilized for specific use cases. 
3.	Usually, LLMs agents for particular task are more likely to hallucinates its users. The risks of LLMs hallucinations were not explored in this paper in details. The built LLM agents might not work well under such vulnerabilities. At least a few results with analysis should have been discussed. Apart from this, LLM agents might face several potential security and privacy issues as described in https://arxiv.org/pdf/2407.19354; this paper does not explore or discuss such vulnerabilities. 
4.	Building the agent only on one privacy policy dataset (though it is large) may not be sufficient to use the LLMs agent in practice.

### Questions
1.	What are the traditional models in page 2?
2.	There is a missing citation in page 3, CNNs for text classification(?)
3.	Figure 1 was never described.
4.	In page 6, what is the process of ensuring valid and relevant outputs? 
5.	Why different metrics were used to evaluate different tasks? The explanation along with a short description of the metrics will benefit the clarity. Same comment for t-test.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study presents a competent investigation into the use of GPT family models for privacy policy comprehension support. However, it may not fully align with ICLR’s intended contribution areas, as it reads more like a system-oriented paper that might be more suited for an HCI venue.

The authors first assess the performance of GPT models, both in zero-shot and few-shot settings, and compare these results against traditional approaches. They conclude that GPT models exhibit reasonable performance levels in this context. Following this evaluation, the study introduces an LLM-driven agent designed to assist users in understanding privacy policies and completing related tasks. Through questionnaires, the study demonstrates that the agent helps reduce cognitive load and enhances both comprehension and user confidence.

While this research is well-executed, I question whether its contributions are significant enough to justify a full paper. The study does not introduce new models or corpora, nor does it directly address gaps in current models related to privacy management, although limitations are acknowledged.

Moreover, it is unclear how the proposed system substantially differs from other reading comprehension and summarization systems. A deeper comparison in this area could provide useful context for assessing the novelty of the approach.

Specific Comments:

Tables 1–3: The rationale for not including fine-tuned models is not sufficiently explained. Fine-tuning could potentially yield stronger baselines or comparative insights in this setting.

### Strengths
The paper is clearly written and easy to follow.

### Weaknesses
While this research is well-executed, I question whether its contributions are significant enough to justify a full paper. The study does not introduce new models or corpora, nor does it directly address gaps in current models related to privacy management, although limitations are acknowledged.

Moreover, it is unclear how the proposed system substantially differs from other reading comprehension and summarization systems. A deeper comparison in this area could provide useful context for assessing the novelty of the approach.

Specific Comments:

Tables 1–3: The rationale for not including fine-tuned models is not sufficiently explained. Fine-tuning could potentially yield stronger baselines or comparative insights in this setting.

### Questions
Tables 1–3: The rationale for not including fine-tuned models is not sufficiently explained. Fine-tuning could potentially yield stronger baselines or comparative insights in this setting.

### Soundness
3

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
5

### Summary
This paper applies the  large language models (LLMs) to enhance user comprehension of privacy policies through an interactive dialogue agent.  The authors first demonstrate that LLMs significantly outperform traditional models in tasks like Data Practice Identification, Choice Identification, Policy Summarization, and Privacy Question Answering. Building on these findings, they then introduce an LLM-based agent that functions as an expert system for processing website privacy policies, guiding users through complex legal language without requiring them to pose specific questions. A user study with 100 participants showed that users assisted by the agent had higher comprehension levels, reduced cognitive load, increased confidence in managing privacy, and completed tasks in less time .

### Strengths
1. Applying the LLM in the digital privacy management is an interesting topic.

### Weaknesses
1. The main technical contribution of this paper appears limited given its current scope and the expectations of ICLR. It may be better suited for HCI venues such as CHI or IUI, which align more closely with the type of work presented.

2. The current study appears to lack IRB approval, and details of the user study are insufficiently reported. Key information such as where did you recruit participants and what is the compensation for participants are missing. Without this information, it is challenging to ensure that the study’s conclusions are reasonable and generalizable to other populations.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors construct an LLM-based tool for assisting users in interpreting and summarizing privacy policies. They evaluate the tool using several benchmarks for privacy policy comprehension/summarization from prior work. In a study of 100 users, they find that users report greater comprehension and greater ease of interpretation when assisted by the LLM tool.

### Strengths
**Originality**

- Includes a systematic user study of ML-assisted privacy policy interpretation — appears to be novel relative to related work, which relies mostly on benchmark datasets (though I am not familiar with this literature).
- Constructs a system for applying state-of-the-artx LLM models to help users interpret privacy policy interpretation — including a broad range of features (interactive QA, classification, summarization) not unified in prior work.

**Quality**

- Appears to analyze the results of a user study competently and with appropriate statistics and measures of error, though some methodological details are missing.
- Appears to correctly apply benchmarks from prior work to evaluate LLM agent performance.
- From the details provided, the LLM tool seems to be well constructed and appropriate for the task.

**Clarity**

- Well written, and for the most part easy to follow.
- Does an excellent job making clear the goals & contributions of the research.

**Significance**

- Provides a technological solution to a clear privacy & transparency issue for internet users.
- Seems to present a clear, significant finding that an LLM agent could help lay users more easily interpret complex privacy policies——this could be a potentially useful workaround, barring systematic improvements to transparency requirements.

### Weaknesses
 **Originality**

**[Minor]** The idea to use ML tools to assist users in interpreting privacy policies is not new—in this sense the contribution of this study is marginal. Still, there is certainly value in evaluating this idea using the most recent large language models, and there is certainly value in conducting a study with actual users to see whether the tool really makes interpretation easier. I am not sure whether there are many user studies in prior work on this idea — perhaps the authors could clarify whether this is the first user study of its kind and, if not, whether it tells us anything new.

**Quality**

Missing methodological details make it hard to tell whether the empirical findings support the broad claims in the abstract and introduction, and I have lingering questions about some of the results.

- **[Minor]** Section 3: Need a clear description of all the benchmark tasks to understand exactly what’s being evaluated — Section 3 seems to assume the tasks have already been defined. Examples:
    - Section 3.1: What does it really mean to identify “User Choice/Control” or “Data Retention”, e.g., as a practice? Does this simply mean the privacy policy describes their user choice allowances or data retention practices, which could range from quite benign to quite egregious? How is this useful to a user?
    - Section 3.2: What is the Choice Identification task? Is this the task described in A.1.3? Was this task defined in Wilson et al. (2016) too?
    - Section 3.3: What’s “Privacy Question Answering”? (Or is it “Policy Question Answering”? Both terms are used.)
    - Section 3.4: What’s in this dataset, as compared to the dataset used in the previous tasks? Who defined the “risky” sentences (what were the human-generated references for the ROUGE score)? Any examples?
    - Section 4 provides a bit more detail, and the examples in the Appendix are somewhat helpful. Perhaps this Section could come before Section 3; or alternatively, move parts of Section 3 to the appendix, and just summarize the most important findings (GPT models perform better on X benchmarks) in a paragraph, using that space instead to better explain the tasks at hand.
- **[Major]** Section 4: These results are striking — users seem to comprehend the privacy policies much more easily with LLM assistance! But there are some key methodological details missing that could determine how rigorous the results are:
    - Did the Experimental Group also have a copy of the privacy policy that they could read directly during the task (not through QA), or did they rely solely on information from the LLM agent? From the Appendix, I infer they did have access to the raw text — do the gains decrease/increase if the user cannot cross-check the LLM agent responses with the raw legal text?
    - Section 6.1: Where/how were users recruited? How many privacy policies did each participant review? How were the privacy policies selected — from one of the previous datasets? Did every participant review the same privacy policy? (How likely is it that these policies appeared in the training data — i.e. leakage?) Where/how was questionnaire administered? This information is key for determining how internally and externally valid these results might be.
    - Was the study IRB approved?
    - L393: What about racial, economic diversity in the sample? How well might these results generalize to other groups, especially marginalized groups?
    - I’m surprised by the finding that the Experimental Group had *higher* trust in info scores than the control group — and I wonder if there’s an issue with construct validity for this question. The relevant question is (L978): “I believe the information I read/received is accurate (1-5).” Given that the control group had direct access to the privacy policies, why would they respond with a 2.6, on average, compared to 4.5 in the experimental group, since the underlying information (the privacy policy) is the same for both groups? My best guess is that the Control Group suspected the company was misrepresenting its privacy practices in its privacy policy, and answered based on their distrust in the company; I suspect the Experimental Group, on the other hand, responded based on their level of trust in the accuracy of the LLM agent’s responses. So the scores may not be directly comparable. The alternative is that using the LLM agent somehow increased people’s confidence in the accuracy of the privacy policy itself, which seems less likely but still possible.
- **[Major]** Generally, it’s not clear how well the benchmarks measure the “correctness” of the agent’s responses — what is the ground truth for each of these tasks? The comprehension questions seem good, but they’re short, and not very granular — whereas the examples in the Appendix show LLM responses with much, much more detailed information about data practices. As the authors point out in the discussion, LLMs often produce incorrect and misleading text, especially when prompted for specific details that are less likely to be represented in training data. Can the authors say anything about the factuality of those more specific responses? How likely are those responses to contain falsehoods about the privacy policy that could mislead users? Can users easily identify false responses by cross-checking with the raw text or the QA feature?

**Clarity**

Generally the paper is easy to follow, with the exception of the omitted methodological details listed above. Some **minor** points of clarity that would be worth addressing: 

- L132: Have ML techniques actually improved privacy policy accessibility in practice? Or is this just a summary of research, not practice?
- L130: What is the OPP-115 dataset? Readers may not know.
- L131: Broken cite here.
- L136: What’s the difference between an LLM and an LLM agent? Is there a definition the authors can give? What makes this application an LLM agent, rather than just an LLM (the fact that the program scrapes hyperlinks, maybe)?
- Fig. 2: Text is too small to read, and often cropped, so it’s not clear what the different elements are. Simple labels might be better.
- Table 1-2: Suggest combining numbers side-by-side, so it’s easy to compare.
- Table 2, L192: SVM F1-score has a misplaced decimal.

**Significance**

- **[Minor]** This is a neat idea, and it seems like it could certainly help users in particular cases. But to frame the significance more precisely, it would be helpful to comment on the scope of a technological solution like this (e.g. in the discussion) — there is a structural issue here with privacy regulations, and with GDPR in particular, that require companies to disclose information about their privacy policies but do not require companies to make that information, and users’ options with respect to their data, truly accessible. In a perfect world, this tool may not be necessary — companies could be required to produce interpretable “privacy labels” similar to Apple’s Privacy Nutrition labels. How does the performance of this LLM-based solution compare to other policy alternatives? (These questions probably cannot be answered in this study, but it is worth mentioning that a technological solution is not necessarily the best solution.)
- **[Major]** Section 3: On a similar note, can the authors report any non-ML baselines here? How does a person do on this task, on their own? It seems less important to know how GPT models compare to BERT or other ML models, and more important to know how this method compares to what users would otherwise be doing in practice. (Unless those traditional models are actually being used by lay users in practice — that would be worth mentioning.)
    - L094: “We provide empirical evidence of the superiority of LLMs over traditional models”:  I’m assuming these sentence refers specifically to *ML* models (would be worth clarifying).  But is this approach superior to the practical alternatives available to users/policymakers? Superior to things like Apple’s “Privacy Nutrition” labels? Superior to writing a simpler privacy policy? Superior to hiring a lawyer? It would help to be more precise with this and similar claims of LLM “superiority”—superior to what?
    - Section 3: It seems like the GPT models perform better than traditional ML models, but stepping back, are these scores good enough to be relied on? For example, the recall scores seem really low here — as far as I can tell, the GPT models miss as many as 30% of instances of third party sharing, and as many as 84% of instances of “data retention”? Can this tool be used to balance precision and recall? Is this the right balance for this kind of task? Recall might well be more important to users in this kind of task.

### Questions
Did the authors explore different kinds of privacy policies in the user study — for example, are the gains from using the LLM tool greater when the privacy policy is longer / more complex?

### Soundness
2

### Presentation
3

### Contribution
2
