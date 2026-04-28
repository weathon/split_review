# AISciVision: A Framework for Specializing Large Multimodal Models in Scientific Image Classification

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Trust and interpretability are crucial for the use of Artificial Intelligence (AI) in scientific research, but current models often operate as black boxes offering limited transparency and justifications for their outputs. Motivated by this problem, we introduce \aiscivision, a framework that specializes Large Multimodal Models (LMMs) into interactive research partners and classification models for image classification tasks in niche scientific domains. Our framework uses two key components: (1) Visual Retrieval-Augmented Generation (VisRAG) and (2) domain-specific tools utilized in an agentic workflow. To classify a target image, \aiscivision first retrieves the most similar positive and negative labeled images as context for the LMM. Then the LMM agent actively selects and applies tools to manipulate and inspect the target image over multiple rounds, refining its analysis before making a final prediction. These VisRAG and tooling components are designed to mirror the processes of domain experts, as humans often compare new data to similar examples and use specialized tools to manipulate and inspect images before arriving at a conclusion. Each inference produces both a prediction and a natural language transcript detailing the reasoning and tool usage that led to the prediction. We evaluate \aiscivision on three real-world scientific image classification datasets: detecting the presence of aquaculture ponds, diseased eelgrass, and solar panels. Across these datasets, our method outperforms fully supervised models in low and full-labeled data settings. \aiscivision is actively deployed in real-world use, specifically for aquaculture research, through a dedicated web application that displays and allows the expert users to converse with the transcripts. This work represents a crucial step toward AI systems that are both interpretable and effective, advancing their use in scientific research and scientific discovery.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces AISciVision, a framework designed to enhance the capability of large multimodal models (LMMs) for scientific image classification tasks. The framework comprises two main components: (1) Visual RAG (or VisRAG), which retrieves contextually similar positive and negative labeled images from the training set that serves as an initial prompt to the LMM or VLM model along with the test image that needs to be classified. (2) AI agentic workflow that engages with domain-specific tools in a multi-round conversation to classify input test image. The goal is to accurately classify the image and also generate transparent reasoning transcripts that detail the decision-making process. The paper also introduces a web application for real-time aquaculture pond detection.

### Strengths
- The paper is well-written and easy to understand.
- The two-stage process of first using VisRAG followed by an interactive AI agentic workflow with domain-specific tools is innovative and well-integrated.
- The framework demonstrates applicability across different domains and generates reasoning transcripts for enhanced interpretability of image classification.
- The paper introduces a web application for aquaculture pond detection which can serve as a data collection tool to build better algorithms based on user feedback.

### Weaknesses
 - The paper could benefit from a stronger motivation section that elaborates on the significance of the selected scientific classification tasks and their scientific impact. While generating reasoning transcripts is valuable, the specific implications of correct classification and the benefit of LMMs/VLMs over supervised classification models are still unclear. For example, the paper does not clearly articulate why a complex framework like AISciVision is needed when simpler, well-established supervised methods could potentially achieve similar or better results in terms of classification accuracy. The lack of a clear justification for the added complexity makes it difficult to assess the practical value of the proposed approach.
- Although the authors claim AISciVision is model-agnostic, experiments are limited to GPT-4o. Including evaluations with other LMMs/VLMs, such as LLaVA [A], BLIP [B], etc. would strengthen this claim and demonstrate broader applicability. The absence of such evaluations raises concerns about the generalizability of the findings and whether the observed performance is specific to the GPT-4o model architecture. Furthermore, the paper does not explore the impact of different prompt variations or hyperparameter tuning on the performance of other LMMs/VLMs, which could be critical for real-world deployment.
- The paper asserts that it outperforms several fully supervised models; however, Table 1 displays a weak baseline of k-NN as a supervised approach. While CLIP + MLP is also included as a supervised baseline, it performs similarly to, and in some cases better than, AISciVision on two of the three datasets (Eelgrass and Solar). To more effectively justify the advantages of AISciVision, it would be helpful to include stronger and more diverse supervised baselines, such as fine-tuned convolutional neural networks (CNNs) or vision transformers (ViTs) that are commonly used in image classification tasks. This would provide a more rigorous comparison and better highlight the potential benefits of the proposed framework.
- The Tools for the Aquaculture dataset leverage additional geospatial location metadata and utilize Google Maps APIs to fetch images of areas beyond the input test image. Depending on the selected tool—such as panning left/right/up/down, or zooming out—these tools can access a wider context. This makes it an unfair comparison for baseline models that solely rely on the input images and have not seen the images of the surrounding area. This raises questions about the validity of the performance gains reported for the aquaculture dataset, as the AISciVision framework has access to privileged information not available to the baselines. The use of external data sources also introduces potential biases and inconsistencies that are not adequately addressed in the paper.
- The domain-specific tools form a significant part of the AISciVision framework but most of the details are missing in the manuscript and are discussed in the appendix. The lack of detailed descriptions in the main text makes it difficult to understand the specific functionalities of these tools and how they contribute to the overall performance of the framework. Furthermore, the paper does not provide a clear rationale for why these specific tools were chosen, nor does it discuss the potential limitations or biases associated with their use.

### Questions
- The inclusion of both positive and negative images as initial prompts is interesting. What specific advantage does this approach offer? How would the model’s performance change if only one positive or negative image is provided?
- Table 2 provides ablations with GPT-4o and different components of AISciVision.In a zero-shot setting, GPT-4o demonstrates strong performance across all datasets. For the Eelgrass and Solar datasets, the majority of performance improvements are attributed to the combination of GPT-4o and VisRAG. What additional benefits do these tools provide in these scenarios?
- In the aquaculture dataset, the most notable improvements come from using GPT-4o along with tools that utilize the Google Maps API and supplemental images. How does the model perform when it is limited to tools similar to those used for the Eelgrass and Solar datasets?
- For the aquaculture dataset, when using images of surrounding areas through the Google Maps API, how do you account for changes in the landscape over time? How does this affect the analysis?
- Why do the initial user prompts to the LMM differ for various datasets when providing positive and negative images?
- Why is the model encouraged to use at least three tools? Does performance vary with fewer or more tools?
- What are the benefits of using VisRAG as a standalone component? Could it be incorporated as one of the tools within the AI agent's workflow?
- How are the domain-specific tools chosen? The same tools are used for two different datasets: the Eelgrass dataset, which contains plant images, and the Solar dataset, made up of satellite images. Why do we refer to them as domain-specific tools?
- The AISciVision framework for Aquaculture pond detection relies on geospatial metadata. What happens if a user does not have the geospatial location metadata for a specific test image while using the web application? Is the framework adaptable for datasets that lack this metadata, or are there alternative features that can be utilized?

### Soundness
2

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
3

### Summary
The paper presents an approach for interpretable image classification tailored to scientific domains. It introduces a framework that enables Large Multimodal Models (LMMs) to perform more accurate and explainable reasoning by integrating Visual Retrieval-Augmented Generation (VisRAG) and domain-specific tool usage. This approach can be effective for niche scientific tasks involving binary image classification, where transparency and understanding of the decision-making process are essential.

### Strengths
1.	Ablations to understand importance of VisRAG and Tools
2.	Exact prompts used were provided making reproduceability easier

### Weaknesses
1.	Compute heavy multi turn conversation.
2.	Limited to binary classification: The approach in its current form is limited to binary classification. Extending the approach to multiclass classification do not appear to be straightforward. If the authors can possible ways to extend beyond binary classification that would be helpful.
3.	Bias from the prediction of supervised model. As discussed in the supplementary, the framework can be heavily influenced by the supervised model.

### Questions
Some suggestions and questions,

1.	It would be interesting to perform an experiment without supervised model in the toolset, considering that the LMM can be heavily influenced by the model.
2.	There is no mention of the train test split for each dataset. It can be relevant information
3.	There is a drop in performance of kNN going from 20% to 100% on Aquaculture dataset. Any explanation for why this is happening?

### Soundness
2

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
4

### Summary
The paper introduces a method for scientific image classification using Visual RAG and external tools with Large Multimodal Models (LLMs)/. For classification, the proposed method tries to mimic an 'expert human' by first retrieving relevant examples from the training to to compare and then using different tools to aid in the classification. They show the effectiveness of their method on 3 real world datasets and also show the reasoning ability through the multi-round dialog component. They also claim that the model is deployed as a web application and is being used by ecologists and scientists.

### Strengths
1. A very creative application of a) Visual RAG, b) utilizing external tools and 3) multi-round dialog with LMMs for scientific image classification.

2. The fact that the model is actively deployed and is used by ecologists for aquaculture research is quite impressive.

### Weaknesses
1. This kind of framework of using Visual RAG + external tools with Large models is not that novel. However, I do agree that their application in scientific images is quite novel.

2. The method provides reasoning of its predictions through it's transcripts during the multi-round dialog process. Although the transcript makes the model more interpretable and diverse, there is no verification/human evaluation of the correctness of the model's reasoning. A human evaluation study of the correctness of the reasoning would have been great.

### Questions
1. The method says that the most similar positive and negative images are retrieved for a test image. However, in the example transcripts, I can't seem to find where this step is happening. Could you explain how this retrieval is happening through an example?

2. The naive baseline of k-nn itself is very strong baseline. Did you find any particular reason for that?

3. It is said that the evaluation are done in two settings: low label (20%) and full labeled (100%). Where are these labels used? to train CLIP+MLP? or to retrieve +ve and -ve examples during Visual RAG?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a method that uses an LMM, such as ChatGPT, in combination with VisRAG and domain-specific tools to classify scientific images. At test time, given an image, the system retrieves similar images and prompts the LMM to utilize the tools (explaining how to use each one) to better understand and then classify the image. In addition to the classification result, the method also provides the confidence score and the conversation with the LMM to ensure transparency for the user.

### Strengths
- The authors try to increase the interpretability of classification task
- Make use of LMMs to solve real world problems
- Does not require any additional model training

### Weaknesses
 - Comparing new data to similar data carries a high risk of introducing bias into the process.
- Defining domain-specific tools is challenging, as it requires domain experts, and even experts may overlook some tools.
- Using multiple rounds of prediction increases both inference time and cost.
- Describing domain-specific tools in natural language is not always straightforward.
- The testing datasets are very small and may not cover a broad range of test samples.

### Questions
- How do you use a hardcoded prompt template for the response?
- How does your model output a probability score indicating its confidence?
- How do you determine how many conversation turns are enough?
- In the paper, you state: "We provide text descriptions of the available tools as prompts to the LMM, and instruct how to request tool use" How do you ensure that the LMM reliably follows your instructions behind the scenes? We know LMMs can sometimes misunderstand prompts, requiring users to read the answer, refine their prompt, and ask again.
- In the paper, you mention: "You ask the LMM to have 4 conversation turns." How do you determine that this number (4) is appropriate?
- In the paper, you state: "All embeddings for VisRAG are computed via CLIP." How do you ensure that these images are not out of distribution for CLIP?
- In the paper, you claim that "AISciVision consistently outperforms all baselines on all three datasets." What about the descriptive text your framework returns? Did you conduct any analysis on the quality of those texts?

### Soundness
2

### Presentation
4

### Contribution
2
