# Towards Specialized Web Agents Using Production-Scale Workflow Data

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Large Language Model (LLM) agents are rapidly improving to handle increasingly complex web-based tasks. Most of these agents rely on general-purpose, proprietary models like GPT-4 and focus on designing better prompts to improve their planning abilities. However, general-purpose LLMs are not specifically trained to understand specialized web contexts such as HTML, and they often struggle with long-horizon planning. 
We explore an alternative approach that fine-tunes open-source LLMs using production-scale workflow data collected from over  250 domains
corresponding to 6 billion tokens. This simple yet effective approach shows substantial gains over prompting-based agents on existing benchmarks---\ouragent achieves state-of-the-art direct generation performance on Mind2Web and improves the task success rate by 7.3\% over the previous best text-only web agents  on WebArena.
We further perform detailed ablation studies on various fine-tuning design choices and provide  insights into LLM selection, training recipes, context window  optimization, and effect of dataset sizes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present an alternative approach that fine-tunes open-source LLMs using production-scale workflow data collected to develop specialized web agents. They show that they beat GPT4 on the Mind2Web benchmark with a smaller fine-tuned models on their proprietary dataset. They prepare a proprietary dataset which target is to predict the next step given the website’s DOM and action history. They propose an HTML preprocessing strategy that balances between preserving essential information and minimizing context length.

### Strengths
- An innovative approach for the problem of creating a web agent given a task
- Using a well-crafted production-scale dataset that contains information about the website's DOM, the action history with the next step as the target the authors show that they can finetune language models with about 7B parameters and outperform much bigger ones. This is done with a parameter efficient method (LoRA)
- They present a DOM preprocessing step with to get rid of useless information to make as much information fit in the LLM given its context length
- If the DOM is not fitting in the model, they chunk it sequentially
- They show that their dataset's training size has an effect on the accuracy

### Weaknesses
 - There isn't any type of memory component when it comes to DOM. I think that remembering the previous pages will help. But to include something like this it should probably be embedded as a representation due to limitations in the context length
- In table 1 where you show the performance of the fine-tuned LLMs, add another column to show the same model's performance without finetuning to see the performance gain of the fine-tuning. I see that you the performances of non fine-tuned models on your proprietary in table 4 which makes me wonder why you didn't also include in table 1. dataset baseline
- You assume that the non-useful attributes are the ones which have character to token ratio > 2. This may not always be the case and is highly dependent on the tokenizer and the type of attribute.

### Questions
- The performance in table1 is for the Mind2Web or WebArena? I don't see it mentioned somewhere
- "For performance robustness, we call WorkflowAgent five times and use majority vote to select the final answer". Do you use sampling when you generate the action? What is the reason behind it? Is following a self-consistency approach?
- Is there any reason to not approach this problem with a vision model? You would get rid of many difficulties like preprocessing or making sure the page fits in the model. It would be interesting to train this with a Vision model and actual screenshots of the pages instead of the HTML of the page and evaluate on public benchmarks like multi-modal mind2web. This would make it more flexible and you would not need to preprocess to remove redundant information. Also incorporate previous pages as a context as a form of “memory”

### Soundness
3

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
3

### Summary
This paper proposes WorkflowAgent, an LLM agent for autonomous web navigation tasks. The authors curate large-scale workflow data in real web environments and use LoRA to fine-tune open-source LLMs like Qwen2-7B-Instruct. The performance of WorkflowAgent is evaluated across three benchmarks, demonstrating generalization abilities and significant improvements, setting new SoTA. Moreover, the authors conduct detailed ablation studies and analyses to verify the effectiveness of the WorkflowAgent. In general, this paper fine-tunes an LLM with a newly curated large workflow dataset on web tasks, revealing the potential of fine-tuning smaller LLMs with large-scale data to outperform much larger LLMs.

### Strengths
1. The elaboration of dataset collection and preprocessing in Section 3.2.1-3.2.2 is well-written, clear, and detailed. This can inspire other data collection and processing work in future research.
2. In Section 3.2.4, the authors conduct preliminary experiments to evaluate the impact of model type, window length, and dataset size, well justifying the final settings in the main experiments.
3. Sufficient performance improvement on three different benchmarks show the strong capability and generalizability of the proposed WorkflowAgent.

### Weaknesses
1. Novelty. Assisting and automating web navigation tasks with LLMs is an interesting and important topic, and WorkflowAgent indeed shows impressive performance in Section 4’s experiments among text-only methods. However, this paper deploys conventional and common fine-tuning methods (LoRA) on a widely-used open-source LLM (Qwen2-7B-Instruct) for existing scenarios (LLMs for web tasks), making the paper less innovative. The core methodology lacks significant novelty, relying on standard techniques applied to a well-trodden problem space. The use of LoRA for fine-tuning, while effective, does not introduce any new algorithmic or architectural contributions.
2. Contribution. The large-scale workflow dataset in a real-world web environment plays a vital role in improving WorkflowAgent’s performance, which would have been a primary and important contribution, but it is proprietary and close-sourced due to privacy reasons. In addition, as noted in the footnote of the first page, only WorkflowAgent trained on public datasets will be released, and WorkflowAgent trained on datasets newly curated by authors does not seem to be released. I understand the privacy concerns, but neither the dataset nor the model is open-sourced, it significantly limits the contribution of this paper to the community and makes the experimental results unreproducible. If possible, I kindly ask the authors to consider open-sourcing desensitized datasets or open-sourcing models trained on the newly curated datasets that are used in the experiments for better reproducibility.
3. Motivation. Considering more and more recent studies in this field have utilized MLLMs rather than text-only LLMs to better capture visual information in web tasks, the motivation for choosing a text-only approach needs to be further clarified. The paper does not adequately justify the decision to use a text-only model, especially given the inherent visual nature of web navigation tasks. This raises concerns about the potential limitations of the approach in scenarios where visual context is crucial.
4. Baselines. Some more recent and stronger MLLM web agents also have text-only setting (e.g. WebVoyager_text-only[1]), and they can be compared with the proposed WorkflowAgent as stronger baselines.

### Questions
1. Section 3.2.2 tag attribute filtering: Why are attributes with a character-to-token ratio smaller than 2 considered not semantically meaningful and thus removed? Please elaborate on more details of the intuition here.
2. Would it be possible to open-source the desensitized dataset or only the models trained on the newly curated dataset used in the experiments for better reproducibility?
3. MLLMs can better capture visual information, which can be beneficial in web navigation. What is the motivation for choosing a text-only LLMs-based approach?

### Soundness
2

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
This paper fine-tunes an LLM with a 6B workflow dataset to play as a web agent. The fine-tuned agent improves performance on some web task benchmarks such as Mind2Web and WebArena, which is, to the best of my knowledge, the first of this kind. However, the author doesn't offer evidence to support their technical novelty, like the dataset used for training (I can understand the privacy concerns), models trained, and the episodes of the agent play, unlike a recent similar work which open-sources all materials to replicate their work: https://arxiv.org/abs/2410.13824. In addition, the agent's good overall performance on WebArena requires the massive intervention of LLMs (gpt4o) to translate the environment, plan, and self-evaluate, so I don't see any points in training a cheaper web LLM but requires more general LLMs as a multi-agent system to perform well.

### Strengths
The paper is well written. The web task adaptation of the LLM is novel and seems to be effective, according to their reported figures. The entire pipeline is complete with model comparison, ablation study, and dataset scaling law. The results of the Mind2Web seem promising as the model improves overall performance without adapted training for the dataset.

### Weaknesses
I would question the validity of the results. I check your supplementary materials and find the Mind2Web results are missing. The WebArena results are significantly not complete and hard to interpret. I can understand the privacy concerns, so you can not release the datasets, but what about the data collection platform you mentioned in the paper? I don't think the slim "preprocessing.py" code could support that.

In addition, for the real grounding of the web agent, the end-to-end WebArena's evaluation could more faithfully represent the web interaction capability of your agent than Mind2Web. The results are good from your table, but why does your approach intensively require the integration of LLMs like gpt4o? If the agent requires gpt4o to translate the markup language, to plan, and to evaluate so that you can have a better overall performance, then why does your point of "less inference cost" make sense? Isn't this system a combination of many previous techniques?

What if the observation chunk you feed into the model happens to exclude the required web elements for the task ("for evaluation, we use the last chunk since the target’s location is not known beforehand.")? When I mentioned "unreasonable and unrealistic," I would like to emphasize that the agent's performance should not rely on chance introduced by the system.

Mind2Web may not be a suitable benchmark for testing the agent's generalizability as it's a fixed environment using the "exact match" as the metric. There are web benchmarks defined on the real-world web that evaluate agents by end-to-end play, such as WebVoyager. How well does your agent perform there?

How did you construct the ablation study control group? It's weird that the four-staged gpt-4o multi-agent in your experiment setting (34.2%) performs worse than several LLM-based agents on the WebArena leaderboard. It's easy to control the agent to perform worse.

It seems you have defined a system specifically for improving the success rate on the WebArena benchmark, as typically we would expect the llm agent to help correct the typo in the intent. I have the same question as above, that is, how well does your agent generalize to other web tasks/benchmarks if you keep everything the same as you use the agent for WebArena?

### Questions
- What is the workflow documentation platform you mention in 3.2.1?
- How did you get the action description? From human annotators?
- You seem to have excluded the scroll mouse operation. Why do you have the scroll action in your incomplete WebArena episodes?
- How large is the training dataset? 6B but how many episodes?
- You mention the accessibility tree cannot show whether the element is interactive, but from the WebArena environment using that representation,  it seems to include such information.
- Is your model trained to generate the natural language action description? If not, how could the action description be kept consistent when the agent is implemented?
- The chunk of the observation is unreasonable and unrealistic.
- Exact match is not a good metric to measure the performance of a web LLM. It can only reflect whether the model remembers the dataset patterns well.
- The intensive integration of gpt4o into WebArena task completion is insane. I would call this a multi-agent workflow where only a small portion is replaced with a cheap smaller model.
- Ablation study should be reframed to emphasize how your model contributes to the overall success.
- (Optional) Did you change the interaction script of the WebArena environment? Or otherwise, how could it be possible that you gain 51.9% on the map task without effective combobox selection? And a 70.2% on the Reddit task if the keyword matching in the evaluator is super strict?

### Soundness
2

### Presentation
3

### Contribution
1
