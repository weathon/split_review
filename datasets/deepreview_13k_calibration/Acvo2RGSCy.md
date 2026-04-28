# DeLLMa: Decision Making Under Uncertainty with Large Language Models

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
\vspace{-1mm}
The potential of large language models (LLMs) as decision support tools is increasingly being explored in fields such as business, engineering, and medicine, which often face challenging tasks of \textit{decision-making under uncertainty}.
In this paper, we show that directly prompting LLMs on these types of decision-making problems can yield poor results, especially as the problem complexity increases.
To aid in these tasks, we propose  DeLLMa (Decision-making Large Language Model assistant), a framework designed to enhance decision-making accuracy in uncertain environments.
DeLLMa involves a multi-step reasoning procedure that integrates recent best practices in scaling \textit{inference-time reasoning}, drawing upon principles from decision theory and utility theory, to provide an accurate and human-auditable decision-making process.
We validate our procedure on multiple realistic decision-making environments, demonstrating that DeLLMa can consistently enhance the decision-making performance of leading language models, and achieve up to a 40\% increase in accuracy over competing methods. Additionally, we show how performance improves when scaling compute at test time, and carry out human evaluations to benchmark components of DeLLMa.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors  propose  framework to work with LLMs for decision making under uncertainty; in doing so, they take classical utility/decision theoretic framework as a design guideline: (1) they enumerate first all the states. (2) estimate the probability of those states (3) elicit the utility function from the user, and (4) choose the one that maximises expected utility.   They show their results working with various LLM and in various settings; different preference ranking strategies (pair by pair vs. top1) against benchmarks of zero shot and CoT in two real world  decision problems (one in agriculture the other in stocks investment) and show that they their framework helps with the results significantly. Also considered are ablation studies (on  things such as overlap percentage (of minitibatches in drawing from state-action samples) and sample size, human agreement etc ). Approach also comes with the decision trees naturally, hence making the whole process more explainable.

### Strengths
- Exposition and writing  in general is in  good condition. (There are small rooms for improvement in organisation and clarification.)

- The whole framework is written with careful formal details, thanks to taking decision-theoretic frame, which is a great idea to start with.

-  The results on improvements are powerful; also has high impact potential  due to popularity of prompt engineering in LLMs. The idea is novel and justifiable (with some inherent difficulties and pitfalls ).

- The depth of the analysis and various ablation studies is a strength. 

- The framework also provides (to some extent) an explainable medium which is a strength.

### Weaknesses
 - Content-wise: Unfortunately, too many reference to appendix in many crucial points. This is of course due to  tight page limitation, but authors should seriously think about re-arranging the text more complete. For instance explanations for Table 2 , 3 and 4 really not sufficient (page 10 only call their names without telling what they are).  It seems like the paper would serve much better as a journal publication or other venues with more page (e.g., ICML).  Related: Say also that Figure 11  is in appendix actually.  They try to provide too much (for instance human evaluation at best a study on its own, or should be at least extended to present something substantial)

- On the technical side there are strong assumptions and unclarities:  the assumption of independence between k-latent factors is very strong, and  actually hard to maintain,  also due to natural language part of things.  As a result, uncertainty in the estimation step is taken very crisp, it is pretty difficult to ensure whether these scores are reflecting reality. There is a section called: "How good are state forecasts" (which is a good to have section), however I am not sure it reaches its goal:  This is inherently difficult. They show table 1: claiming two metrics they showing "good results" is hard to justify since we don't know reference to what (maybe its my misunderstanding.) Why are these reasonable? Also the same section, manually annotating a set of ground truth values, how to get it, etc, not very clear to me. 

- Less problematic is the issue of  the number of alternatives are known (coming from the context or imposed to LLM) is a strong working assumption, and undermines  real world settings applicability. 

-Another major issue is the part with Table 4 (human evaluation): this is a nice to have I agree, however, if you go for it then it should  be done in a state that does not weaken the paper. Currently, as explain this is just done by authors, of which we don't know how many, say 4 or 5 on average. Is this result than solid? It is problematic for two reasons: 1)  It should be done not by authors  but by a handful of people (who has nothing to do with paper acceptance) 2) not clear how does it compare to sole human comparison 3) amount of people matters: what if it was a single author paper (I assume it is not due to their expression). What is the standard deviation, significance level  or other statistics on these values? Without all these things , it would be pretty difficult to publish this in even a low-rank psychology journal. And yes, this venue is on rather AI but we still should maintain some sensible quality on experiments if we are to show that. Currently, it just serves only as good as an anecdote.  (Question)

- It is shown to have much better performance against OpenAI's o1 model, but which DeLLma is used is not clear. (Question) 

-  Organisation wise  the DELLMa main picture (there is no name unfortunately for the figure btw to refer to it, but perhaps understandable) comes before the explanations in 3.1 and other sections and create questions immediately. This is a very minor issue. 

-Unclarities in  Page 9, Main results, second paragraph is not satisfying:  The vagueness of explanation is not a weakness per se since authors are careful to call these as hypotheses. Yet, the difference on phenomenon is very small, and now we enforce ourselves to explain the phenomenon, and likely we hallucinate ourselves.  The result can be much more simple: the amount of data considered, and the processing capacity of the model "can be" pretty much be  a reason that top 1, simplifies it much better compared to other.   Also see that when number of alternatives is 5 it already performs better, which might be due to a particular alternative. Relatedly the wayt the average is taken matters: 1) some difficulties might be due to assessing particular actions (are these scores are evaluated permuting through all the alternatives? (E.g., which 2 actions matters)?) 2) averaging across the accuracy score of  different size of scores matters. There I would go for higher weight to the higher number of actions.  These subtleties are unfortunately not clear, (question)

-Mini typo: availble fruits.

### Questions
See the points above as "(question)". Happy to read your take.

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
4

### Summary
This paper proposes DeLLMa (decision-making LLM assistant) to maximise the utility in decision problems, i.e., agriculture planning and finance. DeLLMa consists three steps, 1) based on in-context information, infer and forecast related unknown variables, 2) elicit the utility function which aligns with the user's goals, 3) use the elicited utility function to make the best decision which maximise the expected utility.   Authors claim that DeLLMa is motivated from chain of thoughts and tree of thoughts, but is faster at the inference time especially in the scalability.

### Strengths
- Clearly explain the main concept of DeLLMa as illustrated in Figure 1.
- Capture LLM in decision making with a triplet P=(G, A, C) and four steps, where G is the user goal inferred from the description, A is a list of actions, and C is the contextual information. 
- Include two ranking types: pairwise and top-1.
- Provide clear prompts and code in the appendix.

### Weaknesses
 - Inferring the user’s goal from the context is done by the LLM, which requires the user to have a clear goal in mind. For example, if the farmer has not decided to plant only one type of fruit, DeLLMa may not know how to handle an implicit multiple-fruit situation.
- The applicable scope of DeLLMa is limited. The experiments include only agriculture and stocks, which may mislead readers into thinking DeLLMa generalises across all decision-making tasks.
- There is little information about human agreement; the paper states that the authors served as human annotators, but details are missing.

### Questions
- How will DeLLMa perform on other tasks related to chain-of-thought or tree-of-thought methods discussed in related work?
- If scalability is not a significant issue in certain cases, will DeLLMa outperform other methods?
- In the experiments, one task involves investing on December 1, 2023, and selling on the last trading day of that month (December 29, 2023) to maximize returns. Why were these specific dates chosen? Why not other dates?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces DeLLMa for better decision making by LLMs under uncertainty. It uses a multistep process to achieve this, based on decision theory - state enumeration, forecasting, then utility elicitation and expectation maximization. Then the paper applies this to agro and fin scenarios - showing good improvement over baselines (zero shot, CoT etc). Finally the paper shows that this method generalizes across LLMs and is human auditable.

### Strengths
Originality - the paper is quite original, and the proposed pipeline is creative. I have not seen this multistep approach used with LLMs anywhere before.

Quality - I found the method to be quite well motivated and well presented. The paper is reproducible, and the experiments seem cohesive and well-motivated.

Clarity - The paper is well articulated and clearly structured.

Significance - The paper is definitely an important step in the right direction. Uncertainity quantification in ML has been an active area of research and I am curious to see how this is furthered with LLMs. However I feel that the method has limited applicability to real world scenarios.

### Weaknesses
1. The context window of LLMs clearly limits the state and action spaces, which makes this method of limited real world applicability.
2. It appears that the method is very sensitive to the first state forecasting step. While the method is robust in general, I would like to understand if this is indeed a big bottleneck.
3. The utility elicitaiton method proposed (pairwise ranking) seems a bit too simple for real world scenarios. I would like to know if other methods were tried for this.

### Questions
1. How can DeLLMa be adapted to handle continuous state and action spaces? 
2. The state forecasting method assumes independence bw latent factors. How does this impact total performance?
3. Is DeLLMa able to handle cases where the user task cannot be distilled into a hard utility function?

### Soundness
4

### Presentation
3

### Contribution
3
