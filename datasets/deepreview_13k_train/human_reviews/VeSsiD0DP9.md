# The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Recent advancements in large multimodal models (LMMs) have significantly enhanced performance across diverse tasks, with ongoing efforts to further integrate additional modalities such as video and audio.
However, most existing LMMs remain vulnerable to hallucinations, the discrepancy between the factual multimodal input and the generated textual output, which has limited their applicability in various real-world scenarios. 
This paper presents the first systematic investigation of hallucinations in LMMs involving the three most common modalities: language, visual, and audio. 
Our study reveals two key contributors to hallucinations: overreliance on unimodal priors and spurious inter-modality correlations. 
To address these challenges, we introduce the benchmark \textit{The Curse of Multi-Modalities} (\textbf{CMM}), which comprehensively evaluates hallucinations in LMMs, providing a detailed analysis of their underlying issues. Our findings highlight key vulnerabilities, including imbalances in modality integration and biases from training data, underscoring the need for balanced cross-modal learning and enhanced hallucination mitigation strategies. 
Based on our observations and findings, we suggest potential research directions that could enhance the reliability of LMMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the phenomenon of hallucinations in multimodal large language models (MLLMs), establishing benchmarks and dataset, while also suggesting future research directions. Overall, the paper is well-written and clearly presented.

### Strengths
Hallucination is an important research topic in LLMs. This study expands previous research on hallucinations from purely linguistic tasks to multi-modal tasks, categorizing the causes into two aspects: excessive reliance on unimodal priors and false inter-modal correlations.

### Weaknesses
However, I still have some concerns regarding this work:

1.	My primary focus is on the benchmark dataset. Multimodal data may encounter issues of modality mutual exclusion. For example, audio may express one content while video expresses another content. Thus, when we combine multimodal information, it may be difficult to obtain a singular ground truth, which may impact the reliability of this work.

2. In this paper, the model takes all available modalities as inputs. However, if the prompts focus solely on auditory clues, can we directly input audio into the model to simply address the hallucination issue? For example, in Figure 1(b), since the prompt focuses on auditory cues, can we resolve the hallucination issue by only inputting audio data? Therefore, I wonder if there is a simpler approach to tackle the hallucination problem, which would also avoid the first issue of modality mutual exclusion.

### Questions
Please refer to my comments on weaknesses.

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
3

### Summary
This work provides a new way to understand and analyze hallucinations in multimodal models. Hallucinations are categorized into two main types with three subtypes under each main type. 
A new benchmark is introduced base on this framework, providing 200 samples for each minor category. The benchmark is tested over several existing models, demonstrating the ability to distinguish the performance of these models. This might aid future researchers to analyze the hallucination in their own model.

### Strengths
This work provides an interesting attempt to categorize hallucinations in multimodal models by their causes. Most of the previous related work take hallucination as a single phenomenon and conducts unified assessments of them. This provides great help to researchers to locate problems in their model or in their training process, highlighting the value of this work as a benchmark. This is also a good try to encourage further discussion on hallucination in multimodal models.

### Weaknesses
1. Further experiment needed to support the categorization. The entire work is based on the assumption of a significant part of hallucinations in multimodal models is made up by the categories discussed in this work. Though there is experiment to prove that these categories exists and can explain some of the hallucinations, no statistical numbers is provided in this work to show how significant and identical they are.
2. Lack of Statistical numbers. This work doesn’t provide length distribution of its samples, neither a full distribution of the subjects/events presented in its sample.
3. 1200 sample/2400 questions is a big enough size for a test set, however 600 samples/1200 questions seems much smaller. Some models, like visual only or audio only models, can only use half of the dataset, making this work less helpful than it seems for some researchers.

### Questions
1. How can we categorize a hallucination? Not with your dataset, but with random input/response pair? Categorization in this work is a “principal content” one, reasons for different category is not independent. For example, the “hammer hitting” case provided in the work, is it a visual dominance hallucination as you categorize it, or it is actually a false visual-language correlation like “Chekhov's Gun”?
2. Human exists in every top 10 frequent subject pairs for visual cases. Any balancing methods are taken? Does it damage the soundness of your work?

### Soundness
2

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
The paper presents a novel benchmark to evaluate multimodal hallucinations including audio-visual scenarios. Authors show with an example that hallucinations can occur from over-reliance on unimodal priors and spurious inter-modal correlations. They construct an evaluation dataset and define metrics to quantify hallucinations in vision-language, audio-language and audio-video-language paradigms. The paper presents experiments on various LMMs, including proprietary and open-source models, providing insights into their performance and limitations. The paper further posits that balanced multi-modal training, advanced cross-modal fusion techniques and using diverse prompts can mitigate these issues.

### Strengths
The paper focuses on the task of multi-modal hallucination and the main novelty lies in including tasks that take both video and audio modality into account. The paper is well motivated. The experiments in section 2 showcase how LMMs are sometimes overtly rely on one modality to answer questions. Fig 3 also validates that spurious inter-modal correlation can occur based on co-occurrence of entities and events in training data. The paper is easy to read and follow.

### Weaknesses
1. The paper does not propose any mitigation strategies to counter the hallucinations. e.g. it would be interesting to see the effect on metrics by simply prompting and instructing the model to pay attention to audio and video rather than just asking the question directly.

2. We see from the results that there is a trend that when models does better on perception accuracy (pa) they do worse on Hallucination resistance (hr) and vice-versa which suggests LMMs have tendency to choose yes over no (or vice-versa). How do we make sure the metrics simply aren’t simply capturing the yes/no answering tendency of LMMs rather than the two deficiencies proposed in paper (i.e. Spurious Inter-modality Correlation and Uni-modality Over-reliance)?

3. It is not clear how these findings relate to real world applications. Especially the task in language dominance where authors use anti common-sense videos which feel more like tricking LLM than testing its hallucination rate in real world scenarios.

4. The paper focuses primarily on LMMs that process visual and audio events but they do not consider measuring hallucinations in speech settings. This limits the scope of the paper to some extent.

### Questions
1. How can this framework be extended to detect partial hallucinations? e.g. detecting hallucination in a chain of thought reasoning which may contain correct information as well.

2. An interesting extension may be to incorporate questions about temporal aspects of events. e.g. asking questions like “did the person drink water before eating food?“. Have authors done any investigations with respect to that?

3. From Table 2, it seems some models are already doing well on some tasks achieving > 75% and sometime 90% score for both pa and hr metrics. With the rapid rise in LLMs, how do authors plan to update their dataset to remain challenging?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a benchmark dataset designed to evaluate hallucinations in Large Multimodal Models (LLMs), encompassing language, visual, and audio modalities. The authors investigate potential contributors to these hallucinations, including an overreliance on unimodal priors and spurious inter-modality correlations. Based on these findings, the benchmark presents two categories of evaluation, each containing 600 samples, amounting to a total of 1200 samples and 2400 probing questions. The analysis conducted using this benchmark reveals that imbalances in modality integration and biases in the training data are the primary causes of hallucinations in LMMs.

### Strengths
- The paper is clearly written and effectively presented.
- The motivation behind this work, exploring hallucinations in LMMs across various modal combinations such as audio-language, vision-language, and audio-vision-language, is an interesting direction.
- The introduction of an audio-visual benchmark for evaluating hallucinations in LMMs is a contribution to the field of LMMs.

### Weaknesses
 **The experimental setup used to highlight the first contributor to hallucinations, overreliance on unimodal priors, is less reliable.**
- In Figure 1, the authors present only a single example per modality dominance. The reviewer is curious whether this phenomenon can be generally claimed across a broader range of examples. Could the authors provide the results about the modality dominance on larger set?
- Similarly, in Figure 2, there is a question about which models (FAVOR, GPT-4, Gemini, etc.) were used for the experiments and whether this phenomenon is observable across different models. It would be valuable to clarify if this phenomenon is more pronounced in certain models than others, which underscores the need to clearly identify which models were used for these experiments.
- To substantiate the important claims that motivate this work, the experiments should be conducted more thoroughly, both qualitatively and quantitatively, across more diverse scenarios.

**The description of the benchmark in the main text is unclear.**
- The distribution of the dataset and the categories it covers are not well-defined. It is crucial to detail the statistics (e.g., number of samples per category, distribution of modalities, or breakdown of object vs event-level queries) of the categories covered by the benchmark to encourage future research aimed at advancing this field.
- In Section 3.2.2, the authors do not describe how they identified the global appearance patterns and co-occurrence patterns in the source dataset used to construct the benchmark. As spurious inter-modality correlations are a major contributor to hallucinations, the process of identifying such biases should be more transparently explained.
- The limitations of the dataset, such as its scale and distribution, are not adequately discussed. These information, such as potential biases in the data collection process, challenges in scaling the dataset, or how representative the dataset is of real-world multimodal scenarios, should be included. 
- Table 3 conducts separate evaluations for event-level and object-level hallucinations, yet the statistics supporting this distinction are not clearly presented. This raises questions about the clear differentiation between these categories.

**Further Experimental Recommendations.**
- Additional baseline models should be considered for evaluation, especially for visual-audio-language models (e.g., Video-Salmon, PandaGPT, OneLLM) or audio-language models (e.g., LTU).
- While the models generally perform well on the benchmarks, discrepancies in performance, particularly with visual-language LMMs, raise questions about whether the benchmark is too simplistic or whether it can effectively reflect consistent tendencies of hallucinations across all models.
- Incorporating models of various sizes (e.g.,https://github.com/yxuansu/PandaGPT) could enrich the experiments detailed in Table 5.
- Visualizing attention maps to verify if the models disproportionately focus on one modality, leading to incorrect, hallucinated responses, would support the argument concerning overreliance on specific modalities.

### Questions
- Were the contributors to the hallucinations identified through the proposed benchmark CMM, or were they discerned from a smaller set that motivated the authors to explore further?
- In Figure 2, how did the authors measure the probability of the answer being "yes" or "no"? Given that the LMMs generate free-form text, how did the authors quantify the probability of responses in a binary classification context?
- Does the question template affect the results?
- What is the difference between the dataset used for probing spurious inter-modality correlations in Section 2.2 and the proposed dataset?
- Shouldn't Line 398 state that there is limited availability of audio-language data compared to the visual-audio-language dataset?

### Soundness
2

### Presentation
3

### Contribution
2
