# Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Large Language Models (LLMs) have seen significant progress but continue to struggle with persistent reasoning mistakes. Previous methods of self-reflection have been proven limited due to the models’ inherent fixed thinking patterns. While Multi-Agent Debate (MAD) attempts to mitigate this by incorporating multiple agents, it often employs the same reasoning methods, even though assigning different personas to models. This leads to a “fixed mental set,” where models rely on homogeneous thought processes without exploring alternative perspectives. In this paper, we introduce Diverse Multi-Agent Debate (DMAD), a method that encourages agents to think with distinct reasoning approaches. By leveraging diverse problem-solving strategies, each agent can gain insights from different perspectives, refining its responses through discussion and collectively arriving at the optimal solution. DMAD effectively breaks the limitations of fixed mental sets. We evaluate DMAD against various prompting techniques, including self-reflection and traditional MAD, across multiple benchmarks using both LLMs and Multimodal LLMs. Our experiments show that DMAD consistently outperforms other methods, delivering better results than MAD in fewer rounds.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Diverse Multi-Agent Debate (DMAD), an improved version of Multi-Agent Debate (MAD) that leverages agents using different reasoning methods to break "mental set" and enhance reasoning performance. In DMAD, each agent adopts a distinct prompting strategy (e.g. chain-of-thought, step-back prompting, program-of-thoughts) to generate solutions. The agents then review each other's solutions, extract insights from the different reasoning approaches, and iteratively refine their own responses. Experiments on both language models and multimodal language models across various benchmarks demonstrate that DMAD outperforms MAD with homogeneous reasoning as well as other baselines like self-reflection methods. Key results include DMAD in 2 rounds surpassing MAD in 5 rounds, and improvements of 7-8% on metrics compared to 5% for standard MAD. The paper provides a systematic analysis of DMAD, showing performance improves with more debate rounds and agents using a greater diversity of reasoning methods.

### Strengths
1) The key idea of using diversity in reasoning methods to break mental set and improve multi-agent debate is novel and creative. This can leverage different type of strneghts and activation patternsa of LLMs at inference time to produce diverse outputs. This leverages the ideas from cognitive science - the idea of mental set is interestijng.
2) The approach is evaluated across a variety of models (multiple open and closed-source language and multimodal models), datasets/tasks (4 language and multimodal benchmarks), and against strong baselines (standard MAD, self-reflection methods, etc). The authors demonstrate that DMAD approach works well.
3) The ablation studies on number of agents, debate rounds, importance of thought process, etc provide ways to undersstand the robustness of the papers results.

### Weaknesses
While the experiments cover a good range of models and tasks, it would have been nice to see results on more challenging reasoning datasets like MMLU to further validate the approach.

While the paper shows that using agents with diverse reasoning strategies is helpful, its not clear on what kind of diversity is most effective. The authors use three pre-defined reasoning methods (chain-of-thought, step-back, program-of-thoughts), but do not explore other possibilities or study the properties of these methods that make them complementary. A more principled analysis of reasoning diversity could be helpful. 

The paper shows the benefits of DMAD with a fixed number of agents (3) and debate rounds (2-5). However, there is no systematic analysis of how the performance and computational cost scale with these parameters. In real-world applications, it may be necessary to use a much larger number of agents and rounds to tackle complex reasoning tasks. Understanding the scalability properties of DMAD is important. 
Also, for the multimodal experiments, it's unclear if the visual information is playing an important role. Adding experiments on more vision-centric tasks/datasets could strengthen this aspect. 
Its also not well discussed why self-reflection methods struggle on multimodal tasks compared to language-only tasks. Is this an inherent limitation or due to the specific self-reflection approaches used?

### Questions
Some questions came up during the analysis:

How does DMAD perform on tasks that require multi-hop reasoning over longer contexts? Do the gains over baselines hold there as well?
Expanding on the above,  it would be great to see MMLU results, even if just on a subset of subjects most relevant to reasoning.
Can the authors comment on the computational overhead of DMAD compared to standard MAD, both at inference time and during the debate rounds?
Since multimodal models are more computationally intensive in general, were the number of trials/random seeds adjusted for those experiments? Clarifying those details would be helpful.
Figure 1 is quite interesting - if space permits, visualizing even more of the ablations (number of rounds, removing step output, etc) in this format could provide further insight.

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
The pair introduces Diverse Multi-Agent Debate (DMAD), a new method that encourages AI agents to employ different reasoning approaches when debating to solve problems. Unlike traditional MAD, in which agents use the same reasoning method, DMAD assigns distinct reasoning strategies to each agent. DMAD consistently outperformed other methods across multiple benchmarks, demonstrating that diverse reasoning approaches can help break mental sets - the tendency to approach problems in fixed ways based on past experience. This work provides a promising direction for enhancing AI reasoning capabilities without requiring model retraining.

### Strengths
1: The solution is simple since it doesn't require model retraining or additional data collection, making it immediately applicable.
2: The research provides extensive experimental validation across multiple dimensions and shows consistent improvements.

### Weaknesses
1:Resource Efficiency Analysis

The paper lacks a critical discussion on computational efficiency and practical costs. A detailed analysis comparing token usage, API costs, and computational overhead between DMAD and simpler reasoning strategies would better demonstrate its practical value. This is particularly important for real-world applications where resource constraints must be balanced against performance gains.

2: Weak Theoretical Foundation and Empirical Evidence

While the paper draws motivation from psychology's "mental set" phenomenon, the connection appears tenuous. Traditional MAD with a single reasoning method (e.g., CoT) achieves comparable performance to DMAD (as shown in Table 1), suggesting that method diversity might not be the key driver of improvement (Or statistical significance should be provided). This weakens the paper's central thesis that diverse reasoning methods are necessary to break mental set, as even fixed methods can yield different problem-solving approaches through debate. This raises questions about whether the gains are truly from method diversity or simply from the debate process itself (which also encourages some sort of "divergent thinking").

3: Model Capability Scaling

The paper's focus on large, capable models leaves an important question unexplored: could smaller models using DMAD potentially outperform larger models using simpler reasoning methods? This comparative analysis would better demonstrate the method's value proposition, especially for scenarios where using large models isn't feasible. Understanding how DMAD's effectiveness scales with model size could provide valuable insights for practical applications.

4:Limited Implementation Guidelines

Despite DMAD's potential impact on engineering workflows, the paper lacks concrete guidance on implementation decisions. Critical questions remain unanswered; See Questions blow for more.

5: Incremental Rather Than Novel Contribution:

While the paper effectively implements diverse reasoning in a MAD framework, the core concept builds on existing ideas. Similar approaches of leveraging diverse perspectives for improved reasoning have been explored in recent work (Zhang et al., 2024). Although DMAD shows impressive results, its primary contribution appears to be an incremental improvement (applying diversity to MAD) rather than introducing a fundamentally new concept to the field.

Reference:
Zhang, W., Shen, Y., Wu, L., Peng, Q., Wang, J., Zhuang, Y., & Lu, W. (2024). Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives. 2024 ACL.

### Questions
1: Is there a reason you chose the 3 reasoning strategies (CoT, SBP, PoT)? How about others like least-to-most prompting (Zhou et al., 2023)?

2: Could the system dynamically adjust its reasoning methods during the debate process? For instance, could agents switch reasoning strategies based on the progress of the debate or the nature of disagreements that emerge? 

3: Why do you focus on mathematical reasoning and visual understanding? How about other tasks?

4: What criteria determine the ideal number of debate rounds?  Examining Figure 4 (Performance with increased rounds), there's an interesting pattern where DMAD sometimes achieves better performance in 2 rounds than MAD does in 5 rounds, however would a smarter stopping criteria can help mitigate the problem?


Reference:

Zhou, Denny, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Ed Chi, Yun-Hsuan Sung, Daphne Ippolito, and Claire Cassidy. 2023. "Least-to-most Prompting Enables Complex Reasoning in Large Language Models." In International Conference on Learning Representations (ICLR).

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a new method, Diverse Multi-Agent Debate (DMAD), for enhancing the reasoning capabilities of large language models (LLMs) by incorporating diverse approaches to problem-solving within a debate framework. The approach builds on the Multi-Agent Debate (MAD) method by requiring each agent—represented by an LLM—to employ a unique reasoning strategy in order to address a shared problem. Traditional techniques, such as self-reflection, are limited by the model's fixed patterns of reasoning, and MAD likewise suffers when agents adopt similar approaches due to inherent limitations in reasoning diversity. By (manually) instructing each agent to use a distinct reasoning approach, DMAD seeks to enhance solution accuracy across problem-solving scenarios. In each debate round, agents independently solve a problem and then iteratively refine their solutions using insights from other agents' approaches. DMAD is tested on multiple models, including GPT-4o-mini, LLaMA-3-70B, LLaVA-1.6-13B, Gemini-1.5-Flash, and GPT-4o-2024-05-13, demonstrating overall positive, though incremental, performance gains across benchmarks.

### Strengths
The paper contributes meaningfully to the ongoing exploration of multi-agent debate in LLMs by proposing a straight forward extension of the MAD approach that encourages diverse reasoning within the debate process. DMAD's design is simple and builds logically upon MAD, representing an incremental advance. The experiments are comprehensive and cover multiple relevant benchmarks, which gives a well-rounded view of DMAD’s performance. The inclusion of evaluations across various LLMs, both uni- and multimodal, is particularly nice, as it demonstrates the method's effectiveness across different architectures and contexts. The results show that reasoning techniques enforced by DMAD enhance performance on most tasks, confirming that diversity in reasoning approaches can be advantageous even if the cumulative improvement is moderate. Overall, the paper is clearly written and presents a straightforward extension to the multi-agent debate approaches in LLMs, supported by compelling experimental results.

### Weaknesses
While DMAD is a nice addition to the multi-agent debate line of work, its novelty is limited. The method represents an incremental improvement rather than a fundamentally new concept. The debate setup in DMAD may be perceived as a minor extension of the MAD framework, as it mainly focuses on modifying agents’ reasoning patterns. I would have liked to see additional investigations that more deeply alter the default setup of the debate, even if it was as “simple” as running an ablation study with different number of agents. Additionally, while DMAD shows an overall improvement, some gains are marginal or even negative, raising questions about the method’s broader applicability. Though the authors attempt to reason about cases where DMAD's performance lags behind other approaches, the study could benefit from a more thorough investigation of typical mistakes made during debating with DMAD.

### Questions
## General Questions
1. In Table 1, for the Alg. column and the LLaMA model, the value 72 achieved by DMAD is not the highest (c.f. MAD (All CoT) and CoT - SC); is this a typo or a correct results (in the latter case, please correct the text bolding)?
2. Do you believe there would be merit in attempting to set up another LLM to propose reasoning strategies, instead of having them fixed? I understand this is a feat warranting a paper on its own, though I'm quite curious about such applications, as it would allow one to close the loop — having reasoning strategies being proposed and directly “evaluated” by the agents;
3. Have you examined setups with more than 3 agents? Building on my previous question, I assume it's not as straight forward to find additional reasoning strategies that would be assigned to new debaters? Do you believe, given more reasoning strategies, that the performance of the method would scale up with the number of agents, or would it plateau, similar to what happens with the number of rounds?
4. I got confused when reading Eq. 3 and Eq. 4; namely, history $\mathbb{H}$ is defined as a set of tuples, one per agent, each of which containing information pertaining to a particular agent (question, solving process, answer). Perhaps I am missing something obvious, but in Eq. 4, wouldn't it be sufficient to simply define $h_i \equiv \mathbb{H}$ because $\mathbb{H}$ by definition contains the information tuple for the agent $i$, but also for all other agents? To quote the paper “*$h_i$ represents the history of messages for $M_i$, extended with messages from other agents*”, which to me looks exactly like $\mathbb{H}$?
5. Regarding the MATH benchmark, could you provide some intuition on why the performance degrades after 3 rounds (for GPT-4o-mini) compared to 2 rounds? Additionally, why does the LLaMA model's performance improve linearly with more rounds using the MAD method, but drops after the third round with DMAD? Do you have any insights into what kinds of mistakes are being made with additional rounds when using DMAD?

## Minor Comments
- Line 157: Did you mean to write $h_i$ instead of $A_{i,1}$? The variable $A_{i,1}$ is not referenced in Eq. 1;
- Line 314: Shouldn't this be "DMAD" instead of "MAD"?
- Appendix Figures (e.g., 9, 10, 11, etc.): The figures are difficult to interpret due to the formatting characters. You may want to include pre-formatted versions for clarity and consider adding a footnote explaining that the agents actually receive raw markdown text, if necessary.

### Soundness
3

### Presentation
3

### Contribution
2
