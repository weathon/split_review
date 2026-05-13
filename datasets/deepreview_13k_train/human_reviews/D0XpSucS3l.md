# Scaling Laws for Pre-training Agents and World Models

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
The performance of embodied agents has been shown to improve by increasing model parameters, dataset size, and compute. 
This has been demonstrated in domains from robotics to video games, when generative learning objectives on offline datasets (pre-training) are used to model an agent's behavior (imitation learning) or their environment (world modeling).
This paper characterizes the role of scale in these tasks more precisely. 
Going beyond the simple intuition that `bigger is better', we show that the same types of power laws found in language modeling (e.g. between loss and optimal model size), also arise in world modeling and imitation learning.
However, the coefficients of these laws are heavily influenced by the tokenizer, task \& architecture -- this has important implications on the optimal sizing of models and data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
## Summary
This paper investigates the impact of model size, dataset size, and compute on embodied AI tasks like behavior cloning (BC) and world modeling (WM). Using transformers with tokenized inputs or CNN embeddings, the authors explore scaling behavior using 8.6 years of gameplay data from *Bleeding Edge*. They find that scaling laws—typically observed in language modeling—also apply to embodied AI tasks, with different trade-offs influenced by task, architecture, and tokenization. For instance, in the WM task with 540-token representations, optimal model size scales as $N(optimal) ∝ C^{0.62}$, whereas BC tasks see optimal model size scaling as $ N(optimal) ∝ C^{0.32} $ with the same tokenized setup.

## Quality & Clarity
The paper is written clearly, with effective visualizations such as Figures 3 and 4 showing the loss curves and power law fits for scaling laws across various model sizes. The methodology in Table 1 provides fitted coefficients across model-dataset configurations. In Section 5, several design choices, such as the comparison of architectural choices for BC-Token versus BC-CNN, are explored, and explanations are provided for why specific scaling trends arise in each architecture.

## Recommendation
The paper contributes to the understanding of scaling laws for embodied AI, particularly with evidence of model-dataset trade-offs for BC and world modeling tasks on a single dataset. However, the contributions are limited by their similarity to previous work (e.g., Tuyls et al.) and the relatively narrow focus on architectural adjustments rather than task diversity or downstream metrics. I currently recommend rejection but would be willing to change my stance if the aforementioned weaknesses are addressed.

### Strengths
## Strengths
1. **Visual Encoder Architecture Exploration:** The study explores scaling laws across various visual encoding architectures and pre-training tasks including BC and WM, showing that model scaling behavior in embodied AI resembles language modeling. For example, WM tasks with 256-token representations require scaling model and dataset sizes equally $N(optimal) ∝ C^{0.49}$ and $ D(optimal) ∝ C^{0.51} $.
2. **Tokenizer compression:** The authors find that tokenizer compression rates significantly affect scaling laws. For instance, increasing token compression from 256 to 540 tokens per image in the WM task shifts optimal model scaling to $N(optimal) ∝ C^{0·62}$, favoring larger model sizes.

### Weaknesses
## Weaknesses
1. **Lack of real-world data:** The scaling insights are based on a single simulation task. Previous studies have demonstrated that simulation performance often does not correlate well with real-world robot performance [1]. The analysis would benefit from validation on openly available real-world datasets such as OpenX[2] and DROID[3]. Specifically, the paper does not address the sim-to-real gap, which is a critical challenge in deploying embodied AI systems. The observed scaling laws in simulation may not hold when transferring to real-world environments due to factors such as sensor noise, unpredictable dynamics, and variations in object appearances. This limits the practical applicability of the findings.
2. **Downstream task performance:** The paper focuses exclusively on scaling pre-training loss without examining generalization or performance on downstream tasks, which is crucial for embodied AI applications. The paper does not explore whether lower pre-training loss translates to better performance on tasks such as manipulation, navigation, or interaction. For instance, a model with lower pre-training loss might still struggle with generalization to unseen scenarios or exhibit poor performance when deployed in a real-world setting. Including evaluations on even a select set of downstream tasks would significantly strengthen the practical relevance of the findings.

### Questions
## Questions
1. Would incorporating large-scale real-world robotics data help validate the paper's scaling law claims beyond simulation environments? The current findings, while valuable, are limited to the simulation world.
2. Could the authors demonstrate the practical value of lower pre-training losses by evaluating a subset of pre-trained models on downstream tasks? This would help establish a clear correlation between pre-training performance and downstream task effectiveness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the scaling law within an embodied agent setting, analyzing two tasks: world modeling and behavior cloning. The results indicate that a scaling law exists for both tasks when additional compute resources are provided.

### Strengths
- The paper focuses on an important problem that will have a large impact on the community.

### Weaknesses
Although it is a good attempt at analyzing the scaling law, the analysis lacks comprehensiveness. 
 - The relationship between loss and dataset size, which is mentioned in the introduction, is not presented. For example, in line 53, the authors state, “The optimal trade-off between model and dataset size in world modeling is influenced by the tokenizer’s compression rate (number of tokens per observation) (Section 4.1, Figure 1a & b).” However, Figures 1a and 1b primarily illustrate the effects of computation with different tokenizers and model sizes, without clarifying the influence of dataset size on the results.
 - The experiments utilize a frozen VQGAN visual encoder, which implies that the final claims regarding tokenizers are inherently limited by the performance of the frozen encoder.
 - The architectural analysis includes a set of BC-CNN experiments under the BC loss, but it is unclear why the CNN experiment was not conducted within the world modeling tasks.

### Questions
Please refer to the weakness section.

### Soundness
3

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
4

### Summary
This paper studies scaling laws in the context of agents (specifically in a video game) to study whether and how these laws exist in this setting. The paper looks at how dataset and model size can be optimally scaled to optimize loss for BC and world modeling (next state prediction). The authors find a power law relationship and show how things such as tokenization can effect the optimal scaling parameters.

### Strengths
The paper is well presented and generally clear.

The analyses are well explained and clear to read.

There are a lot of interesting analyses done, the authors really tried a lot of things here and have a lot of results to pick through and analyze.

### Weaknesses
The premise of what this paper is doing is kind of questionable. Specifically, the thing that is being measured is training (will get to that) loss on a BC or state prediction objective, rather than a direct measure of downstream performance. As the authors point out in their related work, most other papers such as Hu et al 2023 do measure downstream performance. The author's justification for this choice then is that this adds complexity and it might be difficulty to ask "more nuanced questions" such as how to trade-off model and dataset size. But this isn't really further justified any further. Why couldn't we do a study looking at that tradeoff on the downstream task. More importantly, this paper draws conclusions based on the training loss for a *proxy* to what researchers actually care about (how well the final agent actually does at test time), and given the choice between looking at this paper's measurements and one that evaluates this, I don't know why you would prefer this. There isn't really even much analysis about why this is a good proxy metric (like some kind of finding that things with lower loss in this paper do in fact do better on the final task, even if the curves are not as smooth)

Not only this, but the paper isn't even looking at the Test loss in these analyses, it's looking at train loss. From S3.4 "We assume training loss is an accurate proxy for test loss. (Appendix B.3.1 analyzes further)." I find this assumption both baffling and completely unjustified in the text of the paper. The cited appendix merely looks at the size of the data they trained on and says "The compute allowed by the infinite data regime is 6ND" (and so they say, they are above that. There isn't a citation for this anywhere, and I am not familiar enough with the literature to tell if this is a thing other works have done. The original scaling law paper as far as I can tell does not do this. But I still do not understand the decision. If you have this large a dataset, surely you have enough data to have a held-out set? Again, scaling laws are not something I was intimately familiar with, so if there is a good justification for this, someone please let me know. But this paper does not justify it and on it's face "assume train and test are the same" feels like an ML sin.

The results are also only validated on a single environment / datasets. This seems like it really is limiting the potential applicability of the paper. What if the conclusions or scaling parameters found in this paper are idiosyncratic to this particular game?

I say this somewhat advisedly, but I am not actually sure the models studied here are large enough to fully justify all the conclusions. Most of the experiments use 206M parameters with many having even smaller (e.g. 27M for Figure 5). The only experiment with a larger size is Figure 7 at 894M. This isn't my biggest criticism, and I know compute is quite expensive, but it feels like this is a major missing thing here.

### Questions
See above

What is this paper doing or concluding that is above prior work?

Why should I trust this proxy loss (train versus test and not final performance) over other works which directly measure the variable of interest?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Less is understood about scaling in embodied learning, but recent works suggest that increasing model and dataset size can lead to capable agents. This paper explores this hypothesis further by delving into scaling laws applicable to pre-training embodied agents and their world models, leveraging larger datasets and enhanced computational resources to improve performance. Focusing on both world modeling and behavior cloning, the study extends the understanding of how scaling affects these models beyond simple increases in parameter count, introducing dependencies on factors like tokenization and model architecture.

### Strengths
#### Strengths:
1. **Empirical Validation:**
   - The paper provides evidence that scaling laws known from LLMs similarly apply to world modeling and BC, validated across some architectures and tokenization strategies.
   - Thoroughness of many results.
   - The systematic experimentation using different model sizes and computational scales support the credibility of the findings.

2. **Take on Tokenization and Architecture:**
   -  Impact of tokenization granularity on optimal model scaling is particularly novel, offering insights into how token compression influences model efficiency and effectiveness.
   - The comparison between tokenized and CNN based approaches in BC provides nice distinctions in how these architectures manage to scale.

3. **Methodology and Analysis:**
   - The paper details the methodologies employed, from the scaling analysis approach to breakdown of the computational and parameter scaling. This thoroughness can ensure clarity and reproducibility of the results.
   - The use of frontier fit and parametric fit methods to analyze scaling laws provides a usable framework for understanding the optimal trade-offs between model size and computational expense.

### Weaknesses
#### Areas for Improvement:
1. **Hyperparameter Selection and Rationale:**
   - While the paper provides a framework for understanding scaling laws, a more granular justification of the choices behind specific hyperparameters, particularly in the synthetic data generation and scaling analyses, would enhance its contribution. Specifically, selection of number of tokens per image in the tokenization process and the learning rates used across different model scales seem crucial to the study’s outcomes but lack a detailed rationale. Providing insights into how these parameters were optimized, may be through sensitivity analyses or referencing empirical benchmarks, could help. It is unclear how the number of tokens per image was selected, and whether this choice was based on reconstruction quality or downstream task performance. Furthermore, the learning rate selection process across different model sizes is not well-defined, and it's unclear if a systematic approach was used to ensure optimal convergence for each model scale. Insights into the selection process for training configurations across different scales could further enhance the paper’s utility to practitioners.
   - Insights into the selection process for training configurations across different scales could further enhance the paper’s utility to practitioners.

2. **Broader Applicability and Generalization:**
   - The study provides insights into scaling laws within controlled experimental setups. However, to enhance the relevance and applicability of these findings to real-world applications, it would be beneficial to extend the analysis beyond the current datasets. Specifically, exploring how these scaling laws hold across datasets with higher environmental variability and some degree of realism or some evidence of extensibility. The current dataset, while useful for controlled experiments, may not fully capture the complexities of real-world embodied learning scenarios. It is unclear if the observed scaling laws would generalize to more complex environments with greater variability in dynamics, object interactions, and agent behaviors. 
   - Extending the analysis to include more diverse datasets or environmental complexities could help validate the laws observed.

3. **Limitations and Future Work:**
   - The paper acknowledges limitations in the scope of architecture and tokenization diversity. 

4. **Less emphasis on embodied AI:**
   - my main criticism concerns the paper's lack of a cohesive narrative explaining the relevance of its findings to embodied intelligence. It is currently less sound in terms of the necessity of the study, or why BC or world modelling techniques need this study particularly. is it because they are the most promising approaches.. or are they the most compelling representative candidates of model-free and model-based approaches or where are we heading with this analysis? Perhaps this can be easily fixed by revising some of the scaling law papers for sing-agent or multi-agent papers cited in the paper. Lastly, might be missing some relevant references and citations in the area, some are highlighted below and good to cite.


### Questions
This paper makes promising contributions to the understanding of scaling laws in the context of pre-training for embodied AI, with clear strengths in empirical validation and methodological rigor. Addressing the identified gaps in hyperparameter transparency and broadening the scope of environments and architectures considered could further enhance its impact. Moreover, clarifying how this research fits into the broader context of embodied AI or RL, specifically the types of tasks and applications targeted and the importance of scaling laws for these areas would make the findings more relevant and engaging. Currently, the title is a bit ambiguous or too broad to understand the scope. I am happy to increase the score post-author response.

### Soundness
3

### Presentation
2

### Contribution
2
