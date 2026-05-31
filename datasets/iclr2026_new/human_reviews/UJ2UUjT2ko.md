## Human Reviewer 1

### Summary
This paper investigates how LLMs bind and retrieve entities in context. Prior work has suggested that LLMs rely mainly on a positional mechanism, retrieving entities by their relative position in a list of contextually bound entities. However, the authors show that this mechanism becomes unreliable when the context grows and entities appear in middle positions, reminiscent of the lost-in-the-middle effect. To explain this, the paper proposes lexical and reflexive mechanisms that complement the positional one. Through systematic interchange interventions, they find that LLMs dynamically mix these three mechanisms depending on position and entity type. They further build a causal model that combines all three mechanisms and achieves up to 95% Jensen–Shannon similarity with true model predictions.

### Strengths
* The authors propose the lexical and reflexive mechanisms as natural extensions of how binding might operate when positional cues become unreliable. They support these hypotheses with well-designed counterfactual interventions that yield clear empirical evidence. The experimental setup, including controlled manipulations of entity positions and roles, provides high causal interpretability rather than correlational evidence.
* The findings are replicated across nine model families and ten distinct tasks,  demonstrating robustness. The mixture model achieves 95% agreement with LLM token predictions, further demonstrating the faithfulness of the proposed framework.
* The parallels drawn to primacy and recency biases in human memory, and the connection to the lost-in-the-middle effect, make the results conceptually relatable.

### Weaknesses
* The three mechanisms are inferred largely through counterfactual patching, but the causal independence between them is assumed rather than rigorously established. For example, lexical and reflexive mechanisms often co-occur. It remains unclear if they are distinct causal variables or correlated manifestations of shared attention dynamics.
* Although filler text is introduced later, most analyses still rely on templated X likes Y style prompts. These may not capture linguistic variability or discourse-level entity binding.

### Questions
See Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 2

### Summary
The authors explore multiple mechanisms by which transformers LMs track entities in context to retrieve factual information. It's already known that models will track the positions of entities and use this mechanism to answer factual questions. The positional mechanism, however, breaks down when there are many entities in context. The authors find that transformers have two other mechanisms: a lexical mechanism where the model looks up the queried entity and a reflexive mechanism where a model looks up information about a promoted token. These mechanisms can all disagree about the answer to a query, which the authors show with interventional experiments. They also create an effective model of this three-mechanism behavior that closely matches the output distributions of the LMs they test on.

### Strengths
- It seems intuitive that something like the lexical mechanism or the reflexive mechanism would exist. It's somewhat surprising that these are separate.
- The interventions show that the different retrieval mechanisms can disagree in their predictions and behavior on the output distribution, which is compelling.
- The authors create an effective model of the three retrieval mechanisms which closely matches the output distribution of the actual model.
- Polluting the context with additional free-form text is a reasonable robustness check

### Weaknesses
- I'm looking for more details about how exactly the interchange interventions were performed and how the authors localized where to do interchange interventions. From the appendix, it seems like this is based on performing interchange interventions on the attention at specific layers on the last token position? And the authors use attention knockout to figure out which layers are passing entity information to the final token position? Can you clarify?
- The main body of the paper would benefit from a bit more explanation of what exactly is going on here (I'm aware of space constraints, but I think this is important). And the appendix would benefit from a clear, high-level description of what the experiments are actually doing.

Minor suggestions and feedback:
- Putting the counterfactual input on top in Figure 1 feels confusing, seems more natural to have the original on top and the counterfactual below?
- I found the text description of the reflexive mechanism (line 231) to be fairly hard to parse. This seems like something that is much easier to show than to say, so a figure could be helpful.
- Line 159: use \citet instead of \citep

### Questions
- It seems like the model uses the reflexive pathway as a "verification" step. Does the reflexive pathway need to match the entity from the lexical pathway (as it does in Figure 1) to work? Is my understanding of this correct?
- See "weaknesses" above re: questions about how the interchange interventions were performed

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper investigates how language models (LMs) retrieve bound entities in context, e.g., “Pete loves jam, Ann loves pie. Who loves pie?”. The authors identify that retrieval arises from a mixture of three mechanisms: positional, lexical, and reflexive.
- Positional: retrieves the target based on the position of the entity group corresponding to the query.
- Lexical: retrieves the entity bound to the queried token itself (e.g., “pie” → “Ann”).
- Reflexive: uses a direct pointer to the target entity token.
They construct a controlled dataset with paired _original_ and _counterfactual_ examples (with entities shuffled), to identify each mechanism via patching experiments. This setup allows them to separate the contribution of each mechanism to the LM’s predictions. They further show that mixing these three mechanisms explains model behavior in longer contexts where the positional mechanism alone fails.  
Finally, they build a simple causal model incorporating these mechanisms, which closely reproduces the LM’s next-token distribution (≈0.95 Jensen–Shannon similarity).

### Strengths
- **Clarity:** The paper is clearly written and well-organized. The motivation, hypotheses, and experimental setup are clearly presented with concrete examples.
- **Originality:** The discovery of two previously undescribed retrieval mechanisms (lexical and reflexive) extends the mechanistic interpretability literature beyond the known positional mechanism.
- **Quality:** The experimental methodology, which uses counterfactual patching and causal modeling, is rigorous and carefully justified.

### Weaknesses
- **Figures:** Some key figures (e.g., Fig. 2) are difficult to interpret. The axes, metrics, and what constitutes “mixed” effects are not clearly explained in the captions or main text, making it hard for readers to connect the visualization to the described mechanisms.
- **Presentation of reflexive mechanism:** The explanation and evidence for the reflexive mechanism remain somewhat unclear. Because the patched context may already contain the predicted token, it is hard to disentangle whether the observed effect truly demonstrates a “pointer” or simply reflects ongoing retrieval from other mechanisms.

### Questions
Dataset
- Could you specify the range of sizes for the entity set $\mathcal{E}$ in the dataset ? 

Figures
- In Figure 2, what exactly does the _y_-axis represent? Is it the proportion of examples where that mechanism predicts the correct answer? The term “index” on the axis is confusing.
- What does “mixed” mean in this context?
- Are cases excluded where the patching does not predict a valid entity (i.e., none of the entities in the list)? Or does this never happen?

Reflexive mechanism
- In the main text, you mention patching into a context where the target entity is not present, to test the reflexive mechanism. However, it still seems possible that the patched representation already contains the target token’s activation, and that in the new context other mechanisms simply suppress it because the answer is implausible. Could you clarify why this result indicates the presence of a direct pointer, rather than the target token being carried over as a side effect of other retrieval processes already in progress?

Causal Model
- When training the causal model variants that exclude one mechanism, are the weights of the remaining mechanisms retrained independently, or are they frozen from the full model? Clarifying this would help interpret the ablation results.

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
3