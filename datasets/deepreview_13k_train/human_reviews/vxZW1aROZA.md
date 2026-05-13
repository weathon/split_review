# EcoAssistant: Using LLM Assistant More Affordably and Accurately

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Today, users ask Large language models (LLMs) as assistants to answer queries that require external knowledge; they ask about the weather in a specific city, about stock prices, and even about where specific locations are within their neighborhood. These queries require the LLM to produce code that invokes external APIs to answer the user's question, yet LLMs rarely produce correct code on the first try, requiring iterative code refinement upon execution results. In addition, using LLM assistants to support high query volumes can be expensive. \system contains three components. First, it allows the LLM assistants to converse with an automatic code executor to iteratively refine code or to produce answers based on the execution results. Second, we use a hierarchy of LLM assistants, which attempts to answer the query with weaker, cheaper LLMs before backing off to stronger, expensive ones. Third, we retrieve solutions from past successful queries as in-context demonstrations to help subsequent queries. Empirically, we show that \system offers distinct advantages for affordability and accuracy, surpassing GPT-4 by $10$ points of success rate with less than $50\%$ of GPT-4's cost.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors present EcoAssistant, a framework for using existing LLMs to generate responses to invoke API calls in a cost effective manner and in a more autonomous manner.

### Strengths
- Having cost-effective solutions are useful and having this paper especially optimize for the cost is a useful strategy. 

- The authors present an intuitive system that's easy to replicate, and have shown useful empirical results.

### Weaknesses
 - I think this paper does suffer from lack of novelty. I think the paper does show an intelligent combination of existing techniques and models, but in my opinion it doesn't meet the threshold for a full paper. It would have been useful if the authors presented a methodology/algorithm that would help automatically optimize given a set of LLMs, or presented an empirical analysis on a much larger dataset with more complex APIs.

 - I think more error analysis would also be needed to identify what kind of queries are problematic for which models. For instance, if we can identify if smaller LLMs can easily answer easy queries then we don't need to ever invoke the larger LLMs - are you already doing this?

 - Can you help me understand how do you define an exit criterion? For instance, what if the agent gets stuck in an infinite loop where the larger LLM and the smaller LLM agent keep going back and forth?

### Questions
- How does this method scale with # of APIs? For instance, the ToolLLM[1] paper had >16,000 APIs in their dataset. This would require some shortlisting using a retriever to make it compatible but I think adding that part would significantly help improve the novelty aspect of the paper.

- I think more error analysis would also be needed to identify what kind of queries are problematic for which models. For instance, if we can identify if smaller LLMs can easily answer easy queries then we don't need to ever invoke the larger LLMs - are you already doing this? 

- Can you help me understand how do you define an exit criterion? For instance, what if the agent gets stuck in an infinite loop where the larger LLM and the smaller LLM agent keep going back and forth? 


References

[1] Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., ... & Sun, M. (2023). Toolllm: Facilitating large language models to master 16000+ real-world apis. arXiv preprint arXiv:2307.16789.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework, EcoAssistant for LLMs to generate API calls for answering user’s queries that require external knowledge. The framework consists of three components: iterative refinement based on automatic feedback from executors; a priority queue of LLMs where cheaper LLMs are used first; cache previously high-quality response as demonstration for further generation. The resulting system demonstrates better performance, and it’s more cost-efficient.  

Overall, the design of EcoAssistant makes a lot of sense, but it lacks novelty and research depth considering many related work in this direction.

### Strengths
- clear presentation of the framework and results
- significant empirical improvement

### Weaknesses
 - EcoAssistant relies on a set of known techniques (e.g., iterative refinement, demonstration library), the system per se is not novel from the technical perspective.
- from the research perspective, it does not investigate (or focus on) several key problems in this system: 1) how do you reliably collect feedback from executors? are the automatic feedbacks reliable, 2) how to decide whether a generated response is good enough to be put in the demonstration library, 3) how to design the policy for back off in the general case?

Overall, I think the design of EcoAssistant is not a significant contribution, and the authors do not go further beyond showing the empirical results of it. Though cost-efficiency is an appealing property, it’s very unclear to me what the back-off policy looks like in general.

### Questions
how do you decide whether a response is a success or not?  is it based on execution error?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an economically efficient language model agent that can interact with API. It incorporates three techniques: 1) conversationally interact with the execution environment, 2) saves cost by using a hierarchy of LLM assistant, 3) using successful demonstration as the in-context examples. Empirical results show that the proposed approach is indeed effective.

### Strengths
The paper proposes an economically efficient system that can interact with APIs via code. The empirical results look convincing to me.

### Weaknesses
This paper delivers a good system and represents a reasonable engineering contribution. However, I am a bit skeptical about its novelty: while probably no one has combined all these three tweaks together before, each of them seems relatively straightforward to me. Can fellow reviewers comment on the novelty for each of the three tweaks? 

(sorry that I am not following the related works very closely so I do not know exactly how novel these ideas were; however, I think they are very straightforward ideas to try after gpt-4 release and does not require conceptual innovations)

### Questions
- Would you mind commenting on the novelty of the proposed approach, or say, the most surprising part of this paper? Thanks!

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
