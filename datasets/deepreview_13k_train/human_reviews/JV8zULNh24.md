# From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Recent reasoning methods (e.g., chain-of-thought, entailment reasoning) help users understand how language models (LMs) answer a single question, but they do little to reveal the LM’s _overall understanding_, or “theory”, about the question’s _topic_, making it still hard to trust the model. Our goal is to materialize such theories - here called _microtheories_ (a linguistic analog of logical microtheories (Blair et al., 1992)) - as a set of sentences encapsulating an LM’s core knowledge about a topic. These statements systematically work together to entail answers to a _set_ of questions to both engender trust and improve performance. Our approach is to first populate a knowledge store with (model-generated) sentences that entail answers to training questions, and then distill those down to a core microtheory which is concise, general, and non-redundant. We show that, when added to a general corpus (e.g., Wikipedia), microtheories can supply critical, topical information not necessarily present in the corpus, improving both a model’s ability to ground its answers to verifiable knowledge (i.e., show how answers are systematically entailed by documents in the corpus, fully grounding up to +8% more answers), and the accuracy of those grounded answers (up to +8% absolute). We also show that, in a human evaluation in the medical domain, our distilled microtheories contain a significantly higher concentration of topically critical facts than the non-distilled knowledge store. Finally, we show we can quantify the coverage of a microtheory for a topic (characterized by a dataset) using a notion of _p-relevance_. Together, these suggest that microtheories are an efficient distillation of an LM’s topic-relevant knowledge, that they can usefully augment existing corpora, and can provide both performance gains and an interpretable, verifiable window into the model’s knowledge of a topic.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach to enhancing question-answering systems by distilling a model's topical knowledge into what the authors term "microtheories." The method involves generating a set of simple, logical facts about the world, which are used to construct entailment chains that support the answering of complex queries. The paper emphasizes the importance of creating relevant and context-specific facts, which can be either generic statements about the world or specific assertions that aid in proving a particular query. The authors introduce a system that generates query statements for each possible answer to a question, ensuring these queries align closely with the answer choices. The effectiveness of this approach is evaluated through expert-annotated task relevance scores, demonstrating that microtheory-based facts are more relevant than random or usage-based facts, particularly when constrained by a fact budget. This work aims to improve the reasoning capabilities of AI systems by providing a structured framework for knowledge representation and retrieval, ultimately leading to more accurate and grounded question answering.

### Strengths
1. The paper presents a novel concept of generating microtheories from models. By utilizing advanced models like GPT-4 and Mixtral-8x22B-Instruct-v0.1, the authors demonstrate a robust approach that is not dependent on a single closed model. This flexibility and innovation in methodology can potentially lead to more accurate and contextually relevant answers in reasoning tasks.

2. Comprehensive evaluation. This thorough evaluation process ensures that the proposed method is not only theoretically sound but also practically effective on three domains. The focus on optimizing microtheory contents given a size budget highlights the paper's attention to practical constraints and efficiency, making it a valuable contribution to the field.

### Weaknesses
- Line 74: The *entailment* in NLP typically is typically referred to as textual entailment, which surely has a formal [definition](https://en.wikipedia.org/wiki/Entailment_(linguistics)). 
- Line 160-161, the method that you extract is using LLM prompting. The problem is, what's the inherent difference of your method compared to chain/tree/graph-of-thought, since you are both distilling knowledge from LLM as intermediate steps. I get it that you used the tricks like entailment consolidation to filter some meaningful microtheories, but there are many existing works focusing on filtering intermediate thoughts or supporting facts to facilitate CoT, which limits the novelty of your work.

### Questions
1. How is the *grounding* metric in section 5.1 calculated in detail?
2. How do you detach the improvements brought by *microtheory* and that possibly brought by seemingly useful LLM-generated chain-of-thought?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a framework of distilling a model’s knowledge of a certain scientific topic into an inspectable, verifiable form of microtheories, and shows that adding microtheories in the original corpus improves entailment engine performance.

### Strengths
1. The paper addresses an important problem of distilling a model’s knowledge of a certain topic into an inspectable, verifiable form
2. The method proposed by the paper can extract facts that are deemed as critically relevant by human experts
3. The distilled facts are helpful for entailment engines to perform QA tasks

### Weaknesses
1. The format of the input to the entailment engine is unclear. The engine takes in a mixture of original corpus such as Wikipedia and microtheories, but how these external information is structured is not clear.
2. The claim "Mt size correlates with QA accuracy" in Section 5.2 seems to be an overstatement, as the authors only show three bins (100, 500, 1000).
3. The fact that only adding more than 1000 facts can increase QA performance shows that current microtheory selection is unable to get the most relevant facts. In addition, 5000/8000 of facts for both datasets are never used in the proof. The authors should discuss 1) why it's happening and 2) the compute needed to retrieve a large enough fact corpus to improve QA performance, and the trade off between selection comprehensiveness and QA performance.
4. Although the paper claims to generate microtheory from both GPT4 and Mixtral to show that their method not only works on closed models, there's no comparison of performance and discussion on how different models may affect microtheory generation. The paper also does not explain why they use GPT4 for ARC and Mixtral for MedQA.
5. Section 5.3 uses "relevance" as a metric to evaluate how the microtheory building process is indeed extracting the more important, central facts about the topic. This is a mismatch: relevant information may not be selected by the entailment engine or really used by the QA model. The authors need to add another experiment on how many facts in the microtheory is used by the entailment engine, or use causal metrics like influence function to show true causality that certain facts are indeed used by the QA model in answers.

### Questions
1. I am confused about the "training questions", do you mean questions in the original training set of ARC and MedQA? Also, the word "training" appeared in this paper so many times in different contexts, "training questions" "training hypothesis" "training set" "training proofs"... but it seems like you are not training the QA module at all?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a method for transforming a model's latent topical knowledge into a microtheories, encapsulating reusable knowledge about a topic. The authors also conducted evaluations demonstrating that, when incorporated into the general corpus, microtheories significantly enhance the model's grounding ability in its answers.

### Strengths
1. The paper proposes an innovative approach to distill microtheories from a model, that aritculates the model's core knowledge about the dataset's topic.
2. The author conducted comprehensive evaluations, including human evaluation to show that the microtheories can both improve the model's ability to ground its answer and improve accuracy.

### Weaknesses
1. Dependence on Training Questions and Answer Options: The method relies heavily on a pre-existing set of training questions and answer options to generate microtheories such as ARC. This dependency restricts its applicability to new corpora that lack such structured data, making the approach challenging to transfer across domains or to corpora where questions and answers aren't predefined.

2. The paper could indeed improve by including more details on the filtering process in Section 3.2.2. Specifically, it doesn’t clarify how many microtheories were ultimately filtered out after applying the redundancy reduction techniques.

### Questions
1. In Figure 7, adding 10 random microtheories to the base corpus could make the performance drops a lot, could you please explain it?

2. See weakness 2

### Soundness
3

### Presentation
3

### Contribution
3
