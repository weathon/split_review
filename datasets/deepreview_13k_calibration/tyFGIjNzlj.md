# Algorithmic Language Models with Neurally Compiled Libraries

- Decision: Reject
- Avg Score: 3.75
- Scores: 5, 6, 3, 1

## Abstract
Important tasks such as reasoning and planning are fundamentally algorithmic, 
{meaning that solving them robustly requires acquiring true reasoning or planning algorithms, rather than shortcuts.}
Large Language Models lack true algorithmic ability primarily because of the limitations of neural network optimization algorithms, their optimization data and optimization objective, but also due to architectural inexpressivity.
To solve this, our paper proposes augmenting LLMs with a library of fundamental operations and sophisticated differentiable programs, so that common algorithms do not need to be learned from scratch. % and can be composed when learning new tasks.
We add memory, registers, basic operations, and adaptive recurrence to a 
transformer architecture built on LLaMA3.
Then, we define a method for directly compiling algorithms into a differentiable starting library, which is used natively and propagates gradients for optimization.
{In this preliminary study, we explore the feasability of augmenting LLaMA3 with a differentiable computer, for instance by fine-tuning small transformers on simple algorithmic tasks with variable computational depth.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses LLMs’ problem with performing symbolic operations. To this end, they investigate one way to incorporate a differentiable interpreter into LLMs. Given a text input, the authors use LLaMa 3.2 to select the correct program, out of a library of programs, and to generate the program’s inputs. A differentiable interpreter then runs the program. A final neural network is then used to produce the final output.
The paper presents experiments on arithmetic and sorting, as well as ablation experiments with simpler neural network models.

### Strengths
Address an important problem, which is well motivated.
The background section is comprehensive and an interesting read.
It proposes an interesting approach of using a differentiable interpreter, as well as preparing a library of programs to choose from, by compiling symbolic programs into differentiable versions.

### Weaknesses
Poor introduction: most of the introduction, apart from the very last paragraph is dedicated to motivating the work. The very last paragraph has 1 sentence which describes the methodology.

Section 3, Methodology: The authors should make it clear what their contributions are. I am left with the impression that the majority of this section (apart from 3.4) are ideas from a previous paper that are just re-stated here. If this is the case, it should be stated more clearly. In itself, 3.4 is very brief and doesn’t describe the method sufficiently well, for example, I am unsure if the method selects only a single program or runs multiple programs during training.

Experiment section, poor presentation:  the setup of each experiment isn’t described clearly: I am unsure what is the set of programs considered, what the neural architecture is for 4.1 and 4.2, what the inputs and outputs look like, what’s the difference between circuits and tables

Experiment section, no baselines: there are no purely neural baselines. Section 4.2 augments and finetunes LLaMa without showing LLaMa’s performance.

Experiment section, unconvincing results: It is not clear to me that the results support the claim in the Introduction that “resulting in a model which is universally expressive, adaptive, and interpretable”.  Specifically, Table 2 presents the result for sorting, where the accuracy is between 33% and 37% which the authors refer to as “decent performance”. I cannot see a way to reaching this conclusion. This leaves an impression that, while the method could perform well in the future, is currently underperforming and unconvincing.

### Questions
How do you differentiate between the selection of different programs? Do you run all of them at once? If not, how do you expect the LLM to learn which program to select if it’s trained only on the error of the outputs?

What are the novel ideas which one can take away from the methodology of this paper?

How do the experiments demonstrate that your method is “universally expressive, adaptive, and interpretable”?

### Soundness
1

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
The authors investigated the feasibility of augmenting large language models with libraries of
differentiable programs.  This is important and very interesting direction.
They augment LLaMA 3.2 with a differentiable interpreter,  develop differentiable algorithm library,
and study how a model can utilise given functions.  This could be potentially great work, but lack of experimentation makes it less appealing.

### Strengths
- Reasoning, arithmetic and algorithmic abilities are still weak spot of LLM .  'Algorithmic Language Models with Neurally Compiled Libraries' suggest interesting and promising approach to improve capabilities of LLM. 
- Authors analyse impact of recursion depth on trainability on Fibonacci dataset
- They create library of differentiable modules and augment LLM with them

### Weaknesses
 - Neurally Compiled Library is primary experimental work. Therefore I believe work would greatly benefit from extending it's evaluation on more, preferable public datasets. Also more detailed about experiments performed (for example what dataset was used for Airithmetic testing on page 8)  would make it more interesting.
- It would be helpful to have baselines with/without  differential modules (i.e Figure 3,  Table 2)
- Model background section would benefit from either added citations or clear indication what was proposed in current work. (I.e Differentiable Registers, Probabilistic execution, Differentiable Interpreter sections)

- Discussion of sorting performance is missing. The paper introduces differentiable insertion sort, but there is no analysis of its performance or comparison to other sorting algorithms. It's unclear how well the model learns to utilize this module, and why it may fail. This is especially important given the authors' claim that the gradient path produced by the algorithm is long and noisy.
- On page 8.  There is statement 'fine-tuned LLaMA 3.2 can achieve descent performance'. Could you please clarify, what you comparing agains?
- 'Furthermore, our results highlight the overall shortcomings of gradient-descent based learning, given that even when the ideal algorithm is already present, there are still scenarios where the model may not learn a perfectly generalizable solution.' This is very interesting finding.  I think both paper and community would benefit if more details on training difficulties, what didn't work, etc would be given.

### Questions
On page 4  'instruction counter' and  'program counter' are mentioned. Could you please clarify what is the difference?
Do formulae (3) and (4) assume broadcasting?
On page 8.  There is statement 'fine-tuned LLaMA 3.2 can achieve descent performance'. Could you please clarify, what you comparing agains?
'Furthermore, our results highlight the overall shortcomings of gradient-descent based learning, given that even when the ideal algorithm is already present, there are still scenarios where the model may not learn a perfectly generalizable solution.' This is very interesting finding.  I think both paper and community would benefit if more details on training difficulties, what didn't work, etc would be given.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors propose to augment LLMs with a differentiable computer equipped with a pre-existing library of functions, as way to to make large foundation models more capable of reliably performing classical algorithms and therefore, in the view of the authors, reasoning. This is in contrast with other tool-use or neurosymbolic approaches, in which LLMs are equipped with an external module (e.g. a calculator, or web browser, or Python interpreter) whose workings are fully interpretable, but which cannot be differentiated through.

### Strengths
The authors' proposal is definitely original, the paper outlines it in a mostly clear manner, and there is reason to believe that such augmentations, once refined and properly scaled, could indeed prove to be invaluable in making foundation models capable of algorithmic reasoning.

### Weaknesses
Ultimately, the author's proposal does not seem to work well enough given the evaluations they present, and by their own admission their paper is more of a initial proof of concept (and a limited one at that) rather than a practical demonstration of the soundness of their approach. In this regard, I cannot provide any more suggestions for improvement than the authors already do in section 6; the paper in its present state is ultimately more suited to be a workshop publication than a main conference paper.
A related point I wish to make is that the authors do not seem to address, either in the introduction or in their experiments, the issue of length generalisation, which is the main problem to solve in order to make LLMs capable of actually running algorithms rather than just find solutions via shortcuts and pattern matching. Showing that their augmented model is capable to length-generalize, even just on a very simple task such as integer sorting or parity, would significantly enhance this paper's contribution. The lack of length generalization is particularly concerning given the focus on algorithmic reasoning, where the ability to handle variable-length inputs is crucial. For example, the experiments on sorting are limited to fixed-length lists, which does not demonstrate true algorithmic capability. Furthermore, the paper does not explore the limitations of the differentiable interpreter, such as its potential to introduce numerical instability or gradient vanishing issues, which are critical aspects to consider when using differentiable components within a neural network architecture. The authors should have provided a more thorough analysis of these potential pitfalls, especially given the sequential nature of their interpreter.

### Questions
- Am I to understand that none of the differentiable intepreter's parameters are trained? If not, which ones are?
- Related to the above, it is still not clear to me which algorithms constitute the compiled library for the experiments in section 4 and, most importantly, how are these algorithms compiled into the model before the training runs.
- In section 4.1, the authors assert that a differentiable circuit ALU generalises "beyond lookup tables". How can this be deduced by figure 3, where text accuracy for differentiable circuits is actually lower than for a lookup tables?
- How did the authors pick the training hyperparameters used in section 4.2?
- In section 4.3, to the authors consider generalising to sorting longer lists at test time (e.g., training on list of size 8 and testing on strings of size 12)
- Again in section 4.3, the authors attribute the weak performance of their augmented model to the difficulty of parsing the natural language description of the problem. Can they provide any evidence (e.g. in the appendix) for this statement via some ablation?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper trains transformers to parse textual inputs into (1) inputs of programs and (2) which program to use from the library. The program's outputs are also unparsed into texts by transformers. 

Specifically, it mainly finetunes Llama (by changing its last layer) to map "Add 3 and 4" into (1) a categorical distribution over programs in the library and (2) categorical distributions over base-128 integers as the programs' inputs. The program's output is a categorical distribution over base-128 integers as well and is then unparsed into texts by neural networks. 

It evaluates such a model in two tasks: 
* Modular Arithmetic (providing arithmetic lookup tables in the library): 100% accuracy
* Sorting (providing insertion sort in the library): ~35% accuracy.

### Strengths
This paper targets an important problem, integrating programs with neural networks.

### Weaknesses
My main concern is about the novelty and the meaningfulness of this work:
- This paper trains/finetunes transformers to parse/unparse between texts and program inputs/outputs. I do not see the difference between this work and other LLM Tool Argumentation works. Parsing and Unparsing have become much more reliable and accurate with LLMs, let alone the problem here is just to choose one program from the library and retrieve arguments of programs from the text. Differentiable programs may provide more information for program search but they still underperform discrete-search-based methods to synthesize conventional programs. The program search problem here is again too easy to consider those nuances of different program synthesis methods...

Other concerns include
* The performance is not satisfying. For example, to learn sort with the ground-truth sort algorithm in the library, the accuracy is still lower than 40%.
* This paper is poorly written and hard to understand. After thoroughly reading the paper, I am still unsure of e.g., 
  - the components of the library, just arithmetic operators, or with sort, or also including some basic logical operators? 
  - why differentiate sorting using differentiable register machines instead of many other works that potentially provide better gradient estimations? 
  - Definition of test accuracies for e.g., sort; 
  - Opinions/Arguments without evidence such as: "While we do not explicitly study them in this work, they almost certainly play a role."

### Questions
* For such a parse/unparse model, why do we need differentiable programs? 
* What is the performance of baselines from the LLM Tool Argumentation field?

### Soundness
1

### Presentation
1

### Contribution
1
