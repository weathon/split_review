## Human Reviewer 1

### Summary
This paper proposes AMADEUS, a training-free RAG framework for role-playing agents that emphasizes persona consistency. It consists of three modules: 1. ACTS (chunking with hierarchical context), 2. GS (LLM-guided gating for personality-rich context), and 3. AE (extraction of beliefs, values, and psychological traits). The authors introduce a new dataset, CharacterRAG, covering 15 anime/game characters with ~976K tokens and 450 QA items, and evaluate consistency using MBTI and BFI personality metrics.

### Strengths
- Interesting Setup: Role-playing agents with persona tracking is a novel and popular topic.

- Clear Modular Design: The ACTS → GS → AE pipeline is well-structured and has potential use in other structured attribute extraction tasks.

- New Benchmark: The authors created a sizable benchmark dataset (CharacterRAG), which could contribute to future research in character-centric modeling.

### Weaknesses
- Problem Framing – RAG for Personality?
The core task is framed around personality extraction and preservation, which is arguably not well-justified as a role for RAG. Personality is a stable trait, and might be better handled by LLM summarization over full context rather than partial retrieval.

- Evaluation Scope Too Narrow
The evaluation overly focuses on MBTI/BFI-style tests. This does not show if the system performs well in downstream tasks (e.g., in-character QA, stylistic imitation). Also, no evidence is given that this personality focus doesn't degrade performance on other tasks.

- MBTI as Ground Truth?
The paper does not clarify how ground-truth MBTI labels are obtained or validated. Are these canonical? Are there characters with ambiguous or contradictory traits across works?

- Overloaded Character Set
Including 15 characters is impressive but risks overwhelming the reader. It would help to narrow the benchmark or focus deeply on 1–2 characters (e.g., Hirasawa Yui) with full backstory and qualitative insights.

- Lack of Ablation Analysis
No ablations are shown to measure the contributions of ACTS, GS, or AE. In particular, the GS module performs LLM-based reranking—this is a strong boost and may unfairly outperform pure retrieval baselines, confounding the comparisons.

### Questions
Why did you choose RAG over LLM summarization for trait extraction, given that personality is a global/stable attribute rather than local/contextual?

How are MBTI ground truths assigned? Are they consensus-based? Are inter-annotator agreements or soft labels considered?

Have you measured whether the AE module introduces hallucinated or speculative traits, especially when context is ambiguous?

What downstream tasks (other than personality QA) can benefit from your pipeline? Could your approach generalize to style transfer or dynamic response generation?

Could you show results using a smaller character subset with detailed breakdowns to improve interpretability?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper investigates RAG-based role-playing agents, which aim to answer user queries using information retrieved from persona documents. The authors propose a new retrieval framework specifically designed for hierarchically structured persona documents, consisting of three key components: Adaptive Context-aware Text Splitter (ACTS), Guided Selection (GS), and an Attribute Extractor.

The ACTS module segments text into overlapping chunks while prepending contextual information from parent nodes within the hierarchical structure to each chunk. The GS component filters these chunks by prompting an LLM to verify whether the correct persona information can be inferred from each chunk. Attribute Extractor extracts psychological traits and value/belief-related attributes from the selected text segments.

The authors construct a self-collected dataset named CharacterRAG, containing 15 distinct characters and 450 question–answer pairs. Their experiments are conducted on this dataset.

### Strengths
i. This paper's attempt to improve the retrieval accuracy of persona information for RAG-based role-playing agents is meaningful. 

ii. The collection of a new dataset demonstrates the authors’ effort to empirically explore this problem and provides a potential resource for future studies.

### Weaknesses
i. The paper is poorly written, and many essential details are missing, which makes it difficult to fully understand and reproduce the proposed approach.

- The description of the CharacterRAG dataset construction process lacks sufficient detail. It is unclear how the persona documents were collected and processed, how the 450 QA pairs were generated, and what standards were used to filter unqualified documents. Furthermore, the authors do not discuss any measures taken to ensure the fidelity and correctness of the dataset. Since all experiments rely entirely on this dataset, these details are critical to ensure the fairness and reliability of the results.

- The method descriptions are confusing and incomplete. The paper claims that the Adaptive Context-aware Text Splitter (ACTS) divides text into optimally sized and overlapping chunks; however, Section 4.1 provides no information on how the optimal chunk length is determined or how the overlap is implemented. Similarly, in Section 4.2 (Guided Selection), the details of the LLM prompting process are missing — including how the prompt templates are constructed and how the model’s responses are evaluated or extracted. In Section 4.3 (Attribute Extractor), the authors only explain why and what attributes are extracted, but fail to specify how the extraction is actually performed.

- According to Section 5.2, Table 4 appears to present the main experimental results. However, both the table and its corresponding analysis are placed later in Section 5.3, which disrupts the logical flow of the paper and makes the structure somewhat confusing.

- In Figure 1, the authors do not explain how the chunk duplication frequencies and chunk usage rates are computed, which makes the figure difficult to interpret. In addition, the text in Figures 1 and 2 is too small to read clearly.

- Figure 5 is mislabeled and should actually be Table 5.

ii. The proposed method appears to be highly tailored to the CharacterRAG dataset. The ACTS component relies on the dataset’s hierarchical structure, while the Attribute Extractor is built upon its predefined attribute taxonomy. As a result, the method may lack scalability and generalizability to other datasets or real-world scenarios. Moreover, comparing this approach with other methods on CharacterRAG may not provide a fair evaluation of its effectiveness.

iii. Guided Selection (GS) relies on LLM to filter chunks, computationally expensive and impractical for large-scale persona documents.

iv. In the main experiments presented in Table 4, despite the dataset-specific design efforts, the improvement over the baseline naive RAG model is marginal, which makes the overall contribution appear limited. Although the proposed method performs relatively well on tasks related to MBTI and BFI, the Guided Selection (GS) component explicitly extracts MBTI- and BFI-related attributes (with the implementation details remaining unclear). Therefore, it is unsurprising that the method outperforms the naive RAG under these conditions.

### Questions
see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper tackles hallucination and weak persona consistency in RAG-based role-playing agents (RPAs) when handling queries outside a character’s knowledge, proposing AMADEUS, a training-free framework. AMADEUS includes three key modules: Adaptive Context-aware Text Splitter (ACTS) for hierarchical context-enhanced persona chunking, Guided Selection (GS) for attribute-relevant chunk retrieval, and Attribute Extractor (AE) for key character attribute extraction to sustain consistency. The authors also build CharacterRAG, a dataset with 15 fictional characters’ persona documents (976K characters) and 450 QA pairs, filling the gap of RAG-based RPA-specific evaluation resources. Experiments against baselines (Naive RAG, CRAG, LightRAG) on multiple LLMs demonstrate AMADEUS outperforms others in both in-knowledge and out-of-knowledge scenarios, lowering hallucination and boosting consistency.

### Strengths
1. AMADEUS (with ACTS, GS, AE modules) fixes RAG-based RPAs’ hallucinations and poor persona consistency in out-of-knowledge queries, outperforming traditional RAG by enhancing chunking, filtering, and attribute extraction.  

2. The manually built CharacterRAG (15 characters, 976K chars, 450 QAs) removes interference (e.g., editor’s inferences) and fills the lack of dedicated RAG-based RPA evaluation resources.  

3.  Using 3 LLMs, 3 embedding models, 3 baselines, and covering in/out-of-knowledge scenarios, experiments combine quantitative metrics (ACC, HS) and human evaluation (Cronbach’s α > 0.8) for credible results.

### Weaknesses
1. The CharacterRAG dataset includes 15 fictional characters, but the paper does not specify their genre (e.g., anime, novel, film) or personality span (e.g., introverted vs. extroverted, heroic vs. villainous). If characters are concentrated in a single genre or share similar traits, the framework’s generalization to diverse role-playing scenarios (e.g., classical novel characters) remains unvalidated.  

2. The Attribute Extractor (AE) only extracts "Belief and Value" and "Psychological Traits," claiming they "directly influence behavior". But it does not explain why other attributes (e.g., "Social Relationships" or "Skill and Expertise," which also shape role responses) are excluded, nor provide comparative experiments to prove these two attributes are more critical for persona consistency. Is it specific to tasks like MBTI and BFI?

3. The evaluation dataset is incomplete. The paper only evaluates tasks like MBTI and BFI, but role-playing involves many other dimensions. Is the method applicable to other role-playing tasks? For example, imitating a character's linguistic style or simulating a character's behavior.

### Questions
1. How is L_max set?
2. Why can finding the information of the k most similar chunks solve problems that are beyond the scope of the character's knowledge?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes a training-free RAG framework for role-playing agents that targets persona consistency even when user queries fall outside a character’s explicit knowledge. The apporoach has three stages: (1) Adaptive Context-aware Text Splitter creates optimally sized, overlapping chunks annotated with hierarchical headings; (2) Guided Selection iteratively filters retrieved chunks using an LLM to prefer passages from which traits can be inferred; and (3) Attribute Extractor derives beliefs/values and Psychological Traits from the selected chunks and feeds them as final context for response generation. The authors also release CharacterRAG, a 15-character, 976K-char persona corpus with 450 QA pairs. Experiments across close-source or open-source models report higher accuracy and lower hallucination scores than RAG baselines, and  human raters find attributions reasonable

### Strengths
The paper explicitly targets a common failure mode in RAG-based role-playing: when a user asks about aspects that are not explicitly in the persona, vanilla retrievers overuse low-relevance chunks and the agent hallucinates. The abstract and introduction motivate this crisply and position AMADEUS as training-free with three modules.

ACTS preserves hierarchical context with empirical support that maximizes summed similarity and minimizes variance; ACTS/ATS outperform standard splitters across embeddings. 

CharacterRAG contains 15 fictional characters (976k characters) and 450 QA pairs with six attribute categories, constructed from the character’s viewpoint (editorial/meta information removed). This fills a gap for RAG-based RPAs. AMADEUS improves stronger performances.

### Weaknesses
CharacterRAG contains only 15 fictional characters, and much of the persona content is mined from Namuwiki; it remains unclear how well findings transfer to real people, evolving personas. Adding non-fictional or time-varying personas would strengthen claims.

While ACTS’s hierarchical extraction cost is noted (O(N)), the end-to-end latency and token/dollar costs (especially for GS/AE with large models) are not reported in detail across LLMs/datasets, limiting deployment guidance.

The related work should cover several fast-moving threads which is missing: (i) LongRAG’s long-unit/long-reader paradigm that challenges short-chunk assumptions; also add RankRAG, which unifies reranking with generation and is conceptually close to your Guided Selection. (ii) Role-playing/persona literature: evaluation benchmarks (CharacterEval; RoleLLM; InCharacter and a non-RAG), Non-RAG persona models (Persona-Adaptive Attention). 

The w/o-RAG baseline shows non-trivial background knowledge, but the paper does not deeply analyze how much persona knowledge the base LLMs already encode or how AE/GS ablations isolate gains beyond retrieval.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4