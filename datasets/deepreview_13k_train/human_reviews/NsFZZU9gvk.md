# Aligned LLMs Are Not Aligned Browser Agents

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Despite significant efforts spent by large language model (LLM) developers to
align model outputs towards safety and helpfulness, there remains an open ques-
tion if this safety alignment, typically enforced in chats, generalize to non-chat
and agentic use cases? Unlike chatbots, agents equipped with general-purpose
tools, such as web browsers and mobile devices, can directly influence the real
world, making it even more crucial to ensure the safety of LLM agents. In
this work, we primarily focus on red-teaming browser agents, LLMs that in-
teract with and extract information from web browsers. To this end, we in-
troduce Browser Agent Red teaming Toolkit (BrowserART), a comprehensive test
suite consisting of 100 diverse browser-related harmful behaviors and 40 syn-
thetic websites, designed specifically for red-teaming browser agents. Our empir-
ical study on state-of-the-art browser agents reveals a significant alignment gap
between the base LLMs and their downstream browser agents. That is, while
the LLM demonstrates alignment as a chatbot, the corresponding agent does not.
Moreover, attack methods designed to jailbreak aligned LLMs in chat settings
transfer effectively to browser agents - with simple human rewrites, GPT-4o and
GPT-4 Turbo -based browser agents attempted all 100 harmful behaviors. We plan to publicly release BrowserART and call on LLM developers, policymakers, and agent developers to collaborate on enhancing agent safety.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article introduces BrowserART -- a red teaming framework for evaluating the safety of LLM-based browser agents. The authors contribute a set of 100 harmful behaviors. A red team is expected to convince the evaluated LLMs to perform these harmful behaviors. The article evaluates eight LLMs in several settings. The two main setups are a plain chatbot and a browser agent. The authors show that as chatbots, the LLMs are more resilient to requests for misbehavior. An additional set of conditions includes several commonly acceptable jailbreaking techniques shown here to increase agents' misbehavior dramatically.

### Strengths
* Evaluating the misbehavior of LLMs in different conditions is important 

* The idea that an LLM may talk and act differently (as humans commonly do) is great!!

* As a red teaming effort, the study achieves remarkable results

### Weaknesses
 * Substantial and important experimental details are missing 
(system prompts are not specified, 2-3 complete specific examples of scenarios provided to both agents and chatbots, details on the tooling of agents). 
Examples of prompts are provided in Fig 1. Fig 4, and Appendix B. Only Fig 1, presents a single pair of prompts one of which is expected to fail and the other not. Please provide a few examples from your dataset that any reader can try in a chat.

The system prompt is only mentioned in the context of agents when discussing the context length. The system prompts have determining effect on LLMs' behavior. Therefore all chat and agent system prompts need to be normalized. If using the exact same prompts is not possible then the differences should be disclosed and discussed.

The authors state that they rely on OpenHands for the implementation of the respective agents. However, to make the paper self-contained, some important details related to the browse agent design are missing. For example, which tools are provided to the agent to perform their task? Assuming a full-fledged agent, the tooling should be extensive. Extensive tooling also implies extensive system prompt which may introduce more confounding factors into the agent behavior. Essentially, if the paper claims that it is "morally easier" for an LLM to do a thing (as an agent) rather than to say it (as a chatbot), this claim should be evaluated with the simplest possible agent. 
Would an agent equipped with a single tool, e.g., posting a tweet, write in that tweet something that it would not write in a chat? -- of course, when everything else (including the system prompt) remains the same.


* Chatbots and agents are evaluated under different conditions 
(differences in queries, different system prompts)
 
* Following from the previous point, the differences in behaviors cannot be undoubtfully attributed to LLM task (chat vs. agent)

* Clarity of the main goal/purpose of the study. 
It is not clear whether the primary purpose of the article is to introduce the BrowserART system or to study the behavior of aligned models? 
Which objective is the main one and which is a side track is important to put the right focus on evaluation.

I believe that the attempt to incorporate more contributions by adding the jailbreaking experiments actually harms the paper -- at least if the main focus is comparing agents to chatbots. This significant additional evidence does not contribute to the main question. It also takes precious space and does not allow a deeper comparison of chatbots vs agents. In case both the current title and the jailbreaking experiments remain then the paper must report the behavior of the chatbots under the same jailbreaking conditions as agents. 

Alternatively, if the main focus is shifting toward introducing BrowserART and chatbots vs. agents as a side observation, then (1) it requires major rewrites, and (2) comparison to chatbots could naturally be reported only in one of the experiments. Of course, even if the focus is shifted, it is expected that this one experiment would compare chatbots and agents under the same conditions.

### Questions
Can the difference in behavior be attributed to different details provided to the agents (to perform their tasks) and not provided to the chatbots? 


What are the differences in chat/agent system prompts, and how significant are these differences?


How would the LLM respond to the instructions with actuation details while lacking only the necessary tools (e.g. to access Gmail)?


How do chatbots react to the same attacks attempted on agents?


Is the primary purpose of the article to introduce the BrowserART system or to study the behavior of aligned models? 
Which objective is the main one and which is a side track?

### Soundness
2

### Presentation
4

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
The authors curate a dataset to assess the willingness of LLM-based agents to attempt harmful behaviors when interacting with a browser. The authors focus on the substantial within-model difference in behavior between chat- and agent-based deployments. They assess these behaviors using both a text- and an image-based browser framework.

### Strengths
Originality: moderate.
Quality: high. Well-chosen, well-scoped hypothesis. Meaningful controls.
Clarity: high. Analyses are well-reasoned and well-presented.
Significance: high. If these results hold, it is a clear call to action to model developers with a demonstrated, focused

### Weaknesses
Noticeable grammatical mistakes.

### Questions
It would be great to assess the performance of Sonnet 3.5 with computer-use and compare it to the previous version of Sonnet 3.5. Does it seem that Anthropic has identified and/or meaningfully addressed this safety concern in its internal testing?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a benchmark that consists of 100 harmful behaviors for red-teaming web agents. The experiments on two types of web agents demonstrate that the web agents are not well aligned even though their underlying model is aligned. Also, existing jailbreaking attacks can transfer well to the agent setting.

### Strengths
1. I believe red-teaming web agents is an important direction. Although lots of concurrent works have already been released, the authors are the first, to the best of my knowledge, to propose such a benchmark by the deadline of paper submission. Therefore, I believe this is one of the earliest works in this direction.

### Weaknesses
1. The paper severely lacks a comprehensive literature review and comparison against existing red-teaming methods for agents. There has been a bunch of related work in this domain, such as [1]. At least some discussions should be provided to demonstrate the difference and novelty of the proposed toolkit.

2. The benchmark is relatively too small, contains only 100 examples, and from my understanding, is not scalable. Also, the hierarchy of risk categories is not well-supported. There have been a lot of safety regulations or risk categories proposed by companies, governments, or researchers, such as [2]. However, the hierarchy here is only a small subset. As a result, the benchmark is not comprehensive.

3. The red-teaming method introduced in the paper lacks novelty. Most examples are manually crafted or transformed from existing examples, and there is no automated way of doing that (or at least not mentioned by the authors). Is it possible to formalize an algorithm to automatically perform red-teaming? Are there any specific characteristics of web agents that should be considered when red-teaming web agents instead of the LLM? Have the authors made efforts to make the existing jailbreaking attacks more effective against agents? Simply designing 100 examples for red-teaming does not bear enough novelty.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces and publicly releases Browser Agent Red teaming Toolkit (BrowserART), a test suite for evaluating the safety of browser-based LLM agents. The authors compile 100 browser-related harmful behaviors + 40 synthetic websites to test if safety-trained LLMs maintain their guardrails when used as browser agents. Their experiments reveal a significant drop in safety alignment between LLMs and their corresponding browser agents, with browser agents more likely to execute harmful behaviors. The paper also demonstrates that existing techniques for jailbreaking LLMs transfer effectively to browser agents.

### Strengths
- Addresses an important, emerging, and under-explored area of AI safety: LLM-based browser agents.
- Promotes collaboration on improving LLM agent safety by publicly releasing Browser ART with 100 harmful behaviors and 40 synthetic websites.
- The paper is well-structured and clearly written.
- Clearly demonstrates that standard safety training of LLMs does not necessarily transfer to browser agent applications.
- A range of SOTA LLMs are evaluated including models from the OpenAI GPT, Anthropic Claude, Meta Llama, and Google Gemini families.

### Weaknesses
No substantive weaknesses.

While the paper identifies the gap in alignment when LLMs are used as browser agents, it does not investigate the underlying reasons. More analysis on why browser agents are more vulnerable could provide valuable insights.

### Questions
- Have you investigated the alignment gap in other kinds of AI agents beyond browser agents?
- What specific changes to LLM safety training do you believe could help address the alignment gap observed in browser agents?

### Soundness
3

### Presentation
3

### Contribution
3
