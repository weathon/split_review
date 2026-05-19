### Summary

The paper proposes a framework to evaluate the rationality and strategic reasoning abilities of LLMs by having them play economic games. The authors show that LLMs exhibit bounded rationality and that some models adapt to game configurations and opponents’ strategies. Some models also make use of game history to improve performance. The authors also introduce an economics arena as a dynamic benchmark to test these abilities of LLMs.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper studies an interesting question. The paper demonstrates some degree of success in enabling LLMs to play economic games. The paper also shows that some LLMs break rules less often when the games and the instructions become more complex, which is an interesting observation.

### Weaknesses

#### Some Related Works


#### comment

The paper is not clearly written. In particular, the methodology section is not well described. It is not clear how the authors ensure that the LLMs understand the economic game they are asked to play. It is also not clear how the LLMs play these games. The paper also lacks analysis on why some LLMs perform better than others. The findings are not particularly novel.

### Suggestions

The paper needs a more detailed explanation of the methodology. Specifically, the authors should clarify how the LLMs are prompted to play the economic games. What specific instructions are given to the LLMs? How are the payoffs and costs represented to the LLMs? It is crucial to understand the exact format of the prompts and the information provided to the LLMs to assess the validity of the results. For example, are the LLMs given a textual description of the game, or is there a more structured input format? The authors should also clarify how the LLMs' actions are translated back into the game environment. Are the LLMs outputting numerical values directly, or are these values extracted from textual responses? Providing concrete examples of the prompts and the LLM outputs for different games would greatly improve the clarity of the paper.

Furthermore, the paper should include a more in-depth analysis of why some LLMs perform better than others in these economic games. The current analysis is limited to observing that some models perform better, but there is no investigation into the underlying reasons. For example, do models with larger training datasets perform better? Do models with different architectures exhibit different strategic reasoning abilities? The authors should explore these questions by analyzing the models' internal states or by conducting ablation studies. It would also be beneficial to analyze the error patterns of different models. Do certain models consistently make the same types of mistakes? This could provide insights into the limitations of each model. The authors could also consider using techniques such as attention visualization to understand which parts of the input the models are focusing on when making decisions.

Finally, the paper should more clearly articulate the novelty of its findings. While the application of LLMs to economic games is interesting, the paper does not clearly demonstrate how its findings are novel compared to existing work on bounded rationality and strategic reasoning. The authors should explicitly compare their results to previous studies and highlight the unique contributions of their work. For example, do the LLMs exhibit any novel behavioral patterns that have not been observed in previous studies of human or artificial agents? The authors should also discuss the limitations of their approach and suggest directions for future research. This would help to contextualize the paper's findings and demonstrate its significance to the field.

### Questions

1. Can you describe your methodology? How do you make sure that the LLMs understand the economic game that you ask them to play? How do LLMs play these games?
2. Can you analyse why some LLMs perform better than others? Do LLMs with larger training datasets perform better? Are there any other correlations?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
