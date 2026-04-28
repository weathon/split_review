# Measuring Language Model Uncertainty With Internal Concepts

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 6, 5, 5

## Abstract
We study the problem of evaluating the predictive uncertainty of large language models (LLMs). 
We assign an uncertainty measure to the correctness of outputs from an LLM conditioned on a query using a form of entropy that applies to semantic objects (concepts).
Unlike prior works, the notion of meaning used to define concepts is derived from the LLM, rather than from
an external model. 
Our method measures an uncertainty over concept structures by drawing from ideas in Formal Concept Analysis (FCA) and lattice/order theory, and can be used to estimate correctness in closed- and open-ended scenarios.
Our method has a relative improvement of up to 4.8% on average across five standard benchmarks as well as improves over comparable baselines on datasets consisting of both closed- and open-ended questions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper is well written and structured. 
It deals with a way to evaluate the uncertainty of a Large Language Model’s (LLM)  in terms of output meaning as corresponding the questions submitted to it. 
The authors approach relies on “internal concepts ” i.e. semantic objects from the LLM itself and not derived from an external semantic model of the language thus avoiding introducing differing/contradicting semantics between the external model and the LLM.
Their approach is entropy-based.

### Strengths
Quantified uncertainty is meant to evaluate the LLM’s responses and thus can help detect highly probable (semantically) odd responses (LLM hallucinations).
The approach tackles both open and close-ended queries and through what is termed “conceptual uncertainty”. It applies a query-dependent “truth-assignment likelihood” function to estimate LLM answers “truthfulness”.
Based on the various LLM responses’ “truthfulness” values, an entropy-based  uncertainty measure is computed. The entropy measure introduced is called “Conceptual Entropy”, only relies on non-all-false LLM responses truth  assignments, and accounts for mutually exclusive concepts and output length differences through length-normalized likelihoods.
Finally uncertainty is computed as a function of answers semantic groups (of model outputs) and their likelihoods.

### Weaknesses
See questions' section

### Questions
S: Statement. Q: Question.

S1: In “2 A GENERAL FRAMEWORK FOR LLM UNCERTAINTY”, you state “ We use the term uncertainty as opposed to confidence as we view uncertainty as independent of the selected output to the query”.  
Q1.1: Can you further clarify ?

S2: In “COMPONENTS OF LLM UNCERTAINTY”, you state “We further decompose existing diversity measures into three key components”. 
Q2.1: Are you referring to “2) measuring some form of answer diversity” form of uncertainty mentioned earlier in the paragraph? 
Q2.2: Isn’t this in contradiction with  your statement in Q1? Or
Q2.3 Do you consider that diversity of answers is independent from selected output?

S3: In “3.1 INTERNAL CONCEPTS”, You state “Given a set of candidate answers A = {a1, . . . , an} ⊂ A∗ for a query q, we view the corresponding “concept structure” as determined by a partial ordering where ai ≤ aj indicates that if ai is a valid output for q, then aj is also a valid output.” 
	Q3.1: This is not clear to me. Doesn’t this make all model candidate answers, whatever their place in the order, valid as a hypothesis? No order depth limit as deeper positions might mean very uncertain?

S4: In “4.1 SETUP-Metric”, you state “randomly selected correct question having a larger uncertainty score than a randomly selected incorrect question.”.
	Q4.1 can you clarify “correct/incorrect question?”

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
To address limitations in existing uncertainty evaluation metrics—such as dependence on external models lacking equivalent knowledge to the evaluated LLM, inability to handle open-ended questions, and failure to leverage hierarchical semantic structures for more effective grouping—the authors propose a framework called Conceptual Uncertainty for assessing LLM uncertainty. Specifically, they introduce an internal concept structure to define the distribution over possible truth assignments to answers, which is then used to calculate the newly-introduced conceptual entropy as a measure of uncertainty. Extensive experiments demonstrate that this proposed metric outperforms baseline methods in handling both open-ended questions and those questions with long answers.

### Strengths
- A novel approach that effectively leverages the inherent hierarchical semantic structures and the internal knowledge of the evaluated LLM to improve the precision of uncertainty evaluation.
- A clear presentation of the motivation and key challenges addressed by the framework.
- Intuitive figures and examples that aid readers in understanding the newly introduced concepts.
- Experiments conducted on both challenging cases, covering both closed- and open-ended questions, as well as questions with short and long answers.

### Weaknesses
 - The clarity of the paper could be further enhanced, as noted in the questions below.
- There appears to be an inconsistency between the algorithm and the main text; specifically, lines 5 and 6 in Algorithm 1 seem more aligned with standard uncertainty evaluation practices rather than fully reflecting the conceptual entropy measure introduced in the paper. If the algorithm is correct, it would be helpful to clarify the connections between the functions in the algorithm and the functions in the main text.
- In line 67, Why can the connection between a and b be quantified by the likelihood ratio of strings of the form qbqa and qa? A more intuitive explanation would be helpful.
- Why does Equation (1) hold? Could you provide a more intuitive rationale for it?
- Some notations in Equation (2) are not formally defined, which may lead to reader confusion.
- How the expected (internal) concepts are determined?
- In line 319, you mention that 20% of the samples are used for parameter tuning. Which specific hyperparameters are tuned?
- Have you evaluated the performance of the new metric on larger-scale LLMs, such as GPT-4 or others?
- How many sample answers are generated to evaluate conceptual uncertainty for each question? How does the sample size impact the performance of the conceptual uncertainty metric?
- In line 360, why is the question “What is my favorite integer between X and Y, inclusive?” considered a closed question?

### Questions
- In line 67, Why can the connection between a and b be quantified by the likelihood ratio of strings of the form qbqa and qa? A more intuitive explanation would be helpful.
- Why does Equation (1) hold? Could you provide a more intuitive rationale for it?
- Some notations in Equation (2) are not formally defined, which may lead to reader confusion.
- How the expected (internal) concepts are determined?
- In line 319, you mention that 20% of the samples are used for parameter tuning. Which specific hyperparameters are tuned?
- Have you evaluated the performance of the new metric on larger-scale LLMs, such as GPT-4 or others?
- How many sample answers are generated to evaluate conceptual uncertainty for each question? How does the sample size impact the performance of the conceptual uncertainty metric?
- In line 360, why is the question “What is my favorite integer between X and Y, inclusive?” considered a closed question?

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
2

### Summary
The submission proposes a new approach to quantifying uncertainty of LLMs. The method, named Conceptual Uncertainty, performs a hierarchical grouping (via a lattice) of candidate answers on the basis of which is then derives a likelihood function, form which an entropy measure is derived. The resulting measure then provides a measure of uncertainty for the scenario. 

The key novelty is the organisation of candidate answers in a lattice structure that captures more detailed relationships between answers than the partitioning into semantically equivalent answers generally considered by previous work. In particular, the lattice is induced by the partial order over answers that represents an answer being correct implying another answer being correct.

The method is then compared empirically to a range of methods from the literature on Mistral 7B, Falcon 7B, and Mamba 2.8B, with the proposed method of Conceptual Uncertainty performing best in most experiments.

### Strengths
S1) The combination of a likelihood function derived directly from the approximation of the partial ordering, as well as the variation on traditional entropy combine elegantly to an intuitively sensible measure of uncertainty. 

S2) The concept lattice is, to the best of my knowledge, an original contribution to the study of LLM uncertainty and conceptually seems to be a step forward from considering only equivalence classes.

S3) In the empirical evaluation the method compares favourably against a wide range of methods from the literature. Notably experiments were performed with transformer-based and with state-space LLMs which is particularly relevant as the proposed approach is highly LLM dependent.

### Weaknesses
W1) To me, the presentation is confusing at times. While effort was made to provide ample examples, they seem under explained and often unclear. For example, as far as I understand the assignment likelihoods in Figure 1 seems unconnected to the lattice in the figure and overall the figure offers little insight at this point in the text without further explanation.

W2) The authors explain that a key distinction of their approach to mot approaches in the literature is that they derive their concept structure from the LLM. This is done by approximately recovering the partial order over concepts via a specific ratio of LLM output probabilities. This then naturally carries with it its own uncertainty based on the LLM which is ignored in this analysis. See also Q2. 
Furthermore, I am not sure if it is not straightforward to adapt other methods to derive their respective concept structures (say semantic equivalence relations) via the LLM. This key distinction therefore seems somewhat weak to me.

### Questions
Q1) In order to estimate the uncertainty of answers for question q, the proposed method uses the ratio of LLM probabilities on question q itself to construct the lattice from which the uncertainty measure is then derived. This seems somewhat circular to me, and intuitively this approach would perform worse in situations with high uncertainty, as the approximated concept lattice would be less reliable. Could you clarify why this cyclic nature is not of greater concern?


Q2) The method relies critically on the approximation of the partial ordering of concepts by I_q. Have you performed any systematic comparisons of the approximate partial orderings to the real partial orderings?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper evaluates the predictive uncertainty of LLMs for tasks such as QA. It assigns an uncertainty using a form of entropy that applies to semantic concepts. A key feature is the acknowledgement of hierarchy of concepts.  A high-level framework is proposed, followed by some specific approaches in the framework that group generated answers, apply some weights, and estimate uncertainty scores for answers using a weighted sort of entropy. Some experiments are performed, revealing good performance on AUROC for some datasets.

### Strengths
The authors propose a method that unifies some of the related work on semantic similarity and uncertainty quantification for LLMs. They propose some new ways to obtain clusters of answers and use those to compute uncertainty.

Another strength is that the results on some datasets seem promising. The choice of datasets is somewhat diverse.

### Weaknesses
In my view, the paper suffers from clarity related issues and seems too similar in many ways to previous work in the space. The paper goes out of its way to make the case that 1) the semantic understanding part of the work is internal rather than external, and 2) the work has theoretical basis as opposed to some prior work.

Re: 1): I could not fully understand the distinction between prior work on external models vs. the claim about using the internal model. Wouldn’t it be possible to use the same LLM for NLI, similar to Kuhn et al.? Why is this distinction important? I did not understand this from the paper, even though it came up several times. The authors claim that their approach measures uncertainty as an intrinsic property of the LLM, but it's unclear why using the same LLM for NLI would not also be considered intrinsic, especially if the NLI task is framed as a prompt. The paper does not adequately explain why a separate NLI model is fundamentally different from using the LLM's own capabilities for NLI, especially given that both approaches rely on the LLM's internal representations to some degree.

Re: 2): the authors claim some theoretical basis but most of the discussion does not seem directly pertinent to the approach. The work feels like an extension of prior efforts. In my view, the claims of the paper are inconsistent with the presentation. The claims of theoretical justification either need to be softened or better explained. The theoretical discussion focuses on the normalization of entropy and hierarchical semantic structures, but the practical implementation seems to rely on disjoint partitions, which are a simplification. The connection between the theoretical framework and the practical algorithm is not clearly established, making the theoretical claims feel somewhat disconnected from the actual method.

As should be clear from many of my comments, I could not fully understand important details in the paper. Further details about my concerns and some associated questions are provided in the next section. Even though I’m familiar with much of the related work, I could not understand the new contributions. Perhaps the authors can clarify some aspects.

### Questions
Some questions and comments follow:

The abstract is too short. There are also some statements about % improvements that are unnecessary – I feel this is not suitable for situations where the datasets and baselines are not well known and standard.

In the second paragraph, the point about “external model” is too vague. This distinction b/w external and internal model was generally unclear to me and needs specification. I recommend adding some detail here. In general, there is a lot of repetition in the paper with details delayed to later, and when they do come later in Section 3, they are not clear enough for me.
 
The authors mention they focus on uncertainty (which is a function of a query) as opposed to confidence (which is a function of a query and generation). As I understand, the system computes a score U(q) for query q, for a model. How should one interpret this score? Does it represent the probability that at least one generation is correct for a query? Doesn’t this depend on the number of generations?

The title of Section 2.1 is too broad – there is a lot of literature that does not follow this paradigm.

Lines 127-129: The authors mention an exception but there are many types of exceptions given the vast literature on the subject of uncertainty quantification for LLMs. I recommend rewriting these lines.

What is the rationale behind the equation in line 215? Is it in the appendix and not in the main text?

Why is the NLI approach of Kuhn et al. for semantic relations between two answers not sufficient? Is that not a way to obtain I_q(a_i, a_j)?

There is an issue with the citation style in several places in the paper, like in line 242.

Why is there a min in equation 1?

What are the other strategies referenced in line 263?

It seems like conceptual entropy is mentioned in some older work. What was in termed in this work? Why was the old term not used?

Re: experiments: parameter tuning is done on 20% of what dataset? The full training dataset? And why is the test set so small, only 400 instances? Did the experiments repeat sub-samples for test set? Is the error mentioned anywhere?

Can the authors clearly explain how the AUROC was computed? This is not clear enough from line 327 and nearby places. When was a question deemed to be correct? When at least 1 answer is correct from the multiple answers generated?

How are correct questions determined when the datasets are combined? I don’t see this mentioned anywhere.

Did the authors run ablations on the Rouge-L threshold for determining correctness of queries for some datasets?

There are many more references in this space – please search for a review paper and add some of these if possible.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to measure the predictive uncertainty of LLMs with concepts. This method defines semantics through the internal conceptual structure of the model rather than an external model, thereby assessing the correctness of open and closed questions.

### Strengths
The proposed method does not rely on external semantic models but instead measures uncertainty based on the internal conceptual structure of LLM itself. It avoids the bias of incorporating external model knowledge into LLM evaluations, making the uncertainty measurement more aligned.

Additionally, the method can adapt to both open-ended questions ("List a city in California") and closed questions ("Which state is number 31?”), which is very useful in many practical application scenarios. 

Through experiments, the method shows an improvement, which demonstrates the effectiveness of conceptual uncertainty in hallucination detection.

### Weaknesses
The proposed method requires generating 10 to 20 candidate answers for each question to construct a conceptual structure, which has a high demand for computational or human annotation resources. This sampling amount will further increase, especially when dealing with open-ended questions. The computational cost associated with generating multiple samples for each query, especially for large language models, could be substantial, potentially limiting the scalability of the approach for real-time applications or very large datasets. Furthermore, the method's reliance on sampling introduces a degree of randomness, which could lead to variability in the uncertainty estimates, making the results less stable across different runs or initializations.

Although the proposed method reduces reliance on external models, it still depends on labeled datasets (for example, accurate matching of correct answers to questions). This places high demands on the accuracy and coverage of the dataset being constructed. In some fields, obtaining sufficient labeled data may be quite difficult. I believe that this may limit the generalizability of this method. The need for precise answer matching, even if used only for evaluation, introduces a potential bias towards datasets where such matching is straightforward, and may not accurately reflect the uncertainty in cases where answers are more nuanced or have multiple valid formulations.

The author used fixed rules and structures to construct concepts and categorized answer groups by defining implicational relationships. However, this may seem limited when dealing with more complex semantic relationships. The use of fixed rules for concept construction may not capture the full richness and complexity of semantic relationships that are present in natural language. For instance, the method might struggle with metaphorical language, idiomatic expressions, or cases where the meaning of a concept is context-dependent. I suggest the authors consider representation engineering [1] to enhance their concept discovery.

### Questions
**Q1**: From the perspective of practical usage, how to balance the trade-off between computational cost and performance improvement?

**Q2**: Do you have plans to use self-supervised or representation techniques to automatically construct concepts in order to reduce annotation dependence?

### Soundness
2

### Presentation
3

### Contribution
2
