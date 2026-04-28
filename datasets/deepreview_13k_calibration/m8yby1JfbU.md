# Is Your Video Language Model a Reliable Judge?

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Evaluating video language models (VLMs) is crucial for improving their understanding of video content. 
Existing evaluation methods depend on single models, 
which may be unreliable or biased due to the models' incapability to understand content or inherent bias, 
ultimately compromising the reliability of evaluation. 
A straightforward remedy is to apply the principle of collective thoughts, 
aggregating reviews from multiple VLMs to enhance reliability. 
This study investigates the efficacy of such approaches in VLM evaluation, 
particularly when the pool of judges includes both reliable and unreliable models. 
Our findings reveal that incorporating collective judgments from such a mixed pool
does not necessarily enhance the accuracy of the final evaluation outcomes, 
because the less reliable judges could introduce noise that 
potentially leads to less reliable evaluations. 
To explore the factors that impact evaluation reliability, 
we fine-tune an underperforming VLM judge, Video-LLaVA, and observe that 
good understanding ability alone is insufficient
to make VLM judges reliable. 
These findings stress the limitations of collective thought approaches in VLM evaluation and 
highlight the need for more advanced methods that can account for the reliability of individual models. 
Our study promotes the development of more reliable evaluation methods for VLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores an important question in the evaluation of Video Language Models (VLMs): the impact of collective intelligence approaches on evaluation accuracy, especially when combining reliable and less reliable VLMs. This is a relevant topic given the growing reliance on VLMs in various applications where understanding complex video content is essential.

### Strengths
Novelty of Approach: The manuscript presents a unique perspective by applying collective intelligence principles to VLM evaluation, attempting to leverage multiple models to mitigate biases present in individual models. This approach is innovative and relevant, as it challenges existing evaluation methodologies that typically rely on single-model assessments.
Analysis of Collective Judgment: The authors' findings regarding the drawbacks of combining reliable and unreliable models are noteworthy. These results caution against blind aggregation in evaluation, highlighting the risk of introducing noise and bias, which can degrade the final evaluation’s reliability.

### Weaknesses
While the paper addresses an important topic, the methodology could be more detailed. Readers may benefit from a clearer explanation of how model reliability was determined and how judgments were aggregated. More specifics on the metrics and statistical techniques used would also strengthen the study’s transparency.

### Questions
Great work！I have no further questions

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
4

### Summary
This work aims to explore the effectiveness in the evaluation of Video Language Model (VLM), especially focus on collective thinking methods.  Traditional evaluation methods usually rely on a single model, which is susceptible to biases in training data and structure and limiting reliability. This work proposes to take different advanced VLMs and LLMs as judges to evaluate video question-answer pairs. An "evaluation-judgment" framework was implemented, where judges gave scores based on accuracy and relevance on a 1 to 5 scale. The advanced model GPT4o was used to integrate the preliminary review results of VLMs to generate the final evaluation. A mixed judge strategy was used to select the most reliable VLMs to contribute to the final evaluation of each visual dimension based on the weighted Cohen's Kappa score.

### Strengths
1. This work is well-written and easy to follow. 
2. The experimental results list the performance comparison of different models in various visual dimensions, including social context, emotional context, object instance count, etc. The scores of models such as GPT4o, GPT3.5, Agent Debate, etc. are compared to show their performance in each visual dimension. The performance scores of some models such as Llama-vid, GPT4o-mini, Internvl2, etc. are shown in table form.

### Weaknesses
1. There are so many new benchmarks for evaluate the VLM recently, and what is best benchmark for evaluating VLM.
2. This work proposed a new method for evaluating VLM, but this area need an evaluation benchmark(system) rather than just a new method.
3. Overall, even though this work proposes a good method and explore new insight, I think the contribution of this work is not enough for evaluating VLMs.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper investigates whether Video LLMs (VLMs) can reliably evaluate other VLMs' performance, and explores if using multiple VLMs collectively as judges improves evaluation reliability. 

Four different judging methods are studied in the paper:

**Review by LLM Agents Debate (Reference-guided grading)**: providing text LLMs with the reference answer and the generated answer and scoring it   
**Review by individual VLM:** A single Video LLM reviews the results from the test model  
**Review with Collective Thoughts:** A strong meta-judge Video LLM is provided with scores generated by individual Video LLM judges.  
**Mixture of Judges:** A score is generated by weighing the scores predicted by individual Video LLMs on the basis of their performance on the specific question type

The CVRR-ES dataset containing 2,400 question-answer pairs from 217 videos, distributed across 11 different visual dimensions (e.g., multiple actions, social context, emotional context) is used for the evaluation. Weighted Cohen's Kappa is used to measure agreement between different evaluation methods.

The key finding is that current Video LLMs (except GPT4o) are not reliable enough to be used as standalone evaluators. GPT-4o, when used as a sole judge, outperformed its performance when combined with less reliable judges.

### Strengths
As many recent works have utilized LLMs and VLMs are judges to evaluate other models, a work exploring the effectiveness of these judges is an interesting topic and of significant potential utility to the community.

### Weaknesses
 - The paper is poorly structured and written, the different methods studied are not clearly separated and are mixed up in different sections  
- The conclusions are based on a single not commonly used dataset, and are unusually strong, its possible that methods like mixture of judges not performing well on this setting is a result of this dataset, and not an universal fact.  
- The overall presentation of the data is poor, the paper is full of radar charts with 11 dimensions, however there’s often no real difference in the dimensions   
- The quality of the plots is often poor, lacking visual clarity, making it hard to understand the data. I suggest the authors generate the figures in some kind of vector graphics format like pdf instead of generating jpeg images.

### Questions
I believe this paper is not quite ready for submission and requires quite a bit more work.

1. Having results on more than one dataset would probably be the single biggest potential improvement. 
2. Re-organizing and rewriting methods section of the paper would be a necessity

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper argues that current VLMs, except for GPT-4o, are generally unreliable as judges for video understanding tasks. The study reveals that collective thoughts, which combine judgments from both reliable and unreliable VLMs, do not necessarily improve evaluation accuracy. Even a proposed mixture of judges offers only minor improvements, underscoring the need for more sophisticated methods to account for individual model reliability.

### Strengths
- The paper provides detailed experimental results, including both quantitative tables and visual comparisons, which effectively illustrate the trends.
- It is written clearly and easy to follow, making the results seem reproducible.
- The analysis highlights the limitations of relying on collective thought when using unreliable VLMs, contributing to the broader discussion on VLM evaluation.

### Weaknesses
 - The paper contains several typographical errors, particularly in how different VLM names are written (e.g., inconsistencies with capitalization and dashes).
- The conclusion that VLMs, other than GPT-4o, are unreliable as judges isn't entirely convincing. It would be helpful to provide more insights or potential solutions to address this issue or offer some speculative methods to improve VLMs as judges.
- The use of "hallucination" as a primary explanation for unreliable performance could be expanded with alternative explanations or further justification.
- This paper concludes that VLMs are not yet mature enough to serve as reliable judges for video understanding tasks. However, it lacks a thorough explanation or well-supported evidence to substantiate this claim. The observations and insights presented could be expanded to provide a clearer understanding of why VLMs fall short and what specific factors contribute to their unreliability.

### Questions
- Have you considered how the advanced judge processes the original video input and the VLM reviews? Is the final review a consolidation of the VLM assessments or a mixture with the advanced judge’s review as well?
- Could the selection of reliable judges in real-time (inference-time) be achieved without using pre-computed weighted scores (rely on LLM agent debate results, which require reference responses)? It might be useful to explore methods that remove outliers more efficiently and enable VLMs to work independently as judges.
- Could the tendency of VLMs to give high scores be a result of their misunderstanding of the content, rather than an inherent bias towards favorable evaluations?
- Is it possible that the use of Weighted Cohen's Kappa as a metric for selecting reliable judges is not optimal, leading to minimal performance improvements?
- The choice of using the Weighted Cohen's Kappa metric and the specific implementation of collective thought for VLMs as judges are not fully justified. A clearer rationale for the implementation would strengthen the validity of the approach.

### Soundness
3

### Presentation
3

### Contribution
2
