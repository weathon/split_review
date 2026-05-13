# Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback

- Decision: Reject
- Scores: 6, 5, 1, 3, 6

## Abstract
Large language models (LLMs) have demonstrated remarkable proficiency in a range of natural language processing tasks. Once deployed, LLMs encounter users with personalized factual knowledge, and such personalized knowledge is consistently reflected through users' interactions with the LLMs. To enhance user experience, real-time model personalization is essential, allowing LLMs to adapt user-specific knowledge based on user feedback during human-LLM interactions. Existing methods mostly require back-propagation to finetune the model parameters, which incurs high computational and memory costs. In addition, these methods suffer from low interpretability, which will cause unforeseen impacts on model performance during long-term use, where the user's personalized knowledge is accumulated extensively.
To address these challenges, we propose Knowledge Graph Tuning (KGT), a novel approach that leverages knowledge graphs (KGs) to personalize LLMs. KGT extracts personalized factual knowledge triples from users' queries and feedback and optimizes KGs without modifying the LLM parameters. Our method improves computational and memory efficiency by avoiding back-propagation and ensures interpretability by making the KG adjustments comprehensible to humans.
Experiments with state-of-the-art LLMs, including GPT-2, Llama2, and Llama3, show that KGT significantly improves personalization performance while reducing latency and GPU memory costs. Ultimately, KGT offers a promising solution of effective, efficient, and interpretable real-time LLM personalization during user interactions with the LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose to personalize the outputs of LLMs by augmenting them with the triplets from the knowledge graph (that is constructed based on the interactions between humans and LLMs), without fine-tuning. Specifically, the authors iteratively update the knowledge graph by generating the triplet that leads to the high probability of generating the correct personalized answer while removing the one with the lowest probability, and then use this constructed knowledge graph by retrieving the relevant triplets from it in response to the given query and augmenting LLMs with them in generating the answer. The authors validate the proposed approach on two knowledge editing benchmark datasets as well as real-world interaction data between humans and LLMs collected from five people, on which it outperforms relevant baselines.

### Strengths
* The proposed approach of updating the triplets within the knowledge graph in regards to the probability of generating the correct answer with them is sound and reasonable.
* The proposed approach outperforms relevant baselines substantially, while only requiring low computational costs.

### Weaknesses
 * The authors do not provide details about how to collect the interaction data between humans and LLMs, for example, how many samples are annotated (i.e., the number of samples seems not comprehensive enough), who are the annotators, and how to pay them. In addition to this, the authors may further demonstrate the quality of the annotated data, as currently it seems questionable.
* Besides this human-annotated data, the authors validate the proposed approach on knowledge editing benchmark datasets (whose goal is to generate the outputs that are counter intuitive compared to the knowledge that common LLMs or knowledge graphs have), which may not be appropriate to evaluate the performance of LLM personalization approaches.

### Questions
Please see the weaknesses above.

### Soundness
2

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
2

### Summary
This paper presents Knowledge Graph Tuning (KGT), a novel method for personalizing large language models (LLMs) by leveraging knowledge graphs (KGs) rather than modifying model parameters. KGT captures personalized factual knowledge from user interactions, updates knowledge graphs, and optimizes them without requiring back-propagation, thereby enhancing computational and memory efficiency.

### Strengths
I. Efficiency: KGT reduces latency and GPU memory usage by eliminating the need for back-propagation, making it suitable for real-time applications.

II. Interpretability: By using KGs to manage user knowledge, KGT enables transparent adjustments to user-specific information, enhancing the interpretability of the personalized responses.

### Weaknesses
I. KGT shares certain similarities with MemPrompt (https://arxiv.org/pdf/2201.06009). The authors should provide a detailed comparison to highlight the distinctive aspects of their approach.

II. Dependence on KG Quality: The effectiveness of the method relies on the accuracy and relevance of the KG. Low-quality KGs may lead to less effective personalization.

III. Complexity of Knowledge Retrieval: KGT may struggle with more complex or abstract knowledge retrieval tasks, where simple knowledge triples may not adequately represent user-specific knowledge.

IV. The quality of the presentation is below ICLR 2025 standards. For example:

 a. The format of the references should be consistent to ensure neatness and professionalism. For instance, the names of conferences should be uniformly presented either in abbreviations or full names, rather than a mixture of both.

b. Some of the referenced papers have already been accepted but are still listed as preprints on arXiv. For example, the line 661 should be "Zhengyan Zhang, Xu Han, Zhiyuan Liu, Xin Jiang, Maosong Sun, and Qun Liu. 2019. ERNIE: Enhanced Language Representation with Informative Entities. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pages 1441–1451, Florence, Italy. Association for Computational Linguistics."

### Questions
Please see weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a personalized knowledge editing algorithm for LLMs leveraging KGs. It avoids fine-tuning the LLMs while updating the user profile for new knowledge from feedback as a graph. The pipeline would be like: query->retrieve KG->LLM->user feedback->Update KG->LLM and iteratively. The idea is valuable for rapidly changing user preferences in various downstream tasks. However, the design of the methodology lacks careful consideration and the detailed comments can be found hereunder.

### Strengths
* This is indeed a Graph RAG paper and can be treated as a new angle which continuously updates the KG with new knowledge.
* The figures are well drawn and easy to follow.

### Weaknesses
 * I recognize the merits of this paper by editing KGs for changing user preference. However, the problem of KG editing is not rocket science, especially each time there will only be very limited triples involved to be added or removed. It could be far more concisely and effectively solved with engineering techniques.
* The word 'tuning' is not suitable which may cause misunderstanding, especially when it only refers to changing the structure of the KG without any parameter learning.
* The code is very important to figure out how the structure of KGs is indeed edited, as well as for the probability calculation. 
* **The paper heavily refers to ROG [1] for the entire methodology which involves plagiarism problem. It changes the storyline by introducing the concept of knowledge editing with no new methods/components.**  Therefore, there is no comment on the remaining of methodology.

### Questions
N/A

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel approach called Knowledge Graph Tuning (KGT) for real-time large language model personalization based on user feedback. The paper addresses the challenges of computational efficiency and interpretability in model personalization by leveraging knowledge graphs (KGs) to optimize the KGs instead of the model parameters. The proposed method is evaluated on state-of-the-art LLMs and compared with several baselines, showing significant improvements in personalization performance while reducing latency and GPU memory costs.

### Strengths
(1) The paper tackles a significant issue in large language models: real-time model personalization based on user feedback. The proposed method presents a promising solution to improve user experience by tailoring LLMs to individual knowledge.

(2) The incorporation of knowledge graphs (KGs) in the proposed method is both innovative and practical. The author offers a theoretical analysis of the method's design.

(3) The experimental evaluation is thorough, featuring tests on multiple datasets with state-of-the-art LLMs. The results highlight the effectiveness and efficiency of the proposed KGT method compared to various baselines.

### Weaknesses
 (1) The novelty of the proposed method is limited. The proposed framework is a typical retrieval-based method that relies on including retrieved facts in the context to tailor the output of LLMs. Similar ideas have been proposed by previous studies [1] and even have been applied in ChatGPT today with the proposed "memory module" (similar open-source version here: https://github.com/mem0ai/mem0).

(2) The proposed method relies on explicit human feedback to "optimize" the retrieval process, which largely limits its practicability. Moreover, it relies on structured KGs, which are hard to construct. Nowadays, ChatGPT and Mem0 can unsupervised and automatically extract memory from conversational contexts for personalized outputs, which is more flexible. 

Although the author proposes a theoretical analysis to explain the "optimization of retrieval". The analysis is trivial, which is widely adopted in the RAG such as [2]

(3) The effectiveness of the proposed method is only evaluated on the fact editing tasks. However, other aspects of alignment are not discussed in the paper, such as HarmfulQ, and compared with other efficient alignment methods, such as Deal [3].

### Questions
(1) Can the proposed method generalize to other alignment tasks and compare the performance with other efficient alignment methods?
(2) Can you compare it with other LLM personalized methods instead of just knowledge editing ones?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel method called Knowledge Graph Tuning (KGT) to personalize large language models (LLMs) in real time. Unlike traditional methods that rely on computationally expensive and memory-intensive back-propagation, KGT leverages external knowledge graphs (KGs) to manage user-specific information. This enables the model to adjust without altering its core parameters, improving efficiency and interpretability. Experimental results demonstrate that KGT significantly enhances personalization performance while lowering latency and resource requirements, showing promise in delivering efficient, effective, and interpretable real-time personalization.

### Strengths
The strengths of the paper lie primarily in its innovative approach to personalization for LLMs. By avoiding the use of back-propagation, KGT significantly reduces computational overhead, leading to faster processing times and lower resource consumption. This makes it particularly suitable for real-time applications, where latency can be a critical factor. Additionally, KGT offers a notable advantage in interpretability. By managing user-specific knowledge through adjustments to external knowledge graphs rather than internal parameters, the process becomes more transparent. This makes it easier to trace how user interactions influence changes, allowing for clearer insights into the personalization mechanics. The scalability of KGT is also a strong point, as the method handles an increasing volume of queries effectively, which is essential for users who accumulate extensive personalized knowledge over time. Experimental results back up these claims, showing that KGT performs better than existing methods in personalization benchmarks.

### Weaknesses
The success of KGT heavily depends on the quality and completeness of the knowledge graphs it uses. If these graphs contain inaccuracies or gaps, the effectiveness of personalization can be compromised, limiting the model's ability to provide relevant responses. Another limitation lies in its reliance on the LLM’s ability to follow instructions accurately when interpreting the knowledge graph. This could lead to inconsistent results if deployed on language models with varied instruction-following capabilities. Furthermore, while KGT aims to reduce user effort by handling knowledge updates through interactions, there are cases where explicit user feedback might still be required. This adds an element of manual intervention, potentially diminishing the appeal of fully automated personalization. The method also lacks a clear mechanism for handling contradictory user feedback over time, particularly when a user’s personalized knowledge evolves and conflicts with previously stored information in the knowledge graph. This could lead to instability in the personalized responses, especially in dynamic user environments.

### Questions
Can the authors elaborate on how KGT handles contradictory user feedback over time, especially when a user’s personalized knowledge evolves and conflicts with previously stored information in the knowledge graph?

### Soundness
3

### Presentation
3

### Contribution
2
