# Generative Modeling of Individual Behavior at Scale

- Decision: Reject
- Scores: 5, 5, 10, 6

## Abstract
Recent years have seen a growing interest in using AI to model human behavior, particularly in domains where humans learn from or collaborate with this technology. While most existing work attempts to model human behavior at an aggregate level, our goal is to model behavior at the individual level. Recent work in the domain of chess has shown that behavioral stylometry, or the task of identifying a person from their actions alone, can be achieved with high accuracy among a pool of a few thousand players. However, this approach cannot generate actions in the style of each player, and hence cannot reason about or influence player behavior in practice. We provide a new perspective on behavioral stylometry that addresses these limitations, by drawing a connection to the vast literature of transfer learning in NLP. Specifically, by casting the stylometry problem as a multi-task learning problem---where each task represents a distinct---we show that parameter-efficient fine-tuning (PEFT) methods can be adapted to model individual behavior in an explicit and generative manner, at unprecedented scale. We apply our approach at scale to two very different games: chess (47,864 players) and Rocket League (2,000 players).

Our approach leverages recent modular PEFT methods to learn a shared set of skill parameters that can be combined in different ways via style vectors. Style vectors enable two important capabilities. First, they are generative: we can generate actions in the style of a player simply by conditioning on the player's style vector. Second, they induce a latent style space that we can interpret and manipulate algorithmically. This allows us to compare different player styles, as well as synthesize new (human-like) styles, e.g. by interpolating between the style vectors of two players.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the modeling of individual behaviors. The learning problem is modeled to multi-task learning. Experiments are made on two large scale games, chess and Rocket League.

### Strengths
1. The paper proposes a novel method to model the individual behavior (player behavior) by applying PEFT (specially LoRA), learning a style vector for each player. In addition, the style vectors allow for the generation of actions by steering. These ideas are novel.

2. Experiments are carefully-designed and confirm the representativeness of the learned style vectors.

### Weaknesses
1. The abstract is confusing. I am not an expert to the concerning domain. For example, what is the purpose to model human behavior using AI? Does the research only contribute to games, or some other domains?

2. Keeping up with the last point, the proposed methods can too specific in the chosen domain. It is not clear whether the proposed method can contribute to a broad range of audience, or contributing to the AI community.

3. I have some questions about the experiment settings. What is the base model used in the experiments?

4. Can the authors explain more on the usage of strong LLMs (e.g. GPT-4o) on the concerning task. For example, if one logging the specific player behavior in the context of GPT-4o, can it perform well in simulating the player?

### Questions
Please see above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper is focusing on modeling individual human behavior in games. Unlike previous works which mainly focus on modeling human behavior at an aggregate level, the authors propose learning an individualized approach for generating actions in the style of each player. To this end, they use a behavioral cloning model based on a multi-task learning approach combined with parameter-efficient finetuning (PEFT) to learn a shared set of skills across players, as well as style vectors that induce a generative model for each player. They use this approach for style steering new players towards desired properties. The authors experiment on two games, chess and RocketLeague, and find that their approach is comparable to the performance of behavioral cloning methods. They also demonstrate they can manipulate the behaviour of players and steer them towards human-interpretable attributes such as, for example, interpolating between player characteristics and style steering from a weaker player’s style to a stronger player’s style.

### Strengths
The multi-task method for modeling players proposed in this paper presents the advantage of being scalable to many players, it is parameter-efficient and allows for human-interpretable control of player attributes

The authors conduct experiments on two games, chess and RocketLeague, and find the proposed method achieves performance comparable to behavioral cloning methods that do full finetuning of the model parameters

Style vectors encode different player skills, and can be combined, interpolated, and steered towards desirable human-interpretable attributes to change the playing style of each player; the analysis of these vectors reveals they are consistent within a single player and across different players.
 
Although the approach combines existing methods in the literature, it applies them in a novel context (player modeling and human-interpretable player steering). The synthesis of new styles experiments show that it is possible to employ basic arithmetic on style vectors to interpolate between players of different strengths and skill levels and steer player styles in desirable directions.

### Weaknesses
While the proposed method is parameter efficient and needs only few shot examples for each player, the performance is often lagging behind state-of-the-art behavioral cloning methods (Figure 2)

Unclear if results in Table 1 are statistically significant, if proposed method surpasses previous approaches and the results are reported across same set of players

The paper needs additional clarifications and details (please see comments and questions below):


Additional comments:

In the unclear in the introduction in which contexts, tasks and domains this approach is relevant. Only towards the end of the introduction it is mentioned this approach is used in game environments for modeling players. 

Line 89 - the authors claim they introduce the notion of style vectors, whereas this is already well established in the literature, particularly in NLP

Line 96 - it would be desirable to briefly summarize the insights of these analyses

Figure 1 - it is unclear which are the MHR adapters and which is the routing matrix in the figure

Lines 230-231 - missing citation for the original Maia model

Line 262 - move-matching accuracy is introduced without explaining what this metric represents and how it is computed

Lines 273- 274 - “our results can be interpreted in this way” - please detail

Line 358: I would suggest replacing “universe” with “environment” (same in Table 1)

### Questions
How many reference set of games are available for each player during few-shot learning?

Table 1 - results for McIlroy-Young et al. (2022b) and McIlroy-Young et al. (2021) are borrowed from their respective papers; how do we know these are the same set of players to make the comparison fair?

Why for the unseen few-shot players you are only comparing to McIlroy-Young et al. (2021) ?

What does Random (%) denote and why are all results in that column 0.25?

Figure 2 - as the game count increases, the performance of MHR-MAIA decreases. How do you explain that? More analysis should be provided in the paper (Section 5.1) of why this happens; Section 5.2 does include some details, however they are coming in late for the reader.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The main focus of this paper is behavioural stylometry---how can one efficiently build AI agents that are customized to individual users. 
The proposed method involves simultaneously finetuning several LoRA adapters as well as a set of mixing rates indicating how much each LoRA adapter should contribute to the prediction for any particular user. The paper uses two games as a case study to evaluate their approach: chess and a soccer-like video game. In both cases, they show their method effectively predicts user moves. The paper further explores how a system trained on some number of users can be easily extended in a few-shot setting to new users.

### Strengths
This paper was a fascinating read, and both the methodology and the experiments used to support its efficacy are quite compelling. While the method being employed (`Poly` with multi-head routing) was already introduced in prior work, this prior work focused on a handful of NLP tasks rather than behavioural modeling for style-customized agents.

After reading the paper, I was left interested in trying out the MHR finetuning approach in other problem domains I'm interested in, and I feel fairly confident in my ability to reproduce the proposed method using the details in the paper.

### Weaknesses
1. I am slightly concerned that, due to me being non-expert in this area, my perception of the proposed method's novelty is greater than it actually is. I would like to see additional explanation in the "Background and Framing" section situating the paper's contributions relative to those in the Polytropon and MHR papers.
2. The majority of the experiments are only on the chess domain. I wold have liked to see more reproduction of experiments on the Rocket League domain.
3. I would have liked to see a user study where human players are asked to assess the style of different agents.
4. I would like to see more analysis of how few-shot performance for unseen players varies as a function of the amount of data available for tuning the new player's style vector. E.g. a figure plotting move prediction accuracy as a function of number of games used for tuning.

### Questions
1. What do the bold numbers mean in Table 1?
3. I don't understand what the y-axis is in Figure 7.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a way to model individual human behavior in games with a scalable, generative approach to behavioral stylometry. Each player is treated as a unique task in a multi-task learning framework, where the authors use parameter-efficient fine-tuning (PEFT) to create style vectors capturing each player’s playstyle. These vectors can then be used to activate shared “skill” parameters, letting the model generate actions tailored to each player. They apply their method to large datasets from chess and Rocket League, and scale their method to tens of thousands of players.

### Strengths
- Their architecture and learning procedure was well motivated and explained; for instance, they tackle the transfer/interference tradeoff in multitask settings by using Polytropon.
- Rather than having to fine-tune a separate model for each person, their approach supports large-scale behavioral modeling by assigning unique style vectors to individuals, which activate specific combinations of shared parameters.
- The model doesn’t just classify or predict; it generates actions in the style of individual players, providing a more dynamic and flexible tool for studying human behavior.
- The methodology is tested in two distinct gaming environments—chess and Rocket League; and the authors applied their model to a substantial dataset, covering tens of thousands of players.

### Weaknesses
 - The paper’s primary contribution is restricted to stylistic adaptation in gaming, without broader implications for other domains. The methodology demonstrates success in chess and Rocket League but fails to show convincingly how these results would generalize to other forms of human behavior modeling.
- It would improve the paper to see more baselines. For example, the authors state "We do not compare to the Transformer-based embedding method because it is incapable of generating moves," however it can still be a good baseline to compare to.
- The authors compare to r McIlroy-Young et al., however, I am not sure if the same test set is used which could make the comparison not that strong?
- While the authors highlight extensions to image generation, the paper does not compare their method against established baselines such as CLIP-guided editing, DreamBooth, or StarGAN. Demonstrating superiority or complementarity to such methods would significantly strengthen the claims of broader applicability.
- Regarding the McIlroy-Young et al. evaluation, the authors' defense about dataset construction is reasonable. However, to ensure fairness and comparability, applying their model to the new test set is necessary. Reporting their original scores on a different test set does not provide a direct comparison and risks misinterpretation. These details about the test set with respect to McIlroy-Young et al. seem rather important, and I'm wondering why these details were not included in the original paper?

### Questions
1. How do you see this model generalizing to non-gaming applications?
2. Can you provide practical examples where style steering would be beneficial?
3. Have you considered the case when a player’s behavior changes significantly over time?

### Soundness
3

### Presentation
3

### Contribution
2
