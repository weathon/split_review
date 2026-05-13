# GeoLLM: Extracting Geospatial Knowledge from Large Language Models

- Decision: Accept
- Scores: 3, 6, 8, 5, 6

## Abstract
The application of machine learning (ML) in a range of geospatial tasks is increasingly common but often relies on globally available covariates such as satellite imagery that can either be expensive or lack predictive power.
Here we explore the question of whether the vast amounts of knowledge found in Internet language corpora, now compressed within large language models (LLMs), can be leveraged for geospatial prediction tasks. 
We first demonstrate that LLMs embed remarkable spatial information about locations, but 
naively querying LLMs using geographic coordinates alone is ineffective in predicting key indicators like population density. 
We then present \method, a novel method that can effectively extract geospatial knowledge from LLMs with auxiliary map data from OpenStreetMap.
We demonstrate the utility of our approach across multiple tasks of central interest to the international community, including the measurement of population density and economic livelihoods.
Across these tasks, our method demonstrates a 70\% improvement in performance (measured using Pearson's $r^2$) relative to baselines that use nearest neighbors or use information directly from the prompt, and performance equal to or exceeding satellite-based benchmarks in the literature.
With \method{}, we observe that GPT-3.5 outperforms Llama 2 and RoBERTa by 19\% and 51\% respectively, suggesting that the performance of our method scales well with the size of the model and its pretraining dataset.
Our experiments reveal that LLMs are remarkably sample-efficient, rich in geospatial information, and robust across the globe.
Crucially, \method{} shows promise in mitigating the limitations of existing geospatial covariates and complementing them well. Code is available on the project website: \href{https://rohinmanvi.io/GeoLLM}{https://rohinmanvi.io/GeoLLM}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method to extract prior geospatial knowledge from pretrained LLM. 
The queried knowledge includes spatial demographics data, census data, and survey data. 
The findings in the paper are interesting, however seem very preliminary. And the experiments are limited.

### Strengths
The paper is well presented, and the experiments cover several different geospatial datasets and tasks in relation to census and demographic data.

### Weaknesses
•	It seems that the proposed GeoLLM can only perform one specific task. After fine-tuning, is the fine-tuned LLMs (e.g., GPT-3.5) able to retain the ability to answer general questions that is not related to the specific task? Including some discussions about the generalization part could be useful.

•	The proposed model can only handle static/tabular geo information. It does not handle other types of spatial data, or spatiotemporal data and tasks.

•	Baselines are too simple. Considering some more recent deep-learning-based or Transformer-based baselines could be more convincing.

•	The experiments are limited.

### Questions
•	Is there any specific tokenization process introduced for GPS coordinates? Normally, the direct tokenizers with LLMs could split the GPS point into several different tokens, which might undermine the ability to understand GPS coordinates correctly.

•	Why using classification setting? The current loss functions that LLMs are using is a kind of binary, where only predictions that exactly match the masked word are considered correct and rewarded, while all other predictions are considered incorrect and penalized. So, there is no has no awareness and no sense of being close to or far away the correct answer. Normally, for the task described in this paper, this kind of sense should be valuable in getting better performance.

•	What about the deployment cost of the proposed GeoLLM? For example, compared to the baselines, what are the fine-tuning costs and inference costs of using GPT-3.5 or other LLMs. From my experience, fine-tuning GPT-3.5 can be very expensive.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study explores leveraging large language models (LLMs) for geospatial prediction tasks, addressing limitations of traditional covariates like satellite imagery. The authors introduce GeoLLM, an approach that effectively extracts geospatial knowledge from LLMs with auxiliary map data. The proposed method demonstrates a 70% improvement in performance compared to baselines, rivaling satellite-based benchmarks. GPT-3.5 outperforms other models, highlighting the scalability of the proposed approach. This research underscores LLMs' efficiency, global robustness, and potential to enhance geospatial analysis.

### Strengths
1. It proposed a novel method for efficiently extracting geospatial knowledge from large language models.
2. The paper outlined experiments to evaluate extracting geospatial knowledge from large language models, which included constructing a comprehensive benchmark, developing a robust set of baselines, and presenting results and an ablation study.
3. The paper revealed that GeoLLMs are sample-efficient, rich in geospatial information, and robust across the globe.

### Weaknesses
1. The paper does not provide a detailed analysis of the potential biases of LLMs and their training corpora. 
2. It would be better to compare the GeoLLM’s performance with the results from satellite images.

### Questions
Have you tried the zero-shot or few-shot performance of various LLMs on the presented tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes GeoLLM, a prompt method that enriches geographic coordinates with auxiliary map data for geospatial prediction task (e.g., population density, economic livelihoods). This prompt approach outperforms some baseline methods in several tasks.

### Strengths
1.  This paper is well structured and good at the clarity of presentation.

2.  The significance of the problem is high, potentially impacting a wide range of geospatial applications and offering a new way to view large language model capabilities.

3. The paper provides a detailed discussion of how large language models can be linked to geospatial applications. This can potentially bring new research opportunities to the field of spatial data mining.

### Weaknesses
1.  The method presented seems to build incrementally on existing methodologies to generate auxiliary texts for prompt engineering, which may not represent a significance in technical novelty.

2.  The scope of experiments could be further expanded to support the conclusion. Please consider the Questions below for details.

### Questions
1.  While Peason's r^2 is used for comparisons with previous literature, can I see more comparisons with baselines on other evaluation metrics like MAE or MSE?
    
2.  Could the paper present the label distribution to evaluate performance variations between urban and rural areas, or densely versus sparsely populated regions?
    
3.  It would be beneficial to include a wider range of baselines, particularly "weaker" text embedding models like Doc2Vec, ELMo, and BERT, paired with basic predictors, for a holistic performance comparison.
    
4.  I tried to use GPT 4.0 for the example in Figure 1, and it looks like it can solve this question pretty well with only coordinates:  
    """User: Coordinates:  
    (40.76208, -73.98042)  
    Population Density (On a Scale from 0.0 to 9.9):
    
    ChatGPT:  
    Given the coordinates (40.76208, -73.98042), this location is in New York City, specifically in Manhattan. Manhattan has one of the highest population densities of any area in the United States.  
    On a scale from 0.0 to 9.9, where 9.9 would represent the most densely populated, Manhattan would be close to the top of that scale. While I can't provide an exact number without more specific criteria for each point on the scale, it would be reasonable to rate Manhattan, particularly Midtown which is where these coordinates roughly point to, above 9.0 on a density scale capped at 9.9, considering its population density surpasses 10,000 people per square kilometer.
    
    User:  
    Just return a number
    
    ChatGPT:  
    9.5  
    """  
    The paper could enhance its soundness by examining the performance with more powerful LLMs. Performance insights using LLama 13b and 70b, as well as the latest GPT-4 model, would be valuable.




5.  Can I see the performance on LLMs without finetuning? It would be necessary to see the impact of fine-tuning in geospatial predictions.
    
6.  Few-shot learning capabilities are an intriguing aspect of LLMs. An analysis of the model’s few-shot performance, both pre and post fine-tuning, could significantly add to our understanding of the method's efficiency and flexibility.
    
7.  The current ablation study does not fully clarify the independent contribution of coordinates to the model's performance. Results from experiments that exclude coordinates from prompts would help demonstrate that the enhanced performance is not solely attributable to the auxiliary map data.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a new method called GEOLLM, which can effectively extract spatial knowledge from large language models and fine tune it by using auxiliary map data from OpenStreetMap. Experiments on various tasks of several large-scale real-world sets show that the method is practical and effective. In the experiment, the author found that the pre-training language model has rich geospatial knowledge, and their method can unlock this knowledge. In addition, the author also discusses how to construct appropriate hints to extract geospatial knowledge, and how to find a balance between knowledge extraction and sample efficiency.
The contributions of the paper include demonstrating the quantity, quality, and scalable nature of geospatial knowledge contained in LLMs and presenting a simple and efficient method for extracting this knowledge.

### Strengths
S1: This paper delves into the internal structure of large-scale language models in extracting geographical knowledge. Utilizing auxiliary map data from OpenStreetMap to extract geospatial knowledge from large language models represents a new approach that has been sparingly explored in previous research. By fine-tuning basic models of different structures and scales and employing prompt templates containing addresses and nearby places, geographical knowledge within pre-trained models is effectively extracted. 
S2: In terms of significance, this paper addresses a challenge in natural language processing by exploring how to extract geospatial knowledge from large-scale language models. The paper proposes a new approach to knowledge extraction based on fine-tuning and prompt strategies, establishing a new concept of "geospatial covariates."

### Weaknesses
W1: Lack of clear prompt templates and answer pairs design. The paper mentions the use of multiple data sources and various tasks; however, there are significant deficiencies in the theoretical approach. Specifically, the paper does not clearly specify whether the prompt formats are the same for each task and lacks detailed descriptions of how prompt templates and answer pairs were designed for different tasks. This lack of clarity makes it challenging for readers to understand the experimental design and poses obstacles for replication and further research.
W2: Lack of clear experimental design details. Furthermore, in terms of experimental design, there are shortcomings in this paper. It does not provide a clear overview of the experimental training process, including the selection of data, preprocessing steps, and hyperparameter tuning. This omission makes it difficult to evaluate the detailed experimental procedure, hindering the reproducibility of the experiments.
W3: Absence of comparison with ground-truth. Additionally, the paper does not thoroughly explore the comparison between experimental results and real-world geospatial data (Ground Truth). Accuracy of geospatial knowledge is crucial in practical applications; however, the paper lacks comparative analysis with actual geographical data.

### Questions
Besides what is mentioned in weaknesses, what does “the prompts’ mean in “This suggests that the model is less prone to overfitting on the prediction tasks compared to the prompts” on page 4?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores possible ways to extract and tease out the geospatial information embedded inside the knowledge bases like LLMs. Specifically, they fine-tune LLMs such as chatGPT and Llama-2 with training data curated using OpenMaps with labels derived from various sources for geospatial tasks. On a variety of tasks, they show that fine-tuning LLMs on such data can effectively outperform several baselines. They further establish the geographical consistency of their results as well as ablation on suitable prompts.

### Strengths
- This paper reveals an innovative way to use LLMs towards a expert tasks such as computing geospatial metrics without access to various kinds of data. 

- The access to various covariates, as mentioned, might not always be available - so the motivation of this work is sound and valid.

- The experiments cover a wide variety of tasks and settings, indicating the power of the proposed approach.

- The experiments involve comparison between multiple LMs like RoBERTa, GPT3.5 and LLama-2, with several useful observations pertaining to performance as well as the data efficiency of each of those.

### Weaknesses
- There are no experiments which really delineate where the performance improvements of the final model are coming from. The chosen baselines are not that strong. To delineate the knowledge offered by the LLMs compared to that of the training data, can the authors also conduct an experiment where they fine-tune a normal neural network (not LLM) on the created training data? For example, we can first pass the prompt to a sentence encoder, and then train an MLP/Neural Network which uses this embedding to predict the output as a regression or classification task  (using the same training data used during fine-tuning). This would separate the contributions offered by the LLM compared to the training data which was used in fine-tuning. 

-  Adding to the above, can the authors also provide results with using zeroshot capabilities of the LLMs? This would help to separate the importance of fine-tuning on custom prompts. 

- Assuming the covariates are indeed available, does the current method offer complimentary benefits to further improve the performance?

- The authors, if possible, should also make comparisons with fine-tuning several other geo-spatial LLM type models, like K2 (Deng et. al. 2023) through fine-tuning on the same set of data.

### Questions
Overall, I have several requests to further delineate the performance improvements due to various aspects, while also using stronger baselines as detailed above. I am ready to raise my rating upon satisfactory rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
