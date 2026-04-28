# Understanding the learned look-ahead behavior of chess neural networks

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
We investigate the look-ahead capabilities of chess-playing neural networks, specifically focusing on the Leela Chess Zero policy network. We build on the work of Jenner et al. by analyzing the model's ability to consider future moves and alternative sequences beyond the immediate next move. Our findings reveal that the network's look-ahead behavior is highly context-dependent, varying significantly based on the specific chess position. We demonstrate that the model can process information about board states up to seven moves ahead, utilizing similar internal mechanisms across different future time steps. Additionally, we provide evidence that the network considers multiple possible move sequences rather than focusing on a single line of play. These results offer new insights into the emergence of sophisticated look-ahead capabilities in neural networks trained on strategic tasks, contributing to our understanding of AI reasoning in complex domains. Our work also showcases the effectiveness of interpretability techniques in uncovering cognitive-like processes in artificial intelligence systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Building upon the previous work of Jenner et al., 2024, this study expands the analysis to examine evidence of learned look-ahead in a powerful chess-playing network. While the original work demonstrated look-ahead capabilities of 1 and 3 moves, this study extends the analysis to consider look-ahead depths of 5 and 7 moves. Additionally, the study presents evidence suggesting that the model can consider multiple lines of move sequences.

### Strengths
- Expands on previous mechanistic interpretability results further, which were open questions from that work, which is important to show that these models can perform deeper look-ahead than previously thought, answering more broader questions about what kind of algorithms these networks can learn purely through data and gradient descent.
- Introduces the puzzle set notation which allows the separation of positions where moves either share or have distinct squares, which allow studying what board distributions are treated in what way by Leela in terms of look-ahead, and provide an analysis about what kinds of board positions we should expect to see Leela do 5th and 7th move look-ahead.

### Weaknesses
- Apart from the puzzle set notation and separation of chess position input distributions, it is not clear what novel conceptual contributions are made in this work that might be more broadly applicable to interpretability research. For instance, the previous work introduced the idea of using a smaller model to filter positions, a bilinear probe design, finding L12H12, and more.
- The claim about the model considering alternative sequences of moves is not convincing (see questions), since there were no interventions done that would make the model pick the _alternative_ move. If indeed the model was deciding between two variations, patching moves from the principal variation should lead to a _reduction_ in log-odds of the primary move.

### Questions
- Primarily if there were any experiments done to make the first move probability reduce in these multiple lines cases, not just increase.
- If the authors want to highlight any novel conceptual techniques that were not prominently highlighted that would be more broadly applicable.

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
The paper extends recent work by Jenner et al. (2024) and investigates whether a chess-playing transformer network exhibits search-like behavior. The original paper found evidence for lookahead within a single line of play, for up to 3 consecutive moves. This paper considers sequences of up to 7 moves, along with positions with two plausible lines of play, and shows evidence that the network considers moves further in the future as well as moves on alternative lines of play. It also shows evidence that the network's behavior is context dependent, with certain attention heads mainly active in a subset of the positions and not others.

### Strengths
The paper extends recent work by Jenner et al. (2024) and investigates whether a chess-playing transformer network exhibits search-like behavior. The original paper found evidence for lookahead within a single line of play, for up to 3 consecutive moves. This paper considers sequences of up to 7 moves, along with positions with two plausible lines of play, and shows evidence that the network considers moves further in the future as well as moves on alternative lines of play. It also shows evidence that the network's behavior is context dependent, with certain attention heads mainly active in a subset of the positions and not others.

### Weaknesses
1. I suspect the audience for this paper could be rather limited, as it relies heavily on the interpretability techniques and evaluation methods introduced in the previous paper. Furthermore, it does not introduce new methodology, other than filtering the dataset into more fine-grained subsets. (Though I do think it answers interesting and unresolved questions from the prior work.)

2. The substantial filtering required to find positions that satisfy the constraints for deeper lines and multiple lines means that they use a much smaller dataset, and the results are likely less statistically significant. However, it should be possible to run these experiments on a much larger starting dataset, and it would be interesting to see if these findings hold up.

3. The log odds reduction plots (e.g. Fig 2) use hue and line-style that are quite unintuitive. I would suggest either making the colors distinct for distinct board squares, or use solid/dashed to distinguish the main/alt line with the same hue for the same move. In any case, there should be some simple scheme that's clearly documented in the main text.

4. The core result seems to be the finding that the model considers multiple move sequences, instead of just the main line. This is significant, as it means the model does search and not just look-ahead. However, these results are explained in just a few paragraphs near the end of Sec 3. I would suggest expanding this section.

5. I would also recommend the authors include (perhaps in the appendix) details about the methodology that are derived from the Jenner et al. paper, so that readers unfamiliar with the prior work will be able to understand what's going on.

### Questions
1. Have you considered using a larger dataset to verify these findings are statistically significant?

2. Is there an intuitive way to interpret the hue and line-style for the log odds reduction plots?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper analyses the look-ahead capabilities of Alpha-Zero like chess-playing programs. Specifically, the authors consider Leela Chess Zero and show the program’s ability to perform longer-term planning (up to 7 half-moves). Through a detailed analysis of the role of particular attention layers and heads, specific observations related to different types of solved (chess) problems are reported.

### Strengths
1) The paper is well written and relatively easy to follow.
2) The experiments are well-designed and formally correct.
3) The considered topic is of interest to the ICLR community.

### Weaknesses
1) The novelty of the paper is limited. The underlying research concept of verifying the Leela’s capabilities of long-term strategic planning directly follows Jenner et al. (2024) paper, only with extended planning horizon (to 7 half-moves)
2) Detailed conclusions regarding the role of concrete layer/head pairs in solving particular types of chess problems (positions) are not especially meaningful, neither from practical nor theoretical point of view.
3) The topic of considering alternative lines of play is not investigated deeply enough in the main paper, even though this path seems to have research potential and may lead to insightful observations.

### Questions
1) What is the real (practical or theoretical) gain from extending the research of Janner et al. (2024) to a longer planning horizon?
2) What can the reader learn from detailed observations regarding the role of particular layer/head combinations?
3) The claim about the insignificance of the starting square is disputable. In certain types of problems, e.g. checkmate in 2 / 3 moves, often both the square which a given piece leaves and the one which the piece moves to are important, as leaving a given square has immediate consequences in terms of stopping the attack/defence of specific squares. What is the basis for the above claim?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents the use of an explainability type of approach to study the depth to which a state of the art deep neural network "analyses" Chess configurations when solving Chess puzzles (and, as a consequence of the network being unaware of this context) as well as during normal play.   The investigation shows that information is used that represents the board state up to 7 moves ahead, with multiple avenues being explored.  The idea is that a similar approach could present insights into the operations or pseudo cognitive processes of neural networks.

### Strengths
The paper extends existing work, going beyond previous results in discovered "search" depth and the fact that multiple paths are considered.  The paper also clearly illustrates that not all positions are explored in the same way, but that e.g. depth is situation dependent.  These are nice contributions made.
The paper is well written and easy to read.  The use architecture of the NN investigate is clearly explained, as is the used data.

### Weaknesses
The contributions made in the paper are nice and interesting, but limited, both in terms of direct importance (personal view as a non-chess player or chess-AI designer), but also with respect to the wider applicability of the results.  It is unclear how the presented contributions, more than at a very vague conceptual level, would be applicable in other environments.  Chess is really well defined, and the rules are clear and we know how to perform search and lookahead.  In a more complex (and with this I mostly mean less well defined and messy environment) it might be difficult to apply a similar approach.
I understand it is always easy to ask for more, but I think the impact of your work would be greatly improved if you could provide an, even conceptual, study of a less well defined environment.  I also realise this is not easy to do.

### Questions
I don't know why the puzzle set notation matters for the outcome.  It is nice information to have to completely reconstruct the work done in the analysis, but it might be information better relegated to the appendix?
I am not sure I fully comprehend the difference between activation patching and ablation.  I understand the difference in approach, but why would both techniques result in different knowledge about the inner workings of the network.

### Soundness
3

### Presentation
3

### Contribution
2
