# DialSim: A Real-Time Simulator for Evaluating Long-Term Multi-Party Dialogue Understanding of Conversational Agents

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 3, 6

## Abstract
Recent advancements in Large Language Models (LLMs) have significantly enhanced the capabilities of conversational agents, making them applicable to various fields (\textit{e.g.}, education). 
  Despite their progress, the evaluation of the agents often overlooks the complexities of real-world conversations, such as real-time interactions, multi-party dialogues, and extended contextual dependencies. To bridge this gap, we introduce \simname, a real-time dialogue simulator.
  In this simulator, an agent is assigned the role of a character from popular TV shows, requiring it to respond to spontaneous questions using past dialogue information and to distinguish between known and unknown information. 
  Key features of \simname include evaluating the agent’s ability to respond within a reasonable time limit, handling long-term multi-party dialogues, and testing the agent's performance under randomized questioning with a diverse and high-quality question-answer dataset. We utilized this simulator to evaluate the latest conversational agents and analyze their limitations. Our experiments highlight both the strengths and weaknesses of these agents, providing valuable insights for future improvements in the field of conversational AI. \simname is available at \href{https://dialsim.io/}{https://dialsim.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces DialSim, a simulator for dialogue based on popular TV series. It leverages fan quizz websites and ChatGPT in order to generate realistic dialogues and Q&As. The introduced dataset is larger than available alternatives and supports long-range dialog and multi-hop questions. Multiple LLMs are tested against this simulator, showing a direct comparison between mainstream open-weight models and available APIs.

### Strengths
# Originality

The domain covered by the paper has been covered by multiple works, however the scale of the proposed dataset is higher than available alternatives. The paper provides a good coverage of the existing literature and its coverage. The method proposed to generate long-range dialogues by leveraging a temporal knowledge graph is novel, and as a whole, the data pipeline leverages existing LLMs in an interesting way.


# Quality and clarity

The paper is well-written, it presents very clearly the various steps of the data creation process and the setup in which mainstream LLMs were tested.


# Significance

The significance of this paper is not clear to me. While extracting long-term dialogue data for benchmarking is broadly useful to NLP researchers, the fact that this data comes from extremely popular sources makes it very hard to claim actual scene understanding by the model. (see weaknesses section)

### Weaknesses
## Time limit scenario
The paper puts a time limit constraint on the responses under some hardware capacity constraints. However, it presents both open-weight LLMs and available APIs under the same light, although the hardware used by APIs is unknown, and is likely to be significantly more powerful than A6000 GPUs.

## Ablating the data preprocessing pipeline
The data creation involves creating prompting of LLMs in order to filter questions and apply personal style transfer. It also leverages a temporal knowledge graph in order to formulate complex, multi-hop questions. It would have made sense to justify this step and show how the current LLMs cannot efficiently solve this task.

## Data leakage is probably significant, making the paper's relevance questionable

Most importantly, this paper introduces a dataset based on highly popular sources. Any current LLM has likely been trained on fan quizzes, episode synopses or even full dialogue scripts for these TV shows. As such, it is impossible to attribute correct answering of the model to an actual understanding of the dialogue as opposed to correct memorization of its training set. The paper attempts to mitigate this by running an "adversarial test", however it is likely that training set memorization goes beyond the memorization of mainstream character names. For instance, any question about how a character bought their new boots in a TV-show-like setup will be irremediably tainted by the memorization of the first episode of Friends. As a consequence, it is not clear to me how relevant the overall approach can be, as it actually relies on the mainstream popularity of the content in order to properly source and curate data.

### Questions
# How should practitioners approach data leakage with this benchmark?

As mentioned in the weaknesses section, it seems likely that the popularity of the content makes for very high data leakage in training sets.   
Have you tested stronger "adversarial" testing methods than simply swapping character names? How can practitioners evaluate their dialogue agents in this framework while making sure that they're actually testing long-range dialogue understanding and not merely training set memorization?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces DialSim, a real-time dialogue simulator, and builds a dataset using this simulator, to evaluate the LLM's ability to play as the role of a character from popular TV shows, and correctly answer randomized questions related to the show w/ or wo/ history context, within a given time limit. 

The paper presents details about the dataset construction, and compares the datasets with several existing related works. The dataset features its large scale, multiple characters, long context that spans several years, relationships between characters that evolve over time, etc. 

The paper conducts extensive experiments on the datasets, with closed- and open-source SOTA models. Results are presented to explore (1) w/ and wo/ history context (2) different forms of history contexts (3) different retrieval methods (4) w/ and wo/ time limit. Then, the paper analyzes the results in detail and provides useful insights.

### Strengths
1. The paper presents a highly novel method to simulate a conversational dataset that can evaluate LLM's abilities from a very practical and real-world scenario consideration (time budget, complex conversation setting, long history, etc.)

2. The paper conducts lots of experiments to compare a list of SOTA models given different settings. The results show that current models cannot handle the task well, demonstrating the effectiveness of the task and dataset.

3. The paper organization and clarity are pretty good.

### Weaknesses
1. The paper does not clearly distinguish between (1) a simulator that helps to generate multi-choice QA / open QA given TV show scripts, and (2) a dataset built with the simulator. This causes some confusions. For example, I wonder:

1) For the evaluation, are the experiments on different datasets conducted on a same, fixed dataset? Does the evaluation incorporate any randomness?

2) If there is a fixed evaluation dataset, then what are its statistics? I noticed that Table 2 presents "Average Fan Quiz Questions per Session=56.7", is this the number of question candidates, or number of actual selected questions?

2. As the paper also points out, although it considers real-world scenarios like time budget and long history, the data source of TV show scripts may limit its application to real-world applications.

### Questions
As written in the Weaknesses section, I'd like to know if there is a fixed evaluation dataset for the evaluation. If so, please present more details about this dataset.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed DialSim, a real-time multi-party dialogue simulator. It is designed with a time limit, random QA, to fully evaluate the conversational LLM agents. Evaluation experiments are conducted on a wide range of baseline LLMs.

### Strengths
1. The authors make a great job to provide a high-quality and large-scale dialogue dataset from TV shows. The conversations in the data are multi-party, a promising and useful domain in the community.

2. The method used to construct the data is carefully-designed, to ensure the quality, e.g. using temporal knowledge graph, character style rephrasing.

### Weaknesses
1. In spite of the construction of the data, the work has minor contribution. While the evaluation spans a wide range of models, the conclusions are normal. I find the adversarial test in the paper interesting, where the model gets rid of the prior knowledge when answering the question, but the authors decide to put them in Appendix. There is space of one more page.

2. Since this work releases a high-quality dataset, it can be very helpful to demonstrate more concrete examples of the dialogues and conduct comparison to previous ones. However, there is no illustrative examples in the paper. It is hard for readers to justify the quality of the data as well as the effectiveness of the generating methods.

3. It is not clear how or to what extent, the mentioned data generation methods e.g. using knowledge graph, can facilitate the quality of the data. The paper lacks corresponding endeavors to illustrate this.

4. The work focuses on multi-party dialogue, a challenging task even for recent LLMs. However, it is a pity that the relevant discussion cannot be found in the related work or analysis of the paper.

5. The constructed DialSim is mainly characterized by its time limit and scale, i.e. some regular factors rather than some other promising factors. Therefore, the contribution of this paper is not positive considering the recent advance in the AI community.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces DialSim, a dialogue simulator for real-time evaluation of a conversational agent’s long-term multi-party dialogue understanding. It provides time-constrained evaluation with high-quality and extensive long-term dialogue.

### Strengths
1.The paper is well-motivated. It introduces real-time constraints in evaluating conversational agents, which is significant in real-world scenarios.

2.Although the task is synthetic, the process of test case generation is novel and reasonable. It also provides flexibility in both generating questions and generating test cases.

3.The experiments encompass RAG-based methods and analysis on errors, storing history and time limit, which are comprehensive and in depth.

### Weaknesses
1.Although DialSim simulates long-term dialogues averaging 350k tokens, the experiment shows that ChatGPT-4o-mini and Llama-3.1 still give correct answer frequently with 8k tokens context length, which means it does not require long context capabilities to solve this task.

2.Data contamination might be a problem. Since DialSim uses scripts from popular TV shows, conversational agents might know the answer of question based on their own knowledge rather than the dialogue.

3.Limited variety of task types and data sources. The paper only focuses on question-answering and TV shows scripts, which may restrict the scope of the benchmark in thoroughly evaluating capabilities of conversational agents.

### Questions
1.Could you provide an analysis on text length utilization and data contamination? I believe it is important to evaluate the quality of this benchmark.

2.I am curious about the performances of LLMs on unanswerable questions, since they demonstrate the extent to which LLMs understand the entire dialogue.

### Soundness
3

### Presentation
2

### Contribution
3
