# MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Recent advancements in foundation models have enhanced AI systems' capabilities in autonomous tool usage and reasoning.
However, their ability in location or map-based reasoning - which improves daily life by optimizing navigation, facilitating resource discovery, and streamlining logistics - has not been systematically studied. To bridge this gap, we introduce MapEval, a benchmark designed to assess diverse and complex map-based user queries with geo-spatial reasoning. MapEval features three task types (textual, API-based, and visual) that require collecting world information via map tools, processing heterogeneous geo-spatial contexts (e.g., named entities, travel distances, user reviews or ratings, images), and compositional reasoning, which all state-of-the-art foundation models find challenging. Comprising 700 unique multiple-choice questions about locations across 180 cities and 54 countries, MapEval evaluates foundation models' ability to handle spatial relationships, map infographics, travel planning, and navigation challenges. Using MapEval, we conducted a comprehensive evaluation of 28 prominent foundation models. While no single model excelled across all tasks, Claude-3.5-Sonnet, GPT-4o, and Gemini-1.5-Pro achieved competitive performance overall. However, substantial performance gaps emerged, particularly in MapEval, where agents with Claude-3.5-Sonnet outperformed GPT-4o and Gemini-1.5-Pro by 16% and 21%, respectively, and the gaps became even more amplified when compared to open-source LLMs.  Our detailed analyses provide insights into the strengths and weaknesses of current models, though all models still fall short of human performance by more than 20% on average, struggling with complex map images and rigorous geo-spatial reasoning. This gap highlights MapEval's critical role in advancing general-purpose foundation models with stronger geo-spatial understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the map-based understanding and reasoning abilities of large language models and vision language models. It introduces MapEval, a comprehensive benchmark designed to evaluate these foundation models using text, API, and vision environments, assessing their capabilities to handle heterogeneous geospatial contexts and perform compositional geo-spatial reasoning. MapEval comprises over 500 questions spanning 138 cities in 45 countries. Extensive experiments are conducted on three types of tasks within the MapEval framework, involving 25 advanced foundation models. The results highlight the impressive capabilities of state-of-the-art commercial foundation models, although they still lag behind human performance by more than 20%. Moreover, significant room for improvement remains for open-source large language models and vision language models.

### Strengths
1. The paper is well-structured and easy to follow.
2. The approach of assessing the geospatial reasoning abilities of advanced foundation models through map services is interesting. By leveraging real-world contexts and results provided by Google Maps, the evaluation becomes both practical and valuable.
3. The MapEval benchmark offers three distinct environments—text, API, and vision—allowing for a comprehensive assessment of foundation models. This setup provides flexibility to examine model performance from different perspectives while maintaining a consistent context.

### Weaknesses
1. The discussion of related work is insufficient. For example, the paper does not discuss the differences and relationships between this study and prior research, such as GeoQA [1] and other similar evaluations [2].

[1] Mai, Gengchen, et al. "Geographic question answering: challenges, uniqueness, classification, and future directions." AGILE: GIScience series 2 (2021): 8.

[2] Roberts, Jonathan, et al. "GPT4GEO: How a Language Model Sees the World's Geography." arXiv preprint arXiv:2306.00020 (2023).

2. The evaluation is relatively small in scale and lacks a systematic approach. The tasks outlined in Table 1 and Figure 2 are overly simplistic, requiring more expert-level geospatial reasoning knowledge to enhance and extend the design of the evaluation framework. The current tasks do not adequately probe the models' abilities to handle complex spatial relationships, temporal dependencies, or multi-step reasoning which are crucial for real-world geospatial applications. For instance, the routing tasks primarily focus on direct paths, neglecting scenarios involving dynamic traffic, road closures, or alternative transportation modes.

3. As shown in Figure 3, although the questions span 54 countries, many nations are represented by only a single question, which is insufficient to ensure a robust evaluation. The abstract's claim regarding spatial coverage seems exaggerated. The lack of balanced geographic representation introduces a bias, potentially favoring models trained on data from more frequently represented regions. This uneven distribution limits the generalizability of the findings and raises concerns about the benchmark's ability to assess performance across diverse geospatial contexts.

4. The set of large language models and vision-language models assessed in the experiments is limited. Some important models, such as the Qwen2.5 series, Qwen2VL series, VILA series, and MiniCPM2.5, should be included to provide a more comprehensive evaluation. The absence of these models, which have demonstrated strong performance in various benchmarks, makes it difficult to ascertain the true state-of-the-art in geospatial reasoning capabilities.

### Questions
1. Could the authors elaborate on the relationship between MapEval and prior research, e.g.,  GeoQA and GPT4GEO?
2. The paper should report additional results for significant foundation models, such as the Qwen2.5 series, Qwen2VL series, VILA series, and MiniCPM2.5.

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
4

### Summary
The paper introduces MAPEVAL, a benchmark designed to assess the geo-spatial reasoning capabilities of foundation models in map-based scenarios. MAPEVAL evaluates models across three task types—textual, API-based, and visual—that involve querying and reasoning with map-based information. These tasks test a model’s ability to handle complex geographical contexts, such as travel routes, location details, and map infographics.

MAPEVAL’s dataset includes 550+ multiple-choice questions spanning 138 cities and 54 countries, examining models’ abilities in areas like spatial relationships, navigation, and planning. The evaluation showed that top models, such as Claude-3.5-Sonnet, GPT-4o, and Gemini-1.5-Pro, performed well overall but still fell significantly short of human accuracy, particularly in complex tasks requiring deep reasoning.

Key challenges identified include handling intricate map visuals, spatial and temporal reasoning, and managing tasks requiring multi-step decision-making. This study highlights MAPEVAL’s potential to advance geo-spatial understanding in AI, suggesting future development could involve models specialized in spatial reasoning or enhanced integration of map tools.

### Strengths
1. Collecting relevant world information using map tools or APIs is a great way to test LLMs' ablility in solving geo-spatial reasoning with both internal and external information.
2. The inclusion of diverse task types of Place Information, Routing, Nearby, Unanswerable, and Trip effectively addresses a wide range of real-world user scenarios.
3. Great effort on using MapQaTor to streamline the collection of textual map data.
4. High quality human-labeled data and evaluation.
5. Broad distribution of data across various global regions.

### Weaknesses
1. Only multiple choice questions are adopted in MapEval. More diversity question type should be added to further explore the ability of LLMs, for real world problems are mostly open-ended.
2. The sample size for each task is limited, you may consider to use some methods to scale up your benchmark with great quality. 
3. It would be more beneficial to test LLMs with different architectures, rather than focusing on different versions of the same model.

### Questions
1. There seem to be some problems with the API calling agent, can you explain more how you train the agent and possibly fix the problems of the agent?

### Soundness
3

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
4

### Summary
This paper presents the MAPEval evaluation dataset, which assesses the capabilities of foundational models (such as large language models and vision-language models) in spatial reasoning and geographic information extraction applications from three perspectives: textual, API-based, and visual evaluation modes. The authors provide a detailed description of the dataset creation process, introduce the performance of multiple models on the dataset, and thoroughly analyze the abilities of different models.

### Strengths
1. This paper is clear, with a detailed description of the dataset collection process and contribution points.
2. This paper tests the performance of multiple models on the dataset, which can provide guidance for readers on using different models.

### Weaknesses
(1) This paper introduces a dataset to evaluate the capabilities of existing models, but I didn't gain much insight from it. Specifically, I learned about the capabilities of different models on this dataset, but then what? It feels like an incomplete study. Perhaps this paper would be more suitable for a data track.
(2) Since the authors only collected a dataset and evaluated different models, the research lacks sufficient innovation. It appears more like an experimental report than a research paper.
(3) What I was hoping to see was some form of inspiration or insight from this paper, but unfortunately, I couldn’t find that. All I can gather is that different models may have advantages and disadvantages in different areas.
(4) I think the paper might be lacking in terms of analyzing the distinct capabilities demonstrated by different models based on the evaluation results. The authors should draw conclusions on how to design a model that performs well across all aspects. This would greatly interest readers and significantly enhance the research value of the paper.
(5) If the authors could attempt and verify the suggestions from point four, I think this paper would be very strong.
(6) In reality, I feel there's also a lack of discussion on the practical applications of large language models (LLMs) and visual language models (VLMs), as they tend to serve different purposes. Specifically, can the conclusions from this paper guide users on designing a comprehensive framework to solve real-world problems? I think further discussion in these areas would be beneficial.
In summary, while the contribution of this paper is clear, it indeed lacks certain elements that would make it more impactful.

### Questions
I believe this research could be further improved by discussing why different models perform differently on the collected dataset, and exploring the relationship between the existing results and model designs to provide more insights.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors claimed that the capabilities of the foundation model in location or map-based reasoning have not been systematically studied. This paper creates a benchmark MAPEVAL to assess map-based user queries with geo-spatial reasoning. MAPEVAL evaluates 25 well-known foundation models on textual, API-based, and visual three types of tasks and 550+ multiple-choice questions. Although, no single foundation model outperforms others on all tasks, they still analyze the strengths and weaknesses of current prominent models. Overall, the benchmarking of foundation model in map tasks like map search is useful, while more in-depth analysis would be beneficial. In addition, I am unsure about whether this paper is actually a fit for ICLR.

### Strengths
1. This paper introduces the MAPEVAL benchmark to evaluate the geo-spatial reasoning capabilities of foundation models in map-based user queries, which is a meaningful effort in general.
2. The paper is generally detailed and easy to follow.
3. The distinction between open-source and closed-source foundation models is useful as a reference for the future.

### Weaknesses
1. The number of test cases available for evaluating foundation models is relatively small, with only around 550 cases. This limited size may not fully capture the diversity of real-world map-based queries, potentially leading to an incomplete assessment of model capabilities. The benchmark might be susceptible to overfitting on the specific set of questions, and the results may not generalize well to unseen scenarios. A larger and more diverse dataset would be necessary to ensure the robustness of the evaluation.

2. The benchmark framework, as described, appears to have limitations in evaluating multi-modal large language models that combine both text and visual information in a truly integrated manner. While the paper mentions visual tasks, it is unclear if the models are truly leveraging the visual and textual information jointly for reasoning, or if they are treating them as separate inputs. The framework should ideally test the models' ability to perform complex reasoning that requires a deep understanding of both modalities.

3. The analysis is not in-depth enough. It would be beneficial to point out the root causes of the performance (rank), which could inspire the future development of map-related foundation models and the gradual specialization of general-purpose models. The paper should delve deeper into the specific types of errors made by each model, analyzing whether the errors are due to lack of spatial reasoning, poor understanding of the textual query, or issues with the API calls. A more granular analysis would help identify the specific weaknesses of each model and provide actionable insights for improvement.

### Questions
1. The last paragraph of the introduction mentions ablation experiments, but I could not find the experimental content or results in the main text.
2. This paper compares the evaluation results of several foundation models, but it should further clarify whether any specific geographic specialized foundation models were used to highlight the specialization in geo-spatial reasoning tasks. If none were used, please explain the reasons. Example models are those developed with geographic knowledge like K2, and remote sensing models (the number is increasing).

### Soundness
2

### Presentation
3

### Contribution
2
