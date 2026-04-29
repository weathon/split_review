# Embracing Trustworthy Brain-Agent Collaboration as Paradigm Extension for Intelligent Assistive Technologies

- Decision: Accept
- Scores: 7, 8, 7

## Abstract
Brain-Computer Interfaces (BCIs) offer a direct communication pathway between the human brain and external devices, holding significant promise for individuals with severe neurological impairments. However, their widespread adoption is hindered by critical limitations, such as low information transfer rates and extensive user-specific calibration. 
To overcome these challenges, recent research has explored the integration of Large Language Models (LLMs), extending the focus from simple command decoding to understanding complex cognitive states.
Despite these advancements, deploying agentic AI faces technical hurdles and ethical concerns.
Due to the lack of comprehensive discussion on this emerging direction, this position paper argues that the field is poised for a paradigm extension from BCI to Brain-Agent Collaboration (BAC).
We emphasize reframing agents as active and collaborative partners for intelligent assistance rather than passive brain signal data processors, demanding a focus on ethical data handling, model reliability, and a robust human-agent collaboration framework to ensure these systems are safe, trustworthy, and effective.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
5

### Summary
This paper presents the position that Brain-Computer Interfaces (BCIs), which have recently integrated Large Language Models (LLMs) to address challenges such as low information transfer rates and extensive user-specific calibration, can be extended into a new paradigm: Brain-Agent Collaboration (BAC), driven by LLM-based agents. The authors argue that with LLM integration, agents can be reframed as active and collaborative partners for intelligent assistance, rather than passive brain signal data processors. 

The authors identifies challenges faced by conventional BCI systems, including safety and ethical concerns, technical limitations, and user-related challenges. They highlight potential obstacles in implementing the proposed BAC system, such as managing LLM hallucinations a and risks to autonomy and privacy, and proposes solutions to address them. In addition, the authors listed challenges in employing LLMs for intelligent assistive technologies, which includes robust neural signal interpretation and LLM integration among others. Finally, the authors introduce a conceptual framework for BAC and four evaluation metrics to assess its performance.

### Strengths
The paper supports its position with clear reasoning and analysis.

### Weaknesses
The authors highlights challenges in employing LLMs for intelligent assistive technologies. However they did not provide guidance or suggested solutions for addressing these challenges.

### Questions
Have you considered a 5th evaluation dimension for the BAC system focused on Ethics

### Presentation
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes Brain Agent Collaboration (BAC), a new paradigm for brain–computer interfaces (BCIs) that embeds large language models (LLMs) into the interaction loop in a proactive, agentic role. It emerges that current BCI systems remain limited, primarily translating brain signals into commands, hence being timely for a shift toward a context-aware interaction. The authors detail shortcomings of existing BCI, including their limited contextual understanding, rigid command mapping, and difficulty in handling signal ambiguity. It then surveys efforts integrating LLMs into BCI that enable models to leverage contextual information and improve interpretation accuracy. Then, the authors address major concerns with LLM–BCI integration, such as privacy risks, susceptibility to hallucinations, and ethical implications of interpreting neural data, outlining mitigation strategies aimed at ensuring safe and responsible deployment. The work ends proposing BAC ecosystem, starting from its core components and extending to evaluation protocols and metrics. The discussion is grounded in an extensive review of the state of the art, positioning BAC as both a technically feasible and socially conscious direction for the future of BCI.

### Strengths
+ The paper is well written, clearly structured, and easy to follow.
+ The proposal is timely and highly relevant to the community.
+ The BAC concept is exciting and thoroughly documented.
+ The position is well supported by extensive and pertinent references to current literature.

### Weaknesses
- The position is overly optimistic given the significant unresolved issues in both BCI and LLM technologies; current methods are not yet ready for such a shift. Some claims overlook the real limitations of BCI, presenting systems that do not truly work in practice as viable for this transition.
- Section 5 largely repeats concepts from the introduction and could be removed to expand Section 6, allowing a clearer presentation of the full proposal.
- Figures are poorly described and add little value to supporting the position.
- Section 6 lacks concrete examples to effectively illustrate the proposed ecosystem.

### Questions
1 - Given the current technological limitations of both BCI and LLMs, how do you envision bridging the gap between the present state of the art and the readiness required for the BAC framework to be feasible in practice?
2 - Could you provide a more critical assessment of the real-world performance of existing BCI systems, particularly addressing those that are currently overrepresented as functional but may not yet deliver reliable outcomes? (e.g., discrepancies in measuring performances with the Leave One Out vs the Leave One Subject Out evaluation strategy)
3 - Can you add concrete, scenario-based examples in Section 6 to illustrate how the proposed BAC ecosystem would operate in practice across different use cases?

### Presentation
4

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper argues that LLMs present a new suite of mechanisms that could extend the paradigm of Brain-Computer Interfaces (BCIs) from passive data processing to active, collaborative agents, in the form of Brain-Agent Collaboration (BAC). The paper lays out existing research indicating the potential and proximity of this approach and then sets out a framework for realizing BAC systems, including mechanisms for evaluating these systems to ensure accuracy and quality of user experience.

### Strengths
This paper effectively communicates foundational information about BCIs, illustrates examples of LLMs in action in the field today, and recognizes potential concerns. They pull citations from a variety of recent publications, demonstrating the timeliness of these questions to the research community. (So fresh that at least one of their cited papers, "LLMs Help Alleviate the Cross-Subject Variability in Brain Signal and Language Alignment," was withdrawn by its authors since submission!) Given the growing interest in agents/agency in AI research, this feels like an appropriate topic for the NeurIPS community to discuss.

### Weaknesses
While there are some occasional typos (often missing words or letters), the piece is pretty readable, even to a non-BCI-expert. As a skeptical reader, not all of my concerns were addressed, but some of that may be a matter of the structure or organization of the arguments. The Alternative Views, for instance, do not seem to address the argument head-on, while the evaluation protocol feels a little tacked on (which is a shame because I think it offers some useful examples for the work, but I wish that there was more of a build up to it from the beginning). It feels like it jumps around a bit. The paper would benefit from more signposting (giving the readers a sense of direction) and more reinforcement of the core thesis (why does THIS evidence or section support your ultimate point?)
Early in my reading, I felt like the author(s) handwaved a bit when saying "These [ethical] considerations cannot be afterthoughts in BAC system development. They must be woven in..." In reality, I think that these concerns are at least partially spoken to in the BAC framework and evaluation metrics, but I wish that had been stated more clearly and the flow of the document to make things more obvious.

### Questions
Is the main argument you are making that we need this framework (I agree) or that LLMs ought to be used in this collaborative fashion (I'm not sure I'm convinced)?
What entities (people/orgs) do you think need to come to the table to advance the framework you've put forward?
How do you evaluate the tradeoff of risks and benefits in privacy and human agency? Are there any existing frames for this?

### Presentation
2
