# Executing Arithmetic: Fine-Tuning Large Language Models as Turing Machines

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of natural language processing and reasoning tasks. However, their performance in the foundational domain of arithmetic remains unsatisfactory. When dealing with arithmetic tasks, LLMs often memorize specific examples rather than learning the underlying computational logic, limiting their ability to generalize to new problems. In this paper, we propose a Composable Arithmetic Execution Framework (\method) that enables LLMs to learn to execute step-by-step computations by emulating Turing Machines, thereby gaining a genuine understanding of computational logic. Moreover, the proposed framework is highly scalable, allowing composing learned operators to significantly reduce the difficulty of learning complex operators. In our evaluation, CAEF achieves nearly $100\%$ accuracy across seven common mathematical operations on the LLaMA 3.1-8B model, effectively supporting computations involving operands with up to 100 digits, a level where GPT-4o falls short noticeably in some settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the limitations of Large Language Models (LLMs) in performing arithmetic tasks, where they often memorize examples rather than grasping the underlying computational logic. To overcome this, the authors propose the Composable Arithmetic Execution Framework (CAEF), which enables LLMs to perform step-by-step computations by simulating Turing Machines. This approach helps the models develop a true understanding of computational logic. Additionally, CAEF's scalability allows it to combine learned operators to ease the learning process for complex operations. The framework demonstrated nearly 100% accuracy across seven common mathematical operations using the LLaMA 3.1-8B model, including computations involving operands with up to 100 digits. This performance surpasses that of GPT-4o in certain aspects.

### Strengths
1. The paper is clearly presented and supplemented with ample illustrative figures, allowing readers to easily grasp its content. 
For instance, Figure 1 shows the process of CAFE executing multiplication, Figure 2 outlines the CAFE framework, and Figures 3 and 4 detail the execution processes of addition and multiplication, respectively. 

2. This paper addresses a critic issue in real-world applications of LLMs. The arithmetic performance of existing LLMs, whether open-source or proprietary, is often unreliable, making it difficult to trust their output. 

3. The idea presented in the paper is refreshing, as converting seven common arithmetic operations into text language interpretable by LLMs is no easy feat. This is achieved using lora-adapters to build executors and aligners, relying on two specific prompts: state and command. 

4. The main table presents great performance results for the seven types of arithmetic operations. The accuracy exceeds 99% for both 50-digit and 100-digit tasks, demonstrating practical applicability.

### Weaknesses
1. It is unfortunate that, as mentioned in Section 6 on limitations, the **efficiency issues**—stemming from *the repeated calls to model.generate()* and the *storage overhead of intermediate prompts and adapter representations*—make this approach challenging to deploy in practical applications.

2. When faced with repeating digit patterns such as "999..." or "456456...", the CAFE's executor and aligner fail to function properly. 
I disagree with the authors' claim that this is an inherent limitation of LLMs. I believe it is more likely due to **the absence of such patterns in the fine-tuning data for the executor and aligner**. This raises concerns about the robustness of the experimental results and *whether CAFE can consistently handle or fail in other unique digit patterns*.

### Questions
Please check Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper attempts to address the low performance of LLMs such as llama-3.1 in arithmetic tasks such as addition and multiplication. They have devised a text-based Turing machine for these tasks, and have fine-tuned an LLM to execute it.

### Strengths
1- Paper's approach in solving arithmetic tasks is grounded in our concrete knowledge of Turing machines, which is less ubiquitous in the literature of length generalization. 

2- Paper is well-written and every part has come with specific goal. Sections 2 to 4 follow a natural recipe to explain the method, along with the results.

### Weaknesses
1- In the abstract, from line 16 to 18, authors claim that their method enables LLMs to execute arithmetic tasks in a more rigorous manner and achieve better generalization. My initial understanding of the passage was that the execution happens in a single query of the LLM, where the output includes the final answer. Whereas in Section 3.2, one realizes that a query to the LLM accounts to running a single step of their control flow. 

2- That said, I'm not convinced the proposed approach can be the primary solution for arithmetic tasks. If I understand correctly, the number of queries increases proportionally to the length of the operands in the task, which is problematic since every query's needed number of auto-regression steps also grows linearly with the length of operands, leading to O(d^2) number of auto-regression steps compared to O(d) for a generating the answer with a decoder-only model (d is the length of operands). The computational analysis is missing in the paper. 

3- In section 4, it's not clear whether the comparison with typical LLMs is done by executing the explained Turing machine with each of them and running the steps in different streams, or asking the answer in a single query to these models. I think a comparison with both methods is necessary when reporting. 

4- To my understanding, the proposed method uses two modules for the implementation: "BASIC EXECUTORS" and "EXECUTOR COMPOSERS". And for working with each of the arithmetic tasks (+, −, ×, ÷, ==, >, and <) they utilize different low rank adapters for fine-tuning. This doesn't give a generic solution for solving arithmetics at test time, where based on the given sample a collection of modules must be placed after each other. 

5- How does the method perform in the presence of text? I do not see any sections discussing this.

### Questions
Please address the concerns expressed above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study proposes to decompose basic arithmetic operations into smaller steps that can be executed by LLMs simulating Turing machines. Specifically, by adapting LLMs into separate aligner and executor modules (both via low-rank adapters), one can map an arithmetic operation into a series of smaller atomic steps that solve the task. At each timestep, the aligner translates the input into a representation that the executor can process. The training data for the aligner and executor are obtained by simulating Turing machine prototypes.

The proposed approach achieves significantly higher accuracies than base LLMs, and generalizes better to inputs with many digits.

### Strengths
* The proposed approach performs significantly better than base LLMs on basic arithmetic operations.
* At a high level, I admire the ambition of implementing computational-theoretic data structures using LLMs. If this works well in a wider variety of settings, it could be applied as a natural-language interface to theoretical computational structures that do not require significant human effort to construct. This could have benefits in both educational and software engineering settings, especially if the LLM is capable of explaining each step of its processing.
* The modularity of the aligner and executor setup may make it easier to debug specific components in cases where the approach does not perform well.
* The idea is mostly clearly presented.

### Weaknesses
 * To generate training data, one needs to create a Turing machine prototype. But once one has this machine, why not just use that to solve the task instead of having an LLM do it? It seems like one is better off having the LLM call the machine as a tool, rather than adapting the LLM to execute this procedure. The one way I could see this approach being beneficial over just using the machine is if the LLM can generalize to harder instances than the original machine was ever designed to handle, or to harder instances than were in the generated training data.
* Basic arithmetic operations represent a relatively easy application. I don’t think this is a significant weakness, since this is otherwise a pretty convincing proof-of-concept, but it may limit the impact of this otherwise neat idea.
* The modularity of the aligner and executor setup means that one must maintain high performance for multiple components over many timesteps. This means that a single point of failure could lead to cascading errors on harder tasks. Furthermore, the necessity of maintaining high performance across multiple modules introduces additional complexity in training and debugging. The error propagation could be particularly problematic when dealing with longer sequences of operations, as the probability of at least one error occurring increases with the number of steps.
* Terminology like “understanding” is abused throughout the paper. In particular, the claim of “general understanding” in the abstract is a significant overclaim, and uses of “understanding” afterwards (especially at L189) are unnecessary and anthropomorphize LLMs. The paper would feel much more objective without this language.
* More of a suggestion than a weakness: the error analysis alluded to in the Limitations section sounds interesting. This would be great as its own Error Analysis section.

### Questions
Questions
=== 
1. What is the advantage of using LLMs to simulate the required Turing machine rather than simply using the Turing machine?
2. Rather than using separate aligner and executor modules, is it possible to perform each step in an end-to-end manner (i.e., using just one adapted LLM to do an alignment and execution step)? This could cut the number of possible points of failure in half.

Typos/Suggestions
===
* L50-51: citation or forward reference needed
* L106: \citet -> \citep
* L110-111: run-on
* L133: some examples/citations would be appreciated
* L183: nitpick: The representation isn’t the space in which the computation takes place. The representation is merely a mathematical abstraction that makes it easier for humans to understand.
* The “step” variable is sometimes presented in text mode, and sometimes in math mode. It would be nice to standardize notation.
* L358: small suggestion: “original” -> “unmodified”. “Original” is polysemous, and the sense of “new” interfered with the intended sense of “unmodified” on my first pass

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new framework, called CAEF (Composable Arithmetic Execution Framework), for enabling large language models (LLMs) to perform arithmetic computations. The framework uses the model to emulate a Turing machine, where an input problem (e.g. 89+2) is solved through a series of <state, command> pairs. States and commands represented in a string format are fed to the model, which performs the computation (transitions) with trained modules for input/output alignment and operation execution. These modules are implemented as LoRA adapters, which are trained separately for different operations, (e.g., there are different adapters for addition and multiplication). Experiments are conducted on LLaMA 3.1, where the framework performance is evaluated per operation in comparison to (a) LLaMA 3.1 fine-tuned with LoRA adapters in an end-to-end fashion, (b) the instruction-tuned version of LLaMA 3.1, and (c) GPT-4o. CAEF often shows substantial gains in performance compared to the baselines, mostly in problems involving numbers with over 10 digits.

### Strengths
* The proposed framework is interesting and creative.

* The results show substantial improvements for numbers with >10 digits.

### Weaknesses
 * While the paper is very interesting, I found it hard to digest as I was struggling to understand the proposed framework and exactly how it is being implemented. Specifically, while I was reading I felt like everything is described on an abstract level, without any grounding in concrete examples or settings. Only at the end of the implementation section (3.3) and after looking at the examples in the appendix, I saw some concrete examples of how the framework is executed. It will be helpful to be more explicit and clear about what a state is, what a command is, what the input and output from the models are exactly, whether there is a single execution of the model or multiple inference passes, etc. There are descriptions of what a state should include and in sections 3.2 and 3.3 there are illustrations for specific examples, but the illustrations are abstract and the explanation is vague.

* If I understand correctly, given a problem (e.g. 89 times 2), the model is executed multiple times, where every transition corresponds to a single inference pass. If this is correct, then I am not sure if the experiments make a fair comparison with the baselines. CAEF executes the model many times using a fine-grained step-by-step solution, while the other baselines solve the problem in an end-to-end manner. Looking at the prompts in the appendix, it seems that the instruct models (e.g. GPT) were not provided with instructions to perform chain-of-thought reasoning or anything that would encourage them to solve the problem step by step.

* There is something problematic about the premise of the paper and specifically the focus on exact arithmetic computations of large numbers (with >10 digits). Why do we need LLMs to perform this kind of computation? Wouldn’t an LLM with an external tool be a better solution in this case? Also related to this point is that one potential argument for an LLM-based solution would be that the LLM could infer the type of problem described and the steps for solving it. However, if I understood correctly, with the proposed framework the model does not make this kind of inference. Namely, the adapters to be used are selected in advance. I may have missed this point, tried to look in the paper but couldn’t find it indicated explicitly anywhere. I assume that the adapters are pre-selected (not by the model) because the results are presented per operator and there are no reported results for the performance on inferring the right adapters for the problem.

### Questions
* Missing reference:
Giving BERT a Calculator: Finding Operations and Arguments with Reading Comprehension, EMNLP 2019.

* Figures are very small and hard to read. Consider showing explicitly what the input and output from the model are.

* Line106: incorrect citation format.

### Soundness
1

### Presentation
2

### Contribution
1
