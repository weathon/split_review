# Controllable Context Sensitivity and the Knob Behind It

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 3, 8

## Abstract
When making predictions, a language model must trade off how much it relies on its context vs.\ its prior knowledge.
Choosing how sensitive the model is to its context is a fundamental functionality, as it enables the model to excel at tasks like retrieval-augmented generation and question-answering. 
In this paper, we search for a knob which controls this sensitivity, determining whether language models answer from the context or their prior knowledge.
To guide this search, we design a task for \defn{controllable context sensitivity}. 
In this task, we first feed the model a context (\contexttext{Paris is in England}) and a question (\querytext{Where is Paris?}); we then instruct the model to either use its prior or contextual knowledge and evaluate whether it generates the correct answer for both intents (either \answertext{France} or \answertext{England}).
When fine-tuned on this task, instruction-tuned versions of Llama-3.1, Mistral-v0.3, and Gemma-2 can solve it with high accuracy (85-95\%). 
Analyzing these high-performing models, we narrow down which layers may be important to context sensitivity using a novel linear time algorithm. 
Then, in each model, we identify a 1-D subspace in a single layer that encodes whether the model follows context or prior knowledge.
Interestingly, while we identify this subspace in a fine-tuned model, we find that the exact same subspace serves as an effective knob in not only that model but also non-fine-tuned instruct and base models of that model family.
Finally, we show a strong correlation between a model's performance and how distinctly it separates context-agreeing from context-ignoring answers in this subspace.
These results suggest a single subspace facilitates how the model chooses between context and prior knowledge, hinting at a simple fundamental mechanism that controls this behavior.
\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes to localize model behavior when models override their parametric knowledge with knowledge provided in context vs. when they do not override. The authors motivate use cases where each of these behaviors is desired, and thus argue that controlling which behavior models exhibit is crucial for various applications. They create a dataset of counterfactual inputs (such as "The capital of France is London") and instructions (such as "Ignore the context") and then test model ability to answer questions such as "What is the capital of France?" with either "London" or "Paris". The authors fine-tune models on this task or prompt them with in-context examples, and then use patchscopes to localize layers at the last token position of the prompt that decode the models' predicted answers when those answers are correct. The authors ensure the models they test are robust at context vs. parametric answer production after fine-tuning across 3 domains. Given the layers found by patchscopes, they run an iterative algorithm to patch outputs of the layers' multi-head self-attention functions to find those which have the most causal effect on models' production of the (in-context or parametric) answer. Finally, they decompose the patched MHSA outputs into a linear interpolation of the original hidden state and a binary variable representing preference for in-context vs. parametric answers (interpolated using learned weight matrix $\mathbf{P}$). They show that this allows them to effectively intervene on models during inference and adjust their predictions, in a way that is robust across datasets and prompt types. Remarkably, this intervention also works on models not fine-tuned for the task, indicating that instruction-tuned models, while not perfect at following instructions about whether to favor or ignore in-context conflicting information, appear to have a very simple and controllable mechanism underlying this behavior.

### Strengths
- Originality: A creative combination of existing ideas (counterfactual dataset creation, patchscopes, activation patching, and distributed alignment search) to provide insight into a meaningful problem.
- Quality: The experiments are generally comprehensive. I appreciated the detailed effort to ensure that the models being tested can robustly do in-context vs. parametric knowledge production beyond the dataset they were trained on. The authors test multiple instruction prompts, and run experiments on 3 different model families. They also use creatively-constructed pairs of prompts to investigate 3 separate steps of the pipeline: where intent is encoded in the model vs. where each of the two answer choices the model can produce are encoded -- I thought this was particularly creative and interesting.
- Clarity: the paper is generally well-written, especially the problem setting and motivation. The mathematical notation is correct and well-written/easy to follow, which I appreciated. 
- Significance: The problem that the paper sets out to solve is well-motivated and of substantial interest to the research community. Some of the findings are really interesting and will be quite meaningful to the community working on parameter-level understanding and control of model behavior. I would theoretically like to see the paper presented at the conference, but I also have substantial concerns (mentioned below).

### Weaknesses
Major:
- Contribution: my main qualm with the paper is that it overstates the novelty of proposing and providing evidence for the research question that there is a simple fundamental mechanism in LMs that modulates whether LMs defer to information in context vs in weights. This has already been shown (via different methodologies) by prior papers, including those cited by the authors in their related work section: for example, https://aclanthology.org/2023.emnlp-main.615/ showed that particular attention heads have a large effect and they can be reweighted to change this behavior. https://arxiv.org/abs/2402.11655 showed multiple mechanisms that play a role in answering counterfactual queries. The paper would thus benefit substantially by toning down this claim of novelty to instead focus on what is different about the proposed methodology that allows the authors to build upon prior work (which the paper does do meaningfully). Relatedly, the proposed counterfactual dataset shares many similarities with prior work. See "missing citations" below for references.
- Related Work: the related works section is lacking a # of related works, and the authors do not spend enough time comparing to or discussing the differences with the related works that are cited (such as Yu et al 2023 and Jin et al 2024, or papers which created counterfactual datasets similar to that proposed in this paper). There should probably be a dedicated paragraph to models handling conflicting knowledge in context vs. in weights and how people have tested this/localized it in addition to the existing paragraph on model interventions for control (see "missing citations" section for some cites).
- Method: the limitation of only patching the outputs of the multi-head self-attention function could partially explain why, e.g., the authors fail to find any localization of the contextual answer mechanism in Figure 2d. I was surprised the authors chose to restrict their study to MHSA functions when there is substantial evidence that MLPs play some role in the production of parametric knowledge like factual queries. Given that we also know that there are redundant mechanisms in overparameterized LMs such that multiple causal interventions could lead to a large effect, I believe a more broad and impactful approach would be to first perform interventions at the final hidden state output of each layer (i.e., residual stream) before narrowing down to the MHSA or MLP functions.

More minor:
- heavy use of terms like "one dimensional subspace" to describe the impact of the paper's findings without any concrete definition given. The authors assume a substantial amount of linear algebra background in readers (see question below-- this may be due to my personal confusion, so I am open to resolving this critique in the rebuttal)
- method: the authors only focus on the final token position in their analysis, so they may be missing some interesting effects (such as which token positions the found causally relevant attention mechanisms at the final token position are attending to). However, I understand looking at more token positions can be quite computationally intensive and the experiments needed to be restricted in some way. 
- It would be valuable or interesting to show some of the patchscope results in the paper apart from the best found set of layers in Figure 2, i.e., how the iterative algorithm built up to the final result.

### Questions
Questions:
- I don't fully understand the claim about the editing occurring in a low-dimensional/rank-one and orthogonal (to what?) subspace, when the learned square linear projection matrix ($P$) is of the same dimensions as the model hidden state. Is this referring to the fact that the intervention (eqn 4) only occurs on a vector defined by a singular constant? Even so, I still don't understand why the loss and/or editing rule (eqns 3 or 4) ensure that the learned projection matrix $P$ is rank-one or orthogonal. I would appreciate clarification on this in the rebuttal. (Regardless of my personal confusion, I think the paper could strongly benefit from at least some explanation of these terms for the reader's benefit).
- "We hypothesize that for a model to solve this task,..." (lines 69-70, 178-179): is this your hypothesis, or did it come from the prior work that you cite (Jin et al 2024)?
- Can you explain a bit more in the paragraph "Iteratively searching for model components" when you apply patchscopes vs. when you apply patching? I didn't understand in the pseudocode why you need to apply both when you could just directly calculate the score assigned to the token(s) of interest after activation patching as is traditionally done

Minor comments/suggestions:
- activation patching was first proposed in https://proceedings.neurips.cc/paper/2020/hash/92650b2e92217715fe312e6fa7b90d82-Abstract.html and https://arxiv.org/abs/2004.14623, not Meng et al 2022.
- it would be good to provide some small amount of background on what the "residual stream" is (and general structure of the Transformer block) for unfamiliar readers
- duplicated sentence in lines 060-065, typo line 130
- I didn't find the upper figures for each of 2a-2d to be particularly meaningful-- particularly if you're not patching *into* the residual stream directly, I didn't understand the dotted line
- a nit, but you use $a_c$ and $a_p$ for both predicted labels and correct labels. Later on you clarify that you only look at correctly predicted instances, so they are the same, but it would be worth mentioning this when you introduce the notation

Some missing citations:
- https://arxiv.org/abs/2402.11655
- https://arxiv.org/abs/2305.16572
- https://openreview.net/forum?id=auKAUJZMO6
- http://arxiv.org/abs/2404.06283

Some others about how models handle irrelevant context:
- http://arxiv.org/abs/2302.00093
- https://openreview.net/forum?id=Tigr1kMDZy
- http://arxiv.org/abs/2310.01558

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies how models choose between input context vs parametric memory when making predictions. To do so, the work designs a task where a knowledge conflict exists between parametric knowledge and provided context, and the model is instructed to either follow the context or ignore the context. The model is then adapted to this task, and the work isolates a subset of layers in the model that can cause a model to switch its prediction to one that agrees either with the context or with prior knowledge. The authors then identify a one-dimensional subspace, or a “knob”, that controls the extent to which a model’s decision will follow the provided context rather than a prior.

### Strengths
* This paper investigates the mechanisms by which models handle the interplay between drawing upon knowledge from their parameters vs relying on context. This paper looks at the specific parts of the model that are responsible for how the model chooses between the two sources. This line of enquiry is very interesting.
* The paper demonstrates that these subspaces can be isolated in multiple different models and the results are generalizable.
* The paper is well-written and clear.

### Weaknesses
 * While the paper is well-written and clear, the framing around main contributions can be made more precise (see questions to authors).



### Questions
1. “These findings suggest a step forward toward developing more robust language models with controllable levels of reliance on context and prior knowledge.” It would be great to describe in more detail why practitioners might want a knob to control context-sensitivity if it depends on individual samples . For example, for some kind of frequently-updated knowledge (‘who is the President of the US’), relying on context may be helpful if it is sourced from an up-to-date datastore, but for some other kinds of knowledge (‘what is the capital of France’) either the parametric memory or context may be useful. Since this seems like a property where the judgement would need to be made on a sample-by-sample basis, it would be good to understand why a practitioner might want a “knob” to set and freeze it. 
2. Similarly, why not just finetune for controllability over context reliance/parametric knowledge reliance if its already a step of the procedure? Why try first finetuning, then identifying the 1-d subspace, then setting its value?
3. The task is framed as a conflict to indicate which of two sources of information the model chooses to make its prediction (“when making predictions, a language model must trade off how much it relies on its context vs. its prior knowledge”). However, I am also curious about whether models may be aggregating information from their parametric knowledge and provided context, and the function of the knob when such a tradeoff does not exist.
4. For Figure 3, would it be possible to compute a baseline for the instruction models without any intent instructions where F_{w} is not set? I expect SIA here to be low but it would be a good sanity check.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper endeavors to tackle the problem of adjusting a language model’s response based on whether it should rely on the given context versus what it’s seen during training. The authors introduce a framework to create a "knob" for adjusting a model's context sensitivity, enabling it to answer based on either provided context or its internal knowledge. 

The main contributions include (1) identification of a 1D subspace that appears to encode preference between context and prior knowledge and (2) experiments using Llama that suggest this knob can be used to modify the sensitivity to the context in certain zero-shot and few-shot settings.

### Strengths
This is an important topic with immediate applications in tasks like retrieval-augmented generation, question answering, and misinformation avoidance.

### Weaknesses
 * The proposed steering methodology doesn’t seem to outperform finetuning baseline, in which case, I’m not sure why practitioners would adopt a fairly more complex approach to this problem.
* I’m not sure the motivation for this problem is clear. Suppose you are given a context and query, if you know that the context should be ignored, why not just manually exclude the context rather than manually set the value of c(w) (e.g., in the example on line 441) and learn this rank-1 orthogonal projection matrix P. The proposed steering methodology indeed seems to perform better for Llama-3.1 8B ICL, and Llama-3.1-Instruct 0-shot but how much of this can be accounted for by just excluding the context in the cases where w = pri. It would make more sense if you want to automatically learn when to leverage the context and when to ignore it, but that doesn’t seem to be the problem that the paper wants to tackle.

### Questions
* How often do you need to learn/re-learn the projection matrix P?  
* Do you anticipate this will work for larger models like Llama3-70B, which is likely better than 8B at ignoring irrelevant contextual information?
* I wonder if you have any intuition as to why finetuning doesn’t seem to help at all on the Arithmetic task compared to ICL.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a method for controlling context-sensitivity in LLMs, allowing them to prioritize either context or prior knowledge based on a "knob" discovered within a specific layer’s subspace.

### Strengths
**Originality**
The authors define the task of controllable context sensitivity and develop new methods to probe model behavior.

**Quality**
The paper presents experimentation across multiple models (Llama, Mistral, and Gemma) strengthening the findings and supporting the claim of a "fundamental mechanism" in language models.

**Clarity**
The paper is well-written.

**Significance**
By uncovering a controllable mechanism for context reliance, this research has practical implications for enhancing model robustness in real-world applications, such as avoiding hallucination or misinformation. The findings advance the understanding of model interpretability by identifying a consistent subspace that regulates context sensitivity across multiple models, which could inspire further research into model control and intervention strategies.

### Weaknesses
See Questions below

### Questions
1. The current scope of the "knob" is limited to toggling between context and parametric knowledge, but the study doesn’t investigate whether this mechanism might extend to other desirable behaviors, such as controlling for safety, reducing bias, or maintaining consistency. Does the subspace affect other behavior of the LLM which may or may not be desirable?

2. A comparison against previous techniques, mentioned in Section 2, would showcase the usability of the proposed technique.

### Soundness
4

### Presentation
4

### Contribution
4
