# Compositional Hardness of Code in Large Language Models - A Probabilistic Perspective

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
A common practice in large language model (LLM) usage for complex analytical tasks such as code generation, is to sample a solution for the entire task within the model's context window. Previous works have shown that subtask decomposition within the model's context (chain of thought), is beneficial for solving such tasks. In this work, we point a limitation of LLMs' ability to perform several sub-tasks within the same context window -- an in-context hardness of composition, pointing to an advantage for distributing a decomposed problem in a multi-agent system of LLMs. The hardness of composition is quantified by a generation complexity metric, \ie, the number of LLM generations required to sample at least one correct solution. We find a gap between the generation complexity of solving a compositional problem within the same context relative to distributing it among multiple agents, that increases exponentially with the solution's length. We prove our results theoretically and demonstrate them empirically.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This submission presents a probabilistic model of compositional problem solving by LLMs (eq (2-3)). Based on this model, the authors present a theoretical result showing that solving the composition (for various notions of "composition") of two problems can be exponentially more complex (for a probabilistic notion of complexity related to the expected number of samples to reach success) than solving the two problems separately. The authors then present some empirical evidence justiying the assumptions behind their model as well as their main theoretical result.

### Strengths
The authors tackle a problem which is of high importance from the perspective of implementation and of explainable AI. Problem decomposition can be both an efficient method (as evidenced in this paper), and one that is easier to interpret (since part of the explaining is being done by the decomposition).

The methodology is elegant, providing what feels like the right level of abstraction to be able to make meaningful and general statements about systems as complex as LLMs. The formal statements are plausible (although there are some issues in the proofs, see below). The empirical evidence, particularly Fig 1 and Fig 2 is convincing (if rather limited).

### Weaknesses
 * Conceptually, a more detailed examination of the notion of composition would probably be beneficial. Some "compositions" are clearly harder than others. Concatenating a function with itself is trivial, composing a function with itself typically isn't. Therefore, the "noise" term which forms the (very elegant) technical heart of the paper cannot be expected to be as agnostic to the composition mechanism as suggested in this work. This aspect of problem composition is not addressed at all.

* Technically, I'm not 100% convinced by the proof of Lemma 1. At Eq (40), Bennet's inequality is used. It says that \(P(\sum_{i=1}^n X_i>t)\leq \exp\left(-\frac{n\sigma^2}{M^2}h\left(\frac{Mt}{n\sigma^2}\right)\right)\). Here, the inequality is reversed and uses a term \(1-\exp()\). This is incompatible with the definition, and would be the lower-bound for \(P(\sum_{i=1}^n X_i\leq t)\). Also, when pattern-matching this definition with Eq (40), I could not find a reason/meaning for the term \(L\) and for the factor \(3\). So Eq (40) looks suspicious. The statement before Eq (42) is also suspicious (and I'm not talking about the typo). What is the probability of \(1-\delta\) associated with? Is it the probability of sampling \( |y_2| \) noise terms such that (42) holds? Can you explain how you go from Eq (35) to Eq (42)?

* Section 4.3 does not really serve any purpose, the noise model is completely ad-hoc (centered Gaussian with standard deviation \(\sigma=1,2\) and so it doesn't tell us anything.

* Specific comments:

- Def 1: Is \(f\) written in \(L\)? What exactly is the meaning of \(y\) implementing \(f\)?
- Def 2: What is \(\Sigma\)? Just below, "sampled from the distribution" -> the conditional distribution \(P(\cdot\mid x)\)?
- Eq (4) and throughout the document: I think you're writing the quotient symbol / when you mean the set difference \(\setminus \) symbol.
- Eq (13)-(14): use \(\exp\) instead of \(exp\)
- l292: \(\delta \exp(8)\approx 3000\delta\)
- l485: \(\Delta \approx 0.05 - 0.2\) looks like a subtraction, also it seems to contradict the earlier point that \(\Delta\approx 0.2\).
- Eq (22): this step is not necessary
- Eq (30): What is \(V\)? Where does it come from?
- Eq (31): I think all instances of \(x\oplus y_1\oplus y_2\) here should be \(x_2\oplus y_2\)
- Eq (33): I would find this step much clearer if you invoked Jensen's Inequality which does the job exactly.
- Eq (34): Minus sign missing before \(\log\)

### Questions
1. Where does the functional shape of eq (5) come from? Why this shape and not another?
2. Can you answer all the questions above about the proof of Lemma 1?
3. In Fig 1 and Fig 2, exactly which of the two Human Eval composition is being used? What happens if you take consider the other?
4. What can you say about the relative compexity of different combination mechanisms and its impact on the noise term of Eq (2-3)?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper addresses a natural problem: how good are LLMs at solving programming tasks when those tasks require compositions of subsolutions? Given the rise of co-pilots, this is extremely relevant. The paper presents a simple mathematical model of the problem, and some experimental results.

While I think the problem is natural, I found the realisation in the present paper to be weak. The formal model is poorly presented (Definition 1 is effectively empty, the theoretical results are laboured and their significance very unclear). The experimental results section is the most interesting, but I found it somewhat contrived and unconvincing. 

Overall, my sense is this is an interesting direction, but its a rather strange paper overall.

### Strengths
Very compelling and natural problem with realworld implications.

### Weaknesses
Theoretical results are poorly presented and laboured. Significance not clear.

Experimental results seem contrived and the experimental setup seems a little arbitrary. Significance of these results not clear.

### Questions
Can you explain the significance of your theoretical results in informal terms?

Can you better justify the experimental set-up and the decisions you made there?

Do you have a clear hypothesis to explain your experimental results?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explains how if an LM is solving 2 coding problems (x1 and x2) at the same time, and since the generation of a solutions is probabilistic based on the temperature, then assuming the probability of finding a correct solution for solving each x1,x2 separately is P1,P2 (i.e. prob of the LLM solving x1 alone in 1 roll-out is P1). Then to solve x1 and x2 coding problems at the same time, at best you’d expect that getting both correct solutions in 1 roll-out is P1*P2. But since the LLM has finite capacity of depth, number of heads, and imperfect attention, then the authors find that the LLM does far worse than P1*P2, because when solving x1 and x2, the solution written for x1 gets noise from seeing the x2, and vice versa.

The paper advocates using an agentic approach and calling the LLM separately for each problem x1 & x2, which allows the LLM to use all its capacity and attention more optimally to solve the problems, so the success rate is P1*P2, and not lots worse.

The paper makes some assumptions and calculates some bounds on how much worse the accuracy of solving x1 & x2 together can be.

The paper shows results on Llama3-8b-Instruct

### Strengths
I like the presentation and analysis done on the problem with COT causing each step to be less likely to succeed if not done in an agentic way, intuitively most folks know completing multi-step tasks successfully has an exponentially small chance of success if all steps must succeed. But this work emphasizes that the prob of success is even worse than that – the multiple steps compete for attention and processing capacity in the layers – reducing chance of success even more – as the chance of each step succeeding is reduced by seeing all the other steps in the context.

I thought the paper was well written, and had lots of references to interesting relevant papers

I agree with the premise of the paper overall, the agent approach does seem intuitively better to eliminate distractions of irrelevant tokens  and empirically that is shown in the experiments in the paper.  I wish there was more empirical data for larger models showing how larger models maybe handle more problems in some scaling law sort of way.

### Weaknesses
W1. I agree from your results that current Llama-8b-Instruct as trained today doesn't do this multiple tasks as well as doing each task in isolation, but maybe if the LLM were fine-tuned on a dataset of compositional tasks they would learn to do screening/masking of irrelevant tokens more aggressively and not see the same degradation as currently seen, which might be because they are not typically trained on compositional tasks as often so haven't learned to aggressively mask/screen irrelevant tokens as well. Kind of impossible to test if training on more compositional data helps, so maybe not a fair weakness comment.

W2. I also wonder if the degraded performance is a model depth/size thing too – where bigger deeper models with more heads can mask/screen irrelevant tokens better and don’t see the degradation overload with multiple problems. It would be a stronger paper to understand either how bigger models do with multiple combined problems compared to solving them individually, and how much better models can do if finetuned on the compositional task so they might learn to mask/screen out irrelevant tokens better.

W3. Theoretically it's not clear to me the work rigorously proves the agent approach should be better for “all” datasets given the x1,y1 might be a few-shot example for the x2,y2 and help solve x2,y2 more accurately. I think the paper shows it doesn’t always help, wasn’t sure if that is just noise or are there reasons like x1 and x2 are so similar to help contextually.

W4. The assumptions about noise in the output layer, I’m unclear if for bigger deeper models if that still holds or if it the irrelevant tokens are masked out effectively on bigger models, or even the 8b models finetuned to do compositional tasks. The bounds analysis makes lots of assumptions that I'm not sure are valid in all cases.

### Questions
I look forward to reading other reviewers feedback and the authors responses and am open to adjust my scores based on more info.

Line 0: Have other papers done similar analysis say for multi-step tasks in general and this is a special case of that?

Line 147: If the LLM is effectively using attention to mask out the irrelevant parts in the lower layers, the higher layers could have noise=0.  So could the noise at L could be 0 in theory for a properly trained LLM for compositional problems?

Line 161: If x1 and x2 are similar – like “x1 = write a function that takes a number and returns the number + 7, x2 = write a function that takes a number and returns the number + 9” – then couldn’t their be a few shot effect that improves the prob of correct y2 given x1, y1, or even correct y1 given very similar x1,x2.  Does the semantic difference/similarities of x1,x2 impact how much worse the prob of a correct answer to both together is than the product of getting a correct answer to each question in isolation?

Line 304: Llama-3-8B Instruct for the model – do the results hold for other models?  Does this work show any interesting scaling law effects for larger Llama models?  Or on the best OpenAI or Anthropic models?  On larger models I would expect composition wouldn’t be as big of an impact, there would be less noise and sort of predictably less noise as the model size scales up. I could imagine that for problems of a certain complexity there is a number of problems that can be solved together before they interfere and start significantly degrading combined performance compared to solving each alone, and that number that can be solved together is proportional to model size in some way.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper develops a complexity metric to measure the composition hardness of complex code generation by LLMs. By this metric, the authors conclude that decomposed individual generation by multiple agents is easier than generation within one context. This claim is further supported by empirical evidence.

### Strengths
originality: The paper provides a novel complexity metric that quantifies code generation difficulty. This is very interesting as the hardness of natural language processing tasks (code generation being one of them as part of instructions/generations can be in natural language) tends to be quite difficult to quantify.

quality: the paper provides both theoretical and empirical evidence for why multi-agent systems should be favored against single-agent generation when it comes to composed code generation problems. This is sound and clear.

clarity: The paper has a clear argument and consistent storyline.

significance: This paper is theoretically and empirically interesting in that it provides a theory to quantify the code generation hardness and also provides experiments to prove it.

### Weaknesses
The math part is too compact and creates difficulty for readers. The authors might consider providing more straightforward intuition and re-organizing some details in the appendix.



### Questions
1. Why is there no related work section?

2. It is not unknown that LLMs insufficiently utilize some part of the long context (e.g., [1]). How do you think this incapability to handle information in a long context window confounds your observation or LLM's incapability in doing complex code generation in one turn?

[1] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. CoRR abs/2307.03172 (2023). arXiv preprint arXiv:2307.03172, 10.

### Soundness
3

### Presentation
3

### Contribution
3
