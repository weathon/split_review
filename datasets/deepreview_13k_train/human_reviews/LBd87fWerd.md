# GASLITEing the Retrieval: Poisoning Knowledge DBs to Mislead Embedding-based Search

- Decision: Reject
- Scores: 8, 6, 5, 5

## Abstract
Embedding-based text retrieval—retrieval of relevant passages from knowledge databases (KDBs) via deep learning encodings—has emerged as a powerful method attaining state-of-the-art search results and popularizing the use of Retrieval Augmented Generation (RAG). Still, like other search methods, embedding-based retrieval may be susceptible to search-engine optimization (SEO) attacks, where adversaries promote malicious content by introducing adversarial passages to KDBs. To faithfully assess the susceptibility of such systems to SEO, this work proposes the _GASLITE_ attack, a mathematically principled gradient-based search method for generating adversarial passages without relying on the KDB content or modifying the model. Notably,  _GASLITE_'s passages _(1)_ carry adversary-chosen information while _(2)_ achieving high retrieval ranking for a selected query distribution when inserted to KDBs. We extensively evaluated  _GASLITE_, testing it on nine advanced models and comparing it to three baselines under varied threat models, focusing on one well-suited for realistic adversaries targeting queries on a specific concept (e.g., a public figure). We found _GASLITE_ consistently outperformed baselines by $\ge$140\% success rate, in all settings. Particularly, adversaries using _GASLITE_ require minimal effort to manipulate search results—by injecting a negligible amount of adversarial passages ($\le$0.0001\% of the KDBs), they could make them visible in the top-10 results for 61-100\% of unseen concept-specific queries against most evaluated models. Among other contributions, our work also identifies several factors that may influence model susceptibility to SEO, including the embedding space's geometry. We will make our code publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces GASLITE, a novel adversarial attack strategy designed to exploit vulnerabilities in embedding-based text retrieval systems. By inserting adversarial passages into knowledge databases (KDBs), GASLITE aims to manipulate search results to favor malicious content being retrieved in the top results. The method employs a gradient-based search to craft passages that not only embed adversary-chosen information but also achieve high visibility in search results for a given query distribution when added to KDBs.

Key contributions include:
1. GASLITE effectively targets the practical challenges of embedding-based retrieval vulnerabilities, focusing on search-engine optimization (SEO) attacks, which aim to present adversarial content prominently in search results.
2. A detailed analysis of threat models and attacker capabilities, which provides a robust framework for understanding and assessing the vulnerabilities in embedding-based search systems.
3. The study conducts extensive empirical evaluations across multiple state-of-the-art retrieval models, demonstrating GASLITE's superior performance compared to previous methods at minimal poison rates. It also considers several baselines and novel threat models closely aligned with SEO goals.

### Strengths
1. The paper is generally well-written, with clear explanations of complex concepts such as the gradient-based optimization process.
2. The experimental design is robust, utilizing a diverse array of retrieval models and demonstrating GASLITE's efficacy across different scenarios. This thorough evaluation enhances the credibility of the results and underscores the method's practical relevance.
3. The paper demonstrates high success rates of the GASLITE attack across multiple retrieval models, achieving impressive results even at low poison rates. These results when compared to baselines are quite impressive and move the filed forward. The flexibility to add further constraints like fluency further demonstrates the effectiveness of the method.

### Weaknesses
1. The assumption of white-box access, while useful for theoretical exploration, might not fully align with real-world scenarios where such access is restricted. Discussing alternative practical attack vectors with limited access would strengthen the work's applicability insights. Most search engines of interest has proprietary models and the knowledge about open source models used in not available. It would be interesting to analyze how the poison passages found using one model generalizes to others.
2. While the paper convincingly demonstrates GASLITE's effectiveness, it lacks a detailed discussion on the method's scalability across larger datasets and systems, a factor crucial for understanding its operational feasibility in extensive real-world applications. Even when comparing with baselines, the runtimes of the systems are not compared. Often than not, the attackers have limited compute budget as well and hence discussing that aspect would have been helpful.

### Questions
1. Can you provide some analysis and comparison of time and resources required to perform these attacks and compare the same for the baselines?
2. Can you share more examples of the generated passages for other concepts than potter and sandwich, especially the ones with fluency constraints?
3. How does the method compare with summarizing the top 10 results for all the queries in the set. The examples on Potter looked like it generated main/popular keywords about Potter in the generated doc to boost its retrieval probability across the common queries.
4. In your selection of the seen and unseen queries for evaluation, do you take care of semantic similarity? If there is a huge overlap of semantic similarity between the train and test query set, it may not be that representative of the threat model.

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
This paper discusses the vulnerability of embedding-based text retrieval systems to search-engine optimization (SEO) attacks. The authors propose a gradient-based attack method called GASLITE, which generates adversarial passages to be inserted into knowledge databases (KDBs) in order to manipulate search results for specific queries or concepts. The attack aims to promote malicious content by ensuring that the adversarial passages rank highly for targeted query distributions without relying on the KDB content or modifying the retrieval model.

### Strengths
1. No need to update model parameters/additional training.
2. No need for read permission of KDB.
The method is better than the baseline method in both Knows All and Knows What scenarios. 
At the same time, |Padv| << |P|, and the position rate is less than or equal to 0.0001%. 
A small number of samples achieve the maximum SEO attack effect. 
It also analyzes various factors that affect the GASLITE attack method in this paper: similarity measurement methods, vector space characteristics of the Embedding model, diversity distribution of target Queries.

### Weaknesses
1. Computational Intensity: The GASLITE attack method is computationally intensive, especially for LLM-based embedding retriever, requiring significant resources, which may limit its scalability and practical application in certain scenarios. This computational demand could be a barrier for less resource-intensive environments or smaller-scale attacks. Specifically, the gradient calculations for each adversarial passage, especially with large language model embeddings, can be extremely costly in terms of both time and memory. This makes it challenging to apply the method to very large knowledge bases or in situations where rapid attack generation is needed.
2. Dependence on External Data: The effectiveness of the attack relies on the ability to generate or obtain a sample of queries related to the targeted concept. If the attacker cannot generate or obtain a representative sample, the attack's effectiveness may be diminished. The quality and diversity of the query sample directly impact the adversarial passages generated. If the query sample is biased or does not cover the full semantic space of the target concept, the resulting attack may be less effective or may not generalize well to unseen queries.
3. Impact of Tokenization: The paper acknowledges that the tokenization process can affect the attack's success, as certain token lists cannot be reached from any text. This implies that the attack's effectiveness is tied to the specific tokenizer used by the embedding model. This dependence on the tokenizer means that the adversarial passages are not necessarily robust across different tokenization schemes. The attack's effectiveness could vary significantly if the target retrieval system uses a different tokenizer than the one used to generate the adversarial passages.

### Questions
1. Why didn't embedding-based retrievers use models such as bge-en-icl 7kM, stella_en_1.5B_v5(1kM), gte-Qwen2-7B-instruct(7kM), and GritLM-7B(7kM)? 
2. How about the effect of these Embedding models with parameters of around 7000M?
3. Do you think there is a better form than info prefix + trigger for Padv?
4. How is the metric informativeness measured?
5. What if the embedding-based retriever is a black box model and we cannot obtain its weights parameters, how can we conduct this SEO attack ?

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
4

### Summary
This paper introduces the GASLITE, a poisoning attack targeting embedding-based text retrieval systems. The authors employ a gradient-based search method to craft adversarial passages, compelling the retriever to return information that the attacker intends to inject. Experimentally, GASLITE demonstrates significant superiority over other baselines across all settings, highlighting the heightened threat of poisoning attacks in text retrieval systems.

### Strengths
1. The authors conduct comprehensive experiments to validate the method's effectiveness. The experimental results indicate that GASLITE performs exceptionally well under three different knowledge conditions.
2. The writing is of high quality, and Figure 1 is clearly conveyed through the GASLITE workflow.
3. Given the widespread use of embedding-based text retrieval, focusing on its security is promising and meaningful.

### Weaknesses
1. My primary concern lies in the authors' assumptions. They assume that the attacker has white-box access to the embedding model, which significantly reduces the attack's practical applicability. Can the authors provide more real-world examples to support the hypothesis that attackers have such high-level access? Additionally, most current poisoning attacks assume black-box access for practical purposes. Can the authors explore how to implement poisoning attacks on text retrieval systems under black-box or gray-box conditions?

2. The method appears to be somewhat less innovative. How does a poisoning attack on text retrieval differ from other poisoning attacks on text data? Is the authors' method merely an adaptation of previous methods applied to text retrieval by modifying the attack algorithm's objective function? While I appreciate the list of improvements to the GASLITE algorithm in Section 4.2, these enhancements seem relatively minor.

3. The discussion of attacking text retrieval via KDB poisoning is too limited in the related work section. The authors should include more references that closely relate to their methodology. Additionally, the paper lacks discussion on defensive strategies and related experiments. For an emerging security issue, I am particularly interested in whether existing defense strategies can mitigate this risk.

4. Can the authors provide information on the time required to run the GASLITE algorithm? The authors mention in the limitations part that the white-box GASLITE algorithm is not very efficient, and constructing a black-box attack using zero-order gradient optimization may be more time-consuming. I would like to know whether attacking the text retrieval system in this context offers sufficient benefits.

### Questions
1. Design an attack algorithm under black-box or gray-box assumptions and provide the corresponding experimental results.
2. Include a discussion on attacking text retrieval via KDB poisoning and explore potential defense strategies.
3. Evaluate the time requirements of the attack method and assess its robustness when faced with defensive strategies.

### Soundness
2

### Presentation
3

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
The authors propose a gradient-based corpus poisoning attack for dense retrieval systems. They consider 3 threat models that incrementally weaken the adversary's assumptions about query knowledge: "knows all", "knows little", "knows (almost) nothing". They use "appeared@k" as a metric to measure attack effectiveness, and show that their attack method outperforms two naive, and one state-of-the-art baseline. They provide further analysis about the distribution of the embedding space.

### Strengths
1) The related work section has very good coverage
2) There is a clear connection between each threat model examined, and the experiment that corresponds to it
3) In their experiments, the authors examine a variety of models

### Weaknesses
1) The novelty of the paper is quite low, and I find it difficult to understand what is the difference between the author's method, and HotFlip. To me it seems that the experiments under different threat models are closely resembling the experiments of HotFlip, where in every threat model we have a different definition of what a query is allowed to be.
2) The authors use non-standard terminology for standard concepts. For example, they use "embedding-based retrieval" for "dense retrieval", or "knowledge database" for "corpus". Using standard terminology is a way to emphasize the novelty of your contribution. Meaning that it is not best practice to make the reader think "this method has never been applied to knowledge databases before", when in reality your knowledge database is just the MSMARCO corpus.
3) In their motivation, the authors emphasize that it is not always the case that SEO attacks have access to user queries. However, all of their threat models have query assumptions -- even the "knows (almost) nothing" experiment, where we still have queries. I believe that a trully queryless attack would help drive your point forward.
4) The authors choose to present the result of each experiment differently, i.e., the "knows all" experiment corresponds to Table 1, the "knows what" experiment corresponds to Figs. 3 and 4 (which are given in the wrong order in the paper), and the "knows (almost) nothing" references Table 8 (which is in the appendix), and  Fig. 5. In reality, I do not have a solid foundation to compare the performance of their algorithm across different threat models.
5) In Table 1, the authors show that their method has 100% success rate for appeared@1, which means that their adversarially generated passages, always outrank relevant passages. This is an extremely strong result, that is not sufficiently explained and discussed. I would like to see some qualitative analysis about what the generated passages look like compared to the relevant passages, and further explanation about why would their method achieve this strong of a performance.
6) "The perfect attack" section does not really fit well with the rest of the story, it reads like an afterthought that was introduced in the paper way too late. Perhaps the authors need to introduce the concept earlier, and ease the reader into why this experiment corresponds to their research objectives. At this point, when we reach Section 7.1, it feels out of topic.

### Questions
Please, refer to my detailed concerns in the "Weaknesses" section.

### Soundness
2

### Presentation
2

### Contribution
2
