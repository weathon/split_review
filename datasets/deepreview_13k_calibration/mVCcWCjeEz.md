# ToEdit: How to Synthesize Text Data to Avoid Model Collapse?

- Decision: Reject
- Avg Score: 6.25
- Scores: 3, 8, 8, 6

## Abstract
We explore model collapse caused by synthetic data, where AI models trained on such data experience a gradual decline in performance. 
Our initial analysis examines language model pretraining on mixed human and synthetic data, highlighting performance degradation. Further statistical analysis reveals distributional shifts and an over-concentration of n-gram features caused by synthetic data. Inspired by these insights, we propose token-level editing on human data, to obtain semi-synthetic data instead of fully using model outputs. As a proof of concept, we theoretically demonstrate that token-level editing can prevent model collapse, as the test error is constrained by a finite upper bound. We conducted extensive experiments on pretraining, continual pretraining, and supervised fine-tuning of language models. The results validate our theoretical proof that token-level editing improves data quality and enhances model performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the role of synthetic data for LM pretraining.

1. The main observation/finding is:

> The mixture of synthetic data and real data is worse than real data only, which is evaluated with perplexity. (trained with Dolma + x% of Cosmopedia, and eval with wikitext-103, Redpajama, RefineWeb, C4-en)

2. A new data synthesis method, TOEDIT, which resamples tokens with lower perplexity using a language model. The authors claim TOEDIT outperforms real data in continual pretraining and SFT scenarios.

### Strengths
The analysis of Cosmopedia synthetic data is comprehensive and provides valuable insights for future research

The theoretical framework is interesting and well-developed

The paper addresses an important question in the field about the utility of synthetic data in pretraining

### Weaknesses
## Review

### summary:
 This paper investigates the role of synthetic data for LM pretraining.

1. The main observation/finding is:

> The mixture of synthetic data and real data is worse than real data only, which is evaluated with perplexity. (trained with Dolma + x% of Cosmopedia, and eval with wikitext-103, Redpajama, RefineWeb, C4-en)

2. A new data synthesis method, TOEDIT, which resamples tokens with lower perplexity using a language model. The authors claim TOEDIT outperforms real data in continual pretraining and SFT scenarios.

### soundness:
 2

### presentation:
 3

### contribution:
 1

### strengths:
 The analysis of Cosmopedia synthetic data is comprehensive and provides valuable insights for future research

The theoretical framework is interesting and well-developed

The paper addresses an important question in the field about the utility of synthetic data in pretraining

### weaknesses:
 **Major Concerns**

1. Significant Literature Gap and Contradictory Findings 
- The paper overlooks a crucial published work [1] that directly contradicts its main findings
- [1] demonstrates that mixing synthetic and real data improves perplexity across various domains in the Pile and enhances downstream task performance
- This fundamental contradiction needs to be addressed and explained

Figure2 in [1] shows that by mixing the synthetic data with the real C4 data, LM can get lower perplexity on various domain corpus of the Pile. [1] also shows the introduce of synthetic data gave better results on downstream tasks. However, this submission claims the mixture of data is worse than real data only, by evaluating the perplexity. (I suspect the evaluation is incorrect which lead to this contrast observation. My 2nd concern below will detail more)

2. Flawed Experimental Design for Main Claims 

The pretraining real data is Dolma, which consist of wikipedia, C4. Hence, the more real data you use, the lower perplexity on Wikitext-103 and C4-en you should expect. So it is domain mismatching problem, instead of saying synthetic data is not useful. 
On the other hand, the synthetic pretraining data Cosmpopedia was build from LLM's rephrase of web-crawled data, which means Cosmopedia's data distribution differs significantly from web-crawled data, making the comparison with RedPajama and RefineWeb potentially unfair.  I would suggest to use proper out of domain text for perplexity evaluation, and also introduce the downstream task evaluation.  I would suggest to follow the evaluation framework from [1] for better comparison

3. TOEDIT Methodology Concerns
- The non-autoregressive token replacement approach may compromise text coherence and grammatical correctness
- No discussion of how grammatical consistency is maintained during token resampling

4. Weak Empirical Results (Baseline performance is concerningly low)
- MMLU: baseline (26.56) vs. proposed (23.63) vs. random (25)
- WinoGrande and Hellaswag results near random guessing. Improvements are marginal (1.3, -0.08) and not statistically significant


**Minor Concern**

1.  The conclusion drawn from "75% words under 0.6 probability" (Lines 265-267) ignores fundamental linguistic entropy
- English typically has 10-11 bits per word entropy
- The observed probability distribution may be natural rather than indicating filtering potential


[1][Rephrasing the Web: A Recipe for Compute and Data-Efficient Language Modeling](https://aclanthology.org/2024.acl-long.757) (Maini et al., ACL 2024)

### questions:
 N/A

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 4

### code_of_conduct:
 Yes

### role:
 Review

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the problem of model collapse in language models trained on synthetic data. The authors propose Token-Level Editing (ToEdit), a method that creates semi-synthetic data by selectively editing tokens based on their probability estimates from a pre-trained model. Key contributions include:

1. Demonstration of non-iterative model collapse when mixing synthetic and human data during pre-training
2. Statistical analysis showing synthetic data suffers from distribution coverage collapse and feature over-concentration
3. A token-level editing approach that theoretically prevents model collapse while improving data quality
4. Experimental validation across pre-training, continual pre-training, and supervised fine-tuning scenarios

### Strengths
- Well-structured paper with clear progression
- The authors identify a critical issue in modern LLM training (model collapse with synthetic data)
- Provides thorough statistical analysis of synthetic data's limitations
- Demonstrates non-iterative model collapse, extending beyond previous work focusing on iterative collapse
- Proposed Method is computationally efficient (single forward pass)
- Tests across multiple training scenarios (pre-training, continual pre-training, fine-tuning)
- Uses various downstream tasks for validation

### Weaknesses
1. Parameter Sensitivity: The paper mentions using a probability threshold p=0.99 for token resampling but doesn't explore how sensitive the results are to this parameter choice. There's no ablation study showing how different threshold values affect performance. The paper doesn't explore or justify why this specific threshold works best. No ablation studies are provided to show the impact of different threshold values

2. Token Resampling Strategy (Limited Justification):
- The choice of top-k sampling with k=8 seems arbitrary
- The paper mentions they tried other sampling strategies (top-p and rejection sampling) but doesn't provide comparative results

3. Progressive Decrease in Editing 
- The assumption that editing operations decrease with a fixed ratio η seems mathematically convenient but lacks empirical validation
- No real-world evidence is provided to support this pattern of decay

4. Distribution Analysis:
- The U-shaped distribution in Figure 6 needs better explanation of why it's a good indicator for token editing
- The "coverage collapse" phenomenon mentioned multiple times could be better defined and explained
- The relationship between "feature over-concentration" and model performance isn't clearly explained

4. Experimental Setup:
- Figure 5 shows results about "DSIR-Selected Data" but details about this selection process aren't well explained
- Details about the continual pre-training setup across different domains (Biomedicine, Finance, Math) are sparse

5. Results Interpretation:
- The improvements shown in Tables 1-3 could use more discussion about statistical significance
- 
- Compare different sampling strategies (top-k, top-p, nucleus sampling) with ablation studies

### Questions
1. Can you please provide justification for choosing p =0.99 and k =8 
2. Can you please provide more evidences for Progressive Decrease in Editing 
3. Can you elaborate the relationship between perplexity improvements and actual model capabilities.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper explores the impact of synthetic data on language model training, particularly the phenomenon of model collapse. Model collapse occurs when models, trained extensively on synthetic data, experience performance degradation due to distributional shifts,  lack of full distributional range of human language, and over-concentrates certain linguistic features, leading to "coverage collapse." The authors propose a novel solution called Token-Level Editing  to counteract model collapse by editing human data at the token level, creating "semi-synthetic" data that retains critical human data distribution characteristics. They demonstrate, both theoretically and experimentally, that this method helps prevent model collapse by bounding test error within a finite range. Through extensive pretraining, continual pretraining, and supervised fine-tuning experiments, the results indicate that token-level editing improves the quality of synthetic data and enhances model performance across tasks.

### Strengths
1. The paper is well written and consistently maintains the readers interest by presenting core findings around synthetic data issues and the proposed token editing approach initially and later go on to support those claims.

2. The paper presents a novel strategy for avoiding model collapse, a critical issue as human data becomes scarce and reliance on synthetic data grows. The proposed Token-Level Editing (ToEdit) approach offers a novel way to mitigate collapse by creating semi-synthetic data, modifying only certain tokens in human data instead of relying entirely on synthetic data. This targeted editing approach preserves key distributional characteristics, reducing the risk of collapse while leveraging the benefits of synthetic data.

3. The authors support their method with a robust theoretical framework, calculating bounded test error as evidence that model performance degradation can be prevented.

4. Empirical results are provided with experiments involving pretraining, continual pretraining, and fine-tuning stages, showing that token-level editing yields consistent performance improvements across diverse learning approaches and domains, such as biomedicine, finance, and mathematics.

### Weaknesses
1. Token-Level Editing relies heavily on a pre-trained language model to estimate token probabilities, which may introduce biases based on the pre-existing model's characteristics. The paper does not explore the potential impact of these biases, such as the model favoring certain linguistic styles or token sequences that were prevalent in its pre-training data. This could limit the diversity of the edited data and potentially hinder the method's ability to generalize across different domains. It would be beneficial to see if an ensemble of models with varied pretraining sources could be used to reduce single-model bias in the token-level editing process. This could enhance the diversity of the generated semi-synthetic data.

2. Although the study focuses on text, with recent LLMs heavily focused on solving tasks such as code generation,  I wonder if ToEdit would work on other data types (e.g., code, tabular data)? Changing tokens in code sequences might make the code prone to errors. It will be interesting to see experiments on the generalizability of ToEdit across different data domains and will help the community understand its broader applicability. The paper does not discuss the challenges of applying token-level editing to structured data, where the meaning of a token is often context-dependent and changes might break the underlying structure or semantics of the data.

3. The experiments are limited to GPT-2 and OLMo models, which may not reflect the broader applicability of Token-Level Editing across diverse architectures. Testing on models like BERT (with bidirectional attention), T5 (with encoder-decoder architecture), and maybe more recent LLMs with sparse attention or mixture-of-experts layers could reveal whether ToEdit’s effectiveness is architecture-agnostic or if it needs adaptation for specific configurations. The paper lacks a discussion on how the method might interact with different attention mechanisms or model architectures, which could lead to varying performance across different model types.

### Questions
Questions & Suggestions:
1. It would help if the paper provided further clarification on the specific threshold values used for token-level editing (e.g., the probability threshold $p=0.99$. Explaining why this threshold was chosen and whether it varies by dataset or model could add depth to the methodology section.

2. Although common, it might still be useful to expand that PPL stands for perplexity. It will be helpful for new researchers.

3. The paper uses terms like "non-iterative model collapse" and "coverage collapse." It would be helpful broader audience to better understand these terms if it was clearly defined.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the problem of model collapse when training with synthetic data, and provides theoretical and empirical evaluations for training under different mixtures of human and synthetic data. They introduce token-level editing, which is a straightforward technique to introduce noise to human-written data by resampling a token every time a prior LLM probability assigned to the next token is larger than p=0.99. Authors show that using token-level editing in pretraining/continual pretraining/supervised finetuning they can achieve comparable performance to using standard human-authored data across a number of downstream tasks.

### Strengths
- Interesting setup with both theoretical and empirical evaluation.
- Empirical evaluation is extensive, covering many downstream tasks and (pretraining / continual pretraining) settings.
- Token-level editing works well in practice for continual pretraining setting, and does not damage learning for pretraining and SFT settings.

### Weaknesses
 - Overall, although results with continual pretraining seem good, I would add way more nuance to results with pretraining and SFT. Differences in results obtained are very narrow and oftentimes the proposed method is numerically worse (by a very small margin).
- I find that some important points are not well addressed, for instance how did authors choose the p=0.99 as their threshold for resampling with token-level editing and what happens if one varies this threshold. This is especially important in light of the positive-to-mixed results (in the reviewer's opinion) obtained in the experiments.
- In Figure 1, you introduce a lot of notation that you do not explain neither in a legend nor in the caption, like $\sigma$, $d$, $T$, $f_0$, $m_1$, $y_1$, $m_0$, $y_0$, etc. Please introduce all these terms in the Figure caption (or in a legend in the figure itself). If that will make things too complicated, simplify the figure by removing the notation.
- In lines 89-92, you briefly describe iterative and non-iterative model collapse. I think this needs more clear language / more detail. What are the key differences between the two? Where are they similar? Why is one more realistic than the other and why? Please focus on that.
- One stark difference in Fig.2 you do not discuss is a bimodal distribution of ppl on human data. Or is that an artifact from the binning strategy you were using (if any)?
- Not sure I fully agree with the discussion around Fig.2 (lines 190-198). I find the plots for 1M human texts and 1M synthetic texts very similar. Why did you choose to use Figures to motivate your work instead of using more objective metrics, like those that measure the similarity between probability distributions?
- I do not think that a line plot is the best setting for Fig.5B, you would probably be better off with a bar plot here. The lines hint at the wrong intuition that they have meaning, whereas only the dots have meaning.
- Applying token-level editing by using top-k sampling with an LLM as the prior when p>0.99 means you discard the tokens where the LLM is too certain. One important question here is how did you choose this number of 0.99, and what would happen if this number were different? How do we generalise any findings (or can propose any future work) based on your results?
- In line 211, you may want to explain how the DSIR sampling works and why you use it in your data analysis.
- You may have written this somewhere, but what percentage of the original tokens are edited (on average per dataset) when you use token-level editing with p=0.99?

Typos worth mentioning:
- Line 211: "important sampling"

### Questions
- In Figure 1, you introduce a lot of notation that you do not explain neither in a legend nor in the caption, like $\sigma$, $d$, $T$, $f_0$, $m_1$, $y_1$, $m_0$, $y_0$, etc. Please introduce all these terms in the Figure caption (or in a legend in the figure itself). If that will make things too complicated, simplify the figure by removing the notation.
- In lines 89-92, you briefly describe iterative and non-iterative model collapse. I think this needs more clear language / more detail. What are the key differences between the two? Where are they similar? Why is one more realistic than the other and why? Please focus on that.
- One stark difference in Fig.2 you do not discuss is a bimodal distribution of ppl on human data. Or is that an artifact from the binning strategy you were using (if any)?
- Not sure I fully agree with the discussion around Fig.2 (lines 190-198). I find the plots for 1M human texts and 1M synthetic texts very similar. Why did you choose to use Figures to motivate your work instead of using more objective metrics, like those that measure the similarity between probability distributions?
- I do not think that a line plot is the best setting for Fig.5B, you would probably be better off with a bar plot here. The lines hint at the wrong intuition that they have meaning, whereas only the dots have meaning.
- Applying token-level editing by using top-k sampling with an LLM as the prior when p>0.99 means you discard the tokens where the LLM is too certain. One important question here is how did you choose this number of 0.99, and what would happen if this number were different? How do we generalise any findings (or can propose any future work) based on your results?
- In line 211, you may want to explain how the DSIR sampling works and why you use it in your data analysis.
- You may have written this somewhere, but what percentage of the original tokens are edited (on average per dataset) when you use token-level editing with p=0.99?

Typos worth mentioning:
- Line 211: "important sampling"

### Soundness
3

### Presentation
2

### Contribution
2
