# Overthinking the Truth: Understanding how Language Models Process False Demonstrations

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
\label{sec:abstract}
Modern language models can imitate complex patterns through few-shot learning, enabling them to complete challenging tasks without fine-tuning. 
However, imitation can also lead models to reproduce inaccuracies or harmful content if present in the context. 
We study harmful imitation through the lens of a model’s internal representations, and identify two related phenomena: \emph{overthinking} and \emph{false induction heads}. % are heads a phenomenon? should we just say ``false induction''?
The first phenomenon, overthinking, appears when we decode predictions from intermediate layers, given correct vs.~incorrect few-shot demonstrations. 
At early layers, both demonstrations induce similar model behavior, but the behavior diverges sharply at some ``critical layer'', after which the accuracy given incorrect demonstrations progressively decreases. 
The second phenomenon, false induction heads, are a possible mechanistic cause of overthinking: these are heads in late layers that attend to and copy false information from previous demonstrations, 
and whose ablation reduces overthinking. 
Beyond scientific understanding, our results suggest that studying intermediate model computations could be a promising avenue for understanding and guarding against harmful model behaviors

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates how language models can learn to generate harmful outputs from few-shot prompts containing inaccuracies or biases. 

The key findings are:

Models tend to "overthink" and decrease in accuracy on incorrect prompts after a certain "critical layer", while accuracy keeps improving on correct prompts. This suggests incorrect information mainly affects later processing stages.
Attention heads in later layers preferentially attend to and reproduce incorrect labels from the prompt demonstrations. Ablating a small number of these "false induction heads" significantly reduces the accuracy gap between correct and incorrect prompts.

### Strengths
The paper:
- Provides novel insights into the internals of in-context learning through layerwise decoding and attention analysis. Links model behavior to specific components.

- Extensive experiments across models, datasets and prompt variations. Head ablation results generalize across tasks.

- Connects to related ideas like overthinking and induction heads. Builds understanding of model internals.

### Weaknesses
The paper lacks in the following ways:
- Focuses on a simplified setting of permutations of class labels. 
- Does not cover more subtle inaccuracies or biases.
- Only studies text classification tasks. Unclear if findings apply to more open-ended generative tasks.
- No modification of model training process itself to mitigate issues.

### Questions
- If the prompt contained factual inaccuracies or harmful content, would you expect to see similar overthinking and false induction effects?
- Could you train with additional regularization to discourage attention to incorrect prompt content?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on understanding how language models process correct versus incorrect inputs in few-shot learning contexts, emphasizing harmful imitation. Two phenomena are identified: overthinking and false induction heads. Overthinking occurs when models, given incorrect demonstrations, tend to have reduced accuracy when predictions are decoded from later layers; stopping the model early, before all layers have processed the input, can increase accuracy. False induction heads are specific components in the model that contribute to overthinking by attending to and replicating incorrect information from previous demonstrations. The study's findings advocate for a deeper examination of intermediate model computations to understand and mitigate harmful behaviors in language models​.

### Strengths
- The paper explores new concepts like "overthinking" (previously introduced) and "false induction heads" (novel), offering a fresh lens to study transformers, particularly in handling harmful imitation.

- Solid research execution is evident. Specific model components, like attention heads causing errors, are identified and well analyzed.

- The paper is well-structured and very readable. Concepts are clearly and consistently articulated.

- The methodologies provided comprise a strong set of interpretability methods directed specifically at in-context learning and the role of the examples included.
  - For instance, interpreting outputs from intermediate layers in such ways may prove useful for understanding what the optimal sets of example to provide to the LLM is, in addition to what is attempted in this paper, which is to understand how bad examples affect overall accuracy.

- The paper studies the important issue of harmful content (which, as outlined above, may extend eventually to non-useful or even non-optimal content within the context). Overall, the findings are practically significant and offer insights for controlling model outputs against harmful examples and wrongful imitation.

### Weaknesses
 - The paper details the phenomena of overthinking and false induction heads, but it doesn’t fully articulate how these insights could be applied practically to improve model behavior.
  - For instance, while head ablations are discussed as a method to reduce overthinking, the practical impact of these modifications on model functionality and broader applicability is not thoroughly explored in real-world scenarios​ i.e. how does one know when the input examples are likely to be false, and that heads ought to be ablated?
- The methodology involves decoding from intermediate layers and identifying false induction heads, but the paper could provide a more explicit explanation of these processes i.e. how predictions were extracted and analyzed at each layer, and how the heads contributing to overthinking were identified and analyzed.
- The paper could better acknowledge that the 'incorrectness' of permuted labels can vary based on the dataset and what each label signifies. Some permuted labels might be clearly wrong, while others could be more ambiguous, and providing specific examples for each dataset could clarify this aspect and help to understand the results.
  - It's not clear in the example from Figure 1 that demonstrations are "incorrect", and that all "imitation" is wrongful- there is still an argument that context is important, and in this example (at least in the example where all labels are permuted), could the LLM not understand the label permutation and simply interpret that negative sentiments require a positive classification, and vice versa?
- The reference and justification around the use of the logit lens near the start of the paper could be strengthened, though the authors do come back to discuss it in more detail towards the end.

### Questions
Please see weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies inner mechanism of LLMs when facing false demonstations.

### Strengths
I like this paper. This work provides interesting findings.

### Weaknesses
1. Since the authors conduct experiments under in-context learning setting, we may not be sure these findings are from models themself or implicit tuning (in-context learning). Could the authors provide explanations?

2. Can we expand tasks to include generation-based tasks like QA?

### Questions
Please see Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
