# Data-Centric Human Preference Optimization with Rationales

- Decision: Reject
- Scores: 8, 5, 5, 3

## Abstract
\label{abstract}
Reinforcement learning from human feedback plays a crucial role in aligning language models towards human preferences, traditionally represented through comparisons between pairs or sets of responses within a given context. While many studies have enhanced algorithmic techniques to optimize learning from such data, this work shifts focus to improving preference learning through a data-centric approach. Specifically, we propose enriching existing preference datasets with machine-generated rationales that explain the reasons behind choices. We develop a simple and principled framework to augment current preference learning methods with \emph{rationale} information. Our comprehensive analysis highlights how rationales enhance learning efficiency. Extensive experiments reveal that rationale-enriched preference learning offers multiple advantages: it improves data efficiency, accelerates convergence to higher-performing models, and reduces verbosity bias and hallucination. Furthermore, this framework is versatile enough to integrate with various preference optimization algorithms. Overall, our findings highlight the potential of re-imagining data design for preference learning, demonstrating that even freely available machine-generated rationales can significantly boost performance across multiple dimensions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a data-centric approach to RLHF by enriching preference datasets with machine-generated rationales. These rationales offer explanations for choices between preferred and non-preferred responses, addressing ambiguity and enhancing the effectiveness of preference learning. The proposed framework integrates rationales into the training process, can save annotation costs by 3x, and lands the fine-tuned model at better performance. Extensive experiments demonstrate that rationale-enriched learning outperforms traditional methods, with benefits across various preference optimization algorithms. 

This work underscores the potential of rationale-based data augmentation in preference learning, paving ways for more effective language model alignment and encouraging further exploration of unpaired preference learning scenarios.

### Strengths
1. This paper is well written. The notations are clear.

2. It provides up-to-date literature on RLHF techniques. It underscores the potential of rationale-based data augmentation in preference learning, paving ways for more effective language model alignment and encouraging further exploration of unpaired preference learning scenarios.

3. Among many lines of work addressing the economic utility of dataset design and construction in RLHF, mechanism design has been recently explored to enhance the overall economic utility of dataset construction in RLHF.
The merits of introducing mechanism design are well supported by game theory studies, both theoretically and practically:

Zhang, G., & Duan, J. (2024). VickreyFeedback: Cost-efficient Data Construction for Reinforcement Learning from Human Feedback. 
https://arxiv.org/abs/2409.18417

Matsushima, H., Noda, S.: Mechanism design with general ex-ante investments. Journal of Mathematical Economics 106, 102831 (2023)

4. The experiments on Orca and UltraFeedback are convincing, with rational theoretical analysis using mutual information as a tool and in-depth ablation discussion in the appendix B.2.

### Weaknesses
This paper underlines the impact of including rationale in the RLHF fine-tuning process. In other words, the proposed method generally leverages auxiliary data to enhance the model performance. 

However, generating qualitative rationales alongside existing datasets might increase the annotation cost in dollar terms. Therefore, the breakeven analysis and the operating guidance could have been more straightforward to project owners with a limited annotation budget in dollar terms.

### Questions
It would be great if the total cost (rationale annotation cost vs. fine-tuning performance) breakeven could be revealed in dollar terms, and the operating guidance could be discussed for project owners with a limited annotation budget.

One way could be to provide a detailed cost-benefit analysis, including estimated costs for generating rationales (e.g., API costs if using a language model) versus the potential savings from reduced annotation needs. This would give project owners more concrete information to assess the method's practicality within their budget constraints.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates if incorporating rationales along with binary preference data can help improve alignment preference. To this end the authors propose rationale-DPO, an extension to the popular alignment method DPO. They compare the two algorithms with on different datasets (orca, ultrafeedback) and for different models (Mistral-7B-v0.1, Zephyr-7B-Beta etc.). The authors also propose a simplified information theoretic analysis to better understand rationale based preference modeling.

### Strengths
This study is well motivated and adds to the literature of incorporating richer feedback (additional of rationales in this case) to do more efficient RLHF alignment.

### Weaknesses
Weakness:
1. While the problem is well motivated, the methodology to maximize the likelihood of generating the given preference and the rational is a very intuitive and simple method and is not significantly novel.
2. Difficulty collecting data: procuring rationales can be more expensive as compared to getting just binary feedback. In addition, for certain cases like when you are comparing artwork it might not be possible to humans to explain their choice. While using LLMs to generate rationales is an efficient way of scaling the method, there is a risk of getting a misaligned response if that model is misaligned (for ex. not harmless) and it may also lead to an echo chamber as no new perspective beyond what the rationale generating LLM believes is true will be in the dataset. How do you envision addressing these challenges?
3. In Figure 2, it seems that DPO win rate is only lagging behind RDPO by ~5-8% for the same amount of data points, however, RDPO requires a lot more text for a single data point.

### Questions
1. Instead of plotting data points w.r.t performance metrics, it will be worthwhile to plot the total number of text tokens used for training w.r.t the performance metrics. For example, if the rationale itself is quite longer than the original texts for comparison it can contain a lot more information which might explain the improvement in performance. Additionally, it is also worthwhile to report the average training time for the both procedures.

2. For the vs DPO and vs SFT section, can you please provide the exact formula you used to compute the win rates? Are there any tie-breaking rules?

### Soundness
2

### Presentation
2

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
The paper introduces a new method for incorporating machine-generated rationales into preference fine-tuning, enhancing language models’ performance without extra human annotation. The authors demonstrate that maximizing rationale likelihood alongside preference loss improves model efficacy.

### Strengths
1. The paper proposes a new approach to integrate model-generated rationales in preference tuning, avoiding the need for additional human labels.
2. Experimental results show that optimizing rationale likelihood alongside preference loss boosts model performance, reducing annotation needs and training data volume.

### Weaknesses
1. The proposed method can be seen as a combination of the preference loss such as DPO and the rationale log-likelihood. The paper lacks further exploration of how the two components contribute to improved performance. A few questions are:
    - a. In the ablation study on $\gamma$, it seems the scale of gamma (from 1.0 to 10.0) does not matter at all. Did the authors try smaller $\gamma$ or extremely large $\gamma$?
    - b. How does tuning solely on rationale likelihood without DPO loss affect performance? Will the performance increase? 
    - c. Justification is needed for a variable $\gamma$ given the theoretical suggestion of $\gamma=1$.

2. Experimentation lacks rigor and thoroughness:
    - a. Reporting win-rate against DPO alone does not fully capture the rationale’s benefit. It is hard to evaluate the absolute improvement brought by the rationale loss. It would be better to report win-rate against a fixed opponent such as GPT-4 on AlpacaEval 2.0. This can ensure that the baseline DPO model is properly trained to a satisfactory performance.
    - b. Another related question is that there is no evidence that the DPO model in this paper is fully optimized. One may question if the dataset is weak or if the hyperparameters are adequately explored. For example, Llama3-8b-instruct + Ultrafeedback annotated by PairRM (see SimPO’s GitHub page for their dataset and model performance) can achieve a 40% LC win-rate, and the LC win-rate reported in the appendix is below 25%. I understand that SimPO did not release their training configuration, but the point here is that one cannot effectively conclude that the rationale loss significantly improves the performance.
    - c. The length bias is a key issue in preference fine-tuning. In the main text, it is reported that RDPO can produce much shorter responses and maintain a higher win-rate against DPO. This is quite surprising and deserves more analysis or explanation from the authors. On the other hand, in section B.4, the length on the AlpacaEval 2.0 dataset remains close to DPO or the original model.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a new direct preference optimization method that leverages preference rationales (natural language explaining the reasons why one response is better than another). The proposed method adds a supervised loss term to the DPO objective, jointly training/anchoring the model to generate a valid preference rationale. Each preference rationales are generated with an LLM-as-Judge, augmenting a conventional binary preference dataset.

The method can be seen as a form of hybrid distillation from both preference data (DPO) and from LLM-as-Judge rationales.

### Strengths
- The area of generative reward modeling is important and gaining traction.
- Promising experimental results across two datasets, performing comparable or better than DPO.

### Weaknesses
1. Limited novelty and poor positioning with respect to the growing literature on synthetic preference generation and generative reward modeling (see missing references below, to be discussed in the paper). In addition, the authors focus entirely on direct preference optimization as an alignment method, but reward modeling + reinforcement learning remain a major paradigm for LM alignment. How does this work translate to this setting and compare to the following baselines?

References
RLCD: Reinforcement Learning from Contrastive Distillation for Language Model Alignment. Yang et al., 2024.
West-of-N: Synthetic Preference Generation for Improved Reward Modeling. Pace et al., 2024.
Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. Zheng et al., 2024.
Self-Taught Evaluators. Wang et al., 2024.

2. I found the theoretical analysis and motivation for the method unclear.
  - Equation 2 (L230) -> why is the joint probability decomposed in this way? Why doesn’t the preference label also depend on the rationale? Surely there isn’t a single ground-truth preference considering what is discussed in the intro (multiple valid preference labels based on different raters’ values)? In fact, does Section 5 not use the opposite formulation (“the preference inferred from the rationale”)?
  - Information-theoretic results may be interesting but are completely relegated to the appendix, so they cannot be counted as a contribution of the paper. Authors state “Our analysis demonstrates a closed-form relationship between rationale informativeness and its alignment with true preferences”, without including any explanation for this claim. What does this mean and what is the form of this relationship?

3. Finally, the experimental setup is too weak to demonstrate the added value of the proposed method.
  - Is performance improvement statistically significant? Fig 2 suggests that DPO > RDPO with 1K Ultrafeedback data, but we obtain the opposite result in Fig 3. If the result is due to statistical uncertainty, this should be measured and shown on plots (RDPO outperforms DPO by a similar margin in Fig 2, which could therefore not be statistically significant).
  - Preference dataset sizes are typically >>11K (see top-perfoming RMs on RewardBench, for example). Why did the authors focus their analysis on such a small, non-representative dataset size. Also, why is there no improvement in performance with DPO beyond 1K preferences?
  - Related: L353, why pick the DPO model trained with 12K Ultrafeedback preferences as baseline, if its SFT performance is lower than that or models trained on less data?
  - Why not evaluated model performance on established benchmarks such as RewardBench/AlpacaEval?
  - How does RDPO with poor quality rationales (e.g. permuted / opposite) perform against standard DPO? I imagine much worse, since we are training on biased information. How can practitioners ensure that their rationales’ quality is sufficiently high to afford gains and not harm performance?
  - Why is RDPO performing similarly to DPO then trained on Llama-3-8B in Figure 5?

### Questions
See weakness points above.

Some additional questions I had when reading the paper, that I believe should be clarified:
- How are draws measured in Fig 2?
- I don’t understand this sentence: “the drawing rate for the RDPO model is stable and low across different training data sizes, which shows that RDPO winning rate is higher not due to flipping the draw points but the losing points.” Can authors clarify?
- Fig2 caption typo: Winrare

### Soundness
2

### Presentation
2

### Contribution
2
