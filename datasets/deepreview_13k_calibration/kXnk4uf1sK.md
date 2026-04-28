# We are confident in trusting Language Models for annotating online sexism in political discourse, but are they good?

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Large Language Models (LLMs) have recently gained popularity for text analysis within the social sciences due to their versatility and context-aware capabilities. The use of prompt-based learning of LLMs has especially increased its application in classification tasks and text annotation of sensitive topics like sexism. While studies have used them for capturing online sexism, not much has been known of their capabilities across lesser-known discourses like that of political discourse, and how the models distinguish between partisan bias to gender bias. In this research, our main contributions could be listed as: i) comparing different LLMs through prompt engineering in their capability of detecting sexism in political discourse; and ii) proposing a new algorithm for capturing the confidence of the LLM predictions in classification tasks. Experimental results demonstrate a clear indication of trigger events that provoke online sexism, and yet no clear advantage of using LLMs while predicting sexism. Surprisingly, the results do not improve with more instructive prompts, but our algorithm proves to be effective in capturing the confidence of each model on their predicted labels.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work  investigates performance of multiple LLMs in the task of detecting sexism in political discourse and proposes a new algorithm for capturing the confidence of the LLM predictions in classification tasks.

### Strengths
-	The paper targets an important task. 
-	The paper is clearly written.
-	Extensive experiments were conducted.

### Weaknesses
 - There are plenty of papers on detecting misogyny, sexism, etc using LLMs in text. I don’t see political discourse offering specific challenges that requires examining this task in this type of content specifically. Further motivation to this aspect of the work is needed.
- Line 105: I don’t really see prompt engineering as the reason behind generating good annotations with LLMs, prompt engineering is a tool used to create prompts that can be used to interact with LLMs. The LLMs themselves are the reason/major player in the eventual performance observed in classification for a given task. This confusion continues with line 113, as majority of existing studies focused on investigating the performance of LLMs themselves and not the prompts for NLP tasks.
- The dataset has some issues that might effect the outcomes of the work.
	- Data annotation process is somewhat unclear. For example, starting line 174, the two labels/concepts mentioned are described as if they are mutually exclusive, while the work was introduced as detecting sexist language in political discourse. I assume there are many cases where the text is political and sexist. Other missing details are the number of annotators, their gender (as I believe in such task, gender of annotator can bring its own biases to the process), how many annotations were collected per tweet?, etc 
	- The data is really small and targets very few politicians under very specific and small number of trigger events, this of course significantly reduces the studies generalizability for the problem. 
	- Nothing about the quality of the annotations is mentioned. This is key to establish trust in the study built on top of such data.

### Questions
-	Line 163: how was this keywords list created? I suggest also sharing/releasing it with the paper. 
-	The paper builds a new dataset for the task/up to my knowledge, there are several existing datasets, why not use them?
-	Due to how unbalanced the data is, I suggest not reporting Accuracy. This will also help save space and increase table 3’s font size. Also, prompt category names should be the same as those listed under 3.2.1.
-	In Sec 4, I suggest the core observations/outcomes of each experiment to be better highlighted int ext.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an evaluation of various LLMs in detecting sexism within political discourse, proposing a new algorithm to measure prediction confidence. The authors discuss the limitations of current LLMs in detecting subtle, context-specific sexism through prompt engineering, suggesting that prompt specificity may not enhance model accuracy (as anticipated).

### Strengths
-	This paper is centered around a very interesting topic which is highly relevant given the current online landscape.
-	The corpus will be a useful resource for further research on the subject.
-	Clearly scoped tasks and objectives.

### Weaknesses
The paper is generally well written, however there are a few points that must be addressed:

- A section describing existing corpora (annotated for sexism) is missing. The authors should include a brief overview of the existing datasets, including their annotation scheme.

- I believe that since the company was bought, what had previously been free access to Twitter’s API, has been removed. Was the data collected before the cutoff date (~March 2023)?

- At the beginning of Section 3.1.3 the authors state that *’the data was annotated by a group of experts who work on gender studies in political science’*. Until the limitations section, the reader is left to wonder about the IAA and how the final labels were assigned -- these aspects should be mentioned earlier (i.e., in the same section). It would have been good to have even a small sample of the dataset labelled by all the annotators. Does the error analysis reveal any correlations between ‘misclassified’ instances and the person who labelled them?

- On line 201, the authors mention four trigger events, but only three are presented in Table 1.  Considering that on line 907, three trigger points are mentioned, I assume this is the correct number?

- Llama 3 was used for the emotion extraction task – how comes the authors did not include this model too in their analysis?


### Questions
Please see the above.

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
3

### Summary
The paper investigates how efficient are LLMs in predicting sexism in online discourse. The experiments are conducted on a twitter dataset conducted as part of the study which includes tweets from 22 with location as UK. They use 5 different LLMs and 4 different prompt types to evaluate the sexism prediction on the dataset. In addition, the also introduce a metric for predicting confidence of the models in their predictions using an uncertainty estimation.

### Strengths
- The paper uses an extremely imbalanced dataset to predict sexism in online political discourse.However, this is similar to real-world scenario where majority of the texts are non-sexist, making the research question quite interesting. 
- In addition to model comparison, they also perform error analysis to understand the reason of mis-classifications.
- They provide a relatively straight forward method to measure confidence of the models in their predictions.

### Weaknesses
Confidence metric:
- A temperature of 0 is used during the confidence estimation. This is practical if you want to evaluate the model on a deterministic response. However, in a practical setting, we do not use low/zero temperature as the models would constraint models diversity. It would be have been more intuitive to see the variation in the metric across different temperatures or at least on the temperature setting shows some level of randomness. The choice of temperature 0, while ensuring deterministic outputs, limits the exploration of the model's uncertainty, which is crucial for real-world applications where models need to handle diverse and nuanced inputs. A more comprehensive analysis would involve evaluating the confidence metric across a range of temperatures to understand how the model's certainty changes with increased randomness in the output.
- The number of iteration used is 3, which is probably sufficient given that at temperature 0, the variance in the generated output will be very less. But small variations in the seed values might influence the model predictions. So, I am not entirely sure if the number of iterations would be sufficient for statistically robust confidence. While the authors mention that they used different seed values, the impact of seed variation on the confidence metric needs to be thoroughly investigated. The current approach of using only three iterations, even with different seeds, might not be sufficient to capture the full range of variability in the model's predictions, especially when dealing with complex and nuanced tasks like sexism detection. A more robust approach would involve a larger number of iterations and a statistical analysis of the variance in the confidence scores.

Clarity in writing:
- While the paper explores interesting research questions like confidence estimation of LLMs, lack of clarity in writing style seriously affects the readability of the paper. I would suggest not using passive voice in sentences and rewriting the content for better clarity should be done before acceptance.

### Questions
- Line 201 says "**four** incidents of 2022 were chosen.. " and line 206-207 says  We attributed the **three** different trigger events to two trigger types", was this a mistake ? Or are the **incidents** different from **events**?
- In table 2, there are 2 tables, one showing "Political trigger event" and the other "Sexist trigger event". I am assuming that the total size of the dataset is the sum of the two and you reported the model performance on the combined version of the dataset. Is my assumption right? In any case, this explanation could benefit from a bit more clarity in writing.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper brings a focus on the task of detecting sexism specifically from political discourse. It includes an assessment of existing LLMs through prompt engineering when it comes to this task and then propose a new algorithm for capturing the confidence of the LLM
predictions in classification tasks. Their methodology illustrates trigger events in text that provoke sexism. Nonetheless they also claim that it provides no clear advantage when predicting sexism.

### Strengths
The model covers a thorough analysis of sexism detection on political discourse online using state of the art Large Language Models. For such a niche task, prompt engineering seems to be the right approach but they also put a detailed analysis into the robustness of the prompts they use as well as the calculation of a confidence score based on the outputs yielded by LLMs.

### Weaknesses
While this work addresses an important issue in language i.e. sexism detection and also provides a thorough picture of state-of-the-art LLMs when it comes to solving it, the overall novelty of this paper is low. It does not provide any specific understanding of what drives sexism within political narratives and or solutions of how models can be trained to capture such semantic cues in text. The analysis lacks a deeper investigation into the nuances of political discourse that might make sexism detection different from general text. The paper does not explore the specific characteristics of political language, such as the use of rhetoric, framing, and coded language, which could be crucial in understanding how sexism manifests in this context. Furthermore, the study does not delve into the potential impact of political context, such as the political leaning of the speaker or the target audience, on the interpretation of potentially sexist statements.

### Questions
The central thesis of this paper is understanding and detecting sexism in political discourse, yet it fails to specifically highlight what about political discourse require special investigation than regular text for sexism detection.

### Soundness
3

### Presentation
3

### Contribution
3
