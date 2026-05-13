# BRIDGE: Bootstrapping Text to Guide Time-Series Generation via Multi-Agent Iterative Optimisation and Diffusion Modelling

- Decision: Reject
- Scores: 6, 8, 1, 3, 8

## Abstract
Time-series Generation (TSG) is an impactful research direction, as generating realistic sequences can be used to create educational materials, in simulations and for counterfactual analysis in decision making. It has further the potential to alleviate the resource bottleneck that arises from a lack of diverse time-series data required to train large time-series foundational models. However, most existing TSG models are typically designed to generate data from a specified domain, which is due to the large divergence in patterns between different real-world TS domains. In this paper, we argue that text can provide semantic information (including cross-domain background knowledge and instance temporal patterns) to improve the generalisation of TSG. To do so, we introduce ``Text Guided Time Series Generation'' (TG$^2$)---the task of generating realistic time series from handful of example time series paired with their textual description. We further present a Self-Refine-based Multi-Agent LLM framework to synthesise a realistic benchmark for TG$^2$ and show that the collected text descriptions are both realistic and useful for time-series generation.  We develop a first strong baseline for the TG$^2$, Bridge, which utilises LLMs and diffusion models to generate time series which encode semantic information as cross-domain condition. Our experimental results demonstrate that Bridge significantly outperforms existing time-series generation baselines on 10 out of 12 datasets, resulting in data distributions that are more closely aligned to target domains. Using the generated data for training positively impacts the performance of time series forecasting models, effectively addressing training data limitations. This work bridges the gap between LLMs and time series analysis, introducing natural language to help the time series generation and its applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work investigates the effects of supplementing time-series encoding with textual information for time-series generation. In doing so, the authors create a multi-agent LLM-based method to generate a benchmark dataset. To evaluate the quality of the synthetic data, this work compares models trained on real and their synthetic data. This work also describes a text conditioned diffusion model to generate new time series.

### Strengths
Overall I find this work to be exciting and interesting. The use of a multi-agent LLM method to generate a benchmark is both a timely and resourceful solution. Moreover, textual conditioning allows for more diverse and nuanced means to condition time-series generation; a valuable contribution to the field.

### Weaknesses
# Writing
While I am fairly positive and supportive of this work, it is ultimately difficult to recommend publication in it's current state. This is almost entirely due to the way the paper is written. After reading paragraphs multiple times and already being familiar with this topic I felt that I did not have the level of understanding I would like to given the time I put into reading this. I believe this will significantly limit the impact of this work. I recognize the difficulty the authors face in describing multiple components (multi-agent LLM method and diffusion-based time-series generation), where each component itself has many details. However, in this situation I believe the authors need to do a better job illustrating their method using figures, specific language/terms, removing jargon, and potentially streamlining some details or moving them to the appendix.

I believe this work can benefit most from a better interaction between the text and the figures. In it's current state, I believe this manuscript does not fully utilize the figures. I would like to see a subfigure/box/illustration for each key component which is referenced in the text. This way a reader can follow along visually and via the text. This is very helpful because there are a lot of moving parts in this paper and it is easy to forget the relationship between these parts. In a well made figure that is integrated into the text, the reader can look at the figure to remind themselves how each component fits into the overall scheme. Practically, it would be good if the authors refer to a figure in every or everyother sentence in sections 3 and 4.

- There is a lot of terms and jargon that I believe could be better defined or removed. Figures will also help with this.
- The abstract says this work outperform on 10 out of 12 datasets, but the introduction states 11 out of 12.
- Please run this work through a spell/grammer check, I found misspelled words and missing punctuation.

# Results
Figure 3 is both very hard to read and poorly made. Both of these lead to a convoluted message and potentially erroneous interpretations. For example, to me it looks like the in (2) the trend stays the same, but the diffusion model only introduces extra noise that varies with conditioning. However, this is not the entirely correct interpretation.
- Increase font size of the axis
- merge the x axes in each column
- All plots in each column need to have the same y range
- Fill the white space to the left and right

From this Figure 3, it seems that generated time series are much noisier. I would like to see how the overall variance of the datasets compare from original, without conditioning, and with conditioning, along with some (possibly brief) discussion.

### Questions
1) In what ways do the LLM prompts succeed and fail?
2) In what ways do the text succeed and fail to describe the time series (e.g. sinusoidal, trending upward, extreme values, ...)?

### Soundness
3

### Presentation
1

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
- This paper aims to overcome the challenge of non-availability of diverse time-series data required to train large time-series foundational models which has potentially limited the widespread usage of LLMs for downstream time series tasks compared to NLP domain. To this aim, the authors proposed the use of text to guide the process of synthetic time series generation while further proposing a Self-refining multi agent LLM framework to optimise those textual descriptions. They make use of semantic prototypes for conditioning the time series generation step using the diffusion model. This helps in generation of time series representative of diverse domains.

### Strengths
* The paper addresses an important research question that is required in extending the use of LLMs to the domain of times series which make it a significant contribution.
* The novelty is highlighted through the innovative use of text to guide time series generation.
* The paper is well-written making it easier for the reader to comprehend.

### Weaknesses
 - There are a number of typos including grammatical errors in the paper (For ref lines 84, 85, 102, 226, 256, 328, 422..)
- In the results section, I don’t find an explanation as to why using BRIDGE w/o text is the second best performing model. Eliminating text component from your framework removes the novelty. What makes Bridge better than other baselines even when no text is provided?

### Questions
- There is no mention of the number of runs over which the results have been averaged. Are the numbers in the results table fairly stable across runs? What is the standard deviation across different runs?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
To summarize, the paper mainly does three things:
1. Introduce a new task, TG^2 ("Text-Guided Time Series Generation"), which is to generate realistic time series in an in-context learning style, aided by text descriptions of what's going on (i.e. you input into the model a handful of time series, with text descriptions of what happens in the time series, and then the model outputs newly synthesized time series in that style)
2. They introduce a synthetic dataset for this task (i.e. they generate a bunch of text labels for classic time series benchmarks). They generate these synthetic text descriptions by using multi-agent LLM framework that they propose.
3. They develop a baseline ("BRIDGE") for the TG^2 task, and evaluate it on this synthetic benchmark, and show that on average it outperforms other baselines.

### Strengths
1. I thought that section 4.2, on "Semantic Prototyping", was very clear and well-motivated. "Encoding knowledge from different perspectives and... associating features with time series" sounds like a very well-motivated way of solving this problem. 
2. I think that in-context learning to generate new time series from observed time series is a timely and important problem. And the intention of using text-descriptions to aid that process is very well-motivated.
3. The related work section was very thorough. I appreciated how they split "TS-for-LLM" and "LLM-for-TS"

### Weaknesses
I wasn't fully convinced by the paper's motivation; I felt that some of it was misleading. For example, the introduction states: _"The LLM-for TS approach seeks a more fundamental solution by pre-training models on time series data, as exemplified by TimesFM (Das et al., 2023) and Chronos (Ansari et al., 2024). While showing promising results, these methods demand substantial computing resources and large datasets. The limited availability of time series data compared to NLP and CV domains poses a significant challenge in developing models with emergent abilities similar to traditional LLMs, making it difficult to consistently meet the data requirements for such approaches. We argue that using text to assist in cross-domain TS generation can help overcome the data scarcity issues inherent to the TS domain."_ The authors made a similar claim again in the related work section: _"Chronos, on the other hand, takes advantage of the achievements in NLP by converting time series data into discrete tokens and pretraining the time series model using cross-entropy loss instead of MSE, achieving SOTA performance on multiple datasets (Ansari et al., 2024). However, these methods rely on large scale computing resources to scale them and construct large datasets. It is unrealistic to assume that such requirement can always be met"._ I found this misleading for a few reasons:

1. It is standard practice to highlight strengths and shortcomings of past work, but in this case, the comparison to the Chronos paper seems dishonest, because it positions the BRIDGE paper as one that overcomes these issues, when in reality, the BRIDGE method seems even more resource hungry based on the detailes provided in the paper. The Chronos models were each trained on an 8xA100 GPU, where each GPU has 40gb and their base model trains in 17 hours with this setup (see their appendix). In contrast, the present paper conducted their experiments on up to 8 H100/A100 80GB GPUs, and don't say how long it took. **This implies that BRIDGE training requires GPUs that are at least twice as big as Chronos' requirements.** Furthermore, given that LLM-style training (as in Chronos) is very optimized, and Diffusion-style training (as in BRIDGE) is very time consuming, it seems like this is actually a way in which the BRIDGE paper is slower and requires more computing resources?
2. One of the main contributions of the Chronos paper was to introduce a 100% synthetic dataset, using Gaussian processes. They find that that augmenting with this dataset helps alleviate the data scarcity issue considerably. Additionally, their "TSMixup" procedure alleviates data scarcity issues by training on randomly weighted sums of their ground truth data, which they find improves generalizability significantly. Did the authors of the BRIDGE paper consider either of these strategies, or things similar to them, from the Chronos paper? In section 5, the authors say ask _"Can synthetic data be used to help improve the performance of TS task?"_. This would have been a good place to consider such an experiment.

There are a few points in the paper where a lack of attention to detail gives me low confident that the paper's details are accurate. Proofreading work before submitting it, ensuring consistency, etc, is very important. For example:
1. In the abstract, it says _"Our experimental results demonstrate that BRIDGE significantly outperforms existing time-series generation baselines on 10 out of 12 datasets"_ and in the intro it says that _"The proposed method outperforms all baselines on 11 out of 12 datasets"_

### Questions
1. Can the authors please clarify the point about resource utilization in the "weaknesses" section?
2. (Looking at Definition 1...) Would it be accurate to describe the TG^2 task paradigm as approximating the data distribution without providing an explicit class label? And then would it be accurate to describe the BRIDGE method as automatically extracting an "implicit" representation for a class label (in the form of the weighted sum of the orthonormal basis, as described in Section 4)?
3. (Looking at Section 3.2...) how do we know that, when the LLM agent interacts with an external environment (e.g. Wikipedia/Google), and retrieves information for the text description, that there isn't any data leakage happening? If I understand correctly, these are all common datasets, so looking up information about them on the internet can possible give information about the test splits that the model isn't supposed to see during the in-context learning process...

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a large language model (LLM)-based multi-agent framework to generate textual descriptions that augment time series data in a self-refining manner. Which may help the transfer of knowledge across domains and benefit low-resource time series domains. The authors introduce a benchmark for text-guided time series generation (TG2) and present a novel conditional diffusion model, BRIDGE. This model leverages sparsely activated prototypes as an alternative to direct text conditions. Experimental results demonstrate that the proposed method outperforms baselines in both text generation and forecasting, validating the effectiveness of BRIDGE within the TG2 framework.

### Strengths
1. Generating time series through text descriptions to leverage cross-domain knowledge transferring from LLMs for under-resourced time series domains is promising. Bridging the gap between times series and language which may depict underlying causalities is a valuable domain.
2. The use of text to indirectly introduce pre-trained knowledge into a diffusion model specifically trained for time series rather than relying solely on LLMs is a good idea.
3. The authors performed experiments in datasets across different domains as well as unseen domains which show the potential of the proposed methods in cross-domain time-series generation.

### Weaknesses
## Missing details 

There are important details are missing in the paper, and some parts of the paper are not self-contained:
 * **Detailed Agent Design:** Key details about the agent design are omitted. A breakdown of prompt strategies, inter-agent interaction protocols, and the function of each agent role within intra- and inter-group discussions would be important given that agent design is a crucial component of this paper. There is also no discussion or justifications about those design choices.
* **Diffusion Model Specifics:** The paper lacks explicit detail on critical hyperparameters, model architecture, and the training process for the diffusion model. Algorithm 1 provides an overview, yet it is insufficiently mapped to Section 4, for example, epsilon is not defined explicitly, leading to an incomplete picture.
* **Prototype Analysis:** The paper introduces prototypes as a central innovation of BRIDGE which distinguishes the proposed method from vanilla conditional diffusion models, but the analysis remains limited. Please read the questions for details.

## Experiment design 
Certain experimental designs weaken the overall findings:
 * **Section 6.1**, the usefulness of text is analyzed over the description generation stage (i.e., whether the description can be used to better reconstruct the time series) instead of the actual time series generation which is the real focus of interest of the proposed method.
 * **Section 6.2**, there is no comparison to diffusion model baselines which raises questions regarding fairness and completeness, especially given the observation that `Bridge w/o Text` seems to be essentially a vanilla unconditional diffusion model, but can already outperform most baselines.
 * **Section 6.3**, the models are pre-trained, which introduces confounding factors from the pretraining knowledge, and makes it hard to evaluate the effect of the dataset. 
 * **Section 6.4** lacks ablation on the prototypes themselves (e.g., comparing prototype vs. direct text embedding usage), making it unknown about the benefits of using prototypes.

## Code and Data Availability

I cannot find any code or data provided in the paper or the open review page. The lack of code or data sharing, given that a benchmark (TG2) is presented as a primary contribution, is problematic.

### Questions
## Major questions & suggestions
1. Where do the initial text descriptions come from? Generated by LLMs? What is the “query” in Fig 5? Only the time series? Or some initial background? If so, where do those backgrounds come from? 
2. How could text provide information for generating high-frequency components, given the often ambiguous nature of text descriptions? Does text contribute meaningfully to these components? A spectral analysis could reveal how text features influence generation quality.
3. Figure 3 shows representative examples to illustrate the effect of text conditions, however, analysis on a few samples is inadequate to draw any conclusion, and introducing some statistical analysis on the samples in different cases can largely increase the creditability of the observed patterns. 
4. Could the authors elaborate on why a small set of bases is preferable to word embeddings directly? An experiment comparing the two approaches would be informative. How do these bases adequately conclude and represent the vast variability in time series patterns?
5. It is interesting that the bases are activated sparsely. It would also be helpful to visualize or analyze the pattern of how the bases are activated and whether each basis aligns with some specific time series patterns.

## Minor
1. What kind of context (e.g., the topic, content, background of time series) is provided for the agents to perform a search for the given time series in Section 3.2 Step 1?
2. Section 3.2, Step 2: “On the other hand, we also allow the agents to propose more appropriate evaluation metrics”, it is not elaborated anywhere

## Typos
1. **Table 4:** “Best results are highlighted in bold face” should read “underlined.”
2. **Table 5:** Replace “We experiment with the number of 4, 8, 10 separately” with “4, 8, 16” to match table values.
3. **Formula 2:** Should be c_z, not cz
4. **Tables 7 & 8:** The table is not colored as described in the caption.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a new method for generating high quality time-series from text descriptions. They first propose a multi-agent setup for refining text descriptions of time-series. They also propose a new diffusion-based method for generating time-series data. They test which components of textual descriptions have the greatest impact on performance, the quality of the generated time-series (with and without text) and the performance of models trained on synthesized data compared to real data.

### Strengths
Overall, I think this is a strong paper and tackles a new and emerging issue in time-series analysis, which is building high quality datasets, particularly with text components. 
1. They propose both a new time-series text refinement approach and a time-series generation method. I think having both of those components improves the strength of the paper dramatically. 
2. They propose a multi-agent approach for text refinement which appears to significantly improve the quality of the text descriptions
3. Multi-agent dataset generation seems to be relatively understudied within the time-series domain.
4. Their diffusion based time-series approach generates high quality time-series data with diverse properties and is useful for training models.
5. They also test which components of the text descriptions are impacting performance which I thought was very interesting, and they test their generated time-series quality in terms of both pure generation quality and for model training purposes.

### Weaknesses
1. No code provided
2. No data exampled provided. Particularly I would like to see more examples of refined text paired with time-series. This would also make it easier to understand the overall quality of the text and time-series generation.
3. It is difficult to disentangle which parts of the agent architecture contribute to the improved text descriptions.

### Questions
1. Are you going to release the code for this project?
2. The authors highlight the usefulness of the data, particularly for combined text and time-series descriptions. Why not make and release a collection of these? It would also improve the impact fullness of this work.
3. How would removing parts of the agent architecture impact performance? What about different text models?

### Soundness
3

### Presentation
4

### Contribution
3
