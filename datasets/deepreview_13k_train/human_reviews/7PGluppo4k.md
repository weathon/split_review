# Logically Consistent Language Models via Neuro-Symbolic Integration

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Large language models (LLMs) are a promising venue for natural language understanding and generation.
However, current LLMs are far from reliable: they are prone to generating non-factual information and,
more crucially, to contradicting themselves when prompted to reason about relations between entities of the world.
These problems are currently addressed with large scale fine-tuning or by delegating reasoning to external tools.
In this work, we strive for a middle ground and  introduce a loss based on neuro-symbolic reasoning that teaches an LLM to be logically consistent with an external set of facts and rules and improves self-consistency even when the LLM is fine-tuned on a limited set of facts.
Our approach also allows to easily combine multiple logical constraints at once in a principled way, delivering LLMs that are more consistent w.r.t. \textit{all} constraints and improve over several baselines w.r.t. a given constraint.
Moreover, our method allows LLMs to extrapolate to unseen but semantically similar factual knowledge, represented in unseen datasets, more systematically.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores improving LLMs' factuality and logical consistency through neuro-symbolic reasoning. It introduces a neuro-symbolic loss function that is used to fine-tune LLMs on a given set of external facts and rules. Experiments show that this approach achieves improved consistency and generalizes more effectively to unseen yet similar constraints compared to baseline methods, including those that rely on external reasoning tools.

### Strengths
The paper offers a novel approach by integrating neuro-symbolic reasoning into the fine-tuning of large language models (LLMs) to improve factuality and logical consistency. While existing approaches for enhancing consistency in LLMs often rely on external reasoning tools or extensive fine-tuning, this paper proposes a middle-ground solution: a neuro-symbolic-based loss function that promotes logical consistency by maximizing the probability of constraint satisfaction. This approach (LoCo-LMs) is grounded in weighted model counting and semantic loss, offering a flexible framework that applies consistently across various logical constraints, such as negation and implication.

The paper conducts extensive experiments to showcase LoCo-LMs' effectiveness over traditional approaches, demonstrating improvements in logical consistency, factuality, and transferability across different logical constraints and datasets. The method also proves efficient, achieving good performance even with limited training data.

By enhancing logical consistency without requiring external reasoning frameworks, the approach has important implications for deploying LLMs in tasks that demand reliable, logic-based reasoning. Its ability to generalize to unseen (yet semantically similar) facts presents a promising pathway for real-world applications where models need to work reliably with sparse data.

### Weaknesses
Evaluation scope:

The experiments primarily focus on logical constraints such as negation, implication, and reverse implication. While these are fundamental, they fall short of capturing the more complex reasoning scenarios often required in real-world applications. For instance, the paper could improve by incorporating evaluations on multi-hop reasoning tasks or exploring more sophisticated logical constraints.


Shift in language modeling distribution:

The authors assess possible shifts in the language modeling distribution by measuring changes in perplexity, yet their evaluation could be expanded. Adding downstream tasks (e.g, question answering, reading comprehension, mathematical reasoning, etc.) would allow to assess whether the proposed fine-tuning approach not only improves logical consistency but also maintains the language capabilities of the original model.


Robustness of the results:

The experiments reveal that fine-tuning LoCo-LMs improves generalization only within the same type of constraints, and it even hurts performance when the constraints differ between fine-tuning and testing (see Table 4). This limitation could be especially pronounced in smaller models, so testing on larger models could provide further insights. It would also be valuable to explore whether these performance gains also transfer to more capable models, such as comparing performance between LlaMa 2 and LLaMa 3, with and without LoCo-LMs.


Sensitivity to prompting:

The effectiveness of the approach appears to be sensitive to the specific prompt formats used during fine-tuning and evaluation. This suggests that the gains in consistency might be partially due to prompt selection rather than the model’s inherent logical coherence. Broader testing across diverse prompt templates would enhance the robustness and reproducibility of the results. Moreover, there are alternative prompting methods to elicit logical consistency, such as prompting the model to respond sequentially to a series of related questions, conditioned on previous answers.

### Questions
Please see "Weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces LoCo-LLM, a fine-tuning method for LLMs that leverages a neuro-symbolic inspired semantic loss function to enhance its factuality and logical consistency. The proposed semantic loss function is based on weighted model counting, with weights derived from the LLM’s probability estimates. LoCo-LLM employs sentential decision diagrams to efficiently compute this loss.

Detailed experiments compare LoCo-LLM with baselines that use external reasoners and traditional cross-entropy-based fine-tuning. Experimental results on the BeliefBank and EntailmentBank datasets show that the proposed framework outperforms baselines on metrics such as factuality and consistency.

The code to reproduce these results is provided as supplementary material and will be released on GitHub under a permissible license.

### Strengths
- The idea of using a neuro-symbolic loss function to improve logical consistency and factuality in LLM responses is novel and interesting. The proposed loss function is generalizable, can be extended to complex logical constraints, and may prove useful in enhancing LLMs' reasoning capabilities.
- The detailed experimental results demonstrate the advantages of the proposed method over baselines, even on relatively small (5-10%) datasets.

### Weaknesses
 - Although the loss function is explained thoroughly, other components, such as circuits and sentential decision diagrams, are not discussed in detail. Including these details would improve the paper's readability.

- The experiments are conducted on datasets with outputs of fewer than 4 tokens, leaving it unclear how well the proposed method supports generating longer, factually and logically consistent responses.

### Questions
- For the pre-trained baseline models in Tables 1 and 2, do the scores improve with greedy decoding?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a fine tuning method for improving logical consistency in language models. Given a set of facts and a set of constraints the idea is to finetune the model to make sure that certain logical constraints are respected, typically implication and negation. The authors show that indeed finetuning allows to improve self consistency and that this transfers beyond the facts and constraints used for finetuning to other entities and and settings.

### Strengths
The problem of improving logical consistency in language models is important. The approach is simple and does not require a lot of inference time compute since it is based on finetuning. The empirical results that show transfer and generalization beyond the training distribution are informative and interesting.

### Weaknesses
 * Clarity: the paper can do a better job at explaining the details of its method. The authors spend two pages (section 2) on explaining logical constraints in a way that is too elaborate (for example, defining the xor operator in line 124, and defining implication in terms of negation and or in line 137) and unnecessary. On the other hand details on the actual method is limited (see questions below), specifically the paragraph in 232 and the precise process of how logical constraints are transformed into differentiable graphs are explained in a manner that is insufficient. The description of the experiments also mixes unimportant implementation details with more important details on the experimental setup which makes it hard to understand the details of the experiments and what can be concluded from them.

* Related to the above - Figure 1 takes a lot of real-estate but is not helpful. The only thing we see is that there is baseline that makes a mistake on 3 examples and the proposed model does not make the mistake. This does not say a lot on the method, or the aggregate results only we can learn about the types of logical constraints that will be used. This might be ok if the important parts of the paper were clear, but they are not sufficiently clear at this point.

* Key point that was unclear to me:  line 242 paragraph: I don’t understand if the method handles facts that can be inferred from \alpha and the KB but require more than one hop? When training the SL loss, are those considered? Say we have in the KB, “albatross is a bird”, “birds are an animal”, “albatross can fly”, “if an animal can fly then the animal can move”. Will the SL loss contain a term about whether albatrosses and whether they can move or not? Is this done implicitly somehow? Where do we do the inference of all potential things that can be inferred from the KB and the constraints and take those into account in the SL loss?

* More on clarity: in section 3, you define \mathcal{D}_c = {alpha_1, \dots, \alpha_m}. But the structure of \alpha is not clearl defined. It would be gold ot make this much clearer, it becomes clearer later as you read more, but should be explained better at this point.

* Clarity: z ~p_\theta(z) is confusing. Supposedly p_theta is the language model and it look like sampling from the unconditional distribution of text, but the text says something else, that it is sampling truth assignments conditioned on what appears in \alpha_i but this is not clear from the notation.

Another key point are some problems with clarity and worries about the experimental setup. 

* IIUC the only baseline that is reported that is not from the authors is ConCord for which two numbers exactly are reported and that's it. There is some reference to maieutic prompting but it is unclear if this should be another baseline or is too similar to ConCord. It is not clear if there are not reasonable baselines to compare other than that. There is reference to few-shot baselines, but it is not expalined what are the examples in the few-shot examples and how they are supposed to help, in fact in many cases results are worse for few-shot compared to zero-shot. Overall, the authors should make clear if there is no past work beyond ConCord and just finetuning on the KB (XENT) without using the constraints

* Second, for ConCord, it seems that the authors use ROBERTA-ANLI as an inference model. But for their LOCO method it seems like they are using hard constraints that are guaranteed to be true - if that's the case this is unfair towards ConCORD. Can the authors provide more details about how and why they outperform ConCord? Do the two methods use the same models and same constraints? Form the fact that the authors say that Concord requires ROBERTA-ANLI it sounds like the answer is "no" but would be good to understand better what's going on. Since we only have two numbers in the paper that are not baselines implemented by the authors it is important to understand the details in this setup.

To conclude, I found the overall premise of the paper interesting but the paper needs to be clearer both in terms of method and in terms of experimental results and how they relate to past work.

### Questions
* Line 192: the authors claim that they expect transfer from albatross to cockerel since they are similar - but there is no definition of what is similarity, and how should the model know when things are similar enough to conclude new facts about entities and when not. I assume this refers to some vague simlarity measure in the space of hidden representations, but this is still confusing.

* Line 469 - where are the resutls? are they in Table 3? the paper doesn't say

* What is the few-shot baselines precisely? what are the examples given and how are they helpful?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper describes an approach for improving the logical consistency and factuality of language models, using neuro-symbolic integration.
The paper starts with a list of facts and logical constraints. All the valid combinations of truth values for these facts are then iterated and used as targets during optimization.
The experiments evaluating the correctness and consistency of the learned facts show that this method outperforms vanilla models and a baseline using an external solver.

### Strengths
The paper is making advancements in neurosymbolic modelling.
It is certainly a nice achievent to not have to rely on an external solver and being able to push the knowledge into the main neural model.

### Weaknesses
The evaluation is the weakpoint of the paper at the moment.

Macaw-Large, which is used for the main experiments, is quite old already (pre-LLM).
Even Llama-2 used in later experiments is much less capable on most tasks compared to the current Llama-3.2.
This raises questions how applicable the proposed methods are to the current generation of language models.

The main baseline is CONCORD, which is from 2019 and uses RoBERTa.
The fact that the proposed system is able to outperform this baseline without using an external solver is great.
But there really should be some additional baselines with newer methods that also use model updating.
For example, there is a whole library of papers focussing on updating specific facts in language models using targeted fine-tuning.

The whole evaluation is performed on very artificial tasks. It would be very useful to see how these changes impact the model performance in practical applications.


Asking the LLM “Is an albatross not an organism?” is a very unnatural phrasing, whereas LMs are trained to predict natural continuations. I suspect that may be negatively affecting the performance for LMs.

### Questions
The method relies on collecting the probabilities for specific tokens to estimate the yes/no probabilties.
How much is this going to be affected by the label bias of the LLMs?
https://openreview.net/forum?id=shr9PXz7T0
https://arxiv.org/pdf/2402.09910

### Soundness
3

### Presentation
3

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
This paper introduces LOCO-LMS, a fine-tuning method grounded in neural-symbolic reasoning, which significantly enhances the logical consistency and factuality of LLMs by integrating logical constraints as loss functions during training. Unlike traditional methods that rely on external reasoning tools, LOCO-LMS internalizes logical rules, allowing the model to reason independently and improving overall efficiency.

### Strengths
1.  LOCO-LMS effectively improves the model's logical consistency, accommodating complex logical relationships such as positive implication, reverse implication, and negation. This alignment with common sense enhances the quality of responses generated by LLMs.

2.  By incorporating semantic loss, the method minimizes reliance on external reasoning tools, thereby lowering reasoning costs and increasing inference speed.

### Weaknesses
 1. The model assumes that facts are conditionally independent under a given model state, but in actual applications, there may be dependencies between facts, and this assumption may affect the consistency effect. This assumption, while common in neuro-symbolic AI, may limit the model's ability to handle complex scenarios where facts are interlinked. For instance, if the model learns that 'A implies B' and 'B implies C', it might not inherently grasp that 'A implies C' without explicit training on this transitive relationship, leading to inconsistencies when such dependencies are not directly encoded.

2. While it addresses factual inconsistencies in the Llama-7B model, I also concern that its efficiency and scalability may lag behind approaches based on RAG and knowledge editing. The fine-tuning approach, while effective for the specific tasks it targets, might not scale as efficiently to larger models or more diverse datasets compared to retrieval-augmented methods that can leverage external knowledge sources. The computational cost of fine-tuning, especially with complex logical constraints, could become a bottleneck as the model size and the complexity of the logical rules increase.

3. LOCO-LMS is designed for specific tasks and fine-tuning, which limits its applicability to more complex reasoning tasks. Additionally, it may be vulnerable to attacks, such as just-in-time injection. The method's reliance on pre-defined logical constraints during fine-tuning might make it less adaptable to novel or unforeseen reasoning scenarios. Furthermore, the model's internal reasoning mechanism could be susceptible to adversarial attacks that manipulate the input to bypass the learned logical constraints, potentially leading to inconsistent outputs.

### Questions
1. Can LOCO-LMS be adapted for more complex, multi-level, or nonlinear logical reasoning scenarios?

2. How well does LOCO-LMS integrate with existing knowledge editing methods when it comes to incorporating new facts or updating knowledge bases?

### Soundness
3

### Presentation
3

### Contribution
3
