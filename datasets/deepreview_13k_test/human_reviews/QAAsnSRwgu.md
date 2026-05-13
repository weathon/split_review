# From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle

- Decision: Accept
- Scores: 5, 6, 5

## Abstract
In response to the call for agent-based solutions that leverage the ever-increasing capabilities of the deep models' ecosystem, we introduce a comprehensive solution for selecting appropriate models and subsequently planning a set of atomic actions to satisfy the end-users' instructions.

Our system, Hive, operates over sets of models and, upon receiving natural language instructions, schedules and executes, explainable plans of atomic actions. These actions can involve one or more of the available models to achieve the overall task, while respecting end-users specific constraints. Hive is able to plan complex chains of actions while guaranteeing explainability, using an LLM-based formal logic backbone empowered by PDDL operations. We introduce the MuSE benchmark in order to offer a comprehensive evaluation of the multi-modal capabilities of agent systems. Our findings show that our framework redefines the state-of-the-art for task selection, outperforming other competing systems that plan operations across multiple models while offering transparency guarantees while fully adhering to user constraints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents Hive, an agent-based system that selects and coordinates models to execute complex tasks based on user instructions. Hive creates explainable plans using atomic actions across various models, guided by formal logic and PDDL operations, ensuring transparency and adherence to user constraints. The authors also introduce the MuSE benchmark to evaluate multimodal capabilities in agent systems. Results show that Hive outperforms other systems in task selection and transparency.

### Strengths
The KG construction method is thorough, utilizing model metadata from multiple sources to enhance graph quality. The entire planning pipeline demonstrates a clear improvement over prior work, such as HuggingGPT. Additionally, the writing is well-structured and easy to follow, which supports reader comprehension.

### Weaknesses
This paper has several notable weaknesses:

First, it feels like the approach relies heavily on leveraging a powerful LLM to decompose user tasks based on key attributes, selecting open-source models from Huggingface, and executing plans sequentially. In essence, the paper presents a tool-usage framework where the tools are Huggingface models. While there are some unique designs for processing and indexing these models, the contribution appears marginal. The problem-solving paradigm closely resembles prior works, such as HuggingGPT. Additionally, the paper lacks baseline comparisons, particularly in evaluating why their proposed KG construction method is optimal or how it could be further applied in other scenarios.

The experimental design raises concerns as well. Although the authors introduce a new evaluation benchmark, it is based on an in-house dataset. It’s unsurprising that the method performs well on this dataset, but it lacks validation on standard benchmarks, such as classical VQA datasets for multimodal evaluation.

On a broader level, the necessity of maintaining a Huggingface model graph is questionable. As more cheap and advanced models (e.g., GPT-5, LLaMA-4, lower-cost GPT-4o) emerge with capabilities for comprehensive task handling, the reliance on a graph of smaller, domain-specific models may become obsolete. While a graph of non-LLM-based APIs remains valuable (e.g., calculators outperforms LLMs in calculation), most small LLM functionalities in the current graph could eventually be covered by future, more capable LLMs. This brings into question the core motivation behind the paper’s studied topic.

### Questions
Could you please test the pipeline or more baselines on more widely used benchmarks in multimodal domains?

Would you provide more examples about how the KG looks like and an entire planning example from scratch?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new system, HIVE, that coordinates instructions and task executions across models. HIVE also explains steps being taken. HIVE incorporates a capability knowledge graph to organize and retrieve model capabilities and it uses PDDL, a formal logic approach to assist with planning. To thoroughly evaluate, they also developed a new multi-modal benchmark, MuSE, consisting of complex, multi-modal queries. They demonstrate that HIVE outperforms competitors such as HuggingGPT and ControlLLM on MuSE.

### Strengths
Originality
-They claim to be the first multiple model approach to leverage PDDL. 
-Their approach consists of intuitive steps, achieved using new ideas such as PDDL for planning and C-KG for model selection.
-The multi-modal benchmark data set appears to be a new contribution in the multiple model task domain. More clarity here would be great, see my comments below.

Quality
-The idea of using model cards systematically to leverage new models is very practical and useful. I can see this being helpful for doing this at scale (say you have 1000+ models from which to choose).
-HIVE outperforms the competing models on their more challenging dataset (MuSE)

Clarity
-Overall, the steps in their system: parse user prompt → plan → select models → execute is clear and intuitive.

Significance
-They solve the problem of model selection based on many constraints: hardware (model size), licensing, and model performance. This is going to be increasingly important for multi-agent/multiple model systems.

### Weaknesses
-PDDL was not defined until later in the paper - define it in the abstract and/or introduction.
-Not clear if MuSE will be openly available
-The interaction between PDDL and LLM (ChatGPT) in task decomposition could be made clearer - what exactly is the LLM doing and how is it leveraging PDDL? I think since PDDL could be new for readers, being clear here is very important.

### Questions
-I suggest making the abstract more crisp and making the distinction of this work very clear right away.

-Figure 2 needs to be cleaned up - time is in seconds? The numbers look crowded in the image.

-How does this dataset compare with the function-calling datasets? Is the key difference that these queries require model calls as solutions (rather than API/function calls)?

-Will MuSE be open source? 

-Are there multi-modal query-trajectory datasets in the computer vision community? If so, how do those compare with your multi-modal dataset?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes HIVE, a PDDL-based system to fulfill with user requirements with a large set of foundational models. The system can perform complex actions within given constraints
in an explainable manner.

The paper also proposes a MUSE benchmark to evaluate the multi-modal performance of such agent systems.

### Strengths
The papers proposes a method to automatically extract models with capabilities of various modalities from Hugging Face, and explains in details the methodology.

The automatic system also ease the user query but automatically choose the correct model from the pool as the detailed requirement by user in natural language, which is quite meaningful for the rapid-growing multi-modal foundational models in the community.

Experiments show that even the light version can beat the baselines much except for the image-to-audio case. Experiments on the trustworthiness and robustness also show the advantage of HIVE as an explainable system.

### Weaknesses
Although an automatic exaction system designed, the number of final candidates for HIVE are unknown. Appendix A only mentions a very small sets of models, most of them fall behind SOTA much (e.g. in image generation, machine translation, text generation). (also see questions)

The paper fails to mention the context why such a system is necessary given that most recent foundational models are for general purpose in its specific modality or multi-modality domain, and user can easily choose a model from public leaderboard or knowledge, if the candidates of HIVE is only a limited set of models which are not necessarily SOTA.

HIVE fails completely (0.0 score) on image-to-audio, 1 of the 6 settings in Table 2, casting doubt on the generalizability of the system.

It's unclear how many modalities and multi-modality settings are covered in main text without looking into appendix. The list shall be small and should be put into main text to give readers a clearer view of the evaluation settings. There also lacks a concrete example of the possible user query HIVE is designed for until section 4.5, making the paper hard to understand.

### Questions
+ How many models are selected from Hugging Face as the candidates? Since the community is growing rapidly, will the models from earlier years (with worse performance) be actually selected to perform actions? What's the distribution on model years?
+ It's commonly agreed that recent API-based large models (e.g. GPT-4 series, Gemini) performs better than open-sourced models available on Hugging Face. Have those models been taken into account?
+ Many models are very similar in expertise, since recent community mostly focus on *general*-usage foundational model. What's the importance of such system to choose models from a pool? How many models will be actually selected with common instructions (smallest, best)?
+ Is there any insights why HIVE fails on image-to-audio task? The system should be general enough in modality given the wide availability of multi-modal models, and the 0.0 result can hurt much the overall assessment and actual deployment of HIVE or HIVE-based system.

### Soundness
2

### Presentation
2

### Contribution
2
