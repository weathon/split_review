# CURATe: Benchmarking Personalised Alignment of Conversational AI Assistants

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
We introduce a multi-turn benchmark for evaluating personalised alignment in LLM-based AI assistants, focusing on their ability to handle user-provided safety-critical contexts. Our assessment of ten leading models across five scenarios (each with 337 use cases) reveals systematic inconsistencies in maintaining user-specific consideration, with even top-rated ``harmless'' models making recommendations that should be recognised as obviously harmful to the user given the context provided. Key failure modes include inappropriate weighing of conflicting preferences, sycophancy (prioritising user preferences above safety), a lack of attentiveness to critical user information within the context window, and inconsistent application of user-specific knowledge. The same systematic biases were observed in OpenAI's o1, suggesting that strong reasoning capacities do not necessarily transfer to this kind of personalised thinking. We find that prompting LLMs to consider safety-critical context significantly improves performance, unlike a generic `harmless and helpful' instruction. Based on these findings, we propose research directions for embedding self-reflection capabilities, online user modelling, and dynamic risk assessment in AI assistants. Our work emphasises the need for nuanced, context-aware approaches to alignment in systems designed for persistent human interaction, aiding the development of safe and considerate AI assistants.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper designed a benchmark for evaluating the alignment ability of LLMs while interacting with a specific human agent within a conversation. The key idea and novelty of the benchmark is the focus on the safety aspect of the dialogue. For example, if the human mentions a physical limitation that may forbid his participation in some activities, can the LLM make correct suggestion even after the conversations grow? 

The evaluation is across 6 models, 5 scenarios each with 337 examples. A summary of main takeaways:
* Most models are not good at suggesting the right decision while recalling the human's previously mentioned safety information, especially when there are more human with conflict preferences that may mislead the models' decisions.
* Guilding prompt make things better, e.g. “Consider my personal risks, sensitivities and constraints when you make recommendations for me".

### Strengths
* Evaluating safety-critical contexts is a timely and important problem for developing LLM-agent. The angle of evaluating this concept in conversations is a novel contribution.
* The paper is overall well written with clear outlines for contributions and overall clear statements of the experiments design.
* The paper presents detailed failure modes such as sycophancy, inconsistent prioritization of conflicting preferences, and inattentiveness to critical user-specific details. Such an analysis identifies an important next step on improvements in AI systems.

### Weaknesses
 * Evaluations: Both the datasets and the evaluations are done by an LLM (Claude 3.5). Especially for the evaluation, is there any valid human checking involved? How can we ensure that the design and evaluations are not potentially biased to a particular model, e.g. a model that is more similar to Claude?
* Data: Overall, the dataset is small and a little restrictive, as mentioned in section 6. And only 6 models are tested. I see that the ideas and takeaways can be generalized to similar settings. However, the experiment results and data may not be sufficient for evaluating future models. For example, as the size of the models grows, both the length of the conservation and the size of the data can become rather limited. 
* Generalizability: In line with the previous point, although the safety aspect of LLMs is an important dimension for evaluation, the current focus of the paper  is limited to "whether LLM suggestions may conflict with the human's personal limitations". In practice, however, decision makers are usually very much aware of what they can do and cannot do conditioned on their physical limitations. From this aspect, the effort of improving LLM abilities in recalling the human's physical limitations seems to be a secondary concern per se. A more general problem might be "the LLM may forget a key concept mentioned in a conversation and make imperfect suggestion". However, how much does the current results generalize to these questions is questionable due to the limited data and scenarios. 
* A minor suggestion: In the result section, it might be interesting to connect the findings in the previous benchmarking papers of the similar setting (conversation setting) with the current results. For example, is it the case that the LLMs perform well in the previous work in the conversational setting also perform well in the current setting?

### Questions
Please see waknesses. In particular, I hope the authors can add more to the generalizability of the results.

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
3

### Summary
This paper introduces CURATe (Context and User-specific Reasoning and Alignment Test), a benchmark designed to evaluate large language models (LLMs) for their ability to remember and appropriately handle safety-critical, user-specific information in multi-turn conversations. CURATe highlights the limitations of existing models when tasked with maintaining personalized alignment, especially in situations that require balancing safety with conflicting preferences. Through testing on multiple LLMs across scenarios involving severe allergies, phobias, and other safety-critical conditions, CURATe reveals systemic challenges in user-specific alignment and proposes directions for future research in dynamic risk assessment, user modeling, and empathetic reasoning.

### Strengths
The paper introduces:

* A Novel Benchmark for Personalized Safety Alignment: CURATe fills a significant gap in the literature by assessing LLMs' ability to recall and prioritize safety-critical user information within conversational contexts, a feature that goes beyond the typical "helpful and harmless" paradigm.

The benchmark is also comprehensive: The benchmark is extensive, with multi-turn scenarios that simulate realistic challenges in conversational AI, such as managing conflicting user preferences and assessing safety risks.

The paper draws conclusions into failure modes and shows how the benchmark can be used for ablating sources of performance changes (e.g. Figure 4)

### Weaknesses
 * Lack of human annotator calibration of the LLAMA 405B used for rating. Though it is interesting to see the difference in pass rates between frontier models along the scenarios introduced, it is difficult to interpret these results without knowing how ewell the LLAMA ratings align with human 'ground truth' ratings. 
* I would recommend adding a table or figure documenting illustrating the 5 scenarios. What exactly the scenarios are / how they differ is hard to glean from the text. The sentence "In scenarios 2-4, the preferences of other actors are introduced that (1-3) directly conflict with the user’s constraints (e.g., “My partner absolutely loves/would be thrilled by/has always wanted to...”), incrementing at each scenario (within the same conversation turn). In Scenario 5, three users with random, unrelated preferences are introduced instead." is difficult to understand.
* The appendix seems incomplete -- A 1.2 is missing content 
* If the benchmark isn't being released, this is a significant weakness of the paper

### Questions
* Is the benchmark being released? It would be a valuable contribution to the modeling community.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents the results of the evaluation of 5 popular LLMs on a personalized alignment task, using a dataset created by the authors described in the appendix and an LLM evaluator to classify the answers. It shows, as much as possible considering the methodological flaws, considerable shortcomings of those models in handling more complex situations.

### Strengths
It is important to consider HHH in a personalized context, and I commend the authors for tackling the problem. So often HHH is considered in a very generic way, as if everyone is the same and there no cultural contexts.

### Weaknesses
This paper has many problems, starting from the writing. A lot of stuff was moved to the appendix without even proper pointing from the main paper. For example, this is a paper proposing a new benchmark, and no mention about how it was created is made in the main text. I had to look for that information in the appendix. Similarly, the 5 scenarios, a critical part of study, are very briefly described in two small paragraphs, and clearly require more discussion.

The main problem with the paper is that the CURAte benchmark has very limited quality. Since it was generated by an LLM (Claude?) it is very formulaic, very repetitive, nothing like something generated by human beings. For instance, all instances of severe allergy and severe phobia starts with the "I have a severe....", all questions with "Do you think...". If the authors are serious about proposing a benchmark for HHH, entries should be generated by people and curated carefully to avoid mistakes, common-sense errors, etc. Using LLMs to create benchmarks is a dangerous way to move forward with LLM evaluation, and this paper is unfortunately a typical case of incorrect approaches to benchmark creation.

Similarly, the authors use an LLM (LLaMa 3.1. 405B) to judge the results of the other LLMs, assuming that it is able to do so. Using LLMs to evaluate HHH results is very dangerous, especially in this case of difficult scenarios, so the authors should have started showing that LLaMa is in fact good at this task by sampling the evaluations and run a human evaluation of the results. This would give an idea of the level and quality of the errors introduced by using an LLM-based metric, and allow a better and fairer assessment of the results of using it as an evaluator of other LLMs.

In summary, benchmark creation and validation is an area where human input, with strong methodology, is absolutely critical. This paper fails to do so, and ICLR should not endorse benchmark creation with methodological flaws.

### Questions
1. How good is LLaMa in evaluating the other LLMs performance? Did you manually check the results? How often and how does it fail?
2. Why did you not instruct Claude to be more diverse in the dialogue generation?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a benchmark called Curate, designed for evaluating personalized alignment for AI assistants focusing on user-provided safety-related information (e.g. allergy, phobia) multi-turn conversations. Authors evaluated six models e.g. GPT-series, Llama-3, Llama-3.1 on five scenarios (e.g. no added persons, one person with conflicting preferences in conversation). They found that the models that trained by the “harmless” paradigm fail to consider the harmful elements (based on users provided content) and hence give inappropriate recommendations. For example, models fail to weigh the conflicting preferences of different users and models prefer to give recommendations that align with soft user preferences over safety. They also propose some future research directions for model alignment, such as context-aware approaches.

### Strengths
1. Constructed an interesting benchmark that addresses important problems (preference vs safety) on AI alignment through multi-turn conversations. 
2. Good designs on experiments (changing the number of persons) and the ablation studies (changing the prompts).
3. Provide detailed discussion on the current alignment strategies (RLHF)

### Weaknesses
1. Not enough description on benchmark construction and statistics, which reduces the usability of the benchmark. I can only find some parts of the benchmark design process in the Appendix. It is important to have information such as: (1) the prompts used to generate such benchmark (by few-shot prompting), (2) distribution of the 337 use cases on the four categories (trauma triggers…), (3) why the choice to have 337 use case and four categories (4) descriptive statistics: how many turns of conversations etc
2. Linkage between experiment and discussion is weak. It is hard to understand why the findings from experiments and ablation can inspire the discussion (Section 5). For instance (line 462-463) , it’s confusing how the authors make logical steps between our findings (which findings?) → reveal the sycophancy → non-safety-critical preference (I thought the benchmark only has safety-related categories?) → systematic bias (missing example?)
3. No human validation on the evaluation metrics by LLM-as-judge. It is known that the model being used to evaluate favors the responses generated by itself [1]. Authors used the Llama-3.1-405 instruct as the judge. The findings of model performances (specifically the better performance by Llama-3.1-405 instruct) is not convincing without validating if the model judge gives reliable scores.
4. Some claims are overly strong (e.g. line 467: the very notion of ‘harmlessness’ in the HH framework is fundamentally flawed.). I can see the importance of considering the context on aligning harmlessness but it does not sound fair to say the notion is fundamentally wrong. This discussion could be better grounded with some current works on reward models/RLHF-alternatives (e.g. HelpSteer2 [2], SteerLM [3] – consider the graded rewards with contexts) and value alignments works (DailyDilemma [4], Pluralistic alignment [5])

### Questions
Questions:
1. The passing rate by line 252 is confusing: do you mean only score 2 will be classified as passing or both scores (1 and 2) will be classified as passing?
2. The focus on "personalization" sounds more closely related to the soft preferences (e.g. style) and may dilute the contribution of this work. Plus, the benchmarks (based on the four categories names in Figure 13 e.g. Trauma triggers) is more about health and safety. Maybe consider renaming the title/reframe the paper to sharpen the health-related safety aspect?

Minor:
1. Many of the citations in the main paper have wrong formatting. ABC et al. (2024) → (ABC et al., 2024)
2. The legends in figure 2 and figure 3  are confusing. Both are named as Scenarios but one is the variation of benchmarks scenarios and another one is the variation of ablation.
3. Appendix p.16 does not contain the Example Completions. Is it due to the formatting issue?

### Soundness
3

### Presentation
3

### Contribution
3
