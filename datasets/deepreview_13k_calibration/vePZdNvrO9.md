# GameInstruct: Teaching Machines to Reason via Chameleon Game

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Self-play has emerged as a promising approach for generating alignment data to reduce the data annotation costs during the alignment process.
By introducing specific game rules and utilizes the model’s own language capabilities to generate data samples, self-play has achieved promising results.
However, traditional self-play methods face two major challenges: insufficient data diversity during self-iterative training and difficulties in reward signal design.
To solve these problems, this paper introduces GameInstruct, a complex multi-player adversarial environment that increases the complexity of self-play generated data during self-iterative training.
Specifically, we employ the ``Chameleon Game'', where interactions between multiple players raise the diversity of the generated data, improving the model’s reasoning abilities, 
Additionally, we further propose a dynamic reward algorithm to capture signals within player conversations during the whole game.
Experimental results show that compared to existing self-play methods, GameInstruct achieves significant improvements on the HuggingFace Open-LLM-Leaderboard reasoning benchmark while demonstrating continuous improvement and increasing data diversity during self-iterative training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces GAMEINSTURCT, a novel approach within the domain of self-play for generating alignment data, which is crucial in reducing annotation costs during the alignment process. By leveraging a complex multi-player adversarial environment termed the "Chameleon Game," GAMEINSTURCT enhances the diversity of data generated during self-iterative training. This is achieved through multi-player interactions, which elevate the complexity and diversity of scenarios that a model encounters, thereby improving the model's reasoning abilities. Furthermore, the paper proposes a dynamic reward algorithm designed to capture nuanced signals within player conversations throughout the game, which aids in continuous performance optimization.

### Strengths
(1) The paper is articulate and well-organized, with clear definitions of key concepts and a logical flow of ideas. The use of the Chameleon Game as a case study helps in concretely demonstrating the application of GAMEINSTURCT, making the complex concepts more accessible to the reader.

(2) GAMEINSTURCT introduces a unique combination of a multi-player adversarial environment with a dynamic reward system tailored to self-play scenarios.

### Weaknesses
 - The idea that self-play adversarial games can be used for generating alignment data has been proven in some previous work, and the proposed method looks like replacing the old games with the Chameleon Game. While I recognize the contribution, strength and sate-of-the-art performance of this method, it would be more inspiring if the authors could provide more analysis or ablation experiments on why Chameleon Game is better than previously proposed games on generating synthetic data.
- The design of the dynamic reward looks generalizable to other adversarial games. However, effectiveness of it is mainly experimentally verified for Chameleon Game, but not for other adversarial games.

### Questions
(1) Can the authors clarify whether GAMEINSTURCT is intended as a game environment or a training method/framework? If it is an environment, are there plans to open-source the code?

(2) Broader Comparisons: Given the many existing techniques in self-play reinforcement learning, why were only SPIN and SPAG chosen for comparison? Could the authors consider broadening the scope of comparison to include more methods?

(3) Since dynamic reward is a well-understood concept in RL, can the authors discuss how their implementation of dynamic reward in GAMEINSTURCT provides a distinct advantage over existing methods?

(4) Are there plans to test GAMEINSTURCT in other environments beyond the Chameleon Game? This could help in understanding the robustness and generalizability of the proposed method.

(5) Could the authors provide more details on the RL training specifics, the size and source of the imitation datasets, the evolution of dynamic rewards during training, and the specifics of reward shaping? This information is crucial for evaluating the robustness and reproducibility of the results.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces GAMEINSTRUCT, a novel training approach that enhances language models' reasoning capabilities through multi-player adversarial interactions using the "Chameleon Game" framework. The key innovation lies in addressing two major challenges in traditional self-play methods: insufficient data diversity and difficulties in reward signal design. In the Chameleon Game, multiple AI players interact where "civilians" share a common word while a "chameleon" must avoid detection while having a different word, creating complex dynamics that increase training data diversity and prevent model collapse. The authors also propose a dynamic reward algorithm that captures signals from player conversations throughout the game, moving beyond simple win/loss outcomes. Experimental results on the HuggingFace Open-LLM-Leaderboard demonstrate that GAMEINSTRUCT achieves notable improvements over existing self-play methods, particularly in reasoning tasks, while maintaining continuous improvement and data diversity during self-iterative training. The paper claims improvements of 1-2% across various reasoning benchmarks compared to state-of-the-art self-play methods, with the approach showing particular robustness against model collapse during extended training.

### Strengths
1. Leveraging the game playing to improve the reasoning capabilities is interesting. 

2. The main contributions of this paper are i) the chameleon game, ii) the dynamic reward modeling, and iii) the RL training framework. Combining the three modules, the authors demonstrate that the reasoning capability of LLM can be improved.

### Weaknesses
1. The motivation of why solving games can improve reasoning capabilities is not very clear to me. There is no theoretical analysis about this. 

2. This paper only considers a specific game. There are many games, that can also be potentially applied, by taking more games and more data into the training seems not much complexity will be introduced into the framework. 

3. The improvement seems marginal.

### Questions
My questions are as follows:

1. Could the author provide theoretical justifications about why game playing can improve the reasoning capabilities of LLM? You employ the GPT-4 to generate the imitation learning, this may also improve the reasoning capability of LLMs? If yes, no game-playing is needed, just imitation learning. Even further, we can ask gpt-4 to solve complex decision-making tasks, and then generate the training data? therefore, still no game-playing is needed. How to justify this? 

2. The improvement of this method seems marginal. How to justify that additional training with your methods is necessary, given that the improvement is small? Besides, compared with other SFT methods over high-quality training data, your method is much more complex. Therefore, how to justify the necessities of your method?

3. I also have one conceptual question. If game playing can really improve the reasoning capability of LLMs, does that mean the Nash Equilibrium strategy will be the most effective strategy to generate the training data? how about any other equilibrium concepts?

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
3

### Summary
This paper proposes a self-play method called GAMEINSTRUCT, which leverages a multi-player game environment—specifically, the Chameleon Game—to improve language model reasoning by generating diverse, dynamic training data.  GAMEINSTRUCT incorporates multi-agent interactions with a dynamic reward mechanism. This mechanism assigns rewards based on individual player interactions rather than just game outcomes, enhancing the model's ability to develop reasoning skills.

GAMEINSTRUCT also utilizes imitation learning with data from advanced models like GPT-4 to enforce adherence to game rules, contributing to the model’s training effectiveness. Experimental results show that this approach significantly improves reasoning performance across benchmarks, maintaining stability and minimizing data redundancy over successive training iterations.

### Strengths
The strengths of GAMEINSTRUCT lie in its ability to enhance data diversity and model reasoning capabilities through a unique multi-player game-based self-play approach. It generates a broader range of interactions, reducing repetitive data and lowering the risk of model collapse. The incorporation of a dynamic reward mechanism, which evaluates player interactions rather than only final game outcomes, enables more refined training signals that boost the model’s reasoning skills. Additionally, experimental results demonstrate GAMEINSTRUCT’s effectiveness, with notable improvements in reasoning benchmarks and sustained stability across training iterations.

### Weaknesses
GAMEINSTRUCT might introduce higher computational demands due to multi-player interactions and a changing reward system, which may make it harder to scale for larger or limited-resource models. Additionally, it relies on imitation learning using data from advanced models like GPT-4, making it difficult to replicate without similar resources. The changing reward system, though helpful, adds complexity in setting accurate rewards, needing careful tuning for the best results. Finally, while effective for reasoning-based tests, it’s unclear if GAMEINSTRUCT performs well in other areas or tasks beyond language model reasoning.

### Questions
1, As mentioned in the weaknesses, how well does this approach scale when adding more agents? Can it handle the increase efficiently?

2, In section 3.3 on imitation learning, are you fine-tuning other LLMs using GPT-4 generated data? If so, why not use GPT-4 directly as an agent to play the game?

3, This method was only tested on the Chameleon game. Could you try applying it to other tasks as well?

### Soundness
3

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
2

### Summary
This paper introduces a self-play method for generating synthetic alignment data called GAMEINSTRUCT.

This method employs the Chameleon Game to enhance LLM interactions and iteratively improve the capabilities of LLMs. A dynamic reward is designed for this scenario. 

Extensive experiments are conducted to prove the effectiveness and potential of the proposed self-play method, including the potential of continuous improvement across training iterations, and robustness with respect to sampling temperature and model collapse.

### Strengths
- The proposed self-play method utilizing Chameleon Game shows its effectiveness by showing state-of-the-art performance on multiple benchmarks. 
- The proposed method shows potential of continuous improvement across training iterations. Moreover, ablation experiments on self-BLEU score prove its robustness against model collapse compared to other self-play methods.
- The proposed Dynamic Reward Assigning method is proven to improve the performance of the authors' method on several benchmarks, and may generalize to other adversarial games.

### Weaknesses
- The idea that self-play adversarial games can be used for generating alignment data has been proven in some previous work, and the proposed method looks like replacing the old games with the Chameleon Game. While I recognize the contribution, strength and sate-of-the-art performance of this method, it would be more inspiring if the authors could provide more analysis or ablation experiments on why Chameleon Game is better than previously proposed games on generating synthetic data.
- The design of the dynamic reward looks generalizable to other adversarial games. However, effectiveness of it is mainly experimentally verified for Chameleon Game, but not for other adversarial games.

### Questions
The authors mentioned sophisticated language game designs with a wide variety of task scenarios for possible future work. Why Chameleon Game is better compared with previously proposed adversarial games like taboo in SPAG? What component of Chameleon Game makes it different?

### Soundness
3

### Presentation
3

### Contribution
3
