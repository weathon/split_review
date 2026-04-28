# Self-Boosting Large Language Models with  Synthetic Preference Data

- Decision: Accept
- Avg Score: 6.60
- Scores: 5, 8, 8, 6, 6

## Abstract
Through alignment with human preferences, Large Language Models (LLMs) have advanced significantly in generating honest, harmless, and helpful responses. However, collecting high-quality preference data is a resource-intensive and creativity-demanding process, especially for the continual improvement of LLMs. We introduce SynPO, a self-boosting paradigm that leverages synthetic preference data for model alignment. SynPO employs an iterative mechanism wherein a self-prompt generator creates diverse prompts, and a response improver refines model responses progressively. This approach trains LLMs to autonomously learn the generative rewards for their own outputs and  eliminates the need for large-scale annotation of prompts and human preferences. After four SynPO iterations, Llama3-8B and Mistral-7B show significant enhancements in instruction-following abilities, achieving over 22.1% win rate improvements on AlpacaEval 2.0 and ArenaHard. Simultaneously, SynPO improves the general performance of LLMs on various tasks, validated by a 3.2 to 5.0 average score increase on the well-recognized Open LLM leaderboard.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents "SynPO", which trains a self-prompt generator by controlling the keywords used. Noises (extracted also from responses) are inserted to produce the "bad" responses so that a SFT setup is possible where good and bad responses are now available. A separate step involves a response regenerator that is used to refine the model responses to get the good responses. 
The diversity comes from the selection of keywords, which can be sampled from a large pretraining set like RefinedWeb, and the model improves by learning to discern bad and good responses iteratively.

### Strengths
The strength of the paper is that it offers a sound solution in terms of introducing diversity in the self-improvement process. While this is not exactly novel, but I do see a world where this works and improves model progressively. Moreover, use of keyword means that it provides a transparency in what we can control, the granularity of control, and ease of analysis.

### Weaknesses
The weaknesses are the following:
1) I'm not sure if this is completely "self-boosting" as the title claimed, since external knowledge is needed, and careful selection of the keyword might be needed to guide the LLM to learn properly. 
2) I think the paper does not provide much insights into the types of noise (keywords) that are more effective, which seems rather important as an insights in creating the bad samples. 
3) The method relies heavily on the model's ability to generate out from a prompt containing keyword, it might or might not work with less capable LLMs. 
4) The writing is rather unclear, I think it could have been written in a much more understandable manner.

### Questions
Do you have any insights on what kind of noise keywords are bad? What exactly does it make one keyword more noisy than another?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper illustrates a synthetic data generation pipeline, SynPO, for self-generating preference data to align the model. The pipeline consists of (a) self-generating diverse prompts at scale and (b) self-generating paired responses for these prompts. The paired responses are constructed by (i) first sampling generations from the base model, (ii) training a response improver model to synthetically generate the preferred response, and (iii) pairing the preferred response with the base model response to create paired preference data. The method relies only on initial high-quality seed SFT data, and all the remaining data is synthetic. Applying the SynPO method for multiple iterations results in significant alignment performance gains.

### Strengths
- Each component of the SynPO pipeline is intuitive and contributes to the final model performance
- Strong and extensive empirical results, including data analysis (Figure 4, 5) and extensive ablation experiments. 
- Creative uses of the seed SFT data for multiple components of the pipeline.
- Very well written and structured.

### Weaknesses
 - Has the synthetic preference data been tested for benchmark data leakage? I didn't see anything suggesting that checks for data leakage were done.
- While there's novelty to the pipeline as a whole, the individual components of the pipeline have been known. 

There are a few typos as well:
- L193: "an infinite" -> "a huge" (clearly what is being described is not "infinite") 
- L247: \sigma -> \beta. Also, state what is \sigma? I assume it's the sigmoid function. 
- L314: "involve" -> "compare against"
- L316: "involves" -> "use"

### Questions
Data filtering:
- For preference data, why is the rejected response across iterations the one generated by the base model? Why are the model(s) from the previous iteration(s) not used for generating rejected responses? 
- Given that the "chosen response" quality keeps improving in the preference data since the rejected response is from the base model, do the number of filtered-out preference pair data, as stated on L230, come down across iterations?

Results:
- I don't understand the performance gains on TruthfulQA. Any reason for/pattern to these gains?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a framework called SynPO that leverages synthetic preference data for human alignment. The framework starts with the training of a self-prompt generator to create large-scale synthetic prompts. This prompt-generator is trained from the LLM itself, starting from some initial SFT data, and can generate prompts based on keywords. In an iterative process, these prompts are then given to the model to be trained, and passed through a response improver, which is retrained each round to reduce the gap between policy model outputs and gold standard responses. The authors perform experiments with Mistral-Base 7B and Llama3-8B, starting from versions that have undergone SFT supervision on a chat-dataset. They show improvements on three alignment benchmarks: MT-Bench, Arena Hard and AlpacaEval 2.0. They also show an overall improvement on standard benchmarks including Arc, HellaSwag, TQA and MMLU.

### Strengths
The paper does quite extensive experimentation, investigate the diversity of the prompts and do ablations to understand the impact of various parts of their pipeline. The topic will be well-received I believe given the recent attention for alignment and the cost of generating human preference data.

### Weaknesses
In the introduction, it is not entirely clear to me what model is what. E.g. it is mentioned that a self-prompt generator is trained to create synthetic prompts, and after that it is mentioned that model-generated responses are used as rejected candidates and a response improver is used to improve the response. It is also mentioned that a small amount of SFT data is used to steer the generation of synthetic preference data. But what is what? Which model is used with the synthetic preference data? What is the "response"? Is that coming from the self-prompt generator? Are the self-prompt generator and the response improver the same model? Some of this is cleared up later, but the reader does not know that while trying to comprehend that initial paragraph.

Small point: I don't think it is entirely accurate to write that you use Mistral-base and Llama 3 base model, because those models did not undergo SFT. The models stem from these models (as does the Llama 3 8B instruct model), but they are not those base models.

Lastly, I am a bit confused about the improvement on the standard benchmarks. Many of these benchmarks are things learned in pretraining (e.g. knowledge). The fact that some of these scores go up, especially on knowledge benchmarks, is a bit suspicious because knowledge is something that can evidently not be learned from just self-improvement loops. It makes me wonder if the improvement is just due to the input coming from GPT-4. I would ask if you considered a basilen where you do not update the policy model in between, but just do multiple rounds trying to squeeze out more of the GPT generated data without doing iterations with the model itself, or just do more SFT with the initial data, but I think that those are the ablations presented in 4.2 and the difference seems quite large.

### Questions
The fact that some of these scores go up, especially on knowledge benchmarks, is a bit suspicious because knowledge is something that can evidently not be learned from just self-improvement loops. It makes me wonder to what extent the improvement is just coming from the GPT-4 data. Your experiments in 4.2 seem to refute that idea (though you don't look at the benchmarks there I believe), leaving me a bit puzzled. Do you have any other explanation for why the model would improve on something it shouldn't improve on?

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
4

### Summary
The paper introduces SynPO, a self-boosting framework that improves LLMs using synthetic preference data rather than human annotations. The key innovation is a two-part process: (1) A self-prompt generator creates diverse prompts using just three keywords, and (2) A response improver that refines model outputs. The refined outputs are used as "chosen" responses and the original outputs as "rejected" responses for preference learning. Testing on Llama3-8B and Mistral-7B shows significant improvements in instruction following (~22-30% win rate improvements on benchmarks) and general performance (3-5% increase on Open LLM leaderboard) after four iterations.

### Strengths
Novel and Practical Solution:
Addresses a critical challenge in LLM development - the scarcity of high-quality preference data
Provides a scalable way to generate training data without relying on human annotations
Simple but effective keyword-based prompt generation strategy

### Weaknesses
Limited Task Scope:
Primary evaluation focuses on instruction-following tasks with limited testing on complex reasoning tasks or specialized domains
Some tasks show performance degradation (e.g., Mistral's performance on GSM8K)


Unexplained Performance Gaps:
The dramatic improvement over SFT baseline (e.g., from 6.6% to 34.0% win rate) needs more analysis
Limited ablation studies on why the synthetic data works so much better

### Questions
See weaknesses

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce SynPO (Self-Boosting Preference Optimization), a framework that enables LLMs to autonomously generate synthetic data and enhance their performance through iterative self-boosting.  SynPO leverages a self-prompt generator and response improver to collaboratively produce high-quality synthetic preference data for training. This process allows the model to learn responses aligned with preferences, leading to performance improvements on benchmarks like the Open LLM Leaderboard, AlpacaEval 2.0, and Arena-Hard.

### Strengths
1. The authors contribute by demonstrating infinite generation potential through experiments that examine performance changes relative to the number of synthetic datasets. They also clarify the limitations by distinguishing this capacity from the sustained utility of such datasets over time.

2. The contribution to diversity within the keyword list is effectively demonstrated, with supporting experiments that validate this aspect.

3. Previous research has rarely considered multi-turn interactions; however, the authors establish the effectiveness of their proposed method under multi-turn dialogue conditions.

4. The self-boosting approach employed in the optimization process is appropriate and well-suited for enhancing model performance.

### Weaknesses
1. An ablation study on the effect of excluding noise keywords is necessary for Lines 156–157.

2. Analysis of the types of keywords is insufficient. The authors justify random sampling based on diversity, yet the study lacks analysis on which extraction forms might be more beneficial, or order affects outcomes.

3. It would be interesting to see experiments that vary the number of keywords or increase them significantly.

4. The most concerning issue is the weak validation of out-of-distribution data. Since the seed dataset reflects OpenAI GPT’s preferences, as do Alpaca 2.0 and Arena-Hard, this likely influences the performance shown in Table 2. Additionally, while Table 4 shows considerable improvement on TQA included in the UltraFeedback dataset, effects are minimal on other datasets, suggesting that SynPO does not fully resolve in-distribution bias issues. There are also doubts about whether this approach could be more efficient or effective than methods in other studies applying CoT rather than simple SFT.

### Questions
1. References are needed for studies on a word-to-text task [1] and similar augmentation research where word sets are extracted from sentences in existing datasets, combined to create new synthetic datasets, and enhanced in quality using contrastive learning [2].

    [1] *Lin, B. Y., Zhou, W., Shen, M., Zhou, P., Bhagavatula, C., Choi, Y., & Ren, X. (2020, November). CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning. In Findings of the Association for Computational Linguistics: EMNLP 2020 (pp. 1823-1840).*

    [2] *Seo, J., Moon, H., Lee, J., Eo, S., Park, C., & Lim, H. S. (2023, December). CHEF in the Language Kitchen: A Generative Data Augmentation Leveraging Korean Morpheme Ingredients. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (pp. 6014-6029).*

### Soundness
3

### Presentation
2

### Contribution
2
