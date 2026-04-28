# JustLogic: A benchmark for natural language deductive reasoning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Logical reasoning is a critical component of Large Language Models (LLMs), and substantial research efforts in recent years have aimed to enhance their deductive capabilities. However, existing deductive reasoning benchmarks, which are crucial for evaluating and advancing LLMs, are inadequate due to their lack of task complexity, presence of prior knowledge as a confounder, and superficial error analysis. To address these deficiencies, we introduce JustLogic, a synthetically generated deductive reasoning benchmark designed for rigorous evaluation of LLMs. JustLogic is (i) highly complex, capable of generating a diverse range of linguistic patterns, vocabulary, and argument structures; (ii) context-independent, eliminating the advantage of models possessing prior knowledge and ensuring that only deductive reasoning is used to answer questions; and (iii) capable of in-depth error analysis on the heterogeneous effects of reasoning depth and argument form on model accuracy. Our experimental results on JustLogic reveal that the performance of most state-of-the-art (SOTA) LLMs, specifically Llama3-8B (57.8\%), Llama3-70B (64.6\%), and GPT-4o (65.6\%), is significantly worse than the average human performance (73.0\%). A recently released reasoning model, OpenAI o1-preview, performed substantially better, with an accuracy of 81.0\%. However, it still lags behind the human ceiling of 100.0\%. These results demonstrate that the JustLogic benchmark is realistic and achievable for both humans and models and that there is still substantial room for improvement in the deductive reasoning capabilities of LLMs. We posit that the use of context-dependent and relatively simplistic benchmarks has misrepresented the reasoning abilities of many SOTA models. We release our open-source dataset to provide accurate evaluations of model performance in deductive reasoning and to facilitate LLM advancement through in-depth error analysis.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces JustLogic, a benchmark designed to test LLMs' deductive reasoning without the bias of prior knowledge. It highlights the shortcomings of the exitsting logical benchmarks based on complexity and error analysis -- showing some of the sythetic datasets, while may not rely on prior knowledge, are not complex enough. Other datasets, are complex but may be solve using prior human knowledge. Authors curate a large number of logical derivations, using a mix of LLM and human generated templates and propositions from GenericsKB, authors create a logical benchmark, which is synthetic, (possibly) not true in the real world and complex.  Despite improved performance by models like OpenAI o1-preview, they still lag behind human reasoning. JustLogic aims to drive deeper evaluation and enhancement of LLM capabilities.

### Strengths
1. The paper highlights flaws in current reasoning benchmarks: low complexity, prior knowledge dependence, and limited error analysis.
2. It addresses the flaws highlighted in point 1 while constructing the new dataset JustLogic that have been unaddressed in datasets like FOLIO, ProofWriter, etc.
3. The solution to the flaws like focusing on argument complexity and Prior knowledge independence looks interesting.
4. Very minimal manual effort is required to construct the dataset.

Authors also aspire to make it more future-proof by leveraging synthetic creation abilities.

### Weaknesses
1. There are several points which are claimed but do not have enough justification, for example, it may not be naturally true that a "conclusion" is untrue in the real world just because it is synthetic. No effort have been made to enforce factual inaccuracies -- they should also compare with PrOntoQA, which created a "Fictonal" ontology and a " false" ontology for this purpose. I believe, such a process is required, if you really want to ensure that prior knowledge will not affect the results. The authors' approach of using GenericsKB sentences, while diverse, does not guarantee factual incorrectness, and simply mixing and matching sentences does not ensure that the resulting conclusions are not accidentally true or plausible. This is a crucial point that needs more rigorous handling, perhaps by explicitly creating contradictions or using a fictional knowledge base as done in PrOntoQA.
2. Overall the conclusion that every LLM except o1 is lagging -- seems to not add much to the ongoing body of knowledge. Why are some of the derivations difficult vs easy. Only 1/2 line of explanations are given, that too in a hand-wavy manner (L513). The analysis of why certain argument forms are harder than others is superficial. A more in-depth analysis, perhaps involving the logical structure of the argument forms or the specific types of inferences required, is needed. For example, are argument forms with more complex nested quantifiers harder? Are those that require multiple applications of modus ponens more challenging? This should be investigated more thoroughly.
3. There are some issues with authors arguments about "flaws" in the benchmarks. See questions.

### Questions
1. Context-ndependent is mentioned in abstract/intro many times. It is unclear how the authors ensured. Seemed like nothing special has been done.
2. Why is the average human performance so low? If you recruit more trained puzzle solvers, such as say linguistic olympiad participants or winners, I believe they may do much better, In that case, this false supremacy of o1 should not be there.
3. L100: Why is it novel? I did not understand what is claimed to be novel here at all.
4. Tab 1: It will be better to clarify what does complexity mean in statistical terms, number of clauses, words etc.
5. L290: This Step 3 is written in a very convouted way or is it the process? Are we saying we have a conclusion and we do not know using logic, whether the conclusion is entailed or not. This can not be true.
Then why a paragraph is randomly assigned an answer? Please explain clearly.
6. L317: How is the number of domains measured? Is it from GenericsKB? 
The vocab seems to have been created by a mix of chosen templates and words from GenericsKB. Hard to say that it is significantly complex -- give GKB sentences are quite simple and there are limited templates authors curated.
7. L333: This may not be that simple. One may be able to prove the negation in a smaller set of steps. Is that considered as well? Or, the dataset does not have such examples?
8. L350-353: Very interesting paragraph. Again how do authors ensure the factual incorrectness of the conclusions? 
9. L442:Why is the performance on CLUTTRR so low compared to JustLogic?
10. L514: For the apparently long tail argument forms, have you qualitatively evaluated the CoT or some other ways to actually see what reasoning is being done by the LLMs?

### Soundness
3

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
5

### Summary
This paper describes a procedure for synthesizing data to test the logical reasoning abilities of language models.
The proposed method consists of:
1. Constructing random propositional logic arguments
2. Substituting natural language statements drawn at random from GenericsKB for the propositional variables
3. Sampling a truth value for the example (from True/False/Uncertain) and generating a query statement accordingly (either the conclusion of the argument, its negation, or a random related statement from GenericsKB, respectively)

The authors use this procedure to construct a challenge dataset, JustLogic, and evaluate several LLMs on it, in addition to conducting a human baseline study on MTurk. The human average is 73%, while OpenAI o1-preview gets 81%. The authors state that the 'human ceiling' is 100%, but do not clarify whether this is the accuracy of the best-performing participant, or just implying that every question was answered correctly by at least one participant.

### Strengths
The authors rightly state that conflating prior knowledge and inferred knowledge is an issue with certain ubiquitous benchmarks, and causes problems when they are used to make claims about reasoning. It is helpful to have more challenging datasets that are controlled to ensure performance reflects models' ability to reason from provided context, rather than other extraneous features.

### Weaknesses
Two of the properties of JustLogic claimed as virtues by the authors are somewhat dubious:
- W1: **The truth value of a statement is unrelated to its truth value in the real world** (termed "context-independence" by the authors). This seems to me to be mostly a source of confusion for both models and human labelers, as the dataset tacitly overrides the truth values of very basic facts. The value of "context-independence" is ensuring that answers can't be guessed based on questions in the absence of premises (as the authors test in 5.1). However, this can be accomplished without contradicting world knowledge - see for example MuSR (Sprague et al., 2024), in which premises involve world knowledge but answer options are controlled so that correctness solely reflects argument structure.
- W2: **High "natural language complexity", by which the authors mean vocabulary size.** I think this is a straightforward overclaim: the linguistic complexity of the task does not increase just because propositional variables have been substituted for longer or more diverse spans. A nontrivial notion of natural language complexity would imply a higher degree of complexity in the _relationship between_ the natural language and the logical argument structure, i.e. comprehending a wider range of linguistic structures would be required in order to recover the logical structure. In my opinion this would also imply moving beyond propositional logic, as natural language largely revolves around predicate-argument structure.

Additionally:
- W3: The 'future-proofness' of the dataset is called into question by the fact that o1-preview outperforms the human average. Additional results showing that the dataset's complexity knobs can be turned up to counteract this would mitigate this weakness. As it stands, the authors claim that the dataset can be scaled to match stronger models but do not actually demonstrate this for the strongest model.

### Questions
**Suggestion:** It would be helpful for clarity if you could use a term other than 'context-independence' to describe the property of answer correctness not being influenced by prior knowledge, as 'context-independent' is ambiguous and somewhat counterintuitive: in fact, answers in JustLogic are _only_ sensitive to the question and context (JustLogic accuracy goes to random chance when C is omitted from the CQO tuple in 5.1). The clarity of the paper's arguments would be improved by avoiding the use of 'context' to refer to both world knowledge and question premises.

**Q1:** How is the human ceiling computed?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a synthetic benchmark JustLogic to assess the deductive reasoning capabilities of LLMs. Key contributions include
* Benchmark Design: JustLogic is a benchmark specifically for evaluating LLMs' logical reasoning skills. It minimizes the influence of prior knowledge, ensuring that models rely on logical deduction alone rather than external knowledge.
* Evaluation of Existing Models: JustLogic's experiments reveal that current LLMs, such as GPT-4 and Llama3 variants, perform significantly below human accuracy on deductive tasks, indicating substantial room for improvement in LLM reasoning capabilities.
* Error Analysis: JustLogic allows detailed analysis of model errors, exploring how factors like argument form and reasoning depth affect model accuracy, thus offering insights into specific areas of reasoning weakness in LLMs.

### Strengths
* Originality: This paper contributes a well-defined deductive reasoning benchmark addressing limitations in prior benchmarks by focusing on memorization-aware design and error analysis. The originality lies in synthesizing complex deductive tasks without relying on real-world facts, thus eliminating the influence of prior knowledge, which is usually ignored in existing benchmarks.

* Quality : JustLogic’s design is grounded in logical principles, using well-established argument forms (e.g., modus ponens) to construct queries. It provides a comprehensive evaluation across multiple LLMs and include human baselines, showing the benchmark’s realism and effectiveness. The extensive error analysis further strengthens the paper.

* Clarity: The paper is clearly written and organized into motivation, dataset construction, and evaluation. 

* Significance: This work contributes to LLM reasoning evaluation, as it introduces a benchmark that better reflects true deductive reasoning without overly reliance on memorized facts.

### Weaknesses
1. “it is important to note that, despite being drawn from real-world data, the statements are generally factually inaccurate. This is intentional.” “By using real-world yet factually inaccurate statements, we combine realism and context-independence.”

It does not make much sense to “intentionally” choose factually inaccurate statements. The authors claim to study reasoning from a perspective of “eliminating the influence of prior knowledge and ensuring context independence” (L93). However, the effect of prior knowledge is exerted from both the positive and negative sides, i.e. certain knowledge could align with or disagree with a given query. For example, if a model is already pretty sure about the fact that “Japan is in Asia”, then this degree of certainty would likely to affect the reasoning about the question that leads to “Japan is not in Asia”, so the influence of prior knowledge is not “eliminated”. In this sense, the topic would be counterfactual reasoning, which has been studied by a few previous work [1]. A more reasonable principle of choosing the statements would be complete irrelevance of real-world knowledge, e.g. “My cat Fluffy likes paper bags”.

2. “The variable(s) within each expression is ultimately replaced by randomly selected generic, realworld sentences from GenericsKB-Best”

It would be better to include more details about the GenericsKB-Best dataset. One of the concerns would be: Is it assured that any two statements in the dataset are semantically independent with each other? For example, if statement A is “Japan is in Asia”, while statement B is “Japan is not in Asia”, then “A and B” will actually reduce to False. This problem would be more pronounced when the “argument complexity” is scaled up, as there would be more statements involved.

3. Error analysis is somewhat superficial. It is not surprising to see a decrease in performance as the reasoning depth increases. A more interesting investigation would be regarding at which step the model starts to fail and why, as it would be a direct guidance of steering the model towards the correct reasoning path and avoid straying from the subject.

4. It would be better to add another section to prove the robustness of the benchmark by finetuning a model on the synthetic deductive data, showing whether the benchmark can be hacked by training on test data.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
