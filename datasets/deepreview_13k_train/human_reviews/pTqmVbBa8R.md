# Generative Modeling of Individual Behavior at Scale

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Recent years have seen a growing interest in using AI to model human behavior, particularly in domains where humans learn from or collaborate with this AI. While most existing work attempts to model human behavior at an aggregate level, our goal is to model behavior at the individual level. Recent work in the domain of chess has shown that behavioral stylometry, or the task of identifying a person from their actions alone, can be achieved with high accuracy among a pool of a few thousand players. We provide a new perspective on behavioral stylomery by connecting it to the vast literature of transfer learning in NLP. Specifically, by casting the stylometry problem as a multi-task learning problem---where each task is a distinct person---we show that parameter efficient fine-tuning (PEFT) methods can be adapted to perform stylometry at an unprecedented scale (47,864 players), while enabling few-shot learning for unseen players. Our approach leverages recent modular PEFT methods to learn a set of skill parameters that can be combined in different ways using style vectors. Style vectors enable two important capabilities. First, they make our approach generative, in that we can generate actions in the style of a player by simply indexing into that player's style vector. Second, they induce a latent style space that we can interpreted and manipulated algorithmically. This allows us to compare different player styles, as well as synthesize new (human-like) styles, e.g., merging the styles of two players or interpolating between their styles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to model individual behavior in chess using a multi-task learning framework that leverages parameter-efficient fine-tuning (PEFT) methods. The paper introduces a style vector for each player that captures their distribution over latent skills learned from a shared inventory of adapters. The style vector enables generative modeling, stylometry, and style analysis and synthesis of players.
The paper evaluates the method on a large-scale dataset of over 47,000 players and 244 million games, and shows that it can perform stylometry with high accuracy, predict Elo ratings, probe player styles, and create novel human-like styles.

### Strengths
1. The paper proposes a novel and rigorous method to model individual behavior in chess using a multi-task learning framework that leverages parameter-efficient fine-tuning methods.
2. The paper introduces a style vector for each player that captures their distribution over latent skills learned from a shared inventory of adapters. The style vector enables generative modeling, stylometry, and style analysis and synthesis of players.
3. The paper evaluates the method on a large-scale dataset of over 47,000 players and 244 million games, and shows that it can perform stylometry with high accuracy, predict Elo ratings, probe player styles, and create novel human-like styles.

### Weaknesses
1. The paper focuses on modeling individual behavior in chess, which is a specific and narrow domain. The method may not generalize well to other domains or tasks that have different characteristics or constraints. For example, the highly structured nature of chess, with its discrete moves and clear rules, might not translate well to domains with continuous action spaces or more ambiguous decision-making processes. The reliance on a large dataset of chess games might also be a limitation, as similar datasets may not be available for other tasks.

2. The paper assumes that the players’ styles are stationary and independent of the context or the opponent. However, in practice, players may adapt their styles to the situation or the opponent, which could affect the accuracy and validity of the method. This assumption of stationarity might lead to an oversimplified representation of player behavior, failing to capture the dynamic nature of strategic adaptation. For example, a player might adopt a more aggressive style when facing a weaker opponent or a more defensive style when under pressure, which would not be captured by a static style vector.

### Questions
How do you see this method to generalize beyond a game setting, e.g., to role-play text generation (e.g., Character AI)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel method to model individual behavioral stylometry. Specifically, the authors take it as a multi-task learning problem where each task refers to a distinct person. The method is parameter-efficient and thus can perform stylometry at an unprecedented scale with few-shot learning enabled. Experimental results on chess data show the effectiveness of the method.

### Strengths
1. The topic is interesting and the proposed way for modeling human individual behavior looks novel to me.

2. Overall the paper is clearly written and easy to follow.

### Weaknesses
1. The method looks to some extent incremental to me: some existing techniques such as Lora and Polytropon are combined and employed for a specific task. 

2. Currently, the empirical result is only on a chess dataset. As the paper aims at modeling human behavior, it would be good if more related datasets could be considered. See question 4.

minors:

Typos: "we use this to to evaluate few-shot learning ..." and "we run a simulated tournament between the them".

### Questions
1. What is the intuition behind to model each player as a task? 

2. Is there any data imbalance / long tail problem under this setting?

3. Can we have a fig5-like result for interpolation over the style space?

4. Can the method be applied to games with asymmetric information like poker?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper scales up the individual-level behavior simulation at scale using Parameter Efficient Fine-Tuning (specifically Poly LoRA). This has significantly scaled up the simulation, with the neat addition of new capabilities such as individual-style generation and style analysis. This work demonstrates how the latest PEFT methods can significantly scale up fine-grained human behavior simulation. The authors use chess game analysis as an example, but similar simulations could be possible in other domains.

### Strengths
* By combining multiple of the latest scalability fine tuning techniques, the authors were able to successfully scale up the individual-level simulation in unprecedented ways.
* Authors provide interesting observations from the simulation proving the individual models are indeed helpful for the scaled analysis of human behavior. e.g. Figure 5

### Weaknesses
 * Besides the interesting adaptation in the fine-grained human behavior analysis, the actual technical contribution is quite limited because they are simple extensions of the previous work on the chess domain.
* Even considering limited work in the chess game simulation, the empirical comparison is pretty weak. They could have considered other baselines such as ones with standard DNNs for example from one model.
* Technical contribution to the machine learning communities seems to be limited since the work is a straightforward extension o f the Maia model with small modifications.

### Questions
Please take a look at the weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
