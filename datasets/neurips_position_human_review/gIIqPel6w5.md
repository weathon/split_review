# Inference-Based Privacy Violations Demand Immediate Recognition as a Distinct AI Safety Priority

- Decision: Reject
- Scores: 4, 7, 2

## Abstract
This position paper argues that inference-based privacy (IBP) risks, AI systems’ ability to infer sensitive personal information from seemingly innocuous inputs, represent a distinct and urgent threat to privacy that remains critically under-addressed in current AI safety discourse. Unlike traditional privacy violations that involve unauthorized access to known data, IBP risks arise from AI systems' ability to infer private attributes through indirect signals and correlations, even when individuals are not present in training datasets. We show that these risks are not hypothetical: they are already evident in deployed systems, from radiology models inferring protected health attributes to large language models deducing personal demographics from subtle linguistic cues. Existing regulatory and technical frameworks, designed primarily for preventing explicit data leakage, are ill-equipped to address these emergent inference threats. We call on researchers, policymakers, and practitioners to recognize IBP as a distinct and immediate category of AI safety risk, and to develop dedicated strategies in response.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
This position paper argues that inference-based privacy (IBP) risks should be recognized as a distinct and urgent AI safety priority. This paper defines IBP risks as the capacity of AI systems to deduce sensitive personal information from seemingly harmless data, a threat they contend is inadequately addressed by current technical and regulatory frameworks.

### Strengths
S1: The paper excels at defining Inference-Based Privacy (IBP) risk and distinguishing it from traditional data privacy issues like data breaches. It formally defines an IBP violation as a model inferring a sensitive attributes from non-sensitive data z about an individual who was not in the training dataset, which clarifies why methods focused on data access are insufficient. This distinction is crucial because it highlights that the privacy harm occurs from the generation of new, sensitive insights, not the leakage of existing data.


S2: he paper provides a thorough critique of why existing privacy protection measures are inadequate for addressing IBP risks. It systematically dismantles the effectiveness of technical solutions like differential privacy and federated learning, explaining their limitations in preventing inferences based on population-level patterns. Furthermore, it identifies specific gaps in major regulations like the GDPR and the EU AI Act, which are not designed to handle passive inference that doesn't lead to immediate, significant effects.

### Weaknesses
O1: The paper's technical solutions, like "Inference Detection," may understate their implementation difficulty. It acknowledges challenges are "genuine" but is overly optimistic, as detecting undefined "inference overreach" is a significant leap compared to other AI safety issues, making the solutions seem more feasible than they are.

O2: The rebuttal to the "Innovation and Utility Argument" is underdeveloped. It suggests consent as a solution but doesn't fully grapple with the powerful economic incentives driving these capabilities, failing to explore the market forces that resist privacy constraints.

O3: Using AlphaEvolve as a precedent for escalating risk relies on speculation about "spontaneous emergence." By calling it a "plausible risk," the paper shifts from its evidence-based arguments to a less certain claim, which detracts from its otherwise strong grounding in documented phenomena.

### Questions
N/A

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper argues that Inference-Based Privacy (IBP) risks, where AI systems generate sensitive information through inference rather than exposing stored data, are an under-recognized but critical category of AI safety risk. The paper calls on policymakers, researchers, and practitioners to treat IBP as a distinct area requiring urgent attention.

The paper starts by formally defining IBP risk and distinguishing IBP risk from other AI privacy risks because it involves generating novel sensitive data through pattern recognition, not retrieving stored data. The author(s) provide illustrative examples of this risk from recent research. The paper goes on to describe why current privacy risk mitigations fall short in addressing IBP risk. The paper also highlights gaps in current regulatory privacy frameworks to protect individuals against IBP risk.

The paper propose a framework for addressing IBP risk, including technical and regulatory approaches (constraining inference capabilities as part of AI safety) and research priorities. The author(s) address potential objections to their arguments and end with a call to action to address IBP risk in this "critical window for action."

### Strengths
This paper is very well written, with a clear argument. It makes a compelling case for focus on an underrepresented area of AI safety research. The definition of IBP risk and its distinction from other types of privacy risks is well supported by literature illustrating the occurrence of IBP risk across a variety of domains. 

The paper flows logically from this theoretical definition to clearly articulating why current approaches to privacy risk mitigation are insufficient for mitigating IBP risk. The framework that the author(s) propose to address these gaps is systematic and internally consistent, providing a solid foundation for future research.

The author(s) have also done an excellent job of anticipating potential objections to their argument and addressing each of these objections to make their argument more compelling.

### Weaknesses
The paper's description of current regulatory frameworks and their gaps is lacking in supporting evidence or literature, with only brief references to specific regulations (GDPR, CCPA) and insufficient specificity about their regulatory gaps. Additional detail would strengthen the author(s)' arguments that regulatory frameworks must evolve to meaningfully address IBP risk.

Some arguments are repeated in the conclusion, making the contribution feel less concise than it could be and resulting in the reader feeling that the argument has been over-argued.

The paper acknowledges but underplays the potential negative impact on innovation of constraining inference, which may weaken the persuasiveness of the policy argument.

### Questions
Your framework emphasizes constraining inference capabilities to reduce IBP risk. How do you envision balancing this with legitimate use cases where inference is essential (e.g., clinical decision support, fraud detection)? Could you elaborate on how to distinguish between harmful vs. beneficial inferences in a way that can be operationalized during model design or auditing?

### Presentation
4

---

## Human Reviewer 3

### Rating
2

### Rating Number
2

### Confidence
4

### Summary
This position paper argues that Inference-Based Privacy (IBP) which is the ability of AI systems to infer sensitive personal information from seemingly innocuous inputs, should be recognized as an urgent and distinct AI safety priority. The authors distinguish IBP from traditional data leakage, highlight concrete risks across domains such as medical imaging, large language models, vision-language models, and autonomously evolving systems, and emphasize the inadequacy of current technical and regulatory safeguards. To address these challenges, the paper proposes a multi-faceted framework spanning technical interventions, policy and regulatory measures, and new research priorities, ultimately calling for immediate collective action to prevent IBP violations from becoming entrenched in future AI systems.

### Strengths
1. The paper highlights an timely issue and argues for its recognition as a distinct AI safety priority, using concrete examples across domains (medical AI, LLMs, vision-language models).

2. The structure is coherent and the inclusion of alternative perspectives, making the topic relevant and potentially valuable for community discussion at NeurIPS.

### Weaknesses
1. The paper is very short (6.5 pages) relative to NeurIPS standards and relies solely on text, without any figures or tables to improve readability or to summarize comparisons for general readers. 

2. While concrete examples are provided, the evidence base is limited: citations and descriptions are limited, there is no systematic summary of existing privacy-related techniques, and no comparative analysis (which could be illustrated with charts or tables). 

3. Although it is a position paper, the contribution and position remain overly abstract, as the manuscript repeatedly emphasizes the urgency of the issue without offering substantive discussion of potential mitigation strategies. The proposed “Framework for Immediate Action” is presented only at a high level, lacking concrete potential methodological tools, design blueprints, or feasible solution pathways.

4. The discussion of alternative views is underdeveloped: All arguments are framed in generic terms (“critics,” “some might contend”) without any references or supporting evidence, weakening the credibility of the counter-argumentation.

### Questions
1. Could the authors provide a more systematic overview of existing privacy-related techniques (e.g., differential privacy, federated learning, secure computation) and clarify how their proposed framing of IBP uniquely extends or differs from prior work?

2. The proposed “Framework for Immediate Action” is described at a high level. Can the authors elaborate with possible methodological tools, design blueprints, or example pathways that could make this framework more actionable for the ML community?

3. The discussion of alternative views is framed in generic terms (“critics,” “some might contend”) without references. Could the authors cite and engage with specific prior works or stakeholders who hold these views, to strengthen the credibility of their counter-arguments?

4. Since the paper calls for privacy is inherently interdisciplinary, how do the authors envision integrating insights from some subjects such as law, social sciences, or HCI into the development of IBP mitigation strategies?

### Presentation
1
