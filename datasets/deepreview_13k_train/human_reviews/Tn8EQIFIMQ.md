# Language Models Trained to do Arithmetic Predict Human Risky and Intertemporal Choice

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
The observed similarities in the behavior of humans and Large Language Models (LLMs) have prompted researchers to consider the potential of using LLMs as models of human cognition. However, several significant challenges must be addressed before LLMs can be legitimately regarded as cognitive models. For instance, LLMs are trained on far more data than humans typically encounter, and may have been directly trained on human data in specific cognitive tasks or aligned with human preferences. Consequently, the origins of these behavioral similarities are not well understood. In this paper, we propose a novel way to enhance the utility of LLMs as cognitive models. This approach involves (i) leveraging computationally equivalent tasks that both an LLM and a rational agent need to master for solving a cognitive problem and (ii) examining the specific task distributions required for an LLM to exhibit human-like behaviors. We apply this approach to decision-making -- specifically risky and intertemporal choice -- where the key computationally equivalent task is the arithmetic of expected value calculations. We show that an LLM pretrained on an ecologically valid arithmetic dataset, which we call Arithmetic-GPT, predicts human behavior better than many traditional cognitive models. Pretraining LLMs on ecologically valid arithmetic datasets is sufficient to produce a strong correspondence between these models and human decision-making. Our results also suggest that LLMs used as cognitive models should be carefully investigated via ablation studies of the pretraining data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper shows that by solely training next token prediction on arithmetic data requiring computations related to real-world decisions (e.g., computing expectations) it's possible to predict with good accuracy human behavior. Results improve (slightly?) when the pretrained computations involve numbers which resemble real-world distributions.

### Strengths
- I found the results of the paper very surprising, I think that the approach is creative, and to the best of my knowledge, may perhaps offer a minimal explanation for why LLMs replicate human behavior in some cognitive biases - namely, something about the next word prediction mechanism and mathematical data? Without the need for any language-related observations at all.

### Weaknesses
I don't have strong concerns, and I'm generally positive about this paper, though I feel like Section 3.4 (Human Targets) contains many preprocessing decisions with some very specific factors (annual discount factor set to 0.85). I didn’t understand the need for these, or whether they affect the results. For example, I don’t understand this part: “In cases involving ambiguous gambles where probabilities are unknown, we used the special token to denote gambles with unknown probabilities.” (Line 237) Can you please elaborate?

### Questions
- I wonder if the positioning of the paper may be different - something along the lines of "LLMs were observed to replicate human cognitive biases, here we show a possible explanation, indicating that this may be due to the task, architecture, and numerical reasoning, without requiring any natural language supervision, world knowledge or common sense." Does this make sense? If so, I think it would have been easier for me to understand the paper.
- I wonder what would happen if the LLM was trained on other mathematical tasks, not relating to expectation? Would it still be able to explain human behavior to some extent?

### Soundness
3

### Presentation
2

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
The paper presented a method to enable a model to act as a cognitive model for a cognitive task by training it on 1) computationally similar tasks 2) with similar distribution. The authors demonstrate their method on the task of risky and intertemporal choice, by pre-training on synthetic expected value calculations data of ecological distribution. The paper compares their trained model, Arithmetic-GPT, with Llama-3-70B, and a few traditional cognitive models. Arithmetic-GPT shows a good ability to explain human data.

### Strengths
1. The paper is clear and well-written.
2. The method is novel and demonstrates strong results for a small model and relatively small data.
3. The results showcase the method's ability to create a good cognitive model for the target task.
4. The deduction of implicit values from ARITHMETIC-GPT is interesting and insightful.

### Weaknesses
1. The paper is a bit lean on the experimental side.
2. Lack of experimentation with different model sizes that can allow a better understanding of their effect on the model's ability to act as a cognitive model. Similarly, there are no experiments designed to assess the effect of the data quantity that is emphasized as key factors that differentiate humans from LLMs. The absence of a performance drop when using smaller datasets suggests the model might be overfitting to the target data distribution, rather than generalizing from the underlying computational principles. This also connects to the LLaMA3 performance, as it highlights how overfitting to the task and domain is not always straightforward, yet appears to be the case here.
3. The paper claims that their approach is general, but they only train on one type of computational task, e.g. expected value calculations. Another example can enhance the paper, even pointing to other concrete examples can be valuable. For example, does this also hold to more language-oriented tasks? in that case, are smaller dedicated models will also outperform strong LLMs? The connection between the chosen computational task and meaningful hypotheses is not clear, which limits the generalizability of the approach. For language-oriented tasks, training on rational solutions might not yield a cognitive model that is on par with larger, stronger models, especially within the model size class discussed in the paper.
4. Part of your rationale for choosing ecological distribution is that in humans this can lead to computational errors that are the basis for deviating from the rational decision. However, you didn't analyze both LLaMA3 and Arithmetic-GPT computational abilities both in and out of distributions, and examine their effect on the results. Specifically, benchmarking their expected value calculation abilities both in- and out-of-distribution could provide insights into their connection to the results. For instance, does a model that excels in expected value calculations also serve as a better cognitive model? Are 15K examples enough to master this ability?
5. There is no discussion on the trade-off between a general model like LLaMA3 that can act as a cognitive model in a wide array of tasks and a small and dedicated model as you proposed. The fact that LLaMA models perform comparably to the proposed model for the given task, despite not being trained specifically for it, suggests that for many use cases, using a larger, stronger general-purpose model may be more effective than training a specialized cognitive model.

### Questions
1. There are open models with open data e.g. LLM360 and OLMo, how does this affect your LLMs experiment in the context of the paper experiments?
2. Is there a way to produce figures like the ones in Figure 2 from LLaMA3 embeddings?
3. Can a strong model trained on the human data provide a better upper limit and also act as a cognitive model?

Comments:
1. LLaMA3 is a bit better in Intertemporal choices and on par with the Arithmetic-GPT. The text there doesn't reflect that and does not explain it. Also, the top results from LLaMA3 are not in bold.

### Soundness
3

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
Humans often deviate from optimal choices in tasks involving expected value or temporal patterns. This behavior is also observed in LLMs, though embeddings do not fully capture this deviation. This study explores how this tendency arises in language models by pre-training a small model (Arithmetic-GPT) on expectation calculation tasks then testing its alignment with human choices. 

Synthetic datasets (uniform and ecological, each with perturbed and unperturbed versions) are created for model pre-training and tested on four human datasets related to risky and inter-temporal decisions. Model comparisons included pre-trained Llama (natural language input + log-likelihoods, natural language + text embeddings, arithmetic + embeddings), Arithmetic-GPT variants (four dataset versions and no training), four behavioral models, and MLPs directly trained on task features. Results show that Arithmetic-GPT trained on unperturbed ecological data shows the highest explained variance with human decisions (input: embeddings/log-likelihoods, output: human decisions).

### Strengths
- **Originality**: 
     - Proposes a new test environment to evaluate the effectiveness of using language models as cognitive models.
     - The ecological data pre-training approach is a simple approach to model principles with human decision-making patterns.

 - **Quality and Clarity**: 
     - Comprehensive benchmarking across multiple models, including classical behavioral and neural models.
     - Very clear writing, but with minor typos (e.g., line 376, "fitted" → "fit").

### Weaknesses
 Overall, I am uncertain if the proposed task is too simple to make any sophisticated claims on language models as cognitive models. 

 - Does Arithmetic-GPT’s performance really represent actual human decision processes, or is it not possible that Arithmetic-GPT's "human-like behavior” could instead be a reflection of general statistical tendencies that happen to deviate from optimal choice, rather than an insight into genuine human cognition?
- Table 3 shows that Arithmetic-GPT only marginally outperforms the larger Llama model. This suggests that Llama, without specialized pre-training, already captures much of the variance in human choices. I suppose the claim is somewhat valid given the limited capacity of the Arithimetic-GPT backbone, but the authors’ emphasis on Arithmetic-GPT's superiority might be overstated given that its improvement is slight and comes from training on targeted synthetic data.

### Questions
- A minor question regarding the experiments: Why not also try training Llama or Arithmetic-GPT on the task features as the MLP?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors explore how language models can serve as cognitive models by investigating their behavior in risky and intertemporal choice tasks. The authors introduce Arithmetic-GPT, a small language model specifically trained on arithmetic tasks that simulate expected value (EV) and present value (PV) calculations essential to decision-making. By training Arithmetic-GPT (A-GPT) on a non-ecologically and ecologically valid datasets, the authors show that A-GPT exhibits decision-making patterns that closely resemble human choices (in particular for the ecologically valid dataset). Moreover, A-GPT outperforms both traditional behavioral models and some large, general-purpose language models in predicting human risk and time preferences. The work porposed by the authors underscores the importance of tailored training datasets for aligning language model behavior with human cognitive processes and provides insights into how synthetic datasets may enhance models' ability to predict human decision patterns.

### Strengths
1. This work exemplifies the potential of LLMs to gain insights in human cognitive processing, and as a results showcases the elegance of the auhtors thought process.

2. The auhors compare their model to a relevant suite of other models, and use several datasets to drive their point. This systematic comparison highlights the quality of this work and further amplifies the results obtained with A-GPT.

3. The paper is clear and well structured, allowing for smooth reading. The figures are informative and clearly illustrate the points made in the text.

### Weaknesses
Within the range of what the paper is tackling, I do not see any weaknesses in this work.

I do however believe that the authors could have gained further understanding of human risky and intertemporal choices by generating several other datasets that systematically target specific aspect of EV and PV calculations, i.e., parametrically changing the ablation level of specific EV and PV compononents. 

Moreover, it would be interesting to relate the A-GPT results with explainability in order to potentially provide more interpretability to the embeddings.

I will however not discount any points in my rating. I understand the limitations in terms of computation,cost, time and manuscript space.

### Questions
Typo:

There is an issue with the presentation of Figure A2 which falls under appendix F rather than E.

### Soundness
3

### Presentation
4

### Contribution
3
