# Seeker: Enhancing Exception Handling in Code with a LLM-based Multi-Agent Approach

- Decision: Reject
- Scores: 1, 5, 3

## Abstract
In real-world software development, improper or missing exception handling can severely impact the robustness and reliability of code. Exception handling mechanisms require developers to detect, capture, and manage exceptions according to high standards, but many developers struggle with these tasks, leading to fragile code. This problem is particularly evident in open-source projects and impacts the overall quality of the software ecosystem.
To address this challenge, we explore the use of large language models (LLMs) to improve exception handling in code. Through extensive analysis, we identify three key issues: Insensitive Detection of Fragile Code, Inaccurate Capture of Exception Types, and Distorted Handling Solutions. These problems are widespread across real-world repositories, suggesting that robust exception handling practices are often overlooked or mishandled.
In response, we propose \emph{Seeker}, a multi-agent framework inspired by expert developer strategies for exception handling. Seeker uses agents—Scanner, Detector, Predator, Ranker, and Handler—to assist LLMs in detecting, capturing, and resolving exceptions more effectively. Our work is the first systematic study on leveraging LLMs to enhance exception handling practices, providing valuable insights for future improvements in code reliability.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces Seeker, a tool for generating exception handling code with LLMs. Seeker is based on a multi-agent system that first locates the code location that needs exception handling, then performs RAG on a dataset of existing exception handling code, and finally generates the appropriate exception handling code. Seeker contributes to the standardization, interpretability, and generalization of automated exception handling generation.

### Strengths
- Some preliminary studies seems to be conducted to guide the development of Seeker.

### Weaknesses
 - Paper writing is quite bad, to be honest, looks like automatically generated without much polishing. I have very hard time to follow the main contributions of this paper. Many terms are mentioned without proper explanation.

- The contribution is more on the engineering side than research. Namely Seeker is a combination of existing techniques: agent framework, RAG, few-shot learning, etc.

- Experiments were performed on a very limited number of open-source repositories, limiting the validity of the results.

- lines 75-86: I cannot follow the concern about the "standardization" of existing exception handling techniques. What does it mean exactly, can you give an example?

- How did you come up with the "chain-of-thought used by senior human developers" in Figure 1(b), is it from user studies / interviews, or from any prior work? Also, it is hard to tell any valuable information from the figure, which is basically putting together a random set of buzz words.

- line 155-161: Can you specify how many codebases (repositories), code reviews, and exception handling examples have you studied in the preliminary study? What does "implementation results" mean?

- line 162-170: When you talk about these phenomena, specifically when mentioning things like "prompts without effective guidance information" "increasing the interpretability" "increasing the generalization information", can you specify which prompts you are referring to or comparing between? It is hard to map the four kinds of prompts with your text.

- The four kinds of prompts seem to be a key part of the technique. Looking at their definitions in Section 3.2 and the examples in figures 4 and 5, where do you get the specific exception types, code-level scenario analysis, and the handling strategy, for the Fine-grained {Reminding, Inspiring, Guiding} prompts, respectively? From the examples it looks like they are generated based on existing exception handling code snippets, but what happens when we apply your technique to new codebases without any existing exception handling code snippets?

- line 264-266: these are not three ways of "handle" exceptions. The throw keyword in the method signature is to declare a possible exception, the throw keyword in method body is to actually throw an exception, and only the try-catch block is for handling an exception.

- The steps in Seeker is not consistent. In Section 1 it was described as "Scanner, Detector, Predator, Ranker, and Handler", but in Section 3.3 it changes to "Planner, Detector, Predator, Ranker, and Handler".

- You are introducing several techniques/algorithms, namely "Common Exception Enumeration (CEE)" and "Deep Retrieval-Augmented Generation (Deep-RAG)", very superfically in the main text, and immediately redirect to the appendix. Please don't do that---the main text should be self-contained, so at least include some basic details and examples to explain how they work. I did check the part of appendix talking about CEE and Deep-RAG, but my impression is that they're just engineering contributions hidden behind the fancy word---CEE = few-shot learning, and Deep-RAG = a for loop doing RAG multiple times. Please correct me if I'm wrong.

- line 433: what is the CodeReviewModel you are using here to compute Automated Code Review Score?

- line 482: how is Code Review Score (6th metric) different from the Automated Code Review Score (1st metric)?

- line 486-490: In your experiment dataset, is there any overlapping between your evaluation examples and the examples used for RAG?

### Questions
- lines 75-86: I cannot follow the concern about the "standardization" of existing exception handling techniques. What does it mean exactly, can you give an example?

- How did you come up with the "chain-of-thought used by senior human developers" in Figure 1(b), is it from user studies / interviews, or from any prior work? Also, it is hard to tell any valuable information from the figure, which is basically putting together a random set of buzz words.

- line 155-161: Can you specify how many codebases (repositories), code reviews, and exception handling examples have you studied in the preliminary study? What does "implementation results" mean?

- line 162-170: When you talk about these phenomena, specifically when mentioning things like "prompts without effective guidance information" "increasing the interpretability" "increasing the generalization information", can you specify which prompts you are referring to or comparing between? It is hard to map the four kinds of prompts with your text.

- The four kinds of prompts seem to be a key part of the technique. Looking at their definitions in Section 3.2 and the examples in figures 4 and 5, where do you get the specific exception types, code-level scenario analysis, and the handling strategy, for the Fine-grained {Reminding, Inspiring, Guiding} prompts, respectively? From the examples it looks like they are generated based on existing exception handling code snippets, but what happens when we apply your technique to new codebases without any existing exception handling code snippets?

- line 264-266: these are not three ways of "handle" exceptions. The throw keyword in the method signature is to declare a possible exception, the throw keyword in method body is to actually throw an exception, and only the try-catch block is for handling an exception.

- The steps in Seeker is not consistent. In Section 1 it was described as "Scanner, Detector, Predator, Ranker, and Handler", but in Section 3.3 it changes to "Planner, Detector, Predator, Ranker, and Handler".

- You are introducing several techniques/algorithms, namely "Common Exception Enumeration (CEE)" and "Deep Retrieval-Augmented Generation (Deep-RAG)", very superfically in the main text, and immediately redirect to the appendix. Please don't do that---the main text should be self-contained, so at least include some basic details and examples to explain how they work. I did check the part of appendix talking about CEE and Deep-RAG, but my impression is that they're just engineering contributions hidden behind the fancy word---CEE = few-shot learning, and Deep-RAG = a for loop doing RAG multiple times. Please correct me if I'm wrong.

- line 433: what is the CodeReviewModel you are using here to compute Automated Code Review Score?

- line 482: how is Code Review Score (6th metric) different from the Automated Code Review Score (1st metric)?

- line 486-490: In your experiment dataset, is there any overlapping between your evaluation examples and the examples used for RAG?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses a critical issue in software development: the deficiencies in exception handling practices that lead to unreliable and fragile code. The authors propose a novel multi-agent framework called Seeker, which leverages large language models (LLMs) to enhance exception handling in programming, specifically within Java codebases. Seeker mainly has five dedicated agents: *Planner* to segment a given codebase into manageable units, *Detector* to identify fragile areas in the code, *Predator* to incorporate the external knowledge, *Ranker* to assign grades to the detected exceptions, and *Handler* to generate optimized code incorporating exception-handling strategies. Accordingly, this paper systematically identifies common pitfalls in exception handling and proposes solutions based on empirical studies of human developer practices. The empirical evaluation shows that combining comprehensive exception knowledge with a specialized agent framework as in Seeker, exception-handling code can be generated with adequate success.

### Strengths
- Presents the first systematic study of LLMs in the context of exception handling, which can better scale than all related work, to real-world scenarios.
- The integration of a Common Exception Enumeration (CEE) suggests that the framework can be widely adopted by developers, enhancing the robustness of code generation practices.
- The paper is well-written and easy to follow.

### Weaknesses
 - *Missing related work / potential baseline* [1]: Exception-handling code is highly project-specific. Accordingly, the cited work deals with the tasks of: (1) identifying code that can throw exceptions, (2) localizing the statements that belong to the try-block, and (3) identifying the exceptions the highlighted block can throw (everything but the objective of *Handler* in *Seeker*).
- *Limited Discussion on Evaluation Granularity*: Evaluation primarily focuses on overall performance metrics without a deeper discussion on the granularity of exception handling improvements. For instance, some code can throw multiple exceptions, or have multiple blocks that need handling. Further insights into specific types of exceptions and their handling would strengthen the findings.
- *Limited evaluation*: Gap between experiments and final conclusions drawn.

### Questions
1. How might the framework be adapted to evaluate exception handling at a more granular level?
2. How do the authors ensure that the handling strategies recommended by the Handler agent are not only correct but also optimal?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The work supports LLMs for exception handling by enhancing them with the seeker framework. The proposed framework has five agents for detecting, capturing and resolving exceptions.  Experimental results indicate that seeker gives better results as compared to other approaches based on multiple measures

### Strengths
- The area is interesting and important
- The approach is promising
- An empirical comparison with existing techniques is presented
- The appendix contains details of the method and experiments

### Weaknesses
 - I found the paper's flow to be quite confusing. It seems the author's had a lot of material to cover, most of which is placed in the appendix. Perhaps because of this, the actual paper lacks clarity and the required detail. It would be helpful if the authors present the material in the main sections, and refer to the appropriate appendix in case the reader wants further detail.
- There seems to be forward referencing in the paper. Material is introduced without proper explanation, and is explained in later sections e.g. Figure1
- The exact contribution(s) need to be written more clearly in the Introduction. Moreover, the material supporting the main contributions seems to be in the appendix and not the main sections e.g. deep-rag algorithm or discussion on the high concurrency.
- The experiments section seems to be defining the evaluation measures rather than focusing on an explanation of the experiments and results
- The authors mention that the superior performance of their approach can be attributed to several factors. However, it is not clear which factor is actually contributing towards the better results
- Some sentences are confusing e.g. in the first para of the Introduction: HumanEval() first proposed to let LLM generating code based on .......

### Questions
- The abstract mentions insights for future improvements in code reliability. Where are these discussed?
- The first paragraph of the Introduction discussed the importance of functional correctness of code and it's evaluation. It contains sentences that need to be re-written for describing the existing work more clearly
- What do you mean by the main peak area? 
- Where is the research question " Do we need to enhance the standardization, interpretability and generalizability of exception handling in real code development scenarios?" answered?
- The explanation of Figure 1 in the introduction is not clear
- How was the chain of thought in Fig 1b) developed? 
- Why is there a need of section 3.1 in Methodology?
- What is Figure 2 showing and where is it referred?
- In algorithm1, where is 'low nesting level' defined. What is meant by 'logical flow is clear'?
- What is meant by the 'thoughtful approach' of the planner?
- Is there a need to dedicate more than a page to defining the evaluation measures in the Experiments section?
- Where are the industry practices that were employed in the approach discussed?

### Soundness
2

### Presentation
2

### Contribution
2
