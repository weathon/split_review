# AgentSquare: Automatic LLM Agent Search in Modular Design Space

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recent advancements in Large Language Models (LLMs) have led to a rapid growth of agentic systems capable of handling a wide range of complex tasks. However, current research largely relies on manual, task-specific design, limiting their adaptability to novel tasks. In this paper, we introduce a new research problem: \underline{Mo}dularized \underline{L}LM \underline{A}gent \underline{S}earch (MoLAS). We propose a modular design space that abstracts existing LLM agent designs into four fundamental modules with uniform IO interface: \emph{Planning}, \emph{Reasoning}, \emph{Tool Use}, and \emph{Memory}. Building on this design space, we present a novel LLM agent search framework called AgentSquare, which introduces two core mechanisms, \emph{i.e.}, \emph{module evolution} and \emph{recombination}, to efficiently search for optimized LLM agents. To further accelerate the process, we design a performance predictor that uses in-context surrogate models to skip unpromising agent designs. Extensive experiments across six benchmarks, covering the diverse scenarios of web, embodied, tool use and game applications, show that AgentSquare substantially outperforms hand-crafted agents, achieving an average performance gain of 17.2\% against best-known human designs. Moreover, AgentSquare can generate interpretable design insights, enabling a deeper understanding of agentic architecture and its impact on task performance. We believe that the modular design space and AgentSquare search framework offer a platform for fully exploiting the potential of prior successful designs and consolidate the collective efforts of research community.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces AgentSquare, a framework designed to automatically optimize LLM agent architectures within a modular design space. It proposes a novel approach, termed Modularized LLM Agent Search (MoLAS), by defining a modular architecture divided into Planning, Reasoning, Tool Use, and Memory modules. AgentSquare employs module evolution and recombination mechanisms, along with a performance predictor, to explore and identify optimal combinations within the design space efficiently. The framework is evaluated on six benchmarks, showing a 17.2% performance improvement over existing hand-crafted agent designs.

### Strengths
- Modularity and Reusability: The modular allows the reuse and recombination of components, which aligns well with LLM advancements in modularization and scalability. 

- Effective Search Mechanism: The combination of module evolution, recombination, and performance prediction seems to be a robust optimization strategy. The proposed performance predictor effectively reduces evaluation costs, addressing practical limitations in real-world deployments of LLM agents.

- Comprehensive Evaluation: Benchmarks across domains such as web applications, embodied AI, and gaming provide evidence of AgentSquare’s efficacy and generalizability.

- Interpretable Insights: The framework’s ability to provide human-interpretable design insights is a useful addition, potentially helping in  aiding the design and tuning of future LLM-based agents.

### Weaknesses
My main issue with the paper is that while the modular approach is beneficial in the short-term, it may limit flexibility by enforcing predefined components. Extending the modular design to allow more dynamic, task-specific modules could enhance its applicability.

Additionally, the framework’s reliance on LLM-driven suggestions for module evolution and recombination could inherit biases or inefficiencies from the LLM models themselves, potentially limiting the quality of novel configurations.

Minor comment: 
- Many citations miss parenthesis around them. Try using \citep instead.

### Questions
The authors write that: “In contrast, module-level searching methods including random and Bayesian search lack a clear and insightful search direction." Where do we see this? When looking at the figures, it seems that random search is a pretty competitive baseline?

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
This paper introduces a modular design space for LLM agents named “Modularized LLM Agent Search (MoLAS)” and proposes an evolutionary framework named “AgentSquare” for optimizing and recombining the various modules (covering planning, reasoning, tool use and memory) within this design space. It further introduces a performance prediction model for ruling out unpromising candidate solutions, hence rendering the search process more efficient. Through comprehensive evaluations it is demonstrated that their autonomous, modular design of LLM agents significantly outperforms manual designs and other search algorithms, and offers interpretable insights that complement human knowledge. This paper thus contributes to more standardized and scalable development of agentic systems that exploit prior successful experience, minimizing the reliance on human intervention.

### Strengths
1.The paper is well-organized and uses language that is easy to understand. 

2.The paper is well motivated, addressing an interesting research question. It innovatively consolidates existing (and potentially upcoming) LLM agent designs into a unified framework, and effectively leverages their successful experience for better design. 

3.The experiments are conducted with both quantitative evaluations (including task performances, API costs and search trajectories), and qualitative analyses such as the specific module combinations of optimized agents and insights drawn from the newly discovered modules. 
 
4.The authors have made their code repository available on GitHub, which ensures reproducibility and promotes future work.

### Weaknesses
1.There are some inconsistencies within the paper that might cause confusion. For example, Equation (2) and (3) indicate that both module recombination and evolution take past experience as input, which is not the case in Figure 3. Besides, the random initialization (as mentioned in experimental setup) seems to contradict the arguments made at the beginning of Section 3.3.

2. It seems more fair to also take into account the API cost incurred by search when you compare the performance-cost trade-offs of AgentSquare and manual design. However, the paper did not mention this information.

3.The experimental results appear to be obtained from a single run. The authors are suggested to carry out repeated experiments, and report averaged results and standard deviations to demonstrate the robustness of their approach.

### Questions
1.Are there any specific criteria for selecting the 16 LLM agents when constructing module pools? Besides, human labor involved in standardizing these modules might become prohibitive if one hopes to leverage a larger number of existing agents. Are there any measures to tackle this problem? 

2.Could you elaborate a bit more on the evaluation of candidate solutions? Specifically, it is currently unclear when solutions are evaluated by the performance predictor and when they are tested in the real task environment. 

Thank you!

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
3

### Summary
This paper proposed a framework for automatically selecting and optimizing for off the shelf LLM-based methods from existing literature. It proposes a new concept:MoLAS to enhance agent performance through modular evolution and recombination. The design includes four fundamental modules: Planning, Reasoning, Tool Use, and Memory and uses an in-context performance predictor to efficiently evaluate designs, outperforming manually crafted agents across six benchmarks by an average of 17.2%.  In sum up, AgentSquare provides a platform for researchers to reuse and extend prior successful LLM agent designs.

### Strengths
This method shows it's originality in using evolutionary and recombined mechanisms to automatically explore optimal combinations, effectively consolidating prior research efforts. It also provides empirical testing across diverse benchmarks, showing improvement over handcrafted and prior methods. The research extends to its broad applications and the potential to unify efforts within the LLM agent community, reducing reliance on task-specific human design part and enabling a more systematic exploration of agent architectures.

### Weaknesses
The paper lacks clarity regarding the definition of certain components of the method, particularly the performance evaluation function mentioned in Section 3.1. It is unclear what specific metrics are used for each task and how these metrics are aggregated or compared across different benchmarks. Additionally, the method shows limited novelty, as it primarily focuses on leveraging LLMs to recombine and select existing components rather than introducing a fundamentally new application or capability for LLMs. The core mechanism of modular evolution and recombination, while effective, does not fundamentally address the limitations inherent in the base modules themselves, as it relies heavily on reusing previous designs. The paper also does not fully explore the potential limitations of the in-context performance predictor, such as its sensitivity to the prompt design or its ability to generalize across diverse tasks.

### Questions
1. What is the evaluation and metric function to optimize the searching process ?
2. How does it scales if extending to multi-agent problem?
3. Is it able to solve manipulation tasks ?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
I am disheartened to report I believe this paper involves a form of plagiarism and likely involves intentional academic misconduct (or at least suspect behavior). For full transparency, and because I am an author of the plagiarized work and thus have a stake beyond a normal reviewer, I am making my review public and non-anonymous. 

We posted a paper called “Automatic Design of Agentic Systems” (ADAS) on August 15th to arXiv and shared it on X and LinkedIn. It was submitted for review at ICLR 2025. 

This review is of AgentSquare: Automatic LLM agent search in modular design space. It was posted to arXiv on Oct 8 2024. 

This AgentSquare paper clearly takes many components from the ADAS paper, including the main ideas (slightly modified), repackages them (after adding a bit of new work), and presents the paper as a completely new set of ideas, all without acknowledging the significant degree to which it has lifted many key elements from our paper. It does cite ADAS, but only as an afterthought in the last paragraph before the conclusion, rather than writing throughout the paper (including in the motivation) that the ADAS paper is an extremely relevant piece of prior work and from which they copied (and slightly adapted) core pieces: the main ideas, unique writing choices, data visualizations, code, and prompts (which have significant chunks directly copied without modification). 

It is hard to believe this is an honest mistake. Instead, the evidence causes me to conclude it is an attempt to get an ICLR publication by hoping the reviewers are not aware of how similar this paper is to a previous arXiv paper. Given how similar this new piece of work is, I would expect (and feel scholarship demands) this new paper to mention ADAS early and often, including discussing how it inspired their work and how the works differ, and to acknowledge that this new paper uses many pieces of the ADAS paper. I would also expect AgentSquare to compare to ADAS, since a central claim is that it is an improvement over the approach ADAS took. Instead, the paper is written in such a way that a busy reviewer/reader might not know such a similar work exists, and thus mistakenly attribute credit for the big ideas, results, and novelty to this new work.

If the authors are somehow so unaware of what is appropriate and required in academic writing that this is all an honest mistake, then in my view they should let the community know that, apologize, and entirely rewrite the paper to properly inform readers. 

Note: this is almost certainly not a case of the work being done concurrently, because the paper copied so many pieces from ADAS (including prompts used in their experiments). 

To be clear, there are some nice new innovations in the paper (if the data are to be believed, see below). Properly written (and with more careful comparisons to ADAS and ablations of what makes this paper different and if they help), this paper could have been accepted as a nice innovation on top of ADAS. Instead, I believe it should be rejected as plagiarism. There is not enough time and rounds of review in this conference's review process for reviewers to consider a full rewrite (including back and forth) at this stage. 

Here is evidence of untoward behavior:

1. The prompts from ADAS are largely copied verbatim and then modified in a few places. The amount of overlap makes it certain they copied from our work, yet they did not acknowledge doing so. They should report using a prompt from another paper. But more importantly, it shows how similar the work is to, and was inspired by, ADAS, and thus that ADAS should have been mentioned throughout (as prior work, something to be compared to, something they built on and were inspired by, etc.). You can see the similarities here: https://drive.google.com/file/d/1vHPW2EXvx7LjFv-kDhQHyb_VGHTnndD8/view?usp=sharing

2. ADAS did something rare: it said it was (A) recognizing and naming “a new research area” named Automatic Design of Agentic Systems, and (B) introducing a new search algorithm within that area named Meta Agent Search. AgentSquare clones that template, saying “we introduce a new research problem: Modularized LLM Agent Search (MoLAS)” and “building on this design space, we present a novel LLM agent search framework called AgentSquare.” It is uncommon for papers to name a new research area explicitly, let alone also introduce an instance within it. 

3. Moreover, MoLAS is not a new research area. It is a subset of ADAS. It is a more constrained subset of ADAS, at least the way it is initially presented, which is that MoLAS is constrained to combine pre-existing, human-designed agent modules. However, in a contradiction that is confusing and harms novelty, later the paper also says the modules can be changed, removing this constraint, meaning that MoLAS is thus just ADAS with a new name?

4. Even if ADAS is not identical, it clearly is a very related prior work, yet it is not mentioned in the introduction, nor anywhere in the paper until the second-to-last paragraph. Yet other, much less related work is mentioned (line 053), suggesting an intentional choice to deceive the reader/reviewer by hiding work that hurts the novelty claims of this paper. Also, some of the claims in the introduction say effectively that things like ADAS do not exist or are rare (line 047): clearly ADAS should be mentioned in that context, but isn’t. 

5. The plot style of ADAS Fig. 3a is very similar to Fig. 4, providing further evidence of the central role the ADAS paper played in inspiring and catalyzing the AgentSquare paper. 

6. One (somewhat, see * below) new thing in AgentSquare vs. ADAS is an explicit surrogate model that predicts an agent’s performance, saving compute vs. running a real evaluation. However, I am very skeptical of this data. Even with much training and years of research, getting surrogate models to be highly predictive (e.g. in Neural Architecture Search) is very difficult. I have a hard time believing an LLM is even good zero shot, yet these data say it is nearly PERFECT zero shot. That raises an important question: why are there so few (5) points shown per run (e.g. versus the many more shown in many more per run in Fig. 4)? How did you select these 5? Can you provide code that replicates this experiment, so the community can run it independently and verify it? I do not mean the overall search, which is expensive, but just the zero-shot predictions and the evaluations for all agents produced per experiment. I have never asked for such a thing in review before, but extraordinary claims require extraordinary verification, in my mind, especially given the cloud of suspicion raised by all the other issues in this review.  If the surrogate model is indeed this good, that is a major discovery and worthy of publication in some form, and I recommend you share it in a properly written paper. 

The net effect of all of this evidence forced me to conclude the paper is at best deeply flawed due to many innocent mistakes, and at worst intentionally dishonest, with the latter seeming far more likely. 

If there were no plagiarism issues, I would also point out:

- There is no ablation of memory, one of the key new things they claim they added, and thus no evidence it helps

-  The paper should cite https://arxiv.org/abs/2206.08896

- *Surrogate models arguably implicitly exist within ADAS since it asks for proposals the model thinks will be high-performing, meaning it could use its predictions to guide proposals. However, we know from things like Chain of Thought and Reflexion that one can coax better performance by asking an LLM in the right way and/or asking it to reflect post-hoc on a creation. 

- The paper claims that ADAS’ search in the space of code is an over-simplification. While it is true that describing the search space is simple, searching in it is MUCH more complex. I think it is much more appropriate to say that MoLAS is simplifying search by constraining it to a simple, small search space vs. ADAS, the latter of which allows any possible agent. 

- The paper claims that ADAS is proposed without consideration of existing agent architectures. I disagree, since one can easily inject them as seeds in the search archive (and we did consider that). But we prefer that to be a choice: it likely speeds up search, but also biases it. 

It saddens me to make these accusations. However, I deeply believe in the integrity of the scientific process, including peer review. It relies on trust, and I think we need to stay vigilant and hold people accountable so we can maintain that trust as much as possible. 

Jeff Clune

Professor, Computer Science
University of British Columbia
JeffClune.com

Canada CIFAR AI Chair & Faculty Member
Vector Institute

### Strengths
See main review.

### Weaknesses
I am disheartened to report I believe this paper involves a form of plagiarism and likely involves intentional academic misconduct (or at least suspect behavior). For full transparency, and because I am an author of the plagiarized work and thus have a stake beyond a normal reviewer, I am making my review public and non-anonymous.

We posted a paper called “Automatic Design of Agentic Systems” (ADAS) on August 15th to arXiv and shared it on X and LinkedIn. It was submitted for review at ICLR 2025.

This review is of AgentSquare: Automatic LLM agent search in modular design space. It was posted to arXiv on Oct 8 2024.

This AgentSquare paper clearly takes many components from the ADAS paper, including the main ideas (slightly modified), repackages them (after adding a bit of new work), and presents the paper as a completely new set of ideas, all without acknowledging the significant degree to which it has lifted many key elements from our paper. It does cite ADAS, but only as an afterthought in the last paragraph before the conclusion, rather than writing throughout the paper (including in the motivation) that the ADAS paper is an extremely relevant piece of prior work and from which they copied (and slightly adapted) core pieces: the main ideas, unique writing choices, data visualizations, code, and prompts (which have significant chunks directly copied without modification).

It is hard to believe this is an honest mistake. Instead, the evidence causes me to conclude it is an attempt to get an ICLR publication by hoping the reviewers are not aware of how similar this paper is to a previous arXiv paper. Given how similar this new piece of work is, I would expect (and feel scholarship demands) this new paper to mention ADAS early and often, including discussing how it inspired their work and how the works differ, and to acknowledge that this new paper uses many pieces of the ADAS paper. I would also expect AgentSquare to compare to ADAS, since a central claim is that it is an improvement over the approach ADAS took. Instead, the paper is written in such a way that a busy reviewer/reader might not know such a similar work exists, and thus mistakenly attribute credit for the big ideas, results, and novelty to this new work.

If the authors are somehow so unaware of what is appropriate and required in academic writing that this is all an honest mistake, then in my view they should let the community know that, apologize, and entirely rewrite the paper to properly inform readers.

Note: this is almost certainly not a case of the work being done concurrently, because the paper copied so many pieces from ADAS (including prompts used in their experiments).

To be clear, there are some nice new innovations in the paper (if the data are to be believed, see below). Properly written (and with more careful comparisons to ADAS and ablations of what makes this paper different and if they help), this paper could have been accepted as a nice innovation on top of ADAS. Instead, I believe it should be rejected as plagiarism. There is not enough time and rounds of review in this conference's review process for reviewers to consider a full rewrite (including back and forth) at this stage.

Here is evidence of untoward behavior:

1. The prompts from ADAS are largely copied verbatim and then modified in a few places. The amount of overlap makes it certain they copied from our work, yet they did not acknowledge doing so. They should report using a prompt from another paper. But more importantly, it shows how similar the work is to, and was inspired by, ADAS, and thus that ADAS should have been mentioned throughout (as prior work, something to be compared to, something they built on and were inspired by, etc.). You can see the similarities here: https://drive.google.com/file/d/1vHPW2EXvx7LjFv-kDhQHyb_VGHTnndD8/view?usp=sharing

2. ADAS did something rare: it said it was (A) recognizing and naming “a new research area” named Automatic Design of Agentic Systems, and (B) introducing a new search algorithm within that area named Meta Agent Search. AgentSquare clones that template, saying “we introduce a new research problem: Modularized LLM Agent Search (MoLAS)” and “building on this design space, we present a novel LLM agent search framework called AgentSquare.” It is uncommon for papers to name a new research area explicitly, let alone also introduce an instance within it.

3. Moreover, MoLAS is not a new research area. It is a subset of ADAS. It is a more constrained subset of ADAS, at least the way it is initially presented, which is that MoLAS is constrained to combine pre-existing, human-designed agent modules. However, in a contradiction that is confusing and harms novelty, later the paper also says the modules can be changed, removing this constraint, meaning that MoLAS is thus just ADAS with a new name?

4. Even if ADAS is not identical, it clearly is a very related prior work, yet it is not mentioned in the introduction, nor anywhere in the paper until the second-to-last paragraph. Yet other, much less related work is mentioned (line 053), suggesting an intentional choice to deceive the reader/reviewer by hiding work that hurts the novelty claims of this paper. Also, some of the claims in the introduction say effectively that things like ADAS do not exist or are rare (line 047): clearly ADAS should be mentioned in that context, but isn’t.

5. The plot style of ADAS Fig. 3a is very similar to Fig. 4, providing further evidence of the central role the ADAS paper played in inspiring and catalyzing the AgentSquare paper.

6. One (somewhat, see * below) new thing in AgentSquare vs. ADAS is an explicit surrogate model that predicts an agent’s performance, saving compute vs. running a real evaluation. However, I am very skeptical of this data. Even with much training and years of research, getting surrogate models to be highly predictive (e.g. in Neural Architecture Search) is very difficult. I have a hard time believing an LLM is even good zero shot, yet these data say it is nearly PERFECT zero shot. That raises an important question: why are there so few (5) points shown per run (e.g. versus the many more shown in many more per run in Fig. 4)? How did you select these 5? Can you provide code that replicates this experiment, so the community can run it independently and verify it? I do not mean the overall search, which is expensive, but just the zero-shot predictions and the evaluations for all agents produced per experiment. I have never asked for such a thing in review before, but extraordinary claims require extraordinary verification, in my mind, especially given the cloud of suspicion raised by all the other issues in this review.  If the surrogate model is indeed this good, that is a major discovery and worthy of publication in some form, and I recommend you share it in a properly written paper.

The net effect of all of this evidence forced me to conclude the paper is at best deeply flawed due to many innocent mistakes, and at worst intentionally dishonest, with the latter seeming far more likely.

If there were no plagiarism issues, I would also point out:

- There is no ablation of memory, one of the key new things they claim they added, and thus no evidence it helps

-  The paper should cite https://arxiv.org/abs/2206.08896

- *Surrogate models arguably implicitly exist within ADAS since it asks for proposals the model thinks will be high-performing, meaning it could use its predictions to guide proposals. However, we know from things like Chain of Thought and Reflexion that one can coax better performance by asking an LLM in the right way and/or asking it to reflect post-hoc on a creation.

- The paper claims that ADAS’ search in the space of code is an over-simplification. While it is true that describing the search space is simple, searching in it is MUCH more complex. I think it is much more appropriate to say that MoLAS is simplifying search by constraining it to a simple, small search space vs. ADAS, the latter of which allows any possible agent.

- The paper claims that ADAS is proposed without consideration of existing agent architectures. I disagree, since one can easily inject them as seeds in the search archive (and we did consider that). But we prefer that to be a choice: it likely speeds up search, but also biases it.

It saddens me to make these accusations. However, I deeply believe in the integrity of the scientific process, including peer review. It relies on trust, and I think we need to stay vigilant and hold people accountable so we can maintain that trust as much as possible.

Jeff Clune

Professor, Computer Science
University of British Columbia
JeffClune.com

Canada CIFAR AI Chair & Faculty Member
Vector Institute

### Questions
See main review.

### Soundness
3

### Presentation
2

### Contribution
3
