# StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization

- Decision: Accept
- Scores: 6, 8, 5, 8

## Abstract
Retrieval-augmented generation (RAG) is a key means to effectively enhance large language models (LLMs) in many knowledge-based tasks. 
However, existing RAG methods struggle with knowledge-intensive reasoning tasks, because useful information required to these tasks are badly scattered. 
This characteristic makes it difficult for existing RAG methods to accurately identify key information and perform global reasoning with such noisy augmentation.
In this paper, motivated by the cognitive theories that humans convert raw information into various structured knowledge when tackling knowledge-intensive reasoning, we proposes a new framework, StructRAG, which can identify the optimal structure type for the task at hand, reconstruct original documents into this structured format, and infer answers based on the resulting structure. 
Extensive experiments across various knowledge-intensive tasks show that StructRAG achieves state-of-the-art performance, particularly excelling in challenging scenarios, demonstrating its potential as an effective solution for enhancing LLMs in complex real-world applications

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces StructRAG, a novel framework designed to enhance LLMs for knowledge-intensive reasoning tasks by structuring information at inference time. StructRAG addresses limitations in existing retrieval-augmented generation (RAG) methods, which struggle when relevant knowledge is dispersed and reasoning demands are complex. Inspired by cognitive theories, StructRAG applies a hybrid structure router to identify the best structure type for each task, a scattered knowledge structurizer to transform raw documents into structured knowledge, and a structured knowledge utilizer to perform multi-step reasoning. This framework achieves state-of-the-art results across multiple benchmarks and tasks, particularly excelling in challenging scenarios where information is fragmented and extensive reasoning is required.

### Strengths
The paper addresses a challenging problem in LLM and RAG research, focusing on improving knowledge-intensive reasoning for real-world tasks. The idea of information structurization for RAG is clear and innovative, offering a new approach in this area.

The architecture and its components are described clearly, with each part of the StructRAG model explained in a way that makes it easy to follow. The experiments are thorough and well-documented, including ablation studies that show the contributions of each module and support the effectiveness of the approach.

Overall, the work has practical applications and could be adapted to a range of RAG-related tasks, suggesting it has potential for further impact in the field.

### Weaknesses
The study presents StructRAG’s effectiveness with a single structured knowledge type for each task, yet it is unclear how the model would perform on tasks requiring multiple types simultaneously. For example, an ablation study that evaluates combinations of two fixed structure types could shed light on whether using multiple structure types consistently improves performance across different task categories.

The paper does not provide details on the distribution of structure types chosen by the hybrid structure router in its dataset. Since some structure types, such as algorithmic pseudo code, may be more complex to extract compared to tables or catalogues, reporting this distribution would clarify the router’s efficacy across different structure types. Additionally, an analysis of the structurizer’s performance in cases involving algorithmic structuring would help assess whether these cases yield similar performance gains as simpler structures.

Table 5 highlights performance differences when using fixed structure types, but these differences may be influenced by the distribution of tasks that align better with certain types (e.g., most tasks in the dataset naturally suited to tables). A breakdown of the dataset showing the router’s selected structure types and a comparison to human-selected types would be useful. Such a comparison could indicate how well the router aligns with human judgment and whether adding certain structure types as a standard complement might enhance overall performance in diverse datasets.

In Table 3 and Figure 3, the exact match (EM) rate for Set 4 appears close across methods or even equivalent in some cases. Could the authors clarify whether this is due to specific characteristics of the dataset (e.g., limited answer variation) or if this is a coincidence? If the dataset impacts EM rates, additional context would be helpful.

### Questions
In Table 3 and Figure 3, the exact match (EM) rate for Set 4 appears close across methods or even equivalent in some cases. Could the authors clarify whether this is due to specific characteristics of the dataset (e.g., limited answer variation) or if this is a coincidence? If the dataset impacts EM rates, additional context would be helpful.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces StructRAG, a novel framework for improving retrieval-augmented generation (RAG) in knowledge-intensive reasoning tasks. The key insight is that existing RAG methods struggle when useful information is scattered across documents, making it difficult to identify and reason with key information.

Inspired by cognitive theories about how humans process information using different knowledge structures, StructRAG consists of three main components:

1. A hybrid structure router that determines the most appropriate structure type (e.g., tables, graphs) for a given task
2. A scattered knowledge structurizer that converts raw documents into the chosen structured format
3. A structured knowledge utilizer that decomposes complex questions and performs reasoning using the structured knowledge

To train the hybrid structure router effectively, the authors develop a novel pipeline for generating training data through task synthesis, solution simulation, and preference judgment, combined with the DPO algorithm for preference learning.

Experimental results show that StructRAG achieves state-of-the-art performance across various knowledge-intensive tasks, with particularly strong improvements on more complex tasks. The framework also demonstrates better performance and faster operation compared to existing Graph RAG methods.

The paper's main contribution is presenting a cognitively-inspired approach to structuring information during inference time in RAG systems, offering a promising direction for handling complex reasoning tasks where relevant information is scattered across multiple sources.

### Strengths
This paper demonstrates several notable strengths:

- The novel integration of cognitive science principles into RAG systems. The authors establish meaningful connections between human information processing and computational approaches, making the cognitive science foundation both natural and practical.

- The paper addresses a well-recognized challenge in the field: efficient information retrieval from unstructured inputs. Their solution, particularly the Hybrid Structure Router that mimics human decision-making combined with DPO fine-tuning, offers an innovative yet implementable approach.

- The experimental evaluation is comprehensive, comparing StructRAG against current state-of-the-art approaches including long-context models, traditional RAG, RQ-RAG, and GraphRAG. The promising results across these various settings demonstrate the method's practical value.

- The ablation studies are particularly insightful, reflecting the authors' thorough analysis and iterative refinement of their methodology.

### Weaknesses
While not a significant weakness, one suggestion concerns the comparison with Graph RAG. Graph RAG typically excels with complex relational data rather than long-context scenarios, which might explain its relatively poor performance in many of the experimental settings. A more targeted comparison using relationship-heavy datasets could provide additional insights into the relative strengths of both approaches.

### Questions
Lines 458-460 highlight a challenge in real-world applications. How do the authors propose to address this challenge?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a novel method to summarise the document with Hybrid Structure Router, and it dynamically converted documents into graph, chunk, catalogue, algorithm, table. It showed that the new method had better performance in terms of score and latency. The paper contains thorough literature review, and detailed experiment results. However, the paper only evaluates the performance on Qwen2-7B-Instruct model, which is a relatively small model. It did not evaluate on other main stream models like llama, and also did not evaluate the new method on models with larger amount of parameters. For example, the GraphRAG method used GPT-4-turbo in their original paper, and it is very hard to conclude that StructRAG is better than GraphRAG with the results of Qwen2-7B-Instruct presented in this paper.

### Strengths
- It proposed a novel method
- It conducted thorough literature review
- It compared the method with other RAG methods including Long-context, RAG, RQ-RAG, GraphRAG

### Weaknesses
 - It did not provide the definition of LLM score
- It only tested the new model with Qwen2-7B-Instruct with relatively small amount of parameters, and lacks of experiment results with other models or models with larger amount of parameters


### Questions
- What is the definition of LLM score
- Did you tested the new method StructRAG with other models, or models with larger amount of parameters?

### Soundness
3

### Presentation
3

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
The paper addresses the challenge of handling RAG with complex documents, where information may be scattered across different parts of multiple documents. For RAG to be accurate, it must precisely retrieve and integrate all relevant texts, which presents a significant challenge. To tackle this, the authors propose a method that mimics human cognitive processes by using LLMs to convert dispersed information into various types of structured knowledge. Additionally, they employ a Hybrid Structure Router, trained with DPO, to select the appropriate structure type for each query. The implementation of this approach demonstrates its effectiveness in improving performance across most tasks.

### Strengths
**Originality**: This paper introduces a novel approach to addressing the complex issue of RAG from multiple knowledge sources. The proposed process includes summarizing structured knowledge into five categories and utilizing LLMs for the construction and retrieval of this structured knowledge. This approach demonstrates a high degree of originality.

**Quality**: The writing quality of the paper is commendable, with coherent reasoning and a logical flow that makes it easy for readers to understand. The authors have conducted detailed experiments across multiple datasets, effectively demonstrating the validity of StructRAG.

**Clarity**: The paper is logically and structurally well-organized, with a clear presentation of the proposed framework's structure and processes. The use of formulas and diagrams effectively illustrates the concepts and workflow.

**Significance**: This paper effectively addresses the challenge of handling RAG with complex documents by aggregating knowledge from different sources and structuring it into specified formats. This approach significantly enhances the performance and applicability of RAG systems.

### Weaknesses
The paper, while introducing the StructRAG framework, relies significantly on the inherent capabilities of large language models (LLMs) for structuring and utilizing raw knowledge. However, it could benefit from a more detailed discussion on the challenges encountered during knowledge processing and on strategies for more effectively leveraging LLMs in this context.

### Questions
1. Could you provide more detailed examples of tasks that are suitable for each of the five types of structured knowledge you propose? This would help clarify the rationale behind categorizing them into these five types.

2. When using LLMs to extract structured knowledge, do the LLMs have the capability to directly generate knowledge in the specified formats? Did you perform any checks or corrections on the outputs generated by the LLMs?

### Soundness
4

### Presentation
4

### Contribution
3
