# MAD-Sherlock: Multi-Agent Debates for Out-of-Context Misinformation Detection

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
One of the most challenging forms of misinformation involves the out-of-context (OOC) use of images paired with misleading text, creating false narratives. Existing AI-driven detection systems lack explainability and require expensive finetuning. We address these issues with MAD-Sherlock: a \textbf{M}ulti-\textbf{A}gent \textbf{D}ebate system for OOC Misinformation Detection. MAD-Sherlock introduces a novel multi-agent debate framework where multimodal agents collaborate to assess contextual consistency and request external information to enhance cross-context reasoning and decision-making. Our framework enables explainable detection with state-of-the-art accuracy even without domain-specific fine-tuning. Extensive ablation studies confirm that external retrieval significantly improves detection accuracy, and user studies demonstrate that MAD-Sherlock boosts performance for both experts and non-experts. These results position MAD-Sherlock as a powerful tool for autonomous and citizen intelligence applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper describes a method to detect a particular kind of misinformation, where text is paired with an image misleadingly out of context, using debating LLMs. The LLMs are equipped with a reverse image web search retrieval system. The paper shows this system performs well compared to many baselines and alternatives from the literature, as well as in a user study assessing how much the explanations the LLMs generate help humans.

### Strengths
Important problem and the general approach of retrieval-augmented LLMs, with something to improve their reasoning (here, debate), makes a lot of sense.

Comparison with many alternative methods from literature.

Good experiments on different debate setups, both as an ablation here and potentially informative for methods in other domains too.

### Weaknesses
A baseline with the LLM and retrieval system used but without debate - similar to actor-skeptic but without the skeptic - seems missing. I feel like this is important to understand how much debate is actually helping, since it isn't guaranteed that it would perform worse than e.g. some less effective forms of debate that might confuse things more, or compared to other methods from the literature which might be using models weaker than GPT-4o.  

Cost and time efficiency are not reported. This also connects to the previous point, and seems a key consideration when comparing multiple LLMs engaging in multi-turn debates, which could be significantly more costly than e.g. a single LLM setup. A high cost could be an important limitation, and regardless, important information for readers considering if they could apply the work. It would be useful to see a comparison of the cost and time efficiency of this method with other strong baselines, such as Sniffer and GPT-4o#.

Although - aside from the baseline point mentioned above - the comparisons with existing methods are extensive, they are all performed on a single dataset. The margin compared to the next-best performing approach (Sniffer with fine-tuning) is only about 1.7%, and there are no error bars reported. So, it's not very clear how definitive the performance conclusions are. While the dataset used is a standard one for this task, this does not eliminate the possibility of dataset-specific biases or spurious correlations that could favor the proposed approach. This makes it difficult to assess the generalizability of the results.

Overall, the combination of the three preceding two points forms my main concern: the framework looks promising, but some information is missing for a reader to make a full, confident assessment. Below I note two minor issues I had with the writing:

Discussion of Lin et al (line 167): it's clear the current work is quite different. It's less clear to me, though, why this work is highlighted in general, given that it is so different, including entirely different domain. Maybe this could be contextualized a bit more broadly in terms of approaches to classification by debating LLMs, or some other connecting insight or argument beyond "here's another work that used debating LLMs".

Section 3.1: I was a bit unclear when first reading this on what is background information on possible ways a debate could be structured, vs. what you actually test yourselves. Maybe the wording could be a bit more explicit that you test all of these.

### Questions
Why summarize using Llama 13B as opposed to a more recent Llama? It seems like Llama 3 8b is both smaller and has significantly better performance?

The user study asks participants to not search the web themselves. I can see that being applicable for laypeople, who might not want to spend time checking stuff or know what should be checked. I'm less sure for journalists, are there cases where they too wouldn't be using web search?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
MAD-Sherlock, a Multi-Agent Debate system for detecting out-of-context (OOC) misinformation, addresses issues of existing AI detection systems. It introduces a novel framework where multimodal agents collaborate to assess context consistency and request external info. Enables explainable detection with high accuracy without domain-specific fine-tuning. The experimental results confirm external retrieval improves accuracy, and user studies show it boosts performance for both experts and non-experts, making it a powerful tool for intelligence applications.

### Strengths
* The paper presents a meaningful problem in multimodal fake content detection: OOC (Out-of-Context).
* The method proposed in the paper is very interesting and achieved state-of-the-art (SOTA) results, validating its effectiveness.
* The paper is written in great detail.

### Weaknesses
 * The paper primarily addresses the Out-of-Context (OOC) issue of fake online content. However, it does not provide a detailed explanation or analysis of why the debate approach was introduced and how it effectively addresses the OOC problem.

* The introduction of external information retrieval can lead to label leakage issues.

* The selection of baselines in the paper is not enough; it should include some multimodal fake online content detection methods[1,2] as baselines for comparison. For example, models like GPT-4o were not designed specifically for fake online content detection, so the comparison methods in the paper lack convincing power.

* This paper lacks sufficient ablation experiments to demonstrate the effectiveness of each component of MAD-Sherlock and its contribution to the overall performance.

* In the section 4.3.1,

>We also observe a significant performance increase when the agent believes it is conversing with a human instead of another AI agent

the paper lacks an explanation and analysis to clarify why this phenomenon occurs.

### Questions
1. Why introduce the debate framework to address the OOC problem? It would be helpful if the authors could clarify the insight behind this choice.

2. For the different debate strategies, how do they vary in addressing the OOC problem? Apart from the results shown in Table 1, is there additional analysis or explanation provided here?

3. How can it be ensured that the introduction of external information retrieval will not lead to label leakage issues?

Additionally, it would be helpful if the authors could address the issues mentioned in the "weaknesses" section.

### Soundness
2

### Presentation
2

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
MAD-Sherlock is a multi-agent debate system designed to detect out-of-context misinformation by analyzing inconsistencies between images and accompanying text. Unlike traditional AI models, it enables multiple multimodal agents to independently assess and debate the context of information, using external retrieval to enhance accuracy and provide clear, explainable insights.

### Strengths
1. The MAD-Sherlock framework introduces a multi-agent debate approach to detect out-of-context misinformation, combining asynchronous debates with external information retrieval to enhance the model's contextual understanding and interpretability. This approach shows significant innovation compared to single-agent methods.
2. The model provides human-readable explanations during the decision-making process, which is a major improvement over current AI-driven misinformation detection systems.
3. This work attempts to leverage internet searches to extract external information and use it to enhance the performance of misinformation detection and proves its effectiveness.
5. Interesting findings:
    1. The comparison of various debate methods reveals that asynchronous debate is the most effective, providing valuable insights for designing multi-agent debate frameworks.
    2. There is a significant performance improvement when models believe they are debating against a human rather than another AI agent.
    3. The method also allows agents the freedom to change their opinions mid-debate. In such settings, agents demonstrate an enhanced ability to critically evaluate arguments and identify subtle inconsistencies.

### Weaknesses
1: Lack of data cleaning for external information

Apart from what was mentioned in Appendix A.1:

> First, while our model excels at detecting out-of-context image-text pairs, its reliance on external retrieval can lead to reduced accuracy when relevant context is unavailable or difficult to retrieve.

(1) The paper seems to lack verification of the authenticity and quality of the extracted external information. Without thorough data cleaning, if low-quality data or even fake news is retrieved, it could negatively impact the judgment results.

(2) During the pre-training process, commercial LLMs use carefully cleaned data. If a conflict arises between the parameter knowledge of the LLM itself and the external knowledge, how should it be resolved? This is not uncommon; when an event occurs, it is often accompanied by numerous rumors, even conflicting ones. Blindly trusting the external knowledge retrieved online could lead to undesirable outcomes.

(3) Only the Bing Visual Search API was used for information retrieval. Is it proven to be reliable and effective enough?

2: Reliability and effectiveness of LLM summarization, and potential side effects

In Section 3.3.2, you mentioned using LLMs, such as Llama-13B, to summarize information, focusing only on the most important parts of the text. I am curious about how it determines the most important parts and whether it might miss important details. Could the performance of Llama-13B itself become a bottleneck in the workflow?

Information summarized and rewritten by the LLM inevitably alters the original language pattern, and when such processed information is provided to the agents, could it make the already potentially unreliable external information even harder to detect?

3: Limited dataset

Only the NewsCLIPpings dataset was used, which may lack representativeness. This dataset is from 2021, a time when LLMs were not as prevalent as they are now, and AIGC content was limited. I question whether it is representative of the current and future online news landscape and the ability of this work to detect LLM-generated misinformation.

4: Questionable fairness of the user study

As mentioned in Appendix A.4.1, in the user study, participants were not allowed to access the internet and could not retrieve external information (e.g., Bing Visual Search API) like MAD-Sherlock. They could only rely on their own experience and common ensense, which is unfair. At the very least, a control group should be added, allowing participants to access the same external information as MAD-Sherlock.

### Questions
see above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents MAD-Sherlock, a multi-agent debate system designed for out-of-context misinformation detection. MAD-Sherlock leverages a multi-agent framework where each agent independently analyzes image-text pairs and engages in multiple rounds of debate to assess contextual consistency. The system incorporates external information retrieval to enhance the agents' reasoning capabilities, achieving high detection accuracy and explainability without the need for task-specific fine-tuning. A unique aspect of MAD-Sherlock is its systematic construction and comparison of various multi-agent debate strategies, offering a comprehensive exploration of debate structures within a multi-agent framework for OOC detection.

### Strengths
1. This paper applies external information retrieval and multi-agent collaboration to the task of out-of-context misinformation detection, which is a relatively novel approach. The authors effectively combine these elements in this context, and the experimental results demonstrate the effectiveness of this method.

2. Unlike previous work, MAD-Sherlock specifically constructs and compares different multi-agent debate strategies, providing a systematic analysis of various debate methods in out-of-context detection. This exploration is quite interesting, and it also offers valuable insights for applying multi-agent frameworks in similar tasks.

3. The authors built a complete pipeline that combines image and text processing, including external data collection and cleaning, which is a substantial effort. Handling multimodal data and integrating external information adds complexity to the system.

### Weaknesses
1. Multi-agent collaboration and debate strategies are popular methods for improving results, and incorporating external information is also common in multi-agent setups like AutoGPT. The experiments here don’t include comparisons with these popular frameworks, especially those that also use external data and agent collaboration. Adding such comparisons would highlight where MAD-Sherlock stands out.

2. While external retrieval improves the system’s accuracy, it could backfire if relevant information isn’t available or if the search results are inconsistent or irrelevant. The paper doesn’t delve much into this issue; it would be helpful to discuss how the system performs in cases where external information is incomplete or unavailable to gauge robustness.

3. The multi-agent debate structure adds a lot of computational cost, which isn’t fully detailed in the paper. It would be useful to see ablation studies comparing debate length and performance to understand the trade-offs in runtime and accuracy. This would make it easier to evaluate MAD-Sherlock’s feasibility for practical applications.

### Questions
Why did you only compare with pretrained multimodal baseline methods? Is it because this approach is more commonly used for this task? Additionally, why didn’t you include comparisons with systems that use multi-agent collaboration with external information retrieval?

### Soundness
3

### Presentation
3

### Contribution
3
