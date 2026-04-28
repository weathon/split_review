# Searching for High-Value Molecules Using Reinforcement Learning and Transformers

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Reinforcement learning (RL) over text representations can be effective for finding high-value policies that can search over graphs. However, RL requires careful structuring of the search space and algorithm design to be effective in this challenge. 
  Through extensive experiments, we explore how different design choices for text grammar and algorithmic choices for training can affect an RL policy's ability to generate molecules with desired properties. We arrive at a new RL-based molecular design algorithm (\methodName) and perform a thorough analysis using 25 molecule design tasks, including computationally complex protein docking simulations. From this analysis, we discover unique insights in this problem space and show that \methodName achieves state-of-the-art performance while being more straightforward than prior work by demystifying which design choices are actually helpful for text-based molecule design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the potential of reinforcement learning (RL) methods to discover new, high-value molecules and presents a new RL-based molecular design algorithm called ChemRLformer. The authors conduct extensive experiments and analysis to show that ChemRLformer achieves state-of-the-art performance while being more straightforward than prior work. The paper provides unique insights into the application of RL to molecular design and highlights the importance of careful search space structuring and algorithm design.

### Strengths
1. The paper addresses an important problem in the field of molecular design, which has significant implications for society. The potential of RL methods to discover new, high-value molecules could have a major impact on drug discovery, materials science, and other fields.

2. The paper presents a new RL-based molecular design algorithm called ChemRLformer, which achieves state-of-the-art performance while being more straightforward than prior work. The authors provide unique insights into the application of RL to molecular design and highlight the importance of careful search space structuring and algorithm design.

3. The paper is well-written and easy to understand, even for readers who may not be familiar with RL or molecular design. The authors provide clear explanations of their methods and results, and use visual aids to help illustrate their points.

4. The authors conduct extensive experiments and analysis using 25 molecule design tasks, including computationally complex protein docking simulations. They explore how different design choices for text grammar and algorithmic choices for training can affect an RL policy’s ability to generate molecules with desired properties.

### Weaknesses
1. It is confusing why the authors assume a discount rate of 1 in Section 4.1. Even with a finite trajectory, a discount rate smaller than 1 is not obligatory, it can also help. A discount rate of 1 can prevent the agent from learning and executing long-term tasks, as it won't appropriately discount long-term returns, leading it to prioritize immediate rewards and neglect long-term benefits. It is suggested to justify this setting. The authors should clarify why a discount factor of 1 is optimal for their specific molecular design problem, especially considering that a discount factor less than 1 could encourage the agent to explore more diverse molecular structures by valuing future rewards differently. The lack of a clear explanation makes it difficult to assess the appropriateness of this choice.

2. REINFORCE is a very classic yet old algorithm. It is highly recommend to try more recent algorithms, e.g., TROP or PPO. I am not an exert in RL for molecular optimization, but I doubt whether it is the state-of-the-art RL algorithm in this field. For example, (i) due to its reliance on stochastic policies and simple optimization methods, REINFORCE can be more susceptible to getting stuck in local optima, making it less effective in complex and high-dimensional environments; (ii) due to its on-policy mechanism, REINFORCE requires a large number of samples to estimate gradients accurately. This can make it computationally expensive and slow for complex tasks and environments. The authors should provide a more thorough justification for their choice of REINFORCE, especially considering the availability of more advanced algorithms. A comparison with other RL algorithms, particularly those known for better sample efficiency and stability, would strengthen the paper.

3. It would be more convincing if domain experts can help to judge the effectiveness of ChemRLformer from molecular's perspective. The current evaluation relies heavily on computational metrics, which may not fully capture the practical value of the generated molecules. Input from domain experts could provide valuable insights into the chemical feasibility and potential applications of the designed molecules. The authors should consider incorporating qualitative feedback from experts in the field to complement the quantitative results.

### Questions
Please refer to Weaknesses.

### Soundness
2 fair

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a method for molecule design using language models and RL. First, a GPT-style model is pre-trained in an autoregressive fashion. The model is then finetuned using REINFORCE algorithm to generate high-value molecules. The authors discuss several design choices and perform ablation studies to confirm their hypotheses.

### Strengths
1. The problem is of high importance
1. The paper is well-written
1. The numerical results are well documented and contain ablation studies

### Weaknesses
1. Some of the design choices seem to be dated. For example, 
    * it is not clear why REINFORCE is used as the policy learning algorithm, as opposed for instance to PPO. 
    * there is no automatic entropy tuning for exploration.
    * Reinforcement Learning with Human Feedback can be also an interesting approach to try
2. The details for the backbone language model as scarce. It would be also interesting to discuss the design choices for language modeling, e.g., pretraining architecture (BERT vs GPT),  tokenizer etc
3. It would be good to see if increasing the transformer size would lead to performance improvement. If I am not mistaken increasing the RNN size could lead to issues while training and therefore this could potentially become the strength of the paper.

### Questions
1. A most popular approach nowadays to finetuning transformers is reinforcement learning with human feedback. In RLHF, the reward preference model is trained to choose between several samples of the transformer and then the fine-tuning is performed using PPO algorithm. Have the authors considered this approach? 
1. It is not clear why the authors use Reinforce instead of more popular PPO for example. I appreciate that the authors did an ablation study on the KL constraint, but PPO has other benefits in comparison with Reinforce 
1. Details of the backbone model are not given. Is it a standard GPT model? Was the tokenizer standard or also trained? 
1. It is not clear why the authors chose GPT-style model as opposed to BERT style model, where the whole sequences can be predicted directly. This approach was used, e.g  by Cowen-Rivers et al albeit for a different problem and with a different RL algorithm. A discussion on the subject would be interesting.
1. Haarnoja et al 2018 proposed an automatic tuning procedure of entropy that can explicitly state the target level of entropy. It would be interesting to have this as ablation as well. 
1. I am confused about referencing Mnih et al 2013 regarding the use of replay buffer for on-policy algorithms. Don’t Mnih et al use an off-policy algorithm? 
1. Furthermore, I am not quite sure what a replay buffer for on-policy algorithm means. Does it mean that we use samples for several previous iterations not just the most recent one?
1. The results could be displayed better, with this scale the improvement of the model does not seem too large, but could be deceptive. 
1. In Figure 2 CheMBL offers high diversity and high redundancy results, which seems confusing at first. Please comment in the figure caption

UPD:
References :
* Cowen-Rivers, Alexander I., et al. "Structured Q-learning For Antibody Design." arXiv preprint arXiv:2209.04698 (2022).   
* Haarnoja, Tuomas, et al. "Soft actor-critic algorithms and applications." arXiv preprint arXiv:1812.05905 (2018).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors propose Transformer-based approach with Reinforcement Learning tuning for molecular generation. Approach is tested using different datasets and wide ablation study is conducted.

### Strengths
Promising approach for the molecular generation. Experiments are conducted using three different datasets and impact of each of them is shown. 

Good ablation study includes the design choices, different models architectures and even other RL algorithms beside REINFORCE are tested.

### Weaknesses
 **Relevant work**

Some relevant works seem to be missing:

* MolGPT (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10232454/) also uses Transformer for molecular generation but without RL.

* Taiga (https://pubs.acs.org/doi/10.1021/acs.jcim.1c00600) uses Transformer and REINFORCE algorithm for the molecular generation with different properties optimization.

* Please also consider citing the relevant parallel work which applies offline RL for the similar problem: https://www.biorxiv.org/content/10.1101/2023.11.29.569328v1 (once it is public)

The second work seems to be very similar in terms of approach and I'm not sure about the novelty of the approach itself.

** Results presentation **

* I haven't noticed the comparison against any other methods.

* From the plots I couldn't understand what "Div." and "Red." columns stand for.

* I couldn't find reported scores for different tasks (e.g., similarity, QED or SA). It would be nice to see them.

* There are no samples of generated molecules. RL could hack reward functions and generate molecules which make no sense. Reward hacking is mentioned by the authors but including resulting molecules is essential.

### Questions
Please include relevant work which is mentioned in the **Weaknesses**

* What are the principal differences between you approach and Taiga?

* Can you compare against MolGPT, Taiga and REINVENT (or similar approach)? 

* What are "Div." and "Red." columns?

* What are the scores for different reward components (e.g. QED)? 

* Can you please provide examples of generated molecules? The picture of molecular graphs and real drugs for given targets is fine.

* How did you make run docking process so fast? From my experience even GPU-accelerated programs for docking are quite slow. Is acceleration achieved because the docking is performed to the fixed target protein?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a study of different design choices (problem representation, neural architecture, pretraining, etc) in the space of string-based RL for molecular discovery. The paper presents extensive experiments, including more than 25 molecule design tasks, to compare different design choices. The best combination of design choices is then used to propose a new RL-based molecular design algorithm (ChemRLformer). The paper also provides a thorough discussion of the results and provides valuable insights and recommendations for practitioners in the field of molecular discovery.

The paper is well written and organized. It is easy to follow and understand. The paper is also well motivated and provides a good introduction to the field of string-based RL for molecular discovery. I recommend the paper for acceptance.

### Strengths
- Technical Soundness: The paper demonstrates a high level of technical rigor. It conducts extensive experiments that compare various design choices (such as problem representation, neural architecture, pretraining, etc.) within the realm of string-based reinforcement learning for molecular discovery. Moreover, the paper offers a comprehensive discussion of the results and imparts valuable insights and recommendations for future research.

- Clarity and Organization: The paper is well-written and organized, making it easy to understand and follow. It effectively motivates the reader and provides a solid introduction to the field of string-based reinforcement learning for molecular discovery.

- Significance: The paper makes a substantial contribution to the field of molecular discovery. It offers a comprehensive comparative study of diverse design options (problem representation, neural architecture, pretraining, etc.) within the domain of string-based reinforcement learning for molecular discovery.

- Table 1 provides a nice summary of the different algorithms for text-based molecule design.

### Weaknesses
 - Originality: While the paper offers a thorough numerical comparison of different design choices (problem representation, neural architecture, pretraining, etc.) in the context of string-based reinforcement learning for molecular discovery, its originality is somewhat constrained.


### Questions
- (Introduction) "...our own algorithm (MoLRL)" - what is MoLRL?
- (Table 1) What is the difference between "MoLRL" and "ChemRLformer (Ours)"? Is MolRL the general framework and ChemRLformer the best combination of design choices based on the ablation study? Please clarify.
- (Section 4) "The molecular design space is complex but the benefit from finding improved options is great." This sentence reads a bit too colloquially. Please rephrase.
- (Section 4) "However, the corresponding transition function induced in the graph representation of molecules is more complex as it is determined by the encoding/decoding rules of the chosen text representation." Are these constraints hard-coded in situ on the transitions dynamics or are they learned? Please clarify.
- (Figure 2) "(a) Performance on SMILES-based molecular design with pertaining (left) and with pretrianing and RL (right)." Please correct the typos "pertaining" and "pretrianing".
- (Figure 2) "b) performance on SMILES-based molecular docking with pertaining (right) and with pretrainig and RL (right)." First (right) should be (left). Please correct.
- (Figure 2) How does the "pretraining only" results (left column) are computed? Is this a zero-shot evaluation? I can't find the answer in the text. Please clarify.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
