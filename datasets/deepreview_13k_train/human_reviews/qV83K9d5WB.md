# Large Language Models as Tool Makers

- Decision: Accept
- Scores: 3, 6, 5, 5

## Abstract
\rewritten{
Recent research has highlighted the potential of large language models (LLMs) to improve their problem-solving capabilities with the aid of suitable \emph{external tools}. In our work, we further advance this concept by introducing a \emph{closed-loop framework}, referred to as \underline{L}LMs \underline{A}s \underline{T}ool \underline{M}akers (\ours), where LLMs \emph{create} their own reusable tools for problem-solving. Our approach consists of two phases: 1) tool making: an LLM acts as the \emph{tool maker} that crafts \emph{tools} for a set of tasks, where a tool is implemented as a Python utility function. 2) tool using: another LLM acts as the \emph{tool user}, which applies the tool built by the tool maker for problem-solving. The tool user can be either the same or a different LLM from the tool maker. On the problem-solving server side, tool-making enables continual tool generation and caching as new requests emerge. This framework enables subsequent requests to access cached tools via their corresponding APIs, enhancing the efficiency of task resolution.
Beyond enabling LLMs to create their own tools, our framework also uncovers intriguing opportunities to optimize the \emph{serving cost} of LLMs: Recognizing that tool-making requires more sophisticated capabilities, we assign this task to a powerful, albeit resource-intensive, model. Conversely, the simpler tool-using phase is delegated to a lightweight model. This strategic division of labor allows the once-off cost of tool-making to be spread over multiple instances of tool-using, significantly reducing average costs while maintaining strong performance. Furthermore, our method offers a \emph{functional cache} through the caching and reuse of tools, which stores the functionality of a class of requests instead of the natural language responses from LLMs, thus extending the applicability of the conventional cache mechanism.
We evaluate our approach across various complex reasoning tasks, including Big-Bench tasks. With GPT-4 as the tool maker and GPT-3.5 as the tool user, \ours demonstrates performance equivalent to using GPT-4 for both roles, but with a significantly reduced inference cost.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel method for prompting large language models that instructs them to create their own tools implemented as Python functions which help them solve various tasks that might otherwise be challenging to solve without any tool use. The idea is to prompt a larger LLM (e.g. GPT-4) to write a Python function for solving some given task (along with simple unit tests and documentation with example usage) and then passing this as context to a smaller LLM (e.g. GPT-3.5) and asking it to solve a problem by using a given tool. The key assumption is that larger LLMs are more capable of writing good tool functions compared to smaller LLMs. However, since larger LLMs are more expensive to run, it is beneficial to have them produce a tool that can then be successfully reused by smaller LLMs which are cheaper to run. Additionally, the authors propose a scheme for using another LLM that can decide, given a task, whether it needs to ask the larger LLM to produce a tool, or if it can reuse some of the already produced tools and pass them to the smaller LLM. The authors evaluate their method against reasoning tasks and show the feasibility of their approach.

### Strengths
**S1**: The paper presentation is relatively clear and easy to follow. Prior work is adequately referenced.

**S2**: The method is relatively simple which makes it easily applicable. On top of that, the overall approach and distribution of roles between the tool-maker, tool-user, and dispatcher are sensible in this context.

**S3**: The proposed method seems to perform favorably compared to the chain-of-thought baseline across 6 reasoning tasks.

### Weaknesses
 **W1**: My key issue with the paper is that I'm not sure how substantial the contribution is. I understand the recent enthusiasm surrounding large language models. Furthermore, I do think there could be some scientific merit to studying questions like "What can LLMs do?", "Where do they fail?", and "If we do X, can we make LLMs do Y?" as these questions could deepen our understanding of LLMs, their capabilities, and potential for making them even more powerful. However, prompting LLMs is relatively easy. Hence, to publish a paper about prompting LLMs I would expect either some extremely non-trivial and surprising method or a very wide analysis across a large number of tasks that could further our understanding of the LLMs' capabilities and limitations. On top of that, what I would really love is to see a paper that is able to provide a compelling explanation of why LLMs are able or not able to do something (e.g. solve the Chinese remainder theorem task). On the other hand, a method that essentially says "Hey LLM here is a task, can you write a tool that solves it, etc..." is hardly something I would find surprising, especially given that the authors compare it against only a single baseline (which is equally simple in my opinion) and across only a small handful of relatively simple tasks. PS: I am OK to be challenged on this view (either by the authors and/or by other reviewers and PC members) but this is how I see things. ***TLDR***: In my opinion, the novelty bar for papers that propose methods to prompt LLMs should be much higher and should require much more effort and creativity than is presented in this work.

### Questions
**Q1**: Why does CoT achieve a score of 0.0 on the "Chinese Remainder Theorem" problem and LATM achieves 100.0? Also, how does vanilla GPT fare on that task (and why does it fail if it fails)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the "Large Language Models as Tool Makers (LATM)" framework, which explores the idea of language models creating their own reusable tools for problem-solving. LATM has the ability to craft tools to address challenges. It comprises two phases: tool making and tool using, with a division of labor between powerful and cost-effective models. Additionally, LATM introduces a functional cache mechanism to reduce serving costs. Experiments on a range of complex reasoning tasks show that LATM achieves high performance while being cost-effective.

### Strengths
1. The high-level idea of this paper is intuitive and makes sense. It introduces an innovative approach for utilizing large language models, allowing them to create reusable tools, resembling human tool-making abilities.
2. This paper focuses on the practical setting, by strategically allocating the labor between powerful and lightweight models optimize performance while reducing computational costs.
3. The experiments show that the proposed method achieves better performance.

### Weaknesses
1. The paper states that they use a self-verification process with a few labeled instances. However, it is not clear whether the performance is stable with a different selection of few-shot validation examples. It is crucial to understand the sensitivity of the tool creation process to the specific examples used for self-verification, as this could introduce bias or instability in the generated tools. A more rigorous analysis, perhaps involving multiple random seeds for the selection of validation examples, is needed to assess the robustness of the approach.
2. It is not clear how the tool maker can rectify the incorrect tools made in previous rounds (mentioned in 3.1). More case studies are recommended. The paper mentions an iterative process, but lacks detail on how the tool maker identifies and corrects errors in previously generated tools. This is a critical aspect of the framework, and a deeper explanation, including specific examples of error detection and correction, is necessary to fully understand the system's ability to learn and adapt.
3. Is it possible to evaluate other tool-making benchmarks such as ToolBench[1], and APIBank[2]? These datasets will be useful in faithfully evaluating the tool-making ability of LLMs. The current evaluation focuses on complex reasoning tasks, which may not fully capture the nuances of tool creation. Evaluating on established tool-making benchmarks would provide a more comprehensive assessment of the proposed method's capabilities and allow for direct comparison with other approaches.

### Questions
1. What is the price for the tool maker module?
2. Can you provide more case studies on how the tool makers conduct the self-verification process?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Recently, LLMs have demonstrated impressive problem-solving ability to address complex tasks. In this paper, authors introduce a *closed-loop* framework, called LLMs As Tool Makers (LATM). More specifically, this paper introduces two phases: tool making and tool using. Tool making uses LLMs to make new tools via a form of Python utility function and tool using means using tools for problem-solving. Experimental results demonstrate that LATM can achieve performance that matches GPT-4.

### Strengths
1. This paper introduces how to use LLMs to make a tool, which sounds interesting. To fulfill this point, this paper proposes two stages: Tool Making and Tool Using. For Tool Making, the authors adopt three sub-stages: Tool Proposing, Tool Verification, and Tool Wrapping to achieve the target.
2. Experimental results demonstrate the proposed method can improve the performance of LLMs in utilizing tools.

### Weaknesses
 1. Tool making is an interesting idea. However, one weakness in this direction is that we could have many external tools in real-world scenarios and the capability of tool-making should be able to explore new tools that do not have before. Therefore, to further improve the feasibility of the proposed method, it will be better to explore the capability of tool-making to make new tools when also considering the existence of external tools. Specifically, the current method seems limited to creating tools that are essentially wrappers around existing functionalities or APIs, rather than generating novel capabilities. For example, if the LLM is given access to a calculator API, it might create a tool to compute the average of a list of numbers, but it would not be able to create a tool that performs symbolic differentiation, which is a new capability.
2. Compared with Tool making, the design of Tool use is relatively trivial. Many works (e.g., AutoGPT, HuggingGPT) have explored the feasibility of tool use by using LLMs. The paper does not adequately address how the proposed tool use mechanism differs from or improves upon existing methods. The tool use phase appears to be a standard application of LLMs for tool orchestration, lacking significant novelty or a detailed comparison to existing frameworks.

### Questions
1. This paper mainly utilized the GPT-based models for evaluation, do you try any other open-source LLMs?
2. In Tool verification, the authors utilize 3 validation samples. So how to obtain these validation samples? Are these samples manually created and Are these validation samples fixed or different when meeting different user instructions? What are the generalizations of these examples in different scenarios?
3. Based on my observations, the current LATM can only make tools in language form and cannot support multimodal ability, right?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a Tool-Making and Tool-Using framework with two separate LLMs and a functional caching mechanism to re-use tools for functionally analogous requests. With the dichotomy of making and using of tools, the former is assigned to heavier models (e.g. GPT-4) to implement python utility functions while the latter can be conducted with cheaper models (e.g. GPT 3.5). This strategy saves costs and, at the same time, doesn't impact performance as much.

### Strengths
The paper was well-written and easy to read. The description of the problem and the proposed solution were clearly explained.

The idea of "dynamically generating tools from a stream of tasks" is novel (to the extent of the reviewer's knowledge) and if explored more concretely and evaluated end-to-end can be a considerable contribution to the community with many applied use cases in the industry.

### Weaknesses
The paper seems to be lacking originality and doesn't propose a significant contribution to the LLM domain. Here are the reasons for this conclusion:

Generating Python programs (utility functions), or Tool-making,  has been suggested before in similar works such as that of Chameleon (Lu et al.) referred to there as the "Program Generator" module or the Voyager (Wang et al) or the Creator (Qian et al). Tool-using, as well, is a widely used approach within the realm of LLMs to the extent that OpenAI has released models with function-calling abilities. With these points in mind, the novelty of the proposed work gets limited to using lighter models (cost effectiveness) for tool-using to reduce costs and introducing the function cache (reusibility). We appreciate that the authors have clearly credited the mentioned works with their tool-making ideas, particularly the Chameleon with its Python tools where the "Program Verifier" is the couterpart to the proposed "Tool Verification" step in the current paper.

The paper initially gives the impression that the functional cache and the dispatcher to be playing a central role in the proposed LATM. However, the dispatcher was only adopted in the stream of experiments and, even then, in a set of isolated tests. Accordingly it is not clear if the end-to-end performance of the LATM method across heterogenous tasks was evaluated trusting the reliability of the dispatcher and the functional cache to make the right calls.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
