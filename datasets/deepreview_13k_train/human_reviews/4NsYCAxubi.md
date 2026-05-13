# fPLSA: Learning Semantic Structures in Document Collections Using Foundation Models

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
\looseness=-1
Humans have the ability to learn new tasks by inferring high-level concepts from existing solutions, then manipulating these concepts in lieu of the raw data. Can we automate this process by deriving latent semantic structures in a document collection using foundation models? We introduce \codename, a foundation-model-based Probabilistic Latent Semantic Analysis (PLSA) method that iteratively clusters and tags document segments based on document-level contexts. These tags can be used to model the structure of given documents and for hierarchical sampling of new texts. Our experiments on story writing, math, and multi-step reasoning datasets demonstrate that \codename tags help reconstruct the original texts better than existing tagging methods. Moreover, when used for hierarchical sampling, \codename produces more diverse outputs with a higher likelihood of hitting the correct answer than direct sampling and hierarchical sampling with existing tagging methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the problem of discovering text segments that share common characteristics and assigning them the same tag description. It proposes an LLM-based method that iteratively assigns tags to document segments and improves each tag description based on the segment cluster. The authors aim to show that these tags are helpful for a reconstruction task and in improving “Hits@K” accuracy in evaluation sets created from WritingPrompts, MATH, and the BBH benchmark.

### Strengths
- This work proposes to discover “tags” for text segments in an unsupervised fashion and a novel algorithm that is inspired by the probabilistic latent semantic analysis (PLSA).
- The algorithm leverages the ability of an LLM to analyze textual materials and is able to find detailed and meaningful tags, as shown in the qualitative results of the paper.
- The paper show favorable empirical results compared to multiple baselines: traditional latent Dirichlet allocation, it variant + LLM, prompting, and chain-of-thought prompting.

### Weaknesses
1. The writing in this paper is often too generic and high-level. For example, when a reader reads the motivation at L011-L014 “Humans have the ability to learn new tasks by inferring high-level concepts from existing solutions, then manipulating these concepts in lieu of the raw data. Can we automate this process by deriving latent semantic structures in a document collection using foundation models?”, they may wonder: 
    - What tasks do you mean?
    - Existing solutions of the “new tasks” or other relevant tasks?
    - What does it mean to manipulate high-level concepts?
    - How do you define “semantic structures” in a document collection? It’s not precise to describe a set of “tags” as a structure.
2. The novelty of the method is limited and its connection to PLSA and EM is loose. The proposed algorithm is simple: (1) Initialize a certain number of tag descriptions. (2) Prompt an LLM to assign a tag to each document segmentation based on the tag descriptions. (3) Let an LLM generate a new tag description that describes the shared characteristics of the segments in this cluster.
    - The main Eq. (4) is actually not used: $p(d)$, $p(x_k|d)$,  $p_\Theta(t|x_k,d)$, and $p_\Theta(w_{1\dots n}|t)$ are not computed.
    - L153: The parameters $\theta_t$ are textual descriptions instead of floating-point parameters and no training is happening.
    - L157: No probability distribution is involved. An LLM is employed to greedily perform the steps in the algorithm.
    - PLSA is a generative model of the training documents that it is estimated on, and it is not a generative model of new documents. But this paper aims to find tags that apply to unseen examples.
3. While the convergence criteria matters for an EM algorithm, this paper simply sets the number of iteration to 30. Not enough analyses is perform on the impact of the number of iterations.
4. In the reconstruction experiments the method based on learned tags solves a multiple choice problem of picking the ground truth $x_k$ from a set of candidate segments. However, baselines such as prompting in Eq. (7) requires a language model to generate the ground truth $x_k$. These seem not comparable.
5. Although the experiment results are positive compared to the baselines, the setups are synthetic. Would be nice to see the application of this algorithm to achieve competitive results according to standard evaluation metrics of the used datasets, which are common benchmarks.
6. Many details are missing. See the Questions below.

### Questions
1. What prompt templates are used in various experiments?
2. How are the textual descriptions $\theta_t$ initialized in the algorithm? How can the initial tag descriptions meaningfully be assigned to the segments?
3. Sec 4.1 Evaluation Datasets: How do you convert the input query and the output answer of each example into segments? Do you learn tags only for segments of answers, but not queries/prompts/questions?
4. Sect 4.1: This is titled Evaluation Datasets but indeed describes data for clustering and tagging.
5. L195: How do you sample alternative segments?
6. L188: What do you mean by the test documents? The datasets are query-answer examples.
7. In the Hits@K evaluation:
(a) Do you first generate the tag sequence based on the input of a test example or randomly? 
(b) Does a model predict an answer based on the tag sequence in one prompting call?
(c) How do you evaluate if a sampled solution is correct or not?
(d) Why do you say the proposed algorithm improves diversity in outputs, which is not evaluated? In fact, diversity is neither necessary nor sufficient for a model to perform a reasoning task well.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces an improved version of probabilistic Latent Semantic Analysis (pLSA), termed fPLSA (Foundation-Model-Based PLSA), which incorporates Large Language Models (LLMs) to refine the modeling of latent tags in documents for topic modeling. It conducts some experiments to verify the effectiveness of fPLSA.

### Strengths
(1) Study a classic task

(2) Propose a new method

(3) conduct some experiments to verify the effectiveness of the proposed method.

### Weaknesses
(1) Insufficient technical contribution: The method utilizes LLMs for tag Description Generation. Specifically, the fPLSA model  generates descriptive tags for the document segments by prompting the LLM with segments assigned to a particular tag to produce a cohesive summary that represents what these segments have in common. The parameters of the LLM are kept frozen during the process. This means the LLM is not fine-tuned during fPLSA training but is used in a static manner. While the integration of LLMs into pLSA offers a novel approach to document modeling, the core statistical methodologies underlying pLSA (like the EM algorithm) remain largely unchanged. This limited modification of the underlying statistical framework of pLSA, despite the incorporation of LLMs, raises concerns about the depth of the technical contribution. The method essentially uses LLMs as a feature engineering step rather than fundamentally altering the topic modeling process itself.

(2) Missing necessary experiments: need to involving more baselines that use LLMs for topic modeling, like Pham et al. (2024), Wang et al. (2023) mentioned in the paper. 

(3) Poor writing: The transition of some contents are abrupt and hard to readers to understand the points, such as the first and second  paragraphs in the introduction.

(4) Missing Implementation Details: all the prompts used in the experiment are not specified such as those for fPLSA and GenOutline (a baseline)

(5) Unclear motivation of the experiment setting: the paper uses GPT-4 for clustering and tagging  while using ChatGPT to measure the accuracy. The authors explain it’s because GPT-4 may have data contamination issues on some benchmarks. I think this explanation is lame and need more clarifications while potentially leading to unfair comparison.

### Questions
please refer to the weaknesses

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
2

### Summary
The paper introduces fPLSA (foundation-model-based Probabilistic Latent Semantic Analysis), a novel approach for identifying latent semantic structures in document collections by combining traditional PLSA with the contextual understanding of large language models (LLMs). fPLSA enhances probabilistic clustering and unsupervised topic modeling by assigning semantic "tags" to document segments through an iterative Expectation-Maximization (EM) process, where each tag captures both local meaning and broader document context. This structured tagging approach enables fPLSA to better capture complex segment relationships, making it valuable for hierarchical sampling, document analysis, and potentially other downstream tasks such as structured summarization. The paper demonstrates fPLSA’s effectiveness across diverse datasets—narrative (story writing), problem-solving (math), and multi-step reasoning—showing improvements in text reconstruction likelihood and Hits@K accuracy, underscoring its robustness and versatility.

### Strengths
- **Innovative Approach:** fPLSA is a well-conceived combination of probabilistic topic modeling and LLM-based embedding, creating a tagging system that captures both low- and high-level semantics. This approach enables a nuanced understanding of document structure that extends beyond traditional methods, addressing complex relationships within text segments.
- **Diverse Evaluation:** The method is rigorously evaluated across multiple datasets, including narrative, mathematical, and multi-step reasoning tasks, demonstrating consistent performance improvements in text reconstruction and sampling diversity. This diversity in datasets reinforces the robustness and generalizability of the approach.
- **Potential for Cross-Domain Applications:** fPLSA’s ability to structure and tag text meaningfully is a powerful tool for hierarchical content generation, segmentation, and structured summarization, with substantial applications across various domains, such as education, content generation, information retrieval, and summarization.
- **Foundation for Future Research in Unsupervised Document Tagging:** fPLSA provides a strong foundation for future work in unsupervised document tagging and text segmentation. Its hierarchical tagging approach encourages further exploration in transfer learning, document summarization, and adaptive segmentation, inspiring new research directions for improved document understanding and organization.

### Weaknesses
 - **Single-Document Applicability:** fPLSA heavily relies on cross-document patterns during training, which is not fully addressed in terms of single-document use cases. At test time, users often only have one document. It would be beneficial to clarify how fPLSA’s pre-trained tags would generalize to individual documents without access to cross-document patterns. For instance, can the model effectively apply pre-learned tags from similar training data to new documents? Specifically, the paper lacks a discussion on the potential degradation in tag quality when the test document's content or structure diverges significantly from the training corpus. This is a critical gap, as the effectiveness of the learned tags is predicated on the assumption that test documents share similar underlying semantic structures with the training data.
- **Lack of Efficiency Analysis:** Given fPLSA’s reliance on LLMs, a discussion on computational efficiency would be valuable. While LLMs are powerful, they are computationally expensive. Addressing the practical feasibility of deploying fPLSA at scale (or proposing more efficient variations) would make the paper’s findings more actionable. The paper should include a detailed analysis of the computational resources required for both training and inference, including memory consumption and processing time, especially when dealing with large document collections. This analysis is essential for assessing the scalability of the proposed approach.
- **Potential LLM Biases:** Since fPLSA uses pre-trained LLMs to assign tags, there is a risk of encoding biases from the LLM's training data into the tags. The authors could explore ways to mitigate or assess the impact of these biases, especially for datasets or domains sensitive to fairness and accuracy. The paper should include a discussion on how the choice of LLM might affect the semantic tags and whether specific mitigation strategies are needed to ensure that the tags are not skewed by the LLM’s inherent biases. This is particularly important when dealing with sensitive topics or datasets where fairness is a concern.
- **Segmentation Granularity:** The paper does not discuss how sensitive fPLSA is to the choice of segment granularity (e.g., sentence, paragraph) and whether different segmentation approaches yield more cohesive or meaningful tags. Further examination of this could provide clarity on best practices for applying fPLSA across different document types and tasks. The paper should explore the impact of different segment sizes on the quality of the learned tags and provide guidelines for selecting appropriate segment granularity based on the characteristics of the document and the task at hand. This analysis is crucial for optimizing the performance of fPLSA across diverse applications.
- **Potential for Downstream Applications:** Although the paper’s results demonstrate fPLSA’s effectiveness in hierarchical sampling, the model's broader potential in downstream tasks is not explored. Given the rich, hierarchical nature of fPLSA tags, they could be valuable for applications like multi-level text summarization, where each tag could represent a theme or section for summarization. Exploring these applications would broaden fPLSA’s impact.

### Questions
- How would fPLSA perform when applied to a single document at test time, especially if that document differs significantly in structure or content from the training set? Can pre-learned tags from similar training data reliably generalize to new documents in such cases, or would fine-tuning on representative samples be necessary to improve performance?
- Given fPLSA’s structured tagging capabilities, could the authors discuss its applicability to downstream tasks like structured text summarization and content retrieval? Prior research on text summarization with text segmentation has demonstrated that segmenting texts by themes can enhance summarization quality [1]. Could fPLSA’s tags be similarly used to segment and summarize each thematic section, creating a coherent multi-level summary? Additionally, might these tags support content retrieval or indexing by allowing documents to be searchable by thematic segments? Including a brief paragraph on such applications could highlight the contribution's versatility.
- Can the authors provide insights into fPLSA’s computational cost compared to the baselines? For instance, would a less resource-intensive model (like a smaller language model) yield competitive results without the same computational burden?
- How sensitive is fPLSA to the choice of segment granularity (sentence, paragraph, etc.)? In testing, did certain segmentation approaches yield more cohesive or meaningful tags, and if so, could the authors elaborate?
- Since pre-trained LLMs may encode biases, did the authors observe any potential bias issues during fPLSA’s tagging process? If so, what mitigation strategies might they recommend for fair and balanced tag generation?

**References**
1. Semantic Self-Segmentation for Abstractive Summarization of Long Documents in Low-Resource Regimes. AAAI 2022.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
### [Updates 12/04/2024]
To anyone reading the reviews: The authors published all their responses in the final hours of the rebuttal period (midnight EST). When I tried to respond just now, I realized I can no longer make my response public, so I'm updating my official review here. To clarify, **it was the authors who did not engage during the rebuttal period, not the reviewers**.

### Original Content
The paper introduces fPLSA, a foundation-model-based extension of Probabilistic Latent Semantic Analysis (PLSA), aimed at discovering semantic structures within document collections through clustering and tagging of text segments. Unlike traditional topic modeling, which often relies on word co-occurrences, fPLSA leverages Large Language Models (LLMs) to understand segment-level semantics in a broader document context. It applies an Expectation-Maximization (EM) algorithm to iteratively refine segment tags, enhancing both text reconstruction accuracy and hierarchical sampling. Experimental results on datasets for story writing, math, and reasoning show that fPLSA significantly outperforms traditional and LLM-based tagging methods in text reconstruction and solution diversity. This makes it suitable for generating effective problem-solving guides and diverse text outputs across varied tasks.

### Strengths
The article is generally well-written except for the technical part, which I find somewhat confusing. According to the article, fPLSA's strengths lie in its enhanced semantic understanding, leveraging LLMs for capturing nuanced document structures beyond lexical co-occurrence. This approach yields more accurate text reconstruction and supports hierarchical sampling, producing diverse, high-quality outputs in applications like story generation and problem-solving. Its specific and detailed tagging outperforms generic LLM-based tags, enhancing content generation. Additionally, fPLSA’s unsupervised clustering reduces the need for labeled data, while its demonstrated adaptability across domains and improved Hits@K accuracy make it a versatile, efficient tool for semantic analysis and structured text generation.

### Weaknesses
- The usage of math symbols is sometimes confusing. Also not required, it is suggested that the authors follow the [default notation](https://github.com/ICLR/Master-Template/raw/master/iclr2025.zip) for a clearer presentation of the equations.

- The proposed method is not thoroughly explained. For example, the computation of some terms in (4) is missing, as well as its optimization algorithm, e.g., how to calculate $p(x_k|d)$. From my perspective, if one chooses to express the idea using math formulas, then every term should be clearly explained except for the cases where it is extremely obvious, which I think does not apply to (4).

- A figure or algorithm may better explain the proposed method.

- The authors use GPT-4 for clustering and tagging but GPT-3.5 for response generation and did not provide experimental results on other combinations. The performance of the proposed method therefore may not be universally applicable.

-  Potential data leakage issues (detailed in Questions).

- The explanation of how $p(x_k|d)$ is modeled is unclear. It is not sufficient to say that a segment is randomly sampled; the underlying distribution and sampling process need to be explicitly defined. The lack of clarity here makes it difficult to assess the validity of the approach.

- The context window mechanism is not well-defined. While the authors mention using a context window of 2 or an unlimited context window, the exact implementation and impact of these choices on the model's performance are not clear. Specifically, how the model handles the unlimited context window and whether it leads to any computational or performance issues should be addressed.

- The nature of the tags as natural language descriptions rather than categorical labels raises concerns about the appropriateness of calling them 'latent variables' in the context of PLSA. The connection between these descriptive tags and the probabilistic framework of PLSA is not clearly established, and the authors should clarify how these tags are integrated into the model's probabilistic calculations.

- The sampling of $t_k$ conditioned on $x_k$ in (5), which is then used to estimate the probability of reconstructing $x_k$, introduces a potential data leakage issue. This setup seems to use the target variable in the prediction process, which could lead to inflated performance metrics and an inaccurate assessment of the model's generalization ability.

- The use of step-by-step solutions from the training set for clustering and tagging in the BBH dataset raises significant concerns about data leakage. This approach could lead to the model learning to reproduce known solutions rather than generalizing to new problems, thus undermining the validity of the evaluation.

### Questions
- I'm a bit confused by the relation between w, x, and d. If $w_{1:n}=x_k\subset d$, how is $p(x_k|d)$ modeled in (4)? Why is it necessary to include both $x_k$ and $d$ as conditional terms?

- Context window: I'm not sure I understand how the segments are selected in this article. Is a segment a fixed-length sequence of tokens? Are there any overlaps between different segments? In Line 238, the authors mentioned "we use a context window size of 2 on WritingPrompts and use unlimited context window". How should the "unlimited context window" be interpreted?

- According to [1], the latent variable ($z$ in [1]) is supposed to be categorical. This article borrowed the same concept from [1] but I'm not sure whether this article follows the original setup. The authors did mention that they "set the number of tags to 100", but the example tags in Table 3 showed that the tags are natural language descriptions rather than categorical labels. I wonder how the tags are generated, and if calling it "latent" is still appropriate.

- In (5), $t_k$ is sampled condition on $x_k$, which is later used to estimate the probability of reconstructing $x_k$. Is this a typo? Doesn't this lead to data leakage and make the results of (5) unfairly high?

- For BBH, I'm not sure why it is necessary to "use the step-by-step solutions produced by their automatic Chain-of-Thought
prompt inference algorithm for clustering and tagging". Does it mean that a part of the (ground-truth) solutions is utilized as the prompt to the model for problem-solving? I think this is a huge data leakage issue and would greatly undermine the soundness of the evaluation of the proposed method.

- Since tag generation is a recursive process, what would the token consumption be for achieving the presented results? How about the baseline models?

[1] Hofmann, T. "Probabilistic latent semantic indexing." Proceedings of the 22nd annual international ACM SIGIR conference on Research and development in information retrieval. 1999.

### Soundness
2

### Presentation
1

### Contribution
2
