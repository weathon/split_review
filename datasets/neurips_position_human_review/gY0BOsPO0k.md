# Falsify, Don’t Just Discover - AI Generated Discoveries are NOT Born Scientific

- Decision: Reject
- Scores: 3, 6, 7

## Abstract
Rapid development of artificial intelligence has drastically accelerated the development of scientific discovery. Recently, the rise of Large Language Models (LLMs) has led to the prosperity of autonomous agents, which enable scientists to seek references at different stages of their research. The demonstrated autonomy of these agents has led to designations such as "AI Scientist". However, it remains an open question whether we have truly reached the stage where scientific discovery can be fully automated. In this paper, $\textit{we posit that automated scientific discovery needs \textbf{automated falsification}}$, which has not received sufficient attention in current research favors. As stated in Popper (1935), the central component of scientific research is falsification, where experiments are designed or theories are deduced to validate or refute hypotheses. To automate scientific discovery, the falsification process should also be studied towards full automation. We review the substance of falsification in each stage along the development of AI-accelerated scientific discovery, and analyze the subject, the object, and the degree of automation of the falsification process. Following this, we initiate $\textbf{Baby-AIGS}$, a proof-of-concept AI-generated discovery system enabled by automated falsification. Through qualitative and quantitative studies, we reveal the feasibility of automated falsification, and advocate for responsible and ethical development of such systems for research automation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The position paper considers automated scientific discovery, and suggests that the primary component of scientific discovery is ‘falsification’.  The authors then take the position that automated scientific discovery ‘needs automated falsification’.  Here, scientific discovery is generically considered to be hypothesis, followed by falsification, which is defined as the process where ‘experiments are designed or theories are deduced to validate or refute hypotheses.’  


The paper defines 4 levels of AI-assisted scientific discovery (Fig 2).  Discussion includes some comments on various literature of AI-assisted science, including optimization, mathematics, etc.  Table 1 lists some representative works and the degree to which they may have falsification.  The paper also presents a ‘baby step system’ to illustrate the ideas.  Some experiments are carried out where an agent helps search through various parameter choices in the specific problems studied.

### Strengths
The authors put forward the general idea that AI methods for scientific discovery will need AI methods for 'falsification' of ideas, in order to verify and validate AI reasoning. 

The paper builds and carries out experiments with several search-type problems, and automates ablation procedures to help find workable solutions in these specific simulation environments.  Automating ablation could be a very useful topic for study and developing general methods.

The work gives a lot of somewhat high level discussion of many existing AI based tools for various scientific and optimization applications.

The experimental portion may be of interest to researchers using AI tools for smart search in various applications, especially in a cycle of experimental design for optimization.The BABY-AIGS experiments could be useful to the community developing the various tools used in the experiment.

### Weaknesses
The paper starts from a very high level notion of scientific discovery as hypothesis generation, much like classical science.  It is then argued that somehow researchers exploring the use of AI methods to help with science and applications are not sufficiently embracing some form(s) of automated verification and validation.  Yet this seems to be clearly not true.  Virtually every ML paper uses metrics for success in one form or another, and similarly most ML papers contains ablation studies.

The paper doesn't make a convincing case for the position.  Any ML modeler or solver needs to have some kind of V-and-V, that depend on the specific context. E.g., the LLM programming and planning literature has many works that consider ways to verify and validate an LLM plan or program.  These naturally lead to feedback, prompt revision, and so on.

The paper eventually reduces the problem to the search-type problems.  Tools are developed for generating possible solution sets, and selecting from these, and iterating to achieve a desired metric of success.  

The paper confuses discovery with optimization of some model or simulation.  Selecting parameters, or finding the contributing factor from a list, are not scientific discoveries.

### Questions
Isn't this work confusing general scientific discovery with fitting parameters, or finding contributing factors, for some observed (or simulated) process?  Aren't there many tools and methods for smart search, such as methods to assist materials research by finding good experimental parameters iteratively?

It seems the authors have really studied and developed methods for smart ablation studies.  Perhaps this can be a useful general research direction?

### Presentation
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduce a great view point that automated scientific discovery needs automated falsification. It is  very important for AI Scientists, Robot Scientists and other autonomous research agents to generate reliable scientific discoveries.

### Strengths
This paper summarized the four paradigms of AI-accelerate scientific discovery systems: AI as a performance optimizer, AI as a research assistant, AI as an Automated Scientist, AI forms a Research Community. And point out the importance of falsification in the automated the scientific discovery.

### Weaknesses
1. The authors need to discuss in detail whether AI as a peer reviewer can be viewed as a process of falsification to some extent?

2. Table 1 provides a good summary and statistics of AI-powered scientific discovery works. However, the concept of Robot Scientist predates the emergence of AI Scientist. The author may consider adding text or table descriptions related to Robot Scientists. For reference, please refer to the relevant literature "An Ontology for a Robot Scientist", "Scaling Laws in Scientific Discovery with AI and Robot Scientists", and "Towards Robot Scientists for Autonomous Scientific Discovery".

### Questions
Similar to the weakness, although the author discusses peer review in the limitation, it is still unclear whether AI as a peer reviewer can be viewed as a process of falsification. Intuitively, AI as a peer reviewer can, to a certain extent, assist in falsification. The author would be wise to provide a more in-depth discussion.

### Presentation
2

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
The rise of LLMs leads to increaded utilization of them by scientists in the process of discovery. The authors take up this topic and make the point "that automated scientific discovery needs automated falsification".  First, the authors discuss the development of AI-accelerated scientific discovery in detail. Then they present their core idea of automating science through AI-empowered falsification. They also present alternate views and finally present a proof of concept.

### Strengths
- The paper takes up an important topic.
- It is well written and gives a good overview of the literature.
- It is thought provocing.

### Weaknesses
- I am not sure if the topic belongs more in the field of philosophy and if the automated falsification is possible, as for many examples finally a human evaluation or wet lab experiments are needed.

### Questions
- see wekaness above.
- If the evaluation is also done by AI system, is there the danger that one is caught in a loop between the "generator of hypothesis" and the "falsificator"?
- Are it actually two systems or could it not be consideres as one large system?
- Should the results from the falsifcation stage be incorporated into the training of the discovery system?

### Presentation
4
