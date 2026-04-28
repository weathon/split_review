# Alice in Wonderland: Simple Tasks Reveal Severe Generalization and Basic Reasoning Deficits in State-Of-the-Art Large Language Models

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 5, 3, 6, 6

## Abstract
Large Language Models (LLMs) are often described as being instances of foundation models - that is, models that possess strong generalization and therefore transfer robustly across various tasks and conditions in few-show or zero-shot manner, while exhibiting scaling laws that predict generalization improvement when increasing the pre-training scale. These claims of strong generalization and advanced reasoning function enabling it rely on measurements by various standardized benchmarks where state-of-the-art (SOTA) models score high. We demonstrate here a dramatic breakdown of generalization and basic reasoning of all SOTA models which claim strong function, including advanced models like GPT-4 or Claude 3 Opus trained at the largest scales, using a simple, short common sense problem formulated in concise natural language, easily solvable by humans (AIW problem). The breakdown is dramatic as it manifests in both low average performance and strong performance fluctuations on natural problem variations that change neither problem structure nor its difficulty, while also often expressing strong overconfidence in the wrong solutions, backed up by plausible sounding explanation-like confabulations. Various standard interventions in an attempt to get the right solution, like chain-of-thought prompting, or urging the models to reconsider the wrong solutions again by multi step re-evaluation, fail. We take these observations to the scientific and technological community to stimulate re-assessment of the capabilities of current generation of LLMs as claimed by standardized benchmarks. Such re-assessment also requires common action to create standardized benchmarks that would allow proper detection of such deficits in generalization and reasoning that obviously remain undiscovered by current state-of-the-art evaluation procedures, where SOTA LLMs obtain high scores. Code for reproducing experiments in the paper and raw experiments data can be found at https://anonymous.4open.science/r/AITW_anonymous-69A6/

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper demonstrates that LLMs struggle with generalisation on a simple problem. Specifically the authors construct a question and various variations thereof of a `simple' family relationship question. (i.e. in short the question is: Alice has N brother and M sisters. How many sisters does Alice's brother have?) The paper demonstrates that small variations of this question break state-of-the-art LLMs, even across different prompting techniques.

### Strengths
The strengths of the paper:
1. Good number of experiments specific to the question demonstrated by the authors
2. Careful analysis across a wide variety of models.
3. Interesting finding that breaks models.

### Weaknesses
The weakness of the paper:
1. The study while interesting and definitely highlights a problems with modern LLMs is quite limited by the actual test set (basically being based on a single question and variations thereof).
2. The study is quite limited into the actual limitations of the model.

Concretely, although many models were run on this small dataset (and it is understandable that so many models can only be run on smaller datasets [reasonably]), the contribution is quite limited regardless. **Finding specific phrasings that break a model is very common** to most problems and to most people that have done prompt engineering.

Furthermore, the actual analysis while removes high-level doubts in the approach (such as the female boost, or the control question) do not provide deeper insights into what might be going on. Very interesting work in this regard would be "Physics of Language Models", which provides excellent analysis of how model perform and why they generalise poorly. https://physics.allen-zhu.com/

Generally, your work is very interesting and should be pursued further. Well done, however, in terms of research contribution it requires more interesting datasets (than single examples that work poorly and then others that work well, as mentioned earlier this is very common for most tasks). Also, your analysis should be much more detailed in terms of how and why models perform poorly or well on these tasks. (Again, the Physics of Language Models is an amazing work (not ours, unfortunately ;)).

### Questions
Some questions that could help you with you research:
1. What specifically do you think can discovered about LLMs using your research (going beyond that LLMs perform poorly on specific examples, but perform better on others?)
2. How could you construct a dataset that measures that specific quality?
3. How could you then propose methods to overcome a fundamental problem that you have identified?

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
4

### Summary
The authors discovered a surprisingly simple and concise problem that makes most LLMs, including state-of-the-art models, fail. The problem, namely AIW, belongs to the class of basic reasoning problems where humans excel. The authors show that LLMs fail on the vanilla version of the AIW problem and semantically equivalent variations; techniques such as chain-of-thoughts or more advanced prompting methods fail at mitigating such issues.

### Strengths
I am really surprised that such a simple example makes LLMs fail, so I consider this discovery valuable. I tried to prompt a few models, and I agree with the authors that this problem is indeed hard even for models like GPT-4 (though I tried a few times with GPT-o1-preview, and it correctly solves the task, but it surprisingly fails to reply with nonsense when we input negative numbers!).

The article is well written and easy to follow, and the AIW results are robust enough to support the claim that most LLMs fail on such problems.

### Weaknesses
The authors did not try to add illustrations (e.g., k-shot) to mitigate the issue. I tried to add an illustration, but some models still failed. That analysis would add value to the work. While more expensive, fine-tuning a small model would also add value to the consistency of the case study they present.

Beyond that, my biggest concern is that the authors tried and reported only one example of failure across multiple models. 
To make an analogy with the adversarial robustness literature, this is equivalent to finding a single adversarial example in computer vision that makes most models misclassify an input (an example of a ‘universal trigger’).
The paper lacks a consistent analysis of other examples, and, in this form, it reduces the contribution to an exciting yet anecdotal showcase of failure. Plenty of articles show failure cases of LLMs on *many* examples and variations; one very popular is [1].

Furthermore, the authors do not provide a solution or a tentative plan to mitigate the problem (but that is not necessarily a limitation).
The authors do not give a reasonable rationale behind why LLMs fail on the AIW problem. Interestingly, it points out that LLMs fail on the AIW Light Arithmetic Total Girls, but that is another anecdotal showcase of failure that does not tell us much about why LLMs fail on such simple problems.
For example, a model that solves the vanilla AIW would possibly “create” a graphical representation of Alice and her brothers and sisters; then, the LLM can count the number of edges from one of the brothers connected to all the sisters. That means a sufficient (but not necessary) condition to solve the problem is being able to perform 2-hops reasoning and counting (from one of the brothers to all the sisters). LLMs seem to lack such capability.

### Questions
1) What happens when N and M grow larger than 7, and why do they decide to set that as the upper bound on such variables? 

2) Have the authors tried with floating and/or negative values for N and M? If a model still replies with the consistent (yet wrong) reasoning, that is a strong hint a model does not understand the task under consideration (i.e., it cannot connect numerical and graphical reasoning with family relationships).

3) Have the authors tried to ask the model to generate a graphical representation of Alice’s family and then solve the task?

4) Why do the authors focus on a single example and not on a consistent range of variations of similar problems?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tests SOTA LLMs’ reasoning abilities by testing them with a bunch of variants of the AIW problem.

### Strengths
1. The tests are across different SOTA LLMs.

### Weaknesses
1. The whole paper is about one type of questions:  “Alice has N brothers and she also has M sisters. How many sisters does Alice’s brother have”. I personally feel like it is hard to judge model’s capabilities based on one type of question alone. Model’s generalization and reasoning abilities are maybe on a spectrum and with only one question, it is hard to tell where the model falls on this spectrum. It is concerning that the entire analysis hinges on a single problem type, as this approach may not capture the breadth of reasoning skills that LLMs are purported to possess. The paper does not explore how the models perform on other types of logical or mathematical reasoning tasks, making it difficult to ascertain whether the observed failures are specific to this particular problem structure or indicative of a more general deficiency.

2. GPT-4o has superior performance, possible suggesting this might have to do with model size or training?  It is not clear whether the superior performance of GPT-4o is due to inherent architectural advantages, a larger training dataset, or more sophisticated training techniques. The paper does not delve into the specific factors that contribute to the performance differences between the models, which limits the insights that can be drawn from the results. A more detailed analysis of the model architectures and training procedures would be beneficial to understand the underlying reasons for the observed performance variations.

3. I don’t consider “female boost” as totally redundant information. For one thing, if you are testing the model’s reasoning abilities, it should disentangle model’s syntactic understanding as a separate thing. “She” as a sole indicator of Alice being a female is more a syntactic problem, which shouldn’t part of model’s burden if one’s goal is simply to test reasoning abilities. The argument that the “female boost” is redundant overlooks the fact that natural language understanding is an integral part of the reasoning process. The ability to correctly interpret pronouns and their referents is a fundamental aspect of language comprehension, and it is not necessarily a separate issue from reasoning. By adding the explicit statement “Alice is female,” the authors are potentially simplifying the task by removing a layer of syntactic complexity, which may not be a valid way to isolate reasoning abilities. The fact that this boost improves performance suggests that the models may be struggling with basic language understanding, which is a critical component of reasoning.

4. Personally, I feel like this paper adds nothing significantly interesting to the existing discussion on whether LLM can reason or generalize. For one thing, a pure test on reasoning should not rely much on extra knowledge. The test in the paper (AIW) needs model’s understanding of “she” as Alice (syntactic) and basic family structure (external knowledge). The actual reasoning, on the other hand, is in my opinion, perhaps not the main bottleneck. This is also supported in the paper where “female boost” variants can improve performance. The paper's claim that the AIW problem is a pure test of reasoning is questionable, as it requires a basic understanding of family relationships and pronoun references. These elements introduce external knowledge and syntactic processing into the task, which may confound the assessment of pure reasoning abilities. The fact that the “female boost” improves performance further suggests that the models may be struggling with these aspects rather than the core reasoning component. The paper does not adequately address how these confounding factors are controlled for or how they might influence the results.

### Questions
1. For figure 1, what do the numbers like 55, 56, 63, 69 mean?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper demonstrate a dramatic breakdown of generalization and basic reasoning of all SOTA models (ncluding advanced models like GPT-4 or Claude 3 Opus) which claim strong function, using a simple, short, conventional common sense problem formulated in concise natural language (AIW problem). The authors observe that large language models (LLMs) exhibit significant performance fluctuations on simple problems across minor variations that should not impact problem-solving ability at all. Additionally, various standard interventions, such as chain-of-thought prompting, failed to yield correct solutions in the AIW problem. These observations highlight the need to re-evaluate the claimed capabilities of the current generation of LLMs.

### Strengths
* This paper is well-written and presents clear ideas.

* The authors conduct extensive experiments on over 36 LLMs to demonstrate the breakdown of SOTA LLMs on the somple AIW problem.

* Fully Open-sourced code and data to reproduce the result.

### Weaknesses
 * The problem setting of AIW has certain interfering factors. After some attempts, I found that the main reason LLMs perform poorly on AIW origin is due to easy thinking. For example, "Alice has 3 brothers, and each of these brothers has the same sisters, who are Alice's sisters. Alice has 6 sisters, so each of her brothers has 6 sisters." The issue here is that the LLM overlooks counting Alice herself, rather than lacking reasoning ability. I believe that testing similar problems in mathematical reasoning tasks (like GSM8K or MATH) would be more convincing.

* Quite a few typo errors. line 016, few-show -> few-shot; format of most of the citations is wrong.

### Questions
See weaknesses.

Recently, I came across another paper that is similar in content to this study. I know this paper was published online prior to [1],  I'm just curious about what advantages the authors believe the AIW dataset presented in this paper has compared to [1], which focuses on the mathematical reasoning task.

[1] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors study reasoning capabilities of various SOTA LLMs in a controlled environment, by synthesizing a very simple yet efficient task, Alice in Wonderland (AIW). This task is composed of multiple variations of the following template: "Alice has N brothers and she also has M sisters. How many sisters does Alice’s brother have?". Authors systematically study more than 20 models by varying M/N, changing family relations, introducing redundant information, and varying between prompt templates. Authors showed that models not only fail on this simple task showing high variation between prompt templates, but also that their failure can not be attributed to arithmetic or commonsense knowledge errors, but occur due to the lack of generalization and basic reasoning abilities.

### Strengths
- Authors discuss an important problem of LLM reasoning abilities
- Paper is clearly written
- Proposed evaluation framework is novel and simple to implement and verify
- Authors perform extensive experiments across various models and prompt templates
- Detailed ablation studies on AIW variations support main claims of the paper

### Weaknesses
 - Even though authors prove that SOTA LLMs fail on AIW task, I don't think we can claim that they are not capable of robust reasoning. On the contrary, paper shows that LLMs are capable of some types reasoning (like arithmetic, or basic family relations), but fail on the others (logical reasoning).
- There are multiple formatting issues in the paper, probably caused by moving text between templates, that hurt overall presentation of the paper (see Questions section for example).


### Questions
1. Why do you think Llama-3 performs so much worse then Llama-2 model? What framework did you use to run evaluations for models with  open weights? I wonder, if there might be any issues with prompts, as Llama-3 models require different special symbols in chat template than Llama-2.

2. There are some issues with citations across the paper where brackets are missing in most of the citations, for ex. in lines 41-42: "...visual recognition Radford et al. (2021) or language understanding Devlin et al.(2018); Raffel et al. (2020); Brown et al. (2020), l..." should be  "...visual recognition (Radford et al., 2021) or language understanding (Devlin et al., 2018; Raffel et al., 2020 ...".  Multiple periods are missing: lines 111, 117, 192, 309, 458, 460, 463.  Chapter 3.1.1 "original. like" -> "original, like" in multiple places.

### Soundness
3

### Presentation
3

### Contribution
3
