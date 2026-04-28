# Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 8, 6, 6

## Abstract
Do large language models (LLMs) solve reasoning tasks by learning robust generalizable algorithms, or do they memorize training data?
To investigate this question, we use arithmetic reasoning as a representative task. 
Using causal analysis, we identify a subset of the model (a circuit) that explains most of the model's behavior for basic arithmetic logic and examine its functionality.
By zooming in on the level of individual circuit neurons, we discover a sparse set of important neurons that implement simple heuristics. Each heuristic identifies a numerical input pattern and outputs corresponding answers.
We hypothesize that the combination of these heuristic neurons is the mechanism used to produce correct arithmetic answers. 
To test this, we categorize each neuron into several heuristic types---such as neurons that activate when an operand falls within a certain range---and find that the unordered combination of these heuristic types is the mechanism that explains most of the model's accuracy on arithmetic prompts.
Finally, we demonstrate that this mechanism appears as the main source of arithmetic accuracy early in training.
Overall, our experimental results across several LLMs show that LLMs perform arithmetic using neither robust algorithms nor memorization; rather, they rely on a ``\emph{bag of heuristics}''.
\footnote{Code at \repo}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper uses causal analysis to understand how (small scale) LLMs solve arithmetic. They identify that the model's output really depends on only a small subset of its parameters which they call a circuit and use this to explain its behavior. They find that each neuron in this circuit implements some form of a heuristic and the model's overall behavior can be explained as a collection of these simple heuristics. They run extensive experiments and analysis to validate their claims and show that somewhat surprisingly, the model is neither relying purely on memorization or learning a robust generalizable algorithm for addition or multiplication.

### Strengths
1. Arithmetic tasks are a particularly useful test bed to understand the learning mechanism of LLMs. However, it has been an open question as to what algorithm the model is truly learning. This work makes an important step in this direction, particularly since it applies to the newest edition of LLMs.
2. The bag of heuristics finding explains the lack of length generalization in most LLMs on arithmetic tasks.
3. The experiments and analysis are extensive and the authors make an effort to validate all of their claims sufficiently.
4. The paper is well written with the ideas explained clearly with good intuition.

### Weaknesses
1. A lot of the analysis assumes that the tokenizers all tokenize numbers as a single token up to some limit. While I found this interestingly to be true for llama3 and pythia, I don't think this is always true. In fact, the llama2 tokenizer itself was different in that it tokenized each digit individually. I would like to see if these findings are tokenizer specific. Specifically, the reliance on single-token representations for numbers may obscure the underlying mechanisms when models process multi-token numbers, potentially leading to different conclusions about the learned heuristics. This is a significant limitation that needs further exploration.
2. The sampling mechanism of activation patching seems to be of fairly "high-variance". Sampling a "random counterfactual prompt" from the universe of prompts seems to me like it would lead to widely different results. Is this true? The choice of counterfactual prompts could introduce significant variability in the identified circuits, making the results less robust. The paper should include a more rigorous analysis of the sensitivity of the results to the choice of counterfactual prompts, perhaps by quantifying the variance in the identified circuits across different sets of counterfactuals.
3. The difference between the total logit contribution of the heuristc neurons to the correct answers vs the incorrect answers is fairly small. And thus it is plausible that this is not the only (or even main) failure mode of the bag of heuristics. The small difference in logit contributions raises concerns about the completeness of the identified heuristics in explaining the model's behavior. It's possible that other factors, such as interference from other parts of the network or more complex interactions between neurons, are contributing to the model's errors. A more comprehensive analysis that considers these additional factors is needed.
4. The experiments on tracking development across training steps is on a model with a very different tokenizer and much worse performance than Llama3-8B. I understand that this is necessary since llama3-8b's training data is not public, however it does mean the results are slightly harder to compare. This difference in model architecture and performance makes it difficult to generalize the findings about circuit development to the Llama3-8B model, which is the primary focus of the study. The paper should acknowledge this limitation and discuss the potential implications for the generalizability of the results.

### Questions
1. In Figure 3, is the position of Operator 1, Operator 2 a range? Or are the inputs only up to the point where it is a single token?
2. Am I right in understanding that once the circuit is identified, the network can be replaced with a highly sparse version of the same network? (Say 98.5% sparse where the fixed components can be replaced by biases?)
3. Does the bag heuristics finding imply that length generalization for these models is impossible?

### Soundness
4

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
2

### Summary
This paper explores the reasoning mechanisms behind arithmetic calculations in large language models (LLMs). The authors use causal analysis to identify an "arithmetic circuit" responsible for these calculations, finding that LLMs apply a set of heuristic-based neurons rather than true algorithmic methods or pure memorization. Each neuron in this circuit encodes simple, pattern-based heuristics that activate for specific operand patterns and contribute to the model's ability to solve arithmetic prompts. The paper provides a comprehensive examination of these heuristics and their emergence over training time, shedding light on the limitations and generalization abilities of LLMs in mathematical reasoning.

### Strengths
This paper applies causal analysis and activation patching experiments to identify individual neuron behaviors.

The authors' step-by-step examination, from identifying neurons and classifying them into heuristic types to analyzing their evolution over training time, offers a thorough perspective on LLMs' arithmetic reasoning mechanisms.

The paper may facilitate future studies on generalization abilities.

### Weaknesses
This paper focuses on arithmetic calculation but mentions general reasoning at the beginning. I feel that this could be a overclaim because simple one-step calculation is far away from reasoning.

The authors get all conclusions from pre-trained checkpoints. But I am thinking that all models need fine-tuning before usage, it is better to have similar analysis on arithmetically or generally fine-tuned LLMs.

The focus is primarily on arithmetic reasoning, which may not fully generalize to other complex reasoning tasks. It is interesting to see the model behavior when arithmetic calculation is embedded in texts.

### Questions
The classification of neurons into heuristic types was manually conducted. Do you think if it is possible to develop an automated or semi-supervised system to reduce human bias?

You mention that the "bag of heuristics" mechanism evolves gradually during training. Have you observed whether certain heuristics are reinforced at specific training stages?

Your analysis reveals cases where the model’s heuristics do not generalize to certain arithmetic prompts. Could you provide more insights into these failure cases? For instance, are there specific numerical ranges or types of prompts where the model tends to fail more frequently?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
It is unclear how large language models solve reasoning tasks. For example, do they simply memorize the solution or learn generalizable reasoning processes. This papers demonstrate language models use a set of heuristics to solve arithmetic (a task where we expect a successful learner to learn generalizable algorithms). The paper characterizes the different types of heuristics being implemented as how heuristics are developed during training.

### Strengths
- For the most part the paper was well-written and well motivated. At any given point in the paper, it was easy to understand (1) what the hypothesis being tested is, (2) why the authors are testing this hypothesis, (3) the experimental setup, and (4) the results.
- The experiments conducted by the authors are thorough and well-support the claims made throughout the paper.
- The topic of the paper is timely and illuminates an interesting aspect of arithmetic reasoning in language models that has not been explored before. I think this will add value both to those working in mechanistic interpretability (because of the clean experimental designs) as well as those working in NLP in general (as it provides an important case study).
- The paper's results are replicated across models of different scales as well.

### Weaknesses
 - The title of the paper is slightly misleading: “Models Sovle Math with a Bag of Heuristics” in reality the authors only examine arithmetic where both operands have less than three digits. Maybe for greater number of digits, these heuristics are somehow algorithmically combined? This question is left open in the paper (which is fine, I think the paper is a good contribution as is), but the title does not reflect this.
    - In the very least, I think this point should be mentioned briefly in the limitations section.
 - There are some experimental details which are shoved under the rug which I cannot find the appendices (see below). I think adding (probably in the appendices) these would greatly help the reproducibility of the results.
 - Eq. 2, pg. 4, why are the authors measuring faithfulness by averaging the percentage change in logits? It seems that a more principled approach would be checking how much the correctness of the model (measured through accuracy) decreases as a result of mean ablation. Did the authors ablate over this design variable?
- In Fig. 7, I am confused by what the x-axis is here. It would make sense that it the accumulation of heuristics, but that is not what the axis label implies. Could the authors elaborate on this a bit more?
- In line 321, the authors use $t=0.6$ as the intersection threshold, why was this hyperparameter specifically chosen, was it based on the alignment with manual insepction? I do not see ablations over this parameter in the appendices.
- In lines 408-410, “incorrect prompts have more heuristic neurons associated with them than correct prompts” how are the authors measuring this involvement? Is this through the same sort of patching that was done before, but in this case how are the authors patching the neurons for a baseline incorrect response?
- It has been shown in some recent works that logic lens in very often unreliable see [1]. Have the authors tried other hidden state decoding methods like [1,2,3]? I wonder if this could be used to better classify some of the heuristics that did not fall into any of the identified categories.
- In lines 347-355, the authors perform knockout experiments. I am wondering if we knockout say a neuron associated with the heuristic $\textrm{op}_1 \equiv 0\mod2$ that significantly contribues sto the output, we not only see a decrease in performance, but also a *decrease in performance on inputs specifically where the first operand is even?* This would provide even stronger evidence for not only the importance of the heuristics, but also the claimed functionality of each of them.
    - Is this what Fig. 7 is trying to show, specifically, the importance of the “associated prompts?”

### Questions
- Eq. 2, pg. 4, why are the authors measuring faithfulness by averaging the percentage change in logits? It seems that a more principled approach would be checking how much the correctness of the model (measured through accuracy) decreases as a result of mean ablation. Did the authors ablate over this design variable?
- In Fig. 7, I am confused by what the x-axis is here. It would make sense that it the accumulation of heuristics, but that is not what the axis label implies. Could the authors elaborate on this a bit more?
- In line 321, the authors use $t=0.6$ as the intersection threshold, why was this hyperparameter specifically chosen, was it based on the alignment with manual insepction? I do not see ablations over this parameter in the appendices.
- In lines 408-410, “incorrect prompts have more heuristic neurons associated with them than correct prompts” how are the authors measuring this involvement? Is this through the same sort of patching that was done before, but in this case how are the authors patching the neurons for a baseline incorrect response?
- It has been shown in some recent works that logic lens in very often unreliable see [1]. Have the authors tried other hidden state decoding methods like [1,2,3]? I wonder if this could be used to better classify some of the heuristics that did not fall into any of the identified categories.
- In lines 347-355, the authors perform knockout experiments. I am wondering if we knockout say a neuron associated with the heuristic $\textrm{op}_1 \equiv 0\mod2$ that significantly contribues sto the output, we not only see a decrease in performance, but also a *decrease in performance on inputs specifically where the first operand is even?* This would provide even stronger evidence for not only the importance of the heuristics, but also the claimed functionality of each of them.
    - Is this what Fig. 7 is trying to show, specifically, the importance of the “associated prompts?”

[1] Belrose, Nora, et al. "Eliciting latent predictions from transformers with the tuned lens." *arXiv preprint arXiv:2303.08112* (2023).

[2] Pal, Koyena, et al. "Future lens: Anticipating subsequent tokens from a single hidden state." *arXiv preprint arXiv:2311.04897* (2023).

[3] Ghandeharioun, Asma, et al. "Patchscope: A unifying framework for inspecting hidden representations of language models." *arXiv preprint arXiv:2401.06102* (2024).

### Soundness
4

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
4

### Summary
This paper investigates how LLMs solve arithmetic tasks, questioning whether they rely on robust algorithms or if they instead depend on memorization or simple heuristics. Using methods like activation patching and linear probing, the authors identify a subset of neurons responsible for arithmetic tasks in LLMs, which they term the “arithmetic circuit.” The study reveals that LLMs rely on a "bag of heuristics" formed by a small subset of individual neurons, each triggered based on specific input patterns. Through various experiments and ablations, the paper demonstrates that this heuristic-based mechanism is the primary method for handling arithmetic prompts, even from early stages of model training. The authors conclude that LLMs’ arithmetic capabilities do not stem from robust algorithms or mere memorization, but from a combination of these lightweight heuristics.

### Strengths
1. The paper makes a valuable contribution by providing a mechanistic interpretation of how LLMs handle arithmetic tasks, adding a nuanced understanding of model behavior beyond existing studies on memorization and algorithmic capability. By identifying individual neurons and describing them as "heuristic carriers," this study offers a novel perspective on LLM internal operations.
2. The authors clearly articulate their methodology and conclusions. The visualizations, especially those illustrating neuron activation patterns, support comprehension and substantiate the paper’s core claims about the heuristic-based arithmetic mechanism.
3. The paper employs causal analysis techniques to dissect the arithmetic circuit in LLMs and validate its findings with multiple ablation experiments. The robustness of this methodological approach makes the proposed hypothesis and claims convincing.

### Weaknesses
1. While the study primarily focuses on arithmetic tasks, it does not fully explore whether this heuristic-driven mechanism applies to other types of reasoning. Future work extending the approach to different reasoning domains would help determine the generalizability of these findings.
2. Classifying neurons into heuristic types may oversimplify the actual complexity of neuron interactions in LLMs. Additionally, the manual classification of heuristic types could introduce subjective bias.

### Questions
1. How would the proposed heuristic-based mechanism scale with model size or complexity? Does the number or type of heuristics vary significantly with larger models?
2. Would small models trained from scratch on arithmetic tasks also rely on a "bag of heuristics"? Or would they have a different mechanism to learn arithmetic? One suggestion is to train a small model (like using a NanoGPT framework) from scratch and apply the same analysis. 
3. Are there any insights into how these heuristics interact or overlap in other reasoning contexts, such as multi-step reasoning tasks? Does the mechanism generalize across tasks?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper characterizes which neurons correspond to LLM performance on arithmetic problems. First, it demonstrates that only a few attention heads in early layers are important, while MLP layers in later stages play a significant role. Through a more detailed analysis using methods like probing, the study identifies several crucial neurons in MLPs, discovering that certain operands can activate these neurons. Finally, the paper introduces the concept of "bag of heuristics" for these operand-activated neurons, claiming that this mechanism can account for how LLMs solve arithmetic problems.

### Strengths
The paper employs numerous experiments to validate its findings, and the discovery of neurons activated by specific operands is intriguing.

### Weaknesses
Despite applying various methods and experiments, the main contribution and conclusions drawn from the experiments are overclaimed and unclear. I summarize my primary concerns as follows:
1. The paper predominantly focuses on the MLPs in later layers, specifically on the last token ("=" sign), while neglecting the attention module in early layers. However, the representation of the last token in subsequent layers heavily depends on attention from early layers. Understanding how transformers utilize the attention mechanism for arithmetic problems is arguably more crucial than examining the function of subsequent layers. Specifically, the paper does not sufficiently explore how information about the operands and operators is routed through the attention heads to the final token position. This includes analyzing which specific attention heads are responsible for transferring the relevant information and how the attention weights are distributed across different tokens.
2. While arithmetic equations have approximately 1,000,000 combinations, this study only samples 100 prompts for most of its results. This limited sample size introduces significant randomness and undermines the validity of the findings. The paper does not adequately address the potential for sampling bias and the representativeness of the chosen prompts. It is unclear if the observed patterns generalize to a broader range of arithmetic problems or if they are specific to the particular set of prompts used in the experiments. The lack of a systematic approach to prompt selection further weakens the reliability of the conclusions.
3. A critical issue is that this paper fails to provide a clear explanation of how LLMs solve arithmetic problems. For instance, we CANNOT explain how a transformer solves a problem like "21 + 17 =" in **more detail** than: "The LLM computes a representation for the last token based on the context in early layers, and then activates certain neurons to obtain the final result in subsequent layers." The paper does not offer a mechanistic explanation of how the identified neurons in the later MLP layers actually perform the arithmetic computation. It remains unclear how these neurons interact and what specific computations they perform to arrive at the correct answer. The "bag of heuristics" concept is not sufficiently detailed to explain the underlying computational process.
4. The conclusions drawn from the experiments are often overclaimed and unclear. For example, in Section 4, the heuristic matching method is confusing. The results from this method don't seem to provide more useful information than the activation patching experiments. It appears that neurons from any model obtained by this method would likely show results similar to those in Figures 8 and 9. The paper does not provide a clear justification for why the heuristic matching method is superior to other methods for identifying important neurons. The lack of a comparative analysis with alternative approaches makes it difficult to assess the true value of the proposed method.

### Questions
See weaknesses. Another question is about eq(3), can you explain h and v based on SwiGLU equation in https://paperswithcode.com/method/swiglu?

### Soundness
3

### Presentation
2

### Contribution
3
