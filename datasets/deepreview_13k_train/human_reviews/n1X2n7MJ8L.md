# CulturalBench: a Robust, Diverse and Challenging Benchmark on Measuring (the Lack of) Cultural Knowledge of LLMs

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
To make large language models (LLMs) more helpful across diverse cultures, it is essential to have effective cultural knowledge benchmarks to measure and track our progress. Effective benchmarks need to be robust, diverse, and challenging. We introduce \benchmark: a set of 1,227 human-written and human-verified questions for effectively assessing LLMs' cultural knowledge, covering 45 global regions including the underrepresented ones like Bangladesh, Zimbabwe, and Peru. Questions - each verified by five independent annotators - span 17 diverse topics ranging from food preferences to greeting etiquettes. We evaluate models on two setups: \benchmark-Easy and \benchmark-Hard which share the same questions but asked differently. We find that LLMs are sensitive to such difference in setups (e.g., GPT-4o with 27.3\% difference). Compared to human performance (92.6\% accuracy), \benchmark-Hard is more \textit{challenging} for frontier LLMs with the best performing model (GPT-4o) at only 61.5\% and the worst (Llama3-8b) at 21.4\%. Moreover, we find that LLMs often struggle with tricky questions that have multiple correct answers (e.g., What utensils do the Chinese usually use?), revealing a tendency to converge to a single answer. Our results also indicate that OpenAI GPT-4o substantially outperform other proprietary and open source models in questions related to all but one region (Oceania). Nonetheless, all models consistently underperform on questions related to South America and the Middle East.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This study proposes 1,227 human-written and human-verified questions to asses cultural knowledge of LLMs covering 45 global regions, and 17 diverse topics. Each question is verified by five independent annotators.

### Strengths
- Coverage of 45 regions associated with different culture
- Evaluated using 30 current LLMs. 
- Details experimental results with different analysis

### Weaknesses
 - Number of questions are relatively low compare to any other recent datasets. While it covers more countries, but number of questions per country is low (Appendix B, Table 2). For example, how do you justify the performance by just asking 7 questions (e.g., Canada)? This performance evaluation can have both effects, either it is underestimating of overestimating the performance. As a rule of thumb, a sample size of at least 30 is considered the minimum for statistical analysis due to the Central Limit Theorem.
- L161: "but did not verify the final questions by humans" --> Is this necessary when question is already written by human? Do you mean verifying by other annotators. 
- L203: "These non-human written benchmarks" --> this is a contradictory statement. This study also used LLMs in the process, which makes the authors' criticism of prior work for doing the same seems contradictory. In addition, this study criticizes prior work "Over-reliance on Web Sources -- scraped web sources may be used during models pretraining". This whole question formulation process is based on LLMs knowledge, which is inherently knowledge from web sources. 
- L206-208: Low performance does not necessary mean challenging. 
- L329: GPT-4o-mini is used for the classification of questions into topics. It could be have done manually. This categorization is subjective in nature and requires a guideline to follow. For example, one can argue that "how to greet people" is a daily life activity. One of the major claims/contributions is the breadth of topic coverage, which has been addressed inadequately. 
- I did not find any prompt in Appendix C. 
- What was the reason to limit to "most 3-7 questions"? Is there any reference that culture can be defined by 5-7 questions? 
- L333-336: The discussion seems arbitrary. Annotators ask question based on their knowledge. If number of annotators are less, meaning we are limiting the background knowledge, also limiting the diversity of the questions. 
- This study is highlighting "discovery approach" very much. It is important to justify why it is beneficial. 
- While it is an study about cultural knowledge, therefore, one would expect that dataset will be in native language, however, this study is focused on English. 

- By looking at the resource, it seems that question is generic, can be applicable to different countries by replacing country. See first example here. For the second example, answer varies location to location within the culture.  

23,23,"In Bangladesh, which festival celebration style is most likely appropriate for expressing the collective cultural identity?",Hosting a potluck where each individual brings a dish from their own ethnic background.,Celebrating only the most widely recognized national holiday.,Selecting one culture each year to highlight and exclusively celebrate its festivals.,Ignoring all cultural festivals to maintain neutrality.,B,Bangladesh

94,94,"In Bangladesh, what is a customary action before stepping into someone's home?",Light incense at the entrance,Remove your shoes,Offer to cook a meal,Clap your hands twice,B,Bangladesh

### Questions
- What does it mean to be "less represented", as per as online digital content representation languages are typically categorized as low, medium and high resource languages.
- What is the purpose of CULTURALBENCH-Hard? 
- L171: How many topics initially discovered by the annotators? As it was open-ended, one can assume that number of topics could be even more than 17 topics
- Which model is used for brainstorming? 
- "culturally relevant scenarios" --> Was it completely open? Were there any instructions like what it means to be culturally relevant scenarios? Example in Figure 10 is not clear. As an annotator how should one start with it?  
- Answers often come in different forms such short or long for the same question. Did you observe any such? How did you manage that? It may come from multiple annotators. What values (e.g., temperature) did you choose on the LLM while generating question and answer? Was it same for all annotators. 
- L348: For the evaluation, did the model always generated correct answer? It is possible that it produced extra tokens. How did you deal with that? 
- L376: How did you compute human performance - 92.4%?

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
This paper introduces CULTURALBENCH, a new benchmark for evaluating large language models' (LLMs) cultural knowledge across 45 global regions, including underrepresented areas like Bangladesh, Zimbabwe, and Peru. The benchmark consists of 1,227 human-written, human-verified questions spanning 17 cultural topics, such as food preferences and greeting etiquette. The authors propose two evaluation setups: CULTURALBENCH-Easy and CULTURALBENCH-Hard, which feature the same questions phrased differently to assess the models' robustness to variations in question formulation.

The paper introduces a comprehensive, diverse benchmark to assess LLMs’ cultural understanding across regions that are often neglected in existing datasets. By using two different question setups, the authors highlight that LLMs' performance is sensitive to how questions are framed, with differences as high as 27.3% observed in GPT-4o. The authors compare LLMs, including GPT-4o and Llama3-8b, against human performance. While human annotators achieve 92.6% accuracy, the best LLM (GPT-4o) reaches only 61.5% accuracy on the more challenging setup, revealing significant gaps in cultural knowledge. The paper identifies specific shortcomings in LLMs, particularly in regions like South America and the Middle East, as well as difficulties in handling questions with multiple valid answers.

### Strengths
The authors collect a culture-related question-answering dataset by using a pipeline consisting of three steps: 1) Red-teaming data collection; 2) Human Quality Chek 3) Filtering. The proposed datset is verified by five annotators. There are several merits of this dataset:

1. The dataset is divided into CulturalBench-easy and CulturalBench-hard, which are more differentiable than current culture-related datasets, covering more diverse topics and more challenging questions.

2. The model's performance on CULTURALBENCH-Hard is far behind human performance, where GPT-4o achieves the best performance.

3. The authors propose some interesting analysis on different providers' LLMs on questions from different regions. For example, they find that models perform better in questions relating to North America, South Asia, and West/South Europe than South America, East Europe, and the Middle East. Meanwhile, Qwen-2-72B and Mistral Large do not perform well in answering their own region's cultural knowledge.

### Weaknesses
My major concern with this work is the form of the multiple choice question. As many researchers agree and argue before, LLMs usually show unstable and unpredictable performance when are required to answer multiple choice questions. Why not design some generation tasks to evaluate LLM's capability towards culture-related questions?

While culture-related question-answering problem is not novel at the moment given the previous similar work, including CultureLLM, CultureBank, and SeaLLM. I am wondering whether the authors could propose more diverse data types, not limited to the multiple-choice format. How do your multiple-choice formats compare to or improve upon the formats used in these works?

In addition, the experimental results are not counterintuitive enough. For instance, GPT-4o leads in most regions, Models score lower in questions relating to South America, East Europe, and the Middle East, etc. More in-depth analyses are expected to be done.

### Questions
1. Have you considered other question formats beyond the multiple choice question answering?

2. Have you considered evaluating the self-knowledge of LLMs when answering culture-related questions. As shown in Line 511 to Line 513, the authors provide two extra options: “I don’t have knowledge” and “This question is unanswerable” – to enable annotators to indicate when they cannot provide a response. However, we have not observed the comparison between LLMs and humans in terms of the self-knowledge.

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
4

### Summary
The authors have created a cultural knowledge benchmark, CulturalBench, through AI assisted interactive red-teaming.
The major contribution I would consider to be relevant to HCI aspects, of how they setup and conducted the benchmark curation using human annotators and with AI assistance.

I believe such work fits better in HCI focused conferences.

Some other recent work (such as CultureBank) leveraged social networks (reddit, twitter etc.) to curate similar datasets and benchmarks. One can argue that collecting such data indirectly provides wider representation, especially in multicultural regions, which the authors of this paper briefly mention but dont go into much details. I.e., when thinking about culture knowledge of a country/region that is largely multi-cultural, which aspects play a large role or how those multiple identities (county of origin, ethnicity, religion, current place of residence) interplay to define what is the 'culture' of this region?

### Strengths
Devised an effective AI assisted framework for engaging human annotators in curation of cultural knowledge benchmarks.
The paper is well written and the AI assisted framework holds promise to increase annotators involvement/engagement.

### Weaknesses
The main focus of this paper is in describing the human annotators setup with AI assisted implementation.

It lacks some of the comparison with other cultural knowledge benchmarks (such as CultureBank) that were generated using other approaches and as such, lacks the discussion of how this approach is better and what are the limitations comparing to others.

As alluded by the authors, no fine-grained (and I would add, no consideration for multiplicity of identities) cultural classification -- which is mentioned to be a limitation of the annotation platform used -- that may have non-neglected impact on the resulted benchmark.

### Questions
What was the approach taken to represent accurately multi-cultural countries? If the annotators were from specific country but not part of a specific culture (being it ethnical, religious or other), was that taken into consideration?

How about other multiplicity of identities which may have an impact on how one perceives ones culture?

Would be good to include detailed description of annotator selection criteria, particularly for multicultural countries. 
I would suggest to include discussion on how the authors accounted for within-country cultural diversity in their data collection and validation process, including how they addressed the interplay of multiple identities (e.g., country of origin, ethnicity, religion, current place of residence) in defining the 'culture' of a region.

Can you include a detailed comparison between your approach and methods like CultureBank that use social media data? Discussing potential advantages and limitations of each approach for capturing cultural diversity, especially in multicultural regions

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
4

### Summary
The paper describes work on developing a high-quality benchmark called CulturalBench for measuring cultural knowledge of LLMs. The benchmark contains a total of 1,227 high-quality and human-verified English prompts covering culture-based questions from 45 global regions and split into two versions of the benchmark: CulturalBench-Easy and CulturalBench-Hard. The paper introduces CulturalTeaming which is the process of constructing high-quality generation questions from cultures and validation based on majority voting. The paper highlights differences of CulturalBench from existing culture-evaluating benchmarks including quality checks for all 1,227 questions, discovery-based topics, and higher topic coverage. One particularly finding that stood out for me is that model providers' flagship models were not able to obtain higher performance in cultural knowledge relating to their region.

### Strengths
The paper is well-written and easy to read. I particularly appreciate the level of completeness of the paper and how it packages its contributions in terms of benchmarking cultural knowledge of LLMs. I find the CulturalTeaming process used to ensure quality of questions crafted by humans towards specific cultural practices as part of the benchmark to be one of the paper's strengths. The author/s highlight this difference compared to existing benchmarks where instances are not verified iteratively and strongly through majority voting. In terms of results, the paper has interesting findings such as learning that model providers from specific regions (ex. Qwen from Asia/China) seem not to meet the expectation that it will emerge as the best performing model for East Asian culture assessment.

### Weaknesses
Some of the issues I find from the paper are as follows:

1.  **Small test instance count which has certain disadvantages.** 1,227 test instances may be a good initial overview of performance but not enough to tell something about an LLM’s true/reliable understanding of geographic-specific culture (ex. South Europe or Oceania) as it only contains 20-100 test instances (even less if you revert it back to its original question-type form). The quality control in developing the benchmark is an advantage (and I think this should be a common practice that other benchmarks can replicate) but I’m concerned about the practical usability of said benchmark as the trend in evaluating culture understanding is more favorable towards depth on a specific global region than a catch-all/one-size-fits-all evaluation. The limited number of instances, particularly when broken down by sub-regions, raises concerns about the statistical power of the benchmark to draw meaningful conclusions about an LLM's cultural understanding in those specific areas. For example, a region with only 20-30 questions may not be sufficient to capture the nuances of its culture, and performance differences could be due to random chance rather than genuine understanding.

2.  **Selective results using commercial models.** The authors did perform in-depth analysis of the question type and versions of models in Section 5.2 but only for commercial models. This does not make sense to me as there is very little to know about these models due to their closed nature. It would make the paper stronger if the same analysis is done on more transparent/open-weight models used like Llama, Qwen and even models not included in the experiments but are made with culture in mind such as Aya models by Cohere. The lack of analysis on open-weight models limits the generalizability of the findings and makes it difficult to compare the performance of these models on the benchmark. This is a missed opportunity to provide a more comprehensive analysis of the cultural understanding of various LLMs.

3.  **Lack of discussion on how to grow and develop the benchmark.** For culture knowledge benchmarks like this one, it might strengthen the paper if the authors provide sufficient and convincing discussion on how the community or any plans to grow and develop the benchmark, given its small number of test instances. This can be in the form of improving the framework in Figure 1. Without this, the benchmark will only cover a snapshot of cultures of different geographical areas which, again, makes its real-life usage questionable. The absence of a clear plan for future development and expansion of the benchmark is a significant drawback. A static benchmark with a limited number of instances will quickly become outdated and may not be representative of the evolving cultural landscape.

4.  **Wrong accusation on poor diversity of previous benchmarks**. I oppose the author/s statement to label topic-specific benchmarks focusing specifically on food, social etiquette, etc as "narrow" and of  "poor diversity" in the related work section. As a reader, the tone of the paragraph comes as negative. While these benchmarks cover more specific aspects of culture, they have their own application as to why it is important to benchmark LLMs on different specific cultural aspects like food. They are considered semantic proxies of culture by a survey paper (Adilazuarda et al., 2024), which is a good starting point for understanding how LLMs capture cultures. This is not a negative connotation per se. Moreover, I would argue that it is better to have a benchmark that prioritizes depth on a specific aspect of culture but provides solid, empirical insights on that direction than a benchmark that tries to "catch-all" cultures but obtains very limited unrepresentative findings from small test instances.

### Questions
How is a binary question format classified as hard when there are more chances of a model picking either one correct from the two choices? I believe I’m missing something because this is not clearly explained in the paper. If a benchmark is hard/challenging, the first thing that comes to me is something similar to MMLU-Pro (https://arxiv.org/abs/2406.01574) where there are greater than 5 (max 10) choices.

See other questions raised in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes CulturalBench, an AI-assisted red-teaming collected dataset. The dataset aims to help improve the cultural understanding ability of LLMs, which is so meaningful. Besides, the datasets is collected by local people, covering lots of areas and topics. The experiments in the paper also improve the effectiveness of the dataset.

### Strengths
1. The paper proposes a pipeline for collect cultural data leveraging AI-assisted red-teaming.

2. The human collecting process is professional and considerable.

### Weaknesses
1. I am confusing about the experiment in the last part of sec.5.1. You supposed that models perform better on the easy version because models can guess the answer of some questions without seeing the questions. Your experiment is to compute the semantic similarity of the cultural name with each answer. I think it may only prove the cultural relativity of each pair. A better exploration may be to control the variables. For example, disturb the choices of each question to change their cultural relativity, and see the new results. For example, you could conduct this additional experiment of randomizing answer choices and re-evaluating model performance, to more conclusively demonstrate whether models are relying on cultural relativity heuristics.

2. Can CulturalBench helps to enhance models' cultural understanding? More experiments on prompting or fine-tuning may be more interesting. For example, you can fine-tune models using your data and conduct in-context learning and other prompt engineerings.

### Questions
1. According to sec.3.2, how to define the correct answers for a question with multiple answers considering cultural diversity?

### Soundness
3

### Presentation
3

### Contribution
3
