# Distributional reasoning in LLMs: Parallel Reasoning Processes in Multi-hop Reasoning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Large language models (LLMs) have shown an impressive ability to perform tasks believed to require "thought processes”. When the model does not document an explicit thought process, it becomes difficult to understand the processes occurring within its hidden layers and to determine if these processes can be referred to as reasoning. We introduce a novel and interpretable analysis of internal multi-hop reasoning processes in LLMs. We demonstrate that the prediction process for compositional reasoning questions can be modeled using a simple linear transformation between two semantic category spaces. We show that during inference, the middle layers of the network generate highly interpretable embeddings that represent a set of potential intermediate answers for the multi-hop question. We use statistical analyses to show that a corresponding subset of tokens is activated in the model's output, implying the existence of parallel reasoning paths. These observations hold true even when the model lacks the necessary knowledge to solve the task. Our findings can help uncover the strategies that LLMs use to solve reasoning tasks, offering insights into the types of thought processes that can emerge from artificial intelligence. Finally, we also discuss the implication of cognitive modeling of these results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method to analyze multi-hop reasoning in LLMs by modeling their prediction process as a linear transformation between semantic spaces. The authors find that intermediate model layers create interpretable embeddings representing potential answers, activating specific token subsets and suggesting parallel reasoning paths. This framework offers insights into how LLMs mimic thought processes, even without direct task knowledge, with implications for understanding AI reasoning and cognitive modeling.

### Strengths
- This paper addresses a critical challenge in understanding LLM reasoning by probing the multi-hop reasoning processes. The discussion on human cognitive processes and LLM reasoning mechanisms is also inspiring.

- The study presents a clear illustration of distributional reasoning in LLMs (esp. with the example in Figure 2), which is a novel finding to my knowledge.

### Weaknesses
 - While the illustration of distributional reasoning is interesting, the remaining analysis seems confusing to me. For example, what's the motivation of the analysis that uses the matrix to approximate the second-hop reasoning? The paper mentioned "This method reveals the extent to which the second-hop operation is invariant to the prompt specifics." why is this an important question to explore? and what's the takeaway from this analysis?

- The writing needs to be improved to make the logic clearer. Especially, there should be strong and clear motivation before going into any notations and technical details of the analysis. The current version makes readers very easy to get lost.

### Questions
See the weakness.

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
This paper provides a study of the internal reasoning processes of LLMs when answering compositional questions. 
They find that one can apply linear models on the activations for specific task-related tokens at intermediate transformer layers to approximate the reasoning of the model at the "outcome" final prediction layer. This supports a hypothesis that LLMs consider a distribution of possible answers at intermediate layers then narrow down the final answer at later ones, in a process akin to the parts of the "spread of activation" and propositional reasoning theories of human cognition.

The authors consider a synthetic dataset (the Compositional Celebrities dataset from Press et al 2023, as well as carefully crafted variants to test for hallucinatory scenarios) and provide strong evidence for their hypothesis. The authors argue that transformer-based LLMs can be used to test questions in cognitive modeling.

### Strengths
* The paper is well-written and well-motivated. 
* The study design is clear and effective, and the results are interesting and well-supported. The secondary experiments (4.2 on the interpretability of the intermediate layers, and 4.3 on whether this type of reasoning still holds when the answer is hallucinatory) do a good job of preemptively answering follow-up questions I had on the original study. 
* The finding will be of interest to people concerned with whether current LLMs can shed light on questions in cognitive modeling of reasoning processes.

### Weaknesses
 **W1** The primary weakness of the paper is that it only considers one clean, synthetic dataset with one type of question. It is unclear whether such a clean result would hold on a more realistic reasoning dataset. The authors acknowledge this in their limitations section, but it is still the case that this paper shows __one__ scenario in which a clean form of reasoning can be approximated using linear modeling for __one__ kind of problem. The paper would be stronger with at least one other dataset that is more complex than 2-hop compositional questions and/or noisier than the templatic questions in Compositional Celebrities. Otherwise, this analysis should really be considered exploratory rather than comprehensive.

**W2** l501 "This bridges a gap that was observed by cognitive sciences decades ago and emphasis the role of AI
research in cognitive modeling." -- it would be helpful to describe more specifically how the result contributes the debate surrounding this gap (i.e., why they are incongruous) more specifically in the context of existing work. The paper seems to argue that both associative and propositional reasoning can take place at the same time in a single framework -- whether this is possible has been the subject of debate for many years, and various other cognitive models have been proposed that integrate both paradigms to differing degrees, e.g. [ACT-R](https://wires.onlinelibrary.wiley.com/doi/full/10.1002/wcs.1488?casa_token=9nMiql_9dRMAAAAA%3A1kKURVyse66RR4wdR3wxa1DDWQI_HO0D-oUAPfHepYuJzEhYj_0Jo77bV5qSxGHQq9O4Sz3VPpYa) and [CLARION](https://en.wikipedia.org/wiki/CLARION_(cognitive_architecture)). Comparing your consideration of transformers to these other frameworks and discussing how the contributions differ would benefit the paper.

**W3** The authors' analysis method appears to be constrained to a very specific type of question, where the intermediate and final answers are not directly related to the question's subject. The authors state that the linear transformation-based model can only work if the questions are a specific kind of unnatural, where the final answer shouldn't be related to the question subject directly ('y' is not related directly to 'banana' without the context of its color). It is unclear why the method would not work for more natural multi-hop questions whose sub-questions are more topically consistent. This constraint severely limits the applicability of the findings.

**W4** The authors added a new dataset to the paper's experiments, but it is relegated to a tiny paragraph in the appendix. If this new dataset is to be included, it should be more thoroughly described, including the methodology for its creation, rather than simply stating that "we used Gemini". The lack of detail makes it difficult to assess the validity and generalizability of the results obtained with this new dataset.

**W5** The paper frequently uses language that suggests the model is actively "using" the suggest-then-narrow-down mechanism, which is an overclaim given that the analysis does not demonstrate causality. For example, statements such as "Our findings can help uncover the strategies that LLMs use to solve reasoning tasks" (L24), "what strategy does the model use when applying the implicit approach?" (L64), "LLMs use the same reasoning process even when they hallucinate their answers" (L116), and "Evaluating this consistency can help assess the ability of LLMs to use valid reasoning processes" (L507) imply a causal relationship that has not been established. While the authors acknowledge the lack of direct causality in the limitations section, the main body of the paper should be clearer about the distinction between strong association and evidence of usage.

### Questions
**Q1** Does this analysis generalize to any sort of task that isn't 2-step compositional reasoning? What classes of task/problem does this framework make sense for, and what kind would it be unrealistic?

**Q2** This analysis suggests that the suggest-then-narrow-down reasoning approach can be __induced__ from the model's intermediates, but that is not the same thing as the model necessarily __using__ that approach. How can we have confidence that the model is actually using this reasoning chain and not rely upon other forms of reasoning instead/ in addition?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the mechanism of multi-hop reasoning of LLM. Specifically, the paper uses a compositional two-hop question answering setup as a test bed for the investigation. It proposes the hypothesis, referred to as distributional reasoning, that the first attribute extraction creates a distribution of possible attributes on which the second extraction can operate simultaneously to derive the final answer. To test the proposed hypothesis, the paper constructs a linear model to predict the activation of the final layer based on the activations of intermediate layers. The results indicate that once the model depth reaches a certain threshold, the activations of intermediate layers can linearly predict the activations of the final layer. Additionally, the paper demonstrates that the intermediate layers activate a small subset of tokens representing potential intermediate answers.

### Strengths
1. The paper proposes a hypothesis to interpret the multi-hop reasoning ability of LLM and designs sound experiments to test the proposed hypothesis. The findings provide interesting insights on neural cognition and reasoning.
2. The paper is clearly written. The experiments are well-designed with main results (Section 4.1 & 4.2) providing direct support to the hypothesis and additional results (Section 4.3) ruling out the confounding factor of the possibility of LLM simply memorizing knowledge.

### Weaknesses
1. While I can follow the proposed hypothesis and think the experiments are well-designed for testing them, I am unsure whether we can draw a conclusion that LLMs use distributional reasoning to answer multi-hop questions. As the authors also point out in the Limitations section, the paper only experiments on the two-hop question answering setup and all the questions are synthesized from one data source, the results may be different on questions with very different structures. For example, I am wondering whether the proposed hypothesis still hold on answering math problems that require multiple steps to solve. Or, still within the question answering setup, can the concept of distributional reasoning be identified on answering n-hop questions when n > 2?
2. Another major concern is the implication of the proposed hypothesis. Although the experimental results support the proposed hypothesis, it does not exclude other possibilities - therefore, I personally think the contributions of "computational framework demonstrating the role of associations in structured reasoning" is a bit oversold. A way to strengthen the contribution is to demonstrate the potential usage of the discovered hypothesis/pattern. Can the finding on distributional reasoning help us design better reasoning algorithm (e.g., discover self-inconsistency) or help us train models better at multi-hop reasoning? Even though the paper mentions some relevant aspects in Section 5, it lacks a proof-of-concept to showcase this is a promising way to go.

### Questions
See the questions raised in "Weaknesses".

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the inner processes of LLMs on two-hop reasoning tasks. The authors identify the categories of the intermediate and final answers and study their activation in the LLMs. They find that these categories can respectively be found in the intermediate and final layers and that the connection between the intermediate and final activations can be mapped using a linear transformation. Moreover, they find that LLMs consider multiple hypotheses in parallel, with the middle layers representing the potential intermediate answers and the final layers the potential final answers.

### Strengths
The paper is well written and mostly easy to read and understand.

The proposed methodology is an interesting way for studying the challenging problem of LLM interpretability. The resulting findings provide intriguing insights into the reasoning of LLMs in two-hop composition tasks and can be very useful to the research community.

### Weaknesses
Although the analysis provided in the paper is quite interesting, the main issue of the paper is its limitation to a single dataset and two-hop questions, which restricts the possibility to extrapolate the findings to larger settings. More specifically:

1. The activation of a word is independent from the rest of the logits, therefore this activation may not be the main reasoning mechanism happening inside the LLM but a byproduct or a minor function only marginally used in the total prediction. The paper does not clearly establish if the activation is the main reason for the final model prediction. It might be interesting to compute relative activations with respect to the other dimensions of the layer representation with (e.g. with softmax).

2. The example provided in Figure 1 is a composition of two simple queries. The category mapping found could be an artifact coming from the task instead of a property of the model on two-hop reasoning tasks. The evidence provided in the experiments does not seem to eliminate this possibility.

3. Figure 4 does not include legends for the plots, making them hard to interpret. It would be good to include what each data point/plot corresponds to.

4. The experiments focus on two-hop reasoning. To assess the robustness of the findings, it would be interesting to see if they hold to n-hop queries with n higher than two. Queries recalling names could easily be modified into three-hop by asking to return the first letter of the name instead of the full name as done in Figure 1.

### Questions
1. Have you conducted experiments to verify if the identified mechanism is the main function responsible for the final model prediction or how much does it contribute to it?

2. How diverse are the questions asked in the experiments? How did you assess that the dataset used contain sufficiently diverse queries for your findings to be robust?

3. Have you conducted experiment on n-hop reasoning tasks with $n>2$ to verify if your findings scale to more complex multi-hop reasoning tasks?

4. What are the average sizes of the semantic categories $c_1$ and $c_2$?

### Soundness
3

### Presentation
3

### Contribution
2
